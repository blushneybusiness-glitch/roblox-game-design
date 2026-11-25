# Tower Defense Simulator

> You place and upgrade towers against 20 to 50 waves with up to three friends, and unlock new towers with coins and levels. It mattered because it set its all-time peak more than six years after it was created, with no summon banner.

| | |
|---|---|
| Studio | Paradoxum Games |
| Released | Universe created 5 Jun 2019; launch date not known |
| Genre | [Tower defense](../genres/tower-defense.md), classic (unlock by coins and level) |
| Peak concurrent players | 159,824 on 4 Oct 2025 ([Rolimons](https://www.rolimons.com/game/3260590327)) |
| Players now | 12,114 (Roblox public API, 25 Nov 2026); 30-day peak 65,994 |
| Players per server | 50 in the lobby; matches split cash for up to 4 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Other public numbers: 5.10B visits, 3.55M favourites, 94.1% rating, average playtime 12.96 minutes ([Rolimons](https://www.rolimons.com/game/3260590327)).

## 1. Core loop

Easy mode, the mode for new players ([TDS wiki Easy Mode](https://tds.fandom.com/wiki/Easy_Mode)):

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Start | Enters a match with $500 ($600 with group bonus) | 0 | Map, path, empty slots | Cash 500 |
| Place | Places Scouts at $125 | 0 to 20 | Tower appears | Cash down |
| Wave | Towers fire; kill cash arrives | timer 1:00, skip after 0:20 | Cash per kill | Wave bonus (200 + 160 x (waves - 1)) x (1 - 0.1 x players) |
| Upgrade | Buys tower levels | between waves | Model changes | Scout DPS 1 to 24.6 |
| Counter | Adds a hidden-detection tower | before wave 8 | Hidden enemies pass blind towers | Lives |
| Boss | Kills the Brute on wave 20 (no timer) | about 7:00 total | Triumph | 300 coins, 50 EXP, 25 tower EXP |

Cycle time: about 7 minutes a match. Our arithmetic: 420 seconds for 20 waves is 21 seconds a wave, so players skip almost every wave as soon as the skip button appears at 0:20. Dead time inside a match: not measured. Cash comes only from kills; the solo player also gets a clear bonus of 35% of the wave bonus (20% in a party).

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | not known |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | not known |
| 5:00 to 15:00 | not known |

No tutorial or first-session record was found. What the wiki gives: the player starts at level 0 owning two towers, Scout and Sniper; Easy mode has no level gate; a first triumph pays 300 coins plus 100 coins once from the "Recruit" badge ([TDS wiki Towers](https://tds.fandom.com/wiki/Towers), [Levels](https://tds.fandom.com/wiki/Levels)).

**Our read** from those numbers: first reward at about 7:00 (the first triumph); first purchase right after it, since 300 coins buys Paintballer (100) and Demoman (200); the 50 EXP from that win clears the 48.5 EXP needed for level 1. Two wins, about 14 minutes, buy the whole 100 / 200 / 300 starter set. Teaching is done by the enemy order: a new type about every 2 waves (Speedy at 2, Slow at 4, Hidden at 8, Armored at 13, Enraged at 17).

## 3. Progression

**Tower unlocks** ([TDS wiki Towers](https://tds.fandom.com/wiki/Towers)):

| Tier | Towers and coin prices |
|---|---|
| Free | Scout, Sniper |
| Starter | Paintballer 100, Demoman 200, Boomerang 300, Slime Trooper 300, Soldier 350 |
| Intermediate | Freezer 650, Assassin 800, Militant 800, Shotgunner 850, Hunter 1,000, up to Crook Boss (level 30) |
| Advanced | Commander 4,000 up to Gatling Gun 35,000 (level 175) |
| Hardcore (level 50) | Paid in gems: Brawler 1,250 up to Hacker 5,500 |
| Evolved | Gems plus 15,000 coins, base tower at tower level 20 |

**Tower upgrades.** Scout: place $125, upgrades $50, $375, $1,350, $2,200, total $4,100. Cost per DPS goes from $125 to $166.5 ([TDS wiki Scout](https://tds.fandom.com/wiki/Scout)). Tower EXP: 50 at level 1, growing 1.09 per level, 2,549 to level 20; skipping costs 499 gems.

**Player levels.** EXP to next level is 45 + 3.5 x next level for levels 0 to 10, 8 x next level for 10 to 40, 260 + 1.5 x next level above 41 ([TDS wiki Levels](https://tds.fandom.com/wiki/Levels)). Our arithmetic: level 5 needs 277.5 EXP (about 6 Easy wins), level 10 needs 642.5 (about 13).

**Mode gates** (third-party table, [Bloxodes](https://bloxodes.com/wiki/tower-defense-simulator/modes); Hardcore confirmed on the official wiki):

| Mode | Waves | Level |
|---|---|---|
| Easy | 20 | none |
| Casual | 25 | none listed |
| Intermediate | 30 | 5 |
| Molten | 35 | 15 |
| Fallen | 40 (Hidden Wave to 42) | 30 |
| Challenge Trials | 40 | 40 |
| Hardcore | 45 | 50 |
| Voidcore | 50 | 50, after a Hardcore triumph |
| Frost | 40 | 60 |
| Sandbox | not listed | 250 |

**Hardcore** ([TDS wiki](https://tds.fandom.com/wiki/Hardcore_Mode)): starting cash solo $900, duo $750, trio $600 each; kill cash split 50% or 33%; about 40 minutes; consumables off; final boss Void Reaver on wave 45; pays gems by formula plus a 250-gem triumph bonus. Our arithmetic: 53 seconds a wave, and a trio starts with 2 times the solo cash, not 3.

## 4. Session and return hooks

- Weekend 2x EXP, Friday to Sunday; VIP adds 1.25x.
- A triumph guarantees one extra item: consumable 50%, ticket 30%, crate or support item 20%.
- Skin crates: Basic Crate 500 coins; daily skin store at 500, 750 and 1,000 coins ([TDS wiki Basic Crate](https://tds.fandom.com/wiki/Basic_Crate)).
- Live events and an event store (Operation I.C.E, Null & Void, Surf & Turf, Spring Frenzy, Halloween 2025 named on the [wiki](https://tds.fandom.com/wiki/Events)); battle pass currency at 16 or 17 per Hardcore wave in recent passes.
- Limited towers sold for a fixed window (Commando "only available until 1 Dec 2024").
- Update day and time: not known.

## 5. Other players

Lobby of 50. Matches of 1 to 4 with cash split (kill cash 50 / 33 / 25% for 2 / 3 / 4 players; wave bonus cut 10% per player). VIP adds map voting. PVP exists from level 25 with ELO. No trading is documented. Badges show how few reach the top: "Triumph Hardcore" is held by 236,527 players on the current version and 999,814 on the old one, against 5.10B visits. What gets clipped: not known.

## 6. Money

From the public pass list, 25 Nov 2026 ([pass endpoint](https://apis.roblox.com/game-passes/v1/universes/1176784616/game-passes?passView=Full&pageSize=100)):

| Item | Type | R$ | What it does |
|---|---|---|---|
| VIP | Pass | 375 | Map voting, auto wave skip, rainbow tag, +25% EXP, 3 premium crates, 3 tower pets shown |
| Crook Boss | Pass | 225 | Skips level 30 |
| Mortar | Pass | 300 | Skips level 75 |
| Turret | Pass | 340 | Skips level 50 |
| Cowboy | Pass | 340 | Skips 4,000 coins after Badlands II |
| Warden / Saboteur | Pass | 450 / 449 | Skip coin-and-map unlocks |
| Time Dilator | Pass | 1,299 | Skips level 50 and 3,000 gems |
| Mercenary Base | Pass | 1,350 | Skips level 150 |
| Pursuit | Pass | 1,500 | Skips 15,000 coins and level 100 |
| Engineer / Hacker | Pass | 1,690 / 2,249 | Hardcore towers (4,500 / 5,500 gems at level 50) |
| Gatling Gun | Pass | 1,949 | Skips 35,000 coins at level 175 |
| Sandbox Plus+ | Pass | 7,999 | Instant sandbox, admins, legacy content |
| Skin bundles | Pass | 300 to 360 | Cosmetic |

About 30 limited and event passes are off sale. The snapshot agrees (19 on sale, 31 off) and adds three small passes on sale: Custom Music 85, Resize Your Player! 70, Meme Emotes 55 [data, Nov 2026]. The wiki notes regional pricing and price tests of about plus or minus 25% ([TDS wiki Gamepasses](https://tds.fandom.com/wiki/Gamepasses)). Where offers appear and best sellers: not known.

**Developer products [data, Nov 2026].** The snapshot reads 300, its cap. 277 are on sale; without 43 gift copies, 5 parked at 99,999 R$ or more and 1 test item, 228 remain, 20 to 2,500 R$, median 108.5 R$. 140 of them buy one event-pass rank each, across about 12 events. 12 of 228:

| Product | R$ | Kind |
|---|---|---|
| 1,000 Coins | 70 | Coin ladder, smallest of 5 |
| 25,000 Coins | 1,500 | Largest |
| 100 Gems | 70 | Gem ladder, smallest of 5 |
| 5,000 Gems | 2,500 | Largest |
| 3x Revive Tickets | 29 | Revive |
| 3x Spin Tickets | 49 | Spin |
| Exp Boost | 110 | Boost |
| Rank 1 - Hexscape | 32 | Event-pass rank |
| Rank 19 - Hexscape | 68 | |
| Corrupted Touch - Skip | 399 | Event mission skip (7 at 299 to 399) |
| All Levels (Kingpin) | 1,199 | Tower levels (8 towers, 479 to 1,199) |
| Premium Crate | 60 | Crate (25 to 399) |

Our arithmetic: coins come at 14.3 per R$ in the smallest pack and 16.7 in the largest; gems at 1.4 and 2.0. Most ranks cost 30 R$ plus 2 R$ per rank number (Rank 19: 68), and a few ranks about 100 R$ more (Rank 12: 154).

## 7. Why it works

No developer statement was found. Measured: 94.1% rating and a 2025 peak six years after creation. **Our read:**

- Every tower can be had three ways (coins, level, Robux), so nobody is locked out and payers skip time.
- Easy mode pays the first two towers in one 7-minute win.
- Enemy types arrive on a schedule, so each new tower answers a problem the player has just met.
- Hardcore at level 50 is a long goal that about 236,000 players have finished on the current version.

## 8. What went wrong

The player count falls between events: 12,114 now against a 30-day peak of 65,994, 7.6% of the all-time peak. The wiki's pass rows needed a second check before individual prices could be quoted. Specific failed updates: not known.

## 9. What to take from it

- A 20-wave, 7-minute intro mode with a 60-second wave timer and a skip at 20 seconds.
- First win pays 300 coins against starter towers at 100, 200 and 300.
- A new enemy type every 2 waves; hidden enemies by wave 8.
- Per-player starting cash drops 900 / 750 / 600 for 1 / 2 / 3 players.
- Early-unlock price rises with the level skipped: 225 R$ at level 30, 1,949 R$ at level 175.
- Mode gates at levels 5, 15, 30, 50 and 60.
- Event-pass ranks sold one at a time, 30 R$ plus 2 R$ per rank, so the last ranks of a pass cost about twice the first [data, Nov 2026].

## Sources

- [Rolimons TDS](https://www.rolimons.com/game/3260590327); Roblox public API, 25 Nov 2026
- TDS wiki: [Easy Mode](https://tds.fandom.com/wiki/Easy_Mode), [Hardcore Mode](https://tds.fandom.com/wiki/Hardcore_Mode), [Towers](https://tds.fandom.com/wiki/Towers), [Scout](https://tds.fandom.com/wiki/Scout), [Levels](https://tds.fandom.com/wiki/Levels), [Gamepasses](https://tds.fandom.com/wiki/Gamepasses), [Basic Crate](https://tds.fandom.com/wiki/Basic_Crate), [Events](https://tds.fandom.com/wiki/Events)
- [TDS pass endpoint](https://apis.roblox.com/game-passes/v1/universes/1176784616/game-passes?passView=Full&pageSize=100)
- [Bloxodes TDS modes](https://bloxodes.com/wiki/tower-defense-simulator/modes) (third party)
- Genre: [genres/tower-defense.md](../genres/tower-defense.md)
