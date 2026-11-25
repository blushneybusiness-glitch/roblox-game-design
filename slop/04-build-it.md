# Building one: the recipe

Ten steps, in the order to do them. Every table headed **Start with** holds starting values derived from the hits in [01-anatomy.md](01-anatomy.md). They are a first draft to tune with a stopwatch and then with live data. They are not facts about what works.

Before step 1, be honest about the bet. Read [05-after-the-peak.md](05-after-the-peak.md): most attempts fail, the window is short, and a game that works still loses most of its players within months.

## Step 1. One sentence: the hit you follow and the verb you change

Write: "It is **[live hit]**, but you **[new verb]** instead of **[its verb]**."

| Follower | The sentence |
|---|---|
| Steal An Egg | Steal a Brainrot, but you take eggs from animals in the wild and run them home, instead of buying from a conveyor |
| Break and Steal an Egg | Steal An Egg, but you break the eggs out with a pickaxe |
| Throw Food For Animals | Steal An Egg, but you throw food to attract the animal, instead of carrying an egg |
| Kick a Lucky Block | A lucky-block roller, but your kick sets off a tsunami you have to outrun |

Rules for the sentence:

- The new verb is something the player's body does in the world (throw, kick, ride, break, carry), not a system (craft, merge, level).
- The new verb makes a picture. If you cannot draw the thumbnail from the sentence, pick another verb.
- Everything else stays as the player already knows it: base, units that earn, rarities, rebirth. Players arrive knowing how those work. Do not make them learn two new things.
- Search Roblox for your sentence. If someone shipped it more than two weeks ago and it is growing, you are late for that one.

## Step 2. Choose the skeleton and the server size

| If the game is about | Skeleton | Players per server |
|---|---|---|
| Owning things others can take | A: buy, place, earn, protect | 6 to 8 |
| Growing things and showing them | A, with clocks in place of theft | 4 or 5 |
| Going out to get things and bringing them back | B: train, reach, carry home, earn | 5 to 7 |
| Racing other players up a number | B on a shared course | 20 or more |

## Step 3. Build the ladder from payback time

Do this in a spreadsheet before any code. For each unit choose its income per second and its payback in seconds. Price is the product.

**Start with:**

| # | Tier | Income per second | Payback (s) | Price | On offer |
|---|---|---|---|---|---|
| 1 | Common | 1 | 25 | 25 | always |
| 2 | Common | 3 | 60 | 180 | always |
| 3 | Common | 6 | 80 | 480 | always |
| 4 | Common | 12 | 95 | 1,140 | always |
| 5 | Rare | 25 | 105 | 2,625 | always |
| 6 | Rare | 60 | 115 | 6,900 | always |
| 7 | Epic | 150 | 125 | 18,750 | always |
| 8 | Epic | 400 | 140 | 56,000 | always |
| 9 | Legendary | 1,000 | 155 | 155,000 | once every 5 minutes |
| 10 | Legendary | 3,000 | 175 | 525,000 | once every 5 minutes |
| 11 | Mythic | 10,000 | 200 | 2,000,000 | once every 15 minutes |
| 12 | Mythic | 40,000 | 230 | 9,200,000 | once every 15 minutes |
| 13 | God | 150,000 | 260 | 39,000,000 | once every 45 minutes |
| 14 | God | 600,000 | 290 | 174,000,000 | once every 45 minutes |

The pattern: income multiplies by 2 to 4 per step, payback grows by 10% to 15% per step, and nothing passes 300 seconds.

**The last column does the pacing.** Price only holds a player back for the first quarter of an hour. After that, what they can buy is set by what the shop offers and how often, which is how Steal a Brainrot stretches a ladder across weeks (a Legendary within 5 minutes, a Mythic within 15, a Brainrot God within about 45). Without the stock clocks, this same ladder is finished in under half an hour.

Then set:

- **Starting cash:** enough for the first purchase and nothing more. Plants vs Brainrots gives $400, the price of two starter plants.
- **Slots:** 10 to start, as in Steal a Brainrot. The early game is filling them; the mid game is replacing what is in them.
- **Sell-back:** 50% of the price, so replacing a unit costs something.
- **Round the prices** to numbers a child can read: 25, 200, 500, 1.1K.

This ladder is the example file `tools/examples/start-with-ladder.json`. Run through `python tools/pacing.py`, with 10 slots and a first rebirth costing 2,000,000, an ideal player gets:

| Check | This ladder | The real Steal a Brainrot ladder, same tool |
|---|---|---|
| First purchase | 0:08 | 0:08 |
| Purchases in the first 5 minutes | 29 | 21 |
| Longest wait in the first 15 minutes | 25 seconds | 73 seconds |
| First rebirth | about 21 minutes | about 20 minutes |
| First Mythic | about 23 minutes | about 21 minutes |
| First unit of the top tier | about 45 minutes | about 45 minutes |

Real players are slower than the ideal one, so read these as the fastest possible times. Two things to take from the right-hand column: the hit gives a new player a purchase every 15 seconds for the first five minutes, and after the first half hour purchases arrive on the stock clock, one every 5 to 15 minutes. That later stretch is where theft, the trip home and events have to carry the session, which is why steps 6 and 10 are not optional.

For your own ladder, check three things in the tool's output: the first purchase lands in the first 15 seconds, the longest wait between two purchases in the first 15 minutes is under 90 seconds, and the ladder is not finished before 3 hours.

## Step 4. Add the second roll

**Start with:**

| Result | Chance | Multiplier | Looks like |
|---|---|---|---|
| Normal | 82% | x1 | plain |
| Gold | 11% | x1.5 | gold material |
| Diamond | 5% | x3 | glassy, blue |
| Ruby | 1.5% | x10 | red, glowing |
| Rainbow | 0.5% | x20 | cycling colour; announced to the server |

Averaged out, this makes units worth about 1.4 times their base income (0.82 + 0.11 x 1.5 + 0.05 x 3 + 0.015 x 10 + 0.005 x 20 = 1.385), so allow for that in step 3. Show the table in the game. If Robux can buy a roll or improve its odds, read [foundations/15-the-line.md](../foundations/15-the-line.md) before building it.

## Step 5. Set the clocks

**Start with:**

| Clock | What changes | On the HUD |
|---|---|---|
| 5 minutes | The main shop or conveyor stock. Units 1 to 8 always present; a Legendary guaranteed once per 5 minutes, a Mythic once per 15, a God once per 45. | Always |
| 30 minutes | A second, rarer stock (eggs, gear) | When within 5 minutes |
| 24 hours | Three daily offers for in-game currency | On join |
| 7 days | The Saturday event | Countdown from 48 hours out |

Offline: timers keep running; per-second income continues at 25% to 50%, counted for up to 8 hours away, so a night pays 2 to 4 hours of earnings.

## Step 6. Write the rules of loss

Pick one. Both work; they produce different games.

**Theft (Skeleton A).** Fill in this table and do not start building until every row has an answer:

| Rule | Start with |
|---|---|
| What can be taken | One placed unit per raid. Never cash, never anything bought with Robux. |
| The carry | On foot, in view, at 70% speed, for 8 to 15 seconds |
| The stop | Any hit drops the unit where the thief stands; the owner or anyone else can pick it up |
| The lock | 60 seconds of full protection, then 10 to 15 seconds before it can be used again |
| Lock growth | +10 seconds per rebirth |
| New-player grace | No raids on a player in their first 5 minutes |
| Offline | A base whose owner has left cannot be raided |
| The answer | The victim sees the thief's name and a marker on them for 30 seconds |

**The trip home (Skeleton B).**

| Rule | Start with |
|---|---|
| The trip | 10 to 30 seconds from pickup to base |
| The threat | One per zone, visible from the start of the trip, slightly slower than a player whose stat fits the zone |
| A hit | The prize drops; the player keeps everything else |
| The line | A marked edge of the base. Across it, the prize is banked |
| Other players | Can pick up a dropped prize. Cannot take a banked one, or can only through the theft rules above |

In both cases: nothing may open a Robux prompt at the moment of loss.

## Step 7. Design the rebirth

**Start with:**

| Rebirth | Cash | Named units required | Multiplier | Also gives |
|---|---|---|---|---|
| 1 | What a steady player has after 20 to 40 minutes (2,000,000 on the step 3 ladder) | Two specific units from tiers 5 and 6 | x1.5 | +10 s lock, tool 1 |
| 2 | x3 | Two from tiers 7 and 8 | x2 | +1 slot, a visible change to the base, tool 2 |
| 3 | x8 | Two from tiers 8 and 9 | x3 | +1 slot, tool 3 |
| 4 | x3 | Two from tiers 9 and 10 | x4 | +1 slot, tool 4 |
| 5 | x3 | Two from tiers 10 and 11 | x5 | +1 slot, a second visible change |

- A "tool" is a new way to act on other players or on the world: a slap, a grapple, a trap, a speed burst.
- Take only the cash and the named units. Leave the rest of the base.
- Show the next rebirth's requirements on the HUD as pictures of the two units, from the first minute. That is the long goal.

## Step 8. Script the first five minutes

Fill in [kit/templates/first-session-script.md](../kit/templates/first-session-script.md). **Start with** these gates:

| By | The player has |
|---|---|
| 0:00 | Spawned at their own base, facing the shop or conveyor, starting cash on screen |
| 0:10 | Bought unit 1 by walking to it and tapping once |
| 0:15 | Seen it arrive at their base and the cash counter move |
| 0:40 | Bought a second unit with money the first one earned |
| 1:30 | Seen an upgraded unit (gold or better) appear in the shop or in a neighbour's base |
| 2:00 | Four or more units; a pointer shows the lock or the first trip |
| 3:00 | Used the lock, or completed one trip home, with a result that cannot fail the first time |
| 5:00 | Seen the rebirth requirements; seen the richest base on the server |

No offers. No text boxes. No window that opens by itself.

## Step 9. Decide what is for sale

The hits sell very few passes and price them low (see [01-anatomy.md](01-anatomy.md)). Across the charts, the median top-100 game lists 5 passes and 57 products that can be bought again ([data/ANALYSIS.md](../data/ANALYSIS.md)). **Start with:**

| Product | Type | R$ | Note |
|---|---|---|---|
| x2 Cash | Pass | 99 to 299 | The one pass every hit has |
| x2 of the trained stat, or x2 growth speed | Pass | 149 to 467 | Skeleton B and grow games |
| VIP (a tag, a small bonus, a cosmetic) | Pass | 249 to 375 | |
| A first small product | Product | 10 to 25 | 91% of the top 100 games sell something at 25 R$ or less [data, Nov 2026] |
| Restock now, a reroll | Product | 49 to 79 | Median 75 R$ across the charts, 49 in simulators; Grow a Garden charges 79 |
| Luck for 10 minutes, a lucky block | Products | see the monetization page | Paid random items: read [foundations/15-the-line.md](../foundations/15-the-line.md) first |

Leave these out: anything that takes units from other players for Robux, anything that sells safety at the moment of loss, and any power that event attendance cannot also earn. See [foundations/12-monetization.md](../foundations/12-monetization.md) for prices and placement and [foundations/15-the-line.md](../foundations/15-the-line.md) for the rules on random items.

## Step 10. Build three Saturdays before you launch

For each of the first three weeks, have ready:

- One limited upgrade tier, slightly stronger than the last (x2, then x2.5, then x3).
- Five to ten new units at the top of the ladder.
- One event that happens to the whole server at a set hour, lasting 30 to 60 minutes.
- A countdown in the game from 48 hours before.

Use [kit/templates/update-plan.md](../kit/templates/update-plan.md).

## Order of work

**Our read**, sized for one to three people:

| Days | Build | Stop and check |
|---|---|---|
| 1 to 4 | The shop or conveyor, the base, units that earn, the ladder from step 3, grey boxes for everything | Is buying and watching the number rise something you want to keep doing for 10 minutes? If not, change the verb. Do not add systems to a loop that is not working. |
| 5 to 9 | The new verb from step 1, the loss rules, the second roll, the 5-minute clock | Hand a phone to someone who has never seen it. Say nothing. Time the gates in step 8. |
| 10 to 15 | Rebirth, sounds for every action, the visible base changes, passes, funnel events | Run the checklist in [03-quality-bar.md](03-quality-bar.md) |
| 16 to 21 | Three Saturdays of content, the countdown, phone performance | Launch |

Launch is where tuning starts. Steal An Egg was live for seven weeks before it broke out, and Throw Food For Animals took off with its first update, five weeks after it was created ([RoStats](https://rostats.io/records)). Plan to update weekly for at least six weeks and read the funnel every week ([foundations/14-metrics-and-diagnosis.md](../foundations/14-metrics-and-diagnosis.md)).

## When to stop

Write these down before launch and keep to them:

- If fewer than half of new players are still present at 5 minutes after two rounds of fixes to the first session, the verb is wrong. Go back to step 1.
- If the first five minutes hold but almost nobody returns the next day after two more updates, the game has no reason to come back. Add the clocks and offline growth before anything else.
- If six weekly updates have gone by with no growth, stop and take what you learned to the next one.

Next: [05-after-the-peak.md](05-after-the-peak.md).
