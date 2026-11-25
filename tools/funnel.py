#!/usr/bin/env python3
"""Reads a game's stats and says where players are lost and what a test can prove.

    python tools/funnel.py tools/examples/stats-example.json
    python tools/funnel.py --size 0.43 0.51 --per-day 600

The stats file is JSON in the shape described in kit/templates/stats-intake.md.
The report gives, in this order: the step funnel and its largest drop-off, the
first-session curve and the window with the highest leave rate, each stage of
the player's path against its reference, the splits by traffic source and by
device, the rows of the diagnosis table in foundations/14-metrics-and-diagnosis.md
that the numbers match, the stage to work on first, and the smallest change your
traffic can prove.

It finds where players leave. It cannot say why. For that, watch the moment it
names: kit/stats-to-plan.md, step 3.

Python 3.8 or newer. No packages needed.
"""

import argparse
import json
import math
import sys

# Medians of large Roblox games (GameAnalytics 2026: 500+ games with 1M+ monthly
# users, see foundations/14). Used only when the file gives no "p50" from your
# own dashboard, which is the better reference.
PUBLIC_MEDIAN = {"session_minutes": 9.8, "d1": 0.103, "d7": 0.016, "d30": 0.005}

# A first-session bar that circulates among Roblox producers. It has no written
# source (foundations/05). Printed for information, never used for a verdict.
YARDSTICK = {0.5: 0.95, 1.0: 0.87, 5.0: 0.65}

Z_CONF = 1.96    # 95% confidence, two-sided
Z_POWER = 0.84   # a real change is caught 4 times in 5

# key, stage, label, kind, page, highest value any game plausibly reports
STAGES = [
    ("play_through_rate", "Clicked", "Play-through rate", "rate",
     "foundations/11-clips-and-packaging.md", 0.6),
    ("session_minutes", "First session", "Average session time, min", "minutes",
     "foundations/05-first-session.md and foundations/04-core-loop.md", None),
    ("d1", "Next day", "Day 1 retention", "rate", "foundations/08-retention.md", 0.6),
    ("d7", "Days 2 to 7", "Day 7 retention", "rate",
     "foundations/06-progression-and-economy.md", 0.5),
    ("d30", "Days 8 to 28", "Day 30 retention", "rate", "foundations/13-live-ops.md", 0.4),
    ("conversion", "Pays", "Conversion rate", "rate", "foundations/12-monetization.md", 0.5),
]
STAGE_ORDER = ["Clicked", "First session", "Next day", "Days 2 to 7", "Days 8 to 28", "Pays", "Any"]
NEW_PLAYER_RATES = ("d1", "d7", "d30")
FIRST_SESSION_PAGE = "foundations/05-first-session.md and foundations/04-core-loop.md"

THIRD_GONE = "a third or more gone"
FELL = "fell on last period"
BELOW = "below the median"
WEAK = (BELOW, THIRD_GONE, FELL)
UNJUDGED = ("no data", "no reference")

SPLIT_COLUMNS = [("at_1min", "at 1:00"), ("at_5min", "at 5:00"), ("d1", "day 1"), ("d7", "day 7")]

WARNINGS = []


def pct(x, digits=1):
    return "%.*f%%" % (digits, 100.0 * x)


def points(x, digits=1):
    return "%.*f" % (digits, 100.0 * x)


def clock(minutes):
    seconds = int(round(minutes * 60))
    return "%d:%02d" % (seconds // 60, seconds % 60)


def thousands(x):
    return "{:,}".format(int(round(x)))


def plain(label):
    return label.replace(", min", "")


def as_rate(x, label, limit=None):
    """Accepts 0.052 or 5.2 for 5.2%. Warns when the result looks like a typing slip."""
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        WARNINGS.append("%s is not a number and was ignored." % label)
        return None
    if x > 1.0:
        x = x / 100.0
    if x < 0 or x > 1:
        WARNINGS.append("%s is outside 0 to 100%% and was ignored." % label)
        return None
    if limit is not None and x > limit:
        WARNINGS.append("%s reads as %s. If you meant %s, write %g."
                        % (label, pct(x), pct(x / 100.0, 2), round(x / 100.0, 5)))
    return x


def noise(p, n):
    """Half-width of the 95% interval for a rate p measured on n players."""
    if not n or n <= 0 or p is None:
        return None
    return Z_CONF * math.sqrt(max(p * (1 - p), 0.0) / n)


def gap_noise(p1, n1, p2, n2):
    """Half-width of the 95% interval for the difference of two rates."""
    if not n1 or not n2 or n1 <= 0 or n2 <= 0:
        return None
    return Z_CONF * math.sqrt(max(p1 * (1 - p1), 0.0) / n1 + max(p2 * (1 - p2), 0.0) / n2)


def players_per_version(p1, p2):
    """Players each version needs to tell rate p1 from rate p2."""
    if p1 == p2:
        return float("inf")
    mean = (p1 + p2) / 2.0
    top = (Z_CONF * math.sqrt(2 * mean * (1 - mean))
           + Z_POWER * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))
    return (top / (p2 - p1)) ** 2


def smallest_provable_rise(p, n):
    """Smallest rise from rate p that n players per version can prove."""
    if p is None or not n or n <= 0 or p >= 1:
        return None
    low, high = 0.0, 1.0 - p
    if players_per_version(p, p + high) > n:
        return None
    for _ in range(60):
        mid = (low + high) / 2.0
        if players_per_version(p, p + mid) > n:
            low = mid
        else:
            high = mid
    return high


def curve_points(curve):
    pts = sorted(curve.items())
    if not pts:
        return []
    if pts[0][0] > 0:
        pts = [(0.0, 1.0)] + pts
    return pts


def share_at(pts, minute):
    """Share still playing at a minute, read off the curve (straight line between points)."""
    for (t0, s0), (t1, s1) in zip(pts, pts[1:]):
        if t0 <= minute <= t1:
            if t1 == t0:
                return s1
            return s0 + (s1 - s0) * (minute - t0) / (t1 - t0)
    return None


def blend(rows, column):
    """Share-weighted value of a column over some rows of a split table."""
    pairs = [(r["share"], r[column]) for r in rows if r["share"] and r[column] is not None]
    weight = sum(s for s, _v in pairs)
    if weight <= 0:
        return None, 0.0
    return sum(s * v for s, v in pairs) / weight, weight


def load(path):
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    if not isinstance(raw, dict):
        raise ValueError("the file must hold one JSON object")

    def parse_curve(key):
        curve = {}
        for minute, share in (raw.get(key) or {}).items():
            try:
                at = float(minute)
            except (TypeError, ValueError):
                WARNINGS.append("%s: '%s' is not a minute. Write minutes as numbers, 0.5 for 30 seconds."
                                % (key, minute))
                continue
            value = as_rate(share, "%s at minute %s" % (key, minute))
            if value is not None:
                curve[at] = value
        return curve

    data = {
        "name": raw.get("name", "unnamed game"),
        "dates": raw.get("dates"),
        "days": raw.get("days"),
        "per_day": raw.get("new_players_per_day"),
        "first_session": parse_curve("first_session"),
        "previous": parse_curve("first_session_previous"),
        "funnel": [],
        "metrics": {},
        "by_source": [],
        "by_device": [],
        "milestone": as_rate(raw.get("first_milestone_share"), "first_milestone_share"),
    }

    for row in raw.get("funnel") or []:
        if row.get("users") is None:
            continue
        data["funnel"].append({"step": str(row.get("step", "?")), "users": float(row["users"]),
                               "minute": row.get("minute")})

    for key, _stage, label, kind, _page, limit in STAGES:
        entry = (raw.get("metrics") or {}).get(key) or {}
        if kind == "rate":
            data["metrics"][key] = {
                "value": as_rate(entry.get("value"), label, limit),
                "p50": as_rate(entry.get("p50"), label + " 50th percentile", limit),
                "p90": as_rate(entry.get("p90"), label + " 90th percentile"),
            }
        else:
            data["metrics"][key] = {k: (None if entry.get(k) is None else float(entry[k]))
                                    for k in ("value", "p50", "p90")}

    for key in ("by_source", "by_device"):
        for row in raw.get(key) or []:
            name = str(row.get("name", "?"))
            paid = row.get("paid")
            if paid is None:
                # Roblox names its paid sources "Sponsored ads", "Search ads" and "Portal ads".
                paid = key == "by_source" and ("sponsored" in name.lower() or name.lower().endswith("ads"))
            clean = {"name": name, "paid": bool(paid),
                     "share": as_rate(row.get("share"), "%s share" % name)}
            for column, _title in SPLIT_COLUMNS:
                clean[column] = as_rate(row.get(column), "%s %s" % (name, column))
            data[key].append(clean)

    total = raw.get("new_players")
    if total is None and data["days"] and data["per_day"]:
        total = float(data["days"]) * float(data["per_day"])
    if total is None and data["funnel"]:
        total = data["funnel"][0]["users"]
    data["new_players"] = float(total) if total else None
    if data["per_day"] is None and data["new_players"] and data["days"]:
        data["per_day"] = data["new_players"] / float(data["days"])
    return data


def check_data(data, out):
    notes = list(WARNINGS)
    n = data["new_players"]
    if n is None:
        notes.append("No player count given (days and new_players_per_day). The report cannot tell "
                     "a real gap from noise.")
    elif n < 1000:
        notes.append("Only %s new players in the range. A 10%% rate measured on them is uncertain by "
                     "+/- %s points; trust only gaps of 3 points or more." % (thousands(n), points(noise(0.10, n))))
    if data["days"] is not None and float(data["days"]) < 7:
        notes.append("The range is %g days. Use 7 full days so every weekday appears once." % float(data["days"]))
    pts = curve_points(data["first_session"])
    for (t0, s0), (t1, s1) in zip(pts, pts[1:]):
        if s1 > s0 + 1e-9:
            notes.append("The first-session curve rises between %s and %s. Shares still playing can only fall: "
                         "check the numbers." % (clock(t0), clock(t1)))
    for a, b in zip(data["funnel"], data["funnel"][1:]):
        if b["users"] > a["users"]:
            notes.append("Funnel step '%s' has more players than '%s' before it. Steps must be in the order "
                         "players do them, and all from the same date range." % (b["step"], a["step"]))
    for key, title in (("by_source", "traffic source"), ("by_device", "device")):
        shares = [r["share"] for r in data[key] if r["share"] is not None]
        if shares and not 0.95 <= sum(shares) <= 1.05:
            notes.append("The %s shares add up to %s, not 100%%." % (title, pct(sum(shares), 0)))
        total = data["metrics"]["d1"]["value"]
        mixed = blend(data[key], "d1")[0]
        if total and mixed and abs(mixed - total) / total > 0.2:
            notes.append("The %s split gives a day 1 retention of %s and the total says %s. The split and the "
                         "total come from different dates or filters." % (title, pct(mixed), pct(total)))
    if notes:
        out.append("CHECK THE NUMBERS FIRST")
        for note in notes:
            out.append("  - " + note)
        out.append("")


def funnel_report(data, out):
    steps = data["funnel"]
    out.append("STEP FUNNEL")
    if len(steps) < 2:
        out.append("  No step funnel given. Without one nobody can say which step loses players.")
        out.append("  Log one funnel event per row of kit/templates/first-session-script.md first.")
        out.append("")
        return None
    first = steps[0]["users"]
    has_minute = any(s["minute"] is not None for s in steps)
    layout = "  %-26s %7s %9s %10s %6s %8s %16s" if has_minute else "  %-26s %9s %10s %6s %8s %16s"
    head = ["step"] + (["reached"] if has_minute else []) + ["players", "of joiners", "kept", "lost",
                                                             "lost, of joiners"]
    out.append(layout % tuple(head))
    largest = None
    lowest = None
    in_order = True
    for index, step in enumerate(steps):
        cells = [step["step"][:26]]
        if has_minute:
            cells.append("" if step["minute"] is None else clock(float(step["minute"])))
        if index == 0:
            cells += [thousands(step["users"]), "100%", "", "", ""]
        else:
            before = steps[index - 1]
            kept = step["users"] / before["users"] if before["users"] else 0.0
            lost = before["users"] - step["users"]
            lost_share = lost / first if first else 0.0
            in_order = in_order and kept <= 1.0
            cells += [thousands(step["users"]), pct(step["users"] / first, 0), pct(kept, 0),
                      thousands(lost), pct(lost_share, 0)]
            found = {"from": before, "to": step, "kept": kept, "lost": lost, "lost_share": lost_share,
                     "reached_share": step["users"] / first if first else 0.0, "index": index}
            if largest is None or lost > largest["lost"]:
                largest = found
            if lowest is None or kept < lowest["kept"]:
                lowest = found
        out.append(layout % tuple(cells))
    if largest:
        out.append("  Largest drop-off: '%s' to '%s' loses %s players, %s of everyone who joined."
                   % (largest["from"]["step"], largest["to"]["step"], thousands(largest["lost"]),
                      pct(largest["lost_share"], 0)))
        others = sorted(steps[i]["users"] / steps[i - 1]["users"] for i in range(1, len(steps))
                        if i != largest["index"] and steps[i - 1]["users"])
        if others and in_order:
            half = len(others) // 2
            middle = others[half] if len(others) % 2 else (others[half - 1] + others[half]) / 2.0
            if middle > largest["kept"]:
                gain = largest["from"]["users"] * (middle - largest["kept"]) / first
                largest["gain"] = gain
                spread = ("the other step keeps %s" % pct(middle, 0) if len(others) == 1 else
                          "the other steps keep %s to %s, median %s" % (pct(others[0], 0), pct(others[-1], 0),
                                                                        pct(middle, 0)))
                out.append("  That step keeps %s; %s. At that rate %s more of every 100"
                           % (pct(largest["kept"], 0), spread, points(gain, 0)))
                out.append("  joiners would reach '%s'. This is arithmetic on your funnel, not a forecast."
                           % largest["to"]["step"])
    if lowest and largest and lowest["index"] != largest["index"]:
        out.append("  Hardest step: '%s' to '%s' keeps %s of the players who reach it."
                   % (lowest["from"]["step"], lowest["to"]["step"], pct(lowest["kept"], 0)))
    out.append("")
    return {"largest": largest, "lowest": lowest}


def rate_rise_is_real(before, after, n):
    """True when the leave rate of a window is above the window before it by more than the noise."""
    if after["rate"] <= before["rate"]:
        return False
    if not n:
        return after["rate"] > before["rate"] * 1.25

    def spread(w):
        at_risk = n * w["s0"]
        length = w["t1"] - w["t0"]
        if at_risk <= 0 or length <= 0 or w["s0"] <= 0:
            return 0.0
        share = min(max(w["lost"] / w["s0"], 0.0), 1.0)
        return math.sqrt(share * (1 - share) / at_risk) / length

    return after["rate"] - before["rate"] > Z_CONF * math.sqrt(spread(before) ** 2 + spread(after) ** 2)


def first_session_report(data, out):
    pts = curve_points(data["first_session"])
    out.append("FIRST SESSION (share of new players still playing)")
    if len(pts) < 2:
        out.append("  No curve given. Read it off the New User First Session Retention chart")
        out.append("  (Creator Hub, Analytics, Engagement).")
        out.append("")
        return None
    n = data["new_players"]
    out.append("  %-15s %10s %14s %23s" % ("window", "still in", "lost, points", "leave rate per minute"))
    windows = []
    for (t0, s0), (t1, s1) in zip(pts, pts[1:]):
        lost = s0 - s1
        rate = (lost / s0) / (t1 - t0) if s0 > 0 and t1 > t0 else 0.0
        windows.append({"t0": t0, "t1": t1, "s0": s0, "s1": s1, "lost": lost, "rate": rate, "rises": False})
    for index, w in enumerate(windows):
        w["rises"] = index > 0 and rate_rise_is_real(windows[index - 1], w, n)
        out.append("  %-15s %10s %14s %23s%s" % ("%s to %s" % (clock(w["t0"]), clock(w["t1"])), pct(w["s1"], 0),
                                                points(w["lost"], 0), pct(w["rate"], 0),
                                                "  <- rises" if w["rises"] else ""))
    out.append("  Leave rate: of the players still in the game when the window starts, the share leaving each minute.")
    steepest = max(windows, key=lambda w: w["rate"])
    line = "  Highest leave rate: %s to %s." % (clock(steepest["t0"]), clock(steepest["t1"]))
    inside = [s["step"] for s in data["funnel"]
              if s["minute"] is not None and steepest["t0"] < float(s["minute"]) <= steepest["t1"]]
    if inside:
        line += " Steps players reach in that window: %s." % ", ".join("'%s'" % s for s in inside)
    out.append(line)

    falls = []
    if data["previous"]:
        cells = []
        for minute in sorted(data["previous"]):
            now = share_at(pts, minute)
            if now is None:
                continue
            before = data["previous"][minute]
            width = gap_noise(now, n, before, n)
            if width is None:
                verdict = "no player count, so noise is not known"
            elif abs(now - before) <= width:
                verdict = "inside the noise of +/- %s" % points(width)
            elif now < before:
                verdict = "a real fall, noise is +/- %s" % points(width)
                falls.append({"minute": minute, "now": now, "before": before, "width": width})
            else:
                verdict = "a real rise, noise is +/- %s" % points(width)
            cells.append("%s %s now, %s before (%s)" % (clock(minute), pct(now, 0), pct(before, 0), verdict))
        for index, cell in enumerate(cells):
            out.append("  %s %s" % ("Against the previous period:" if index == 0 else " " * 28, cell))
    falls.sort(key=lambda f: f["before"] - f["now"], reverse=True)
    marks = [(m, share_at(pts, m)) for m in sorted(YARDSTICK)]
    marks = [(m, s) for m, s in marks if s is not None]
    if marks:
        out.append("  A bar some producers use, with no written source: %s. Yours: %s."
                   % (", ".join("%s at %s" % (pct(YARDSTICK[m], 0), clock(m)) for m, _s in marks),
                      ", ".join(pct(s, 0) for _m, s in marks)))
    out.append("")
    return {"points": pts, "windows": windows, "steepest": steepest, "falls": falls}


def stage_report(data, session, out):
    n = data["new_players"]
    rows = []
    for key, stage, label, kind, page, _limit in STAGES:
        if key == "session_minutes" and session:
            # The two curve rows sit in front of session time: a player meets them first.
            fallen = {f["minute"]: f for f in session["falls"]}
            for minute, curve_key in ((1.0, "at_1min"), (5.0, "at_5min")):
                value = share_at(session["points"], minute)
                if value is None:
                    continue
                if minute == 1.0 and value <= 2.0 / 3.0:
                    verdict, source = THIRD_GONE, "diagnosis table"
                elif minute in fallen:
                    verdict, source = FELL, "your previous period"
                else:
                    verdict, source = "no reference", ""
                rows.append({"key": curve_key, "stage": "First session", "kind": "rate",
                             "label": "Still playing at %s" % clock(minute), "page": FIRST_SESSION_PAGE,
                             "value": value, "p50": None, "p90": None, "verdict": verdict, "source": source,
                             "fall": fallen.get(minute)})
        entry = data["metrics"][key]
        value, p50, p90 = entry["value"], entry["p50"], entry["p90"]
        source = "your dashboard"
        if p50 is None and key in PUBLIC_MEDIAN:
            p50, p90, source = PUBLIC_MEDIAN[key], None, "large-game median"
        if value is None:
            verdict = "no data"
        elif p50 is None:
            verdict = "no reference"
        else:
            width = noise(value, n) if key in NEW_PLAYER_RATES else None
            if width is not None and abs(value - p50) <= width:
                verdict = "too close to call"
            elif value < p50:
                verdict = BELOW
            elif p90 is not None and value >= p90:
                verdict = "above the band"
            elif p90 is not None:
                verdict = "in the band"
            else:
                verdict = "at or above the median"
        rows.append({"key": key, "stage": stage, "label": label, "kind": kind, "page": page,
                     "value": value, "p50": p50, "p90": p90, "verdict": verdict,
                     "source": source if p50 is not None else "", "fall": None})

    out.append("STAGES, in the order a player meets them")
    out.append("  %-14s %-26s %7s %7s %7s  %-23s %s" % ("stage", "number", "yours", "50th", "90th", "verdict",
                                                       "compared with"))
    for row in rows:
        out.append(("  %-14s %-26s %7s %7s %7s  %-23s %s" % (
            row["stage"], row["label"], show(row, row["value"]), show(row, row["p50"]),
            show(row, row["p90"]), row["verdict"], row["source"])).rstrip())
    out.append("")
    return rows


def show(row, x):
    if x is None:
        return "-"
    return "%.1f" % x if row["kind"] == "minutes" else pct(x)


def split_table(rows, title, first_column, columns, out):
    out.append(title)
    out.append("  %-28s %6s " % (first_column, "share") + " ".join("%9s" % t for _c, t in columns))
    for row in rows:
        name = row["name"] + (" (paid)" if row.get("paid") else "")
        out.append("  %-28s %6s " % (name[:28], "-" if row["share"] is None else pct(row["share"], 0))
                   + " ".join("%9s" % ("-" if row[c] is None else pct(row[c])) for c, _t in columns))


def source_report(data, rows, out):
    """Returns the columns where paid traffic is really lower, and the values without paid traffic."""
    table = data["by_source"]
    if not table:
        return [], {}
    n = data["new_players"]
    columns = [(c, t) for c, t in SPLIT_COLUMNS if any(r[c] is not None for r in table)]
    paid_rows = [r for r in table if r["paid"]]
    free_rows = [r for r in table if not r["paid"]]
    gaps = []
    without_paid = {}
    extra = []
    if paid_rows and free_rows:
        summary = {"name": "Not paid, together", "paid": False,
                   "share": sum(r["share"] or 0.0 for r in free_rows)}
        for c, _t in columns:
            summary[c] = blend(free_rows, c)[0]
        extra.append(summary)
    split_table(table + extra, "BY TRAFFIC SOURCE", "source", columns, out)
    if not paid_rows:
        out.append("  No source is marked \"paid\": true, so ad traffic could not be set apart.")
    for c, t in columns:
        if not (paid_rows and free_rows):
            break
        paid, paid_weight = blend(paid_rows, c)
        free, free_weight = blend(free_rows, c)
        if paid is None or free is None:
            continue
        without_paid[c] = free
        width = gap_noise(paid, n * paid_weight if n else None, free, n * free_weight if n else None)
        real = width is not None and abs(paid - free) > width
        if width is None:
            out.append("  %s: paid %s against %s for the rest." % (t.capitalize(), pct(paid), pct(free)))
        else:
            out.append("  %s: paid %s against %s for the rest. The gap is %s the noise (+/- %s points)."
                       % (t.capitalize(), pct(paid), pct(free), "bigger than" if real else "inside", points(width)))
        if real and paid < free:
            gaps.append({"column": c, "title": t, "paid": paid, "free": free, "paid_share": paid_weight})
        stage = next((r for r in rows if r["key"] == c), None)
        if stage and stage["value"] is not None and stage["p50"] is not None and stage["value"] < stage["p50"]:
            gap = stage["p50"] - stage["value"]
            rest = stage["p50"] - free
            if rest <= 0:
                out.append("  %s is %s points under the median, and all of that is the paid traffic:"
                           % (stage["label"], points(gap)))
                out.append("  the other sources are at %s." % pct(free))
            elif rest < gap:
                out.append("  %s is %s points under the median: %s of those points are the paid traffic,"
                           % (stage["label"], points(gap), points(gap - rest)))
                out.append("  %s are the game." % points(rest))
    out.append("")
    return gaps, without_paid


def device_report(data, out):
    """Returns the columns where phones are really lower than computers."""
    table = data["by_device"]
    if not table:
        return []
    n = data["new_players"]
    columns = [(c, t) for c, t in SPLIT_COLUMNS if any(r[c] is not None for r in table)]
    split_table(table, "BY DEVICE", "device", columns, out)

    def pick(words):
        for row in table:
            if any(w in row["name"].lower() for w in words):
                return row
        return None

    phone = pick(("phone", "mobile"))
    computer = pick(("computer", "desktop", "pc"))
    gaps = []
    if phone and computer:
        for c, t in columns:
            if phone[c] is None or computer[c] is None:
                continue
            width = gap_noise(phone[c], n * phone["share"] if n and phone["share"] else None,
                              computer[c], n * computer["share"] if n and computer["share"] else None)
            real = width is not None and abs(phone[c] - computer[c]) > width
            if width is None:
                out.append("  %s: %s %s against %s %s." % (t.capitalize(), phone["name"], pct(phone[c]),
                                                        computer["name"], pct(computer[c])))
            else:
                out.append("  %s: %s %s against %s %s. The gap is %s the noise (+/- %s points)."
                           % (t.capitalize(), phone["name"], pct(phone[c]), computer["name"], pct(computer[c]),
                              "bigger than" if real else "inside", points(width)))
            if real and phone[c] < computer[c]:
                gaps.append({"column": c, "title": t, "phone": phone[c], "computer": computer[c],
                             "share": phone["share"]})
    out.append("")
    return gaps


def match_symptoms(data, rows, funnel, session, paid_gaps, phone_gaps):
    """Rows of the diagnosis table in foundations/14 that the numbers match."""
    by_key = {r["key"]: r for r in rows}
    found = []

    def add(stage, symptom, yours, likely, fix, kind, page):
        found.append({"stage": stage, "symptom": symptom, "yours": yours, "likely": likely,
                      "fix": fix, "kind": kind, "page": page})

    ptr = by_key["play_through_rate"]
    if ptr["verdict"] == BELOW:
        add("Clicked", "Many impressions, low play-through",
            "%s against a median of %s." % (pct(ptr["value"]), pct(ptr["p50"])),
            "the thumbnail and title promise nothing a player wants, or the image is not the game.",
            "five clearly different thumbnails for 7 days, each showing real play; a verb-and-thing title.",
            "packaging", "foundations/11-clips-and-packaging.md")

    if session:
        pts = session["points"]
        one, three = share_at(pts, 1.0), share_at(pts, 3.0)
        if one is not None and one <= 2.0 / 3.0:
            add("First session", "A third or more leave before 60 s",
                "%s are gone at 1:00." % pct(1 - one, 0),
                "the promised object is not on screen when the player gains control, or the HUD hides it.",
                "promised object at the spawn; cut the HUD to six items.",
                "world and screen", "foundations/05-first-session.md")
        if one is not None and three is not None and (one - three) > (1 - one):
            add("First session", "Leaves cluster at 61 to 180 s",
                "%s points are lost between 1:00 and 3:00, against %s in the first minute."
                % (points(one - three, 0), points(1 - one, 0)),
                "our read: the first reward came and the second did not.",
                "make purchases 2 and 3 as fast as purchase 1; check the wait with tools/pacing.py.",
                "numbers", "foundations/04-core-loop.md")

    if funnel and funnel["largest"]:
        big = funnel["largest"]
        add("First session", "The largest drop-off in the funnel (table row: a cliff at one funnel step)",
            "'%s' to '%s' loses %s players (%s of everyone who joined) and keeps %s."
            % (big["from"]["step"], big["to"]["step"], thousands(big["lost"]), pct(big["lost_share"], 0),
               pct(big["kept"], 0)),
            "the step cannot be found, needs reading, can fail, or costs a wait. The funnel cannot say which.",
            "find out which with the zoom funnel (kit/stats-to-plan.md, step 4), then change one thing.",
            "not known yet", "foundations/05-first-session.md")

    if session:
        windows = session["windows"]
        for index, w in enumerate(windows):
            if index > 0 and w["t0"] >= 5.0 and w["rises"]:
                add("First session", "Steady until minute 5 or 6, then a drop",
                    "the leave rate rises from %s to %s a minute after %s."
                    % (pct(windows[index - 1]["rate"], 0), pct(w["rate"], 0), clock(w["t0"])),
                    "our read: the opening ended and no long goal replaced it.",
                    "put the next zone or the rebirth requirements on screen before minute 5.",
                    "screen", "foundations/05-first-session.md")
                break
        if session["falls"]:
            f = session["falls"][0]
            add("First session", "The first-session curve fell against the previous period",
                "at %s, %s now against %s before." % (clock(f["minute"]), pct(f["now"], 0), pct(f["before"], 0)),
                "something changed: an update added a step or a message, performance fell, or the traffic mix moved.",
                "list what shipped between the two periods; read the error and performance reports; split by source.",
                "regression", "foundations/14-metrics-and-diagnosis.md")

    early = [g for g in phone_gaps if g["column"] in ("at_1min", "at_5min")] or phone_gaps
    if early:
        g = early[0]
        add("First session", "Phones bounce more than computers",
            "%s: %s on phones against %s on computers; phones are %s of new players."
            % (g["title"], pct(g["phone"]), pct(g["computer"]), "-" if g["share"] is None else pct(g["share"], 0)),
            "memory and frame rate on 2 to 4 GB Android phones, a control outside the thumb's reach, or small text.",
            "test a full server on a 3 GB Android phone; read frame rate and out-of-memory exits by device.",
            "device", "foundations/10-feel-and-feedback.md")

    if data["milestone"] is not None and data["milestone"] < 0.25:
        add("First session", "The first milestone keeps under a quarter of joiners",
            "%s reach it." % pct(data["milestone"], 0),
            "our read: the milestone comes too early or is too hard.",
            "place it after the first reward, the first purchase and the first sight of the long goal, or lower its cost.",
            "numbers", "foundations/06-progression-and-economy.md")

    minutes = by_key["session_minutes"]
    if minutes["value"] is not None and minutes["value"] < 7:
        add("First session", "Average session under 7 minutes",
            "%.1f minutes." % minutes["value"],
            "dead time in the loop; sessions of 0 to 3 minutes go with a 4.31% median day 1 retention.",
            "fill the loop table with measured seconds and treat every wait.",
            "rules and numbers", "foundations/04-core-loop.md")

    d1, d7 = by_key["d1"], by_key["d7"]
    long_session = (minutes["value"] is not None and minutes["p50"] is not None
                    and minutes["value"] >= minutes["p50"])
    if long_session and d1["value"] is not None and d1["value"] < 0.06:
        add("Next day", "Long first sessions, day 1 retention under 6%",
            "%.1f minutes a session, %s return the next day." % (minutes["value"], pct(d1["value"])),
            "our read: nothing pulls the player back: no clock, nothing growing while they are away.",
            "one 5-minute clock and growth while offline before anything else.",
            "rules", "foundations/08-retention.md")
    if (d1["value"] is not None and d1["verdict"] not in (BELOW,) + UNJUDGED
            and d7["value"] is not None and d7["value"] < 0.01):
        add("Days 2 to 7", "Day 1 retention near the median, day 7 under 1%",
            "day 1 %s, day 7 %s." % (pct(d1["value"]), pct(d7["value"], 2)),
            "the ladder runs out or stops showing progress.",
            "log time-to-level; add the next ladder step.",
            "numbers and content", "foundations/06-progression-and-economy.md")

    pays = by_key["conversion"]
    if pays["verdict"] == BELOW:
        add("Pays", "Conversion below the median",
            "%s against a median of %s." % (pct(pays["value"], 2), pct(pays["p50"], 2)),
            "prices too high for the audience, or the shop is hard to find.",
            "check prices against the genre table; remove hard-coded prices and enrol in Managed Pricing.",
            "numbers and screen", "foundations/12-monetization.md")

    if paid_gaps:
        g = next((x for x in paid_gaps if x["column"] == "d1"), paid_gaps[0])
        add("Any", "Day 1 retention and playtime drop when ads run",
            "%s: %s for paid sources against %s for the rest; paid sources bring %s of new players."
            % (g["title"], pct(g["paid"]), pct(g["free"]), pct(g["paid_share"], 0)),
            "ad traffic is colder, or the ad promises something the first minute lacks.",
            "judge the game on the other sources; show real play in the ad or cut the spend; then fix the step "
            "where ad players stop.",
            "packaging", "foundations/11-clips-and-packaging.md")

    found.sort(key=lambda s: STAGE_ORDER.index(s["stage"]))
    return found


def symptom_report(symptoms, out):
    out.append("ROWS OF THE DIAGNOSIS TABLE YOUR NUMBERS MATCH (foundations/14-metrics-and-diagnosis.md)")
    if not symptoms:
        out.append("  None with the numbers given.")
        out.append("")
        return
    out.append("  A match says where to look. It is not proof of the cause.")
    for index, s in enumerate(symptoms, 1):
        out.append("  %d. [%s] %s" % (index, s["stage"], s["symptom"]))
        out.append("       Yours:     %s" % s["yours"])
        out.append("       Likely:    %s" % s["likely"])
        out.append("       First fix: %s" % s["fix"])
        out.append("       Kind:      %s.  Read %s" % (s["kind"], s["page"]))
    out.append("")


def where_first_session(funnel, session, out):
    """Prints where in the first session to look. Returns a goal for the largest drop-off, if any."""
    located = False
    goal = None
    if funnel and funnel["largest"]:
        big = funnel["largest"]
        when = ""
        if big["from"]["minute"] is not None and big["to"]["minute"] is not None:
            when = ", around %s to %s" % (clock(float(big["from"]["minute"])), clock(float(big["to"]["minute"])))
        out.append("  Where:  the largest drop-off, '%s' to '%s'%s:" % (big["from"]["step"], big["to"]["step"], when))
        out.append("          %s players, %s of everyone who joined." % (thousands(big["lost"]),
                                                                    pct(big["lost_share"], 0)))
        located = True
        if big.get("gain"):
            goal = ("the share of joiners who reach '%s'" % big["to"]["step"], big["reached_share"],
                    big["reached_share"] + big["gain"] / 2.0, "half the gap to the other steps", True)
    if session:
        w = session["steepest"]
        out.append("  %s  the highest leave rate, %s to %s."
                   % ("      " if located else "Where:", clock(w["t0"]), clock(w["t1"])))
        located = True
    if not located:
        out.append("  Where:  not known. No first-session curve and no step funnel were given, so the moment")
        out.append("          cannot be found. Log the funnel first: foundations/14-metrics-and-diagnosis.md,")
        out.append("          section Instrumenting.")
    return goal


def first_report(data, rows, funnel, session, symptoms, paid_gaps, phone_gaps, without_paid, out):
    out.append("WORK ON THIS FIRST")
    weak = [r for r in rows if r["verdict"] in WEAK]
    then = "  Then:   kit/stats-to-plan.md from step 3: watch that moment, name the cause, name the kind of fix."

    if not weak:
        judged = [r for r in rows if r["verdict"] not in UNJUDGED]
        if not judged:
            out.append("  No stage could be judged: the file has no dashboard number with a reference.")
            if funnel or session:
                out.append("  Start with the first session. For most new players it is the only one.")
                where_first_session(funnel, session, out)
                out.append("  Read:   %s" % FIRST_SESSION_PAGE)
                out.append(then)
            else:
                out.append("  Fill kit/templates/stats-intake.md. The five numbers under 'The least you need' are enough to start.")
        else:
            out.append("  No stage is clearly below its median with the numbers given.")
            close = [plain(r["label"]) for r in rows if r["verdict"] == "too close to call"]
            if close:
                out.append("  Too close to call on this many players: %s." % ", ".join(close))
            banded = [r for r in rows if r["value"] is not None and r["p90"]]
            if banded:
                far = min(banded, key=lambda r: r["value"] / r["p90"])
                out.append("  Next target: %s, at %s against a 90th percentile of %s."
                           % (plain(far["label"]), show(far, far["value"]), show(far, far["p90"])))
                out.append("  Read:   %s" % far["page"])
            if symptoms:
                out.append("  The rows listed above still match your numbers. They are the next places to look.")
            missing = [plain(r["label"]) for r in rows if r["verdict"] in UNJUDGED and r["key"] not in
                       ("at_1min", "at_5min")]
            if missing:
                out.append("  Not judged, no data or no reference: %s." % ", ".join(missing))
        out.append("")
        return

    target = weak[0]
    stage = target["stage"]
    same_stage = [r for r in weak if r["stage"] == stage]
    for index, row in enumerate(same_stage):
        lead = "  Stage:  %s. " % stage if index == 0 else "          "
        if row["verdict"] == THIRD_GONE:
            out.append("%s%s of new players are gone at 1:00. A third or more is a row of the diagnosis table."
                       % (lead, pct(1 - row["value"], 0)))
        elif row["verdict"] == FELL:
            f = row["fall"]
            out.append("%sThe share still playing at %s fell from %s to %s against the previous period."
                       % (lead, clock(f["minute"]), pct(f["before"], 0), pct(f["now"], 0)))
        else:
            unit = " min" if row["kind"] == "minutes" else ""
            out.append("%s%s is %s%s against a median of %s%s (%s)."
                       % (lead, plain(row["label"]), show(row, row["value"]), unit, show(row, row["p50"]), unit,
                          row["source"]))

    if any(r["verdict"] == FELL for r in same_stage):
        out.append("          That is more than the noise. Look first at what changed between the two periods.")

    goal = None
    if stage == "First session":
        goal = where_first_session(funnel, session, out)
    else:
        out.append("  Where:  %s" % {
            "Clicked": "the thumbnails, the icon and the title.",
            "Next day": "what the player owns at the end of the first session that changes while they are away.",
            "Days 2 to 7": "the ladder: how long each step takes and what the player sees of the next one.",
            "Days 8 to 28": "the update rhythm and what players do together.",
            "Pays": "the shop: what is sold, at what price, and how a player finds it.",
        }[stage])
        if target["kind"] == "rate" and target["p50"] is not None:
            goal = (plain(target["label"]).lower(), target["value"], (target["value"] + target["p50"]) / 2.0,
                    "half the gap to the median", target["key"] in NEW_PLAYER_RATES)
        if target["key"] in NEW_PLAYER_RATES and data["metrics"]["session_minutes"]["value"] is None:
            out.append("  Note:   no session time was given. If it is under 7 minutes, the first session comes")
            out.append("          before this stage.")
        free = without_paid.get(target["key"])
        if free is not None and target["p50"] is not None and free >= target["p50"]:
            out.append("  Note:   without paid traffic this number is %s, at or above the median. The gap is the"
                       % pct(free))
            out.append("          ads, not the game: read foundations/11-clips-and-packaging.md before changing the game.")
    if goal:
        what, now, aim, why, on_new_players = goal
        out.append("  Target: start with %s:" % why)
        out.append("          %s from %s to %s." % (what, pct(now), pct(aim)))
        rise = smallest_provable_rise(now, float(data["per_day"]) * 7.0) if data["per_day"] and on_new_players else None
        if rise is not None and aim - now >= rise:
            out.append("          A 14-day split at your traffic can prove a rise of %s points, so this can be read."
                       % points(rise))
        elif rise is not None:
            out.append("          A 14-day split at your traffic can prove only %s points or more. Plan a bigger"
                       % points(rise))
            out.append("          change, a longer test, or a number nearer the start of the funnel.")
    before = []
    if paid_gaps:
        before.append("split every number by traffic source: paid players leave faster than the rest (table above).")
    if phone_gaps and stage in ("First session", "Next day"):
        before.append("check phones apart from computers: the gap is bigger than the noise (table above).")
    for index, line in enumerate(before):
        out.append("  %s %s" % ("First: " if index == 0 else "       ", line))
    numbers = [str(i) for i, s in enumerate(symptoms, 1) if s["stage"] in (stage, "Any")]
    if numbers:
        out.append("  Rows:   %s in the list above." % ", ".join(numbers))
    out.append("  Read:   %s" % target["page"])
    out.append(then)
    later = [plain(r["label"]) for r in weak if r["stage"] != stage]
    if later:
        out.append("  Later:  %s. They sit behind this stage: fix it, then read them again." % ", ".join(later))
    out.append("")


def proof_report(data, rows, funnel, session, out):
    per_day = data["per_day"]
    out.append("WHAT YOUR TRAFFIC CAN PROVE")
    if not per_day:
        out.append("  Give new_players_per_day to see the smallest change a test can prove.")
        out.append("")
        return
    per_day = float(per_day)
    lines = []
    if funnel and funnel["largest"]:
        big = funnel["largest"]
        lines.append(("Reached '%s'" % big["to"]["step"][:24], big["reached_share"], True))
    if session:
        five = share_at(session["points"], 5.0)
        if five is not None:
            lines.append(("Still playing at 5:00", five, False))
    by_key = {r["key"]: r for r in rows}
    for key in ("d1", "d7"):
        if by_key[key]["value"] is not None:
            lines.append((by_key[key]["label"], by_key[key]["value"], True))
    if not lines:
        out.append("  No rate on new players was given.")
        out.append("")
        return
    layout = "  %-32s %7s %14s %14s %14s %17s"
    out.append("  %s new players a day. The smallest rise a test can tell from noise: points, then the same"
               % thousands(per_day))
    out.append("  rise as a share of the number now.")
    out.append(layout % ("number", "now", "14-day split", "28-day split", "60-day split", "7 days each side"))

    def cell(value, players):
        rise = smallest_provable_rise(value, players)
        if rise is None:
            return "-"
        return "+%s (%s)" % (points(rise), pct(rise / value, 0) if value > 0 else "-")

    for label, value, in_experiment in lines:
        cells = [cell(value, per_day * days / 2.0) if in_experiment else "-" for days in (14, 28, 60)]
        cells.append(cell(value, per_day * 7.0))
        out.append(layout % (label[:32], pct(value), cells[0], cells[1], cells[2], cells[3]))
    out.append("  A split is a Roblox Experiment: one control and one variant, 50/50, all players, 14 to 60 days.")
    out.append("  Roblox shows its own minimum detectable effect, as a share, when you create one. Use that")
    out.append("  figure when you have it. It says games under 1,000 daily users may not get useful data.")
    out.append("  7 days each side is before against after, with no random split: weekday, updates and traffic")
    out.append("  mix move the number too. Under 1,000 players a side, trust only gaps of 3 points or more.")
    out.append("  For any other pair of numbers: python tools/funnel.py --size 0.43 0.51 --per-day %d" % per_day)
    out.append("")


def size_mode(p1, p2, per_day):
    p1, p2 = as_rate(p1, "first rate"), as_rate(p2, "second rate")
    if p1 is None or p2 is None or p1 == p2:
        sys.exit("Give two different rates, for example --size 0.43 0.51")
    need = players_per_version(p1, p2)
    print("To tell %s from %s:" % (pct(p1), pct(p2)))
    print("  %s players per version (95%% confidence, a real gap is caught 4 times in 5)." % thousands(math.ceil(need)))
    if not per_day:
        return
    split = int(math.ceil(2 * need / float(per_day)))
    side = int(math.ceil(need / float(per_day)))
    if split > 60:
        print("  At %s new players a day a 50/50 split needs %d days, more than the 60 a Roblox Experiment"
              % (thousands(per_day), split))
        print("  can run. Test a bigger change, or a step nearer the start of the funnel.")
    else:
        print("  At %s new players a day a 50/50 split needs %d days of traffic. A Roblox Experiment runs"
              % (thousands(per_day), split))
        print("  14 to 60 days, so plan %d." % max(14, split))
    if side > 28:
        print("  Before against after would need %d days each side. Over that long the weekday mix, updates"
              % side)
        print("  and traffic change too much to trust the comparison.")
    else:
        print("  Before against after: %d days each side for the count. Use at least 7 each side so every"
              % side)
        print("  weekday appears once.")


def main():
    parser = argparse.ArgumentParser(description="Find where a game loses its players.")
    parser.add_argument("stats", nargs="?", help="JSON file; see kit/templates/stats-intake.md")
    parser.add_argument("--size", nargs=2, type=float, metavar=("NOW", "EXPECTED"),
                        help="players needed to tell two rates apart, for example --size 0.43 0.51")
    parser.add_argument("--per-day", type=float, help="new players a day, used with --size")
    args = parser.parse_args()

    if args.size:
        size_mode(args.size[0], args.size[1], args.per_day)
        return
    if not args.stats:
        parser.error("give a stats file, or --size NOW EXPECTED")
    try:
        data = load(args.stats)
    except (OSError, ValueError) as err:
        sys.exit("Could not read %s: %s" % (args.stats, err))

    out = ["Stats check: %s" % data["name"]]
    facts = []
    if data["dates"]:
        facts.append(str(data["dates"]))
    if data["new_players"]:
        facts.append("%s new players" % thousands(data["new_players"]))
    if facts:
        out.append("  " + ", ".join(facts))
    out.append("")

    check_data(data, out)
    funnel = funnel_report(data, out)
    session = first_session_report(data, out)
    rows = stage_report(data, session, out)
    paid_gaps, without_paid = source_report(data, rows, out)
    phone_gaps = device_report(data, out)
    symptoms = match_symptoms(data, rows, funnel, session, paid_gaps, phone_gaps)
    symptom_report(symptoms, out)
    first_report(data, rows, funnel, session, symptoms, paid_gaps, phone_gaps, without_paid, out)
    proof_report(data, rows, funnel, session, out)
    print("\n".join(out).rstrip())


if __name__ == "__main__":
    main()
