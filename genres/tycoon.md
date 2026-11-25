# Tycoon

> **The feeling sold:** "I built this whole place myself, and it makes money while I watch."

This page covers three shapes: dropper tycoons (buy buttons, machines make cash), management tycoons (hire staff, lay out a restaurant or park, serve customers) and co-op shop or restaurant games (up to 6 friends run one business). Player counts marked "now" are from Roblox public API, 25 Nov 2026.

## At a glance

| | |
|---|---|
| Core verb | Buy the next thing (a button, a worker, a plot), then collect the cash it makes. In management tycoons: serve the next customer. |
| Study these first | **Restaurant Tycoon 3**: the 2025 management leader, 6,221 now, ships 2 to 4 features a month. **Military Tycoon**: the only documented 21-step income ladder and a 40-step rebirth. **Theme Park Tycoon 2**: a star-rating checklist as the goal, live since 2012. **Lumber Tycoon 2**: a land ladder and a tool ladder, live since 2009. **Karinderya!**: a co-op eatery that rose to six figures and fell to 1% to 2% of its peak. None has a teardown in this repo yet. |
| Session that works | Karinderya!: 20.8 minutes average ([rotrends](https://www.rotrends.com/game/10648820673/Karinderya)). Not known for the others. |
| Players per server | 6 for co-op management (Restaurant Tycoon 3, Karinderya!, Run a Restaurant!, Supermarket Simulator). 6 to 18 for classic tycoons (Theme Park Tycoon 2 and Lumber Tycoon 2 at 6, Military Tycoon 12, Car Dealership Tycoon 15, War Tycoon 18). One outlier: Supermarket Together at 50. |
| Who owns the genre | Old games hold small, steady crowds: Theme Park Tycoon 2 (created 2012) 2,045 now, Lumber Tycoon 2 (2009) 1,718, Restaurant Tycoon 2 (2019) 1,137, War Tycoon (2020) 6,651. The newest leader is Restaurant Tycoon 3 (January 2025) at 6,221. 2026 entries spike and fall: Karinderya! peaked at 126K to 295K in September 2026 (trackers disagree) and has 2,954 now. 2026 mansion and military shells sit at 3,000 to 5,000. |
| Build cost | Not known from sources. **Our read:** the cost is the content after the base. Restaurant Tycoon 3 shipped about 25 dated features in the 17 months after its alpha. |
| Money comes from | Auto Collect (99 to 575 R$ across tycoons), build-freedom and capacity passes, and 2x cash. Karinderya! sells only developer products (194 of them, no passes). |
| What kills clones | A base that can be finished, with nothing to do after it. |

Sources for this table: [Roblox games API](https://games.roblox.com/v1/games?universeIds=7094518649,1214576306,31970568,2092410051,1434220026,7843413523,6657933195,10553704684,9970645639,10648820673,10708913337), [games API, classic tycoons](https://games.roblox.com/v1/games?universeIds=2471084,605887098), [games API, military and mansion tycoons](https://games.roblox.com/v1/games?universeIds=1526814825,2788648141,3191268194,8724785394,10698216738,4518160318,9913288302), [rowatcher](https://rowatcher.com/games/10648820673), [rotrends](https://www.rotrends.com/game/10648820673/Karinderya), [Earnaldo](https://earnaldo.com/blog/karinderya), [Restaurant Tycoon 3 DevForum changelog](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704).

## Why people play it

The store pages say what is promised. Restaurant Tycoon 3 promises money "while you're offline" ([games API](https://games.roblox.com/v1/games?universeIds=5750914919,5361032378,10708913337,7094518649)). Karinderya! sets one goal on its page: "Be the first 5 star owner" ([games API](https://games.roblox.com/v1/games?universeIds=10648820673)). Theme Park Tycoon 2 grades every park from 0.5 to 5 stars against a printed checklist ([TPT2 wiki: Rating](https://tpt2.fandom.com/wiki/Rating)).

Age, device and player quotes: not known from sources.

**Our read:** the need is visible ownership. Every purchase stands in the world as a new object, so after 10 minutes the player can point at a building that did not exist when they joined. Management tycoons add a second need: a machine the player designed, such as a restaurant with 16 staff.

## The loop, with a stopwatch

Leader: **Restaurant Tycoon 2**, the management loop with the most documented numbers ([RT2 wiki: Cheeseburger](https://restaurant-tycoon-2.fandom.com/wiki/Cheeseburger), [Workers](https://restaurant-tycoon-2.fandom.com/wiki/Chefs), [Upgrades](https://restaurant-tycoon-2.fandom.com/wiki/Upgrades), [Ratings](https://restaurant-tycoon-2.fandom.com/wiki/Ratings)). No source timed any step.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Customers arrive | Nothing; the group picks a table | not known | A group sized to the largest free table walks in | Seats filled |
| 2. Order and cook | Cooks or lets chefs cook | not known | Chef at the station | Dish: Cheeseburger $6 basic, $9 advanced |
| 3. Serve | Waiter carries the dish | not known | Food arrives at the table | Service rating, from waiter happiness, level and wait time |
| 4. Pay | Walks to the table to pick up cash | not known | Cash left on the table, or a card payment | Money. Credit Card Payments ($600) auto-collects 50% |
| 5. Spend | Buys a worker, upgrade or plot | not known | New worker appears | First worker $200: 34 basic dishes or 23 advanced (our arithmetic) |

How the others differ. **Military Tycoon** pays 25 cash for each shot at a dummy "worker" in your base ([wiki: Worker](https://military-tycoon.fandom.com/wiki/Worker)). **Lumber Tycoon 2** pays per unit of wood, and planks sell for 5 to 10 times the log price, so a sawmill trip is the loop's big step ([wiki: Wood](https://lumber-tycoon-2.fandom.com/wiki/Wood)). **Theme Park Tycoon 2** charges guests per ride, stall and entry; set a price too high and they complain and stop paying ([wiki: Money](https://tpt2.fandom.com/wiki/Money)). **Karinderya!** gives 6 players different stations in one eatery: take order, cook, serve, grocery ([Earnaldo guide](https://earnaldo.com/blog/karinderya-beginner-guide)).

The loop stack:

| Every | What finishes | Example |
|---|---|---|
| A few seconds | A dish is paid, a shot pays | RT2 $6 to $9; Military 25 cash |
| About a minute | The next worker or upgrade | RT2's first 15 purchases run $100 to $3,500 |
| 5 to 10 minutes | A plot expansion | RT2 plots $600, $1,200, $1,600; TPT2 nearest ring $5,000 |
| A session | A star level | TPT2: 0.5 stars, then 2 stars |
| A day | A daily bonus | TPT2 $1,750 a day; RT3 daily friendship meter pays diamonds |
| A week | An update | Karinderya! on Saturdays |
| After the base | Rebirth or a new system | Military Tycoon rebirth; RT3 franchising |

The minute and 5-to-10-minute rows are **our read** of the price lists. Time to finish a base is on no source for any tycoon.

## The first five minutes

What the sources record. Karinderya! opens with a blue banner, "Place Table and Chairs". The player puts furniture on green footprint pads, assigns seats, and serves a couple of customers. Only then does the codes button appear. Three teleport tabs (Grocery, Home, Shop) and five left icons (Shop, Menu, Index, Eatery, Settings) follow ([Earnaldo guide](https://earnaldo.com/blog/karinderya-beginner-guide), [AllThings.How](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/)). Theme Park Tycoon 2 starts the player with $11,000 and a first goal of one ride, one food stall, one drink stall and one restroom for 0.5 stars and 200 credits ([wiki: Money](https://tpt2.fandom.com/wiki/Money), [wiki: Getting started](https://tpt2.fandom.com/wiki/Getting_started!)). Military Tycoon's wiki says buy the cheapest workers first, then capture an oil rig ([wiki: Worker](https://military-tycoon.fandom.com/wiki/Worker)). No source gives seconds for any of these steps.

Gates for a new tycoon:

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | The player stands on their own plot. One button glows, and it is free or costs less than the starting cash. | Military's first worker is free; Karinderya!'s banner points at the first placement. |
| 0:30 | First purchase made, first cash collected. | **Our read:** Military's second worker costs 35, under 2 shots at 25 cash. |
| 1:00 | Two or three income objects stand on the plot. | **Our read**, from the Start with ladder below. |
| 3:00 | First 10x jump bought (the third button), and the first goal checklist is on screen. | TPT2's 0.5-star list; the 10x opening jump in Military's ladder. |
| 5:00 | 8 to 10 buttons bought, and the first expansion or upgrade tier is visible with its price. | **Our read**, from the Start with ladder below. |

## Numbers that work

**What is not known.** No source has a first-20-buttons table, an income-per-second table or a time-to-finish figure for any dropper tycoon. The tables below are the ladders that were found, from a shooting tycoon, a restaurant tycoon, a lumber game and a park builder.

**Opening ladders.** Ratios are our arithmetic.

| Game | First purchases in price order | Ratio, step to step | Source |
|---|---|---|---|
| Military Tycoon workers (21) | 0, 35, 350, 1,250, 2,000, 3,000, 3,500, 3,500, 5,000, 5,000, 5,500, 6,500, 7,000, 7,500, 8,000 | 10x, 3.6x, 1.6x, then 1.0x to 1.4x | [wiki](https://military-tycoon.fandom.com/wiki/Worker) (wiki groups by location; in-game order not stated) |
| Restaurant Tycoon 2 workers, per type | $200, $500, $1,000, $1,500, $2,000, $2,500, $3,000 | 2.5x, 2x, 1.5x, 1.33x, 1.25x, 1.2x | [wiki](https://restaurant-tycoon-2.fandom.com/wiki/Chefs) |
| Restaurant Tycoon 2 upgrades and plots | 100, 250, 600, 600, 600, 800, 1,200, 1,200, 1,600, 1,800, 2,000, 2,000, 2,500, 3,200, 3,500 | mostly 1.0x to 2x | [wiki](https://restaurant-tycoon-2.fandom.com/wiki/Upgrades) |
| Lumber Tycoon 2 axes | $12, $90, $190, $550, $2,040 | 7.5x, 2.1x, 2.9x, 3.7x; damage per second roughly doubles early (0.3, 0.75, 1.33, 2.10, 3.33) | [wiki](https://lumber-tycoon-2.fandom.com/wiki/Axes) |
| Lumber Tycoon 2 land | $100, $3,000, $6,000, then +$3,000 each to $72,000 | 30x, 2x, 1.5x, 1.33x ... 1.04x | [wiki](https://lumber-tycoon-2.fandom.com/wiki/Land_Store) |
| Theme Park Tycoon 2 plot rings | $5,000, $10,000, $20,000, $40,000, $80,000, $120,000, $180,000 | 2x for four rings, then 1.5x | [wiki](https://tpt2.fandom.com/wiki/Plot_expansions) |

The shape repeats: one big jump from free to a few hundred, then steps of 1.2x to 2x.

**What a full base costs.** Conversions are our arithmetic.

| Game | Whole base | In units of the first income |
|---|---|---|
| Military Tycoon | 150,135 cash for all 21 workers | 6,005 shots at 25 cash (shot rate not documented) |
| Restaurant Tycoon 2 | $45,950 for all upgrades and plots, plus $22,300 for 7 chefs, 7 waiters, 2 operators, 1 driver | About 7,600 advanced cheeseburgers at $9 |
| Lumber Tycoon 2 | $900,100 for all 25 plots | 90,010 oak planks at 10, or 2,143 Phantom planks at 420 |
| Theme Park Tycoon 2 | $1,600,000 plus 9,000 credits for all money plots | 145 times the $11,000 start; 914 days of the $1,750 daily bonus |

**Rebirth.** Military Tycoon resets the whole base for +0.1 to the cash multiplier, up to x5 at 40 rebirths. Each step unlocks something: bunker hatch and helicopter at 1, submarine at 2, RPG at 4, bomber at 5, warplane at 12, Railgun at 25. Gamepass, event and buildable units and the ATM survive the reset. The rebirth price is not documented ([wiki: Rebirths](https://military-tycoon.fandom.com/wiki/Rebirths)). **Our read:** rebirth 1 adds 10% income, so the rebuild takes about 91% as long as the first build. What pays for the reset is the unlock list.

**Staff.** Restaurant Tycoon 3 caps chefs at 8 and servers at 8, with hire costs from 250 to 17.5K cash and walk-speed upgrades of +20% to +60% ([Bloxodes RT3 workers](https://bloxodes.com/wiki/restaurant-tycoon-3/workers)). Restaurant Tycoon 2 caps chefs and waiters at 7, or 12 with a pass, and workers level themselves to 15 ([wiki](https://restaurant-tycoon-2.fandom.com/wiki/Chefs)).

**Start with:** a 20-button dropper ladder. It copies the opening shape above (10x, then about 3.3x, then 1.6x, then about 1.3x per step) and the payback rule from [slop/01-anatomy.md](../slop/01-anatomy.md): each object earns back its price in 25 to 300 seconds. Assumptions: income is passive, and the player buys each button the moment they can afford it. This is our read; tune it with [tools/pacing.py](../tools/pacing.py).

| Button | Price | Adds income/s | Payback (s) | Wait to afford (s) | Minutes in | Total income/s |
|---|---|---|---|---|---|---|
| 1 | free | +5 | - | 0 | 0.0 | 5 |
| 2 | 30 | +3 | 10 | 6 | 0.1 | 8 |
| 3 | 300 | +10 | 30 | 38 | 0.7 | 18 |
| 4 | 1,000 | +22 | 45 | 56 | 1.7 | 40 |
| 5 | 1,600 | +25 | 64 | 40 | 2.3 | 65 |
| 6 | 2,200 | +30 | 73 | 34 | 2.9 | 95 |
| 8 | 4,000 | +45 | 89 | 30 | 3.9 | 178 |
| 10 | 6,800 | +70 | 97 | 29 | 4.9 | 303 |
| 12 | 11,500 | +105 | 110 | 30 | 5.9 | 493 |
| 15 | 25,000 | +195 | 128 | 32 | 7.4 | 978 |
| 18 | 52,000 | +345 | 151 | 35 | 9.1 | 1,843 |
| 20 | 84,000 | +500 | 168 | 37 | 10.3 | 2,758 |

Buttons in between keep the 1.27x to 1.38x step. The result: a wait of 30 to 56 seconds between buttons, and 20 buttons in about 10 minutes. Payback rises from 10 to 168 seconds, inside the 300-second ceiling. Past button 20, let the wait grow to 60 to 120 seconds and open the next floor or zone every 10 buttons.

## What brings them back

**Later in the same session.** The next button, every 30 to 60 seconds in the ladder above (our read). Customer variety: Restaurant Tycoon 3 has rare customers (VIP, birthday, food critic, celebrity, rude), and a pass triples the chance of them ([game-passes API](https://apis.roblox.com/game-passes/v1/universes/7094518649/game-passes?passView=Full&pageSize=50)). Karinderya!'s customers are named characters: Marcus never pays, Jeeson steals about half his orders, and players stop runners by hitting them with a frying pan. An in-game Customers Index lists them ([AllThings.How](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/)).

**Tomorrow.** Theme Park Tycoon 2 pays $1,750 a day, 16% of the starting money (our arithmetic) ([wiki](https://tpt2.fandom.com/wiki/Money)). Restaurant Tycoon 3 has a daily friendship meter that pays diamonds (15 July 2025) and earns offline since 28 August 2026. The offline rate and cap are not known ([DevForum](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704)). Karinderya! has no offline income on record.

**Next week and after, once the base is finished.** This is where tycoons differ most:

| Game | What there is to do after the last button |
|---|---|
| Restaurant Tycoon 3 | Franchising (26 Sep 2025), food rarity, rare customers, cash objectives, milestones, a third floor, a drive-thru, Level 4 kitchens, events ([DevForum](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704)) |
| Military Tycoon | 40 rebirths, each with a weapon, vehicle or turret unlock ([wiki](https://military-tycoon.fandom.com/wiki/Rebirths)) |
| War Tycoon | Rebirths unlock gear such as a Barrett sniper in the Bunker; cash also comes from capture points and kills ([game-passes API](https://apis.roblox.com/game-passes/v1/universes/1526814825/game-passes?passView=Full&pageSize=50)) |
| Theme Park Tycoon 2 | Star rating up to 5 stars, levels to 93 (one ride or stall picked per level since 10 Apr 2026), 28 achievements, 64 plots ([wiki: Leveling](https://tpt2.fandom.com/wiki/Leveling)) |
| Lumber Tycoon 2 | 23 wood types, from oak at 10 a plank to Phantom at 420; 25 land plots ([wiki: Wood](https://lumber-tycoon-2.fandom.com/wiki/Wood)) |
| Karinderya! | 5 stove tiers, mystery boxes at 10,000 and 20,000 cash, weekly decoration updates ([AllThings.How](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/)) |

**Our read:** the games that last have a layer that never completes: rebirth steps, levels, rare customers, franchises. A star rating or a list of furniture ends.

## Other players

**Server size.** 6 in co-op management, 12 to 18 in PvP tycoons (Military 12, War Tycoon 18) ([games API](https://games.roblox.com/v1/games?universeIds=1526814825,2788648141,3191268194,8724785394,10698216738,4518160318,9913288302)).

**What they do together.** Co-op games split jobs. Karinderya! has four stations (Eatery, Grocery, Counter, Shop). Restaurant Tycoon 3's highest friend permission, co-owner, can cook and hire, and guides warn that it can be used to sabotage ([Sportskeeda, secondary](https://www.sportskeeda.com/roblox-news/restaurant-tycoon-3-a-beginner-s-guide)). Both games give a friend boost to earnings. Run a Restaurant! has a player-to-player market ([game-passes API](https://apis.roblox.com/game-passes/v1/universes/9970645639/game-passes?passView=Full&pageSize=50)).

**What they do to each other.** War Tycoon pays cash for kills and captured points. In Military Tycoon, gamepass vehicles and guns can be taken by other players if the owner rebirths while they are in the server ([wiki: Gamepasses](https://military-tycoon.fandom.com/wiki/Gamepasses)).

**What gets clipped:** not known from sources. **Our read:** in a co-op eatery it is the named thief running out with food and a player chasing him with a frying pan.

## Money

| Game | Pass | R$ | What it does |
|---|---|---|---|
| Restaurant Tycoon 3 | Sandbox Mode | 1,499 | Build freely |
| Restaurant Tycoon 3 | Faster Cooking | 449 | Chefs 25% faster, player 50% |
| Restaurant Tycoon 3 | 3x Customer Luck | 399 | More rare customers |
| Restaurant Tycoon 3 | Auto Money Collection | 299 | No walking to tables |
| Restaurant Tycoon 3 | Chip Shop Diva (super staff) | 200 a month | One staff member at Level 5 |
| Own a Grocery Store | All Passes / 2x Cash / Starter Pack | 1,299 / 449 / 9 | 13 passes in all |
| Run a Restaurant! | Plot Expansion / Cash Flow / Auto Collect | 999 / 249 / 199 | Cash Flow: 30% chance a customer pays 2x |
| Theme Park Tycoon 2 | All 5 passes | 898 total | Collisions off, 24 plots, ride operation, height, colours |
| War Tycoon | F-35 Bundle / 2X CASH / Auto Collect | 1,499 / 249 / 99 | 20 passes, mostly vehicles and weapons |
| Military Tycoon | Instant Rebirth | a little over 750 | One rebirth per purchase |
| Lumber Tycoon 2 | Money packs | 9 to 1,799 | About 50 to 55 money per R$ at every size |

Sources: game-passes API for [RT3](https://apis.roblox.com/game-passes/v1/universes/7094518649/game-passes?passView=Full&pageSize=50), [Own a Grocery Store](https://apis.roblox.com/game-passes/v1/universes/10553704684/game-passes?passView=Full&pageSize=50), [Run a Restaurant!](https://apis.roblox.com/game-passes/v1/universes/9970645639/game-passes?passView=Full&pageSize=50), [TPT2](https://apis.roblox.com/game-passes/v1/universes/31970568/game-passes?passView=Full&pageSize=50), [War Tycoon](https://apis.roblox.com/game-passes/v1/universes/1526814825/game-passes?passView=Full&pageSize=50) (all 25 Nov 2026); [Bloxodes RT3 workers](https://bloxodes.com/wiki/restaurant-tycoon-3/workers); [Military wiki](https://military-tycoon.fandom.com/wiki/Instant_Rebirth); [LT2 wiki: Money](https://lumber-tycoon-2.fandom.com/wiki/Money).

Auto Collect is in almost every catalogue, from 99 (War Tycoon) to 575 R$ (Mega Mansion Tycoon 2). Theme Park Tycoon 2 and Restaurant Tycoon 3 sell no currency at all. Supermarket Together and Karinderya! sell no passes. **Our read:** a tycoon's pass list is a map of its friction. Walking to collect, the item limit, the build grid and the wait for rare customers are what players pay to remove. Price them from 99 to 499 and keep one big build-freedom pass near 1,500.

Where offers appear: not known from sources.

**The line.** 3x Customer Luck, Cash Flow's 30% chance and cash-bought mystery boxes all touch chance. Once a paid item changes odds, Roblox's paid random item rules apply. A monthly staff subscription renews without the player acting. See [foundations/15-the-line.md](../foundations/15-the-line.md) and [foundations/12-monetization.md](../foundations/12-monetization.md).

## Live ops

| Game | Rhythm | What an update holds |
|---|---|---|
| Restaurant Tycoon 3 | 2 to 4 features a month, June 2025 to November 2026 | A customer type (celebrity, rude, dine-and-dash), a worker (two new staff on 20 Nov 2026), a building system (third floor, drive-thru, demolition mode) |
| Karinderya! | Weekly, Saturdays; updates open about 12:00 to 12:30 UTC, players peak at 13:30 UTC | Events, Decorations Pt. 1 (tiles, counter upgrades, dishwasher); codes at milestones: 50KCCU gives 50,000 cash, 2MVISITS gives 5,000 cash and a Deluxe Stove |

Sources: [DevForum](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704), [Earnaldo](https://earnaldo.com/blog/karinderya), [AllThings.How](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/).

When updates stop: Retail Tycoon 2 was last updated 8 April 2026 and has 710 players now. My Restaurant! was last updated 12 May 2026 and has 329, from 890M lifetime visits ([games API](https://games.roblox.com/v1/games?universeIds=7094518649,1214576306,31970568,2092410051,1434220026,7843413523,6657933195,10553704684,9970645639,10648820673,10708913337)).

**Our read:** a small team can sustain Restaurant Tycoon 3's rhythm better than Karinderya!'s. One new customer type or staff member every 1 to 2 weeks is a small build. A weekly decoration pack is also small, but it is used up in one session. See [foundations/13-live-ops.md](../foundations/13-live-ops.md).

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| CCU falls to 1% to 2% of peak in about 80 days while the like ratio stays at 97% | The content runs out. Karinderya!: peak 126K to 295K in September 2026, 2,954 now, 97.4% like; weekly updates did not stop it ([rowatcher](https://rowatcher.com/games/10648820673), [rotrends](https://www.rotrends.com/game/10648820673/Karinderya)) | Build an after-base layer before launch: rebirth, franchises, rare customers, levels |
| Players stop after the last purchase | The goal is a finish line ("be the first 5 star owner") | Put a repeating goal after it. Military Tycoon has 40 rebirth steps |
| CCU drifts down with no event | No update in months. Retail Tycoon 2: last update April 2026, 710 now | 2 to 4 small features a month, like Restaurant Tycoon 3 |
| Friends quit after one session together | A co-owner wrecks the restaurant (guides warn of this in Restaurant Tycoon 3) | Permission tiers: helper, cook, co-owner; nothing can be sold or demolished by a helper |
| Rebirth rate near zero | The reset costs a full rebuild for +10% | Give every rebirth a visible unlock, as Military does at 1, 2, 4, 5, 10, 12 |
| A 2026 shell stalls at 3,000 to 5,000 CCU | Same mansion or military template as the 2026 clones | Change one structure: co-op roles, PvP income (War Tycoon), named customers |
| Wait between buttons climbs past 2 minutes in the first 10 minutes | Prices grow faster than income | Rebuild the ladder by payback time (Start with above). No sourced tycoon example; the rule is from [slop/01-anatomy.md](../slop/01-anatomy.md) |

## Checklist

1. A new player's first button is free or costs less than the starting cash, and it glows within 5 seconds of spawning.
2. Payback of every button in the first 20 is between 10 and 300 seconds.
3. The wait between buttons in the first 10 minutes is 20 to 60 seconds.
4. The opening ladder has one jump of about 10x, then steps of 1.2x to 2x.
5. 20 buttons take 8 to 15 minutes.
6. A goal checklist with a number (stars, rating, level) is on screen by 3:00.
7. The after-base layer exists at launch and has at least 10 steps (rebirths, levels, franchises).
8. Each rebirth unlocks something the player can see or use, besides a multiplier.
9. Customers or events include at least 5 named types with different behaviour.
10. Co-op games: 6 players per server and at least 3 different jobs.
11. Co-op games: a helper permission that cannot sell, demolish or spend the owner's cash.
12. Auto Collect, if sold, costs 99 to 299 R$.
13. Nothing sold for Robux changes odds unless the odds are shown.
14. An update ships at least every 2 weeks for the first 3 months.
15. A daily return reward exists and is worth 10% to 20% of the starting money (TPT2: 16%).

## Twists and open space

Variations that already worked:

- **PvP-fed income.** War Tycoon pays for oil, capture points and kills. 6,651 now, 18 per server, live since 2020.
- **Co-op eatery with misbehaving named customers.** Karinderya! peaked at 126K to 295K concurrent players in September 2026, one to two months after its 7 August launch (trackers disagree).
- **Restaurant to franchise.** Restaurant Tycoon 3 added franchising five months after its alpha and holds 6,221 now with a 95.3% like ratio.
- **Large co-op store.** Supermarket Together runs 50 per server and sells no passes; 1,249 now.

**Our read**, angles that look under-served:

- A co-op eatery with Karinderya!'s first hour plus Military's 40-step rebirth, so the launch spike has somewhere to go.
- A dropper tycoon with timed customer events (a celebrity every 15 minutes, a rush every hour), borrowing the clocks from [genres/rng.md](rng.md) and [genres/fishing-and-digging.md](fishing-and-digging.md).
- An index as the long goal: every customer, dish and machine is a collectible ([foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md)).

## Sources

Related pages: [foundations/06-progression-and-economy.md](../foundations/06-progression-and-economy.md), [foundations/08-retention.md](../foundations/08-retention.md), [foundations/09-other-players.md](../foundations/09-other-players.md), [slop/01-anatomy.md](../slop/01-anatomy.md). No tycoon has a teardown in this repo yet.

Main external sources: Roblox games, votes and game-pass APIs (25 Nov 2026); the Military Tycoon, Restaurant Tycoon 2, Lumber Tycoon 2 and Theme Park Tycoon 2 wikis (pages linked inline); the [Restaurant Tycoon 3 DevForum changelog](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704); [Bloxodes](https://bloxodes.com/wiki/restaurant-tycoon-3/workers); [Earnaldo](https://earnaldo.com/blog/karinderya) and [AllThings.How](https://allthings.how/karinderya-on-roblox-how-to-make-money-fast/) on Karinderya!; trackers [rowatcher](https://rowatcher.com/games/10648820673) and [rotrends](https://www.rotrends.com/game/10648820673/Karinderya).
