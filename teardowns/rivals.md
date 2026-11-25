# RIVALS

> Short gun duels, first to 5 rounds, queued from pads on a shared lobby floor. It is the only Roblox shooter at scale in 2026.

| | |
|---|---|
| Studio | Nosniy Games |
| Released | Created 26 May 2024 |
| Genre | Duel shooter ([genres/shooter.md](../genres/shooter.md)) |
| Peak concurrent players | 967,342 on 14 Feb 2026 ([Rolimons](https://www.rolimons.com/game/17625359962)) |
| Players now | 163,930 (Roblox public API, 25 Nov 2026); 19.47B visits |
| Players per server | 40 per lobby; fights are 1v1 to 5v5, Free For All 16 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Queue | Presses Play or steps on a Duel Zone pad in the lobby | Not known | Lobby with pads | Queue count |
| Map | Votes; in ranked each team bans one map and two weapons, and three maps narrow to one | Not known | Map cards | None |
| Round | Fights to elimination; up to 2 weapon swaps per duel | Not known | 100 health; sniper 50 body, 150 head | Health |
| Timeout | More combined health wins the round; an exact tie goes to a random side | Timer not known | Graveyard map rings a church bell for sudden death | Round score |
| Match | First to 5 round wins | 5 to 9 rounds | Win screen | Tasks, contracts, pass |

Sources: [Bloxguides](https://bloxguidesgg.com/games/rivals), [wiki: Game Hints](https://robloxrivals.fandom.com/wiki/Game_Hints), [wiki: Gamemodes](https://robloxrivals.fandom.com/wiki/Gamemodes).

Cycle time, dead time and round length: not known. Other modes: Team Deathmatch to 250 points (2 per elimination) or 8 minutes; Free For All 16 players for 8 minutes with the top 5 counted as winners; Gun Game moves you up one weapon per elimination or assist. The wiki counts 21 modes ([Bloxodes](https://bloxodes.com/wiki/rivals/gamemodes)).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Not known |
| 0:10 to 1:00 | Not known. New players hold Assault Rifle, Handgun, Fists and Grenade |
| 1:00 to 5:00 | Optional Shooting Range tasks; Beginner 2v2 queue on the Arena map, where enemies show through walls at round start |
| 5:00 to 15:00 | Not known |

Beginner Tasks are one-off and pay Keys: visit the range 1, break 5 targets 1, slide 3 times 1, equip the Scythe 2, Scythe dash 3 times 2, throw a grenade 2, play a Beginner 2v2 3, eliminate 5 players 3, win a duel 3. Our arithmetic: 18 Keys in all ([wiki: Tasks](https://robloxrivals.fandom.com/wiki/Tasks)). The Beginner 2v2 is closed to players above a win threshold. First purchase: the Uzi at 20 Keys, 2 more than the beginner tasks pay. Seconds to first fight: not known.

## 3. Progression

Weapons are bought with Keys ([Bloxguides](https://bloxguidesgg.com/games/rivals)):

| Tier | Keys | R$ at 4.5 to 4.9 per Key (our arithmetic) | Days of daily tasks at 6 Keys (our arithmetic) |
|---|---|---|---|
| Assault Rifle | free | | |
| Uzi | 20 | about 98 | day 1 after beginner tasks |
| Wildcat | 35 | about 170 | 3 |
| Standard | 0 to 75 | up to about 370 | up to 10 |
| Prime | 200 to 550 | about 900 to 2,700 | 31 to 89 |
| Contraband | 575 to 700 | about 2,600 to 3,400 | 93 to 114 |

Day counts assume the 18 beginner Keys and only the three daily tasks; bonus tasks (6 more Keys) halve them. Login reward amounts are not known.

**Ranked** ([Miraheze](https://robloxrivals.miraheze.org/wiki/Ranked), [Timesaver](https://timesaver.gg/blog/roblox-rivals-ranked)):

| Rule | Value |
|---|---|
| Gate (Season 4) | Level 100, 10 duels, 50 tasks, account 30 days old, hardware attestation, Roblox age check |
| Placement | 10 matches, capped at Diamond I |
| Divisions | Bronze 0 / 200 / 400 up through Onyx 3,000 / 3,200 / 3,400 in 200-ELO steps; Nemesis 3,600; Archnemesis top 200 |
| Decay | From Onyx I: play 10 duels every 3 days or lose 100 ELO a day |
| Protection | One free ELO Shield a day below Platinum I |
| Party | Within 400 ELO (800 in Season 3); Nemesis and above queue 3v3 only |
| Settings | Aim assist halved and capped at 0.5; Auto Shoot locked to Dynamic; no third person |
| Season reward | Glory = 1,250 x (wins / 250) + 1,250 x (final ELO / 3,600), cap 2,500, plus up to 500 from the Ranked Contract; a weapon reward at 200 ranked wins in Seasons 0 and 1 |

Timesaver reports that spending 200 Robux can clear the Roblox-side checks.

**Contracts** reward time and kills per weapon: a Charm Capsule at 5 minutes, a wrap at 20 minutes, a Wrap Box at 6 hours; elimination steps at 5, 100, 250, 2,000, 10,000 and up to 40,000 ([wiki: Contracts](https://robloxrivals.fandom.com/wiki/Contracts)).

## 4. Session and return hooks

- **Daily tasks:** play 5 duels 1 Key, eliminate 15 players 2 Keys, win 2 duels 3 Keys. Bonus tasks after that: play 12 duels, eliminate 40, win 12 duels, for another 6 Keys ([wiki: Tasks](https://robloxrivals.fandom.com/wiki/Tasks)). Free daily login rewards.
- **Season Pass:** 70 tiers. One tier per 25 duel round wins or 20 minutes played, capped at 7 tiers, then paused for 7 days ([wiki: Season Pass](https://robloxrivals.fandom.com/wiki/Season_Pass)). Our arithmetic: 10 weeks to finish free, and 140 minutes of play a week fills the cap. The pass also grants 10 Skin Tickets a season.
- **Ranked decay** on a 3-day clock for the top ranks.
- **Updates:** Update 10 (28 Feb 2025, ranked added), 15 (26 Sep 2025), 17 (12 Dec 2025), 20 (24 Apr 2026), 22 (4 Sep 2026), 25 (about 14 Nov 2026, Season 4). Our arithmetic: one update about every 6 weeks.
- **Rotating modes:** Juggernaut (one player at 3,000 health against 7 at 100), Swift Standoff (1 health, one revolver round), and co-op event towers, one with 17 floors and a boss on floor 10 ([Bloxodes](https://bloxodes.com/wiki/rivals/gamemodes)).

## 5. Other players

40 players share a lobby and see each other on the pads. Leaving a ranked match counts as a loss and locks you out for 15 minutes. Top 200 get a Mythical Arch skin; everyone placed gets a rank charm. A win worth +0 ELO grants a "Stomp" charm. Trading: not found. Private duels: not found on the wiki.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| 10 / 40 / 90 / 450 / 1,100 Keys | Product | 49 / 199 / 449 / 2,199 / 4,999 | Currency for weapons and cosmetics |
| Skin Case | Product | 249 (shop shows 245); 724 for three | Random skin |
| Pass tiers 1 / 5 / 10 / 20 / 70 | Product | 99 / 499 / 999 / 1,999 / 6,999 | Skip pass tiers |
| Starter | Pass | 59 | Bundle |
| RPG | Pass | 95 | Bundle |
| Medkit Bundle | Pass | 289; 202 in the snapshot, named "[30% OFF]" | Bundle |
| Exogun | Pass | 649; 454 in the snapshot, "[30% OFF]" | Bundle |
| Standard Weapons | Pass | 849; 799 in the snapshot, "[20% OFF]" | Bundle |
| Classic | Pass | 865 | Bundle |
| Energy | Pass | 975 | Bundle |
| Heavy Duty | Pass | 1,425 | Bundle |

Sources: [Bloxguides](https://bloxguidesgg.com/games/rivals), [Rolimons](https://www.rolimons.com/game/17625359962), [wiki: Season Pass](https://robloxrivals.fandom.com/wiki/Season_Pass). Prime Pass price: not known. The snapshot has these 8 passes on sale and Pixel Bundle off sale; the discount sits only in the names, as the API's base price equals the sale price [data, Nov 2026].

**Developer products [data, Nov 2026].** 175 on sale, 15 to 6,999 R$; 78 are "GIFT" copies. The other 97 have a median of 549 R$. They disagree with the sources above: the Key packs, named Key, Mega, Super, Ultra and Legendary Key Bundle, cost 59 / 199 / 385 / 1,649 / 3,749, while their gift copies keep the older 49 / 199 / 449 / 2,199 / 4,999; a Skin Case costs 289 and three cost 545; 10 pass levels cost 799. 12 more of the 97:

| Product | R$ | Kind |
|---|---|---|
| +30 / +40 / +50 / +60 Season Pass Levels | 2,999 / 3,199 / 4,999 / 5,999 | Level skips (9 steps, 1 to 70) |
| Daily Skin A (Common / Rare / Legendary) | 299 / 359 / 599 | Daily shop, slots A to E |
| Spooky Prize Wheel | 30 | Spin (10 for 249, 25 for 599) |
| Refresh Tasks | 15 | Task reroll |
| Legendary Candy Bundle | 3,749 | Event currency, priced like Keys |
| Super Starter Bundle! | 67 | Starter |

Our arithmetic, if the Key amounts above still hold: 0.17 Keys per R$ in the smallest pack and 0.29 in the largest. A spin costs 30 R$ singly and 24 R$ in the 25 pack; 40 levels cost 3,199 R$, 80 a level against 99 for one.

Keys also buy cosmetics: Charm Capsule 3, Wrap Box 5, Finisher Pack 10, featured wrap 25, universal wrap 250. The Prize Wheel (Update 22) lists 4 Keys 35%, 2 Goodie Bags 25%, 10 Keys 20%, Celestial wrap 15%, Skin Ticket 4%, Legendary Light Fifty skin 0.5%; the list sums to 99.5%. Our arithmetic: 3.4 Keys per spin on average from the Key slots. How spins are earned: not known. Best sellers: not known.

## 7. Why it works

No developer statements were found. Measured: 967,342 peak, 163,930 now, 98.2M favorites (Roblox public API, 25 Nov 2026).

**Our read:**
- The duel is short and always ends with a winner, through the health fallback at the timer.
- The lobby is the queue. Players walk onto a pad instead of waiting in a menu.
- New players fight new players first, and see enemies through walls for a moment.
- Ranked is a long goal with a high fence (Level 100, 30-day account) and a season reward that pays for wins as much as for rank.
- Free Keys (6 a day) put a mid-tier gun about a month away, so Robux buys time, not access.

## 8. What went wrong

Reports that mobile aim assist stops working after updates, from a low-quality source ([marix.app](https://marix.app/library/games/rivals-mobile-aim-assist-broken)). An undated patch note cut aim assist field of view from 180 to 15 degrees and doubled its strength; it may be stale. The fan wiki lags the live game: it names Seasons 0 to 3 while Season 4 is live. Peak to now is a fall of 83% in nine months. Cause: not known.

## 9. What to take from it

- First to 5 rounds, 1v1 to 3v3; the timer gives the round to the side with more combined health.
- Beginner queue below a win threshold, one map, enemies briefly visible.
- First gun costs 20 against 18 beginner Keys; a mid gun costs about 31 days of free Keys.
- Ranked gate: Level 100, 10 duels, 50 tasks, 30-day account; placement capped at Diamond I.
- Decay only from Onyx I: 10 duels every 3 days or minus 100 ELO a day.
- 70-tier pass, 7 tiers a week by play, 99 R$ a tier to skip.
- Daily skin products in 5 slots (A to E), each at three rarities: 299 common, 359 to 449 rare, 479 to 599 legendary [data, Nov 2026].

## Sources

- [Roblox games API](https://games.roblox.com/v1/games?universeIds=6035872082), read 25 Nov 2026
- [Rolimons](https://www.rolimons.com/game/17625359962)
- [Bloxguides RIVALS](https://bloxguidesgg.com/games/rivals)
- [Bloxodes modes](https://bloxodes.com/wiki/rivals/gamemodes)
- [RIVALS Fandom wiki](https://robloxrivals.fandom.com/wiki/Gamemodes): Gamemodes, Tasks, Contracts, Season Pass, Game Hints, Ranked
- [Miraheze Ranked](https://robloxrivals.miraheze.org/wiki/Ranked)
- [Timesaver: Season 4 ranked](https://timesaver.gg/blog/roblox-rivals-ranked)
