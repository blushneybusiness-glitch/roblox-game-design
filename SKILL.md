---
name: roblox-game-design
description: Designs, audits and fixes Roblox game designs using sourced teardowns of real hits, a playbook for every genre, a scored design audit and a pacing simulator. Use when someone wants to design a Roblox game, check whether an idea is good, find out why players leave or do not come back, make a game stickier, build a trend or "slop" game (steal, grow, +1, brainrot), set prices, plan updates, or tear down how a hit works. Covers simulators, tycoons, RNG, obbies, horror, survival, fighting, anime RPGs, shooters, sports, tower defense, roleplay, pet games, dress-up, hangouts, driving, sandbox, party and social-deduction games.
---

# Roblox game design

This folder is a handbook. Follow [AGENTS.md](AGENTS.md) in this folder: it has the eight rules, the procedure for each kind of request, and the map of pages.

The short form:

1. **Name the reference game and the changed verb**, or ask for them. Do not design without them.
2. **Read the genre playbook** in `genres/` (index: [genres/README.md](genres/README.md)) and, for trend games, [slop/](slop/README.md).
3. **Produce the documents, not a description**: the one-page design, the loop table with seconds, the first-session script, the economy sheet. Templates are in `kit/templates/`.
4. **Check the numbers**: `python tools/pacing.py <economy.json>`.
5. **Run the audit**: [kit/design-audit.md](kit/design-audit.md). Report failed gates first.
6. **Run the nothing detector on your own answer**: [kit/nothing-detector.md](kit/nothing-detector.md).

For a game that is live and losing players, start from [foundations/14-metrics-and-diagnosis.md](foundations/14-metrics-and-diagnosis.md) and change one thing.

Never invent a number. Use the ones in this folder with their sources, or label a proposal "Start with". The audience for these games is mostly children: every mechanism has a line, and it is in [foundations/15-the-line.md](foundations/15-the-line.md).
