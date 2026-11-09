#!/usr/bin/env python3
"""local_trap_real_rows.py (Local, 9 November 2026; L1611 S-16 block, P-L2): do real trapped right halves fill the
relaxed eventual gap languages of the gate trap?

Usage: python3 local_trap_real_rows.py KIT_DIR ROWS HORIZON SKIP MAXGAPS SEED

Real rows: ROWS random right halves of support at most 30 (bit i = cell i + 1, the top cell black), driven by the kit's
alternating column (black at even times), run exactly with Python integers to time HORIZON. u is cell 1 at odd
times. A row's first odd-time window (cells 1..16) in the kit's 829-window trap is its entry; its black cells of u at
or after entry give its gap word, from which the first SKIP gaps are dropped (the start transient, longer than the
core's convergence in the relaxed graphs). All factors of up to MAXGAPS gaps are collected over all trapped rows.

Relaxed languages: for W = 18, 26, 28, the eventual automaton of local_trap_eventual_dfa.py (the recurrent core of the
width-W lift and its path sets). It prints, per length n <= MAXGAPS: the number of words the width-W eventual
language accepts, how many of them real rows show, and how many real factors the language rejects (must be 0).

PREDICTION (L1611 P-L2, before this ran): real rows show at least 95% of the width-26 eventual words up to 10 gaps,
and none of its forbidden words. Counterfactuals: below 80% (the relaxed graphs overstate the real language), or any
rejected real factor (the lift or the code is wrong).
Result (seed 2, 1,500 rows, horizon 6001, skip 16): no rejected factor at widths 18, 26, 28 (HELD); coverage of
the width-26 eventual words 35/35 at 8 gaps, 51/53 at 9, 71/79 at 10 (MISSED the 95%, above the 80% counterfactual).
local_trap_real_freq.py then shows the missing words are rare rather than absent.
"""
import random
import re
import sys
import time
from pathlib import Path

import numpy as np

KIT, ROWS, HOR, SKIP, MG, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TL = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
TSET = set(TL)
TRAP = np.array(TL, dtype=np.int64)

# --- real rows ---------------------------------------------------------------------------------------------
rng = random.Random(SEED)
facts = {}
t0 = time.time()
trapped = 0; entry_times = []; gaps_total = 0
for r in range(ROWS):
    row = rng.getrandbits(29) | (1 << 29)          # support at most 30, cell 30 black
    entered = False; us = []
    for t in range(HOR + 1):
        if t % 2 == 1:
            if not entered and (row & 0xFFFF) in TSET:
                entered = True; entry_times.append(t)
            if entered:
                us.append(row & 1)
        c = 1 if t % 2 == 0 else 0
        row = ((row << 1) | c) ^ (row | (row >> 1))
    if not entered:
        continue
    trapped += 1
    bl = [i for i, b in enumerate(us) if b]
    g = [b - a for a, b in zip(bl, bl[1:])][SKIP:]
    gaps_total += len(g)
    for n in range(1, MG + 1):
        S = facts.setdefault(n, set())
        for i in range(len(g) - n + 1):
            S.add(tuple(g[i:i + n]))
print(f'real rows: {ROWS} drawn, {trapped} entered the trap by {HOR}, median entry {sorted(entry_times)[len(entry_times) // 2] if entry_times else None}, '
      f'{gaps_total} gaps after skipping {SKIP} per row; {time.time() - t0:.0f} s', flush=True)
assert all(set(x) <= {3, 5} for x in facts[1]), facts[1]


# --- relaxed eventual automata --------------------------------------------------------------------------
def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def eventual_accepts(W):
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64); k = 0
    for a in (0, 1):
        for b in (0, 1):
            succ[:, k] = order[np.searchsorted(sl, step(step(lift, 0, a, W), 1, b, W))]; k += 1
    head = (lift & 1).astype(bool)

    def gap(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool); nxt[succ[S].ravel()] = True
            S = np.flatnonzero(nxt & (head == (j == g - 1)))
            if len(S) == 0:
                break
        return S
    B = np.flatnonzero(head)
    while True:
        B2 = np.union1d(gap(B, 3), gap(B, 5))
        if len(B2) == len(B):
            break
        B = B2
    acc = {0: {(): B}}
    for n in range(1, MG + 1):
        acc[n] = {}
        for w, S in acc[n - 1].items():
            for g in (3, 5):
                T = gap(S, g)
                if len(T):
                    acc[n][w + (g,)] = T
    return {n: set(acc[n]) for n in range(1, MG + 1)}


for W in (18, 26, 28):
    A = eventual_accepts(W)
    line = []
    for n in range(1, MG + 1):
        a = A[n]; f = facts.get(n, set())
        line.append(f'{n}:{len(a & f)}/{len(a)} rej {len(f - a)}')
    print(f'W={W}: shown/accepted, rejected real factors, by gaps -> ' + '; '.join(line), flush=True)
    n = MG
    miss = sorted(A[n] - facts.get(n, set()))[:5]
    print(f'   e.g. accepted but never shown at {n} gaps: {["".join(map(str, w)) for w in miss]}', flush=True)
