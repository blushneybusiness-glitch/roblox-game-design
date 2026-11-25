# The first session

Open this page when you are designing what a new player does from the moment they have control, or when your dashboard shows players leaving in the first five minutes.

The first session is not a tutorial placed in front of the game. It is the game, played by the hardest audience it will ever have: someone who knows nothing, owes you nothing, and has a full page of other games one tap away. This page turns "make a good first impression" into a script with times and a set of gates to measure.

## What is known

**Roblox ranks games on the first minutes.** Its recommendation system counts first-play bounce in two buckets, players who leave in under 60 seconds and players who leave between 61 and 180 seconds, next to play-through rate, play days and playtime ([02-the-platform.md](02-the-platform.md)). A weak first three minutes costs the player and then costs every future impression.

**Most new players do not come back.** Across more than 500 large Roblox games, the median share of new players who return the next day is 10.3%, and the top 1% of games reach 22.2% ([02-the-platform.md](02-the-platform.md)). The first session is the only session most players will ever have.

**A new game's first audience is 16 and older.** Since June 2026 a new experience reaches under-16s only after enough older, age-checked players have engaged with it ([02-the-platform.md](02-the-platform.md)). The first session has to hold a 16-year-old before a 9-year-old ever sees it.

**What the hits put in the first minute:**

| Game | The first thing a new player gets | Source |
|---|---|---|
| Steal a Brainrot | A free base with 10 slots, 30 seconds of protection, and a $25 unit that earns $1 a second | [slop/01-anatomy.md](../slop/01-anatomy.md) |
| Grow a Garden | A seed for 10 that is ready in 8 seconds and sells for about 20 | [slop/01-anatomy.md](../slop/01-anatomy.md) |
| Plants vs Brainrots | $400, exactly the price of two starter plants that grow in 5 seconds | [slop/01-anatomy.md](../slop/01-anatomy.md) |
| Tower Defense Simulator | Two free towers; the easiest mode is 20 waves in 7 minutes and pays 300 coins, enough for the next unlocks at 100, 200 and 300 | [genres/tower-defense.md](../genres/tower-defense.md) |
| Brookhaven | 15 of 21 house plots and 80 of 81 roles free | [genres/roleplay.md](../genres/roleplay.md) |
| Doors | The first monster can arrive as early as door 3 | [genres/horror.md](../genres/horror.md) |

None of these opens with an explanation. Each opens by handing over the thing the title promised.

**How many players get past the first gate.** From Roblox's public badge endpoint, 25 November 2026:

| Game | First gate | Share of everyone who joined |
|---|---|---|
| Speed Run 4 | Finish level 1 | 62% |
| Doors | Survive the first monster | 55% |
| +1 Speed Keyboard Escape | Rebirth once | 42% |
| A Dusty Trip | Travel 1,000 metres | 25% |
| Driving Empire | Own 5 cars | 20% |

Sources and detail are on the genre pages. Across the 15 charted games that have both a welcome badge and a numbered chain of milestones, the median share of welcome-badge holders who reached the first milestone is 24%, with a range from 1% to 89% [data, Nov 2026] ([data/ANALYSIS.md](../data/ANALYSIS.md)). Even in hits, most players never clear the first real milestone. Where you place that milestone, and how hard it is, decides more than anything that comes after it.

**A yardstick, with a warning.** A first-session survival target that circulates among Roblox producers is 95% of new players still present at 30 seconds, 87% at one minute and 65% at five minutes. We could not find it in a written source, so treat it as one practitioner's bar, not a benchmark. The chart to hold it against exists: Roblox's dashboard has a "New User First Session Retention" chart showing the share still playing each minute after joining ([14-metrics-and-diagnosis.md](14-metrics-and-diagnosis.md)).

## The rules

**1. The title's promise happens in the first 30 seconds.** If the game is called Steal a Brainrot, a brainrot is in front of the player when they gain control. The gap between what the title and thumbnail promised and what the first half minute delivers is what the bounce buckets measure.

**2. The player does the core verb before anything explains it.** First input within 5 seconds of gaining control. The object to act on is within 10 studs of the spawn and is the most visible thing on screen.

**3. The first reward arrives within 10 to 15 seconds and is not the worst one.** The hits pay inside 8 to 25 seconds. A first reward from the bottom of the rarity table teaches the player that this is what the game feels like.

**4. Nothing can fail in the first minute.** Rig the first attempts: the first throw lands, the first catch holds, the first purchase is affordable to the coin. Plants vs Brainrots sets starting money to exactly two purchases. Real difficulty starts once the player has something.

**5. One new thing at a time, taught by doing it.** A pointer, an arrow or a highlighted object, with at most three words. No paragraph, no slideshow, no video. If a step needs a sentence to explain, redesign the step.

**6. The first purchase is the tutorial for buying.** By 45 to 60 seconds the player has spent in-game money on something that visibly changed their situation, and can see the next thing to buy.

**7. A long goal is on screen by minute 5.** Something the player wants and cannot yet afford, shown as a picture and a number: the next zone, the rebirth requirements, the car in the showroom.

**8. Another player's success is visible by minute 5.** A richer base next door, a higher rank on a board, a rare pet walking past. It answers the question "what does this look like if I keep going?" without a word.

**9. No offers, no pop-ups, no windows that open by themselves.** Not in the first five minutes. A purchase prompt before the player cares teaches them to close things.

**10. The HUD grows with the player.** Show only the controls the player needs right now. A button appears the first time it is useful. A new player facing sixteen icons reads none of them.

**11. Design for the hardest case.** A 10-year-old on a 3 GB Android phone, sound on, alone, who has never played this genre and will read three words at most. Then check it still works for a 16-year-old on a laptop, because that is who arrives first.

**12. Skill gates wait.** See the badge table above. Put the first test of skill after the first reward, the first purchase and the first sight of the long goal.

## Gates

**Start with** these and tighten them from your own funnel. The first column is common to every genre. Genre pages give their own values where the evidence differs.

| Gate | Collect-and-earn games | Round and match games | Run-based games (horror, survival) | Open games (roleplay, sandbox) |
|---|---|---|---|---|
| First input after gaining control | 5 s | 5 s (in a lobby with something to do) | 5 s | 5 s |
| First reward | 10 to 15 s | First round under way within 60 s | First item or opened door within 30 s | A house or vehicle owned within 60 s |
| The title's promise has happened | 30 s | 60 s | 60 to 90 s (first threat) | 60 s |
| First purchase or upgrade | 45 to 60 s | After the first round, under 4 min | After the first run | Not needed |
| First rare or surprising moment | 2 min | First win or near-win, under 5 min | First scare, under 3 min | First secret or first other player, under 3 min |
| First moment with another player | 3 min | In the first round | From the lobby | 2 min |
| Long goal on screen | 5 min | 5 min | End of the first run | Not needed; show the range of things to do |
| Words the player must read | 10 | 15 | 15 | 10 |
| Offers shown | 0 | 0 | 0 | 0 |

The values in the first column match what the collect-and-earn hits do. The other columns are our reading of the genre pages, where timed first sessions were mostly not available.

## How to do it

1. **Write the script.** Fill [kit/templates/first-session-script.md](../kit/templates/first-session-script.md): one row for every 20 seconds or less, from 0:00 to 15:00, saying what the player does, sees and hears.
2. **Mark the gates** on the script and compare them with the table above.
3. **Build it in grey boxes** before anything else exists.
4. **Watch a stranger play it** on a phone. Say nothing. Run a stopwatch. Write the measured time next to each gate. Repeat with five more people. Children if the game is for children.
5. **Log one funnel event per row** of the script, numbered in the order players do the steps.
6. **Launch small and read the chart.** On the first-session retention chart, find the minute with the steepest fall. Open the game, play to that minute, and look at what is on screen.
7. **Change one thing** in that minute. Ship. Read again after the data window. Repeat. Expect to do this many times; the first version of a first session is never the one that works.

## Checks

- [ ] A stranger on a phone reached the first reward in under 15 seconds without help.
- [ ] The thing the title names is on screen when the player gains control.
- [ ] The first three attempts at the core verb cannot fail.
- [ ] The first reward is from the middle of the table or better.
- [ ] The player reads ten words or fewer in the first five minutes.
- [ ] No window opens by itself and no offer appears in the first five minutes.
- [ ] By minute 5 the player has seen something they want and cannot afford.
- [ ] By minute 5 the player has seen what a more advanced player owns.
- [ ] The HUD shows six controls or fewer in the first minute.
- [ ] Each row of the script has a funnel event, and the dashboard shows the share reaching each one.
- [ ] The measured gates are written next to the scripted ones.

## Mistakes

| Symptom on the dashboard | Cause | Fix |
|---|---|---|
| Many leave in under 60 seconds | The first screen is not what the title promised, or the player cannot find the first thing to do | Put the promised object at the spawn. Remove everything between spawn and first input |
| Many leave between 1 and 3 minutes | The first reward came, and the second did not, or a wait arrived with nothing to do | Check the loop table for dead time ([04-core-loop.md](04-core-loop.md)). Make the second and third purchase as fast as the first |
| A cliff at one funnel step | That step can be failed, or needs reading | Rig it so it cannot fail the first time. Replace the text with a pointer |
| Players finish the opening and leave by minute 6 | No long goal; the opening ended and nothing replaced it | Put the next zone, the reset requirements or a rare item on screen before minute 5 |
| Good first session on desktop, poor on phones | A control is under the left thumb, text is too small, or the frame rate drops | Test on a 3 GB Android phone. See [10-feel-and-feedback.md](10-feel-and-feedback.md) |
| Players who arrive from ads leave faster than the rest | The ad promised something else, or ad traffic is simply colder | Compare by traffic source before changing the game ([11-clips-and-packaging.md](11-clips-and-packaging.md)) |
| The tutorial has a high completion rate and next-day return is still low | The tutorial is separate from the game | Delete the tutorial. Teach inside the first real loop |

## Sources

Platform signals, medians and the under-16 rule: [02-the-platform.md](02-the-platform.md). First-minute facts for each game: the slop and genre pages linked in the tables. Badge shares: Roblox public badge endpoint, 25 November 2026. The gate values and the rules are our reading of those facts; the collect-and-earn column is the best supported.
