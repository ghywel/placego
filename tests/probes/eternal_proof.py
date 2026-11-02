#!/usr/bin/env python3
"""L1292 (Local, 2026-11-02): the light-speed recurrence conjecture, checked exactly for each period p = 2^m.
Predictions P12a-P12c in reports/rule30-genealogy.md section 26.2, written first.
Run: python3 tests/probes/eternal_proof.py   (seconds to minutes; no files written)

Columns are p-periodic rings, stored as p-bit integers (bit t = the value at time t). From the state (u, v) =
(c_(k-1), c_k) the next column w satisfies w(t+1) = w(t) XOR (u OR v)(t): defined iff popcount(u | v) is even, two
choices w(0) = 0 or 1. The start is (c_(-2), c_(-1)) = (0, all ones). Rain: (a, abar) <-> (abar, a), a = 0101...
"""
import sys
from collections import deque


def run(p):
    mask = (1 << p) - 1
    a = sum(1 << t for t in range(1, p, 2))          # bit t = t mod 2
    abar = mask ^ a

    def succ(u, v):
        d = u | v
        if bin(d).count('1') % 2:
            return []
        y = d
        s = 1
        while s < p:
            y ^= (y << s) & mask
            s <<= 1
        w0 = (y << 1) & mask                           # w(t) = XOR_{s<t} d(s), w(0) = 0
        return [(v, w0), (v, w0 ^ mask)]

    rain = {(a, abar), (abar, a)}
    # sanity: the start reaches the rain and the defect
    start = (0, mask)
    s1 = succ(*start)
    s2 = [y for x in s1 for y in succ(*x)]
    assert set(s2) >= {(a, abar), (abar, a), (a, a), (abar, abar)}, (p, s2)
    # reachable graph from the defect states
    seen = {}
    order = []
    dq = deque([(a, a), (abar, abar)])
    for st in dq:
        seen[st] = None
    edges_into_rain = 0
    while dq:
        st = dq.popleft()
        order.append(st)
        nxt = succ(*st)
        seen[st] = nxt
        for n in nxt:
            if n in rain:
                edges_into_rain += 1
            elif n not in seen:
                seen[n] = None
                dq.append(n)
        if len(seen) > 20_000_000:
            return None
    # cycle check and longest path by iterative DFS
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {s: WHITE for s in seen}
    longest = {}
    cyclic = False
    for root in ((a, a), (abar, abar)):
        if colour[root] != WHITE:
            continue
        stack = [(root, iter(seen[root]))]
        colour[root] = GREY
        while stack:
            node, it = stack[-1]
            advanced = False
            for n in it:
                if n in rain:
                    continue
                if colour[n] == GREY:
                    cyclic = True
                    continue
                if colour[n] == WHITE:
                    colour[n] = GREY
                    stack.append((n, iter(seen[n])))
                    advanced = True
                    break
            if not advanced:
                stack.pop()
                colour[node] = BLACK
                longest[node] = 1 + max((longest[n] for n in seen[node] if n not in rain and n in longest), default=0)
    L = max(longest.get((a, a), 0), longest.get((abar, abar), 0))
    return len(seen), edges_into_rain, cyclic, L


for m in range(1, 8):
    p = 1 << m
    r = run(p)
    if r is None:
        print(f'p={p}: state cap reached'); break
    n, into, cyc, L = r
    print(f'p={p:4d}: states reachable from the defect {n:9d}; edges back into the rain {into}; cycle {cyc}; '
          f'longest path after the defect {L} columns')
    sys.stdout.flush()
print('ETERNAL_PROOF_DONE')
