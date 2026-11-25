# Why game designs fail

Read this once before using the rest of the handbook. It explains what the other pages are for.

Roblox games rarely fail on code. They fail on design, and the failure is usually visible on paper before anything is built. The same twelve mistakes appear again and again, in documents written by people and, more consistently, in documents written by AI models. A language model has never been bored, never lost something it cared about and never waited eight seconds for a fish to bite. It can produce a design that reads perfectly and plays like a form.

Each failure below has three parts: how it looks on paper, what happens in the game, and the tool in this handbook that prevents it. The last section is written for AI agents.

## The twelve failures

### 1. A list of features instead of a timeline

**On paper:** "Pets, rebirths, daily rewards, a shop, trading, leaderboards." Every item is reasonable.

**In the game:** nobody decided what happens at second 10, minute 2 and minute 5. The player meets the features in whatever order the menus present them. Most leave before reaching any.

**Instead:** write the first fifteen minutes as a script, one line per 20 seconds ([05-first-session.md](05-first-session.md)). A feature that has no line in the script does not exist for most players, because the median Roblox game sees 10.3% of new players return the next day ([02-the-platform.md](02-the-platform.md)).

### 2. No stopwatch

**On paper:** a loop drawn as a circle. "Cast, wait, reel, sell."

**In the game:** the wait is half the cycle. The circle did not say so.

**Instead:** a loop table with seconds in every row, dead time added up, and a treatment for every wait ([04-core-loop.md](04-core-loop.md)).

### 3. Invented from nothing

**On paper:** an original concept with original systems.

**In the game:** the player has to learn everything at once and learns nothing. Meanwhile every system is untested.

**Instead:** start from one live game that players already understand, keep its systems, and change one thing ([03-idea-and-reference.md](03-idea-and-reference.md)). Steal a Brainrot itself was built on the rights to an earlier game.

### 4. The twist is in the theme

**On paper:** "It's Steal a Brainrot, but with pets."

**In the game:** the player already has progress in the original. A new skin gives no reason to start again. A reskin of exactly this kind by one of Roblox's largest studios had 7 players in November 2026 ([slop/03-quality-bar.md](../slop/03-quality-bar.md)).

**Instead:** change the verb. Steal became break-and-steal, throw, kick, ride.

### 5. Nothing is at stake

**On paper:** every system is fair, safe and kind. Nothing can be lost. Nobody can interfere with anybody.

**In the game:** nothing matters, so nothing is worth watching, guarding or telling a friend about. The designer removed the reasons to stay while removing the reasons to be upset.

**Instead:** decide on purpose what the player can lose, how they can protect it, and what another player can do to them. Then check the result against [15-the-line.md](15-the-line.md). The biggest games on the platform run on loss, envy and scarcity ([slop/02-why-it-holds.md](../slop/02-why-it-holds.md)). They have also been criticised for it. Both facts belong in the design.

### 6. Systems before the toy

**On paper:** forty pages on progression, three lines on what the player does with their hands.

**In the game:** a well-organised way to unlock more of something nobody wanted to do in the first place.

**Instead:** build the core verb in grey boxes and play it for ten minutes with no rewards at all. Add systems only once that is worth doing ([04-core-loop.md](04-core-loop.md), rule 10).

### 7. Progress in menus

**On paper:** "Players upgrade their multiplier."

**In the game:** a number in a corner got bigger. Nobody else can see it and the player forgets it in a minute.

**Instead:** every gain is an object in the world that a stranger can see and rank ([slop/02-why-it-holds.md](../slop/02-why-it-holds.md), mechanism 2).

### 8. Written for adults at desks

**On paper:** a tutorial with six steps of text. A HUD with sixteen buttons.

**In the game:** about 65% of a typical game's players are on Android, most of those on phones with 2 to 4 GB of memory ([02-the-platform.md](02-the-platform.md)). Many are children. They do not read the text and cannot hit the buttons.

**Instead:** the title is the instruction, the first object is the tutorial, and the whole loop works under one thumb ([05-first-session.md](05-first-session.md), rule 11).

### 9. No numbers

**On paper:** "balanced progression", "rewarding loot", "engaging pacing".

**In the game:** whatever the first guess happened to be. Nobody can tell whether it is right, because nothing was specified to be wrong.

**Instead:** every statement carries a time, a number or what is on screen ([kit/nothing-detector.md](../kit/nothing-detector.md)); the price ladder is checked with `tools/pacing.py` before it is built ([06-progression-and-economy.md](06-progression-and-economy.md)).

### 10. The first test of skill comes first

**On paper:** "The game starts with an exciting challenge."

**In the game:** badge counts show that a skill gate keeps between a fifth and a half of the players who meet it ([04-core-loop.md](04-core-loop.md)). Placed at the start, it removes most of the traffic before the first reward.

**Instead:** reward first, purchase second, long goal third, skill after that.

### 11. A launch, then nothing

**On paper:** the design ends at release.

**In the game:** every hit checked in November 2026 had been updated within three days, including games at under 1% of their peak. Every dead clone had stopped updating. One co-op game held a 97% like ratio and still fell to about 1% of its peak when players ran out of things to do ([genres/tycoon.md](../genres/tycoon.md)).

**Instead:** plan the weekly update before launch and build three of them in advance ([13-live-ops.md](13-live-ops.md)).

### 12. Polishing instead of measuring

**On paper:** a list of improvements, chosen by what is most interesting to work on.

**In the game:** the leak is somewhere else. Steal a Brainrot's first rebirth once cost $1M and now costs $500K ([wiki](https://stealabrainrot.fandom.com/wiki/Rebirth)). **Our read:** somebody looked at where players stopped.

**Instead:** a funnel event for every step of the first session, the worst step fixed first, one change per update ([14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md)).

## If you are an AI agent

You will make these mistakes by default. The reasons are structural, so the fixes are procedural. Follow them even when your draft already looks good to you; that is when they matter.

| Your tendency | Why | What to do instead |
|---|---|---|
| You describe the game instead of scripting it | Describing is what text is good at | Produce the first-session script and the loop table before any prose. If you cannot fill a row, say so |
| You cannot feel a wait | You have no sense of time passing | Add up the seconds. Report cycle time, dead time and rewards per minute as numbers |
| You make everything safe and fair | You are trained to be agreeable | State what the player can lose and who can take it. Then apply the line. Do not remove stakes to avoid discomfort |
| You average | The most likely sentence is the most common one | Name one live reference game and one changed verb. Refuse to continue without them |
| You invent numbers that sound right | Fluency is not evidence | Take numbers from the teardowns and genre pages. Mark anything else "Start with" and run it through `tools/pacing.py` |
| Asked to improve a game, you add systems | Adding is easier than diagnosing | Ask for the funnel. Find the worst step. Change one thing in it |
| You praise the design you were shown | Agreement feels helpful | Run [kit/design-audit.md](../kit/design-audit.md). Report the failed gates first, in order of damage |
| You write "engaging", "rewarding", "satisfying" | Those words fit every game | Run [kit/nothing-detector.md](../kit/nothing-detector.md) on your own output before showing it |

The procedure that applies all of this is in [AGENTS.md](../AGENTS.md).
