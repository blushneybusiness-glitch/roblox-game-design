# From stats to a plan

Use this page when you have a live game's numbers and must decide what to change first. It starts from a filled [stats intake](templates/stats-intake.md) and ends with one change, the number it should move, and the date you will know. An AI agent can follow it step by step, and a person can check that the agent did.

The stages, the benchmarks and the table of symptoms are in [foundations/14-metrics-and-diagnosis.md](../foundations/14-metrics-and-diagnosis.md). This page is the order of work.

## What numbers can and cannot do

- **They find the moment:** the stage, the minute, the step, the device, the traffic source.
- **They do not give the cause.** A step that loses 29% of everyone who joined can be hidden, slow, hard or dull. The funnel looks the same for all four. The cause comes from watching that moment (step 3) and from a narrower funnel (step 4).
- **A fix is a bet until it is read.** Before-and-after numbers have been published for thumbnails, titles, ads and prices. For first-session changes we found none ([table below](#what-single-changes-have-done)). You learn the size of your fix from your own test.

## Step 0. Check the numbers can carry a decision

| Check | Passes when | If it fails |
|---|---|---|
| Range | 7 full days or more, the same days for every number | Pull the numbers again |
| Players | 1,000 or more new players in the range | Use 14 or 28 days. Under 1,000, trust only gaps of 3 points or more ([foundations/14](../foundations/14-metrics-and-diagnosis.md), rule 6) |
| Quiet range | No update, no ad campaign starting or ending, no event inside it | Use the days after, or read the days before and after apart |
| Complete retention | The range ended 2 or more days ago for day 1, 8 for day 7, 31 for day 30 | Leave the stage out and write "not known yet" |
| Filters | Totals were read with no filter on | Read again |
| Splits | Source shares and device shares each add up to about 100% | Fix the table; the tool warns when they do not |

Write what failed at the top of your report. Do not diagnose on numbers that failed.

## Step 1. Run the tool

Write the intake's numbers into a JSON file ([shape](templates/stats-intake.md#the-file-for-the-tool)) and run:

```
python tools/funnel.py my-stats.json
```

It prints, in order: checks on the numbers; the step funnel with its largest drop-off; the first-session curve with the leave rate per minute; every stage against its band; the splits by source and device, each gap tested against noise; the rows of the diagnosis table your numbers match; the stage to work on first; and the smallest change your traffic can prove. The end of the report for the invented example in [tools/examples/stats-example.json](../tools/examples/stats-example.json):

```
WORK ON THIS FIRST
  Stage:  First session. Average session time is 5.1 min against a median of 9.0 min (your dashboard).
  Where:  the largest drop-off, 'First purchase' to 'Second purchase', around 0:54 to 2:00:
          1,210 players, 29% of everyone who joined.
          the highest leave rate, 0:30 to 1:00.
  Target: start with half the gap to the other steps:
          the share of joiners who reach 'Second purchase' from 43.1% to 51.3%.
          A 14-day split at your traffic can prove a rise of 3.0 points, so this can be read.
  First:  split every number by traffic source: paid players leave faster than the rest (table above).
          check phones apart from computers: the gap is bigger than the noise (table above).
```

How the tool decides: the first session counts as weak when average session time is under the median, when a third or more of new players are gone at 1:00, or when the curve fell against the previous period by more than the noise. Every other stage counts as weak when its number is under the 50th percentile of your band by more than the noise. The earliest weak stage comes first.

## Step 2. Three checks before you believe the stage

1. **Traffic source.** If paid players leave faster than the rest by more than the noise, read the line that splits the gap. In the example, day 1 retention is 5.0 points under the median and 2.9 of those points are the paid traffic. Roblox's first-session ranking signals count only players who came from Recommended For You ([foundations/14](../foundations/14-metrics-and-diagnosis.md)). If the number is at or above the median without the paid sources, the job is the ads ([foundations/11-clips-and-packaging.md](../foundations/11-clips-and-packaging.md)), not the game.
2. **Device.** If phones are lower than computers by more than the noise, open the Performance page before you redesign anything (step 5, kind "device").
3. **A fall against last period.** If the first-session curve fell by more than the noise, list what shipped between the two periods and read the error and performance reports. This is Roblox's own advice for that chart ([Engagement docs](https://create.roblox.com/docs/en-us/production/analytics/engagement)).

Then take the earliest weak stage. Roblox's ranking weighs the early signals first and says to fix core gameplay before monetization ([foundations/14](../foundations/14-metrics-and-diagnosis.md), rule 1).

## Step 3. Watch the moment

The tool names a window and a step. Go there.

1. On a phone, on an account that has never played, with the sound on and a stopwatch running, play to the step before the drop.
2. Write four lines:
   - At [time] the player has [cash, items, level].
   - The screen shows [every HUD item and every open window].
   - The game asks the player to [action].
   - The next reward is [seconds] away.
3. Count six things: seconds since the last reward, seconds until the next thing can be afforded, items on the HUD, words on screen, windows that opened by themselves, taps the asked action needs.
4. Hold the counts against the gates in [foundations/05-first-session.md](../foundations/05-first-session.md) and in the genre playbook.
5. Watch six first-time players reach that moment, and say nothing. For each one write where they looked, what they tapped first and the second they stalled.

**If you are an AI agent:** with Studio tools you can time the gates in a playtest and count what is on screen. You cannot stand in for a ten-year-old on a phone. Report the gates as measured, report behaviour as "not observed", and ask for a screen recording or the watch notes.

## Step 4. Name the cause with a zoom funnel

A player lost between two steps is in one of four places. A zoom funnel is a second, small funnel that puts three more steps between the two:

| Zoom step | Log it when | A drop just before it means | Kind of fix |
|---|---|---|---|
| Found | The next thing to act on is on the player's screen, or its window is open | They did not find it | World or screen |
| Could | They can do it: enough cash, close enough, cooldown over | They found it and had to wait | Numbers |
| Tried | They press the button or make the attempt | They could and did not want to, or did not understand the button | Rules or screen |
| Done | The step succeeds (the next step of your main funnel) | They tried and it failed | Rules |

Build it as its own funnel and leave the onboarding funnel alone. Roblox allows ten funnels a game, sends funnel events only from the server and only in a published game, and counts a skipped step as done ([Funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)). So log each zoom step only after the one before it:

```lua
local AnalyticsService = game:GetService("AnalyticsService")
local Players = game:GetService("Players")

local ZOOM = "ZoomSecondPurchase"
local reached = {} -- [player] = number of the last zoom step logged

local function zoom(player, step, name)
	if (reached[player] or 0) ~= step - 1 then
		return -- in order only: Roblox counts a skipped step as done
	end
	reached[player] = step
	-- The player's id as the session id makes each player count once.
	AnalyticsService:LogFunnelStepEvent(player, ZOOM, tostring(player.UserId), step, name)
end

Players.PlayerRemoving:Connect(function(player)
	reached[player] = nil
end)

-- Call from the server at each moment:
-- zoom(player, 1, "First purchase done")
-- zoom(player, 2, "Unit 2 on screen")
-- zoom(player, 3, "Can afford unit 2")
-- zoom(player, 4, "Pressed buy")
-- zoom(player, 5, "Owns unit 2")
```

When a step happens on the client, such as a window opening, the client tells the server through a RemoteEvent and the server checks the step number before logging it. The same page shows that check. This zoom reads one session: a player who leaves and comes back is counted where they stopped.

A zoom funnel on a first-session step fills fast, because every new player passes it on their first day. Read it after 3 to 7 days.

**If you cannot add events this week,** use the pointing test. **Our read:** sit next to a first-time player, and when they stall, point at the place on the screen without speaking. If they carry on at once, it was a world or screen problem. If they already knew and were waiting, it is numbers. If they shrug, it is rules: the next step is not worth doing.

## Step 5. Name the kind of fix

Seven kinds. Each has a different owner and a different document. A fix of the wrong kind ships, looks better, and moves nothing.

| Kind | You know it by | Who does it, with what | Before it ships |
|---|---|---|---|
| World | The thing to act on is off screen, behind the player, or more than 10 studs from where they stand | Level layout; [foundations/05](../foundations/05-first-session.md), rules 1 and 2 | A first-time player walks to it within 5 s |
| Screen | The zoom drops at Found while the thing is in reach; first-timers tap the wrong place; more than six items on the HUD at rest; a step needs more than three words read | A UI design process, briefed with [templates/screen-brief.md](templates/screen-brief.md) | The brief's watch test passes |
| Numbers | The zoom drops at Could: the wait for the next purchase is longer than the genre's gate | [templates/economy-sheet.md](templates/economy-sheet.md) and `tools/pacing.py` | The pacing tool passes |
| Rules | The zoom drops at Tried or at Done: the step can fail, costs what the player just earned, or leads to nothing they want. Or long sessions with day 1 under 6%: nothing changes while they are away | The loop table and the script; [foundations/04](../foundations/04-core-loop.md), [08](../foundations/08-retention.md), [15](../foundations/15-the-line.md) | The [design audit](design-audit.md) gates it touches pass |
| Content | Day 1 holds and day 7 falls; players sit at the top of the ladder | [templates/update-plan.md](templates/update-plan.md); [foundations/13](../foundations/13-live-ops.md) | Three updates are built ahead |
| Packaging | Play through rate under the median; paid players leave faster; like ratio under 70% | Thumbnails, title, ads; [foundations/11](../foundations/11-clips-and-packaging.md) | Five different thumbnails, left for 7 days |
| Device | Phones under computers by more than the noise; crashes or out-of-memory exits high on Android | The Performance page and a phone; [foundations/10](../foundations/10-feel-and-feedback.md) | 30 frames a second on a 3 GB Android phone, full server |

**One kind per update.** One change means one thing a player would notice at that moment. A new state of one screen is one change. A new screen and new prices are two, and they ship as two updates, the earlier stage first.

## Step 6. Write up to three hypotheses and choose one

Each in this form:

```
H1  Stat:    share of joiners who reach 'Second purchase'
    Now:     43.1%          Expect: 51% or more
    Change:  one sentence, one change
    Kind:    screen
    Because: what was seen, with a time, a number and what is on screen
    Proof:   split, 14 days, 50/50, goal: onboarding funnel to step 5. Can prove +3.0 points
    Guards:  day 1 retention and playtime do not fall
    Read on: the date
    Wrong if: the number that makes you revert
```

**Start with** an expected number of half the gap to the reference. For a stage, the reference is the 50th percentile of your band. For a funnel step, it is the median keep rate of the other steps in the same funnel. The tool prints both.

Then hold the expected rise against "What your traffic can prove" in the report. If it is smaller than the smallest provable rise, the test cannot read it. Choose a bigger change, a number nearer the start of the funnel, or a longer test. Or ship it on judgement and write "cannot be read" in the log. Do not ship it and later claim it worked.

Order the hypotheses by: the earliest stage, then the most players lost, then the fewest days of work. Ship the first.

## Step 7. Ship it so it can be read

**Put the change behind a config key.** Roblox's experience configs hold values that change without publishing a new version or restarting servers, and can give different players different values ([Configs docs](https://create.roblox.com/docs/en-us/production/configs)). The old screen or number stays in the game as the control.

```lua
local ConfigService = game:GetService("ConfigService")

local function shopVersion(player)
	local snapshot = ConfigService:GetConfigForPlayerAsync(player)
	return snapshot:GetValue("shop_after_first_buy") -- "old" or "new"
end
```

`ConfigService` runs on the server only, so the server reads the value and tells the client which screen to show. The first `GetValue` call is what enrols a player in an experiment. For a change in the first minutes, read it when the player joins. For a change further in, read it when the player first reaches that part, so players who never get there are not enrolled (same page, and [Experiments docs](https://create.roblox.com/docs/en-us/production/experiments)).

**Route A: a Roblox Experiment.** What the Experiments docs say:

| Fact | Value |
|---|---|
| What it compares | A control and one or two variants of a config value. Roblox recommends one variant against the control at 50/50 on a large rollout |
| Length | 14 to 60 days |
| Always tracked | Day 1 and day 7 retention, playtime, session time, ARPU, ARPPU, payer conversion, updated every 24 hours |
| Your own goal | The Custom metric set adds up to three metrics built from funnel, economy or custom events. A funnel metric is the share of players who reach a step you choose |
| Before it starts | Roblox shows the minimum detectable effect for your goal and traffic. It says games under 1,000 daily users may not get useful data |
| First 24 hours | Playtime, ARPU and payer conversion update every 5 minutes. A variant is flagged for harm when its whole confidence interval is below -10% for playtime or -20% for the other two, and only with 10,000 or more players enrolled |
| A result counts | When the confidence interval of the change does not include zero |
| While it runs | The config key is locked. The metrics cannot be changed |

For a first-session fix, set the goal to the onboarding funnel with the step after the leak as its completion step, and target the experiment at new players.

**Route B: before against after.** For games too small for route A. Turn the key on for everyone, then compare 7 full days before with 7 full days after: same weekdays, same filter, nothing else shipped. The count is the same as a 14-day split, but nothing is random, so the weekday, the traffic mix and anything else that changed are in the number too. Trust a gap only when it is bigger than the tool's "7 days each side" figure, and under 1,000 players a side only when it is 3 points or more.

**While a test runs:**

- Ship nothing else. Roblox's wording: changes can invalidate results "even if the changes seem unrelated".
- Leave the thumbnails, the title and the ad spend alone. They change who arrives, and that moves every first-session number.
- Let it run its full length. Early results swing: players react to a change because it is new, and Roblox warns that this fades.
- If the experiment page shows a sample ratio mismatch banner, stop and restart it. The docs say so.

## Step 8. Read, decide, log

1. On the read date, look at the goal first, then the guards.
2. **Keep** when the goal moved by more than the noise and no guard fell. **Revert** when it did not, unless there is another reason to keep the change. Turning the key off is the revert.
3. Write the row in the hypothesis log of [templates/update-plan.md](templates/update-plan.md): date, stat, change, expected, read on, result, keep or revert.
4. Pull the numbers again, run the tool again, take the next leak.

With 14-day experiments this is two measured changes a month, six in a quarter. With 7 days each side it is three or four a month, because the week after one change is the week before the next. Roblox lets experiments on different config keys run at the same time, and says to do it only when you are confident they do not affect each other. Plan a quarter as six to twelve changes, not sixty.

## The report an agent returns

```
STATS REPORT: game, date range
NUMBERS USED   what was given, new players in the range, what failed step 0
WHERE          the stage, the window, the step, with the numbers that show it
NOT THE GAME   how much of the gap is paid traffic, a device, or a fall after an update
WATCHED        what is on screen at that moment; gates measured; who watched and how
CAUSE          one sentence and its evidence. "Not known" when step 3 or 4 was not done
KIND           one of the seven
HYPOTHESES     up to three in the form of step 6, the chosen one first
HANDOFF        the filled screen brief, or the pacing JSON, or the update-plan row
READ ON        the date; the result that keeps it; the result that reverts it
NOT KNOWN      everything the numbers and the watching did not show
```

A report with no "watched" section has found a place, not a cause. Say so in its first line.

## Worked example

The file [tools/examples/stats-example.json](../tools/examples/stats-example.json) is invented: a collect-and-earn game three weeks after launch, 600 new players a day, about 900 daily users.

**Step 0.** 4,200 new players over 7 full days. Passes.

**Steps 1 and 2.** The tool names the first session: 5.1 minutes a session against a median of 9.0. The largest drop-off is "First purchase" to "Second purchase", between 0:54 and 2:00: 1,210 players, 29% of everyone who joined. That step keeps 60% while the others keep a median of 83%. Paid traffic is 55% of new players and explains 2.9 of the 5.0 points by which day 1 is under the median, so the ad spend goes to the owner as a separate decision, and the game is still 2.1 points short without it. Phones hold 27% at five minutes against 38% on computers; the Performance page shows no rise in crashes or memory exits, so the phone gap is noted for the brief, not treated as a device fix.

**Step 3.** Watched on a phone. At 0:54 the player buys the first unit for 25 cash; it earns 1 a second. The shop window closes by itself. The HUD shows 14 icons. The second unit costs 50, so it can be afforded 50 seconds later. Four of six first-time players walked around their base for 20 seconds or more and tapped the unit they already owned. Two found the shop button.

**Step 4.** A zoom funnel, read after five days on the 2,160 players who made a first purchase:

| Zoom step | Players | Kept |
|---|---|---|
| First purchase done | 2,160 | |
| Unit 2 on screen | 1,400 | 65% |
| Can afford unit 2 | 1,350 | 96% |
| Pressed buy | 1,310 | 97% |
| Owns unit 2 | 1,296 | 99% |

The drop is at Found. Players who see the second unit buy it. A third never see it.

**Step 5.** Kind: screen. The 50-second wait is under the 90 seconds the pacing tool allows in the first 15 minutes, and the zoom keeps 96% at Could, so the numbers stay as they are.

**Step 6.**

```
H1  Stat:    share of joiners who reach 'Second purchase'
    Now:     43.1%          Expect: 51% or more
    Change:  after the first purchase the shop stays open and one arrow with the words
             "Buy next" points at unit 2 until it is bought
    Kind:    screen
    Because: the zoom keeps 65% at "Unit 2 on screen" and 96% or more after it; four of six
             first-timers did not find the shop among 14 HUD icons
    Proof:   Roblox Experiment, 14 days, 50/50, new players, goal: onboarding funnel to
             'Second purchase'. The tool says +3.0 points can be proved; +8 is expected
    Guards:  day 1 retention and playtime do not fall
    Read on: day 15
    Wrong if: the rise is under 3 points
```

The game has about 900 daily users, under the 1,000 below which Roblox says an experiment may not give useful data. The step is early and its rate is near 50%, so by our arithmetic 610 players a version are enough to tell 43% from 51% (`python tools/funnel.py --size 0.43 0.51 --per-day 600`). The owner creates the experiment and reads the minimum detectable effect Roblox shows. If that is above 19% of the current rate, which is the 8 points expected, the fix goes out by route B.

**Handoff.** The change is a screen, so it goes to the UI process as a filled [screen brief](templates/screen-brief.md): the moment (0:54, first unit just bought, 0 cash, 50 seconds to the next), what happens now (window closes, 14 icons, four of six lost), the job ("at 0:54 a new player who has just bought their first unit sees the second unit and what it costs, and buys it within 60 seconds, reading no more than two words"), what may not change (prices, the loop, the art style), and the two checks.

No result is shown, because none exists. The example ends where a real one would wait 14 days.

## What single changes have done

Published results of one change at a time. Each is restated from the page linked, where the source is discussed.

| Change | Result | Source |
|---|---|---|
| Two to five thumbnails with personalisation on | Qualified play through rate +8.5% on average in Roblox's test, some games +50%; +12% across 8,000+ games, best +56% | [Thumbnails docs](https://create.roblox.com/docs/en-us/production/publishing/thumbnails); [staff post](https://devforum.roblox.com/t/5-tips-from-roblox-staff-to-get-the-most-out-of-thumbnail-personalization/3471689); [foundations/11](../foundations/11-clips-and-packaging.md) |
| 16:9 ad thumbnails in place of other shapes | Qualified play-through +57%, Roblox's estimate | [DevForum, August 2025](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159) |
| Real play in the ad image in place of icon art | Plays per click 7.9% against 0.23%, one game, one day | [DevForum](https://devforum.roblox.com/t/need-advice-on-my-games-ad-performance-and-next-steps/4760265) |
| A new title with a new thumbnail | Ad click-through 1.54% to 3.27%; unnamed speaker, two things changed at once | [transcript](https://sozai.app/transcript/roblox-sponsored-ads-explained/) |
| Managed Pricing in place of hard-coded prices | Median earnings +4%; Slap Battles over +15% | [DevForum](https://devforum.roblox.com/t/managed-pricing-one-system-for-better-pricing-and-earnings-growth/4684738) |
| Automatic translation | Qualified play through rate +0.87% on average; playtime of new Korean and Japanese speakers +4% | [DevForum](https://devforum.roblox.com/t/automatic-translation-experiment-results-and-next-steps/3878129) |
| Running ads, one shooter | Day 1 about 3% with ads against 5% to 8% without | [DevForum](https://devforum.roblox.com/t/sponsored-ads-traffic-degrades-the-engagement-metrics-used-for-discovery-causing-paid-acquisition-to-harm-organic-ranking/4838351) |
| A first-session change: a pointer, a smaller HUD, a faster first reward | Not known. No published before-and-after was found. The one public case posted no numbers after its changes | [DevForum](https://devforum.roblox.com/t/my-day-1-retention-is-awful-23-losing-half-my-players-in-under-2-minutes-what-am-i-doing-wrong-with-onboarding/4186434) |

**Our read:** the changes with published numbers are the ones Roblox can run across thousands of games. What a pointer or a shorter wait does in your game is something only your own test can tell you, which is why step 7 comes before any claim.

## Mistakes

| Symptom | Cause | Fix |
|---|---|---|
| A new HUD shipped and nothing moved | The leak was a wait, not the screen. The kind was never named | Step 4 before step 5 |
| The fix worked for two days and faded | Players reacted to the change because it was new; the test was read early | Run the full length |
| Day 1 fell after an ad push that brought more players | Paid players are in the average | Read by source before anything else |
| Three fixes shipped together and day 1 rose a point | Nobody knows which one did it, or whether any did | One kind per update |
| The report lists five fixes and no numbers | The tool and step 3 were skipped | Send it back: every hypothesis needs now, expect and proof |
| 14 days, and the experiment shows no clear change | The expected rise was under the minimum detectable effect | Check it before starting; test bigger changes |
| The funnel changed shape the week a step was added | The range crosses the day the steps changed | Read from the day of the change |
| The agent redesigned three screens | The brief did not say what may not change | Fill section 7 of the screen brief |

## Sources

Roblox Creator Docs read on 25 November 2026: [Analytics dashboard](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard), [Engagement](https://create.roblox.com/docs/en-us/production/analytics/engagement), [Funnel events](https://create.roblox.com/docs/en-us/production/analytics/funnel-events), [Experience configs](https://create.roblox.com/docs/en-us/production/configs) and [Experiments](https://create.roblox.com/docs/en-us/production/experiments). The published results are restated from [foundations/11](../foundations/11-clips-and-packaging.md), [12](../foundations/12-monetization.md) and [14](../foundations/14-metrics-and-diagnosis.md). The zoom funnel, the seven kinds, the pointing test, "half the gap" and the worked example are our own; the example's numbers are invented. The sample-size arithmetic is the two-proportion formula in [tools/funnel.py](../tools/funnel.py), at 95% confidence, catching a real change 4 times in 5.
