# Anatomy of a slop hit

The big slop games of 2025 and 2026 are built from the same parts. This page lays the parts out with the real numbers so they can be compared and reused. Player counts marked "now" are from Roblox's public API on Wednesday 25 November 2026 at 13:53 UTC, a weekday morning in the US, so they sit near each game's daily low.

## The hits, side by side

| Game | Created | Players per server | Peak concurrent | Now | Session | Game passes |
|---|---|---|---|---|---|---|
| Grow a Garden | 26 Mar 2025 | 4 | 22.3M (23 Aug 2025) | 18K | about 21 min | 1, off sale |
| Steal a Brainrot | 16 May 2025 | 8 | 25.4M (Oct 2025) | 42K | about 9 min | 3: 2x Money 299 R$, VIP 375, Admin Commands 7,999 |
| Escape Tsunami For Brainrots | 15 Dec 2025 | 8 | 4.1M to 5.0M, early 2026 (trackers disagree) | 3.8K | not known | from 129 to 888 R$ |
| +1 Speed Keyboard Escape | 18 Jan 2026 | 22 | 4.0M to 6.1M (trackers disagree) | 19K | about 9 min | about 50 cosmetic, 19 to 2,999 R$ |
| Kick a Lucky Block | 7 Apr 2026 | 5 | about 533K (15 Aug 2026) | 12K | not known | 6, from 99 to 729 R$ |
| Steal An Egg | 25 Jul 2026 | 7 | 14.3M (19 Sep 2026) | 852K | about 17 min | 2: x2 Money 299, x2 Growth Speed 467 |
| Throw Food For Animals | 18 Sep 2026 | 5 | 2.47M (14 Nov 2026) | 237K | about 17 min | 2: x2 Cash 99, x2 Training Power 149 |

Sources: created dates, server sizes, "now" and passes from Roblox's public game and game-pass endpoints (25 Nov 2026). Peaks from [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden), [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players/), [RoStats records](https://rostats.io/records), [RoVitals](https://rovitals.com/) and Rolimons. Session lengths are tracker estimates from RoVitals and Rolimons.

Three things to notice before the detail:

- **Server sizes are tiny.** Every collect-and-steal game holds 4 to 8 players. Only the race game holds 22.
- **Pass lists are short.** The two biggest hits of late 2026 sell two passes each. The money is in products that can be bought again (speed, restocks, lucky blocks, seed packs). Across the charts the median top-100 game lists 57 such products against 5 passes [data, Nov 2026] ([data/ANALYSIS.md](../data/ANALYSIS.md)); each game's own list is in its teardown.
- **Sessions are 9 to 21 minutes.** These are short-visit games that people open many times.

## Skeleton A (2025): buy, place, earn, protect

This is Steal a Brainrot. Grow a Garden is the same skeleton with waiting in place of theft.

| Step | Steal a Brainrot | Grow a Garden |
|---|---|---|
| Get a unit | Buy it from a conveyor every player on the server can see | Buy a seed when the shop restocks (every 5 minutes) |
| Place it | It goes on a plot in your base | Plant it in your plot |
| It earns | Cash per second, forever | It grows, then you harvest and sell it |
| Spend | Buy a rarer unit; a full base forces you to replace weak units | Buy rarer seeds, gear, eggs |
| The risk | Any player can walk in and carry a unit away unless your base is locked | A paid item lets other players steal crops; otherwise the "risk" is missing a restock |
| Reset | Rebirth: pay cash plus named units, get a multiplier, a slot, a longer lock, a new tool | Ascension, once every 4 hours |

Sources: [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot), [Steal a Brainrot wiki: Rebirth](https://stealabrainrot.fandom.com/wiki/Rebirth), [Bloxodes: Grow a Garden shops](https://bloxodes.com/wiki/grow-a-garden/shops), [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden).

## Skeleton B (2026): train, reach, carry home, earn

Steal An Egg, Throw Food For Animals, Kick a Lucky Block, Escape Tsunami and +1 Speed Keyboard Escape all use this one.

| Step | What happens | Steal An Egg | Throw Food For Animals |
|---|---|---|---|
| Train a stat | A number goes up from a trivial input | Speed, on a treadmill in your base | Throw Power, on pull-up stands |
| Reach a farther zone | The stat is the key to the next area | 15 biomes, gated by Speed | 19 areas, reached by throwing farther |
| Bring back a collectible | The trip home is the danger | Grab an egg and run it home before the guardian or another player knocks you down | Throw food; the animal it attracts goes to your pen |
| It earns | Income per second at your base | Pets earn $1 a second up to $5 billion a second | Animals earn money in the pen |
| Spend | Better training gear, better base | Upgrade treadmill and base | Buy better food for rarer animals |

Sources: the games' own descriptions through Roblox's public API; [Bloxodes: Steal An Egg](https://bloxodes.com/wiki/steal-an-egg); [Bloxodes: Throw Food For Animals](https://bloxodes.com/wiki/throw-food-for-animals).

**Our read:** Skeleton B fixes the weakest part of Skeleton A. In A, the only thing to do between purchases is wait for money. In B the wait has a job (train) and the purchase has a trip (go out, come back with something), so there are two more verbs in the loop and one of them carries risk.

## The parts, with their numbers

### 1. A ladder priced by payback time

Steal a Brainrot's conveyor units, base versions:

| Rarity | Unit | Price | Income per second | Payback (seconds) |
|---|---|---|---|---|
| Common | Noobini Pizzanini | $25 | $1 | 25 |
| Common | Lirilì Larilà | $250 | $3 | 83 |
| Common | Tim Cheese | $500 | $5 | 100 |
| Common | Talpa Di Fero | $1K | $9 | 111 |
| Common | Pipi Kiwi | $1.5K | $13 | 115 |
| Rare | Trippi Troppi | $2K | $15 | 133 |
| Rare | Tric Trac Baraboom | $9K | $65 | 138 |
| Epic | Cappuccino Assassino | $10K | $75 | 133 |
| Epic | Wombo Rollo | $42.5K | $275 | 155 |
| Legendary | Sigma Boy | $325K | $1.35K | 241 |
| Mythic | Frigo Camelo | $350K | $2K | 175 |
| Mythic | Toiletto Focaccino | $4.85M | $16K | 303 |
| Brainrot God | Tralalero Tralala | $10M | $50K | 200 |
| Brainrot God | Appelini | $69M | $300K | 230 |
| Secret | La Vacca Saturno Saturnita | $80M | $325K | 246 |
| Secret (top) | Dragon Cannelloni | $250B | $250M | 1,000 |

Prices and income from [AllThings.How, updated 9 Nov 2026](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/). Payback is our arithmetic: price divided by income per second.

The first purchase in three of the hits:

| Game | Starting position | First purchase | Pays back in |
|---|---|---|---|
| Steal a Brainrot | A free base with 10 slots | Noobini Pizzanini, $25, about 1 in 6 of everything the conveyor sends out | 25 seconds |
| Grow a Garden | Carrot seeds always in stock | A carrot seed for 10; it grows in 8 seconds and sells for about 20 | 8 seconds |
| Plants vs Brainrots | $400 | Two $200 cactus seeds, which is exactly the starting money; each grows in 5 seconds | not known |

Sources: Steal a Brainrot wiki ([Base](https://stealabrainrot.fandom.com/wiki/Base), [Red Carpet](https://stealabrainrot.fandom.com/wiki/Red_Carpet)); Grow a Garden wiki ([Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop)); Plants vs Brainrots wiki ([Cactus](https://plantsvsbrainrots.fandom.com/wiki/Cactus)), which may describe the launch version. The 1-in-6 share is our arithmetic from the wiki's spawn weights.

Price runs from $25 to $250 billion, a factor of ten billion. Payback runs from 25 seconds to about 300 seconds for everything below the very top, a factor of twelve. **Our read:** this is the most important table in the section. The designer did not let price outrun income. A unit always pays for itself in a few minutes at most, so buying never stops feeling worth it, at any level of wealth. Design the ladder by payback time and let the prices fall out of it. [04-build-it.md](04-build-it.md) shows how.

### 2. About ten rarity tiers, each roughly ten times the last

- Steal a Brainrot: 8 tiers (Common, Rare, Epic, Legendary, Mythic, Brainrot God, Secret, OG). Income spans $1 to $600M a second. By October 2026 the Secret tier alone held 354 units out of about 580 ([Bloxodes rarities](https://bloxodes.com/wiki/steal-a-brainrot/rarities)).
- Steal An Egg: 10 tiers, Common at $1 to $3 a second up to Eternal at $65M to $5B, 150 pets ([Bloxodes pets](https://bloxodes.com/wiki/steal-an-egg/pets)).
- Grow a Garden: 609 crops, 461 pets, 83 eggs by November 2026 ([Bloxodes index](https://bloxodes.com/wiki/grow-a-garden)).

New content goes in at the top. That is why the top tiers are so crowded.

### 3. A second roll on every unit

| Game | No upgrade | Upgrades and odds | Source |
|---|---|---|---|
| Steal a Brainrot | 84% | Gold x1.25 at 10%, Diamond x1.5 at 5%, Rainbow x10 at 1% | [Bloxodes mutations](https://bloxodes.com/wiki/steal-a-brainrot/mutations) |
| Throw Food For Animals | 79.5% | Gold x1.5 at 13%, Diamond x3 at 4%, Emerald x5 at 2%, Ruby x10 at 1%, Rainbow x20 at 0.5% | [Bloxodes mutations guide](https://bloxodes.com/articles/throw-food-for-animals-mutations-guide) |
| Grow a Garden | not published | Silver x5, Gold x20, Rainbow x50, plus weather mutations from x2 up to x365 | [Bloxodes calculator](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator) |

The rarity of the unit and the mutation on it are two separate rolls. A common unit with a rare mutation can be worth more than a rare unit without one, so no purchase is ever certain to be boring.

### 4. Zone gates that multiply

Steal An Egg's Speed gates: none, 900, 10K, 40K, 170K, 700K, 2.5M, 18M, 150M, 700M, 2.5B, 7B, 20B, 50B, 250B ([Bloxodes biomes](https://bloxodes.com/wiki/steal-an-egg/biomes)). Each gate is about 3 to 10 times the one before.

### 5. Clocks

| Clock | Game | What happens |
|---|---|---|
| 5 minutes | Grow a Garden | Seed shop and gear shop restock |
| 30 minutes | Grow a Garden | Egg stock changes |
| 30 minutes | Steal An Egg (Turkey event) | Boss appears at :15 and :45 past the hour and stays 5 minutes |
| 60 minutes | Grow a Garden | Event-currency shop restocks |
| 4 hours | Grow a Garden | Ascension becomes available again |
| 24 hours | Grow a Garden | Daily deals; first plot expansion finishes |
| 7 days | All of them | The Saturday event |

Sources: [Bloxodes: Grow a Garden shops](https://bloxodes.com/wiki/grow-a-garden/shops), [Bloxodes: Turkey Takeover guide](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide).

### 6. A reset that adds more than a multiplier

Steal a Brainrot's first rebirths ([wiki](https://stealabrainrot.fandom.com/wiki/Rebirth), read 25 Nov 2026):

| Rebirth | Cash | Units you must own | Multiplier | Lock | Slots | New tools |
|---|---|---|---|---|---|---|
| 1 | $500K | Trippi Troppi, Gangster Footera | x0.5 | +10 s | none | Iron Slap, Gravity Coil, Bee Launcher |
| 2 | $1.5M | Boneca Ambalabu, Brr Brr Patapim | x1 | +10 s | +1 and a second floor | Gold Slap, Coil Combo, Rage Table |
| 3 | $12.5M | Trulimero Trulicina, Chimpanzini Bananini | x2 | +10 s | +1 | Diamond Slap, Grapple Hook, Taser Gun |
| 4 | $35M | Chef Crabracadabra, Glorbo Fruttodrillo | x3 | +10 s | +1 | Emerald Slap, Invisibility Cloak, Boogie Bomb |
| 5 | $100M | Frigo Camelo, Orangutini Ananassini | x4 | +10 s | +1 | Ruby Slap, Medusa's Head |
| 10 | $125B | Girafa Celestre | x9 | +10 s | +1 and a third floor | Glitched Slap, Body Swap Potion |
| 19 | $30Qa | La Grande Combinasion | x19 | +10 s | +1 | Grief Guard |

Four things to copy from this table:

- The cash cost multiplies by 3 to 10 each step. The multiplier only adds 1. The reset gets harder much faster than it gets stronger.
- Each rebirth needs **named units**, so the player has to hunt specific characters. "Get more money" becomes "find a Trippi Troppi".
- Each rebirth gives **something to do**: a new slap, a grapple hook, a taser. These are tools for bothering other players.
- Each rebirth gives **something others can see**: a second floor at rebirth 2, a third at rebirth 10.

The wiki also records that the first rebirths were made cheaper after launch (rebirth 1 was $1M, rebirth 2 was $3M). The first reset is the one most players never reach, and the developers moved it closer.

### 7. One live hour a week

On Saturday 21 November 2026 every tracked slop hit peaked at once ([RoVitals](https://rovitals.com/)):

| Game | Saturday peak | Normal level that week | Ratio |
|---|---|---|---|
| Steal An Egg | 6.84M | about 650K | about 10x |
| Throw Food For Animals | 2.45M | about 230K | about 11x |
| Steal a Brainrot | 729K | about 37K | about 20x |
| +1 Speed Keyboard Escape | 653K | about 18K | about 36x |
| Kick a Lucky Block | 139K | about 10K | about 14x |
| Grow a Garden | 68.5K | about 15K | about 5x |

Every record in this genre was set on a Saturday: Grow a Garden's 21.3M (21 June 2025) and 22.3M (23 August 2025), Steal An Egg's 14.3M (19 September 2026). Steal a Brainrot's update log runs from Update 1 on 31 May 2025 to Update 75 on 14 November 2026: 75 Saturday updates in 77 weeks ([wiki: Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log)). Throw Food For Animals' events start at 6 AM Pacific time and some last only 30 to 60 minutes ([Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals)).

### 8. Almost nothing to read

Each hit's store description is a list of five to seven short lines, each starting with a verb. Steal a Brainrot's whole "how to play" is: buy, steal, generate money, rebirth, troll. None of the hits has a tutorial that the research could find.

### 9. A shared shop with weights, announcements and a guarantee

Steal a Brainrot's conveyor (the "Red Carpet") is one shop for the whole server. Units walk out of a cave, cross the carpet and vanish at the far end. Everyone sees the same units and the first to pay gets one ([wiki: Red Carpet](https://stealabrainrot.fandom.com/wiki/Red_Carpet)).

| Rule | Value |
|---|---|
| Share of spawns by rarity (our arithmetic from the wiki's weights) | Common about 63%, Rare 25%, Epic 11%, Legendary 1%, Mythic 0.23%, Brainrot God 0.02% (about 1 in 5,000) |
| Guarantee | A Legendary within 5 minutes, a Mythic within 15, a Brainrot God within about 45 (the last is the wiki's estimate) |
| Announcement | Brainrot God and Secret spawns are announced to the server |
| After you buy | The unit walks to your base. Until it arrives, any player can buy it out from under you for 150% of the price |
| Selling | Returns 50% of the price ([wiki: Cash](https://stealabrainrot.fandom.com/wiki/Cash)) |
| Slots | 10 on the first floor, up to 18 with the second floor (rebirth 2), up to 25 with the third (rebirth 10) ([wiki: Base](https://stealabrainrot.fandom.com/wiki/Base)) |

Steal An Egg's top pet in each late biome has the same odds, 0.02% ([wiki: Drop Rates](https://stealanegg.fandom.com/wiki/Drop_Rates)).

**Our read:** the guarantee matters as much as the odds. Pure chance at 1 in 5,000 could leave a server dry for hours. The timers promise every server a Legendary every 5 minutes and a Mythic every quarter of an hour, so something worth running for always arrives inside one session.

## The loop stack of a slop hit

A game holds attention when something finishes at every time scale ([foundations/04-core-loop.md](../foundations/04-core-loop.md)). This is how the slop hits fill each one:

| Every | What finishes | Example |
|---|---|---|
| 1 second | A cash tick | Steal a Brainrot income per second |
| 25 to 300 seconds | A unit pays for itself; the next one becomes affordable | The payback column above |
| 1 minute | The base lock runs out | Steal a Brainrot: 60 seconds, plus 10 per rebirth ([wiki](https://stealabrainrot.fandom.com/wiki/Base)) |
| 5 minutes | The shop restocks; a Legendary is guaranteed | Grow a Garden seed shop, Steal An Egg eggs, Steal a Brainrot conveyor |
| 15 minutes | A Mythic is guaranteed | Steal a Brainrot conveyor |
| 30 to 60 minutes | A rare shop or a boss appears | Egg stock, event boss |
| One session (9 to 21 minutes) | A new tier, a new zone, or a rebirth | Tracker session lengths above |
| Away from the game | Crops grow, units keep earning | Grow a Garden offline growth |
| One day | Daily deals, a plot expansion finishing | Grow a Garden |
| One week | The Saturday event and its limited item | All of them |

No row is empty. That is the anatomy.

Next: [02-why-it-holds.md](02-why-it-holds.md) explains why each part works and how to build it.
