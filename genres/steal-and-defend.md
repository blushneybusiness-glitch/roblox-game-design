# Steal and defend

> **The feeling sold:** "My base makes money and everyone can see it. I can take their best one, and they can take mine if I forget the lock."

This page applies the genre template to the steal family: [Steal a Brainrot](../teardowns/steal-a-brainrot.md), [Steal An Egg](../teardowns/steal-an-egg.md), Break and Steal an Egg and the copies around them. Why each part works is argued once, in [slop/02-why-it-holds.md](../slop/02-why-it-holds.md). This page gives the per-game numbers and the starting values for a new game of this kind. Player counts marked "now" are from the Roblox public API, 25 Nov 2026, 13:53 UTC, a weekday morning in the US.

## At a glance

| | |
|---|---|
| Core verb | Buy (or grab) a unit, place it, and carry other players' units away |
| Study these first | [Steal a Brainrot](../teardowns/steal-a-brainrot.md): the reference conveyor, lock and rebirth tables. [Steal An Egg](../teardowns/steal-an-egg.md): the same payoff with a trained stat and a run home. Break and Steal an Egg: a follower that worked (1.31M peak, [RoStats](https://rostats.io/records)). BIG Games' Steal a Pet: the reskin that failed (7 players now) |
| Session that works | About 9 minutes (Steal a Brainrot) to 16 to 17 minutes (Steal An Egg), tracker estimates ([RoVitals](https://rovitals.com/game/109983668079237), [Rolimons](https://www.rolimons.com/game/107778070777162)) |
| Players per server | 8 (Steal a Brainrot), 7 (Steal An Egg, Break and Steal an Egg). Dead clones used 10 (Roblox public API, 25 Nov 2026) |
| Who owns the genre | Open to a changed verb, closed to a reskin. Steal a Brainrot (created May 2025) is at 42K now; Steal An Egg (created July 2026) took first place on Roblox within two months and holds 852K now. Both are owned by DoBig Studios ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games)) |
| Build cost | Teams in this scene are 5 or 6 people and ship in days to months ([IJoC, 2026](https://ijoc.org/index.php/ijoc/article/download/25738/5347/109408?inline=1)). **Our read:** a first version is about three weeks for one to three people ([slop/04-build-it.md](../slop/04-build-it.md)); the costly parts are server-checked theft and weekly content |
| Money comes from | x2 cash passes (299 R$), a VIP pass (375 R$), and developer products, listed with their prices in the teardowns of [Steal a Brainrot](../teardowns/steal-a-brainrot.md) and [Steal An Egg](../teardowns/steal-an-egg.md) |
| What kills clones | Same verb, late, then no updates |

## Why people play it

The audience skews young: about 35% of Grow a Garden's players were under 13, the closest age figure the research has for this family ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Steal a Brainrot's growth came from theft clips and strategy videos with tens of millions of views ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)). Its own store text lists five verbs, ending with "troll" (Roblox public API, 25 Nov 2026).

**Our read:** the player buys two things. One is a number that goes up every second at a base anyone can walk past. The other is a story: "I took a Brainrot God from the kid next door" or "I lost mine at the door". The second is what gets filmed. The same theft is what reviewers attacked: Polygon wrote that Steal a Brainrot became the biggest game on Roblox by making children miserable (quoted by [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)). Read [foundations/15-the-line.md](../foundations/15-the-line.md) before you build a theft game.

## The loop, with a stopwatch

Leader: Steal a Brainrot. Seconds are "not known" where no source timed them.

| Step | Player does | Seconds | Sees and hears | Number that moves |
|---|---|---|---|---|
| 1. Pick | Walks to the shared carpet and buys a unit as it passes | not known (spawn interval not found) | Units walk out of a cave and vanish at the far end; God and Secret spawns are announced to the server ([wiki](https://stealabrainrot.fandom.com/wiki/Red_Carpet)) | Cash down by the price ($25 to $250B) |
| 2. Walk home | Nothing; the unit walks to the base | not known | Any player can buy it out from under you for 150% of the price while it walks | Risk of losing it |
| 3. Earn | Nothing | Every 1 s | Cash ticks up at the plot | $1/s to $600M/s base income |
| 4. Pay back | Waits or does steps 5 to 6 | 25 to about 300 s for normal units | The next unit becomes affordable | Payback is price divided by income ([AllThings.How](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/)) |
| 5. Lock | Presses the base button | 60 s, +10 per rebirth, +10 with VIP | A shield over the base ([wiki](https://stealabrainrot.fandom.com/wiki/Base)) | Lock time |
| 6. Steal | Walks into an unlocked base, picks up a unit, carries it home | Hold and carry time not known | Owner gets an alarm naming the unit; thief slows from speed 34 to 20 and cannot use gear; a success is broadcast in the rarity's colour ([wiki](https://stealabrainrot.fandom.com/wiki/Stealing)) | One unit moves bases |
| 7. Defend | Hits the carrier with the free bat | not known | The unit goes back home ([wiki](https://stealabrainrot.fandom.com/wiki/Gears)) | Unit saved |
| 8. Rebirth | Pays cash plus two named units | First one at about 32 min of ideal play (our arithmetic, see below) | +1 slot, longer lock, new gear, a new floor at R2 and R10 | Multiplier +1 |

**How Steal An Egg differs.** There is no shop. The player grabs an egg from a wild animal in one of 15 biomes and runs it home while the biome's guardian and other players try to knock them down; bats and bear traps make the carrier drop it ([Bloxodes](https://bloxodes.com/wiki/steal-an-egg)). The egg grows in the base, hatches and earns. Between trips the player trains Speed on a treadmill, and Speed is the key to the next biome ([wiki](https://stealanegg.fandom.com/wiki/Biomes)). So the purchase of step 1 becomes a trip, and the wait of step 4 becomes training. Break and Steal an Egg adds breaking the egg with a pickaxe, guards and an index (Roblox public API, 25 Nov 2026).

**The loop stack** in Steal a Brainrot:

| Every | What closes | Number |
|---|---|---|
| 1 second | A cash tick | $1/s at the start |
| 30 seconds | A new arrival's protection ends | 30 s ([wiki](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing)) |
| 1 to 4 minutes | The lock runs out; the next unit pays back | 60 to 250 s lock (250 s at R19 is our arithmetic); 25 to 300 s payback |
| 5 / 15 / 45 minutes | A Legendary / Mythic / Brainrot God is guaranteed on the carpet | [wiki](https://stealabrainrot.fandom.com/wiki/Red_Carpet); the 45 is the wiki's estimate |
| 1 to 2 hours | A seasonal event: every 2 h on weekdays, every hour at weekends | [wiki](https://stealabrainrot.fandom.com/wiki/Hourly_Events) |
| About 3 to 4 sessions | Rebirth 1 | 32 min ideal against 9-minute sessions (our arithmetic) |
| 7 days | The Saturday update | 75 updates in 77 weeks ([wiki](https://stealabrainrot.fandom.com/wiki/Update_Log)) |

## The first five minutes

Nobody in the research timed these games on a device. The leader's timeline below is reconstructed from the wiki numbers; every line is **Our read** unless it carries a link.

| By | This has happened | Source or reasoning |
|---|---|---|
| 0:05 | Spawned next to an empty base of 10 slots, facing the carpet | Base is free on joining, 10 slots on floor 1 ([wiki](https://stealabrainrot.fandom.com/wiki/Base)) |
| 0:30 | An arrow and a "go buy a Noobini" prompt; the first unit bought if one has walked out. Join protection ends | The only scripted tutorial step found ([wiki](https://stealabrainrot.fandom.com/wiki/Noobini_Pizzanini)); Noobini is 100 of the carpet's 590 weight, about 17% of spawns (our arithmetic); 30 s protection ([wiki](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing)). Starting cash: not known |
| 1:00 | First unit has paid back its $25 | 25 s payback at $1/s |
| 3:00 | Second unit type (Lirilì Larilà, $250) affordable | 1.5 to 4 min by the research's arithmetic |
| 5:00 | Tim Cheese ($500) affordable; a Legendary has crossed the carpet | About 4 min; the 5-minute pity timer |

Gates for a new game in this genre. **Start with:**

| By | Gate | Why this number |
|---|---|---|
| 0:15 | One earning unit owned | The leader's first unit is affordable at once and pays back in 25 s |
| 0:30 | Unit 1 has paid for itself | 25 s payback plus walking time |
| 1:00 | First contact with theft (seen, done or suffered) | The leader's protection window is 30 s; the action exists from the first minute |
| 3:00 | Lock used once; second unit type owned | Lock lasts 60 s, so a player who has locked once will meet the timer again inside the session |
| 5:00 | The next rebirth's two named units shown; a guaranteed rare has appeared in the shared shop | The 5-minute pity timer |

## Numbers that work

**The carpet's odds.** The wiki publishes spawn weights; the shares are our arithmetic from a weight total of about 590 ([wiki](https://stealabrainrot.fandom.com/wiki/Red_Carpet), read 25 Nov 2026).

| Rarity | Weight per unit | Share of spawns | Roughly 1 in | Guarantee |
|---|---|---|---|---|
| Common | 100 (Noobini) down to 37 | 62.7% | 1.6 | |
| Rare | 30 down to 15 | 25.1% | 4 | |
| Epic | 13 down to 1.75 | 11.0% | 9 | |
| Legendary | 1 down to 0.3 | 1.0% | 100 | within 5 min |
| Mythic | 0.2 down to 0.05 | 0.23% | 430 | within 15 min |
| Brainrot God | 0.05 down to 0.0001 | 0.020% | 5,000 | within about 45 min |
| Secret | 0.0003 down to 1e-15 | 0.00007% | 1.4 million | none |

Steal An Egg uses the same top odd: from Cherry Blossom on, every biome rolls 37.51 / 26.27 / 16.83 / 13.96 / 4.36 / 0.74 / 0.31 / 0.02%, so the top pet is 1 in 5,000 there too ([wiki](https://stealanegg.fandom.com/wiki/Drop_Rates)).

**Ownership rules in Steal a Brainrot** ([Base](https://stealabrainrot.fandom.com/wiki/Base), [Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Stealing](https://stealabrainrot.fandom.com/wiki/Stealing), [Gears](https://stealabrainrot.fandom.com/wiki/Gears)):

| Rule | Value |
|---|---|
| Slots | 10 (R0 to R1), 11 to 18 on floor 2 (R2 to R9), 19 to 25 on floor 3 (R10 to R19) |
| Sell-back | 50% of price |
| Buy-out of a unit walking home | 150% of price |
| Lock | 60 s, +10 s per rebirth, +10 s with the VIP pass |
| Join protection | 30 s |
| Carrier | Speed 34 to 20 (-41%), jump 7.2 to 4.32 (-40%), no gear |
| Free defence | A bat for every player; a hit sends the unit home |
| First speed gear | Speed Coil, $750, speed 34 to 51 (+50%) |
| Trap | $1K, freezes for 7 s, at most 5 placed |
| Index | Each completed entry adds +0.5x income |

Our arithmetic on those rows: a defender with the $750 coil runs at 51 against a carrier's 20, 2.55 times faster. A buy-out at 150% turns a 200-second payback (Tralalero Tralala, $10M at $50K/s) into 300 seconds, still inside the normal ladder, so sniping a God unit off the carpet is always worth it.

**Rebirth cash ratios** (cash from [Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/rebirths), 17 Nov 2026; ratios our arithmetic): R1 $500K, R2 x3, R3 x8.3, R4 x2.8, R5 x2.9, then about x3.2 per step to R7 ($1B), x5 per step to R10 ($125B), x3.8 per step to R15 ($100T) and x4.2 per step to R19 ($30Qa). Multiplier +1 each time.

**Steal An Egg's treadmills** cost x17 to x27 more per tier while Speed per step rises only x1.25 to x2.7 ([wiki](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data)). The full ladder and the steps per biome gate are in [the teardown](../teardowns/steal-an-egg.md).

**Start with:**

| Value | Start with | Derived from |
|---|---|---|
| Players per server | 6 to 8 | Leaders 7 and 8; dead clones 10 |
| Shop | One shared conveyor, about 60% common, 25% rare, 11% epic, 1% legendary, 0.25% mythic, 0.02% top | Steal a Brainrot's shares rounded |
| Guarantees | Legendary 5 min, mythic 15 min, top tier 45 min | Same pity timers; a 9-minute session sees one legendary at least |
| Buy-out | 150% while the unit walks home, walk 5 to 10 s | Keeps the snipe inside a 300 s payback |
| Slots | 10, then +1 per rebirth and a new floor at R2 and R10 | Same |
| Sell-back | 50% | Same |
| Lock | 60 s, +10 s per rebirth | Same; 250 s by R19 |
| Carrier | 60% speed, no gear; first defence gear at 150% speed | 2.5x chase ratio, as above |
| Join protection | 30 s is the leader's value; this handbook's recipe uses 5 min ([slop/04-build-it.md](../slop/04-build-it.md)) | A new player should earn before they can lose |
| Rebirth 1 | 20 to 40 min of steady play, two named units | The leader's is about 32 min ideal |
| Rebirth cost | x3 per step, one x8 jump at R3, multiplier +1 | Steal a Brainrot R1 to R5 |

## What brings them back

**Later in the same session.** The lock runs out every 60 to 250 seconds. A Legendary is due every 5 minutes and a Mythic every 15. Steal a Brainrot also runs a seasonal event every 2 hours on weekdays and every hour at weekends ([wiki](https://stealabrainrot.fandom.com/wiki/Hourly_Events)). In Steal An Egg the eggs in every biome reset every 5 minutes ([wiki](https://stealanegg.fandom.com/wiki/Eggs)).

**Tomorrow.** Offline income. Steal a Brainrot's wiki contradicts itself: the Cash page says about 50% of the online rate, the Offline Cash page says about 3% with a 5-hour cap ([Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash)). The second page's own example (a day offline worth about 43 minutes online) equals 3% of 24 hours, so it ignores its own cap. Treat the real rule as not known. No daily reward was found in either leader.

**Next week and after.** The Saturday update: Steal a Brainrot shipped Update 1 on 31 May 2025 and Update 75 on 14 November 2026 ([wiki](https://stealabrainrot.fandom.com/wiki/Update_Log)). Twelve limited mutations from x2 to x14, all on Saturdays ([Bloxodes](https://bloxodes.com/wiki/steal-a-brainrot/mutations)). Steal An Egg runs a new event every Saturday from 7 to 8 AM PT, with a boss inside the event at :15 and :45 past every hour for 5 minutes ([Bloxodes](https://bloxodes.com/articles/steal-an-egg-turkey-takeover-guide)). Rebirth caps were raised in steps, from R6 to R7 at Update 1 up to R19 at Update 62, so the ladder kept growing ([wiki](https://stealabrainrot.fandom.com/wiki/Update_Log)).

## Other players

- **Server size.** 7 or 8. **Our read:** at that size every neighbour is a person you can name by the end of a session; see [slop/02-why-it-holds.md](../slop/02-why-it-holds.md), mechanism 4.
- **What a player sees.** Every base and every unit on its plot. Rare spawns and successful thefts are announced to the server.
- **What they can do to each other.** Snipe a unit walking home (150%), steal from an unlocked base, hit a carrier, trap (7 s), and from R4 the Boogie Bomb makes a target drop the unit ([wiki](https://stealabrainrot.fandom.com/wiki/Gears)). Of 40 gear items only 3 need no rebirth, so each rebirth hands over new ways to act on other players.
- **What can be lost and how it is protected.** One placed unit per theft. Protection: the lock, the 30-second join window, the bat, and one unit (Spyder Elephant) that cannot be stolen.
- **Trading.** The Trade Plaza (Update 54, 20 Jun 2026) has no stealing inside. Its tiers gate on income: normal, Pro at 25B/s, OG at 100B/s plus an OG unit ([wiki](https://stealabrainrot.fandom.com/wiki/Trade_Plaza)). **Our read:** 25B/s is 100 times the base rate of the top Secret unit ($250M/s), so the Pro room is a status room.
- **The clip.** A theft that ends at the door, or a God unit sniped while it walks home.

## Money

| Game | Item | Type | R$ |
|---|---|---|---|
| Steal a Brainrot | 2x Money | Pass | 299 |
| Steal a Brainrot | VIP (includes +10 s lock) | Pass | 375 |
| Steal a Brainrot | Admin Commands | Pass | 7,999 |
| Steal An Egg | X2 Money | Pass | 299 |
| Steal An Egg | X2 Growth Speed (eggs grow twice as fast) | Pass | 467 |
| Steal A Pet And Ride It | Auto Collect 49, Sakura Barn 149, VIP 199, Race Car Treadmill 249, 3x Open Speed 299, x2 Tickets 299, Mini Games VIP 299, Champion Pass 399 | Passes | 49 to 399 |

Sources: Roblox public API, 25 Nov 2026. Developer products (lucky blocks, Speed in Steal An Egg, items) could not be read; Kotaku confirms Speed can be bought with real money in Steal An Egg ([Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952)).

What backfired: the strongest items and server-admin powers sold for Robux drew the pay-to-win criticism ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot)). **Our read:** in a theft game, any paid item that takes from or protects against another player is the part a parent objects to. Policy points: paid luck or lucky blocks are paid random items; see [foundations/15-the-line.md](../foundations/15-the-line.md) and [foundations/12-monetization.md](../foundations/12-monetization.md).

## Live ops

Steal a Brainrot: one update every Saturday for 77 weeks (75 updates), plus events every 1 to 2 hours. One experiment failed: an hourly "Admin Machine" that the wiki records as a failure ([wiki](https://stealabrainrot.fandom.com/wiki/Hourly_Events)). Steal An Egg: Saturday events since October 2026, a Jonas Brothers concert on 31 Oct 2026 ([Bloxodes](https://bloxodes.com/wiki/steal-an-egg)). Both were updated within a day of 25 Nov 2026. The clones in the next section stopped within days to months. **Our read:** a small team can hold one Saturday update a week if three are built before launch ([slop/04-build-it.md](../slop/04-build-it.md)).

## How these games die

| Symptom you can measure | Likely cause | Fix |
|---|---|---|
| Peak to weekday morning below 0.2% after a year: Steal a Brainrot 25.4M to 25.9M (Oct 2025) down to 42,139 (0.17%) | The trend aged; event spikes inflated the peak | Keep the Saturday: it still drew 729K on 21 Nov 2026 against about 37K on weekdays ([RoVitals](https://rovitals.com/game/109983668079237)) |
| Same-verb copy near zero within months: BIG Games' Steal a Pet, created 32 days after Steal a Brainrot, 7 players now, last update 6 Feb 2026 | A reskin of a game players already have progress in | Change the verb ([slop/03-quality-bar.md](../slop/03-quality-bar.md)) |
| Updates stop after weeks: Steal Anime! (last update Aug 2025, 457 now), Italian Brainrot Thieves (Oct 2025, 231) | A single push, no service | Weekly update day fixed before launch |
| Server of 10 with bases nobody passes: Italian Brainrot Thieves | Neighbours become strangers | 6 to 8 per server |
| Follower falls to 5% of its peak in 5 weeks: Break and Steal an Egg 1.31M (18 Oct 2026) to 61,970 | Hot window of a wave | Plan the product list and events for a 4 to 10 week window ([slop/05-after-the-peak.md](../slop/05-after-the-peak.md)) |
| Leader down 37.6% on its 30-day average two months after peak: Steal An Egg ([RoVitals](https://rovitals.com/game/107778070777162)) | Normal decay, slowed by weekly events | Rebirths and collections that last weeks |
| About 200 public cheat scripts: Steal a Brainrot ([Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/)) | Client-trusted actions | Server decides every buy, carry and lock |

Sources for counts: Roblox public API, 25 Nov 2026; [RoStats](https://rostats.io/records).

## Checklist

- [ ] 6 to 8 players per server; every base visible from the shared shop.
- [ ] First earning unit owned within 15 seconds; it pays back in 30 seconds or less.
- [ ] Conveyor shares published in the game; the top tier is 1 in 5,000 or rarer and has a guarantee timer.
- [ ] Guarantees at 5, 15 and 45 minutes for the three rarest regular tiers.
- [ ] A unit walking home can be bought out at a premium (start at 150%).
- [ ] 10 starting slots, 50% sell-back.
- [ ] Lock lasts 60 seconds and grows 10 seconds per rebirth.
- [ ] A carrier is slowed by about 40% and cannot use gear; a free tool lets any defender stop them.
- [ ] Nothing can be taken in a player's first 30 seconds (better: first 5 minutes) or while they are offline.
- [ ] Rebirth 1 needs two named units and is reachable in 20 to 40 minutes.
- [ ] Every rebirth adds one slot, 10 seconds of lock and at least one new gear item.
- [ ] A theft is announced to the server and the owner gets an alarm naming the unit.
- [ ] No Robux prompt opens when something is stolen.
- [ ] A trade area exists where stealing is off.
- [ ] Three Saturday updates built before launch.

## Twists and open space

Variations that produced hits:

- Take from the wild, not a shop, and run it home past a guardian: Steal An Egg, 14.3M peak ([RoStats](https://rostats.io/records)).
- Break the egg out with a pickaxe and dodge guards: Break and Steal an Egg, 1.31M peak.
- Defend with plants against units that walk at you, which then become yours: Plants vs Brainrots, covered in [grow-and-harvest.md](grow-and-harvest.md).
- Ride the collectible: Steal A Pet And Ride It, 7,980 now (Roblox public API, 25 Nov 2026).

**Our read** on open angles:

- Theft with a cost to the thief. Today a failed theft costs nothing. A carry that risks one of the thief's own units would make defence and attack the same size of decision.
- Team bases. Every leader is one player per base. Two friends sharing a base and a lock would use the friend signal Roblox counts ([foundations/02-the-platform.md](../foundations/02-the-platform.md)).
- A version for younger players with theft replaced by a race to the same unit. Same carpet, same snipe, nothing taken from a base.

## Sources

- Teardowns: [Steal a Brainrot](../teardowns/steal-a-brainrot.md), [Steal An Egg](../teardowns/steal-an-egg.md).
- Analysis: [slop/01-anatomy.md](../slop/01-anatomy.md), [slop/02-why-it-holds.md](../slop/02-why-it-holds.md), [slop/03-quality-bar.md](../slop/03-quality-bar.md), [slop/04-build-it.md](../slop/04-build-it.md), [slop/05-after-the-peak.md](../slop/05-after-the-peak.md).
- Steal a Brainrot wiki: [Base](https://stealabrainrot.fandom.com/wiki/Base), [Red Carpet](https://stealabrainrot.fandom.com/wiki/Red_Carpet), [Cash](https://stealabrainrot.fandom.com/wiki/Cash), [Offline Cash](https://stealabrainrot.fandom.com/wiki/Offline_Cash), [Stealing](https://stealabrainrot.fandom.com/wiki/Stealing), [Methods of stealing](https://stealabrainrot.fandom.com/wiki/Methods_of_stealing), [Gears](https://stealabrainrot.fandom.com/wiki/Gears), [Update Log](https://stealabrainrot.fandom.com/wiki/Update_Log), [Hourly Events](https://stealabrainrot.fandom.com/wiki/Hourly_Events), [Trade Plaza](https://stealabrainrot.fandom.com/wiki/Trade_Plaza).
- Steal An Egg wiki: [Biomes](https://stealanegg.fandom.com/wiki/Biomes), [Eggs](https://stealanegg.fandom.com/wiki/Eggs), [Drop Rates](https://stealanegg.fandom.com/wiki/Drop_Rates), [Treadmills data](https://stealanegg.fandom.com/wiki/Module:Treadmills/Data).
- [Bloxodes: Steal a Brainrot rebirths](https://bloxodes.com/wiki/steal-a-brainrot/rebirths), [mutations](https://bloxodes.com/wiki/steal-a-brainrot/mutations), [Steal An Egg](https://bloxodes.com/wiki/steal-an-egg); [AllThings.How price table](https://allthings.how/steal-a-brainrot-values-belt-price-and-income-per-second-for-all-99-brainrots/); [RoStats records](https://rostats.io/records); [RoVitals](https://rovitals.com/); [Game Rant](https://gamerant.com/roblox-what-is-steal-a-brainrot-explained-gameplay-player-count-scripts/); [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot); [Kotaku](https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952).
- Roblox public API (games, game passes), 25 Nov 2026.
