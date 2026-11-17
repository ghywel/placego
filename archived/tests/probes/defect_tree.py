#!/usr/bin/env python3
"""L1294 T15 (Local, 2026-11-02): structure of the pair graph from the defect, p = 8, 16, 32, 64.
Predictions in reports/rule30-genealogy.md section 29.3, written first. Run: python3 tests/probes/defect_tree.py

States (u, v) = (c_(k-1), c_k) as p-bit time-rings (bit t = time t). Children (v, w) with w the running XOR of u | v
from w(0) in {0, 1}, defined iff |u | v| is even (the state "continues"). Roots: both defect phases (a, a), (abar, abar).
P15a: does the second column determine the first among reachable states?
P15b: when |v| is odd, exactly one child continues (guard on the hand proof).
P15c: mean number of continuing children per continuing node.
"""
from collections import defaultdict


def run(p):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    pc = lambda x: bin(x).count('1')

    def integ(d):
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M
            s <<= 1
        return (y << 1) & M

    roots = [(A, A), (M ^ A, M ^ A)]
    seen, stack = set(roots), list(roots)
    while stack:
        u, v = stack.pop()
        d = u | v
        if pc(d) & 1:
            continue
        w0 = integ(d)
        for w in (w0, w0 ^ M):
            if (v, w) not in seen:
                seen.add((v, w)); stack.append((v, w))
    cont = lambda s: pc(s[0] | s[1]) % 2 == 0
    by_second = defaultdict(set)
    for s, u in seen:
        by_second[u].add(s)
    clash = sum(1 for u in by_second if len(by_second[u]) > 1)
    forced_bad = forced_n = 0
    kids = []
    for s in seen:
        if not cont(s):
            continue
        u, v = s
        w0 = integ(u | v)
        c0, c1 = cont((v, w0)), cont((v, w0 ^ M))
        if pc(v) & 1:
            forced_n += 1
            forced_bad += (c0 + c1 != 1)
        else:
            forced_bad += (c0 != c1)
        kids.append(c0 + c1)
    dist = [kids.count(i) for i in range(3)]
    print(f'p = {p:2d}: reachable states {len(seen):7d}; second columns with two or more first columns: {clash}; '
          f'odd |v| nodes {forced_n}, forced-child rule violations {forced_bad}; continuing nodes {len(kids)}, '
          f'continuing children 0/1/2: {dist}, mean {sum(kids) / len(kids):.4f}')


for p in (8, 16, 32, 64):
    run(p)
print('DEFECT_TREE_DONE')
