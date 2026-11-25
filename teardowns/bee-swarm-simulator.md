# Bee Swarm Simulator

> Your bees gather pollen, your hive turns it into honey, honey buys more bees: a gather-and-convert simulator that still holds about 49,000 players 8.7 years after it was made.

| | |
|---|---|
| Studio | Onett (a solo creator account) |
| Released | Created 21 Mar 2018 (Roblox public API, 25 Nov 2026) |
| Genre | [Simulator](../genres/simulator.md), gather and convert |
| Peak concurrent players | Not known |
| Players now | 48,695 (Roblox public API, 25 Nov 2026) |
| Players per server | 6 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Other public numbers: 4.70 billion visits, 6.59 million favourites, 95.6% up-votes (our arithmetic from 3.06M up and 140k down), last updated 21 Nov 2026 ([games API](https://games.roblox.com/v1/games?universeIds=601130232)).

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1 | Walks into a field; bees fly out and gather | not known | Flowers shrink, tokens drop | Pollen in the backpack |
| 2 | Picks up tokens | under 10 (tokens vanish after 10 s) | Token icons on the ground | Boosts, items |
| 3 | Returns to the hive and converts | not known | Pollen becomes honey | Honey |
| 4 | Spends honey on an egg or a hive slot | not known | A new bee in the hive | Bees owned |
| 5 | Reaches a bee-count gate | not known | A new field opens | Fields (23) |

Sources: [techwiser: mechanics](https://techwiser.com/bee-swarm-simulator-other-mechanics-guide/), [ofzenandcomputing: fields](https://www.ofzenandcomputing.com/bee-swarm-simulator-fields-guide/).

Cycle time and dead time: not known. The wait is the walk back to the hive and the convert.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Claim one of 6 hives on the server ([wiki: Hive](https://bee-swarm-simulator.fandom.com/wiki/Hive)) |
| 0:10 to 1:00 | Not timed. **Our read:** first bee hatched; Black Bear's first quest taken: 100 pollen from the Sunflower field for 200 honey |
| 1:00 to 5:00 | Not timed. **Our read:** Basic Eggs bought from 1,000 honey; five 0-bee fields open (Sunflower, Dandelion, Mushroom, Blue Flower, Clover) |
| 5:00 to 15:00 | Not timed. **Our read:** 5 bees owned, which opens Strawberry, Spider and Bamboo |

First reward, first purchase, first rare moment: not timed. First long goal: Black Bear's sixth quest pays a Silver Egg. No beginner's guide was found. Teaching is done by quest bears ([wiki: Black Bear](https://bee-swarm-simulator.fandom.com/wiki/Black_Bear)).

## 3. Progression

**Fields by bees owned:** 0 bees 5 fields; 5 bees 3 more; 10 bees Pineapple, Stump and brick fields; 15 bees Cactus, Pumpkin, Pine Tree, Rose; 20 bees Hub and Ant; 25 bees Mountain Top; 35 bees Pepper and Coconut ([ofzenandcomputing, Aug 2026](https://www.ofzenandcomputing.com/bee-swarm-simulator-fields-guide/)). The gate is a collection count, so honey buys progress only through bees.

**Hive slots.** A basic hive holds 25 bees; 25 more slots are sold at the Mountain Top shop, up to 50 ([wiki: Hive Slot](https://bee-swarm-simulator.fandom.com/wiki/Hive_Slot)):

| Extra slot | Honey | Ratio to previous | Compared with all earlier slots (our arithmetic) |
|---|---|---|---|
| 1 | 3,000,000 | | |
| 2 | 7,750,000 | 2.58 | 2.6x |
| 5 | 37,085,938 | 1.54 | 0.75x |
| 10 | 209,117,953 | 1.37 | 0.43x |
| 15 | 894,566,712 | 1.32 | 0.35x |
| 20 | 20,132,877,003 | 2.17 | 0.96x |
| 21 | 46,154,052,716 | 2.29 | 1.12x |
| 23 | 285,456,003,884 | 2.55 | 1.43x |
| 25 | 2,169,203,229,760 | 2.83 | 1.73x |
| All 25 | 3,421,214,977,088 | | |

The step falls from 2.6x to 1.32x by slot 15, then climbs back to 2.83x. Each slot from 21 on costs more than all the slots before it put together. Slots 21 to 25 are 98.8% of the total. The last slot costs 723,000 times the first. The 35-bee gate needs 10 extra slots: 692 million honey (our arithmetic).

**Our read on pacing:** honey per hour is not in our sources, so calendar time is not known. The shape still says a lot. The five last slots cost 82 times everything spent on slots 1 to 20. A player whose honey income stopped growing at slot 20 would need 82 times their whole slot journey again. The ladder only works for a player whose income keeps multiplying through better bees, which is why the last slots are a target for months, not days. Each of them adds one bee out of 46 to 50, so their payback is far beyond the 25 to 300 seconds of the slop ladder in [slop/01-anatomy.md](../slop/01-anatomy.md). They are a sink and a flex.

**Eggs** ([wiki: Egg](https://bee-swarm-simulator.fandom.com/wiki/Egg), [wiki: Ticket Tent](https://bee-swarm-simulator.fandom.com/wiki/Ticket_Tent)):

| Egg | Price | Odds | Tickets per Mythic, expected (our arithmetic) |
|---|---|---|---|
| Basic | 1,000 honey, rising per purchase to a 10,000,000 cap | 87% Basic, 10% Rare, 2.5% Epic, 0.5% Legendary | |
| Silver | 50 tickets or 100 R$ | 64.9% Rare, 30% Epic, 5% Legendary, 0.1% Mythic | 50,000 |
| Gold | 100 tickets (once 50) or 200 R$ | 79% Epic, 20% Legendary, 1% Mythic | 10,000 |
| Diamond | 400 tickets | 95% Legendary, 5% Mythic | 8,000 |
| Mythic | 2,500 tickets | 100% Mythic | 2,500 |

Ticket prices step 2x, 4x, 6.25x. **Our read:** the dearest egg is the cheapest Mythic, 20 times cheaper than rolling Silver Eggs. Saving tickets beats spending them, so the egg ladder rewards patience.

**Black Bear quests:** 6 quests to a Silver Egg (honey 200, 400, 500, 650, 750, 1,000), 9 to a Gold Egg (2,100 up to 25,000), 20 to a Diamond Egg (35,000 to about 275,000, a Royal Jelly every 4th), then an hourly repeating quest. All of them pay 2,352,532,300 honey. Our arithmetic: the Gold stage pays 28x the Silver stage while the pollen asked rises 250x (100 to 25,000). The whole quest line buys extra slots 1 to 13 and stops short of slot 14: 0.07% of the slot total.

## 4. Session and return hooks

| Timer | What |
|---|---|
| 10 s | Dropped tokens vanish |
| 2 min 35 s | Night; day lasts 2 to 10 minutes (was 10 to 30). A sprout planted at night has a 60% chance to be a Moon Sprout |
| 5 min | Idle sprouts despawn; Ladybug and Rhino Beetle respawn |
| 20 / 30 min | Mantis and Scorpion / Spider respawn |
| about 45 min | Sparkle locations regenerate |
| 1 h | Werewolf respawns; Black Bear's repeat quest |
| 16 h | Special Sprout Summoner, after all eight Legendary bees are found |
| 96 h | Stump Snail respawns (81 h 36 min with a gifted Vicious Bee) |

Sources: [techwiser](https://techwiser.com/bee-swarm-simulator-other-mechanics-guide/), [wiki: Mobs](https://bee-swarm-simulator.fandom.com/wiki/Mobs). Our arithmetic: respawns span about 1,150x, from 5 minutes to 4 days. Seasonal catalogs sell eggs for event currency. Daily rewards, codes and update day: not known.

## 5. Other players

6 hives per server. Trading, theft, co-op and leaderboards: not known from our sources. What gets clipped: not known.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| x2 Ticket Chance | Pass | off sale | by name |
| Bear Bee | Pass | off sale | by name |
| x2 Gather Pollen | Pass | off sale | by name |
| x2 Convert Speed | Pass | off sale | by name |
| Silver Egg | Robux price on the egg | 100 | Paid random bee |
| Gold Egg | Robux price on the egg | 200 | Paid random bee |

All four passes were off sale on 25 Nov 2026 ([passes API](https://apis.roblox.com/game-passes/v1/universes/601130232/game-passes?passView=Full&pageSize=100)). The snapshot agrees, and the egg prices match it [data, Nov 2026]. Best sellers: not known.

Products [data, Nov 2026]: 92 listed for sale, but 18 carry placeholder prices of 9,999,999 R$ or more (old event packs and a "Discontinued" Bear Bee), so 74 can be bought: 10 to 4,500 R$, median 800. About 45 are themed packs and bundles at 300 to 4,500. 12 of 74:

| Product | R$ | Note |
|---|---|---|
| Ticket | 10 | 0.10 tickets per R$ |
| 25 / 100 / 510 Tickets | 200 / 400 / 1,700 | |
| 1800 Tickets | 4,500 | 0.40 tickets per R$: 4 times the single ticket (our arithmetic) |
| 700 Ticket Offer | 1,200 | 0.58 tickets per R$, the best rate listed |
| Diamond Egg / Mythic Egg | 400 / 1,200 | |
| x2 Convert Speed Voucher / Bear Bee Voucher | 250 / 800 | The off-sale passes, now sold as products |
| Royal Jelly | 45 | 10 for 300 |

**Our read:** expected R$ per Mythic bee is 100,000 by Silver Egg, 20,000 by Gold, 8,000 by Diamond and 1,200 by Mythic Egg, the same ladder as tickets. A Mythic Egg bought outright costs 1,200 R$; its 2,500 tickets bought at the best pack rate would cost about 4,300 (our arithmetic).

## 7. Why it works

No developer statements were found. Measured: 95.6% approval and 48,695 players at 8.7 years, about 10 players now per million lifetime visits (our arithmetic), against 0.1 for Mining Simulator 1 and 2.

**Our read:**
- Gates count bees, so every purchase moves the player toward a named field.
- Timers from 10 seconds to 4 days give a reason to play for one minute or come back in four days.
- A sink of 3.42 trillion honey means a veteran never runs out of something to buy.
- The best-value egg is the dearest, so saving is the smart move.

## 8. What went wrong

Known changes: day length cut from 10 to 30 minutes to 2 to 10; Gold Egg raised from 50 to 100 tickets. Their reasons are not known. No decline or economy break is documented in our sources.

## 9. What to take from it

- Gate zones by count owned (0, 5, 10, 15, 20, 25, 35), not by currency.
- A 25-step capacity sink whose last 5 steps are 98.8% of the total.
- Quest chain of 6, 9, then 20 quests, each stage ending in a better egg.
- Premium eggs where the dearest is the best value: 2,500 tickets per Mythic versus 50,000.
- Enemy respawns from 5 minutes to 96 hours.
- Old passes re-sold as vouchers (products) at 250 to 800 R$ instead of one-time passes [data, Nov 2026].

## Sources

- Roblox public API, 25 Nov 2026: [games](https://games.roblox.com/v1/games?universeIds=601130232), [passes](https://apis.roblox.com/game-passes/v1/universes/601130232/game-passes?passView=Full&pageSize=100)
- [Bee Swarm Simulator wiki](https://bee-swarm-simulator.fandom.com): Hive, Hive Slot, Egg, Ticket Tent, Black Bear, Mobs (linked above)
- [techwiser: mechanics](https://techwiser.com/bee-swarm-simulator-other-mechanics-guide/), [ofzenandcomputing: fields](https://www.ofzenandcomputing.com/bee-swarm-simulator-fields-guide/)
- Genre: [genres/simulator.md](../genres/simulator.md)
