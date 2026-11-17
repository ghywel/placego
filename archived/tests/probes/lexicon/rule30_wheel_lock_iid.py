#!/usr/bin/env python3
"""rule30_wheel_lock_iid.py: LKI (renamed from LK, which rule30_locked_core_lock.py already uses), does column 1 next to the clamped 0101 wall lock onto the wheel when the right half is
an INFINITE fair random row, as it does for finite right halves (Cloud's RV, RV2, RD)? Bears on GPT's GC563 (the
history-conditioned prediction error beta_n of the fair ensemble) and on row 6.1. Local's run; predictions pushed
before it.

RUN-ON:     cpu, Python standard library, a few minutes
COMMAND:    python3 tests/probes/lexicon/rule30_wheel_lock_iid.py

Model: Cloud's RV coding (bit i = site i, wall white at even times). An "infinite" row is a fair random row of width
T + 8: the cone of site 1 at time T reaches site T + 1, so the zero tail beyond never touches the observed column. A
time t is "on the wheel" when column 1 agrees with some rotation of the period-56 wheel U on a stretch of at least 56
consecutive steps containing t (Cloud's departures() lock rule). T = 2000; the window measured is t = 1000 .. 1999.

PREDICTIONS (Local's, published before the run):
  LKI-C1 (control): finite random right halves of width 16 .. 64 (RV's ensemble) spend most of the window on the wheel
         (at least 0.7 of the time), as RD's chained locks imply.
  LKI-P1 (blind, confidence 0.5): infinite fair rows also spend at least half of the window on the wheel, averaged
         over 200 rows.
  LKI-P2 (blind, confidence 0.5): the empirical entropy of visible 8-blocks starting at even times 1000 .. 1984, pooled
         over the 200 infinite rows, is below 0.3 bits per symbol (the support language's count growth gives about
         0.44 at length 10, GC502 and RRL).
  D1 (descriptive): the same two numbers at window 200 .. 399, to see whether the ensemble is still settling.
Counterfactual: if infinite rows rarely lock, the fresh randomness arriving from the right keeps the wall region
unlocked, the wheel is a property of finite right halves, and GC563's beta need not tend to zero.
OUTCOME, 2026-10-08 18:07 (M5, one run at commit 0981b01, 2.3 s): LKI-C1 PASS (finite rows on the wheel 0.932 of the
window). LKI-P1 HELD: infinite fair rows are on the wheel 0.953 of t = 1000 .. 1999 (D1: already 0.941 at 200 .. 399).
LKI-P2 REFUTED: pooled 8-block entropy 0.390 bits per symbol, but the test was ill-chosen, since pooling over the
wheel's 28 visible phases measures phase variety, not unpredictability. Post-hoc and exploratory (400 fresh infinite
rows, visible symbols at even t = 1000 .. 1998): the conditional entropy H_(k+1) - H_k of the next symbol given the
last k is 0.67, 0.61, 0.147, 0.132, 0.116, 0.099, 0.099, 0.084, 0.083, 0.082, 0.080 bits at k = 1, 2, 4, 8, 12, 16,
20, 24, 28, 32, 40, still drifting down slowly; the distinct k-blocks number 18, 32, 56, 101, 171 at k = 8, 16, 24,
32, 40.
"""
import math
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P = 56
T = 2000


def column1(right, n):
    row, out = right << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) & 1)
    return out


def on_wheel(c1):
    flag = [0] * len(c1)
    t, n = 0, len(c1)
    while t + P <= n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        for u in range(t, s):
            flag[u] = 1
        t = s
    return flag


def block_entropy(cols, lo, hi, k=8):
    cnt = Counter()
    for c1 in cols:
        for t in range(lo, hi - 2 * k + 2, 2):
            cnt[tuple(c1[t + 2 * j] for j in range(k))] += 1
    tot = sum(cnt.values())
    return -sum(v / tot * math.log2(v / tot) for v in cnt.values()) / k


def measure(rows, lo, hi):
    cols = [column1(r, T) for r in rows]
    frac = sum(sum(on_wheel(c)[lo:hi]) for c in cols) / (len(cols) * (hi - lo))
    return frac, block_entropy(cols, lo, hi)


def main():
    rng = random.Random(20261008)
    finite = [rng.getrandbits((16, 24, 32, 48, 64)[i % 5]) | 1 for i in range(200)]
    infinite = [rng.getrandbits(T + 8) for _ in range(200)]
    f_frac, f_h = measure(finite, 1000, 2000)
    print('LKI-C1', 'PASS' if f_frac >= 0.7 else 'FAIL', 'finite rows on the wheel %.3f, block entropy %.3f' % (f_frac, f_h))
    i_frac, i_h = measure(infinite, 1000, 2000)
    print('infinite rows: on the wheel %.3f, 8-block entropy %.3f bits/symbol' % (i_frac, i_h))
    print('LKI-P1', 'HELD' if i_frac >= 0.5 else 'REFUTED')
    print('LKI-P2', 'HELD' if i_h < 0.3 else 'REFUTED')
    e_frac, e_h = measure(infinite, 200, 400)
    print('D1 window 200 .. 399: on the wheel %.3f, 8-block entropy %.3f' % (e_frac, e_h))


if __name__ == '__main__':
    main()
