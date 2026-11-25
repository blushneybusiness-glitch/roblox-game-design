# Throw Food For Animals

> Train Throw Power, throw food from a launch strip into farther areas, and the animal it attracts goes to your pen and earns. The newest giant of the [plus-one](../genres/plus-one.md) family, at 2.47M players three weeks after its first update.

| | |
|---|---|
| Studio | Group "Goofy Chupacabra" (Roblox public API) |
| Released | 18 Sep 2026 |
| Genre | Plus-one (train, reach, bring home) |
| Peak concurrent players | 2.45M to 2.47M: 2,474,602 on Sat 14 Nov 2026 ([RoStats](https://rostats.io/records)); 2,450,448 on Sat 21 Nov 2026 ([RoVitals](https://rovitals.com/game/120219252362013)) |
| Players now | 237,487 (Roblox public API, 25 Nov 2026, 13:53 UTC) |
| Players per server | 5 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

The wiki is small (8 pages) and its food table draws on community databases (Game.Guide, eggvalues.com, Stealthy Gaming), not on game files. Treat its numbers as community-reported.

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Train | Uses a pull-up stand | not known | Throw Power rises | Throw level |
| Throw | Runs to the checkered launch strip, taps "TAP TO THROW!" ([Bloxodes](https://bloxodes.com/articles/throw-food-for-animals-zones-food-guide)) | not known | Food lands in the front, middle or back third of an area | Distance |
| Catch | Nothing | not known | An animal comes to the food; mutation and size roll | Chance per animal |
| Bank | Nothing | not known | Animal walks into the base pen | Income per second |
| Spend | Buys better food | | | Food price |

Cycle time: not known. The skill element is aiming: each animal lives in one third of its area ([Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes)).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Free starter Carrot in hand, at the launch strip |
| 0:10 to 1:00 | First throw into the Forest; a Frog ($2/s) is 56.9% likely, a Snail ($1/s) 7.4% |
| 1:00 to 5:00 | Apple ($30) after about 15 s of Frog income; Banana ($150) after 30 to 60 s with 2 or 3 animals |
| 5:00 to 15:00 | Throw level toward 28, the Savanna gate |

Timings after 0:10 are our reconstruction from the wiki tables. First rare moment: a Gold catch, 13% per throw by Bloxodes' table. First long goal: the next area's distance and level. Tutorial: not documented.

## 3. Progression

**Foods** ([Foods](https://throw-food-for-animals.fandom.com/wiki/Foods); ratios our arithmetic): Carrot free; Apple $30; Banana $150 (x5); Toast $4K (x26.7); Orange $20K (x5); Pear $200K (x10); Cheese $1M (x5); Bread Loaf $12M (x12); Water Melon $60M (x5); Croissant $650M (x10.8); Chocolate $3.2B (x4.9); Mushroom $30B (x9.4); Bacon $150B (x5); Burger $1.3T (x8.7); up to Uranium Cake at "$9Qad" (tier 17). 50 foods after Update 3. Sources disagree on one food (Shank: $618T or $6.8T). The pattern: x5, then a x9 to x27 jump between tiers. Whether food is bought once or used up per throw: not known.

**Areas** ([Areas](https://throw-food-for-animals.fandom.com/wiki/Areas)) and **animals** ([Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes)):

| Area | Distance (studs) | Throw level | Animal income range |
|---|---|---|---|
| Forest | 5 | 1 | $1 to $25/s |
| Savanna | 173 | 28 | $40 to $1K/s |
| Desert | 341 | 62 | $1.5K to $38K/s |
| Jungle | 509 | 96 | $60K to $1.5M/s |
| Ocean | 677 | 129 | not known |
| Mountains | 845 | 163 | not known |
| Taiga | 1K | 201 | not known |
| Winter | 1.3K | 244 | not known |
| Phantom Harbor | 5.2K | 1K | not known |
| Nuclear Wasteland | 6.2K | 1.2K | not known |

19 areas after Update 3; 8 animals each (12 in Nuclear Wasteland); 148 animals. Bloxodes counts 12 index slots per zone, which does not match the wiki's 8 animals.

**Forest animals:** Snail $1/s (Carrot, 7.4%), Frog $2 (Carrot, 56.9%), Bunny $3 (Apple, 44.4%), Owl $5 (Banana, 93.4%), Kookaburra $8, Badger $12, Cow $18, Pony $25 (Banana, 78.6%). The percentages are attract chances per qualifying throw and do not sum to 100 per food.

Our arithmetic on the tables: the distance gate grows by 168 studs per area for the first six; the level gate by about 34. Income per area multiplies by about 40, and the first animal of a new area earns about 1.5 times the best of the last ($25 to $40, $1K to $1.5K, $38K to $60K).

**Fixed rules:**

- An animal always sells for 20 times its income per second, so selling returns 20 seconds of income.
- Animals from eggs and the shop earn a multiple of the player's best animal's income instead of a fixed rate (x1 to x9 by the wiki; one product advertises up to 1,200%), so they never go out of date.
- One mutation per animal. Bloxodes' odds, not confirmed by the wiki: none 79.5%, Gold x1.5 13%, Diamond x3 4%, Emerald x5 2%, Ruby x10 1%, Rainbow x20 0.5% ([Bloxodes](https://bloxodes.com/articles/throw-food-for-animals-mutations-guide)). Nine sizes, Big to Infinite, stack with mutations. Luck rises with training, food tier and a Robux "Lucky Throw" power-up. The average effect is worked out in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md).

Rebirth: not on the wiki.

## 4. Session and return hooks

Saturday events, normally at 6 AM PT ([Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals)):

| Date (2026) | Event | Length |
|---|---|---|
| Sat 31 Oct, 9 AM PT | New Map + Admin Abuse | 1 hour |
| Sat 7 Nov | New Map + Admin Abuse | 30 min |
| Sat 14 Nov | Dreamland | 1 hour |
| Sat 21 Nov | Thanksgiving | 27 hours |
| Sat 28 Nov | Winter Is Coming | upcoming |

A new map arrives with most events. Offline income, daily rewards, restock clocks: not known.

## 5. Other players

Five per server, each with a visible pen. No theft, trading or co-op is documented. The clip: a Rainbow or Infinite-size catch landing in the back third of a far area.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| x2 Cash | Pass | 99 | Doubles income |
| x2 Training Power | Pass | 149 | Doubles training |
| Lucky Throw | Product | 9 for one; 39 for 5 to 499 for 100 [data, Nov 2026] | 100x luck on one throw (product description) |
| Egg and shop animals | Products | 40 to 12,000 [data, Nov 2026] | Earn x1 to x9 of your best animal; Enchanted Eggs say up to 1,200% |

Passes from the Roblox public API, 25 Nov 2026; the snapshot has these 2 and no others [data, Nov 2026]. Its x2 Cash is the cheapest among the hits: Steal a Brainrot and Steal An Egg charge 299, Kick a Lucky Block 399.

**Developer products [data, Nov 2026].** 50 on sale; without 2 gift copies, 48 remain, 2 to 12,000 R$, median 99 R$. Lucky Throws, training, and Enchanted Eggs each appear as two parallel ladders at different prices. The descriptions state what each gives. 12 of 48:

| Product | R$ | What the description says |
|---|---|---|
| Money Pack 1 | 24 | Income of 3 minutes |
| Money Pack 4 | 199 | Income of 5 hours |
| Throw Power Pack 1 | 2 | +5 Throw Power |
| Throw Power Pack 4 | 99 | +500 Throw Power |
| Server Luck 2x | 19 | Whole server 1x to 2x, +15 min |
| Server Luck 16x | 159 | 8x to 16x, the maximum |
| 5 Lucky Throws | 39 | 100x luck each, saved for later |
| 100 Lucky Throws | 499 | |
| Enchanted Egg | 79 | Up to 1,200% of your best animal (10 for 649) |
| 5m of Training | 39 | Strength of 5 minutes of training |
| Jellyfish | 40 | Limited animal, $7.5M/s |
| Hydra | 12,000 | Limited animal, $10Qi/s; top price |

Our arithmetic: money packs cost 480 R$ per hour of income at 3 minutes and 40 R$ at 5 hours, 12 times cheaper; Throw Power gives 2.5 per R$ at the bottom and 5.1 at the top; a Lucky Throw costs 7.8 R$ in the 5 pack and 5.0 in the 100 pack. Server luck doubles at each step for about double the price, and it stacks for everyone present.

## 7. Why it works

It took off with its first update, five weeks after creation: the 24-hour average went from 1,673 to 6,914 (+313%) on 23 Oct 2026 ([RoStats](https://rostats.io/records)). Approval 94.1%, 455.8M visits (Roblox public API). Session about 17 minutes ([RoVitals](https://rovitals.com/game/120219252362013)).

**Our read:**

- The throw is one tap that makes a picture: food in the air, an animal running to it.
- Geometric income against a straight-line gate makes each new area come faster than the last.
- Paid animals that scale with the player's best keep a purchase worth having at every level.
- 19 areas and 50 foods two months after launch: a new area most weeks.

## 8. What went wrong

Too new to have fallen. On Saturday 21 Nov 2026 it peaked at 2.45M against about 230K that week, so most of its audience comes on event days. Copies made 6 days after its breakout hold 3,000 to 4,000 players each; followers that changed the verb did better: Throw a Seed 44,386, Throw a Friend for Monsters 12,183 (Roblox public API, 25 Nov 2026).

## 9. What to take from it

- An animal sells for 20 seconds of its income, so selling is only for space.
- Paid units earn a multiple of the player's best unit (x1 to x9 by the wiki, up to x12 by one product's own text).
- Distance gates +168 studs per area while income multiplies x40.
- Each new area's first unit earns 1.5x the last area's best.
- Food prices x5 within a tier and x9 to x27 between tiers.
- A Saturday event at 6 AM PT, 30 to 60 minutes of admin abuse with a new map.
- Money packs sold as minutes of the buyer's own income (3 min for 24 R$ to 5 h for 199 R$), so a pack keeps its value at every stage [data, Nov 2026].

## Sources

Throw Food For Animals wiki: [Foods](https://throw-food-for-animals.fandom.com/wiki/Foods), [Areas](https://throw-food-for-animals.fandom.com/wiki/Areas), [Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes). [Bloxodes overview](https://bloxodes.com/wiki/throw-food-for-animals), [zones and food guide](https://bloxodes.com/articles/throw-food-for-animals-zones-food-guide), [mutations guide](https://bloxodes.com/articles/throw-food-for-animals-mutations-guide). [RoStats](https://rostats.io/records), [RoVitals](https://rovitals.com/game/120219252362013). Roblox public API (games, game passes), 25 Nov 2026.
