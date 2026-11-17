#!/usr/bin/env python3
"""local_run_grammar.py (Local, 9 November 2026; S-16 construction, step 1c): the run grammar of real trapped rows.
Usage: python3 local_run_grammar.py KIT_DIR ROWS HORIZON SEED

A gap word after entry is read as its internal runs: the number of 5s between consecutive 3s. This prints the
frequency of each run length, the counts of consecutive run pairs (r, s) against an independent baseline, and the
pairs and triples that never occur among frequent runs. Same rows as local_code_freq.py (support at most 30, the
kit's alternating column, exact integers, 16 gaps skipped after entry into the kit's trap).

PREDICTION (written before this ran; clock read 22:01:33 UTC): runs 0 and 2 never occur (33, 3553 are forbidden
after entry); run 1 is rare (353 follows about 1.2% of 3s); the pair (4, 4) never occurs while (3, 3), (3, 4),
(4, 3), (4, 5), (5, 4) all do; and (1, 1, 1) never occurs (3535353). Counterfactual: (4, 4) occurs at a rate
comparable to its baseline, which would make local_code_freq.py's zeros a parsing artefact.
First run (seed 17, started 22:01:53 UTC): (4, 4) occurs 123 times against a baseline of 114, so that part MISSED
(the counterfactual); runs 0 and 2 never occur, (1, 1, 1) and (4, 4, 4) never occur, and odd runs dominate even runs.
RE-ANALYSIS PREDICTION, same seed, before the second run (clock read 22:02 UTC, see the launch line): a pair (4, 4)
is never followed by a run of 3 or more, only by a run of 1 (or by the end of the data), which would explain why every
code word containing BABAB (runs 4, 4 and then at least 3) is absent. Counterfactual: (4, 4, s) with s >= 3 occurs.
Second run (started 22:02:37 UTC): MISSED. (4, 4) is followed by runs 3 (14), 5 (35) and more, but it is preceded only
by runs 3 (67), 11 (52), 7 (2) and 12 (1): that is why (4, 4, 4) and (5, 4, 4) never occur. Odd runs 362,915, even 36,410.
"""
import collections
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TSET = {int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))}


def gaps_of(row, hor):
    entered = False; us = []
    for t in range(hor + 1):
        if t % 2 == 1:
            if not entered and (row & 0xFFFF) in TSET:
                entered = True
            if entered:
                us.append(row & 1)
        row = ((row << 1) | (1 if t % 2 == 0 else 0)) ^ (row | (row >> 1))
    if not entered:
        return None
    bl = [i for i, b in enumerate(us) if b]
    return [b - a for a, b in zip(bl, bl[1:])]


rng = random.Random(SEED)
one = collections.Counter(); two = collections.Counter(); three = collections.Counter()
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    g = g[16:]
    threes = [i for i, x in enumerate(g) if x == 3]
    runs = [b - a - 1 for a, b in zip(threes, threes[1:])]
    one.update(runs)
    two.update(zip(runs, runs[1:]))
    three.update(zip(runs, runs[1:], runs[2:]))
tot = sum(one.values()); t2 = sum(two.values())
print(f'{tot} internal runs; run-length frequencies (run: count, share):')
for k in sorted(one):
    if one[k] >= 1:
        print(f'   {k:3d}: {one[k]:8d}  {one[k] / tot:.5f}')
print('pairs (r, s) with r, s <= 7: observed / independent baseline')
for r_ in range(0, 8):
    row = []
    for s in range(0, 8):
        e = t2 * (one[r_] / tot) * (one[s] / tot)
        row.append(f'{two[(r_, s)]:>7d}/{e:>7.0f}' if e >= 1 else f'{two[(r_, s)]:>7d}/{"-":>7}')
    print(f'   r={r_}: ' + ' '.join(row))
print('triple (1,1,1):', three[(1, 1, 1)], '; triple (4,4,4):', three[(4, 4, 4)], '; pair (4,4):', two[(4, 4)])
print('runs after a pair (4, 4):', sorted((k[2], v) for k, v in three.items() if k[:2] == (4, 4)))
print('runs before a pair (4, 4):', sorted((k[0], v) for k, v in three.items() if k[1:] == (4, 4)))
print('parity: odd runs', sum(v for k, v in one.items() if k % 2), 'even runs', sum(v for k, v in one.items() if k % 2 == 0))
