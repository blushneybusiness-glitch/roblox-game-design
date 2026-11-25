# The nothing detector

Most game-design writing is true and useless. "Make the core loop engaging." "Reward the player early." "Add social features." Nobody can build from these sentences and nobody can prove them wrong, which is why they survive. This page is a test that removes them.

Run it on any design document, any audit, any piece of advice, and on your own writing before you show it to anyone.

## The test

For each sentence that makes a claim about the game, look for three things:

| Tag | The sentence says | Example |
|---|---|---|
| **W** (when) | A time, measured from a named starting point | "within 10 seconds of gaining control" |
| **N** (number) | A price, rate, count, odds or percentage | "costs $25 and earns $1 a second" |
| **S** (screen) | What the player sees or hears | "the coin flies to the counter and it ticks with a sound" |

- Two or three tags: keep it.
- One tag: rewrite it until it has two.
- No tags: delete it. Nothing was lost.

Then check every number in what is left:

| The number is | It must have |
|---|---|
| A fact about a real game or the platform | A source and a date |
| Measured in your own build | The device, and who held the stopwatch |
| A proposal for your game | The label "start with", and the reasoning or the real number it was derived from |
| None of these | It is invented. Remove it or find it |

## Words that fail on sight

These words describe a hope, not a design. Each one must be replaced by the measurement it stands for.

| Word | Replace with |
|---|---|
| engaging, compelling, addictive | How many rewards per minute; how long the session; what share return tomorrow |
| rewarding, satisfying | What the player gets, how soon, and what it looks and sounds like |
| polished, juicy, smooth | Which actions have a sound and a visible reaction, and how fast the reaction starts |
| balanced, fair | The win rate, the payback time, the odds, or the time to the next purchase |
| intuitive, accessible | How many words the player reads, how many buttons are on screen, which device it was tested on |
| immersive, atmospheric | What is on screen and in the speakers, and what the player is doing while it happens |
| deep, rich, meaningful | How many real decisions per minute and what each one costs |
| social | How many players per server, what one can see of another, and the verb between them |
| progression | The ladder: its steps, prices and the minutes between them |
| retention mechanics | What is unfinished when the player leaves and what has changed when they return |
| unique, innovative | The one thing that differs from the named reference game |
| fun | Nothing. Describe what happens |

## Rewrites

| Fails | Passes |
|---|---|
| Hook the player in the first few seconds. | The object the title names is within 10 studs of the spawn. The first tap on it pays out within 10 seconds. |
| Provide a smooth onboarding experience. | No text in the first five minutes beyond three-word pointers. The first three attempts at the core action cannot fail. |
| Give players a sense of progression. | Every purchase adds an object to the player's base. At rebirth 2 the base gains a second floor that neighbours can see. |
| Balance the economy carefully. | The first unit pays for itself in 25 seconds. No unit in the first hour takes more than 300. The longest wait between purchases in the first 15 minutes is under 90 seconds. |
| Use rarity to create excitement. | Each unit has an 11% chance of a gold version at 1.5 times income and a 0.5% chance of a rainbow version at 20 times, announced to the server. |
| Encourage players to return daily. | The shop restocks every 5 minutes and crops grow offline, so a returning player's first action is a harvest. Three daily offers change at midnight UTC. |
| Add social and competitive elements. | Six players per server in a ring of bases. Any unlocked base can be raided for one unit. The lock lasts 60 seconds. |
| Make combat feel impactful. | A hit plays a sound within 0.1 seconds, freezes both characters for 0.1 seconds, and knocks the target back 6 studs. The fourth hit of a string always knocks down for 2 seconds. |
| Create a scary atmosphere. | Each monster has one sound that plays before it appears and one action that defeats it. The first one arrives by the third room. |
| Monetise without being pay-to-win. | Two passes: double cash at 199 R$ and a cosmetic tag at 249 R$. No purchase window opens by itself in the first five minutes or when the player loses something. |
| Keep the game fresh with regular updates. | An update every Saturday at 15:00 UTC with five to ten new units, one limited upgrade tier, and a 45-minute event. A countdown is on the HUD from Thursday. |
| Optimise for mobile. | A full server holds 30 frames per second on a 3 GB Android phone. Every control in the loop is reachable with the right thumb. Buttons are at least 48 pixels. |

## Seven sentences that sound like design

Each of these appears in almost every weak design document. Each is a heading pretending to be content.

1. "The core loop is collect, upgrade, unlock." (Every game. Which seconds?)
2. "Players will be motivated by progression." (To do what, next, on which screen?)
3. "We will use a variable reward schedule." (With which odds, shown how?)
4. "The game will have strong social features." (Which verb between two players?)
5. "Monetisation will be fair and optional." (What is sold, for how much, at what moment?)
6. "We will iterate based on analytics." (Which event, which number, which threshold?)
7. "The art style will be appealing to our audience." (Which reference, and what was measured from it?)

When one of these appears, replace it with the table or script it is avoiding.

## For AI agents

Run the test on your own output before returning it. Do it literally:

1. List every sentence that makes a claim about the game.
2. Tag each W, N, S.
3. Rewrite or delete anything with fewer than two tags.
4. For every number, state which of the four kinds it is. If it is none, remove it.
5. Search your text for the words in the table above and replace each.

If a user asks for design advice and you cannot produce sentences that pass, the honest answer is a list of the measurements you need from them: the loop timings, the first-session funnel, the price ladder. Ask for those. Do not fill the space.
