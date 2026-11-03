#!/usr/bin/env python3
"""L1439 (Local, 2026-11-03): P-h. Is the 11/81 wall on 1010000 robust under every right input?
Run: python3 tests/probes/wolfram/a4_slow_wall_closure.py DATA63.json T0 CAP PATTERN W2 [W2 ...]
For a finite perturbation PATTERN (XORed onto the background on [0, 12)), simulate exactly to T0, take A4's anchored state
(anchor F - 1, window of W2 cells), and close it under both values of the cell beyond the window (A4's transitions, the
one-way anchor). Then test for an exact potential psi(s') - psi(s) = P * motion + (P - S) with (P, S) = (81, 70): assign psi
along a BFS tree and check every edge. Prints sizes and verdicts only.
"""
import json
import sys
from collections import deque

import numpy as np

data = json.load(open(sys.argv[1])); T0 = int(sys.argv[2]); CAP = int(sys.argv[3]); PAT = int(sys.argv[4], 0)
WS = [int(w) for w in sys.argv[5:]]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
P, S = 81, 70
rule = lambda a, b, c: a ^ (b | c)
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]


def transitions(state):
    """a4_closure_export.transitions, the one-way anchor."""
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    outs = []
    for b in (0, 1):
        cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
        new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
        if new[0] != Eb(0, 1):
            ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
        else:
            ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
        Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
        if not any(ns[i] != Enew(i + 1) for i in range(len(ns))):
            return None
        outs.append((((tq + 1) % q, ndq, ns), mv))
        if mv == -1:
            break
    return outs


lo = -2 * T0 - 10; hi = T0 + 22; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
for _ in range(T0):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
d = np.flatnonzero(row ^ bg); Fi = int(d.min()); A = Fi - 1 - c
assert A - 1 > lo + T0 + 1 and A + max(WS) + 1 < hi - T0 - 1 or True
for W2 in WS:
    assert Fi + W2 < len(row) - T0 - 1, 'window beyond the exact range'
    start = (T0 % q, (T0 - A) % N, tuple(int(v) for v in row[Fi: Fi + W2]))
    seen = {start: 0}; psi = {start: 0}; order = [start]; edges = {}; dq_ = deque([start]); why = None
    while dq_:
        st = dq_.popleft(); outs = transitions(st)
        if outs is None:
            why = 'a successor loses its difference'; break
        edges[st] = outs
        for nst, mv in outs:
            if nst not in seen:
                seen[nst] = len(order); order.append(nst); psi[nst] = psi[st] + P * mv + (P - S); dq_.append(nst)
        if len(order) > CAP:
            why = 'cap %d' % CAP; break
    if why:
        print('pattern 0x%x T0=%d W=%d: closure FAILS (%s) after %d states' % (PAT, T0, W2, why, len(order)), flush=True)
        continue
    bad = sum(1 for st, outs in edges.items() for n, mv in outs if psi[n] - psi[st] != P * mv + (P - S))
    ne = sum(len(o) for o in edges.values())
    print('pattern 0x%x T0=%d W=%d: closure CLOSES with %d states, %d edges; exact 11/81 potential: %s (violating edges %d); '
          'psi range [%d, %d]' % (PAT, T0, W2, len(order), ne, bad == 0, bad, min(psi.values()), max(psi.values())), flush=True)
print('A4_SLOW_WALL_CLOSURE_DONE')
