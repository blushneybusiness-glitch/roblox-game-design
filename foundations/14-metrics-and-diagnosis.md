# Metrics and diagnosis

Open this page after launch, when you have numbers and need to know what to change first. It lays the player's path out as one funnel with the benchmark for each step, shows how to read other games' funnels for free, maps symptoms to first fixes, and says how many players a test needs. The design advice for each step lives on the page the funnel table links.

## What is known

### The funnel

Metric names are the ones Roblox's Creator Dashboard and discovery documentation use ([Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard), [Discovery docs](https://create.roblox.com/docs/production/promotion/discovery), [Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)). Public benchmarks are the GameAnalytics 2026 report on 500+ Roblox games with 1M+ monthly users ([GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)); the caveats are below.

| Stage | Dashboard metric | Benchmark that exists | Owned by |
|---|---|---|---|
| Seen | Impressions (Home Recommended For You, sponsored) | None published | [11-clips-and-packaging.md](11-clips-and-packaging.md) |
| Clicked | Play Through Rate (under Acquisition); ad click-through in Ads Manager | Similar-experience band in your dashboard only. Ad CTR "around 1 to 1.5%" appears only in a search snippet, unverified ([DevForum](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265)) | [11-clips-and-packaging.md](11-clips-and-packaging.md) |
| First minute | First-play bounce, under 60 s and 61 to 180 s (a ranking signal); New User First Session Retention chart ([Engagement docs](https://create.roblox.com/docs/production/analytics/engagement)) | None published | [05-first-session.md](05-first-session.md) |
| First session | Average Session Time | Median 9.8 min, p75 12.0, p90 14.7, top 1% 21.1 | [04-core-loop.md](04-core-loop.md) |
| Next day | Day 1 Retention | Median 10.3%, top 1% 22.2% | [08-retention.md](08-retention.md) |
| Days 2 to 7 | Day 7 Retention (measured on the 8th day); play days out of 6 (ranking signal) | Median 1.6%, top 1% 9.1% | [06-progression-and-economy.md](06-progression-and-economy.md), [08-retention.md](08-retention.md) |
| Days 8 to 28 | Day 30 Retention (31st day); Day 8 to 28 play days (ranking signal) | Median 0.5%, top 1% 4.7% | [13-live-ops.md](13-live-ops.md), [09-other-players.md](09-other-players.md) |
| Pays | Conversion Rate (share of daily users who pay), ARPPU, ARPDAU | 3.80% of players paid anything in a year; ARPPU median $0.70, top 1% $55.31 | [12-monetization.md](12-monetization.md) |

The D7 and D30 charts stay empty for the latest 7 and 30 days ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)). The first-session ranking signals count only players who arrived from Recommended For You, never those from ads, search, friends or social links ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).

### Benchmarks

**What Roblox shows.** Each retention KPI, session time, ARPPU, ARPDAU, conversion and play-through rate carries a "similar experiences" band from the 50th to the 90th percentile; in Roblox's example a D1 band of 12.11% to 18.73%. It needs 100+ daily users, updates daily and is not used for ranking ([Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)). Details are in [02-the-platform.md](02-the-platform.md).

**GameAnalytics.** The funnel-table medians come from games that reached 1M monthly users, so 10% D1 is level with successful games; GameAnalytics calls the "20% D1 is good" rule inflated ([GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)). Its 2025 report, a vendor sample, links session length to D1 ([GameAnalytics](https://www.gameanalytics.com/cn/reports/2025-roblox-report)):

| Average session | D1 median | D1 p90 |
|---|---|---|
| 0 to 3 min | 4.31% | 9.25% |
| 7 to 12 min | 7.91% | 11.55% |
| 13 to 18 min | 10.24% | 14.96% |
| 19 to 24 min | 11.46% | 18.20% |
| 25+ min | 10.76% | 18.86% |

**Our read:** D1 roughly doubles from the shortest sessions to 13 minutes and then flattens. Past about 20 minutes, a longer first session buys little next-day return, and Roblox stops counting playtime at 60 minutes per player per day anyway ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)).

**Two studio rules.** Zach Letter, CEO of WonderWorks (SpongeBob Tower Defense, shipped in 6 weeks by 4 people), says that being at the 90th percentile across all the dashboard metrics means a hit ([Deconstructor of Fun](https://www.deconstructoroffun.com/blog/how-to-build-a-real-business-on-roblox-in-2026)). Alexander Hicks, co-founder of Twin Atlas (World // Zero, Creatures of Sonaria), uses about 3 new players per hour to sustain 1 concurrent player ([Naavik](https://naavik.co/podcast/launching-original-ip-on-roblox/)).

**Our read** on the Hicks rule: one concurrent player is 60 player-minutes per hour, so 3 arrivals an hour means each new player adds about 20 minutes of play over their whole life in the game, about two median sessions. A target of 100 CCU needs about 300 new players an hour, 7,200 a day. Our snapshot gives a second ratio: daily unique players are a median 21.6 times current CCU (p25 17.1, p75 28.4), inferred from badge win rates [data, Nov 2026] ([data/ANALYSIS.md](../data/ANALYSIS.md)).

### Reading the first-session retention chart

Roblox calls it the New User First Session Retention chart. It shows the share of new players still playing a given number of minutes after their first join, with the previous period drawn next to the current one, and Roblox's example reads the 5-minute point week on week ([Engagement docs](https://create.roblox.com/docs/production/analytics/engagement)). The circulating 95% / 87% / 65% at 30 s / 1 min / 5 min yardstick has no written source ([05-first-session.md](05-first-session.md)). Roblox's advice: instrument every first-session step and fix the largest drop-off ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention.md)).

Find the minute with the steepest fall. On a fresh account on a phone, play with a stopwatch to that minute and write down what is on screen, what the player was just given and what they are asked to do. One public case: a mining game lost about 30% of players in the first minute and half within 2 minutes; replies blamed a cluttered HUD and mines too small to find. No after-data was posted ([DevForum](https://devforum.roblox.com/t/my-day-1-retention-is-awful-23-losing-half-my-players-in-under-2-minutes-what-am-i-doing-wrong-with-onboarding/4186434)).

### Free data on other games: the badge endpoint

Roblox's public badge endpoint needs no login:

```
https://badges.roblox.com/v1/universes/<universeId>/badges?limit=100&sortOrder=Asc
```

Each badge carries `awardedCount`, the number of unique users who ever earned it, and a created date (example: [Mega Easy Obby](https://badges.roblox.com/v1/universes/1261193936/badges?limit=100)). `winRatePercentage` is a fraction between 0 and 1; our snapshot finds it consistent with past-day awards divided by past-day players, which Roblox does not document [data, Nov 2026]. A game with more than 100 badges spans several pages. The universe ID is the number the games endpoint takes (`games.roblox.com/v1/games?universeIds=`); `tools/snapshot.py` collects badges for every charted game.

Divide each step by the first step and you have the game's progress funnel.

| Game | Chain | Share of the base reaching each step |
|---|---|---|
| [Doors](../teardowns/doors.md) | Joined 536.7M, survive Rush, survive Seek, Figure, finish the Hotel | 55%, 19%, 9.5%, about 2.7% ([API](https://badges.roblox.com/v1/universes/2440500124/badges?limit=100&sortOrder=Asc)) |
| [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) | Day 10 (409M), 30, 100, 500 | 100%, 50.7%, 21.4%, 2.6% ([API](https://badges.roblox.com/v1/universes/7326934954/badges?limit=100&sortOrder=Asc)) |
| [Dead Rails](../teardowns/dead-rails.md) | 10 km (123M), 20 km, 50 km, 80 km, beat Tesla | 100%, 64%, 33%, 27%, 12% ([API](https://badges.roblox.com/v1/universes/7018190066/badges?limit=100&sortOrder=Asc)) |
| A Dusty Trip | Joined 368.7M, 1 km, 5 km, 20 km | 24.9%, 3.6%, 0.6% ([API](https://badges.roblox.com/v1/universes/5650396773/badges?limit=100&sortOrder=Asc)) |
| [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md) | 1 kill (171M), 10, 100, 1,000, 10,000 | 54%, 19%, 5.8%, 0.64% ([API](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100)) |
| Mega Easy Obby | Stage 5 (294M), 50, 100, 200, 825; prestige 1 | 54%, 37%, 21%, 0.45%; 3% ([API](https://badges.roblox.com/v1/universes/1261193936/badges?limit=100)) |
| Natural Disaster Survival | 1 disaster survived (447M), 10, 100, 1,000 | 29%, 2.5%, 0.06% ([API](https://badges.roblox.com/v1/universes/65241/badges?limit=100&sortOrder=Asc)) |
| Driving Empire | Own 5 cars (82.4M), 10, 20, 50, 100 | 32%, 9.5%, 0.9%, 0.2% (our division) ([API](https://badges.roblox.com/v1/universes/1202096104/badges?limit=100)) |
| [Murder Mystery 2](../teardowns/murder-mystery-2.md) | Level 10 (313M), 20, 50, 100 | 53%, 16.5%, 5.4% [data, Nov 2026] |
| [Fisch](../teardowns/fisch.md) | Welcome badge (123M), 50, 1,000, 10,000 catches | 23%, 9.5%, 3.5% [data, Nov 2026] |

Four limits:

1. **Counts are lifetime** and mix the launch crowd with today's players. Fisch's 50-catch step is 23.4% lifetime but 36.4% of yesterday's welcome awards [data, Nov 2026]; the past-day column in our snapshot is today's funnel.
2. **Late badges break the base.** Bee Swarm Simulator's welcome badge has 2.9M awards, its 1-million-honey badge 19.5M [data, Nov 2026]. Check created dates first.
3. **Counts have no clock.** They say how many reached day 30, not how long it took.
4. **Many games have none.** 40% of the top 300 have zero badges [data, Nov 2026].

**Our read** on what the ten funnels show: the first real milestone keeps between a quarter and a half of joiners; each 10x step after that keeps a third to a half; long ladders flatten once players are committed (99 Nights day 50 to 100 keeps 63%, Dead Rails 50 to 80 km keeps 82%). If your own first step keeps under a quarter, the step is too early or too hard.

## The diagnosis table

Find the earliest stage where you are below the 50th percentile band, then the row. Rows with a linked case come from sourced cases; the rest are **Our read:**.

| Stage | Symptom | Likely cause | First fix | Read |
|---|---|---|---|---|
| Seen | Almost no Home impressions | No custom thumbnail, or the reduced-exposure banner is on (copycat metadata, mismatched title, leading with giveaways) ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)) | Upload a custom 16:9 thumbnail; check the banner; appeal through Support | [02](02-the-platform.md) |
| Seen | Home impressions fall while total players rise during an ad campaign | Ad-acquired players are not shown the game again in Recommended For You; Roblox says this is not a penalty ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)) | Nothing to fix; judge the game on organic players | [11](11-clips-and-packaging.md) |
| Clicked | Many impressions, low play-through | Thumbnail and title promise nothing a player wants. Personalization lifted play-through 8.5% to 12% on average ([DevForum](https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689)). A retitle from "Sell Your Data" to "Hack a Business", with a new thumbnail, took ad CTR from 1.54% to 3.27%; unnamed speaker, cause not isolated ([transcript](https://sozai.app/transcript/roblox-sponsored-ads-explained/)) | Five clearly different thumbnails for 7 days; a verb-and-thing title | [11](11-clips-and-packaging.md) |
| Clicked | Normal CTR, almost no plays | The image is not the game. One day of ads: icon art 852 clicks, 2 plays; gameplay art 466 clicks, 37 plays ([DevForum](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265)) | Show real gameplay in every thumbnail | [11](11-clips-and-packaging.md) |
| Clicked | High clicks, like ratio under 70% | Bait title; the bait clones sit at 59% to 70% against 85% to 97% for hits ([slop/03](../slop/03-quality-bar.md)) | Plain title that says what the game does | [11](11-clips-and-packaging.md) |
| First minute | D1 and playtime drop when ads run | Ad traffic is colder. One shooter: D1 about 3% with ads against 5% to 8% without, playtime 11 to 12 min against 28 to 30, 45% of new players stopped at the Deploy button ([DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)) | Split every chart by traffic source before changing the game; then fix the step where ad players stop | [11](11-clips-and-packaging.md) |
| First minute | A third or more leave before 60 s | The promised object is not on screen, or the HUD hides it ([mining case](https://devforum.roblox.com/t/my-day-1-retention-is-awful-23-losing-half-my-players-in-under-2-minutes-what-am-i-doing-wrong-with-onboarding/4186434)) | Promised object at the spawn; cut the HUD to six items | [05](05-first-session.md) |
| First minute | Leaves cluster at 61 to 180 s | **Our read:** the first reward came and the second did not | Make purchases 2 and 3 as fast as purchase 1 | [04](04-core-loop.md) |
| First minute | A cliff at one funnel step | The step can fail or needs reading. Trihex Studios watches one event, "spawned a house"; a drop in it flags a UI problem ([GameAnalytics](https://www.gameanalytics.com/blog/advice-from-the-devs-built-community-on-roblox)) | Rig the step to succeed the first time; replace text with a pointer | [05](05-first-session.md) |
| First minute | Phones bounce more than computers | Memory: about 65% of players are on Android, 60% of those on 2 to 4 GB ([Roblox docs](https://create.roblox.com/docs/performance-optimization/test-on-hardware)) | Test a full server on a 3 GB Android phone | [10](10-feel-and-feedback.md) |
| First session | Average session under 7 minutes | Dead time in the loop; 0 to 3 min sessions go with 4.31% median D1 (table above) | Fill the loop table with measured seconds; treat every wait | [04](04-core-loop.md) |
| First session | Steady until minute 5 or 6, then a drop | **Our read:** the opening ended and no long goal replaced it | Put the next zone or rebirth requirements on screen before minute 5 | [05](05-first-session.md) |
| First session | Overall D1 and playtime fall right after a popular update | A bigger, less committed crowd lowers the averages. One tycoon went from 18 min and 8% to 10% D1 to 12 min and 4% to 6% ([DevForum snippet](https://devforum.roblox.com/t/sudden-drop-on-playtime-and-retention-with-update/3880064)) | Compare cohorts by source and join date before reverting | [08](08-retention.md) |
| Next day | Long first sessions, D1 under 6% | **Our read:** nothing pulls the player back: no clock, nothing growing offline | One 5-minute clock and offline growth before anything else ([slop/04](../slop/04-build-it.md)) | [08](08-retention.md) |
| Next day | D1 fine on weekdays, "falls" on Monday | Traffic peaks on Saturdays ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)); the tracked slop hits peaked at 5 to 36 times weekday level ([slop/02](../slop/02-why-it-holds.md)) | Compare the same weekday week on week | [13](13-live-ops.md) |
| Days 2 to 7 | D1 near the median, D7 under 1% | The ladder runs out or stops showing progress. Roblox's advice for D7: grant an item at each level so time-to-level is measurable ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention.md)) | Log time-to-level; add the next ladder step | [06](06-progression-and-economy.md) |
| Days 2 to 7 | Players stop at the first rebirth | The reset takes too much. Steal a Brainrot changed its rebirth from taking the whole base to taking only the required units ([wiki](https://stealabrainrot.fandom.com/wiki/Rebirth)) | Take only what the rebirth needs; first rebirth at 20 to 40 min | [06](06-progression-and-economy.md) |
| Days 8 to 28 | Slow decline over weeks | Updates stopped. Dungeon Quest (last update 17 Oct) and Swordburst 3 (Feb) had 51 and 15 players ([games API](https://games.roblox.com/v1/games?universeIds=848145103,4093155512)); Mega Easy Obby, untouched since Jan 2024, has 68 ([obby notes API](https://games.roblox.com/v1/games?universeIds=1261193936)) | A fixed weekly update day with something new to collect | [13](13-live-ops.md) |
| Days 8 to 28 | Low co-play days | No invite prompts or private servers; joins, invites and private servers are what counts ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)) | Invite prompt at a win or a loss; free or cheap private servers | [09](09-other-players.md) |
| Days 8 to 28 | A social reward floods the game with spam | Adopt Me's friend-based currency made players spam friend requests, and many moved to private servers ([Roblox newsroom](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform)) | Reward playing together, never the act of adding a friend | [09](09-other-players.md) |
| Any | Under-16 reach lost, or a feature must come out | A policy change. Steal An Egg's treadmill video feed broke the 25 Aug 2026 rule on reward-driven feeds; the game was pulled briefly and returned without it ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)). Royale High retired a diamond-stake fountain in 2019 because it resembled gambling ([wiki](https://royale-high.fandom.com/wiki/Fountain)) | Check the line before building, and design waits as part of the game | [15](15-the-line.md) |
| Pays | Earnings flat, conversion low, prices hard-coded | Prices too high for the audience. Price optimization raised median earnings 4%; Slap Battles gained over 15% with lower prices ([DevForum](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738)) | Remove hard-coded prices and enrol in Managed Pricing | [12](12-monetization.md) |
| Pays | Wallet balances keep rising, purchases slow | Sources outrun sinks; Roblox says sources minus sinks should sit near zero ([Economy docs](https://create.roblox.com/docs/en-us/production/analytics/economy-events)) | Add a sink at the level where balances pile up | [06](06-progression-and-economy.md) |

## Testing a change

**One stat per update, the number written first.** Write in [kit/templates/update-plan.md](../kit/templates/update-plan.md): the worst stat, the change, "moves from A to B", and the date to read it. Two changes in one update make both unreadable.

**The data delay.** Benchmarks update daily, sales reports every 48 hours ([Analytics docs](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)). D1 for players who joined on the day of a change is known two days later, D7 eight days later, D30 thirty-one days later. Ranking uses moving windows and staged signals ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)). Roblox staff say to leave thumbnail tests for 7 days ([DevForum](https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689)), and Managed Pricing tests run about 3 weeks ([DevForum](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738)). **Start with:** read any retention change after 7 full days, so every weekday appears once.

**How many players a test needs.** For a rate p measured on n players, the standard error is √(p(1−p)/n). At 95% confidence the true value lies within 1.96 standard errors. Our arithmetic for a 10% rate (D1) and a 50% rate (still present at 5 minutes):

| Players (n) | 10% rate: ± points | 50% rate: ± points | Smallest gap between two versions of this size you can trust, at 10% |
|---|---|---|---|
| 500 | 2.6 | 4.4 | 3.7 |
| 1,000 | 1.9 | 3.1 | 2.6 |
| 5,000 | 0.8 | 1.4 | 1.2 |
| 20,000 | 0.4 | 0.7 | 0.6 |

So a 10% D1 measured on 1,000 new players is really somewhere between about 8.1% and 11.9%. Telling 10% from 12% needs about 1,900 players per version to reach 95% confidence half the time, and about 3,800 per version to catch the gap 4 times in 5. **Our read:** at 300 new players a day, a 2-point D1 test takes about two weeks. Small games should test big changes, or first-session steps, where rates sit near 50% and results arrive on day one. Roblox Experiments runs real A/B splits ([analytics essentials](https://create.roblox.com/docs/en-us/production/game-design/analytics-essentials)): one or two variants of a config value against a control, for 14 to 60 days, tracking day 1 and day 7 retention, playtime, session time and spending, with a funnel step as the goal if you choose one. Roblox shows the minimum detectable effect before the start and says games under 1,000 daily users may not get useful data ([Experiments docs](https://create.roblox.com/docs/en-us/production/experiments)). Before-and-after comparisons mix in the weekday and the traffic source. The routine for both is in [kit/stats-to-plan.md](../kit/stats-to-plan.md), step 7. Staff say thumbnail personalization results may mean nothing under about 1,000 daily users ([DevForum](https://devforum.roblox.com/t/live-now-personalize-your-thumbnails-to-attract-more-users/3257233)).

## Instrumenting

- **Funnel events.** Roblox offers one-time funnels (`LogOnboardingFunnelStepEvent`) and recurring ones (`LogFunnelStepEvent`), up to 10 funnel tabs, server-side only, in published games. A skipped step counts the earlier steps as complete ([Funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)).
- **One event per row** of [kit/templates/first-session-script.md](../kit/templates/first-session-script.md), numbered in the order players do them. Because a skipped step counts the earlier steps as complete, a step added in the middle takes the number of its place and the steps after it move up. A mid-flow step given the last number would mark every earlier step done. Note the date of the change and read the funnel from that date; the dashboard shows a warning when a date range crosses a step change ([Funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)).
- **A zoom funnel** when one step loses the most players: three extra steps between it and the step before, logged as a funnel of its own, to tell "did not find it" from "had to wait" from "tried and failed" ([kit/stats-to-plan.md](../kit/stats-to-plan.md), step 4).
- **A recurring funnel** for the daily loop: join, collect, first purchase of the session, clock check.
- **Slice by traffic source.** Acquisition splits Home recommendations, Continue Play, Today's Picks, Friends, Search, Teleport and sponsored ([Acquisition docs](https://create.roblox.com/docs/production/analytics/acquisition)).
- **Slice by device.** The Filter By menu has Platform (computer, phone, tablet, console, VR) and OS. A filter applies to every chart on every analytics page until you turn it off, and a chart that cannot use it greys it out ([Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)). A funnel filter looks at the device a player had at the funnel's first step ([Funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)). The performance dashboard shows frame rate, crash rate, out-of-memory exits and memory by device ([Performance docs](https://create.roblox.com/docs/en-us/production/analytics/performance)); read it next to the funnel.
- **Read by join day.** The Retention page ends with a table of each join day's return over its first 10 days and each join week's over 10 weeks, with playtime, payer conversion and revenue per user ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)). It is the cleanest way to set the days before an update against the days after.
- **Log the long milestones** (first rebirth, day 10) as badges, so your funnel compares with the table above.

## The rules

1. **Fix the earliest weak stage first.** Ranking weighs play-through and bounce first, a strong D8 to 28 is "very unlikely" after a poor D1 and D2 to 7, and Roblox says to fix core gameplay before monetization ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
2. **Compare with the band, then with yourself.** GameAnalytics medians come from 1M-user games; week-on-week change in your own cohorts is the number to act on.
3. **Aim for the 90th percentile on every signal** (Letter's rule). Games strong in both retention and monetization may get broader distribution ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
4. **One stat per update, expected number written first, read after 7 days.**
5. **Split by traffic source before changing the game.** Ad players are excluded from ranking signals and retained at about half the rate in the shooter case.
6. **Under 1,000 players per version, trust only gaps of 3 points or more.**
7. **Your first milestone keeps at least a quarter of joiners** (**Our read**, from the ten funnels).

## How to do it

`python tools/funnel.py <stats.json>` does steps 1 and 2 from a file of your numbers and adds what your traffic can prove. [kit/templates/stats-intake.md](../kit/templates/stats-intake.md) says where each number is in the dashboard, and [kit/stats-to-plan.md](../kit/stats-to-plan.md) is the full routine with a worked example.

1. Fill the funnel table with your numbers and your dashboard band; circle the earliest stage below the 50th percentile.
2. Find its row in the diagnosis table and play to the minute or step it names.
3. Pull two competitors' badge funnels and compare their first milestone with yours.
4. Write one line in the update plan, check the player count against the testing table, ship, read after 7 days, keep or revert.

## Checks

- [ ] The funnel table is filled for every stage, with the dashboard band next to each number.
- [ ] Every row of the first-session script has a funnel event, numbered in the order players do the steps.
- [ ] Retention is read per traffic source.
- [ ] The update plan has one stat, an expected number and a read date at least 7 days after release.
- [ ] Each version in a test has at least 1,000 new players, or the expected gap is 3 points or more.
- [ ] Two competitors' badge funnels have been pulled and their created dates checked.
- [ ] The first milestone keeps at least 25% of joiners.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| A change "worked", then the number went back | Saturday read against a Tuesday, or 300 players | Compare 7 full days; check the testing table |
| A competitor's step is over 100% | Badge added after launch | Use badges created with the base |
| The D7 chart shows a fresh collapse | The latest 7 days are not filled yet | Ignore the last 7 days of D7, the last 30 of D30 |
| Funnel charts break after a new step | The new step sits mid-flow with the last number, or the date range crosses the change | Number steps in play order; read from the day of the change |
| Revenue work while D1 is under the band | Wrong stage | Fix the earliest weak stage first |

## Sources

Roblox Creator Docs (analytics, discovery, funnel events), GameAnalytics via GameDev Reports, Deconstructor of Fun, Naavik, DevForum threads and wikis, all linked inline. Badge funnels: Roblox public API, 25 Nov 2026, and [data/ANALYSIS.md](../data/ANALYSIS.md). The sample-size table, the arrival-rate arithmetic and rows marked **Our read** are our own.
