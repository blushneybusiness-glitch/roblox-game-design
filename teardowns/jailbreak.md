# Jailbreak

> Escape prison, rob banks and stores, and outrun the police, or play the police and cash in criminals' bounties. It is the longest-running open-world cops-and-robbers game on Roblox, with 8.1 billion visits.

| | |
|---|---|
| Studio | Badimo |
| Released | Place made 6 Jan 2017 (Roblox public API); public release 21 Apr 2017 ([Wikipedia](https://en.wikipedia.org/wiki/Jailbreak_(Roblox))) |
| Genre | Open-world cops and robbers; see [genres/driving.md](../genres/driving.md) |
| Peak concurrent players | Not known |
| Players now | 4,843 (Roblox public API, 25 Nov 2026) |
| Players per server | 30 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Visits 8,098,905,883; votes 87.7% up (Roblox public API, 25 Nov 2026). Wikipedia records over $1M revenue in its first year. No dated peak was found. On the same day, Emergency Hamburg (made 2021, 50 per server) had 14,062 players, almost three times as many.

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Escape (first time only) | Uses one of seven routes out of prison | not known | Prison walls, police | Team changes to Criminal |
| Rob | Robs a store or heist | 10 (Gas Station) to about 600 (Tomb) | Duffel bag fills | Bag cash |
| Get away | Drives off | not known | Bounty rises | Bounty +$250 to +$2,400 |
| Bank or lose it | Reaches safety, or is arrested | Arrest: 10 handcuffed, about 5 in a cell | Items stripped on arrest | Cash, or the officer gains the bounty |
| Spend | Buys a vehicle | not known | New vehicle in the garage | Cash |

Every robbery can be open at once (the "Capless" system), and each closes for about 4 to 8 minutes after it is robbed ([Robberies & Heists](https://jailbreak.fandom.com/wiki/Robberies_%26_Heists)). **Our read:** dead time is the drive between robberies, not a wait. A player always has another open target.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Joins as a Prisoner with $3,000 ([Cash](https://jailbreak.fandom.com/wiki/Cash)) and picks Prisoner or Police ([Teams](https://jailbreak.fandom.com/wiki/Teams)) |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | Escapes. Routes include C4 from a donut, a sewer hatch, punching a power box 10 times, a vent with set opening hours, pickpocketing a keycard ([Escaping](https://jailbreak.fandom.com/wiki/Escaping)). Timings not known. |
| 5:00 to 15:00 | First robberies; four free vehicles (Comet, Helicopter, Cruiser boat, Jeep) can now be spawned ([Vehicles](https://jailbreak.fandom.com/wiki/Vehicles)) |

First purchase: the Pickup at $9,000, "commonly bought by newer players" ([Pickup](https://jailbreak.fandom.com/wiki/Pickup)). First contact with another player, first rare moment: not known. How anything is taught: not known; no beginner's guide page was found. **Our read:** none of the seven routes needs money, so the first escape is a skill check, not a purchase.

## 3. Progression

Robberies (wiki pages linked from [Robberies & Heists](https://jailbreak.fandom.com/wiki/Robberies_%26_Heists); public-server values). Per minute is our arithmetic: top payout divided by rob time plus closed time.

| Robbery | Payout | Rob | Closed | Bounty | Per minute |
|---|---|---|---|---|---|
| Rising City Bank | $75 to $9,000 | about 5 min | about 5 min | $1,500 | $900 |
| Jewelry Store | $500 to $6,600 | about 5 min | about 5 min | $1,000 | $660 |
| Museum (2 players) | $700 per kg, bag 5 kg (10 with pass), up to $8,400 | about 4 min | about 4 min | $1,250 | $1,050 |
| Crown Jewel | $750 to $9,600 | 3.5 min | about 6 min | up to $2,400 | $1,011 |
| Oil Rig | $45 to $9,600 | 5 min | 7 min | $1,750 | $800 |
| Cargo Train | $250 to $4,800 | 2 min | 6 min | $800 | $600 |
| Tomb (2 players) | $7,000 | 9 to 10 min | 5 to 6 min | $1,500 | $467 |
| Mansion | $13,000 | boss fight | open 6 PM to 4 AM in-game | $2,000 assist | not known |
| Donut Shop, Gas Station, Grocery | $750 ($1,500 with Bigger Duffel) | Gas Station about 10 s | Donut about 5 min | $250 | about $150 per store |

Private servers wait longer and pay about a tenth. Paychecks are gone: criminal paychecks went in Fall 2023, police paychecks ($1,200 base) on 24 Oct 2025 ([Daily Paycheck](https://jailbreak.fandom.com/wiki/Daily_Paycheck)). All income now comes from playing.

Vehicle ladder and time to reach it (our arithmetic, at $500 to $1,000 per minute of heists, travel not counted):

| Vehicle | Price | Step | Time from $3,000 start |
|---|---|---|---|
| Pickup | $9,000 | 3x the start | about 15 min of small stores, or 6 to 12 min of heists |
| Jet Ski | $50,000 | 5.6x | about 50 to 100 min |
| Volt Bike | $1,000,000 | 20x | about 17 to 33 hours |
| Concept | $2,500,000 ([Earnaldo, promotional](https://earnaldo.com/blog/jailbreak-free-robux-guide)) | 2.5x | about 40 to 80 hours |

Bounty: capped at $15,000 (Season 18), raised to $20,000 (Dec 2023) and $25,000 (13 Jun 2026). Above $3,500 an arrested criminal goes to the Maximum Security Prison. Bounties no longer reset on death ([Bounty](https://jailbreak.fandom.com/wiki/Bounty), [Arrest](https://jailbreak.fandom.com/wiki/Arrest)). Our arithmetic: a bank, a jewelry store and a museum add $3,750, so three robberies put a criminal over the line; the $25,000 cap is about 17 bank robberies.

## 4. Session and return hooks

- Robbery reopen timers of about 4 to 8 minutes.
- VIP: $1,000 a day and one tier-two safe a day.
- Codes in the description: "takeback" for $20,000 cash during The TakeBack (Roblox public API, 25 Nov 2026).
- Events in the last 12 months ([Bloxodes](https://bloxodes.com/events/jailbreak), [AllThingsHow](https://allthings.how/jailbreak-the-epic-update/)), in days: Winter Update 14, Forcefield 5, Season 31 11, anniversary Chapter 4 21, Season 33 60, The Hunt 12, The TakeBack 6. No fixed schedule.
- Seasons, now removed ([Seasons](https://jailbreak.fandom.com/wiki/Seasons)): 80 XP daily cap (120 with the pass), weekly contracts, a reward at levels 2 to 10, a grand-prize vehicle at level 10, Season Pass 299 R$, double XP in the last 5 days. Levels 2 to 10 could be bought with $56,000 cash. The page is marked removed on 29 Oct 2026, and a developer said seasons are paused after Season 33.

## 5. Other players

30 players split into Police and Prisoners; Criminal is reached only by escaping. Police collect bounties as cash and the criminal loses no cash; road spikes pay police 10% of the bounty. A criminal who resets or leaves hands the bounty to the nearest officer. The top 6 bounties are on a board. Team balance rule: not known.

Trading ([Trading](https://jailbreak.fandom.com/wiki/Trading)): only on Trading Island, added 10 Jun 2022. 60 seconds to accept (90 with Trading VIP), up to 8 items a side, two confirmations, lopsided trades declined automatically. Cash, free vehicles and pass items cannot be traded.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| VIP Lifetime | Pass | 750 | +20% cash (not safes), $1,000 a day, a safe a day, 10 garage slots |
| VIP Monthly | Subscription | 239 a month ([Earnaldo, promotional](https://earnaldo.com/blog/jailbreak-free-robux-guide)) | Not detailed |
| Pro Garage | Pass | 450 | Spawn any owned vehicle anywhere, shorter spawn timers |
| Crime Boss | Pass | 400 | not known |
| SWAT Team | Pass | 400 | not known |
| VIP Trading | Pass | 350 | Teleport to Trading Island, 90 s accept timer |
| Duffel Bag | Pass | 345 | The wiki's Bigger Duffel: small stores $750 to $1,500, Museum bag 5 to 10 kg |

Car Stereo (200 R$) is also sold. Prices: Roblox public API, 25 Nov 2026. The snapshot matches these 7 passes and lists 2 more off sale, XP Boost and Extra Storage [data, Nov 2026]. Best sellers: not known. **Our read:** VIP Lifetime costs about 3 months of VIP Monthly.

**Developer products [data, Nov 2026].** 66 are listed on sale, but 40 carry "(DISABLED)" in their names. 26 active remain, 1 to 15,000 R$, median 247.5 R$; 7 of them are gift copies of passes. 12 of 26:

| Product | R$ | Kind |
|---|---|---|
| 10,000 Cash | 95 | Cash ladder, smallest of 5 |
| 100,000 Cash | 940 | |
| 1 MILLION Cash | 8,250 | Largest |
| Season Pass | 299 | Season |
| Get Out Of Jailbreak Jail | 1,500 | Jail exit, by its name |
| THE NUKE | 15,000 | Top-priced item |
| Rocket Fuel [+50] | 30 | Fuel ladder |
| Rocket Fuel [+250] | 99 | |
| Spawn Airdrop | 99 | Spawns a drop |
| TIER 4 Duffel Bag | 150 | Bag tier (tiers 2, 3: 65, 90) |
| Rent Vehicle | 50 | Rental |
| Ad Reward (2x Cash) | 1 | Ad reward |

Our arithmetic: cash comes at 105 per R$ in the 10,000 pack and 121 in the 1,000,000 pack, 15% more; fuel at 0.6 R$ a unit in the 50 pack and 0.4 in the 250 pack. A disabled "250,000 Cash" at 8,000 R$ gave 31 cash per R$; the live one at 2,345 R$ gives 107, so cash costs about a third of what it did. What THE NUKE does: not known beyond its name.

## 7. Why it works

No developer interview was found. **Our read:**

- Every robbery is short (10 seconds to 10 minutes) and the next is already open, so there is always a target.
- The bounty makes success visible to the other team: the top 6 bounties are on a board, worth up to $25,000 each to police.
- The first car is 3 times the start cash, reachable in the first 15 minutes.

## 8. What went wrong

- The income throttle has been rewritten four times in about three years: Classic, Robbery Groups (Fall 2023, rotating every 8 minutes, removed after wide dissatisfaction), Dynamic (4 open at once), and now Capless.
- No new robbery was added for 910 days before the Grocery Store. The Crater City Bank was removed on 13 Jun 2026.
- 37 seasonal vehicles are listed as unobtainable.
- Seasons were dropped after Season 33 on 29 Oct 2026.
- Players now: 4,843 on 8.1B visits; peak not known, so the size of the fall is not known.

## 9. What to take from it

- First paid vehicle at 3x starting cash ($3,000 to $9,000), reachable in about 15 minutes.
- Robberies of 10 s to 10 min, each closed 4 to 8 min after, all open at once: about $500 to $1,000 per minute of cycle.
- Bounty that rises per robbery ($250 to $2,400), capped ($25,000), and pays the officer, not the victim.
- Two-player gates on the best robberies (Museum, Tomb).
- Trading fenced onto one island: 60 s timer, 8 items a side, no cash.
- Burst events of 4 to 21 days with a cash code in the description.
- A cash ladder of 5 packs from 95 to 8,250 R$, with only 15% more cash per R$ at the top [data, Nov 2026].

## Sources

- Roblox public API, 25 Nov 2026: [game](https://games.roblox.com/v1/games?universeIds=245662005), [passes](https://apis.roblox.com/game-passes/v1/universes/245662005/game-passes?passView=Full&pageSize=100), [votes](https://games.roblox.com/v1/games/votes?universeIds=245662005), [badges](https://badges.roblox.com/v1/universes/245662005/badges?limit=100)
- Jailbreak wiki: [Robberies & Heists](https://jailbreak.fandom.com/wiki/Robberies_%26_Heists), [Cash](https://jailbreak.fandom.com/wiki/Cash), [Bounty](https://jailbreak.fandom.com/wiki/Bounty), [Arrest](https://jailbreak.fandom.com/wiki/Arrest), [Teams](https://jailbreak.fandom.com/wiki/Teams), [Escaping](https://jailbreak.fandom.com/wiki/Escaping), [Vehicles](https://jailbreak.fandom.com/wiki/Vehicles), [Pickup](https://jailbreak.fandom.com/wiki/Pickup), [Seasons](https://jailbreak.fandom.com/wiki/Seasons), [Trading](https://jailbreak.fandom.com/wiki/Trading), [Daily Paycheck](https://jailbreak.fandom.com/wiki/Daily_Paycheck)
- [Bloxodes events](https://bloxodes.com/events/jailbreak), [AllThingsHow](https://allthings.how/jailbreak-the-epic-update/), [Wikipedia](https://en.wikipedia.org/wiki/Jailbreak_(Roblox)), [Earnaldo (promotional)](https://earnaldo.com/blog/jailbreak-free-robux-guide)
