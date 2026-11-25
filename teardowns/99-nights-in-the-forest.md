# 99 Nights in the Forest

> A party of 1 to 5 keeps a campfire alive for 99 in-game days while rescuing four lost kids; it set the 2025 benchmark for co-op survival runs with a 14 million player peak.

| | |
|---|---|
| Studio | Grandma's Favourite Games ([fan wiki](https://99nightsintheforest.wiki/)); developers Alec Kieft, Cameron Angland, Matthew Hufton ([Wikipedia](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest)) |
| Released | Created 4 Mar 2025 (Roblox public API, 25 Nov 2026) |
| Genre | Co-op survival run. See [genres/survival.md](../genres/survival.md) |
| Peak concurrent players | 14,153,173 on Saturday 4 Oct 2025 ([Rolimons](https://www.rolimons.com/game/79546208627805)); Wikipedia gives 14.2M ([Wikipedia](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest)) |
| Players now | 175,700 (Roblox public API, 25 Nov 2026, European evening); 30-day peak 1,520,535 ([Rolimons](https://www.rolimons.com/game/79546208627805)) |
| Players per server | 25 per server (Roblox public API, 25 Nov 2026); parties of 1 to 5 ([fan wiki](https://99nightsintheforest.wiki/)) |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

One day and night is the loop. Day lasts 3:00 and night 1:30, so one cycle is 4:30 ([wiki: Days](https://99-nights-in-the-forest.fandom.com/wiki/Days)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Gather | Chops logs, loots, runs junk through the grinder for scrap | 0 to 180 (day) | Sack fills: 5, 15 or 20 slots by sack tier ([guide](https://ddingpy.github.io/mynote/posts/99-nights-in-the-forest-roblox-survival-guide)) | Logs, scrap (1, 3, 5 or 8 per item by bolt icon) ([wiki: Crafting](https://99-nights-in-the-forest.fandom.com/wiki/Crafting)) |
| Feed the fire | Drops fuel into the campfire | During the day | Fire bar rises; each level widens the map and the safe zone | Fire level 1 to 6 ([wiki: Campfire](https://99-nights-in-the-forest.fandom.com/wiki/Campfire)) |
| Build | Spends wood and scrap at the bench | During the day | New object in camp | Bench tier 1 to 5 |
| Night | Holds the safe zone, stuns the deer with a flashlight | 180 to 270 | The deer, wolves, cultists on raid nights | HP, hunger |
| Dawn | Nothing; the counter ticks | 270 | Day counter goes up | +1 day, up to +9 with kids and beds |

Cycle time 270 seconds. On the first nights there are no wolves (night 1) and the deer is passive (day 1) ([fan wiki](https://99nightsintheforest.wiki/)), so the 90-second night is mostly waiting in the safe zone. **Our read:** that is up to 90 seconds of dead time per cycle early on, filled by crafting and cooking at camp. How long each day step takes is not known.

## 2. First session

Times assume a 1x counter, which the wiki says applies to days 1 to 10 regardless of kids and beds ([wiki: Days](https://99-nights-in-the-forest.fandom.com/wiki/Days)).

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Lobby. Pick a party size of 1 to 5 in the matchmaking box ([fan wiki](https://99nightsintheforest.wiki/)). |
| 0:10 to 1:00 | Day 1. Light the fire for 1 log ([wiki: Campfire](https://99-nights-in-the-forest.fandom.com/wiki/Campfire)). |
| 1:00 to 5:00 | Fire to level 2 (6 logs) and level 3 (11 logs) before dusk at 3:00. Night 1 at 3:00 to 4:30: the deer does not attack ([wiki: Days](https://99-nights-in-the-forest.fandom.com/wiki/Days)). |
| 5:00 to 15:00 | Day 2 starts at 4:30: the deer may wake, the Pelt Trader visits. Day 3 at 9:00: carnival or frogs, alien or meteor event at night. Day 4 at 13:30, with a warning the day before. |
| 16:30 | First Cultist raid, night 4 ([wiki: Night Raids](https://99-nights-in-the-forest.fandom.com/wiki/Night_Raids)). |

First rare moment: day 3 events at 9:00. First long goal shown: the 99-day counter and four kids. How the game teaches is not known. **Our read:** the first raid lands at 16:30 and the average session is 16.13 minutes ([Rolimons](https://www.rolimons.com/game/79546208627805)), so a typical visit ends around the first real fight.

## 3. Progression

**In the run: the campfire.** Each step needs any one of the fuels listed ([wiki: Campfire](https://99-nights-in-the-forest.fandom.com/wiki/Campfire)).

| Step | Logs | Coal | Fuel canisters | Oil barrels | Biofuel |
|---|---|---|---|---|---|
| 1 to 2 | 6 | - | - | - | - |
| 2 to 3 | 11 | 2+ | 2+ | - | - |
| 3 to 4 | 50-75+ | 23+ | 9-12+ | - | 30+ |
| 4 to 5 | 70-120+ | 45+ | 19-25+ | 4+ | 30+ |
| 5 to 6 | 275-350+ | 170+ | 35+ | 8+ | 80+ |

After level 4 one log adds under 1% to the bar. Bigger parties find the fire harder to fuel. If it dies, the deer always spawns, the safe zone and regen vanish and the map locks (same source). Burn rate in seconds: not known. **Our read:** log steps multiply by 1.8, 4.5 to 6.8, 1.4 to 1.6, then 2.9 to 3.9; at least 413 logs reach level 6, so far-biome fuels take over.

**The calendar.** One day per night at 1x. Each rescued kid adds 1 and each Old Bed adds 1, capped at 9 days per night ([wiki: Missing Children](https://99-nights-in-the-forest.fandom.com/wiki/Missing_Children), [wiki: Crafting](https://99-nights-in-the-forest.fandom.com/wiki/Crafting)). Older guides said +2 or +3 per kid ([roonby](https://roonby.com/2025/06/20/99-nights-in-the-forest-roblox-guide-full-walkthrough-ending-how-to-survive-100-days/amp/)); the wiki is newer. A 1x run is 445.5 minutes; at 9x from day 1 it is 49.5 minutes ([wiki: Days](https://99-nights-in-the-forest.fandom.com/wiki/Days)).

**Our read:** if days 1 to 10 ignore multipliers, the fastest run is 10 x 4.5 = 45 minutes plus 89 / 9 x 4.5 = 44.5 minutes, about 89.5 minutes. The Swiftness badge is "99 days under 90 minutes", which fits that arithmetic.

**Across runs: classes.** 39 active classes, 10 to 600 diamonds, 9,165 for all: Camper 10 (-10% hunger drain), Medic 40, Lumberjack 70 (+20% log), Berserker 100 (auto-revive once), Blacksmith 200, eight classes at 600 ([wiki: Classes](https://99-nights-in-the-forest.fandom.com/wiki/Classes)). Each class has 3 levels unlocked by counters (Camper: 75 food cooked and 200 logs burned, then 150 and 350). Robux skips level 2 for 290 [data, Nov 2026] (the wiki said 250) and level 3 for 400 (same source).

**Diamond income.** Day 50 pays 2, day 99 pays 3, a stronghold chest 5, daily quests 5 each or 15 for all three; badges pay their star rating once. The wiki puts a full routine (99 days, 3 strongholds, all dailies) at about 35 diamonds ([wiki: Diamonds](https://99-nights-in-the-forest.fandom.com/wiki/Diamonds)). **Our read:** a 600 class is about 17 full-routine days; every class is about 262.

## 4. Session and return hooks

- Three daily quests (above).
- Shop: since 19 Sep 2026 every class is always in stock and 3 or 4 random classes get 10%, 15% or 20% off for 24 hours ([wiki: Classes](https://99-nights-in-the-forest.fandom.com/wiki/Classes)). This replaced a rotating stock with 99 R$ rerolls.
- Hard Mode and biome choice unlock at a best of 10 days ([wiki: Update Log](https://99-nights-in-the-forest.fandom.com/wiki/Update_Log)).
- Updates: Saturday, with a developer "update party" at 1 PM EST and the update about 30 minutes later. Weekly from 27 Jun 2025 to 18 Apr 2026, then about every two weeks from 13 Jun 2026 (same source).

## 5. Other players

Difficulty is set by party size at the start and does not drop if players leave; a lone survivor of a 5-party faces raids sized for five ([fan wiki](https://99nightsintheforest.wiki/)). Raids grow to a cap of 8 cultists every 4 days ([wiki: Night Raids](https://99-nights-in-the-forest.fandom.com/wiki/Night_Raids)). Squad classes: Medic, Support, Base Defender, Scavenger. No trading or stealing is described.

Badge funnel ([badges API](https://badges.roblox.com/v1/universes/7326934954/badges?limit=100&sortOrder=Asc), Roblox public API, 25 Nov 2026):

| Badge | Awarded | Share of day 10 |
|---|---|---|
| Survive 10 days | 408.7M | 100% |
| 20 days | 280.5M | 68.6% |
| 30 days | 207.4M | 50.7% |
| 50 days | 140.0M | 34.2% |
| 100 days | 87.5M | 21.4% |
| Swiftness (under 90 min) | 58.5M | 14.3% |
| Teamwork (99 days, team of 5) | 8.9M | 2.2% |

Firemaking I (level 3) 737.3M, II 76.5% of I, III 41.7%, IV 24.0% (same source).

## 6. Money

Passes: 4 listed, 1 on sale [data, Nov 2026]. Decorator Pass, 199 R$: free hammer and paintbrush, remote furniture buying, trader discounts ([wiki: Diamonds](https://99-nights-in-the-forest.fandom.com/wiki/Diamonds)). Diamond Hunter Pass, Ranger Class and Medic Class are listed but not for sale.

Products: 24 on sale, 40 to 2,500 R$, median 240 (a 1 R$ test item left out) [data, Nov 2026]. Each diamond pack has a "Gift" copy at the same price. 12 of 24:

| Product | R$ | Note |
|---|---|---|
| 20 / 100 / 250 / 700 Diamonds | 99 / 400 / 900 / 2,500 | 0.20 diamonds per R$ at 99, 0.28 at 2,500: 39% more (our arithmetic) |
| Self Revive / Self Revive Again | 55 / 95 | Diamonds cannot buy revives ([wiki: Diamonds](https://99-nights-in-the-forest.fandom.com/wiki/Diamonds)) |
| Revive Friend / Revive Everyone | 95 / 230 | |
| Skip to Level 2 / Skip to Level 3 | 290 / 400 | Class level skips |
| Starter Survival Kit | 299 | |
| Reroll Classes (1) | 99 | Six reroll products, 99 to 400, are still listed |

The page's earlier sources disagree: a search snippet of [PC Gamer](https://www.pcgamer.com/games/survival-crafting/roblox-99-nights-in-the-forest-revive) gave revives at 45 and 200, and the [wiki: Classes](https://99-nights-in-the-forest.fandom.com/wiki/Classes) the level 2 skip at 250. **Our read:** the second self revive costs 73% more than the first, so the price climbs inside one run. The cheapest 600 diamonds is 900 + 900 + 400 = 2,200 R$. Best sellers are not known.

## 7. Why it works

Average session 16.13 minutes, the longest of the big co-op hits; 10.38M favorites; 90.5% rating ([Rolimons](https://www.rolimons.com/game/79546208627805)). Two 2025 Innovation Awards ([Wikipedia](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest)). No developer interview was found.

**Our read:**
- One object (the fire) is the clock, the base and the progress bar at once.
- Kids and beds let a party choose how fast the calendar runs, from 445 to about 90 minutes.
- Classes are bought only with earned diamonds, so a run that fails still pays toward the next one.
- The record fell on a Saturday update day, 99 days after the class system launched on 27 Jun 2025.

## 8. What went wrong

- Peak to 30-day peak is 10.7%; the snapshot is 1.2% of peak (our arithmetic on [Rolimons](https://www.rolimons.com/game/79546208627805)).
- Half of players who reach day 10 are gone before day 30 (badge funnel above).
- Updates slowed from weekly to about every two weeks in June 2026; the wiki log shows none between 18 Apr and 13 Jun 2026 ([wiki: Update Log](https://99-nights-in-the-forest.fandom.com/wiki/Update_Log)).
- The Fortnite collaboration drew a mixed reaction ([Wikipedia](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest)).

## 9. What to take from it

- A 3:00 day and 1:30 night, with the first raid on night 4 (16:30 into the run).
- A fuel ladder of 5 steps where logs go 6, 11, 50, 70, 275 and a new fuel type joins at step 2 and 4.
- A calendar speed-up of +1 day per night per rescue or bed, capped at 9x.
- Difficulty fixed by party size at the start, 1 to 5 players.
- Classes at 10 to 600 earned diamonds against about 35 free diamonds per full day of play.
- A self revive at 55 R$, 95 R$ the second time, and 230 R$ for the team [data, Nov 2026].

## Sources

- [99 Nights Fandom wiki](https://99-nights-in-the-forest.fandom.com/wiki/Days) (pages linked in the text), [99nightsintheforest.wiki](https://99nightsintheforest.wiki/), [Wikipedia](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest), [Rolimons](https://www.rolimons.com/game/79546208627805)
- Roblox public API, 25 Nov 2026: [badges](https://badges.roblox.com/v1/universes/7326934954/badges?limit=100&sortOrder=Asc), [game passes](https://apis.roblox.com/game-passes/v1/universes/7326934954/game-passes?passView=Full&pageSize=50)
- Genre playbook: [genres/survival.md](../genres/survival.md)
