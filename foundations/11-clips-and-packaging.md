# Clips and packaging

This page covers what a player meets before they control a character: title, icon, thumbnails, the game page, paid ads, creator videos and invites from friends. Open it before you upload the first thumbnail, before you spend the first ad credit, and whenever impressions are high but plays are low. The ranking rules behind it are on [02-the-platform.md](02-the-platform.md). Roblox changed its discovery system on 15 June 2026, so older facts are dated.

## What is known

### The top of the funnel in three steps

| Step | Where | The number you can see | What decides it |
|---|---|---|---|
| 1. Seen | A tile on Home, search, a chart, a sponsored slot, a friend's activity | Impressions (thumbnail personalisation, Ads Manager) | Your past signals; a custom thumbnail is required for any Home recommendation |
| 2. Played | The player taps the tile and joins | Play-through rate (PTR): how often users play after seeing the game in Recommended For You; ads also show click-through rate (CTR) and cost per play | Icon, thumbnail, title |
| 3. Stayed past the first minute | The first 60 to 180 seconds | First-play bounce, a negative signal bucketed under 60 s and 61 to 180 s | The first session ([05-first-session.md](05-first-session.md)) |

Sources: [Discovery docs](https://create.roblox.com/docs/production/promotion/discovery), [Discovery FAQ](https://create.roblox.com/docs/discovery-faq), [Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard). PTR and bounce are the first and second ranking signals. Roblox publishes no target for either.

One developer's ad test (27 July 2026, 5 credits a day, one day) shows why steps 2 and 3 must be read together ([DevForum](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265)):

| Thumbnail | Impressions | Clicks | CTR (as reported) | Plays | Cost per play |
|---|---|---|---|---|---|
| The icon art reused | 32,269 | 852 | 2.59% | 2 | 1.695 credits |
| Custom art of the game | 17,236 | 466 | 2.7% | 37 | 0.044 credits |

**Our arithmetic:** the click rates match, but 7.9% of clicks became plays with custom art against 0.23% with icon art, about 34 times more. One game, one day: a warning, not a law. A tile that gets clicks without showing the game wastes them.

### Titles

The October 2026 top 20 by average players ([Bloxodes](https://bloxodes.com/stats/reports/roblox-october-2026), a tracker; page partly read):

- **Verb plus thing** leads: [Steal an egg](../teardowns/steal-an-egg.md) (No. 1, 1.28M average), [Steal a Brainrot](../teardowns/steal-a-brainrot.md) (No. 8), Break and Steal an Egg (No. 12, new), Ride A Pet (No. 15, new). Three of the 20 contain "Steal".
- **The "+1" template**: +1 Speed Keyboard Escape (No. 10), with +1 Stone Skipping and +1 Loot To Forge lower down.
- No visible title starts with "Grow", the template of mid-2025.
- New entries name one object or act: Climb For Animals Eggs, Build and Kill Zombies, Survive a Million Monkeys.

On the 18 November chart, four new titles used "Ragdoll", several a "Realistic" prefix, and 11 games still carried a pumpkin emoji or Halloween tag three weeks after Halloween ([GGRecon](https://www.ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/)). Slop hits put a seasonal emoji in square brackets before a two-to-four-word name and swap it each event: a turkey on Kick a Lucky Block, a chilli on [Grow a Garden](../teardowns/grow-a-garden.md) (Roblox public API, 25 Nov 2026).

**The top 300 titles, counted.** The repo's snapshot of all public charts ([data/ANALYSIS.md](../data/ANALYSIS.md), section 6) measured the 300 games with the most players on 25 November [data, Nov 2026]:

| Measure | Top 300 |
|---|---|
| Length, full title with tags and emoji | median 21 characters (middle half 15 to 27) |
| Core title without tags | median 3 words |
| A bracket tag such as [UPD], [THANKSGIVING] or a turkey emoji in brackets | 51% |
| An emoji | 53% |
| An update or event word (UPDATE, NEW, EVENT, 2X, PART 2) | 16% |
| Starts with a verb | 18% (Build 6, Steal 4, Throw 4, Raise 4, Fish 3, Survive 3, Run 3) |
| "Verb a/an thing" shape, as in Steal a Brainrot | 8% |
| "+1" in the title | 2% |
| Core title in all capitals | 5% |

**Our read:** the bracket tag is the norm, used by half the chart. A verb opening is a minority choice, 18%, that the 2026 slop hits share; it fits games whose whole loop is one verb.

**Bait titles.** Dead clones of 2026 hits use "ADMIN PANEL", "X999999M" and "FREE" (Roblox public API, 25 Nov 2026):

| Title | Players, 25 Nov 2026 | Like ratio | Updated for |
|---|---|---|---|
| "Kick for ADMIN PANEL! X999999M" | 78 | 63.0% | 2 days |
| "KICK FREE BLOCK (X999)" | 1,256 | 70.2% | 5 days, then the creator account was deleted |
| "Kick Blocks for ADMIN PANEL! X999999M" | 20 | 88.3% | not known |
| [Throw Food For Animals](../teardowns/throw-food-for-animals.md) (a hit) | 238,007 | 94.1% ([RoWatcher](https://rowatcher.com/games/10766972131)) | updated 25 Nov |

Emoji in the clone titles are left out. Across the sample, bait clones ran 59% to 70% liked and hits 85% to 97%. Rating alone does not sort hits from failures: one bait title sits at 88.3%, and some plain-titled dead clones are above 90%. A low rating does flag a bait title. Across the top 300 the median like ratio is 89% and the bottom tenth starts at 74%; Party & Casual games run lower, median 73% with one at 30% [data, Nov 2026]. **Our read:** under about 75% liked, a non-party game is in the bottom tenth of the chart.

Roblox's wording ([Discovery docs](https://create.roblox.com/docs/discovery)): titles must be accurate with no irrelevant keywords; titles that lead with money get less exposure; avoid repetitive titles; a game that follows a trend should add a twist of its own. Close copies are "no longer prioritized for recommendations".

**The one measured title change.** A game retitled from "Sell Your Data" to "Hack a Business", with a new thumbnail at the same time, went from 1.54% to 3.27% ad click-through: 2.1 times the clicks per impression by our arithmetic ([SozAI transcript](https://sozai.app/transcript/roblox-sponsored-ads-explained/)). The speaker is unnamed, the video undated, title and thumbnail changed together, and nothing was controlled. The speaker advises third-grade reading level and keyword research.

### Thumbnails and icons

| Asset | Spec | Source |
|---|---|---|
| Icon | Square, at least 512x512; some surfaces show it at about 150x150; one per language | [Icons docs](https://create.roblox.com/docs/production/publishing/experience-icons) |
| Thumbnail | 16:9, ideally 1920x1080; other shapes are stretched; keep key content off the bottom edge, where the player count can cover it | [Thumbnails docs](https://create.roblox.com/docs/production/promotion/thumbnails) |
| Game page | Up to 10 images and videos | same |
| Personalisation | 2 to 5 active thumbnails, each under 3 MB | same |

Roblox's icon advice: imagery that matches the gameplay, nothing ambiguous, bright saturated colour for fantasy, muted for sombre themes, heavy contrast for horror.

**Thumbnail personalisation** shows each active thumbnail to random groups and shifts impressions to the winner for each player segment. Roblox calls it a multi-armed bandit, not an A/B test.

| Source | Date | Average lift in qualified PTR | Best case |
|---|---|---|---|
| Thumbnails docs | older | +8.5% | about +50% |
| [Roblox staff post](https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689), 8,000+ games | 2025 | +12% (relative) | +56% |

Staff tips: wait at least 7 days, or until the next update, before restarting (called the most important tip); keep up to 5; make them clearly different from each other; show new content; avoid clickbait, which can trigger low-quality warnings. Roblox also estimated 16:9 ad thumbnails lift qualified play-through 57% over other shapes (August 2025, [DevForum](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159)).

**Our arithmetic:** with a 7-day minimum, a game gets at most 4 test rounds per 28-day window. A +12% relative lift on a 3% PTR gives 3.36%.

One unnamed video describes Steal An Egg's icon as a running character holding an egg, a dragon-like dinosaur behind, high contrast, one focal point, little text ([SozAI](https://sozai.app/transcript/game-accidentally-solved-roblox-algorithm/index.md)). Counts of faces or words in top thumbnails are not known.

### The game page

- **Description.** Recent slop hits use five to seven short lines, each starting with a verb (Roblox public API, 25 Nov 2026; see [slop/01-anatomy.md](../slop/01-anatomy.md)). No Roblox guidance on length was found.
- **Video.** Allowed: camera angles, light post-processing, a logo, highlights, in-game UI text, catalog music. Banned: anything not in the game, enhanced visuals, real-world footage, voice-over, voice chat, music with lyrics, ads or subjective claims. It shows first on the page and can appear on Home. Quota: 3 uploads a month, rejected ones included. Not shown on Xbox, PlayStation or VR ([Thumbnails docs](https://create.roblox.com/docs/production/promotion/thumbnails)). No maximum length is stated.
- **Tags.** Accurate genre tags and an accurate gameplay video reduce bounces ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)).
- **Events.** Up to 10 at once, 5 thumbnails each; update posts of 60 characters, one every three days ([Experience events](https://create.roblox.com/docs/en-us/production/promotion/experience-events)).
- **Social links.** Up to 3, visible only to age-checked 16+ since 30 June 2026 ([Social links](https://create.roblox.com/docs/en-us/production/promotion/social-media-links)).

### Ads

| Item | Value | Source |
|---|---|---|
| Ad credit | 263 Robux (Sep 2025, was 285); cannot be converted back | [RDC recap](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106), [Ads Manager docs](https://create.roblox.com/docs/production/promotion/ads-manager) |
| Minimums | Buy 1 credit; a campaign needs 10 (2,630 Robux, our arithmetic) | [DevForum, Nov 2025](https://devforum.roblox.com/t/ads-manager-updates-home-search-combined-new-benchmarks-and-sunsetting-the-classic-flow/4084863) |
| Placement | Home sponsored tile and search (top 2 slots, then every 10 results); up to 10 custom 16:9 thumbnails per campaign | same |
| Audiences | All; New (never played or 180+ days away); Recent (needs 10,000 recent players); Lapsed (needs 20,000) | Ads Manager docs |

Cost per play, published by Roblox "as of Nov 11, 2025"; later figures are not known:

| Objective | Cost per play | Per 1,000 plays (our arithmetic) |
|---|---|---|
| Maximize Plays | $0.0073 | $7.30 |
| Reactivate Users | $0.011 | $11.00 |
| Drive Retention | $0.0113 | $11.30 |
| Acquire New Users | $0.0187 | $18.70 |

**Ranking.** Ad-acquired players are excluded from every Recommended For You signal, even if they later return through Home ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).

**A developer report against ads.** On 29 August 2026 the makers of an extraction shooter reported playtime of 11.1 to 12 minutes per user with ads on against 28.0 to 29.9 with ads off, and D1 of about 3% against 5% to 8%. About 85% of one week's new plays came from ads, and 45% of them dropped at the Deploy step ([DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351)). The claim that this hurt organic ranking is unproven and conflicts with the docs.

**How studios use ads.** Nathan Clemens (UndoneBuilder, 24 games, 850M+ sessions) markets only to seed a launch to a few thousand to about 10,000 players, then lets the algorithm take over ([Naavik](https://naavik.co/podcast/mastering-the-roblox-meta/)). The unnamed speaker above says Roblox recommends 16 credits a day for at least 3 days, ideally a week, stopping once Home impressions overtake sponsored ones (single practitioner, unverified). WonderWorks (SpongeBob Tower Defense) reports buying no paid acquisition ([Naavik](https://naavik.co/podcast/the-creator-led-studio-playbook/)).

**Roblox's own claim.** The 5 newest games to reach the top 20 by earnings all began with Sponsored ads, and nearly half of the top 100 creators used Ads Manager in 2025 ([RDC recap](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106), [DevForum](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159)). This is Roblox selling its product; it shows no cause.

**Our arithmetic:** 16 credits a day is 4,208 Robux, so a 7-day seed is about 29,500 Robux. 10,000 Maximize Plays cost about $73. At the report's 3% D1 that buys 300 day-1 returners, about $0.24 each; at 8%, 800 at about $0.09.

### Creators and clips

What is documented:

- **Video grew faster than play.** March to August 2025: players roughly doubled while Roblox hours watched went from under 20M a month to 85.6M. In July 2025 Grow a Garden was 44.5M hours, 56% of all Roblox viewership, much of it 24/7 trading streams ([Stream Hatchet](https://hatchet.gg/blog/the-link-between-roblox-streamers-and-roblox-players/)). No causal estimate.
- **Short video carried the hits.** Grow a Garden's coverage was mostly short-form video ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Steal a Brainrot's theft clips reached tens of millions of views ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)). One analysis argued that clips of players losing a Brainrot taught the mechanic; that is opinion.
- **Developers as creators.** Jandel of Splitting Point said in July 2025 he has 12M TikTok followers (self-reported; another source says 7.5M). Grow a Garden went from about 500 concurrent at the partnership to about 1M a month later, with weekly updates ([GamesBeat](https://gamesbeat.com/janzen-madsen-interview/)); his mock "admin war" with Steal a Brainrot on 23 August 2025 set the 22.3M record. KreekCraft, a large Roblox YouTuber, released Sail For Brainrots in February 2026; it earned "tens of thousands of dollars" within weeks ([The Star / Bloomberg](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators)).
- **Updates planned as videos.** WonderWorks designs each weekly update to produce 3 to 4 creator videos ([Naavik](https://naavik.co/podcast/the-creator-led-studio-playbook/)). Clemens and Janzen Madsen say videos help only when creators choose to make them, not when paid; Clemens says brand deals take about 2 months and mostly stopped ([Naavik](https://naavik.co/podcast/mastering-the-roblox-meta/)).
- **Brand-deal rules.** Posted 20 March 2026; registration and labels required from 4 May 2026, with under-13 restrictions; register at least 5 business days ahead. Revenue share from early 2027 per 1,000 qualified visits in the first 28 days: US $1.50, Tier 1 (UK, Canada, Australia, New Zealand, Nordics) $0.75, Tier 2 $0.20, Tier 3 $0.05. Roblox's creator price guideline is about $4 to $5 per 1,000 visits ([DevForum](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365)). Disclosure must be clear and, for codes, come just before the code ([Roblox Help](https://en.help.roblox.com/hc/articles/360026092011)).
- **Meme rights.** The Tung Tung Tung Sahur character was removed from Steal a Brainrot on 13 September 2025 after a copyright dispute ([Know Your Meme](https://knowyourmeme.com/memes/tung-tung-tung-sahur-song-steal-a-brainrot-rap-by-devvey)).

**Our read: the 15-second clip test.** No source measured what makes a clip spread, but the clips that travelled (thefts, admin wars, a prize lost at the door) share four traits. Before building a feature, describe its 15-second clip and score it:

| # | Test | Pass |
|---|---|---|
| 1 | Readable with the sound off | A stranger can say what happened from the picture alone |
| 2 | A winner and a loser on screen | Two players, or a player and a threat, in the same shot |
| 3 | A payoff | Something is gained, lost, broken or revealed before second 15 |
| 4 | No context needed | Makes sense to someone who never played |

The trip home in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md) passes all four. A stat screen passes none.

### Friends and reach

- **Invite prompts.** Check `SocialService:CanSendGameInviteAsync()` in a pcall, then `PromptGameInvite`. LaunchData takes up to 200 characters; if the prompt text overflows, the prompt does not show ([Invite prompts](https://create.roblox.com/docs/production/promotion/invite-prompts)). An invite join skips matchmaking and lands in the friend's server ([DevForum, Dec 2023](https://devforum.roblox.com/t/updates-to-invites-joining-friends-just-got-easier/2729692)). A "6 times more users sending invites" figure is attributed to the docs but was not on the page as read.
- **Referrals.** Officially supported: reward both sides, one reward per invitee, a cooldown ([Referral system](https://create.roblox.com/docs/en-us/production/promotion/referral-system)).
- **Experience notifications.** Opted-in users 13+ only; 100+ visits needed; one per user per day per game; 99 characters; the opt-in prompt is hidden for under-13s and if shown in the last 30 days; false time pressure and bait-and-switch rewards are banned; notifications cannot be required ([Experience notifications](https://create.roblox.com/docs/production/promotion/experience-notifications)). **Our arithmetic:** at most about 12 opt-in asks per player per year.
- **Moments.** Clips up to 30 seconds, in beta since September 2025. Since 28 July 2026 a Moments tab sits on the home page in Canada, New Zealand and Singapore, rolling out globally. Each clip has a one-tap Join; one-tap discovery is for age-checked 16+ ([Roblox newsroom](https://about.roblox.com/newsroom/2026/07/moments-new-homepage-unlocks-gaming-for-all)).
- **Translation.** Roblox's automatic translation test (June 2025) lifted qualified PTR 0.87% on average and new Korean and Japanese speakers' playtime 4% ([DevForum](https://devforum.roblox.com/t/automatic-translation-experiment-results-and-next-steps/3878129)).
- **A local theme.** Karinderya!, a 6-player Filipino eatery co-op released 7 August 2026, reached about 14.5M to 16.7M visits; tracker peaks range from 57K to 295K. No Tagalog was found in-game ([RoTrends](https://www.rotrends.com/game/10648820673/Karinderya)). **Our read:** evidence for a local theme with English text, not for local-language games.

## The rules

1. **Name the game with a verb and one object, 2 to 4 words.** Three of the October top 20 contain "Steal", and the 2026 slop hits all follow the pattern.
2. **Keep money, Robux, "FREE" and "X999999" out of the title.** Roblox gives money in metadata less exposure, and bait clones ran 59% to 70% liked against 85% to 97% for hits.
3. **Upload a custom 16:9 thumbnail at 1920x1080 before day one.** No custom thumbnail, no Home recommendations.
4. **Show the real game in the thumbnail.** In one test, game art turned 7.9% of clicks into plays against 0.23% for reused icon art.
5. **Run 5 different thumbnails and leave them 7 days.** Staff report +12% average, up to +56%, and name early restarts as the main mistake.
6. **Make the icon readable at 150x150.** Roblox shows icons at about that size. **Our read:** one focal object, high contrast, three words or fewer.
7. **Fix the first 60 seconds before buying ads.** Bounce is the second signal, and ad players who bounce cost money without moving rank.
8. **Use ads to seed, then stop.** Seed to a few thousand to 10,000 players, judge D1 and playtime by source, stop when Home impressions pass sponsored ones.
9. **Plan every update around 3 to 4 clips** that pass the 15-second test.
10. **Show the invite button when a player wants a witness.** Invite joins skip matchmaking and co-play days are a signal. **Our read:** right after a big win or a theft, with LaunchData that spawns the friend beside them.
11. **Ask for notification opt-in only after the first reason to return exists.** The prompt can show at most once every 30 days.
12. **Swap the seasonal tag each event.** **Our read:** remove it within 7 days of the event ending; a Halloween tag in late November says the game may be abandoned.

## How to do it

1. **Title test.** Five people who have not seen the game read the title and say what you do. Pass: 4 of 5 name the core verb.
2. **Icon and 5 thumbnails,** each showing a different real moment. Shrink the icon to 150x150 and check it reads.
3. **Description:** five to seven lines, each starting with a verb, in the order the player does them.
4. **One gameplay video** inside the rules: real footage, no voice-over, no lyrics.
5. **Score each planned feature** with the clip test and write the clip into [kit/templates/update-plan.md](../kit/templates/update-plan.md).
6. **Before ad spend,** check first-session bounce and the funnel from [kit/templates/first-session-script.md](../kit/templates/first-session-script.md).
7. **Seed** if needed: 10 thumbnails in the campaign, daily budget, 3 to 7 days. Move the best 3 to 5 into Home personalisation.
8. **Read results by source** in the Acquisition tab: D1 and playtime for ad players against Home players ([14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md)).

## Checks

| Check | Pass |
|---|---|
| Title | 2 to 4 words, contains the core verb, no money words; about 21 characters with its tag (top-300 median) [data, Nov 2026] |
| Icon | 512x512 or larger; readable at 150x150 |
| Thumbnails | 2 to 5 active, all 16:9 at 1920x1080, all showing the real game |
| Thumbnail test | Not restarted within 7 days |
| Description | 5 to 7 lines, each starting with a verb |
| Video | No voice-over, no lyrics, nothing outside the game |
| First minute | Core action on screen inside 60 seconds before any ad spend |
| Ads | Judged on D1 and playtime by source |
| Clips | 3 or more moments per update pass all four clip tests |
| Invite | `CanSendGameInviteAsync` checked; prompt text fits |
| Notifications | Text 99 characters or fewer; opt-in asked after a reason to return |

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| High CTR, few plays | Thumbnail not showing the game, or joins failing on phones | Real game art; test the join on a 2 to 4 GB phone |
| High PTR, high bounce under 60 s | The tile promises what the first minute lacks | Put the thumbnail's object within 5 studs of spawn ([05-first-session.md](05-first-session.md)) |
| No personalisation winner | Restarted early, or thumbnails too alike | Leave 7 days; make each a different moment |
| Like ratio under 75% in week one | Bait title or an oversold page | Plain verb title; describe only what is in the game |
| Ad plays up, D1 and playtime down | Ad players bounce at an early step | Fix that step; cut the budget; judge by source |
| No creator videos after an update | Nothing to film | Add a server-wide moment with a winner and a loser |
| Invite prompt never appears | Text overflow, or no availability check | Shorten the text; check first in a pcall |

## Sources

- Roblox Creator Docs (undated, read Nov 2026): [Discovery](https://create.roblox.com/docs/discovery), [Discovery (promotion)](https://create.roblox.com/docs/production/promotion/discovery), [Discovery FAQ](https://create.roblox.com/docs/discovery-faq), [Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails), [Experience icons](https://create.roblox.com/docs/production/publishing/experience-icons), [Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager), [Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard), [Experience events](https://create.roblox.com/docs/en-us/production/promotion/experience-events), [Social media links](https://create.roblox.com/docs/en-us/production/promotion/social-media-links), [Invite prompts](https://create.roblox.com/docs/production/promotion/invite-prompts), [Referral system](https://create.roblox.com/docs/en-us/production/promotion/referral-system), [Experience notifications](https://create.roblox.com/docs/production/promotion/experience-notifications).
- Roblox DevForum: [Thumbnail personalisation tips](https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689), [Ads Manager, Aug 2025](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159), [Ads RDC recap, Sep 2025](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106), [Ads Manager, Nov 2025](https://devforum.roblox.com/t/ads-manager-updates-home-search-combined-new-benchmarks-and-sunsetting-the-classic-flow/4084863), [Ad test, Jul 2026](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265), [Ad traffic report, Aug 2026](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351), [Advertising policies](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365), [Invites](https://devforum.roblox.com/t/updates-to-invites-joining-friends-just-got-easier/2729692), [Translation results](https://devforum.roblox.com/t/automatic-translation-experiment-results-and-next-steps/3878129).
- Roblox: [Moments, 28 Jul 2026](https://about.roblox.com/newsroom/2026/07/moments-new-homepage-unlocks-gaming-for-all), [Help: disclosure](https://en.help.roblox.com/hc/articles/360026092011); Roblox public API, 25 Nov 2026.
- Trackers: [Bloxodes, Oct 2026](https://bloxodes.com/stats/reports/roblox-october-2026), [GGRecon, 18 Nov 2026](https://www.ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/), [RoWatcher](https://rowatcher.com/games/10766972131), [RoTrends](https://www.rotrends.com/game/10648820673/Karinderya).
- Creators and studios: [Stream Hatchet](https://hatchet.gg/blog/the-link-between-roblox-streamers-and-roblox-players/), [GamesBeat](https://gamesbeat.com/janzen-madsen-interview/), [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden), [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/), [The Star / Bloomberg](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators), [Naavik: creator-led studio](https://naavik.co/podcast/the-creator-led-studio-playbook/), [Naavik: mastering the meta](https://naavik.co/podcast/mastering-the-roblox-meta/), [Know Your Meme](https://knowyourmeme.com/memes/tung-tung-tung-sahur-song-steal-a-brainrot-rap-by-devvey).
- Unnamed practitioner, unverified: [SozAI: sponsored ads](https://sozai.app/transcript/roblox-sponsored-ads-explained/), [SozAI: Steal An Egg](https://sozai.app/transcript/game-accidentally-solved-roblox-algorithm/index.md).
