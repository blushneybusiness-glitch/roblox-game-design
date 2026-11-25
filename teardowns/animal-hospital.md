# Animal Hospital (Anomaly)

> Check in animal patients, test each one three ways, and shut out the ones that are not really animals, while the hospital fills with hazards. It was the anomaly-spotting hit of 2026 and won Best New Game, then fell to about 1% to 2% of its peak in under five months.

| | |
|---|---|
| Studio | Animal Anomaly (verified group) |
| Released | 10 May 2026, on PC, mobile and consoles |
| Genre | Anomaly-spotting horror with co-op survival ([genres/horror.md](../genres/horror.md)) |
| Peak concurrent players | Sources conflict: 736,948 on 5 July 2026 (Rolimons, quoted by [GosuGamers](https://www.gosugamers.net/entertainment/news/78741-animal-hospital-becomes-roblox-s-latest-horror-sensation-here-s-everything-you-need-to-know)) or 1.3M on 10 July 2026 ([RoWatcher](https://rowatcher.com/games/10148749921/animal-hospital-anomaly/dying)) |
| Players now | 14,042 (Roblox public API, 25 Nov 2026). 2.54 billion visits, 3.30 million favourites. RoWatcher: 7-day average 15K, 30-day average 20K, down 41.7% in 30 days |
| Players per server | 30 maximum per the API; parties of up to 4 per GosuGamers; solo is possible |
| Teardown date | 25 November 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Our arithmetic: 14,042 is 1.9% of the lower peak and 1.1% of the higher one.

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1 | Checks in a patient at reception | not known | An animal at the counter | none |
| 2 | Visual check at the counter | not known | Twitching, three eyes, a hollow face | none |
| 3 | Camera check on CCTV (after the first shift) | not known | A watcher, a skinwalker on screen | none |
| 4 | Photo check on a developed polaroid | Must finish developing, or a cursed photo costs 10 Sanity | Static, a mismatched photo | Sanity |
| 5 | Registers the patient or closes the shutters | not known | Shutters slam | Patient admitted or refused |
| 6 | Treats admitted patients: Basic Medical, X-Ray, Heart Monitor, Surgery | Surgery is timed and cannot be left once started | Treatment rooms | Patient saved or lost |
| 7 | Survives hazards that spawn whatever the desk decided | not known | Bed monster, stalker, slime, fire, a death ritual | Sanity |

Sources: [animal-hospital.wiki](https://animal-hospital.wiki/), [GosuGamers](https://www.gosugamers.net/entertainment/news/78741-animal-hospital-becomes-roblox-s-latest-horror-sensation-here-s-everything-you-need-to-know), [OP.GG](https://op.gg/roblox/wiki/animal-hospital). Shift length and patients per shift are not known.

The run fails when Sanity, which replaces health, reaches 0, or when three patients die. Each shift survived adds to a Total Shifts streak; a new game starts at day one. Sanity comes back with coffee, chocolate or class perks.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Lobby; form or join a party |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | not known. The first shift has reception and photo checks only; CCTV anomalies are locked |
| 5:00 to 15:00 | not known. After a shift, players return to the lobby for a new shift or a new party |

The first-minute tutorial sequence is not documented. The game teaches by adding checks: CCTV after shift 1, and after shift 10 a static photo no longer guarantees an anomaly ([spottheanomaly.wiki](https://spottheanomaly.wiki/animal-hospital-anomaly), [OP.GG](https://op.gg/roblox/wiki/animal-hospital)).

## 3. Progression

Anomalies by the check that reveals them ([spottheanomaly.wiki](https://spottheanomaly.wiki/animal-hospital-anomaly)):

| Check | Count | Counter |
|---|---|---|
| Reception | 8 | Shutters |
| CCTV (after shift 1) | 5 | Shutters |
| Photo | 4 | Shutters; a cursed photo must be spotted on the desk; the Stalker check-in must be photographed |
| Hazards inside | 14 | One each: walk around the bed monster, do not look at the stalker, extinguisher for slime and fire, coffee on every candle for the death ritual. Only Skinwalkers can be killed (taser, gun) |

Totals differ by source and update: 31, 23 or about 14. A wrongly admitted anomaly "awakens" later as a Skinwalker, tendrils after surgery, or ghosts after a failed save.

Two currencies: Cash per shift (Taser, Coffee, shop upgrades) and permanent Animal Coins for ten levelable Classes, from Intern to Secret Agent, each with Sanity, utility or starting-cash perks. Launch had five shifts and six classes ([animalhospital.blog](https://animalhospital.blog/release-date/)). Prices: not known.

## 4. Session and return hooks

A named update every 1 to 3 weeks in 2026, per a fan blog: Ambulance (12 Jun), two class updates (19 and 26 Jun), Hazmat Team (25 to 27 Jul), Dr. Harlow event and Rain Shift (8 to 11 Aug), Second Floor with Sewers and Laboratory (5 to 7 Sep), Halloween (17 Oct to 14 Nov), Thanksgiving (21 to 30 Nov). Double Animal Coin weekends on 19 to 21 Sep, 3 Oct and 31 Oct to 2 Nov ([animalhospital.blog](https://animalhospital.blog/release-date/)). Daily rewards: not known.

## 5. Other players

Co-op parties with ten classes that split the work (security, medicine, Sanity support). No trading or theft found. Loss is the run only. What gets clipped: not documented.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Secret Agent class | Product | 890 | Class; Robux-only since 19 June 2026 |
| Head Nurse class | Product | 190 | Marked Robux on a fan wiki |

The game-pass endpoint returned no passes on 25 Nov 2026 ([Roblox public API](https://apis.roblox.com/game-passes/v1/universes/10148749921/game-passes?passView=Full&pageSize=50)). Everything is sold as developer products. Class prices are from the snapshot [data, Nov 2026].

Products [data, Nov 2026]: 42 on sale, 7 to 1,590 R$, median 160. 12 of 42:

| Product | R$ | Note |
|---|---|---|
| Coins Small / Medium / Large / Huge | 99 / 380 / 890 / 1,590 | Coin amounts are not in the names, so coins per R$ is not known |
| Revive / Revive [2nd] | 45 / 70 | |
| Revive Friend / Revive All | 49 / 130 | |
| Refresh Shop | 19 | |
| Detect Skinwalker | 9 | |
| Starter Bundle | 99 | |
| Secret Agent | 890 | Class (table above) |

Also listed: six "Tier" products from 129 to 1,590 and three "Upgrade" products from 59 to 199, contents not known; seasonal skin packs at 199 to 499. **Our read:** with no passes, every purchase is per run or per item. The second revive in a run costs 56% more than the first (our arithmetic), and a 9 R$ hint at the core check (spotting the skinwalker) is the cheapest item in the game after a 7 R$ skin rental.

## 7. Why it works

Four awards at the 2026 Roblox Innovation Awards: Best New Game, People's Choice, Best Innovation in Creative Direction and The Builderman Award ([Roblox newsroom](https://about.roblox.com/newsroom/2026/09/2026-roblox-innovation-awards)). It was rated 95% with over 463M visits two months in, and is labelled Minimal: light blood, mild violence, occasional jump scares ([GosuGamers](https://www.gosugamers.net/entertainment/news/78741-animal-hospital-becomes-roblox-s-latest-horror-sensation-here-s-everything-you-need-to-know)). A fan wiki says it was inspired by Scary Shawarma Kiosk and Dandy's World.

**Our read:**
- The desk check feeds a second layer. A wrong call at the counter becomes a roaming hazard minutes later, so the player always does two things.
- One default counter (shutters) keeps a 30-player server readable on a phone; the exceptions are few enough to learn.
- New checks unlock with progress, and the trusted sign stops being trusted at shift 10.
- A Minimal label keeps every age group able to find it.

## 8. What went wrong

- From a July peak of 737K to 1.3M to 14K in about 4.5 months, while shipping an update every 1 to 3 weeks. **Our read:** a spike from clips and awards, without a long goal to hold players.
- Clones did not follow it up. Related games on one listing (player counts from [RoLearn](https://rolearn.dev/games-like/scary-shawarma-kiosk-the-anomaly/), date not shown, and the list is for Scary Shawarma Kiosk, not Animal Hospital): Bake or Die 2.5K, Dangerous Night 2.2K, Anomaly Cafe 1.3K, Scary Grocery: The Night Shift 472, Scary Meatball Stall 355, Night 67 204.
- The clones changed the setting and added one twist: a cafe, a cinema where shooting innocents has consequences, a hotel with a rule wall ([gaming.net](https://www.gaming.net/best-roblox-games-like-animal-hospital/)). **Our read:** most kept only the desk check.

## 9. What to take from it

- Three checks per arrival (look, camera, photo), with the second check unlocked after the first shift.
- One default counter for nearly every desk anomaly; 2 exceptions.
- A wrong call returns later as a roaming threat with its own single counter.
- Fail at Sanity 0 or 3 patient deaths; a streak counter for shifts survived.
- Break one trusted sign at a set point (shift 10).

## Sources

- [Roblox games API](https://games.roblox.com/v1/games?universeIds=10148749921), 25 Nov 2026
- [GosuGamers](https://www.gosugamers.net/entertainment/news/78741-animal-hospital-becomes-roblox-s-latest-horror-sensation-here-s-everything-you-need-to-know), [RoWatcher](https://rowatcher.com/games/10148749921/animal-hospital-anomaly/dying), [Roblox newsroom](https://about.roblox.com/newsroom/2026/09/2026-roblox-innovation-awards)
- [animal-hospital.wiki](https://animal-hospital.wiki/), [spottheanomaly.wiki](https://spottheanomaly.wiki/animal-hospital-anomaly), [OP.GG](https://op.gg/roblox/wiki/animal-hospital), [animalhospital.blog](https://animalhospital.blog/release-date/) (fan sources)
- [RoLearn](https://rolearn.dev/games-like/scary-shawarma-kiosk-the-anomaly/), [gaming.net](https://www.gaming.net/best-roblox-games-like-animal-hospital/)
