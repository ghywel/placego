#!/usr/bin/env python3
"""local_trap_ladder.py (Local, 9 November 2026): the gate trap lifted to widths W = 16, 18, 20, 22, and the gap
language at each width, to decide how much S-16 is (one more forbidden word, or a ladder with structure).

Usage: python3 local_trap_ladder.py KIT_DIR [WMAX] [NGAPS]

The lift at width W: every window of columns 1..W at an odd time whose first 16 columns are a window of the kit's
trap. It is closed under the double step with column W + 1 free at both steps (its 16-column prefix moves by the kit's
step2 with the window's own column 17), and a right half in the trap is in it at every width. For each W: the minimal
forbidden gap words over 3 and 5 up to NGAPS gaps (forbidden, with the word minus its first gap and the word minus its
last gap allowed), the number of allowed words by length, and a growth estimate.

PREDICTION, written before the first run (20:13 UTC). (1) The ladder keeps adding words: width 20 adds at least one
minimal forbidden word beyond 3535353 within 16 gaps, among the backlog's candidates 353555535353 or 553535555353 or
words of the same shape (3s separated by runs of 5s). (2) The language keeps positive growth at every width (the
period-5 lock inside the trap reads 5555... forever, and mixtures with isolated 3s survive), so the per-sample entropy
falls with W but stays well above zero (above 0.08 bit at W = 22). Counterfactual for (1): no new word at 20 or 22,
which would make S-16 a finished one-word follow-up; for (2): the growth collapses towards 1, which would make the
eventual language thin and the left statement Q01GapWords far weaker than its kit form, a much bigger S-16.

Record searched: L1608, GC2789, CL760 (the 18-column death of 3535353, three implementations); SW02-RESULTS CP-2.2
(tail entropy at most 0.12707); SW02-BACKLOG CP-2 (the family 33, 3553, 3535353, 353555535353, 553535555353 and the
question of a structural law); Lee R30-20261030-60990f (18-cell pool). No width ladder of the trap's gap language is
in the record or the kit.
"""
import math
import re
import sys
import time
from pathlib import Path

import numpy as np

KIT = Path(sys.argv[1])
WMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 22
NG = int(sys.argv[3]) if len(sys.argv) > 3 else 16
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = np.array([int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))],
                dtype=np.int64)


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


for W in range(16, WMAX + 1, 2):
    t0 = time.time()
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    idx = {int(w): i for i, w in enumerate(lift)} if W <= 18 else None
    # successor table over lift positions, via a sorted lookup
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64)
    k = 0
    for a in (0, 1):
        for b in (0, 1):
            v = step(step(lift, 0, a, W), 1, b, W)
            pos = np.searchsorted(sl, v)
            assert np.all(sl[np.minimum(pos, len(sl) - 1)] == v), 'lift not closed'
            succ[:, k] = order[pos]; k += 1
    head = (lift & 1).astype(bool)

    def after_gap(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool)
            nxt[succ[S].ravel()] = True
            want = (j == g - 1)
            S = np.flatnonzero(nxt & (head == want))
            if len(S) == 0:
                return S
        return S

    allowed = {(): np.flatnonzero(head)}
    frontier = [()]
    forb = []
    for n in range(1, NG + 1):
        nxt_f = []
        for wd in frontier:
            for g in (3, 5):
                v = wd + (g,)
                S = after_gap(allowed[wd], g)
                if len(S):
                    allowed[v] = S; nxt_f.append(v)
                else:
                    forb.append(v)
        frontier = nxt_f
    minimal = [v for v in forb if v[1:] in allowed]
    cnt = [sum(1 for v in allowed if len(v) == n) for n in range(NG + 1)]
    # growth per sample from words by sample length L = sum of gaps: count allowed words of sample length in a band
    bylen = {}
    for v in allowed:
        bylen[sum(v)] = bylen.get(sum(v), 0) + 1
    print(f'W={W}: lift {len(lift)} windows, closed; {time.time() - t0:.1f} s', flush=True)
    print('   minimal forbidden up to', NG, 'gaps:', [''.join(map(str, v)) for v in minimal], flush=True)
    print('   allowed words by number of gaps:', cnt, flush=True)
    print('   gap-count growth ratios (last four):', [round(cnt[n + 1] / cnt[n], 4) for n in range(NG - 4, NG)], flush=True)
    L1, L2 = 3 * NG - 18, 3 * NG          # sample lengths whose allowed words all have at most NG gaps
    c1, c2 = bylen.get(L1, 0), bylen.get(L2, 0)
    print(f'   allowed words of sample length {L1} and {L2}: {c1}, {c2}; growth estimate',
          round(math.log2(c2 / c1) / (L2 - L1), 4) if c1 and c2 else None, 'bit per sample', flush=True)
