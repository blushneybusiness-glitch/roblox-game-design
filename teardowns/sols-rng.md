# Sol's RNG

> You press one button every 3.2 seconds and get an aura labelled "1 in N"; it matters because it is three years old, still has about 40,000 players, and does it with one button and a set of clocks built around it.

| | |
|---|---|
| Studio | Sol's Studio |
| Released | 3 December 2023 (Roblox public API) |
| Genre | RNG rolling ([genres/rng.md](../genres/rng.md)) |
| Peak concurrent players | About 156K, April 2026 (one tracker, [rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29)) |
| Players now | 40,264 (Roblox public API, 25 Nov 2026); 2.316B visits; 91.4% like ratio |
| Players per server | 20; private servers are free |
| Teardown date | 25 November 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Roll | Presses roll, or Auto Roll does it | 3.2 (spin plus cooldown); 1.2 with Quick Roll | Spin | Roll count |
| Result | Reads it | 0 below the cutscene threshold; above it not known | Aura and "1 in N"; cutscene and chat line from 1 in 1,000 | Best aura owned |
| Keep | Equips, stores or deletes | about 1 (our read) | Storage | Slots used |
| Bonus roll | Nothing | Every 10th roll (32 s at base) | Bonus marker | Luck x2 |
| Craft | Spends auras and potions | not known | Jake's Workshop, Stella's Cauldron | Basic luck |

Sources: [wiki: Rolling](https://sol-rng.fandom.com/wiki/Rolling), [Cutscenes](https://sol-rng.fandom.com/wiki/Cutscenes), [Luck](https://sol-rng.fandom.com/wiki/Luck).

Cycle time 3.2 s, so 1,125 rolls an hour, or 3,000 with Quick Roll (our arithmetic). Dead time is the spin itself. Auto Roll is free for joining the studio's Roblox group, so the roll continues while the player crafts, walks or runs the obby for Basic Blessing (+30% luck for 1 minute, back every 2 minutes in public servers) ([rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide)).

## 2. First session

Times are our arithmetic at 3.2 s a roll ([wiki: Tutorial](https://sol-rng.fandom.com/wiki/Tutorial)).

| Time | What happens |
|---|---|
| 0:00 to 0:10 | First roll, equip it |
| 0:10 to 1:00 | 10 rolls for the tutorial daily quest: Tutorial Potion and 400 coins. "A Road to Gears" accepted: 1,000 coins |
| 1:00 to 5:00 | Gear Basing crafted (one Common, Uncommon, Good, Rare); roll 60; Luck Glove crafted (2 Divinus, 1 Crystallized, 3 Rare), about 64 to 100 rolls in |
| 5:00 to 15:00 | Obby for Basic Blessing; then a roll rarer than 1 in 1,000 (about 48 minutes at base), the Lunar Device, roll 150, potion deliveries |

First reward at about 0:32. First rare moment (1 in 1,000 or rarer): about 48 minutes on average with no luck items. First purchase: not known. First contact with another player: not documented; **our read** is the first chat line announcing someone's Epic roll. First long goal shown at about 5:00 (the second quest batch). Teaching is a skippable quest chain of 10 quests in 3 batches.

## 3. Progression

The ladder ([rblxguide aura tiers](https://rblxguide.com/games/sols-rng/updates/auras-list-by-rarity)): Basic (1 to 999, 20 auras), Epic (1,000+, 27), Unique (10,000+, 25), Legendary (99,999+, 23), Mythic (999,999+, 58), Exalted (10M+, 48), Glorious (100M+, 54), Transcendent (1B to 7.5B, 6 plus 2 crafted), Dimensional (7.5B to 12.5B, 1, crafted). 169 event auras. First auras: 1 in 2, 4, 5, 8, 16, 32, 64.

The luck formula ([wiki: Luck](https://sol-rng.fandom.com/wiki/Luck)): Luck = ((1 + Basic Luck) x Bonus Roll + Special Luck) x VIP. Aura odds are divided by luck and floored.

| Source | Kind | Value |
|---|---|---|
| Lucky Potion | Basic, 60 s | +25%, 1,000 coins from Mari |
| Fortune I / II / III | Basic, 300 s | +50% / +75% / +100%, brewed from 10 / 25 / 50 Lucky Potions |
| Luck Glove / Frozen Gauntlet / Ragnaroker | Basic, gear | +25% / +150% / +455% |
| Bonus roll | Multiplies Basic | x2 every 10th roll; Gravitational Device x6 |
| Heavenly Potion | Special, one roll | +150,000 (250 Lucky Potions plus four auras) |
| VIP / VIP+ | Final | x1.2 / x1.2 (x1.3 with VIP) |

Speed: Speed Potion +10% for 1 minute (2,000 coins); Haste I to III +20% to +30% for 5 minutes ([wiki](https://sol-rng.fandom.com/wiki/Haste_Potions)).

Biomes are timed world states. Windy, Snowy and Rainy start at 1 in 500, 600 and 750 per second and last 2 minutes, so one arrives every 8 to 12 minutes on average (our arithmetic). Rarer ones run from Sandstorm (1 in 3,000, 650 s) to Dreamspace (1 in 3,500,000, 192 s) ([Bloxodes](https://bloxodes.com/wiki/sols-rng/biomes)). A biome's own auras roll at better odds inside it and 3x worse outside.

Storage size: one guide says 6 slots with a 400-coin first expansion; the wiki does not confirm it.

## 4. Session and return hooks

| Clock | What happens |
|---|---|
| 32 s | Bonus roll |
| 2.5 min | Day and night swap; Solar and Lunar drop from 1 in 50,000 to 1 in 5,000 in their half |
| 8 to 12 min | A common biome, announced in chat |
| 1 to 2.5 h | A rare biome |
| Daily | Quests; VIP gets 3 rerolls |
| Season | Season pass (Season IX now) |
| Events | Valentine's (14 Feb 2026, 10 auras), Boss Raid Chapter 2 (28 Feb 2026, 10 auras and a boss) |

Offline progress: none documented. Update day: not known; last update 24 November 2026 (Roblox public API).

## 5. Other players

Others see your rolls: from 1 in 1,000 a chat line with your name and the odds; from 1 in 10,000 a drop beat and lines flashing around the map; from 1 in 100 million every screen in the server turns monochrome, with thunder, a beam and a "[GLOBAL]" line ([wiki: Cutscenes](https://sol-rng.fandom.com/wiki/Cutscenes)). Whether the global line reaches other servers is not stated. Trading, theft, co-op and leaderboards: not known. **Our read:** the Glorious screen effect is the clip, because it happens to 20 people at once.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| RNG Premium Pass Season IX | Pass | 499 | Season rewards; eight earlier season passes are off sale |
| VIP+ | Pass | 350 | x1.2 final luck (x1.3 with VIP), auto item collection |
| VIP | Pass | 249 | x1.2 final luck and quest rewards, 3 daily quest rerolls, walk speed |
| Quick Roll | Pass | 100 | Removes the spin; about 1.2 s per roll; 20-minute free trial |
| Invisible Gear | Pass | 80 | |
| Starter Pack | Pass | 49 | Title, gear, potions, 15,000 coins |
| Merchant Teleporter | Pass | 40 | |

Source: [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5361032378/game-passes?passView=Full&pageSize=50), 25 Nov 2026. Black Friday prices on the wiki: VIP 175, VIP+ 245, Quick Roll 70 ([wiki](https://sol-rng.fandom.com/wiki/Gamepasses)). The snapshot matches the table: 7 passes on sale, 8 older season passes and 3 Innovator packs off sale [data, Nov 2026]. Best sellers: not known. Where offers appear: not known.

**Developer products [data, Nov 2026].** 110 on sale. Without 50 gift copies, 3 ad items parked at 1,000,000,000 R$ and one named "not used", 56 remain, 10 to 10,000 R$, median 250 R$. There is no currency pack. The game sells themed packages in volumes of 3 or 4, 7 donation products (10 to 10,000 R$) and small utilities. 12 of 56:

| Product | R$ | Kind |
|---|---|---|
| Update Package Alpha | 150 | 20 Potion Chests and 5 Rare Potion Chests |
| Update Package Alpha [Black Friday] | 120 | Sale copy |
| Update Package Delta | 750 | Top of 4 volumes |
| Ticket Package I | 250 | 10 Lucky Tickets and potion gift boxes |
| Ticket Package III | 750 | |
| 2026 Halloween Package I | 199 | Event package (II: 499) |
| 2026 Halloween Package III | 799 | |
| Random Merchant Token | 150 | Summons a merchant |
| One-time Biome Randomizer | 80 | Rerolls the biome once |
| Reroll daily quest | 10 | Quest reroll |
| Bossraid Rental Aura Reroll | 20 | Reroll |
| R$10,000 Donation! | 10,000 | Donation, top of 7 |

Our arithmetic: each Black Friday copy is 20% off (120/150, 200/250, 360/450, 600/750). Volume III of a package costs 3.0 to 4.0 times volume I (Ticket 750/250, Halloween 799/199). Update Package Alpha works out to 6 R$ a potion chest.

## 7. Why it works

Developer statements and measured retention: not found. What is measured: 91.4% like ratio from 1.58M votes and a peak in its third year.

**Our read:**

- Four clocks of different lengths (32 s, 2.5 min, 8 to 12 min, hours) mean one is always close to finishing, so the one button never feels static.
- The ladder spans about 10 factors of ten. At base speed a 1 in 1,000,000 aura takes about 800 hours of rolling (our arithmetic), so luck items have a job at every stage.
- Crafting eats the junk: Fortune III costs 1,250 luck-minutes of Lucky Potions and returns 500, which removes duplicates and coins while giving a strong 5-minute window.
- The announcement ladder turns a private roll into a server event from 1 in 1,000 up.

## 8. What went wrong

Players now are about 26% of the tracker peak (our arithmetic). Potion values changed between eras, so guides disagree: a Lucky Potion was reported at +25% and +100%, and Fortune III at +100% and +250%; the wiki gives +25% and +100%. Peak history comes from one tracker only. Complaints, economy breaks: not found.

## 9. What to take from it

- A 3.2-second roll, cut to 1.2 seconds by a 100 R$ pass.
- A ladder of 9 tiers from 1 in 2 to 1 in 12.5 billion, one factor of ten per tier.
- A bonus roll at x2 luck every 10th roll.
- Announcements at 1 in 1,000 (chat), 1 in 10,000 (map), 1 in 100 million (whole server).
- Three common biomes at 1 in 500 to 750 per second, 2 minutes each.
- Potion tiers that cost 10, 25 and 50 of the tier below for +50%, +75%, +100%.
- No currency for sale: packages in 3 to 4 volumes per event, volume III at 3 to 4 times volume I, rerolls at 10 to 20 R$ [data, Nov 2026].

## Sources

- [Sol's RNG wiki](https://sol-rng.fandom.com/wiki/Luck): Rolling, Luck, Cutscenes, Biomes, Tutorial, Gamepasses, potion pages.
- [Bloxodes biomes](https://bloxodes.com/wiki/sols-rng/biomes); [rblxguide beginners guide](https://rblxguide.com/games/sols-rng/updates/beginners-guide); [rblxguide aura tiers](https://rblxguide.com/games/sols-rng/updates/auras-list-by-rarity).
- Roblox [games API](https://games.roblox.com/v1/games?universeIds=5361032378), [votes API](https://games.roblox.com/v1/games/votes?universeIds=5361032378), [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5361032378/game-passes?passView=Full&pageSize=50), 25 Nov 2026.
- [rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29).
