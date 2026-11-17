#!/usr/bin/env python3
"""local_b_lock.py (Local, 9 November 2026; S-16 construction, step 1e): do trapped rows fall into (3555)^inf?
Usage: python3 local_b_lock.py KIT_DIR ROWS HORIZON SEED

For each trapped row (same conventions as local_run_grammar.py), its tail at the horizon: (3,5,5,5)-periodic over
its last 200 gaps, all 5s over its last 200 gaps (the period-5 lock), or neither. For rows ending (3555)^inf, the gap
index at which the periodic tail starts. Then the run statistics of the rows in neither class only.

PREDICTION (written before this ran; clock read 22:04 UTC, see the launch line): at least 30% of trapped rows end in
(3555)^inf by time 8001, a few in all 5s, and among the remaining rows the over-representation of runs of 3 falls
sharply (runs of 3 below 45% of their internal runs). Counterfactual: under 5% end in (3555)^inf, so the
over-representation of BBBBBBBB is a property of the live dynamics, not of a lock.
Result (started 22:04:37 UTC): MISSED; the counterfactual happened. No trapped row ends in (3555)^inf or in all 5s.
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
cls = collections.Counter(); starts = []; live_runs = collections.Counter()
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    tail = g[-200:]
    if len(tail) == 200 and all(tail[i] == (3, 5, 5, 5)[(i - tail.index(3)) % 4] for i in range(tail.index(3), 200)) and 3 in tail[:4]:
        cls['B-lock'] += 1
        i = len(g) - 1
        k = (len(g) - 200 + tail.index(3))
        while k - 4 >= 0 and g[k - 4:k] == [3, 5, 5, 5]:
            k -= 4
        starts.append(k)
    elif len(tail) == 200 and all(x == 5 for x in tail):
        cls['A-lock'] += 1
    else:
        cls['neither'] += 1
        g2 = g[16:]
        th = [i for i, x in enumerate(g2) if x == 3]
        live_runs.update(b - a - 1 for a, b in zip(th, th[1:]))
tot = sum(cls.values())
print(f'{tot} trapped rows of {ROWS}: ' + ', '.join(f'{k} {v} ({v / tot:.3f})' for k, v in cls.items()))
if starts:
    s = sorted(starts)
    print(f'(3555)^inf tails start at gap index: median {s[len(s) // 2]}, 10th {s[len(s) // 10]}, 90th {s[9 * len(s) // 10]}')
lt = sum(live_runs.values())
print('runs in rows that are in neither class:', ', '.join(f'{k}:{v / lt:.4f}' for k, v in sorted(live_runs.items())[:10]))
