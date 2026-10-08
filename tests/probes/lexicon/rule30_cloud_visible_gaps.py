#!/usr/bin/env python3
"""rule30_cloud_visible_gaps.py: RV, Cloud's second reading of GC502 to GC504, and the wheel read as gaps.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_visible_gaps.py [TRIALS=1500] [T=3000] [SEED]
COST:       a few minutes.

The model is GPT's (GC499): Rule 30 on the right half, sites 1, 2, ..., with the wall at site 0 clamped to 0 at
even times and 1 at odd times. The visible trace is site 1 at even times (one symbol per wall period). GPT's claims,
read by hand in CL033: no visible 11 (GC499), no visible 00000 (GC502), the first zero run is decided by sites
a, b, q, r, z = 1 .. 5 (GC503), and after a visible 101 the next zero run has length 1, 3 or 4, never 2 (GC504).
This script is an independent check with Cloud's own coding (a row is an integer, bit i is site i, bit 0 the wall).

Controls (GPT's claims, checked independently):
  RV-C1: the distinct visible words of length n from initial right words of length 2n - 1 with a zero tail number
         2, 3, 5, 8, 12, 17, 25 for n = 1 .. 7 (GC502), and C_2's words are 00, 01, 10 (GC500).
  RV-C2: GC503's zero-run formula holds on all 32 five-bit patches, each with 64 random farther tails.
  RV-C3: GC504's characterization of visible 101 (a = 1, b = q = 0, r OR z = 1) holds on all 32 patches with random
         tails, and initial sites 10001 force the visible prefix 10100001 for every tail tried.
Found by looking, before any run (Cloud, 2026-10-08 12:50 BST; not evidence):
  The wheel U has period 56, so its visible half is U at even indices, 28 symbols: 0001000010000100001000010010.
  Its gaps (zero runs between ones) are, cyclically, 4, 4, 4, 4, 2, 4: five maximal latches and one short gap.
  Its ones have density 6/28 = 3/14, near GC502's floor of 1/5. An even class c is visible position c/2, and the six
  even classes left after one turn (entry 26: 2, 12, 22, 32, 42, 52) are exactly the third zeros of the five 4-gaps
  and the 1 that ends the 2-gap. GC503 then says what a departure there must be. At a third zero the 4-gap becomes a
  2-gap. At class 52 the 2-gap becomes a 3-gap or a 4-gap. A departure at a second or fourth zero would make a 1-gap
  or 3-gap, and that needs column 2 white at the gap's first zero (GC503: R = 1 needs b = q = 0, R = 3 needs b = 0).
  A departure at a 1, or at a first zero, is barred at every time by no-00000 or no-11.
PREDICTIONS (Cloud's, pushed before the first run):
  RV-P1: the visible wheel word and its gap code are as written above, and the word obeys GC502 and GC504 cyclically.
         Confidence 0.97 (the word was read off U by hand).
  RV-P2: at every real departure from the wheel at an even class 2, 12, 22, 32 or 42, after at least 56 steps on it,
         the trigger at the gap's first zero (time s - 4) is b = q = 1, r = z = 0: the 4-gap's trigger loses r OR z
         and keeps q. Confidence 0.6. (GC503 allows b = 1, q = 0 as the other way to make a 2-gap.)
  RV-P3: at every such departure at class 52, the new gap has length 4, never 3 (so column 2 stays black at the
         gap's first zero, as the wheel has it). Confidence 0.6.
  RV-C4 (control): at every even-class departure, column 1 is 1 at s - 6 and 0 at s - 4 and s - 2, as the wheel
         word requires.
Counterfactual: if RV-P2 fails with q = 0, column 3 is not locked at the gap's start when a forward kick begins. If
RV-P3 fails, a backward kick can turn column 2 white at the gap start, and "column 2 is locked" is not why the
second and fourth zeros never kick.
"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P = 56
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else int.from_bytes(os.urandom(4), "big")


def step(row, t):
    """One Rule 30 update of the right half; bit 0 is the wall, white at even times."""
    new = (row << 1) ^ (row | (row >> 1))
    return (new & ~1) | ((t + 1) % 2)


def rows_from(right, n):
    """Rows at times 0 .. n - 1 from initial right sites (bit i of `right` is site i + 1), zero tail."""
    row, out = right << 1, []
    for t in range(n):
        out.append(row)
        row = step(row, t)
    return out


def visible(right, n):
    rows = rows_from(right, 2 * n - 1)
    return "".join(str((rows[2 * k] >> 1) & 1) for k in range(n))


def sites(row, lo, hi):
    return tuple((row >> i) & 1 for i in range(lo, hi + 1))


def zero_run(word):
    return next((i for i, c in enumerate(word) if c == "1"), len(word))


def gc503(a, b, q, r, z):
    if a:
        return 0
    if not (b or q):
        return 1
    if not b:
        return 3
    if not q or not (r or z):
        return 2
    return 4


def controls(rng):
    counts = [len({visible(w, n) for w in range(2 ** (2 * n - 1))}) for n in range(1, 8)]
    c2 = sorted({visible(w, 2) for w in range(8)})
    print("RV-C1", "PASS" if counts == [2, 3, 5, 8, 12, 17, 25] and c2 == ["00", "01", "10"] else "FAIL",
          counts, c2)
    bad = 0
    for patch in range(32):
        bits = [(patch >> i) & 1 for i in range(5)]
        for _ in range(64):
            right = patch | (rng.getrandbits(16) << 5)
            bad += zero_run(visible(right, 6)) != gc503(*bits)
    print("RV-C2", "PASS" if not bad else f"FAIL ({bad})", "(32 patches x 64 tails)")
    bad = 0
    for patch in range(32):
        a, b, q, r, z = [(patch >> i) & 1 for i in range(5)]
        claim = a == 1 and b == 0 and q == 0 and (r or z)
        for _ in range(64):
            right = patch | (rng.getrandbits(16) << 5)
            bad += (visible(right, 3) == "101") != bool(claim)
    forced = {visible(0b10001 | (rng.getrandbits(20) << 5), 8) for _ in range(200)}
    print("RV-C3", "PASS" if not bad and forced == {"10100001"} else f"FAIL ({bad}, {forced})")
    n8 = len({visible(w, 8) for w in range(2 ** 15)})
    print(f"exploratory: C_8 = {n8}")


def wheel_word():
    v = "".join(str(U[2 * k]) for k in range(P // 2))
    ones = [i for i, c in enumerate(v) if c == "1"]
    gaps = [(ones[(j + 1) % len(ones)] - ones[j] - 1) % len(v) for j in range(len(ones))]
    vv = v + v
    ok = "11" not in vv and "00000" not in vv and "101001" not in vv
    held = v == "0001000010000100001000010010" and gaps == [4, 4, 4, 4, 2, 4] and ok
    print("RV-P1", "HELD" if held else "REFUTED", v, "gaps", gaps, "obeys GC502/GC504:", ok)


def departures(rows):
    c1 = [(r >> 1) & 1 for r in rows]
    out, t, n = [], 0, len(c1)
    while t + P + 8 < n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        if s + 8 >= n:
            break
        out.append((s, (s - d) % P))
        t = s
    return out


def main():
    rng = random.Random(SEED)
    controls(rng)
    wheel_word()
    fwd, back, c4, events = Counter(), Counter(), 0, 0
    for i in range(TRIALS):
        w = (16, 24, 32, 48, 64)[i % 5]
        rows = rows_from(rng.getrandbits(w) | 1, T)
        for s, a in departures(rows):
            if a % 2 or a not in (2, 12, 22, 32, 42, 52):
                continue
            events += 1
            c1 = [(rows[s + k] >> 1) & 1 for k in range(-6, 9, 2)]          # visible at s-6, s-4, ..., s+8
            c4 += c1[:3] != [1, 0, 0]
            trig = sites(rows[s - 4], 1, 5)
            gap = zero_run("".join(map(str, c1[1:])))
            (back if a == 52 else fwd)[(a, gap, trig[1:])] += 1
    print(f"SEED {SEED}: {TRIALS} trials, T = {T}, {events} departures at even classes after a full turn")
    print("RV-C4", "PASS" if not c4 else f"FAIL ({c4})")
    print("forward (class, gap, trigger b q r z):", dict(sorted(fwd.items())))
    print("class 52 (class, gap, trigger b q r z):", dict(sorted(back.items())))
    p2 = all(g == 2 and tr == (1, 1, 0, 0) for (a, g, tr) in fwd)
    p3 = all(g == 4 for (a, g, tr) in back)
    print("RV-P2", "HELD" if p2 and fwd else "REFUTED", "RV-P3", "HELD" if p3 and back else "REFUTED")


if __name__ == "__main__":
    main()
