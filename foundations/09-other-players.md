# Other players

This page covers server size, what players see of each other, what they can do to each other, trading, friends, and talking now that chat needs an age check. Open it when you set your server size, before you build stealing, trading or co-op, and when your game feels empty with players in it. Neighbours and theft in slop games are in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md) (mechanisms 4 and 5) and are not repeated here.

## What is known

### Players per server, by genre

Sizes are the maximum players per server (Roblox public API, 25 Nov 2026).

| Band | Genre | Games and their server size | Why this band (**Our read**) |
|---|---|---|---|
| 1 | Physics toys | Hyper Realistic Ragdoll 1 ([games API](https://games.roblox.com/v1/games?universeIds=10773618503)) | Nobody else ruins the clip. |
| 4 to 8 | Collect, steal and grow | [Grow a Garden](../teardowns/grow-a-garden.md) 4; [Throw Food For Animals](../teardowns/throw-food-for-animals.md), Plants vs Brainrots 5; [Steal An Egg](../teardowns/steal-an-egg.md) 7; [Steal a Brainrot](../teardowns/steal-a-brainrot.md), Escape Tsunami 8 ([games API](https://games.roblox.com/v1/games?universeIds=10563114921)) | Every neighbour becomes a known person within one session. |
| 5 to 10 | Small co-op, asymmetric horror, tycoons | Flee the Facility 5, Piggy 6, [Forsaken](../teardowns/forsaken.md) 9 ([games API](https://games.roblox.com/v1/games?universeIds=6331902150)); Theme Park Tycoon 2 6; [Bee Swarm Simulator](../teardowns/bee-swarm-simulator.md) 6; [Build a Boat for Treasure](../teardowns/build-a-boat-for-treasure.md) 7; [Pet Simulator 99](../teardowns/pet-simulator-99.md) 10 | Each player has a role or plot the others depend on or can visit in a minute. |
| 10 to 13 | Duel sports, dress-up, round games | Blue Lock: Rivals 10, Volleyball Legends 12 (6v6); [Dress to Impress](../teardowns/dress-to-impress.md) 13; [Murder Mystery 2](../teardowns/murder-mystery-2.md) 12; [Epic Minigames](../teardowns/epic-minigames.md) 12 | Two teams of 5 or 6, or an audience small enough that every outfit walks the runway. |
| 12 to 20 | Fighting hubs, RPGs, fishing, RNG, towers | [Blox Fruits](../teardowns/blox-fruits.md) 12, [The Strongest Battlegrounds](../teardowns/the-strongest-battlegrounds.md) 15, Blade Ball 16; [Fisch](../teardowns/fisch.md), [Sol's RNG](../teardowns/sols-rng.md), [Tower of Hell](../teardowns/tower-of-hell.md) 20 ([games API](https://games.roblox.com/v1/games?universeIds=994732206,3808081382,3508322461)) | Enough strangers for a fight or an audience for a rare catch. |
| 22 to 30 | Races, survival co-op, tower defense lobbies, roleplay | +1 Speed Keyboard Escape 22; [99 Nights in the Forest](../teardowns/99-nights-in-the-forest.md) 25; Toilet Tower Defense 30; [Brookhaven](../teardowns/brookhaven.md), [Jailbreak](../teardowns/jailbreak.md) 30 | A shared spectacle or a town; most players never meet. |
| 35 to 50 | Big lobbies | [Adopt Me](../teardowns/adopt-me.md) 35, [Rivals](../teardowns/rivals.md) 40, [BedWars](../teardowns/bedwars.md) 40, [Doors](../teardowns/doors.md) 50, [Tower Defense Simulator](../teardowns/tower-defense-simulator.md) 50 | The server is a lobby. Play happens in smaller groups (Doors elevators of 1 to 4, BedWars teams). |
| 100 | Voice hangouts, whole-server events | MIC UP 100, Build the Pyramid! 100 ([games API](https://games.roblox.com/v1/games?universeIds=2626227051)), Ink Game 100-player lobbies | 100 is the voice-chat ceiling (below). |

- **New hits are small.** Almost all 2026 leaders use 5 to 8 players. The large social games (Adopt Me 35, Brookhaven 30) are all older than 18 months ([games API](https://games.roblox.com/v1/games?universeIds=10563114921,3317771874,2440500124,994732206,2753915549,383310974,1686885941)).
- **The cap is not the crowd.** Doors averages 22.9 players in a 50-player server ([Rolimons](https://www.rolimons.com/game/6516141723)).
- **Failed steal clones went bigger.** Two dead brainrot clones used 10 players per server ([games API](https://games.roblox.com/v1/games)).

Roblox's docs give no advice on server size ([Players class](https://create.roblox.com/docs/en-us/reference/engine/classes/Players)). The one hard number: voice works only in places of 100 players or fewer, up from 50 on 24 Mar 2026 ([Voice chat docs](https://create.roblox.com/docs/en-us/chat/voice-chat), [DevForum](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031)).

Across the whole top 300 by players, the repo's snapshot ([data/ANALYSIS.md](../data/ANALYSIS.md), section 5) gives the spread by Roblox's own genre labels [data, Nov 2026]:

| Genre (top 300) | Games | Median server size | Most common sizes |
|---|---|---|---|
| Simulation | 108 | 8 | 6, 12, 5 |
| Survival | 41 | 20 | 20, 30, 25 |
| Roleplay & Avatar Sim | 31 | 25 | 50, 30, 25 |
| Action | 31 | 20 | 20, 30, 40 |
| Sports & Racing | 16 | 10 | 8 |
| Party & Casual | 15 | 24 | 12, 25 |
| Shooter | 13 | 14 | 8 |
| Strategy (mostly tower defense) | 9 | 30 | 30, 50 |
| All 300 | 300 | 15 (middle half 8 to 25) | 20, 6, 12 |

13 of the 300 run single-player servers, mostly ragdoll physics toys such as Hyper Realistic Ragdoll and Bloody Ragdoll Physics. 8 run more than 50; the largest is a Survival game at 200.

### What a player can see of other players

| What is visible | Example and number | Source |
|---|---|---|
| Bases and their size | Steal a Brainrot adds a second floor at rebirth 2 and a third at rebirth 10. Bee Swarm has 6 hives per server, 25 to 50 slots each. | [SaB wiki: Base](https://stealabrainrot.fandom.com/wiki/Base), [Bee Swarm wiki: Hive](https://bee-swarm-simulator.fandom.com/wiki/Hive) |
| Rare hatches, held by few | Steal An Egg "Hatched Secret!" badge: 0.03% of players; "Hatched Eternal!": 0.01% | [Bloxodes SAE](https://bloxodes.com/wiki/steal-an-egg) |
| Kill counts | TSB kill badges at 1, 10, 100, 1,000 and up. Of 171.4M players with a first kill, 53.9% reach 10, 18.9% reach 100, 5.8% reach 1,000, 0.64% reach 10,000. | [TSB badges API](https://badges.roblox.com/v1/universes/3808081382/badges?limit=100) |
| Ranks and server gates | Dress to Impress: 14 star ranks; Pro servers need 3,000+ stars, Master 10,000+ | [DTI wiki: Ranks](https://dti-dress-to-impress.fandom.com/wiki/Stars) |

Our arithmetic on the TSB ladder: each x10 step keeps 54%, then 35%, then 31%, then 11% of the players who reached the step before. So each badge is 2 to 3 times rarer than the one below until 1,000 kills, then 9 times rarer. **Our read:** a badge held by 1 in 17 is rare enough to mean something and common enough that a server of 15 sees one now and then.

### What players do to and with each other

| Action | Real rules and prices found |
|---|---|
| Steal | Steal a Brainrot: 60 s lock, +10 s per rebirth, 30 s protection after joining, carrier slowed and visible. Grow a Garden sells a steal at 37 R$ per crop; it can fail and the server sees a banner naming both players ([GaG wiki: Stealing](https://growagarden.fandom.com/wiki/Stealing)). Full rules: [slop/02](../slop/02-why-it-holds.md), mechanism 5. |
| Trade | See the trading section below. |
| Gift | Garden Tower Defense lets passes (Auto Roll, x2) be gifted through trade ([GTD wiki](https://garden-tower-defense.fandom.com/wiki/Trading_Plaza)). Toilet Tower Defense made units, coins, gems and boosts giftable on 11 Nov 2026 ([TTD wiki](https://toilet-tower-defense.fandom.com/wiki/Clone_Crate_Update)). Anime Defenders made most items untradable except gifts ([wiki](https://anime-defenders.fandom.com/wiki/Updates)). |
| Vote | Dress to Impress: 360 s to dress, then every other player rates each outfit 1 to 5 stars, top three on a podium ([DTI wiki](https://dti-dress-to-impress.fandom.com/wiki/Dress_to_Impress/Game_Mode)). Epic Minigames sells "choose the next minigame" for 9 R$ ([wiki](https://typical-games.fandom.com/wiki/Epic_Minigames)). |
| Revive | Doors: 40 R$ for one; packs of 5, 10, 25 for 145, 239, 479 R$; window 5 min solo, 2 min in a group ([Doors wiki](https://doors-game.fandom.com/wiki/Revives)). 99 Nights: 55 R$ for one, 230 R$ for the team [data, Nov 2026]. Dead Rails Doctor class: 3 free revives per run ([wiki](https://deadrails.fandom.com/wiki/Classes)). |
| Co-operate | Forsaken: 2 to 3 survivors per generator, 5 generators per map ([wiki](https://forsaken2024.fandom.com/wiki/Objectives)). Jailbreak's Museum needs 2 players to start ([wiki](https://jailbreak.fandom.com/wiki/Mansion)). |
| Compete | TSB: one free-for-all of 15. Combat Warriors team modes forbid team kills but allow carrying teammates ([wiki](https://combat-warriors.fandom.com/wiki/Gamemodes)). |

Our arithmetic on Doors revives: 40, 29, 23.9 and 19.2 R$ each for 1, 5, 10 and 25, so bulk halves the price. **Our read:** the 2-minute group window is about how long friends will wait.

### Party size, difficulty and friend bonuses

| Game | Rule | Source |
|---|---|---|
| Tower Defense Simulator, Hardcore | Starting cash per player: solo $900, duo $750, trio $600. Kill cash is split 50% each in a duo, 33% in a trio, whoever did the damage. | [TDS wiki](https://tds.fandom.com/wiki/Hardcore_Mode) |
| Toilet Tower Defense | Coin bonus x1.2, x1.4, x1.5 for 1, 2, 3 friends | [TTD wiki](https://toilet-tower-defense.fandom.com/wiki/Difficulties) |
| Doors | Knobs +0.1x per friend, up to +0.3x | [Doors wiki: Knobs](https://doors-game.fandom.com/wiki/Knobs) |
| Pressure | Currency +5% per friend, up to +245% in a 50-player run | [Pressure wiki](https://pressure.fandom.com/wiki/Currency) |
| Grow a Garden | +10% sell value per friend in the server, up to +40% | [GaG wiki: Sheckles](https://growagarden.fandom.com/wiki/Sheckles) |
| 99 Nights in the Forest | Difficulty is fixed by party size at the start, even if players leave | [99nightsintheforest.wiki](https://99nightsintheforest.wiki/) |

Our arithmetic: a TDS duo starts with $1,500 between them, 1.67 times a solo $900; a trio $1,800, twice. The team gets more but each player less, so a duo must agree who builds what. Friend bonuses cluster at +5% to +20% per friend, capped at +30% to +50%. Grow a Garden caps at +40%, but a 4-player server holds only 3 others, so the real maximum is +30%.

A friend bonus can backfire. Adopt Me tested a friend-based currency; players spammed friend requests to farm it, and many moved to private servers to escape the spam ([Roblox newsroom, Aug 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform)).

### Trading

| Game | Who may trade, from when | Limits |
|---|---|---|
| MM2 | Level 10+ since 28 Dec 2021, added after duping | 4 different items per trade; 6 s wait after any change before accept; effects, emotes and radios cannot be traded ([MM2 wiki](https://murder-mystery-2.fandom.com/wiki/Trading)) |
| Adopt Me | Ultra-rare and legendary items need a free Trade License from a 3-question safe-or-scam test | Slots 4, then 9 (Nov 2020), then 18 (May 2023); 5 s countdown resets on any change; "unfair trade" warning adds 15 s; 30-day trade history ([Adopt Me wiki](https://adoptme.fandom.com/wiki/Trade_System)) |
| Royale High | Level 75+ | 40 items; 10 s cooldown on changes ([RH wiki](https://royale-high.fandom.com/wiki/Trading)) |
| Jailbreak | Only on Trading Island (or a 350 R$ pass to teleport) | 8 items per side; two confirms each; one-sided trades auto-declined ([Jailbreak wiki](https://jailbreak.fandom.com/wiki/Trading)) |
| Anime Vanguards | Level 50; only units no longer obtainable, skins, gifted passes | Traits and pity reset on traded units; a dupe means an automatic trade ban until review ([AV wiki](https://animevanguards.fandom.com/wiki/Trading)) |
| Fisch; Garden Tower Defense | Level 15 ([Fischipedia](https://fischipedia.org/wiki/Level)); 25 victories ([GTD wiki](https://garden-tower-defense.fandom.com/wiki/Trading_Plaza)) | GTD sells trading stalls from 25 to 649 R$ |

**Duplication.** Anime Vanguards delayed trading because "one mistake" could ruin the economy ([AV wiki](https://animevanguards.fandom.com/wiki/Stage_Notes)). Toilet Tower Defense has a community list of about 50 duped unit types by serial number, and on 11 Nov 2026 added a Clone Crate that takes duped units for a roll at 90% / 9% / 1% ([TTD wiki](https://toilet-tower-defense.fandom.com/wiki/Clone_Crate_Update)). The scale of the damage is not known.

**Real money and law.** Grow a Garden fruit and pets were sold for real money on eBay and Discord, which breaks Roblox's terms ([Wikipedia, citing Bloomberg](https://en.wikipedia.org/wiki/Grow_a_Garden)). Royale High blocks trading in South Korea and the Netherlands ([RH wiki](https://royale-high.fandom.com/wiki/Trading)). Check PolicyService `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed` before letting a player trade paid random items ([Paid random items docs](https://create.roblox.com/docs/production/monetization/paid-random-items)). The effect of trading on retention and spending is not known.

### Friends, matchmaking and private servers

- **Matchmaking weighs friends above everything.** Default weights: Friends 15, Latency 3, Text Chat 3, Occupancy 2, Play History 2, Language 2, Age 1, Voice Chat 1, Device 0. Friends alone (15) outweigh all others together (14) ([Matchmaking scoring](https://create.roblox.com/docs/en-us/matchmaking/scoring)). You can change the weights and add 2 custom signals ([Custom matchmaking](https://create.roblox.com/docs/en-us/matchmaking/customize-matchmaking)).
- **Which friend joins count for recommendations.** "Intentional co-play days per user" is the fifth signal in the Home ranking. It counts joins, invites and private servers ([Discovery docs](https://create.roblox.com/docs/en-us/production/promotion/discovery)); being placed together by matchmaking does not count, and reserved-server sessions were added in Dec 2025 ([DevForum staff post](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441)). Only players who first arrived from Recommended For You count for these signals. A newcomer brought in by a friend link does not ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)). **Our read:** the co-play signal rewards your existing players coming back together, not friends you recruit.
- **Private servers.** Free or a monthly Robux price; changing the price cancels every subscription ([Private servers docs](https://create.roblox.com/docs/en-us/production/monetization/private-servers)). Roblox Plus includes paid private servers, and since 24 Sep 2026 only one free one per game; the creator still earns up to 100 R$ per Plus subscriber per month ([DevForum](https://devforum.roblox.com/t/changes-to-roblox-plus-private-server-limits/4739922)).
- **Prices found.** Natural Disaster Survival 300 R$ a month ([wiki](https://roblox.fandom.com/wiki/Player:Stickmasterluke/Natural_Disaster_Survival)); Sol's RNG free. Private-server perk passes: TSB 499, Type Soul 799 R$ ([passes API](https://apis.roblox.com/game-passes/v1/universes/3808081382/game-passes?passView=Full&pageSize=100)). Jailbreak robberies there pay about a tenth.
- **Invites.** Call `CanSendGameInviteAsync` first; LaunchData holds up to 200 characters; no rate limit is stated ([Invite prompts](https://create.roblox.com/docs/en-us/production/promotion/invite-prompts)). Experience notifications: 13+ only, one per player per day, 99 characters ([Notifications docs](https://create.roblox.com/docs/en-us/production/promotion/experience-notifications)).

### Talking

- **Text chat needs an age check** worldwide since 7 Jan 2026. Age groups: under 9, 9-12, 13-15, 16-17, 18-20, 21+. A group chats with its own and neighbouring groups ([Roblox newsroom](https://about.roblox.com/newsroom/2026/01/roblox-age-checks-required-to-chat)).
- **Voice** is for age-verified users 13+, only in places of 100 or fewer, spatial by default ([Voice chat docs](https://create.roblox.com/docs/en-us/chat/voice-chat)); users voice-chat only with their own age group ([DevForum](https://devforum.roblox.com/t/voice-chat-is-now-supported-in-servers-of-up-to-100-users/4534031)).
- **What you may build instead.** Fixed preset phrases are allowed, and must go through Quick Words after May 2027. Player-typed text must go through TextChatService; editable text is allowed if filtered and limited to one submission per player per minute ([Chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines)).
- **What games did.** Adopt Me added backpack viewing and "suggest remove" in trades on 14 Jan 2026, after the age-group chat limits ([Adopt Me wiki](https://adoptme.fandom.com/wiki/Trade_System)). Dress to Impress added Safechat in Apr 2026. TSB puts an emote wheel on B.

**Our read:** many of your players cannot send a single chat line. Agreeing a trade, calling for help or saying "follow me" must also work through a button or an emote.

### The moment that gets filmed

| Genre | Moment | Evidence |
|---|---|---|
| Steal and defend | A unit carried out of someone's base; the owner chasing | Theft clips reached tens of millions of views ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)) |
| Grow and trade | Trading a rare crop or pet live | 24/7 trading streams gave Grow a Garden millions of watch hours ([Hatchet](https://hatchet.gg/blog/the-link-between-roblox-streamers-and-roblox-players/)) |
| Physics toys | A ragdoll fall | Four ragdoll games held 173,624 players on 18 Nov 2026 ([GGRecon](https://www.ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/)) |
| Fighting, horror, dress-up, RNG | A comeback kill, a jump scare, a podium finish, a server-wide rare roll | **Our read:** no clip numbers were found for these genres |

Moments clips carry a one-tap Join for age-checked 16+ players from 28 Jul 2026 ([Roblox newsroom](https://about.roblox.com/newsroom/2026/07/moments-new-homepage-unlocks-gaming-for-all)).

## The rules

1. **Pick the server size from the genre band above, then go to the low end.** **Start with:** 6 for steal, 4 or 5 for grow-and-show (as in [slop/02](../slop/02-why-it-holds.md)), 12 for a fighting hub or round game, 20 for fishing or RNG. Reason: the 2026 hits sit at 5 to 8 and the failed steal clones at 10.
2. **Never go above 100 if players talk.** Voice is off in places over 100.
3. **Every visible status item is 2 to 3 times rarer than the one below it, with one far step at the top.** The TSB kill ladder runs 1.9x, 2.8x, 3.2x, then 9x rarer per step. **Our read:** a badge everyone holds says nothing; a badge nobody holds is never seen.
4. **Every harmful action has a counter the victim can use within 5 seconds.** Steal a Brainrot's free bat and Steal An Egg's knock-down both do this. Full rules in [slop/02](../slop/02-why-it-holds.md).
5. **Friend bonuses: +10% per friend, capped at +30% to +50%, and only for friends who are already in the server.** Reason: the found bonuses sit at +5% to +20% per friend. Adopt Me's farmable friend currency drove players to private servers.
6. **Party scaling splits the reward, not just the difficulty.** **Start with:** each extra player in a group of up to 3 lowers each person's starting money by 17% to 20% and raises the team total (TDS: $900, $750, $600 per player, so $900, $1,500, $1,800 per team).
7. **Revives: offer one free route and one paid route.** The paid price found is 19 to 45 R$; across 355 charted games selling one, the median revive product is 45 R$ (19 in Simulation, 65 in Survival) [data, Nov 2026]. The window is 2 minutes in a group. Never show the paid revive prompt until the free route is used up, and never during a loss streak (see [15-the-line.md](15-the-line.md)).
8. **Trading opens only after a level or win gate.** Found gates: MM2 level 10, Fisch 15, GTD 25 victories, AV 50, Royale High 75. The hours each takes are not known. **Start with:** 1 to 5 hours of play. **Our read:** a gate stops fresh accounts dumping duped items, and players learn prices before they can be cheated.
9. **Every trade has a forced pause after the last change.** Found: 5 s (Adopt Me), 6 s (MM2), 10 s (Royale High). Plus a warning on unfair trades and a record of the last 30 days.
10. **Build anti-dupe before trading.** One serial number per item, never reused, server-side trade, and an automatic freeze on a duplicated serial. AV shipped trading late because of this; TTD's dupes ended up as a product.
11. **Build for intentional co-play.** An invite button at a win or loss, and a private server with custom rules. Joins, invites and private servers are what Roblox counts.
12. **Everything said in words can be said without them.** Preset phrases, an emote wheel, a "follow me" marker, item preview in trades.

## How to do it

1. Write your band and server size on your [one-page design](../kit/templates/one-page-design.md), with one line on why it is not 2 bigger.
2. Table every player-to-player action: who, when (seconds after joining), counter, cooldown, what the server sees.
3. List every visible status item with the share you expect to hold it; each step 2 to 3 times rarer. After launch, read real shares from badge counts (`python tools/snapshot.py`).
4. Write trading rules before trading code: gate, slots, pause, warnings, history, untradable items, dupe detection.
5. Play with three friends, chat off. Add a button or emote for every moment someone had to explain out loud.
6. Run the [design audit](../kit/design-audit.md).

## Checks

| Check | Pass |
|---|---|
| Server size | Within your genre's band; 8 or fewer for any game with stealing |
| Voice | Server size 100 or fewer if you want voice |
| Counter | Every harmful action can be answered by the victim within 5 s |
| Friend bonus | 30% to 50% cap; needs the friend in the server; cannot be farmed by sending friend requests |
| Party | Rewards per player and difficulty both change with group size, written as numbers |
| Revive | A free route exists; paid price 45 R$ or less; no prompt at the moment of death in a streak |
| Trade gate | 1 to 5 hours of play before trading opens |
| Trade pause | 5 to 10 s after the last change, with an unfair-trade warning |
| Dupe | Every tradable item has its own serial number, checked on the server; 0 items share one |
| No text | Trading, helping and grouping all work with chat switched off |
| Invite | An invite prompt appears at a win or loss, checked with `CanSendGameInviteAsync` |

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Players in the server but nobody notices anyone | Server too big, or bases far apart | Cut to the genre's low end; put bases around one shared spot |
| A friend lands in another server | Friends weight lowered in custom matchmaking | Keep Friends at 15 |
| Players leave after being robbed | No counter within 5 s, or the loss is too big | One unit per theft; a free tool to hit the thief; protection after joining |
| Friend requests flood the game | Friend bonus that pays per request or per new friend | Pay only for friends already in the server, capped |
| Duped items flood the market | Client-side trades, no serial numbers | Server-side trades, one serial per item, freeze on duplicate |
| Trades are scams | Accept possible right after a swap | 5 to 10 s pause after any change; unfair warning; history |
| Private servers empty public ones | Same pay as public | Full rate only in public |

## Sources

Every fact links its source inline. The groups: Roblox public API (games, badges, passes), 25 Nov 2026; Roblox Creator Docs ([matchmaking](https://create.roblox.com/docs/en-us/matchmaking/scoring), [discovery](https://create.roblox.com/docs/en-us/production/promotion/discovery), [private servers](https://create.roblox.com/docs/en-us/production/monetization/private-servers), [voice](https://create.roblox.com/docs/en-us/chat/voice-chat), [chat guidelines](https://create.roblox.com/docs/en-us/chat/guidelines)); the Roblox newsroom and DevForum; game wikis (MM2, Adopt Me, Royale High, Jailbreak, Anime Vanguards, Toilet Tower Defense, Doors, TDS, Grow a Garden); and press ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/), [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden), [Hatchet](https://hatchet.gg/blog/the-link-between-roblox-streamers-and-roblox-players/)).

Next: [10-feel-and-feedback.md](10-feel-and-feedback.md).
