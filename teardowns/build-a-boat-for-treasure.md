# Build a Boat for Treasure

> Build a boat from blocks, launch it down a river of stages, and earn gold for every stage it survives. It shows how to wrap a free building toy in one clear goal, and it has done so since 2016.

| | |
|---|---|
| Studio | Chillz Studios |
| Released | Place made 2 Nov 2016 (Roblox public API) |
| Genre | Building sandbox; see [genres/sandbox.md](../genres/sandbox.md) |
| Peak concurrent players | Not known |
| Players now | 10,008 (Roblox public API, 25 Nov 2026) |
| Players per server | 7 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Visits 5,265,307,439; favourites 8,582,029; votes 93.4% up; last updated 17 Nov 2026 (Roblox public API, 25 Nov 2026).

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Build | Places blocks on the team plot (about 95 x 128 to 119 x 113 studs by team colour) | not known | The boat takes shape | Blocks left in inventory |
| Launch | Starts the voyage | not known | The plot turns to water ([Building Space](https://build-a-boat-for-treasure.fandom.com/wiki/Building_Space)) | none |
| Sail | Steers through stages graded green, yellow, red, purple | not known | Hazards break blocks off | +8 gold at the black wall ending each stage |
| Treasure | Reaches the end | not known | Treasure chest | +25 gold |
| Spend | Buys blocks or chests | not known | New blocks | Gold down |

Gold from the [Gold](https://build-a-boat-for-treasure.fandom.com/wiki/Gold) wiki page. Cycle time is not known: no source gives the length of one voyage. The wiki's theoretical rush rate assumes a 7-second chest cycle, 54,000 gold an hour (122,000 with both boosts), which is a ceiling for a boat built only to rush. Dead time: not known. **Our read:** the build phase has no dead time, because the player is always placing; the voyage may have some once the boat is set on course.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Joins with 10 gold and 8 free blocks ([Gold](https://build-a-boat-for-treasure.fandom.com/wiki/Gold), [Wood Block](https://build-a-boat-for-treasure.fandom.com/wiki/Wood_Block)) |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | not known |
| 5:00 to 15:00 | not known |

First reward: 8 gold at the end of the first stage. First purchase: 10 gold buys two Common chests or two Wood blocks. First long goal shown: the Treasure at the end of the river. Quests for newer players pay 100 gold and 25 balloon blocks (Cloud), 300 gold and a ball (Soccer), 450 gold and 25 glue (Find Me) ([main page](https://build-a-boat-for-treasure.fandom.com/wiki/Build_A_Boat_For_Treasure)). How the first build is taught: not known. No source describes it.

## 3. Progression

Gold per run ([Gold](https://build-a-boat-for-treasure.fandom.com/wiki/Gold)):

| | Base | Group member | Gold Multiplier pass | Both |
|---|---|---|---|---|
| Per stage | 8 | 10 | 16 | 18 |
| Treasure | 25 | 32 | 50 | 57 |
| Full run (entrance, 9 stages, Treasure) | about 105 | | | 237 |

Shop block price found: Wood, 50 for 250 gold (5 each). 202 blocks have existed, up to 165 permanent ([Blocks](https://build-a-boat-for-treasure.fandom.com/wiki/Blocks)). Prices of other blocks: not known.

Chests ([Bloxodes](https://bloxodes.com/wiki/build-a-boat-for-treasure/chests)); runs to afford is our arithmetic at 105 gold per run:

| Chest | Gold | Material pulls | Decorations | Abilities | Runs to afford |
|---|---|---|---|---|---|
| Common | 5 | 1 | 1 | 0 | 0.05 |
| Uncommon | 15 | 4 | 1 | 0 | 0.14 |
| Rare | 45 | 12 | 2 | 1 | 0.43 |
| Epic | 135 | 38 | 4 | 2 | 1.3 |
| Legendary | 405 | 120 | 8 | 4 | 3.9 |

Odds from the same page (it notes some rows do not sum to 100%): Common materials Wood 25%, Fabric 25%, Stone 15%. Rare materials Concrete 35%, Marble 25%; Rare abilities Cannon, Switch, Piston 17% each. Epic materials Concrete 35%, Coal 35%, Titanium 20%; abilities 12% to 13% each, including Thruster. Legendary Brick 40%, Titanium 35%, Obsidian 25%; abilities 11% to 12% each, including Harpoon.

Expected value (our arithmetic):

| Wanted | From | Expected gold per item | Runs per item |
|---|---|---|---|
| Titanium | Legendary | 9.6 | 0.09 |
| Cannon | Rare | 265 | 2.5 |
| Thruster | Epic | about 540 | 5.1 |
| Harpoon | Legendary | about 880 | 8.4 |

The ladder: chest price triples each tier. A Rare chest costs 0.43 runs and holds the first ability block. A Legendary costs about 4 runs. The 42 stages include 5 seasonal ones and one extreme stage ([Earnaldo, promotional](https://earnaldo.com/blog/build-a-boat-for-treasure-beginner-guide)). No rebirth or prestige is in the sources.

## 4. Session and return hooks

Quests (100 to 450 gold). Seasonal stages (5 of 42). Badge ladder of run counts, with thresholds not known ([badges, Roblox public API, 25 Nov 2026](https://badges.roblox.com/v1/universes/210851291/badges?limit=100)):

| Badge | Awards | Share of Treasure Hunter (our arithmetic) |
|---|---|---|
| Treasure Hunter | 121,204,505 | 100% |
| Master Boater | 72,224,899 | 60% |
| Treasure Expert | 64,604,887 | 53% |
| Treasure Master | 35,441,725 | 29% |
| Challenge Winner | 4,724,348 | 4% |

**Our read:** each step of the Treasure badge ladder keeps a little over half the players of the step before.

Daily rewards, offline progress, restocks, update day: not known.

## 5. Other players

7 players per server, on team plots. Group perks on the game page: Member +25% gold, Mega Member +300% health, Royal Member +4 barrels of TNT (Roblox public API, 25 Nov 2026). Trading, stealing and leaderboards: not known. **Our read:** the clip is the launch, when a boat sails or falls apart in front of the server.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Gold Multiplier | Pass | 500 | Stage gold 8 to 16, Treasure 25 to 50 |
| Fox Character | Pass | 250 | Cosmetic character |
| Penguin Character | Pass | 250 | Cosmetic character |
| Chicken Character | Pass | 250 | Cosmetic character |
| Extra save slot | Product | 100 each ([Earnaldo, promotional](https://earnaldo.com/blog/build-a-boat-for-treasure-beginner-guide); confirmed [data, Nov 2026]) | One more saved boat |

Pass prices: Roblox public API, 25 Nov 2026, and the snapshot matches them; three old Saving Slot passes are off sale [data, Nov 2026]. The group bonus does not stack with the Gold Multiplier, per the promotional guide, but the wiki gives 18 gold per stage with both. Best sellers: not known. Chests are bought with gold, which is earned in play and also sold as products.

Products [data, Nov 2026]: 21 on sale, 5 to 2,000 R$, median 250, plus a "[Gift]" copy of most of them at 1.5 times the price. 12 of 21:

| Product | R$ | Note |
|---|---|---|
| 50 Gold | 5 | 10 gold per R$ |
| 300 / 1050 / 7700 Gold | 30 / 100 / 700 | |
| 23k Gold | 2,000 | 11.5 gold per R$: 15% more (our arithmetic) |
| +1 Saving Slot | 100 | |
| +100 Wood / Glass / Neon Blocks | 50 / 100 / 300 | |
| +5 Harpoons | 200 | |
| +3 Ultra Boat Motors | 250 | One of 9 part packs at 250 |
| +3 Sonic Jet Turbines | 500 | |

**Our read:** at about 11 gold per R$, the top 405-gold chest costs about 37 R$ and a full run's 105 gold about 10 R$. Robux buys parts and blocks in packs of 3 to 100, never a finished boat.

## 7. Why it works

No developer statement was found. Players vote 93.4% up. **Our read:**

- The player can build any shape, but the goal (reach the Treasure) never changes. Every build gets a test with a score: stages survived.
- One stage pays 8 gold and the cheapest chest costs 5, so even a boat that sinks after one stage buys something.
- Abilities (Cannon, Thruster, Harpoon) sit in Rare and higher chests, 2.5 to 8.4 runs away. Each run funds the part that makes the next run farther.
- The only multiplier sold is 2x gold; the building itself is never sold.

## 8. What went wrong

Not known. The sources record no economy break or failed update. The Treasure's payout is described two ways (flat 25, or by speed), so its current rule is unverified.

## 9. What to take from it

- Start with enough currency for 2 of the cheapest items: 10 gold against a 5-gold chest.
- Pay at every checkpoint: 8 gold per stage, so a failed run still buys something.
- A full run worth about 20 cheapest items: 105 gold against 5.
- A 5-tier chest ladder that triples in price: 5, 15, 45, 135, 405.
- The first special part in the third tier, about 2.5 runs away (Cannon from a 45-gold chest).
- Sell one 2x multiplier at 500 R$, and never the act of building.

## Sources

- Roblox public API, 25 Nov 2026: [game](https://games.roblox.com/v1/games?universeIds=210851291), [passes](https://apis.roblox.com/game-passes/v1/universes/210851291/game-passes?passView=Full&pageSize=100), [votes](https://games.roblox.com/v1/games/votes?universeIds=210851291), [badges](https://badges.roblox.com/v1/universes/210851291/badges?limit=100)
- Build a Boat wiki: [Gold](https://build-a-boat-for-treasure.fandom.com/wiki/Gold), [Wood Block](https://build-a-boat-for-treasure.fandom.com/wiki/Wood_Block), [Blocks](https://build-a-boat-for-treasure.fandom.com/wiki/Blocks), [Building Space](https://build-a-boat-for-treasure.fandom.com/wiki/Building_Space), [main page](https://build-a-boat-for-treasure.fandom.com/wiki/Build_A_Boat_For_Treasure)
- [Bloxodes: chests](https://bloxodes.com/wiki/build-a-boat-for-treasure/chests); [Earnaldo (promotional)](https://earnaldo.com/blog/build-a-boat-for-treasure-beginner-guide)
