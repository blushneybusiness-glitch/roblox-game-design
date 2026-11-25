# Writing standard

Everything in this repo follows the rules on this page. They exist because most game-design advice is true and useless: "make the core loop engaging", "reward the player", "add progression". Nobody can build from that, and nobody can check it.

If you add or change a page, hold it to the same rules.

## Rule 1: stopwatch, number, screen

Every design statement has to answer three questions:

1. **When** does it happen? (seconds or minutes from a named starting point)
2. **How much?** (a number: price, odds, rate, count, percentage)
3. **What does the player see or hear?**

If a sentence cannot answer at least two of the three, rewrite it or delete it.

| Vague (delete) | Specific (keep) |
|---|---|
| Give the player an early reward. | The first coin lands within 10 seconds of the player gaining control. It pops out of the object they hit, flies to the counter, and the counter ticks up with a sound. |
| Make progression feel meaningful. | Each new tier earns 4 to 6 times the tier before it and costs about 8 times as much, so a tier takes longer than the last one but the jump is visible the moment you buy it. |
| Add social features. | Six players per server, bases in a ring 40 studs apart, every base open to view, so within 10 seconds of joining a new player sees what a rich base looks like. |
| Use scarcity to drive engagement. | The shop restocks every 5 minutes. A rare seed appears in about 1 restock out of 30. The timer is on the HUD. |
| Make the game feel good. | Every hit plays a sound within 0.1 s, scales the target to 1.15 for 0.08 s, and spawns a number that rises 3 studs and fades in 0.6 s. |

## Rule 2: say where each claim comes from

A reader has to be able to tell a fact from an opinion. Use these forms and nothing else.

| Kind of claim | How to write it |
|---|---|
| A fact about a game or the platform | State it and link the source inline: `The seed shop restocks every 5 minutes ([wiki](https://...)).` |
| A number from this repo's own data snapshot | Tag it `[data]` and give the snapshot date: `The median top-100 game has 9 passes [data, Nov 2026].` |
| A practitioner's claim | Name the person and link it: `Tizzy, a producer of several simulator hits, reports ... ([video](https://...)).` Say what they shipped the first time they appear on a page. |
| Our own deduction | Start the sentence with **Our read:** |
| A suggested value for the reader's game | Put it in a table or line headed **Start with:**. These are starting points to tune, never facts. |

More rules for evidence:

- Player counts, prices, policies and rankings go stale. Give each one a month and a year.
- If a source is about mobile or PC games and not Roblox, say so in the sentence.
- If two sources disagree, give both.
- "Not known" is an acceptable answer. A guessed number is not.
- Do not cite a page you have not read.

## Rule 3: plain words

Write for a 14-year-old developer whose first language may not be English.

- Short sentences. One idea per sentence.
- The same word for the same thing on every page. The glossary below is the list.
- Tables for numbers. Prose for reasons.
- No words that praise without measuring. These are banned unless a number follows in the same sentence: *engaging, rewarding, satisfying, immersive, polished, balanced, fun, addictive, compelling, intuitive, juicy, smooth, seamless, robust, rich, deep, meaningful, dynamic, unique, innovative*.
- No openers that delay the point ("It is important to note that", "When it comes to").
- No hype. If a mechanic works, the numbers will say so.

## Rule 4: one job per page

- A **foundation** page explains one part of design that applies to every genre.
- A **genre playbook** follows [kit/templates/genre-playbook.md](kit/templates/genre-playbook.md) section by section. Do not add or drop sections.
- A **teardown** follows [kit/templates/teardown.md](kit/templates/teardown.md).
- A page links to other pages instead of repeating them.

## Rule 5: describe what works, and mark the line

This repo explains mechanics that hold attention, including the uncomfortable ones: loss, envy, scarcity, random rewards. Hiding them would make the repo useless, and the audience for these games is mostly children, so every page that covers such a mechanic also says where the line is. The line is defined in [foundations/15-the-line.md](foundations/15-the-line.md): no lies about odds or timers, no pressure at moments of loss, nothing that Roblox policy forbids, and nothing a parent would call a trick if they watched over the player's shoulder.

## Rule 6: do not copy

Paraphrase sources and link them. Quote only a short phrase when the exact wording matters. Wiki tables of numbers are facts and can be restated with a link; wiki prose cannot be pasted.

## Glossary

| Term | Meaning here |
|---|---|
| Fantasy | The feeling the game sells, said in one sentence a child could repeat. |
| Core verb | The one action the player repeats most. |
| Loop | A chain of steps that ends where it started, with the player slightly better off. |
| Cycle time | Seconds for one pass through the core loop. |
| Dead time | Seconds in a cycle where the player has no decision and no input. |
| First session | A new player's time from joining until they first leave. |
| Gate | A pass/fail check with a number, for example "first reward within 10 seconds". |
| Bounce | Leaving within the first 60 seconds. |
| D1, D7, D28 | Share of new players who play again 1, 7 and 28 days after their first day. |
| CCU | Concurrent users: players in the game at the same moment. |
| Sink / source | Where currency leaves / enters the economy. |
| Rebirth (prestige) | Resetting progress in exchange for a permanent multiplier or new content. |
| Flex | Anything a player owns or has done that other players can see. |
| Live ops | Updates, events and offers after launch. |
| Pass / product | Game pass (bought once) / developer product (can be bought again). |
| R$ | Robux. |
| Slop | Fast-made, trend-following games built on a proven simple loop. See [slop/](slop/). |

## How to add a teardown

1. Copy [kit/templates/teardown.md](kit/templates/teardown.md) to `teardowns/<game-name>.md`.
2. Fill every section from sources you have read. Write "not known" where you could not find a number.
3. Time the first session yourself on a fresh account with a stopwatch if you can. Say that you did, and on what device.
4. Add the game to the table in `teardowns/README.md` and link it from the genre playbook it belongs to.

## How to update the data

`python tools/snapshot.py` pulls the public charts again and `python tools/analyze.py` rebuilds `data/ANALYSIS.md`. Both need only Python 3.10 or newer and no account. See [data/README.md](data/README.md).
