# Design audit

A pass/fail and scored review for a Roblox game design. Use it on a design document before building, on a grey-box prototype, or on a live game. It takes about an hour by hand and a few minutes for an AI agent that has the material.

The audit is strict on purpose. A design gets no credit for what it intends. If something is not written down, not in the build, or not measured, it counts as missing.

## What you need

| For a design document | For a live game, also |
|---|---|
| The one-page design ([template](templates/one-page-design.md)) | The first-session retention chart and the funnel |
| The loop table ([template](templates/core-loop-table.md)) | Next-day, days 2 to 7 and days 8 to 28 retention |
| The first-session script ([template](templates/first-session-script.md)) | Session length by device |
| The economy sheet ([template](templates/economy-sheet.md)) | The pass and product list with sales |
| The update plan ([template](templates/update-plan.md)) | A stopwatch run of the first five minutes on a phone |

If a document is missing, the gates that depend on it fail. Say which document is missing and stop scoring that part.

For a live game, [templates/stats-intake.md](templates/stats-intake.md) lists every number in the right-hand column and where it is in the dashboard. When the question is "which number do I fix first", use [stats-to-plan.md](stats-to-plan.md) instead of the audit.

## Part A: gates

Twelve checks. Each is pass or fail. One failed gate means the design is not ready, whatever the score says.

| # | Gate | Passes when | Page |
|---|---|---|---|
| G1 | The promise | There is one sentence a nine-year-old could repeat, and the title names the main verb and thing | [03](../foundations/03-idea-and-reference.md) |
| G2 | Reference and change | One live game is named as the reference, with its current players, and one thing is changed, and that thing is a verb, not a theme | [03](../foundations/03-idea-and-reference.md) |
| G3 | The loop is timed | The loop table has seconds in every row and dead time is under one third of the cycle | [04](../foundations/04-core-loop.md) |
| G4 | The first reward | The script (or the stopwatch, for a build) shows first input within 5 seconds and first reward within 15, or within the genre's value in [05](../foundations/05-first-session.md) | [05](../foundations/05-first-session.md) |
| G5 | A clean first five minutes | No more than 10 to 15 words to read, no purchase offer, no window that opens by itself, and nothing that can fail in the first minute | [05](../foundations/05-first-session.md) |
| G6 | The numbers are checked | The economy sheet exists and `tools/pacing.py` passes on it. For games without an earning ladder: a table of what the player gains per minute for the first 15 minutes | [06](../foundations/06-progression-and-economy.md) |
| G7 | Another player is in the loop | The design names a verb between two players and a server size with a reason | [09](../foundations/09-other-players.md) |
| G8 | Three reasons to return | Written answers for: later today, tomorrow, next week. Each names a mechanism and a number | [08](../foundations/08-retention.md) |
| G9 | The truth | Odds are shown and match the server, timers do not restart or lie, no purchase window opens by itself when the player loses something (a revive button the player chooses to press on a death screen is the accepted exception), and paid random items follow Roblox's rules | [15](../foundations/15-the-line.md) |
| G10 | The phone | The loop works with one thumb, and the build holds 30 frames a second on a 3 GB Android phone with a full server. For a document: both are stated as requirements | [10](../foundations/10-feel-and-feedback.md) |
| G11 | Three updates ready | Three weekly updates are planned, each with things to collect and one event moment | [13](../foundations/13-live-ops.md) |
| G12 | The funnel is wired | A funnel event exists for each row of the first-session script, numbered in the order players do the steps | [14](../foundations/14-metrics-and-diagnosis.md) |

## Part B: score

One hundred points. For each line, give full points only when the evidence is in front of you. Give half when it is present but untested or partly true. Give zero when it is absent, vague, or only promised. Write the evidence next to each score: a quoted line from the design, or a measured number.

### 1. Promise and packaging (10)

| Points | Criterion |
|---|---|
| 3 | The title is a verb and a thing, two to four words, with no bait words |
| 3 | The thumbnail is described as one scene of the main verb, with one to three characters, and could be drawn from the one-sentence promise |
| 2 | Three games that tried something close are listed with their peaks and current players |
| 2 | A 15-second clip of the game would be understood with the sound off by someone who has never seen it |

### 2. The first five minutes (20)

| Points | Criterion |
|---|---|
| 4 | The thing the title names is on screen at the spawn |
| 4 | First input, first reward and first purchase land inside the gates |
| 3 | The first reward is from the middle of the table or better, and the first three attempts cannot fail |
| 3 | One thing is taught at a time, by a pointer of three words or fewer |
| 3 | By minute 5 the player has seen something they want and cannot afford, and what a more advanced player owns |
| 3 | The measured times are written next to the scripted ones, from a stranger playing on a phone |

### 3. The core loop (20)

| Points | Criterion |
|---|---|
| 4 | The core verb is one word and is done in the world, not in a menu |
| 4 | Every wait is shortened, given a job, made tense or moved off-screen |
| 4 | A number visibly goes up at least 20 times in the first five minutes |
| 3 | There is at least one real decision a minute |
| 3 | Every row of the loop stack is filled, from seconds to a week |
| 2 | With all rewards removed, the core verb is still worth doing ten times |

### 4. Progression and economy (15)

| Points | Criterion |
|---|---|
| 4 | The first purchase pays back in 30 seconds or less and nothing in the first hour takes more than 300 |
| 3 | The longest wait between purchases in the first 15 minutes is under 90 seconds |
| 3 | The first reset is reachable in 20 to 40 minutes and gives something to do, something to show and a number |
| 3 | The ladder lasts at least 3 hours for an ideal player, and the design says what stretches it (stock clocks, gates) |
| 2 | Sources and sinks are listed and a sink grows with the player |

### 5. Other players (10)

| Points | Criterion |
|---|---|
| 3 | Everything a player owns is a visible object; three players' progress can be ranked from one screenshot |
| 3 | The verb between players has written rules: what can be taken or given, how, and how it is stopped |
| 2 | The server size fits the genre's evidence |
| 2 | A friend who joins lands with their friend, and playing together gives something |

### 6. Returning (10)

| Points | Criterion |
|---|---|
| 3 | When the player leaves, something is unfinished and something keeps growing |
| 3 | A clock is always on screen and a returning player's first action is a reward |
| 2 | There is a reason to be there at a set time each week |
| 2 | There is a reason that lasts into days 8 to 28: a ladder that takes weeks, a collection that grows, friends |

### 7. Feel (5)

| Points | Criterion |
|---|---|
| 3 | Every action in the loop has its own sound and a visible reaction that starts within 0.1 seconds |
| 2 | The game can be followed with the sound off, and the last action can be named with eyes closed |

### 8. Money and the line (5)

| Points | Criterion |
|---|---|
| 2 | Few products, each relieving a named pain, with prices inside the genre's bands |
| 2 | Nothing sold gives power over another player that showing up cannot also earn |
| 1 | A parent watching over the player's shoulder would not call any prompt, timer or odds display a trick |

### 9. Live ops (5)

| Points | Criterion |
|---|---|
| 2 | A fixed update day and hour, shown in the game |
| 2 | Each planned update adds things to collect |
| 1 | Each update names one stat it is meant to move |

## Part C: the report

Write the result in this order. Failures first.

```
VERDICT: ready / fix gates first / redesign

GATES FAILED
- G4 The first reward: script shows first reward at 0:48 (gate: 0:15).
- ...

SCORE: 61 / 100
1 Promise and packaging   7/10   evidence: ...
2 First five minutes      9/20   evidence: ...
...

TOP FIVE FIXES, in order of expected effect
1. Stat: share of new players still present at 1 minute.
   Change: move the first unit to the spawn and cut the opening text.
   Expect: first reward from 0:48 to under 0:15.
   Read: 7 days after shipping.
   Page: foundations/05-first-session.md
2. ...

NOT KNOWN
- What the audit could not judge and what would be needed to judge it.
```

**Verdicts**

| Result | Verdict |
|---|---|
| All gates pass and 80 points or more | Ready to build, or ready to promote |
| One or two gates fail, or 60 to 79 points | Fix the failed gates first, then the lowest-scoring section |
| Three or more gates fail, or under 60 points | Redesign, starting from the loop table |

## Rules for the auditor

1. **Evidence or zero.** "The game will have satisfying feedback" is not evidence. A list of actions with their sounds is.
2. **Failures first.** Do not open with what is good.
3. **Fixes are hypotheses.** Each names one stat, one change and the number expected. Never "improve onboarding".
4. **Order by damage.** A gate that fails in the first minute outranks everything that happens later, because most players never get later.
5. **Use the genre page.** Where a genre playbook gives its own numbers, they replace the general ones here.
6. **Say what you could not judge.** A live game without its funnel cannot be scored on sections 2 and 6. Say so and ask for the funnel.
7. **Run the nothing detector on your own report** ([nothing-detector.md](nothing-detector.md)).
