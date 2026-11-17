#!/usr/bin/env python3
"""local_code_witness.py (Local, 9 November 2026; S-16 construction attempt, step 1): which words of the free code
{A = 5, B = 3555} do real trapped right halves realize?

Usage: python3 local_code_witness.py KIT_DIR ROWS HORIZON KMAX SEED

A realized code word is an exact physical witness: a finite right half, run exactly beside the kit's alternating
column, whose head gaps after entry into the kit's trap contain the word as a factor starting at a black head. Unlike
acceptance by a relaxed width-W graph, which certifies a physical row only for durations below (W - 16)/2 samples,
this needs no width argument. For the record, a code factor here must start at a 3 or at a block boundary: the
gaps are parsed greedily into A and B blocks from every position where a block can start (a 5 always starts an A;
a 3 must be followed by 5, 5, 5 to start a B), and the k-block words seen are collected.

It prints, per k, the number of distinct k-block code words seen against 2^k, and the longest run A^n followed by B.

PREDICTION (written before the first run; clock read 21:59:45 UTC): all 2^k code words appear for k <= 8;
coverage falls below 100% at some k <= 12 only by rarity; and runs A^n B appear with n of at least 20.
Counterfactual: some short code word (k <= 6) never appears in a million gaps, which would point to a physical
obstruction that the relaxed widths to 30 do not see, and against G1' at every width.
Result (started 22:00:07 UTC): all code words realized up to k = 7; at k = 8, 248 of 256 (MISSED); longest A^n B with
n = 55 (HELD). The missing words are B-dense.
"""
import random
import re
import sys
from pathlib import Path

KIT, ROWS, HOR, KMAX, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
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


def blocks_from(g, i, kmax):
    """Parse up to kmax code blocks starting at gap index i; return the block string."""
    out = []
    while len(out) < kmax and i < len(g):
        if g[i] == 5:
            out.append('A'); i += 1
        elif g[i] == 3 and i + 3 < len(g) and g[i + 1] == g[i + 2] == g[i + 3] == 5:
            out.append('B'); i += 4
        else:
            break
    return ''.join(out)


rng = random.Random(SEED)
seen = {k: set() for k in range(1, KMAX + 1)}
longest = 0; total = 0
for r in range(ROWS):
    g = gaps_of(rng.getrandbits(29) | (1 << 29), HOR)
    if g is None:
        continue
    g = g[16:]
    total += len(g)
    run = 0
    for i, x in enumerate(g):
        if x == 5:
            run += 1
        else:
            if run and i + 3 < len(g) and g[i + 1] == g[i + 2] == g[i + 3] == 5:
                longest = max(longest, run)
            run = 0
        if x == 5 or x == 3:
            b = blocks_from(g, i, KMAX)
            for k in range(1, len(b) + 1):
                seen[k].add(b[:k])
print(f'{ROWS} rows, horizon {HOR}, {total} gaps after skipping 16 per row')
for k in range(1, KMAX + 1):
    missing = sorted(set(''.join(w) for w in __import__('itertools').product('AB', repeat=k)) - seen[k])
    print(f'   k={k:2d}: {len(seen[k]):5d} of {2 ** k:5d} code words seen; missing e.g. {missing[:4]}')
print(f'longest run A^n followed by B: n = {longest}')
