# Doors

> Open 100 numbered doors in a haunted hotel with up to three friends, and answer each monster with the one move that beats it. It set the template for one tell, one counter and one fixed damage number per threat.

| | |
|---|---|
| Studio | LSPLASH, with Redibles ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games)) |
| Released | 10 August 2022 (place created 14 March 2021) |
| Genre | Room-based horror run ([genres/horror.md](../genres/horror.md)) |
| Peak concurrent players | 381,720 on 29 January 2023 ([Rolimons](https://www.rolimons.com/game/6516141723)) |
| Players now | 15,436 (Roblox public API, 25 Nov 2026); 15,253 on Rolimons. 8.05 billion visits, rating 93.06% |
| Players per server | 50 maximum, 22.9 on average; runs start from elevators of 1 to 4 players, custom elevators up to 50 ([wiki](https://doors-game.fandom.com/wiki/Elevator)) |
| Teardown date | 25 November 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1 | Opens the next numbered door | not known | Door number above the frame | +1 Knob ([wiki](https://doors-game.fandom.com/wiki/Knobs)) |
| 2 | Searches drawers and chests | not known | Gold, items; a spider 1 time in 200 ([wiki](https://doors-game.fandom.com/wiki/Timothy)) | Gold |
| 3 | Reads a tell | not published | Flicker, rumble, "psst", footsteps | none |
| 4 | Answers it | A closet is safe for about 12 ([wiki](https://doors-game.fandom.com/wiki/Hide)) | Closet view; heartbeat minigame near Figure | Health, by a fixed amount if wrong |

Cycle time per room is not published. The average session is 9.68 minutes ([Rolimons](https://www.rolimons.com/game/6516141723)). A player cannot fall far behind the party: when too many rooms are open ahead of them (5 at first, then 4 and 3 later in the floor), Void teleports them to the newest room for 20 to 40 damage ([wiki](https://doors-game.fandom.com/wiki/Void)).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Lobby with 12 elevators; stepping in starts a 5 to 30 second countdown ([wiki](https://doors-game.fandom.com/wiki/Lobby)) |
| 0:10 to 1:00 | Pre-Run Shop with a 30 second timer; Reception, then Door 1. Rush cannot spawn on Doors 1 and 2 |
| 1:00 to 5:00 | First Rush possible from Door 3; Rush comes about every 10 doors ([wiki](https://doors-game.fandom.com/wiki/Rush)) |
| 5:00 to 15:00 | First Seek chase in rooms 28 to 46; Library and Figure at Door 50; Jeff Shop at Doors 53 to 59 |

Nothing is taught with text before play. Teaching happens at death: the Guiding Light screen gives one line per cause, such as "pay attention to cues" for Rush ([wiki](https://doors-game.fandom.com/wiki/Guiding_Light)). First reward: 1 Knob at Door 1. First contact with another player: the elevator. First long goal shown: not known.

## 3. Progression

Threats, with tell, counter and damage, are in [genres/horror.md](../genres/horror.md#one-tell-one-counter-one-punishment-doors). The structure:

| Floor | Length | Gate |
|---|---|---|
| Hotel | 100 rooms; Library at 50, Electrical Room at 100 | none |
| Mines | 100 rooms; new threats at 101 to 105; Seek at 142 to 149 and again from somewhere between 170 and 184; Dam boss at 200 | not known |
| Backdoor | 50 rooms, timed; levers add time | not known |
| Outdoors | 35 rooms | Door 90 or 99 with Shears and a Skeleton Key; 10 Stardust |
| Archives | about 26 sectors of 50 rooms | Door 60 with two Lockpicks and a Skeleton Key |

Sources: [OP.GG floors](https://op.gg/roblox/wiki/doors/floors), [Seek](https://doors-game.fandom.com/wiki/Seek), [Shops](https://doors-game.fandom.com/wiki/Shops).

Knobs, the soft currency: 1 per numbered door, 50 per floor finished, 1 per 20 Gold (capped at 500), plus 0.1x per friend up to 0.3x, times 5 with a Boost ([wiki](https://doors-game.fandom.com/wiki/Knobs)).

| Shop | Items and prices |
|---|---|
| Pre-Run (Hotel), Knobs; 30 s timer; items upgrade for 10 Stardust | Lighter 50, Lockpicks x2 50, Vitamins x3 100, Flashlight 100 (item-price pairing read from the wiki's layout) |
| Jeff Shop (Hotel), Gold | Lighter 100, Vitamins 100, Lockpick 100, Flashlight 200, Skeleton Key 300, Crucifix 500 |

Our arithmetic: a plain Hotel escape pays about 150 Knobs, so the full 300-Knob Pre-Run kit takes two escapes. A death at Door 50 pays 50, enough for one Lighter.

Modifiers (80 since 26 Aug 2023) unlock after the first Hotel finish. Each changes a rule and adds a Knob bonus of +5% to +10%, or removes one (Bug Spray -10%) ([wiki](https://doors-game.fandom.com/wiki/Modifiers)).

The badge funnel shows how far players get (Roblox public API, 25 Nov 2026):

| Badge | Share of 536.7M joiners |
|---|---|
| Survived Rush | 55% |
| Survived Seek | 19% |
| Survived Figure | 9.5% |
| Finished the Hotel (Rock Bottom, both versions) | 2.7% |
| Hotel Hell (150%+ modifiers) | 0.08% |

## 4. Session and return hooks

- Daily Runs (since 2 Jan 2026): 25 Knobs and 3 Stardust per escape ([wiki](https://doors-game.fandom.com/wiki/Knobs)).
- Today's Deals skins rotate daily at 3 PM EST ([wiki](https://doors-game.fandom.com/wiki/Shops)).
- Seasonal modes: Candy Vault (52 rooms, 20-minute alarm), Trick or Treat (500 rooms), Party Mode (250 rooms, 300 HP, 7-minute limit) ([OP.GG](https://op.gg/roblox/wiki/doors/floors), [wiki](https://doors-game.fandom.com/wiki/Party_Mode)).
- Major updates: Hotel+ 28 Jan 2023, Modifiers 26 Aug 2023, Backdoor 15 Mar 2024, Content Update 20 Dec 2024, Great Outdoors 10 Aug 2025, Daily Runs 2 Jan 2026 ([wiki](https://doors-game.fandom.com/wiki/Updates)).

## 5. Other players

Parties of 1 to 4. 40% of joiners hold the Buddy System badge for a run with a friend. Friends add up to 0.3x Knobs. A player can pull Giggle off a friend's face ([wiki](https://doors-game.fandom.com/wiki/Giggle)). A dead player can be revived within 2 minutes in a party, 5 minutes solo. No trading, no theft, no loss beyond the run. What gets clipped: not documented; **Our read:** the friend who did not reach a closet.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Revive | Product | 40; 145 for 5; 239 for 10; 479 for 25 | Back into the run |
| Knob packs | Product | 49 for 250 up to 1,799 for 16,000 | Pre-Run items |
| 5x Knob Boost | Product | 59 for one, 129 for three [data, Nov 2026] | 5x Knobs for one floor |
| Stardust | Product | 25 for 10 up to 499 for 350 [data, Nov 2026] | Item upgrades, Outdoors entry |
| Second and third revive in a run | Product | 60, then 120 [data, Nov 2026] | Revive yourself again |
| +1 Permanent Save Slot | Product | 50 [data, Nov 2026] | |
| Admin Panel | Pass | 499 | Admin and stream tools (Dec 2024) |
| Kitty Bundle | Pass | 299 | not known |

Sources: [Revives](https://doors-game.fandom.com/wiki/Revives), [Shops](https://doors-game.fandom.com/wiki/Shops), [game-pass endpoint](https://apis.roblox.com/game-passes/v1/universes/2440500124/game-passes?passView=Full&pageSize=50) (Roblox public API, 25 Nov 2026). Each UGC accessory bought also gives 200 Knobs and 1 revive.

The snapshot matches both passes (a Halloween '26 pass is off sale) and every revive and Knob price above. It settles the boost price that the wiki and older sources gave as 59, 99 or 129: 59 buys one boost and 129 buys three [data, Nov 2026]. Products: 21 on sale, 25 to 1,799 R$, median 129, leaving out 16 "GIFT" copies and a 1,000,000-Knob placeholder at 100,000 R$. The table above covers 20 of the 21; the last is an "(OLD)" 3-run boost at 100. Stardust runs from 0.40 to 0.70 per R$, 75% more at the top (our arithmetic). The gift copy of the Admin Panel costs 375, a quarter less than the pass.

The revive is offered on the death screen. It is blocked while Rush, Ambush, Seek or A-120 is active, in the Greenhouse, the Electrical Room and Mines rooms 190 to 200, and it resets the reward door counter. The window was 30 seconds before the Content Update. Our arithmetic: packs bring the price from 40 to 19 R$ each; Knob packs from 5.1 to 8.9 Knobs per R$, so a 150-Knob escape is worth about 17 to 29 R$. Best sellers: not known.

## 7. Why it works

Doors won Best Use of Audio at the 2026 Roblox Innovation Awards ([GosuGamers](https://www.gosugamers.net/entertainment/news/79176-full-list-of-winners-at-the-roblox-innovation-awards-2026)) and keeps a 93.06% rating. Its monsters became plush toys (Screech, Dec 2022; Seek, May 2023) ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games)).

**Our read:**
- Every threat is learnable in one death: one tell, one counter, one hint line.
- Damage follows warning length, and Rush only spawns where a closet exists, so deaths feel earned.
- Random spawn timing and fake tells keep a known rule set tense.
- Difficulty is placed late: half of joiners beat Rush, 1 in 37 finishes the Hotel.
- A failed run still pays, so death leads to the next elevator.

## 8. What went wrong

- Players now are 4.0% of the January 2023 peak, which came the day after Hotel+.
- Major updates come one or two a year, and counts fall between them.
- Threats were retuned after launch. Ambush's returns dropped from up to 12 before Hotel+, to 6 before the Mines, to at most 3. The revive window grew from 30 seconds to 2 or 5 minutes ([Ambush](https://doors-game.fandom.com/wiki/Ambush), [Revives](https://doors-game.fandom.com/wiki/Revives)).
- The biggest badge drop is between Rush and Seek: 35% of Rush survivors survive Seek.

## 9. What to take from it

- Each threat: one tell, one counter, a fixed damage number on 100 HP; long warnings kill, short ones take 40.
- First threat from room 3, then about one per 10 rooms, never in a room without a hiding spot or in the 2 rooms after a chase.
- A chase of 6 to 8 rooms in each half of a 100-room floor, after 2 to 5 rooms of warning.
- Hiding limited to about 12 s, then 40 damage and a 10 s lockout.
- Soft currency of 1 per room and 50 per floor against first items at 50.
- Revives at 19 to 40 R$, blocked during a threat and at the finale, costing the run's door reward; a second and third in one run cost 60 and 120 R$ [data, Nov 2026].

## Sources

- [Doors wiki](https://doors-game.fandom.com/wiki/Rush): Rush, Ambush, Seek, Figure, Hide, Void, Knobs, Shops, Revives, Modifiers, Updates, Guiding Light
- [OP.GG Doors floors](https://op.gg/roblox/wiki/doors/floors) and [items](https://op.gg/roblox/wiki/doors/items)
- [Roblox games API](https://games.roblox.com/v1/games?universeIds=2440500124) and [badges API](https://badges.roblox.com/v1/universes/2440500124/badges?limit=100&sortOrder=Asc), 25 Nov 2026
- [Rolimons](https://www.rolimons.com/game/6516141723), [Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games)
