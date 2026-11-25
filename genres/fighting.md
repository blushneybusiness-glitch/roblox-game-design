# Fighting and battlegrounds

> **The feeling sold:** "I pick a hero, I land a combo, and everyone in the server sees me win."

This page covers free-for-all battlegrounds (The Strongest Battlegrounds, Jujutsu Shenanigans, Heroes Battlegrounds), weapon brawlers (Combat Warriors, Slap Battles), a boxing game (Untitled Boxing Game) and Blade Ball. Numbers marked "Roblox public API, 25 Nov 2026" were read from Roblox's own game, pass, vote and badge endpoints that day. Combat timings for these games are community figures. **No developer-stated combat timing (hit-stop, parry window, stun length, i-frames) was found for any game on this page.** The first-minute flow of The Strongest Battlegrounds, Jujutsu Shenanigans and Heroes Battlegrounds was not documented by any source either.

## At a glance

| | |
|---|---|
| Core verb | Hit: a 4-click light-attack string, then a dash or a skill |
| Study these first | [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md): the clearest template, 10 of its characters free, kill badges in powers of 10. Jujutsu Shenanigans: the largest battlegrounds game now, with skills on keys 1 to 4 and saved builds. Combat Warriors: the only wiki-stated parry numbers and a daily spin with published odds. Heroes Battlegrounds: a PvE boss and mastery quests next to the PvP. |
| Session that works | 11 to 16 minutes: TSB 12.2, JJS 16.2, Blade Ball 13.5, UBG 11.5 ([Rotrends](https://rotrends.com/game/3808081382)) |
| Players per server | 15 to 22 for the battlegrounds (TSB 15, HB 15, Blade Ball and Slap Battles 16, JJS 20, UBG 22); Combat Warriors 35 ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=994732206,1451439645,3808081382,4568630521,4777817887,2380077519,3508322461,6161049307,4730278139,1359573625,1390601379)) |
| Who owns the genre | Two 2022 games. JJS (created April 2022) had 75,272 players and TSB (August 2022) 44,365 on 25 Nov 2026. The 2023 entrants are far smaller: Legends Battlegrounds 5,201, Heroes Battlegrounds 2,920 ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=3808081382)). Blade Ball (2023) peaked near 150K and holds about 15.7K. |
| Build cost | Not known. What makes it expensive: each character is a full moveset (TSB lists 176 techniques, 33 for one character alone, [Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds/techniques)), and hit detection has to work at 100 to 200 ms ping. |
| Money comes from | Early-access characters (245 to 345 R$), private servers and VIP (299 to 799 R$), cosmetic passes (95 to 199 R$) |
| What kills clones | Long gaps between characters, and fights that feel decided by ping or by three players ganging on one. |

## Why people play it

Who plays (ages, devices) is not known. What the sources show: TSB gives 10 characters away, and no pass in TSB, JJS, Heroes Battlegrounds or Legends Battlegrounds sells damage ([TSB passes](https://apis.roblox.com/game-passes/v1/universes/3808081382/game-passes?passView=Full&pageSize=100)). Skill is named: TSB players trade "techs" such as "Curve Dash", 4 light attacks then a side dash ([Bloxodes techniques](https://bloxodes.com/wiki/the-strongest-battlegrounds/techniques)). JJS reached #2 on the Top Trending chart ([Rotrends](https://rotrends.com/game/3508322461)).

Ratings on 25 Nov 2026: TSB 83.7%, JJS 86.3%, Heroes Battlegrounds 85.5%, Combat Warriors 83.4%, Blade Ball 93.5% ([Roblox votes API, 25 Nov 2026](https://games.roblox.com/v1/games/votes?universeIds=3808081382,3508322461,994732206,4730278139,4568630521,1390601379,4777817887,2380077519,1451439645,648454481,1359573625,985731078,848145103,6161049307)). The fighters rate lower than the grind RPGs (Blox Fruits 92.3%).

**Our read:** the player wants to look good in front of 15 strangers within a minute of joining, with no grind in the way. Losing to a better player is accepted. Losing to lag or to a 3-on-1 is what drives the low ratings (see "How these games die").

## The loop, with a stopwatch

The Strongest Battlegrounds. Controls are from the game's own description ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=3808081382)). Timings are community wiki figures relayed by a guide, which itself says none are developer-published ([rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/ragdoll-cancel-and-evasive)).

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Close in | Double-tap W to run, Q to dash | Forward or back dash: 5 s cooldown. Side dash: 2 s | Character dashes about 3 to 4.5 "tiles" | Forward dash hit: 4% damage |
| Light-attack string | Hold left click | First hit starts in 9 to 15 frames, 0.15 to 0.25 s at 60 fps (our arithmetic) | 4 hits | 3%, 3%, 4%, 4% of health: 14% for the string |
| Ragdoll | The 4th hit lands | Knockdown 2 s, then 0.5 s of stun immunity | Target flies and lies down | Guaranteed on the 4th hit |
| Escape | The victim presses Q while ragdolled | Cooldown not stated | Ragdoll cancel | Combo ends |
| Block | Hold F | No perfect-block window published | 180 degree arc in front | Damage blocked |
| Awaken | Press G when the bar is full | 45 s of ultimate mode ([wiki](https://roblox.fandom.com/wiki/The_Strongest_Battlegrounds)); some characters have no timer | Bar fills from damage dealt | Meter: 200 (The Strongest Hero), 350 (most), 420 (Brutal Demon) ([rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/characters)) |
| Kill | Finish the target | Not known | Kill feed | +1 kill, +2 for a finisher ([Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds)) |

Seconds per kill and respawn time: not known.

**Our arithmetic:** at 14% per string, a target needs about 7 full strings to die, more if they block. A Black Flash (6 times a light attack, 24% on a mini uppercut or downslam, community figure) is worth almost two strings in one hit, which is why it is the clip moment.

**How the others differ.** JJS adds skills on keys 1 to 4, a special on R and save slots for builds ([JJS description](https://games.roblox.com/v1/games?universeIds=3508322461)). Combat Warriors uses weapons and a parry on F, in 30-minute free-for-all rounds ([wiki: Gamemodes](https://combat-warriors.fandom.com/wiki/Gamemodes)). Untitled Boxing Game is 1-on-1 boxing with stamina and 3 knockdowns per fight ([community guide](https://www.ofzenandcomputing.com/how-to-play-untitled-boxing-game/)). Blade Ball is round-based: a 15-second "Game Starting" banner, a mode vote, and rounds that usually end around the 4th or 5th deflection ([guide](https://allthings.how/roblox-blade-ball-how-to-play-full-guide/)).

**The loop stack:**

| Every | What finishes | Example |
|---|---|---|
| 0.15 to 0.25 s | A light attack lands | TSB start-up |
| 2 to 5 s | A dash is ready again; a ragdoll ends | TSB side dash 2 s, forward 5 s, knockdown 2 s |
| Not known | A kill or a death | Seconds per kill were not measured by any source |
| 45 s | An awakening runs out | TSB |
| 50 kills | An emote spin | TSB, or 25 R$ |
| One session (11 to 16 min) | A kill badge at 10 or 100 | Funnel below |
| 24 hours | Daily spin | Combat Warriors, from level 10 |
| Weekend | 2x XP and spin drops from kills, Friday to Sunday | Combat Warriors |
| Month | Monthly kill titles reset | TSB |

## The first five minutes

No source documents the first minute of TSB, JJS or Heroes Battlegrounds. What is known:

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | TSB: The Strongest Hero is already equipped | [rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/how-to-unlock-every-character) |
| 0:30 | TSB: the player is in the free-for-all arena with 14 others. Blade Ball: the player is spectating the round in progress | [Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds); [Blade Ball guide](https://allthings.how/roblox-blade-ball-how-to-play-full-guide/) |
| 1:00 | First damage dealt; the awakening bar has started to fill | Bloxodes describes this order; timing is **Our read** |
| 3:00 | Not known. The first kill is the first badge: 171.4M TSB players and 24.8M JJS players hold one | [TSB badges](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100); [JJS badges](https://badges.roblox.com/v1/universes/3508322461/badges?limit=100) |
| 5:00 | Not known | |

None of these games has a documented tutorial. Jujutsu Infinite, an anime fighter-RPG, does: 69.3% of players finished it (21.2M of 30.6M, [badges](https://badges.roblox.com/v1/universes/3808223175/badges?limit=100)).

**Gates for a new game (Our read, built from the above):**

- A fighter is equipped before the player can move. No menu first.
- The first hit lands within 30 seconds of spawn.
- A practice target with a real reward exists: Heroes Battlegrounds' PvE boss "The Prototype" has 14.3M defeats and UBG's sparring NPC 3.1M ([HB badges](https://badges.roblox.com/v1/universes/4568630521/badges?limit=100), [UBG badges](https://badges.roblox.com/v1/universes/4730278139/badges?limit=100)).
- No bots, protected spawn zones or skill matchmaking were documented for any of these games. Do not assume the leaders use them.

## Numbers that work

**Combat numbers (all community-reported, none developer-stated):**

| Game | Number | Source |
|---|---|---|
| TSB | Light string 4 hits, 3/3/4/4% (14%); start-up 9 to 15 frames | [rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/ragdoll-cancel-and-evasive) |
| TSB | Knockdown 2 s; roll-clash ragdoll about 3 s; stun immunity 0.5 s after ragdoll | same |
| TSB | Forward/back dash 5 s cooldown, 4.5 tiles; side dash 2 s, about 3 tiles | same |
| TSB | Critical Hit 3x a light attack; Black Flash 6x; Black Flash window about 4 s after a Critical Hit | same |
| Combat Warriors | Parry window about 0.5 s. Miss: you are stunned about 1.5 s, recharge about 3 s. Hit: enemy stunned 3 s, recharge about 1 s. A ragdolled player cannot recover until still for 2 to 3 s | [wiki: Parry](https://combat-warriors.fandom.com/wiki/Parry) |
| UBG | 0% stamina: stunned about 2 s. Block break: stunned about 2 s, then 70% of block restored. Perfect dodge opens the opponent about 5 s, cooldown about 8 s. Failed ultimate drops the meter to 70%. Counter 1.25x | [community guide](https://www.ofzenandcomputing.com/how-to-play-untitled-boxing-game/) |

Blade Ball parry windows appear on one guide site, but the page gives no source and contradicts itself, so they are not repeated here ([dungeonpath](https://dungeonpath.com/posts/blade-ball/deflect-parry-timing-guide/)).

**Our read on the parry:** in Combat Warriors a hit parry buys 3 s of free attack and a missed one costs 1.5 s. The reward is twice the risk, so trying is worth it, but the 3 s recharge stops a player from spamming F.

**Every combo has an exit.** TSB's ragdoll can be cancelled with Q; JJS lets Q "escape" a stun; Heroes Battlegrounds has a "recovery dash" ([JJS](https://games.roblox.com/v1/games?universeIds=3508322461), [HB](https://games.roblox.com/v1/games?universeIds=4568630521)); UBG caps a fight at 3 knockdowns.

**Progress without levels: the kill ladder.** TSB has no levels. Kills do not unlock characters. Kill totals unlock accessories and auras, monthly kill placement unlocks titles that reset each month, and private-server kills do not count ([rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/how-to-unlock-every-character)). The badges ([Roblox badges API, 25 Nov 2026](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100)):

| Kills | TSB holders | Share of 1-kill holders | Kept from the step before | Heroes BG kept | Combat Warriors kept |
|---|---|---|---|---|---|
| 1 | 171,392,111 | 100% | | | |
| 10 | 92,301,778 | 53.9% | 53.9% | 39.1% | 92.8% (from 1) |
| 100 | 32,438,447 | 18.9% | 35.1% | 30.1% | 83.8% |
| 1,000 | 10,019,762 | 5.8% | 30.9% | 17.8% | 47.6% |
| 10,000 | 1,091,741 | 0.64% | 10.9% | 2.8% | |
| 100,000 | 850 | | | | |
| 1,000,000 | 1 | | | | |

"Kept" columns are our arithmetic from the [HB](https://badges.roblox.com/v1/universes/4568630521/badges?limit=100) and [Combat Warriors](https://badges.roblox.com/v1/universes/1390601379/badges?limit=100) badges. Badge counts are lifetime and some badges were added after launch, so the ratios are indicative. Combat Warriors' badge base is small (1.77M first kills) and committed, which explains its gentle curve.

**Our read:** in TSB about half of the players who get one kill reach ten, then each 10x step keeps about a third, until 10,000, where only 1 in 9 continues. The 10-to-100 step loses 65% of players, so that gap is where a cosmetic unlock does the most work. TSB fills it with an emote spin every 50 kills.

**Robux price of a kill.** An emote spin costs 50 kills or 25 R$ ([Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds)). Our arithmetic: TSB prices one kill at 0.5 R$.

**Daily spin odds, Combat Warriors** ([wiki: Daily spin](https://combat-warriors.fandom.com/wiki/Daily_spin)): one free spin per 24 hours from level 10, or 49 R$ per spin. Uncommon 55%, Rare 42%, Epic 1.5%, Legendary 1%, Exotic 0.5%. A pity counter guarantees a rarity when full (the wiki's example: 75 of 75 for Epic). The two exotic weapons, Chainsaw and Dragon Slayer, can also be earned through weapon mastery.

**Our arithmetic:** Epic or better is 3%, so about 33 spins on average. Exotic is 1 in 200: 200 days of free spins, or 9,800 R$ at 49 R$ each, before pity. The mastery route gives a non-paying player a second road to the same weapon.

**Lag.** Sampled public servers in Blox Fruits and JJS showed 43 to 182 ms ping on 25 Nov 2026 ([servers API](https://games.roblox.com/v1/games/2753915549/servers/Public?limit=100&sortOrder=Desc)). The DevForum threads describe these approaches:

| Approach | Detail | Source |
|---|---|---|
| Client runs, server checks | The ability plays on the attacker's client at once; a remote asks the server to validate; on disagreement the server cancels the input and fixes cooldowns (full rollback rarely needed). Tested at 120 ms; the author says trouble starts near 100 ms, and 50 ms still felt delayed | [DevForum 4175630](https://devforum.roblox.com/t/writing-a-client-based-combat-system/4175630) |
| Knockback on a clone | The attacker's client hides the victim, predicts physics on a clone, then resyncs after landing. Works because ragdolls are long. Stacking knockback on a victim already flying broke it | same |
| Server-owned body | Server anchors the character, network owner set to nil, the owning client streams root position every frame | same |
| Spatial-query hitbox | GetPartsBoundInBox or GetPartsInPart over Touched. Example box 4.6 x 4 x 5.75 studs, offset 0.25 up and half its length forward. Timestamp lag compensation with a capped rollback window and distance checks against cheats. A wider box is "more forgiving" | [DevForum 3623640](https://devforum.roblox.com/t/creating-a-battlegrounds-like-hitbox/3623640) |

One poster claims TSB does all hit detection on the server; the thread itself says this is unverified.

**Start with** (each value from the tables above; tune it):

| Setting | Value | Why |
|---|---|---|
| Players per server | 15 | TSB and HB both use 15; JJS 20 |
| Light string | 4 hits at 3/3/4/4%, first hit in 0.15 to 0.25 s, forced ragdoll on hit 4 | TSB's community figures |
| Ragdoll | 2 s, then 0.5 s immunity, cancel on the dash key | Bounds every combo; 2 s also hides resync (DevForum) |
| Dashes | Side 2 s, forward 5 s | TSB |
| Parry (if used) | 0.5 s window; miss = 1.5 s self-stun; hit = 3 s enemy stun | Combat Warriors: reward 2x the risk |
| Ultimate | Fills from damage, lasts 45 s | TSB |
| Hitbox | About 4.6 x 4 x 5.75 studs, server validation, test at 120 ms | DevForum |
| Kill badges | 1, 10, 100, 1,000, 10,000 | All four ladders. Expect about 50%, 19%, 6%, 0.6% of first-killers to reach 10, 100, 1,000, 10,000 (TSB) |
| Cosmetic between 10 and 100 kills | One unlock every 25 to 50 kills | TSB's 50-kill spin sits in the 65% drop |
| Free roster | Most fighters free; each early-access fighter turns free after about 6 months | TSB: 10 of 12 playable characters free; Martial Artist about 6 months in early access |

## What brings them back

**Later in the same session.** The awakening bar (200 to 420 points, filled by damage) and kill-streak badges. Combat Warriors' streak badges at 5, 10, 15, 20 and 25 are held by 761,754, 277,259, 165,901, 114,277 and 85,775 players ([badges](https://badges.roblox.com/v1/universes/1390601379/badges?limit=100)). The next badge on the kill ladder is never more than 10 times away.

**Tomorrow.** Combat Warriors' daily spin (24 hours, from level 10). Blade Ball's daily login runs Day 1 to Day 5 ([guide](https://allthings.how/roblox-blade-ball-how-to-play-full-guide/)). Combat Warriors also sells "Unlimited Daily Quests" for 249 R$, so it has daily quests ([passes](https://apis.roblox.com/game-passes/v1/universes/1390601379/game-passes?passView=Full&pageSize=100)).

**Next week and after.** Combat Warriors gives 2x XP and a chance of daily spins from kills every Friday, Saturday and Sunday ([description](https://games.roblox.com/v1/games?universeIds=1390601379)). TSB resets monthly kill titles. New characters arrive in early access and turn free months later. Heroes Battlegrounds unlocks "mastered" characters through quests: 179K to 2.79M players hold each mastery badge ([badges](https://badges.roblox.com/v1/universes/4568630521/badges?limit=100)). Combat Warriors masters heavy weapons for the Dragon Slayer and light weapons for the Chainsaw.

## Other players

- **Server size.** 15 to 22 in one shared arena; JJS servers sampled at a median of 18 of 20 on 25 Nov 2026. Combat Warriors runs 35.
- **What a player sees.** Everyone in one free-for-all, a kill feed, auras and accessories that show a kill total.
- **What they can do.** Fight anyone. TSB adds ranked 1v1, 2v2 and 3v3; no point values were found ([Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds)). Combat Warriors adds King of the Hill (called the most popular mode), Capture the Flag and team modes where teammates can revive and carry each other ([wiki](https://combat-warriors.fandom.com/wiki/Gamemodes)).
- **What can be lost.** Nothing permanent. A death costs a streak.
- **The known problem.** TSB's free-for-all produces 2v1 and 3v1 fights, and its wiki lists this as a criticism ([wiki](https://roblox.fandom.com/wiki/The_Strongest_Battlegrounds)).
- **The clip.** A named tech, a Black Flash, a comeback during an awakening. In Slap Battles the clips come from secret badges: "Error glove" (1.66M holders), "be a rock for 15 minutes straight" (2.9M), "you met the owner" (48.6K) ([badges](https://badges.roblox.com/v1/universes/2380077519/badges?limit=100)).

## Money

| Pass | TSB | JJS | Heroes BG | Legends BG |
|---|---|---|---|---|
| Early access character | 299 | 345 | 245 | 299 |
| Private server tier | 499 | | 499 (commands) | 399 |
| VIP | 299 | | 799 | 399 |
| Kill sound | 199 | 120 | 199 | 199 |
| Emote slots / pages | 99, 99 | 175 | 95 | 99 |
| Awakening outfit | 99 | 115 | | 99 |
| Other | | Build saves 125 | Move text 199, toxic emotes 95 | Skill text 99, kill message 99, auto claim 99 |

All prices in R$ ([Roblox public API, 25 Nov 2026](https://apis.roblox.com/game-passes/v1/universes/5265857965/game-passes?passView=Full&pageSize=100); [TSB](https://apis.roblox.com/game-passes/v1/universes/3808081382/game-passes?passView=Full&pageSize=100), [JJS](https://apis.roblox.com/game-passes/v1/universes/3508322461/game-passes?passView=Full&pageSize=100), [HB](https://apis.roblox.com/game-passes/v1/universes/4568630521/game-passes?passView=Full&pageSize=100)).

The four share one template: early access 245 to 345, private server 399 to 499, VIP 299 to 799, cosmetics 95 to 199. Others: Blade Ball VIP and Double Coins 240 each; Combat Warriors Gold 999; UBG Dual Gloves 399; Slap Battles sells glove abilities (OVERKILL 450). Top Earning chart: Blade Ball #17, JJS #26 ([Rotrends](https://rotrends.com/game/4777817887)). Developer product prices and where offers appear: not known.

**Our read:** early access is a head start that gets sold again with every new character. TSB's Tech Prodigy sat in early access from 21 Dec 2024 to 17 May 2026, about 17 months; Martial Artist about 6 ([rblxguide](https://rblxguide.com/games/the-strongest-battlegrounds/updates/how-to-unlock-every-character), community dates that partly contradict each other).

**Policy points.** TSB's description says emotes and spins are random with "equal chance" and no duplicates. UBG styles roll from 5 rarity tiers, with the top "Shiny" tier at 0.007%, 1 in 20,000 spins (community figure). Combat Warriors sells luck passes that raise Epic and above. Any paid roll, or a pass that improves one, falls under Roblox's paid-random-item rules: see [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

- **TSB** promised an update every 2 to 3 weeks; gaps often run a month or more, and one, before the KJ update, was close to 4 months ([wiki](https://roblox.fandom.com/wiki/The_Strongest_Battlegrounds)). Listed events: KJ update 21 to 28 Dec 2024, an update 16 to 25 May 2026, "The Arsenal" 24 to 30 Oct 2026, Halloween 1 to 22 Nov 2026. During the summer event a Crab Boss spawned every 30 minutes ([Bloxodes](https://bloxodes.com/wiki/the-strongest-battlegrounds)).
- **Last updates before 25 Nov 2026:** TSB 24 Nov, Blade Ball and Slap Battles 22 Nov, JJS 16 Nov, Combat Warriors 15 Nov ([Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=3508322461,4777817887,2380077519,1390601379,1451439645,648454481,1359573625,3419284255,3808223175,6161049307,985731078,848145103,4871329703,4093155512)).
- **Event spikes.** TSB averaged 52,423 players in October 2026 and peaked at 87,610 on 25 Oct, during The Arsenal. JJS averaged 130,620 with a daily high of 299,410 on 24 Oct ([Bloxodes Oct 2026](https://bloxodes.com/stats/reports/roblox-october-2026)). On 25 Nov JJS was at 75,272.
- **What a small team can sustain.** Not known from the sources. **Our read:** one new character with 10 to 30 techniques is the unit of content here, so plan the early-access window around how long one character takes you to build.

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Players fall about 90% from peak within months | One mechanic, little new to master. Blade Ball peaked near 150K and held 15,709 on 25 Nov 2026 | New modes and abilities on a fixed rhythm, before the drop |
| Update gaps of 4+ weeks against a promise of 2 to 3 | Characters take longer than planned (TSB) | Promise a rhythm you can keep; run timed events between characters |
| Low rating, complaints of "unfair" | 2v1 and 3v1 in free-for-all (TSB) | Ranked or team modes; a short protection after respawn (**Our read**) |
| Complaints that hits did not land | Hit detection depends on ping (TSB criticism) | Client prediction with server validation, test at 120 ms (DevForum) |
| Cheaters in public servers | No visible anti-cheat (TSB criticism) | Server distance and timestamp checks |
| Kill funnel steeper than TSB's | HB keeps 2.1% of first-killers to 1,000 kills against TSB's 5.8% | A PvE path and cosmetics between 10 and 100 kills |
| Near-zero players after a pause | Type Soul (a fighter-RPG) went private and came back on 16 Jul 2026 with a new team; 29 players on 25 Nov 2026 | Do not stop; a return after a year starts from nothing |

## Checklist

- [ ] A fighter is equipped before the player can move.
- [ ] First hit possible within 30 seconds of spawn.
- [ ] Light string of 3 to 5 hits ends in a ragdoll of about 2 s.
- [ ] Every combo can be escaped: a dash-cancel plus at least 0.5 s of immunity after a ragdoll.
- [ ] Dash cooldowns between 2 and 5 seconds.
- [ ] Hits tested at 120 ms simulated ping and still register.
- [ ] Server size between 12 and 22.
- [ ] At least 3 of every 4 fighters free (TSB: 10 of 12); nothing sold adds damage.
- [ ] Kill badges at 1, 10, 100, 1,000 and 10,000.
- [ ] A cosmetic unlock at least every 50 kills.
- [ ] Early access price between 245 and 345 R$, with a date when it turns free.
- [ ] Cosmetic passes at 95 to 199 R$; private server at 399 to 499 R$.
- [ ] Any paid roll shows odds that sum to 100%.
- [ ] A practice target or PvE boss that gives real rewards.
- [ ] An update or event at least every 3 weeks.

## Twists and open space

**Already produced hits:** a destructible arena (JJS credits Combat Mayhem, [description](https://games.roblox.com/v1/games?universeIds=3508322461)); one shared homing ball that speeds up (Blade Ball, 16 players); gloves bought with "slaps" earned by slapping (Slap Battles); boxing with 28+ rolled styles in 5 tiers (UBG, community count); PvE inside PvP (Heroes Battlegrounds' Prototype, 14.3M defeats).

**Under-served (all Our read):**

- A battlegrounds game whose first minute is documented and timed. No leader's is.
- Small-server duels for younger players: no game in the sources protects new players with matchmaking or bots.
- Co-op battlegrounds against bosses as the main mode, with PvP as the side mode. HB's Prototype numbers suggest demand.
- A phone-first control layout: lock-on and aim assist for phone and controller were not documented anywhere.

## Sources

- Teardown: [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md). Related: [foundations/10-feel-and-feedback.md](../foundations/10-feel-and-feedback.md), [foundations/09-other-players.md](../foundations/09-other-players.md), [foundations/12-monetization.md](../foundations/12-monetization.md), [anime RPG playbook](anime-rpg.md).
- Roblox public API, 25 Nov 2026: [games](https://games.roblox.com/v1/games?universeIds=3808081382), [votes](https://games.roblox.com/v1/games/votes?universeIds=3808081382,3508322461,994732206,4730278139,4568630521,1390601379,4777817887,2380077519,1451439645,648454481,1359573625,985731078,848145103,6161049307), badges ([TSB](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100), [HB](https://badges.roblox.com/v1/universes/4568630521/badges?limit=100), [Combat Warriors](https://badges.roblox.com/v1/universes/1390601379/badges?limit=100)), passes as linked above.
- Wikis: [roblox.fandom.com: TSB](https://roblox.fandom.com/wiki/The_Strongest_Battlegrounds), [Combat Warriors: Parry](https://combat-warriors.fandom.com/wiki/Parry), [Daily spin](https://combat-warriors.fandom.com/wiki/Daily_spin), [Gamemodes](https://combat-warriors.fandom.com/wiki/Gamemodes).
- Community guides (unverified): [rblxguide TSB](https://rblxguide.com/games/the-strongest-battlegrounds/updates/ragdoll-cancel-and-evasive), [Bloxodes TSB](https://bloxodes.com/wiki/the-strongest-battlegrounds), [OfZenAndComputing UBG](https://www.ofzenandcomputing.com/how-to-play-untitled-boxing-game/), [allthings.how Blade Ball](https://allthings.how/roblox-blade-ball-how-to-play-full-guide/).
- Trackers: [Rotrends](https://rotrends.com/game/3808081382), [Bloxodes October 2026 report](https://bloxodes.com/stats/reports/roblox-october-2026).
- DevForum: [client-based combat](https://devforum.roblox.com/t/writing-a-client-based-combat-system/4175630), [battlegrounds hitbox](https://devforum.roblox.com/t/creating-a-battlegrounds-like-hitbox/3623640).
