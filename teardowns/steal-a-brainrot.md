# Steal a Brainrot

> Buy meme characters off a shared carpet, earn from them at a base, lock it, and steal from the neighbours. The first Roblox game past 25 million concurrent players, and the template for [steal-and-defend](../genres/steal-and-defend.md).

| | |
|---|---|
| Studio | SpyderSammy (Spyder Games), owned by DoBig Studios ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot)) |
| Released | 16 May 2025 |
| Genre | Steal and defend |
| Peak concurrent players | 25.4M to 25.9M, 11 Oct 2025 ([PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players/); 25,836,222 per the [wiki](https://stealabrainrot.fandom.com/wiki/Steal_a_Brainrot_(Game)); 25,868,678 per [RoVitals](https://rovitals.com/game/109983668079237) citing Guinness) |
| Players now | 42,139 (Roblox public API, 25 Nov 2026, 13:53 UTC); 729K on Saturday 21 Nov 2026 |
| Players per server | 8 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Buy | Pays for a unit on the carpet | not known | Units walk from a cave and vanish at the far end | Price $25 to $650B |
| Walk home | Waits | not known | Anyone can buy it out for 150% until it arrives | |
| Earn | Nothing | 1 s ticks | Cash at the plot | $1/s to $600M/s |
| Lock | Presses the base button | 60 s +10 per rebirth | Shield | |
| Steal | Carries a unit from an unlocked base | not known | Owner alarm; thief slowed 41%; broadcast on success | |
| Rebirth | Pays cash plus named units | about 32 min to the first (below) | New floor at R2, R10 | Multiplier +1 |

Cycle time is one payback: 25 to about 300 seconds ([AllThings.How](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/), our arithmetic). The dead time inside it is filled by locking, stealing and defending.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Spawn by a free base of 10 slots, next to the carpet ([wiki](https://stealabrainrot.fandom.com/wiki/Base)) |
| 0:10 to 1:00 | An arrow and a "go buy a Noobini" prompt, the only scripted step found ([wiki](https://stealabrainrot.fandom.com/wiki/Noobini_Pizzanini)). Noobini costs $25, earns $1/s, pays back in 25 s. Join protection ends at 0:30 ([wiki](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing)) |
| 1:00 to 5:00 | Lirilì Larilà ($250) at about 1.5 to 4 min; Tim Cheese ($500) at about 4 min; a Legendary guaranteed by 5:00 |
| 5:00 to 15:00 | Rares ($2K to $9K); a Mythic guaranteed by 15:00 |

Starting cash: not known. The 1:00 to 15:00 timings are our reconstruction. First rare moment: a Gold, Diamond or Rainbow roll on the carpet (10%, 5%, 1%). First long goal: rebirth 1, $500K plus Trippi Troppi and Gangster Footera. Our arithmetic, from an idealised simulation (greedy buys, 10 slots, every unit always on the carpet, no theft): about 32 minutes to $500K, or three to four 9-minute sessions.

## 3. Progression

**Carpet units, base income** ([AllThings.How, 9 Nov 2026](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/); payback our arithmetic). The full ladder is in [slop/01-anatomy.md](../slop/01-anatomy.md); two rungs it leaves out:

| Rarity | Unit | Price | Income/s | Payback (s) |
|---|---|---|---|---|
| Legendary | Burbaloni Loliloli | $35K | $200 | 175 |
| OG (event only) | Meowl | $650B | $600M | 1,083 |

**Carpet shares**, our arithmetic from the wiki's weights, total about 590 ([wiki](https://stealabrainrot.fandom.com/wiki/Red_Carpet)): Common 62.7%, Rare 25.1%, Epic 11.0%, Legendary 1.0%, Mythic 0.23%, Brainrot God 0.020% (1 in 5,000), Secret about 1 in 1.4 million. Noobini alone is about 17%. Pity: Legendary within 5 min, Mythic within 15, God within about 45 (the wiki's estimate). The wiki's mutation weights on the carpet (Gold 7, Diamond 3, Rainbow 0.2) do not reproduce the published 10/5/1% odds unless the no-mutation weight is known; copies in existence (Noobini: 10.2% Gold, 5.0% Diamond, 0.9% Rainbow) fit 10/5/1.

**Catalogue** by 21 Oct 2026: Common 12, Rare 12, Epic 21, Legendary 26, Mythic 42, Brainrot God 107, Secret 354, OG 7 ([Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/rarities)).

**Slots and sell-back.** 10 on floor 1; 11 to 18 on floor 2 (R2 to R9); 19 to 25 on floor 3 (R10 to R19). Selling returns 50%. Each completed index entry adds +0.5x ([Cash](https://stealabrainrot.fandom.com/wiki/Cash)).

**Rebirths** ([Bloxodes, 17 Nov 2026](https://bloxodes.com/wiki/steal-a-brainrot/rebirths)): R1 $500K (x0.5), R2 $1.5M, R3 $12.5M, R4 $35M, R5 $100M, R7 $1B, R10 $125B, R15 $100T, R19 $30Qa (x19). Each: +1 multiplier, +10 s lock, +1 slot from R2, new gear, a cash bonus from $5K (R1) to $250T (R19) ([Beebom](https://beebom.com/steal-a-brainrot-rebirth-guide-levels-and-rewards/)). Beebom gives multipliers one step higher (x1 at R1). The wiki's game page says 20 rebirths; the dated tables stop at 19, and the cap reached R19 at Update 62 ([wiki](https://stealabrainrot.fandom.com/wiki/Update_Log)). Cash ratios, our arithmetic: x3, x8.3, x2.8, x2.9, then about x3 to x5 per step.

**Gear ladder by rebirth** (40 items; [wiki](https://stealabrainrot.fandom.com/wiki/Gears)):

| Unlocked at | Items and prices |
|---|---|
| Join | Free bat |
| R0 | Slap $500; Speed Coil $750 (speed 34 to 51); Trap $1K (7 s freeze, at most 5) |
| R1 | Iron Slap $2.5K, Gravity Coil $3K, Bee Launcher $10K |
| R2 / R3 | $15K to $25K / $50K to $100K |
| R4 | $200K to $500K, including Boogie Bomb (target drops the unit) |
| R5 / R6 to R9 | $1M to $5M / $1.5M to $20M |
| R10 to R15 | $25M to $700M |
| Top | Grief Shield $10B |

Only 3 items need no rebirth.

## 4. Session and return hooks

- Pity timers at 5, 15 and 45 minutes.
- Seasonal events every 2 hours on weekdays and every hour at weekends. An hourly "Admin Machine" was tried; the wiki calls it a failure ([wiki](https://stealabrainrot.fandom.com/wiki/Hourly_Events)).
- Updates every Saturday: Update 1 on 31 May 2025 to Update 75 on 14 Nov 2026, 75 updates in 77 weeks ([wiki](https://stealabrainrot.fandom.com/wiki/Update_Log)). Update 76 is dated "October 21, 2026", almost certainly a typo for 21 November.
- Twelve limited mutations, x2 (Bloodrot, 7 Jun 2025) to x14 (Eclipse, 3 Oct 2026), all launched on Saturdays, returning only in admin events or reruns ([Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/mutations)).
- Offline income: the wiki contradicts itself. The Cash page says about 50%; the [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash) page says about 3% capped at 5 hours, and its own example (a day offline equals about 43 minutes online) is 3% of 24 hours, which ignores the cap. Not known.
- A Bruno Mars concert in January 2026 drew a reported 12.8M ([GamesIndustry.biz](https://www.gamesindustry.biz/roblox-claims-bruno-mars-steal-a-brainrot-performance-drew-a-record-128-million-concurrent-users-issued-54-million-brainrot-collectibles)).

## 5. Other players

Every base is in view. Lock 60 s, +10 per rebirth, +10 with VIP; 30 s join protection. A carrier drops from speed 34 to 20 and jump 7.2 to 4.32 and cannot use gear; the owner hears an alarm naming the unit; a success is broadcast in the rarity's colour; one unit (Spyder Elephant) cannot be stolen ([wiki](https://stealabrainrot.fandom.com/wiki/Stealing)). The Trade Plaza (Update 54, 20 Jun 2026) bans stealing inside and has three tiers: normal, Pro (25B/s income) and OG (100B/s plus an OG unit). It replaced the Trade Machine of Update 39 ([wiki](https://stealabrainrot.fandom.com/wiki/Trade_Plaza)). Clips of thefts reached tens of millions of views ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)).

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| 2x Money | Pass | 299 | Doubles income |
| VIP | Pass | 375 | Includes +10 s lock |
| Admin Commands | Pass | 7,999 | Server-admin powers |

Passes from the Roblox public API, 25 Nov 2026; the snapshot has these 3 and no others [data, Nov 2026].

**Developer products [data, Nov 2026].** The snapshot reads 300, its cap, and only 118 are on sale with a price. Without 12 named "DISABLED PRODUCT" at 999,999,999 R$, one unnamed item and 22 gift copies, 83 remain, 19 to 11,992 R$, median 99 R$. 34 of them skip an egg timer. 12 of 83:

| Product | R$ | Kind |
|---|---|---|
| Cash Pack #1 | 59 | Cash ladder, step 1 of 5 |
| Cash Pack #5 | 2,499 | Step 5 (steps 2 to 4: 379, 659, 1,249) |
| StarterPack | 189 | Starter |
| 2x Server Luck | 249 | Luck for the whole server |
| 8x Server Luck | 2,999 | (4x: 999) |
| 1x Spin (Hacker Wheel) | 99 | Spin; 3 wheels sold the same way |
| 10x Spin (Hacker Wheel) | 499 | (3x: 199) |
| +1 Secret Lucky Block | 1,499 | Lucky block |
| +8 Secret Lucky Block | 11,992 | Top price in the list |
| Skip Timer - Craburger Egg | 19 | Egg timer skip, cheapest |
| Skip Timer - Cerberus Egg | 199 | Egg timer skip, dearest |
| +10 Speed | 229 | Speed (+1: 39, +5: 99) |

Cash amounts are not in the names or descriptions, so cash per Robux cannot be computed. Our arithmetic: Pack 5 costs 42 times Pack 1; a spin costs 99 R$ singly and 49.9 in tens; 8 Secret Lucky Blocks cost exactly 8 times one (1,499 each), so that ladder has no bulk discount; server luck doubles in power as the price roughly triples or quadruples.

Purchases were estimated at US$64M by March 2026 ([Bloomberg via The Star](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators)). Best sellers: not known.

## 7. Why it works

It won Best Creative Direction at the 2025 Roblox Innovation Awards ([Variety](https://variety.com/2025/gaming/news/grow-a-garden-roblox-innovation-awards-2025-winners-1236510387/)). Approval 85.1% (Roblox public API). The developers have not explained their design in the sources read.

**Our read:**

- The payback stays at 25 to 300 s from $25 to $80M, so buying never stops paying.
- Every rebirth hands over tools for acting on other players; 37 of 40 gear items sit behind rebirths.
- The 150% buy-out puts a fight on the carpet as well as in the bases.
- The pity timers promise every 9-minute session at least one Legendary.

The "why" behind each is argued in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md).

## 8. What went wrong

- Pay-to-win: the best items and admin powers sold for Robux ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot)).
- About 200 public cheat scripts for auto-collect and auto-steal ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)).
- Tung Tung Tung Sahur was removed in September 2025 over a licensing dispute and restored on 29 Nov 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot)).
- The fall: 25.4M to 42,139 on a weekday morning (0.17%). 30-day average 109,632 in 2026, down 20.4% ([RoVitals](https://rovitals.com/game/109983668079237)).

## 9. What to take from it

- A shared shop with published weights: top regular tier 1 in 5,000, guaranteed every 45 minutes.
- A 150% buy-out on a unit walking home.
- 10 starting slots, 50% sell-back, a new floor at rebirths 2 and 10.
- A 60-second lock, +10 per rebirth; 30-second join protection.
- A carrier at 59% speed with no gear, and a free bat for every defender.
- A first rebirth at about 32 minutes of ideal play, needing two named units.
- Server-wide luck for sale at 2x, 4x and 8x for 249, 999 and 2,999 R$, so one buyer lifts the odds for everyone in the server [data, Nov 2026].

## Sources

[Steal a Brainrot wiki](https://stealabrainrot.fandom.com/wiki/Steal_a_Brainrot_(Game)): [Base](https://stealabrainrot.fandom.com/wiki/Base), [Red Carpet](https://stealabrainrot.fandom.com/wiki/Red_Carpet), [Noobini Pizzanini](https://stealabrainrot.fandom.com/wiki/Noobini_Pizzanini), [Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash), [Gears](https://stealabrainrot.fandom.com/wiki/Gears), [Stealing](https://stealabrainrot.fandom.com/wiki/Stealing), [Methods of stealing](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing), [Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log), [Hourly Events](https://stealabrainrot.fandom.com/wiki/Hourly_Events), [Trade Plaza](https://stealabrainrot.fandom.com/wiki/Trade_Plaza). [Bloxodes rebirths](https://bloxodes.com/wiki/steal-a-brainrot/rebirths), [rarities](https://bloxodes.com/wiki/steal-a-brainrot/rarities), [mutations](https://bloxodes.com/wiki/steal-a-brainrot/mutations). [AllThings.How](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/), [Beebom](https://beebom.com/steal-a-brainrot-rebirth-guide-levels-and-rewards/), [Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot), [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players/), [RoVitals](https://rovitals.com/game/109983668079237), [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/), [Bloomberg via The Star](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators). Roblox public API (games, game passes), 25 Nov 2026.
