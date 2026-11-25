# Retention: this session, tomorrow, weeks two to four

This page answers three questions for any genre: why a player stays for the rest of this session, why they come back tomorrow, and why they are still here in weeks two to four. Open it when Day 1 is fine but Day 7 collapses, or before you design timers, daily rewards, events or a rebirth ladder. The first five minutes are on [05-first-session.md](05-first-session.md); updates and seasons on [13-live-ops.md](13-live-ops.md).

## What is known

### How long players stay

GameAnalytics measured 500+ Roblox games with at least 1M monthly players (Aug 2025 to Jul 2026) and 16,000+ mobile games (2025) ([GA 2026 Roblox](https://www.gameanalytics.com/reports/2026-roblox-report), [GA 2026 mobile and PC](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks)).

| Metric | Roblox median | Roblox top 1% | Mobile median | Mobile top 1% |
|---|---|---|---|---|
| D1 | 10.3% | 22.2% | about 22% | 64-68% |
| D7 | 1.6% | 9.1% | just under 4% | over 25% |
| D30 | 0.5% | 4.7% | 0.68-0.79% | 13-15% |
| Session length, per game | 9.8 min | 21.1 min | 3.1-3.5 min | over 22 min |
| Sessions per player per day, per game | 1.56 | 8.30 | not given | about 14 |

The Roblox sample only includes games that reached 1M monthly players, so a new game probably sits below these medians. The per-player median session (7.28 min) is a different metric; do not mix the two.

Our arithmetic: the top 1% beat the median 2.2 times on D1, 5.7 times on D7 and 9.4 times on D30. **Our read:** the best games win most in weeks two to four. (Each row is ranked separately, so the top D1 game is not always the top D30 game.)

D1 by average session length, GameAnalytics 2025 (vendor data, [report](https://www.gameanalytics.com/cn/reports/2025-roblox-report)):

| Average session | 0-3 min | 7-12 min | 13-18 min | 19-24 min | 25+ min |
|---|---|---|---|---|---|
| D1 median | 4.31% | 7.91% | 10.24% | 11.46% | 10.76% |
| D1 90th percentile | 9.25% | 11.55% | 14.96% | 18.20% | 18.86% |

**Our read:** D1 rises with session length up to about 20 minutes, then stops. This is a correlation, not proof that longer sessions cause returns.

Average sessions reported by trackers (estimates from public data):

| Genre | Game: minutes | Source |
|---|---|---|
| Anime RPG | [Blox Fruits](../teardowns/blox-fruits.md) 24.3, King Legacy 22.9 | [Rotrends](https://rotrends.com/game/994732206), [Rotrends](https://rotrends.com/game/1451439645) |
| Battlegrounds | JJS 16.2, [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md) 12.2 | [Rotrends](https://rotrends.com/game/3508322461), [Rotrends](https://rotrends.com/game/3808081382) |
| Roguelite | Pixel Blade 7.5 | [Rotrends](https://rotrends.com/game/6161049307) |
| Horror | [Forsaken](../teardowns/forsaken.md) 19.75, [Doors](../teardowns/doors.md) 9.68 | [Rolimons](https://www.rolimons.com/game/18687417158), [Rolimons](https://www.rolimons.com/game/6516141723) |
| Survival | [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) 16.13, [Dead Rails](../teardowns/dead-rails.md) 14.87, Natural Disaster Survival 9.19 | [Rolimons](https://www.rolimons.com/game/79546208627805), [Rolimons](https://www.rolimons.com/game/116495829188952), [Rolimons](https://www.rolimons.com/game/189707) |
| Grow and steal | [Grow a Garden](../teardowns/grow-a-garden.md) about 21, [Steal a Brainrot](../teardowns/steal-a-brainrot.md) about 9 | [RoVitals](https://rovitals.com/game/126884695634066), [RoVitals](https://rovitals.com/game/109983668079237) |
| RNG | Anime Dice 32.9 | [Rotrends](https://www.rotrends.com/game/10708913337/Anime-Dice) |

**Our read:** session length follows one unit of play. A Pixel Blade run takes a few minutes; Grow a Garden's 21 minutes is four 5-minute restocks.

### What the platform counts

Since 15 June 2026, Recommended For You scores each player over 28 days ([DevForum](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575), [Discovery docs](https://create.roblox.com/docs/production/promotion/discovery), [FAQ](https://create.roblox.com/docs/discovery-faq)). Most important first:

| Signal | What counts |
|---|---|
| 1. Play-through rate | Plays after seeing the game in Recommended For You |
| 2. First-play bounce | Negative: leaving the first session in under 60 s, or 61-180 s |
| 3. Play days per user | Averaged for Day 1, Days 2-7 (out of 6 days) and Days 8-28 |
| 4. Playtime per user | Capped at 60 minutes per user, per game, per day |
| 5-8 | Co-play days (joins, invites, private servers), qualified sessions, spend days, Robux spent |

Signals are per-user averages from organic players only; ad-acquired players are excluded. The FAQ calls a strong Days 8-28 "very unlikely" when Day 1 and Days 2-7 are poor. Story and finite games are not penalised for lower long-term retention. Roblox's own chart counts D7 as the 8th day and D30 as the 31st ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)).

Our arithmetic: 9.8 minutes x 1.56 sessions is about 15 minutes per player per day, a quarter of the 60-minute cap. **Our read:** for almost every game, more score comes from one more play day than from more minutes on a day already played.

### Where players stop

Lifetime badge award counts (Roblox public API, 25 Nov 2026). Badges added after launch, and players who skip steps, make the ratios indicative only.

| Game (genre) | Base | Share of base reaching each milestone | What it shows |
|---|---|---|---|
| Doors, horror run ([badges](https://badges.roblox.com/v1/universes/2440500124/badges?limit=100&sortOrder=Asc)) | Joined, 536.7M | Survive Rush 55%, Seek 19%, escape the Hotel 2.7% | 1 joiner in 37 clears the first floor |
| 99 Nights, survival run ([badges](https://badges.roblox.com/v1/universes/7326934954/badges?limit=100&sortOrder=Asc)) | Survive 10 days, 408.7M | Day 20 69%, 30 51%, 50 34%, 100 21%, 250 7.4% | Step survival rises from 69% (day 10 to 20) to 94% (day 90 to 100) |
| Dead Rails, train journey ([badges](https://badges.roblox.com/v1/universes/7018190066/badges?limit=100&sortOrder=Asc)) | Travel 10 km, 123.3M | 20 km 64%, 50 km 33%, 80 km 27%, boss 12% | 82% of those at 50 km reach 80 km |
| A Dusty Trip, driving distance ([badges](https://badges.roblox.com/v1/universes/5650396773/badges?limit=100&sortOrder=Asc)) | Welcome, 368.7M | 1 km 25%, 5 km 3.6%, 20 km 0.6% | 1 km to 5 km keeps 14%, the steepest step here |
| Mega Easy Obby, stages ([badges](https://badges.roblox.com/v1/universes/1261193936/badges?limit=100)) | Stage 5, 293.6M | 50: 54%, 100: 37%, 200: 21%, 450: 7.9%, 825: 0.45% | About 10% lost per 5 stages early, 2-5% later |
| The Strongest Battlegrounds ([badges](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100)) | First kill, 171.4M | 10 kills 54%, 100 19%, 1,000 5.8%, 10,000 0.64% | Each 10x step keeps about a third |
| Blox Fruits, seas ([badges](https://badges.roblox.com/v1/universes/994732206/badges?limit=100)) | Second Sea, 99.1M | Third Sea 62% (King Legacy 45.5%, [badges](https://badges.roblox.com/v1/universes/1451439645/badges?limit=100)) | A late gate still loses 38-55% |
| Driving Empire, cars owned ([badges](https://badges.roblox.com/v1/universes/1202096104/badges?limit=100)) | Own 5, 82.4M | 10: 32%, 20: 9.4%, 50: 0.9%, 100: 0.17% | Each doubling loses about two-thirds |
| +1 Speed Keyboard Escape, incremental ([badges](https://badges.roblox.com/v1/universes/9584852943/badges?limit=100)) | Welcome, 358.6M | First rebirth 42.4% | The first reset sits in the first session or two |

**Our read:** the first wall takes a third to a half of the players who reach it. After it each step loses less: 99 Nights and Dead Rails keep over 80% per step past day 50 or 50 km. Most retention work is getting players over the first wall.

Counted from the welcome badge instead, the first wall is steeper. The repo's snapshot of the top 300 ([data/ANALYSIS.md](../data/ANALYSIS.md), section 10) found 15 games with both a welcome badge and a numbered chain [data, Nov 2026]:

| Measure | Value |
|---|---|
| Welcome-badge holders who reach the first milestone | median 24%, range 1.3% to 89% |
| ... who reach the middle milestone | usually 1% to 7% |
| First milestone set low | Squid Game X, 5 wins: 29%; 100 Days at Sea, survive 5 days: 69% |
| First milestone set high | Clean The Ballpit!, 5 stars: 1.3%, then 10 stars: 0.01% |
| Level chain, [Murder Mystery 2](../teardowns/murder-mystery-2.md) | level 10 to 20 keeps 53%, then 64%, 67%, 73% per 10 levels; 5.4% of level-10 players reach 100 |
| Long survival chain, 100 Days at Sea | 2.2% of first-timers reach day 90 |
| Top 300 games with no badges at all | 40% (median 2 badges per game) |

The base is lifetime awards, so a badge added after launch distorts it; Tower Defense Simulator's 89% is an upper bound for that reason.

**Our read:** about three in four new players never reach the first milestone, so put it inside the first session, where the low-set games put it. When each step costs about twice the play time of the last, expect 50% to 75% to carry on to the next one, with the steepest drop first.

Welcome-badge holders per lifetime visit are a public sign of repeat play [data, Nov 2026]: 2% to 3% for long-lived grinders (Fisch, Fish It!, Anime Crusaders X), 14% to 31% for party and round games, 44% for Clean The Ballpit! at 24 days old. **Our read:** a low ratio means many visits per player. Check a rival's ratio before copying its loop.

### The mechanisms, with their numbers

| Mechanism | Numbers found |
|---|---|
| Two goals on screen | [Pet Simulator 99](../teardowns/pet-simulator-99.md) ranks 1-3 need 13, 25 and 32 stars ([wiki](https://pet-simulator.fandom.com/wiki/Ranks_(Pet_Simulator_99))). [Bee Swarm Simulator](../teardowns/bee-swarm-simulator.md)'s first bear pays a Silver Egg after 6 quests, Gold after 9 more, Diamond after 20 more ([wiki](https://bee-swarm-simulator.fandom.com/wiki/Black_Bear)). Roblox advises short, mid and long-term goals on screen ([docs](https://create.roblox.com/docs/production/game-design/onboarding.md)). |
| Clocks and restocks | Grow a Garden: seeds 5 min, eggs 30, event shop 60, deals 24 h ([wiki](https://growagarden.fandom.com/wiki/Seed_Shop), [Bloxodes](https://bloxodes.com/wiki/grow-a-garden/shops)). Steal a Brainrot guarantees a Legendary within 5 min, a Mythic within 15 ([wiki](https://stealabrainrot.fandom.com/wiki/Red_Carpet)). Pet Simulator 99: 8+ free gift pads on 30 min to 5 h cooldowns, bigger drops on longer ones ([wiki](https://pet-simulator.fandom.com/wiki/Free_Items_(Pet_Simulator_99))). |
| Offline growth | Grow a Garden grows offline ([Roblox API](https://games.roblox.com/v1/games?universeIds=7436755782)). Steal a Brainrot's wiki gives two figures, about 50% of the online rate or about 3% capped at 5 h ([Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash)). A Kongregate analyst called Egg, Inc.'s 2-hour cap "likely a mistake" ([GDC Europe 2016](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507), mobile). |
| Daily caps | [Adopt Me](../teardowns/adopt-me.md) 300 Bucks a day, 500 with a paid item ([wiki](https://adoptme.fandom.com/wiki/Bucks)). [Jailbreak](../teardowns/jailbreak.md)'s last season system 80 XP a day ([wiki](https://jailbreak.fandom.com/wiki/Seasons)). [BedWars](../teardowns/bedwars.md) first 5,000 XP x2.5, cap 52,000 ([wiki](https://robloxbedwars.fandom.com/wiki/Player_Level)). |
| Timed gifts in a session | Bubble Gum Simulator INFINITY: gifts at 2, 3, 4, 5, 7.5, 15, 30, 60, 90 min, the last two at 20x luck ([wiki](https://bgs-infinity.fandom.com/wiki/Playtime)). Roblox's Engagement Rewards package: example thresholds 10, 30, 60 min ([docs](https://create.roblox.com/docs/en-us/resources/feature-packages/engagement-rewards)). |
| Login streaks | Adopt Me 25, 50, 100, 200, 300 Bucks on days 1-5, then the cycle restarts. Bloxburg $100, $200, $500, $1,000, B$20; a gap over 48 h resets ([wiki](https://welcome-to-bloxburg.fandom.com/wiki/Daily_Reward)). Midnight Racing Tokyo ¥100,000 to ¥1,000,000 by day 6, a free car on day 7 ([Earnaldo](https://earnaldo.com/blog/midnight-racing-tokyo-free-robux-guide)). Roblox's package: a durable item after 7 straight days. |
| The weekly event | Saturday 21 Nov 2026: six hits peaked at 4.6 to 36 times their weekday level ([RoVitals](https://rovitals.com/)). [Throw Food For Animals](../teardowns/throw-food-for-animals.md) events start 6 AM Pacific, some 30-60 min ([Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals)). 99 Nights: update party Saturdays 1 PM EST ([wiki](https://99-nights-in-the-forest.fandom.com/wiki/Update_Log)). |
| Collections | Driving Empire above. Find the Markers: 377 marker badges added in batches of 5-11, about 1,300 players after five years with no passes (Roblox public API, 25 Nov 2026, [badges](https://badges.roblox.com/v1/universes/3056160040/badges?limit=100)). |
| Friends | Default matchmaking weighs friends 15 against 14 for all other signals together ([docs](https://create.roblox.com/docs/en-us/matchmaking/scoring)). Grow a Garden +10% sell value per friend, up to +40% ([wiki](https://growagarden.fandom.com/wiki/Sheckles)). Doors +0.1x Knobs per friend, up to +0.3x ([wiki](https://doors-game.fandom.com/wiki/Knobs)); 40% of joiners hold its run-with-a-friend badge. Adopt Me's 100-Buck bonus tasks need a friend ([wiki](https://adoptme.fandom.com/wiki/Task_Board)). |
| Reset ladders that take weeks | Blox Fruits 80-120 h to max level without passes (community estimate, [bloxmeta](https://bloxmeta.gg/games/blox-fruits/guides/fastest-leveling-guide)). 99 Nights: a 600-diamond class is about 17 days of the full daily routine ([wiki](https://99-nights-in-the-forest.fandom.com/wiki/Diamonds)). Dead Rails: all classes and trains 4,645 bonds, 36 to 465 runs ([wiki](https://deadrails.fandom.com/wiki/Bonds)). |

Our arithmetic:

- Adopt Me's 5-day login cycle pays 675 Bucks, 2.25 days of capped earnings: a bonus on top of play.
- Bloxburg's day 4 and Midnight Racing Tokyo's day 6 pay 10 times day 1, and both ladders end on something different in kind.
- Blox Fruits at one 24-minute session a day takes 200 to 300 days, far past the 28-day window.

**Evidence on daily rewards is thin.** One small game's A/B test found a daily reward did not raise playtime per player; others in the thread claimed streaks help, without data ([DevForum, 2025](https://devforum.roblox.com/t/do-daily-rewards-actually-keep-players-retention/3556728)). Measured effects of streaks, timers or playing with friends on retention: not known.

### The psychology, and how strong it is

None of these studies are about Roblox.

| Effect | What was found | Strength |
|---|---|---|
| Endowed progress | Car-wash cards needing 8 paid washes: 34% finished with 2 free stamps, 19% without (300 cards) ([Nunes and Drèze 2006](https://msbfile03.usc.edu/digitalmeasures/jnunes/intellcont/Endowed%20Progress%20Effect-1.pdf)). The effect depended on the reason given for the head start. | Single field study |
| Goal gradient | Café stamp card: gaps between purchases shrank about 20% toward the reward, then slowed again after it ([Kivetz, Urminsky and Zheng 2006](https://business.columbia.edu/sites/default/files-efs/pubfiles/1200/goalgradient.pdf)). | Single study, strong field data |
| Loss aversion | Losses weigh 1.955 times gains (95% interval 1.82-2.10) in one 2024 meta-analysis ([Brown et al.](https://www.aeaweb.org/doi/10.1257/jel.20221698)); 1.31 (1.10-1.53) in another, with 6 of 19 studies significant ([Walasek et al.](https://wrap.warwick.ac.uk/185745)). A 2025 paper is titled "Loss aversion is not robust" ([IDEAS](https://ideas.repec.org/a/eee/joepsy/v107y2025ics0167487025000133.html)). Use 1.3 to 2, not 2.25. | Replicated, smaller and contested |
| Zeigarnik | A 2025 meta-analysis found no memory advantage for unfinished tasks, but a tendency to resume them ([Ghibellini and Meier](https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html)). | Memory effect failed; resuming holds |
| Near-miss | On a simplified slot machine, near-misses felt worse than misses yet raised the wish to play on, only when the player controlled the gamble ([Clark et al. 2009](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neuron.2008.12.031&resultType=core&format=json)). | Single study, gambling research |
| Variable-ratio rewards | Established in animal learning; "why games hook people" claims come without sources. | Folklore for games |

**Our read:** the best-supported tools show progress: a bar, a head start, the next goal in view. Loss framing is a moderate lever and the one regulators watch hardest in children's products. Near-miss design comes from slot machines; see [15-the-line.md](15-the-line.md).

## The rules

1. **End every session with one thing unfinished and one thing growing.** A bar at 60-90% or a restock under 5 minutes away, plus something that keeps running while the player is gone. *Why:* the urge to resume replicates.
2. **Show the next goal within the reward animation**, in the same 1-2 seconds. *Why:* the goal-gradient slowdown after a reward.
3. **Start every goal partly filled.** **Start with:** 2 of 10, with the reason on screen ("for your first catch"). *Why:* 34% against 19%.
4. **Run three clocks.** **Start with:** 5 minutes on the HUD, 30 or 60 minutes for something rarer, one daily reset at a fixed UTC hour. *Why:* Grow a Garden's set, and its 21-minute session.
5. **Pay offline, capped to cover a night.** **Start with:** up to 8 hours counted at 25-50% of the online rate, so a night pays 2 to 4 hours of online earnings (the payout [02-why-it-holds.md](../slop/02-why-it-holds.md) uses). Timers (crops, eggs) finish at full speed. Nothing is lost offline. *Why:* a 2-hour cap was called a mistake; a night is 8 hours.
6. **Reward before any request.** Within 10 seconds of spawning, the returning player collects what grew and reads one line on what happened. No shop or pass prompt before that.
7. **Login ladder: a gain, ending on an object.** **Start with:** 5-7 days, the last cash day 10 times day 1, day 7 an item that cannot be bought; a missed day restarts quietly. *Why:* losses weigh at most about 2 times gains, and loss-framed streaks are what regulators flag.
8. **Cap daily free earnings at what a 20-30 minute player earns.** *Why:* Adopt Me, Jailbreak and BedWars cap the day; the platform counts days, and ignores minutes past 60. **Our read:** a cap moves effort from hours into days.
9. **One live hour a week.** **Start with:** Saturday, same hour, 30-60 minutes, a lobby countdown, one item that exists only then. *Why:* 4.6 to 36 times the weekday peak.
10. **Give each friend a number.** **Start with:** +10% per friend in the server, up to +30-40%, shown by the currency counter, never behind Robux. *Why:* Grow a Garden and Doors; co-play days are a signal.
11. **First reset in 20-40 minutes; the full ladder longer than 28 days.** *Why:* 42% of +1 Speed's joiners have rebirthed; a ladder finished in a week leaves nothing for Days 8-28. Each reset gives something to do, something to show and a number.
12. **Reward collection doublings.** **Start with:** milestones at 5, 10, 20, 50 and 100, each bigger, since each doubling loses about two-thirds.

## How to do it

1. **Design the end of a session.** On your [core-loop-table.md](../kit/templates/core-loop-table.md), mark minute 10 (the median session) and minute 20. At each, write what is unfinished (a bar and its percentage) and what is growing (a timer and its output). An empty cell needs rule 4 or 5.
2. **Design the return.** Script the first 30 seconds of session two like [first-session-script.md](../kit/templates/first-session-script.md): second 0 spawn, 5 the grown thing in view, 10 collected, 15 login reward, 20 next goal. Move every pop-up after second 20.
3. **Design days 8 to 28.** On [update-plan.md](../kit/templates/update-plan.md), build four Saturday events before launch. Run your ladder through `python tools/pacing.py`; the last tier must land after 28 days at 15-30 minutes a day, or add a second ladder (collection, ranked season, mastery).
4. **Measure where players stop.** Add a badge or funnel step per milestone (`LogFunnelStepEvent`, [funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)), read counts from `https://badges.roblox.com/v1/universes/<id>/badges?limit=100` as in [data/ANALYSIS.md](../data/ANALYSIS.md) section 10, and fix the step that loses most first. Compare D1 and D7 with the tables above; see [14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md).

## Checks

| Check | Pass |
|---|---|
| Session end | At minute 10: a bar at 60%+ and a timer under 5 minutes |
| Return | Something collected within 10 s of spawning, before any prompt |
| Offline | 8 hours away pays; nothing lost offline |
| Next goal | A goal bar appears within 2 s of every reward |
| Head start | Multi-step goals open 10-20% filled, with a reason |
| Login ladder | 5-7 days, ends on an object, no loss message |
| Weekly | Four events built before launch, fixed day and hour |
| Friends | A free, visible per-friend bonus |
| Long ladder | Last tier needs 28+ days at 15-30 minutes a day |
| Funnel | First big milestone keeps 50%+ of the step before (TSB 54%, Dead Rails 64%, 99 Nights 69%) |
| First milestone | Reachable in the first session; 25%+ of welcome-badge holders earn it (top-300 median 24%) [data, Nov 2026] |
| Benchmarks | D1 at least 10.3%, D7 at least 1.6% |

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Good D1, D7 near zero | Nothing new after day 2 | Weekly event and a 28+ day ladder (rules 9, 11) |
| Long sessions, few return days | All value in one sitting | Daily cap and fixed reset (rules 4, 8) |
| Log in, claim, leave | The login reward is the only reason | A clock or grown thing next to the claim (rule 1) |
| Returners quit in the first minute | Pop-ups before anything is collected | Reward before request (rule 6) |
| Players stop after rebirth 1 | Rebirth only gives "x2" | Add an action, a visible change and a number |
| One milestone loses most players | A cost or difficulty wall | Lower that step or add a goal halfway |
| Players quit after a missed streak | Reset framed as a loss | Restart quietly; keep streak rewards small (rule 7) |

## Sources

Every source is linked inline where it is used: GameAnalytics 2026 and 2025 reports; Roblox Discovery docs, FAQ and the 15 Jun 2026 DevForum post; Roblox retention, funnel, onboarding, Engagement Rewards and matchmaking docs; Roblox public badge endpoints (25 Nov 2026); Rolimons, Rotrends and RoVitals; game wikis, Bloxodes, bloxmeta and Earnaldo; the DevForum daily-reward thread; Pecorella, GDC Europe 2016 (mobile); and the psychology papers in the table.

Next: [09-other-players.md](09-other-players.md).
