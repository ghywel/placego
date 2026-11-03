#!/usr/bin/env python3
"""L1420 (Local, 2026-11-03): NIGHT-TASKS A4 data. Rebuild closed_set.py's moving-anchor closure for one ring background
and alignment, and certify the front law by integer potentials instead of the recurrent-part DP.
Run: python3 tests/probes/wolfram/a4_closure_export.py NAME P S W [R S0] [OUT.json]

Transitions, start state and phase bookkeeping are copied from closed_set.py (with GC2394's corrected phase): state
(t mod q, (t - A) mod N, strip of the W cells right of the anchor A). Edge weight w = P * motion + (P - S), motion -1 (retreat)
or 0. The law's slope is (S - P)/P per step, so every cycle of the closure must have weight 0. Then Bellman-Ford gives two
integer potentials with  lo(s') - lo(s) <= w  and  hi(s') - hi(s) >= w  on every edge, and for every path from the start,
  lo(end) - lo(start) <= sum w <= hi(end) - hi(start),
so |P (A(t) - A(t0)) + (P - S)(t - t0)| <= C with C = max over states of max(|lo - lo0|, |hi - hi0|).
Prints the closure size, the cycle-weight check, C, the start state and whether every state's strip holds a mismatch.
"""
import json
import sys
from collections import deque

import numpy as np

name, P, S, W = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
WORDS = {'G8': '1000', 'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000'}
y = np.array([int(c) for c in WORDS[name]], dtype=np.uint8); N = len(y)
cst = lambda s: s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y):
    orb.append(cur.copy()); cur = cst(cur)
orb = [tuple(int(v) for v in o) for o in orb]; q = len(orb)
rule = lambda a, b, c: a ^ (b | c)
E = lambda x, t, r, s: orb[(t + s) % q][((t - x) + r) % N]


def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n


def transitions(state, r, s):
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s) % q][((dq + dt - i) + r) % N]
    outs = []
    for b in (0, 1):
        cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
        new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
        if new[0] != Eb(0, 1):
            ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
        else:
            ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
        Enew = lambda i: orb[(tq + 1 + s) % q][((ndq - i) + r) % N]
        if not any(ns[i] != Enew(i + 1) for i in range(len(ns))):
            return None
        outs.append((((tq + 1) % q, ndq, ns), mv))
        if mv == -1:
            break
    return outs


def start_state(r, s, t0, T=400):
    WL = 2 * T + 100; WR = T + 60; c = WL
    bg = np.array([E(x, 0, r, s) for x in range(-WL, WR)], dtype=np.uint8)
    pert = bg.copy(); pert[c] = 1; pert[c + 1:] = 0
    a, bb = bg.copy(), pert.copy()
    for _ in range(t0):
        a, bb = step(a), step(bb)
    d = np.flatnonzero(a ^ bb); xB = int(d.min()) - c - 1
    assert xB >= -(t0 + 1) and xB + W < WR - t0
    assert all(int(bb[c + x]) == E(x, t0, r, s) for x in range(-(WL - t0), xB + 1))
    return (t0 % q, (t0 - xB) % N, tuple(int(v) for v in bb[c + xB + 1: c + xB + 1 + W])), xB


def closure(r, s, start, cap=60000):
    seen = {start: 0}; order = [start]; edges = {}; dq_ = deque([start])
    while dq_:
        st = dq_.popleft(); outs = transitions(st, r, s)
        if outs is None:
            return None, None
        edges[st] = outs
        for nst, _ in outs:
            if nst not in seen:
                seen[nst] = len(order); order.append(nst); dq_.append(nst)
                if len(order) > cap:
                    return None, None
    return order, edges


def potentials(order, edges, sign):
    """Bellman-Ford from the start: sign = +1 gives lo (shortest), -1 gives hi (longest). None if a nonzero cycle exists."""
    idx = {st: i for i, st in enumerate(order)}
    INF = 10 ** 18
    d = [INF] * len(order); d[0] = 0
    for it in range(len(order) + 1):
        changed = False
        for st, outs in edges.items():
            if d[idx[st]] == INF:
                continue
            for nst, mv in outs:
                w = sign * (P * mv + (P - S))
                if d[idx[st]] + w < d[idx[nst]]:
                    d[idx[nst]] = d[idx[st]] + w; changed = True
        if not changed:
            return [sign * v for v in d]
    return None


als = [(int(sys.argv[5]), int(sys.argv[6]))] if len(sys.argv) > 6 else [(r, s) for r in range(N) for s in range(q)]
for (r, s) in als:
    st0, A0 = start_state(r, s, 300)
    order, edges = closure(r, s, st0)
    if order is None:
        continue
    lo = potentials(order, edges, +1); hi = potentials(order, edges, -1)
    ok = lo is not None and hi is not None
    C = max(max(abs(v) for v in lo), max(abs(v) for v in hi)) if ok else None
    print('%s (P,S)=(%d,%d) W=%d alignment (r,s)=(%d,%d): start anchor A0=%d at t0=300; closure %d states, %d edges; '
          'zero-weight cycles (both potentials exist): %s; C = %s' % (
              name, P, S, W, r, s, A0, len(order), sum(len(v) for v in edges.values()), ok, C), flush=True)
    if len(als) > 1 and len(order) > 600:
        continue
    if len(sys.argv) > 7 and ok:
        data = {'name': name, 'P': P, 'S': S, 'W': W, 'r': r, 's': s, 'N': N, 'q': q, 'orb': orb, 't0': 300, 'A0': A0,
                'states': [[st[0], st[1], list(st[2])] for st in order],
                'edges': [[order.index(st), [[order.index(n), mv] for n, mv in outs]] for st, outs in edges.items()],
                'lo': lo, 'hi': hi, 'C': C}
        json.dump(data, open(sys.argv[7], 'w'))
        print('wrote', sys.argv[7])
    if len(als) > 1 and ok:
        break
print('A4_EXPORT_DONE')
