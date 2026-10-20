#!/usr/bin/env python3
"""g328_review.py: Cloud's carrying-review check of GPT's G328 (exact obstructions, protected one-hole counts (2,2,c)).
Exhaustive over every admitted input for 7 <= M <= MMAX: does a partition exist (two disjoint pairs of sums u, v in
P = [0,M] minus q; the rest is the size-c filler), and is the failure set exactly G328's three families? Also checks
(2), the protected-cut reduction, against the six cuts directly, and the pair-count formula.
PREDICTIONS (before any run): the failure set equals the stated list at every M (0.9); (2) equals the six cuts (0.95).
"""
import sys
T = lambda r: r * (r + 1) // 2

def check(Mmax):
    bad = []; nfail = 0; n = 0
    for M in range(7, Mmax + 1):
        c = M - 4
        for q in range(1, M):
            P = [x for x in range(M + 1) if x != q]; Ps = set(P)
            fib = {}
            for i, x in enumerate(P):
                for y in P[i + 1:]: fib.setdefault(x + y, []).append((x, y))
            tot = T(M) - q
            # pair-count formula: before deletion floor((min(z,2M-z)+1)/2); one deletion removes at most one pair
            for z in range(1, 2 * M):
                full = (min(z, 2 * M - z) + 1) // 2
                actual = len(fib.get(z, []))
                if not (full - 1 <= actual <= full): bad.append(('count', M, q, z))
            for u in range(1, 2 * M):
                for v in range(u, 2 * M):
                    w = tot - u - v
                    six = (u >= 3 and v >= 3 and w >= T(c) and u + v >= 10 and u + w >= T(c + 2) and v + w >= T(c + 2))
                    two = (3 <= u <= 2 * M - 1 - q and 3 <= v <= 2 * M - 1 - q and 10 <= u + v <= 4 * M - 6 - q)
                    if six != two: bad.append(('(2)', M, q, u, v))
                    if not six: continue
                    n += 1
                    ok = any(not (set(a) & set(b)) for a in fib.get(u, []) for b in fib.get(v, []) if a != b)
                    exc = (q == 1 and {u, v} == {4, 6}) or (M == 7 and q == 3 and {u, v} in ({3, 8}, {4, 10}))
                    if not ok: nfail += 1
                    if ok == exc: bad.append(('classification', M, q, u, v, 'partition' if ok else 'no partition'))
        if M % 10 == 0: print(f'  M={M}: admitted {n}, failures {nfail}, mismatches {len(bad)}', flush=True)
    return n, nfail, bad

if __name__ == '__main__':
    n, nfail, bad = check(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
    print('admitted inputs', n, '| failures', nfail, '| mismatches with G328', len(bad), bad[:10])
