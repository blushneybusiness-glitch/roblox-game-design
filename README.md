# Roblox Game Design

A field manual for designing, auditing and fixing Roblox games, built from teardowns of the games that actually hit. Written for developers and for the AI assistants they work with.

Most game-design advice is true and useless: "make the core loop engaging", "reward the player early", "add social features". You cannot build from it and you cannot check your game against it. This handbook is the opposite. Every statement carries a time, a number or what is on screen, and every fact carries its source.

## What it looks like

A few of the things inside, each with its source on the page it comes from:

- Steal a Brainrot's first unit costs $25 and earns $1 a second. Across a price ladder that spans a factor of ten billion, the time a unit takes to pay for itself only moves from 25 seconds to about 300. ([slop/01-anatomy.md](slop/01-anatomy.md))
- Played by an ideal player, that real ladder gives 21 purchases in the first five minutes. After the first quarter of an hour the pacing is done by stock timers, not prices. ([slop/04-build-it.md](slop/04-build-it.md))
- On Saturday 21 November 2026 the tracked trend hits peaked at 5 to 36 times their weekday players. Steal a Brainrot has shipped 75 Saturday updates in 77 weeks. ([slop/01-anatomy.md](slop/01-anatomy.md))
- In Doors, 55% of everyone who ever joined survived the first monster, 19% survived the first chase and about 2.7% finished the first floor. ([genres/horror.md](genres/horror.md))
- A reskin of the biggest trend game, made by one of the largest studios on the platform, kept the verb, changed the theme, and had 7 players in November 2026. The followers that worked changed the verb. ([slop/03-quality-bar.md](slop/03-quality-bar.md))
- Of the top 100 games on 25 November 2026, 43% were under six months old, 58% had published an update in the last 24 hours, and the median one listed 5 passes and 57 products that can be bought again, the cheapest at 10 R$. ([data/ANALYSIS.md](data/ANALYSIS.md))
- The median large Roblox game sees 10.3% of new players return the next day. The top 1% see 22.2%. ([foundations/02-the-platform.md](foundations/02-the-platform.md))

## Start here

| You want to | Go to |
|---|---|
| Read the whole thing in two minutes | [foundations/00-the-short-version.md](foundations/00-the-short-version.md) |
| Design a new game | [foundations/03-idea-and-reference.md](foundations/03-idea-and-reference.md), then your genre in [genres/](genres/README.md), then the templates in [kit/templates/](kit/templates/) |
| Find out why players leave your game | [kit/design-audit.md](kit/design-audit.md) and [foundations/14-metrics-and-diagnosis.md](foundations/14-metrics-and-diagnosis.md) |
| Turn your dashboard numbers into the next change | [kit/templates/stats-intake.md](kit/templates/stats-intake.md), then [kit/stats-to-plan.md](kit/stats-to-plan.md) |
| Hand a screen to a UI designer or a design agent | [kit/templates/screen-brief.md](kit/templates/screen-brief.md) |
| Make a trend game ("slop") that holds players | [slop/](slop/README.md) |
| See how a specific hit works | [teardowns/](teardowns/README.md) |
| Have an AI assistant do any of the above properly | [AGENTS.md](AGENTS.md) and [kit/prompts.md](kit/prompts.md) |

## What is inside

| Folder | Contents |
|---|---|
| [foundations/](foundations/00-the-short-version.md) | Sixteen pages on what applies to every genre: the platform, the idea, the core loop, the first session, economy, rarity, retention, other players, feel, packaging, money, live ops, metrics, and where the line is |
| [genres/](genres/README.md) | Twenty-five playbooks with the same sections in each: the loop with a stopwatch, the first five minutes, numbers that work, what brings players back, money, how games in the genre die, and a pass/fail checklist |
| [slop/](slop/README.md) | Trend games in depth: the anatomy of a hit, eleven mechanisms that hold players, hit against dead clone, a ten-step recipe with starting numbers, and what happens after the peak |
| [teardowns/](teardowns/README.md) | How individual hits work, in numbers: loop, ladder, odds, clocks, prices |
| [kit/](kit/design-audit.md) | A design audit with twelve gates and a hundred-point score, a test that removes empty advice, a routine that turns a live game's numbers into one change that can be read, templates for every design document, and prompts for AI assistants |
| [tools/](tools/pacing.py) | `pacing.py` checks a price ladder's timing. `funnel.py` reads your stats and says where players are lost. `snapshot.py` and `analyze.py` re-pull and re-analyse Roblox's public chart data |
| [data/](data/README.md) | A snapshot of the charts from 25 November 2026: 2,408 games, 16,831 passes, 105,745 products and 12,718 badges as CSV, with an analysis |
| [research/](research/README.md) | How this was researched, the sources, and what it could not find |

## Use it with an AI assistant

AI models are bad at game design in a specific way: they write a description that sounds right and never say what happens at second 10. [AGENTS.md](AGENTS.md) is a procedure that stops that. It makes the assistant name a reference game, write the loop with a stopwatch, script the first session, check the numbers with a tool, and report what fails before what works.

**Claude Code.** Install the repository as a skill:

```
git clone https://github.com/blushneybusiness-glitch/roblox-game-design ~/.claude/skills/roblox-game-design
```

Then ask for what you want: "design a tower defense game", "audit my game", "why do players leave in the first minute?", "here are my stats, what do I fix first?".

**Codex, Cursor and other agents.** Clone the repository into your project, or next to it. These tools read `AGENTS.md` on their own.

**Any chat assistant.** Attach the pages you need and paste a prompt from [kit/prompts.md](kit/prompts.md).

## The pacing tool

`tools/pacing.py` plays a price ladder the way an ideal player would and reports when things happen. It needs Python 3.8 or newer and nothing else.

```
python tools/pacing.py tools/examples/start-with-ladder.json
```

```
Summary
  First purchase:                      0:08
  Purchases in the first 5 / 15 / 60 min: 29 / 67 / 89
  Longest wait, first 15 min:          0:25 (starting at 12:01)
  Rebirth 1:                           20:41
  Nothing left to buy from:            7:30:03

Checks
  PASS first purchase within 15 s (at 0:08)
  PASS no wait over 90 s in the first 15 min (longest 0:25)
  PASS Rebirth 1 between 20 and 40 min (at 20:41)
  PASS ladder lasts at least 3 h (runs out at 7:30:03)
  PASS no unit pays back slower than 300 s (14 God: 290 s)
```

Describe your own ladder with [kit/templates/economy-sheet.md](kit/templates/economy-sheet.md).

## The stats tool

`tools/funnel.py` reads the numbers from your Creator Hub dashboard and says which stage to work on first, where in the first session players leave, how much of a gap comes from ad traffic or one device, and the smallest change your traffic can prove. It finds the place. [kit/stats-to-plan.md](kit/stats-to-plan.md) is the routine for finding the cause and choosing one fix.

```
python tools/funnel.py tools/examples/stats-example.json
```

```
WORK ON THIS FIRST
  Stage:  First session. Average session time is 5.1 min against a median of 9.0 min (your dashboard).
  Where:  the largest drop-off, 'First purchase' to 'Second purchase', around 0:54 to 2:00:
          1,210 players, 29% of everyone who joined.
          the highest leave rate, 0:30 to 1:00.
  Target: start with half the gap to the other steps:
          the share of joiners who reach 'Second purchase' from 43.1% to 51.3%.
          A 14-day split at your traffic can prove a rise of 3.0 points, so this can be read.

WHAT YOUR TRAFFIC CAN PROVE
  number                               now   14-day split   28-day split   60-day split  7 days each side
  Reached 'Second purchase'          43.1%      +3.0 (7%)      +2.1 (5%)      +1.5 (3%)         +3.0 (7%)
  Day 1 retention                     5.5%     +1.5 (27%)     +1.0 (19%)     +0.7 (13%)        +1.5 (27%)
  Day 7 retention                     0.9%     +0.7 (75%)     +0.5 (51%)     +0.3 (33%)        +0.7 (75%)
```

The example's numbers are invented. Put your own in with [kit/templates/stats-intake.md](kit/templates/stats-intake.md). When the fix is a screen, [kit/templates/screen-brief.md](kit/templates/screen-brief.md) hands it to a UI designer or to a design agent such as [Drip](https://github.com/8bitgfx/drip).

## How to read the evidence

| You see | It means |
|---|---|
| A linked fact | It comes from the page linked, as read in November 2026 |
| "Roblox public API, 25 Nov 2026" or `[data]` | A number pulled from Roblox's own public endpoints; the snapshot is in `data/` |
| "Our read:" | The authors' deduction. Reasoning, not a finding |
| "Start with:" | A starting value for your own game, derived from the real numbers above it. Tune it |
| "not known" | The research did not find it. Nobody guessed |

Player counts, prices and platform rules change. Each one here has a date. Roblox changed its recommendation system, its rules for reaching under-16s and its rules on video feeds within one year; check before you rely on any of them.

## What is thin

Stated plainly, so you know where to trust it less:

- **Timed first sessions.** Almost no source times what a new player does second by second, and nobody here played each game with a stopwatch. The first-session numbers are strongest for the collect-and-earn games, where the ladders allow arithmetic. Most genre pages say "not known" for the first minute.
- **What developers say.** Interviews exist for a handful of hits. For most games the reasons a design works are our reading of its numbers.
- **Peaks.** Trackers disagree, sometimes by a factor of two. Ranges are given where they do.
- **Retention by genre.** Roblox does not publish it. The only retention figures are platform-wide medians from one analytics vendor.
- **Session lengths.** Tracker estimates.
- **The stats routine.** `kit/stats-to-plan.md` and `tools/funnel.py` are built from Roblox's documentation and standard sample-size arithmetic. They have not been run on a live game's dashboard yet, and their example is invented.

If you can fill one of these from your own dashboard or your own stopwatch, see [CONTRIBUTING.md](CONTRIBUTING.md).

## How it was made

Researched and written in November 2026 with Claude, Anthropic's AI model: twenty research passes over Roblox's documentation and announcements, the games' own wikis, Roblox's public data endpoints, tracker sites and press, followed by a second pass on each genre for in-game numbers, then written to the standard in [CONTRIBUTING.md](CONTRIBUTING.md). The method, the sources and the limits are in [research/README.md](research/README.md).

The audience for most of these games is children. The handbook explains mechanics that work through loss, envy and scarcity, because leaving them out would make it useless, and it says on each page where the line is. [foundations/15-the-line.md](foundations/15-the-line.md) explains why.

## Licence

MIT. See [LICENSE](LICENSE). Game names and characters belong to their owners.
