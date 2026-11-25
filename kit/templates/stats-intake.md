# Template: stats intake

Fill this each time you look at a live game's numbers, then hand it to whoever will diagnose the game: a person, or an AI agent following [AGENTS.md](../../AGENTS.md). It lists the numbers a diagnosis needs, where each one lives in Roblox's Creator Hub, and the file that [tools/funnel.py](../../tools/funnel.py) reads.

What to do with the filled page is in [kit/stats-to-plan.md](../stats-to-plan.md). What each stage means is in [foundations/14-metrics-and-diagnosis.md](../../foundations/14-metrics-and-diagnosis.md).

These are totals. Do not paste player names or user ids into an intake.

## Before you copy a number

The dashboard facts on this page are from Roblox's Creator Docs as read on 25 November 2026.

1. **Pick 7 full days**, Monday to Sunday, or 14, or 28. Every number on this page comes from the same range. Traffic peaks on Saturdays, so the range has to hold each weekday the same number of times.
2. **End the range early enough.** Retention is plotted by the day a player first joined: day 7 for a join date appears 7 days later and day 30 appears 30 days later ([Retention docs](https://create.roblox.com/docs/en-us/production/analytics/retention)). End the range at least 2 days ago for day 1, 8 for day 7, 31 for day 30.
3. **Write down what happened inside the range:** an update, the start or end of an ad campaign, an event, a creator's video. If an update shipped inside it, use only the days after.
4. **Turn filters off, then on.** A filter set with Filter By stays on for every chart on every analytics page until you turn it off ([Analytics dashboard docs](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)). Read the totals with no filter. Then read the splits.
5. **Use the figure for the whole range,** the summary above each chart, never one day. The Export button on a chart saves its dates and values as a CSV file (same page).
6. **No dashboard yet?** All the charts need more than 10 daily users and 10 play hours for 7 days in a row. The benchmark band compares you with games that have at least 100 daily users (same page). Below that, go to "The least you need" at the end.

## 1. The game

| | |
|---|---|
| Game and genre | |
| The live game it is closest to | |
| Launch date | |
| Date range of these numbers | |
| New players per day, average over the range | |
| Daily users | |
| What happened inside the range | |
| The number you most want to move | |

## 2. One number for each stage

In Creator Hub, open the game. The pages are in the left menu.

| Stage | Number | Page | Yours | Band, 50th | Band, 90th |
|---|---|---|---|---|---|
| Seen | New users with impressions | Analytics, Acquisition | | none shown | none shown |
| Clicked | Play through rate | Analytics, Acquisition | | | |
| First session | Average session time, minutes | Analytics, Engagement | | | |
| Next day | Day 1 retention | Analytics, Retention | | | |
| Days 2 to 7 | Day 7 retention | Analytics, Retention | | | |
| Days 8 to 28 | Day 30 retention | Analytics, Retention | | | |
| Pays | Conversion rate: the share of daily users who paid | Monetization, Overview | | | |
| Pays | ARPPU and ARPDAU | Monetization, Overview | | | |

The band is the range drawn on those charts for games with similar players, from the 50th to the 90th percentile. Roblox draws it for every retention number, average session time, play through rate, conversion rate, ARPPU and ARPDAU. A newer game may get a genre band or an all-experiences band; write which one you see ([Analytics dashboard docs](https://create.roblox.com/docs/en-us/production/analytics/analytics-dashboard)).

## 3. The first-session curve

Analytics, Engagement, the chart named New User First Session Retention. It shows the share of new players still playing a given number of minutes after their first join, with the previous period next to the current one ([Engagement docs](https://create.roblox.com/docs/en-us/production/analytics/engagement)). Copy the minutes your chart shows.

| Minute | 0:30 | 1:00 | 2:00 | 3:00 | 5:00 | 10:00 | 15:00 |
|---|---|---|---|---|---|---|---|
| Still playing, this period | | | | | | | |
| Still playing, previous period | | | | | | | |

## 4. The step funnel

Analytics, Funnel. The page appears once the game logs funnel events, and holds up to ten funnels ([Funnel docs](https://create.roblox.com/docs/en-us/production/analytics/funnel-events)). Copy the onboarding funnel, one row per step, in order.

| Step | Name | Minute a player reaches it | Players |
|---|---|---|---|
| 1 | Joined | 0:00 | |
| 2 | | | |
| 3 | | | |

- The minute comes from the "Measured in the build" column of your [first-session script](first-session-script.md), or from a stopwatch run.
- The funnel counts players by the day they entered it, and a filter looks only at what a player was at their first step (same page).
- If a step was added, moved or renamed inside the range, use only the days after. The dashboard puts a warning on that step.
- No funnel yet: that is the first job. See "Instrumenting" in [foundations/14-metrics-and-diagnosis.md](../../foundations/14-metrics-and-diagnosis.md).

## 5. Two splits

Read the same numbers again with Filter By set, one value at a time. A filter that a chart cannot use is greyed out; write "not available".

**By traffic source.** Filter By, Source. Roblox's sources are Home recommendations, Continue play, Today's Picks, Home other, Friends, Search, Charts, Sponsored ads, Search ads, Portal ads, Teleport and Other ([Acquisition docs](https://create.roblox.com/docs/en-us/production/analytics/acquisition)). Keep the three or four largest and add the rest together.

| Source | Share of new players | Still playing at 5:00 | Day 1 retention | Paid for? |
|---|---|---|---|---|
| | | | | |
| | | | | |

The new-users table on the Acquisition page also gives, for each source: users with plays, conversion from impression to play, day 7 retention, playtime per user over 7 days, and payer conversion and revenue per user over 30 days (same page). Copy its day 7 column if day 1 by source is greyed out.

**By device.** Filter By, Platform: computer, phone, tablet, console, VR. Use OS as well to set Android against iOS.

| Device | Share of new players | Still playing at 5:00 | Day 1 retention |
|---|---|---|---|
| Phone | | | |
| Computer | | | |
| Tablet and console | | | |

## 6. Money

- Conversion rate, paying users per day, ARPPU and ARPDAU for the range (Monetization, Overview; [Monetization docs](https://create.roblox.com/docs/en-us/production/analytics/monetization)).
- The five items that earned the most Robux in the range: name, pass or product, price, number sold.
- The shop funnel, if one is logged: opened the shop, looked at an item, saw the purchase prompt, bought.
- The minute of the first session at which the first offer appears.

## 7. The in-game economy

Only if the game logs economy events. Analytics, Economy ([Economy docs](https://create.roblox.com/docs/en-us/production/analytics/economy-events)):

- Total sources minus total sinks of the main currency over the range. Roblox says this should be close to zero.
- Average wallet balance of all players, of payers and of non-payers, at the start and at the end of the range.
- The three largest sources and the three largest sinks.

## 8. Milestones

The share of everyone who joined that reaches the first milestone a player would name: the first rebirth, the first boss, level 10. Take it from your funnel, or from badges. Roblox's public badge endpoint gives how many players ever earned each badge; the address and its four limits are in [foundations/14-metrics-and-diagnosis.md](../../foundations/14-metrics-and-diagnosis.md).

| Milestone | Players who reached it | Share of everyone who joined |
|---|---|---|
| | | |

## 9. Performance

Fill this when phones lose players faster than computers. Monitoring, Performance, Client tab, broken down by platform or OS. The charts need 100 daily users ([Performance docs](https://create.roblox.com/docs/en-us/production/analytics/performance)).

| Device | Client frame rate | Client crash rate | Unexpected out-of-memory exits | Client memory usage percentage |
|---|---|---|---|---|
| Android | | | | |
| iOS | | | | |
| Windows | | | | |

The same page can break every client chart down by place version, which shows whether the last update made things worse.

## 10. What the game does at those moments

Numbers say where players leave. The game says why. Attach:

- The [first-session script](first-session-script.md) with its "Measured in the build" column filled, or a screen recording of a new player's first five minutes on a phone.
- The number of items on the HUD at rest at 0:10, at 1:00 and at 5:00.
- The words a player must read in the first five minutes.
- Every window that opens by itself, and every offer shown, in the first five minutes.
- The [economy sheet](economy-sheet.md), or the JSON written for `tools/pacing.py`.

## The file for the tool

Copy the numbers into a JSON file in this shape. Leave out what you do not have.

```json
{
  "name": "My game, 10 to 16 November 2026",
  "days": 7,
  "new_players_per_day": 600,

  "first_session": {"0.5": 0.91, "1": 0.74, "2": 0.52, "3": 0.41, "5": 0.30, "10": 0.14},
  "first_session_previous": {"1": 0.75, "5": 0.31},

  "funnel": [
    {"step": "Joined", "users": 4200, "minute": 0},
    {"step": "First reward", "users": 3650, "minute": 0.4},
    {"step": "First purchase", "users": 3020, "minute": 0.9}
  ],
  "first_milestone_share": 0.06,

  "metrics": {
    "play_through_rate": {"value": 0.071, "p50": 0.062, "p90": 0.11},
    "session_minutes": {"value": 5.1, "p50": 9.0, "p90": 14.0},
    "d1": {"value": 0.055, "p50": 0.105, "p90": 0.17},
    "d7": {"value": 0.009, "p50": 0.018, "p90": 0.05},
    "d30": {"value": null},
    "conversion": {"value": 0.006, "p50": 0.011, "p90": 0.03}
  },

  "by_source": [
    {"name": "Home recommendations", "share": 0.35, "at_5min": 0.36, "d1": 0.081},
    {"name": "Sponsored ads", "share": 0.55, "paid": true, "at_5min": 0.24, "d1": 0.031},
    {"name": "Search", "share": 0.10, "at_5min": 0.41, "d1": 0.094}
  ],
  "by_device": [
    {"name": "Phone", "share": 0.72, "at_5min": 0.27, "d1": 0.050},
    {"name": "Computer", "share": 0.22, "at_5min": 0.38, "d1": 0.070},
    {"name": "Tablet and console", "share": 0.06, "at_5min": 0.34, "d1": 0.058}
  ]
}
```

- A share is a fraction (0.74) or a percent above 1 (74). The tool warns when a number looks mistyped.
- A minute is a number: 0.5 is thirty seconds.
- `p50` and `p90` are the two ends of the band from section 2. Without them the tool compares session time and retention with the medians of large games in [foundations/14](../../foundations/14-metrics-and-diagnosis.md).
- A source whose name contains "Sponsored" or ends in "ads" is counted as paid. Set `"paid"` yourself to override.
- A split row can also carry `at_1min` and `d7`.

A complete example with invented numbers is in [tools/examples/stats-example.json](../../tools/examples/stats-example.json).

```
python tools/funnel.py my-stats.json
```

## The least you need

Five numbers: new players per day, the share still playing at 1:00 and at 5:00, average session time, and day 1 retention, with the band where the dashboard draws one. That is enough to name the weak stage. It is not enough to name a step, so the first change it leads to is usually the funnel events.

## If something is missing

| Missing | Do this first |
|---|---|
| The whole dashboard | It opens after 7 days in a row with more than 10 daily users. Until then, watch six first-time players with a stopwatch ([foundations/05-first-session.md](../../foundations/05-first-session.md)) |
| The step funnel | Log one onboarding funnel event per row of the first-session script, wait 7 days |
| The bands | Under 100 daily users there may be none. The tool falls back to large-game medians and says so |
| The split by source | Check the filter is not greyed out. Use the new-users table on the Acquisition page |
| 1,000 new players in the range | Use 14 or 28 days. Under 1,000, only gaps of 3 points or more can be trusted |
