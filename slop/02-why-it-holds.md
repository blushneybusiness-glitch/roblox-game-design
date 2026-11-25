# Why it holds: eleven mechanisms

Each mechanism below has four parts: what it is, the numbers the hits use, how to build it, and where it goes wrong. The numbers and their sources are in [01-anatomy.md](01-anatomy.md); they are repeated here only where needed. Lines headed **Start with** are starting values to tune. Lines headed **Our read** are our deductions.

The order is the order a player meets them.

## 1. The 30-second payback

**What it is.** The first thing the player buys earns back its price before they have time to get bored, and every later purchase does the same within a few minutes.

**The numbers.** Steal a Brainrot's first unit costs $25 and earns $1 a second: 25 seconds to pay for itself. Across the whole conveyor ladder, from $25 to $80 million, payback only rises from 25 seconds to about 300. Grow a Garden's first seed costs 10, grows in 8 seconds and sells for about 20. Plants vs Brainrots hands a new player $400, the price of exactly two starter plants that grow in 5 seconds.

**Build it.**

- Decide payback first, price second. Price = income per second x payback seconds.
- **Start with:** 20 to 30 seconds for the first unit, 80 to 120 seconds by the fifth, never above 300 seconds for anything a player is meant to buy during normal play. Keep 600 seconds and more for the few units that exist to be chased.
- Give enough starting cash to buy the first unit at once. The first purchase is the tutorial.
- Limit slots. Steal a Brainrot starts with 10 and sells units back at 50%. The early game is "fill every slot with the cheap unit", which multiplies income fast, and the mid game is "replace weak units with strong ones", which turns more into better and keeps the base readable.

**Where it goes wrong.** Prices that grow faster than income. If the tenth unit takes 20 minutes to pay back, the player has hit a wall and nothing else on this page will hold them. Check with `python tools/pacing.py` before building.

## 2. Wealth you can see from outside

**What it is.** Everything the player owns stands in the world as an object. A stranger can judge a base in one look.

**The numbers.** Steal a Brainrot puts every unit on its own plot and adds a second floor at rebirth 2 and a third at rebirth 10. Grow a Garden's mutations change how a crop looks, and its plot expansions take 24 hours and 3 days to finish. Throw Food For Animals keeps every animal in a pen at the player's base.

**Build it.**

- Every purchase adds or changes a visible object. No purchase only changes a number.
- Rare things must read as rare from 30 studs away: a different colour, size or glow, not a different label.
- The base's outline changes at milestones (a floor, a wing, a wall).
- The screenshot test: show one screenshot of three bases to someone who has never played. They should rank the three by wealth correctly.

**Where it goes wrong.** Progress that lives in a menu. Multipliers nobody can see. A rich base that looks like a poor one with bigger numbers on the HUD.

## 3. A lottery ticket inside every purchase

**What it is.** Each unit rolls a second time for an upgraded version. The roll is separate from the unit's rarity.

**The numbers.**

| | No upgrade | Small | Medium | Big | Biggest |
|---|---|---|---|---|---|
| Steal a Brainrot | 84% | 10% at x1.25 | 5% at x1.5 | 1% at x10 | |
| Throw Food For Animals | 79.5% | 13% at x1.5 | 4% at x3 | 2% at x5, 1% at x10 | 0.5% at x20 |

Our arithmetic on those tables: the average unit in Steal a Brainrot earns 1.14 times its base income because of mutations, and in Throw Food For Animals 1.41 times. So the whole system adds 14% to 41% to the economy, while the top result is worth 10 to 20 times a normal unit.

**Our read:** that gap is the design. The lottery is cheap for the economy and loud for the player. About one purchase in six gives a small win, which keeps the roll believable, and one in a hundred gives a story.

**Build it.**

- **Start with:** 82% nothing, 11% at x1.5, 5% at x3, 1.5% at x10, 0.5% at x20.
- Give each tier a material anyone can name: gold, diamond, rainbow.
- Stage the reveal. The roll resolves in front of the player with a sound per tier.
- Tell the server about the top tier.

**Where it goes wrong, and the line.** If any roll can be bought with Robux, or improved by something bought with Robux (a luck boost counts), Roblox's paid-random-item rules apply: exact odds shown before purchase and summing to 100%, live odds while a boost is active, and a block in the countries where such items are restricted. See [foundations/15-the-line.md](../foundations/15-the-line.md). Never show odds that differ from the server's.

## 4. Neighbours

**What it is.** A handful of players whose bases sit next to each other.

**The numbers.** Grow a Garden 4 players per server. Throw Food For Animals, Kick a Lucky Block and Plants vs Brainrots 5. Steal An Egg 7. Steal a Brainrot 8. Two of the dead clones in our sample used 10. Grow a Garden also pays for company: each friend in the server adds 10% to what crops sell for, up to 40% by the wiki's account, though a four-player server has room for only three friends ([wiki: Sheckles](https://growagarden.fandom.com/wiki/Sheckles)).

**Our read:** at 4 to 8, every neighbour becomes a character within one session. You learn who is rich, who robbed you, who you can rob. At 30, nobody is anybody, and the same theft is noise.

**Build it.**

- **Start with:** 6 players per server for a steal game, 4 or 5 for a grow-and-show game.
- Bases in a ring or a row, all facing one shared place that everybody has to visit (the conveyor, the shop, the launch strip).
- The owner's name and one number (income per second, or total value) float above each base.
- A friend who joins lands in the same server. Friends who invite each other are also one of the signals Roblox's recommendations count; see [foundations/02-the-platform.md](../foundations/02-the-platform.md).

**Where it goes wrong.** Servers so large that neighbours are strangers. Bases so far apart that nobody passes anyone else's. A lobby that drops friends into different servers.

## 5. Theft, and the lock

**What it is.** Other players can take what you own unless you protect it, and the protection runs out.

**The numbers.** In Steal a Brainrot any unlocked base can be raided. The lock is a button on the base that gives a shield for 60 seconds, every rebirth adds 10 seconds, and a new arrival has 30 seconds of protection ([wiki: Base](https://stealabrainrot.fandom.com/wiki/Base), [Methods of stealing](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing)). A thief carrying a unit is slowed and visible to everyone. Every player gets a free bat on joining; hitting a carrier sends the unit home, and a carrier cannot use gear ([wiki: Gears](https://stealabrainrot.fandom.com/wiki/Gears)). In Steal An Egg the animal you took the egg from and the other players can both knock you down and take it back. Grow a Garden sells theft directly: 37 R$ to steal one crop, it can fail, and the server sees a banner naming thief and victim ([wiki: Stealing](https://growagarden.fandom.com/wiki/Stealing)).

**Why it holds.** People weigh a loss more heavily than an equal gain; recent meta-analyses put the ratio at about 1.3 to 2 (see [foundations/08-retention.md](../foundations/08-retention.md)). The lock turns that into a habit: about once a minute the player has a reason to be standing at home. And a theft gives two players a story: one has a prize, the other has a name to remember.

**Build it.** Write these rules down before any code:

| Rule | Start with |
|---|---|
| What can be taken | Placed units only. Never currency, never anything bought with Robux. |
| How | On foot, carrying it in view of everyone, slowed, over a distance that takes 8 to 15 seconds. |
| How the owner stops it | Hit the thief and the unit drops. A lock that lasts 60 seconds with a short gap before it can be used again. |
| Growth | The lock gets longer with progress (+10 seconds per rebirth). |
| New players | Nothing can be taken in a player's first few minutes. |
| Offline | Nothing can be taken while its owner is not in the server. |
| After a loss | The owner sees who took it and gets a way to go after them. |

**Where it goes wrong, and the line.** This is the mechanism that drew the sharpest criticism: Polygon wrote that Steal a Brainrot became the biggest game on Roblox "by making kids miserable" (quoted by [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)), and reviewers attacked the fact that the strongest protection and tools cost Robux. Theft is the engine and it is also the harm. Three things keep it on the right side:

- Do not sell protection or recovery at the moment of loss. No Robux prompt may open because something was just stolen.
- Cap the loss. One unit per raid, not a whole base. Keep the player's best unit safe if you can afford to.
- Make losing a beginning. The victim needs a next move (chase, steal back, trap) inside five seconds, or they close the game.

## 6. Clocks

**What it is.** Stock that changes on a fixed timer the player can see.

**The numbers.** Grow a Garden's seed and gear shops restock every 5 minutes, eggs every 30, the event-currency shop every 60, daily deals every 24 hours. The stock is the same on every server, and a restock can be bought for 79 R$ ([wiki: Seed Shop](https://growagarden.fandom.com/wiki/Seed_Shop)). A few staple seeds are always in stock; the rare ones appear by chance (one top seed has a 6.67% chance per restock, per [Bloxodes](https://bloxodes.com/wiki/grow-a-garden/seeds)). Steal An Egg's eggs reset every 5 minutes too. Steal a Brainrot's conveyor hides a clock in its odds: a Legendary is guaranteed within 5 minutes and a Mythic within 15. Grow a Garden has the longest sessions of any game in this section, about 21 minutes, which is four restocks.

**Our read:** a fixed interval with random contents means the player always knows when to look and never knows what they will find. "One more restock" is a five-minute promise, and five minutes is short enough to say yes to.

**Build it.**

- **Start with:** one 5-minute clock on the HUD at all times, one 30 or 60-minute clock for a rarer shop, one daily.
- Every tick has guaranteed staples, so a tick is never empty, and a small chance (2% to 7%) of each rare item.
- Announce a rare item in stock to the whole server.
- The clock keeps running when the shop is closed or the player is elsewhere on the map. The pull is strongest when they are busy with something else.

**Where it goes wrong, and the line.** A timer that lies. A countdown that restarts itself, or a "last chance" that returns next week, is the kind of pressure that gets a game reported and removed, and it teaches players to ignore your clocks. A paid restock is acceptable when the price is shown and the next free one is in view.

## 7. It grows while you are away

**What it is.** Progress continues when the player is offline.

**The numbers.** Grow a Garden's own description says the garden grows while you are offline. Its limited weekly items, by contrast, can only be claimed while online ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Steal a Brainrot pays offline income too, though its wiki disagrees with itself on how much: one page says about 50% of the online rate, another about 3% with a 5-hour cap ([Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash)).

**Our read:** the two halves do different jobs. Offline growth makes leaving safe, so the player is not punished for having a life and returns to a reward. Online-only limited items give them a reason to be there at a set time. A game needs both.

**Build it.**

- **Start with:** full growth offline for anything on a timer. For anything that pays per second, 25% to 50% of normal income, counted for up to 8 hours away, so a night away pays 2 to 4 hours of earnings.
- The first thing a returning player does is collect. Reward before any request.
- Show what happened while they were gone in one line.

**Where it goes wrong.** Offline income so high that playing is pointless. Offline loss of any kind. A wall of pop-ups on return before the player can touch what grew.

## 8. One live hour a week

**What it is.** A scheduled event, on the same day every week, with something that only exists then.

**The numbers.** On Saturday 21 November 2026 the six tracked hits peaked at 5 to 36 times their weekday level. Every record in the genre fell on a Saturday. Throw Food For Animals starts its events at 6 AM Pacific and some last 30 to 60 minutes. Steal a Brainrot has released 12 limited mutations since June 2025, each a little stronger than the one before (x2, x4, x6, x7 ... x14), all but one on a Saturday, returning only in later events ([Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/mutations)).

**Build it.**

- Same day, same hour, every week. Put a countdown in the game.
- One item or mutation that can only be obtained during the event.
- Something happens to the whole server in the first five minutes: the developers appear, the sky changes, rare units pour out.
- Everyone who attends leaves with something.
- Build three or four weeks of events before launch. The week you skip is the week the curve breaks.

**Where it goes wrong, and the line.** Each limited item has to beat the last one or nobody comes, so everything older loses value; players who collected the x2 mutation in 2025 now own the weakest one. That is the cost of this mechanism and there is no way round it, only a pace: small steps. Do not make the event item Robux-only. An event a child cannot win by showing up is an advert.

## 9. A reset that changes what you can do

**What it is.** Rebirth: give up cash and named units for permanent gains.

**The numbers.** Steal a Brainrot has 19 rebirths. Each adds 1 to the multiplier, 10 seconds to the lock and, from the second onward, one slot. Each unlocks tools (slaps, a grapple hook, a taser, an invisibility cloak). Cost multiplies by 3 to 10 per step. Each requires specific units. In +1 Speed Keyboard Escape, 42% of everyone who has ever joined has rebirthed at least once (badge counts from Roblox's public badge endpoint, 25 November 2026).

**Our read:** two lessons. First, the reset is early: if 42% of all joiners reach it, it sits inside the first session or two. Two idealised runs of Steal a Brainrot's ladder, one of them with `tools/pacing.py`, put its first rebirth at 20 to 32 minutes of play. Second, a rebirth that only multiplies numbers is a treadmill, and players feel it. Steal a Brainrot's rebirths hand over a new way to interfere with other people, and a bigger building.

**Build it.** See the starting table in [04-build-it.md](04-build-it.md). The rules:

- First rebirth reachable in 20 to 40 minutes of play.
- Every rebirth gives one thing to do, one thing to show, and one number.
- Require named units from rebirth 1, so the player learns to hunt.
- Take only what the rebirth needs. Steal a Brainrot used to take the whole base and changed it to take only the required units ([wiki](https://stealabrainrot.fandom.com/wiki/Rebirth)).

**Where it goes wrong.** A first rebirth hours away. A rebirth that deletes something the player paid Robux for. A rebirth whose only reward is "x2".

## 10. The trip home

**What it is.** The player has to carry the prize from where they got it to where it is safe, and something can stop them on the way.

**The numbers.** In Steal An Egg the player takes an egg in a biome and runs it home before the biome's guardian or another player knocks them down; traps make them drop it ([Bloxodes](https://bloxodes.com/wiki/steal-an-egg)). Kick a Lucky Block's own description says the kick triggers a tsunami the player then has to survive. Escape Tsunami For Brainrots is built on outrunning a wave while carrying what you grabbed.

**Our read:** this is what 2026 added to the 2025 formula, and it is the cheapest source of clips in the genre. Between getting something and banking it there is a stretch of 10 to 30 seconds in which the player can lose it and everyone can see. "Barely made it" and "lost it at the door" are both worth filming.

**Build it.**

- **Start with:** a trip of 10 to 30 seconds. Shorter has no tension; longer is a commute.
- The threat is visible and can be outrun by a player whose stat is right for that zone.
- A hit drops the prize where the player stands. Another player can pick it up.
- A clear line where the prize becomes safe.

**Where it goes wrong.** A threat that cannot be seen coming. A trip so long that losing at the end costs minutes. Losing the stat itself, not just the prize.

## 11. Nothing to read

**What it is.** The game explains itself through its title and its first object.

**The numbers.** The hits' titles are the instruction: Steal a Brainrot, Grow a Garden, Throw Food For Animals, Kick a Lucky Block. Their store descriptions are five to seven lines, each starting with a verb. The research found no tutorial in any of them.

**Build it.**

- Title: a verb, then a thing. Two to four words.
- The first object the player sees is the one the title names, within 5 studs of where they spawn.
- One arrow or highlight at a time. At most three words on it.
- See [foundations/05-first-session.md](../foundations/05-first-session.md) for the gates.

**Where it goes wrong.** A text box before the first action. A menu before the first action. A title that needs explaining.

## What each mechanism is for

**Our read**, as a map from mechanism to the stat it moves:

| Stat | Mechanisms that move it |
|---|---|
| Players still present at 1 and 5 minutes | 1 payback, 2 visible wealth, 3 the lottery, 11 nothing to read |
| Session length | 5 the lock, 6 clocks, 10 the trip home |
| Coming back the same day or the next | 6 clocks, 7 offline growth |
| Coming back next week | 8 the live hour |
| Still playing after a week | 9 rebirth, 4 neighbours who are friends |
| Clips and word of mouth | 5 theft, 10 the trip home, 3 the top lottery result, 8 the live hour |

If a slop game is weak on one stat, start with the mechanisms on that row.

Next: [03-quality-bar.md](03-quality-bar.md).
