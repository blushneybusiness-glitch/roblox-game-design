# Fisch

> You cast, win an 8-second reeling minigame, and fill a bestiary of 1,527 fish across 153 locations; it mattered because it set the template that Fish It!, The Forge and Prospecting! followed.

| | |
|---|---|
| Studio | Fisching |
| Released | 13 March 2024 (Roblox public API) |
| Genre | Fishing collect-a-thon ([genres/fishing-and-digging.md](../genres/fishing-and-digging.md)) |
| Peak concurrent players | About 600K, December 2024 (tracker, [rowatcher](https://rowatcher.com/games/5750914919)) |
| Players now | 78,638 (Roblox public API, 25 Nov 2026); 5.17B visits; 90.9% like ratio |
| Players per server | 20 |
| Teardown date | 25 November 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Cast | Holds and releases | not known | Bobber lands; cast grade does not matter later | |
| Lure | Waits; shakes when prompted | Base x (1 - Lure Speed/100); each shake cuts 0.5 to 1.5 s | Shake prompts | Lure time |
| Reel | Keeps the fish inside a white bar by holding and releasing | 1.2 s lock, then at least 6.8 s | Bar width set by Control (30% of the track at zero); progress moves 12% a second in or out | Progress 0 to 100% |
| Land | Reads the card | about 1 (our read) | Fish, weight, mutation; a perfect catch adds C$10 and +50% XP | Bestiary, XP |
| Sell or appraise | Walks to a merchant or the Appraiser | depends on distance | Value with mutation | C$ |

Source: [Fischipedia: Fishing](https://fischipedia.org/wiki/Fishing).

Minimum perfect catch with no modifiers: 6.8 s reeling, 8 s in all. The wiki's formula is T = 1.2 + 6.8 / (1 + p/100) for progress speed p%. Speed sources run from -85% (Cinder Block Rod: 46.5 s) to +666% (Eidolon Rod late in the reel: 2.1 s) (our arithmetic). Dead time is the lure wait, which shakes shorten. Resilience calms the fish. Bait is used per catch unless the shake minigame is failed ([Fischipedia: Bait](https://fischipedia.org/wiki/Bait)).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Spawn in Moosewood with the free Flimsy Rod; Pierre, the guide NPC, explains fishing |
| 0:10 to 1:00 | First casts and catches (8 s minimum each) |
| 1:00 to 5:00 | First sales; Training Rod C$300 and Plastic Rod C$750 in reach; GPS C$100, Crab Cage C$45 |
| 5:00 to 15:00 | Carbon C$2,000, Long C$3,000, Fast C$4,000, Lucky Rod C$4,500; level 7 opens the first boat |

Sources: [Fischipedia: Moosewood](https://fischipedia.org/wiki/Moosewood), [Level](https://fischipedia.org/wiki/Level). The timings in the left column are our read from the catch length; no source timed them.

First reward at the first catch. First purchase: the Training Rod at C$300, which equals 30 perfect-catch bonuses before any sale value (our arithmetic). First rare moment: a Shiny or Sparkling fish, 1% each, so about 1 catch in 50 shows one (our arithmetic). First contact with another player: not known. First long goal: the Bestiary page for Moosewood. Teaching: one NPC and the minigame itself.

## 3. Progression

Rods: 259 in all, from the free Flimsy Rod to the Tryhard Rod at C$100,000,000 (399% luck) ([Bloxodes rods](https://bloxodes.com/wiki/fisch/rods)).

| Rod | Price (C$) | Luck | Gate |
|---|---|---|---|
| Training | 300 | | Moosewood |
| Lucky | 4,500 | | Moosewood |
| Wildflower / Steady | 7,000 | 75% / 35% | |
| Kings | 100,000 | 85% | |
| Cinder Block | 50,000 | 350%, Control 0.7, Resilience 1000%, Lure -50% | Puzzle spot |
| Destiny | 190,000 | 250% | |
| Great Dreamer | 275,000 | 147% | 50% of a region's Bestiary |
| Carrot | 45,000 | 125% | 100% of a region's Bestiary |
| Kraken / Poseidon / Zeus | 950,000 / 450,000 / 500,000 | 185% / 165% / 110% | Level 180 / 200 / 250 |
| Great Rod of Oscar | 2,500,000 | 280% | Level 250 |
| Astraeus and Polaris Serenade | 50,000,000 | 300% | |
| Tryhard | 100,000,000 | 399% | |

Price does not follow luck: Cinder Block gives 350% for C$50,000, Great Rod of Oscar 280% for C$2.5M. Some prices differ between sources (Abyssal Specter C$300,000 or C$850,000). A rod holds one primary and one secondary enchant; 80 enchants exist.

Level gates ([Fischipedia: Level](https://fischipedia.org/wiki/Level)): trading 15; Trade Plaza and Personal Aquarium 25; season and Vineweaver recipes 40; Shady Bazaar 50; boats at 7, 10, 15, 20, 25, 30, 35, 40, 50. XP comes from fish, chests (1,500 to 2,000), Angler quests (6 to 8 times fish XP), new locations (300), Bestiary pages and the aquarium. The XP curve: not known.

Mutations: one per fish, the highest wins. Shiny and Sparkling 1.85x at 1%, Alpha 2.5x at 0.1%, Aether 15x at 0.004% ([Fischipedia: Mutations](https://fischipedia.org/wiki/Mutations), [Bloxodes](https://bloxodes.com/wiki/fisch/mutations)). Many rods exist to trigger one mutation at 5% to 35%. The top fish: Akkorokamui averages C$2,000,000 before mutations ([rblxguide](https://rblxguide.com/games/fisch)).

Bestiary: 100% pays C$50,000, 100,000 XP and the Aurora bobber, plus the Masterline Rod if the Rod Journal is also complete. Secret, Apex, Divine Secret and Limited fish do not count ([Fischipedia: Bestiary](https://fischipedia.org/wiki/Bestiary)).

Rebirth: none documented.

## 4. Session and return hooks

| Clock | Value |
|---|---|
| Day | 25 real minutes; fish outside their preferred time spawn 75% less |
| Weather | Rolled each half-day (12.5 min); Clear 22.75% by day, 26.09% by night; preferred weather +35% |
| Season | 576 real minutes (9.6 h), the same on all servers; preferred season +25%, otherwise -15% |
| Aquarium | Pays C$, XP and items hourly |
| Events | Fischfright (Halloween), Fischgiving (live 25 Nov 2026), Fischmas (Gingerbread Rod C$5,000) |

Sources: [Fischipedia: Weather](https://fischipedia.org/wiki/Weather), [Bloxodes locations](https://bloxodes.com/wiki/fisch/locations), [Bloxodes rods](https://bloxodes.com/wiki/fisch/rods). Daily reward and update day: not known. 72 codes are listed ([rblxguide](https://rblxguide.com/games/fisch)).

## 5. Other players

Trading from level 15; the Trade Plaza at 25 uses rented stalls and a separate currency, S$. Theft, combat and co-op rules: not documented. Leaderboards: not known. **Our read:** the clipped moment is a rare mutation landing on a two-million-coin fish in front of other anglers.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Sell Anywhere | Pass | 399 | Sell without walking to a merchant |
| Appraise Anywhere | Pass | 399 | |
| Enchant Anywhere | Pass | 299 | |
| Spawn Boat Anywhere | Pass | 299 | |
| Appraisers Luck | Pass | 299 | Appraisals 25% cheaper; better shiny, sparkling, mutation and weight luck |
| Double XP | Pass | 289 | |
| Supporter | Pass | 169 | Tag, halo, C$1,000, star bobber |
| Emote Pack / Bobber Pack | Pass | 99 each | Cosmetic |

Source: [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5750914919/game-passes?passView=Full&pageSize=50), 25 Nov 2026. Total 2,081 R$. The snapshot matches this table and lists two more passes, Aquarium Boat and Radio, that are not for sale [data, Nov 2026]. No pass raises fishing luck. Best sellers and where offers appear: not known.

**Developer products [data, Nov 2026].** The snapshot reads 300 products, its cap, so the full list may be longer. 295 are on sale; without 14 test or unnamed items and one placeholder at 1,000,000,000 R$, 280 remain, from 7 to 4,499 R$, median 699 R$. 173 are single named items (rod skins, boats and similar, by their names) and 51 are bundles. 12 of 280 products:

| Product | R$ | Kind |
|---|---|---|
| Credit Pack 1 | 39 | Currency ladder, step 1 of 5 |
| Credit Pack 3 | 349 | Step 3 |
| Credit Pack 5 | 1,299 | Step 5 |
| Credit Pack 5 [First Time Offer] | 789 | First-purchase price |
| 1 Token | 19 | Second currency |
| 10 Tokens | 99 | |
| 2X Luck - 1 Hour | 59 | Luck by the hour |
| 2X Luck - 10 Hours | 299 | |
| Extend +30 Min [16x Luck] | 1,299 | Extends a luck boost |
| Luck Potion Tier 1 - Skip | 29 | Skip (tiers 2 and 3: 79, 249) |
| Buy 1x Egg | 99 | Egg (10x: 799) |
| Limited Quests Event - Refresh Quests | 25 | Event refresh (7 R$ the first time) |

Credit amounts are not in the names or descriptions, so credits per Robux cannot be computed. Our arithmetic: Pack 5 costs 33 times Pack 1, and its first-time price is 39% off; 2x luck costs 59 R$ an hour bought singly and 30 R$ an hour in the 10-hour product; a token costs 19 R$ singly and 9.9 R$ in the 10-pack. Six more products sell passes as gifts, at 99 to 499 R$.

**Our read:** the passes are convenience, but luck is sold as a product by the hour, so the point in section 7 about one luck curve for everyone holds for passes only.

## 7. Why it works

Developer statements and retention numbers: not found. Measured: 90.9% like ratio and 78,638 players about two years after the peak.

**Our read:**

- The 8-second reel is short enough to repeat hundreds of times and long enough to fail, and the formula keeps a 1.2-second floor that no rod removes.
- Each fish has a zone, a time, a season and a weather, so the same spot changes every 12.5 minutes and every 9.6 hours.
- The top rods sit behind levels, Bestiary percentages and puzzles, so late progress is content, and coins alone do not finish the game.
- The passes sell convenience (access from anywhere). Luck is sold separately, by the hour, as a product.

## 8. What went wrong

Players now are about 13% of the tracker peak (our arithmetic). Rod prices changed between versions, so lists disagree (Phoenix C$50,000 or 40,000; Abyssal Specter C$300,000 or 850,000). The follower Fish It!, released 7 months later, now has 68,566 players, close to Fisch's 78,638. Complaint threads and economy breaks: not found.

## 9. What to take from it

- A catch of 8 seconds: a 1.2 s lock plus 6.8 s divided by (1 + speed/100).
- A day of 25 minutes, weather re-rolled every 12.5 minutes, seasons of 9.6 hours on all servers.
- Spawn modifiers of -75% off-time, +25% / -15% season, +35% weather.
- Rods gated by level 170 to 250 and by 50% and 100% Bestiary, not only by price.
- Mutations from 1.85x at 1% to 15x at 0.004%, one per fish.
- Nine convenience passes at 99 to 399 R$ and no luck pass.
- Luck as a timed product: 2x for 59 R$ for 1 hour or 299 R$ for 10 hours, half the hourly price at ten times the length [data, Nov 2026].

## Sources

- [Fischipedia](https://fischipedia.org/wiki/Fishing): Fishing, Weather, Bait, Moosewood, Level, Bestiary, Mutations.
- Bloxodes: [rods](https://bloxodes.com/wiki/fisch/rods), [mutations](https://bloxodes.com/wiki/fisch/mutations), [locations](https://bloxodes.com/wiki/fisch/locations); [rblxguide](https://rblxguide.com/games/fisch).
- Roblox [games API](https://games.roblox.com/v1/games?universeIds=5750914919) and [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5750914919/game-passes?passView=Full&pageSize=50), 25 Nov 2026.
- [rowatcher](https://rowatcher.com/games/5750914919).
