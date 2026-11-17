#!/usr/bin/env python3
"""local_code_freq.py (Local, 9 November 2026; S-16 construction, step 1b): frequencies of the 8-block code words in
real trapped rows, against an independent-blocks baseline, to tell suppressed code words from rare ones.
Usage: python3 local_code_freq.py KIT_DIR ROWS HORIZON SEED

Same rows and parsing as local_code_witness.py, a different seed. For each 8-block code word: its count, and the
count expected if blocks were independent with the observed per-block B frequency. Prints the least and most
over-represented words, the eight words seed 5 missed, and the B frequency.

PREDICTION (written before this ran; clock read 22:00:52 UTC): the eight seed-5 misses are
strongly suppressed, not just rare: on the new seed they stay at zero or near it while the independent baseline
expects hundreds, and the suppression is concentrated on words with alternating B A B A patterns.
Counterfactual: the misses appear at counts comparable to their baseline, so seed 5's gaps were a sampling effect.
Result (started 22:00:52 UTC): HELD. Zero counts exactly for the words with runs (4, 4, 4) or (5, 4, 4), baselines 156
to 800; BBBBBBBB is 7,183 times its baseline.
"""
import collections
import itertools
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TSET = {int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))}
MISS = ['BAABABAB', 'BABAABAB', 'BABABABB', 'BABABBAB']


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


def blocks_from(g, i, k):
    out = []
    while len(out) < k and i < len(g):
        if g[i] == 5:
            out.append('A'); i += 1
        elif g[i] == 3 and i + 3 < len(g) and g[i + 1] == g[i + 2] == g[i + 3] == 5:
            out.append('B'); i += 4
        else:
            return None
    return ''.join(out) if len(out) == k else None


rng = random.Random(SEED)
cnt = collections.Counter(); one = collections.Counter()
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    g = g[16:]
    for i in range(len(g)):
        b = blocks_from(g, i, 8)
        if b:
            cnt[b] += 1; one[b[0]] += 1
tot = sum(cnt.values()); pB = one['B'] / (one['A'] + one['B'])
exp = {w: tot * pB ** w.count('B') * (1 - pB) ** w.count('A') for w in (''.join(x) for x in itertools.product('AB', repeat=8))}
ratio = sorted(((cnt.get(w, 0) / exp[w], w) for w in exp))
print(f'{tot} eight-block windows; per-block B frequency {pB:.4f}; distinct words seen {len(cnt)} of 256')
print('least over-represented ten (observed/expected, word, observed, expected):')
for r_, w in ratio[:10]:
    print(f'   {r_:.4f}  {w}  {cnt.get(w, 0)}  {exp[w]:.0f}')
print('most over-represented three:', [(round(r_, 2), w, cnt.get(w, 0)) for r_, w in ratio[-3:]])
print('seed-5 misses:', {w: (cnt.get(w, 0), round(exp[w])) for w in MISS})
