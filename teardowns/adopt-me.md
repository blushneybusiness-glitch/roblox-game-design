# Adopt Me!

> You hatch pets, raise them by filling their needs, and trade them toward rarer and glowing versions; it is the longest-running pet game at the top of Roblox.

| | |
|---|---|
| Studio | Uplift Games (about 40 employees, estimated $60M a year, RoWatcher estimate) ([RoWatcher news](https://rowatcher.com/news/roleplay-games-rule-roblox-adopt-me-and-brookhaven-command-900k-players)) |
| Released | 14 Jul 2017 as a child-adoption game; turned to pets in 2019 (Roblox public API, 25 Nov 2026; [RoWatcher news](https://rowatcher.com/news/roleplay-games-rule-roblox-adopt-me-and-brookhaven-command-900k-players)) |
| Genre | Pet raising ([genres/pet-raising-and-animal.md](../genres/pet-raising-and-animal.md)) |
| Peak concurrent players | About 1.88M to 1.92M in April 2021 (Ocean Egg update); sources differ ([GameSpot](https://www.gamespot.com/articles/a-roblox-game-about-adopting-critters-just-set-a-new-concurrent-player-record/1100-6490282/), [RoWatcher](https://rowatcher.com/news/adopt-me-in-2026-sugarfest-500k-players-and-what-s-next)). A RoWatcher page dating 1.9M to April 2026 looks like a tracker error. |
| Players now | 179,781; 45.50B visits (Roblox public API, 25 Nov 2026). RoWatcher's 7-day average was 256K ([RoWatcher](https://rowatcher.com/games/383310974/adopt-me/dying)). |
| Players per server | 35 (Roblox public API, 25 Nov 2026) |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Need | Reads the need over the pet | not known | Need icon (Hungry, Sleepy, School...) | none |
| Fill | Goes to the place or item | not known | Pet eats, sleeps, bathes | none |
| Paid | Need completes | not known | Bucks counter rises | +10 to +20 Bucks, until 300 a day |
| Age | Task counts toward the next stage | not known | Stage name changes | +1 task |
| Hatch | Buys and hatches an egg | not known | New pet | -350 to -1,450 Bucks |
| Merge | 4 Full Grown copies at the Neon Cave | not known | Glowing Neon pet | 4 pets to 1 |

Sources: [wiki: Bucks](https://adoptme.fandom.com/wiki/Bucks), [wiki: Neon Pets](https://adoptme.fandom.com/wiki/Neon_Pets). Cycle time and dead time: not known. Our arithmetic: the 300-Bucks cap is 15 needs at 20 Bucks or 30 at 10.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | not known |
| 0:10 to 1:00 | not known. A free Starter Egg always hatches a Common ([Bloxodes](https://bloxodes.com/wiki/adopt-me/eggs)) |
| 1:00 to 5:00 | not known. A Common needs 3 tasks to go from Newborn to Junior ([wiki: Pets](https://adoptme.fandom.com/wiki/Pets)) |
| 5:00 to 15:00 | not known |

First reward, first purchase, first rare moment, first contact and first long goal: not known; no first-minute sequence was found.

## 3. Progression

**Earning** ([wiki: Bucks](https://adoptme.fandom.com/wiki/Bucks), [wiki: Task Board](https://adoptme.fandom.com/wiki/Task_Board)):

| Source | Bucks |
|---|---|
| Needs | 10 to 20 each; cap 300 per in-game day (500 with the paid Pet Handler Pro Certificate) |
| Jobs | up to 50 per in-game day |
| Daily login | 25, 50, 100, 200, 300, then repeat |
| Task Board | 25 + 25 + 25 + 100 bonus, each of the first three with an egg or gift prize |
| Money Tree | costs 1,450, pays 8 per 5 minutes, max 200 a day |
| x2 weekends | every few months: cap 600 (1,000), double ageing |

**Eggs** (snapshot Oct 2026, [allthings.how](https://allthings.how/adopt-me-every-egg-on-sale-right-now-with-prices-and-odds/), [Bloxodes](https://bloxodes.com/wiki/adopt-me/eggs)):

| Egg | Price | Legendary | Days of 300 cap (our arithmetic) |
|---|---|---|---|
| Cracked | 350 Bucks | 1.5% | 1.2 |
| Pet | 600 Bucks | 3% | 2.0 |
| Fairytale | 750 Bucks or 99 R$ for 4 | 3% | 2.5 |
| Royal | 1,450 Bucks | 8% | 4.8 |

**Ageing.** Six stages, Newborn to Full Grown; rarer pets need more tasks. Per-rarity totals are not verified: one fan guide gives Common 56 and Legendary 275, others disagree, and a June 2026 change reportedly eased ageing ([FindingDulcinea](https://www.findingdulcinea.com/adopt-me-pet-aging-chart/)). Minutes to age a pet: not known. An XP Potion (renamed from Age-Up Potion on 20 Nov 2026) adds 30 tasks; each Friendship Level on a Full Grown pet pays one ([wiki: XP Potion](https://adoptme.fandom.com/wiki/XP_Potion)).

**Neon ladder.** 4 Full Grown copies make 1 Neon; 4 Luminous Neons make 1 Mega Neon: 16 base pets ([wiki: Neon Pets](https://adoptme.fandom.com/wiki/Neon_Pets)). Neon stages run Reborn to Luminous.

## 4. Session and return hooks

- Daily: the Bucks cap resets each in-game day; 4 Task Board tasks; login cycle; 1 Star per login toward Star Rewards (Gemstone Egg at 28 stars).
- Offline: the Pet Pen (September 2025) ages four pets while away; one more slot is a 295 R$ pass ([RoWatcher](https://rowatcher.com/news/adopt-me-in-2026-sugarfest-500k-players-and-what-s-next)).
- Events: weekly chapters (Sugarfest, March 2026), a four-week Halloween with the Phantom Dragon, seasonal dragons (Rose Dragon, Fire Horse), a Homepass battle pass, "Admin Abuse" gift days on 5 Sep and 14 Nov 2026.
- Update weekday: not known. Last update 25 Nov 2026 (Roblox public API).

## 5. Other players

35 per server. Trading ([wiki: Trade System](https://adoptme.fandom.com/wiki/Trade_System), [wiki: Trade License](https://adoptme.fandom.com/wiki/Trade_License)):

| Rule | Value |
|---|---|
| Slots | 4, then 9 (Nov 2020), then 18 (May 2023) |
| Confirm | 5-second timer, restarts on any change; +15 s with an unfair-trade warning |
| Licence | Free; a 3-scenario safe-or-scam test; needed for Ultra-Rare and Legendary; 30 days of history; report button |
| Spectating | since Sep 2023 |
| Backpack viewing | since 14 Jan 2026, after Roblox's age-group chat limits |
| Trading Hub | since 31 Jul 2026; cross-server; 100 Bucks a listing; 2 listings, third for 49 R$; lister must be online |

Social tasks: the Task Board's 100-Bucks bonus needs a friend (play 10 minutes together, visit a friend's home for 60 seconds, host a party). Player stands and taxis set their own prices (0 to 20 Bucks). Nothing can be stolen. What gets clipped: not measured.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Millionaire Pack | pass | 795 | not described in notes |
| Cozy Home Lure | pass | 765 | paid lure (a free Box Lure exists) |
| VIP | pass | 480 | not described in notes |
| +1 Pet Pen Slot | pass | 295 | one more pet ages offline |
| Premium Plots | pass | 285 | not described in notes |
| Ride potion | not known | 150 per pet | makes a pet ridable for good |
| Taxi Driver Bundle | not known | 350 | taxi job |
| Pet Handler Pro Certificate | not known | not known | raises the daily cap from 300 to 500 |

Passes from Roblox public API, 25 Nov 2026, and they match the snapshot [data, Nov 2026]: 5 on sale, 20 off sale; their sum is 2,620 R$ (our arithmetic). Off-sale passes include three mansions, a griffin, a horse, a supercar pack and a glider. The last three rows are from [wiki: Bucks](https://adoptme.fandom.com/wiki/Bucks), [wiki: Neon Pets](https://adoptme.fandom.com/wiki/Neon_Pets), [wiki: Trade System](https://adoptme.fandom.com/wiki/Trade_System); none of them is among the products the snapshot read.

Products [data, Nov 2026]: the list stops at 300 rows, and 65 of those are on sale, 2 to 4,140 R$, median 169. Most Bucks packs come in two sizes at one price (45, 50 or 55 Bucks for 24 R$) and in "10% Discount" and "90% Discount" copies, which are left out below. 12 of 65:

| Product | R$ | Note |
|---|---|---|
| 50 Bucks | 24 | 2.08 Bucks per R$ |
| 200 / 600 / 1,400 / 3,000 Bucks | 85 / 240 / 550 / 1,175 | |
| 10,000 Bucks | 3,910 | 2.56 Bucks per R$: 23% more than 50 Bucks (our arithmetic) |
| 4x Fairytale Egg Bundle | 99 | Paid random pets |
| Instant Hatch | 35 | |
| Fly A Pet Potion | 255 | |
| +1 Trading Hub Listing | 49 | Third listing ([wiki: Trade System](https://adoptme.fandom.com/wiki/Trade_System)) |
| Double Daily Login Reward | 10 | |
| Apple Crumble Mega Neon Paint | 49 | One of 6 paints at 49 |

Millionaire Pack is sold both as a pass and as a product at 795. **Our read:** the Bucks ladder gives only 23% more per Robux at 163 times the price, so packs are priced for the Bucks a player is short of today. Homepass prices and best sellers: not known. No item gives power over another player.

## 7. Why it works

A Roblox developer blog on the update that took it past 400K concurrent exists but could not be read. Measured: monthly players doubled from 30M to 60M between January 2020 and January 2021 ([RoWatcher news](https://rowatcher.com/news/roleplay-games-rule-roblox-adopt-me-and-brookhaven-command-900k-players)). RoWatcher puts typical 2026 days at 430K to 465K.

**Our read:**
- The daily cap keeps Bucks scarce, so a 600-Bucks egg costs two days and a Legendary stays rare (about 67 capped days per expected Legendary from Pet Eggs).
- The 4-into-1 ladder turns duplicates into progress and makes a Mega Neon a visible 16-pet trophy.
- Trading gives every pet a price set by players, and the safety rules let children trade top items.
- Seasons sell one limited pet each, which feeds the trading economy.

## 8. What went wrong

Players now sit at roughly a quarter of the 2021 peak on a typical day (our arithmetic: 450K / 1.9M). Roblox's age-group chat limits forced trade changes in January 2026. Specific complaints and economy breaks: not found.

## 9. What to take from it

- A daily soft-currency cap of 15 to 30 needs (300 Bucks, 500 paid).
- Three egg tiers costing 1.2, 2 and 4.8 days of the cap, with Legendary at 1.5%, 3% and 8%.
- A 4-into-1 merge at two levels: 16 base pets per top pet.
- Trade safety: 5-second restart timer, unfair warning, a licence test for the top two rarities.
- A 5-day login cycle: 25, 50, 100, 200, 300.
- Offline ageing slots sold one at a time (295 R$).

## Sources

- Roblox public API (games, game passes), read 25 Nov 2026
- Adopt Me wiki: [Bucks](https://adoptme.fandom.com/wiki/Bucks), [Task Board](https://adoptme.fandom.com/wiki/Task_Board), [Pets](https://adoptme.fandom.com/wiki/Pets), [Neon Pets](https://adoptme.fandom.com/wiki/Neon_Pets), [XP Potion](https://adoptme.fandom.com/wiki/XP_Potion), [Trade System](https://adoptme.fandom.com/wiki/Trade_System), [Trade License](https://adoptme.fandom.com/wiki/Trade_License)
- [allthings.how eggs](https://allthings.how/adopt-me-every-egg-on-sale-right-now-with-prices-and-odds/), [Bloxodes eggs](https://bloxodes.com/wiki/adopt-me/eggs), [RoWatcher Adopt Me 2026](https://rowatcher.com/news/adopt-me-in-2026-sugarfest-500k-players-and-what-s-next), [RoWatcher tracker](https://rowatcher.com/games/383310974/adopt-me/dying), [RoWatcher news](https://rowatcher.com/news/roleplay-games-rule-roblox-adopt-me-and-brookhaven-command-900k-players), [GameSpot](https://www.gamespot.com/articles/a-roblox-game-about-adopting-critters-just-set-a-new-concurrent-player-record/1100-6490282/), [FindingDulcinea](https://www.findingdulcinea.com/adopt-me-pet-aging-chart/)
