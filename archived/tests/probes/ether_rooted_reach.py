#!/usr/bin/env python3
"""L1364 T55 (Local, 2026-11-03): the rooted observer over the classic ether, restricted to the nodes reachable from
the starts (t mod 4, L mod 7, unknown word), where every actual disturbance begins (a half-line state); Karp's minimum
cycle mean for W = 0..12. reports/rule30-genealogy.md section 59. Run: python3 tests/probes/ether_rooted_reach.py
"""
import runpy, sys, io, contextlib
from fractions import Fraction
import os
sys.argv = ['x', '0']      # load ether_news_speed.py (its W = 0 bound and front runs print to a discarded buffer)
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ether_news_speed.py'), run_name='lib')
succ, X = g['successors'], g['X']
def graph(W):
    start = [(ph, j, (X,) * W) for ph in range(4) for j in range(7)]
    seen = {s: k for k, s in enumerate(start)}; stack = list(start); E = []
    while stack:
        u = stack.pop()
        ph, j, w = u
        for L2, w2 in succ(ph, j, w, W):
            v = ((ph + 1) % 4, L2 % 7, w2)
            if v not in seen:
                seen[v] = len(seen); stack.append(v)
            E.append((seen[u], seen[v], L2 - j))
    return seen, E
def karp(n, E):
    INF = float('inf')
    D = [[INF] * n for _ in range(n + 1)]
    D[0] = [0] * n
    for k in range(1, n + 1):
        for u, v, w in E:
            if D[k - 1][u] + w < D[k][v]:
                D[k][v] = D[k - 1][u] + w
    best = None
    for v in range(n):
        if D[n][v] == INF: continue
        m = max(Fraction(int(D[n][v] - D[k][v]), n - k) for k in range(n) if D[k][v] < INF)
        best = m if best is None or m < best else best
    return best
for W in range(0, 13):
    nodes, E = graph(W)
    mu = karp(len(nodes), E)
    print('W=%2d reachable %d nodes, %d edges: min cycle mean %s -> leftward speed bound %s' % (W, len(nodes), len(E), mu, max(Fraction(0), -mu)), flush=True)
