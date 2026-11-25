# Template: first-session script

Write what a brand-new player does, sees and hears, second by second, from the moment they have control until minute 15. The script is the design of the first session. If a line cannot be written, the first session is not designed yet.

Explained in [foundations/05-first-session.md](../../foundations/05-first-session.md). Gate values for each genre are in that page and in the genre playbooks.

Assume the hardest case: a 10-year-old on a phone, sound on, who has never played this genre, will not read more than three words at a time, and joined alone.

## Script

| Time | Player does | On screen | Sound | Why it is here |
|---|---|---|---|---|
| 0:00 | Gains control | | | |
| 0:05 | | | | First input |
| 0:10 | | | | First reward |
| 0:30 | | | | The title's promise has happened |
| 0:45 | | | | First purchase or upgrade |
| 1:00 | | | | |
| 2:00 | | | | First rare or surprising moment |
| 3:00 | | | | First moment involving another player |
| 5:00 | | | | Long goal is on screen |
| 10:00 | | | | Second system opens |
| 15:00 | | | | The player has a reason to return |

Add rows wherever more than 20 seconds pass without one.

## Gates

| Gate | Target | Scripted | Measured in the build |
|---|---|---|---|
| Seconds from control to first input | | | |
| Seconds to first reward | | | |
| Seconds until the title's promise has happened | | | |
| Seconds to first purchase or upgrade | | | |
| Minutes to first rare or surprising moment | | | |
| Minutes to first moment involving another player | | | |
| Minutes until a long goal is on screen | | | |
| Words of text the player must read to get this far | | | |
| Windows that open by themselves | 0 | | |
| Purchase offers shown | 0 | | |

## Checks on the script

- [ ] The player does the core verb before anything explains it.
- [ ] Nothing in the first minute can fail. The first attempts are rigged to succeed.
- [ ] One new thing is taught at a time, by doing it.
- [ ] Each step is taught by a pointer, an arrow or a highlighted object. Not by a paragraph.
- [ ] The first reward is not the worst tier.
- [ ] A system appears on the HUD only when the player first needs it.
- [ ] By minute 5 the player has seen something they want and cannot yet afford.
- [ ] By minute 5 the player has seen what another player has.
- [ ] The script has been timed in the build, on a phone, by someone who did not write it.

## Funnel events

Log one event for each row above, numbered in the order players do the steps, so the dashboard shows where players leave. Roblox counts a skipped step as done, so a step added later takes the number of its place and the steps after it move up; read the funnel from the day of that change ([foundations/14-metrics-and-diagnosis.md](../../foundations/14-metrics-and-diagnosis.md)). Name the events here before building.

| Step | Event name | Row it marks |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
