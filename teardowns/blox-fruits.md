# Blox Fruits

> You take quests, level up across three seas and hunt for fruits that give powers. It is the template for the anime grind RPG and has held hundreds of thousands of players since 2019.

| | |
|---|---|
| Studio | Not known |
| Released | Created 16 Jan 2019 ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=994732206)) |
| Genre | Anime RPG ([playbook](../genres/anime-rpg.md)) |
| Peak concurrent players | Trackers disagree by more than 3x: 2.8M undated ([Rotrends](https://rotrends.com/game/994732206)) against 823,808 ([Bloxodes](https://bloxodes.com/stats/reports/roblox-october-2026)). October 2026 ran from 174,892 (1 Oct) to 298,041 (31 Oct) |
| Players now | 304,869, 65.66B visits (Roblox public API, 25 Nov 2026) |
| Players per server | 12; sampled public servers were all full, 12 of 12 ([servers API](https://games.roblox.com/v1/games/2753915549/servers/Public?limit=100&sortOrder=Desc)) |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Average session 24.3 minutes, rating 92.3% on about 14M votes, #4 on the Top Earning chart ([Rotrends](https://rotrends.com/game/994732206)).

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Take a quest | Talk to the quest giver; the compass points to the next quest for your level | Not known | Quest text, enemy count | One quest at a time |
| Fight | Defeat 5 to 9 enemies (usually 8) or one boss | Quest 60 to 120 s (community) | Counter goes down | Enemies left |
| Collect | Last enemy falls | | EXP and Beli | e.g. Sky Bandit: 315,000 EXP, 7,000 Beli |
| Level up | Automatic | | Level rises | +3 stat points |
| Spend | Dealer, gacha, swords | Dealer 4 h, gacha 2 h | Stock list | Beli |

Sources: [wiki: Quests](https://blox-fruits.fandom.com/wiki/Quests), [Experience](https://blox-fruits.fandom.com/wiki/Experience), [rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide). Dead time and what the player does during travel: not known. Leaving abandons the quest.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Not known |
| 0:10 to 1:00 | Level-0 quest: 8 Bandits or Trainees for 300 EXP and 350 Beli ([wiki](https://blox-fruits.fandom.com/wiki/Quests)) |
| 1:00 to 5:00 | First quest done, level 1 to 4 (our arithmetic: 86 + 94 + 109 = 289 of 300 EXP) |
| 5:00 to 15:00 | Level 10 after about 6 quests; the Monkey quest pays 2,300 EXP, about 4.8 levels' worth (our arithmetic) |

No developer-stated first-minute flow was found. First fight: inside a minute (our read: nothing gates the level-0 quest). First purchase, first contact with another player and first rare moment: not known. First long goal shown: the gacha at level 50, about 30 quests in (our arithmetic). Nothing is taught except by the compass.

## 3. Progression

**EXP per level** = ceil(2 x L^2.3 + 84); 143.8 billion EXP to reach 2800 ([wiki](https://blox-fruits.fandom.com/wiki/Experience)). Our arithmetic: level 2800 costs 350,000 times level 10.

**Early pacing, normal quests only (our arithmetic, 1 to 2 min per quest):** level 10 after 6 quests, 30 after 17, 60 after 38, 100 after 69, 190 after 138 (2.3 to 4.6 hours). Quests give 2 to 5 levels each until about level 55, then about 1.5. The full table is in the [playbook](../genres/anime-rpg.md#numbers-that-work).

**Seas:** First 0 to 699, Second from 700, Third from 1500, each needing a quest. 99,104,498 players hold the Second Sea badge and 61,461,401 the Third (62.0%) ([badges](https://badges.roblox.com/v1/universes/994732206/badges?limit=100)). Community estimate: 30 to 50 hours for the First Sea, 15 to 25 for each of the others ([bloxmeta](https://bloxmeta.gg/games/blox-fruits/guides/fastest-leveling-guide)).

**Cap:** 2550 at Update 20; 2650 to 2750 on 23 Aug 2025; 2800 by Update 29.3; 3000 on 5 Sep 2026, where EXP stops at 2800 and 40 Island Secret quests give 5 levels each ([Updates/30.0](https://blox-fruits.fandom.com/wiki/Updates/30.0)).

**Fruits:** 42 (Common 7, Uncommon 6, Rare 4, Legendary 11, Mythical 14). Every fruit together: 96,232,500 Beli or 74,380 R$ ([wiki](https://blox-fruits.fandom.com/wiki/Blox_Fruits)). Third-party price list: Rocket 5,000 Beli / 50 R$ up to Dragon 15,000,000 Beli / 5,000 R$ ([games.gg](https://games.gg/roblox/guides/blox-fruits-all-fruits-prices-and-rarities/)).

**Gacha:** 25,000 + 150 x (level - 1) Beli, one roll per 2 hours, from level 50: 32,350 at level 50, 444,850 at 2800. Outcome fixed on the press; no per-fruit odds published; no pity found ([wiki](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Gacha)).

**Races:** first-join roll Human 62.5%, Rabbit, Shark, Angel 12.5% each. V2 at level 850 for 500,000 Beli; V3 2,000,000; full V4 187,250 Fragments ([wiki](https://blox-fruits.fandom.com/wiki/Races)).

**Raids:** five islands, boss at 155,500 HP, 1 to 4 players, join at 700, host at 1,100; chip 100,000 Beli or a fruit; 300 to 1,000 Fragments per raid ([wiki](https://blox-fruits.fandom.com/wiki/Raids)).

## 4. Session and return hooks

| Clock | What happens |
|---|---|
| 60 min (45 on weekends) | A fruit spawns under a random tree; it despawns after 20 min ([wiki: Trees](https://blox-fruits.fandom.com/wiki/Trees), [description](https://games.roblox.com/v1/games?universeIds=994732206)) |
| 1 h | A random First Sea boss may awaken and pay a free gacha roll ([wiki: Bosses](https://blox-fruits.fandom.com/wiki/Bosses)) |
| 2 h | Gacha roll; Mirage dealer (Second and Third Sea) |
| 4 h | Dealer stock, same on every server, at least 3 fruits including Rocket and Spin ([wiki](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Dealer)) |
| 1 to 2 times a month | 2x EXP events, usually weekends (community) |
| 42 to 128 days | A named update |

Named updates ([wiki update pages](https://blox-fruits.fandom.com/wiki/Updates/27.0)):

| Update | Date | Gap to next | What it did |
|---|---|---|---|
| 25 XMAS | 25 Dec 2024 | 113 days | Holiday update; contents not in the sources |
| 26 Gravity | 17 Apr 2025 | 128 days | Not in the sources |
| 27.0 Lightning | 23 Aug 2025 | 69 days | Cap 2650 to 2750 |
| 28 Tiger / Halloween | 31 Oct 2025 | 53 days | Halloween; rest not in the sources |
| 29.0 Control | 23 Dec 2025 | 2 days | Not in the sources |
| 29.1 to 29.3 | Christmas, Valentine's, Easter (28 Mar 2026) | 51, 42 days | Events; cap 2800 by 29.3 |
| 29.5 Dog House | 29 Jul 2026 | 9 days | Event |
| 29.6 Summer PvP Patch | 7 Aug 2026 | 29 days | PvP patch |
| 30.0 Sea 1 Rework | 5 Sep 2026 | | 17 First Sea islands redone, Island Secrets, cap 3000, Dragon rollable from the gacha |

The wiki shows 29.4 on the same date as 29.3, probably an error; if so, 29.3 to 29.5 was 123 days. The game was last changed on 24 Nov 2026. Offline progress: none found.

## 5. Other players

12 per server sharing the same tree fruits and bosses. PvP optional; all progress comes from enemies. Raids for 1 to 4. Trading: not covered by the sources. Leaderboards: not known. Clipped: rare fruits, awakened bosses, a Kitsune in stock (about 0.18% per restock, community figure, [allthings.how](https://allthings.how/blox-fruit-dealer-stock-and-restock-timer-in-blox-fruits-first-sea/)).

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Fruit Notifier | Pass | 2,700 | Alerts to tree spawns |
| Dark Blade | Pass | 1,200 | Sword |
| 2x Mastery | Pass | 450 | Boost |
| 2x Money | Pass | 450 | Boost |
| Fast Boats | Pass | 350 | Travel |
| 2x Boss Drops | Pass | 350 | Drops |
| Permanent fruit | Product | 50 to 5,000 | Power, kept for good, buyable even out of stock |
| 2x EXP | Product | 25 / 99 / 450 / 850 / 1,499 | 15 min / 1 h / 6 h / 12 h / 24 h; never stacks |
| Race reroll | Product | 90 | Or 3,000 Fragments |
| Rocket (physical) | Product | 97 | From the Dog House NPC |
| Private server | Private server | About 100 a month (community) | |

Passes from the [Roblox public API, 25 Nov 2026](https://apis.roblox.com/game-passes/v1/universes/994732206/game-passes?passView=Full&pageSize=100), all six on sale; products from the [wiki](https://blox-fruits.fandom.com/wiki/Experience) and [Races](https://blox-fruits.fandom.com/wiki/Races). The snapshot confirms the product type and every product price above [data, Nov 2026]. Where offers appear and best sellers: not known.

Products [data, Nov 2026]: 152 on sale (a test item and six "[GIFT]" pass copies left out), 25 to 5,000 R$, median 350. 32 are mastery packs (+50 to +400 for each of four weapon types, 1 R$ per point), and three Beli ladders share the same five prices (10,000 to 3M Money); which one a player sees is not known. 12 of 152:

| Product | R$ | Note |
|---|---|---|
| 500 Fragments | 75 | 6.7 Fragments per R$ |
| 2,100 / 4,500 / 10,000 Fragments | 250 / 499 / 999 | |
| 16,000 Fragments | 1,499 | 10.7 Fragments per R$: 60% more (our arithmetic) |
| Change Race (Random) | 90 | Race reroll |
| Spin | 75 | |
| Legendary Scroll / Mythical Scroll | 160 / 500 | 5 Legendary for 800, 3 Mythical for 1,500 |
| +1 Fruit Storage | 400 | |
| Random Fruit | 900 | |
| Dragon | 5,000 | Dearest permanent fruit |

**Our read:** packs of the same mastery cost the same per point at every size, so the bulk bonus sits only on Fragments, the currency for rerolls.

## 7. Why it works

Measured: 24.3-minute sessions, 92.3% approval, full servers, 62% of Second Sea players reach the Third. The developers' own statements: only the game description (cap, fruit timers).

**Our read:**

- The level counter moves about once a minute for the first 3 to 4 hours.
- Three short clocks (1 h spawn, 2 h gacha, 4 h dealer) give every session a lottery on top of the grind.
- Fruit Beli prices span 3,000x but Robux prices only 100x, so the top fruits look cheap in Robux exactly where the grind is longest.
- New levels are added in 100 to 200 level steps behind new content, so finished players get a new goal every few months.

## 8. What went wrong

The sources record no failed update or economy break. Problems visible in the numbers: the gacha's per-fruit odds are unpublished, and a Beli fruit is lost when replaced. The wiki's partial EXP totals (3.32 billion to 700) disagree with its own formula (1.48 billion), so planning numbers need checking against the live game, especially after the Update 30 rework.

## 9. What to take from it

- One quest = 8 enemies in 60 to 120 s, worth 2 to 5 levels early and about 1.5 after level 55.
- EXP per level = 2 x L^2.3 + 84; area gates at about 23% and 50% of the cap (700 and 1500 of 3000).
- A world drop every 60 min (45 on weekends) that despawns after 20.
- A gacha priced at 25,000 + 150 per level, once per 2 hours: about 7 to 9 quests of Beli.
- Shop stock every 4 hours, identical on every server.
- A cap raise of 100 to 200 levels every 2 to 4 months, earned by new quests.

## Sources

- [Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=994732206); [badges](https://badges.roblox.com/v1/universes/994732206/badges?limit=100); [passes](https://apis.roblox.com/game-passes/v1/universes/994732206/game-passes?passView=Full&pageSize=100)
- Blox Fruits wiki: [Quests](https://blox-fruits.fandom.com/wiki/Quests), [Experience](https://blox-fruits.fandom.com/wiki/Experience), [Gacha](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Gacha), [Dealer](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Dealer), [Trees](https://blox-fruits.fandom.com/wiki/Trees), [Raids](https://blox-fruits.fandom.com/wiki/Raids), [Races](https://blox-fruits.fandom.com/wiki/Races), [Bosses](https://blox-fruits.fandom.com/wiki/Bosses), [Updates/30.0](https://blox-fruits.fandom.com/wiki/Updates/30.0)
- Community (unverified): [rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide), [bloxmeta](https://bloxmeta.gg/games/blox-fruits/guides/fastest-leveling-guide), [games.gg](https://games.gg/roblox/guides/blox-fruits-all-fruits-prices-and-rarities/), [allthings.how](https://allthings.how/blox-fruit-dealer-stock-and-restock-timer-in-blox-fruits-first-sea/)
- Trackers: [Rotrends](https://rotrends.com/game/994732206), [Bloxodes](https://bloxodes.com/stats/reports/roblox-october-2026)
- Playbook: [Anime RPG](../genres/anime-rpg.md)
