#!/usr/bin/env python3
"""local_trap_353_decay.py (Local, 9 November 2026): does the factor 353 die out of real trapped rows over time?

Usage: python3 local_trap_353_decay.py KIT_DIR ROWS HORIZON BIN SEED

Hypothesis H-inf: the limit of the trap's eventual gap languages as the width grows is the free code {5, 3555}*,
the FACTOR CLOSURE of the code, whose every internal run of 5s between 3s has length at least three; every word containing
353 eventually dies. Real trapped rows lie in every width's lift, and a width's eventual language applies after a
finite number of gaps, so under H-inf a row's 3s would, late enough, all be followed by at least three 5s.

 It runs ROWS random right halves of EXACT support 30 (the kit's alternating column, exact integers, as
local_trap_real_rows.py) to time HORIZON, and the empty right half, takes each row's gaps from its first black head
at or after entry into the kit's trap, and reports per bin of BIN gaps after entry: the number of rows still
showing a 3 in the observed bin, the number of 3s, and the fraction of 3s followed by 5 then 3
(the factor 353). It also prints the empty right half's 353 count and the gap index of its last 353.

PREDICTION (written before the first run; clock read 21:51:59 UTC): 353 per 3 falls with time after entry but does
not reach zero within the horizon: above 0.001 in the last bin, among rows still showing 3s. Positive finite-time
counts do not refute the asymptotic H-inf; its hypothetical cutoff may lie beyond the horizon. Counterfactual: the fraction falls to 0 in the late bins
while rows still show 3s (strong support for H-inf, and the code would be the limit language), or it stays flat
(no width effect visible in real rows at all).
Result (started 21:52:20 UTC): MISSED; the second counterfactual happened. 353 per 3 is flat, 0.0126, 0.0119,
0.0123, 0.0120 in the four full bins up to 2,000 gaps after entry (all581 trapped rows show a3 in each full bin); the
empty right half shows 353 three times, last at gap 1498. This is a finite-time observation, not a limit-language
or entropy conclusion. GC2800: no trajectories or historical output are changed by these wording corrections.
"""
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, BIN, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
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
nb = 0
stats = {}
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    for i in range(len(g) - 2):
        if g[i] != 3:
            continue
        b = i // BIN
        st = stats.setdefault(b, [set(), 0, 0])
        st[0].add(r); st[1] += 1
        if g[i + 1] == 5 and g[i + 2] == 3:
            st[2] += 1
print(f'{ROWS} rows, horizon {HOR}; bins of {BIN} gaps after entry: bin, rows showing a 3, 3s, 353 per 3')
for b in sorted(stats):
    rows, n3, n353 = stats[b]
    print(f'   {b * BIN:6d}-{(b + 1) * BIN - 1:6d}: {len(rows):5d} rows, {n3:7d} 3s, 353/3 = {n353 / n3:.5f}')
g = gaps_of(0, HOR)
pos = [i for i in range(len(g) - 2) if g[i] == 3 and g[i + 1] == 5 and g[i + 2] == 3]
print(f'empty right half: {len(g)} gaps, {g.count(3)} 3s, {len(pos)} occurrences of 353, last at gap {pos[-1] if pos else None}')
