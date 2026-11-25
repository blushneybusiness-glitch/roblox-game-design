# Progression and economy

Open this page when you set prices, income, upgrade costs or a rebirth, or when players stall at one purchase and leave. It gives the formulas behind buy-and-earn games, the ladders that real Roblox games ship, the three rebirth types, and a way to test your own numbers with [tools/pacing.py](../tools/pacing.py) before a single player sees them.

## What is known

### Payback is the number to watch

Payback is price divided by income per second. In [Steal a Brainrot](../teardowns/steal-a-brainrot.md) the $25 entry unit earns $1/s, a 25 s payback, the shortest in the game ([SAB wiki, Noobini](https://stealabrainrot.fandom.com/wiki/Noobini_Pizzanini)). Early units pay back in 83 to 175 s, mid units in 200 to 300 s, and the top Secret unit ($250B, $250M/s) in 1,000 s. Price spans a factor of about 10 billion while payback spans about 12 ([slop/01-anatomy.md](../slop/01-anatomy.md); [AllThings.How value table](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/)).

**Our read:** price grows a little faster than income, so the price on screen rises by millions while the wait rises by seconds.

### The idle formulas

From Pecorella's idle-maths series ([Game Developer, Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i)):

- Cost of the next copy: `cost = b × r^owned`
- Cost of n more when you own k: `b × r^k × (r^n − 1) / (r − 1)`
- Most you can afford with cash c: `floor(log(c(r − 1) / (b × r^k) + 1) / log r)`
- AdVenture Capitalist's first generator: b = 4, r = 1.07, x2 income at 25 owned and again at 50.

Time to next purchase (TTNP) is cost divided by income. With linear income, TTNP grows by about r per purchase. So TTNP doubles every ln2 / ln r purchases: about 10 at r = 1.07, about 5 at r = 1.15. A milestone multiplier of m buys back log m / log r purchases ([design maths notes, Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i)).

Worked table, one generator line, b = 4, 1.67/s per copy (our arithmetic from the formulas):

| Copies owned | Next cost, r = 1.07 | TTNP, r = 1.07 with x2 at 25 and 50 | Next cost, r = 1.15 | TTNP, r = 1.15, no milestones |
|---|---|---|---|---|
| 10 | 7.87 | 0.5 s | 16.2 | 1.0 s |
| 25 | 21.7 | 0.26 s | 131.7 | 3.2 s |
| 50 | 117.8 | 0.35 s | 4,335 | 52 s |
| 100 | 3,471 | 5.2 s | 4.70M | 7.8 h |
| 150 | | 102 s | | wall |

**Our read:** r decides how many purchases fit before a wall. At 1.15 with no milestones, copy 100 takes 7.8 hours. Exponential cost always beats linear income in the end, so a wall is certain unless a multiplier arrives ([Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i)).

### What is folklore

| Claim | Status |
|---|---|
| "Growth rates of 1.07 to 1.15 are standard" | No source found. AdCap uses 1.07; one designer's example uses 1.15 with income x1.1 per level ([Eric Guan](https://ericguan.substack.com/p/idle-game-design-principles)). Treat the range as folklore. |
| A published TTNP target from a studio | Not known. None was found. |
| "Rainbow = 10x better" (PS99 tooltip) | False. A rainbow pet is about +27% over normal and costs 100 normal pets ([PS99 wiki, Rainbow Machine](https://pet-simulator.fandom.com/wiki/Rainbow_Machine_(Pet_Simulator_99))). |

### Level curves

| Game | XP for the next level | Growth |
|---|---|---|
| [Tower Defense Simulator](../teardowns/tower-defense-simulator.md) tower EXP | 50 at level 1, x1.09 per level | 2,549 to level 20 ([wiki](https://tds.fandom.com/wiki/Scout)) |
| [Pet Simulator 99](../teardowns/pet-simulator-99.md) Huge pets | x2^(1/7) per level | doubles every 7 levels ([wiki](https://pet-simulator.fandom.com/wiki/Huge_Pets_(Pet_Simulator_99))) |
| [Blox Fruits](../teardowns/blox-fruits.md) | 2 × L^2.3 + 84 | one community source, not cross-checked ([rblxguide](https://rblxguide.com/games/blox-fruits/updates/blox-fruits-leveling-guide)) |
| Phantom Forces | 1,000 × rank | no cap ([wiki](https://roblox-phantom-forces.fandom.com/wiki/Ranks)) |

### Real ladders side by side

| Game, ladder | Range | Step ratio | Source |
|---|---|---|---|
| PS99 areas (one currency) | 900 to 750K units | 2.0x to 3.2x, then a new currency with a 500K bridge payment | [PS99 wiki, areas](https://pet-simulator.fandom.com/wiki/Template:PS99SpawnWorldAreaList) |
| PS99 eggs 1 to 10 | 90 to 45,000 | about 2.0x (1.5x to 2.7x) | [PS99 wiki, eggs](https://pet-simulator.fandom.com/wiki/Template:PS99World1EggsList) |
| Bubble Gum Simulator INFINITY eggs | 10 to 1.5M | about 3.3x, with two 11x jumps | [BGSI wiki](https://bgs-infinity.fandom.com/wiki/Module:Egg_Data) |
| [Bee Swarm Simulator](../teardowns/bee-swarm-simulator.md) hive slots | 3M to 2.17T honey (3.42T for all 25) | 2.6x falling to 1.35x, then rising to 2.8x | [Bee Swarm wiki](https://bee-swarm-simulator.fandom.com/wiki/Hive_Slot) |
| [Fisch](../teardowns/fisch.md) Moosewood rods | C$300 to C$4,500 | 2.5x, 2.7x, 2x, 2x | [Fischipedia](https://fischipedia.org/wiki/Moosewood) |
| Fish It rods | $250 to $12M | about 2x to 5x; top rods from quests | [Bloxodes](https://bloxodes.com/wiki/fish-it/rods) |
| Anime Dice dice | $500K to $1.5T | 6x to 8x | [AllThings.How](https://allthings.how/anime-dice-best-dice-upgrade-priority-and-rebirth-tips/) |
| Military Tycoon workers | free to 25,000; 150,135 for all | 10x, 3.6x, 1.6x, then 1.0x to 1.4x | [wiki](https://military-tycoon.fandom.com/wiki/Worker) |
| Lumber Tycoon 2 land | $100, then +$3,000 per plot; $900,100 for 25 | 30x falling to 1.04x | [wiki](https://lumber-tycoon-2.fandom.com/wiki/Land_Store) |
| [Steal an Egg](../teardowns/steal-an-egg.md) speed gates | 900 to 250B speed | about 3x to 10x | [SAE wiki](https://stealanegg.fandom.com/wiki/Biomes) |

**Our read:** the common shape is 2x to 3.5x per step, with a 10x jump at a zone or currency change. Tycoons open with a 10x step, then flatten to 1.2x to 2x. A tycoon's income per second and minutes to finish a base: not known.

### Walls, and what gets players over them

| Wall breaker | Example |
|---|---|
| Milestone multiplier | AdCap x2 at 25 and 50 copies; Clicker Heroes x4 per 25 copies ([Quest for Progress, GDC Europe 2016](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507)) |
| A new currency | PS99 rolls into Gold Bars after about 750K coins, so prices restart at 1 ([PS99 wiki](https://pet-simulator.fandom.com/wiki/Template:PS99SpawnWorldAreaList)) |
| A collection count | Bee Swarm fields open at 0, 5, 10, 15, 20, 25 and 35 bees ([ofzenandcomputing](https://www.ofzenandcomputing.com/bee-swarm-simulator-fields-guide/)); Muscle Legends gyms at 1, 5, 15, 30, 60 and 150 rebirths ([wiki](https://muscle-legends.fandom.com/wiki/Gyms|Rebirths|How_Rebirthing_Works)) |

Bee Swarm's slot ladder is a wall by design: all Black Bear quests pay 2.35B honey, which buys slots 1 to 13 and stops short of slot 14 at 2.54B. That is 0.07% of the 3.42T full cost ([Bee Swarm wiki](https://bee-swarm-simulator.fandom.com/wiki/Black_Bear)).

A wall that kills: Ride A Pet's "R3 Unicorn $2.5B" is cited as the hard wall, and each rebirth wipes cash and hatch luck ([AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/)). Its rebirth cash rises 50x per step, but the odds of the required pet rise from 1 in 500K to 1 in 5Qi. The game reportedly peaked near 1M concurrent in October 2026 (unverified) and had 1,646 on 25 Nov 2026 (Roblox public API, 25 Nov 2026). **Our read:** the wall sat on luck, which no amount of play could buy, and the rebirth took the luck away.

### Prestige formulas

| Game | Prestige formula | Earnings needed to double prestige |
|---|---|---|
| AdVenture Capitalist | `150 × sqrt(lifetime / 1e15)` | about 3x to 4x |
| Cookie Clicker | `cbrt(lifetime / 1e12)` | about 8x |
| Realm Grinder | `(sqrt(1 + 8 × max / 1e12) − 1) / 2` | about 4x |
| Egg, Inc. | `(run / 1e6)^0.14` per run | about 128x |

Source: [Game Developer, Part III](https://gamedeveloper.com/design/the-math-of-idle-games-part-iii). The timing rule: reset when it would add +50% to +200% of the prestige you hold ([Quest for Progress](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507)).

### Roblox rebirth types

| Type | Game | Numbers |
|---|---|---|
| Linear multiplier, steep cost | Steal a Brainrot | 19 rebirths; cash x3 to x10 per step ($500K to $30Qa); multiplier rises by about 1 per step; +1 slot, +10 s base lock and new gear each time ([Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/rebirths)) |
| | Ride A Pet | cash 1M, 50M, 2.5B, 125B, 6.2T (50x each); +1x money and +1 pet slot each ([AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/)) |
| | Plants vs Brainrots | $1M, $50M, $100M, $150M, $300M; +50% luck and money each; wiki may date from August 2025 ([wiki](https://plantsvsbrainrots.fandom.com/wiki/Mechanics)) |
| Small step with a cap | Arm Wrestle Simulator | +15% strength each, maximum 150, then up to 100 Super Rebirths ([wiki](https://arm-wrestle-simulator.fandom.com/wiki/Worlds|Rebirths)) |
| | Muscle Legends | +5% each; costs 10,000 + 5,000 × rebirths strength ([wiki](https://muscle-legends.fandom.com/wiki/Gyms|Rebirths|How_Rebirthing_Works)) |
| | Military Tycoon | +0.1x each, capped at x5 at 40 rebirths; resets the whole base ([wiki](https://military-tycoon.fandom.com/wiki/Rebirths)) |
| No longer resets | Pet Simulator 99 | 9 rebirths since Update 79; areas and coins are kept; +75% pet strength and a feature list each ([PS99 wiki](https://pet-simulator.fandom.com/wiki/Rebirth_(Pet_Simulator_99))) |

Our arithmetic on Steal a Brainrot: x1 to x2 (R2 to R3) costs 8.3x the cash, x2 to x4 (R5) costs 8x, Cookie Clicker's cube-root rate, and x4 to x9 (R10) costs 1,250x.

**Our read:** a +5% to +15% rebirth only works if it takes seconds; Arm Wrestle sells Auto Rebirth for 5 R$ ([passes API](https://apis.roblox.com/game-passes/v1/universes/4582358979/game-passes?passView=Full&pageSize=100)). A steep rebirth needs something on screen each time.

### Sources and sinks

Daniel Cook's typing ([Lost Garden, Value chains](https://lostgarden.com/2021/12/12/value-chains/)): sources are capped, trickle, grind, investment or random; sinks are fixed, repeatable, exponential or competitive. A trickle source pairs with a repeatable sink. A grind or investment source needs an exponential or competitive sink. Cap any exponential source. Keep sinks slightly larger than sources. His example: 10 gold a day with no sink becomes 7,300 gold in 2 years.

Free sources in Roblox games, per hour:

| Game | Faucet |
|---|---|
| [Anime Vanguards](../teardowns/anime-vanguards.md) Time Chamber | 300 gems/h (600 with VIP), so a 50-gem pull every 10 minutes ([wiki](https://animevanguards.fandom.com/wiki/Time_Chamber)) |
| Toilet Tower Defense AFK | 60 coins/h, 1,440 a day ([wiki](https://toilet-tower-defense.fandom.com/wiki/Gamepasses)) |
| PS99 map pads | about 356 to 1,173 diamonds/h, cooldowns 30 min to 5 h (our arithmetic from the [drop tables](https://pet-simulator.fandom.com/wiki/Free_Items_(Pet_Simulator_99))) |
| [Rivals](../teardowns/rivals.md) | 6 Keys a day from dailies ([wiki](https://robloxrivals.fandom.com/wiki/Tasks)); pass capped at 7 tiers a week ([wiki](https://robloxrivals.fandom.com/wiki/Season_Pass)) |

Sinks that eat duplicates: PS99 turns 10 pets into 1 golden (+13%) and 100 into 1 rainbow (+27%) ([wiki](https://pet-simulator.fandom.com/wiki/Golden_Machine_(Pet_Simulator_99))). [Sol's RNG](../teardowns/sols-rng.md) brews Fortune Potions from 10, 25 or 50 Lucky Potions ([wiki](https://sol-rng.fandom.com/wiki/Fortune_Potions)). [Grow a Garden](../teardowns/grow-a-garden.md) charges 1B for a manual shop restock and triples it each time ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden/shops)).

### Stacking multipliers

| Game | Rule |
|---|---|
| Sol's RNG | Luck = ((1 + basic) × bonus roll + special) × VIP. Example: +125% basic gives 2.25, the x2 tenth roll gives 4.5, VIP x1.2 gives 5.4 ([wiki](https://sol-rng.fandom.com/wiki/Luck); our arithmetic) |
| PS99 enchants | copies 1 to 4 give 100%, 60%, 38.3%, 27.5% ([wiki](https://pet-simulator.fandom.com/wiki/Enchants_(Pet_Simulator_99))) |
| Fish It luck passes | add: +30%, +80%, +150% = +260% for 840 R$ ([passes API](https://apis.roblox.com/game-passes/v1/universes/6701277882/game-passes?passView=Full&pageSize=50)) |
| Grow a Garden mutations | variant × (1 + sum of multipliers − count) ([Bloxodes](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator)) |

**Our read:** Sol's and Grow a Garden both add first, then multiply once.

### Readable numbers and offline income

PS99 keeps prices short by moving to a new currency about every 17 areas; Ride A Pet uses suffixes up to Qi (sources above).

| Game | Offline rule |
|---|---|
| Steal a Brainrot | The wiki contradicts itself: one page says about 50%, the dedicated page says about 3% capped at 5 h. The 3% / 5 h figure is more specific and unconfirmed ([wiki](https://stealabrainrot.fandom.com/wiki/Offline_Cash)) |
| Garden Tower Defense Zen Garden | 10% while offline ([wiki](https://garden-tower-defense.fandom.com/wiki/Gamepasses)) |
| Grow a Garden, Anime Dice, Restaurant Tycoon 3 | offline income exists; rate and cap not known |
| Egg, Inc. | 2 h cap, called "likely a mistake" by an analyst who churned ([Quest for Progress](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507)) |

## The rules

1. **Hold payback between 25 s and 300 s for the first ladder.** Steal a Brainrot's belt units run 25 s to about 300 s; only the top Secret reaches 1,000 s. Beyond 300 s the next purchase is more than five minutes away at full income.
2. **Track TTNP, not price.** Price can grow by a factor of a billion if TTNP stays flat. Our read: keep TTNP under 60 s in the first 15 minutes, a band we infer, not a published target.
3. **Use a step of 2x to 3.5x between tiers.** PS99 eggs step 2.0x, BGSI eggs 3.3x, Moosewood rods 2x to 2.7x. Save 10x jumps for a zone or currency change, where the player also sees a new place.
4. **Place a multiplier where TTNP would leave the band.** At r = 1.07, a x2 every 10 purchases holds TTNP flat; AdCap puts x2 at 25 and 50.
5. **Make every reset buy something visible.** Steal a Brainrot pays +1 slot, +10 s lock and a tool per rebirth; PS99 pays a feature list. A reset that only multiplies a number needs to take seconds, as in Arm Wrestle at +15% for 150 rebirths.
6. **Never make luck the only way past a wall, and never reset luck.** Ride A Pet's required-pet odds reach 1 in 5Qi and rebirth wipes Hatch Luck.
7. **Give every source a sink of equal or greater size.** Cook's rule; Bee Swarm's quests pay 0.07% of its slot sink, so honey never piles up.
8. **Add buffs inside a group, multiply across groups.** Sol's adds basic luck before the x2 bonus roll; PS99 cuts the fourth copy of an enchant to 27.5%.

## How to do it

1. Fill [kit/templates/economy-sheet.md](../kit/templates/economy-sheet.md): every unit with price and income, every gate, every rebirth, every source and its sink.
2. Write the units into a JSON file in the shape of [tools/examples/start-with-ladder.json](../tools/examples/start-with-ladder.json). Add `every_s` to units that only appear on a restock clock, and a `gates` entry for each rebirth.
3. Run `python tools/pacing.py my-game.json`. The tool plays the ladder as a player who never idles and always buys the best value, so every time it prints is a lower bound.
4. Read three things:
   - **First purchase.** Under 15 s.
   - **Longest wait in the first 15 minutes.** Under 90 s.
   - **When the ladder runs out.** Not before 3 hours. Also read the longest wait from minute 15 to 60.
5. Fix the longest wait first (cheaper tier, extra unit, or a multiplier) and run again.

What the two bundled examples show (our run of the tool):

| Example | First purchase | Longest wait, 0 to 15 min | Rebirth 1 | Longest wait, 15 to 60 min |
|---|---|---|---|---|
| Start-with ladder (14 units, restock clocks) | 0:08 | 0:25 | 20:41 | 14:51 after the God tier is bought |
| Steal a Brainrot, observed prices | 0:08 | 1:13 | 19:45 | 9:58 |

Our separate check: the 12-unit ladder in [slop/04-build-it.md](../slop/04-build-it.md), played with every unit always in stock, 10 slots and no rebirth, fills all slots with the top unit at about 37 minutes. Restock clocks, extra tiers and the rebirth are what carry it past 3 hours.

**Start with:**

| Lever | Value | Where it comes from |
|---|---|---|
| First unit | price 25, income 1/s | Steal a Brainrot entry unit |
| Payback, top of first ladder | 200 to 300 s | Steal a Brainrot mid tiers |
| Price step between tiers | 2.5x to 3x | middle of the 2x to 3.5x real range |
| Per-copy growth, if copies stack | r = 1.07, x2 at 25 and 50 copies, then every 10 | AdCap; TTNP doubles about every 10 purchases at 1.07 |
| First rebirth | 20 to 40 min of play | [slop/04-build-it.md](../slop/04-build-it.md); both examples land near 20 min |
| Rebirth cost and reward | cash x3 to x8 per step, +1x income, +1 slot | Steal a Brainrot; x8 matches the cube-root rate |
| Offline income | 25% to 50% of the online rate, counted for up to 8 hours away, so a night pays 2 to 4 hours of earnings, as in [slop/04-build-it.md](../slop/04-build-it.md) and [08-retention.md](08-retention.md). Where late-game income is very large, 10% | GTD's 10%; our read that a 2 h cap fails the Egg, Inc. test |

## Checks

- [ ] First purchase happens within 15 s of control (pacing.py).
- [ ] No wait over 90 s in the first 15 minutes.
- [ ] No wait over 5 minutes from minute 15 to 60.
- [ ] The ladder is not exhausted before 3 hours.
- [ ] No unit pays back slower than 300 s in the first ladder.
- [ ] Price steps are 1.5x to 4x, except at a marked zone or currency change.
- [ ] First rebirth lands between minute 20 and 40.
- [ ] Each rebirth gives at least one thing on screen besides a multiplier.
- [ ] Every source in the economy sheet has a named sink.
- [ ] No buff group multiplies with itself; the stack formula is written down.
- [ ] Prices never need more than 4 digits plus a suffix on screen.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Players stop buying around minute 8 and leave | One tier's payback jumps past 300 s | Run pacing.py; split the tier or cut its price |
| Rebirth button ignored | Reset costs more time than it pays back | Prompt at +50% to +200% gain; add a slot or tool to each rebirth |
| Players finish everything in the first hour | Ladder has 12 units and all are always in stock | Add restock clocks, more tiers, or a rebirth gate |
| Currency piles into numbers no one reads | Sources have no matching sink | Type each source; add a repeatable or exponential sink |
| Players quit at one rebirth and never return | Wall depends on luck and rebirth resets luck | Keep luck through rebirth; give a pity path |
| Returning players find an empty bank | Offline cap of 2 h or less | Raise the cap to cover a night or a school day |

## Sources

Formulas and prestige: [Pecorella, Part I](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i), [Part III](https://gamedeveloper.com/design/the-math-of-idle-games-part-iii), [Quest for Progress](https://www.slideshare.net/slideshow/quest-for-progress-gdc-europe-2016/65405507). Sinks: [Lost Garden](https://lostgarden.com/2021/12/12/value-chains/). Game numbers: the links in each table; wikis are community-kept and can lag the game. Live counts: Roblox public API, 25 Nov 2026. Ratios, payback and pacing runs are our arithmetic.
