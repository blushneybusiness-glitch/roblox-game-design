# Forsaken

> One killer hunts the other players of a 9-player server for a 4-minute round while they repair generators. It is the live benchmark for one-killer-versus-many horror on Roblox, and it peaked above 1.2 million players.

| | |
|---|---|
| Studio | Forsaken Dev Team |
| Released | Place created 28 July 2024; soft launch 25 December 2024; on the home page 6 January 2025 ([wiki](https://forsaken2024.fandom.com/wiki/FORSAKEN)) |
| Genre | One versus many horror ([genres/horror.md](../genres/horror.md)) |
| Peak concurrent players | 1,221,080 on 1 November 2025 ([Rolimons](https://www.rolimons.com/game/18687417158)) |
| Players now | 43,357 (Roblox public API, 25 Nov 2026), 3.6% of peak. 5.98 billion visits, 3.32 million favourites. 30-day peak 278,097; rating 84.4% |
| Players per server | 9 maximum, 9 on average |
| Teardown date | 25 November 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

How the killer is chosen each round is not known. **Our read:** with 9 players and one killer, up to 8 are survivors.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1 | Round starts | Clock at 4:00 ([wiki](https://forsaken2024.fandom.com/wiki/Objectives)) | Map, round clock | none |
| 2 | Survivors repair a generator: a 7x7 wire-connect puzzle in 4 layers, 2 or 3 players to a generator | 4 layers; the wiki says each layer "cuts 3 s", 12 s per generator (the page once says 14). We read this as time cut from the round clock | Puzzle grid | Clock down; 2 Player Points and 8 XP per generator (10 with VIP) |
| 3 | Killer chases; survivors sprint and break line of sight | Survivor sprint about 10 s from full | Killer's approach, stamina bar | Stamina 100, drain 10 a second |
| 4 | Survivor recovers | 5 s from empty, plus a 2 s delay after hitting 0 | Stamina bar refilling | Regeneration 20 a second |
| 5 | Round ends | 3:00 at the earliest if all 5 generators are done | Result screen | Points: survivor win 25, killer win 60 |

Our arithmetic: five generators take 60 s off a 240 s clock, so the shortest round is 3:00, as the wiki's numbers imply. The objective is at most a quarter of the round. The other three quarters are chasing, hiding and healing.

Killer stamina is 110 (125 for Jeff the Killer), drains 9.5 a second and regains 21 a second ([wiki](https://forsaken2024.fandom.com/wiki/Stamina)). Our arithmetic: a killer can sprint about 11.6 s against a survivor's 10 s, so a straight chase ends with the survivor empty first. A survivor has to break line of sight before about the 10th second. Slasher's speeds per Bloxodes are 9 walking and 28 sprinting ([Bloxodes](https://bloxodes.com/wiki/forsaken/killers)); survivor speeds are not known. Survivor health is about 100.

The average session is 19.75 minutes ([Rolimons](https://www.rolimons.com/game/18687417158)). Our arithmetic: at most about 5 rounds of 4 minutes, fewer once lobby time is counted (not known).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | First join pays 300 Player Points ([wiki](https://forsaken2024.fandom.com/wiki/Player_Points)) |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | First round, 3 to 4 minutes |
| 5:00 to 15:00 | Rounds 2 to 4 |

First steps, the tutorial and the time to first contact with the killer are not documented. The 300 starting points sit inside the survivor price range (free to 777), so a first purchase may be possible at once (our read; individual survivor prices are not found in our research).

## 3. Progression

Player Points ([wiki](https://forsaken2024.fandom.com/wiki/Player_Points)):

| Event | Points |
|---|---|
| First join | 300 |
| Survivor win | 25 |
| Survivor dies after surviving 60 s or more | 6 |
| Generator done | 2 |
| Healing a Hemorrhage | 10 |
| Killer win / loss / per kill | 60 / 15 / 15 |

No points in private servers.

Roster: 12 survivors (free to 777 points) and 8 killers (free to 2,000; all eight cost 9,838) ([Killers](https://forsaken2024.fandom.com/wiki/Killers), [Survivors](https://forsaken2024.fandom.com/wiki/Survivors)). Killer prices per Bloxodes:

| Killer | Points | Health (Bloxodes) |
|---|---|---|
| Slasher | free | 2,000 |
| c00lkidd | free (a newer guide says only Slasher is free) | 1,000 |
| John Doe | 1,000 | 2,300 |
| Noli | 1,100 | 2,222 |
| 1x1x1x1 | 1,250 | 1,100 |
| Guest 666 | 1,666 | 2,750 |
| Nosferatu | 1,922 | 1,750 |
| Azure | 2,000 | 1,500 |

Source: [Bloxodes](https://bloxodes.com/wiki/forsaken/killers). Killer cooldowns are not listed. Noli plants fake generators at round start.

Our arithmetic: a survivor win with two generators pays about 29 points, so a 1,000-point killer takes about 35 winning rounds, or 17 killer wins. At 4 minutes a round, 35 wins is about 140 minutes of winning rounds, roughly 7 average sessions if every round were won.

## 4. Session and return hooks

The round itself is the hook: 3 to 4 minutes, then the next. A seasonal Easter update in April 2026 is mentioned by a guide. Update 1.2.0 (2026) reworked generators. Daily rewards, restocks and update day: not known. Forsaken patches more often than Doors.

## 5. Other players

9 per server. Survivors share generators (2 or 3 per generator) and heal each other: healing a Hemorrhage pays 10 points. The killer can bleed survivors: Slasher's Bleeding I lasts 5 seconds for about 28 damage, per a search summary of the wiki. There is no trading and nothing is lost beyond the round. What gets clipped: not documented. **Our read:** a chase that ends with a survivor breaking line of sight at the last second of stamina.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| V.I.P | Pass | 599 | XP per generator 10 instead of 8; other effects not known |
| Skin Pack #4 | Pass | 349 | Skins |
| 2x Emotes | Pass | 199 | Emotes |
| Emote Pack #3 | Pass | 189 | Emotes |

Sources: [game-pass endpoint](https://apis.roblox.com/game-passes/v1/universes/6331902150/game-passes?passView=Full&pageSize=50) (Roblox public API, 25 Nov 2026). The snapshot matches: these 4 passes are on sale and 7 older packs are off sale [data, Nov 2026].

**Developer products [data, Nov 2026].** 71 products, all on sale, 30 to 5,850 R$, median 380 R$. 23 of them are gift copies of passes and currency packs. 12 of 71:

| Product | R$ | Kind |
|---|---|---|
| 100$ | 30 | Points ladder, smallest of 8 |
| 20000$ | 5,850 | Points ladder, largest |
| 800 Tix | 99 | Second currency, smallest of 4 |
| 26000 Tix | 1,999 | Largest |
| +400 Candy | 79 | Event currency, smallest of 4 |
| +10,000 Candy | 1,450 | Largest |
| +15 Malice | 199 | Third currency (also 30 for 319) |
| 25% EXP Boost (1 Hour) | 60 | Boost (3, 6, 12 h also sold) |
| 25% EXP Boost (12 Hours) | 690 | |
| 50% Sukkar Boost (1 Hour) | 79 | Event currency boost |
| [WEEK 1] Skip 5 Tiers | 380 | Weekly tier skip (1 tier: 79), weeks 1 to 4 |
| Skip All Quests | 1,500 | Quest skip (one quest: 79) |

The "$" products run 100 to 20,000, the same amounts as the wiki's [Player Points](https://forsaken2024.fandom.com/wiki/Player_Points) packs, but at lower prices: the wiki lists 40 R$ for 100 and 7,600 R$ for 20,000; the snapshot has 30 and 5,850.

Our arithmetic: points cost 0.30 R$ each in the smallest pack and 0.29 in the largest (3.33 and 3.42 per R$), so a 1,000-point killer costs about 300 R$, against about 35 winning rounds of play. Tix give 8.1 per R$ at the bottom and 13.0 at the top, Candy 5.1 and 6.9. The EXP boost costs 60 R$ an hour singly and 57.5 in the 12-hour product. Characters can be earned without paying. No pass sells power directly. Best sellers: not known.

## 7. Why it works

Forsaken won Best Survival Experience at the 2025 Roblox Innovation Awards ([wiki](https://forsaken2024.fandom.com/wiki/FORSAKEN)).

**Our read:**
- A 4-minute round, cut by up to 60 s when survivors work, gives each round a clear end and a reason to do the objective.
- Stamina of 10 s sprint and 5 to 7 s recovery makes every chase a short decision: run now or hide.
- The killer's 10% larger stamina means running alone loses; survivors must use the map and each other.
- A killer win pays 60 against a survivor win of 25, which rewards the harder seat.
- Characters are bought with points from play, at 1,000 to 2,000, so the first paid killer comes after about 7 sessions of winning play.

## 8. What went wrong

- From 1,221,080 (1 Nov 2025) to 43,357: 3.6% of peak a year later. The 30-day peak of 278,097 shows events still lift it.
- The rating, 84.4%, is the lowest of the horror leaders in our research (Doors 93.06%). Causes are not documented.
- Guides disagree on round length (one says 5 to 10 minutes; the wiki says 4:00) and on which killers are free, a sign the rules changed between updates.

## 9. What to take from it

- A 4:00 round clock that objectives shorten: 5 objectives at 12 s each, 3:00 minimum.
- Survivor stamina 100, drain 10 a second, regain 20 a second, 2 s delay at empty; killer 110, drain 9.5, regain 21.
- 9 players per server: one killer, up to 8 survivors, 2 or 3 to an objective.
- Points per round: survivor win 25, killer win 60, objective 2; 300 on first join.
- Characters at 1,000 to 2,000 points, about 35 wins each.
- In the Nov 2026 snapshot points cost 0.29 to 0.30 R$ each, with the bulk discount under 3%, and a weekly tier skip sells at 79 R$ for 1 tier or 380 R$ for 5 [data, Nov 2026].

## Sources

- [Forsaken wiki](https://forsaken2024.fandom.com/wiki/FORSAKEN): Objectives, Stamina, Player Points, Killers, Survivors
- [Bloxodes: Forsaken killers](https://bloxodes.com/wiki/forsaken/killers)
- [Roblox games API](https://games.roblox.com/v1/games?universeIds=6331902150), 25 Nov 2026
- [Rolimons](https://www.rolimons.com/game/18687417158)
- [genres/horror.md](../genres/horror.md)
