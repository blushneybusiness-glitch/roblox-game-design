#!/usr/bin/env python3
"""Pacing check for a buy-units-that-earn economy.

Give it a price ladder and it plays the ladder the way a sensible player
would, then tells you when things happen: the first purchase, the longest
wait between purchases, the first reset, and when the ladder runs out.

    python tools/pacing.py tools/examples/start-with-ladder.json
    python tools/pacing.py my-game.json --minutes 600 --events 80

Python 3.8 or newer. No packages needed.

The player is idealised: they never idle and always buy the best-value thing
on offer. Real players are slower, so read every time as a lower bound.

A unit is always in stock unless it has "every_s": then it is offered once
per interval of that many seconds (a rare unit on a restock clock or a
conveyor with a guarantee). That is how these games stretch a short ladder.

See foundations/06-progression-and-economy.md for how to use the numbers.
"""

import argparse
import json
import sys

DEFAULTS = {
    "start_cash": 0,
    "slots": None,              # how many units can be held; None = no limit
    "sell_back": 0.5,           # share of the price returned when a unit is replaced
    "active_income": 0.0,       # cash per second from the player's own actions
    "income_multiplier": 1.0,   # e.g. the average uplift from a mutation table
    "first_action_s": 8,        # seconds before a new player makes the first purchase
    "seconds_per_purchase": 3,  # walking and tapping time per purchase
    "gate_patience_s": 180,     # the player saves for a reset once it is this close
}


def fmt_time(seconds):
    seconds = int(round(seconds))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return "%d:%02d:%02d" % (h, m, s) if h else "%d:%02d" % (m, s)


def fmt_num(x):
    for limit, suffix in ((1e15, "Qa"), (1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(x) >= limit:
            return ("%.2f" % (x / limit)).rstrip("0").rstrip(".") + suffix
    return ("%.1f" % x).rstrip("0").rstrip(".")


def load(path):
    with open(path, encoding="utf-8") as fh:
        cfg = json.load(fh)
    for key, value in DEFAULTS.items():
        cfg.setdefault(key, value)
    units = cfg.get("units") or []
    if not units:
        sys.exit("The file needs a 'units' list: [{\"name\": ..., \"price\": ..., \"income\": ...}, ...]")
    for u in units:
        if u.get("price", 0) <= 0 or u.get("income", 0) <= 0:
            sys.exit("Unit %r needs a price and an income above zero." % u.get("name"))
    cfg["units"] = sorted(units, key=lambda u: u["price"])
    cfg.setdefault("gates", [])
    cfg.setdefault("targets", {})
    return cfg


def simulate(cfg, max_seconds):
    units = cfg["units"]
    by_name = {u["name"]: u for u in units}
    slots = cfg["slots"]
    gates = list(cfg["gates"])
    multiplier = float(cfg["income_multiplier"])

    cash = float(cfg["start_cash"])
    owned = []                      # names of units held
    t = float(cfg["first_action_s"])
    events = []                     # (time, kind, label, cost, income_after)
    first_buy = {}                  # unit name -> time first bought
    gate_times = {}
    exhausted_at = None

    def base_income():
        return sum(by_name[n]["income"] for n in owned)

    def income():
        return base_income() * multiplier + float(cfg["active_income"])

    last_tick = {}                  # unit name -> index of the stock tick it was last bought in

    def advance(seconds):
        """Let `seconds` pass, earning income."""
        nonlocal t, cash
        if seconds > 0:
            cash += income() * seconds
            t += seconds

    def wait_for(cost):
        """Advance time until `cost` is affordable. Returns False if it never is."""
        if cash >= cost:
            return True
        rate = income()
        if rate <= 0:
            return False
        advance((cost - cash) / rate + 1e-9)
        return True

    def stock_wait(u):
        """Seconds until unit `u` is next on offer. Units without 'every_s' are always in stock.

        A unit with 'every_s' is offered once per interval of that length, and not
        during the first interval, which models a shop that guarantees it "within"
        that time.
        """
        every = u.get("every_s")
        if not every:
            return 0.0
        tick = int(t // every)
        if last_tick.get(u["name"], 0) >= tick:
            return (last_tick.get(u["name"], 0) + 1) * every - t
        return 0.0

    while t < max_seconds:
        rate = income()

        # Is the next reset close enough to save for?
        if gates:
            gate = gates[0]
            missing = [n for n in gate.get("requires", []) if n not in owned]
            unknown = [n for n in missing if n not in by_name]
            if unknown:
                sys.exit("Gate %r requires %r, which is not in the units list." % (gate["name"], unknown[0]))
            total = gate["cash"] + sum(by_name[n]["price"] for n in missing)
            if rate > 0 and (total - cash) / rate <= cfg["gate_patience_s"]:
                if not wait_for(total):
                    break
                for n in missing:
                    cash -= by_name[n]["price"]
                    first_buy.setdefault(n, t)
                    if slots is not None and len(owned) >= slots:
                        weakest = min(owned, key=lambda o: by_name[o]["income"])
                        owned.remove(weakest)
                    owned.append(n)
                if gate.get("consumes_required", True):
                    for n in gate.get("requires", []):
                        if n in owned:
                            owned.remove(n)
                cash = float(gate.get("cash_after", 0))
                multiplier = float(gate.get("income_multiplier_after", multiplier))
                if slots is not None:
                    slots += int(gate.get("slots_add", 0))
                gate_times[gate["name"]] = t
                events.append((t, "reset", gate["name"], total, income()))
                gates.pop(0)
                t += cfg["seconds_per_purchase"]
                continue

        # Otherwise pick the purchase that pays back soonest, counting the wait.
        best = None
        for u in units:
            if slots is None or len(owned) < slots:
                delta = u["income"] * multiplier
                cost = u["price"]
                replaced = None
            else:
                weakest = min(owned, key=lambda o: by_name[o]["income"])
                delta = (u["income"] - by_name[weakest]["income"]) * multiplier
                cost = u["price"] - cfg["sell_back"] * by_name[weakest]["price"]
                replaced = weakest
            if delta <= 0:
                continue
            if rate <= 0 and cost > cash:
                continue
            wait = max(0.0, cost - cash) / rate if rate > 0 else 0.0
            wait = max(wait, stock_wait(u))
            score = wait + cost / delta
            if best is None or score < best[0]:
                best = (score, u, cost, replaced, wait)

        if best is None:
            if gates and rate > 0:
                # Nothing left to buy: save for the reset however long it takes.
                gate = gates[0]
                cfg["gate_patience_s"] = float("inf")
                if exhausted_at is None:
                    exhausted_at = t
                continue
            exhausted_at = t if exhausted_at is None else exhausted_at
            break

        _, u, cost, replaced, wait = best
        advance(wait)
        if not wait_for(cost):
            break
        if t >= max_seconds:
            break
        cash -= cost
        if replaced is not None:
            owned.remove(replaced)
        owned.append(u["name"])
        if u.get("every_s"):
            last_tick[u["name"]] = int(t // u["every_s"])
        first_buy.setdefault(u["name"], t)
        events.append((t, "buy", u["name"], cost, income()))
        t += cfg["seconds_per_purchase"]

    return {
        "events": events,
        "first_buy": first_buy,
        "gate_times": gate_times,
        "exhausted_at": exhausted_at,
        "end_time": min(t, max_seconds),
    }


def longest_gap(events, start, end):
    """Longest stretch without a purchase or reset between `start` and `end` seconds."""
    times = [start] + [e[0] for e in events if start <= e[0] <= end] + [end]
    gaps = [(b - a, a) for a, b in zip(times, times[1:])]
    return max(gaps) if gaps else (0, start)


def report(cfg, result, max_events):
    events = result["events"]
    out = []
    out.append("Pacing check: %s" % cfg.get("name", "unnamed"))
    out.append("Idealised player: never idle, always buys the best value on offer. Real players are slower.")
    out.append("")

    out.append("First %d events" % min(max_events, len(events)))
    out.append("%-9s %-6s %-28s %12s %14s" % ("time", "", "what", "cost", "income/s after"))
    for when, kind, label, cost, rate in events[:max_events]:
        out.append("%-9s %-6s %-28s %12s %14s" % (fmt_time(when), kind, label[:28], fmt_num(cost), fmt_num(rate)))
    if len(events) > max_events:
        out.append("... %d more" % (len(events) - max_events))
    out.append("")

    out.append("First purchase of each unit")
    for u in cfg["units"]:
        when = result["first_buy"].get(u["name"])
        payback = u["price"] / float(u["income"])
        out.append("  %-28s payback %5.0f s   first bought %s" % (
            u["name"][:28], payback, fmt_time(when) if when is not None else "never"))
    out.append("")

    buys = [e for e in events if e[1] == "buy"]
    first = buys[0][0] if buys else None
    gap15, at15 = longest_gap(events, cfg["first_action_s"], 900)
    gap60, at60 = longest_gap(events, 900, 3600)
    out.append("Summary")
    out.append("  First purchase:                      %s" % (fmt_time(first) if first is not None else "never"))
    out.append("  Purchases in the first 5 / 15 / 60 min: %d / %d / %d" % (
        sum(1 for e in buys if e[0] <= 300), sum(1 for e in buys if e[0] <= 900), sum(1 for e in buys if e[0] <= 3600)))
    out.append("  Longest wait, first 15 min:          %s (starting at %s)" % (fmt_time(gap15), fmt_time(at15)))
    out.append("  Longest wait, minute 15 to 60:       %s (starting at %s)" % (fmt_time(gap60), fmt_time(at60)))
    for name, when in result["gate_times"].items():
        out.append("  %-36s %s" % (name + ":", fmt_time(when)))
    if result["exhausted_at"] is not None:
        out.append("  Nothing left to buy from:            %s" % fmt_time(result["exhausted_at"]))
    else:
        out.append("  Nothing left to buy from:            not reached in %s" % fmt_time(result["end_time"]))
    out.append("")

    targets = cfg["targets"]
    if targets:
        out.append("Checks")
        failed = 0

        def check(label, ok, detail):
            nonlocal failed
            failed += 0 if ok else 1
            out.append("  %-4s %s (%s)" % ("PASS" if ok else "FAIL", label, detail))

        if "first_purchase_s" in targets:
            limit = targets["first_purchase_s"]
            check("first purchase within %d s" % limit, first is not None and first <= limit,
                  "at %s" % (fmt_time(first) if first is not None else "never"))
        if "max_gap_first_15min_s" in targets:
            limit = targets["max_gap_first_15min_s"]
            check("no wait over %d s in the first 15 min" % limit, gap15 <= limit, "longest %s" % fmt_time(gap15))
        if "max_gap_15_to_60min_s" in targets:
            limit = targets["max_gap_15_to_60min_s"]
            check("no wait over %d s from minute 15 to 60" % limit, gap60 <= limit, "longest %s" % fmt_time(gap60))
        if "first_gate_minutes" in targets and cfg["gates"]:
            low, high = targets["first_gate_minutes"]
            name = cfg["gates"][0]["name"]
            when = result["gate_times"].get(name)
            check("%s between %d and %d min" % (name, low, high),
                  when is not None and low * 60 <= when <= high * 60,
                  "at %s" % (fmt_time(when) if when is not None else "not reached"))
        if "ladder_min_hours" in targets:
            limit = targets["ladder_min_hours"]
            done = result["exhausted_at"]
            check("ladder lasts at least %s h" % limit, done is None or done >= limit * 3600,
                  "runs out at %s" % fmt_time(done) if done is not None else "not exhausted in the run")
        if "max_payback_s" in targets:
            limit = targets["max_payback_s"]
            worst = max(cfg["units"], key=lambda u: u["price"] / float(u["income"]))
            pb = worst["price"] / float(worst["income"])
            check("no unit pays back slower than %d s" % limit, pb <= limit, "%s: %.0f s" % (worst["name"], pb))
        out.append("")
        out.append("%d check(s) failed." % failed if failed else "All checks passed.")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="Pacing check for a buy-units-that-earn economy.")
    parser.add_argument("config", help="path to a JSON file; see tools/examples/")
    parser.add_argument("--minutes", type=float, default=300, help="how long to simulate (default 300)")
    parser.add_argument("--events", type=int, default=40, help="how many events to print (default 40)")
    args = parser.parse_args()
    cfg = load(args.config)
    result = simulate(cfg, args.minutes * 60)
    print(report(cfg, result, args.events))


if __name__ == "__main__":
    main()
