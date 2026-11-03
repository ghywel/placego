#!/usr/bin/env python3
"""L1378 (Local, 2026-11-03): carrying check of GC2458's endpoint-free budget 44R + 8C <= t.
Run: python3 tests/probes/budget_check.py POTENTIALS.json HEXBITS TMAX

B1 inside the S = 13 strip model (independent step), from every start in M (phase 3, h = -385): the maximum over all
   input paths of 44R + 8C after t ticks, for t = 1..TMAX, where R counts re-anchorings and C counts visits at times
   s < t to the three cost-56 states (0, 2258), (1, 5982), (1, 8030); the budget requires max <= t.
B2 sharpness on the retained specimen from t = 431 (state rho, anchor -68): its falls at relative times 44 and 88,
   and its leftmost difference at relative times 43 and 87 (GC2458: anchor + 1).
"""
import json
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
S = 13


def step(ph, s, u):
    cells = [TAB[(2 + i) % 7][ph] for i in (-1, 0)] + [(s >> j) & 1 for j in range(S)] + [u]
    new = [cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(cells) - 1)]
    ph2 = (ph + 1) % 4
    if new[0] != TAB[2][ph2]:
        strip = [TAB[(2 + i) % 7][ph2] for i in range(-6, 0)] + new[0:S - 6]
        return ph2, sum(b << j for j, b in enumerate(strip)), -7
    return ph2, sum(b << j for j, b in enumerate(new[1:])), 0


h = json.load(open(sys.argv[1]))['pi']
TMAX = int(sys.argv[3])
COST = {(0, 2258), (1, 5982), (1, 8030)}
M = [w for w in range(1 << S) if w & 255 == 159 and h[3 * (1 << S) + w] == min(h)]
succ = {}
worst_slack = None
cur = {(3, w): 0 for w in M}                         # state -> max (44R + 8C) so far
for t in range(1, TMAX + 1):
    nxt = {}
    for (ph, s), val in cur.items():
        add_c = 8 if (ph, s) in COST else 0
        for u in (0, 1):
            ph2, s2, d = step(ph, s, u)
            v = val + add_c + (44 if d < 0 else 0)
            if nxt.get((ph2, s2), -1) < v:
                nxt[(ph2, s2)] = v
    cur = nxt
    m = max(cur.values())
    slack = t - m
    worst_slack = slack if worst_slack is None else min(worst_slack, slack)
    if t in (43, 44, 87, 88, 100, 150, TMAX):
        print('B1 t=%d: max 44R + 8C over all paths from M = %d (slack %d); reachable states %d' % (t, m, slack, len(cur)))
print('B1 minimum slack over t = 1..%d: %d (the budget requires >= 0)' % (TMAX, worst_slack))
bits = int(sys.argv[2], 16)
LO, HI = -900, 1300
g = [TAB[x % 7][0] if x < 0 else ((bits >> x) & 1 if x < 1200 else 0) for x in range(LO, HI + 1)]
lo = LO
for t in range(431 + 89):
    if t in (474, 475, 518, 519):
        L = next(x for x in range(lo + 1, lo + len(g) - 1) if g[x - lo] != TAB[x % 7][t % 4])
        print('B2 t=%d (relative %d): leftmost difference %d' % (t, t - 431, L))
    g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]
    lo += 1
print('BUDGET_DONE')
