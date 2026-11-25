# Feel and feedback

This page is about the half-second after the player does something: what they hear, what moves, what number appears, and how fast. It also covers the physics every Roblox game starts with, combat timing, lag, and the cheap phone most of your players hold. Open it when your game works but feels flat, when players say combat is "laggy", or before you test on a phone. The rule of the page fits in one line: **every action answers with a sound, a movement and a number, and the answer starts within a tenth of a second.**

## What is known

### Why a tenth of a second

A secondary source on Steve Swink's book *Game Feel* says a correction cycle under about 100 ms feels responsive and about 240 ms is an average human reaction cycle ([PocketGamer.biz](https://www.pocketgamer.biz/best-of-british-stephen-morris-considers-the-split-second-timings-needed-for-intuitive-controls), [Liz England review](https://lizengland.com/blog/wp-json/wp/v2/posts/1812)). It has not been checked against the book. Roblox gives 16.67 ms as the frame budget at 60 FPS ([Design for performance](https://create.roblox.com/docs/en-us/performance-optimization/design)).

Our arithmetic: 100 ms is 6 frames at 60 FPS. The answer to a click has to start on one of the next 6 frames.

### Timing numbers from outside Roblox

None of these come from Roblox games. They come from interface design, fighting games and academic studies of game effects. Use them as starting points.

| Topic | Number | Source |
|---|---|---|
| Interface animation | Most run 100 to 500 ms, longer for bigger moves | [NN/g, Animation duration](https://nngroup.com/articles/animation-duration) |
| Modal window | 200 to 300 ms | NN/g, same page |
| Exit versus entrance | Exits shorter: for example appear in 300 ms, leave in 200 to 250 ms | NN/g, same page |
| Instant response | Under 150 ms; large moves 250 to 500 ms | [SAP Fiori motion](https://www.sap.com/design-system/fiori-design-web/v1-120/foundations/visual/motion-design) |
| Hit-stop (freeze on hit) | Illustrative scheme: 8 / 12 / 16 frames for light / medium / heavy. Projectiles give the attacker no hit-stop. | Capcom Street Fighter V column, read only through a search snippet ([Capcom](https://game.capcom.com/cfn/sfv/column/131545?lang=en)) |
| Camera shake | Shake = trauma², trauma kept between 0 and 1, applied to offset and rotation, sampled from noise, trauma decays over time. The talk's own constants are not known. | Eiserloh, GDC 2016 ([GDC Vault](https://gdcvault.com/play/1023146/Math-for-Game-Programmers-Juicing)), via [community implementations](https://godotengine.org/asset-library/asset/735) |
| Hit flash, recoil | White flash for "a frame or two"; recoil of "a few pixels" | [Pichlmair and Johansen 2020 survey](https://ar5iv.arxiv.org/html/2011.09201) |
| Gravity in platformers | Super Meat Boy 41 m/s², Super Mario Bros. 91.28 m/s², Earth 9.8 | same survey |
| Jump buffer | Super Mario 1 to 2 frames; Braid 0.23 s | same survey |
| Fair danger | Disc Room switches lethal hitboxes on up to 50 ms late | same survey |
| How much effect | Medium and high effect levels beat both none and extreme on experience, motivation, play time and performance (Kao 2020) | same survey |
| Effect versus skill | A version with more effects was rated higher but players performed worse (Juul and Begy) | [summary](https://adk.elsevierpure.com/en/publications/good-feedback-for-bad-players-a-preliminary-study-of-juicy-interf) |
| Vibration | Haptic effects improved experience at both effect levels (Breakout, 38 players) | [Waterloo Haptic Lab](https://uwaterloo.ca/haptic-experience-lab/projects/juicy-haptic-design-vibrotactile-embellishments-can-improve) |

Our arithmetic: at 60 FPS, Capcom's 8 / 12 / 16 frames are 133 / 200 / 267 ms. Trauma² means small hits barely shake and big ones shake hard: trauma 0.3 gives 9% of maximum shake, 0.6 gives 36%, 0.9 gives 81%. Three light hits in a row (0.3 each) reach 0.9 and shake nine times as hard as one.

**Our read:** the studies point the same way. No effect loses. Some effect wins. Too much effect makes players worse at the game. Aim for the middle and test.

### Roblox physics defaults

| Setting | Default | Source |
|---|---|---|
| WalkSpeed | 16 studs/s | [Humanoid reference](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml) |
| JumpPower | 50 (used, because UseJumpPower is true by default) | same |
| JumpHeight | 7.2 studs (used only when UseJumpPower is false) | same |
| MaxSlopeAngle | 89 degrees | same |
| Gravity | 196.2 studs/s² | [Workspace reference](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Workspace.yaml) |

**The jump, worked out** (our arithmetic on these defaults):

| | JumpPower 50 | JumpHeight 7.2 |
|---|---|---|
| Launch speed | 50 studs/s | 53.2 studs/s |
| Highest point | 50² / (2 x 196.2) = 6.4 studs | 7.2 studs |
| Time in the air | 2 x 50 / 196.2 = 0.51 s | 0.54 s |
| Flat distance at WalkSpeed 16 | 16 x 0.51 = 8.2 studs | 8.7 studs |

**The warning.** This is projectile maths, not a Roblox measurement. Developers report that jump distance changes with frame rate and with avatar type, R6 or R15 ([DevForum](https://devforum.roblox.com/t/jumping-off-a-trusspart-is-affected-by-fps-and-avatar-type/3292004)), and a beta physics controller once made jumps feel harder in Studio ([DevForum](https://devforum.roblox.com/t/jumping-in-roblox-studio-became-a-lot-more-difficult/2017588)). A third-party blog claims 10 to 12 studs, which conflicts with the maths. Build a gap-test place and measure before you set your gaps. Forum builders space easy jumps 4 to 6 studs apart ([DevForum](https://devforum.roblox.com/t/obby-stage-ideas/644924)). Differences between phone and keyboard jumping were not found.

### Combat feel

**The Strongest Battlegrounds, community-reported.** These numbers come from a guide site relaying the community wiki, not from the developers ([rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/ragdoll-cancel-and-evasive)).

| Part | Number |
|---|---|
| Basic combo (M1) | Up to 4 hits at 3%, 3%, 4%, 4% of health; the 4th hit always ragdolls |
| M1 start-up | 9 to 15 frames |
| Knockdown (ragdoll) | 2 s; clash ragdoll about 3 s |
| Stun immunity after a ragdoll | 0.5 s |
| Dash cooldowns | Side 2 s (about 3 tiles); forward and back share 5 s (4.5 tiles) |
| Forward dash start | 0.15 s at 150 ms latency |
| Block | 180 degree arc in front; no perfect-block window published |

See the [TSB teardown](../teardowns/the-strongest-battlegrounds.md) for the rest of the game.

**Parry windows in two games.**

| Game | Window | If you miss | If you hit | Source |
|---|---|---|---|---|
| Blade Ball | 500 ms | 2 s cooldown | The ball retargets and speeds up "slightly"; it turns red when it targets you | [Blade Ball wiki](https://bladeball.fandom.com/wiki/Gameplay) |
| Combat Warriors | About 0.5 s | You are stunned about 1.5 s; parry recharges in about 3 s | Enemy stunned 3 s (no moving, no inventory); parry recharges in about 1 s | [Combat Warriors wiki](https://combat-warriors.fandom.com/wiki/Parry) (wiki wording: "about") |

Our arithmetic on Combat Warriors: a hit gives you 3 s of free action and costs 1 s of recharge; a miss costs you 1.5 s of helplessness and 3 s of recharge. The swing between outcomes is 4.5 s, so a parry is a real bet. Both games landed on half a second.

**Lag, from developer forum threads.**

- Public servers sampled in Blox Fruits and Jujutsu Shenanigans showed pings of 43 to 182 ms on 25 Nov 2026 ([servers API](https://games.roblox.com/v1/games/2753915549/servers/Public?limit=100&sortOrder=Desc)).
- One developer runs each ability on the client at once, then asks the server to confirm; on disagreement the client rolls back. The author says problems start around 100 ms ping, and even 50 ms felt delayed in a friends' test ([DevForum 4175630](https://devforum.roblox.com/t/writing-a-client-based-combat-system/4175630)).
- The same thread reports an Ultimate Battlegrounds trick: knock back a copy of the victim on the attacker's screen, then resync after landing. Stacking knockback on a victim already flying broke it.
- A hitbox thread prefers spatial queries (GetPartsBoundInBox) to Touched, gives an example hitbox of 4.6 x 4 x 5.75 studs, and suggests timestamp lag compensation with a capped rollback window. Its claims about TSB itself are unverified ([DevForum 3623640](https://devforum.roblox.com/t/creating-a-battlegrounds-like-hitbox/3623640)).
- The Roblox fan wiki lists ping-dependent hit detection among TSB's criticisms ([Roblox wiki: TSB](https://roblox.fandom.com/wiki/The_Strongest_Battlegrounds)).

Our arithmetic: at 182 ms ping, a hit that waits for the server answers in 182 ms or more, nearly double the 100 ms target. The only way to answer in time is to play the sound and animation on the attacker's own screen first and let the server decide the damage.

### Sound as a selling point

+1 Speed Keyboard Escape's description sells its keyboard and candy sounds as "ASMR vibes" ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=9584852943)). It sells an Unlock Soundpacks pass for 85 R$ and once sold a celebrity keycaps soundpack, now off sale ([passes API](https://apis.roblox.com/game-passes/v1/universes/9584852943/game-passes?passView=Full&pageSize=100)). It is rated 96.7% positive and had 18.6K players on 25 Nov 2026, against 83.1% and 3.8K for Escape Tsunami For Brainrots, a similar game built on frantic collection. **Our read:** the calm sound loop may be part of that gap. Nothing measured it.

Sound is also sold one effect at a time. Battlegrounds games sell a custom kill sound for 199 R$ ([TSB passes API](https://apis.roblox.com/game-passes/v1/universes/3808081382/game-passes?passView=Full&pageSize=100)). Blue Lock: Rivals sells a goal sound, a steal sound and a save sound for 149 R$ each ([Rolimons](https://www.rolimons.com/game/18668065416)). Type Soul cut one effect's volume by 30% in a patch ([Gamezebo](https://www.gamezebo.com/walkthroughs/type-soul-update-log/)).

No source measured sound or feel in the hits, or gave number-popup timings.

### The phone

| Fact | Number | Source |
|---|---|---|
| Android share of a typical game's players | About 65% | [Test on hardware](https://create.roblox.com/docs/en-us/performance-optimization/test-on-hardware) |
| Android memory | 60% have 2 to 4 GB, 35% 4 to 8 GB, 5% over 8 GB | same |
| Device speed | Over 50% of players score 10,000 to 20,000 on Passmark | same |
| Roblox's suggested test phones | Infinix Smart 9, Motorola Moto G05, Oppo A18, Amazon Fire HD 10 (2023), plus a Galaxy S22 Ultra | same |
| Overheating | Watch for frame rate dropping over a 10 to 15 minute session | same |
| Device mix, a different count | 44% of players use mobile and PC, 40.76% PC only, 11.55% mobile only, 3.69% console (17,000+ games) | [GameAnalytics 2026 Roblox report](https://www.gameanalytics.com/reports/2026-roblox-report) |
| Frame budget | Under 16 ms CPU per frame for 60 FPS; server memory under 50% | [Performance dashboard](https://create.roblox.com/docs/en-us/production/analytics/performance) |
| Textures | Small on-screen images rarely need more than 512 x 512; minor ones under 256 x 256. Shadows are off below graphics quality 4. | [Memory docs](https://create.roblox.com/docs/projects/performance-optimization/memory) |
| Simulator | Studio's Performance Simulator covers Android and iOS at 2, 3, 4, 6, 8 and 12 GB; Roblox advises testing 2 or 3 GB with heavy background load | [DevForum, Nov 2026](https://devforum.roblox.com/t/test-graphics-and-memory-on-lower-end-devices-with-the-performance-simulator/4979313) |

Our arithmetic: 65% x 60% means about 39% of a typical game's players are on an Android phone with 2 to 4 GB. The two device counts measure different things (share of players by platform, against devices each player uses), so do not add them.

One phone trap from a hit: MM2 players cannot prestige on mobile; they need tablet mode ([MM2 wiki](https://murder-mystery-2.fandom.com/wiki/Prestige)). A feature that exists only on PC is a feature 11.55% to 65% of players never see.

**Touch targets.** No source found gives Roblox touch-target sizes. **Our read:** make every phone button at least as large as the default Roblox jump button, with 2 to 3 button widths between buttons that do opposite things (buy and close, attack and block).

## The rules

1. **Three answers to every action: a sound, a movement, a number.** Reason: each one reaches a different player. The muted phone player sees the motion; the player looking at their character hears the sound; the player planning reads the number.
2. **The answer starts within 0.1 s (6 frames at 60 FPS).** Swink's secondary 100 ms figure. For anything the server must decide, play the sound and motion on the client first.
3. **Interface: open in 0.2 to 0.3 s, close faster.** NN/g's modal range and its exit-shorter-than-entrance rule. **Start with:** open 0.2 s, close 0.15 s, button press 0.08 s.
4. **Hit-stop scales with the hit and stays short.** **Start with:** 0.05 / 0.08 / 0.13 s (3 / 5 / 8 frames) for light / medium / heavy. Capcom's example is 133 to 267 ms for a 1v1 game. **Our read:** in a 15-player free-for-all where others keep moving, the shorter end feels less like lag. No Roblox source measured this.
5. **Shake = trauma², decaying in 0.3 to 0.5 s.** **Start with:** each light hit adds 0.25 trauma, a heavy hit 0.5, trauma falls by 2 per second. Never shake on interface actions.
6. **Medium effects, not maximum.** Kao's study: medium and high beat none and extreme. Juul and Begy: heavy effects can lower performance. Cut any effect that hides the next threat.
7. **Gaps measured, not guessed.** **Start with:** 4 to 6 studs for normal jumps, 7 studs as the hardest unaided jump, never above 8. The default jump is 8.2 studs on paper. Measure in a gap-test place with R6 and R15 at 30 and 60 FPS.
8. **Parry: half a second, with a cost on both sides.** Blade Ball and Combat Warriors both use 0.5 s. **Start with:** 0.5 s window, 1.5 s stun on a miss, 3 s enemy stun on a hit.
9. **Danger switches on late, not early.** Disc Room's lethal hitboxes start up to 50 ms late. **Start with:** 50 ms delay on any hitbox that kills, so a player who saw it coming is not killed by a frame they never saw.
10. **Design for 182 ms.** The worst sampled public ping. **Start with:** a server rollback cap of 0.2 s and a hitbox 10% to 20% wider on the server than the visual, with a distance check against cheating.
11. **Sound is worth paying for.** One hit game sells itself on it; others sell single sounds at 149 to 199 R$. Every core verb gets its own sound, recorded or picked, not a default.
12. **Build and test for a 2 to 4 GB Android phone.** About 39% of players. Textures 512 or less, streaming on, a 15-minute soak test.

## How to do it

1. **Fill in the feedback table** below for every action in your [core loop table](../kit/templates/core-loop-table.md). Any empty cell is a bug.
2. **Run the three tests**, each with a stopwatch and a notepad:
   - **Mute the game.** Play 5 minutes with sound off. Every action must still show what happened. Write down each moment you were unsure.
   - **Close your eyes.** Have someone else play for 2 minutes while you listen only. Can you tell a hit from a miss, a buy from a failed buy, a rare drop from a common one? Each sound you cannot tell apart needs to change.
   - **Hand it to a stranger.** Someone who has never seen the game, on a phone, with no explanation. Time how long until their first core action. Roblox's own onboarding example found most testers pressed the plant button within 10 seconds, so a hint at 11 seconds only reaches stuck players ([Onboarding techniques](https://create.roblox.com/docs/en-us/production/game-design/onboarding-techniques)). If your stranger takes over 10 seconds, the feedback is not pointing at the verb.
3. **Measure the jump** in a gap-test place: platforms 4, 5, 6, 7, 8 and 9 studs apart, tried 10 times each with R6 and R15. Keep normal gaps at least 1.5 studs under the widest gap that passes 10 of 10.
4. **Test lag** with Studio's network settings at 150 ms or more. Every hit must still play its sound and motion within 0.1 s on the attacker's screen.
5. **Test the phone** in the Performance Simulator at 2 GB, then on one real low-end phone from Roblox's list, for 15 minutes. Note the frame rate at minute 1 and minute 15.
6. Write your fixes into the [design audit](../kit/design-audit.md).

### Feedback table (fill in)

The first rows are **Start with** examples. Replace them with your own and add one row per action.

| Action | Sound | Motion | Number | Delay |
|---|---|---|---|---|
| Collect a coin | Short high tick, pitch up 5% per coin in a quick chain | Coin flies to the counter in 0.3 s; counter scales to 1.15 for 0.08 s | "+1" rises 3 studs and fades in 0.6 s | Under 0.1 s |
| Buy a unit | Lower, longer "ka-ching" | Unit appears with a 0.2 s pop; button presses in 0.08 s | Price shown leaving the counter | Under 0.1 s |
| Hit an enemy | Impact layered under a whoosh | Target flashes white 1 to 2 frames; hit-stop 0.05 s | Damage number above the target | Under 0.1 s on the attacker's screen |
| Rare drop | A sound used for nothing else | Light column, 0.5 s camera push-in | Rarity name and odds | Reveal no longer than 2 s |
| Failed action | Dull low thud | Button shakes left-right 2 times in 0.2 s | Reason in 3 words or fewer | Under 0.1 s |
| | | | | |
| | | | | |
| | | | | |

## Checks

| Check | Pass |
|---|---|
| Coverage | Every action in the core loop has a sound, a motion and a number |
| Delay | Each answer starts within 0.1 s, measured from a frame-by-frame screen recording |
| Interface | Windows open in 0.3 s or less and close faster than they open |
| Mute test | A muted player can tell every outcome apart |
| Eyes-closed test | A listener can tell hit from miss, buy from fail, rare from common |
| Stranger test | A stranger on a phone makes the first core action within 10 s |
| Jump | Normal gaps 1.5 studs or more under the measured widest gap; tested in R6 and R15 |
| Lag | At 150 ms simulated ping, hits still answer within 0.1 s on the attacker's screen |
| Parry | Window, miss cost and hit reward are written as numbers |
| Shake | Light hits shake under 10% of maximum; interface never shakes |
| Phone | 15 minutes on a 2 to 4 GB Android phone with no crash and no more than a 10-frame drop |
| Feature parity | Nothing a PC player can do is impossible on a phone |

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| "The game feels laggy" at normal ping | The client waits for the server before showing anything | Play sound and motion on the client; server confirms damage |
| Hits that "didn't register" | Server hitbox the same size as the visual, no lag compensation | Widen the server hitbox 10% to 20%; timestamp rollback capped at 0.2 s |
| Players miss jumps that look easy | Gaps set from the 8.2-stud paper limit | Measure; keep normal gaps 4 to 6 studs |
| Screen is unreadable in fights | Shake and particles on every hit at full strength | Trauma²; cap particles; medium effects |
| Menus feel slow | Open and close animations over 0.5 s, or exits as long as entrances | Open 0.2 s, close 0.15 s |
| Buying feels like nothing happened | Number changes with no sound or motion | Pop, sound and a number leaving the counter |
| Players on phones quit in the first minutes | Crashes from memory, or buttons too small | 2 GB simulator test; textures 512 or less; bigger buttons with space between |
| A feature nobody uses | It exists only on PC, as MM2 prestige did on phone | Test every feature on a phone |
| Every action sounds the same | One default click for everything | One sound per verb; a rare sound used only for rare events |

## Sources

Every fact links its source inline. The groups: Roblox Creator Docs ([Humanoid](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml), [Test on hardware](https://create.roblox.com/docs/en-us/performance-optimization/test-on-hardware)); DevForum threads on combat, hitboxes, jumps and the Performance Simulator; non-Roblox sources (NN/g, SAP Fiori, Capcom, GDC, [Pichlmair and Johansen 2020](https://ar5iv.arxiv.org/html/2011.09201)); game wikis and guides (TSB community-reported, Blade Ball, Combat Warriors, MM2); Roblox public API, 25 Nov 2026; and the [GameAnalytics 2026 Roblox report](https://www.gameanalytics.com/reports/2026-roblox-report).

Next: [11-clips-and-packaging.md](11-clips-and-packaging.md).
