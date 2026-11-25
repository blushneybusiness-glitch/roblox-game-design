# Template: economy sheet

Fill this before building any shop, ladder or rebirth. Then copy the numbers into a JSON file and run `python tools/pacing.py` on it. The tool plays the ladder like an ideal player and tells you when things happen.

Explained in [foundations/06-progression-and-economy.md](../../foundations/06-progression-and-economy.md). A filled example is `tools/examples/start-with-ladder.json`, and a real hit's ladder is `tools/examples/steal-a-brainrot-observed.json`.

## 1. Starting state

| | Value | Reasoning |
|---|---|---|
| Starting cash | | Enough for the first purchase and nothing more |
| Slots (how many earning things can be held) | | |
| Sell-back (share of price returned when replaced) | | |
| Income from the player's own actions, per second | | Zero if only owned things earn |

## 2. The ladder

Decide income and payback. Price is income x payback.

| # | Name | Tier | Income per second | Payback (s) | Price | On offer |
|---|---|---|---|---|---|---|
| 1 | | | | | | always |
| 2 | | | | | | |
| 3 | | | | | | |

- Payback of the first row: 20 to 30 seconds.
- Payback grows 10% to 15% per row and stays under 300 seconds.
- Income multiplies by 2 to 4 per row.
- "On offer" is "always", or "once every N seconds" for rare tiers. That column sets the pace after the first quarter of an hour.

## 3. The second roll

| Result | Chance | Multiplier |
|---|---|---|
| Normal | | x1 |
| | | |

Average multiplier (sum of chance x multiplier): ______. This goes in the tool as `income_multiplier`.

## 4. Resets

| Reset | Cash | Named things required | Income multiplier after | Slots added | Also gives |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

## 5. Where currency comes from and where it goes

| Source | Amount | How often |
|---|---|---|
| | | |

| Sink | Amount | How often |
|---|---|---|
| | | |

If the sources add up to more than the sinks every hour, prices will stop meaning anything within a week. Name the sink that grows with the player.

## 6. Away from the game

| | Value |
|---|---|
| Income while offline, as a share of online income | |
| Cap, in hours of earnings | |
| Timers that keep running offline | |

## 7. Run the check

Copy the sheet into JSON:

```json
{
  "name": "My game",
  "start_cash": 25,
  "slots": 10,
  "sell_back": 0.5,
  "income_multiplier": 1.385,
  "units": [
    {"name": "Unit 1", "price": 25, "income": 1},
    {"name": "Unit 9", "price": 155000, "income": 1000, "every_s": 300}
  ],
  "gates": [
    {"name": "Rebirth 1", "cash": 2000000, "requires": ["Unit 5", "Unit 6"],
     "income_multiplier_after": 2.08, "slots_add": 0}
  ],
  "targets": {
    "first_purchase_s": 15,
    "max_gap_first_15min_s": 90,
    "first_gate_minutes": [20, 40],
    "ladder_min_hours": 3,
    "max_payback_s": 300
  }
}
```

```
python tools/pacing.py my-game.json
```

Read four things in the output:

| Line | Pass when | If it fails |
|---|---|---|
| First purchase | Within 15 seconds | Raise starting cash or lower the first price |
| Longest wait, first 15 minutes | Under 90 seconds | Find the unit bought just after the wait. Its price is too far above the one before. Insert a unit between them or lower it |
| First reset | Between 20 and 40 minutes | Change its cash requirement |
| Nothing left to buy from | Not before 3 hours | Add tiers at the top, or put the top tiers on a slower stock clock |

The tool's player never idles and always buys the best value on offer. Real players are slower. Treat every time as the fastest possible, and expect real first sessions to run one and a half to three times as long.

## 8. After launch

Replace the tool's guesses with what happened: log a funnel event at each first purchase of each tier and at each reset, and compare the real minutes with the sheet. Change the sheet, run the tool, then change the game.
