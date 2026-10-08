#!/usr/bin/env python3
"""rule30_local_review_g237.py: LR4, Local's second reading of GPT's G237 (GC549 checkpoint 32): a white-time row
beginning 000010 forces 101100, 00101, 01001, 00000, 100 at the next five even samples, whatever the farther sites;
and all four of L288's cylinders (11100 then 001000, 001010, 001011 or 001100) reach 000010 at time 8. Row Q6. The
five arrows are read by hand in L292; this probe replays both finite claims in Local's numpy coding. Predictions
pushed before the run.

RUN-ON:     cpu, numpy, seconds
COMMAND:    python3 tests/probes/lexicon/rule30_local_review_g237.py

PREDICTIONS (Local's, published before the run):
  LR4-P1 (confidence 0.95): every completion of 000010 to 20 sites shows the five displayed prefixes at times 2 .. 10.
  LR4-P2 (confidence 0.9): every completion of each of the four cylinders to 25 sites has sites 1 .. 6 = 000010 at
         time 8.
  LR4-C1 (control, the method can fail): the prefix 000011 does not give 101100 at time 2 on every completion.
OUTCOME: not yet run.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rule30_local_review_cylinders import step


def completions(fixed, W):
    free = W - len(fixed)
    idx = np.arange(1 << free, dtype=np.int64)
    rows = np.zeros((1 << free, W), np.uint8)
    rows[:, :len(fixed)] = fixed
    for b in range(free):
        rows[:, len(fixed) + b] = (idx >> b) & 1
    return rows


def prefixes(x, times, lengths):
    seen = {}
    for t in range(max(times)):
        x = step(x, t)
        if t + 1 in times:
            L = lengths[times.index(t + 1)]
            seen[t + 1] = {''.join(map(str, r[:L])) for r in x}
    return seen


def main():
    want = ['101100', '00101', '01001', '00000', '100']
    seen = prefixes(completions([0, 0, 0, 0, 1, 0], 20), [2, 4, 6, 8, 10], [len(w) for w in want])
    p1 = all(seen[2 * (i + 1)] == {w} for i, w in enumerate(want))
    print('LR4-P1', 'HELD' if p1 else 'REFUTED', {t: sorted(v)[:3] for t, v in seen.items()})
    p2 = True
    for tail in ('001000', '001010', '001011', '001100'):
        s = prefixes(completions([1, 1, 1, 0, 0] + [int(c) for c in tail], 25), [8], [6])
        p2 &= s[8] == {'000010'}
        print(tail, sorted(s[8]))
    print('LR4-P2', 'HELD' if p2 else 'REFUTED')
    c = prefixes(completions([0, 0, 0, 0, 1, 1], 20), [2], [6])
    print('LR4-C1', 'PASS' if c[2] != {'101100'} else 'FAIL', sorted(c[2]))


if __name__ == '__main__':
    main()
