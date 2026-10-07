#!/usr/bin/env python3
"""rule30_kick_candles.py: KC, the owner's candles. Which kicks stay possible however long the wheel has run?

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_candles.py [TRIALS=6000] [T=6000] [SEED]
COST:       about 20 minutes per 6,000 trials.

The owner, 2026-10-07: "Are there any other candles that snuff out. Similarly, are their any snuffed candles that
seemingly spontaneously relight." In the exact sense of KS and KA, a candle is a (class, kick) pair, and it is lit
at N if some right side can make that kick after N steps on the wheel. GPT's GC373 and GC377 (checked by Local, L229
and L231) show that lit at N implies lit at every smaller N, so a snuffed candle never relights. The solver shows a
candle out (unsatisfiable) but is slow for long N. A real right half that kicks after N steps shows the candle lit
at N, with no solver. So this script runs real right halves for a long time and records, for every departure after a
run of at least 56 steps on the wheel, its class, its kick and the run's length. The longest run before each
(class, kick) is a proved lower bound on that candle's life: the right half is the certificate, replayable.

Caution (KB-C0's lesson): 21 observations can fit several nearby phases, so a departure's kick is a set. The
per-kick figures credit every kick in the set; the per-class figures are exact.

Controls (a real kick may never contradict a proved death):
  KC-C1: no departure after a run of 56 or more steps at a class outside entry 26's one-turn set
         {2, 12, 22, 32, 39, 42, 49, 52} (one turn of the wheel excludes them for every right side).
  KC-C2: no departure after a run of N*(c) or more steps at a class c of KA's death times: 22 at 53, 2 and 49 at 61,
         39 at 70, 12 at 127.
PREDICTIONS (Cloud's, pushed before the first run):
  KC-P1: classes 32 and 52 each have a departure after a run of more than 560 steps on the wheel, so they are lit at
         least to 560 (answering KS's strain run from below). Confidence 0.7.
  KC-P2: class 42 has a departure after a run of more than 336 steps. Confidence 0.5; it is rare (1 in 300 kicks).
  KC-P3: every one of entry 27's 16 surviving (class, kick) pairs is seen after some run of at least 140 steps.
         Confidence 0.4 (class 42's +5 is realized at only 45 of 56 cases, and some pairs may be very rare).

OUTCOME, 2026-10-07 (by 23:16 BST; three runs of 4,000 trials, T = 6000, seeds 101, 202, 303; 835,089 departures
after at least 56 steps on the wheel):
  KC-C1 PASS and KC-C2 PASS in all three: no real kick contradicts a proved death. Class 12 is seen after runs of up
  to 111 (death 127), class 39 up to 63 (death 70), class 49 at 56 (death 61); classes 2 and 22 not at all.
  Longest run before a departure (any landing): class 32, 336, 300, 300; class 52, 264, 280, 316; class 42, 208 in all
  three runs. With a clean landing (21 observations), class 32 reaches 336 (kicks +2 .. +5) and class 52 reaches 316
  (-6 .. -3), so class 32 is lit at N = 336: that answers KS's strain case from below, with a real right half.
  KC-P1 REFUTED (no run beyond 560), KC-P2 REFUTED (42 peaks at 208), KC-P3 REFUTED (15 of 16 pairs; class 42's +5
  peaks at 106). The tails look exponential, so a long run is rare, not barred.
  Two structures (exploratory): a run's length is fixed modulo 56 by its class and its landing angle, so record
  values recur across seeds (class 42's 208 three times). The kicks at the landing window's edges (class 32's +6,
  class 42's +5 and class 52's -1, landing at 52 or 42) have the shortest records, as class 12's +9 (landing at 54)
  died first, at 40.
"""
import os
import random
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P, F = 56, 20
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
T = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else int.from_bytes(os.urandom(4), "big")
ONE_TURN = {2, 12, 22, 32, 39, 42, 49, 52}
DEATH = {22: 53, 2: 61, 49: 61, 39: 70, 12: 127}
SURVIVE = {32: range(2, 7), 42: range(1, 6), 52: range(-6, 0)}


def kick_of(dn):
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def column1(R, width):
    mask = (1 << (width + T + 4)) - 1
    row, c1 = R << 1, []
    for t in range(T):
        c1.append((row >> 1) & 1)
        row = ((((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)) & mask
    return c1


def departures(c1):
    """(class, kicks, run length) for every departure after at least one full turn on the wheel."""
    out, t, n = [], 0, len(c1)
    while t + P + F < n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        if s + F >= n:
            break
        ks = [kick_of((dn - d) % P) for dn in range(0, P, 2)
              if all(c1[s + j] == U[(s + j - dn) % P] for j in range(F + 1))]
        out.append(((s - d) % P, ks, s - t))
        t = s
    return out


def main():
    rng = random.Random(SEED)
    longest = defaultdict(int)                 # (class, kick) -> longest run before it
    witness = {}
    by_class, events, bad = defaultdict(int), 0, []
    for i in range(TRIALS):
        w = (16, 24, 32, 48, 64, T + 2)[i % 6]
        R = rng.getrandbits(w) | 1
        for a, ks, run in departures(column1(R, w)):
            events += 1
            by_class[a] = max(by_class[a], run)
            if (a not in ONE_TURN and run >= P) or (a in DEATH and run >= DEATH[a]):
                bad.append((a, ks, run, w, R if w <= 64 else "infinite"))
            for k in ks:
                if run > longest[(a, k)]:
                    longest[(a, k)] = run
                    witness[(a, k)] = (w, R if w <= 64 else None)
        if (i + 1) % 1000 == 0:
            print(f"{i + 1} trials, {events} departures after a full turn", flush=True)
    print(f"SEED {SEED}: {TRIALS} trials, T = {T}, {events} departures after at least 56 steps on the wheel")
    for a in sorted(by_class):
        sizes = {k: longest[(a, k)] for (b, k) in sorted(longest) if b == a}
        print(f"class {a:2d}: longest run before a departure {by_class[a]:5d}; by kick {sizes}")
    print("KC-C1", "PASS" if not any(a not in ONE_TURN for a, *_ in bad) else "FAIL")
    print("KC-C2", "PASS" if not any(a in DEATH for a, *_ in bad) else "FAIL", bad[:3])
    print("KC-P1", "HELD" if by_class[32] > 560 and by_class[52] > 560 else "REFUTED",
          f"(32: {by_class[32]}, 52: {by_class[52]})")
    print("KC-P2", "HELD" if by_class[42] > 336 else "REFUTED", f"(42: {by_class[42]})")
    seen = [(a, k) for a, ks in SURVIVE.items() for k in ks if longest[(a, k)] >= 140]
    print("KC-P3", "HELD" if len(seen) == 16 else "REFUTED", f"({len(seen)} of 16 pairs seen after >= 140 steps)")
    print("witnesses (width, seed) for the longest runs of the surviving pairs:",
          {f"{a}{k:+d}": witness[(a, k)] for a, ks in SURVIVE.items() for k in ks if (a, k) in witness})


if __name__ == "__main__":
    main()
