# Grow a Garden

> Buy seeds when the shop restocks, plant, harvest, sell, and show off lucky crops. It set Roblox's concurrent-player record twice in 2025 and is the reference for [grow-and-harvest](../genres/grow-and-harvest.md).

| | |
|---|---|
| Studio | Made by BMWLux (first version in about three days); Splitting Point (Jandel) bought in in April 2025; DoBig Studios holds a minority stake ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)) |
| Released | 26 Mar 2025 |
| Genre | Grow and harvest |
| Peak concurrent players | 22.3M, Saturday 23 Aug 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)) |
| Players now | 18,093 (Roblox public API, 25 Nov 2026, 13:53 UTC); 30-day average 17,106 ([RoVitals](https://rovitals.com/game/126884695634066)) |
| Players per server | 4 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Check shop | Opens the seed shop | Restock every 300 s | Same stock on every server | Stock |
| Buy and plant | Equips a seed, clicks a brown plot | not known | Sprout | Sheckles down |
| Grow | Waits | 8 s (Carrot) to 5,700 s (Sunflower) | Weather may mutate the crop | Size, mutations |
| Harvest | Taps the crop | not known | Weighted crop | Value = base x (weight / base weight)² x mutations |
| Sell | Walks to the seller | not known | Sheckles | +10% per friend present, up to +40% |

Cycle time: 8 seconds on the Carrot, then set by regrowth (16 to 1,855 s). During long grows the player buys gear, hatches eggs, and waits for the next restock or weather.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | The player holds Carrot seeds at their plot ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). The store text teaches in four numbered lines: equip a seed, click a brown plot, wait, harvest |
| 0:10 to 1:00 | First Carrot grows in 8 s and sells for about 20, double its 10 price |
| 1:00 to 5:00 | Strawberry (50) after 1 to 2 minutes of Carrots; Blueberry (400) a few minutes later; first restock at 5:00 |
| 5:00 to 15:00 | Rare seeds roll on each restock; a Common egg (50,000) is far off |

Lines after 0:10 are our reconstruction. Starting Sheckles: not known. First rare moment: a mutated crop or a shared weather (rain about every 20 min). First other player: three neighbours, from the start. First long goal shown: the rare seeds in the shop, priced and timed.

## 3. Progression

**Seed shop** ([Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [stock sizes](https://growagarden.fandom.com/wiki/Template:CropInfo/Shop/Sams_Shop), [crop data](https://growagarden.fandom.com/wiki/Module:Crop_Data), read 25 Nov 2026). Payback is our arithmetic and assumes one fruit per harvest, which the wiki does not state.

| Seed | Sheckles | R$ | In stock | Stock size | Grows | Regrows | Sells | Payback |
|---|---|---|---|---|---|---|---|---|
| Carrot | 10 | 7 | always | 5 to 25 | 8 s | no | ~20 | 8 s (doubles) |
| Strawberry | 50 | 21 | always | 3 to 6 | 32 s | 16 s | 15 | ~80 s (4th harvest) |
| Blueberry | 400 | 49 | always | 1 to 5 | 100 s | 20 s | 20 | ~8 min (20th) |
| Buttercup | 600 | 14 | 1 in 3 | not known | 15 s | no | 600 | break-even |
| Tomato | 800 | 79 | always | 1 to 3 | 1,102 s | 221 s | 30 | ~1 h 54 min (27th) |
| Daffodil | 1,000 | 19 | 1 in 7 | not known | 13 s | no | 1,000 | break-even |
| Corn | 1,300 | 135 | 1 in 6 | not known | not known | not known | not known | |
| Watermelon | 2,500 | 195 | 1 in 8 | not known | 1,000 s | not known | 3,000 | +20% at 1,000 s |
| Pumpkin | 3,000 | 210 | 1 in 10 | not known | not known | not known | not known | |
| Apple | 3,250 | 375 | 1 in 14 | not known | not known | not known | not known | |
| Bamboo | 4,000 | 99 | 1 in 5 | 10 to 20 | 236 s | no | 4,000 | break-even |
| Coconut | 6,000 | | 1 in 20 | | | | | |
| Cactus | 15,000 | | 1 in 30 | | | | | |
| Dragon Fruit | 50,000 | | 1 in 50 | | | | | |
| Mango | 100,000 | | 1 in 80 | | | | | |

Higher up: Divine seeds 150K to 5.6M (1 in 100 to 1 in 180 per restock), Prismatic 10M to 10B (1 in 210 to 1 in 440), Transcendent up to 1Qa (the rarest, Octobloom, 1 in 1,300). Mythical-and-up seeds stock 1 at a time. Seed cap: 800 per save slot.

The finding: single-harvest crops past the Carrot only break even on their sale. The profit is in regrowth and mutations. **Our read:** the stock size is the brake on the Carrot; at most 25 a restock means at most 250 Sheckles of Carrot profit per 5 minutes.

**Mutations** ([Crop Mutations](https://growagarden.fandom.com/wiki/Crop_Mutations), [Bloxodes calculator](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator)): about 498, from x1 to x500. Variants Silver x5, Gold x20, Rainbow x50. Combined value: variant x (1 + sum of mutation multipliers - number of mutations). Odds: not known.

**Gear** (also a 5-minute global restock; [Gear Shop](https://growagarden.fandom.com/wiki/Gear_Shop)): Basic Sprinkler 25K (1 in 3), Watering Can 50K, Trading Ticket 100K or 19 R$, Grandmaster Sprinkler 1B, Levelup Lollipop 10B (1 in 300).

**Eggs** ([Pet Eggs](https://growagarden.fandom.com/wiki/Pet_Eggs), [Eggs](https://growagarden.fandom.com/wiki/Eggs), [Common Egg](https://growagarden.fandom.com/wiki/Common_Egg)):

| Egg | In stock (30-min restock) | Hatch | Top pet |
|---|---|---|---|
| Common (50,000 or 19 R$) | 99% | 10 min | not known |
| Uncommon | 55% | 20 min | not known |
| Rare | 26% | 2 h | 8.33% |
| Legendary | 15% | 4 h | 2.13% |
| Mythical | 9% | 5 h 6 min 40 s | 1.5% |
| Bug | 5% | 8 h | 1% |
| Jungle | 2% | 8 h | 1% |
| Robux premium | | 30 s | 0.25 to 0.5% |

Egg slots: 3 at the start, up to 13 (5 more through Robux or aged pets, 5 through Garden Coins at 40 each). Hatching can be skipped with Robux. Our arithmetic: a Bug egg appears in about 1 restock in 20 (10 hours on average), hatches in 8 hours, and gives its top pet 1 time in 100.

**Ascension:** once every 4 hours, fee up 2 trillion each time. **Plot expansions:** 24 hours and 3 days ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden)). Catalogue by November 2026: 609 crops, 461 pets, 83 eggs, 84 gears.

## 4. Session and return hooks

| Clock | What changes |
|---|---|
| 5 min | Seed and gear shops (global); 79 R$ or ads to restock now |
| About 20 min | Rain, 3 to 5 min; some weathers +50% growth or faster hatching ([Weather](https://growagarden.fandom.com/wiki/Weather)) |
| 30 min | Egg shop |
| 60 min | Event-coin shop; a manual restock costs 1B Sheckles and triples each time |
| 2 to 6 h | Thunderstorm |
| 4 h | Night and Blood Moon cycles; Ascension |
| 24 h | Daily deals: 4 seeds, 1 to 5 stock each, one discounted |
| 7 days | Saturday update; 2026 events in 3 to 4 weekly parts ([Update Log](https://growagarden.fandom.com/wiki/Update_Log)) |

The garden grows offline; weekly exclusive items must be claimed online ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). "Watering Wednesday" runs 3:00 to 3:30 PM PT.

## 5. Other players

Gardens of 4 players side by side. Each friend present adds +10% sell value, up to +40% ([Sheckles](https://growagarden.fandom.com/wiki/Sheckles)); how a 4-player server reaches +40% is not known. Weather is shared by every server. Stealing is a 37 R$ product per crop: it can fail (Robux kept, 100 Sheckles back), pricier crops fail more, and a banner names thief and victim ([Stealing](https://growagarden.fandom.com/wiki/Stealing)). Trading needs a Trading Ticket. The Saturday "admin war" with Steal a Brainrot set the 22.3M record.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Restock | Product | 79 | Refills the seed shop now |
| Steal | Product | 37 | Takes one crop; can fail |
| Common Egg | Product | 19 | One egg |
| Trading Ticket | Product | 19 | Enables trading |
| Seeds | Products | 7 to 1,700 | Buy a seed directly |
| Pharaoh's Eye seed | Product | 829 | 6.67% stock chance in its shop ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden/seeds)) |
| Premium Seed Pack | Pass | off sale | |

The snapshot agrees: the only pass is Premium Seed Pack, off sale [data, Nov 2026].

**Developer products [data, Nov 2026].** The snapshot reads 300, its cap, so the list is cut; the rows above for Restock, Steal, Common Egg and Trading Ticket are not among the 300 and rest on the wiki. 299 are on sale. 52 are parked at 999,999,999 R$ and 6 at 99,999 or 999,999; without those and one unnamed item, 240 remain, 1 to 25,000 R$, median 429 R$. About 70 are eggs, 40 seed packs and 30 chests. 9 of 240:

| Product | R$ | Kind |
|---|---|---|
| +1 Premium Winter Egg | 149 | Egg ladder (3 for 429) |
| +10 Premium Winter Eggs | 1,249 | |
| +1 Exotic Hive Seed Pack | 199 | Seed pack ladder (3 for 575) |
| +10 Exotic Hive Seed Pack | 1,699 | |
| +50 Exotic Hive Seed Pack | 6,999 | |
| +50 Trade Tokens | 50 | Token ladder of 5 |
| +25000 Trade Tokens | 25,000 | |
| + Extra Egg On Farm [1] | 249 | Slot ladder: 249, 399, 799, 1,699, 1,699 |
| Ad Reward: Watering Can Booster | 1 | Ad reward |

Our arithmetic: an egg costs 149 R$ singly and 125 in tens (16% off); a seed pack 199 singly and 140 in fifties (30% off); Trade Tokens are 1 per R$ at every size.

Offers sit on the shops, next to their timers. Revenue: not disclosed; it ranked first on Top Earners by 19 Jul 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)).

## 7. Why it works

Fastest game to 1 billion visits (33 days); coverage was almost entirely short-form video; called the "new generation's FarmVille"; about 35% of players under 13 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Approval 89.9% (Roblox public API).

**Our read:**

- The Carrot doubles money in 8 seconds, so the first minute is all wins.
- A global 5-minute clock with rare rolls gives every session about four reasons to check.
- Eggs from 10 minutes to 8 hours span one session to one night.
- Mutations up to x500 make any crop a possible picture to share.

See [slop/02-why-it-holds.md](../slop/02-why-it-holds.md) for the argument.

## 8. What went wrong

- Peaks were spikes: 21.3M fell to 7.6M within an hour; the 14-day average then was 2.7M.
- Kotaku said it looked like a prototype.
- Monetisation added after the sale was criticised; fruit and pets were sold for real money off-platform, against Roblox's terms.
- Players said events felt rushed; two event teams were formed in July 2025.
- Bot-inflation claims from TD Cowen, later retracted on the manipulation point and disputed by Roblox.
- The fall: 22.3M to 18,093 (0.08%) in 15 months; 2026 high 166,679 on Sat 15 Aug 2026 ([RoVitals](https://rovitals.com/game/126884695634066)).

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden).

## 9. What to take from it

- A global 5-minute restock with 4 staple seeds always in stock and rare seeds at 1 in 3 to 1 in 80.
- A first seed that doubles its price in 8 seconds, with stock capped at 25 a restock.
- Single-harvest seeds that sell for their price; profit from regrowth (16 to 221 s) and mutations (x5 to x500).
- Egg hatches of 10 min, 20 min, 2 h, 4 h, 8 h, with 3 starting slots.
- +10% sell value per friend in the server.
- A shared weather about every 20 minutes, lasting 3 to 5.
- One themed egg and one themed seed pack per event, each sold as 1, 3 and 10 (seed packs also 50), with 16% off at 10 eggs and 30% off at 50 packs [data, Nov 2026].

## Sources

Grow a Garden wiki: [Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [shop template](https://growagarden.fandom.com/wiki/Template:CropInfo/Shop/Sams_Shop), [Crop data](https://growagarden.fandom.com/wiki/Module:Crop_Data), [Gear Shop](https://growagarden.fandom.com/wiki/Gear_Shop), [Pet Eggs](https://growagarden.fandom.com/wiki/Pet_Eggs), [Eggs](https://growagarden.fandom.com/wiki/Eggs), [Common Egg](https://growagarden.fandom.com/wiki/Common_Egg), [Weather](https://growagarden.fandom.com/wiki/Weather), [Crop Mutations](https://growagarden.fandom.com/wiki/Crop_Mutations), [Sheckles](https://growagarden.fandom.com/wiki/Sheckles), [Stealing](https://growagarden.fandom.com/wiki/Stealing), [Update Log](https://growagarden.fandom.com/wiki/Update_Log). [Bloxodes index](https://bloxodes.com/wiki/grow-a-garden), [seeds](https://bloxodes.com/wiki/grow-a-garden/seeds), [calculator](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator). [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden), [RoVitals](https://rovitals.com/game/126884695634066). Roblox public API (games, game passes), 25 Nov 2026.
