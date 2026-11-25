# Social deduction

> **The feeling sold:** "One of us is the killer. Maybe it's me this time, and nobody knows."

This page covers round games built on hidden roles or on one hunter against many: [Murder Mystery 2](../teardowns/murder-mystery-2.md), Flee the Facility, hide-and-seek games, and impostor or werewolf games. Player counts marked "now" are from the Roblox public API, 25 Nov 2026, a weekday.

The evidence is uneven. The two leaders have wikis full of item prices and almost no clocks. Impostor-style games have almost no documentation at all. Where a number is missing, this page says so.

## At a glance

| | |
|---|---|
| Core verb | Survive the round without being identified or caught (innocent, survivor, hider); find and stop the hidden player (sheriff, seeker); kill unseen (murderer, Beast) |
| Study these first | [Murder Mystery 2](../teardowns/murder-mystery-2.md): a 2014 game with 119,439 players now, carried by a cosmetic trading economy. Flee the Facility: the best-documented clocks and reward tables in the genre. Hide and Seek Extreme: the simplest version, still running since 2015. Ink Game's Hide and Seek round (see [party-and-minigames.md](party-and-minigames.md)): a 50/50 split with a rule that forces seekers to act. |
| Session that works | not known for any game in this genre |
| Players per server | Flee the Facility 5, Murder Mystery 2 12, Hide and Seek Extreme 14, Imposters and Roles 15, Breaking Point 2 16, Who's Lying 21 (Roblox public API, 25 Nov 2026) |
| Who owns the genre | Old leaders. Murder Mystery 2 (2014) 119,439 now; Flee the Facility (2017) 12,080; Hide and Seek Extreme (2015) 2,442. Impostor and werewolf clones sit between 132 and 2,526 |
| Build cost | **Our read:** low for the round itself (one map, two or three roles, one clock). The cost is in the cosmetic catalogue: Murder Mystery 2 has 124 godly weapons alone |
| Money comes from | Cosmetic weapons through soft-currency or premium-currency boxes, a VIP or Elite pass, and premium currency packs |
| What kills clones | A copy of the round without an item economy: the leaders' rounds are simple, and the clones without a catalogue sit at 100 to 2,500 players |

## Why people play it

Our research found no player survey. The structure they show:

- **A small secret.** In Murder Mystery 2 only the murderer and the sheriff know their roles. Everyone else guesses ([wiki: Roles](https://murder-mystery-2.fandom.com/wiki/Roles)).
- **A chance at the scarce role every round.** Each round, every Murder Mystery 2 player sees a percentage chance of being Murderer. It starts low and rises each round they are not picked ([wiki: Murderer](https://murder-mystery-2.fandom.com/wiki/Murderer)).
- **Short rounds.** Murder Mystery 2's innocents win if 3 minutes pass ([rblxguide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide)).

**Our read:** the player buys two feelings in one round. As an innocent, three minutes of suspicion with a cheap way out (die, wait, try again). As the murderer, the power of knowing. The rising percentage is a promise that the second feeling is coming.

## The loop, with a stopwatch

Leader: Murder Mystery 2.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Lobby and vote | Walks into a voting room to pick 1 of 3 random maps | not known | Three map options; with no votes, one is picked at random | Votes |
| 2. Role card | Reads their role | not known | Their role and their percentage chance of Murderer | Murderer chance rises if not picked |
| 3. Round starts | Innocents scatter and collect coins | 0 to 10 | The murderer has no knife for the first 10 seconds | Coins, up to 40 |
| 4. Hunt | Murderer kills; sheriff watches and shoots; innocents hide and collect | 10 to 180 | Bodies, a gun shot, a dropped gun | Innocents left; 5 XP per second survived |
| 5. End | Round ends on timeout, murderer death, or everyone dead | 180 at most | Winner screen | XP (table below) |

Sources: [MM2 wiki main page](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2), [Maps](https://murder-mystery-2.fandom.com/wiki/Maps), [Hero](https://murder-mystery-2.fandom.com/wiki/Hero), [Coins](https://murder-mystery-2.fandom.com/wiki/Coins), [rblxguide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide). The 3-minute clock comes from a guide; the wiki pages read did not state round or intermission seconds.

Two rules that change the round. If the sheriff dies, any innocent who picks up the gun becomes Hero, and there can be as many Heroes as innocents. A sheriff who shoots an innocent dies with them ([wiki: Hero](https://murder-mystery-2.fandom.com/wiki/Hero), [Roles](https://murder-mystery-2.fandom.com/wiki/Roles)).

How the others differ:

- **Flee the Facility**: 30-second intermission in the Camp Lapis lobby; vote 1 of 4 maps, most votes wins, ties go to the leftmost option. One Beast, 2 to 4 survivors. Survivors get a 15-second head start while the Beast waits in a cave and picks a power (Runner, Stalker or Seer; default Runner). Survivors hack computers and escape; the round is capped at 15 minutes. A downed survivor ragdolls about 28 seconds and is dragged to a Freeze Pod ([wiki: Maps](https://flee-the-facility.fandom.com/wiki/Maps), [Survivors](https://flee-the-facility.fandom.com/wiki/Survivors), [Beast](https://flee-the-facility.fandom.com/wiki/Beast)).
- **Hide and Seek Extreme**: one random seeker and one random map each round. Hiders spawn together; the seeker is frozen at the same spawn, watching, for "a short period". Then the seeker must touch every hider before the timer ends. Hiders who last win. Seconds: not known ([wiki: Gameplay](https://hide-and-seek-extreme.fandom.com/wiki/Gameplay)).
- **Ink Game Hide and Seek**: teams split 50/50, the odd player goes to hiders, 4-minute limit, and a seeker who kills nobody is eliminated ([wiki](https://ink-game.fandom.com/wiki/Hide_and_Seek)).
- **Impostor and werewolf games**: discussion seconds, vote seconds and role odds: not known. No source we found describes them.

### The loop stack

| Every | What closes | Example |
|---|---|---|
| 10 seconds | The murderer's knife arrives | Murder Mystery 2 |
| 15 seconds | The head start ends | Flee the Facility |
| 20 to 64 seconds | A computer is hacked | Flee the Facility |
| 3 minutes | A round | Murder Mystery 2 |
| 15 minutes at most | A round | Flee the Facility |
| 25 full rounds | A 1,000-coin box (our arithmetic: 1,000 / 40) | Murder Mystery 2 |
| Each level to 100, then prestige | A level, then a reset to 1 with a cosmetic rank | Murder Mystery 2 |
| About a month, three or four times a year | A seasonal event with its own map, box and battle pass | Murder Mystery 2 Halloween 2026, 18 Oct to 16 Nov |

## The first five minutes

No source we found gives seconds from joining to the first round for any game in this genre. The gates below are reasoning from the clocks above.

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | The player is in a lobby with the vote room or map choices in view | Murder Mystery 2 and Flee the Facility both start with a lobby vote |
| 0:30 | The player has voted, or a round is already counting down | Flee the Facility's whole intermission is 30 seconds |
| 1:00 | The player has a role and knows what it means in one line | **Our read:** role cards are the whole tutorial in this genre; Murder Mystery 2 shows role and percentage on one card |
| 3:00 | The player has finished one full round | Murder Mystery 2's 3-minute clock |
| 5:00 | The player has seen their murderer chance rise, or earned their first coins | Murder Mystery 2's coin cap is 40 per round |

## Numbers that work

### Murder Mystery 2 rewards per round

| Role | Coins | XP |
|---|---|---|
| Innocent | Up to 40 (50 with Elite) | 5 per second survived (900 for 3 minutes), +900 for a full coin bag, +600 for a Hero |
| Sheriff | not known | 900 on a win plus 320 per innocent saved; only 100 if the sheriff dies |
| Murderer | not known | 700 per kill |
| Multiplier | | x1.5 for Elite, x1.5 for winning |

Sources: [wiki: Coins](https://murder-mystery-2.fandom.com/wiki/Coins), [XP](https://murder-mystery-2.fandom.com/wiki/XP). The coin cap was 5, then 10 to 15, before Season 1 in May 2019.

Our arithmetic: an innocent who survives the full round with a full bag earns 900 + 900 = 1,800 XP, or 2,700 with the win multiplier. A murderer who kills 11 players in a full server earns 7,700 XP.

### Murder Mystery 2 boxes and the godly grind

| Item | Cost | Odds |
|---|---|---|
| Weapon box | 1,000 coins, or 100 Diamonds, or 1 Mystery Key | Godly about 0.2% (1 in 500) |
| Common Egg (pets) | 1,000 coins | not known |
| Event box, Halloween 2026 | 600 candies | 12 weapons; odds not known |

Sources: [wiki: Boxes](https://murder-mystery-2.fandom.com/wiki/Boxes), [Godly Weapons](https://murder-mystery-2.fandom.com/wiki/Godly_Weapons), [Season 1](https://murder-mystery-2.fandom.com/wiki/Season_1), [Halloween Event 2026](https://murder-mystery-2.fandom.com/wiki/Halloween_Event_2026).

Our arithmetic:

| Step | Value |
|---|---|
| Full-bag rounds per box | 1,000 / 40 = 25 (20 with Elite) |
| Boxes expected per godly | 500 |
| Coins expected per godly | 500,000 |
| Full-bag rounds expected per godly | 12,500 |
| Round time alone at 3 minutes | 37,500 minutes, 625 hours |
| Chance of at least one godly in 100 boxes | 1 − 0.998^100, about 18% |
| Chance of at least one godly in 500 boxes | about 63% |

**Our read:** no player grinds 625 hours for one specific box's godly. The gap is the business: it is filled by Diamonds (bought with Robux; 100 Diamonds per box, so 1 Diamond = 10 coins) and by trading with players who got lucky.

### Flee the Facility clocks and rewards

| Hackers on one computer | Hack time | Skill checks | Person-seconds (our arithmetic) |
|---|---|---|---|
| 1 | 64 s | 6 | 64 |
| 2 | 32 s | 3 | 64 |
| 3 | 20 s | 2 | 60 |

A failed skill check "blows up" the computer and plays an error sound and icon for everyone, including the Beast ([wiki: Computers](https://flee-the-facility.fandom.com/wiki/Computers)). The wiki disagrees with itself on computer count: one page says one per player plus one, another "survivor count + 1".

**Our read:** grouping on one computer saves almost no total effort (64 against 60 person-seconds) but cuts the wait from 64 to 20 seconds, and puts three survivors in one place for the Beast. That trade is the decision.

| Action | Credits | XP |
|---|---|---|
| Hack a computer | 6 | 50 |
| Rescue from a Freeze Pod (once per round) | 20 | 100 |
| Escape | 25 | 300 |
| Beast: each freeze | 25 | not known |
| Beast: freeze all four | 100 in all | 800 |

Sources: [wiki: Credits](https://flee-the-facility.fandom.com/wiki/Credits), [Beast](https://flee-the-facility.fandom.com/wiki/Beast). Levels cost 400 more XP per level up to level 10, then 4,000 per level; the Trading Post opens at level 6 and Pro servers at level 200 ([wiki: Levels](https://flee-the-facility.fandom.com/wiki/Levels), [Trading Post](https://flee-the-facility.fandom.com/wiki/Trading_Post)).

Our arithmetic: a survivor who hacks two computers and escapes earns 12 + 25 = 37 credits. A 700-credit item is about 19 such rounds.

### Who is playing what, 25 Nov 2026

| Game | Created | Players now | Server size |
|---|---|---|---|
| Murder Mystery 2 | 2014 | 119,439 | 12 |
| Flee the Facility | 2017 | 12,080 | 5 |
| Murder Mystery Mad Murderer X | not stated | 2,526 | 12 |
| Hide and Seek Extreme | 2015 | 2,442 | 14 |
| Imposters and Roles (Among Us style) | not stated | 1,679 | 15 |
| Who's Lying | not stated | 199 | 21 |
| A Wolf Or Other | not stated | 132 | 12 |
| Breaking Point 2 | not stated | about 74 to 78 | 16 |

Source: [Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=66654135,372226183,93740418,2305929206,3187874989,5731967654,855385310,2499076778).

**Start with:**

| Value | Start with | Reasoning |
|---|---|---|
| Server size, hidden role | 12 | Murder Mystery 2: 1 murderer, 1 sheriff, 10 innocents |
| Server size, one hunter | 5 | Flee the Facility: 1 Beast, up to 4 survivors |
| Round clock | 3 minutes for hidden role; up to 15 for a chase with objectives | Murder Mystery 2; Flee the Facility |
| Grace period | 10 to 15 seconds before the hunter can act | Murder Mystery 2 knife at 10 s; Flee the Facility head start 15 s |
| Intermission | 30 seconds with a 3 or 4 map vote | Flee the Facility |
| Coin cap per round | 40 | Murder Mystery 2 |
| Box price | 25 full rounds of the cap | Murder Mystery 2: 1,000 coins at 40 a round |
| Top rarity in a box | 0.2% for a tradable cosmetic | Murder Mystery 2. **Our read:** only with a trade market; without one, 500 boxes is a wall |
| Premium currency rate | 1 premium = 10 soft | Murder Mystery 2's box at 1,000 coins or 100 Diamonds |
| Scarce-role picking | Shown percentage that rises each round missed | Murder Mystery 2 |

## What brings them back

**Later in the same session.** The rising murderer percentage: our arithmetic, if every player in a 12-player server had an equal share, is one murderer round in 12, about 36 minutes of 3-minute rounds. Murder Mystery 2's real odds are not published. In Flee the Facility, a Beast is chosen each round.

**Tomorrow.** Daily rewards: not known for both leaders. The trade market runs every day: Murder Mystery 2 has trading servers, and Flee the Facility a Trading Post with "Quick Join" ([wiki: Trading Post](https://flee-the-facility.fandom.com/wiki/Trading_Post)).

**Next week and after.** Murder Mystery 2's levels run to 100, then prestige resets to level 1, up to Prestige X. Prestige is cosmetic and ranks the player above higher-level players who have not prestiged ([wiki: Prestige](https://murder-mystery-2.fandom.com/wiki/Prestige)). Seasonal events (Summer, Halloween, Christmas) each bring a map, a box and a battle pass. Event boxes are never re-opened after the event, so their items only exist in trades ([wiki: Boxes](https://murder-mystery-2.fandom.com/wiki/Boxes)).

## Other players

- **Server size.** 12 gives Murder Mystery 2 one murderer, one sheriff and 10 suspects. 5 gives Flee the Facility one Beast against a team small enough to talk.
- **What a player sees of others.** Weapons and pets. In Disguises mode Murder Mystery 2 removes names (players get NATO-alphabet names) and makes avatars identical, with no radios or pets ([wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2)).
- **Trading.** Murder Mystery 2: 4 unique items per trade, a 6-second wait after each change before accepting, level 10 and up since 28 Dec 2021 after item duplication. Players price items on value-list websites ([wiki: Trading](https://murder-mystery-2.fandom.com/wiki/Trading)).
- **Anti-grief rules.** Shooting an innocent kills the sheriff too. Flee the Facility's Freeze Pod drains only while the Beast is beyond a set distance, so camping next to it does nothing, and a rescue pays 20 credits ([wiki: Beast](https://flee-the-facility.fandom.com/wiki/Beast)).
- **The clipped moment.** **Our read:** the sheriff's last-second shot, an innocent becoming Hero, the Beast arriving as the exit opens.

### Chat rules

Hidden information breaks if dead players can talk to living ones.

- Flee the Facility, since 31 Jan 2025: the general channel works only between rounds. Survivors have a private channel. Players in a round cannot see messages from anyone outside it, and escaped or frozen players cannot message the group still playing ([wiki: Chat System](https://flee-the-facility.fandom.com/wiki/Chat_System)). The wiki ties the change to Roblox's chat system migration.
- Murder Mystery 2's chat rules: not found in our research.
- Evidence on whether chat limits raise or lower retention: not found.

**Our read:** split chat by state, not by role. Living players in the round talk to each other; the lobby and the dead talk to each other; the two never mix until the round ends. That one rule removes the cheapest way to ruin a round, a dead player typing the murderer's name.

## Money

| Game | Item | Type | R$ | What it does |
|---|---|---|---|---|
| Murder Mystery 2 | Elite | Pass | 499 | Elite knife, pet, radio, effect, 1.5x XP, red name tag, 50-coin cap |
| Murder Mystery 2 | Radio | Pass | 475 | Plays audio |
| Murder Mystery 2 | Batwing, Icewing | Pass | 2,499 | Cosmetic (off sale) |
| Murder Mystery 2 | Diamonds, 100 to 13,000 | Product | not known | Boxes, powers |
| Flee the Facility | VIP | Pass | 420 | 15% more XP and credits, double-weight map vote, badge, ban hammer |
| Flee the Facility | Credits, 50 to 4,000 | Product | 25 to 1,700 | 2 to 2.35 credits per R$ (our arithmetic) |

Sources: [MM2 wiki: Gamepasses](https://murder-mystery-2.fandom.com/wiki/Gamepasses), [Elite](https://murder-mystery-2.fandom.com/wiki/Elite_Gamepass), [Diamonds](https://murder-mystery-2.fandom.com/wiki/Diamonds), [FTF wiki: VIP](https://flee-the-facility.fandom.com/wiki/VIP), [Credits](https://flee-the-facility.fandom.com/wiki/Credits). Murder Mystery 2 has released 36 passes; 3 are on sale.

**Where offers appear.** The vote: Flee the Facility VIP doubles the owner's map vote. Murder Mystery 2's powers (Sprint, Trap, Ghost, X-Ray and others) cost 1,000 to 6,000 coins or 100 to 800 Diamonds ([wiki: Shop](https://murder-mystery-2.fandom.com/wiki/Shop)).

**What backfires, and policy.** Flee the Facility removed its crate spin animation on 21 Oct 2023 "for compliance" and now sells crate items directly at 100, 200, 400 or 700 credits by rarity ([wiki: Crates](https://flee-the-facility.fandom.com/wiki/Crates)). Murder Mystery 2's boxes can be opened with Diamonds, which are bought with Robux, so they are paid random items and need published odds. Selling a higher chance of the scarce role would turn the pity percentage into an advert; no source shows either leader doing it. See [foundations/15-the-line.md](../foundations/15-the-line.md) and [foundations/07-rarity-and-collection.md](../foundations/07-rarity-and-collection.md).

## Live ops

- **Murder Mystery 2**: updated 23 Nov 2026. Seasonal events with map, box and battle pass; Halloween 2026 ran 18 Oct to 16 Nov (29 days), and coins did not drop during it ([wiki](https://murder-mystery-2.fandom.com/wiki/Halloween_Event_2026)). The wiki claims the game first passed 1,000,000 concurrent players on the release day of the Summer Event 2026; the wiki gives no source and it was not checked.
- **Flee the Facility**: updated 11 Nov 2026. 15 maps plus 2 event maps ([wiki: Maps](https://flee-the-facility.fandom.com/wiki/Maps)).
- **Hide and Seek Extreme**: last updated 28 Aug 2026, three months before this snapshot.

Update day of week: not known for any of them.

**Our read:** a small team can hold a cosmetic economy with three dated events a year, each adding one box that never returns. Murder Mystery 2 has 12 active standard maps, so new maps are rarer than new boxes.

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Concurrent players stay in the hundreds | A round copy with no item economy | Who's Lying 199, A Wolf Or Other 132, Breaking Point 2 about 74 to 78 (last updated 2 Aug 2026). **Our read:** add something to own and trade before adding roles |
| Item values crash; trade volume spikes | Duplication exploit | Murder Mystery 2 restricted trading to level 10 and up on 28 Dec 2021 after duping |
| A player says the murderer's name in chat after dying | Dead and living players share a channel | Flee the Facility's chat partition (31 Jan 2025) |
| Same players get the scarce role; others leave | Pure random role picks | A visible chance that rises each round missed (Murder Mystery 2) |
| Hunter camps a captured player | No rule against it | Freeze Pod drains only when the Beast is away (Flee the Facility) |
| Paid crates flagged | Spin animation on a paid random item | Flee the Facility's 2023 switch to direct sale by rarity |

## Checklist

1. A role card appears within 60 seconds of joining.
2. The hunter cannot act for the first 10 to 15 seconds of a round.
3. The round has a hard clock: about 3 minutes for hidden role, at most 15 for a chase with objectives.
4. Intermission is 30 seconds or less and holds a 3 or 4 map vote.
5. Each player sees their chance of the scarce role, and it rises every round they miss it.
6. Dead players cannot message living players in the round.
7. Killing a teammate costs the killer (Murder Mystery 2: the sheriff dies too).
8. A captured player can be rescued, and standing next to a captive does not help the hunter.
9. Soft currency per round has a cap (Murder Mystery 2: 40).
10. A box costs about 25 capped rounds.
11. Any box opened with Robux-bought currency shows exact odds.
12. Trading has a level gate and a confirm delay (Murder Mystery 2: level 10, 6 seconds).
13. At least one dated seasonal event a year adds items that never return.
14. Role chance is never sold.

## Twists and open space

Variations that already produced hits:

- **One hunter, objectives for the hunted.** Flee the Facility's computers turn hiding into a task with a 64-second clock.
- **Separate places per mode.** Murder Mystery 2 runs Standard, Disguises and Assassin (everyone has a knife and a target) as separate places sharing player data ([wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2)).
- **Forced action.** Ink Game eliminates a seeker who kills nobody in 4 minutes.

**Our read** on open space:

- An impostor game with an item economy. The clones in our research have the voting but nothing to own, and they top out at 1,679 players.
- A Disguises-style mode as the main mode, with cosmetics shown only in the lobby, so that a godly knife in the lobby does not tell anyone who is holding a knife in the round.
- A shown pity percentage for the hunter role in one-hunter games, which neither Flee the Facility nor Hide and Seek Extreme is documented as using.

## Sources

- Teardown: [Murder Mystery 2](../teardowns/murder-mystery-2.md)
- [Murder Mystery 2 wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2): [Roles](https://murder-mystery-2.fandom.com/wiki/Roles), [Coins](https://murder-mystery-2.fandom.com/wiki/Coins), [XP](https://murder-mystery-2.fandom.com/wiki/XP), [Boxes](https://murder-mystery-2.fandom.com/wiki/Boxes), [Trading](https://murder-mystery-2.fandom.com/wiki/Trading), [Prestige](https://murder-mystery-2.fandom.com/wiki/Prestige)
- [Flee the Facility wiki](https://flee-the-facility.fandom.com/wiki/Maps): [Computers](https://flee-the-facility.fandom.com/wiki/Computers), [Credits](https://flee-the-facility.fandom.com/wiki/Credits), [Chat System](https://flee-the-facility.fandom.com/wiki/Chat_System), [VIP](https://flee-the-facility.fandom.com/wiki/VIP), [Crates](https://flee-the-facility.fandom.com/wiki/Crates)
- [Hide and Seek Extreme wiki: Gameplay](https://hide-and-seek-extreme.fandom.com/wiki/Gameplay)
- [rblxguide: MM2 roles guide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide)
- [Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=66654135,372226183,93740418,2305929206,3187874989,5731967654,855385310,2499076778)
