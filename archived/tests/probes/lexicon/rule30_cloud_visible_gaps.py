#!/usr/bin/env python3
"""rule30_cloud_visible_gaps.py: RV, Cloud's second reading of GC502 to GC504, and the wheel read as gaps.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_visible_gaps.py [TRIALS=1500] [T=3000] [SEED]
            python3 tests/probes/lexicon/rule30_cloud_visible_gaps.py --wheel [TRIALS=800] [SEED=909]   (post-hoc)
            python3 tests/probes/lexicon/rule30_cloud_visible_gaps.py --transients [TRIALS=600] [SEED=707]
COST:       about 15 s; --wheel and --transients about a minute.

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
Found by looking, before any run (Cloud, 2026-10-08, by 12:41 BST; not evidence):
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

OUTCOME, 2026-10-08 (by 12:46 BST; seed 808, 1,500 trials, T = 3000, 15 s; 51,045 departures at even classes after
at least 56 steps on the wheel):
  RV-C1, C2, C3 PASS: GPT's counts C_n = 2, 3, 5, 8, 12, 17, 25, GC503's formula and GC504's characterization and
  forced prefix all reproduce in this coding. Exploratory, no prediction: C_8 = 36.
  RV-P1 HELD: the visible wheel is 0001000010000100001000010010, gaps 4, 4, 4, 4, 2, 4, and obeys GC502 and GC504.
  RV-C4 PASS.
  RV-P2 REFUTED. Every one of the 27,610 forward departures (classes 12: 39, 32: 26,976, 42: 595) has trigger
  b, q, r, z = 1, 0, 1, 1 at s - 4. The 2-gap is made by column 3 turning white (q = 0), not by r OR z failing.
  RV-P3 HELD. All 23,435 class-52 departures make a 4-gap, with trigger 1, 1, 1, 0.
POST-HOC (--wheel, run after the outcome above, so it is exploratory and not a test; seed 909, 800 trials): deep inside
  long locks (at least 40 steps before the departure), the wheel's columns 2 .. 6 at each visible gap start are
  1, 1, 1, 0, 0 at the five 4-gaps (classes 8, 18, 28, 38, 54) and 1, 0, 1, 1, 0 at the 2-gap (class 48), with no
  exception in about 1,920 gap starts per class. (A first version of this mode also read odd times; fixed.) So every
  departure seen is a swap: at a 4-gap's start the orbit shows the 2-gap's state (a forward
  kick, the 2-gap arriving early), and at the 2-gap's start it shows a 4-gap's state (a backward kick, the 2-gap
  arriving late). Against one turn earlier, columns 3 and 5 differ at s - 4. Column 5 already differs at s - 10,
  s - 8 and s - 6, and column 3 first differs at s - 4.

SECOND BLOCK, RV2 (--transients), predictions written 2026-10-08 13:08 BST and pushed before its first run:
  The swap reading says a kick moves the wheel's one 2-gap (early for a forward kick, late for a backward one). If
  that is the whole story, column 1 never leaves the wheel's two-letter gap alphabet {2, 4} between a departure and
  the next lock.
  RV2-P1: in every transient, from the gap containing a departure (after at least 56 steps on the wheel) to the
          start of the next stretch of at least 56 steps on the wheel, every visible gap has length 2 or 4.
          Confidence 0.4.
  RV2-P2: over whole runs (right halves as in the main run, T = 3000, gaps counted from time 200 on), gaps of
          length 1 and 3 together are under 10% of all visible gaps. Confidence 0.5.
  RV2-C1 (control): every gap is 1, 2, 3 or 4 (GC502), and no gap 1 is followed by a gap 2 (GC504).
  Counterfactual: if 1-gaps and 3-gaps are common in transients, a kick is not a rearrangement within the wheel's
  alphabet, and column 1's gap code needs all four letters even near the lock.
OUTCOME RV2, 2026-10-08 (by 13:10 BST; seed 707, 600 trials, T = 3000, 7 s): RV2-C1 PASS (no gap outside 1 .. 4, no
  1-gap followed by a 2-gap). RV2-P1 HELD: all 19,177 transients use only 2-gaps and 4-gaps (10,416 and 9,354). A kick
  moves the 2-gap and nothing else. RV2-P2 REFUTED, narrowly: gaps of length 1 or 3 are 0.1003 of the 189,968 gaps
  counted. The surprise is in the split. There are 19,058 1-gaps but one 3-gap. By GC503 a 3-gap needs b = 0, q = 1
  at its first zero, and (by hand) that follows a visible 1 at t - 2 exactly when columns 2 .. 5 there read 0000,
  100* or 01**: 7/16 of random rows. Evolved right halves next to the wall almost never show it.
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
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1][0] != "-" else 1500
T = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1][0] != "-" else 3000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[1][0] != "-" else int.from_bytes(os.urandom(4), "big")


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


def wheel_mode(trials, seed):
    """Post-hoc: the wheel's columns 2 .. 6 at gap starts, and which columns differ from one turn earlier."""
    from collections import defaultdict
    rng = random.Random(seed)
    deep, diff = defaultdict(Counter), defaultdict(Counter)
    for i in range(trials):
        rows = rows_from(rng.getrandbits((16, 24, 32, 48, 64)[i % 5]) | 1, T)
        c1 = [(r >> 1) & 1 for r in rows]
        for s, a in departures(rows):
            d = (s - a) % P
            t = next(t for t in range(s - 1, -1, -1) if c1[t] != U[(t - d) % P]) + 1 if any(
                c1[t] != U[(t - d) % P] for t in range(s)) else 0
            if s - t >= 2 * P + 40:
                for u in range(t + P + (t + P) % 2, s - 40, 2):           # even (visible) times only
                    if c1[u] == 0 and c1[u - 2] == 1:
                        deep[(u - d) % P][sites(rows[u], 2, 6)] += 1
            if a in (12, 32, 42, 52) and s - t >= 2 * P:
                for off in (2, 4, 6, 8, 10):
                    now, before = sites(rows[s - off], 2, 7), sites(rows[s - off - P], 2, 7)
                    diff[(a, off)][tuple(k + 2 for k in range(6) if now[k] != before[k])] += 1
    print("wheel's columns 2 .. 6 at visible gap starts, by class:")
    for c in sorted(deep):
        print(" ", c, dict(deep[c].most_common(4)))
    print("columns (2 .. 7) that differ from one turn earlier, at s - off, by (class, off):")
    for k in sorted(diff):
        print(" ", k, dict(diff[k].most_common(4)))


def gaps_of(c1, start):
    """(time of the gap's first zero, length) for every complete visible gap from `start` on."""
    out, t = [], start + (start % 2)
    while t < len(c1) - 10 and not (c1[t] == 1):
        t += 2
    while t < len(c1) - 10:
        u = t + 2
        n = 0
        while u < len(c1) - 2 and c1[u] == 0:
            n += 1
            u += 2
        if u >= len(c1) - 2:
            break
        out.append((t + 2, n))
        t = u
    return out


def transients(trials, seed):
    """RV2: visible gaps between each departure and the next lock of at least 56 steps."""
    rng = random.Random(seed)
    trans, whole, pairs12 = Counter(), Counter(), 0
    n_trans, pure = 0, 0
    for i in range(trials):
        rows = rows_from(rng.getrandbits((16, 24, 32, 48, 64)[i % 5]) | 1, T)
        c1 = [(r >> 1) & 1 for r in rows]
        gl = gaps_of(c1, 200)
        whole.update(n for _, n in gl)
        pairs12 += sum(1 for a, b in zip(gl, gl[1:]) if a[1] == 1 and b[1] == 2)
        locks = []                                       # (start, end) of stretches of >= 56 steps on the wheel
        t = 0
        while t + P < len(c1):
            d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
            if d is None:
                t += 1
                continue
            s = t + P
            while s < len(c1) and c1[s] == U[(s - d) % P]:
                s += 1
            locks.append((t, s))
            t = s
        for (a, s), (b, _) in zip(locks, locks[1:]):
            g = [n for (start, n) in gl if s - 8 <= start < b]
            if not g:
                continue
            n_trans += 1
            trans.update(g)
            pure += set(g) <= {2, 4}
    total = sum(whole.values())
    odd = (whole[1] + whole[3]) / total
    print(f"RV2: {trials} trials, {total} gaps after time 200, by length {dict(sorted(whole.items()))}")
    print("RV2-C1", "PASS" if set(whole) <= {0, 1, 2, 3, 4} and whole[0] == 0 and not pairs12 else "FAIL",
          f"(1-then-2 pairs: {pairs12})")
    print(f"transients: {n_trans}; their gaps by length {dict(sorted(trans.items()))}; all in {{2, 4}}: {pure}")
    print("RV2-P1", "HELD" if pure == n_trans and n_trans else "REFUTED",
          f"({pure} of {n_trans} transients use only gaps 2 and 4)")
    print("RV2-P2", "HELD" if odd < 0.10 else "REFUTED", f"(gaps 1 and 3: {odd:.3f} of all gaps)")


if __name__ == "__main__":
    if "--transients" in sys.argv:
        rest = sys.argv[sys.argv.index("--transients") + 1:]
        transients(int(rest[0]) if rest else 600, int(rest[1]) if len(rest) > 1 else 707)
    elif "--wheel" in sys.argv:
        rest = sys.argv[sys.argv.index("--wheel") + 1:]
        wheel_mode(int(rest[0]) if rest else 800, int(rest[1]) if len(rest) > 1 else 909)
    else:
        main()
