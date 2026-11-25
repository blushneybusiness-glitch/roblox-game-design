# Obby

> **The feeling sold:** "I got higher than last time. I made the jump everyone else falls off."

This page covers stage obbies, tower obbies, rage climbs, two-player tether obbies, movement and tag games, and "find the ..." collect-a-thons. The 2026 hybrids where every step adds +1 to a stat (+1 Speed Keyboard Escape, Escape Tsunami For Brainrots) are on their own page: [plus-one.md](plus-one.md).

Counts are from Roblox's public API on 25 Nov 2026 unless a row says otherwise. A badge count is the number of different users who ever earned it, so a chain of stage badges is a survival curve of every player a game has had. These curves are the best evidence this genre has.

## At a glance

| | |
|---|---|
| Core verb | Jump |
| Study these first | [Tower of Hell](../teardowns/tower-of-hell.md): no checkpoints, 6 random sections, 8-minute timer, 23.8K players after eight years. Mega Easy Obby: 825 stages, the cleanest survival curve. Escape Running Head: 12 stages and a boss, 3.08B visits. Barry's Prison Run: easy and hard versions of every course, 14.4K players now. Eternal Towers of Hell: the 11-step difficulty scale and building rules. |
| Session that works | Not known for stage obbies. Tower of Hell caps a round at 8 minutes. Chained (2 Player) gives a badge for reaching 10 minutes, earned 336,522 times since 7 Apr 2026 ([badges API](https://badges.roblox.com/v1/universes/6215464786/badges?limit=100)). |
| Players per server | Towers and stage obbies 12 to 30 (Tower of Hell 20, Mega Easy 12, Barry's 12, Speed Run 4 30). Tether games 15 or 30, 2 to 5 per chain. Tag 40. |
| Who owns the genre | Old games. Tower of Hell (2018) 23.8K now, Barry's (2022) 14.4K, Escape Running Head (2021) 5.8K. Newer games spiked and fell: Chained (2 Player) 42K peak to 859, Untitled Tag Game 31K to 1.4K, Obby But You're on a Bike 6K to 573, Swing Obby for Brainrots about 60K to 335 (peaks from [RoWatcher](https://rowatcher.com/games/6215464786), a single third-party tracker). |
| Build cost | Not known. **Our read:** the cost is stage count. Tower of Hell draws from 330 sections; Mega Easy has 825 stages. |
| Money comes from | Traversal passes (coils, double jump, jetpack) at 99 to 530 R$; VIP at 399 to 699 R$; cosmetics. |
| What kills clones | Content that stops: Mega Easy Obby last updated 3 Jan 2024 and has 68 players against 1.73B visits. |

## Why people play it

No age or device split for obby players is in the sources. What the badges show:

- **Players test themselves on a visible number.** Speed Run 4's "beat it again" badges: twice 3.11M, 10 times 220.7K, 30 times 40.95K ([badges API](https://badges.roblox.com/v1/universes/83858907/badges?limit=100)).
- **Failing is part of the show.** Altitorture's two most common badges are for falling: "Rock Bottom" 65.77M, "Free Fall" (75 m) 39.18M. "Never ragdolled through a stage" has 4.62M ([badges API](https://badges.roblox.com/v1/universes/4877714411/badges?limit=100)).
- **Easy and hard sell to different people.** Barry's easy win 173.21M, hard win 10.01M.

**Our read:** the obby sells one moment: the jump you missed five times and then made. Everything else shortens the wait for it or adds a witness.

## The loop, with a stopwatch

Leader: [Tower of Hell](../teardowns/tower-of-hell.md), the only obby with its round rules written down in full ([wiki](https://tower-of-hell.fandom.com/wiki/Home)). Section times are our arithmetic.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Shop | Buys one gear or mutator for this round | Not known | One gear 30% or 50% off, one mutator 30% off | Coins down 40 to 500 |
| Climb | Jumps through 6 random sections | About 80 per section (480 / 6) | Timer on screen | Coins and XP per section |
| Fall | Drops to the bottom; no checkpoint | 0 | The whole climb below | Coins already earned are kept |
| Finish | Touches the neon door | 480 at most | "Made it to the top" in chat; the timer speeds up for the rest | Up to 100 coins and 100 XP |

How the others differ: a stage obby (Mega Easy, Speed Run 4, Running Head) replaces the round with a fixed, saved line of stages, and the counter is the stage number. A find-the game replaces the jump with a search, and the counter is markers found.

### The loop stack

| Every | What finishes | Example |
|---|---|---|
| 0.5 s | A jump lands or misses | Default air time 0.51 s (below) |
| About 80 s | A section or stage | Tower of Hell noob budget |
| 5 stages | A badge | Mega Easy |
| 8 minutes | A round and its payout | Tower of Hell |
| One session | A level, world or milestone badge | Speed Run 4 levels |
| 1 to 4 weeks | A new stage | Running Head at launch |
| 7 to 14 months | A new mode with its own badges | Barry's |

**Our read:** the rows between one session and one week are empty. No leader in the sources has a sourced daily reward, offline growth or weekly event.

## The first five minutes

No recorded first session for any obby was found. Assembled from Tower of Hell's wiki and the funnels:

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | Spawned at a 6-section tower, 8-minute timer running | [Noob Towers](https://tower-of-hell.fandom.com/wiki/Noob_Towers) |
| 0:30 | First coins for the first section beaten | [Coins](https://tower-of-hell.fandom.com/wiki/Coins) |
| 1:00 | First fall to the bottom | Our read: no checkpoints |
| 3:00 | In a stage obby, stage 1 cleared or the player has left | 38% of Speed Run 4 joiners never complete level 1 |
| 5:00 | A first finish: level 1 (100 XP) and one skill point | [Levels](https://tower-of-hell.fandom.com/wiki/Levels) |

**Start with:** these gates, our read from the size of each funnel's first cliff.

| Gate | Pass if |
|---|---|
| First jump | Within 5 s of spawning, gap 4 studs or less |
| Stage 1 cleared | By 0:30 for 9 in 10 testers |
| First save | End of stage 1 |
| First badge or visible reward | By 1:00 |
| First new obstacle type | By stage 5 |

## Numbers that work

### The physical limits

Engine defaults ([Humanoid](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml), [StarterPlayer](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/StarterPlayer.yaml), [Workspace](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Workspace.yaml)): WalkSpeed 16 studs/s; JumpPower 50; JumpHeight 7.2 studs; UseJumpPower true, so JumpPower is the one in use; Gravity 196.2 studs/s²; MaxSlopeAngle 89°.

Our arithmetic, simple projectile physics (Roblox documents no jump distance):

| | JumpPower 50 (in use) | JumpHeight 7.2 |
|---|---|---|
| Launch speed | 50 studs/s | 53.2 studs/s |
| Highest point | 6.4 studs | 7.2 studs |
| Air time | 0.51 s | 0.54 s |
| Flat distance at walk speed 16 | about 8.2 studs | about 8.7 studs |

The two documented defaults disagree by about 0.8 studs of height. Jump distance is also reported to change with frame rate and R6 versus R15 ([DevForum](https://devforum.roblox.com/t/jumping-off-a-trusspart-is-affected-by-fps-and-avatar-type/3292004), title only). A blog's claim of 10 to 12 studs does not fit this arithmetic ([noping.com](https://noping.com/blog/how-to-long-jump-in-roblox)). Measure in a gap-test place before shipping. Not known: phone versus keyboard, edge forgiveness, kill-part and moving-platform conventions.

### Survival curves

**Mega Easy Obby**, a badge every 5 stages ([badges API](https://badges.roblox.com/v1/universes/1261193936/badges?limit=100)). Shares and losses are our arithmetic.

| Stage | Players | Share of stage 5 | Lost since row above | Lost per stage (compounded) |
|---|---|---|---|---|
| 5 | 293.64M | 100% | | |
| 10 | 262.04M | 89% | 11% | 2.3% |
| 25 | 209.75M | 71% | 20% | 1.5% |
| 50 | 159.63M | 54% | 24% | 1.1% |
| 100 | 109.64M | 37% | 31% | 0.7% |
| 200 | 61.89M | 21% | 44% | 0.6% |
| 300 | 41.98M | 14% | 32% | 0.4% |
| 450 | 23.24M | 7.9% | 45% | 0.4% |
| 600 | 10.32M | 3.5% | 56% | 0.5% |
| 825 | 1.33M | 0.45% | 87% | 0.9% |

Single 5-stage drops of about 29% at 725 and 800 sit where stages were added after most players had left; we read them as an added-later effect, not hard stages. Prestige 1: 8.84M, 3% of stage-5 players.

**Speed Run 4**, 30 classic levels ([badges API](https://badges.roblox.com/v1/universes/83858907/badges?limit=100)):

| Badge | Players | Share of joiners | Lost since row above |
|---|---|---|---|
| Welcome | 308.86M | 100% | |
| Level 1 | 191.66M | 62% | 38% |
| Level 5 | 100.67M | 33% | 47% |
| Level 10 | 66.71M | 22% | 34% |
| Level 15 → 16 | 44.83M → 35.44M | 15% → 11% | 21% in one level |
| Level 26 → 27 | 21.76M → 15.21M | 7.0% → 4.9% | 30% in one level |
| Winner | 10.16M | 3.3% | |

**Escape Running Head**, 12 stages ([badges API](https://badges.roblox.com/v1/universes/2274830359/badges?limit=100)):

| Stage | 1 | 2 | 3 | 5 | 7 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| Players | 324.89M | 250.62M | 218.51M | 140.10M | 90.26M | 51.47M | 42.30M | 21.23M | 10.31M |
| Share of stage 1 | 100% | 77% | 67% | 43% | 28% | 16% | 13% | 6.5% | 3.2% |

Stages 11 and 12 were added on 25 Dec 2023 and 12 Feb 2024 ([games API](https://games.roblox.com/v1/games?universeIds=2274830359)). **Our read:** their 50% drops are the same added-later effect.

**Obby But You're on a Bike**, 111 worlds ([badges API](https://badges.roblox.com/v1/universes/4908792642/badges?limit=100)): Played 372.77M; Beat World 1 54.71M; World 2 15.53M (**72% lost**); World 3 10.96M; World 5 6.32M; World 10 3.26M. A "Beat a World" badge (92.66M) is above World 1 and World 9 is above World 8. **Our read:** worlds can probably be played out of order, so treat this curve as approximate.

**Other ladders:**

| Game | From | To | Share | Source |
|---|---|---|---|---|
| Eternal Towers of Hell | Played 9.63M | First tower 1.87M | 19.4% | [badges API](https://badges.roblox.com/v1/universes/3264581003/badges?limit=100) |
| Eternal Towers of Hell | First tower | 10 towers 279K; 100 towers 41.3K | 15%; 2.2% | same |
| Barry's Prison Run | Easy win 173.21M | Hard win 10.01M | 5.8% | [badges API](https://badges.roblox.com/v1/universes/3310460039/badges?limit=100) |
| Barry's, Alien Base | Easy win 19.7M | Hard win 742K | 3.8% | same |
| Tower of Hell | Newbie 67.49M | Pro 16.16M | 24% | [badges API](https://badges.roblox.com/v1/universes/703124385/badges?limit=100) |
| Chained Together | Joined 82.24M | Team win 175,193 | 0.21% | [badges API](https://badges.roblox.com/v1/universes/6153964325/badges?limit=100) |
| Parkour Legacy | Welcome 6.87M | Tutorial done 2.36M | 34% | [badges API](https://badges.roblox.com/v1/universes/170247232/badges?limit=100) |

**Our read**, four patterns:

1. **The first boundary is the biggest loss.** 38% before Speed Run 4's level 1; 23% between Running Head's stages 1 and 2; 72% between the Bike obby's worlds 1 and 2; 66% of Parkour Legacy joiners never finish the tutorial.
2. **Loss per stage then falls.** Mega Easy: 2.3% per stage in stages 5 to 10, 0.4% in stages 200 to 450.
3. **About half are gone within the first tenth.** Mega Easy 54% at stage 50 of 825; Speed Run 4 33% at level 5 of 30.
4. **A harder version keeps 4% to 24%** of the easier one's finishers.

### Checkpoints, stage counts and the paid skip

All **our read** from the curves.

- **Checkpoints.** A save at the end of every stage. The Roblox Wiki describes difficulty-chart obbies as having a checkpoint at every stage ([Roblox Wiki: Obby](https://roblox.fandom.com/wiki/Obby)); Mega Easy autosaves. No checkpoints only works with short rounds that pay for partial progress, as Tower of Hell does. Spacing in studs: not known.
- **How many stages.** Stage 100 is seen by 37% of Mega Easy players, stage 450 by 8%. Stages 1 to 10 reach nearly everyone, so each is worth many times the effort of stage 300.
- **Where the skip sells.** At the cliffs: the first world boundary, single spikes like Speed Run 4's levels 16 and 27. No pass list contains a "skip stage" pass. The nearest: Running Head's "Ticket to teleport stages" 349 R$, the Bike obby's World Pass 399 R$, Mega Easy's Easy Mode 199 R$ (lava cannot kill you). Skip-stage product prices: not known, because the API does not list products.

**Start with:**

| Value | Start with | Reasoning |
|---|---|---|
| Widest normal gap | 6 to 7 studs edge to edge | 8.2 limit minus a 1 to 2 stud margin (our margin) |
| Gaps in stages 1 to 10 | 4 to 6 studs | Forum builders' easy spacing ([DevForum](https://devforum.roblox.com/t/obby-stage-ideas/644924), informal) |
| Tallest ledge without truss or coil | 6 studs | 6.4 stud jump height |
| Launch, short-stage obby | 100 stages | 37% of Mega Easy players reach 100; they are the next update's audience |
| Launch, long-level obby | 10 to 12 levels | Running Head reached 3.08B visits with 12 |
| New stages | 1 every 1 to 4 weeks for three months | Running Head's update log |
| Milestone badge | Every 5 stages and every level or world | Mega Easy, Speed Run 4 |
| Hard mode | Second version of existing courses; expect 4% to 24% of base finishers | Barry's, Tower of Hell |

### Eternal Towers of Hell: difficulty scale and building rules

The 11 named difficulties, easiest first: Easy, Medium, Hard, Difficult, Challenging, Intense, Remorseless, Insane, Extreme, Terrifying, Catastrophic, coloured from lime to white ([JToH wiki: Difficulty](https://jtoh.fandom.com/wiki/Difficulty)). Each tower gets a decimal rating; the first is 1.00 and the average is 5.93 ([Tower](https://jtoh.fandom.com/wiki/Tower)).

Building rules ([Tower Building and Submitting](https://jtoh.fandom.com/wiki/Tower_Building_and_Submitting)): 10 floors per tower; floors 100 x 100 x 100 studs (up to 175 x 100 x 175); 7,500 parts per tower; snap to 1 or 0.5 studs; no luck-based gameplay; consistent difficulty with no random spikes; little waiting; moving parts in sync; varied jumps; never submit a tower far above your own hardest clear.

Area gates mix a count with a skill check: World 1 asks for 3, 6, 10, 15, 22, 30, 39, 49, 60 towers, and ring 4 also needs 3 Hard and 1 Difficult tower ([Realm](https://jtoh.fandom.com/wiki/Realm)). Our arithmetic: the steps grow by 3, 4, 5, 7, 8, 9, 10, 11.

## What brings them back

**Later in the same session.** Tower of Hell draws a new tower from 330 sections each round; a secret section appears about once per 22.6 towers. Speed Run 4 gives each level its own song and look and hides 8 forbidden and 10 secret levels ([games API](https://games.roblox.com/v1/games?universeIds=83858907)).

**Tomorrow.** Not known. No daily reward was found. Saved progress (Mega Easy) is the only sourced reason to come back to the same place.

**Next week and after.** New stages and modes. Barry's added Lava Mode (25 Apr 2023), Alien Base (20 Sep 2024) and Lego (6 May 2025), each with easy, hard and leaderboard badges. **Our read:** each new mode reopens the whole funnel; a returning player is at level 1 of something again.

## Other players

| Sub-genre | Server | What players do together |
|---|---|---|
| Tower | 20 | Race one tower; each finisher speeds the clock for the rest |
| Stage obby | 12 to 30 | Climb side by side; no interaction documented |
| Tether | 15 or 30 | 2 to 5 players chained; hold E (PC), a pull button (phone) or R2 (console) to pull a partner up ([games API](https://games.roblox.com/v1/games?universeIds=6215464786)) |
| Rope climb | 24 | Press "Request rope" near a player; they request back to accept (Altitorture, [games API](https://games.roblox.com/v1/games?universeIds=4877714411)) |
| Tag | 40 | Climb, slide, roll, vault and swing; players vote on the variant ([games API](https://games.roblox.com/v1/games?universeIds=4864117649)) |
| Prison run | 12 | A VIP-only guard role catches runners (Barry's) |

Moving obstacles in tower games run on each player's own client, so one player cannot block them for another ([Roblox Wiki: Obby](https://roblox.fandom.com/wiki/Obby)). Not known: leaver handling, rope length, tag round length.

**Our read:** the clipped moment is the fall. At a 0.21% win rate, almost every Chained Together session ends with a group falling together, chain in shot. That is why both Chained games sell chain skins.

## Money

Passes API, 25 Nov 2026.

| Item | Game | R$ |
|---|---|---|
| Gravity Coil | Chained (2 Player) / Bike / Mega Easy / Speed Run 4 | 99 / 139 / 299 / 530 |
| Double Jump | Mega Easy / Running Head | 199 / 299 |
| Jetpack | Mega Easy / Running Head / Chained (2 Player) | 449 / 499 / 699 |
| Easy Mode | Mega Easy | 199 |
| Teleport stages | Running Head | 349 |
| VIP | Mega Easy / Speed Run 4 / Eternal Towers | 399 / 599 / 699 |
| Chain skins | Chained (2 Player) | 69 to 699 |
| Ladders, gliders | Steep Steps | 160 to 999 |
| Double Coins | Tower of Hell | 195 |

Sources: [Mega Easy](https://apis.roblox.com/game-passes/v1/universes/1261193936/game-passes?passView=Full&pageSize=100), [Bike](https://apis.roblox.com/game-passes/v1/universes/4908792642/game-passes?passView=Full&pageSize=100), [Speed Run 4](https://apis.roblox.com/game-passes/v1/universes/83858907/game-passes?passView=Full&pageSize=100), [Running Head](https://apis.roblox.com/game-passes/v1/universes/2274830359/game-passes?passView=Full&pageSize=100), [Chained](https://apis.roblox.com/game-passes/v1/universes/6215464786/game-passes?passView=Full&pageSize=100), [Steep Steps](https://apis.roblox.com/game-passes/v1/universes/4117341804/game-passes?passView=Full&pageSize=100), [Eternal Towers](https://apis.roblox.com/game-passes/v1/universes/3264581003/game-passes?passView=Full&pageSize=100). Find the Markers sells no passes and has 1,306 players after five years.

**Our read:** gravity coils cost 99 to 139 R$ in newer games and 299 to 530 in older ones; price new traversal passes near 100. Movement games sell tools that raise the skill ceiling (Parkour Legacy Grappler 500, Wingsuit 800), never skips.

**The line.** A skip is sold to a stuck, frustrated player. Show it as a priced button on the stage, always there, never as a pop-up that opens because the player just died. See [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

| Game | Cadence | Players now |
|---|---|---|
| Escape Running Head | A stage every 1 to 4 weeks at launch | 5.8K; peak 21K Aug 2026 ([RoWatcher](https://rowatcher.com/games/2274830359)) |
| Barry's Prison Run | A new mode every 7 to 14 months | 14,382; peak 65K Jul 2025 ([RoWatcher](https://rowatcher.com/games/3310460039)) |
| Tower of Hell | 7 new sections on 7 Aug 2026, the first since 2023 | 23,802 |
| Steep Steps | Says "every Saturday"; last update 25 Feb 2026 | 23 |
| Mega Easy Obby | Last update 3 Jan 2024 | 68 |

Find the Markers' marker badges by month ([badges API](https://badges.roblox.com/v1/universes/3056160040/badges?limit=100)): 69 at launch (Nov 2021), 43, 40, then 15, 25, 11, 12 through May 2022; later batches of 12 (Oct 2023), 11 (May 2025), and 2, 5, 7, 4 in 2026. Our arithmetic: 152 of the 256 badges in those months came in the first three. It has 377 badges in all.

**Our read:** a small team can hold one stage, or 5 to 10 collectibles, every 2 to 4 weeks. A large random pool can stand in for updates: Tower of Hell added no section between 2023 and August 2026 and has 23.8K players now.

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Near-zero players against a large visit count | Updates stopped (Mega Easy: 68 players, 1.73B visits) | A dated cadence you keep |
| A "weekly" game silent for months | Broken promise (Steep Steps, 23 players) | Promise only what you ship |
| 95%+ fall within a year of the peak | Trend spike with nothing to climb (Swing Obby for Brainrots; Chained (2 Player)) | A ladder that lasts: levels, modes, replay badges |
| 70%+ loss at the first world boundary | Too big a step (Bike obby: 72%) | Variety and the first reward before the boundary |
| 30%+ of joiners never clear stage 1 | First stage too long or hard (Speed Run 4: 38%) | Stage 1 cleared by 0:30 for 9 in 10 testers |
| Lost among hundreds of look-alikes | Clone saturation; reviewers fault formula titles and missing animations ([RoWatcher news](https://rowatcher.com/news/the-brainrot-invasion-how-absurd-meme-games-conquered-roblox-s-charts)) | One rule no other obby has |

## Checklist

1. No normal gap wider than 7 studs at default speed and jump.
2. No ledge above 6 studs without a truss, ladder or coil.
3. Gaps in stages 1 to 10 are 6 studs or less.
4. Widest jump tested on R6 and R15 and at low frame rate.
5. First jump within 5 s of spawning.
6. 9 in 10 testers clear stage 1 by 0:30.
7. Progress saves every stage, or rounds are under 10 minutes and pay for partial progress.
8. A badge or visible reward at least every 5 stages.
9. Your funnel loses under 25% from stage 1 to stage 2 (Running Head: 23%).
10. Launch with 10+ long levels or 100+ short stages.
11. New content dated every 1 to 4 weeks for three months.
12. A harder version of existing content by month two.
13. Traversal passes near 100 R$; every skip a priced button, never a death pop-up.
14. One thing a clip shows that no other obby has.

## Twists and open space

Twists that produced hits: ride something (Bike obby, 372.77M "played" badges); tie players together (Chained (2 Player), 42K peak); escape a chaser with a guard role (Barry's, 4.81B visits); random tower and shared clock ([Tower of Hell](../teardowns/tower-of-hell.md), 29.5B visits); reward falling (Altitorture, 65.77M "Rock Bottom"); search instead of jump (Find the Markers, 989.6M visits); +1 per step ([plus-one.md](plus-one.md)).

Open space, all **our read**:

- **A daily reason to return.** No leader has a sourced daily reward or weekly event.
- **Best obstacles first.** Stages 1 to 10 reach about 90% of a short-stage obby's players. Put the best ideas there.
- **Co-op that survives a leaver.** No tether game documents leaver handling; re-pairing within seconds is open.
- **Phone-first jumps.** No source has phone jump data. A game tested on touch first may face less competition than it looks.

## Sources

Not found in any source: stage length in seconds, checkpoint spacing in studs, phone-versus-keyboard jump differences, skip-stage prices, stage-obby session length, daily rewards, tag round structure, tether leaver rules.

- Teardown: [Tower of Hell](../teardowns/tower-of-hell.md). Related: [plus-one.md](plus-one.md), [foundations/14-metrics-and-diagnosis.md](../foundations/14-metrics-and-diagnosis.md), [foundations/15-the-line.md](../foundations/15-the-line.md).
- Roblox public API (games, votes, passes, badges), 25 Nov 2026, linked per game above.
- Roblox creator docs: [Humanoid](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml), [StarterPlayer](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/StarterPlayer.yaml), [Workspace](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Workspace.yaml).
- Wikis: [Tower of Hell](https://tower-of-hell.fandom.com/wiki/Home), [JToH](https://jtoh.fandom.com/wiki/Difficulty), [Roblox Wiki: Obby](https://roblox.fandom.com/wiki/Obby).
- Peaks: [RoWatcher](https://rowatcher.com/games/703124385), one third-party tracker whose pages sometimes disagree with themselves.
