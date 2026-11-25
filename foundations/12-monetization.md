# Monetization: what sells, at what price, and when to ask

This page is for pricing a Roblox game: the instruments, what the top games charge, what players buy again, and the moment an offer belongs on screen. Open it before you create your first game pass, and again when the dashboard shows players but no revenue. The limits on chance, loss and children are on [15-the-line.md](15-the-line.md). Prices are base (US) Robux prices on 25 November 2026 unless a line says otherwise. They go stale; check the live page before copying one.

## What is known

### The instruments and their rates

| Instrument | Rule (Nov 2026) | Source |
|---|---|---|
| Game pass | Bought once. A pass Roblox promotes must cost 50 to 800 R$. Free trials (one session, at least an hour, one per player per pass) reach all players from 2 Dec 2026. | [Game passes docs](https://create.roblox.com/docs/production/monetization/game-passes), [DevForum](https://devforum.roblox.com/t/introducing-pass-free-trials/4995943) |
| Developer product | Can be bought again. 1 to 1 billion R$. Roblox keeps no purchase history; the game records each receipt. | [Developer products docs](https://create.roblox.com/docs/production/monetization/developer-products) |
| Subscription | At least 49 R$ a month, or $2.99, $4.99, $7.99, $9.99 or $14.99. Robux price can change once per 60 days. | [Subscriptions docs](https://create.roblox.com/docs/production/monetization/subscriptions) |
| Private server | Monthly price set by you; changing it cancels every subscriber. Roblox Plus members get one free per game since 24 Sep 2026, and you earn up to 100 R$ per Plus member per month from time in paid servers. | [Private servers docs](https://create.roblox.com/docs/production/monetization/private-servers), [DevForum](https://devforum.roblox.com/t/changes-to-roblox-plus-private-server-limits/4739922) |
| Paid access | 25 to 1,000 R$ once, no refunds, not on Xbox. | [Paid access docs](https://create.roblox.com/docs/production/monetization/paid-access-robux) |
| Creator share | 70% of Robux spent in your game. | [Economics docs](https://create.roblox.com/docs/production/monetization/economics) |
| Cash-out (DevEx) | $0.0038 per Earned Robux, minimum 30,000. Since 8 Jun 2026, $0.0054 (42% more) for purchases by US players verified 18+ in eligible games. | [DevEx docs](https://create.roblox.com/docs/production/monetization/developer-exchange), [Roblox newsroom](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42) |
| Creator Rewards | 5 R$ a day per Active Spender ($9.99+ in 60 days) who plays your game 10+ minutes, first three games of their day only. Plus 35% of the first $100 a new or lapsed player spends in 60 days if they came by your link or search and you average 100 DAU. Held 60 days. | [DevForum](https://devforum.roblox.com/t/introducing-creator-rewards-earn-more-by-growing-the-community/3777628) |
| Regional prices and Managed Pricing | Regional prices sit between 30% and 100% of list. Since 15 Jun 2026 new games and items are enrolled by default. | [Managed Pricing docs](https://create.roblox.com/docs/production/monetization/managed-pricing), [DevForum](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738) |

Our arithmetic: 1,000 R$ spent in your game becomes 700 Earned Robux and $2.66 ($3.78 at the 18+ US rate). A 299 R$ pass pays you about $0.80, and at the 30% floor a player can see it as about 90 R$.

### What the top games sell as passes

The repo's snapshot ([data/ANALYSIS.md](../data/ANALYSIS.md), section 8) lists every pass of the 1,430 charted games it fetched in full: 16,831 passes [data, Nov 2026].

| Measure | Value |
|---|---|
| Passes on sale, top 100 by players | median 5 (middle half 2 to 10); 17% sell none |
| Cheapest / middle / dearest pass of the median top-100 game | 99 / 249 / 699 R$ (top 300: 79 / 199 / 550) |
| The nine most common prices | 99, 199, 299, 399, 149, 499, 249, 49, 79: together 46% of all passes on sale (our arithmetic) |
| Price endings | 73% end in 9, 18% in 0 |
| Passes at 800 R$ or more | 9% |

The usual pass menu, matched on the pass name [data, Nov 2026]:

| Pass | Share of games selling one | Median price (R$) |
|---|---|---|
| 2x, x2 or double | 50% | 199 |
| VIP | 44% | 299 (Simulation 249) |
| Currency (money, cash, coins) | 31% | 199 |
| Pack or bundle | 26% | 249 |
| Speed | 24% | 129 (obbies 39) |
| Slots, storage, capacity | 18% | 179 |
| Auto-collect | 15% | 149 |
| Luck | 14% | 249 |
| Starter | 12% | 64 (Simulation 49) |
| Admin commands | 8% | 499 (obbies 599) |
| Revive | 2% | 299 |

In 21 hand-checked top games (Roblox public API, 25 Nov 2026, [endpoint](https://apis.roblox.com/game-passes/v1/universes/7709344486/game-passes?passView=Full&pageSize=100)): cheapest 35 R$ ([Brookhaven](../teardowns/brookhaven.md) Vehicle Upgrade), dearest 7,999 R$ ([Steal a Brainrot](../teardowns/steal-a-brainrot.md) Admin Commands); 2x currency up to 450 ([Blox Fruits](../teardowns/blox-fruits.md)); luck ladders 149 / 299 / 599 (Build the Pyramid!) and 275 / 800 ([Pet Simulator 99](../teardowns/pet-simulator-99.md)).

Price bands by genre (the range found, not a rule):

| Genre | What is sold, R$ | Source |
|---|---|---|
| Trend games | 2 or 3 passes, 99 to 467 (2x money, 2x speed, VIP); one vanity item at 7,999 | [slop/01-anatomy.md](../slop/01-anatomy.md) |
| Battlegrounds | Cosmetics 99 to 199, early-access character 245 to 345, private server 399 to 499, VIP 299 to 799. None sells damage. | [TSB passes](https://apis.roblox.com/game-passes/v1/universes/3808081382/game-passes?passView=Full&pageSize=100) |
| Tower defense | Luck potions 99 and 199, VIP about 300, 3x speed 389 to 799, Shiny Hunter 499 to 1,299, early-unlock towers 225 to 1,949 | [Anime Vanguards store](https://animevanguards.fandom.com/wiki/Store), [TDS passes](https://apis.roblox.com/game-passes/v1/universes/1176784616/game-passes?passView=Full&pageSize=100) |
| Roleplay | Vehicles, plots, VIP, music: Brookhaven 35 to 749 (18 passes), [Adopt Me](../teardowns/adopt-me.md) 285 to 795 | [Brookhaven passes](https://apis.roblox.com/game-passes/v1/universes/1686885941/game-passes?passView=Full&pageSize=100) |
| Dress-up | VIP 599 to 799, or 199 to 299 a month; theme pick 19 to 75; extra time 19 to 79 | [DTI products](https://apis.roblox.com/developer-products/v2/universes/5203828273/developerproducts?limit=100) |
| Survival | Utility 95 to 199, class 249 to 499, weapon or vehicle 599 to 699, elite packs 1,000 to 1,989 | [Survival Game passes](https://apis.roblox.com/game-passes/v1/universes/3989768869/game-passes?passView=Full&pageSize=50) |
| Hangouts | Tools 9 to 2,500; PLS DONATE booth skins to 42,000, ad plans to 2,100,000 | [PLS DONATE products](https://apis.roblox.com/developer-products/v2/universes/3317679266/developerproducts?limit=100) |
| Driving | Cosmetics under 300, 2x money 499 to 500, VIP 199 to 1,000, car packs 400 to 5,000 | [Driving Empire passes](https://apis.roblox.com/game-passes/v1/universes/1202096104/game-passes?passView=Full&pageSize=100) |

**Our read:** the newest hits sell the fewest passes. [Steal An Egg](../teardowns/steal-an-egg.md) sells 2 passes and 130 developer products, [Throw Food For Animals](../teardowns/throw-food-for-animals.md) 2 and 50 [data, Nov 2026]. In a 2026 hit the money moves through products bought again.

### Products that are bought again

| Product | Game | R$ | Sells |
|---|---|---|---|
| Revive on the death screen | [Doors](../teardowns/doors.md) | 40; 5 for 145, 10 for 239, 25 for 479 | The run. Our arithmetic: 29, 24, 19 each. Window 5 min solo, 2 in a party ([wiki](https://doors-game.fandom.com/wiki/Revives)). |
| Revive | [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) | 45 one player, 200 the team | The run. Search snippet of [PC Gamer](https://www.pcgamer.com/games/survival-crafting/roblox-99-nights-in-the-forest-revive), not read in full. |
| Revive | A Dusty Trip | about 39 | Community-cited ([fan wiki](https://a-dusty-trip.pages.dev/)) |
| Revive, extra time | [Dress to Impress](../teardowns/dress-to-impress.md) | revive 79 (149 in elimination mode), +60 s 79 | Another round, more time ([products API](https://apis.roblox.com/developer-products/v2/universes/5203828273/developerproducts?limit=100)) |
| Extra time, theme pick | Slay or Nay | +1 minute for everyone 19, theme 19 | Control of the round ([games API](https://games.roblox.com/v1/games?universeIds=10772471673)) |
| Paid restock | Grow a Garden | 79 (or watch ads) | Skipping a 5-minute wait ([wiki](https://growagarden.fandom.com/wiki/Seed_Shop)) |
| Single steal | Grow a Garden | 37 per crop; can fail | A shot at a neighbour's crop ([wiki](https://growagarden.fandom.com/wiki/Stealing)) |
| Seed bought direct | Grow a Garden | 7 up to 1,700 | Skipping the restock lottery |
| Instant hatch, grow all | Steal An Egg | about 9 per egg; about 160 | Timers, per a secondary source ([StudioKrew](https://studiokrew.com/blog/?p=2016)) |
| Grow all, row clear | Plants vs Brainrots | 179; 45 | Timers, space ([wiki](https://plantsvsbrainrots.fandom.com/wiki/Mechanics)) |
| 2x EXP | Blox Fruits | 25 for 15 min, 99 for 1 h, 450 for 6 h, 1,499 for 24 h | Time. Our arithmetic: 100, 99, 75 and 62 R$ per hour ([wiki](https://blox-fruits.fandom.com/wiki/Experience)) |
| Race reroll | Blox Fruits | 90 | A new starting trait |
| Spins | Blade Ball; Combat Warriors; [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md) | 99, 5 for 399, 10 for 749; daily spin 49; emote spin 25 or 50 kills | Rolls. Blade Ball falls from 99 to 75 each in the 10-pack. |
| Raid refill | Toilet Tower Defense | 99 for 3 runs | Skipping a 6-hour cooldown ([wiki](https://toilet-tower-defense.fandom.com/wiki/Raids)) |
| Class level skip | 99 Nights | 250, 400 | A counter grind ([wiki](https://99-nights-in-the-forest.fandom.com/wiki/Classes)) |
| Weather Machine | Natural Disaster Survival | 75 or 85 per use (wikis disagree) | A disaster added to the round |
| Build limit | Brookhaven | +10 props for 100 | Space |

Currency packs: our arithmetic on 14 pack ladders in the genre notes ([Dress to Impress](https://apis.roblox.com/developer-products/v2/universes/5203828273/developerproducts?limit=100), [Rivals](https://bloxguidesgg.com/games/rivals), [99 Nights](https://99-nights-in-the-forest.fandom.com/wiki/Diamonds), [Dead Rails](https://deadrails.fandom.com/wiki/Bonds), [Epic Minigames](https://typical-games.fandom.com/wiki/Epic_Minigames), Doors, Royale High and seven more) shows the largest pack giving 0% (Lumber Tycoon 2) to about 360% (Dead Rails) more currency per Robux than the smallest. The median is about 50% more.

**Products across the charts.** Developer product lists and prices are public through Roblox's developer-products endpoint, without login. The snapshot holds 105,745 of them [data, Nov 2026]. The median top-100 game lists 57 products on sale against 5 passes. Its cheapest product costs 10 R$; 60% of the top 100 sell one at 10 R$ or less and 91% one at 25 R$ or less. Matched on the product name, 1,430 games:

| Product | Share of games selling one | Median price (R$) | By genre (median R$) |
|---|---|---|---|
| Coins, cash, gems | 71% | 199 (top tenth 1,700+) | Simulation 149, Action 299 |
| Pack or bundle | 65% | 399 | Simulation 249, Action 699 |
| Boost, 2x, potion | 60% | 93 | Simulation 69 |
| Starter or beginner offer | 47% | 49 | Simulation 49, Action 99 |
| Crate, egg, chest | 44% | 249 | Simulation 249 |
| Skip | 40% | 99 | Simulation 89, Action 149, obbies 19 |
| Revive, respawn | 25% | 45 | Simulation 19, Survival 65, Action 49 |
| Spin, wheel | 24% | 149 | Survival 99 |
| Restock | 22% | 75 | Simulation 49, Survival 49, Action 54 |
| Donate, tip | 15% | 500 (top tenth 25,000+) | |

**Our read:** revive and restock are sold as consumables, almost never as passes: 25% of games sell a revive product, 2% a revive pass. A product under 25 R$ is standard in the top 100 and works as the first purchase.

### How many players pay, and how much

| Fact | Value | Source |
|---|---|---|
| Players who paid anything in a year | 3.80% (4.2% two years earlier) | GameAnalytics, 500+ games with 1M+ monthly players, Aug 2025 to Jul 2026, via a [secondary write-up](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox). Vendor data. |
| Yearly spend per payer | median $0.81, top 10% $8.88, top 1% $86.36 | Same |
| ARPPU per game | median $0.70, top 1% $55.31 | Same |
| Revenue from the top 15% of payers | about 50% | [Roblox analytics docs](https://create.roblox.com/docs/production/analytics/get-started). Vendor data. |
| Monthly payers, platform | 30M in Q3 2026, down 16%; spend per payer up 5% | [GamesBeat](https://gamesbeat.com/roblox-grows-revenues-in-q3-by-16-but-stock-falls-in-after-hours-trading/), secondary |

Our arithmetic: the top-1% payer spends about 107 times the median payer. Design for 96 players in 100 never paying.

Lifts Roblox reports for its own tools. All vendor data, no outside check:

| Tool | Reported result | Source |
|---|---|---|
| Regional pricing | +4% to +10% Robux spend; +43% to +52% pass purchases in discounted regions | [DevForum](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738) |
| Price optimisation | +4% average earnings; Slap Battles over +15% | same |
| Experiments | About 1 in 4 of 1,000+ tests lifted playtime, average +5%. Build a Crazy Tower +50% payer conversion from a difficulty change. A free item at the end of an obby level: +12.5% playtime, +5.3% D1, revenue unchanged. | [DevForum](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276) |

Roblox's recommendations count **spend days per user** and **Robux spent per user** ([DevForum, 15 Jun 2026](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)). **Our read:** a 25 R$ product bought on five days counts five spend days; one 999 R$ purchase counts one.

### What sells: relief of a named pain

| Pain | Examples, R$ |
|---|---|
| Time | Grow a Garden restock 79; [Sol's RNG](../teardowns/sols-rng.md) Quick Roll 100 cuts a roll from about 3.2 s to 1.2 s ([wiki](https://sol-rng.fandom.com/wiki/Rolling)); Skip Spins 49 to 99; 3x game speed 389 to 799; Pet Simulator 99 Auto Farm 175 |
| Loss | Revives 39 to 45; Field Trip Z "Save Items After Death" 300; Escape Tsunami Rainbow Shield 295, Anti-Wave Device 699 |
| Status | VIP tags 240 to 799; [Murder Mystery 2](../teardowns/murder-mystery-2.md) Elite 499; Chained chain skins 69 to 699 (the chain is in every clip); Rate My Avatar 2 booths 899 and 2,500; Admin Commands 7,999 |
| Convenience | Sell Anywhere 315 to 399 ([Fisch](../teardowns/fisch.md) 399); [Jailbreak](../teardowns/jailbreak.md) Pro Garage 450; storage 19 to 679 |
| Control (smaller) | Theme pick 19 to 75; Natural Disaster Survival round control 300; [Epic Minigames](../teardowns/epic-minigames.md) private-server powers 899 |

What leaders chose not to sell: battlegrounds sell no damage; Fisch sells no luck; Fish It! sells Robux rods weaker than its free quest rods ([Bloxodes](https://bloxodes.com/wiki/fish-it/rods)). Royale High retired its 2x and 4x diamond passes (749 and 1,649 R$) and gave owners a halo, a badge and diamonds worth more than they paid ([wiki](https://royale-high.fandom.com/wiki/Diamonds)).

## The rules

1. **Price from net.** A 299 R$ pass pays $0.80 and may show as 90. Leave Managed Pricing on; its only measured results are positive, though vendor-reported.
2. **Launch with about 5 or 6 passes.** The median top-100 game sells 5, the top-300 game 6; the two biggest late-2026 hits sell 2. **Our read:** every pass is one more decision on the shop screen. Put the variety in products, where the median top-100 game has 57.
3. **Centre the shelf on 199 to 299, prices ending in 9.** The median top-100 game's middle pass is 249 and 73% of pass prices end in 9. Cheapest near 49 to 99, dearest gameplay item near 1,200 to 1,500.
4. **Sell relief of a pain the player felt in the last five minutes.** Every product above sells time, loss, status, convenience or control. **Our read:** a product that creates its own pain (a timer lengthened to sell the skip) is what reviewers attack.
5. **Keep repeat products at 19 to 99, and sell one under 25.** Revives (median 45 R$), restocks (75), skips (99) and boosts (93) sit there across 1,430 games, and 91% of the top 100 have a product at 25 R$ or less. **Our read:** that fits a small balance and adds spend days.
6. **Top currency pack: about 1.5 times the value per Robux of the smallest.** The median of 14 ladders.
7. **Keep the best power earnable in any game with PvP.** Steal a Brainrot, which sells admin powers and top items, is the game criticised for it ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot)).
8. **Random paid items follow Roblox's odds rules.** See [15-the-line.md](15-the-line.md) and [07-rarity-and-collection.md](07-rarity-and-collection.md).

## When to ask

| Rule | Sourced or our read |
|---|---|
| No purchase prompt in the first five minutes. | **Our read.** Roblox scores leaving in under 60 s and in 61 to 180 s as negative signals ([Discovery docs](https://create.roblox.com/docs/en-us/production/promotion/discovery)). No source names a minute for offers. |
| Offer at the moment of need: the timer being watched, the round being dressed for, the run that just ended. | **Sourced as practice:** Grow a Garden sells the restock at the shop; Dress to Impress offers a 75 R$ theme prop each round, and sells Accessory Adjustment for 399 or free after 30 rounds ([guide](https://rblxguide.com/games/dress-to-impress/updates/themes-guide)). That this raises conversion is **our read**; no measured comparison was found. |
| Show the free path beside the paid one. | **Sourced as practice:** Grow a Garden's free restock clock; TSB's 25 R$ or 50 kills; Tower Defense Simulator sells a tower for coins, a level, or Robux. |
| Never ask after a loss caused by another player. | **Our read**, as in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md). |
| A revive on a death screen is the common exception. | **Sourced:** Doors shows a 40 R$ revive there. **Our read:** one offer, a No button the same size, no countdown shorter than the real window, and a free route in the game (Dead Rails' Doctor class gets three free revives per run, [wiki](https://deadrails.fandom.com/wiki/Classes)). |
| A charge only on a press meant to buy. | **Sourced:** the FTC's $245M Epic finding ([FTC](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations)). Dress to Impress changed its theme prop from an automatic purchase to an optional one on 29 Feb 2024. |

## Start with

Worked from the tables above. Tune with Experiments, at least 14 days per test.

| Slot | Start with (R$) | Worked from |
|---|---|---|
| Passes at launch | 4 to 6 | top-100 median 5; trend hits 2 to 3 |
| Entry product | 9 to 25 | 91% of the top 100 sell one at 25 or less; median cheapest 10 |
| Starter offer | 49 | product median 49 in 47% of games |
| 2x core resource pass | 199 | median of 720 games; range found 99 to 450 |
| VIP | 299 (dress-up 599 to 799) | median of 624 games |
| Luck or speed ladder | 149 / 299 / 599 | each step about 2x; luck pass median 249 |
| Revive | 45 (19 in a sim, 65 in survival); 5 for about 145 | product medians; Doors |
| Restock or skip | 49 to 99 | restock median 75 (sims 49), skip 99 |
| Timed boost | 25 for 15 min, 99 for 1 h | Blox Fruits |
| Currency packs | 5 tiers, 49 to about 2,000; top tier 1.5x per Robux | median of 14 ladders |
| Top gameplay item | 1,199 to 1,499 | Build the Pyramid!, Pet Simulator 99 Magic Eggs 1,200, Shiny Hunter 1,299 |
| Vanity item | 7,999, only once there is a crowd to see it | Steal a Brainrot, Tower Defense Simulator |
| Monthly VIP | 199 to 299 | Dress to Impress 299, Jailbreak 239 |

## What backfires

| Case | What happened | Source |
|---|---|---|
| Steal a Brainrot | Polygon wrote it became the biggest game "by making kids miserable" and criticised Robux-only top items and buyable admin powers. | [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/), [Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot) |
| Grow a Garden | Co-owner criticised for excessive monetisation. | [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden) |
| Trend clones | PEAK's studio told players to pirate its game rather than play a "microtransaction-riddled" copy. | [inkl](https://www.inkl.com/news/indie-creators-speak-out-pirate-our-game-over-playing-microtransaction-riddled-clones) |
| Makeup Mania! | About 65K players in October 2026, 89 six weeks later. Shop: VIP, slots, coins, theme and time; no ladder, no season pass. Cause not confirmed. | [RoWatcher](https://rowatcher.com/games/10768023539), [games API](https://games.roblox.com/v1/games?universeIds=10768023539) |
| Residence Massacre | Auto-moderated as "Scamming" in Aug 2026; over 30M Robux barred from cash-out. The developer suspects a reward for joining a community server, plus free crates. Unconfirmed by Roblox. | [DevForum](https://devforum.roblox.com/t/game-with-nearly-200m-visits-banned-for-scamming/4776239) |

## Policy in three lines

Paid random items need numeric odds before purchase, live odds under boosts, a benefit in every outcome and a PolicyService block for restricted players. Notifications may not use false time pressure or trick players into buying. The rest, with dates, is on [15-the-line.md](15-the-line.md).

## How to do it

1. List every pain the loop creates, with its number (wait in seconds, loss in units, walk in studs) in [kit/templates/economy-sheet.md](../kit/templates/economy-sheet.md).
2. Write one product or pass per pain, and its free path.
3. Price from the Start with table. Check the game still pays back with no purchase using `python tools/pacing.py` ([06-progression-and-economy.md](06-progression-and-economy.md)).
4. Write each offer's screen and second. Strike any in the first five minutes or after a theft.
5. Ship with Managed Pricing on and the refund webhook connected, so refunded items are taken back ([DevForum](https://devforum.roblox.com/t/new-transaction-refunded-webhook-notifies-when-a-purchase-is-cancelled/4890339)).
6. After two weeks compare conversion, ARPPU and ARPDAU with the dashboard's similar-experience ranges ([14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md)). Test one price at a time.

## Checks

- [ ] 4 to 8 passes on sale at launch.
- [ ] At least one product at 25 R$ or less (91% of the top 100 [data, Nov 2026]).
- [ ] Each product names its pain in one line.
- [ ] Each timed or random product shows its free path on the same screen.
- [ ] No prompt in the first 5 minutes of a first session.
- [ ] No prompt within 10 seconds of a theft or PvP loss.
- [ ] Buy and No buttons the same size.
- [ ] Top currency pack gives 1.2 to 2 times the value per Robux of the smallest.
- [ ] No rebirth removes a paid item.
- [ ] Every paid random item passes [15-the-line.md](15-the-line.md).

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Players, no revenue | Nothing under 25 R$; nothing tied to a pain | One 9 to 25 R$ product at the most-watched timer |
| Few payers, D7 falling | Power sold; free players outclassed | Make the best power earnable; sell speed and looks |
| Many passes, few buyers | 15+ passes at launch | Cut to 6; move the rest to products |
| "Pay to win" reviews | Top items Robux-only | A grind path for every Robux item |
| Bounce up after a shop change | Prompt in the first minutes | First offer after minute 5 |
| Big pack never sells | Same value per Robux as the small one | Top pack about 1.5x per Robux |

## Sources

Roblox Creator Docs and DevForum posts linked in each table; prices from the Roblox public API, 25 Nov 2026, and the fan wikis linked per row; payer data from [GameAnalytics via GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) and [GamesBeat](https://gamesbeat.com/roblox-grows-revenues-in-q3-by-16-but-stock-falls-in-after-hours-trading/); criticism from [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/), [Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot) and [inkl](https://www.inkl.com/news/indie-creators-speak-out-pirate-our-game-over-playing-microtransaction-riddled-clones); the Epic case from the [FTC](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations).
