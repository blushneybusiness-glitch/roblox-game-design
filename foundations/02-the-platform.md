# The platform

This page holds the facts about Roblox itself that every design has to fit: who plays and on what, how a game gets shown, which numbers are normal, who can join and talk, and what the chart looks like now. Open it before you pick a server size, a content label or a launch date, and whenever a dashboard number looks wrong. Everything here was true on 25 November 2026. Roblox changed its discovery and publishing rules four times between May and August 2026, so check dated items against the live docs.

## What is known

### Who plays

Roblox reported Q3 2026 on 29 October 2026. Daily users fell year on year for the first time ([GGRecon](https://www.ggrecon.com/articles/roblox-daily-players-fall-q3-2026/)).

| Quarter | Daily users (DAU) | Hours in the quarter | Hours per DAU per day (our arithmetic) |
|---|---|---|---|
| Q3 2025 | 152M | about 40B (our arithmetic from the 15% fall) | about 2.9 |
| Q1 2026 | 132M | not known | not known |
| Q2 2026 | 123M | 29B | about 2.6 |
| Q3 2026 | 138M (down 9% on the year) | nearly 34B (down 15%) | about 2.7 |

Sources: [GamesBeat, Q3 2026](https://gamesbeat.com/roblox-grows-revenues-in-q3-by-16-but-stock-falls-in-after-hours-trading/), [Roblox newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox), [GamesBeat, RDC 2026](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/). Monthly paying users fell 16% to 30M; bookings per payer rose 5%.

**Age.** Roblox now counts age only for players who passed an age check: 64% of daily users by Q3, and more than 80% of those aged 13 to 17. Adults were 29% of age-checked daily users worldwide and 37% in the US, up from 27% and 33% in Q2 ([MediaPost](https://www.mediapost.com/publications/article/419134/), a summary of the letter). The share under 13 in 2026 is not known.

**Regions.** One secondary blog gives the Q3 split. Its DAU add up to the reported 138M and its revenue to the reported $1.572B, but it is not the letter itself ([Gaming Amigos](https://www.gamingamigos.com/post/roblox-q3-2026)).

| Region | DAU | Hours | Revenue | Revenue per DAU in the quarter (our arithmetic) | Hours per DAU per day (our arithmetic) |
|---|---|---|---|---|---|
| US and Canada | 24M | 7B | $895M | about $37 | about 3.2 |
| Europe | 32M | 8B | $325M | about $10 | about 2.7 |
| Asia-Pacific | 42M | 10B | $191M | about $4.50 | about 2.6 |
| Rest of world | 40M | 9B | $161M | about $4 | about 2.5 |

**Our read:** a US or Canadian player brings about eight times the revenue of an Asia-Pacific player and plays about 20% longer a day. Most of your players will be outside the US; most of your money will not.

**Devices.** Roblox says Android is about 65% of a typical game's players. Of those, about 60% have 2 to 4 GB of memory, 35% have 4 to 8 GB and 5% more ([Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware)). The same page says to watch for frame rate falling over a 10 to 15 minute session, a sign of overheating. The split between phone, tablet, desktop and console is not known.

**Our read:** 65% x 60% = 39% of all players are on a 2 to 4 GB Android phone, the largest single device class.

### How games are found

On 15 June 2026 Roblox rebuilt Recommended For You, the main row on Home ([DevForum](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)). Its stated reason: the old system overvalued short-term play, so games with exciting thumbnails pushed out games people kept playing ([Roblox newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)). The window grew from 7 days to 28, split into day 1, days 2 to 7 and days 8 to 28.

The signals, in Roblox's order ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery), [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)):

| Rank | Signal | Roblox's definition, paraphrased |
|---|---|---|
| 1 | Play-through rate (PTR) | How often users play after seeing the game in Recommended For You |
| 2 | First-play bounce rate | Negative signal for users who leave a short first session, in two buckets: under 60 seconds, and 61 to 180 seconds |
| 3 | Play days per user | Averaged for day 1, days 2 to 7 (days played out of 6) and days 8 to 28 |
| 4 | Playtime per user | Capped at 60 minutes per user, per game, per day |
| 5 | Intentional co-play days | Days played with friends through joins, invites and private servers |
| 6 | Qualified play sessions | Sessions with accidental clicks and quick bounces removed |
| 7 | Spend days per user | Days the user spent anything |
| 8 | Robux spent per user | Total spend |

Rows 1 to 4 are "most important", rows 5 to 8 "important". The exact weights are not known. Every signal is a per-user average, so a small game with keen players is not held back by its size.

What does not count:

- Only players who joined organically from Recommended For You count for PTR and bounce. Their later days count even if they return another way.
- Players first acquired through ads, curated rows, search, friends or social media are excluded, even if they later return through Home. Sponsored tiles are not candidates for Recommended For You.
- Continue Playing traffic does not count as an impression.

New games do not wait 28 days: signals arrive in stages over a moving window, though Roblox says a strong days 8 to 28 is "very unlikely" after a poor first week. Story games are not penalised for lower long-term retention, and genre is not a ranking factor. Home traffic as a whole peaks on Saturdays, in summer, at back to school and in holidays ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).

**What gets a game shown less** ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)):

- No custom thumbnail. One is required for any Home recommendation.
- Copies. Games whose metadata and place files closely resemble an existing game are "no longer prioritized for recommendations" and may rank lower in search. Protection goes to the game that first added the original material, not the oldest one.
- Misleading pages. Roblox's example: dinosaur title and thumbnails on what is really a generic obstacle course.
- Money in the metadata (Roblox's example: "Robux! Play now!"), and leading with giveaways.
**Charts and search.** Top Playing Now ranks by concurrent users ([DevForum](https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809)). Discover sorts are not personalised and can be filtered by country and device ([DevForum](https://devforum.roblox.com/t/testing-an-enhanced-discover-page-top-charts-and-new-sorts/2954676)). Formulas for Top Trending, Top Earning, Up-and-Coming and Today's Picks are not published. The Trending Events sort needs a public event started in the last 7 days with 1,000+ RSVPs ([Experience events](https://create.roblox.com/docs/en-us/production/promotion/experience-events)). Search is semantic in every supported language ([Discovery docs](https://create.roblox.com/docs/discovery)).

### The gate for reaching players under 16

Since 16 June 2026 a new game is shown first only to age-checked players aged 16+. To reach Roblox Kids (5 to 8) and Roblox Select (9 to 15), it has to collect plays from "highly engaged players" (HEP). Roblox defines an HEP by account age, time in your game and a purchase anywhere on Roblox in the last 60 days; the exact formula is not published ([Kids and Select docs](https://create.roblox.com/docs/en-us/production/publishing/kids-and-select)).

| Date | Entry bar |
|---|---|
| 19 May 2026 | Pilot in New Zealand, the Netherlands, Australia, Indonesia |
| 16 Jun 2026 | Global launch: 500 HEP ([DevForum](https://devforum.roblox.com/t/publishing-to-users-under-16/4697842)) |
| 6 Jul 2026 | HEP definition relaxed; Roblox estimated 33% more new games would qualify |
| 16 Jul 2026 | Bar to stay in: 25 HEP over 60 days, down from 100 ([DevForum](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717)) |
| 19 Aug 2026 | 250 HEP ([DevForum](https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164)) |
| Docs, 25 Nov 2026 | 100 unique plays by HEP within 60 days, checked hourly |

The docs page is undated, and whether the 25 HEP floor still applies is not confirmed. Progress shows under Publish Settings, Manage Audience.

Publishing for all ages also needs ID verification, 2-step verification, the content questionnaire, and either two straight months of Plus or Premium or a refundable 1,000 Robux fee per game. Expedited review skips the HEP bar for 50,000 Robux, refundable, within 48 hours (current docs; a June post said 100,000) ([publishing docs](https://create.roblox.com/docs/en-us/production/publishing/publish-experiences-and-places)). Publishing for 16+ only needs an age-checked account at least 2 days old.

**Our read:** 100 qualifying plays in 60 days is 1.7 a day. Any game that people keep playing clears it; it mainly filters out games that only non-spenders try.

### Benchmarks

Roblox publishes no numeric targets. Its dashboard shows a "similar experiences" band from the 50th to the 90th percentile; in Roblox's example, a D1 band of 12.11% to 18.73% means half of similar games sit at or below 12.11% and one in ten reaches 18.73%. Bands cover retention, session time, ARPPU, ARPDAU, conversion and play-through rate, need 100+ daily users and do not affect ranking ([Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)). Roblox measures D7 on the 8th day and D30 on the 31st ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)).

The best public numbers are GameAnalytics' 2026 report: 500+ Roblox games that reached 1M+ monthly users, August 2025 to July 2026 ([GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox), [GameAnalytics](https://www.gameanalytics.com/reports/2026-roblox-report)). Mobile medians come from 16,000+ games with 1,000+ monthly users in 2025 ([GameAnalytics mobile](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks)).

| Metric (per game) | Roblox median | Roblox p75 / p90 | Roblox top 1% | Mobile median |
|---|---|---|---|---|
| D1 | 10.3% | 12.9% to 15.9% ("median to p75-p90" in GameAnalytics' tips) | 22.2% | about 22% |
| D7 | 1.6% | not known | 9.1% | just under 4% |
| D30 | 0.5% | not known | 4.7% | 0.68% to 0.79% |
| Session length | 9.8 min | 12.0 / 14.7 min | 21.1 min | 3.1 to 3.5 min |
| Sessions per player per day | 1.56 | p90 3.22 | 8.3 | not known |
| ARPPU | $0.70 | p90 $2.33 | $55.31 | not known |

3.80% of players spent anything in the year, down from 4.2% two years earlier. GameAnalytics calls the common "20% D1 is good" rule inflated. Caution: the Roblox sample only has games that reached 1M monthly users while the mobile sample takes any game with 1,000, and the two may define D1 differently.

**Our read:** out of 1,000 new players, a median game in that sample sees 103 return on day 1, 16 on day 7 and 5 on day 30; a top-1% game sees 222, 91 and 47. The gap grows from 2x on day 1 to 9x on day 30. Games separate on long-term retention.

### Servers and people

**Matchmaking.** Roblox drops full, private, reserved and closing servers, scores the rest from 0 to 1 on each signal, and sends the player to the highest weighted total ([Scoring docs](https://create.roblox.com/docs/en-us/matchmaking/scoring)).

| Signal | Default weight |
|---|---|
| Friends (or same IP) | 15 |
| Latency, text chat | 3 each |
| Occupancy (fuller scores higher: 2 of 8 is 0.25), play history, language | 2 each |
| Age gap, voice chat | 1 each |
| Device type | 0 |

Friends (15) outweigh all the rest together (14), so a player lands with a friend whenever there is room. Creators can change weights and add 2 custom signals ([Customize matchmaking](https://create.roblox.com/docs/en-us/matchmaking/customize-matchmaking)). Joining from an invite skips matchmaking entirely ([DevForum](https://devforum.roblox.com/t/updates-to-invites-joining-friends-just-got-easier/2729692)).

**Private and reserved servers.** Private servers can be free or a monthly Robux price and are free for Roblox Plus subscribers, with the creator still paid up to 100 Robux per subscriber a month ([Private servers](https://create.roblox.com/docs/en-us/production/monetization/private-servers)). Reserved servers are made in code by teleporting with a new ReservedServerId ([Teleport](https://create.roblox.com/docs/en-us/projects/teleport)). Default and maximum server sizes are not published; the top 300 charted games range from 1 to 200 players per server [data, Nov 2026].

**Loading.** Instance streaming is on by default for new places (StreamingMinRadius 64, StreamingTargetRadius 1024) ([Streaming](https://create.roblox.com/docs/en-us/workspace/streaming)). No official join-time figure exists.

**Chat.** Since 7 January 2026 every player needs an age check to chat. Bands are under 9, 9 to 12, 13 to 15, 16 to 17, 18 to 20 and 21+; each chats with its own and neighbouring bands, and under 9 needs parental consent ([Roblox newsroom](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat)). All player text goes through TextChatService; fixed preset phrases are allowed and must use Quick Words from May 2027 ([Chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines)).

**Voice.** Age-verified 13+, opt-in, spatial, and only in places capped at 100 players or fewer ([Voice chat](https://create.roblox.com/docs/en-us/chat/voice-chat)).

**Content labels** ([Content ratings](https://create.roblox.com/docs/en-us/production/promotion/content-ratings)):

| Label | Who can play |
|---|---|
| Minimal, Mild | Kids (5 to 8) and Select (9 to 15) once the game passes the gate, and everyone older |
| Moderate | Select (9 to 15) and 16+ |
| Content May Vary | Age-checked 16+ |
| Restricted | Age-verified 18+ |

Drawing or writing seen by others, media sharing and open hangouts are 16+; playable gambling is banned. Since 25 August 2026 a Kids and Select game may not combine a media feed, autoplay and a reward for watching ([DevForum](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188)). [Steal An Egg](../teardowns/steal-an-egg.md) was taken offline on 24 August over a video feed on its treadmill and returned without it ([StudioKrew](https://studiokrew.com/blog/?p=2016)).

### The chart on 25 November 2026

Live counts: Roblox public API, 25 Nov 2026 ([chart](https://apis.roblox.com/explore-api/v1/get-sort-content?sessionId=7f1c2b3a-1111-4222-8333-444455556666&sortId=top-playing-now&device=computer&country=all&cpuCores=8&maxResolution=1920x1080&maxMemory=8192&networkType=wifi), [games](https://games.roblox.com/v1/games?universeIds=10563114921,3317771874,2440500124,994732206,2753915549,383310974,1686885941)).

| # | Game | Playing | Created | Players per server |
|---|---|---|---|---|
| 1 | Steal An Egg | 843,938 | Jul 2026 | 7 |
| 2 | [Brookhaven RP](../teardowns/brookhaven.md) | 333,545 | Apr 2020 | 30 |
| 3 | [Blox Fruits](../teardowns/blox-fruits.md) | 305,008 | Jan 2019 | 12 |
| 4 | [Throw Food For Animals](../teardowns/throw-food-for-animals.md) | 238,007 | Sep 2026 | 5 |
| 5 | [Adopt Me!](../teardowns/adopt-me.md) | 179,211 | Jul 2017 | 35 |
| 6 | [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) | 175,901 | Mar 2025 | 25 |
| 7 | [RIVALS](../teardowns/rivals.md) | 163,502 | May 2024 | 40 |
| 8 | [Murder Mystery 2](../teardowns/murder-mystery-2.md) | 119,459 | Jan 2014 | 12 |
| 9 | Anime Crusaders X | 110,133 | May 2025 | 30 |
| 10 | [Pet Simulator 99](../teardowns/pet-simulator-99.md) | 110,060 | Feb 2022 | 10 |

- At least 12 of the top 40 were created in the last 12 months, and almost all cap servers at 1 to 10 players (Steal An Egg 7, Throw Food For Animals 5, Hyper Realistic Ragdoll 1, Throw a Seed 5, Clean The Ballpit! 6). In the evening count the one exception is 100 Miles Down the River, 44 days old with 20 per server [data, Nov 2026]. The 30 to 35 player games are all older than 18 months.
- On the 18 November chart of 99 games, the 35 created in the previous three months held 922,200 of 4,033,815 players: 22.9%. Games created in 2026 (42 of 99) held 37%. Only two of the top 10 were under three months old ([GGRecon](https://www.ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/)).
- In October 2026 the top 10 held 29% of players, down from about 34% in mid-September, and weekends averaged 14.54M concurrent against 9.73M on weekdays, 1.5 times as many ([Bloxodes](https://bloxodes.com/stats/reports/roblox-october-2026), a tracker). On 25 November the top 10 held 23% of the players in all 2,408 charted games at one moment [data, Nov 2026]: a different base from the tracker's monthly figure, so the two are not a trend.

| Game | Peak | Days from launch to peak | Now as share of peak |
|---|---|---|---|
| [Steal a Brainrot](../teardowns/steal-a-brainrot.md) | 25.4M, Oct 2025 | about 145 | 0.17% |
| [Grow a Garden](../teardowns/grow-a-garden.md) | 22.3M, 23 Aug 2025 | about 150 | 0.08% |
| Steal An Egg | 14.27M, 19 Sep 2026 (one tracker: 5.23M) | 56 | 5.8% |
| Escape Tsunami for Brainrots | 4.1M, Feb 2026 | about 60 | 0.09% |
| [Dead Rails](../teardowns/dead-rails.md) | 1.4M, Apr 2025 | about 105 | 1.1% |
| [Fisch](../teardowns/fisch.md) | 600K, Dec 2024 | about 270 | 13% |
| RIVALS | 964K, Apr 2026 | about 690 | 17% |

Peaks: [PocketGamer.biz](http://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players/), [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden), [StudioKrew](https://studiokrew.com/blog/?p=2016), and RoWatcher, a tracker that often reads low ([Escape Tsunami](https://rowatcher.com/games/9363735110/escape-tsunami-for-brainrots), [Dead Rails](https://rowatcher.com/games/7018190066), [Fisch](https://rowatcher.com/games/5750914919), [RIVALS](https://rowatcher.com/games/6035872082)). Days are our arithmetic from creation dates.

**Our read:** the viral loops peaked inside 60 to 150 days and kept under 6% of the peak. The games that kept 13% to 17% peaked after 9 to 23 months of updates.

### The whole chart in numbers

The repo's own snapshot of every public chart on 25 November 2026 ([data/ANALYSIS.md](../data/ANALYSIS.md)) counts players at about 18:23 UTC, four hours after the table above, so the same games show different counts (Steal An Egg 529,129 against 843,938). All rows are [data, Nov 2026].

| Measure | Value |
|---|---|
| Players needed for rank 50 / 100 / 300 | 27,134 / 17,099 / 6,429 |
| Top 100: median age; released in the last 6 months; over 5 years old | 528 days; 43%; 18% |
| Top 300: median age; released in the last 6 months; launched in 2026 | 98 days; 57%; 186 of 300 |
| Top 100 that published in the last 24 hours / 7 days | 58% / 93% |
| Simulation: share of top-300 games / of their players | 36% / 34% |
| Top Earning top 25 (computer): RPG / tower defense / Simulation | 9 (all Action RPG) / 3 / 5 |
| RPG slots in the Top Earning top 50: computer / high-end phone / low-end tablet | 10 / 5 / 1 |
| Players per server, top 300: median; Simulation; Survival and Action; Roleplay; Strategy | 15; 8; 20; 25; 30 |
| Like ratio, top 300: median / bottom tenth (p10) | 89% / 74% (Party & Casual median 73%) |

**Our read:** the earning list is not the playing list. RPG and tower defense games turn fewer players into more Robux, and the earning list changes with the device: on low-end tablets Simulation takes 17 of the top 50 earning slots and Roleplay 11. Benchmark a phone-first design against those genres.

## The rules (what this means for a design)

1. **Put the core action on screen inside 60 seconds.** Bounce is the second signal and its first bucket is under 60 seconds. See [05-first-session.md](05-first-session.md).
2. **Build the thumbnail, icon and title as a system.** PTR is the top signal, and no custom thumbnail means no Home recommendations. See [11-clips-and-packaging.md](11-clips-and-packaging.md).
3. **Give a reason to return on days 2, 3 and 7, and one for days 8 to 28.** Days 2 to 7 are scored as days played out of 6. See [08-retention.md](08-retention.md).
4. **Fit a full day's goals inside 60 minutes.** Playtime credit stops at 60 minutes per user per game per day. **Our read:** three 15-minute visits on three days earn more signal than one 3-hour visit.
5. **Do not buy rank with ads.** Ad-acquired players never count toward Recommended For You.
6. **Make friends land together.** Friends weigh 15 against 14 for everything else, and joins, invites and private servers count as co-play days. See [09-other-players.md](09-other-players.md).
7. **Plan the first 60 days for a 16+ audience.** Under-16s open up after 100 qualifying plays in 60 days (the bar was 500, then 250, this year). Budget the 1,000 Robux fee or two months of Plus.
8. **Pick the content label before building scary or social features.** Only Minimal and Mild reach ages 5 to 8; drawing, media sharing and open hangouts are 16+.
9. **Keep chat out of the core loop.** Chat needs an age check and stops at neighbouring age bands. Use preset phrases and visible actions for anything every player must do.
10. **Build for a 2 to 4 GB Android phone.** About 39% of players by our arithmetic. Small textures at 512x512 or less, minor ones under 256x256, streaming on ([Memory docs](https://create.roblox.com/docs/projects/performance-optimization/memory)).
11. **Change something original in title, thumbnail and place file.** Close copies are deprioritised, and protection goes to whoever added the original material first.
12. **Ship on Saturday.** Home traffic peaks on Saturdays, and the October weekend average was 1.5 times the weekday one. See [13-live-ops.md](13-live-ops.md).

## How to do it

1. **Read the chart first.** Run `python tools/snapshot.py` and `python tools/analyze.py`, open [data/ANALYSIS.md](../data/ANALYSIS.md), and note server size, age and players for the five games closest to yours. Compare snapshots taken at the same hour.
2. **Fix the platform choices** in [kit/templates/one-page-design.md](../kit/templates/one-page-design.md): content label, server size, whether chat is needed, which features are 16+.
3. **Test on a 2 or 3 GB Android phone**, or the Performance Simulator at 2 or 3 GB with high background load ([DevForum](https://devforum.roblox.com/t/test-graphics-and-memory-on-lower-end-devices-with-the-performance-simulator/4979313)). Compare frame rate at minute 1 and minute 15.
4. **Log each onboarding step** with `LogOnboardingFunnelStepEvent` so drop-off at 60 and 180 seconds shows by step ([Funnel events](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)). Use [kit/templates/first-session-script.md](../kit/templates/first-session-script.md).
5. **Publish to 16+ first** and check the HEP count in Manage Audience daily.
6. **Compare with your own band** once you pass 100 daily users, then use [14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md) to go from a bad number to a fix.

## Checks

| Check | Pass |
|---|---|
| Core action reachable | 60 seconds or less after the player gains control |
| Custom thumbnail | Uploaded before the first public day |
| Return reasons | At least one each for day 2, day 3, day 7 and day 14 |
| Daily goals | Fit inside 60 minutes |
| Friends | A joining friend lands in the same server; an invite button exists |
| Low-end phone | 15 minutes on a 2 to 4 GB Android phone with no crash; minute-15 frame rate within 10% of minute 1 (our threshold) |
| Content label | Chosen, and every feature fits it |
| Chat | Every core action works for a player who cannot chat |
| D1 after 100 DAU | At or above the dashboard band's lower end |
| Like ratio (non-party game) | 74% or more; below that is the bottom tenth of the top 300 [data, Nov 2026] |

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Home impressions near zero | Default thumbnail, or a reduced-exposure banner | Upload a custom 16:9 thumbnail; check the banner and appeal |
| Good D1, impressions fall in week 2 | Poor days 2 to 7 | Add reasons to return on days 2, 3 and 7 |
| Many ad players, no rise in Home traffic | Ad players are excluded from the signals | Stop paying for rank; fix first-session bounce |
| Under-16 audience never opens | Under 100 HEP plays in 60 days, or verification missing | Check Manage Audience; finish ID and 2-step verification |
| Friends split across servers | Friends weight lowered, or a lobby teleports players one by one | Keep Friends at 15; teleport parties together |
| Ranks below a similar older game | Copied title, art or place file | Change the title, art and at least one mechanic |

## Sources

- Roblox Creator Docs (undated, read 25 Nov 2026): [Discovery](https://create.roblox.com/docs/production/promotion/discovery), [Discovery FAQ](https://create.roblox.com/docs/discovery-faq), [Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard), [Retention](https://create.roblox.com/docs/en-us/production/analytics/retention), [Funnel events](https://create.roblox.com/docs/en-us/production/analytics/funnel-events), [Kids and Select](https://create.roblox.com/docs/en-us/production/publishing/kids-and-select), [Publishing](https://create.roblox.com/docs/en-us/production/publishing/publish-experiences-and-places), [Content ratings](https://create.roblox.com/docs/en-us/production/promotion/content-ratings), [Matchmaking scoring](https://create.roblox.com/docs/en-us/matchmaking/scoring), [Customize matchmaking](https://create.roblox.com/docs/en-us/matchmaking/customize-matchmaking), [Private servers](https://create.roblox.com/docs/en-us/production/monetization/private-servers), [Teleport](https://create.roblox.com/docs/en-us/projects/teleport), [Streaming](https://create.roblox.com/docs/en-us/workspace/streaming), [Memory](https://create.roblox.com/docs/projects/performance-optimization/memory), [Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware), [Chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines), [Voice chat](https://create.roblox.com/docs/en-us/chat/voice-chat), [Experience events](https://create.roblox.com/docs/en-us/production/promotion/experience-events).
- Roblox DevForum: [Recommended For You, 15 Jun 2026](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575), [Publishing to users under 16](https://devforum.roblox.com/t/publishing-to-users-under-16/4697842), [Kids and Select launch](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717), [HEP 250](https://devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164), [Media feeds](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188), [Top Playing Now](https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809), [Discover test](https://devforum.roblox.com/t/testing-an-enhanced-discover-page-top-charts-and-new-sorts/2954676), [Invites](https://devforum.roblox.com/t/updates-to-invites-joining-friends-just-got-easier/2729692), [Performance Simulator](https://devforum.roblox.com/t/test-graphics-and-memory-on-lower-end-devices-with-the-performance-simulator/4979313).
- Roblox newsroom: [Discovery, 15 Jun 2026](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox), [Chat age checks, 7 Jan 2026](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat).
- Results: [GamesBeat Q3 2026](https://gamesbeat.com/roblox-grows-revenues-in-q3-by-16-but-stock-falls-in-after-hours-trading/), [GamesBeat RDC 2026](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/), [GGRecon](https://www.ggrecon.com/articles/roblox-daily-players-fall-q3-2026/), [MediaPost](https://www.mediapost.com/publications/article/419134/), [Gaming Amigos](https://www.gamingamigos.com/post/roblox-q3-2026) (secondary, unverified).
- Benchmarks: [GameAnalytics 2026 Roblox](https://www.gameanalytics.com/reports/2026-roblox-report) via [GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox); [GameAnalytics 2026 mobile and PC](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks).
- Chart: Roblox public API, 25 Nov 2026; [GGRecon, 18 Nov 2026](https://www.ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/); [Bloxodes, Oct 2026](https://bloxodes.com/stats/reports/roblox-october-2026); [StudioKrew](https://studiokrew.com/blog/?p=2016); peak sources listed under the decay table.
