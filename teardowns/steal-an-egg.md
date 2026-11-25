# Steal An Egg

> Train Speed on a treadmill, run into a farther biome, grab an egg and get it home before the guardian or another player knocks you down. The biggest slop hit of 2026 and the bridge between [steal-and-defend](../genres/steal-and-defend.md) and [plus-one](../genres/plus-one.md).

| | |
|---|---|
| Studio | Misfitsbsthree and Brockodile, owned by DoBig Studios ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games)) |
| Released | 25 Jul 2026 |
| Genre | Steal and defend, with a trained stat |
| Peak concurrent players | 14.27M to 14.31M, Saturday 19 Sep 2026 ([RoStats](https://rostats.io/records) 14,313,917; [Rolimons](https://www.rolimons.com/game/107778070777162) 14,293,524; [RoVitals](https://rovitals.com/game/107778070777162) 14,272,591) |
| Players now | 852,482, first on Roblox (Roblox public API, 25 Nov 2026, 13:53 UTC); 6.84M on Saturday 21 Nov 2026 |
| Players per server | 7 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Train | Runs on the treadmill in the base | Steps per second not known | Speed rises per step | +2 per step (free treadmill) to +12,750 |
| Go out | Runs to a biome the Speed allows | not known | Gate: Lake at 900 Speed, Desert at 10K | Speed checked |
| Grab | Takes an egg from a wild animal | not known | The biome's guardian chases | Bigger eggs pay more but slow the carrier |
| Run home | Carries the egg | not known | Guardians and players knock carriers down; bats and bear traps make them drop it ([Bloxodes](https://bloxodes.com/wiki/steal-an-egg)) | Egg kept or lost |
| Grow and hatch | Waits | Hatch time not known | Egg grows in the base | x2 with a 467 R$ pass |
| Earn | Nothing | 1 s ticks | Pet in the base | $1/s (Chicken) to $5B/s |

Eggs in each biome reset every 5 minutes ([Eggs](https://stealanegg.fandom.com/wiki/Eggs)). The wait for money is filled by training. At launch the treadmill also showed a short-video feed; see section 8.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Start near the Forest, which has no gate; its guardian is a Chicken |
| 0:10 to 1:00 | First egg grabbed and run home |
| 1:00 to 5:00 | First pet earns: Chicken ($1/s) 34% or Dog ($2/s) 24% of Forest eggs ([Drop Rates](https://stealanegg.fandom.com/wiki/Drop_Rates)) |
| 5:00 to 15:00 | Training toward 900 Speed for the Lake: 450 steps on the free treadmill (our arithmetic); the Sci-Fi treadmill (15K) is the first upgrade |

Every line is our reconstruction from the wiki tables. Hatch time, starting cash and the first-minute flow are not known. First rare moment: the Forest's 1% Brr Brr Patapim. First contact with players: on the first run home.

## 3. Progression

**Biome gates** ([Biomes](https://stealanegg.fandom.com/wiki/Biomes)) and **treadmills** ([Treadmills data](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data)). Steps are our arithmetic: Speed still needed after the previous gate, divided by the Speed per step of the treadmill paired with that biome (the n-th treadmill for the n-th gate). The pairing is ours; the game does not tie them.

| Biome | Guardian | Speed gate | x previous | Treadmill (price, Speed per step) | Steps from previous gate |
|---|---|---|---|---|---|
| Forest | Chicken | none | | | |
| Lake | Swan | 900 | | Base (free, +2) | 450 |
| Desert | Scorpion | 10K | 11.1 | Sci-Fi (15K, +5) | 1,820 |
| Jungle | Tiger | 40K | 4.0 | Flame (250K, +12) | 2,500 |
| Snow | Yeti | 170K | 4.3 | Celebrity (5M, +30) | 4,333 |
| Volcano | Cerberus | 700K | 4.1 | Golden (120M, +80) | 6,625 |
| Abyss Ocean | Moby | 2.5M | 3.6 | Freeze (3B, +100) | 18,000 |
| Prehistoric | T-Rex | 18M | 7.2 | Lucky Block (75B, +200) | 77,500 |
| Stormlands | not known | 150M | 8.3 | Hacker (2T, +500) | 264,000 |
| Cosmic | Cosmic Skeleton | 700M | 4.7 | Demonic (50T, +1K) | 550,000 |
| Cherry Blossom | Oni Tiger | 2.5B | 3.6 | Angelic (1Qa, +2K) | 900,000 |
| Titan Temple | Gorilla King | 7B | 2.8 | Astral (2.5Qa, +3K) | 1,500,000 |
| Angels & Demons | not known | 20B | 2.9 | Guardian (7.5Qa, +8.5K) | 1,529,412 |
| Enchanted Forest | Enchanted Lion | 50B | 2.5 | Alien (75Qa, +12.75K) | 2,352,941 |
| Alien Planet | not known | 250B | 5.0 | Alien | 15,686,275 |

**Our read** of this arithmetic:

- Up to the Volcano, each gate needs roughly 1.5 to 2.5 times the steps of the last. That is a ladder a player can climb.
- From the Prehistoric on, steps jump to hundreds of thousands and then millions. Treadmill steps alone cannot explain how players reach late biomes, so Speed must also come from sources the pages read do not list: rebirths, event boosts (a 2x treadmill for 10 minutes is sold for event currency) and Speed bought with Robux ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)).
- Treadmill price rises x17 to x27 per tier while Speed per step rises x1.25 to x2.7, so each point of Speed per step costs about ten times more each tier. Golden to Freeze is the worst step: x25 the price for x1.25 the Speed.

Carrying a big egg needs more than the listed gate.

**Drop rates** ([Drop Rates](https://stealanegg.fandom.com/wiki/Drop_Rates), from the game's area data): Forest Chicken 34%, Dog 24%, Bird 17%, Owl 10%, Raccoon 7%, Fox 4.5%, Bear 2.5%, Brr Brr Patapim 1%. Top pet in Lake 0.57%, Desert 1.33%, Jungle 0.12%, Snow 0.22%, Volcano 0.18%, Abyss 0.089%. From Cherry Blossom on, every biome uses 37.51 / 26.27 / 16.83 / 13.96 / 4.36 / 0.74 / 0.31 / 0.02%: the top pet is 1 in 5,000, while the two most common still make up 64%. Angels & Demons picks a variant per visit: Angels 45%, Demons 45%, both 10%.

**Pets** (150 in 10 tiers, [Bloxodes](https://bloxodes.com/wiki/steal-an-egg/pets)): Common $1 to $3/s; Uncommon $8 to $18; Rare $35 to $60; Epic $180 to $600; Legendary $1.8K to $7K; Mythic $18.5K to $42K; Cosmic $220K to $1.2M; Secret $3.5M to $8M; Eternal $65M to $5B; Divine $1B to $3B. Badges: "Hatched Secret!" held by 0.03% of players, "Hatched Eternal!" 0.01%, against 297.6M "WELCOME!" awards.

**Mutations** add together; one of each per pet. Dark Matter: income x2.5, applied to an unhatched egg with a 30% chance per 1,750-Void-Pearl item ([Bloxodes](https://bloxodes.com/articles/steal-an-egg-dark-matter-mutation)). Hatch odds, size multipliers, base lock and rebirth rules: not known.

## 4. Session and return hooks

- Eggs reset every 5 minutes.
- A Saturday event, starting at 7 to 8 AM PT: Halloween Dimension (17 Oct), New Alien Biome (7 Nov), Black Market Dealer (14 Nov), Turkey Takeover (21 Nov), Frozen Awakening (28 Nov) ([Bloxodes](https://bloxodes.com/wiki/steal-an-egg)).
- Boss clock inside the Turkey event: King Turkey rampages at :15 and :45 past every hour for 5 minutes. Hits pay Feathers, the weak spot x2, a Golden King Turkey x2 on every hit, and the top three get 500, 300 and 150 bonus Feathers ([Bloxodes](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide)).
- Feather shop: Maple Mutation 200 (10% to apply), 1.25x speed for 5 min 400, 2x treadmill for 10 min 1,200, base skin 5,500, Cornuclaw Egg 7,500, Mapleleaf Moose Egg 22,500. Our arithmetic: the Moose egg equals 45 first-place bonuses; the event ran 6 days, about 290 rampages.
- Weekends average 56.5% more players than weekdays; the daily peak is at 12:00 UTC ([RoVitals](https://rovitals.com/game/107778070777162)).

## 5. Other players

Seven per server. Players steal eggs from each other and Speed decides who escapes; guardians add a threat from the game itself ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)). Base theft rules and any lock: not known. A Jonas Brothers concert ran in the game on 31 Oct 2026. The clip: the egg lost at the base edge.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| X2 MONEY! | Pass | 299 | Doubles income |
| X2 GROWTH SPEED! | Pass | 467 | Eggs grow twice as fast |
| Speed | Product | 3 to 2,999 [data, Nov 2026] | Speed for real money ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)) |

Passes from the Roblox public API, 25 Nov 2026; the snapshot has these 2 and no others [data, Nov 2026].

**Developer products [data, Nov 2026].** 125 on sale. Without 6 gift copies and 4 "Sample Pack" items at 1 R$, 115 remain, 3 to 4,999 R$, median 249 R$. 22 sell Speed in three forms: 12 permanent multiplier tiers, 6 packs and 4 timed boosts. 12 of 115:

| Product | R$ | Kind |
|---|---|---|
| 24k Money | 49 | Money ladder, smallest of 5 |
| 8m Money | 799 | Largest |
| SPEED MULTIPLIER (Tier 1) | 3 | Speed tiers, 1 of 12 |
| SPEED MULTIPLIER (Tier 12) | 1,035 | Tier 12 |
| Speed Pack VI | 2,999 | Speed packs (I: 79) |
| Speed 5 Minutes | 90 | Timed speed |
| Speed 4 Hours | 499 | |
| Limited Egg x1 | 99 | Egg ladder: 1, 3, 10, 50 |
| Limited Egg x50 | 3,499 | |
| Steal DNA Divine | 4,999 | Top of 10 rarities (Common: 49) |
| Instant Hatch (1) | 9 | Hatch skip (10: 299) |
| Shop Reroll | 49 | Restock |

Our arithmetic: Money gives 490 per R$ in the smallest pack and 10,013 in the largest, 20 times more. All 12 multiplier tiers together cost 3,205 R$; late tiers step about 1.45x. Timed speed costs 18 R$ a minute for 5 minutes and 2.1 for 4 hours. An egg costs 99 R$ singly and 70 in fifties. Revenue is only modelled by trackers (US$1.0M to 9.4M per 30 days by RoVitals' model), not reported.

## 7. Why it works

Approval 91.3% on 4.33M votes ([Rolimons](https://www.rolimons.com/game/107778070777162)). It was live 49 days before breaking out: on Saturday 12 Sep 2026 its daily average rose by 1,639,433 (+97.6%), the largest one-day gain RoStats has recorded ([RoStats](https://rostats.io/records)).

**Our read:**

- It keeps Steal a Brainrot's payoff (units earning at a base, rare rolls, theft) and replaces the shop with a trip.
- Training gives the wait a job, and Speed doubles as the key to the map.
- The same 1-in-5,000 top roll as Steal a Brainrot, in every late biome.

## 8. What went wrong

- The treadmill's "Reels" screen played short videos, mostly AI-made content and uncredited TikToks. On 25 Aug 2026 Roblox removed from its under-16 catalogues any game that rewards watching an autoplaying feed; the game was pulled briefly and returned without Reels ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952), [DevForum](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188)). The ban came 18 days before the surge, so removing Reels did not stop the growth.
- Decline: daily readings fell about 77% from 2.18M on 4 Oct ([Endgame Tools](https://endgametools.com/en/roblox/players/steal-an-egg)); the 30-day average is down 37.6%. Now at 6% of peak, still first on Roblox.

## 9. What to take from it

- Speed gates about x4 per biome for the first five biomes after a first gate of 900 (450 free steps).
- Training gear priced x20 per tier for x2.5 Speed per step.
- Eggs that reset every 5 minutes in each biome.
- Biome odds that keep the two most common pets at about 64% and drop the top pet from 1% to 0.02%.
- A boss on a 30-minute clock that stays 5 minutes, paying an event currency with a top-three bonus.
- The trained stat sold three ways: 12 permanent tiers from 3 to 1,035 R$, 6 packs, and timed boosts from 90 R$ for 5 minutes [data, Nov 2026].

## Sources

Steal An Egg wiki: [Biomes](https://stealanegg.fandom.com/wiki/Biomes), [Eggs](https://stealanegg.fandom.com/wiki/Eggs), [Drop Rates](https://stealanegg.fandom.com/wiki/Drop_Rates), [Treadmills data](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data). [Bloxodes overview](https://bloxodes.com/wiki/steal-an-egg), [pets](https://bloxodes.com/wiki/steal-an-egg/pets), [Turkey guide](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide), [Dark Matter](https://bloxodes.com/articles/steal-an-egg-dark-matter-mutation). [RoStats](https://rostats.io/records), [Rolimons](https://www.rolimons.com/game/107778070777162), [RoVitals](https://rovitals.com/game/107778070777162), [Endgame Tools](https://endgametools.com/en/roblox/players/steal-an-egg), [Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952), [DevForum policy](https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188), [Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games). Roblox public API (games, game passes), 25 Nov 2026.
