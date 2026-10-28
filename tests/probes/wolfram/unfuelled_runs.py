#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): how long a right-diagonal plateau can continue once every new start bit is 0.

Builds the complete reachable cap-P pair graph (as pair_graph_bits.py). From every state whose newer diagonal has least
period q, follows only the start-bit-0 child while the newer diagonal keeps period q, and reports the longest such
run for each q <= P, with the run-length distribution. Beyond a finite seed's last cell every start bit is 0, so this
bounds the part of any plateau (at period q <= P) that lies past the seed. Usage: unfuelled_runs.py P
"""
import sys, collections
P = int(sys.argv[1]); M = (1 << P) - 1
def pe(g):
    y = (g << 1) & M; k = 1
    while k < P: y ^= (y << k) & M; k <<= 1
    return y
def lp(x):
    n = P
    while n > 1:
        h = n // 2
        if all(((x >> (i * h)) & ((1 << h) - 1)) == (x & ((1 << h) - 1)) for i in range(P // h)): n = h
        else: break
    return n
start = (0, M); idx = {start: 0}; order = [start]; succ0 = []; i = 0
while i < len(order):
    a, b = order[i]; i += 1; g = a | b
    if bin(g).count("1") & 1: succ0.append(None); continue
    base = pe(g)
    for s in (0, M):
        v = (b, base ^ s)
        if v not in idx: idx[v] = len(order); order.append(v)
    succ0.append(idx[(b, base)])
per = [lp(b) for a, b in order]
memo = [0] * len(order)
def run(v):  # iterative: length of the start-bit-0 chain at constant period
    chain = []; w = v
    while True:
        chain.append(w)
        nx = succ0[w]
        if nx is None or per[nx] != per[v] or memo[nx] or len(chain) > 10 ** 6: break
        w = nx
    nx = succ0[w]
    tail = memo[nx] if (nx is not None and per[nx] == per[v] and memo[nx]) else 0
    for k, u in enumerate(reversed(chain)):
        memo[u] = tail + k + 1
    return memo[v]
best = collections.defaultdict(int); dist = collections.defaultdict(collections.Counter)
for v in range(len(order)):
    if per[v] < 4: continue
    r = memo[v] or run(v); best[per[v]] = max(best[per[v]], r); dist[per[v]][r] += 1
for q in sorted(best):
    print(f"cap {P}, period {q}: longest unfuelled run {best[q]} diagonals; run-length counts {dict(sorted(dist[q].items()))}")
