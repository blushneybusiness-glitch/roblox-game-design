# The core loop

Open this page when you are deciding what the player does over and over, or when players leave and you cannot say which minute bored them.

A loop is a chain of steps that ends where it started with the player slightly better off. Every design document has one drawn as a circle of nouns: "collect, upgrade, unlock". That drawing hides the two things that decide whether the loop works: how long each step takes, and what the player is doing during it. This page replaces the circle with a table and a stopwatch.

## What is known

**Sessions are short.** The median Roblox game's sessions last 9.8 minutes ([foundations/02-the-platform.md](02-the-platform.md)). Tracker estimates for individual hits run from about 9 minutes (Steal a Brainrot, +1 Speed Keyboard Escape, Doors) through 16 to 17 (99 Nights in the Forest, Steal An Egg, Throw Food For Animals) to 20 to 24 (Forsaken, Grow a Garden, Blox Fruits). A loop has to pay out many times inside that.

**The top is new, and it is small-server.** Of the top 100 games by players on 25 November 2026, 43% were under six months old, and simulation games, the largest group, most often run 6 players per server [data, Nov 2026] ([data/ANALYSIS.md](../data/ANALYSIS.md)).

**The hits pay out fast and often.** Run through `tools/pacing.py`, Steal a Brainrot's real price ladder gives an ideal new player 21 purchases in the first five minutes, with no wait longer than 73 seconds in the first quarter of an hour ([slop/04-build-it.md](../slop/04-build-it.md)). Grow a Garden's first seed is ready in 8 seconds. Plants vs Brainrots' first plants grow in 5.

**Waiting is given a job, or moved off-screen.** Steal An Egg has the player run on a treadmill to raise Speed while money accumulates. Grow a Garden puts the wait on a 5-minute shop clock and lets crops grow while the player is offline. Steal a Brainrot fills the wait with a shared conveyor to watch and neighbours to rob ([slop/01-anatomy.md](../slop/01-anatomy.md)).

**Filling the wait with something outside the game got a hit pulled.** Steal An Egg's treadmill originally played a feed of short videos. Roblox banned reward-driven feeds from its under-16 catalogues in August 2026 and the game came back without it ([slop/05-after-the-peak.md](../slop/05-after-the-peak.md)).

**Skill gates lose most players, and the public badge counts show how many.** From Roblox's public badge endpoint, 25 November 2026:

| Game | Gate | Share who pass |
|---|---|---|
| Doors | Survive the first Rush | 55% of everyone who joined |
| Doors | Survive the Seek chase | 19% |
| Doors | Finish the Hotel | about 2.7% |
| Speed Run 4 | Finish level 1 | 62% |
| Speed Run 4 | Finish level 10 | 22% |
| The Strongest Battlegrounds | 10 kills, of those with 1 | 54% |
| The Strongest Battlegrounds | 100 kills, of those with 1 | 19% |
| A Dusty Trip | Reach 1,000 metres | 25% of everyone who joined |
| Chained Together (two-player obby) | Win | 0.21% |
| +1 Speed Keyboard Escape | Rebirth once | 42% of everyone who joined |

Details and sources are in [genres/horror.md](../genres/horror.md), [genres/obby.md](../genres/obby.md), [genres/fighting.md](../genres/fighting.md), [genres/survival.md](../genres/survival.md) and [genres/plus-one.md](../genres/plus-one.md). The last row is the contrast: a loop that needs no skill carries almost half of all joiners to its first reset.

**A toy alone does not last.** The ragdoll and crash-physics games of autumn 2026 reached tens of thousands of concurrent players within weeks of launch on the strength of one physical toy ([genres/sandbox.md](../genres/sandbox.md)). A toy with nothing stacked above it is a short visit.

## The rules

**1. Write the loop as a table with seconds.** One row per step: what the player does, how many seconds it takes, what they see, what they hear, which number moves. Use [kit/templates/core-loop-table.md](../kit/templates/core-loop-table.md). If you cannot fill a row, that step is not designed.

**2. The core verb is something the player's body does in the world.** Throw, kick, carry, steal, dodge, place, drive. A verb that happens in a menu (craft, merge, assign) can support a loop but should not be its centre. The followers that succeeded in 2026 each changed the body verb; the ones that kept the verb and changed the theme did not ([slop/03-quality-bar.md](../slop/03-quality-bar.md)).

**3. Count the dead time and keep it under a third of the cycle.** Dead time is every second in which the player has no input and no decision. **Our read:** a third is the ceiling. A fishing loop that waits 8 seconds for a bite in a 16-second cycle is at half, and players feel that as "nothing is happening" even when the reward is good.

**4. Every wait needs one of four treatments.**

| Treatment | What it means | Example |
|---|---|---|
| Shorten it | Under 2 seconds, or gone | A first crop that grows in 5 to 8 seconds |
| Give it a job | The player trains, aims, collects or repositions during it | The treadmill in Steal An Egg |
| Make it the tension | The outcome is visibly approaching and uncertain | The run home with an egg while a guardian closes in |
| Move it off-screen | It becomes a clock the player leaves and returns to | The 5-minute restock; offline growth |

A wait with none of the four is where players leave.

**5. Something visibly goes up at least four times a minute at the start.** That is the rate the hits set: 21 to 29 purchases in the first five minutes. **Our read:** the rate can fall after the first quarter of an hour, and in the hits it does (to one purchase every 5 to 15 minutes, set by the stock clock), but only once other loops are running.

**6. Fill every time scale.** A game holds when something finishes every few seconds, every minute, every five to ten minutes, every session, every day and every week. This is the loop stack. Fill the table at the bottom of the template. An empty row is the hole players fall through. The stack of a slop hit is laid out in [slop/01-anatomy.md](../slop/01-anatomy.md).

**7. One real decision a minute.** A decision is a choice between two options that both make sense: buy the cheap unit now or save for the better one; lock the base or go raiding; risk one more room or cash out. Holding a button is not a decision. A loop with no decisions is a progress bar, and players treat it as one: they leave it running and stop looking.

**8. Put another player inside the loop.** Someone who can take what you made, see what you made, or needs you to make it. A loop that would play identically on an empty server is a single-player game paying for multiplayer hosting. See [09-other-players.md](09-other-players.md).

**9. Put skill gates after the player has something to lose.** The badge table says a skill gate keeps between a fifth and a half of the players who meet it. That is acceptable at minute 20, when the player owns things and has friends in the server. At second 30 it is most of your traffic gone before the first reward.

**10. Test the toy before building the stack.** Take away every reward, currency and unlock. Is doing the core verb ten times still something you would choose to do? If not, no progression system will rescue it. Then test the reverse: with the toy removed and only the numbers left, is there any reason to be at the screen?

## How to do it

1. Name the core verb in one word.
2. Fill the loop table for one pass through the loop. Before there is a build, write the seconds you intend.
3. Add up cycle time, dead time, decisions per minute and rewards per minute.
4. For every waiting step, write which of the four treatments it gets.
5. Fill the loop stack. Find the empty rows.
6. Build the loop in grey boxes: no art, no shop, no progression beyond the first three purchases. Three to five days.
7. Play it for ten minutes yourself, then hand it to someone who has not seen it, on a phone, and say nothing. Time each step with a stopwatch and replace your intended seconds with the measured ones.
8. If you were bored before minute ten, change the verb or the waits. Do not add a system.

## Checks

- [ ] The core verb is one word and happens in the world.
- [ ] The loop table has measured seconds in every row.
- [ ] Dead time is under one third of the cycle.
- [ ] Every waiting step is shortened, has a job, carries tension, or is off-screen.
- [ ] In the first five minutes a number visibly goes up at least 20 times.
- [ ] There is at least one real decision per minute.
- [ ] Another player can take, see or need what this loop produces.
- [ ] No skill gate stands before the first reward.
- [ ] Every row of the loop stack is filled.
- [ ] The grey-box loop was played for ten minutes by someone who did not build it.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Players leave between minute 1 and minute 3 | The first cycle has a wait with no treatment | Find the longest step with no input and shorten it or give it a job |
| Players leave the game running and tab away | No decisions; the loop is a progress bar | Add a choice with a cost each minute: what to replace, when to risk, whom to target |
| Long sessions from a few players, almost none from the rest | A skill gate too early | Move it later, or make the first three attempts impossible to fail |
| The game looks busy in a screenshot and nothing happens in a minute of play | Rewards are in menus | Put each reward on an object in the world ([slop/02-why-it-holds.md](../slop/02-why-it-holds.md), mechanism 2) |
| A strong first hour, then nothing | The stack has no daily or weekly row | Add a clock, offline growth and a weekly event ([08-retention.md](08-retention.md), [13-live-ops.md](13-live-ops.md)) |
| Everything is unlocked and nobody stays | A stack with no toy | Go back to the verb. Make the action itself worth repeating: sound, movement, a physical result |
| Players love it for a day | A toy with no stack | Keep the toy. Add the ladder and the clocks above it |
| The loop is the same alone or in a full server | No other player in the loop | Add one verb between players: take, show, help, race |

## Sources

Session lengths and platform medians: [02-the-platform.md](02-the-platform.md) and the genre pages. Ladder timings: `tools/pacing.py` with the example files in `tools/examples/`. Badge shares: Roblox public badge endpoint, 25 November 2026, through the genre pages linked above. The one-third ceiling on dead time, the four-per-minute reward rate and the one-decision-per-minute rule are our reading of those numbers, not published findings.
