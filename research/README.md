# How this was researched

This page says what the handbook rests on, how it was put together, and where it is weak. Read it before trusting a number more than it deserves.

## When

All research was done on 25 November 2026. "Now" on any page means that day unless the page says otherwise. Live player counts were pulled on a Wednesday morning, US time, so they sit near each game's daily low.

## How

The handbook was researched and written with Claude, Anthropic's AI model, in three stages.

**1. Twenty research passes, one per topic.** Six covered things common to every genre: the platform and its discovery system, the chart history from 2024 to 2026, design theory and economy maths, monetisation and live operations, what developers have said in public, and how games get their players. Thirteen covered genre families. One built the data snapshot in [`data/`](../data/README.md). Each pass wrote notes with a source address next to every fact, marked its own deductions, and listed what it could not find.

**2. A second pass on each genre for in-game numbers.** The first pass could not read most game wikis. The second read them page by page, through each wiki's own pages, and added the odds tables, price ladders, timers and update logs that the genre pages and teardowns are built on.

**3. Writing to a standard.** Each page was written from the notes under the rules in [CONTRIBUTING.md](../CONTRIBUTING.md): facts only from the notes, the source carried into the page, every deduction marked "Our read", every proposed value marked "Start with", and "not known" where the notes had nothing.

## What the sources are

| Kind | Examples | How far to trust it |
|---|---|---|
| Roblox's public endpoints | Players now, visits, server size, created and updated dates, game passes with prices, badge award counts | High. These are Roblox's own numbers. Badge counts are lifetime totals, so ratios between badges are indicative: badges added later have had less time to be earned |
| Roblox's documentation and announcements | Discovery signals, policies, pricing rules | High for what the page said on the day. Roblox changes these often and most documentation pages carry no date |
| The games' own wikis | Odds, prices, timers, update logs | Medium. Wikis are written by players, can lag the game, and sometimes contradict themselves. Contradictions are stated on the page |
| Tracker sites | Peak players, averages, session lengths | Low to medium. Trackers sample at intervals and disagree with each other, sometimes by a factor of two. Ranges are given where they do. Session lengths and revenue figures from trackers are estimates |
| Press and reference pages | Launch stories, disputes, awards | Medium. Used for events and dates |
| Vendor reports | Retention and session medians from one analytics company | Medium. One vendor's customers, limited to large games |
| Guides and fan sites | Used only where nothing better existed | Low. Labelled where used. One site that promotes a paid service is named as promotional wherever it appears |
| Research papers and industry talks | Psychology, idle-game maths, game feel | Graded on the page as replicated, single study, practitioner or folklore. Most of it is not about Roblox, and the pages say so |

## What the handbook's own numbers are

- **"Our arithmetic"** is a calculation on sourced numbers: a payback time, a ratio, an expected value. The inputs are on the page so it can be redone.
- **Results from `tools/pacing.py`** are simulations of an ideal player. They are lower bounds on time, not measurements of real players.
- **"Start with"** values are proposals. Nobody has shipped a game on them.
- **Results from `tools/funnel.py`** are arithmetic on the numbers you give it: shares, differences, and the standard formula for how many players a test of two rates needs. The rows it matches are the symptoms of [foundations/14](../foundations/14-metrics-and-diagnosis.md) turned into thresholds. Where the page's wording was loose ("cluster", "steady, then a drop"), the threshold is our reading.

## What was added after the first version

The stats intake, [kit/stats-to-plan.md](../kit/stats-to-plan.md), the screen brief and `tools/funnel.py` were added on the same day. Their facts about the dashboard, funnels, configs and Experiments come from Roblox's Creator Docs, read page by page on 25 November 2026. That reading also corrected two things in [foundations/14](../foundations/14-metrics-and-diagnosis.md): how funnel steps must be numbered, and that charts can be filtered by device. The routine has not been run on a live game's dashboard yet, and its examples are invented and say so.

## What it could not find

**No game was played with a stopwatch.** This is the largest gap. The first-session sections say what the hits give a new player and, for collect-and-earn games, what the arithmetic implies. They rarely say what a real new player experiences second by second. Where a genre page says "not known" for the first minute, that is why.

**Search ran out.** The research had a fixed allowance of web searches and used it up partway through the first stage. Everything after that came from pages that could be addressed directly. The cost shows most in what developers have said: interviews and talks were found for a handful of hits, and for most games the reasons a design works are deductions from its numbers.

**Roblox does not publish retention or revenue by game or by genre.** The only retention figures are platform-wide medians. Nothing here can tell you what day-1 retention a good horror game has.

**What sells is not known.** The snapshot has every pass and product each charted game lists, with its price. It has no sales figures, so which products carry a game's revenue is a deduction wherever a page says it.

**Peaks before mid-2026 are poorly dated.** The trackers that keep history began in 2026.

**Nothing was measured about feel, performance or interface quality** in any game. Those sections are reasoning.

## How to check or extend it

- Re-pull the public data: `python tools/snapshot.py`, then `python tools/analyze.py`.
- Check the handbook against its own rules: `python tools/lint.py`.
- Time a first session yourself and add it to a teardown. [CONTRIBUTING.md](../CONTRIBUTING.md) says how.
- If a number here is wrong, the fix is a source and a date.

## Sources

Every fact on a page links the page it came from. The complete list of external addresses the handbook cites, grouped by site, is in [sources.md](sources.md).
