"""Dated, reproducible snapshot of Roblox's public charts (Python 3.10, standard library only).

Usage:
    python tools/snapshot.py                 # snapshot dated today (UTC)
    python tools/snapshot.py --date 2026-11-25 --deep 600 --delay 0.25

What it does (all unauthenticated, read-only GET requests to public Roblox web endpoints):
  1. Charts: explore-api get-sorts (every page) for each device x country combination, then
     get-sort-content for every Games sort (following nextPageToken when one is returned).
  2. Universe details (games.roblox.com/v1/games) and votes (games.roblox.com/v1/games/votes)
     for every distinct universe seen in any chart.
  3. For the "deep" set (top N by concurrent players, plus every game in any Top Earning list):
     game passes, badges (capped) and developer products (capped).
  4. Tidy CSVs in data/: charts.csv, games.csv, passes.csv, badges.csv, products.csv.

Raw responses are cached, gzip-compressed, under data/raw/<date>/ so a re-run with the same
--date never refetches. Delete a file there to force a refetch of that one response.
No login, cookie or API key is used or needed. Fetched text is stored as data only.
"""

import argparse
import csv
import datetime as dt
import gzip
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
UA = "Mozilla/5.0 (compatible; roblox-design-handbook-snapshot/1.0; public read-only research)"

# Device option ids come from the "device_filter_v1" filter returned by get-sorts itself.
# ("phone"/"tablet" are not valid ids: the API silently falls back to "computer".)
DEVICES = ["computer", "high_end_phone", "low_end_phone", "high_end_tablet",
           "low_end_tablet", "console", "vr"]
COUNTRIES = ["all", "us"]

BADGE_CAP = 300      # badges per game (3 pages of 100)
PRODUCT_CAP = 300    # developer products per game
PASS_PAGE_CAP = 5    # pages of 100 game passes

# Universes fetched in full even when they are not in any chart on the day (case studies).
# 10764627709 = Huss Valley, 10765012427 = Build the Pyramid! (both 2026 releases).
WATCHLIST = [10764627709, 10765012427]

STATS = {"net": 0, "cache": 0, "err": 0, "429": 0}


class Fetcher:
    def __init__(self, raw_dir, delay):
        self.raw_dir = raw_dir
        self.delay = delay
        self.last = 0.0

    def path(self, key):
        safe = re.sub(r"[^A-Za-z0-9_.\-/]", "_", key)
        return os.path.join(self.raw_dir, *safe.split("/")) + ".json.gz"

    def get(self, url, key):
        """Return parsed JSON, or None on a permanent error. Results (and errors) are cached."""
        p = self.path(key)
        if os.path.exists(p):
            STATS["cache"] += 1
            with gzip.open(p, "rt", encoding="utf-8") as f:
                rec = json.load(f)
            return None if "_error" in rec else rec["body"]
        backoff = 2.0
        for attempt in range(7):
            wait = self.delay - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            status, body = None, None
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    status, body = r.status, r.read().decode("utf-8", "replace")
            except urllib.error.HTTPError as e:
                status = e.code
                try:
                    body = e.read().decode("utf-8", "replace")[:2000]
                except Exception:
                    body = ""
                if e.code == 429 or e.code >= 500:
                    if e.code == 429:
                        STATS["429"] += 1
                    ra = e.headers.get("Retry-After") if e.headers else None
                    sleep = float(ra) if ra and ra.isdigit() else backoff
                    sys.stderr.write("  HTTP %s, backing off %.0fs: %s\n" % (e.code, sleep, url))
                    time.sleep(min(sleep, 120))
                    backoff *= 2
                    continue
            except Exception as e:  # network hiccup
                sys.stderr.write("  network error %s, retrying: %s\n" % (e, url))
                time.sleep(backoff)
                backoff *= 2
                continue
            STATS["net"] += 1
            os.makedirs(os.path.dirname(p), exist_ok=True)
            fetched = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
            if status == 200:
                try:
                    parsed = json.loads(body)
                except ValueError:
                    parsed = None
                if parsed is not None:
                    with gzip.open(p, "wt", encoding="utf-8") as f:
                        json.dump({"url": url, "fetched_utc": fetched, "status": 200, "body": parsed}, f,
                                  ensure_ascii=False, separators=(",", ":"))
                    return parsed
            STATS["err"] += 1
            with gzip.open(p, "wt", encoding="utf-8") as f:
                json.dump({"url": url, "fetched_utc": fetched, "status": status, "_error": (body or "")[:500]}, f)
            return None
        STATS["err"] += 1
        return None


def write_csv(name, header, rows):
    path = os.path.join(DATA, name)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(h, "") for h in header])
    print("wrote %s (%d rows)" % (path, len(rows)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--deep", type=int, default=600, help="games (by concurrent players) to fetch passes/badges/products for")
    ap.add_argument("--delay", type=float, default=0.25, help="seconds between network calls")
    ap.add_argument("--extra", default="", help="comma list of extra universe ids to fetch in full")
    a = ap.parse_args()
    date = a.date
    raw = os.path.join(DATA, "raw", date)
    os.makedirs(raw, exist_ok=True)
    F = Fetcher(raw, a.delay)
    sess = str(uuid.uuid5(uuid.NAMESPACE_URL, "roblox-snapshot-" + date))  # stable per date

    # ---------------- 1. charts ----------------
    chart_rows = []
    sort_names = {}
    for country in COUNTRIES:
        for dev in DEVICES:
            tag = "%s_%s" % (dev, country)
            tok, page, sorts = None, 0, []
            while True:
                page += 1
                u = ("https://apis.roblox.com/explore-api/v1/get-sorts?sessionId=%s&device=%s&country=%s"
                     % (sess, dev, country))
                if tok:
                    u += "&sortsPageToken=" + urllib.parse.quote(tok)
                d = F.get(u, "charts/sorts_%s_p%d" % (tag, page))
                if not d:
                    break
                sorts.extend(d.get("sorts") or [])
                tok = d.get("nextSortsPageToken")
                if not tok or page > 20:
                    break
            print("charts %-20s %d sorts" % (tag, len(sorts)))
            for s in sorts:
                if s.get("contentType") != "Games":
                    continue
                sid = s.get("sortId")
                sort_names[sid] = s.get("sortDisplayName") or sid
                games, ptok, p2, applied = [], None, 0, s.get("appliedFilters") or ""
                while True:
                    p2 += 1
                    u = ("https://apis.roblox.com/explore-api/v1/get-sort-content?sessionId=%s&sortId=%s&device=%s&country=%s"
                         % (sess, urllib.parse.quote(sid), dev, country))
                    if ptok:
                        u += "&pageToken=" + urllib.parse.quote(ptok)
                    c = F.get(u, "charts/content_%s_%s_p%d" % (sid, tag, p2))
                    if not c:
                        break
                    games.extend(c.get("games") or [])
                    applied = c.get("appliedFilters") or applied
                    ptok = c.get("nextPageToken")
                    if not ptok or p2 >= 10:
                        break
                if not games:  # fall back to the games embedded in get-sorts
                    games = s.get("games") or []
                for i, g in enumerate(games, 1):
                    chart_rows.append({
                        "snapshot_date": date, "device": dev, "country": country, "sort_id": sid,
                        "sort_name": sort_names[sid], "applied_filters": applied, "rank": i,
                        "universe_id": g.get("universeId"), "root_place_id": g.get("rootPlaceId"),
                        "name": g.get("name"), "player_count": g.get("playerCount"),
                        "up_votes": g.get("totalUpVotes"), "down_votes": g.get("totalDownVotes"),
                        "genre_l1": g.get("genreL1"), "is_sponsored": g.get("isSponsored"),
                        "content_maturity": g.get("contentMaturity"), "minimum_age": g.get("minimumAge"),
                        "age_recommendation": g.get("ageRecommendationDisplayName"),
                    })
    write_csv("charts.csv", ["snapshot_date", "device", "country", "sort_id", "sort_name", "applied_filters",
                             "rank", "universe_id", "root_place_id", "name", "player_count", "up_votes",
                             "down_votes", "genre_l1", "is_sponsored", "content_maturity", "minimum_age",
                             "age_recommendation"], chart_rows)

    # ---------------- 2. details + votes ----------------
    chart_info = {}
    for r in chart_rows:
        uid = r["universe_id"]
        if not uid:
            continue
        ci = chart_info.setdefault(uid, {"sorts": set(), "best_rank": 10**6, "earning_best": None,
                                         "maturity": r["content_maturity"], "min_age": r["minimum_age"],
                                         "age_rec": r["age_recommendation"]})
        ci["sorts"].add(r["sort_id"])
        ci["best_rank"] = min(ci["best_rank"], r["rank"])
        if r["sort_id"] == "top-earning":
            ci["earning_best"] = r["rank"] if ci["earning_best"] is None else min(ci["earning_best"], r["rank"])
    print("distinct universes in charts:", len(chart_info))
    for w in WATCHLIST + [int(x) for x in a.extra.split(",") if x.strip()]:
        chart_info.setdefault(w, {"sorts": set(), "best_rank": "", "earning_best": None,
                                  "maturity": "", "min_age": "", "age_rec": "", "watch": True})
    uids = sorted(chart_info)
    details, votes = {}, {}
    for i in range(0, len(uids), 50):
        batch = uids[i:i + 50]
        ids = ",".join(str(x) for x in batch)
        d = F.get("https://games.roblox.com/v1/games?universeIds=" + ids, "games/details_%d_%d" % (batch[0], len(batch)))
        for g in (d or {}).get("data", []):
            details[g["id"]] = g
        v = F.get("https://games.roblox.com/v1/games/votes?universeIds=" + ids, "games/votes_%d_%d" % (batch[0], len(batch)))
        for g in (v or {}).get("data", []):
            votes[g["id"]] = g

    # ---------------- 3. deep set ----------------
    by_playing = sorted(details, key=lambda u: -(details[u].get("playing") or 0))
    deep = list(by_playing[:a.deep])
    for u, ci in chart_info.items():
        if (ci["earning_best"] is not None or ci.get("watch")) and u not in deep and u in details:
            deep.append(u)
    deep_set = set(deep)
    print("deep set:", len(deep))

    pass_rows, badge_rows, prod_rows = [], [], []
    counts = {}
    for n, u in enumerate(deep, 1):
        if n % 25 == 0:
            print("  deep %d/%d  (net %d, cache %d, err %d, 429s %d)" % (n, len(deep), STATS["net"], STATS["cache"], STATS["err"], STATS["429"]))
        c = counts.setdefault(u, {"passes": 0, "badges": 0, "products": 0, "passes_ok": False,
                                  "badges_ok": False, "products_ok": False, "badges_capped": False,
                                  "products_capped": False})
        # game passes
        tok = None
        for page in range(1, PASS_PAGE_CAP + 1):
            url = "https://apis.roblox.com/game-passes/v1/universes/%d/game-passes?passView=Full&pageSize=100" % u
            if tok:
                url += "&pageToken=" + urllib.parse.quote(tok)
            d = F.get(url, "passes/%d_p%d" % (u, page))
            if d is None:
                break
            c["passes_ok"] = True
            for gp in d.get("gamePasses") or []:
                c["passes"] += 1
                pass_rows.append({
                    "snapshot_date": date, "universe_id": u, "pass_id": gp.get("id"),
                    "name": gp.get("displayName") or gp.get("name"), "price": gp.get("price"),
                    "base_price": gp.get("userBasePriceInRobux"), "is_for_sale": gp.get("isForSale"),
                    "has_discount": bool(gp.get("priceDiscountDetails")),
                    "description": gp.get("displayDescription") or "",
                    "created": gp.get("created"), "updated": gp.get("updated"),
                })
            tok = d.get("nextPageToken")
            if not tok:
                break
        # badges
        cur = None
        for page in range(1, BADGE_CAP // 100 + 1):
            url = "https://badges.roblox.com/v1/universes/%d/badges?limit=100&sortOrder=Asc" % u
            if cur:
                url += "&cursor=" + urllib.parse.quote(cur)
            d = F.get(url, "badges/%d_p%d" % (u, page))
            if d is None:
                break
            c["badges_ok"] = True
            for b in d.get("data") or []:
                st = b.get("statistics") or {}
                c["badges"] += 1
                badge_rows.append({
                    "snapshot_date": date, "universe_id": u, "badge_id": b.get("id"),
                    "order_index": c["badges"], "name": b.get("displayName") or b.get("name"),
                    "description": b.get("displayDescription") or b.get("description") or "",
                    "enabled": b.get("enabled"), "created": b.get("created"),
                    "awarded_count": st.get("awardedCount"), "past_day_awarded_count": st.get("pastDayAwardedCount"),
                    "win_rate_percentage": st.get("winRatePercentage"),
                })
            cur = d.get("nextPageCursor")
            if not cur:
                break
            if page == BADGE_CAP // 100:
                c["badges_capped"] = True
        # developer products
        cur = None
        for page in range(1, PRODUCT_CAP // 100 + 1):
            url = "https://apis.roblox.com/developer-products/v2/universes/%d/developerproducts?limit=100" % u
            if cur:
                url += "&cursor=" + urllib.parse.quote(cur)
            d = F.get(url, "products/%d_p%d" % (u, page))
            if d is None:
                break
            c["products_ok"] = True
            for p in d.get("developerProducts") or []:
                c["products"] += 1
                prod_rows.append({
                    "snapshot_date": date, "universe_id": u, "product_id": p.get("ProductId"),
                    "developer_product_id": p.get("DeveloperProductId"),
                    "name": p.get("displayName") or p.get("Name"), "price": p.get("PriceInRobux"),
                    "is_for_sale": p.get("IsForSale"), "description": p.get("displayDescription") or "",
                    "created": p.get("Created"), "updated": p.get("Updated"),
                })
            cur = d.get("nextPageCursor")
            if not cur:
                break
            if page == PRODUCT_CAP // 100:
                c["products_capped"] = True

    write_csv("passes.csv", ["snapshot_date", "universe_id", "pass_id", "name", "price", "base_price",
                             "is_for_sale", "has_discount", "description", "created", "updated"], pass_rows)
    write_csv("badges.csv", ["snapshot_date", "universe_id", "badge_id", "order_index", "name", "description",
                             "enabled", "created", "awarded_count", "past_day_awarded_count",
                             "win_rate_percentage"], badge_rows)
    write_csv("products.csv", ["snapshot_date", "universe_id", "product_id", "developer_product_id", "name",
                               "price", "is_for_sale", "description", "created", "updated"], prod_rows)

    # ---------------- 4. games.csv ----------------
    game_rows = []
    for u in uids:
        g = details.get(u)
        if not g:
            continue
        ci = chart_info[u]
        v = votes.get(u, {})
        cr = g.get("creator") or {}
        c = counts.get(u, {})
        game_rows.append({
            "snapshot_date": date, "universe_id": u, "root_place_id": g.get("rootPlaceId"),
            "name": g.get("name"), "creator_id": cr.get("id"), "creator_name": cr.get("name"),
            "creator_type": cr.get("type"), "creator_verified": cr.get("hasVerifiedBadge"),
            "playing": g.get("playing"), "visits": g.get("visits"), "favorited_count": g.get("favoritedCount"),
            "up_votes": v.get("upVotes"), "down_votes": v.get("downVotes"), "max_players": g.get("maxPlayers"),
            "created": g.get("created"), "updated": g.get("updated"), "genre": g.get("genre"),
            "genre_l1": g.get("genre_l1"), "genre_l2": g.get("genre_l2"), "price": g.get("price"),
            "avatar_type": g.get("universeAvatarType"), "private_servers_allowed": g.get("createVipServersAllowed"),
            "content_maturity": ci["maturity"], "minimum_age": ci["min_age"], "age_recommendation": ci["age_rec"],
            "in_charts": bool(ci["sorts"]),
            "chart_sorts": "|".join(sorted(ci["sorts"])), "n_chart_sorts": len(ci["sorts"]),
            "best_chart_rank": ci["best_rank"], "top_earning_best_rank": ci["earning_best"] if ci["earning_best"] else "",
            "deep_fetched": u in deep_set,
            "n_passes": c.get("passes", "") if c.get("passes_ok") else "",
            "n_badges": c.get("badges", "") if c.get("badges_ok") else "",
            "badges_capped": c.get("badges_capped", ""),
            "n_products": c.get("products", "") if c.get("products_ok") else "",
            "products_capped": c.get("products_capped", ""),
            "description": g.get("description") or "",
        })
    write_csv("games.csv", ["snapshot_date", "universe_id", "root_place_id", "name", "creator_id", "creator_name",
                            "creator_type", "creator_verified", "playing", "visits", "favorited_count", "up_votes",
                            "down_votes", "max_players", "created", "updated", "genre", "genre_l1", "genre_l2",
                            "price", "avatar_type", "private_servers_allowed", "content_maturity", "minimum_age",
                            "age_recommendation", "in_charts", "chart_sorts", "n_chart_sorts", "best_chart_rank",
                            "top_earning_best_rank", "deep_fetched", "n_passes", "n_badges", "badges_capped",
                            "n_products", "products_capped", "description"], game_rows)
    print("done. network calls %d, cache hits %d, errors %d, 429s %d" % (STATS["net"], STATS["cache"], STATS["err"], STATS["429"]))


if __name__ == "__main__":
    main()
