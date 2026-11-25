# Murder Mystery 2

> One murderer, one sheriff and up to ten innocents play a 3-minute round of hide, hunt and guess; a trading economy of cosmetic knives and guns has kept a 2014 game above 100,000 concurrent players in 2026.

| | |
|---|---|
| Studio | Nikilis |
| Released | Murder Mystery created 18 Jan 2014; Murder Mystery 2 released 25 Dec 2014 ([wiki: Timeline](https://murder-mystery-2.fandom.com/wiki/Timeline)) |
| Genre | [Social deduction](../genres/social-deduction.md) |
| Peak concurrent players | The wiki claims 1,000,000 on the release day of the Summer Event 2026, with no source; not checked ([wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2)) |
| Players now | 119,439, with 32.4B visits and 24.9M favourites (Roblox public API, 25 Nov 2026, [link](https://games.roblox.com/v1/games?universeIds=66654135)) |
| Players per server | 12 |
| Teardown date | 25 Nov 2026 |
| How it was studied | Wiki, public API and published sources. Not timed on a device. |

## 1. Core loop

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| Vote | Walks into the voting room, picks 1 of 3 random maps | not known | Three maps; no votes means a random pick | Votes |
| Role | Reads the role card | not known | Role, and their percentage chance of Murderer | Chance rises if not picked |
| Grace | Innocents scatter | 0 to 10 | The murderer has no knife yet | Coins |
| Hunt | Murderer kills, sheriff shoots, innocents hide and collect coins | 10 to 180 | Bodies, shots, a dropped gun | Up to 40 coins; 5 XP per second survived |
| End | Timeout, murderer dead, or everyone dead | at most 180 | Result screen | XP |

Sources: [wiki main page](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2), [Maps](https://murder-mystery-2.fandom.com/wiki/Maps), [rblxguide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide). The 3-minute clock is from a guide; intermission length is not known.

Roles: 1 Murderer, 1 Sheriff, Innocents = players minus 2, capped at 10. With 2 players there are no innocents ([wiki: Innocent](https://murder-mystery-2.fandom.com/wiki/Innocent)). If the sheriff dies, an innocent who picks up the gun becomes Hero; there can be as many Heroes as innocents. A sheriff who shoots an innocent dies too ([wiki: Hero](https://murder-mystery-2.fandom.com/wiki/Hero)).

Dead time: a dead innocent waits for the round to end, up to about 170 seconds. **Our read:** that wait is cheap because it is capped at 3 minutes and the next round brings a new role roll.

## 2. First session

| Time | What happens |
|---|---|
| 0:00 to 0:10 | not known (the wiki mentions a loading screen, then the vote) |
| 0:10 to 1:00 | not known |
| 1:00 to 5:00 | not known; **our read:** one round, probably as an innocent |
| 5:00 to 15:00 | not known |

First reward: coins inside the first round. First purchase: a box at 1,000 coins, 25 full-bag rounds (our arithmetic). First rare moment: being picked Murderer or Sheriff. First contact with another player: the vote room. First long goal shown: the role percentage. How anything is taught: not known.

## 3. Progression

**Coins.** Up to 40 per round as an innocent, 50 with the Elite pass. The cap was 5, then 10 to 15, before Season 1 ([wiki: Coins](https://murder-mystery-2.fandom.com/wiki/Coins)).

**XP** ([wiki: XP](https://murder-mystery-2.fandom.com/wiki/XP)):

| Role | XP |
|---|---|
| Innocent | 5 per second survived, +900 for a full coin bag, +600 as Hero |
| Sheriff | 900 on a win plus 320 per innocent saved; 100 if the sheriff dies |
| Murderer | 700 per kill |
| Multiplier | x1.5 for Elite, x1.5 for winning |

**Levels and prestige.** Level cap 100, then prestige resets to level 1, up to Prestige X. Prestige is cosmetic and ranks the player above higher-level players who have not prestiged. Phones cannot prestige without tablet mode. 14,572,419 players had reached the level-100 badge by 26 Jul 2026 ([wiki: Prestige](https://murder-mystery-2.fandom.com/wiki/Prestige)).

**Boxes.** 1,000 coins, 100 Diamonds or 1 Mystery Key each. 11 boxes can be opened now (6 knife, 3 gun, 2 mystery). Rarities: Common, Uncommon, Rare, Legendary, Godly, Chroma. Godly odds about 0.2%, 1 in 500. 124 godly weapons exist, 85 knives and 39 guns ([wiki: Boxes](https://murder-mystery-2.fandom.com/wiki/Boxes), [Godly Weapons](https://murder-mystery-2.fandom.com/wiki/Godly_Weapons)).

Our arithmetic on the godly grind:

| Step | Value |
|---|---|
| Full-bag rounds per box | 25 |
| Boxes expected per godly from one box | 500 |
| Coins | 500,000 |
| Rounds | 12,500 |
| Round time at 3 minutes | 625 hours |
| Chance of a godly in 100 boxes | about 18% |

**Crafting** ([wiki: Crafting](https://murder-mystery-2.fandom.com/wiki/Crafting)):

| Input | Output |
|---|---|
| 12 Common Shards | Random Uncommon |
| 12 Uncommon Shards | Random Rare |
| 12 Rare Shards | Random Legendary |
| 20 Legendary Shards | Seer (a godly) |
| 10 Godly Shards + 10 Godly Metal | Random painted Seer or Chroma Seer |

How shards are earned: not known.

**Powers** ([wiki: Shop](https://murder-mystery-2.fandom.com/wiki/Shop), [rblxguide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide)): Footsteps free; Sleight and Ninja 1,000 coins or 100 Diamonds; Sprint, Fake Gun, Haste, Trap, Decoy 3,000 or 400; Ghost and X-Ray 6,000 or 800. Sprint gives +50% speed for 5 seconds with a 27-second cooldown.

## 4. Session and return hooks

- **Role chance.** Each player's Murderer chance is shown every round, starts low, and rises each round they are not Murderer. A repeat Murderer is rare. Sheriff odds depend on server size. Exact numbers are not published ([wiki: Murderer](https://murder-mystery-2.fandom.com/wiki/Murderer)).
- **Seasonal events.** Halloween 2026 ran 18 Oct to 16 Nov: a new map, a 30-tier battle pass (tier 1 free, tiers 2 to 29 at 600 candies each, tier 30 at 100,000 candies, 117,400 in all per the wiki; our sum of those parts is 116,800), an event box at 600 candies with 12 weapons, a Halloween Key every second tier, and no coin drops during the event ([wiki](https://murder-mystery-2.fandom.com/wiki/Halloween_Event_2026)). Our arithmetic: 117,400 candies over 29 days is about 4,050 a day.
- **Event boxes never return.** 18 event boxes up to the wiki's count; their items exist after the event only through trades ([wiki: Boxes](https://murder-mystery-2.fandom.com/wiki/Boxes)).
- **Codes** from the developer's social posts and a YouTuber; none work now ([wiki: Codes](https://murder-mystery-2.fandom.com/wiki/Codes)).
- Daily rewards and update day: not known.

## 5. Other players

- **Trading**: 4 unique items per trade; 6-second wait after any change before accepting; effects, emotes and radios cannot be traded; requests can be turned off; level 10 and up since 28 Dec 2021 after duplication. Value-list websites price items, one in "seers" and one in raw units ([wiki: Trading](https://murder-mystery-2.fandom.com/wiki/Trading)).
- **Modes**: Standard; Disguises (NATO-alphabet names and identical avatars, no radios or pets); Assassin (everyone has a knife and a target, no powers). Each is a separate place sharing player data ([wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2)).
- **Flex**: the weapon in hand, pet, and prestige rank.
- **Clipped moment**: **Our read:** the sheriff's last shot and the innocent who becomes Hero.

## 6. Money

| Item | Type | R$ | What it does |
|---|---|---|---|
| Elite | Pass | 499 | Elite knife, pet, radio and effect; 1.5x XP; red name tag; 50-coin cap |
| Radio | Pass | 475 | Plays audio |
| BUNDLE: Mortal | Pass | 3,399 | Bundle [data, Nov 2026] |
| Item packs | Pass, off sale | 899 to 1,299 | Cosmetics |
| Batwing, Icewing | Pass, off sale | 2,499 | Cosmetics |
| Diamonds: 100, 400, 800, 2,000, 5,500, 13,000 | Product | 100, 400, 800, 1,700, 4,500, 10,000 [data, Nov 2026] | Boxes (100 each), powers |

Sources: [wiki: Gamepasses](https://murder-mystery-2.fandom.com/wiki/Gamepasses) (36 released, 3 on sale), [Elite](https://murder-mystery-2.fandom.com/wiki/Elite_Gamepass), [Diamonds](https://murder-mystery-2.fandom.com/wiki/Diamonds). One Diamond buys what 10 coins buy. The snapshot lists 73 passes: the 3 on sale are Elite, Radio and BUNDLE: Mortal, and 70 are off sale [data, Nov 2026]. Best sellers: not known.

**Developer products [data, Nov 2026].** 156 are listed on sale; without 11 with blank or dash-only names, 145 remain, 25 to 22,500 R$, median 1,699 R$. The endpoint marks old event packs (Halloween keys, Beach Balls) as on sale too, so which ones the shop shows now is not known. 87 are currency or key packs, mostly on one price ladder of 100, 400, 800, 1,700, 4,500, 10,000 and 22,500 R$, and 38 are single Godly weapons at 1,699 R$ each. 12 of 145:

| Product | R$ | Kind |
|---|---|---|
| Gems x100 | 100 | Diamond ladder (the wiki's six amounts), smallest |
| Gems x13,000 | 10,000 | Largest |
| +50 Coins | 25 | Coin ladder, smallest |
| +3500 Coins | 1,450 | Largest |
| Key x1 | 100 | Box keys, smallest |
| Key x360 | 22,500 | Largest |
| Candies x800 | 100 | Event currency, smallest |
| Candies x270,000 | 22,500 | Largest |
| GODLY: Darksword | 1,699 | One Godly weapon |
| BUNDLE: Snowstorm | 3,399 | Bundle |
| Legendary Pack: Latte | 399 | Cosmetic pack |
| Bundle Offer 1 | 400 | Offer (5 tiers, 400 to 10,000) |

Our arithmetic: Diamonds give 1.0 per R$ in the smallest pack and 1.3 in the largest; coins 2.0 and 2.4; a key costs 100 R$ singly and 62.5 R$ in the 360 pack; candies 8 and 12 per R$. A bundle costs 3,399 R$, 1 R$ more than two single Godlies (2 x 1,699), so bundles carry no discount.

## 7. Why it works

Developer statements: not found. Measured: 119,439 players now, 32.4B visits, and 10,967,237 up votes against 1,113,197 down, about 91% ([omni-search](https://apis.roblox.com/search-api/omni-search?searchQuery=Breaking+Point&sessionId=abc&pageType=all)).

**Our read:**

- The round is 3 minutes and needs no skill to start; the economy behind it takes hundreds of hours.
- 0.2% godlies from boxes that cost 25 rounds make every godly scarce, and trading lets a lucky player's box pay off for others. The value-list sites mean a knife has a price everyone knows.
- Event boxes that never return add old items the market can never refill, so the catalogue's value keeps growing with each event.
- The visible, rising Murderer chance turns a run of innocent rounds into waiting for a turn.

## 8. What went wrong

- Item duplication forced a level-10 gate on trading in Dec 2021.
- Phones cannot prestige without switching to tablet mode.
- Event-only coin pauses (no coins during Halloween 2026) stop the normal box path for a month.
- Decline: none in our research; the game is at 119K in Nov 2026.

## 9. What to take from it

1. A 3-minute round with a 10-second grace period before the hunter can act.
2. Soft currency capped at 40 per round; a box at 25 capped rounds.
3. A top rarity of 0.2%, only together with player trading (4 items, 6-second confirm, level-10 gate).
4. A shown chance of the scarce role that rises every round missed.
5. Seasonal boxes, about a month each, that never reopen.
6. Premium currency at 10 soft per 1 premium, the same items buyable both ways.
7. One price ladder (100 to 22,500 R$, 7 steps) reused for every currency and key pack, and the top rarity also sold outright at 1,699 R$ a weapon [data, Nov 2026].

## Sources

- [Murder Mystery 2 wiki](https://murder-mystery-2.fandom.com/wiki/Murder_Mystery_2) and the pages linked above
- [rblxguide: MM2 roles guide](https://rblxguide.com/games/murder-mystery-2/updates/mm2-roles-guide)
- [Roblox public API, 25 Nov 2026](https://games.roblox.com/v1/games?universeIds=66654135)
