# Anime RPG and dungeon crawler

> **The feeling sold:** "Every quest makes me stronger, and one day I will find the fruit everyone wants."

This page covers the anime grind RPGs (Blox Fruits, King Legacy, Grand Piece Online) and the dungeon crawlers (Dungeon Quest, World // Zero, Pixel Blade). **No developer-stated combat timings and no documented first-minute flow were found for any of these games.** Every minute count below is our arithmetic from wiki tables and community estimates.

## At a glance

| | |
|---|---|
| Core verb | Take a quest, defeat about 8 enemies, level up |
| Study these first | [Blox Fruits](../teardowns/blox-fruits.md): the template, with a published EXP formula and three seas. King Legacy: a tiered key gacha with published odds. World // Zero: a 10-world dungeon chain with difficulty tiers. Dungeon Quest: a 17-dungeon ladder, and a warning. |
| Session that works | 21 to 24 minutes: Blox Fruits 24.3, King Legacy 22.9, Grand Piece Online 20.8; the roguelite Pixel Blade 7.5 ([Rotrends](https://rotrends.com/game/994732206)) |
| Players per server | 12 for Blox Fruits, King Legacy and World // Zero; Pixel Blade 20; Dungeon Quest 40; Grand Piece Online instanced ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=994732206,1451439645,3808081382,4568630521,4777817887,2380077519,3508322461,6161049307,4730278139,1359573625,1390601379)) |
| Who owns the genre | Games from 2018 and 2019. Blox Fruits (created January 2019) had 304,869 players and King Legacy (December 2019) 43,030 on 25 Nov 2026 ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=994732206)). The newest crawler in the sources, Pixel Blade (June 2024), had 1,938. The old crawlers are near zero: Dungeon Quest 51, Swordburst 3 15. |
| Build cost | Not known. What makes it expensive is content per level: Blox Fruits has 34 bosses and 42 fruits; Dungeon Quest built 17 dungeons in six years. |
| Money comes from | Permanent power items (fruits 50 to 5,000 R$), boosts (2x EXP, 2x drops), and notifiers that watch a timer for you (2,699 to 2,700 R$) |
| What kills clones | Running out of content: a crawler whose newest dungeon is 13 months old has 51 players. |

## Why people play it

The grind RPGs hold 21 to 24 minutes per session against 11 to 16 for battlegrounds games. Every progress bar in Blox Fruits and King Legacy comes from enemy and boss kills; PvP is optional ([description](https://games.roblox.com/v1/games?universeIds=994732206)). Approval is high: Blox Fruits 92.3% on about 14M votes, King Legacy 91.5%, World // Zero 94.7%, Pixel Blade 96.8% ([Roblox votes API, 25 Nov 2026](https://games.roblox.com/v1/games/votes?universeIds=3808081382,3508322461,994732206,4730278139,4568630521,1390601379,4777817887,2380077519,1451439645,648454481,1359573625,985731078,848145103,6161049307)). Blox Fruits was #4 on the Top Earning chart, King Legacy #22 ([Rotrends](https://rotrends.com/game/1451439645)). Ages and devices: not known.

**Our read:** the player wants a long project with a number that always moves (the quest bar) plus a lottery on top (fruit spawns, the dealer, the gacha).

## The loop, with a stopwatch

Blox Fruits ([wiki: Quests](https://blox-fruits.fandom.com/wiki/Quests), [Experience](https://blox-fruits.fandom.com/wiki/Experience)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Take a quest | Talk to the quest giver; the compass points to the next quest for your level | Not known | Quest text with an enemy count | One quest at a time |
| Fight | Defeat 5 to 9 enemies, usually 8, or one boss | Whole quest 60 to 120 s (community, [rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide)) | Counter on the quest | Enemies left |
| Finish | Last enemy falls | | EXP and Beli | First quest: 300 EXP, 350 Beli |
| Level up | Automatic | | Level rises | +3 stat points |
| Spend | Fruit, sword or gacha roll | Dealer every 4 h, gacha every 2 h | Dealer stock | Beli |

Leaving the game abandons the quest. Our arithmetic: if all of a quest were fighting, one enemy takes 8 to 15 seconds.

**How the others differ.** King Legacy has 4 stats and 12,400 points; three can reach 4,250 and the fourth only 400, so a build is a choice ([wiki](https://king-legacy.fandom.com/wiki/Beginners_Guide)). Grand Piece Online finds fruits under trees, by fishing, in chests and dungeons ([description](https://games.roblox.com/v1/games?universeIds=648454481)). The crawlers replace the quest with a timed run: Dungeon Quest's dungeons have 9 to 15 minute limits; World // Zero gives 3 lives on Normal and 3 end chests of which you open 2 ([wiki](https://world-zero.fandom.com/wiki/Dungeons)).

**The loop stack (Blox Fruits):**

| Every | What finishes |
|---|---|
| 8 to 15 s | One enemy (our arithmetic) |
| 1 to 2 min | One quest, worth 1.5 to 5 levels early on |
| 20 min | A tree fruit despawns |
| 45 to 60 min | A fruit spawns under a random tree |
| 1 h | A random First Sea boss may awaken and pay a free gacha roll |
| 2 h | One gacha roll; the Mirage dealer restocks |
| 4 h | The fruit dealer restocks |
| One session (24 min) | 16 to 34 levels early in the First Sea (our arithmetic below) |
| Weekend | Fruit every 45 min; 2x EXP events once or twice a month (community) |
| 42 to 128 days | A named update |

## The first five minutes

No source documents the first minute of Blox Fruits, King Legacy or Grand Piece Online.

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | Not known | |
| 0:30 | A quest is available at level 0: 8 Bandits or Trainees for 300 EXP and 350 Beli | [wiki: Quests](https://blox-fruits.fandom.com/wiki/Quests) |
| 1:00 | First fight. Dungeon Quest: Desert Temple is open on first join | Our read: nothing gates either ([Dungeon Quest wiki](https://dungeonquestroblox.fandom.com/wiki/Dungeons)) |
| 3:00 | First quest done, level 1 to 4 | Our arithmetic: levels 1 to 3 need 86 + 94 + 109 = 289 of the 300 EXP |
| 5:00 | Level 10 needs about 6 Bandit quests | Our arithmetic below |

King Legacy keeps new players on its Starter Island until level 50 ([wiki](https://king-legacy.fandom.com/wiki/Beginners_Guide)). Jujutsu Infinite's tutorial is finished by 69.3% of players ([badges](https://badges.roblox.com/v1/universes/3808223175/badges?limit=100)).

**Gates for a new game (Our read):** a quest at level 0 with its enemies in view; the first level-up inside 90 seconds; each of the first quests worth 2 or more levels.

## Numbers that work

**Blox Fruits, the first 15 quests.** EXP and Beli from the [wiki](https://blox-fruits.fandom.com/wiki/Quests). EXP to level up is ceil(2 x L^2.3 + 84) ([wiki: Experience](https://blox-fruits.fandom.com/wiki/Experience)). The last three columns are our arithmetic, with the community's 1 to 2 minutes per quest. Update 30 reworked the First Sea, so check against the live game.

| # | Enemy | Min level | Quest EXP | Beli | EXP to level up at min level | Levels per quest | Minutes per level |
|---|---|---|---|---|---|---|---|
| 1 | Bandit / Trainee | 0 | 300 | 350 | 86 | 3.5 | 0.3 to 0.6 |
| 2 | Monkey | 10 | 2,300 | 800 | 484 | 4.8 | 0.2 to 0.4 |
| 3 | Gorilla | 15 | 4,500 | 1,200 | 1,099 | 4.1 | 0.2 to 0.5 |
| 4 | Gorilla King (boss) | 20 | 9,500 | 2,000 | 2,050 | 4.6 | boss |
| 5 | Pirate | 30 | 13,000 | 3,000 | 5,078 | 2.6 | 0.4 to 0.8 |
| 6 | Brute | 40 | 22,000 | 3,500 | 9,762 | 2.3 | 0.4 to 0.9 |
| 7 | Chef (boss) | 55 | 45,000 | 8,000 | 20,215 | 2.2 | boss |
| 8 | Desert Bandit | 60 | 45,000 | 4,000 | 24,676 | 1.8 | 0.5 to 1.1 |
| 9 | Desert Officer | 75 | 65,000 | 4,500 | 41,168 | 1.6 | 0.6 to 1.3 |
| 10 | Snow Bandit | 90 | 90,000 | 5,000 | 62,571 | 1.4 | 0.7 to 1.4 |
| 11 | Snowman | 100 | 150,000 | 5,500 | 79,706 | 1.9 | 0.5 to 1.1 |
| 12 | Yeti (boss) | 105 | 220,000 | 10,000 | 89,161 | 2.5 | boss |
| 13 | Chief Petty Officer | 120 | 225,000 | 6,000 | 121,185 | 1.9 | 0.5 to 1.1 |
| 14 | Vice Admiral (boss) | 130 | 415,000 | 15,000 | 145,664 | 2.8 | boss |
| 15 | Sky Bandit | 150 | 315,000 | 7,000 | 202,405 | 1.6 | 0.6 to 1.3 |

**Our arithmetic, repeating the best normal quest at each level (no bosses, no enemy drops):**

| Reach level | Quests | Minutes | Quest Beli earned | Fruit that Beli buys |
|---|---|---|---|---|
| 10 | 6 | 6 to 12 | 2,100 | none |
| 30 | 17 | 17 to 34 | 14,500 | Spin (7,500) |
| 60 | 38 | 38 to 76 | 85,000 | Bomb (80,000) |
| 100 | 69 | 69 to 138 | 223,000 | Spike (180,000) |
| 150 | 103 | 103 to 206 | 420,500 | Sand (420,000) |
| 190 | 138 | 138 to 276 | 665,500 | Light (650,000) |

Fruit prices from an undated third-party list ([games.gg](https://games.gg/roblox/guides/blox-fruits-all-fruits-prices-and-rarities/)); the column assumes the player saves every Beli and the dealer has the fruit.

**Our read:** a new player gets 2 to 5 levels per quest up to level 55, then about 1.5. The level counter moves about once a minute for the first 3 to 4 hours. Bosses pay 2 to 3 times a normal quest on the same island: a jump the player can see coming.

**The seas: First to Second to Third.**

| | First Sea | Second Sea | Third Sea |
|---|---|---|---|
| Levels | 0 to 699 | 700 to 1499 | 1500 to 2800, +200 from Island Secrets |
| Players with the badge | Not in the badge list | 99,104,498 | 61,461,401 (62.0% of Second Sea) |
| EXP to cross, from the formula | 1.48 billion | 16.8 billion | 125.5 billion |
| Hours (community) | 30 to 50 | 15 to 25 | 15 to 25 (to the old 2550 cap) |

The Second Sea adds raids, race upgrades, a second dealer and boats; the Third adds race V4 and sea danger levels ([Raids](https://blox-fruits.fandom.com/wiki/Raids), [Races](https://blox-fruits.fandom.com/wiki/Races), [Sea](https://blox-fruits.fandom.com/wiki/Sea)). Sources: [badges](https://badges.roblox.com/v1/universes/994732206/badges?limit=100), [bloxmeta](https://bloxmeta.gg/games/blox-fruits/guides/fastest-leveling-guide). The wiki states 3.32 billion EXP to level 700 and 23 billion more to 1500, but summing its own formula gives 1.48 and 16.8 billion; both reach 143.8 billion at 2800. Which partial figure is right is not known. King Legacy's same step keeps 45.5% (6,093,073 to 2,771,404, [badges](https://badges.roblox.com/v1/universes/1451439645/badges?limit=100)).

**Our read:** 82% to 87% of all EXP sits in the Third Sea, yet the community's hours are heaviest in the First. Quest EXP grows faster than the EXP each level needs, so a level costs 2.6 to 4.3 minutes in the First Sea and 0.9 to 1.4 in the Third (our arithmetic from the community hours). Late play feels faster than early play.

**Level caps.** Blox Fruits: 2550 at Update 20; 2650 to 2750 on 23 Aug 2025; 2800 by Update 29.3 (28 Mar 2026); 3000 on 5 Sep 2026, where EXP stops at 2800 and 40 Island Secret quests add 5 levels each ([Updates/27.0](https://blox-fruits.fandom.com/wiki/Updates/27.0), [Updates/30.0](https://blox-fruits.fandom.com/wiki/Updates/30.0)). King Legacy 5450 (an older wiki page says 5,000), Grand Piece Online 675, World // Zero 175, Dungeon Quest's top dungeon level 215. Our arithmetic: level 2800 costs 169.6M EXP, 350,000 times level 10.

**Clocks.**

| Clock | Game | What happens |
|---|---|---|
| 60 min (45 on weekends) | Blox Fruits | One fruit under a random tree, up to 2 in private servers |
| 20 min | Blox Fruits | A tree fruit despawns; dropped fruits do not |
| 1 to 2 h, then 15 min | King Legacy | Fruit spawn, then despawn |
| 2 h | Blox Fruits | One gacha roll; Mirage dealer restocks |
| 4 h | Blox Fruits | Dealer restocks at 00, 04, 08, 12, 16, 20, same on every server, always with Rocket and Spin |
| 5 h | King Legacy | Black Market restocks |
| Friday to Sunday | Grand Piece Online | 2x Legendary and Mythical fruit rates, 2x boss drops, 1.25x EXP |
| Thursday, Monday | World // Zero | Loot Mayhem extra drop; Nightmare Monday 2x coins |

Sources: [Trees](https://blox-fruits.fandom.com/wiki/Trees), [Dealer](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Dealer), descriptions of [Blox Fruits](https://games.roblox.com/v1/games?universeIds=994732206), [King Legacy](https://games.roblox.com/v1/games?universeIds=1451439645) and [GPO](https://games.roblox.com/v1/games?universeIds=648454481), [King Legacy: First Sea](https://king-legacy.fandom.com/wiki/First_Sea), [World // Zero](https://world-zero.fandom.com/wiki/Dungeons). Sources disagree on whether the dealer runs on UTC or Pacific time ([Beebom](https://beebom.com/blox-fruits-stock/)).

**Our arithmetic:** a tree fruit is on the map 20 of every 60 minutes on weekdays (33%), 20 of 45 on weekends (44%). A 24-minute session overlaps a dealer restock 10% of the time. **Our read:** most sessions miss the restock, and the 2,700 R$ Fruit Notifier is sold against exactly that.

**The gacha price formula.** 25,000 + 150 x (level - 1) Beli per random fruit, once per 2 hours, from level 50: 32,350 at level 50, 129,850 at 700, 444,850 at 2800. The result is fixed when the button is pressed; odds are worse than natural spawns and unpublished ([wiki](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Gacha)). Our arithmetic against quest Beli: 9.2 Brute quests at level 50, 7.2 Snowman quests at 100, 6.8 Sky Bandit quests at 150. **Our read:** a roll costs 7 to 18 minutes of quests and the 2-hour cooldown keeps it a treat. The price grows linearly while income grows faster, so it gets relatively cheaper with level.

**Fruit prices: Robux compresses what Beli spreads.** From the same third-party list: Rocket 5,000 Beli or 50 R$ (100 Beli per R$), Quake 1,000,000 or 1,500 (667), Kitsune 8,000,000 or 4,000 (2,000), Dragon 15,000,000 or 5,000 (3,000). Beli prices span 3,000x, Robux prices 100x. All 42 fruits cost 96,232,500 Beli or 74,380 R$ ([wiki](https://blox-fruits.fandom.com/wiki/Blox_Fruits)). **Our read:** Dragon takes 15 times Quake's grind but costs only 3.3 times its Robux, so Robux looks cheapest where the grind is longest. A Robux fruit is permanent; a Beli fruit is lost when replaced.

**King Legacy's key gacha** ([wiki: Gacha](https://king-legacy.fandom.com/wiki/Gacha)), from level 100:

| Key | How you get it | Epic | Legendary | Keys per Legendary (our arithmetic) |
|---|---|---|---|---|
| Copper | 25,000 Beli, max 10 per hour | 1% | 0.05% | 2,000 |
| Iron | 3 gems | 2.5% | 0.1% | 1,000 |
| Gold | 15 gems | 12% | 0.5% | 200 |
| Platinum | Trade in fruits (Common 1 point to Legendary 30) | 37.5% | 2.5% | 40 |
| Diamond | 3 Platinum + 15 iron ingots + 35 rusted scraps | 45% | 10% | 10 |
| Iridium | 10 Diamond + 10 aqua gems | 45% | 35% | 2.9 |

**Our arithmetic:** a Legendary by copper alone costs 50M Beli and 200 hours of cooldown. Iron and gold cost the same gems per Legendary (3,000) and nearly the same per Epic (120 and 125). Gems come only from the Golden Arena, codes and some world bosses. No pity was found in King Legacy or Blox Fruits.

**Dungeon Quest's ladder** ([wiki: Dungeons](https://dungeonquestroblox.fandom.com/wiki/Dungeons)):

| Dungeons | Levels by difficulty | Time limit | Added |
|---|---|---|---|
| Desert Temple | 1, 5, 15 | 15 min | 2018, remade Dec 2023 |
| Winter Outpost | 30, 40, 50 | 15 min | 2019, remade Mar 2024 |
| Seven, Pirate Island to Steampunk Sewers | 60 to 125: two difficulties 5 apart, 10 levels between dungeons | 9 to 12 min | Mar to Oct 2019 |
| Orbital Outpost, Volcanic Chambers | 135 to 155 | 9 to 12 min | 2020 |
| Aquatic Temple, Enchanted Forest, Northern Lands | 160 to 185 | 11 to 12 min | 2021 |
| Gilded Skies | 190, 195 | 11 min | Nov 2022 |
| Yokai Peak | 200, 205 | 15 min | Oct 2023 |
| Abyssal Void | 210, 215 | 15 min | 11 Oct 2024 |

Our arithmetic: 8 dungeons in 2019, then 2, 3, 1, 1, 1 a year. The newest was 13 months old when 51 people were playing (the root place may undercount). Average clear times are not published.

**World // Zero's world funnel**: players who beat each world's final boss, from 5,956,411 for World 1 to 754,936 for World 8 ([badges, Roblox public API, 25 Nov 2026](https://badges.roblox.com/v1/universes/985731078/badges?limit=100)). The wiki lists 10 worlds; badges cover 8.

| World | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Share of World 1 | 100% | 59.9% | 42.6% | 31.7% | 24.3% | 18.8% | 17.0% | 12.7% |
| Kept from the world before | | 59.9% | 71.2% | 74.3% | 76.7% | 77.5% | 90.1% | 74.6% |

World levels run from 1 to 12 (World 1) to 130 to 135 (World 10); cap 175; EXP to level L is L x 30 x (L + 1) + 10 ([wiki](https://world-zero.fandom.com/wiki/Character_Levels)). Challenge difficulty doubles enemy damage, allows 1 life, removes the lowest drop tier and doubles Epic and Legendary drops; Nightmare also doubles health; Insane is 4x damage and health with only Legendary drops in Worlds 1 to 10.

**Our read:** the first step loses 40%, then each step keeps about three quarters. Pixel Blade's Normal-to-Nightmare clear keeps 14.6% (4.66M to 0.68M, [badges](https://badges.roblox.com/v1/universes/6161049307/badges?limit=100)): about 1 in 7 replays a map on a harder tier.

**Grand Piece Online: paid access and weekends.** 1,993,690 players hold a "Paid Access Token" badge against 22,845,079 for "A New Adventure" ([badges](https://badges.roblox.com/v1/universes/648454481/badges?limit=100)): our arithmetic, 8.7% of all players joined while entry cost Robux. It adds Friday-to-Sunday boosts, shorter fruit timers for premium, a battle royale, and seasonal battle passes; Season 8 sold as one 6,999 R$ pass ([passes](https://apis.roblox.com/game-passes/v1/universes/648454481/game-passes?passView=Full&pageSize=100)). Deepwoken, with permanent character loss, charges 400 R$ to enter and sells only emotes ([description](https://games.roblox.com/v1/games?universeIds=1359573625)).

**Start with** (derived from the tables above; tune it):

| Setting | Value | Why |
|---|---|---|
| Players per server | 12 | Blox Fruits, King Legacy, World // Zero; Blox Fruits servers sampled 12 of 12 |
| Quest | 8 enemies, 60 to 120 s | Blox Fruits |
| EXP per level | a x L^2.3 + b, scaled to your cap | Blox Fruits formula |
| Quest EXP | 3 to 5 levels per quest to level 25, 2 to 2.5 to level 55, then about 1.5 | First-15 table |
| Area gates | At about 23% and 50% of the cap; expect about 60% of gate-two players to pass gate three | 700 and 1500 of 3000; 62% badge step |
| World drop | One per server every 60 min, gone after 20; every 45 min on weekends | Blox Fruits |
| Gacha | Once per 2 h, priced at 7 to 9 quests of currency, base + 150 per level | Blox Fruits formula |
| Shop | Every 4 h, same on every server, 2 staples always in | Blox Fruits dealer |
| Cap raise | 100 to 200 levels per step, earned by new quests, every 2 to 4 months | Blox Fruits 2650 to 3000 |
| Dungeon | 9 to 15 minute limit, a new dungeon every 10 levels, two difficulties 5 levels apart | Dungeon Quest |
| Hard tier | 2x monster stats, 1 life, lowest loot tier removed, top drops doubled | World // Zero Challenge |

## What brings them back

**Later in the same session.** The next level is 1 to 2 minutes away. Bosses pay a jump: Dough King and Tyrant of the Skies give 6 levels each ([rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide)). Our arithmetic: a 24-minute session contains a weekday fruit spawn 40% of the time (24 of 60 minutes).

**Tomorrow.** Per day, our arithmetic: 6 dealer restocks, 12 gacha windows, 24 tree spawns per server (32 on weekends). Pixel Blade pays "wishes" for daily login ([description](https://games.roblox.com/v1/games?universeIds=6161049307)). King Legacy's copper keys refill at 10 per hour.

**Next week and after.** Weekend boosts; World // Zero's Thursday and Monday events; Blox Fruits 2x EXP events once or twice a month (community); cap raises every few months; Blox Fruits races (V2 at level 850 for 500,000 Beli, V3 2,000,000, full V4 187,250 Fragments, [wiki](https://blox-fruits.fandom.com/wiki/Races)).

## Other players

Twelve players share each tree fruit and boss; Blox Fruits public servers sampled full on 25 Nov 2026 ([servers API](https://games.roblox.com/v1/games/2753915549/servers/Public?limit=100&sortOrder=Desc)). PvP is optional. Co-op: Blox Fruits raids are five islands ending in a 155,500 HP boss for 1 to 4 players, from level 700, paying 300 to 1,000 Fragments ([wiki](https://blox-fruits.fandom.com/wiki/Raids)); King Legacy raids take 6, Pixel Blade parties 4. What can be lost: a Beli fruit when replaced; in Deepwoken, the character. The clip: a rare fruit under a tree, a Kitsune in stock (about 0.18% per restock, community figure, [allthings.how](https://allthings.how/blox-fruit-dealer-stock-and-restock-timer-in-blox-fruits-first-sea/)), an awakened boss.

## Money

| Game | Item | R$ |
|---|---|---|
| Blox Fruits | Fruit Notifier; Dark Blade; 2x Mastery, 2x Money; Fast Boats, 2x Boss Drops | 2,700; 1,200; 450 each; 350 each |
| Blox Fruits | Permanent fruits; race reroll | 50 to 5,000; 90 |
| Blox Fruits | 2x EXP for 15 min, 1 h, 6 h, 12 h, 24 h (never stacks) | 25, 99, 450, 850, 1,499 |
| Jujutsu Infinite | Item Notifier; Heavenly Restriction | 2,699; 1,699 |
| Grand Piece Online | Season 8 battle pass; private servers; race reroll | 6,999; 525; 250 |
| World // Zero | +1 Item Drop; VIP; Offline Incubator | 1,299; 799; 599 |
| Dungeon Quest | Extra Item; 2x Gold; VIP | 1,200; 540; 480 |

Passes from the Roblox public API, 25 Nov 2026 ([Blox Fruits](https://apis.roblox.com/game-passes/v1/universes/994732206/game-passes?passView=Full&pageSize=100)); 2x EXP from the [wiki](https://blox-fruits.fandom.com/wiki/Experience).

**Our read:** the notifier is the dearest pass in Blox Fruits and Jujutsu Infinite, above any sword: it sells time against a clock the player cannot watch. A 6 to 24 hour boost sold into a 24-minute average session targets heavy players. The hardcore RPGs sell almost no power (Deepwoken emotes, Peroxide a trading sign and donations, Arcane Odyssey cosmetics). Where offers appear and best sellers: not known.

**Policy.** Random fruits next to paid boosts and premium discounts bring Roblox's paid-random-item rules into play; see [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

**Blox Fruits.** Named updates from December 2024 to September 2026 came 113, 128, 69, 53, 2, 51 and 42 days apart, then events on 29 Jul and 7 Aug 2026 and the Sea 1 rework on 5 Sep 2026 ([wiki](https://blox-fruits.fandom.com/wiki/Updates/30.0)). Two of them raised the cap (27.0 and 30.0), several were holiday events, and 30.0 rebuilt 17 First Sea islands. The full table is in the [teardown](../teardowns/blox-fruits.md#4-session-and-return-hooks). The game changed again on 24 Nov 2026. Gaps never ran past about 4 months.

**The crawlers.** Dungeon Quest: last update 17 Oct 2026, last dungeon 11 Oct 2024, 51 players. Swordburst 3: untouched since 27 Feb 2026, 15 players. Type Soul went private and returned on 16 Jul 2026 with a new team: 29 players despite 819M visits ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=848145103,4093155512)).

**What a small team can sustain.** Not known. **Our read:** a quest island is the unit of content: two or three normal quests plus a boss, covering about 30 levels (Jungle 10 to 29, Pirate Village 30 to 59, Desert 60 to 89).

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Players near zero, rating still high | No new dungeon for a year: Dungeon Quest, 91.8%, 51 players | A new dungeon or tier every 2 to 4 months |
| Players near zero after a freeze | Swordburst 3: last update Feb 2026, 15 players | Never a quarter without content |
| A comeback that brings nobody back | Type Soul, back after a year: 29 players | Keep a small rhythm instead of a long pause |
| Players stop at the cap | The grind is finished | Raise the cap 100 to 200 levels through new quests (Island Secrets) |
| Steep drop at the last gate | King Legacy keeps 45.5% from Second to Third Sea, Blox Fruits 62% | Give the middle area new systems (raids, races) |
| Mid-game feels slow | Quest EXP below 1 level | Keep quest EXP growing faster than the curve |

## Checklist

- [ ] A quest is offered at level 0.
- [ ] First level-up within 90 seconds of the first fight.
- [ ] Each of the first 5 quests gives at least 2 levels.
- [ ] A level-up every 0.5 to 1.5 minutes for the first 3 hours.
- [ ] Stat totals capped so not every stat can be maxed (King Legacy: 12,400 points for 4 stats of up to 4,250).
- [ ] Three clocks under 4 hours (spawn, gacha, shop), shown in game.
- [ ] A weekend boost on fixed days.
- [ ] Area gates at about a quarter and a half of the cap.
- [ ] Hard tiers double monster stats and remove the lowest loot tier.
- [ ] Odds published for every random roll.
- [ ] A named update at least every 4 months.

## Twists and open space

**Already produced hits:** paid entry with permanent character loss (Deepwoken, 400 R$, 2,459 players on 25 Nov 2026); a run-based roguelite crawler (Pixel Blade, 7.5-minute sessions, 96.8%); paid access phases and season passes (Grand Piece Online); tiered keys that turn spare fruits into better rolls (King Legacy's Platinum key).

**Under-served (all Our read):**

- A crawler built for 7 to 8 minute runs, with a timed first minute.
- A grind RPG without seas and fruits: Blox Fruits and King Legacy both use them, and Grand Piece Online is built on fruits too.
- A crawler that keeps shipping dungeons: Dungeon Quest and Swordburst 3 lost their players after the updates stopped, while Dungeon Quest's rating stayed at 91.8%.

## Sources

- Teardown: [Blox Fruits](../teardowns/blox-fruits.md). Related: [foundations/06-progression-and-economy.md](../foundations/06-progression-and-economy.md), [foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md), [foundations/13-live-ops.md](../foundations/13-live-ops.md), [fighting playbook](fighting.md).
- Roblox public API, 25 Nov 2026: [games](https://games.roblox.com/v1/games?universeIds=994732206), badges ([Blox Fruits](https://badges.roblox.com/v1/universes/994732206/badges?limit=100), [King Legacy](https://badges.roblox.com/v1/universes/1451439645/badges?limit=100), [World // Zero](https://badges.roblox.com/v1/universes/985731078/badges?limit=100), [GPO](https://badges.roblox.com/v1/universes/648454481/badges?limit=100)), passes as linked.
- Wikis: [Blox Fruits Quests](https://blox-fruits.fandom.com/wiki/Quests), [Experience](https://blox-fruits.fandom.com/wiki/Experience), [Gacha](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Gacha), [Dealer](https://blox-fruits.fandom.com/wiki/Blox_Fruit_Dealer), [King Legacy Gacha](https://king-legacy.fandom.com/wiki/Gacha), [Dungeon Quest Dungeons](https://dungeonquestroblox.fandom.com/wiki/Dungeons), [World // Zero Dungeons](https://world-zero.fandom.com/wiki/Dungeons).
- Community guides (unverified): [rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide), [bloxmeta](https://bloxmeta.gg/games/blox-fruits/guides/fastest-leveling-guide), [games.gg](https://games.gg/roblox/guides/blox-fruits-all-fruits-prices-and-rarities/).
- Trackers: [Rotrends](https://rotrends.com/game/994732206), [Bloxodes October 2026 report](https://bloxodes.com/stats/reports/roblox-october-2026).
