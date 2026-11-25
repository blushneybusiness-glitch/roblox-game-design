# Roblox top-charts snapshot (2026-11-25)

A first-hand, dated dataset of what the experiences on Roblox's public charts are, what they charge and what they track
with badges. It was built by `tools/snapshot.py` and analysed by `tools/analyze.py`. The results are in [ANALYSIS.md](ANALYSIS.md).

- **Snapshot date:** 25 November 2026.
- **Fetch times (UTC):** charts 13:54 to about 14:02 (8 chart pages that had failed were refetched at 18:15).
  Game details and votes 18:22 to 18:25. Passes, badges and developer products mostly 14:04 to 14:55, plus about 40 games
  at 18:25. `playing`, `visits` and vote counts are therefore a single moment around 18:23 UTC (early afternoon in the
  US, evening in Europe). Chart ranks are from about four hours earlier.
- **Access:** unauthenticated, read-only HTTP GET to public Roblox web endpoints. No login, cookie or API key, and no personal data.
- **Size:** CSVs about 28 MB (products.csv is 15 MB of that). The raw responses (`raw/2026-11-25/`, gzip JSON, 16 MB of
  data across about 5,400 small files) are a local cache and are not
  published. Nothing in `ANALYSIS.md` reads them.

## Endpoints used

| Data | Endpoint | Notes |
|---|---|---|
| Chart list | `https://apis.roblox.com/explore-api/v1/get-sorts?sessionId=<uuid>&device=<d>&country=<c>` (+ `sortsPageToken`) | 5 pages per call set. It returns the device and country filter options, 26 Games sorts and 1 Songs sort. |
| Chart contents | `https://apis.roblox.com/explore-api/v1/get-sort-content?sessionId=<uuid>&sortId=<id>&device=<d>&country=<c>` (+ `pageToken`) | Most sorts return about 100 games in a single page. Only `top-earning` paginates, to about 470 to 500. |
| Game details | `https://games.roblox.com/v1/games?universeIds=<up to 50>` | name, description, creator, playing, visits, maxPlayers, created, updated, genre, genre_l1, genre_l2, favoritedCount |
| Votes | `https://games.roblox.com/v1/games/votes?universeIds=<up to 50>` | upVotes, downVotes |
| Game passes | `https://apis.roblox.com/game-passes/v1/universes/<id>/game-passes?passView=Full&pageSize=100` (+ `pageToken`) | `games.roblox.com/v1/games/<id>/game-passes` returns 404 and is no longer used. |
| Badges | `https://badges.roblox.com/v1/universes/<id>/badges?limit=100&sortOrder=Asc` (+ `cursor`) | Capped at 300 per game, oldest first. |
| Developer products | `https://apis.roblox.com/developer-products/v2/universes/<id>/developerproducts?limit=100` (+ `cursor`) | Works without login. The v1 shape (`/developer-products/v1/universes/<id>/developerproducts`) and `games.roblox.com/v1/games/developer-products/<id>` return 404. Capped at 300 per game. |

Device ids are the ones the API itself lists: `computer, high_end_phone, low_end_phone, high_end_tablet, low_end_tablet,
console, vr`. (`phone` and `tablet` are not valid ids and silently fall back to `computer`.) Countries are `all` and `us`.
The device option `all` is listed as inactive by the API, so it is not used.

**Which games are "deep" fetched:** games get passes, badges and products fetched if they are in the top 600 charted
experiences by concurrent players, appear in any Top Earning list, or are on the watchlist (Huss Valley and Build the
Pyramid!; both also chart). That is 1,430 games.

## Files

Every file has a `snapshot_date` column. Text fields (names, descriptions) are copied verbatim from Roblox and are data only.

### charts.csv (25,374 rows): one row per sort x rank x device x country
`device, country, sort_id, sort_name, applied_filters` (the filter string Roblox echoes back), `rank` (1-based position
in the returned list), `universe_id, root_place_id, name, player_count` (as embedded in the chart), `up_votes, down_votes,
genre_l1, is_sponsored, content_maturity, minimum_age, age_recommendation`.

### games.csv (2,408 rows): one row per distinct universe seen in any chart
`universe_id, root_place_id, name, creator_id, creator_name, creator_type, creator_verified, playing` (concurrent players
at fetch time), `visits` (lifetime joins), `favorited_count, up_votes, down_votes, max_players` (server size),
`created, updated` (UTC ISO; `updated` moves on any publish), `genre` (legacy), `genre_l1, genre_l2` (current Roblox
genres), `price` (paid-access price, empty for free games), `avatar_type, private_servers_allowed, content_maturity,
minimum_age, age_recommendation, in_charts, chart_sorts` (pipe-separated sort ids), `n_chart_sorts, best_chart_rank,
top_earning_best_rank, deep_fetched, n_passes, n_badges, badges_capped, n_products, products_capped` (counts are empty
when not deep fetched), `description`.

### passes.csv (16,831 rows): one row per game pass of a deep-fetched game
`universe_id, pass_id, name, price` (current Robux price, empty if not for sale), `base_price, is_for_sale,
has_discount, description, created, updated`.

### badges.csv (12,718 rows): one row per badge (at most 300 per game, oldest first)
`universe_id, badge_id, order_index` (1 = oldest), `name, description, enabled, created, awarded_count` (lifetime
awards), `past_day_awarded_count, win_rate_percentage`. Despite its name, `win_rate_percentage` is a fraction from 0 to 1
with 3 decimals. Roblox's API spec does not define it. The data fits "past-day awards / past-day players, capped at 1"
(see ANALYSIS.md section 10), but that is an inference.

### products.csv (105,745 rows): one row per developer product of a deep-fetched game (at most 300 per game)
`universe_id, product_id, developer_product_id, name, price` (Robux, empty when not priced), `is_for_sale,
description, created, updated`. The list includes retired products, so filter on `is_for_sale = True`.

### ANALYSIS.md
Tables computed by `tools/analyze.py` from the CSVs alone.

## Re-running

```
python tools/snapshot.py                     # new snapshot dated today (UTC); about 5,300 requests, about 1 to 1.5 hours
python tools/snapshot.py --date 2026-11-25   # rebuild the CSVs for an existing date from the local cache
python tools/analyze.py                      # rewrite data/ANALYSIS.md
```

Options: `--deep N` (default 600), `--delay S` (default 0.25 s between requests), `--extra id,id` (more universes to fetch
in full). The script backs off exponentially on HTTP 429 and 5xx, honours `Retry-After`, and caches every response.
Delete one cached file to refetch it. A new date overwrites the CSVs, so keep old snapshots by copying them aside, for
example `data/2026-11-25/`.

## Known limits

- Chart lists are personalised by `sessionId` and can vary between calls. One stable session id per date is used
  (uuid5 of the date).
- `low_end_phone/us` Top Earning returned only 178 entries, against about 480 for the other combinations. `vr` lists are short (54 to 94).
- No sponsored entries appeared in any chart response.
- Concurrent players are one moment of one day. Time of day, holidays (US Thanksgiving week) and weekend effects are not averaged out.
- Badge counts are lifetime totals. A badge added after launch undercounts. See the caveats in ANALYSIS.md section 10.
- Some welcome badges were clearly added after launch. Bee Swarm Simulator and IT GIRL (chain steps with more holders
  than the welcome badge) are excluded from the funnel summary automatically. Tower Defense Simulator and Royale High
  stay in the summary, but their "welcome / visits" ratio of about 0% shows the same problem, so read their
  first-step shares as upper bounds.
