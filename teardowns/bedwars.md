# BedWars

> Teams collect iron from a generator, buy blocks and weapons, guard their bed and break everyone else's. Once your bed is gone, your next death is final. It peaked at 334,747 players in 2022 and sells 113 kits.

| | |
|---|---|
| Studio | Easy.gg |
| Released | Created 27 May 2021 |
| Genre | Round-based team PvP arena ([genres/shooter.md](../genres/shooter.md)) |
| Peak concurrent players | 334,747 on 27 Aug 2022 ([Rolimons](https://www.rolimons.com/game/6872265039)) |
| Players now | 16,300 (Roblox public API, 25 Nov 2026); 30-day peak 38,010 ([Rolimons](https://www.rolimons.com/game/6872265039)); 11.87B visits |
| Players per server | 40 cap. Squads 16 (4 teams of 4), Doubles 16 (8 x 2), Solo 8, ranked 10 (5v5), 30v30 60 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Collect | Stands at the base generator | 1 iron per second at level 0, cap 100 | Iron pops out | Iron |
| Buy | Spends at the Item Shop | Wool stack every 8 s of iron | Shop menu | Iron, emeralds |
| Defend | Covers the bed with blocks | Bed plating lasts the first 4 minutes | Blocks around the bed | Bed health 20 |
| Raid | Crosses to a map generator or an enemy bed | Emerald every 69 s at tier 1 | Map generators, other teams | Emeralds, diamonds |
| Break | Hits an enemy bed: 6 hits with a wood tool, 2 with diamond | Not known | Bed breaks; that team's deaths become final | Teams alive |
| End | Last team standing; deathmatch starts at 20:00 (Squads) | Our read: 20 to 25 minutes per match | Win screen | Win XP 100 to 400 |

Sources: [Team Generator](https://robloxbedwars.fandom.com/wiki/Team_Generator) (stub), [Item Shop](https://robloxbedwars.fandom.com/wiki/Item_Shop), [Bed](https://robloxbedwars.fandom.com/wiki/Bed), [Emerald Generator](https://robloxbedwars.fandom.com/wiki/Emerald_Generator) (marked outdated), [Classic](https://robloxbedwars.fandom.com/wiki/Classic).

Respawn delay in seconds: not known. A team still alive 60 s after losing its bed is highlighted for the rest of the match. **Our read:** the 20 to 25-minute estimate comes from the deathmatch trigger at 20:00; no page states an average.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Not known |
| 0:10 to 1:00 | Not known |
| 1:00 to 5:00 | Not known. Bed plating protects beds for the first 4 minutes of a match |
| 5:00 to 15:00 | Not known. Emerald generators move to tier 2 at 5:00 and tier 3 at 10:00 |

The wiki has no beginner's guide. Three kits are free each week. The first 5,000 XP of each day counts 2.5 times. Seconds to first fight: not known.

## 3. Progression

**In-match economy.** Prices from the [Item Shop](https://robloxbedwars.fandom.com/wiki/Item_Shop); seconds are our arithmetic at the level-0 base rate of 1 iron a second.

| Item | Price | Seconds of base iron |
|---|---|---|
| Wool x16 | 8 iron | 8 |
| Shears, Stone Sword, pickaxe | 20 iron | 20 |
| Bow | 24 iron | 24 |
| TNT, Gloop | 35 iron | 35 |
| Stone Brick x16 | 40 iron | 40 |
| Leather armour (3 pieces) | 50 iron | 50 |
| Iron Sword | 70 iron | 70 |
| Fireball | 75 iron | 75 |
| Iron armour | 120 iron | 120 (base cap is 100, so collect twice) |
| Siege TNT | 350 iron | 350 |
| Telepearl | 2 emeralds | |
| Diamond Sword | 4 emeralds | |
| Crossbow | 7 emeralds | |
| Diamond armour | 8 emeralds | |
| Emerald Sword | 20 emeralds | |
| The Headhunter | 24 emeralds | |
| Emerald armour | 40 emeralds | |

**Generators.**

| Generator | Rate | Cap |
|---|---|---|
| Base, level 0 | 1 iron / 1 s | 100 |
| Base, level 6 | 1 iron / 0.5 s, 1 diamond / 75 s | 150 |
| Base, level 16 | 1 iron / 0.3 s, 1 diamond / 20 s, 1 emerald / 30 s | 225 |
| Map diamond (since 17 Nov 2023) | 1 / 40 s | 5 uncollected |
| Map emerald, tier 1 to 5 | 69 / 54 / 44 / 34 / 24 s, stepping up every 5 minutes | 3 uncollected |

Breaking an enemy's bed plating gives your team +30% generator speed and 3 diamonds; each further plating adds +10%. Sources: [Team Generator](https://robloxbedwars.fandom.com/wiki/Team_Generator), [Diamond Generator](https://robloxbedwars.fandom.com/wiki/Diamond_Generator), [Emerald Generator](https://robloxbedwars.fandom.com/wiki/Emerald_Generator). The emerald page is marked outdated, and an older history entry on the diamond page describes tiered rates that later changed.

Our arithmetic on one emerald generator: about 4.3 emeralds in minutes 0 to 5, 5.6 in 5 to 10, 6.8 in 10 to 15, 8.8 in 15 to 20, about 25 by 20:00. A Diamond Sword (4 emeralds) takes 276 s at tier 1, close to the 4-minute plating. Emerald armour (40) is out of reach for a team holding one generator before 20:00.

**Account level.** Max 200. XP per level starts at 3,000 and rises 1,000 a level to 52,000 at level 50, then stays flat. Daily cap 52,000 XP. Level 20 needs 250,000 XP in total and level 50 needs 1,375,000 ([Player Level](https://robloxbedwars.fandom.com/wiki/Player_Level)). Our arithmetic: at least 5 days to level 20 and 27 days to level 50; every level past 50 takes at least a day.

**Ranked** ([Ranked](https://robloxbedwars.fandom.com/wiki/Ranked)): account 7 days old and level 20. 5v5 only since Season 16. Each team has 20 seconds to ban 2 kits. Seven ranks with four divisions each (Nightmare has one), 100 RP per division, win +8 to 30 RP, loss -5 to -25. 5 placement matches land between Bronze 1 and Gold 4. Nightmare needs top 200 worldwide.

## 4. Session and return hooks

- **Weekly:** 3 free kits every Friday, 4 from level 20 ([Kit](https://robloxbedwars.fandom.com/wiki/Kit)).
- **Daily:** first 5,000 XP at 2.5x; 52,000 XP cap.
- **Battle pass:** 50 levels. Recent themed passes run 4 weeks: Halloween 2026 ran 23 Oct to 20 Nov ([Halloween 2026](https://robloxbedwars.fandom.com/wiki/Battle_Pass/Halloween_Season_2026)). Earlier seasons ran 8 to 16 weeks or more. Levels pay 500 or 1,000 BedCoins, Gold Lucky Crates, skins and emotes; a free track shares the same levels.
- **Ranked seasons:** Season 14 about 19 weeks (13 Sep 2025 to 23 Jan 2026), Season 15 about 15 weeks (to 8 May 2026).
- **Limited modes:** Arachne's Lair, Marrow's Madness ([Bloxodes](https://bloxodes.com/wiki/bedwars)).
- **XP boosts:** account verification +20%, clan coins up to +50%, AFK area 1 XP per 3 s.

## 5. Other players

Up to 8 teams per match. What can be lost: your bed, and with it your respawns. Plating protects it for 4 minutes (6 in 16v16 and ranked); the Classic page says 8 minutes in Squads, so the wiki contradicts itself. Ranked uses rank-pairing limits against boosting (a Gold player can queue with Platinum and below) and warnings then timeouts for leaving. Top 200 get an emote; Gold and above get a "Victorious" kit skin. Trading: not found.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Standard kit | Pass | 399 (or 10,000 BedCoins) | Character ability |
| Recent kit | Product | 479 (or 12,000 BedCoins) | Character ability |
| Former battle-pass kit | Product | 599 (or 25,000 BedCoins) | Character ability |
| Ember & Lumen Kit Bundle | Pass | 799 | Two kits |
| VIP Rank | Pass | 400 | Not known |
| Battle pass | Pass | 799 | Premium track, +20% pass XP |
| Battle pass level | Product | 300 each, 15,000 for 50 | Skip a level |

Sources: [Kit](https://robloxbedwars.fandom.com/wiki/Kit), [Battle Pass](https://robloxbedwars.fandom.com/wiki/Battle_Pass), [Rolimons](https://www.rolimons.com/game/6872265039). Types and the 300-per-level ladder are from the snapshot [data, Nov 2026]: 49 of 82 passes on sale, 46 of them kits at 399 plus a 399 Clan Pass. The 479 and 599 kits are products, not passes. The season battle passes are passes and were all off sale on 25 Nov 2026; a "Gift Battle Pass" product costs 799. Our arithmetic: kits trade at about 25 BedCoins per Robux, except former pass kits at about 42. Buying every pass level costs 18.8 times the pass. Best sellers: not known.

Products [data, Nov 2026]: 183 on sale (a 1 R$ item, a "test" item and a duplicate left out), 49 to 15,000 R$, median 799. About 70 are kit skins at 799 and 50 are level skips. 12 of 183:

| Product | R$ | Note |
|---|---|---|
| 1,000 Bed Coins | 49 | 20.4 coins per R$ |
| 4,500 / 12,000 Bed Coins | 199 / 499 | |
| 26,000 Bed Coins | 999 | 26.0 coins per R$: 27% more (our arithmetic) |
| 1 Level / 10 Levels / 50 Levels | 300 / 3,000 / 15,000 | No bulk discount |
| Check-In Skip | 49 | |
| New Player Bundle | 149 | |
| Ranked Pass | 200 | |
| Zola Kit | 479 | Recent kit |
| Frost Queen Lyla | 799 | One of about 70 kit skins |

**Our read:** level skips stay at a flat 300 each, while coins get 27% cheaper in bulk, so the game discounts the currency and never the pass shortcut.

## 7. Why it works

No developer statements were found.

**Our read:**
- The bed is a respawn token. Early deaths cost nothing, so new players keep fighting; late deaths are final, so the end of a match is tense.
- Iron at 1 a second makes the first purchase arrive in 8 s and the first real weapon in 70 s.
- Emerald generators speed up every 5 minutes, so the match gets louder toward the 20:00 deathmatch.
- 113 kits with 3 free a week let players try before paying 399 R$.

## 8. What went wrong

Peak 334,747 (Aug 2022) to 16,300 now: a fall of 95%. Cause: not known. The wiki is inconsistent on plating length and lists an outdated emerald page. A source claimed a 3-day "Ranked Season 17" in Aug 2026; the wiki lists ranked seasons only up to 15, so that claim is not used here.

## 9. What to take from it

- Base resource at 1 a second with a cap of 100; cheapest useful item at 8 s, first weapon upgrade at 70 s.
- Respawns free until a team objective falls; protect it for the first 4 minutes.
- A premium resource that speeds up every 5 minutes (69 s to 24 s), with a deathmatch at 20:00.
- Characters sold at one price (399 R$) with 3 free each Friday.
- A 50-level, 4-week themed pass at 799 R$, levels at 300 R$.
- Ranked behind a 7-day account and about 5 days of capped XP.

## Sources

- [Roblox games API](https://games.roblox.com/v1/games?universeIds=2619619496), read 25 Nov 2026
- [Rolimons](https://www.rolimons.com/game/6872265039)
- BedWars Fandom wiki: [Classic](https://robloxbedwars.fandom.com/wiki/Classic), [Ranked](https://robloxbedwars.fandom.com/wiki/Ranked), [Team Generator](https://robloxbedwars.fandom.com/wiki/Team_Generator), [Diamond Generator](https://robloxbedwars.fandom.com/wiki/Diamond_Generator), [Emerald Generator](https://robloxbedwars.fandom.com/wiki/Emerald_Generator), [Item Shop](https://robloxbedwars.fandom.com/wiki/Item_Shop), [Bed](https://robloxbedwars.fandom.com/wiki/Bed), [Kit](https://robloxbedwars.fandom.com/wiki/Kit), [Battle Pass](https://robloxbedwars.fandom.com/wiki/Battle_Pass), [Player Level](https://robloxbedwars.fandom.com/wiki/Player_Level)
- [Bloxodes BedWars](https://bloxodes.com/wiki/bedwars)
