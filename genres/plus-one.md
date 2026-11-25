# Plus-one: train a stat, reach a zone, bring it home

> **The feeling sold:** "Every step makes me faster. Faster gets me farther. Farther has the good stuff, and I bring it home."

This page covers train-a-stat incrementals and their 2026 hybrids: +1 Speed Keyboard Escape, [Throw Food For Animals](../teardowns/throw-food-for-animals.md), Kick a Lucky Block, Escape Tsunami For Brainrots and Ride A Pet. They share three parts: a stat that rises from a trivial input, zones gated by that stat, and a collectible carried back to a base where it earns. [Steal An Egg](../teardowns/steal-an-egg.md) uses the same skeleton with theft added, so it sits in [steal-and-defend.md](steal-and-defend.md). Why the skeleton works is in [slop/01-anatomy.md](../slop/01-anatomy.md) (Skeleton B) and [slop/02-why-it-holds.md](../slop/02-why-it-holds.md) (mechanism 10). Counts marked "now" are from the Roblox public API, 25 Nov 2026, 13:53 UTC.

## At a glance

| | |
|---|---|
| Core verb | A trivial repeated input that adds to one stat: step, throw, kick, ride |
| Study these first | [Throw Food For Animals](../teardowns/throw-food-for-animals.md): the current leader (237K now) with full food, area and animal tables. +1 Speed Keyboard Escape: the purest "+1", a 22-player race with 47 priced passes. Ride A Pet: rebirths gated by luck, not cash. Escape Tsunami For Brainrots: the hazard version, and the steepest fall |
| Session that works | About 9 minutes (+1 Speed), 11.67 minutes (Escape Tsunami), about 17 minutes (Throw Food For Animals), tracker estimates ([RoVitals](https://rovitals.com/game/95082159892680), [Rolimons](https://www.rolimons.com/game/131623223084840), [RoVitals](https://rovitals.com/game/120219252362013)) |
| Players per server | 5 (Throw Food For Animals, Kick a Lucky Block), 6 (Ride A Pet), 8 (Escape Tsunami), 22 (+1 Speed Keyboard Escape) (Roblox public API, 25 Nov 2026) |
| Who owns the genre | Nobody for long. A new leader every few months: Escape Tsunami (created Dec 2025), +1 Speed (Jan 2026), Kick a Lucky Block and Ride A Pet (Apr 2026), Throw Food For Animals (Sep 2026). The 2022 "+1 Jump" games that started the idea hold 54 and 14 players now |
| Build cost | **Our read:** the cheapest skeleton in this handbook to build. A stat, a course of zones and a pen. Content per zone (8 animals in Throw Food For Animals) is the running cost |
| Money comes from | x2 stat and x2 cash passes (99 to 399 R$), luck passes, and in the race game cosmetic trails up to 2,999 R$ |
| What kills clones | A stat with nothing worth bringing home, and a spike with no weekly event behind it |

## Why people play it

The research has no age or device split for these games. What it has: +1 Speed sells "ASMR" keyboard clicks and candy sounds in its own description and carries the highest approval of any game in this family, 96.7%. Escape Tsunami, the frantic one, sits at 83.1% (Roblox public API, 25 Nov 2026).

**Our read:** the stat is a number that never stops rising, and the zone gate turns that number into a place. A player can say "I can reach the Desert now" a few minutes after "I need 28 more levels". The collectible gives the trip a payoff that stays: it sits in the pen and earns while the player trains for the next gate.

## The loop, with a stopwatch

Leader: Throw Food For Animals. Sources: [Bloxodes zones guide](https://bloxodes.com/articles/throw-food-for-animals-zones-food-guide), [Areas](https://throw-food-for-animals.fandom.com/wiki/Areas), [Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes). The wiki has 8 pages and draws on community databases, not game files.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Train | Uses a pull-up stand | not known | Throw Power rises | Throw level |
| 2. Pick food | Chooses the best food owned | | Food in hand | Carrot free; Apple $30; Banana $150 |
| 3. Throw | Runs to the checkered launch strip, taps "TAP TO THROW!" | not known | Food flies; lands in the front, middle or back third of an area | Distance: area 2 needs 173 studs and level 28 |
| 4. Attract | Nothing | not known | An animal comes to the food | Chance per animal (Frog 56.9% on a Carrot); a mutation roll and one of nine sizes |
| 5. Bank | Nothing | not known | The animal goes into the pen at the base | Income per second ($1 to $1.5M/s in the first four areas) |
| 6. Spend | Buys better food | | | Food x5 to x27 per step |
| 7. Reach | Throws into the next area once the level allows | | New area, 8 new animals | First animal of the new area earns about 1.5x the best of the last |

**How the others differ.**

- **+1 Speed Keyboard Escape.** Every step gives +1 Speed. The course is giant candy keyboard keys; one wrong move sends you back to the start (Roblox public API description). Wins, not animals, are the spending currency; trails are passive speed multipliers; rebirths are required to progress ([TechWiser](https://techwiser.com/roblox-1-speed-keyboard-escape-wiki/)). Nothing is carried home, and 22 players race each other.
- **Kick a Lucky Block.** Kick the block to roll a brainrot, survive the tsunami the kick sets off, place the brainrot on your plot, buy weights to kick farther (Roblox public API description).
- **Escape Tsunami For Brainrots.** Run out, grab brainrots, outrun the wave, upgrade units and base slots; spawn machines and lucky blocks give more rolls (Roblox public API description). Waves move at 85 (super slow) to 220 (lightning); special waves at 70; a geyser after a 7-second warning ([Waves](https://escape-tsunami-for-brainrots.fandom.com/wiki/Waves)). The wiki gives no unit. **Our read:** if these are studs per second, even the slowest wave is over five times Roblox's default walk speed of 16 ([Humanoid reference](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml)), so speed upgrades are the whole game.
- **Ride A Pet.** The pet you ride is the stat: its speed decides how far you get. A radar shows the distance to an egg; you carry it home under a break timer and hatch it in a nest ([AllThings.How](https://allthings.how/ride-a-pet-on-roblox-how-to-play-full-guide/)).

**The loop stack** across the family:

| Every | What closes | Example |
|---|---|---|
| 1 input | The stat goes up by a fixed amount | +1 per step (+1 Speed); +2 per step on Steal An Egg's free treadmill |
| 10 to 30 seconds | A trip ends: the collectible is banked or lost | [slop/02-why-it-holds.md](../slop/02-why-it-holds.md), mechanism 10 |
| About 20 seconds | An egg spawn window closes | Ride A Pet ([AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/)) |
| 5 minutes | Eggs reset; weather changes | Steal An Egg ([wiki](https://stealanegg.fandom.com/wiki/Eggs)); Ride A Pet weather lasts 5 min |
| One session | The next zone gate | Throw Food For Animals: +34 levels per area early |
| 1 to 3 sessions | First rebirth | 42.4% of everyone who joined +1 Speed has rebirthed (badges, Roblox public API) |
| 7 days | The weekly event | Throw Food For Animals Saturday 6 AM PT; Escape Tsunami "Wave Wednesday" |

## The first five minutes

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | Throw Food For Animals: the player holds a free Carrot near the launch strip. Ride A Pet: the player is riding a Snail, green arrows point to the shop stalls | [Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals); [AllThings.How](https://allthings.how/ride-a-pet-on-roblox-how-to-play-full-guide/) |
| 0:30 | First animal caught (a Frog, $2/s, is 56.9% likely per qualifying Carrot throw). Ride A Pet: Advanced Radar bought for $50 | [Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes); AllThings.How |
| 1:00 | Apple ($30) affordable after about 15 s on one Frog | Our arithmetic |
| 3:00 | Banana ($150) bought with 2 or 3 Forest animals; Ride A Pet: first egg carried home and hatched, first index rewards of $1,000 and $5,000 | Our arithmetic; AllThings.How |
| 5:00 | Ride A Pet: the Snail (speed 15) replaced by an Axolotl (165) at the end of the tutorial; +1 Speed: free codes give 15,000 Speed, and liking plus joining the group another 15,000 | [AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/); [PocketGamer](https://www.pocketgamer.com/roblox/1-speed-keyboard-escape-codes/) |

No source timed these on a device; the timings are our reconstruction from the numbers.

Gates for a new plus-one game. **Start with:**

| By | Gate | Why this number |
|---|---|---|
| 0:10 | The stat has risen at least once, with a sound | The input is trivial; the first press is the tutorial |
| 0:30 | First collectible banked and earning | Throw Food For Animals' first catch is a coin flip on the first throw |
| 1:00 | Second item affordable | Apple at 15 s of Frog income |
| 3:00 | Second zone visible with its gate number on screen | Steal An Egg's first gate is 900 Speed, 450 steps on the free treadmill |
| 5:00 | One upgrade to the training tool bought | Steal An Egg's second treadmill costs 15K and gives +5 a step, 2.5x the free one |

## Numbers that work

**Throw Food For Animals areas** ([Areas](https://throw-food-for-animals.fandom.com/wiki/Areas), [Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes)):

| Area | Distance (studs) | Throw level | Rank-1 income | Rank-8 income |
|---|---|---|---|---|
| Forest | 5 | 1 | $1/s | $25/s |
| Savanna | 173 | 28 | $40/s | $1K/s |
| Desert | 341 | 62 | $1.5K/s | $38K/s |
| Jungle | 509 | 96 | $60K/s | $1.5M/s |
| Ocean | 677 | 129 | not known | not known |
| Mountains | 845 | 163 | not known | not known |
| Phantom Harbor | 5.2K | 1K | not known | not known |
| Nuclear Wasteland | 6.2K | 1.2K | not known | not known |

Our arithmetic: the distance gate adds 168 studs per area for the first six areas, a straight line. Income multiplies by about 40 per area. Inside an area the 8 animals span x25, and the first animal of a new area earns about 1.5 times the best of the previous one ($25 to $40, $1K to $1.5K, $38K to $60K). Rewards grow geometrically while the gate grows in a line, so each new area should feel faster than the last.

**Steal An Egg's training tool**, the clearest cost curve for a trained stat ([wiki](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data)): prices go x17, x20, x24, x25, x25, x27 per tier while Speed per step goes x2.4, x2.5, x2.7, x1.25, x2, x2.5. Our arithmetic: each tier costs about ten times more per point of Speed per step. The steps each biome needs are in [the teardown](../teardowns/steal-an-egg.md).

**Ride A Pet rebirths** ([AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/)):

| Rebirth | Cash | Pet you must own | Hatch chance of that pet |
|---|---|---|---|
| 1 | $1M | Horse | 1 in 500K |
| 2 | $50M | Fox | 1 in 21M |
| 3 | $2.5B | Unicorn | 1 in 1T |
| 4 | $125B | Phoenix | 1 in 30T |
| 5 | $6.2T | Kitsune | 1 in 1Qi |
| 6 | $325T | Kitsune | 1 in 1Qi |
| 7 | $50Qa | Dragon | 1 in 5Qi |

Each gives +1x money and +1 pet slot (7x and 12 placed pets at the end). A rebirth clears cash and bought Hatch Luck; placed pets stay. Our arithmetic: cash steps are x50 four times in a row, a clean ladder; the odds of the required pet grow far faster (x42, then x48,000 at R3), so the real wall is luck. The guide names R3's Unicorn as the wall most players hit. Egg Luck values run from 1 (White Egg) to 2.5T (Volcanic Egg), and multiply into the rarity roll ([robloxden](https://robloxden.com/game-guides/ride-a-pet/all-egg-spawn-locations-in-ride-a-pet)).

**Funnel.** +1 Speed's Welcome badge has 358.63M awards and its Rebirth badge 151.94M: 42.4% of all joiners have rebirthed (Roblox public API, 25 Nov 2026).

**Start with:**

| Value | Start with | Derived from |
|---|---|---|
| Stat per input | +1 (or +2 on the free trainer) | +1 Speed; Steal An Egg's free treadmill |
| First gate | About 450 inputs | Steal An Egg Lake: 900 Speed at +2 |
| Gate growth | Distance or level: a straight line (+168 studs a zone). Speed: about x4 per zone for the first five | Throw Food For Animals; Steal An Egg (x4.0 to x4.3 from Desert to Volcano) |
| Reward per zone | x40 for the first unit of each zone; the first unit of a new zone earns 1.5x the best of the last | Throw Food For Animals |
| Units per zone | 8, spanning x25 in income | Throw Food For Animals |
| Training tool tiers | Price x20 per tier, stat per input x2.5 | Steal An Egg |
| Sell value | 20 s of the unit's income | Throw Food For Animals: selling is only for freeing space |
| Paid units | Earn a multiple of the player's best unit (x1 to x9 by the wiki; one product advertises up to 1,200%) | Throw Food For Animals; they never go out of date |
| Rebirth | Cash x50 per step, +1x money, +1 slot; first one inside 1 to 3 sessions | Ride A Pet; +1 Speed's 42% |
| Threat | Visible from the trip's start; a few speed tiers, with a warning (7 s) before a surprise hazard | Escape Tsunami waves and geyser |
| Server size | 5 to 8 to collect; 20 or more to race | Leaders |

## What brings them back

**Later in the same session.** The next gate number is always on screen. Eggs reset every 5 minutes in Steal An Egg; Ride A Pet eggs spawn at fixed points announced by the server, and weather events last 5 minutes ([robloxden](https://robloxden.com/game-guides/ride-a-pet/all-egg-spawn-locations-in-ride-a-pet)).

**Tomorrow.** Collectibles keep earning in the pen. Offline rules: not known for any game in this family. Daily rewards: not found. +1 Speed's free gift button unlocks after tasks ([PocketGamer](https://www.pocketgamer.com/roblox/1-speed-keyboard-escape-codes/)).

**Next week and after.** Throw Food For Animals runs a Saturday event at 6 AM PT: a new map with admin abuse for 30 to 60 minutes, then a 27-hour Thanksgiving event on 21 Nov 2026 ([Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals)). Escape Tsunami adds new waves each "Wave Wednesday" ([Waves](https://escape-tsunami-for-brainrots.fandom.com/wiki/Waves)). +1 Speed's event badges arrive every 1 to 6 weeks (26 and 27 Aug, 7 Oct 2026), with a birthday badge held by 1.85M (Roblox public API). Ride A Pet shipped the Volcanic Egg on 29 Sep 2026 and a mutation update in September ([Beebom](https://beebom.com/ride-a-pet-wiki/)).

## Other players

- **Server size decides the game.** At 22, +1 Speed is a shared race and a spectacle. At 5 to 8, the collect games are small groups where players see each other's pens.
- **What they can do to each other.** Little, outside Steal An Egg. Throw Food For Animals, Ride A Pet and Kick a Lucky Block have no theft in the sources read. Escape Tsunami sells a Harpoon Gun (640 R$) and a Shockwave Bomb (349 R$); what they do to other players is not documented.
- **Trading.** +1 Speed sells a Premium Trade Booth for 159 R$.
- **The clip.** The near miss: the wave catches someone at the line, or a throw lands a Rainbow animal in the back third.

## Money

| Game | Item | Type | R$ |
|---|---|---|---|
| Throw Food For Animals | x2 Cash 99; x2 Training Power 149 | Passes | 99 to 149 |
| Kick a Lucky Block | Auto Kick 99; x2 Brainrot Luck 249; x2 Mutation Luck 265; x2 Kick Power 349; x2 Cash 399; VIP 729 | Passes | 99 to 729 |
| Escape Tsunami | Speed Boost 129; Double Jump Coil 160; VIP 175; Infinity Ball 245; Rainbow Shield 295; Super Speed Boost 329; Shockwave Bomb 349; Harpoon Gun 640; Anti-Wave Device (turns off all waves for a while) 699; VIP+ 888 | Passes | 129 to 888 |
| +1 Speed Keyboard Escape | Treadmills: Gold 79, Diamond 345, Candy 749, ADMIN 1,199. Wins x2 95; Soundpacks 85; Trade Booth 159; 20 equip slots 299. Trails 19 to 2,999; auras 90 to 1,849 | Passes (47 priced) | 19 to 2,999 |
| Ride A Pet | Infinite Radar 399; Eternal Radar 500 (or $30M in game) | Pass; in-game item | 399 to 500 |

Sources: Roblox public API, 25 Nov 2026; Ride A Pet radar from [AllThings.How](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/). Throw Food For Animals also sells a "Lucky Throw" Robux power-up that raises luck ([Bloxodes](https://bloxodes.com/articles/throw-food-for-animals-mutations-guide)).

Notes:

- The x2 stat pass is this family's own product: x2 Training Power, x2 Kick Power, paid treadmills.
- +1 Speed retired twelve tiered "Speed Multiplier" passes and now sells mostly cosmetics. **Our read:** in a 22-player race, paid speed decides the race, while a trail only shows; the move kept its approval at 96.7%.
- Escape Tsunami's Anti-Wave Device sells the removal of the threat. **Our read:** a paid way to skip the danger empties the loop for the buyer and makes the free game look like a sales pitch.
- Paid luck (Lucky Throw, x2 Brainrot Luck) makes rolls paid random items; see [foundations/15-the-line.md](../foundations/15-the-line.md).

## Live ops

Weekly events in every live leader, on a fixed weekday: Saturday at 6 AM PT for Throw Food For Animals, Wednesday for Escape Tsunami. Throw Food For Animals broke out with its first update, five weeks after creation: the 24-hour average went from 1,673 to 6,914 (+313%) on 23 Oct 2026 ([RoStats](https://rostats.io/records)). Escape Tsunami (22 Nov), +1 Speed (23 Nov) and Throw Food For Animals (25 Nov) were all updated in the last week before 25 Nov 2026 (Roblox public API), but Escape Tsunami has added no badge in about 9.5 months. **Our read:** a small team can sustain one new zone of 8 units per week, which is how Throw Food For Animals reached 19 areas and 50 foods two months after launch.

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Under 0.1% of peak after 10 months: Escape Tsunami 4.1M to 5.0M (Jan to Feb 2026, trackers disagree) down to 3,804; 30-day peak 28,673 ([Rolimons](https://www.rolimons.com/game/131623223084840)) | A meme spike on a thin loop (11.67-min session, 83.1% approval); no badges added | A collection and rebirth ladder that lasts weeks; new goals every week |
| 0.1% of peak in 53 days: Ride A Pet 1,550,673 (3 Oct 2026) to 1,646 | A wall at R3 (a 1-in-1T pet) and a reset that takes bought luck | Keep walls on cash and time, not on luck alone; never reset what was bought |
| 2 to 3% of peak in 3 months: Kick a Lucky Block 374K to 533K (Aug to Sep 2026) down to 11,943; 30-day average 11,521 ([RoVitals](https://rovitals.com/game/89469502395769)) | Hot window of a wave | Plan for 4 to 10 weeks ([slop/05-after-the-peak.md](../slop/05-after-the-peak.md)) |
| 0.3 to 0.5% of peak in 3 to 4 months, but 653K on a Saturday: +1 Speed 4.0M to 6.1M (Aug to Sep 2026) down to 18,879 | Weekday drift; the weekly event still works | Keep the event; it is 36x the weekday level |
| The 2022 ancestors near zero: "Every Second You Get +1 Jump" 446.7M visits, 54 players; "+1 Jump Every Second" relaunched Nov 2026 with 1 player | The bare mechanic with no theme, course or collectible | A themed course, sound, a collectible |
| Followers made late sit at a few thousand: Throw Food clones created 6 days after its breakout, 3,000 to 4,000 each; bait titles ("KICK FREE BLOCK (X999)") at 63 to 70% approval | Same verb, late; broken promise | Change the verb within two weeks, or do not follow ([slop/03-quality-bar.md](../slop/03-quality-bar.md)) |

Sources: [RoStats](https://rostats.io/records), [RoVitals](https://rovitals.com/), Roblox public API, 25 Nov 2026.

## Checklist

- [ ] The stat rises on the first input, inside 10 seconds, with a sound.
- [ ] The first collectible is banked and earning inside 30 seconds.
- [ ] The next gate's number is on screen at all times.
- [ ] The first gate takes about 450 inputs on the free trainer.
- [ ] Each new zone's first unit earns about 1.5x the best unit of the zone before.
- [ ] 8 units per zone, spanning about x25.
- [ ] Each training tier costs about x20 and gives about x2.5 per input.
- [ ] The trip home lasts 10 to 30 seconds, and the threat is visible from its start.
- [ ] A hit costs the prize, never the stat.
- [ ] Paid units scale with the player's best, so a purchase does not go stale.
- [ ] First rebirth reachable within the first three sessions; every rebirth keeps placed units and anything bought with Robux.
- [ ] No product removes the threat for the buyer.
- [ ] Mutation and size odds are shown; paid luck shows live odds.
- [ ] One weekly event on a fixed day and hour, with a countdown.

## Twists and open space

Variations that produced hits:

- The stat as a race on a themed course with ASMR audio: +1 Speed, 4.0M to 6.1M peak.
- Throwing to attract: Throw Food For Animals, 2.47M peak ([RoStats](https://rostats.io/records)).
- A hazard you set off yourself: Kick a Lucky Block.
- Riding the collectible: Ride A Pet, 1.55M peak; its follower Steal A Pet And Ride It holds 7,980 now.
- Throwing a person: Throw a Friend for Monsters, created 3 Nov 2026, 12,183 now (Roblox public API).

**Our read** on open angles:

- A co-op trip. Every leader sends players out alone. One carries, one clears the path, both bank.
- A threat that learns. The wave and guardian are fixed. A threat that speeds up when the player banks often keeps the trip tense late in the ladder.
- A walk-away mode. +1 Speed's calm loop earns the family's best approval. A plus-one game that rewards rhythm and sound over frantic grabbing has room.

## Sources

- Teardowns: [Throw Food For Animals](../teardowns/throw-food-for-animals.md), [Steal An Egg](../teardowns/steal-an-egg.md).
- Analysis: [slop/01-anatomy.md](../slop/01-anatomy.md), [slop/02-why-it-holds.md](../slop/02-why-it-holds.md), [slop/03-quality-bar.md](../slop/03-quality-bar.md), [slop/04-build-it.md](../slop/04-build-it.md), [slop/05-after-the-peak.md](../slop/05-after-the-peak.md).
- Throw Food For Animals wiki: [Areas](https://throw-food-for-animals.fandom.com/wiki/Areas), [Foods](https://throw-food-for-animals.fandom.com/wiki/Foods), [Mutations & Sizes](https://throw-food-for-animals.fandom.com/wiki/Mutations_%26_Sizes); [Bloxodes](https://bloxodes.com/wiki/throw-food-for-animals).
- Escape Tsunami wiki: [Waves](https://escape-tsunami-for-brainrots.fandom.com/wiki/Waves). Steal An Egg wiki: [Treadmills data](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data), [Eggs](https://stealanegg.fandom.com/wiki/Eggs).
- Ride A Pet: [AllThings.How progression](https://allthings.how/ride-a-pet-progression-guide-best-pets-and-all-7-rebirths/), [AllThings.How how to play](https://allthings.how/ride-a-pet-on-roblox-how-to-play-full-guide/), [robloxden](https://robloxden.com/game-guides/ride-a-pet/all-egg-spawn-locations-in-ride-a-pet), [Beebom](https://beebom.com/ride-a-pet-wiki/).
- +1 Speed: [TechWiser](https://techwiser.com/roblox-1-speed-keyboard-escape-wiki/), [PocketGamer codes](https://www.pocketgamer.com/roblox/1-speed-keyboard-escape-codes/).
- [RoStats records](https://rostats.io/records), [RoVitals](https://rovitals.com/), [Rolimons](https://www.rolimons.com/game/131623223084840), [Humanoid reference](https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/Humanoid.yaml); Roblox public API (games, game passes, badges), 25 Nov 2026.
