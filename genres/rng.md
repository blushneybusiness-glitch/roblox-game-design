# RNG

> **The feeling sold:** "Every roll could be the one in a billion, and when it lands the whole server sees my name."

This page covers rolling games in the Sol's RNG mould (press roll, get an aura with a "1 in N" label, chase rarer ones) and roll-place-earn games, where the rolled unit goes on a pedestal and makes cash. Player counts marked "now" are from Roblox public API, 25 Nov 2026.

## At a glance

| | |
|---|---|
| Core verb | Roll, then keep or delete what came out. |
| Study these first | **[Sol's RNG](../teardowns/sols-rng.md)**: the reference structure, a 3.2-second roll and a ladder from 1 in 2 to 1 in 12.5 billion. **Anime Dice**: the 2026 roll-place-earn hit, 98.9% like ratio, weekly updates for 7 weeks. |
| Session that works | Anime Dice: 32.9 minutes average ([rotrends](https://www.rotrends.com/game/10708913337/Anime-Dice)). Sol's RNG: not known. |
| Players per server | Sol's RNG 20, Anime Dice 9 ([games API](https://games.roblox.com/v1/games?universeIds=10708913337,5750914919,5361032378,7094518649)). |
| Who owns the genre | One old leader. Sol's RNG (created December 2023) has 40,264 now and peaked at about 156K in April 2026, in its third year (one tracker, [rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29)). Anime Dice (August 2026) peaked at 102.6K and has 8,759 now. Most "X RNG" clones sit below 500 players; a few hold 2,000 to 9,000 (Anime Nexus RNG 8,831, RNG RollAttacks 3,791, AURA X 2,399) ([omni-search](https://apis.roblox.com/search-api/omni-search?searchQuery=Sol%27s%20RNG&sessionId=11111111-2222-3333-4444-555555555555&pageType=all)). |
| Build cost | Not known from sources. **Our read:** the cost is art. Sol's RNG lists 261 permanent rollable auras and 169 event auras, and every rare one needs its own cutscene. |
| Money comes from | A season pass (499 R$), final-luck multipliers (249 and 350), and faster rolls (100 in Sol's RNG; 799 for Double Roll in Anime Dice). |
| What kills clones | One ladder and one button, with nothing that changes between rolls. |

## Why people play it

Sol's RNG calls itself the "#1 luck-based RNG game on Roblox" and gives free private servers ([games API](https://games.roblox.com/v1/games?universeIds=5361032378)). Anime Dice's page headline is that money generates while the player is offline ([Bloxodes](https://bloxodes.com/wiki/anime-dice)). Age, device and player quotes: not known from sources.

**Our read:** the need is a lottery ticket that costs nothing but time, with a printed number on the prize. "1 in 50,000" is a flex anyone can read. The chat line that tells the server turns a private win into a public one.

## The loop, with a stopwatch

Leader: **Sol's RNG** ([wiki: Rolling](https://sol-rng.fandom.com/wiki/Rolling), [wiki: Cutscenes](https://sol-rng.fandom.com/wiki/Cutscenes), [wiki: Luck](https://sol-rng.fandom.com/wiki/Luck)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Roll | Presses roll, or Auto Roll does it (free for joining the studio's group) | 3.2 (spin plus cooldown); 1.2 with Quick Roll | The spin | Roll count |
| 2. Result | Reads it | 0 below the player's cutscene threshold; length above it not known | Aura name and "1 in N". From 1 in 1,000: black-screen cutscene and a server chat line | Rarest aura owned |
| 3. Keep or delete | Equips, stores or deletes | about 1 (our read) | Storage slots; a Storage Full warning can be switched on ([wiki: Settings](https://sol-rng.fandom.com/wiki/Settings)) | Storage used |
| 4. Bonus roll | Nothing | every 10th roll: 32 s, or 12 s with Quick Roll (our arithmetic) | Bonus marker | Luck x2 on that roll |
| 5. Craft | Turns auras and potions into gear | not known | Jake's Workshop, Stella's Cauldron | Basic luck: Luck Glove +25% |

Cycle time is the roll: 1,125 rolls an hour at 3.2 s, 3,000 at 1.2 s (our arithmetic). There is no dead time to fill, because Auto Roll keeps rolling while the player walks, crafts or does the obby.

**Anime Dice differs** in what the roll is for. A rolled anime unit goes on a pedestal and earns cash, cash buys dice with higher luck, and luck rolls rarer units ([Bloxodes](https://bloxodes.com/wiki/anime-dice)). The roll feeds an income loop instead of a collection alone.

The loop stack in Sol's RNG:

| Every | What finishes | Source |
|---|---|---|
| 3.2 s | A roll | [Rolling](https://sol-rng.fandom.com/wiki/Rolling) |
| 32 s | A bonus roll at 2x luck | [Luck](https://sol-rng.fandom.com/wiki/Luck) |
| 60 s | A Lucky Potion (+25%) runs out | [Lucky Potion](https://sol-rng.fandom.com/wiki/Lucky_Potion) |
| 2.5 min | Day and night swap | [rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide) |
| 5 min | A Fortune Potion runs out | [Fortune Potions](https://sol-rng.fandom.com/wiki/Fortune_Potions) |
| 8 to 12 min | A common biome starts and lasts 2 min (our arithmetic below) | [Biomes](https://sol-rng.fandom.com/wiki/Biomes) |
| 1 to 2.5 h | A rare biome (Sandstorm to Corruption) | [Bloxodes biomes](https://bloxodes.com/wiki/sols-rng/biomes) |
| A day | Daily quests; VIP gets 3 rerolls | [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5361032378/game-passes?passView=Full&pageSize=50) |
| A season | A new season pass (Season IX now; eight earlier ones listed, off sale) | same |

## The first five minutes

Sol's RNG's tutorial, in order ([wiki: Tutorial](https://sol-rng.fandom.com/wiki/Tutorial)). Times are our arithmetic at 3.2 s a roll with no luck.

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | First roll done and equipped | Tutorial step 1 |
| 0:30 | 10 rolls done; reward: Tutorial Potion and 400 coins | Tutorial daily quest; 10 x 3.2 s = 32 s |
| 1:00 | "A Road to Gears" accepted (1,000 coins); Gear Basing needs one Common, Uncommon, Good and Rare | Rare is 1 in 16, so about 16 to 30 rolls |
| 3:00 | Roll 60 done | 60 x 3.2 s = 3.2 min |
| 5:00 | Luck Glove crafted: 2 Divinus (1 in 32), 1 Crystallized (1 in 64), 3 Rare (1 in 16) | About 64 to 100 rolls, 3.5 to 5.5 min |

The next batch asks for one roll rarer than 1 in 1,000. That is the first long goal: about 48 minutes at base speed, 18 with Quick Roll (our arithmetic, including the bonus roll). The tutorial can be skipped.

Gates for a new RNG game:

- First roll within 5 seconds of spawning, with no menu in between.
- First reward (coins and a potion) within 40 seconds.
- First craft within 2 minutes, from auras the player already rolled.
- First luck item equipped by 5:00.
- First long goal stated by 5:00, reachable in 30 to 60 minutes.

## Numbers that work

**The odds ladder** ([rblxguide aura tiers](https://rblxguide.com/games/sols-rng/updates/auras-list-by-rarity)):

| Tier | 1 in N | Auras |
|---|---|---|
| Basic | 1 to 999 | 20 |
| Epic | 1,000 to 9,999 | 27 |
| Unique | 10,000 to 99,998 | 25 |
| Legendary | 99,999 to 999,998 | 23 |
| Mythic | 999,999 to 9,999,999 | 58 |
| Exalted | 10,000,000 to 99,999,998 | 48 |
| Glorious | 99,999,999 to 999,999,998 | 54 |
| Transcendent | 999,999,999 to 7,500,000,000 | 6, plus 2 crafted |
| Dimensional | 7,500,000,001 to 12,500,000,000 | 1, crafted only |
| Event | limited time | 169 |

Each tier is one factor of ten. The first auras sit at 1 in 2, 4, 5, 8, 16, 32 and 64 ([rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide)). An aura that only exists in one biome is placed two tiers above its raw odds.

**Time to a tier.** Our arithmetic: rolls = N divided by average luck; bonus roll lifts average luck to 1.1. "Stack" is Luck Glove (+25%) plus Fortune III (+100%) plus VIP (x1.2), average luck 2.97 by the [wiki's formula](https://sol-rng.fandom.com/wiki/Luck), with Quick Roll.

| Target | Base, 3.2 s | Quick Roll, 1.2 s | Stack plus Quick Roll |
|---|---|---|---|
| 1 in 1,000 | 48 min | 18 min | 7 min |
| 1 in 10,000 | 8 h | 3 h | 67 min |
| 1 in 1,000,000 | 808 h | 303 h | 112 h |
| 1 in 100,000,000 | 80,800 h | 30,300 h | 11,200 h |

The bottom rows are why one-roll potions exist. Heavenly Potion adds +150,000 luck to one roll, which turns 1 in 100 million into about 1 in 560 for that roll (our arithmetic). It costs 250 Lucky Potions plus four auras.

**Announcements by rarity** ([wiki: Cutscenes](https://sol-rng.fandom.com/wiki/Cutscenes)):

| From | What happens |
|---|---|
| 1 in 1,000 (Epic) | Black-screen cutscene, server chat line: "[user] HAS FOUND [aura], CHANCE OF 1 IN ..." |
| 1 in 10,000 (Unique) | Adds a drop beat, a coloured star, yellow lines flashing around the map |
| 1 in 100,000,000 (Glorious) | Every player in the server goes monochrome, thunder, a giant beam, and a "[GLOBAL]" chat line |

Whether "[GLOBAL]" reaches other servers is not stated. Cutscene length in seconds is not known. Players set their own cutscene threshold; one guide suggests skipping animations below 1 in 1,000 ([rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide)).

**Biomes: timed world states** ([Bloxodes biomes](https://bloxodes.com/wiki/sols-rng/biomes); the first three confirmed on the [wiki](https://sol-rng.fandom.com/wiki/Biomes)). Mean wait is our arithmetic, 1 divided by the per-second chance, assuming the check runs every second.

| Biome | Chance per second | Mean wait | Lasts |
|---|---|---|---|
| Windy | 1 in 500 | 8 min | 2 min |
| Snowy | 1 in 600 | 10 min | 2 min |
| Rainy | 1 in 750 | 12.5 min | 2 min |
| Sandstorm | 1 in 3,000 | 50 min | 650 s |
| Hell | 1 in 6,666 | 1.9 h | 666 s |
| Starfall | 1 in 7,500 | 2.1 h | 10 min |
| Corruption | 1 in 9,000 | 2.5 h | 650 s |
| Glitched | 1 in 30,000 | 8.3 h | 2 min |
| Dreamspace | 1 in 3,500,000 | 40 days | 192 s |

Older guides give other values for Snowy, Null and Starfall. Chat announces every biome except Normal and Glitched. A biome's own auras roll at far better odds inside it, and 3x worse outside it (Wind: 1 in 300 inside, 1 in 900 outside).

**Crafting as the sink.** Lucky Potion: +25% for 60 s, 1,000 coins. Fortune I, II, III: +50%, +75%, +100% for 300 s, brewed from 10, 25 and 50 Lucky Potions ([wiki](https://sol-rng.fandom.com/wiki/Fortune_Potions)). In "luck-percent minutes" (our arithmetic):

| Potion | Input, as Lucky Potions | Luck-minutes in | Luck-minutes out |
|---|---|---|---|
| Fortune I | 10 | 250 | 250 |
| Fortune II | 25 | 625 | 375 |
| Fortune III | 50 | 1,250 | 500 |

**Our read:** Fortune I is a fair swap. Fortune III destroys 60% of the input to buy a higher peak. That is the sink: duplicates and coins disappear, and the player gets a short, strong window to roll in.

**Anime Dice's dice ladder** ([AllThings.How](https://allthings.how/anime-dice-best-dice-upgrade-priority-and-rebirth-tips/)); ratios are our arithmetic:

| Dice | Luck | Cost | Cost ratio | Luck ratio |
|---|---|---|---|---|
| Nature | 20x | start | | |
| Lightning | 42x | $500K | | 2.1x |
| Ice | 100x | $4M | 8x | 2.4x |
| Magma | 200x | $30M | 7.5x | 2x |
| Storm | 400x | $200M | 6.7x | 2x |
| Shadow | 750x | $1.5B | 7.5x | 1.9x |
| Light | 1,500x | $12B | 8x | 2x |
| Blood Moon | 3,000x | $100B | 8.3x | 2x |
| Void | 5,000x | $1.5T | 15x | 1.7x |

Each doubling of luck costs about 7.5 times as much. Grade income multipliers run D 1.1x, C 1.2x, B 1.6x, A 3x, A+ 4.5x, S 7x, S+ 10x, Z 15x, Z+ 25x. Unit odds run from 1 in 15 to 1 in 200 ([AllThings.How](https://allthings.how/anime-dice-full-guide-for-roblox-update-4/)). Rebirth thresholds conflict between two guides ($500K, $5M, $500M in one; $500M in the other), each adding +0.5x.

**Start with:** (our read, derived from the tables above)

| Value | Start with | Why |
|---|---|---|
| Roll time | 3 s free, 1.2 s with a 100 R$ pass | Sol's numbers; the pass gives 2.7x more rolls an hour |
| Ladder | 1 in 2 to about 1 in 10 billion, 9 tiers, one factor of ten each | Sol's tiers |
| Bonus roll | Every 10th roll, x2 luck | Something finishes every 30 s |
| Cutscene | From 1 in 1,000, threshold settable by the player | Sol's Epic tier |
| Server effect | Map flash from 1 in 10,000; whole-server screen effect and global line from 1 in 100 million | Sol's Unique and Glorious |
| Common biomes | 3, at 1 in 500 to 750 per second, 2 min each | One starts every 8 to 12 min |
| Rare biomes | 4 or 5, at 1 in 3,000 to 9,000 per second, 4 to 11 min each | One every 1 to 2.5 h |
| Potion tiers | Cost 10, 25, 50 of the tier below; +50%, +75%, +100% for 5 min | Sol's Fortune line, a built-in sink |
| First long goal | A 1 in 1,000 roll, reachable in 30 to 60 min | Sol's tutorial batch 2 |
| Event content | At least as many event items as permanent ones over a year | Sol's: 169 event auras against 261 permanent |

## What brings them back

**Later in the same session.** A bonus roll every 32 seconds, a common biome every 8 to 12 minutes, potions that run out after 1 or 5 minutes, and a craft recipe that is always a few auras short. **Our read:** these are four clocks of different lengths, so at any moment one of them is close to finishing. That is why a game with one button holds players: the button stays the same while the world around it changes.

**Tomorrow.** A daily 10-roll quest pays 400 coins and a potion ([rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide)). VIP adds 3 daily quest rerolls. Anime Dice earns cash while the player is away; the cap is not known.

**Next week and after.** Sol's RNG ships named beats: a Valentine's update on 14 February 2026 with 10 auras, Boss Raid Chapter 2 on 28 February with 10 auras and a boss, and Season Pass 5 to 3 April 2026 ([rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29)). The tier ladder spans 10 factors of ten, so a rarer aura always exists. Anime Dice ran a Saturday-to-Tuesday event window every week from 27 September to 11 November 2026 ([Bloxodes](https://bloxodes.com/wiki/anime-dice)).

## Other players

**Server size.** 20 in Sol's RNG, 9 in Anime Dice.

**What a player sees of others.** Every roll from 1 in 1,000 up, as a chat line with the player's name. From 1 in 10,000, flashing lines around the map. From 1 in 100 million, the whole server's screen. Biome starts are announced to everyone, so the server reacts to the same event at once.

**What they can do to or with each other.** Not known from sources: no trading or combat between players is documented in either game. Free private servers exist in Sol's RNG.

**What can be lost.** Auras deleted from full storage. Sol's RNG has delete-warning thresholds set by rarity.

**What gets clipped.** **Our read:** the Glorious moment: the screen goes grey for 20 players, thunder, a beam, and a chat line with a 1 in 100 million number.

## Money

| Game | Item | R$ | What it does |
|---|---|---|---|
| Sol's RNG | RNG Premium Pass Season IX | 499 | Season pass |
| Sol's RNG | VIP+ | 350 | x1.2 final luck (x1.3 with VIP), auto item collection |
| Sol's RNG | VIP | 249 | x1.2 final luck and quest rewards, 3 daily rerolls |
| Sol's RNG | Quick Roll | 100 | Roll in about 1.2 s; free 20-minute trial |
| Sol's RNG | Starter Pack | 49 | Title, gear, potions, 15,000 coins |
| Anime Dice | Double Roll | 799 | |
| Anime Dice | Ultra Luck / Roll Speed / More Traits | 499 / 349 / 329 | |
| Anime Dice | More Grades / VIP / More Cash / Luck | 299 / 249 / 199 / 199 | 8 passes, 2,922 in all, plus 9 developer products |

Sources: [Sol's RNG game-passes API](https://apis.roblox.com/game-passes/v1/universes/5361032378/game-passes?passView=Full&pageSize=50), [Anime Dice game-passes API](https://apis.roblox.com/game-passes/v1/universes/10708913337/game-passes?passView=Full&pageSize=50), 25 Nov 2026. The Sol's RNG wiki records a Black Friday price of 175, 245 and 70 for VIP, VIP+ and Quick Roll, 30% off ([wiki](https://sol-rng.fandom.com/wiki/Gamepasses)).

In both games the cheapest pass removes friction (Quick Roll 100) and the dearer ones multiply luck or rolls. Where offers appear in the flow: not known from sources.

**The line.** A luck pass changes the odds of every roll after it. That makes the roll a paid random item under Roblox's rules: show exact odds, show live odds while a boost is active, and never show odds that differ from the server's. See [foundations/15-the-line.md](../foundations/15-the-line.md) and [foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md).

## Live ops

Sol's RNG works in seasons (nine passes so far) and eras (Era 9 in mid-September 2024 added about 10 to 12 auras), with holiday updates and boss raids between them ([rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29), [game-passes API](https://apis.roblox.com/game-passes/v1/universes/5361032378/game-passes?passView=Full&pageSize=50)). An update holds about 10 auras, a boss, or a season pass. It was updated on 24 November 2026.

Anime Dice shipped an event window every Saturday at noon Pacific time for 7 weeks, with codes for each update (UPDATE4: 2 Lucky Spins, 10 Trait Rerolls, 10 Tickets, 3 Gems) ([AllThings.How](https://allthings.how/anime-dice-full-guide-for-roblox-update-4/)). Weekly windows did not stop a fall from 102.6K to 8,759, about 91% (our arithmetic).

**Our read:** a small team can sustain 10 auras every 2 weeks if each aura is a recolour plus one particle effect, and save full cutscenes for the top 2 tiers. See [foundations/13-live-ops.md](../foundations/13-live-ops.md).

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Stuck below 500 CCU from launch | A copy of the ladder with nothing else: the fate of most "X RNG" games in search | Add the clocks: bonus roll, biomes, potions, crafting |
| Launch spike falls about 90% in three months while likes stay near 99% | Anime Dice: 102.6K to 8,759 at 98.9% like. Cause not documented | **Our read:** build a second layer (biomes, boss raids, a season) before week 3 |
| Players skip the result screen and stop reading it | Cutscenes on every roll stretch the 3.2 s cycle | A player-set cutscene threshold, as Sol's RNG has |
| Rolling stops when storage fills | A full inventory blocks the core verb | Storage Full warning and delete thresholds by rarity |
| Top tier reached in the first week | Ladder too short | 9 to 10 factors of ten; one-roll potions to reach the top on purpose |
| Guides and players disagree on what an item does | Values changed between eras without notice (Sol's potion values differ by source and era) | Print the number on the item in game |

## Checklist

1. First roll within 5 seconds of spawning.
2. A roll takes 2 to 4 seconds free, and a pass cuts it to about 1.2 seconds.
3. The ladder spans at least 9 factors of ten.
4. Every result shows its "1 in N" number on screen.
5. A cutscene plays from about 1 in 1,000, and the player can raise the threshold.
6. The server sees a chat line from 1 in 1,000 and a map effect from 1 in 10,000.
7. A bonus roll or similar fires every 20 to 40 seconds.
8. At least 3 biomes start every 8 to 12 minutes on average, each lasting about 2 minutes.
9. At least one craft recipe uses the 5 most common auras.
10. Potion tiers cost more input than they return, so crafting removes items.
11. The first long goal is reachable in 30 to 60 minutes.
12. Storage warns before it is full.
13. Any luck pass shows live odds while active.
14. A season or event adds new items at least every 4 weeks.

## Twists and open space

Variations that already worked:

- **Roll, place, earn.** Anime Dice adds pedestals and offline income to the roll; launched 15 August 2026, it peaked at 102.6K (date not known).
- **Boss raids** inside an RNG game: Sol's RNG's Boss Raid Chapter 2 drove a spike in February 2026.

**Our read**, angles that look under-served:

- Roll-place-earn with Sol's RNG's biome clock, so the pedestal game has world events.
- An RNG game where duplicates fuse into one stronger copy, so every roll after day one still matters.
- A co-op roll: the whole server's rolls fill one shared meter that opens a biome.

## Sources

Related: [teardowns/sols-rng.md](../teardowns/sols-rng.md), [foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md), [foundations/08-retention.md](../foundations/08-retention.md), [foundations/15-the-line.md](../foundations/15-the-line.md).

Main external sources: the [Sol's RNG wiki](https://sol-rng.fandom.com/wiki/Luck) (Rolling, Luck, Cutscenes, Biomes, Tutorial, potion pages); [Bloxodes biomes](https://bloxodes.com/wiki/sols-rng/biomes); [rblxguide](https://rblxguide.com/games/sols-rng/updates/beginners-guide); [Bloxodes: Anime Dice](https://bloxodes.com/wiki/anime-dice); [AllThings.How on Anime Dice](https://allthings.how/anime-dice-best-dice-upgrade-priority-and-rebirth-tips/); Roblox games and game-pass APIs (25 Nov 2026); trackers [rowatcher](https://rowatcher.com/games/5361032378/sol-s-rng-eon-1-29) and [rotrends](https://www.rotrends.com/game/10708913337/Anime-Dice).
