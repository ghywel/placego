#!/usr/bin/env python3
"""local_trap_real_freq.py (Local, 9 November 2026; L1611 S-16 block): frequencies of the 10-gap factors of real
trapped rows, to tell suppressed words from rare ones. Usage: python3 local_trap_real_freq.py KIT_DIR ROWS HORIZON SKIP SEED

Same rows and conventions as local_trap_real_rows.py (support at most 30, the kit's alternating column, entry into
the kit's trap, SKIP gaps dropped), a different seed. Prints the counts of every 10-gap factor, least frequent first,
and the counts of the eight width-18 eventual words that seed 2 never showed.

PREDICTION, written before this ran (clock read 20:34:02 UTC): with 3,000 rows and a new seed, the eight words stay at zero, while
the least frequent word that does occur has a count of at least 50 (so zero is suppression, not rarity).
Counterfactual: some of the eight appear, or the shown words thin out continuously towards zero (then they are rare,
and the 90% coverage is a sample-size effect).
Result: MISSED. Two of the listed words appear once each (3535553535, 3535555553) and the low counts thin out
continuously (1, 1, 1, 3, 3, 3, 5, 5, 5, 9 in 1,769,893): the counterfactual held; these words are rare, not shown
absent. Three listed words stay at zero.
"""
import collections
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, SKIP, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TSET = {int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))}
MISSING = ['3535355553', '3535553535', '3535555353', '3535555553', '3555535353']
rng = random.Random(SEED)
cnt = collections.Counter()
for r in range(ROWS):
    row = rng.getrandbits(29) | (1 << 29)
    entered = False; us = []
    for t in range(HOR + 1):
        if t % 2 == 1:
            if not entered and (row & 0xFFFF) in TSET:
                entered = True
            if entered:
                us.append(row & 1)
        row = ((row << 1) | (1 if t % 2 == 0 else 0)) ^ (row | (row >> 1))
    bl = [i for i, b in enumerate(us) if b]
    g = ''.join(str(b - a) for a, b in zip(bl, bl[1:]))[SKIP:]
    for i in range(len(g) - 9):
        cnt[g[i:i + 10]] += 1
items = sorted(cnt.items(), key=lambda kv: kv[1])
print('distinct 10-gap factors', len(cnt), '; total', sum(cnt.values()))
print('least frequent ten:', items[:10])
print('most frequent three:', items[-3:])
print('the earlier missing words:', {w: cnt.get(w, 0) for w in MISSING})
