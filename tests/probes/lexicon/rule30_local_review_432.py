#!/usr/bin/env python3
"""rule30_local_review_432.py: LR2, Local's second reading of GPT's GC549 checkpoint 29: from a white even-time row
whose sites 1 .. 5 read 11100, column 1 can never show the visible word 1000010001001 (a 4-gap, a 3-gap, a 2-gap).
Row Q6 and the 3-gap question (RV3). Predictions pushed before the run.

RUN-ON:     cpu, numpy, seconds
COMMAND:    python3 tests/probes/lexicon/rule30_local_review_432.py

Local's coding (not GPT's paired map or its decimal updates): every completion of the prefix is a row of a numpy
array (one byte per site), all rows stepped together under Rule 30 with the wall clamped white at even times and
black at odd times. The first k visible symbols (site 1 at times 0, 2, .., 2k - 2) depend on sites 1 .. 2k - 1 only,
so for each target length k the count is over the 2^(2k - 6) completions of the 11100 prefix to 2k - 1 sites.

PREDICTIONS (Local's, published before the run):
  LR2-C1 (control): the prefix alone gives visible 100 (k = 3, one source), and a fresh random right half of width 64
         evolved 40 steps by this coding reproduces RV's integer coding of the same row at every step.
  LR2-P1 (confidence 0.9): no completion to 25 sites shows 1000010001001 (checkpoint 29; Cloud's RRL found the
         fourteen-symbol factor 01000010001001 absent by SAT).
  LR2-P2 (confidence 0.85): the survivor counts at k = 3 .. 13 are GPT's 1, 4, 16, 64, 256, 656, 1716, 1280, 5120,
         12000, 0.
  LR2-P3 (confidence 0.85): at k = 10 every survivor has sites 6 .. 8 equal to 001.
  Unexpected check (descriptive): at k = 12, the distinct values of sites 6 .. 11 among the 12,000 survivors.
OUTCOME: not yet run.
"""
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = [int(ch) for ch in '1000010001001']
PREFIX = [1, 1, 1, 0, 0]


def visible(rows, k):
    """rows: uint8 array [n, W] of sites 1 .. W at time 0 (wall white). Returns column 1 at times 0, 2, .., 2k - 2."""
    x = rows.copy()
    n, W = x.shape
    out = [x[:, 0].copy()]
    for t in range(2 * k - 2):
        wall = t % 2                                            # wall value at time t
        left = np.concatenate([np.full((n, 1), wall, np.uint8), x[:, :-1]], axis=1)
        right = np.concatenate([x[:, 1:], np.zeros((n, 1), np.uint8)], axis=1)
        x = left ^ (x | right)
        if t % 2 == 1:
            out.append(x[:, 0].copy())
    return np.stack(out, axis=1)


def completions(k):
    W = 2 * k - 1
    free = W - 5
    idx = np.arange(1 << free, dtype=np.int64)
    rows = np.zeros((1 << free, W), np.uint8)
    rows[:, :5] = PREFIX
    for b in range(free):
        rows[:, 5 + b] = (idx >> b) & 1
    return rows


def main():
    sys.path.insert(0, HERE)
    import rule30_three_gap_death as rv                         # RV's integer coding (Cloud's), for the control
    rng = random.Random(4321)
    right = rng.getrandbits(64)
    arr = np.array([[(right >> i) & 1 for i in range(64 + 90)]], np.uint8)
    ints = rv.rows_from(right, 41)
    x, ok = arr.copy(), True
    for t in range(40):
        left = np.concatenate([np.full((1, 1), t % 2, np.uint8), x[:, :-1]], axis=1)
        rgt = np.concatenate([x[:, 1:], np.zeros((1, 1), np.uint8)], axis=1)
        x = left ^ (x | rgt)
        ok &= all(int(x[0, i - 1]) == (ints[t + 1] >> i) & 1 for i in range(1, 100))
    v3 = visible(completions(3), 3)
    c1 = ok and v3.shape[0] == 1 and list(v3[0]) == [1, 0, 0]
    print('LR2-C1', 'PASS' if c1 else 'FAIL')
    counts, sites10, tails12 = [], None, None
    for k in range(3, 14):
        rows = completions(k)
        vis = visible(rows, k)
        keep = np.all(vis == np.array(TARGET[:k], np.uint8), axis=1)
        counts.append(int(keep.sum()))
        if k == 10:
            sites10 = {tuple(r[5:8]) for r in rows[keep]}
        if k == 12:
            tails12 = sorted({''.join(map(str, r[5:11])) for r in rows[keep]})
    print('counts k = 3 .. 13:', counts)
    print('LR2-P1', 'HELD' if counts[-1] == 0 else 'REFUTED')
    print('LR2-P2', 'HELD' if counts == [1, 4, 16, 64, 256, 656, 1716, 1280, 5120, 12000, 0] else 'REFUTED')
    print('LR2-P3', 'HELD' if sites10 == {(0, 0, 1)} else 'REFUTED', sites10)
    print('unexpected check: sites 6 .. 11 at k = 12:', tails12)


if __name__ == '__main__':
    main()
