#!/usr/bin/env python3
"""sc13_chess_clock.py: spark SC13 (SPARKS.md). The chess clock as an account.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    <decompressor of a Lichess monthly .pgn.zst> | python3 -I tests/probes/sparks/sc13_chess_clock.py
COST:       a few minutes; reads PGN text on standard input until it has 20,000 games at each of 300+0 and 180+0,
            then stops. Only totals are printed: no player names, game links or games are kept.

For each player's moves 11 to 60, the move time is the drop in that player's [%clk] annotation (whole seconds).
Moves are binned by the clock before the move in 12 logarithmic bins from 5 to 290 seconds, and the logarithm of
the mean move time is fitted against the logarithm of the mean clock; a fixed fraction of the time left gives a
slope of 1. Prediction (published in SPARKS.md before this ran): slope 0.6 +- 0.2 at 5+0. Fail: a slope between 0.9
and 1.1, or below 0.4.
Control: synthetic players who spend a fixed fraction of their clock, with lognormal noise, and whose clocks are
shown in whole seconds go through the same bins and fit; the slope must be 1 +- 0.05.
Post hoc (added after the first run, and labelled so in SPARKS.md): the same fit within one band of move numbers,
moves 21 to 40, so that the opening's fast moves do not sit in the top bins, and with bins of fewer than 100 moves
left out.
"""
import math, random, re, sys

CLK = re.compile(r"\[%clk (\d+):(\d\d):(\d\d)\]")
EDGES = [5 * (290 / 5) ** (i / 12) for i in range(13)]
WANT = 20_000


def binned(pairs):
    """pairs of (clock before, move time) -> per-bin (count, mean clock, mean time)."""
    acc = [[0, 0.0, 0.0] for _ in range(12)]
    for c, t in pairs:
        if EDGES[0] <= c < EDGES[-1]:
            i = min(11, int(12 * math.log(c / 5) / math.log(290 / 5)))
            a = acc[i]
            a[0] += 1; a[1] += c; a[2] += t
    return [(n, sc / n, st / n) for n, sc, st in acc if n]


def slope(bins):
    xs = [math.log(c) for n, c, t in bins if t > 0]
    ys = [math.log(t) for n, c, t in bins if t > 0]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def player_pairs(clocks, lo=11, hi=60):
    """One player's clocks after each of their moves -> (clock before, time) for their moves lo to hi."""
    return [(clocks[k - 1], clocks[k - 1] - clocks[k]) for k in range(lo - 1, min(hi, len(clocks)))]


def control():
    rng = random.Random(13)
    pairs = []
    for _ in range(4000):
        true, shown = 300.0, [300]
        for _ in range(60):
            true -= 0.04 * true * math.exp(0.8 * rng.gauss(0, 1) - 0.32)
            if true <= 0:
                break
            shown.append(math.floor(true))
        pairs += player_pairs(shown)
    s = slope(binned(pairs))
    assert abs(s - 1) <= 0.05, s
    return s


def main():
    print(f"control: synthetic fixed-fraction players give slope {control():.3f} (must be 1 +- 0.05)")
    games = {"300+0": [], "180+0": []}
    band = {"300+0": [], "180+0": []}
    negative = {"300+0": 0, "180+0": 0}
    tc, lines = None, []
    for line in sys.stdin:
        if line.startswith("[TimeControl "):
            tc = line.split('"')[1]
        elif line.startswith("1. ") and tc in games and len(games[tc]) < WANT:
            cl = [int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in CLK.findall(line)]
            pairs = player_pairs(cl[0::2]) + player_pairs(cl[1::2])
            negative[tc] += sum(1 for c, t in pairs if t < 0)
            games[tc].append([(c, t) for c, t in pairs if t >= 0])
            band[tc] += [(c, t) for c, t in player_pairs(cl[0::2], 21, 40) + player_pairs(cl[1::2], 21, 40)
                         if t >= 0]
            if all(len(g) >= WANT for g in games.values()):
                break
    for tc, gs in games.items():
        pairs = [p for g in gs for p in g]
        bins = binned(pairs)
        print(f"\n{tc}: {len(gs)} games, {len(pairs)} moves (moves 11 to 60), {negative[tc]} moves with the clock "
              f"rising dropped")
        print("  clock before (s)   moves   mean time (s)   fraction of clock")
        for n, c, t in bins:
            print(f"  {c:16.1f} {n:8d} {t:15.2f} {t / c:18.3f}")
        s = slope(bins)
        print(f"  slope {s:.3f}")
        if tc == "300+0":
            verdict = ("PASS" if 0.4 <= s <= 0.8 else
                       "FAIL" if 0.9 <= s <= 1.1 or s < 0.4 else "PARTIAL: outside the predicted band, not refuted")
            print(f"  prediction 0.6 +- 0.2: {verdict}")
        hb = [b for b in binned(band[tc]) if b[0] >= 100]
        print(f"  post hoc, moves 21 to 40 only, bins of 100 moves or more: slope {slope(hb):.3f}; "
              + ", ".join(f"{c:.0f} s: {t / c:.3f}" for n, c, t in hb))
        big = [b for b in bins if b[0] >= 100]
        print(f"  post hoc, moves 11 to 60, bins of 100 moves or more: slope {slope(big):.3f}")


if __name__ == "__main__":
    main()
