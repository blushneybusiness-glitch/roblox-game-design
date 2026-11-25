# Live ops: update rhythm, events, seasons

Open this page before launch, to plan the weeks after it, and again when the weekly numbers slide. It covers what an update contains, how often the leaders ship and on which day, live events with real times and lengths, season sizes, daily rewards, and what a small team can carry. The output is a filled [kit/templates/update-plan.md](../kit/templates/update-plan.md).

## What is known

### An update, to a player, is new things to get

What the leaders put in one update:

| Game | Typical content of one update | Source |
|---|---|---|
| [Brookhaven](../teardowns/brookhaven.md) | 1 to 2 houses, 1 to 3 vehicles, 5 to 12 props, 1 to 6 tools; a new location or system about every second week; a pass or paid bundle every 2 to 3 weeks (wiki-based count) | [Brookhaven wiki Changelog](https://brookhaven.fandom.com/wiki/Changelog) |
| Garden Tower Defense | 2 limited-stock units, each with a promo code, plus a mode or system, sometimes an event | [GTD wiki Update Logs](https://garden-tower-defense.fandom.com/wiki/Update_Logs) |
| [Dress to Impress](../teardowns/dress-to-impress.md), small drop | 3 items, a mini-quest, a code | [DTI wiki Update Log 2026](https://dti-dress-to-impress.fandom.com/wiki/Update_Log/2026) |
| Dress to Impress, seasonal drop | 58 to 64 items (Spring and Summer 2026), a new map or lobby, minigames, a new pass season | same |
| [Steal a Brainrot](../teardowns/steal-a-brainrot.md) | New units, often a limited event mutation; rebirth caps raised in steps | [SAB wiki Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log) |

Two practitioners on why: Zach Letter of WonderWorks designs each weekly update to produce 3 to 4 creator videos ([Naavik](https://naavik.co/podcast/the-creator-led-studio-playbook/)). Janzen Madsen of Splitting Point says players forgive minor bugs but leave if updates are slow ([GameAnalytics, a vendor piece](https://gameanalytics.com/blog/splitting-point-how-field-trip-z-got-45m-players/)).

### Who ships weekly, and when

| Game | Day and hour | Count | Source |
|---|---|---|---|
| Steal a Brainrot | Saturday | Update 1 on 31 May 2025 to Update 75 on 14 Nov 2026: 75 updates in 77 weeks | [SAB wiki Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log) |
| [Steal An Egg](../teardowns/steal-an-egg.md) | Saturday; events start 7 to 8 AM Pacific | Weekly since 22 Aug 2026 | [Bloxodes](https://bloxodes.com/wiki/steal-an-egg), [StudioKrew](https://studiokrew.com/blog/?p=2016) |
| [Throw Food For Animals](../teardowns/throw-food-for-animals.md) | Saturday, 6 AM Pacific (one at 9 AM) | Weekly from 31 Oct 2026 | [Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals) |
| [Grow a Garden](../teardowns/grow-a-garden.md) | Saturday | 2026 events in 3 to 4 weekly parts (Beanstalk, Fall Market, Halloween, Anubis) | [GAG wiki Update Log](https://growagarden.fandom.com/wiki/Update_Log) |
| Garden Tower Defense | Saturday | v1.0.0 on 4 Jun 2025 to v1.77.0 on 14 Nov 2026: 77 versions in about 528 days, one per 6.9 days | [GTD wiki Update Logs](https://garden-tower-defense.fandom.com/wiki/Update_Logs) |
| Volleyball Legends | Saturday, 11:30 AM Eastern | Update 95 on 7 Nov 2026; created 17 Dec 2024, about 99 weeks earlier (our arithmetic) | [RBLXGuide](https://rblxguide.com/games/volleyball-legends) |
| Brookhaven | Friday, 6 PM Eastern | 20 weekly entries from 19 Jun to 6 Nov 2026, no week missing | [Brookhaven wiki Changelog](https://brookhaven.fandom.com/wiki/Changelog) |
| [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) | Weekly, with a 45-minute "Update Party" with players before each update | not known | [DevForum](https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940) |

On 25 Nov 2026, 14 of 17 top games checked had published within the previous two days ([games API](https://games.roblox.com/v1/games?universeIds=10563114921,7709344486,7436755782)). A publish stamp shows any deploy, not content size.

The repo's snapshot of every public chart that day ([data/ANALYSIS.md](../data/ANALYSIS.md), section 4) gives the same picture at scale [data, Nov 2026]:

| Slice | Median days since last publish | Within 1 day | Within 7 days | Within 30 days | Over 90 days |
|---|---|---|---|---|---|
| Top 50 | 0.9 | 56% | 92% | 98% | 2% |
| Top 100 | 0.8 | 58% | 93% | 99% | 1% |
| Top 300 | 0.8 | 56% | 91% | 99% | 0% |

**Our read:** publishing at least weekly is the norm at the top, so it does not set a game apart. Not publishing for a month sets it apart the other way.

What Saturday does to player counts:

| Measure | Value | Source |
|---|---|---|
| Platform, October 2026 | Weekend average 14.54M against weekday 9.73M: weekends 49% higher (our arithmetic) | [bloxodes](https://bloxodes.com/stats/reports/roblox-october-2026) |
| Steal An Egg | Weekends average 56.5% more players than weekdays | [RoVitals](https://rovitals.com/game/107778070777162) |
| Six slop hits on Saturday 21 Nov 2026 | Saturday peak 5 to 36 times the week's normal level | [RoVitals](https://rovitals.com/); full table in [slop/01-anatomy.md](../slop/01-anatomy.md) |
| How long a spike lasts | Grow a Garden fell from 21.3M to 7.6M within an hour and 5.5M within two | [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden) |

### The counter-examples

| Game or source | Rhythm | Result or reason | Source |
|---|---|---|---|
| [RIVALS](../teardowns/rivals.md) | Numbered updates: 10 on 28 Feb 2025, 15 on 26 Sep 2025, 20 on 24 Apr 2026, 25 about 14 Nov 2026. 15 updates in 89 weeks, one about every 6 weeks (our arithmetic) | Peaked about 23 months after launch; 17% of peak today. Trackers put the peak at 964K (April 2026) or 967K (14 Feb 2026) | [Bloxguides](https://bloxguidesgg.com/games/rivals), [RoWatcher](https://rowatcher.com/games/6035872082), [Rolimons](https://www.rolimons.com/game/73956553001240) |
| Dress to Impress | 8 log entries in 16 weeks (Jul to Oct 2026); a big seasonal drop every 11 to 14 weeks | Cheap mini-drops fill the gaps between seasons | [DTI wiki](https://dti-dress-to-impress.fandom.com/wiki/Update_Log/2026) |
| Roblox's retention guide | Smaller updates to existing mechanics every 2 to 4 weeks; larger features every 2 to 3 months | Roblox's documented advice | [Retention doc](https://create.roblox.com/docs/en-us/production/analytics/retention.md) |
| Nathan Clemens (24 games, 850M+ sessions) | Fridays, every 2 to 3 weeks; he dropped weekly | His choice for his studio | [Naavik](https://naavik.co/podcast/mastering-the-roblox-meta/) |

And the two counter-examples in the other direction, where updating did not hold the game:

- Steal a Brainrot and Grow a Garden still publish every day or two and sit at 42K and 18K on a weekday morning, 0.17% and 0.08% of their peaks (Roblox public API, 25 Nov 2026).
- Karinderya and Anime Dice shipped weekly through their first quarter and still fell 90% to 99% ([earnaldo](https://earnaldo.com/blog/karinderya), [bloxodes](https://bloxodes.com/wiki/anime-dice)).

### When updates stop

| Game | Last update | Players | Source |
|---|---|---|---|
| Anime Defenders | No numbered update after Update 9 on 18 Dec 2024 | 377,836 peak (21 Jul 2024) to 188 | [Anime Defenders wiki](https://anime-defenders.fandom.com/wiki/Updates), [Rolimons](https://www.rolimons.com/game/17017769292) |
| "KICK FREE BLOCK (X999)" | Updated for 5 days in Aug 2026 | 1,256 | Roblox public API, 25 Nov 2026 |
| "Steal Anime!" | Stopped after 2 months (3 Aug 2025) | 457 | same |
| "Steal a Pet" by BIG Games | 6 Feb 2026 | 7 | same |
| Makeup Mania! | 21 Nov 2026; description still says "new content coming soon"; no ladder or pass found | 89, created 25 Sep 2026 | same |
| Build the Pyramid! | 25 Oct 2026, 31 days before the snapshot; created 3 Sep 2026 | 435, yet still rank 281 in Top Earning on computer | [data, Nov 2026] |

The Anime Defenders cause is not stated by any source; an IP problem is also possible. For Build the Pyramid! one snapshot shows the stalled publishing and the low count together, not which caused which. More dead clones are in [slop/03-quality-bar.md](../slop/03-quality-bar.md).

### The live event

| Part | What the games do | Source |
|---|---|---|
| Day | Saturday for every slop hit above; Friday for Brookhaven | tables above |
| Hour | 6 to 9 AM Pacific (Throw Food 6 AM, Steal An Egg 7 to 8 AM, one Jonas Brothers event 8 to 9 AM) | [Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals), [Bloxodes](https://bloxodes.com/wiki/steal-an-egg) |
| Length | Throw Food's admin sessions: 1 hour, 30 minutes, 1 hour, then a 27-hour Thanksgiving event. Grow a Garden's "Watering Wednesday": 30 minutes, 3:00 to 3:30 PM Pacific | [Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals), [Bloxodes](https://bloxodes.com/wiki/grow-a-garden) |
| What attendees get | Steal An Egg's Admin Abuse: boosted spawns and luck. Steal a Brainrot: exclusive characters. Grow a Garden: weekly exclusive items that must be claimed while online | [StudioKrew](https://studiokrew.com/blog/?p=2016), [Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot), [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden) |
| A clock inside the event | Steal An Egg's King Turkey appears at :15 and :45 past every hour for 5 minutes; hits pay Feathers, top three get 500, 300 and 150 extra; Feathers buy a 1.25x speed boost (400) up to an event egg (22,500) | [Bloxodes Turkey guide](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide) |
| A limited item whose power rises in small steps | Steal a Brainrot's 12 limited mutations from Jun 2025 to Oct 2026: x2, x4, x6, x7, x7.5, x8.5, x9, x10, x11, x12, x13, x14. They return only through admin events or reruns | [Bloxodes mutations](https://bloxodes.com/wiki/steal-a-brainrot/mutations) |
| A countdown | Grow a Garden's wiki shows the next update countdown (28 Nov 2026); Dress to Impress rotates its Weekly Boutique every Saturday at 11 AM Eastern | [GAG wiki](https://growagarden.fandom.com/wiki/Update_Log), [rblxguide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide) |

**Our read** on the mutation ladder: the first steps doubled (x2 to x4), then every later one added only 0.5 to 1. The gaps between them were 3 to 10 weeks (our arithmetic from the dates). Each new item is the best one, so attending matters, but no event makes last month's item worthless. One listed date (25 Jul 2025) was a Friday by our calendar check, so read "Saturdays" as "almost always Saturdays".

What failed: Steal a Brainrot tried an hourly "Admin Machine", which its wiki judges a failure; its seasonal events now run every 2 hours on weekdays and every hour at weekends ([SAB wiki](https://stealabrainrot.fandom.com/wiki/Hourly_Events)). Dress to Impress crashed in the first minutes of a three-hour limited code item in December 2024 ([Wikipedia](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game))).

Platform-wide events in 2026:

| Event | Dates | Shape | Effect seen | Source |
|---|---|---|---|---|
| The Hunt: Roblox 20 | 17 to 28 Sep 2026; hub opened 9 AM Pacific | 20 portals, one per year since 2006; finishing all unlocks 20 more games; limited UGC rewards | [Jailbreak](../teardowns/jailbreak.md) 30,608 on 19 Sep (4.9K now); Lumber Tycoon 2 26,956 on 26 Sep | [DevForum](https://devforum.roblox.com/t/join-the-hunt-roblox-20/4875900), [bloxodes Sept](https://bloxodes.com/stats/reports/roblox-september-2026) |
| The Hollow | 22 Oct to 2 Nov 2026; opened 2 PM Pacific | 9 horror games, a new monster each day, live finale 31 Oct, limited avatar items | not known | [DevForum](https://devforum.roblox.com/t/the-hollow-new-platform-wide-survival-event-for-halloween/4948535) |
### Seasons and passes

| Game | Tiers | Length | Price | How you earn tiers | Source |
|---|---|---|---|---|---|
| RIVALS Season Pass | 70 (free track 69 rewards) | 10 weeks without paying (our arithmetic) | Tier skip 99 R$ flat; all 70 for 6,999. Pass price not known | 1 tier per 25 duel round wins or 20 minutes played; capped at 7 tiers a week | [RIVALS wiki](https://robloxrivals.fandom.com/wiki/Season_Pass) |
| [BedWars](../teardowns/bedwars.md) Battle Pass | 50 levels | Earlier seasons 8 to 16 weeks; Halloween 2026 was 4 weeks (23 Oct to 20 Nov) | 799 R$; 300 R$ per level, 15,000 for all 50 | Pass gives +20% XP; 5 themed passes in 2026 | [BedWars wiki](https://robloxbedwars.fandom.com/wiki/Battle_Pass) |
| Dress to Impress Baddie Pass | Usually 30, 40 in Halloween 2026 | 8 to 16 weeks (Summer 2026: 4 Jul to 6 Sep, 9 weeks) | Free track; Diamond Pass 299; VIP 799 unlocks VIP tiers; 1 skip 199, 3 skips 499 | Daily tasks 150 XP each; XP doubled above tier 10 | [rblxguide](https://rblxguide.com/games/dress-to-impress/updates/baddie-pass-guide), [developer products API](https://apis.roblox.com/developer-products/v2/universes/5203828273/developerproducts?limit=100) |
| [Epic Minigames](../teardowns/epic-minigames.md) Epic Pass | not known | 56 days, starting automatically at 00:00 UTC on 1 Mar, 1 Jun, 1 Sep, 1 Dec | not known | Stars from daily and weekly challenges; unspent stars become 5 coins each | [Epic Pass wiki](https://typical-games.fandom.com/wiki/Epic_Pass) |
| Volleyball Legends | not known | Season 20 arrived with Update 95: about 5 weeks per season (our arithmetic) | not known | not known | [RBLXGuide](https://rblxguide.com/games/volleyball-legends) |

Roblox ships a Season Pass and Engagement Rewards feature package (beta, March 2025) with settable price, season length, XP and rewards ([DevForum](https://devforum.roblox.com/t/beta-new-feature-packages-season-pass-engagement-rewards/3579550)).

**Our read** on the pass numbers: a weekly tier cap (RIVALS: 7) makes the season length a design choice instead of a race, and it makes the pass a weekly return reason for 10 weeks. Skips are priced so that buying the whole pass costs 8 to 19 times the pass itself (BedWars 15,000 against 799; RIVALS 6,999 against an unknown pass price), so skips sell one or two tiers at the end of a season, not the season.

### Daily and playtime rewards

| Game | Schedule | Source |
|---|---|---|
| Epic Minigames | Playtime gifts of 15 coins at 5 min, 30 at 20 min, 45 at 40 min, reset at midnight UTC; a Community Chest of 30 coins every hour; 3 daily missions at 30 coins each; Play Rewards every 5 min up to 60 min | [Typical Games wiki](https://typical-games.fandom.com/wiki/Epic_Minigames) |
| [Adopt Me!](../teardowns/adopt-me.md) | Daily reward 25, 50, 100, 200, 300 Bucks on days 1 to 5, then the cycle restarts; a daily earning cap of 300 Bucks (500 with a paid item); 4 daily tasks, 3 at 25 Bucks plus a prize and a friend task at 100 | [Adopt Me wiki: Bucks](https://adoptme.fandom.com/wiki/Bucks), [Task Board](https://adoptme.fandom.com/wiki/Task_Board) |
| Welcome to Bloxburg | $100, $200, $500, $1,000, then B$20 on day 5; claimable about every 23 hours; a gap over 48 hours resets the streak; streak trophies at 7, 14 and 30 days pay $10,000, $30,000 and $75,000 plus B$20 | [Bloxburg wiki](https://welcome-to-bloxburg.fandom.com/wiki/Daily_Reward) |
| Dress to Impress | 15 Cash on day 1 plus 15 per consecutive day (105 on day 7, 420 in the first week); a rewarded ad multiplies a day's reward by 1.5 | [rblxguide](https://rblxguide.com/games/dress-to-impress/updates/how-to-get-money-guide) |
| RIVALS | 3 daily tasks paying 6 Keys a day in total; free daily login rewards | [RIVALS wiki: Tasks](https://robloxrivals.fandom.com/wiki/Tasks) |
| [Anime Vanguards](../teardowns/anime-vanguards.md) | Challenges reset every 30 minutes, 24 hours and 7 days, capped at 20 completions a day | [AV wiki](https://animevanguards.fandom.com/wiki/Gamemodes) |

Evidence on whether they work is thin. One small game's A/B test of a daily reward did not raise total playtime per player ([DevForum, 2025](https://devforum.roblox.com/t/do-daily-rewards-actually-keep-players-retention/3556728)). Roblox reports that a free item at the end of an obby level gave +12.5% playtime and +5.3% D1 ([DevForum](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276)).

**Our read:** Roblox's recommendation system counts playtime only up to 60 minutes per player per day ([DevForum](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441)). Epic Minigames' Play Rewards stop at exactly 60 minutes. Playtime gifts past an hour pay the player for time that earns the game nothing in discovery. Play days do count, which is what the 5-day ladders buy.

### Codes and milestones

| Kind | Examples | Source |
|---|---|---|
| Active codes at once | Brookhaven 70; Berry Avenue 279; Dress to Impress 26, each a free item | [Bloxodes Brookhaven](https://bloxodes.com/wiki/brookhaven-rp), [Bloxodes Berry Avenue](https://bloxodes.com/wiki/berry-avenue-rp), [rblxguide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide) |
| One code per drop | Dress to Impress "KATSEYE", "PROUD", "10BILLION"; Garden Tower Defense one code per limited unit; Anime Dice RELEASE then UPDATE1 to UPDATE4 (2 to 10 spins) | [DTI wiki](https://dti-dress-to-impress.fandom.com/wiki/Update_Log/2026), [GTD wiki](https://garden-tower-defense.fandom.com/wiki/Update_Logs), [allthings.how](https://allthings.how/anime-dice-full-guide-for-roblox-update-4/) |
| Milestone codes | Karinderya 50KCCU and 2MVISITS; The Forge 90KCCU plus a weekly admin-event code; BloxNG "next code at 40K likes"; Drag Drive next code at 225,000 likes | [allthings.how](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/), [bloxodes](https://bloxodes.com/wiki/the-forge), Roblox public API descriptions, 25 Nov 2026 |

A reward for joining an outside community server is a moderation risk: one game with nearly 200M visits was auto-moderated for "Scamming" and its developer suspects that reward ([DevForum](https://devforum.roblox.com/t/game-with-nearly-200m-visits-banned-for-scamming/4776239)). See [15-the-line.md](15-the-line.md).

### Capacity

- WonderWorks ran 52 weekly updates with about 14 full-time staff, building each update in the final days before release from Discord feedback ([Naavik](https://naavik.co/podcast/the-creator-led-studio-playbook/)).
- Splitting Point's Field Trip Z updates were often finished about an hour before release ([GameAnalytics](https://gameanalytics.com/blog/splitting-point-how-field-trip-z-got-45m-players/)).
- 99 Nights built its Cultist Stronghold dungeon in about two days, and its team speaks about burnout ([DevForum](https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940), [Made on Roblox podcast](https://about.roblox.com/podcast)).
- Grow a Garden set up two event teams in July 2025 after players said events felt rushed ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)).
- Paradoxum tested trailers from a month to 2 to 3 days ahead and settled on about one week ahead, 30 seconds or less, with a retrospective after every update ([DevForum](https://devforum.roblox.com/t/creator-spotlight-belownatural%E2%80%99s-journey-building-paradoxum-games/3027035)).

## The rules

1. **Every update adds something a player can collect.** At least 2 new collectibles, as in Garden Tower Defense. Fixes ride along; they are never the update.
2. **Fix one day and one hour and keep them.** Every slop hit uses Saturday morning Pacific; Brookhaven uses Friday 6 PM Eastern. **Our read:** a fixed slot lets players plan, and it lets creators record on time.
3. **Weekly is the default; every 2 to 3 weeks is the floor.** Weekly is what the slop hits, Brookhaven and Volleyball Legends do. Roblox's guide and Clemens accept 2 to 4 weeks. Long gaps are what the dead games share: 93% of the top 100 published within 7 days of the snapshot and 1% had gone over 90 days [data, Nov 2026].
4. **One live moment a week, 30 to 60 minutes long.** That is Throw Food's admin-session length. A spike falls by two thirds within an hour, so a longer event is mostly empty server time.
5. **Raise the limited item's power in small steps: about x2 at first, then +0.5 to +1.** Steal a Brainrot went x2 to x14 over 12 events in 16 months.
6. **Seasons of 4 to 10 weeks with a weekly tier cap.** RIVALS: 70 tiers, 7 per week. Skips sell single tiers.
7. **Daily rewards escalate over 5 days and stop paying at 60 minutes of play.** Adopt Me and Bloxburg both use 5-day ladders; discovery ignores minutes past 60.
8. **Build at least 3 weeks of updates before launch.** **Our read:** Steal An Egg broke out on day 49 and peaked on day 56. A team building each update the night before has nothing left for that week.
9. **One stat per update, written down before shipping, read after the data window.** At least 7 days for a ranking stat, 14 for an experiment, as Roblox advises. Its Experiments tool saw about 1 in 4 of over 1,000 tests lift playtime, by about +5% on average ([DevForum](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276)). A launch influx can lower D1 on its own: one tycoon fell from 8-10% to 4-6% after an update ([DevForum](https://devforum.roblox.com/t/sudden-drop-on-playtime-and-retention-with-update/3880064)).
10. **Do not expect updates alone to hold a game.** Daily publishing did not hold Steal a Brainrot or Grow a Garden. The update has to give a reason to come back on a new day ([08-retention.md](08-retention.md)).

## How to do it

1. Copy [kit/templates/update-plan.md](../kit/templates/update-plan.md).
2. Pick your day and hour. Put a countdown to it on the HUD and in the game description.
3. Fill the capacity lines: hours per week for content, collectibles those hours buy, weeks already built.
4. Write the minimum update (below) for each of the first 6 weeks. Build 3 of them before launch.
5. Choose the live moment for each week: an admin session, a boss on a clock, a limited stock, or a reveal.
6. Decide the season: length, tier count, weekly cap, free and paid tracks. Start the first one in week 2 or 3, after the core loop has been fixed once.
7. Set up the daily layer: a 5-day ladder and playtime gifts that end at 60 minutes.
8. Plan one code per update and one milestone code you can announce (likes or concurrent).
9. Before each update, write one row in the hypothesis log: the worst funnel stat, the change, the number you expect, the read date ([14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md)).
10. Release a trailer of 30 seconds or less about a week before. After each update, hold a retrospective and fill the result column.

**Start with** this minimum weekly update for a team of 1 to 4. It is the smallest content set in the tables above (Garden Tower Defense, Dress to Impress small drops):

| Part | Minimum | Taken from |
|---|---|---|
| New collectibles | 2, one of them limited by stock or by a date | GTD: 2 limited units per update |
| Event moment | 1 session of 30 to 60 minutes at the fixed hour | Throw Food admin sessions |
| Code | 1, tied to the update | GTD, DTI |
| Something to film | 1 new visual or interaction a creator can show in 15 seconds | Letter: 3 to 4 videos per update |
| Fixes | Any, never alone | Madsen |

**Start with** this season if you add a pass: 50 tiers, 5 weeks of play at a cap of 10 tiers a week, a free track, a paid track at 299 R$, single-tier skips at 99 R$. The ratios come from RIVALS (7 tiers a week over 10 weeks) halved in length to match the 4 to 5 week seasons of BedWars Halloween and Volleyball Legends; the 299 R$ price is Dress to Impress's Diamond Pass.

## Checks

- [ ] The update day and hour are fixed, shown in the game, and have not moved in 4 weeks.
- [ ] Every update in the last 6 weeks added at least 2 collectibles.
- [ ] No gap between updates is longer than 21 days.
- [ ] There is one live moment a week, 30 to 60 minutes, with a countdown visible for at least 24 hours before.
- [ ] Each limited item is stronger than the last by +0.5 to +1 multiplier, or by a stated step, not by 10x.
- [ ] At least 3 weeks of updates are built ahead of the calendar.
- [ ] Every update has a hypothesis row with an expected number and a read date at least 7 days later.
- [ ] Daily rewards escalate over 5 days; playtime gifts stop by 60 minutes.
- [ ] A season, if any, has a weekly tier cap and lasts 4 to 10 weeks.
- [ ] The event was tested in a full server before it went live.
- [ ] No code, gift or event reward requires joining an outside community.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Saturday looks like any other day | No live moment, or a moment at a different hour each week | One fixed hour, a countdown, 30 to 60 minutes, something only attendees get |
| Players drift away in week 3 to 5 | Updates add systems and fixes, not things to collect | At least 2 collectibles per update; ship systems inside collectible updates |
| A spike, then an empty server for hours | Event too long, or everything given out in the first minutes | 30 to 60 minutes; a boss on a 30-minute clock (Steal An Egg) to spread the arrivals |
| The game crashes when the event opens | Code drop or limited item tested only in small servers (Dress to Impress, Dec 2024) | Load-test a full server; stagger the reward over the first minutes |
| The team misses a week, then another | Updates built the night before; no buffer (99 Nights spoke of burnout) | Keep 3 weeks built ahead; drop to every 2 weeks rather than skip randomly |
| Daily-reward claims rise, playtime does not | The reward pays for showing up, not for playing (one A/B test saw no lift) | Tie daily tasks to the core verb (RIVALS: play 5 duels, win 2) |
| An update "made things worse" in week one | A bigger, newer influx lowers the percentages | Compare same-source cohorts, wait 7 to 14 days before deciding |
| Updates every week, players still leaving | The update gives no reason to return on a new day | Add a timed item, a weekly cap or a 5-day ladder ([08-retention.md](08-retention.md)) |

## Sources

- Roblox public API (`games.roblox.com/v1/games`), 25 Nov 2026; [games API batch](https://games.roblox.com/v1/games?universeIds=10563114921,7709344486,7436755782).
- Roblox: [Retention doc](https://create.roblox.com/docs/en-us/production/analytics/retention.md); [DevForum: Recommended For You signals](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441); [DevForum: Experiments insights](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276); [DevForum: Season Pass feature package](https://devforum.roblox.com/t/beta-new-feature-packages-season-pass-engagement-rewards/3579550); [The Hunt](https://devforum.roblox.com/t/join-the-hunt-roblox-20/4875900); [The Hollow](https://devforum.roblox.com/t/the-hollow-new-platform-wide-survival-event-for-halloween/4948535).
- Wikis: [Steal a Brainrot Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log), [Hourly Events](https://stealabrainrot.fandom.com/wiki/Hourly_Events); [Grow a Garden Update Log](https://growagarden.fandom.com/wiki/Update_Log); [Garden Tower Defense Update Logs](https://garden-tower-defense.fandom.com/wiki/Update_Logs); [Brookhaven Changelog](https://brookhaven.fandom.com/wiki/Changelog); [DTI Update Log 2026](https://dti-dress-to-impress.fandom.com/wiki/Update_Log/2026); [Anime Defenders Updates](https://anime-defenders.fandom.com/wiki/Updates); [RIVALS Season Pass](https://robloxrivals.fandom.com/wiki/Season_Pass), [Tasks](https://robloxrivals.fandom.com/wiki/Tasks); [BedWars Battle Pass](https://robloxbedwars.fandom.com/wiki/Battle_Pass); [Epic Pass](https://typical-games.fandom.com/wiki/Epic_Pass), [Typical Games: Epic Minigames](https://typical-games.fandom.com/wiki/Epic_Minigames); [Adopt Me Bucks](https://adoptme.fandom.com/wiki/Bucks), [Task Board](https://adoptme.fandom.com/wiki/Task_Board); [Bloxburg Daily Reward](https://welcome-to-bloxburg.fandom.com/wiki/Daily_Reward); [Anime Vanguards Gamemodes](https://animevanguards.fandom.com/wiki/Gamemodes).
- Guides and trackers: [Bloxodes: Steal An Egg](https://bloxodes.com/wiki/steal-an-egg), [Throw Food For Animals](https://bloxodes.com/wiki/throw-food-for-animals), [Grow a Garden](https://bloxodes.com/wiki/grow-a-garden), [mutations](https://bloxodes.com/wiki/steal-a-brainrot/mutations), [Turkey guide](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide), [Brookhaven](https://bloxodes.com/wiki/brookhaven-rp), [Berry Avenue](https://bloxodes.com/wiki/berry-avenue-rp), [The Forge](https://bloxodes.com/wiki/the-forge), [Anime Dice](https://bloxodes.com/wiki/anime-dice); [rblxguide: DTI](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide), [Baddie Pass](https://rblxguide.com/games/dress-to-impress/updates/baddie-pass-guide), [money guide](https://rblxguide.com/games/dress-to-impress/updates/how-to-get-money-guide); [RBLXGuide: Volleyball Legends](https://rblxguide.com/games/volleyball-legends); [Bloxguides: RIVALS](https://bloxguidesgg.com/games/rivals); [StudioKrew](https://studiokrew.com/blog/?p=2016); [RoVitals](https://rovitals.com/); [RoWatcher: RIVALS](https://rowatcher.com/games/6035872082); [Rolimons: Anime Defenders](https://www.rolimons.com/game/17017769292); [bloxodes Oct 2026](https://bloxodes.com/stats/reports/roblox-october-2026), [Sept 2026](https://bloxodes.com/stats/reports/roblox-september-2026); [earnaldo: Karinderya](https://earnaldo.com/blog/karinderya); [allthings.how: Karinderya](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/), [Anime Dice](https://allthings.how/anime-dice-full-guide-for-roblox-update-4/).
- Practitioners: [Naavik: WonderWorks](https://naavik.co/podcast/the-creator-led-studio-playbook/); [Naavik: Clemens and Madsen](https://naavik.co/podcast/mastering-the-roblox-meta/); [GameAnalytics: Splitting Point](https://gameanalytics.com/blog/splitting-point-how-field-trip-z-got-45m-players/); [DevForum: 99 Nights](https://devforum.roblox.com/t/creator-spotlight-the-story-behind-99-nights-in-the-forest/4036940); [DevForum: Paradoxum](https://devforum.roblox.com/t/creator-spotlight-belownatural%E2%80%99s-journey-building-paradoxum-games/3027035); [Made on Roblox podcast](https://about.roblox.com/podcast).
- Other: [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden), [Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot), [Dress to Impress](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game)); [DevForum: daily rewards test](https://devforum.roblox.com/t/do-daily-rewards-actually-keep-players-retention/3556728); [DevForum: update hurt numbers](https://devforum.roblox.com/t/sudden-drop-on-playtime-and-retention-with-update/3880064); [DevForum: game banned for scamming](https://devforum.roblox.com/t/game-with-nearly-200m-visits-banned-for-scamming/4776239).
