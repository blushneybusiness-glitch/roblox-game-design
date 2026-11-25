# Template: screen brief

One page that hands one diagnosed screen to whoever designs the UI: a person, or a design process run by an AI agent such as [Drip](https://github.com/8bitgfx/drip). Fill it when [kit/stats-to-plan.md](../stats-to-plan.md) ends in a fix of the kind "screen". For any other kind of fix this is the wrong document.

A designer told "make the shop better" returns a better-looking shop. This brief gives them the moment, the player, the one job the screen has, what may not change, and the number that decides whether it worked.

One brief covers one state of one screen. Two screens are two briefs and two updates.

## 1. Why this screen

| | |
|---|---|
| Stat to move | |
| Now | |
| Expect | |
| How it will be read: split or before against after, days, players per version | |
| Guard stats that must not fall | |
| Config key that switches between the old screen and the new one | |

Copy these from the chosen hypothesis ([kit/stats-to-plan.md](../stats-to-plan.md), step 6).

## 2. The moment

| | |
|---|---|
| Time in the first-session script, or the funnel step | |
| What the player has just done | |
| What the player holds: cash, items, level | |
| What the player should do next | |
| Seconds they have before the gate is missed | |
| Device most of them are on | |

About 65% of a typical game's players are on Android, and about 60% of those phones have 2 to 4 GB of memory ([foundations/02-the-platform.md](../../foundations/02-the-platform.md)). Roblox runs in landscape on phones unless the game changes it ([Mobile input docs](https://create.roblox.com/docs/en-us/input/mobile)).

## 3. What happens now

Evidence, not opinion. Leave a line empty before you guess it.

- Screenshot or recording of this moment on a phone:
- Items on the HUD at rest, counted and listed:
- Words on screen:
- Windows that open by themselves:
- What first-time players did: how many were watched, what they tapped first, how many seconds they stalled:
- The zoom funnel: found, could, tried, done:

## 4. The job, in one sentence

`At [time], a new player who has [state] does [action] within [seconds], reading no more than [number] words.`

If the sentence needs an "and", it is two jobs. Pick the one the stat depends on.

## 5. The reference

| | |
|---|---|
| The live game whose version of this moment works | |
| Screenshot of it at the same moment | |
| What to copy from it | |
| The one thing to do differently, and why | |

The handbook's first rule holds for a screen too: start from one live game's version of it and change one thing ([AGENTS.md](../../AGENTS.md), rule 1).

## 6. Rules the screen must keep

| Rule | Value | From |
|---|---|---|
| Items on the HUD at rest | Six or fewer in the first minute. A button appears the first time the player needs it | [foundations/05](../../foundations/05-first-session.md), rule 10 |
| Pointers | One at a time, three words or fewer | [foundations/05](../../foundations/05-first-session.md), rule 5 |
| Words read in the first five minutes, all screens together | 10 to 15, by genre | [foundations/05](../../foundations/05-first-session.md), gates |
| Windows that open by themselves, and offers | None in the first five minutes. Never a purchase window at a moment of loss | [foundations/05](../../foundations/05-first-session.md), rule 9; [foundations/15](../../foundations/15-the-line.md) |
| The long goal | On screen by minute 5, as a picture and a number | [foundations/05](../../foundations/05-first-session.md), rule 7 |
| Answer to a tap | A sound and a visible reaction start within 0.1 s. A tap that fails says why in three words or fewer | [foundations/10](../../foundations/10-feel-and-feedback.md) |
| Corners to keep clear on a phone | Bottom left and bottom right hold Roblox's thumbstick and jump button. The top bar holds Roblox's own buttons | [Position and size docs](https://create.roblox.com/docs/en-us/ui/position-and-size); [On-screen containers docs](https://create.roblox.com/docs/en-us/ui/on-screen-containers) |
| Reach | Controls used in the loop sit within reach of the right thumb, placed relative to the jump button. A button 40% down from the top edge can be reached on a phone and barely on a tablet | [Position and size docs](https://create.roblox.com/docs/en-us/ui/position-and-size); [slop/03](../../slop/03-quality-bar.md) |
| Safe area | Interactive UI stays inside Roblox's default core UI safe area, clear of the top bar and the camera cut-out | [On-screen containers docs](https://create.roblox.com/docs/en-us/ui/on-screen-containers) |
| Sizing | Position and size by scale with a text size limit, so the screen holds on phone, tablet, computer and console | [Cross-platform docs](https://create.roblox.com/docs/en-us/projects/cross-platform) |
| Truth | Every price, timer and chance on the screen matches the server | [foundations/15](../../foundations/15-the-line.md) |

**Start with:** buttons of 48 pixels or more on a phone, the value in [slop/03-quality-bar.md](../../slop/03-quality-bar.md). Google's guidance for Android apps is 48 dp, about 9 mm, with 8 dp between targets ([Android Accessibility Help](https://support.google.com/accessibility/android/answer/7101858)). That figure is for Android apps, not for Roblox, and whether a Roblox pixel equals a dp on every phone is not known. Check on a real phone that a thumb hits the button.

## 7. What may not change

- [ ] The rules of the game and the loop.
- [ ] Prices, incomes, timers and odds. Those are a "numbers" fix and ship on their own.
- [ ] Any other screen.
- [ ] The game's art style, fonts and colours.

A designer who believes one of these is the real problem says so and stops. They do not fix it inside this brief. An update that changes two things cannot be read.

## 8. What comes back

- The screen at phone size in landscape, in each state: at rest, pressed, cannot afford, done, and before the player has unlocked it.
- The same screen on a tablet, a computer and a console, with the order a gamepad moves through it.
- Every string on the screen, with the word count.
- The motion and the sound for the main action, with their times in seconds.
- A list of what was taken off the screen.
- The build behind the config key from section 1, with the old screen untouched.

## 9. Done when

Both checks are written before the work starts.

1. **The watch test.** **Start with:** 5 of 6 first-time players on a phone do [the action in section 4] within [its seconds], with nobody speaking.
2. **The live read.** The stat in section 1 reaches the expected number on the read date, and no guard stat falls by more than the noise.

If check 1 fails, the screen does not ship. If check 1 passes and check 2 fails, the cause was not the screen: go back to step 4 of [kit/stats-to-plan.md](../stats-to-plan.md).

## Handing it to Drip

[Drip](https://github.com/8bitgfx/drip) is a public plugin that makes a coding agent work through a design process: it studies references, proposes directions, builds, and has a separate critic review the result. It starts from a short brief. Fill that brief from this page so it has nothing to ask. Field names are those of Drip 0.7, November 2026.

| Drip's field | Take it from |
|---|---|
| `what` | "One state of one Roblox screen:" and its name, with the two funnel steps it sits between (section 2) |
| `audience` | Section 2: new players, the device, landscape, how many words they will read |
| `job` | The sentence of section 4, then "moves [stat] from [now] to [expect]" from section 1 |
| `feel` | Two or three words for the style the game already has |
| `loves` | The reference of section 5 and what to copy from it |
| `hates` | What section 3 found, in the game's own numbers: "14 icons at rest", "a window that opens by itself" |
| `constraints` | Sections 6, 7 and 8 in full, and "a Roblox ScreenGui, landscape phone first, not a web page" |
| `redesign` | `keep-brand` |

Three things to say in words, because Drip's defaults are for web pages:

1. **Keep the game's style.** Drip extends a project's approved design by default. Leave that on. A new art direction is a second change in the same update.
2. **Give it the frame.** Drip checks a page at 1,440 and 390 pixels wide. A Roblox phone screen is landscape. Give it the phone size from Studio's device emulation and ask for the check at that size.
3. **The stat outranks the critic.** Drip's critic judges how the screen looks and reads. Section 9 judges whether players do the thing. A screen has to pass both, and when they disagree section 9 wins.

If you have adapted Drip to Roblox UI with its adapt command, name that pack when you start the task.

Any other designer or tool: sections 1 to 9 are the whole brief.
