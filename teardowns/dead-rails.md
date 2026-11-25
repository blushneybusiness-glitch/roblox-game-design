# Dead Rails

> Up to four players drive a train 80 km through a zombie-filled West, feeding it anything that burns; it peaked at about 1.5 million players and made fuel the clock of a journey game.

| | |
|---|---|
| Studio | not known |
| Released | Created 1 Jan 2025 (Roblox public API, 25 Nov 2026) |
| Genre | Co-op journey. See [genres/survival.md](../genres/survival.md) |
| Peak concurrent players | 1,476,198 on Saturday 19 Apr 2025 ([Rolimons](https://www.rolimons.com/game/116495829188952)) |
| Players now | 15,593 (Roblox public API, 25 Nov 2026, European evening); 30-day peak 37,740 ([Rolimons](https://www.rolimons.com/game/116495829188952)) |
| Players per server | 16 per server (Roblox public API, 25 Nov 2026); co-op for up to 4 ([Bloxodes](https://bloxodes.com/wiki/dead-rails)) |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

The run: start in a fortified town, drive toward Mexico, stop at a fortified town every 10 km, finish at 80 km and defeat Nikola Tesla ([Bluestacks guide](https://www.bluestacks.com/blog/game-guides/roblox/rl-dead-rails-beginners-guide-en.html)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Fuel | Throws coal, furniture or corpses into the furnace | A few per item (not timed) | Gauge out of 50 rises | Coal +13 (4,225 m), corpse +2 (650 m) ([Beebom](https://beebom.com/dead-rails-fuel/amp/)) |
| Drive | Runs the train | About 154 per 10 km at top speed (our arithmetic below) | Distance counter | km, gauge falls |
| Stop and loot | Searches a town, bank, fort | not known | Money bags, bonds, guns | $ for the run, bonds kept forever |
| Night | Defends the train | 160 per night | Zombies from 10 PM | 6 runners on night 1, +6 per cloudy night to 30 ([wiki: Day Cycle](https://deadrails.fandom.com/wiki/Day_Cycle)) |
| Safe town | Sells, buys coal and guns | not known | Fortified town every 10 km | Coal $20 ([DroidGamers](https://www.droidgamers.com/guides/how-many-coal-do-you-need-to-finish-dead-rails/)) |

The in-game day is 8 real minutes: 320 seconds of day and 160 of night ([wiki: Day Cycle](https://deadrails.fandom.com/wiki/Day_Cycle)). Top speed is 65 (Wooden train 75), and the Conductor class drives 30% faster ([wiki: Train](https://deadrails.fandom.com/wiki/Train)).

**Our read:** if 65 is metres per second, 80 km is about 20.5 minutes of pure driving. The wiki says a "travel 20 km" objective takes 10 to 40 minutes ([wiki: Run Objectives](https://deadrails.fandom.com/wiki/Run_Objectives)), so a full looted run is 30 minutes or more against a 14.87-minute average session ([Rolimons](https://www.rolimons.com/game/116495829188952)). Dead time is the driving between stops; the player fills it by feeding the furnace and shooting.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Spawn in a Fortified Town with a gold bar (sells for about $50) and a sack ([Bluestacks](https://www.bluestacks.com/blog/game-guides/roblox/rl-dead-rails-beginners-guide-en.html)). |
| 0:10 to 1:00 | Sell the bar, buy coal at $20, fuel the train. |
| 1:00 to 5:00 | Drive and loot. First 10 km town at about 2.6 minutes of pure driving (our arithmetic). |
| 5:00 to 15:00 | First night: 6 Runner Zombies under a cloudy sky ([wiki: Day Cycle](https://deadrails.fandom.com/wiki/Day_Cycle)). Rifles and shotguns are the upgrade between 20 and 40 km ([Bluestacks](https://www.bluestacks.com/blog/game-guides/roblox/rl-dead-rails-beginners-guide-en.html)). |

The in-game start hour is not in the sources, so the first night's real time is not known. First long goal shown: 80 km. How the game teaches is not known.

## 3. Progression

**In the run: fuel.** The gauge holds 50 units, about 325 m per unit once moving ([Beebom](https://beebom.com/dead-rails-fuel/amp/)).

| Item | Fuel | Distance |
|---|---|---|
| Nikola Tesla (the boss) | 41 | 13,350 m |
| Coal | 13 | 4,225 m |
| Barrel | 6 | 1,950 m |
| Chair, werewolf | 5 | 1,625 m |
| Rope, painting | 4 | 1,300 m |
| Book, wheel | 3 | 975 m |
| Zombie, wolf, outlaw, horse and other bodies | 2 | 650 m |
| Newspaper, wanted poster | 1 | 325 m |

Finishing takes about 19 coal for most classes and 16 for Miner or Conductor ([Beebom](https://beebom.com/dead-rails-fuel/amp/)); another guide says 21 coal, $420 ([DroidGamers](https://www.droidgamers.com/guides/how-many-coal-do-you-need-to-finish-dead-rails/)).

**Our read:**
- A full tank is 16,250 m, about 20% of the run. One coal is about 5%.
- 80,000 / 4,225 = 18.9, so 19 coal checks out. At $20 that is $380 of coal for a whole run.
- Night 1's 6 runners are worth 12 fuel, almost one coal. Night 5's 30 are worth 60, more than a full tank. Killing is a fuel source.

**Across runs: bonds.** Bonds are the permanent currency ([wiki: Bonds](https://deadrails.fandom.com/wiki/Bonds)).

| Source | Bonds |
|---|---|
| Win, Normal | 10 |
| Win, Nightmare | 20 |
| First win on any mode | +5 |
| Looting every point of interest | about 100 to 130 per run |
| Castle / Outlaw's Town / bank | 18 / 8 to 16 / 3 to 6 |
| Challenges | 5 to 30 (three weekly at 25) |
| Run objectives | 2 bonds and $20 each, up to 16 per run |

Sinks: 33 classes (4 limited) cost 1,545 bonds in all; trains 3,100 ([wiki: Classes](https://deadrails.fandom.com/wiki/Classes), [wiki: Train](https://deadrails.fandom.com/wiki/Train)). Single classes cost 15 to 100: Doctor 15 (three free revives a run), Miner 15 (2 coal), Conductor 50 (2 coal, faster train, half HP), Cowboy 50, Ironclad 100 (armor, 10% or 20% slower, guides disagree) ([DroidGamers classes](https://www.droidgamers.com/guides/dead-rails-classes-guide/)). A search snippet gives train prices of 250 to 285 bonds ([Sportskeeda via search](https://www.sportskeeda.com/roblox-news/all-train-variants-dead-rails-price-usage)).

**Our read:** looting pays 10 to 13 times a win. The bond economy rewards stopping, which is also what makes runs long. Every class is about 11 to 14 fully looted runs.

Difficulty modes (14 Nov 2026): Hard +25% bonds, Extreme +50% with half health regen, Nightmare +100% with no regen. Each unlocks from distance or a win on the mode below ([wiki: Changelogs](https://deadrails.fandom.com/wiki/Changelogs)). Class levels became Mastery trees on 31 Oct 2026: 1 point per 200 XP, points also sold for Robux (same source).

## 4. Session and return hooks

- Three weekly challenges at 25 bonds each ([wiki: Bonds](https://deadrails.fandom.com/wiki/Bonds)).
- Saturday releases in the log read: 20 Oct (Act 1), 24 Oct, 31 Oct, 7 Nov, 14 Nov, 21 Nov 2026. Timed "Dispatch" events run 72 hours to six days ([wiki: Changelogs](https://deadrails.fandom.com/wiki/Changelogs)).
- Distance badges every 10 km. Offline progress and daily rewards: not known.

## 5. Other players

Parties of up to 4 on a 16-player server. Healing (Doctor), fuel (Miner, Conductor) and defence (Ironclad, The Alamo) are split across classes. Since 24 Oct 2026 there is global matchmaking and invasions ([wiki: Changelogs](https://deadrails.fandom.com/wiki/Changelogs)).

Distance funnel ([badges API](https://badges.roblox.com/v1/universes/7018190066/badges?limit=100&sortOrder=Asc), Roblox public API, 25 Nov 2026):

| Badge | Awarded | Share of 10 km |
|---|---|---|
| Travel 10 km | 123.3M | 100% |
| 20 km | 79.0M | 64.0% |
| 30 km | 58.6M | 47.5% |
| 40 km | 45.5M | 36.9% |
| 50 km | 40.9M | 33.2% |
| 80 km | 33.7M | 27.3% |
| Defeat Tesla | 14.9M | 12.1% |

**Our read:** 36% drop between 10 and 20 km; past 50 km, 82% finish. Only 44% of finishers beat Tesla, so the boss is a second wall.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Tommy Gun | Pass | 175 | Weapon |
| Mauser C96 | Pass | 148 | Weapon |
| Sawed-Off Shotgun | Pass | 148 | Weapon |
| +5 Storage | Pass | 95 | Storage |
| 5 / 10 / 20 / 50 / 100 / 200 bonds | Product | 65 / 95 / 129 / 199 / 379 / 565 | 13 down to 2.83 R$ per bond |

Sources: [game-passes API](https://apis.roblox.com/game-passes/v1/universes/7018190066/game-passes?passView=Full&pageSize=50) (Roblox public API, 25 Nov 2026), [wiki: Bonds](https://deadrails.fandom.com/wiki/Bonds), [wiki: Changelogs](https://deadrails.fandom.com/wiki/Changelogs). **Our read:** the top class (100 bonds) costs 379 R$ or about one fully looted run. Best sellers are not known.

The snapshot matches the four passes and the six bond prices [data, Nov 2026]. Products: 19 on sale, 45 to 899 R$, median 199 (four items named "1" to "4" at 1 to 4 R$ left out). 12 of 19:

| Product | R$ | Note |
|---|---|---|
| 5 Bonds | 65 | 0.08 bonds per R$ |
| 200 Bonds | 565 | 0.35 bonds per R$: 4.6 times the smallest pack (our arithmetic) |
| 5 / 15 / 25 / 50 MP | 75 / 199 / 299 / 549 | MP is our reading of Mastery points |
| 100 MP | 899 | 15 R$ per point at 5, 9 at 100 |
| Self Revive | 45 | |
| Revive Teammate Grave / Revive Team | 67 / 200 | |
| Mastery XP Boost - 3 Runs | 100 | |
| Starter Pack | 149 | |

Two Christmas bundles sell at 275 and 499. **Our read:** all 33 classes (1,545 bonds) cost about 4,400 R$ at the best rate. The steep bond discount, 4.6 times from bottom to top, is the largest bulk bonus of the games in this set.

## 7. Why it works

Rating 92.5% and 6.20M favorites ([Rolimons](https://www.rolimons.com/game/116495829188952)). No developer statement was found.

**Our read:**
- The train is a moving base and a clock; any object, enemy or boss can be weighed as metres.
- A safe town every 10 km cuts 80 km into eight short legs with a shop at each.
- Classes are cheap next to a run's loot, so a first or second run already buys a new way to play.

## 8. What went wrong

- 30-day peak is 2.6% of the all-time peak (our arithmetic on [Rolimons](https://www.rolimons.com/game/116495829188952)).
- A full run is about twice the average session, and 36% of players who reach 10 km stop before 20 km.
- Class counts conflict across guides (13, 29, 34, 33), a sign of frequent reworks. Update history before October 2026 was not read.

## 9. What to take from it

- A 50-unit gauge where the best common fuel fills 26% and one full tank covers 20% of the run.
- A safe stop every 1/8 of the journey (10 of 80 km).
- A night of 160 s inside an 8-minute day, enemies rising +6 a night to 5x the first.
- Win pays 10, full looting 100 to 130: pay for exploring more than for finishing.
- Classes at 15 to 100 bonds, all 33 for 1,545; bond packs at 2.83 to 13 R$ per bond.
- Revives at three sizes: self 45, a teammate 67, the whole team 200 R$ [data, Nov 2026].

## Sources

- [Dead Rails Fandom wiki](https://deadrails.fandom.com/wiki/Bonds) (pages linked in the text), [Beebom fuel](https://beebom.com/dead-rails-fuel/amp/), [DroidGamers classes](https://www.droidgamers.com/guides/dead-rails-classes-guide/), [Bloxodes](https://bloxodes.com/wiki/dead-rails), [Rolimons](https://www.rolimons.com/game/116495829188952)
- Roblox public API, 25 Nov 2026: [badges](https://badges.roblox.com/v1/universes/7018190066/badges?limit=100&sortOrder=Asc), [game passes](https://apis.roblox.com/game-passes/v1/universes/7018190066/game-passes?passView=Full&pageSize=50)
- Genre playbook: [genres/survival.md](../genres/survival.md)
