# Grow and harvest

> **The feeling sold:** "I planted it, I came back, it was huge and golden, and my friends saw it."

This page covers games where the player plants, waits, harvests, sells and shows: [Grow a Garden](../teardowns/grow-a-garden.md), Plants vs Brainrots and the followers. Why clocks, offline growth and visible wealth hold players is argued in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md); this page gives the per-game tables and starting values. Counts marked "now" are from the Roblox public API, 25 Nov 2026, 13:53 UTC.

## At a glance

| | |
|---|---|
| Core verb | Plant, then harvest |
| Study these first | [Grow a Garden](../teardowns/grow-a-garden.md): the reference for shop clocks, regrowth and mutations; 22.3M peak. Plants vs Brainrots: the same studio family adds defence (plants kill walking units, which then earn). Grow a Garden 2: a sequel in name only, to see what not to do |
| Session that works | About 21 minutes in Grow a Garden, the longest of the slop hits ([RoVitals](https://rovitals.com/game/126884695634066)) |
| Players per server | 4 (Grow a Garden), 5 (Plants vs Brainrots) (Roblox public API, 25 Nov 2026) |
| Who owns the genre | Nobody holds it now. Grow a Garden (created March 2025) leads with 18K; Plants vs Brainrots 2,475; Grow a Garden 2 about 1,000. The 2026 wave went to steal and throw games |
| Build cost | Grow a Garden's first version took a 16-year-old about three days ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). **Our read:** the expensive part is content: 609 crops, 461 pets and 83 eggs by November 2026 ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden)) |
| Money comes from | Developer products: restocks (79 R$), seeds bought with Robux (7 to 1,700 R$), eggs and hatch skips. Almost no passes |
| What kills clones | A sequel or reskin with no weekly event and no shared clock |

## Why people play it

About 35% of Grow a Garden's players were under 13. It was the fastest game to 1 billion visits (33 days), and its coverage was almost entirely short-form video. A critic called it the "new generation's FarmVille"; Kotaku said it looked like a prototype ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Its store text tells players to flex fruits and finds on friends and says the garden grows while they are offline (Roblox public API, 25 Nov 2026).

**Our read:** two wants. Something keeps happening while the player is away, so coming back always pays. And a lucky crop (gold, rainbow, struck by a rare weather) is a picture a child can show. Nothing is taken from anyone unless a player pays to steal, so the genre carries far less of the harm in [foundations/15-the-line.md](../foundations/15-the-line.md) than [steal-and-defend.md](steal-and-defend.md).

## The loop, with a stopwatch

Leader: Grow a Garden. Sources: [Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [crop data](https://growagarden.fandom.com/wiki/Module:Crop_Data), [Sheckles](https://growagarden.fandom.com/wiki/Sheckles), [Bloxodes calculator](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Check stock | Opens the seed shop | Restock every 300 s, the same on every server | Rare seeds in stock or not | Stock: 4 staples always, rare seeds by chance |
| 2. Buy | Buys seeds | not known | Seed in inventory | Sheckles down: Carrot 10 up to 1Qa |
| 3. Plant | Equips the seed, clicks a brown plot | not known | Sprout | Plot space |
| 4. Grow | Waits, or plants more | Carrot 8 s; Strawberry 32 s; Blueberry 100 s; Tomato 1,102 s; Sunflower 5,700 s | Crop grows; weather can mutate it | Size and mutations roll |
| 5. Harvest | Taps the crop | not known | Crop with a weight | Value = base x (weight / base weight)² |
| 6. Regrow | Nothing | Strawberry 16 s, Blueberry 20 s, Tomato 221 s, Sunflower 1,855 s | Plant fruits again | Free harvests |
| 7. Sell | Walks to the seller | not known | Sheckles counter | +10% per friend in the server, up to +40% |
| 8. Show | Stands in the garden | | Neighbours see mutated crops | Nothing; status |

**How Plants vs Brainrots differs.** The plants are towers. Brainrots walk down a street from a spawner; a plant that defeats one turns it into the player's unit, which earns cash per second. A new player gets $400, the price of two $200 Cactus seeds, which grow in 5 seconds ([Cactus](https://plantsvsbrainrots.fandom.com/wiki/Cactus)). It has five rebirths and a Fuse Machine (plant plus brainrot makes a new brainrot in 1 to 7 minutes) ([Mechanics](https://plantsvsbrainrots.fandom.com/wiki/Mechanics)). The wiki dates from the August 2025 launch, so these numbers may be out of date.

**The loop stack** in Grow a Garden ([Bloxodes shops](https://bloxodes.com/wiki/grow-a-garden/shops), [Weather](https://growagarden.fandom.com/wiki/Weather), [Bloxodes index](https://bloxodes.com/wiki/grow-a-garden)):

| Every | What closes |
|---|---|
| 8 to 20 seconds | A Carrot grows; a Strawberry or Blueberry regrows |
| 5 minutes | Seed shop and gear shop restock |
| About 20 minutes | Rain, lasting 3 to 5 minutes; some weathers give +50% growth |
| 30 minutes | Egg shop restocks |
| 60 minutes | The event-coin shop restocks |
| 2 to 6 hours | Thunderstorm |
| 4 hours | Night or Blood Moon cycle; Ascension available again |
| 10 minutes to 8 hours | An egg hatches, by egg type |
| 24 hours | Daily deals (4 seeds, 1 to 5 stock each, one discounted); first plot expansion finishes |
| 3 days | Second plot expansion finishes |
| 7 days | Saturday update; events run in 3 or 4 weekly parts |

## The first five minutes

No source timed a first session. Lines without a link are **Our read**, built from the shop and crop tables.

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | The player holds Carrot seeds and stands at their plot | Players start with carrot seeds ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)); four numbered lines in the store text teach equip, click a plot, wait, harvest |
| 0:30 | First Carrot harvested and sold for about 20 | Grows in 8 s; seed costs 10 |
| 1:00 | Several Carrot loops; money doubled each time | 10 to 20 per 8 s |
| 3:00 | Strawberry (50) bought; it regrows every 16 s | 1 to 2 minutes of Carrot loops |
| 5:00 | First restock watched; Blueberry (400) within reach | Restock at 300 s; "a few minutes" to 400 |

Gates for a new grow game. **Start with:**

| By | Gate | Why this number |
|---|---|---|
| 0:15 | First crop harvested and sold | Carrot is 8 s; Cactus in Plants vs Brainrots 5 s |
| 1:00 | Money doubled at least twice | Carrot doubles in 8 s |
| 3:00 | First crop that regrows is planted | Strawberry regrows in 16 s; regrowth is where profit lives (below) |
| 5:00 | First restock seen, with the timer on screen | 300 s clock |
| 10:00 | First egg bought or first rare weather seen | Common egg hatches in 10 min; rain every 20 min |

## Numbers that work

**Seed ladder, first rungs** ([Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [crop data](https://growagarden.fandom.com/wiki/Module:Crop_Data), read 25 Nov 2026). The full table with stock sizes and payback is in [the teardown](../teardowns/grow-a-garden.md).

| Seed | Price | R$ | In stock | Grows | Sells | Regrows |
|---|---|---|---|---|---|---|
| Carrot | 10 | 7 | always | 8 s | about 20 | no |
| Strawberry | 50 | 21 | always | 32 s | 15 | 16 s |
| Blueberry | 400 | 49 | always | 100 s | 20 | 20 s |
| Buttercup | 600 | 14 | 1 in 3 | 15 s | 600 | not stated |
| Tomato | 800 | 79 | always | 1,102 s | 30 | 221 s |
| Daffodil | 1,000 | 19 | 1 in 7 | 13 s | 1,000 | not stated |
| Bamboo | 4,000 | 99 | 1 in 5 | 236 s | 4,000 | not stated |

Three findings, all our arithmetic on that table:

1. **Only the first seed profits on its sale.** Carrot doubles its price in 8 seconds. Buttercup, Daffodil and Bamboo sell for exactly their seed price. Profit past the first rung comes from regrowth and from mutations.
2. **Regrowth payback, assuming one fruit per harvest** (the wiki does not give fruit counts): Strawberry pays back on its 4th harvest, at about 80 s; Blueberry on its 20th, at about 8 minutes; Tomato on its 27th, at about 1 hour 54 minutes. After that every harvest is profit.
3. **Mutations are the real money.** Value = base x size factor x variant x (1 + sum of mutation multipliers - number of mutations) ([Bloxodes](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator)). A Gold (x20) Carrot that is also Wet (x2) and Chilled (x2) sells for 20 x 20 x 3 = 1,200, sixty times a plain one.

**Clocks on rare seeds.** Each restock is a roll. Our arithmetic on expected wait at 5 minutes per restock: Buttercup (1 in 3) 15 min; Bamboo (1 in 5) 25 min; Watermelon (1 in 8) 40 min; Coconut (1 in 20) 100 min; Dragon Fruit (1 in 50) about 4 hours; Mango (1 in 80) about 7 hours; the rarest seed (1 in 1,300) about 4.5 days.

**Eggs** ([Pet Eggs](https://growagarden.fandom.com/wiki/Pet_Eggs), [Eggs](https://growagarden.fandom.com/wiki/Eggs)):

| Egg | Chance in a 30-min restock | Hatch | Chance of the top pet |
|---|---|---|---|
| Common | 99% | 10 min | not known |
| Uncommon | 55% | 20 min | not known |
| Rare | 26% | 2 h | 8.33% |
| Legendary | 15% | 4 h | 2.13% |
| Mythical | 9% | 5 h 6 min 40 s | 1.5% |
| Bug | 5% | 8 h | 1% |
| Robux premium eggs | | 30 s | 0.25 to 0.5% |

Egg slots: 3 at the start, up to 13. **Our read:** the hatch ladder is shaped to life. A Common egg finishes inside one 21-minute session; a 4 to 8 hour egg finishes overnight or during a school day, so it pulls the player back the next morning.

**Plants vs Brainrots rebirths** ([Mechanics](https://plantsvsbrainrots.fandom.com/wiki/Mechanics)): R1 $1M plus two named brainrots, then $50M, $100M, $150M, $300M, each +50% luck and +50% money. Ratios (our arithmetic): x50, then x2, x1.5, x2. The first rebirth is the wall and the later ones flatten, the opposite of Steal a Brainrot's x3 to x8 steps.

**Start with:**

| Value | Start with | Derived from |
|---|---|---|
| Players per server | 4 or 5 | Leaders 4 and 5 |
| Shop clock | 300 s, same stock on every server | Grow a Garden |
| Staples | 4 seeds always in stock, with 5 to 25 of the cheapest per restock | Grow a Garden; the stock cap stops the Carrot doubling from running away (at most 25 x 10 = 250 profit per restock from Carrots, our arithmetic) |
| Rung 1 | Doubles its price in 8 to 10 s | Carrot |
| Price steps, first rungs | x5, then x8 | 10, 50, 400 |
| Single-harvest seeds past rung 1 | Sell for their price; value from size and mutation | Buttercup, Daffodil, Bamboo |
| Regrowing seeds in the first hour | Pay back within one session (under 20 min) | Strawberry 80 s and Blueberry 8 min pass; Tomato at about 114 min would not |
| Rare seed odds per restock | 1 in 3 to 1 in 80 on the first 15 rungs | Grow a Garden |
| Weather | One event every 20 min, 3 to 5 min long, shared by all servers | Grow a Garden rain |
| Eggs | Hatch 10 min, 20 min, 2 h, 4 h, 8 h; 3 slots | Grow a Garden |
| Company | +10% sell value per other player in the server | Grow a Garden |

## What brings them back

**Later in the same session.** The 5-minute restock and regrowth every 16 to 20 seconds. A 21-minute session is about four restocks.

**Tomorrow.** The garden grows offline (Roblox public API description). Eggs of 4 to 8 hours finish overnight. Daily deals every 24 hours. The first plot expansion takes 24 hours, the second 3 days ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden)). Offline growth rules in detail: not known.

**Next week and after.** The Saturday update, with events split into three or four weekly parts (Beanstalk, Fall Market, Halloween and Anubis each ran P1 to P3 in 2026) ([Update Log](https://growagarden.fandom.com/wiki/Update_Log)). Weekly exclusive items can only be claimed while online ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). A weekday event, "Watering Wednesday", runs 30 minutes from 3:00 PM PT ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden)). Ascension once every 4 hours, its fee growing by 2 trillion each time.

## Other players

- **Server size.** 4 in Grow a Garden. Gardens sit next to each other.
- **Company pays.** Each friend in the server adds 10% to sell value, up to 40% ([Sheckles](https://growagarden.fandom.com/wiki/Sheckles)). In a 4-player server a player can have at most three others with them, so how the 40% cap is reached is not known.
- **Weather is shared.** It runs on all servers at once, and admins trigger weather before updates ([Weather](https://growagarden.fandom.com/wiki/Weather)).
- **What can be lost.** Only through a paid steal: 37 R$ per crop, it can fail (the Robux is kept and 100 Sheckles refunded), pricier crops fail more often, and the server sees a banner naming thief and victim ([Stealing](https://growagarden.fandom.com/wiki/Stealing)).
- **Trading.** A Trading Ticket (100K Sheckles or 19 R$) enables it ([Gear Shop](https://growagarden.fandom.com/wiki/Gear_Shop)). Items were also sold for real money on eBay and Discord, which breaks Roblox's terms ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)).
- **The clip.** A crop with a rare mutation, or the whole server under a rare weather. The Saturday 23 Aug 2025 "admin war" with Steal a Brainrot set the 22.3M record.

## Money

| Game | Item | Type | R$ |
|---|---|---|---|
| Grow a Garden | Restock now (or watch ads) | Product | 79 |
| Grow a Garden | Steal one crop | Product | 37 |
| Grow a Garden | Common Egg | Product | 19 |
| Grow a Garden | Trading Ticket | Product | 19 |
| Grow a Garden | Seeds bought with Robux | Product | 7 (Carrot) to 1,320 to 1,700 (top seeds) |
| Grow a Garden | Pharaoh's Eye seed (6.67% stock chance) | Product | 829 |
| Grow a Garden | Instant egg refresh, hatch skip, egg slots | Products | not known |
| Grow a Garden | Premium Seed Pack | Pass | off sale |
| Plants vs Brainrots | Cactus seed 5; Wheelbarrow (clears a row) 45; Extra Inventory 149; Grow All 179; VIP 249 | Products and passes | 5 to 249 |

Sources: [Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [Stealing](https://growagarden.fandom.com/wiki/Stealing), [Common Egg](https://growagarden.fandom.com/wiki/Common_Egg), [Eggs](https://growagarden.fandom.com/wiki/Eggs), [Bloxodes seeds](https://bloxodes.com/wiki/grow-a-garden/seeds), [Plants vs Brainrots Mechanics](https://plantsvsbrainrots.fandom.com/wiki/Mechanics); passes from the Roblox public API, 25 Nov 2026. The wiki lists two seeds at different Robux prices on two pages (Cacao 509 or 679, Crimson Thorn 919 or 1,149).

Where offers sit: on the shop itself, next to the timer. **Our read:** a 79 R$ restock sold beside a visible 5-minute timer is an honest offer because the free one is always in view ([slop/02-why-it-holds.md](../slop/02-why-it-holds.md), mechanism 6). What backfired: monetisation added after the studio's sale was criticised ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). The paid steal sells a loss to another child; this handbook's recipe leaves it out ([slop/04-build-it.md](../slop/04-build-it.md)). Premium eggs with a 0.25 to 0.5% top pet are paid random items: see [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

Grow a Garden updates every Saturday. Every record update of 2025 landed on a Saturday (31 May, 14 Jun, 21 Jun, 23 Aug) except Blood Moon on Sunday 18 May. After players complained that events felt rushed, two dedicated event teams were set up in July 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). It was still updated on 25 Nov 2026 at 0.08% of its peak. **Our read:** splitting one event into three weekly parts gives a small team three Saturdays from one theme.

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| The record collapses within the hour: Grow a Garden's 21.3M (21 Jun 2025) fell to 7.6M in one hour and 5.5M in two; its 14-day average was 2.7M | Peaks are event spikes | Judge the game by the weekly average |
| 0.08% of peak 15 months later: 22.3M to 18,093; 2026 high 166,679 on Sat 15 Aug 2026 ([RoVitals](https://rovitals.com/game/126884695634066)) | Trend aged; catalogue bloat at the top (609 crops) | Keep the Saturday; the game still spikes about 5x on event days |
| A sequel loses 55% in 30 days: Grow a Garden 2 (created 21 May 2026), about 1,000 now, last update 3 Nov 2026 | A borrowed name, no update rhythm | Change the verb, ship weekly ([slop/03-quality-bar.md](../slop/03-quality-bar.md)) |
| A farm game from 157K daily-average gain to 79 players: Build A Ring Farm, spike 31 May 2026, last update 27 Oct 2026 ([RoStats](https://rostats.io/records)) | No retention layer behind the spike | Clocks, eggs, offline growth before launch |
| Parents and press object to spending | Monetisation added after a sale; off-platform money trading | Price shortcuts, never outcomes; keep trades in the game |
| Event days feel rushed | One team doing content and events | Separate event work, as Grow a Garden did in July 2025 |

## Checklist

- [ ] 4 or 5 players per server; every garden in view of the others.
- [ ] First crop harvested and sold within 15 seconds of control.
- [ ] Rung 1 doubles its price in under 10 seconds; its stock per restock is capped.
- [ ] Four staple seeds are always in stock.
- [ ] A 5-minute restock timer is on the HUD, and the stock is the same on every server.
- [ ] Rare seeds have published odds per restock between 1 in 3 and 1 in 80 for the first 15 rungs.
- [ ] At least one crop that regrows is affordable inside 3 minutes; every regrowing crop in the first hour pays back inside 20 minutes.
- [ ] Mutations change how a crop looks and multiply its value; the value formula is shown in the game.
- [ ] A shared weather event happens about every 20 minutes and lasts 3 to 5 minutes.
- [ ] Eggs hatch on a ladder from 10 minutes to 8 hours; 3 egg slots to start.
- [ ] Crops keep growing offline, and the return screen shows what grew in one line.
- [ ] Each other player in the server adds a sell bonus.
- [ ] No Robux product takes anything from another player.
- [ ] Events are split into weekly parts and land on the same day each week.

## Twists and open space

Variations that produced hits:

- Plants as towers, and the defeated attacker becomes the earning unit: Plants vs Brainrots, 4.73B visits (Roblox public API, 25 Nov 2026).
- Pets from eggs layered on the garden: Grow a Garden's 461 pets and 83 eggs ([Bloxodes](https://bloxodes.com/wiki/grow-a-garden)).
- Throwing the seed: Throw a Seed, created 7 Nov 2026, 44,386 now (Roblox public API). Its mechanics were not researched; see [plus-one.md](plus-one.md) for the throw family.

**Our read** on open angles:

- Co-op plots. The friend bonus already pays for company. A plot two friends tend together, with one shared harvest, would turn the bonus into a loop.
- A garden with a trip. Every leader grows in place. A 2026-style trip (fetch a rare seed from a far zone and carry it home, as in [plus-one.md](plus-one.md)) gives the wait a job.
- Fewer, slower-rotating crops. Grow a Garden bloated to 609 crops. A game that rotates a smaller set weekly could keep each crop worth a picture.

## Sources

- Teardown: [Grow a Garden](../teardowns/grow-a-garden.md). Related: [Steal a Brainrot](../teardowns/steal-a-brainrot.md).
- Analysis: [slop/01-anatomy.md](../slop/01-anatomy.md), [slop/02-why-it-holds.md](../slop/02-why-it-holds.md), [slop/03-quality-bar.md](../slop/03-quality-bar.md), [slop/04-build-it.md](../slop/04-build-it.md), [slop/05-after-the-peak.md](../slop/05-after-the-peak.md).
- Grow a Garden wiki: [Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop), [Crop data](https://growagarden.fandom.com/wiki/Module:Crop_Data), [Gear Shop](https://growagarden.fandom.com/wiki/Gear_Shop), [Pet Eggs](https://growagarden.fandom.com/wiki/Pet_Eggs), [Eggs](https://growagarden.fandom.com/wiki/Eggs), [Common Egg](https://growagarden.fandom.com/wiki/Common_Egg), [Weather](https://growagarden.fandom.com/wiki/Weather), [Crop Mutations](https://growagarden.fandom.com/wiki/Crop_Mutations), [Sheckles](https://growagarden.fandom.com/wiki/Sheckles), [Stealing](https://growagarden.fandom.com/wiki/Stealing), [Update Log](https://growagarden.fandom.com/wiki/Update_Log).
- Plants vs Brainrots wiki: [Cactus](https://plantsvsbrainrots.fandom.com/wiki/Cactus), [Plants](https://plantsvsbrainrots.fandom.com/wiki/Plants), [Mechanics](https://plantsvsbrainrots.fandom.com/wiki/Mechanics).
- [Bloxodes: Grow a Garden index](https://bloxodes.com/wiki/grow-a-garden), [shops](https://bloxodes.com/wiki/grow-a-garden/shops), [seeds](https://bloxodes.com/wiki/grow-a-garden/seeds), [crop value calculator](https://bloxodes.com/tools/grow-a-garden-crop-value-calculator); [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden); [RoVitals](https://rovitals.com/game/126884695634066); [RoStats records](https://rostats.io/records).
- Roblox public API (games, game passes), 25 Nov 2026.
