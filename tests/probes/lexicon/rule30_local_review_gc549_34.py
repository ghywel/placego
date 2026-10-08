#!/usr/bin/env python3
"""rule30_local_review_gc549_34.py: LR5, Local's second reading of GPT's GC549 checkpoint 34 (the five-zero certificate of
checkpoint 19 has a redundant first anchor), in Local's column-by-column coding (rule30_local_review_gc549.py). Row
Q6. Predictions pushed before the run.

RUN-ON:     cpu, Python standard library, under a second
COMMAND:    python3 tests/probes/lexicon/rule30_local_review_gc549_34.py

PREDICTIONS (Local's, published before the run):
  LR5-P1 (confidence 0.9): among the 89 no-11 nine-symbol words, f_14 = .. = f_17 = 0 at phase 0 only for 010101001.
  LR5-P2 (confidence 0.85): keeping the other four of the five zeros at depths 13 .. 17 and dropping depth 14, 15, 16
         or 17 leaves 8, 3, 5 and 1 words avoiding 11 and 101001 (GPT's counts).
  LR5-C1 (control): with all five zeros the no-11, no-101001 count is 0 (checkpoint 19, LR-P2).
OUTCOME: not yet run.
"""
import os
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rule30_local_review_gc549 import left_cells, no11, has


def main():
    words = [w for w in product((0, 1), repeat=9) if no11(w)]
    F = {w: left_cells(w, 0, 17)[0] for w in words}
    four = [''.join(map(str, w)) for w in words if all(F[w][j] == 0 for j in range(14, 18))]
    print('LR5-P1', 'HELD' if four == ['010101001'] else 'REFUTED', four)
    counts = []
    for drop in (14, 15, 16, 17):
        keep = [j for j in range(13, 18) if j != drop]
        counts.append(sum(1 for w in words if all(F[w][j] == 0 for j in keep) and not has(w, '101001')))
    print('LR5-P2', 'HELD' if counts == [8, 3, 5, 1] else 'REFUTED', counts)
    c1 = sum(1 for w in words if all(F[w][j] == 0 for j in range(13, 18)) and not has(w, '101001'))
    print('LR5-C1', 'PASS' if c1 == 0 else 'FAIL', c1)


if __name__ == '__main__':
    main()
