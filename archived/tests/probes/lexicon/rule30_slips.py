#!/usr/bin/env python3
"""rule30_slips.py: the wheel's slips as particles. Part 3 of the proof route (RULE30-PRIZE.md section 8.6): can
the slips conspire? First, what is a slip?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_slips.py [W=12] [T=2048]
COST:       a few minutes on one core.

An exploratory look (2026-10-05, not recorded) suggested three things:
  - the domain of section 8.5 is a wedge on the right of column 0, pure near it (column 1 1.000, column 2 0.998)
    and fading into the interior (0.70 by column 12);
  - a slip is a defect travelling in from the right at about half a cell per step;
  - the defect has the same shape in unrelated right halves.
This script makes those claims measurable.

Method. The right side (columns 0..6, column 0 clamped to 0101...) runs for T steps from every right half up to W
cells; locked ones (column 1 eventually 56-periodic) are set aside. The domain D_i(t), i = 0..6, t mod 56, is the
majority value of column i over windows where column 1 equals U at some phase, aligned to that phase. It is built
from the training half (R divisible by 7) and used on the test half (the rest). A slip is a window boundary where
column 1 stops being U at its phase d. Its front is the arrival time t_i at each column i = 1..6: the first time in
the two windows around the slip at which column i leaves D_i at phase d and leaves it again within the next 6 steps.
Its shape is the pattern of cells off the domain in columns 1..6 over the 12 steps from t_1 - 8 to t_1 + 3. Its shift
is the phase of the next exact window (within 10 windows) minus d, mod 56.

PREDICTIONS, written 2026-10-05 before this script's first run:
  P1 (blind): at least 70% of slips have a front from the right, t_6 < t_5 < ... < t_1, with a mean step
     (t_1 - t_6) / 5 between 1.5 and 2.5 (a speed of about half a cell per step).
  P2 (blind): at most 10 distinct shapes cover at least 80% of slips.
  P3 (uncertain): within each of the 5 commonest shapes, one shift accounts for at least 80% of its slips.
  C  (cross-validation): on the test half, inside exact windows, columns 1..6 agree with the training domain at least
     95% of the time.
  CF1 (counterfactual, direction): at the same slips, a front from the LEFT (t_1 < t_2 < ... < t_6, the same step
     range) occurs at most 10% of the time, so the direction is not an artefact of the detector.
  CF2 (counterfactual, noise): inside long exact stretches (no slip), a front from the right across columns 2..6 (the
     same test without column 1, which cannot depart there) occurs at most 10% of the time.
REFUTED-BY: C, CF1 or CF2 failing (the instrument); P1, P2 or P3 failing.

OUTCOME of the first run, 2026-10-05 (W = 12, T = 2048): 560 training and 3,370 test right halves, 22,937 slips.
  C passed (0.9861). CF1 passed (0 of 22,937 fronts from the left).
  CF2 FAILED, vacuously: 0 of 0. Exact windows rarely come five in a row (8.4% of windows are exact; rule30_wheel.py,
     Q1), so no boundary qualified. The noise control could not run, and it needs another design.
  P1 REFUTED as operationalised: 0 of 22,937. The shapes below show why. The front runs diagonally from column 5,
     8 steps before t_1, to column 1 at t_1, but column 6 departs a step AFTER column 5, so the strict order over six
     columns fails every time. The front zigzags (3, 1, 3, 1 steps between columns), about half a cell per step on
     average, in step with the trace. A cleaner test of the speed needs another definition of arrival.
  P2 HELD: only 4 distinct shapes, and the 10 commonest (that is, all 4) cover 96.7% of slips. The commonest, 19,259
     slips (84%), and the third, 552, differ in one cell. So a slip is essentially one kind of particle.
  P3 REFUTED: within the commonest shape the commonest shift is 52, at only 28% (26 at 43% in the second, 32 at 31% in
     the third). The phase after a slip is not set by the first particle alone, presumably because more particles
     arrive before the wheel locks again.
"""
import sys, pathlib
from collections import Counter, defaultdict

W = int(sys.argv[1]) if len(sys.argv) > 1 else 12
T = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
P, M = 56, 6

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def spacetime(R):
    """Rows as small integers: bit i = column i, i = 0..6."""
    mask = (1 << (R.bit_length() + T + 3)) - 1
    row, rows = R << 1, []
    for t in range(T):
        rows.append(row & ((1 << (M + 1)) - 1))
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return rows


def cell(st, t, i):
    return (st[t] >> i) & 1


def phases(col1):
    out = []
    for a in range(0, T - P + 1, P):
        w = col1[a:a + P]
        d = next((d for d in range(P) if all(w[t] == U[(a + t - d) % P] for t in range(P))), None)
        out.append(d)
    return out


def locked(col1):
    last_bad = max([t for t in range(T - P) if col1[t] != col1[t + P]], default=-1)
    return last_bad < T - P - 400


def front(st, D, d, lo, hi):
    """Arrival times t_1..t_6 (None where absent) of a persistent departure from the domain at phase d."""
    out = []
    for i in range(1, M + 1):
        off = [cell(st, t, i) != D[i][(t - d) % P] for t in range(lo, hi)]
        ti = next((lo + j for j in range(len(off)) if off[j] and any(off[j + 1:j + 7])), None)
        out.append(ti)
    return out


def from_right(ts):
    if any(t is None for t in ts):
        return False
    if not all(ts[i] > ts[i + 1] for i in range(len(ts) - 1)):
        return False
    step = (ts[0] - ts[-1]) / (len(ts) - 1)
    return 1.5 <= step <= 2.5


def from_left(ts):
    if any(t is None for t in ts):
        return False
    if not all(ts[i] < ts[i + 1] for i in range(len(ts) - 1)):
        return False
    step = (ts[-1] - ts[0]) / (len(ts) - 1)
    return 1.5 <= step <= 2.5


def main():
    votes = [[[0, 0] for _ in range(P)] for _ in range(M + 1)]
    n_train = n_test = 0
    for R in range(0, 1 << W, 7):                         # pass 1: the training half builds the domain
        st = spacetime(R)
        col1 = [cell(st, t, 1) for t in range(T)]
        if locked(col1):
            continue
        n_train += 1
        for k, d in enumerate(phases(col1)):
            if d is None:
                continue
            for t in range(k * P, k * P + P):
                for i in range(M + 1):
                    votes[i][(t - d) % P][cell(st, t, i)] += 1
    D = [[0 if v[0] >= v[1] else 1 for v in votes[i]] for i in range(M + 1)]

    agree = tot = 0
    slips, cf2_n, cf2_hit = [], 0, 0
    for R in range(1 << W):                               # pass 2: the test half
        if R % 7 == 0:
            continue
        st = spacetime(R)
        col1 = [cell(st, t, 1) for t in range(T)]
        if locked(col1):
            continue
        n_test += 1
        ph = phases(col1)
        for k, d in enumerate(ph):
            if d is None:
                continue
            for t in range(k * P, k * P + P):
                for i in range(1, M + 1):
                    agree += cell(st, t, i) == D[i][(t - d) % P]
                    tot += 1
        for k in range(1, len(ph)):
            d = ph[k - 1]
            if d is not None and ph[k] is None:
                ts = front(st, D, d, (k - 1) * P, min(T, (k + 1) * P))
                nxt = next((ph[j] for j in range(k + 1, min(len(ph), k + 11)) if ph[j] is not None), None)
                shape = None
                if ts[0] is not None and ts[0] - 8 >= 0 and ts[0] + 4 <= T:
                    shape = tuple(int(cell(st, t, i) != D[i][(t - d) % P]) for t in range(ts[0] - 8, ts[0] + 4)
                                  for i in range(1, M + 1))
                slips.append((ts, shape, None if nxt is None else (nxt - d) % P))
            if 2 <= k <= len(ph) - 3 and all(ph[j] is not None and ph[j] == ph[k] for j in range(k - 2, k + 3)):
                cf2_n += 1
                cf2_hit += from_right(front(st, D, ph[k], (k - 1) * P, (k + 1) * P)[1:])
    report("C cross-validation: the training domain describes the test half (columns 1..6, exact windows)",
           tot > 0 and agree / tot >= 0.95, f"{agree / tot:.4f}; train {n_train}, test {n_test} right halves")
    n = len(slips)
    cf1 = sum(from_left(ts) for ts, _, _ in slips)
    report("CF1 fronts from the left are rare at slips (the direction is not the detector's)", n > 0 and cf1 / n <= 0.10,
           f"{cf1} of {n}")
    report("CF2 inside long exact stretches a front across columns 2..6 is rare", cf2_n > 0 and cf2_hit / cf2_n <= 0.10,
           f"{cf2_hit} of {cf2_n}")
    p1 = sum(from_right(ts) for ts, _, _ in slips)
    steps = [(ts[0] - ts[-1]) / (M - 1) for ts, _, _ in slips if from_right(ts)]
    verdict("P1 slips are fronts from the right at about half a cell per step", n > 0 and p1 / n >= 0.70,
            f"{p1} of {n} ({p1 / n:.1%}); mean step {sum(steps) / len(steps):.2f}" if steps else f"{p1} of {n}")
    shapes = Counter(s for _, s, _ in slips if s is not None)
    ranked = shapes.most_common()
    cover10 = sum(c for _, c in ranked[:10]) / n if n else 0
    verdict("P2 at most 10 shapes cover 80% of slips", cover10 >= 0.80,
            f"the 10 commonest cover {cover10:.1%}; {len(shapes)} distinct shapes")
    by_shape = defaultdict(Counter)
    for _, s, sh in slips:
        if s is not None and sh is not None:
            by_shape[s][sh] += 1
    p3 = []
    for s, c in ranked[:5]:
        sh = by_shape[s]
        top = sh.most_common(1)[0] if sh else (None, 0)
        p3.append((c, top[0], top[1] / sum(sh.values()) if sh else 0.0))
    verdict("P3 within each of the 5 commonest shapes one shift is at least 80%", all(f >= 0.80 for _, _, f in p3),
            "; ".join(f"{c} slips, shift {d} at {f:.0%}" for c, d, f in p3))
    print("\n   the commonest shapes (columns 1..6 left to right, 12 steps from t_1 - 8; # = off the domain):")
    for s, c in ranked[:3]:
        print(f"      x{c}:")
        for r in range(12):
            print("         " + "".join("#" if s[r * M + i] else "." for i in range(M)))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
