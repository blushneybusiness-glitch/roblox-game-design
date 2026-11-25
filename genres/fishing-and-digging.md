# Fishing and digging

> **The feeling sold:** "There is always one more thing in the water I have never caught, and my next rod can catch it."

This page covers fishing, digging and mining collect-a-thons: a short catch or dig action, a gear ladder that raises luck and speed, zones and clocks that decide what can be found, and an index to fill. Player counts marked "now" are from Roblox public API, 25 Nov 2026.

## At a glance

| | |
|---|---|
| Core verb | Cast (or dig, or mine), win a short minigame, sell or keep the catch. |
| Study these first | **[Fisch](../teardowns/fisch.md)**: the leader, 1,527 fish, 259 rods, a catch formula published on its wiki. **Fish It!**: a follower that made the minigame simpler and sells luck; now close to Fisch in players. **The Forge**: mining that feeds a forging minigame, peaked higher than Fisch. **Prospecting!**: two gear ladders in parallel (shovel and pan). |
| Session that works | Not known from sources. |
| Players per server | 20 for Fisch, Fish It! and Prospecting!; 12 for The Forge ([games API](https://games.roblox.com/v1/games?universeIds=5361032378,6701277882,7671049560,7629331599,10563114921,6705549208,9145063979,10774071683)). |
| Who owns the genre | New games can enter. Fisch (March 2024) peaked at about 600K in December 2024 and has 78,638 now. Fish It! arrived 7 months later and has 68,566. The Forge (May 2025) peaked at about 870K in December 2025, above Fisch, and has 22,002. Prospecting! (May 2025) has 2,370. Peaks are tracker figures ([rowatcher](https://rowatcher.com/games/5750914919)). |
| Build cost | Not known from sources. **Our read:** the cost is the catalogue. Fisch lists 1,527 fish in 153 locations; The Forge 156 ores and 35 pickaxes. |
| Money comes from | Sell Anywhere (299 to 399 R$), luck passes where sold (Fish It! +30% to +150%), and convenience (enchant, appraise, forge anywhere). |
| What kills clones | A gear ladder with nothing at the top: once the best rod is bought, every catch is the same. |

## Why people play it

Fisch's wiki says each fish bites only in its own zone, and many also need a time of day, weather or season ([rblxguide](https://rblxguide.com/games/fisch)). Fish It! sells "over a million catch variations" and co-op fishing on its store page ([games API](https://games.roblox.com/v1/games?universeIds=10563114921,6701277882,7671049560,10648820673)). Age, device and player quotes: not known from sources.

**Our read:** the need is collecting with a calm verb. The catch takes about 8 seconds, needs some skill, and almost never fails badly. The index tells the player exactly what is missing, and the clocks tell them when to come back for it.

## The loop, with a stopwatch

Leader: **Fisch** ([Fischipedia: Fishing](https://fischipedia.org/wiki/Fishing)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Cast | Holds and releases | not known | Bobber lands; cast grade does not matter later | |
| 2. Lure | Waits, shakes when prompted | Base x (1 - Lure Speed/100); each shake cuts 0.5 to 1.5 s | Shake prompts | Lure time |
| 3. Reel | Holds and releases to keep the fish inside a white bar | 1.2 s input lock, then at least 6.8 s; 8 s total with no modifiers | Bar is 30% of the track at zero Control; progress moves 12% a second | Progress, 0 to 100% |
| 4. Land | Reads the catch | about 1 (our read) | Fish card; a perfect catch pays C$10 and +50% XP | Bestiary, XP |
| 5. Sell or appraise | Walks to a merchant | depends on distance | Sale value with mutation multiplier | C$ |
| 6. Spend | Buys rod, bait, boat | | | Luck, Control, Resilience, Lure speed |

Progress at zero loses the fish. Bait is used up per catch unless the shake minigame is failed ([Fischipedia: Bait](https://fischipedia.org/wiki/Bait)).

How the followers differ. **Fish It!**: click to charge, then click quickly ([games API](https://games.roblox.com/v1/games?universeIds=10563114921,6701277882,7671049560,10648820673)). **Prospecting!**: dig sediment with a shovel, then shake a pan to find minerals ([wiki: Pans](https://prospecting.fandom.com/wiki/Pans)). **The Forge**: mine ores, then run a multi-stage forging minigame that grades the item from Broken to Masterwork ([Bloxodes](https://bloxodes.com/wiki/the-forge)).

The loop stack:

| Every | What finishes | Game |
|---|---|---|
| 8 s | A catch (4.6 s at +100% progress speed) | Fisch |
| 12.5 min | Weather is rolled for the next half-day | Fisch |
| 25 min | A full day and night | Fisch |
| 1 h | Personal aquarium pays C$, XP and items; Celestial Clash at :35 for 15 min | Fisch; The Forge |
| 3 h | Wandering Runesmith for 15 min | The Forge |
| 9.6 h | A season changes, the same on all servers | Fisch |
| 4 to 8 weeks | A seasonal event or banner | All three |

## The first five minutes

What the sources record. Fisch spawns players in Moosewood, where a guide NPC, Pierre, explains fishing. The Flimsy Rod is free; the Training Rod costs C$300 ([Fischipedia: Moosewood](https://fischipedia.org/wiki/Moosewood)). Fish It! starts on Fisherman Island with a free Starter rod; the Luck Rod costs $250, and a Toy Rod is free for liking the game and joining the group ([Bloxodes Fish It rods](https://bloxodes.com/wiki/fish-it/rods)). Prospecting! starts at Rubble Creek, where John gives the tutorial and the first quest ([wiki: Locations](https://prospecting.fandom.com/wiki/Locations)). No source gives seconds.

Gates for a new game, our read from the 8-second catch:

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | Holding a free tool at the water's edge | Fisch's free Flimsy Rod |
| 0:30 | First catch landed and shown on a card | Lure plus 8 s reel |
| 1:00 | First sale | |
| 3:00 | 10 to 15 catches; the first rod upgrade is affordable | Training Rod C$300 equals 30 perfect-catch bonuses alone (our arithmetic) |
| 5:00 | First upgrade bought; the index shows the next missing fish and where it lives | |

## Numbers that work

**The catch formula** ([Fischipedia: Fishing](https://fischipedia.org/wiki/Fishing)). Minimum perfect reel T = 1.2 + 6.8 / (1 + p/100) seconds, where p is progress speed in percent. Values are our arithmetic.

| Progress speed | Minimum reel (s) | Example |
|---|---|---|
| -85% | 46.5 | Cinder Block Rod (forced) |
| 0% | 8.0 | No modifiers |
| +30% | 6.4 | A strong enchant (enchants give +5% to +30%) |
| +100% | 4.6 | |
| +300% | 2.9 | |
| +666% | 2.1 | Eidolon Rod after 70% progress |

**Our read:** in the wiki's formula the 1.2-second lock is a floor that no gear removes, so even the best rod keeps a short beat of tension. Cinder Block shows the trade a rod can carry: 350% luck for C$50,000, paid for with a 46-second reel.

**Rod and tool ladders.** Ratios and price-per-luck are our arithmetic.

Fish It! rods ([Bloxodes](https://bloxodes.com/wiki/fish-it/rods)):

| Rod | Price | Luck | Price ratio | Price per 1% luck |
|---|---|---|---|---|
| Starter | free | 0% | | |
| Luck Rod | $250 | 50% | | 5 |
| Carbon | $900 | 30% | 3.6x | 30 |
| Grass | $1,500 | 55% | 1.7x | 27 |
| Damascus | $3,000 | 80% | 2x | 38 |
| Ice | $5,000 | 60% | 1.7x | 83 |
| Lucky | $10,000 | 130% | 2x | 77 |
| Midnight | $50,000 | 100% | 5x | 500 |
| Steampunk | $215,000 | 175% | 4.3x | 1,229 |
| Chrome | $437,000 | 229% | 2x | 1,908 |
| Fluorescent | $715,000 | 300% | 1.6x | 2,383 |
| Astral | $1,000,000 | 350% | 1.4x | 2,857 |
| Hazmat | $1,300,000 | 380% | 1.3x | 3,421 |
| Ares | $3,000,000 | 455% | 2.3x | 6,593 |
| Angler | $8,000,000 | 530% | 2.7x | 15,094 |
| Bamboo | $12,000,000 | 760% | 1.5x | 15,789 |
| Ghostfinn, Element, Diamond, Withering | quests only | 610%, 1,111%, 1,300%, 1,463% | | |

Price for 1% of luck rises about 3,000 times from the first rod to the last bought one. Rods whose luck drops (Carbon, Ice, Midnight) sell speed or weight instead. The four best rods are free quest rewards, each needing the one before.

Other ladders:

| Game | Ladder | Steps | Ratio, step to step | Source |
|---|---|---|---|---|
| Fisch | Rods at Moosewood: free, C$300, 750, 2,000, 4,000; Lucky Rod C$4,500 | 259 rods up to C$100M | 2.5x, 2.7x, 2x, 2x | [Fischipedia](https://fischipedia.org/wiki/Moosewood), [Bloxodes](https://bloxodes.com/wiki/fisch/rods) |
| Prospecting! | Pans: start, $500, $12K, $55K, $333K, $1M, $3.5M, $10M, $35M; luck 1 to 50 | 9 | 24x, then 2.9x to 6.1x | [wiki](https://prospecting.fandom.com/wiki/Pans) |
| Prospecting! | Shovels: start, $3K, $25K, $75K, $135K, $320K, $1.33M, $4M, $12.5M | 9 | 8.3x, then 1.8x to 4.2x | [wiki](https://prospecting.fandom.com/wiki/Shovels) |
| The Forge | Pickaxes: free, $150, $500, $1,500, $5,000, $10,000 ... $7.77M; power 3 to 1,100 | 25 listed with prices, 35 in all | 3.3x, 3x, 3.3x, 2x, then 1.1x to 1.7x | [Bloxodes](https://bloxodes.com/wiki/the-forge/pickaxes) |

The Forge's power grows about 370 times while price grows about 50,000 times. Prospecting!'s pan luck grows 50 times while price grows 70,000 times. Fisch's top rods are gated by level (170 to 250), Bestiary completion (50% and 100%) and quests as well as coins.

**Clocks** ([Fischipedia: Weather](https://fischipedia.org/wiki/Weather), [Bloxodes: The Forge](https://bloxodes.com/wiki/the-forge)):

| Clock | Value | Effect on spawns |
|---|---|---|
| Fisch day | 25 real minutes (12.5 day, 12.5 night); 1 real second = 1 game minute | Outside a fish's preferred time: -75% |
| Fisch season | 576 real minutes (9.6 h), same on all servers | Preferred season +25%, otherwise -15% |
| Fisch weather | Rolled at the start of each half-day; Clear 22.75% by day, 26.09% by night | Preferred weather +35% |
| The Forge | Celestial Clash at :35 every hour for 15 min; Runesmith about every 3 h for 15 min; totems 5 min | Luck Totem +25% mining luck |

**Our read:** if the modifiers multiply, a fish's spawn weight swings from 0.21 (wrong time, wrong season) to 1.69 (right season, right weather), about 8 times. And 9.6 hours does not divide 24, so a player who logs in at the same hour each day meets a different season.

**Bestiary rewards** ([Fischipedia: Bestiary](https://fischipedia.org/wiki/Bestiary), [Bloxodes Fisch rods](https://bloxodes.com/wiki/fisch/rods)):

| Milestone | Reward |
|---|---|
| Each location page | Coins, XP and a bobber |
| 50% of a region | Great Dreamer Rod (C$275,000, 147% luck) |
| 100% of a region | Carrot Rod (C$45,000, 125% luck) |
| 100% overall | C$50,000, 100,000 XP, Aurora bobber; Masterline Rod if the Rod Journal is also 100% |

Secret, Apex, Divine Secret and Limited fish do not count, so 100% stays reachable.

**Mutations.** Fish It! rolls one per catch ([Bloxodes](https://bloxodes.com/wiki/fish-it/mutations)):

| Mutation | Value | Chance |
|---|---|---|
| Galaxy | 6.5x | 0.5% |
| Midnight, Gemstone | 4.8x | 0.7%, 0.5% |
| Lightning | 4.2x | 0.8% |
| Radioactive, Corrupt | 4x | 0.9%, 0.5% |
| Gold, Fairy Dust | 3.8x | 1.6%, 0.6% |
| Ghost | 3.5x | 1.4% |
| Holographic | 3.4x | 0.9% |
| Albino | 2.3x | 2.5% |
| Stone | 2.2x | 4% |

Our arithmetic: 14.9% of catches carry a mutation, about 1 in 7, and the average catch is worth 1.34 times its base. The More Mutations pass (+60%) lifts that to about 24% and 1.54 times. Fisch keeps one mutation per fish (the highest wins): Shiny and Sparkling 1.85x at 1%, Alpha 2.5x at 0.1%, and Aether 15x at 0.004%, 1 in 25,000 ([Fischipedia: Mutations](https://fischipedia.org/wiki/Mutations), [Bloxodes](https://bloxodes.com/wiki/fisch/mutations)). Many Fisch rods exist to trigger one mutation, at 5% to 35%.

**The followers, and what each changed:**

| Game | Released | Changed from Fisch | Result |
|---|---|---|---|
| Fish It! | Oct 2024 | Click-to-charge minigame; luck sold in stacking passes (+260% for 840 R$; Fisch sells none); best rods free from quests; weak Robux rods (Angelic 399 R$ at 180% against Ghostfinn's free 610%); a machine that removes mutations; a battle pass | Peak 1.4M or 2.7M (trackers conflict); 68,566 now; 82.8% like, the lowest of the set |
| Prospecting! | May 2025 | Two ladders at once, shovel and pan; Toughness decides which deposits can be dug; levels are mostly vanity; meteor showers | 2,370 now; peak not known |
| The Forge | May 2025 | Mining feeds forging with a graded result; combat with 43 enemies; 22 races, rolled (relic races 0.1%); hourly world events; 30-day banners | Peak 870K, 7 months after release; 22,002 now; 94.4% like |

Sources: [rowatcher Fish It!](https://rowatcher.com/games/6701277882), [rowatcher The Forge](https://rowatcher.com/games/7671049560), [votes API](https://games.roblox.com/v1/games/votes?universeIds=6701277882), [Bloxodes Fish It rods](https://bloxodes.com/wiki/fish-it/rods), [Prospecting wiki: Level](https://prospecting.fandom.com/wiki/Level).

**Start with:** (our read, derived from the tables above)

| Value | Start with | Why |
|---|---|---|
| Base catch | 6 to 8 s, with a fixed 1 s lock | Fisch: 8 s, 1.2 s lock |
| Speed formula | T = lock + rest / (1 + speed/100) | Fisch's published formula; gear never takes it to zero |
| Perfect catch bonus | +50% XP and a small coin bonus | Fisch |
| Tool ladder | 15 to 25 bought tiers; first step 2.5x to 4x, then 1.3x to 2x, with a 4x to 5x jump where a new zone opens | Fisch 2.5x first step; Fish It! 3.6x, then 5x and 4.3x at Midnight and Steampunk |
| Top of ladder | Best 3 to 5 tools from quests and index milestones | Fish It! quest rods; Fisch Bestiary rods |
| Price per luck | Rises about 1,000x to 3,000x from first to last tier | Fish It! 5 to 15,789 per 1% |
| Day | 20 to 25 min | Fisch 25 min |
| Weather | Re-rolled every half-day, about 1 in 4 clear | Fisch |
| Season | A period that does not divide 24 h | Fisch 9.6 h |
| Mutations | About 12 values, 15% of catches, average 1.3x; one top value near 15x at 1 in 25,000 | Fish It! table; Fisch Aether |
| Index | Rewards at each zone page, at 50% and 100% of a region, and a rod at 100% overall; exclude the rarest tiers | Fisch Bestiary |

## What brings them back

**Later in the same session.** A catch every 8 seconds, a weather roll every 12.5 minutes, a full day every 25 minutes, and a fish that only bites at night 12.5 minutes away. The Forge adds Celestial Clash at :35 every hour.

**Tomorrow.** Fisch's personal aquarium pays every hour ([Bloxodes locations](https://bloxodes.com/wiki/fisch/locations)). Seasons change every 9.6 hours, so tomorrow's water holds different fish. Other daily rewards: not known.

**Next week and after.** Index percentages and the rods behind them; level gates at 15 (trading), 25 (Trade Plaza, aquarium), 40, 50 (Shady Bazaar) and boats at levels 7 to 50 ([Fischipedia: Level](https://fischipedia.org/wiki/Level)); quest chains to the top rods; seasonal events with event rods.

## Other players

**Server size.** 20 in the fishing games; 12 in The Forge.

**What they see and do.** Fisch opens trading at level 15 and the Trade Plaza at 25, where players rent stalls ([Fischipedia: Level](https://fischipedia.org/wiki/Level)). Fish It! sells co-op fishing on its store page. The Forge's world events gather the server at one time. No source documents theft or player combat in these games.

**What can be lost.** Bait and the fish itself, if progress reaches zero. Nothing is taken by other players.

**What gets clipped.** Not known from sources. **Our read:** a 15x Aether catch, or a 2-million-coin Apex fish (Akkorokamui averages C$2,000,000 before mutations ([rblxguide](https://rblxguide.com/games/fisch))).

## Money

| Game | Pass | R$ | What it does |
|---|---|---|---|
| Fisch | Sell Anywhere / Appraise Anywhere | 399 / 399 | |
| Fisch | Enchant Anywhere / Spawn Boat Anywhere / Appraisers Luck | 299 each | Appraisers 25% cheaper, better appraisal luck |
| Fisch | Double XP / Supporter | 289 / 169 | 9 passes, 2,081 in all; no luck pass |
| Fish It! | Advanced Luck / Extra Luck / Small Luck | 545 / 245 / 50 | +150%, +80%, +30% fishing luck, stacking |
| Fish It! | Hyper Pack / VIP / Sell Anywhere / More Mutations | 999 / 445 / 315 / 295 | More Mutations: +60% chance |
| The Forge | Forge Anywhere / Better Forge / Fast Forge | 549 / 449 / 299 | Better Forge +30% quality; Fast Forge skips two-thirds of the minigame |
| The Forge | Supporter / Sell Anywhere / Double Storage | 379 / 349 / 249 | 11 passes, 3,038 in all |
| Prospecting! | 2x Shards / More Ring Slots / Sell Anywhere | 599 / 575 / 299 | |

Sources: game-passes API for [Fisch](https://apis.roblox.com/game-passes/v1/universes/5750914919/game-passes?passView=Full&pageSize=50), [Fish It!](https://apis.roblox.com/game-passes/v1/universes/6701277882/game-passes?passView=Full&pageSize=50), [The Forge](https://apis.roblox.com/game-passes/v1/universes/7671049560/game-passes?passView=Full&pageSize=50), [Prospecting!](https://apis.roblox.com/game-passes/v1/universes/7629331599/game-passes?passView=Full&pageSize=50), 25 Nov 2026. Best sellers: not known.

Sell Anywhere is in all four, at 299 to 399. **Our read:** the walk to the merchant is the friction players pay most often to remove. Fish It!'s low like ratio (82.8% against Fisch's 90.9%) sits next to selling luck, but no source shows one caused the other.

**The line.** A luck or mutation pass changes the odds of every catch. Roblox's paid random item rules then apply: exact odds shown, live odds while the boost is active. See [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

| Game | What ships | When |
|---|---|---|
| Fisch | Holiday events with event rods: Fischfright (Halloween), Fischgiving (live on 25 Nov 2026), Fischmas (Gingerbread Rod C$5,000) | Each holiday; version 2.07.0 |
| Fish It! | Islands and fish: Classic Event (42 fish, 2 Secret, battle pass), Pirate Cove (12 Jan 2026), Lava Basin (15 fish, charm crafting), Sky Island (+10 fish) | Nov 2025, Jan 2026, Feb 2026, then Sky Island (date not known) |
| The Forge | Twilight Banner 3 Nov to 3 Dec 2026; shard earning ends 7 Dec, shop closes 14 Dec; a 90KCCU code | 30-day banners |

Sources: [Bloxodes Fisch rods](https://bloxodes.com/wiki/fisch/rods), [rowatcher Fish It!](https://rowatcher.com/games/6701277882), [Bloxodes Fish It locations](https://bloxodes.com/wiki/fish-it/locations), [Bloxodes: The Forge](https://bloxodes.com/wiki/the-forge).

**Our read:** the unit of content is a zone with 10 to 40 fish and one event rod. A small team can ship one a month. See [foundations/13-live-ops.md](../foundations/13-live-ops.md).

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| A digging game at almost zero players | No ladder or clocks to hold anyone. Dig it! (2024): 11 players now | A gear ladder, an index, a day clock |
| Peak falls about 97% within a year | The Forge: about 870K to 22,002; cause not documented | **Our read:** one 30-day banner at a time is not enough for a peak that size; plan zones in advance |
| Like ratio 8 points below rivals | Fish It!: 82.8%; it sells luck, but the cause is not proven | Sell convenience, keep the best gear free, as Fisch does |
| Late players stop buying gear | Price per luck so steep that the next rod changes nothing | Gate the top tools by quests and index milestones |
| Guides and players quote different prices | Rods repriced between versions (Fisch's Abyssal Specter: C$300,000 in one list, C$850,000 in another) | Show the current price and stats in game; announce changes |
| A two-ladder game stays small | Prospecting!: 2,370 now, levels "mostly vanity" | Make level unlock something: zones, tools, trading |

## Checklist

1. A free tool is in hand within 5 seconds of spawning.
2. A base catch or dig takes 6 to 8 seconds, with a fixed lock of about 1 second.
3. Gear can cut the catch time but never below the lock.
4. The first upgrade costs 2.5 to 4 times the starting tool and is affordable within 3 minutes.
5. The ladder has at least 15 bought tiers, with a step of 1.3x to 2x after the first few.
6. The best 3 tools come from quests or index milestones, not coins or Robux.
7. A day-night cycle of 20 to 25 minutes changes what can be caught.
8. Weather or another state re-rolls at least every 15 minutes.
9. About 15% of catches carry a mutation; the top one is near 1 in 25,000.
10. The index pays at each zone, at 50% and at 100%, and excludes the rarest tier.
11. Every fish shows where and when it can be found once it is in the index.
12. Sell Anywhere, if sold, costs 299 to 399 R$.
13. Any luck or mutation pass shows live odds while active.
14. A new zone or event ships at least every 4 to 6 weeks.

## Twists and open space

Variations that already produced hits:

- **Mine and forge.** The Forge feeds its gathering loop into a crafting minigame: peak about 870K.
- **Simpler catch, paid luck, free top rods.** Fish It!: 68,566 now.
- **Dig down.** Drill to Earth's Core had 12,035 players at the moment of one search; Dig to Escape 3,959 ([omni-search](https://apis.roblox.com/search-api/omni-search?searchQuery=Dig%20to%20China%20OR%20Dig%20It%20OR%20Prospecting%20OR%20The%20Forge&sessionId=11111111-2222-3333-4444-555555555555&pageType=all)).

**Our read**, angles that look under-served:

- A fishing game with [Sol's RNG](../teardowns/sols-rng.md)-style timed biomes and server announcements for the top mutation ([rng.md](rng.md)).
- A co-op boat: 4 players with different jobs (steer, cast, reel, sell), borrowed from the co-op roles in [tycoon.md](tycoon.md).
- A digging game whose catch goes on display at a base that earns, the Skeleton B loop in [slop/01-anatomy.md](../slop/01-anatomy.md).

## Sources

Related: [teardowns/fisch.md](../teardowns/fisch.md), [foundations/06-progression-and-economy.md](../foundations/06-progression-and-economy.md), [foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md), [foundations/10-feel-and-feedback.md](../foundations/10-feel-and-feedback.md).

Main external sources: [Fischipedia](https://fischipedia.org/wiki/Fishing) (Fishing, Weather, Bait, Moosewood, Level, Bestiary, Mutations); Bloxodes on [Fisch](https://bloxodes.com/wiki/fisch/rods), [Fish It!](https://bloxodes.com/wiki/fish-it/rods) and [The Forge](https://bloxodes.com/wiki/the-forge/pickaxes); the [Prospecting! wiki](https://prospecting.fandom.com/wiki/Pans); Roblox games, votes and game-pass APIs (25 Nov 2026); [rowatcher](https://rowatcher.com/games/5750914919).
