#!/usr/bin/env python3
"""local_phase_lock.py (Local, 9 November 2026; S-16 construction, step 1d): are the 3s of trapped rows locked to a
phase sublattice, and is the sparser code with runs of 3 and 5 only physically complete?
Usage: python3 local_phase_lock.py KIT_DIR ROWS HORIZON SEED KMAX

For each trapped row (same rows and conventions as local_run_grammar.py), the sample positions of its 3s after the
16-gap skip, taken relative to its first 3 there. Prints the distribution of these offsets modulo 2, 4, 8 and 16,
pooled over rows. Then the run sequences restricted to runs in {3, 5}: per length k, how many of the 2^k sequences
of k consecutive runs, each 3 or 5, occur as k consecutive internal runs somewhere.

PREDICTION (written before this ran; clock read 22:03:22 UTC): offsets are strongly concentrated mod 2 (at least 85%
on one residue, since odd runs make even distances), and still concentrated mod 4 but less; and every {3, 5} run
sequence occurs up to k = 10. Counterfactual: no concentration beyond mod 2 (then the (4, 4) predecessor rule is not
a phase law), or some {3, 5} sequence of length at most 8 never occurs (then the sparser code is not complete either).
Result (started 22:03:43 UTC): MISSED on both. Offsets are uniform mod 2, 4, 8, 16 (0.519 / 0.481 mod 2), and the
{3, 5} run code is complete only to length 4: (5, 5, 5, 5, 5) never occurs.
"""
import collections
import itertools
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, SEED, KMAX = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
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
res = {m: collections.Counter() for m in (2, 4, 8, 16)}
seen = {k: set() for k in range(1, KMAX + 1)}
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    g = g[16:]
    pos, t = [], 0
    for x in g:
        if x == 3:
            pos.append(t)
        t += x
    if not pos:
        continue
    for p in pos:
        for m in res:
            res[m][(p - pos[0]) % m] += 1
    runs = [(b - a - 3) // 5 if False else None for a, b in zip(pos, pos[1:])]
    threes = [i for i, x in enumerate(g) if x == 3]
    runs = [b - a - 1 for a, b in zip(threes, threes[1:])]
    for k in range(1, KMAX + 1):
        for i in range(len(runs) - k + 1):
            w = runs[i:i + k]
            if all(v in (3, 5) for v in w):
                seen[k].add(tuple(w))
for m in res:
    tot = sum(res[m].values())
    print(f'offsets of 3s mod {m:2d}: ' + ', '.join(f'{k}:{res[m][k] / tot:.3f}' for k in sorted(res[m])))
for k in range(1, KMAX + 1):
    miss = sorted(set(itertools.product((3, 5), repeat=k)) - seen[k])
    print(f'   {{3,5}} run sequences of length {k:2d}: {len(seen[k]):5d} of {2 ** k:5d}; missing e.g. {miss[:3]}')
