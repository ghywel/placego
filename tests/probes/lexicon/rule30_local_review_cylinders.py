#!/usr/bin/env python3
"""rule30_local_review_cylinders.py: LR3, Local's second reading of GPT's GC549 checkpoint 31 (three of L288's four final
cylinders cannot make the closing 2-gap of 1000010001001). Row Q6. Predictions pushed before the run.

RUN-ON:     cpu, numpy, seconds
COMMAND:    python3 tests/probes/lexicon/rule30_local_review_cylinders.py

GPT's claim is universal over farther sites: for initial sites 1 .. 11 equal to 11100 followed by 001010, 001011 or
001100, every completion gives the even-time prefixes 0010100 (time 12), 010010 (14), 00000 (16) and 100 (18). With
site 2 white under a visible 1 at time 18, the hand identity b_next = b AND (q OR r) (read by Local by hand in L290)
keeps site 2 white at time 20, and GC503 then allows only a 1-gap or a 3-gap there, never the 2-gap the word needs.
Local's coding: every completion of sites 12 .. 25 (2^14 per cylinder) stepped together in numpy, the wall clamped
white at even times; time-18 sites 1 .. 3 need initial sites up to 21, so 25 sites cover every displayed prefix.

PREDICTIONS (Local's, published before the run):
  LR3-C1 (control): the stepping agrees with RV's integer coding on 200 random rows over 24 steps.
  LR3-P1 (confidence 0.9): for each of the three cylinders, every completion has the four displayed prefixes.
  LR3-P2 (confidence 0.9): over all rows of 8 sites at a white time with site 1 black, site 2 two steps later equals
         b AND (q OR r) (sites 2, 3, 4 as b, q, r), where site 1 two steps later is the next visible symbol's row.
  LR3-P3 (confidence 0.6): for 001000 the time-18 prefix is not constant over completions (GPT's unknown is genuine
         dependence, not lost cancellation). Descriptive: the distinct time-18 sites 1 .. 3 and their counts.
OUTCOME, 2026-10-08 16:02 (M5, one run at commit 57dd481, 0.5 s): LR3-C1 PASS; LR3-P1 and P2 HELD (all 2^14 completions
of each closed cylinder show 0010100, 010010, 00000, 100 at times 12 .. 18; b_next = b AND (q OR r) on every row).
LR3-P3 REFUTED: for 001000 all 16,384 completions also give time-18 prefix 100, so GPT's unknown was a lost
cancellation, not dependence, and the fourth cylinder closes like the other three. Post-hoc, exact constant prefixes
on that branch: 0000100 (time 8), 101100 (10), 00101 (12), 01001 (14), 00000 (16), 100 (18); by hand, site 6 at time
10 is 1 XOR (1 OR *) = 0 from the time-8 prefix, where the ternary run had an unknown.
"""
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
W = 25


def step(x, t):
    n = x.shape[0]
    left = np.concatenate([np.full((n, 1), t % 2, np.uint8), x[:, :-1]], axis=1)
    right = np.concatenate([x[:, 1:], np.zeros((n, 1), np.uint8)], axis=1)
    return left ^ (x | right)


def cylinder(fixed):
    free = W - len(fixed)
    idx = np.arange(1 << free, dtype=np.int64)
    rows = np.zeros((1 << free, W), np.uint8)
    rows[:, :len(fixed)] = fixed
    for b in range(free):
        rows[:, len(fixed) + b] = (idx >> b) & 1
    return rows


def main():
    sys.path.insert(0, HERE)
    import rule30_three_gap_death as rv
    rng = random.Random(9)
    ok = True
    for _ in range(200):
        r = rng.getrandbits(40)
        x = np.array([[(r >> i) & 1 for i in range(80)]], np.uint8)
        ints = rv.rows_from(r, 25)
        for t in range(24):
            x = step(x, t)
            ok &= all(int(x[0, i - 1]) == (ints[t + 1] >> i) & 1 for i in range(1, 60))
    print('LR3-C1', 'PASS' if ok else 'FAIL')
    want = {12: '0010100', 14: '010010', 16: '00000', 18: '100'}
    p1 = True
    for tail in ('001010', '001011', '001100', '001000'):
        x = cylinder([1, 1, 1, 0, 0] + [int(c) for c in tail])
        seen = {}
        for t in range(18):
            x = step(x, t)
            if t + 1 in want:
                L = len(want[t + 1])
                vals = {''.join(map(str, r[:L])) for r in x}
                seen[t + 1] = vals
        if tail != '001000':
            good = all(seen[T] == {want[T]} for T in want)
            p1 &= good
            print(tail, 'all completions match' if good else 'MISMATCH', {T: sorted(v)[:4] for T, v in seen.items()})
        else:
            pref = [''.join(map(str, r[:3])) for r in x]
            hist = {p: pref.count(p) for p in sorted(set(pref))}
            print('001000 time-18 sites 1..3:', hist)
            print('LR3-P3', 'HELD' if len(hist) > 1 else 'REFUTED')
    print('LR3-P1', 'HELD' if p1 else 'REFUTED')
    p2 = True
    for r in range(1 << 8):
        bits = [(r >> i) & 1 for i in range(8)]
        if bits[0] != 1:
            continue
        x = np.array([bits + [0] * 4], np.uint8)
        x = step(step(x, 0), 1)
        b, q, rr = bits[1], bits[2], bits[3]
        p2 &= int(x[0, 1]) == (b & (q | rr))
    print('LR3-P2', 'HELD' if p2 else 'REFUTED')


if __name__ == '__main__':
    main()
