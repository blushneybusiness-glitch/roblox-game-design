# Dress to Impress

> Up to 13 players get a theme, dress for 6 minutes, walk a runway one at a time and rate each other from 1 to 5 stars. It made the timed fashion contest one of Roblox's largest formats of 2024, and every dress-up game of 2026 copies it.

| | |
|---|---|
| Studio | Dress To Impress Group ([Wikipedia](https://en.wikipedia.org/wiki/Dress_to_Impress_%28video_game%29)) |
| Released | 11 Nov 2023 with 60 items ([update log](https://rblxguide.com/games/dress-to-impress/update-log)); place created 18 Oct 2023 (Roblox public API, 25 Nov 2026) |
| Genre | Dress-up round game. See [genres/dress-up.md](../genres/dress-up.md). |
| Peak concurrent players | 0.65M to 1.73M, Aug to Dec 2024, unverified: 651K Aug 2024 ([Wikipedia](https://en.wikipedia.org/wiki/Dress_to_Impress_%28video_game%29)), 1.1M Dec 2024 ([RoWatcher](https://rowatcher.com/games/5203828273)), 1.5M ([RoWatcher news](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits)), 1.73M (a blog snippet) |
| Players now | 52,854; 11.39B visits (Roblox public API, 25 Nov 2026) |
| Players per server | 13. Style Showdown 7, Freeplay 17 ([guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide)). |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Lobby | Waits | not known | The next theme near the end of the countdown, then a teleport | none |
| Dress | Picks clothes, hair, makeup | 360 (300 on Casual) | The avatar changes with each item | Items worn, cap 18 (13 Casual, 24 with a pass) |
| Runway | Walks in join order, poses | not known per player | One model at a time | none |
| Vote | Rates every other model | During the runway | 1 to 5 star buttons | That model's stars |
| Podium, payout | Watches | not known | Top three on a podium, then a board of stars and Cash | Career stars; 0 to 60 Cash |

Sources: [wiki: Game Mode](https://dti-dress-to-impress.fandom.com/wiki/Dress_to_Impress/Game_Mode), [wiki: Cash](https://dti-dress-to-impress.fandom.com/wiki/Currency/Cash).

Cycle time is at least 360 seconds plus 13 walks of unpublished length. In 2023 the round was 30 seconds of intermission and 180 of dressing ([guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide)), so dressing time has doubled. **Our read:** the dead time is the 12 walks that are not yours, and the vote gives each of them one decision.

## 2. First session

No source times it. New players start on a Casual server: 300-second clock, 13-item cap, no Accessory Adjustment, and a tutorial whose contents are not known ([guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide)).

| Time | What happens |
|---|---|
| 0:00 to 0:10 | not known |
| 0:10 to 1:00 | not known; a Casual lobby |
| 1:00 to 5:00 | The first dressing phase |
| 5:00 to 15:00 | **Our read:** the first runway and stars, not before about 5:00 because dressing takes 300 seconds |

First reward: Cash piles on the map (pink 1 to 3, gold 15 to 25) and 15 Cash for the first Daily Login. First purchase: a fan guide suggests a pose pack, the cheapest 1,800 Cash, which is 30 rounds at the 60-Cash ceiling ([money guide](https://rblxguide.com/games/dress-to-impress/updates/how-to-get-money-guide)). First long goal: Accessory Adjustment after 30 rounds, or 399 R$. **Our arithmetic:** 30 rounds of at least 360 seconds is 3 hours.

## 3. Progression

| Server | Entry | Added |
|---|---|---|
| Casual | New players; 300 s, 13 items | 18 Oct 2025 |
| Regular | Anyone; 360 s, 18 items | 4 Nov 2023 |
| Pro | 3,000+ stars (was 2,000, then 1,500) | 11 Nov 2023 |
| Master | 10,000+ stars | 1 Mar 2025 |
| VIP | VIP pass | 11 Nov 2023 |

Source: [wiki: Game Mode](https://dti-dress-to-impress.fandom.com/wiki/Dress_to_Impress/Game_Mode).

| Rank | Stars | Reward item | Rounds at 20 stars each |
|---|---|---|---|
| New Model | 0 | | 0 |
| Rising Star | 50 | | 3 |
| Aspiring Model | 200 | | 10 |
| Fashionista | 500 | | 25 |
| Glamourista | 1,000 | | 50 |
| Fashion Maven | 1,500 | Nails | 75 |
| Runway Queen | 3,000 | Bag | 150 |
| Trend Setter | 6,000 | Skirt | 300 |
| Runway Diva | 15,000 | Crown | 750 |
| Top Model | 25,000 | Silk Robe | 1,250 |
| Glamour Elite | 50,000 | | 2,500 |
| Fashion Mogul | 75,000 | | 3,750 |
| Supernova | 100,000 | Crown | 5,000 |
| Fashion Goddess | 150,000 | | 7,500 |

Sources: [wiki: Ranks](https://dti-dress-to-impress.fandom.com/wiki/Stars); reward items from the [guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide).

Stars per standard round are not known; the wiki does not publish them. The last column uses one unverified report that even winners get about 20 stars ([PC Gamer](https://www.pcgamer.com/games/sim/i-played-robloxs-hottest-game-thats-sweeping-social-media-and-got-my-ass-handed-to-me-by-a-bunch-of-12-year-olds), snippet only) and assumes a win every round, so read it as a floor. **Our arithmetic:** the top rank is then 7,500 wins, 750 hours of dressing alone. Each threshold is 1.3 to 4 times the one before. Style Showdown pays 100, 50 and 33 stars to its top three ([guide](https://rblxguide.com/games/dress-to-impress/updates/style-showdown-guide)); whether these are career stars is not known.

Cash: 0 to 60 a round. The 98 Cash items total 163,800, median 1,500; pose packs 1,800 to 5,000 ([money guide](https://rblxguide.com/games/dress-to-impress/updates/how-to-get-money-guide)). **Our arithmetic:** the whole Cash catalogue is 2,730 rounds at the ceiling.

## 4. Session and return hooks

- Every round: Theme Prop offer (75 R$) and +60 Seconds (79 R$).
- Every 24 hours: Daily Tasks (150 Blue Hearts each); Daily Login of 15 Cash on day 1 plus 15 per day in a row, 105 on day 7, 420 in week one; a Roblox ad multiplies a day by 1.5 ([money guide](https://rblxguide.com/games/dress-to-impress/updates/how-to-get-money-guide)).
- Every Saturday 11 AM Eastern: 4 new Weekly Boutique items.
- Every 8 to 16 weeks: a Baddie Pass season of 30 tiers (40 at Halloween 2026) ([guide](https://rblxguide.com/games/dress-to-impress/updates/baddie-pass-guide)) and a large Saturday item drop. Week ranges are our arithmetic from the dates; the 2026 calendar is on the [genre page](../genres/dress-up.md#live-ops).

No offline progress is documented.

## 5. Other players

Every walk has up to 12 judges, who can throw paid reactions. Freeplay's 0 to 10 Judge Panel cards pay nothing ([Freeplay guide](https://rblxguide.com/games/dress-to-impress/updates/freeplay-mode-guide)). Spite voting and clique voting are the main complaint ([RoWatcher news](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits)). The changes, in order:

| Date | Change |
|---|---|
| 2023 | Joining 20 s or less before voting keeps you off the runway (unverified whether it still applies) |
| 29 Feb 2024 | Theme Prop changed from automatic purchase to optional |
| 17 Aug 2024 | Theme voting added |
| not dated | Pro gate moved 2,000 to 1,500 to 3,000 stars |
| 1 Mar 2025 | Master servers at 10,000+ stars |
| 12 Jul 2025 | "Fairer voting" trial |
| 19 Jul 2025 | Vote penalties removed except on Master servers; replacement promised |
| 16 Aug 2025 | Theme voting returns, every 4 rounds |
| 18 Oct 2025 | Casual servers for new players |
| 9 May 2026 | Theme voting removed |

Sources: [how-to-win guide](https://rblxguide.com/games/dress-to-impress/updates/how-to-win-guide), [themes guide](https://rblxguide.com/games/dress-to-impress/updates/themes-guide), [guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide). No replacement for the penalties is recorded.

Clipped: runway walks and poses, such as the TikTok "Pose 28" emote.

## 6. Money

Prices: Roblox public API, 25 Nov 2026.

| Item | Type | R$ | What it does |
|---|---|---|---|
| VIP Pass | pass | 799 | VIP dressing room, lounge, servers, tag, some Baddie Pass tiers |
| VIP one month (gift prop) | product | 299 | 30 days of VIP |
| Increased Item Limit | pass | 129 | Cap 18 to 24 |
| x2 Money | pass | 399 | Doubles Cash pickups |
| Custom Makeup, Materials+ | pass | 349, 299 | Editors |
| Clothing sets (9) | pass | 279 to 449 | Fixed outfits; gift bundles x3, x5 |
| Diamond Baddie Pass | product | 299 | Paid season track; skips 199, 3 for 499 |
| Theme Prop | product | 75 | Pick the theme and runway style |
| +60 Seconds | product | 79 | More dressing time |
| Accessory Adjustment | product | 399 | Free after 30 rounds |
| Reactions (5 uses) | product | 29 to 129 | Roses 29, Tomato 59, Poop 129 |
| Cash packs | product | 100 to 4,500 | 500 to 40,500 Cash, 5 to 9 per R$ |

VIP gives no documented scoring or voting advantage ([VIP guide](https://rblxguide.com/games/dress-to-impress/updates/vip-guide)). **Our arithmetic:** permanent VIP equals 2.7 months of monthly VIP, so it is cheaper from month three (897 against 799). Best sellers are not known.

The snapshot agrees with every price above [data, Nov 2026]. It shows 14 passes on sale: 8 clothing sets (a ninth, Futuristic Suit, is off sale) and a Run Faster pass at 149. Products: 37 on sale, 9 to 4,500 R$, median 149, leaving out about 50 "Gifting Prop" copies (sold singly, x3 and x5), five donation items and three test items. Not in the table above:

| Product | R$ | Note |
|---|---|---|
| Revive / Revive (Elimination Game Mode) | 79 / 149 | |
| immunity | 99 | |
| Copy Outfit | 99 | |
| Daily Login Bonus / Claim Missed Advent Day | 99 / 99 | |
| Robux Hair Slot A / B / C / D | 99 / 149 / 299 / 499 | Each slot dearer than the last |
| Seasonal Tier 1 to 5 | 100 to 4,500 | Same prices as the Cash packs |

**Our read:** a missed login day sells for 99 R$, the same as the bonus itself, so a broken streak has a price.

## 7. Why it works

No developer statement on design was found. Measured: 7.8M favourites, 90.5% likes ([RoWatcher](https://rowatcher.com/games/5203828273)), three 2024 Roblox Innovation Awards, growth tied to celebrity collabs, TikTok and streamers ([RoWatcher news](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits)).

**Our read:** 790+ themes make the same 18-item puzzle new each round. Real people judge every look within minutes. Stars and money are separate ladders, so Robux never buys rank. In-round offers land inside the 360-second clock, while the player sees what they lack.

## 8. What went wrong

- Spite and clique voting; penalties added and withdrawn within a week in July 2025.
- A three-hour limited code item crashed the game in its first minutes in Dec 2024; the Lady Gaga event also crashed servers ([Wikipedia](https://en.wikipedia.org/wiki/Dress_to_Impress_%28video_game%29)).
- Accusations against the founder in Sept 2024 and a community-manager removal (Wikipedia).
- **Our arithmetic:** 52,854 players now is 3% to 8% of the 2024 peak range.

## 9. What to take from it

- A 300 to 360-second build against one theme, then a runway scored 1 to 5 stars by everyone else.
- A new-player server with a shorter clock and fewer slots (300 s, 13 items); star gates for higher servers (3,000 and 10,000).
- A 14-rank ladder to 150,000 stars, thresholds rising 1.3 to 4 times, a wearable at 6 ranks.
- An 18-item cap and a 129 R$ pass that raises it by a third.
- Moment-of-need products inside the round: theme 75 R$, +60 seconds 79 R$.
- VIP at 799 permanent or 299 a month.

## Sources

Dress to Impress fandom wiki (Game Mode, Cash, Ranks, Update Log 2026) and rblxguide.com summaries of it, read 25 Nov 2026; Wikipedia; RoWatcher; Roblox public API, 25 Nov 2026. All linked inline.
