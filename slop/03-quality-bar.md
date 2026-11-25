# Quality slop: hit against dead clone

For every slop hit there are hundreds of copies with a handful of players. This page lists what is measurably different between them, then what is probably different but could not be measured, then a checklist.

## The graveyard

Ten copies, checked through Roblox's public API on 25 November 2026:

| Clone (players now) | Created | Last updated | Like ratio | What it did |
|---|---|---|---|---|
| "Steal a Pet" by BIG Games, one of the largest studios on Roblox (7) | 17 Jun 2025 | 6 Feb 2026 | 86.6% | Same verb as Steal a Brainrot, 32 days later, then abandoned |
| "Italian Brainrot Thieves" (231) | 3 Jun 2025 | 26 Oct 2025 | 80.8% | 10-player servers; stopped updating |
| "Steal Anime!" (457) | 7 Jun 2025 | 3 Aug 2025 | 86.3% | Stopped updating after two months |
| "STEAL a Brainrot or DIE" (7) | 3 Feb 2026 | 17 Sep 2026 | 91.7% | Launched nine months after the original |
| "KICK FREE BLOCK (X999)" (1,256) | 12 Aug 2026 | 17 Aug 2026 | 70.2% | Bait title; updated for five days |
| "Kick for ADMIN PANEL! X999999M" (78) | 26 Jul 2026 | 28 Jul 2026 | 63.0% | Bait title; updated for two days |
| "Steal A Pet" by another studio (65) | 23 Aug 2026 | 10 Oct 2026 | 82.8% | Same verb, late |
| "+1 Jump Every Second" (1) | 12 Nov 2026 | never | 75.0% | A 2022 idea relaunched unchanged |
| "Grow a Garden 2" (about 1,000) | 21 May 2026 | 3 Nov 2026 | not recorded | A sequel in name; down 55% in 30 days |
| "Plants VS Zombies [NEW]" (42) | not recorded | not recorded | 68.6% | A borrowed name |

And three followers that worked:

| Follower | Created | What it changed | Result |
|---|---|---|---|
| Break and Steal an Egg | 5 Sep 2026, a week before Steal An Egg's surge | Break eggs with a pickaxe, escape guards, an index to fill | 1.31M peak on 18 Oct 2026; 62K now |
| Throw a Seed | 7 Nov 2026, two weeks after Throw Food For Animals took off | The thing thrown and what it produces | 44K now |
| Throw a Friend for Monsters | 3 Nov 2026 | The thing thrown is another player | 12K now |

Sources: Roblox public search, game and vote endpoints, 25 Nov 2026; [RoStats records](https://rostats.io/records).

## What is measurably different

### 1. The hit is still being updated. The clone is not.

Every hit was updated within three days of the check: Steal An Egg on 24 November, Throw Food For Animals on 25 November, Steal a Brainrot on 24 November, Grow a Garden on 25 November. That includes two games at under 1% of their peak. The clones stopped after two days, five days, two months.

**Our read:** an update rhythm is the cheapest quality signal there is and the one clones fail most often. A copy is usually a single push. The hits are services.

### 2. The follower that works changes the verb.

Steal became break-and-steal, throw, kick, ride. BIG Games kept the verb, changed the collectible from brainrots to pets, and ended with 7 players. A big studio's art and audience did not save a reskin.

**Our read:** players do not move to a second copy of something they already have progress in. They try a neighbour that offers a new action with the same payoff.

### 3. The follower that works is early.

Break and Steal an Egg existed a week before the game it followed broke out. Throw a Seed appeared about two weeks after its original took off. The copies of Throw Food For Animals made six days after its breakout sit at 3,000 to 4,000 players; same-verb copies made a month or more late sit in the hundreds or lower.

**Our read:** the window is about two weeks from the breakout, and most of the players inside it stay with the original. A follower is competing for the players who want something next to the hit, not for the hit's players.

### 4. The hit's title is plain. The clone's title is bait.

Hits: verb, then thing. Clones: "X999999M", "ADMIN PANEL", "FREE". The bait titles carry like ratios of 59% to 70%, against 85% to 97% for the hits. A title that promises what the game does not deliver gets the click and then the dislike, and Roblox's discovery documentation says experiences with copied or misleading titles and thumbnails are shown less ([Discovery docs](https://create.roblox.com/docs/production/promotion/discovery)).

A like ratio does not pick winners, though. Plenty of dead clones are rated above 90%. A low ratio flags a broken promise; a high one only keeps you in the race.

### 5. The hit has a long ladder.

Steal An Egg: 15 biomes with gates up to 250 billion Speed, 150 pets in 10 tiers. Steal a Brainrot: 19 rebirths and about 580 units. Throw Food For Animals: 19 areas and 50 foods two months after launch. The clones have no wikis at all, which is its own measurement: nobody found enough in them to write down.

### 6. The hit's server size fits its game.

Collect-and-steal hits use 4 to 8 players per server. Two of the dead clones above used 10.

## What is probably different (not measured)

No research could measure these from the outside, so everything in this part is **our read**. Each is checkable on your own game in an afternoon.

| Quality | The check |
|---|---|
| Speed of the first minute | Stopwatch from gaining control to owning a unit that earns. Under 20 seconds on a phone. |
| Feedback | Every buy, collect, steal, lock and reveal has its own sound and a visible reaction that starts within 0.1 seconds. Mute the game: can you still tell what just happened? Close your eyes: can you still tell? |
| Phone performance | Android is about 65% of a typical game's players, and about 60% of those phones have 2 to 4 GB of memory ([Roblox docs](https://create.roblox.com/docs/performance-optimization/test-on-hardware)). A full server means 6 or 8 bases of animated units. Test a full server on a 3 GB Android phone. |
| One-thumb play | Everything in the core loop can be done with the right thumb. Buttons at least 48 pixels. Nothing important under the left thumb's stick. |
| Trust | A unit a player earned is never lost to a bug, a disconnect or a bad save. One viral "I lost everything" clip costs more than a week of updates. |
| Cheat resistance | Steal a Brainrot has about 200 public cheat scripts for auto-collecting and auto-stealing ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)). In a game about theft, a cheater takes real things from real children. The server decides every purchase, every carry and every lock. |
| A readable screen | Six things or fewer on the HUD at rest: cash, the clock, lock, the next goal, shop, settings. |

Quality here does not mean art. Kotaku said Grow a Garden looked like a prototype ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)) while it held the all-time record. It means tuning, speed, trust and showing up every week.

## Checklist

Hold your game against this before spending anything on promotion. Each line is pass or fail.

**Idea**

- [ ] I can say in one sentence which live hit this follows and which verb I changed.
- [ ] If I am following a wave, the original broke out less than two weeks ago. If not, the game stands without the wave.
- [ ] The title is a verb and a thing, two to four words, with no "X999", "FREE", "ADMIN" or a borrowed name.
- [ ] No character, name or art in it belongs to someone else. See [05-after-the-peak.md](05-after-the-peak.md).

**First five minutes**

- [ ] From gaining control to owning an earning unit: under 20 seconds, measured on a phone.
- [ ] The first unit pays for itself in 30 seconds or less.
- [ ] No purchase in the first hour has a payback above 300 seconds (`python tools/pacing.py`).
- [ ] The player reads at most ten words to get through the first five minutes.
- [ ] No purchase offer and no self-opening window in the first five minutes.

**Structure**

- [ ] 4 to 8 players per server, bases within sight of each other.
- [ ] Everything owned is a visible object; three bases can be ranked by wealth from one screenshot.
- [ ] Every unit rolls for an upgraded version; the odds are shown in the game and match the server.
- [ ] A 5-minute clock is on the HUD.
- [ ] The loss rules are written down, nothing is lost while offline, and no purchase window opens by itself at a loss.
- [ ] The first rebirth is reachable in 20 to 40 minutes and gives something to do, something to show and a number.
- [ ] A steady player does not run out of ladder in the first 3 hours.

**Operations**

- [ ] Three Saturday events are built before launch.
- [ ] The update day and hour are fixed and shown in the game.
- [ ] A full server holds 30 frames a second on a 3 GB Android phone.
- [ ] Every purchase, carry and lock is decided by the server.
- [ ] Funnel events are logged for each step of the first five minutes ([kit/templates/first-session-script.md](../kit/templates/first-session-script.md)).

Next: [04-build-it.md](04-build-it.md).
