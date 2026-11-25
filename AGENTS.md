# Instructions for AI agents

This repository is a handbook for designing, auditing and fixing Roblox games. If you are an AI agent helping someone with a Roblox game's design, follow this file. It exists because AI models produce game-design advice that reads well and changes nothing. The procedure below is how to avoid that.

Read [foundations/01-why-designs-fail.md](foundations/01-why-designs-fail.md) once. Its last section describes your default mistakes.

## Eight rules

1. **Reference first.** Before designing anything, name one live Roblox game the design starts from and the one thing it changes. The change must be a verb the player does, not a theme. If the user has not given these, ask. Do not continue without them.
2. **Timeline before prose.** Produce the loop table and the first-session script before writing any description of the game. If you cannot fill a row, say which row and why.
3. **Never invent a number.** Use numbers from the teardowns, genre pages and `data/` in this repo, with their source. Anything else is a proposal: label it "Start with", show what real number it was derived from, and check it with `tools/pacing.py` when it is a price or an income.
4. **Put something at stake on purpose.** Say what the player can lose, who can take it, and how it is protected. Then check it against [foundations/15-the-line.md](foundations/15-the-line.md). Do not remove stakes to make the design feel kinder.
5. **One change per fix.** Every recommendation names one stat, one change, the number you expect, and when to read it. Never "improve onboarding".
6. **Failures first.** When reviewing, lead with what fails, ordered by how early in the player's first session it happens. Do not open with praise.
7. **Run the nothing detector on your own output** before returning it: [kit/nothing-detector.md](kit/nothing-detector.md). Every claim needs two of: a time, a number, what is on screen.
8. **Measure when you can.** If you can run the game (Roblox Studio tools, a playtest, a video), time the gates with a clock: seconds to first input, first reward, first purchase. A measured number replaces any estimate, yours included.

## What to do for each kind of request

### "Design a game" or "is this idea good?"

1. Read [foundations/00-the-short-version.md](foundations/00-the-short-version.md) and [foundations/03-idea-and-reference.md](foundations/03-idea-and-reference.md).
2. Find the genre in [genres/README.md](genres/README.md) and read its playbook in full. If the game is a fast, trend-following collect-and-earn game, read [slop/](slop/README.md) too.
3. Read the teardown of the reference game if one exists in [teardowns/](teardowns/README.md).
4. Fill, in this order:
   - [kit/templates/one-page-design.md](kit/templates/one-page-design.md)
   - [kit/templates/core-loop-table.md](kit/templates/core-loop-table.md)
   - [kit/templates/first-session-script.md](kit/templates/first-session-script.md)
   - [kit/templates/economy-sheet.md](kit/templates/economy-sheet.md), then write its JSON and run `python tools/pacing.py <file>`; fix the ladder until it passes
   - [kit/templates/update-plan.md](kit/templates/update-plan.md) for the first three weeks
5. Run [kit/design-audit.md](kit/design-audit.md) on what you produced. Report the failed gates to the user. Do not hide them.

### "Review my game", "audit this", "why is nobody staying?"

1. Ask for, or find, the material listed at the top of [kit/design-audit.md](kit/design-audit.md). For a live game the funnel and the first-session retention chart matter most; [kit/templates/stats-intake.md](kit/templates/stats-intake.md) lists every number and where it lives in the dashboard.
2. Run the audit. Use the genre playbook's numbers where it gives its own.
3. Return the report in the audit's format: verdict, failed gates, scores with evidence, five fixes as hypotheses, and what you could not judge.

### "My day-1 retention is 4%", "players leave in the first minute", any single bad number

1. Open [foundations/14-metrics-and-diagnosis.md](foundations/14-metrics-and-diagnosis.md). Find the stage of the funnel the number belongs to.
2. Use its diagnosis table to pick the likely cause. Confirm it against what the game does at that moment: play to that minute or read the script.
3. Propose one change, as a hypothesis with an expected number, and the page that explains it. `python tools/funnel.py --size <now> <expected> --per-day <new players>` says how many players and days the test needs.

If the user has more than one number, use the next procedure instead.

### "Here are my stats", "what should I fix first?", "improve my numbers"

1. Get the numbers in the shape of [kit/templates/stats-intake.md](kit/templates/stats-intake.md). If the first-session curve and the step funnel are both missing, say that the first job is the funnel events, and offer a design audit in the meantime.
2. Write the numbers as JSON and run `python tools/funnel.py <file>`. It names the weak stage, the window, the step, how much of a gap is ad traffic or one device, and the smallest change the game's traffic can prove.
3. Follow [kit/stats-to-plan.md](kit/stats-to-plan.md) from step 2. Do not skip step 3: the tool finds where players leave, and only watching that moment says why. If you cannot watch the game, say so and ask for a recording or the watch notes.
4. Name the kind of fix before proposing one: world, screen, numbers, rules, content, packaging or device. One kind per update.
5. Return the report in that page's format: at most three hypotheses, one chosen, each with the number now, the number expected, and how many days until it can be read.
6. Hand the chosen fix on in its own document. A screen goes out as a filled [kit/templates/screen-brief.md](kit/templates/screen-brief.md), which maps onto the brief a UI design process such as Drip takes. A number goes out as a pacing JSON checked with `tools/pacing.py`. Anything else goes out as a row in the update plan.

### "Make it more addicting", "make it stickier"

1. Ask which number is weak: the first five minutes, session length, next-day return, week two. If they do not know, treat it as an audit request.
2. Use the table at the end of [slop/02-why-it-holds.md](slop/02-why-it-holds.md), which maps each stat to the mechanisms that move it, and [foundations/08-retention.md](foundations/08-retention.md).
3. For every mechanism you propose, state where its line is. The players are mostly children.

### "Make a slop game", "follow this trend"

1. Read [slop/README.md](slop/README.md) and [slop/05-after-the-peak.md](slop/05-after-the-peak.md). Tell the user the odds and the timing honestly.
2. Follow [slop/04-build-it.md](slop/04-build-it.md) step by step. Step 1, the sentence with the changed verb, is not optional.
3. Check the result against [slop/03-quality-bar.md](slop/03-quality-bar.md).

### "What should I sell?", "set my prices"

[foundations/12-monetization.md](foundations/12-monetization.md) for what sells and at what price in the genre, then [foundations/15-the-line.md](foundations/15-the-line.md). Nothing is offered in the first five minutes, and no purchase window opens by itself at a moment of loss.

### "Plan my updates"

[foundations/13-live-ops.md](foundations/13-live-ops.md) and [kit/templates/update-plan.md](kit/templates/update-plan.md). Every update adds things to collect and names one stat.

### "Tear down this game"

Use [kit/templates/teardown.md](kit/templates/teardown.md). Roblox's public endpoints give players, server size, passes with prices and badge counts without a login; `tools/snapshot.py` shows how to call them. Badge counts make a progress funnel. Write "not known" for anything you could not find.

## When information is missing

Ask before you design. These five answers change everything that follows:

1. Which live game is this closest to, and what is the one thing you change?
2. Who builds it, and for how many weeks?
3. Is it a bet on a current trend, or a game meant to last years?
4. For a live game: what share of new players are still there at 1 minute and at 5 minutes, and what share return the next day?
5. What do you want to be true in four weeks that is not true now?

If the user cannot answer the fourth, the first job is the funnel events, not a redesign.

## How to treat the numbers here

- Player counts, prices and policies are dated. Most were collected on 25 November 2026. Roblox changes its rules often. When a decision depends on a number, check it is still true: `python tools/snapshot.py` re-pulls the charts, passes and badges.
- "Our read" marks the authors' deductions. Weigh them as reasoning, not as findings.
- "Start with" marks starting values. They are a first draft for a stopwatch and a live funnel to correct.
- "Not known" means the research did not find it. Do not fill the gap from memory. Say it is not known.
- Where a genre page and a foundation page disagree, the genre page wins for that genre.

## Map

| Path | Use it for |
|---|---|
| [foundations/00-the-short-version.md](foundations/00-the-short-version.md) | The whole handbook in 25 lines |
| [foundations/01-why-designs-fail.md](foundations/01-why-designs-fail.md) | The twelve failures, and the section for AI agents |
| [foundations/02-the-platform.md](foundations/02-the-platform.md) | Who plays, how games are found, benchmarks, rules |
| [foundations/03-idea-and-reference.md](foundations/03-idea-and-reference.md) | Choosing the idea |
| [foundations/04-core-loop.md](foundations/04-core-loop.md) | The loop with a stopwatch |
| [foundations/05-first-session.md](foundations/05-first-session.md) | The first five minutes and their gates |
| [foundations/06-progression-and-economy.md](foundations/06-progression-and-economy.md) | Payback, ladders, resets |
| [foundations/07-rarity-and-collection.md](foundations/07-rarity-and-collection.md) | Odds, pity, reveals, collections |
| [foundations/08-retention.md](foundations/08-retention.md) | Staying and returning |
| [foundations/09-other-players.md](foundations/09-other-players.md) | Server size, conflict, trading, status |
| [foundations/10-feel-and-feedback.md](foundations/10-feel-and-feedback.md) | Sound, motion, timing, phones |
| [foundations/11-clips-and-packaging.md](foundations/11-clips-and-packaging.md) | Title, thumbnail, ads, creators |
| [foundations/12-monetization.md](foundations/12-monetization.md) | What sells and at what price |
| [foundations/13-live-ops.md](foundations/13-live-ops.md) | Updates, events, seasons |
| [foundations/14-metrics-and-diagnosis.md](foundations/14-metrics-and-diagnosis.md) | The funnel and the symptom-to-fix table |
| [foundations/15-the-line.md](foundations/15-the-line.md) | Where compelling becomes manipulative; Roblox policy |
| [genres/](genres/README.md) | One playbook per genre, same sections in each |
| [slop/](slop/README.md) | Trend games: anatomy, mechanisms, quality bar, recipe, lifecycle |
| [teardowns/](teardowns/README.md) | How individual hits work, in numbers |
| [kit/design-audit.md](kit/design-audit.md) | The gates, the score, the report format |
| [kit/nothing-detector.md](kit/nothing-detector.md) | The test that removes empty advice |
| [kit/stats-to-plan.md](kit/stats-to-plan.md) | From a live game's numbers to one change that can be read |
| [kit/templates/](kit/templates/) | The documents a design consists of, the stats intake and the screen brief |
| [kit/prompts.md](kit/prompts.md) | Prompts for a person to paste |
| [tools/pacing.py](tools/pacing.py) | Checks a price ladder's timing |
| [tools/funnel.py](tools/funnel.py) | Reads a stats file: weak stage, matched symptoms, what the traffic can prove |
| [tools/snapshot.py](tools/snapshot.py), [tools/analyze.py](tools/analyze.py) | Re-pull and re-analyse the public chart data |
| [data/](data/README.md) | The chart snapshot: games, passes, products, badges |
| [research/](research/README.md) | How this was researched, and its limits |
| [CONTRIBUTING.md](CONTRIBUTING.md) | The writing standard, if you add or change a page |
