# Prompts

Prompts to paste into an AI assistant that has this repository available (cloned into the project, installed as a skill, or attached as files). Each one points the assistant at [AGENTS.md](../AGENTS.md) so it follows the procedure instead of improvising.

Replace the parts in brackets.

## Design a game

```
Follow AGENTS.md in the roblox-game-design repository.

I want to design a Roblox game. It is closest to [live game], and the one thing I change is [the verb the player does differently].
Team: [how many people], time: [how many weeks]. It is [a bet on a current trend / meant to last years].

Read the genre playbook and the reference game's teardown. Then produce, in this order: the one-page design, the core loop table with seconds, the first-session script to minute 15, the economy sheet with its JSON, and the update plan for three weeks. Run tools/pacing.py on the JSON and fix the ladder until it passes. Finish by running kit/design-audit.md on your own design and tell me which gates fail.

Do not describe the game in general terms. Every statement needs a time, a number, or what is on screen.
```

## Check an idea before building

```
Follow AGENTS.md in the roblox-game-design repository.

Idea: [one sentence].

Tell me: which live game it starts from and what verb it changes; three games that tried something close, with their peaks and current players from data/ or the teardowns; whether it is a wave bet or an evergreen bet and what that means for timing; and the five gates in kit/design-audit.md it is most likely to fail. If you need something from me to answer, ask before guessing.
```

## Audit my game

```
Follow AGENTS.md in the roblox-game-design repository. Run kit/design-audit.md.

Game: [name and link, or the design documents].
What I have measured: [share of new players still present at 1 minute and 5 minutes, next-day return, session length, anything else].

Report in the audit's format: verdict, failed gates first, the score with evidence for each line, five fixes as hypotheses (one stat, one change, the number you expect, when to read it), and what you could not judge. Do not open with what is good.
```

## Fix one number

```
Follow AGENTS.md in the roblox-game-design repository.

My [stat] is [value]. [Anything known about where players leave.]

Use foundations/14-metrics-and-diagnosis.md to find the stage and the likely cause. Check the cause against what the game does at that moment: [describe the first minutes, or attach the script]. Propose one change, with the number you expect and how many players I need before I can trust the result.
```

## Make a trend game

```
Follow AGENTS.md in the roblox-game-design repository. Read slop/README.md and slop/05-after-the-peak.md first and tell me the odds and the timing honestly.

The hit I am following: [game]. It broke out on [date].
My changed verb: [verb], or propose three.

Then follow slop/04-build-it.md step by step and check the result against slop/03-quality-bar.md.
```

## Tear down a game

```
Follow AGENTS.md in the roblox-game-design repository. Use kit/templates/teardown.md.

Game: [name and link].

Pull what is public: players, server size, passes with prices, and the badge list with award counts, which gives a funnel of how far players get. Read the game's wiki for the ladder, odds and timers. Write "not known" for anything you cannot find. Finish with three to six structures another game could reuse, each with its number.
```

## Plan the next four updates

```
Follow AGENTS.md in the roblox-game-design repository. Use foundations/13-live-ops.md and kit/templates/update-plan.md.

Game: [name]. Worst stat right now: [stat and value]. Team hours per week: [number].

For each of the next four weeks: the things players can collect, the limited item, the event moment with its day and hour, the one stat the update should move and by how much.
```
