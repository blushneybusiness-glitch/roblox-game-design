# Tower of Hell

> Climb a randomly built tower with no checkpoints before the clock runs out; it is the obby that has held a large audience the longest, with 29.5B visits in eight years.

| | |
|---|---|
| Studio | YXceptional Studios (group) |
| Released | 18 Jun 2018 |
| Genre | Tower obby ("Obby & Platformer", "Tower Obby" in the API) |
| Peak concurrent players | 75K, August 2026 ([RoWatcher](https://rowatcher.com/games/703124385); single tracker, and a peak eight years after launch, so treat with caution) |
| Players now | 23,802 (Roblox public API, 25 Nov 2026) |
| Players per server | 20 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

Identity, visits, votes (4,408,822 up, 1,577,375 down, 73.6% positive) and server size from the [games API](https://games.roblox.com/v1/games?universeIds=703124385) and [votes API](https://games.roblox.com/v1/games/votes?universeIds=703124385). Round rules from the [Tower of Hell wiki](https://tower-of-hell.fandom.com/wiki/Home), read 25 Nov 2026. Wiki Robux prices are UK regional prices, and the wiki may lag the game.

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Shop | Buys one gear or mutator for this round with coins | Not known | Shop at the bottom; a Pyx NPC takes 30% or 50% off one gear, a Pixy NPC 30% off one mutator | Coins down 40 to 500 |
| Climb | Jumps up 6 random sections (noob) or 12 (pro) | About 80 per noob section, 50 per pro section (our arithmetic: 480 s / 6, 600 s / 12) | Timer on screen | Coins and XP accrue per section |
| Fall | Drops to the bottom | 0 | No checkpoint | Coins already earned are kept |
| Finish | Touches the neon door on the finish section | | A "made it to the top" chat line; the timer runs twice as fast for everyone still climbing | Up to 100 coins and 100 XP (noob), 250 (pro) |
| Next round | A new tower is drawn | | New layout | Level bar |

Cycle time: one round, at most 8 minutes (noob) or 10 (pro). Each finisher doubles the timer's speed; whether two finishers make it 4x is not confirmed. Our arithmetic: a first finish with 4:00 left makes that 4:00 pass in 2:00. Dead time: from finishing or giving up until the next tower; length not known.

Sources: [Noob Towers](https://tower-of-hell.fandom.com/wiki/Noob_Towers), [Pro Towers](https://tower-of-hell.fandom.com/wiki/Pro_Towers), [Finish](https://tower-of-hell.fandom.com/wiki/Finish), [Gears](https://tower-of-hell.fandom.com/wiki/Gears), [Mutators](https://tower-of-hell.fandom.com/wiki/Mutators).

## 2. First session

No recorded first session was found. This is assembled from the wiki rules.

| Time | What happens |
|---|---|
| 0:00 to 0:10 | Spawn in a 6-section noob tower with the 8-minute timer running. A white portal under the start platform leads to pro towers. |
| 0:10 to 1:00 | First sections climbed; coins paid from the first section beaten. |
| 1:00 to 5:00 | First fall to the bottom (our read: no checkpoints makes this near certain). |
| 5:00 to 15:00 | A first finish pays 100 coins and 100 XP, enough for level 1 and one skill point, and enough coins for a Trowel (40) plus a Speed Coil (60) next round. |

First reward: the first section beaten. First rare moment: a secret section, about once per 22.6 noob towers. First long goal: the skill tree. Pro towers never lock; any player can take the portal ([Pro Towers](https://tower-of-hell.fandom.com/wiki/Pro_Towers)). No teaching is described in the sources.

## 3. Progression

**Sections.** The wiki counts 330 vanilla sections, plus secret, vaulted, removed, horizontal, start and finish sections, 482 ever. Seven vanilla sections were added on 7 Aug 2026, the first since 2023. Each section is labelled Easy, Medium or Hard and Short, Medium or Long ([Sections](https://tower-of-hell.fandom.com/wiki/Sections)). Two wiki pages disagree on secret sections (24 versus 36).

**The draw.** Weighted random. Every vanilla section has weight 1,000; most secret sections 50; Saboteur 250. Total 332,451. That gives about 1 in 135.6 per section slot for a secret, one per 22.6 noob towers, and 1 in 1,329.8 for Saboteur. The wiki marks these weights as an editors' reconstruction ([Secret Sections](https://tower-of-hell.fandom.com/wiki/Secret_Sections)).

**Coins.** Max coins x (sections beaten / total)^2, rounded down ([Coins](https://tower-of-hell.fandom.com/wiki/Coins)). Our arithmetic:

| Sections beaten | Noob (6, max 100) | Pro (12, max 250) |
|---|---|---|
| 1 of 6 / 3 of 12 | 2 | 15 |
| 3 of 6 / 6 of 12 | 25 | 62 |
| 5 of 6 / 9 of 12 | 69 | 140 |
| All | 100 | 250 |

Double Coins (pass or mutator) doubles this; both together give 3x, not 4x. Coins are kept on leaving mid-round.

**Levels.** XP equals coins earned but is lost on leaving mid-round. Level L needs 100 x L more XP; cumulative XP = 50 x (L^2 + L). One skill point per level ([Levels](https://tower-of-hell.fandom.com/wiki/Levels)).

| Level | Cumulative XP | Noob wins (our arithmetic) |
|---|---|---|
| 1 | 100 | 1 |
| 5 | 1,500 | 15 |
| 14 | 10,500 | 105 |
| 80 (skill tree maxed) | 324,000 | 3,240 (or 1,296 pro) |

**Shop.** Gear and mutators last one round. Prices in coins for noob / pro / max (18 sections):

| Item | Noob | Pro | Max | Share of one noob win |
|---|---|---|---|---|
| Trowel (platform lasts 5 s, 8 s cooldown) | 40 | 76 | 112 | 40% |
| Speed Coil | 60 | 120 | 180 | 60% |
| Hourglass (freezes moving parts) | 72 | 144 | 216 | 72% |
| Gravity Coil / Hook | 80 | 152 | 224 | 80% |
| Fusion Coil | 90 | 150 | 210 | 90% |
| Extra Time (+2 min) | 50 | 86 | 122 | 50% |
| High Speed (+25%) | 100 | 160 | 220 | 1 win |
| Low Gravity (-25%) | 130 | 220 | 310 | 1.3 wins |
| Invincibility | 500 | 860 | 1,200 | 5 wins |

Our arithmetic: pro prices are about 1.7 to 2 times noob prices while a pro win pays 2.5 times, so gear is cheaper per win in pro towers.

**Skill tree.** 80 points to max; one branch active at a time. Speed Coil +75% / +140% / +200% for 1 / 2 / 5 points; Gravity Coil Double Jump 14 points; Trowel block 8 then 16 studs for 2 and 3 points ([Skill Tree](https://tower-of-hell.fandom.com/wiki/Skill_Tree)).

**Badges** ([badges API](https://badges.roblox.com/v1/universes/703124385/badges?limit=100)):

| Badge | Holders | Share of Newbie (our arithmetic) |
|---|---|---|
| Newbie (beat a first tower) | 67.49M | 100% |
| Mutated | 28.47M | 42% |
| Pro | 16.16M | 24% |
| Explorer | 3.66M | 5.4% |
| Saboteur (steal the power source) | 228,056 | 0.34% |
| Maxed (skill tree full) | 42,675 | 0.063% |
| Certified Beast | 2,323 | |

The Pro badge's exact condition is not in the sources.

## 4. Session and return hooks

A new random tower every round. A rare secret section to chase. A new discount on one gear and one mutator every round. A rotating effect stock added on 8 Jun 2026 ([Home](https://tower-of-hell.fandom.com/wiki/Home)). Daily rewards, offline progress and a weekly update day: not known.

## 5. Other players

Twenty players climb the same tower. Each finisher speeds the clock for the rest. Private server owners can skip rounds, set tower size and lock the shop ([games API](https://games.roblox.com/v1/games?universeIds=703124385)). No trading, theft or co-op is documented. **Our read:** the clip is a fall from the last section with the sped-up clock on screen.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Double Coins | Pass | 195 | 2x coins |
| Halloween Coils Bundle | Pass | 90 | Cosmetic coils (contents not known) |
| Haunted Bundle | Pass | 480 | Not known |
| Invisibility / Double Jump / Bunny Hop | Product (mutator) | 9 / 15 / 20 (UK) | One round |
| Checkpoints | Product (mutator) | 11 (UK) | A checkpoint every other section, one round |
| Double Coins mutator | Product | 11 (UK) | One round |
| Coins | Product | 200 for 9, 500 for 25, 2,000 for 75, 10,000 for 350 (UK) | 22 to 29 coins per R$ |
| Skill Reset | Product | 20 or 50 (the wiki gives both); 20 in the snapshot | Refund skill points |

Passes from the [passes API](https://apis.roblox.com/game-passes/v1/universes/703124385/game-passes?passView=Full&pageSize=100), 25 Nov 2026; Summer Bundle and Infinite Coins have no current price. Products from the wiki. Best sellers: not known.

**Developer products [data, Nov 2026].** 21 on sale, 9 to 1,200 R$, median 20 R$. The snapshot, read without an account, gives the same prices as the UK rows above, and the 3 passes on sale match. One more coin product, 100 Coins at 65 R$ (1.5 coins per R$), sits far off the ladder. The rest of the list, 6 of 21:

| Product | R$ | What it does |
|---|---|---|
| One Week Membership | 35 | Buy Robux-only gear and mutators with coins (description) |
| One Month Membership | 120 | Same, for a month |
| Common Stock | 15 | Stock ladder: 15, 30, 60, 200 |
| Legendary Stock | 200 | |
| Hourglass | 15 | Stops time (description) |
| Blue Halo | 1,200 | Top price; cosmetic by name |

Our arithmetic: the month membership costs 3.4 weeks' price for about 4.3 weeks.

Our arithmetic: one noob win (100 coins) is worth about 4.5 R$ at the smallest coin pack.

## 7. Why it works

What is measured: 8 years live, 23.8K players now, 73.6% positive. The developers' reasons are not in the sources.

**Our read:**
- 330 sections drawn at random make every round a new course without new building; none were added from 2023 to August 2026.
- No checkpoints keeps the skill floor high; paying for partial progress means a failed climb still earns.
- The finisher speed-up turns other players into pressure on screen.
- Gear at 40% to 90% of one win means every win buys an edge for the next round.

## 8. What went wrong

- From 24 Mar to 2 May 2021 the timers were cut to 6 and 8 minutes, then put back to 8 and 10 ([Noob Towers](https://tower-of-hell.fandom.com/wiki/Noob_Towers)).
- Gear and mutators cost Robux until 16 Aug 2020, when they moved to coins ([Mutators](https://tower-of-hell.fandom.com/wiki/Mutators)).
- Complaints, failed updates and decline: not known. 26.4% of votes are negative.

## 9. What to take from it

- No checkpoints, but pay per section as max x (progress)^2, so a failed climb still earns.
- An 8-minute round for 6 sections: about 80 seconds per section.
- Each finisher doubles the clock speed for everyone else.
- A pool of 330 sections at equal weight, secrets at 1/20 weight: one rare find per 22.6 rounds.
- Gear priced at 40% to 90% of one win, lasting one round.
- Level XP of 100 x level: level 1 after one win, the last skill point after 3,240.
- A membership at 35 R$ a week or 120 R$ a month that lets coins buy the Robux-only gear [data, Nov 2026].

## Sources

- Roblox public API, 25 Nov 2026: [games](https://games.roblox.com/v1/games?universeIds=703124385), [votes](https://games.roblox.com/v1/games/votes?universeIds=703124385), [passes](https://apis.roblox.com/game-passes/v1/universes/703124385/game-passes?passView=Full&pageSize=100), [badges](https://badges.roblox.com/v1/universes/703124385/badges?limit=100).
- Tower of Hell wiki: [Home](https://tower-of-hell.fandom.com/wiki/Home), [Noob Towers](https://tower-of-hell.fandom.com/wiki/Noob_Towers), [Pro Towers](https://tower-of-hell.fandom.com/wiki/Pro_Towers), [Sections](https://tower-of-hell.fandom.com/wiki/Sections), [Secret Sections](https://tower-of-hell.fandom.com/wiki/Secret_Sections), [Coins](https://tower-of-hell.fandom.com/wiki/Coins), [Levels](https://tower-of-hell.fandom.com/wiki/Levels), [Gears](https://tower-of-hell.fandom.com/wiki/Gears), [Mutators](https://tower-of-hell.fandom.com/wiki/Mutators), [Skill Tree](https://tower-of-hell.fandom.com/wiki/Skill_Tree), [Finish](https://tower-of-hell.fandom.com/wiki/Finish).
- [RoWatcher](https://rowatcher.com/games/703124385) for the peak.
- Genre playbook: [genres/obby.md](../genres/obby.md).
