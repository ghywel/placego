#!/usr/bin/env python3
"""local_trap_core18_complete.py (Local, 9 November 2026): is the eventual gap language of the gate trap at width W
exactly the shift of finite type with no 33, no 3553 and no 3535353?

Usage: python3 local_trap_core18_complete.py KIT_DIR [W ...]

Start from the recurrent core C of the width-W lift (local_trap_ladder2.py: the stable set of black windows reached
after gaps 3 and 5). Explore the product of the path-set automaton from C with the six-gap memory of the three words,
over every reachable pair; a disagreement is a word one side reads and the other does not.

PREDICTION, written before the first run (first run started 20:18:05 UTC): at W = 18, 20 and 22 the product closes with no disagreement,
so the eventual language at those widths is exactly the three-word shift (entropy 0.12707 bit per sample); at W = 16
it disagrees (3535353 is read there). Counterfactual: a disagreement at 18, a word longer than 20 gaps that the core
cannot read, in which case the 18-column eventual language is smaller than the three-word shift and S-16 needs the
longer word found first.

First run (20:18:05 UTC): HELD at all four widths (16 disagrees only on 3535353, 47 windows; 18, 20, 22 close).
ADDENDUM PREDICTION, before the second run (second run started 20:18:50 UTC): at W = 24 and 26 the product also closes with no disagreement.
Counterfactual: a disagreement there, a new eventual word, and the ladder has not stopped at 18.
Second run (20:18:50 UTC): MISSED. W = 24 disagrees twice (histories ending 5535353 and 3555353), W = 26 31 times: the
eventual language shrinks again past 22. The counterfactual happened.

Record searched: local_trap_ladder2.out (this session: the three words up to 20 gaps at 18, 20, 22), L1608's product
test at width 16 (19 states, no disagreement for the five words), SW02-RESULTS CP-2.2.
"""
import re
import sys
from pathlib import Path

import numpy as np

KIT = Path(sys.argv[1])
WS = [int(x) for x in sys.argv[2:]] or [16, 18, 20, 22]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = np.array([int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))],
                dtype=np.int64)
F = [(3, 3), (3, 5, 5, 3), (3, 5, 3, 5, 3, 5, 3)]
M = max(len(f) for f in F) - 1


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


for W in WS:
    lift = (TRAP[:, None] | (np.arange(1 << (W - 16), dtype=np.int64)[None, :] << 16)).ravel()
    order = np.argsort(lift); sl = lift[order]
    succ = np.empty((len(lift), 4), dtype=np.int64)
    k = 0
    for a in (0, 1):
        for b in (0, 1):
            v = step(step(lift, 0, a, W), 1, b, W)
            succ[:, k] = order[np.searchsorted(sl, v)]; k += 1
    head = (lift & 1).astype(bool)

    def after_gap(S, g):
        for j in range(g):
            nxt = np.zeros(len(lift), dtype=bool)
            nxt[succ[S].ravel()] = True
            S = np.flatnonzero(nxt & (head == (j == g - 1)))
            if len(S) == 0:
                break
        return S

    B = np.flatnonzero(head)
    while True:
        B2 = np.union1d(after_gap(B, 3), after_gap(B, 5))
        if len(B2) == len(B):
            break
        B = B2
    seen = {(B.tobytes(), ())}
    todo = [(B, ())]
    dis = []
    while todo and len(seen) < 200000:
        S, h = todo.pop()
        for g in (3, 5):
            S2 = after_gap(S, g)
            hh = h + (g,)
            ok = not any(len(hh) >= len(f) and hh[-len(f):] == f for f in F)
            if bool(len(S2)) != ok:
                dis.append((''.join(map(str, hh)), len(S2), ok))
            if ok and len(S2):
                key = (S2.tobytes(), hh[-M:])
                if key not in seen:
                    seen.add(key); todo.append((S2, hh[-M:]))
    print(f'W={W}: core {len(B)}; product pairs {len(seen)}{" (capped)" if todo else ""}; disagreements {len(dis)}',
          dis[:4], flush=True)
