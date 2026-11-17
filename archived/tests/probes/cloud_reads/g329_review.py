#!/usr/bin/env python3
"""g329_review.py: Cloud's carrying-review check of GPT's G329 (protected adjacent pair targets u, u+1 and one filler).
Exhaustive over r, s >= 1, c >= 1 with M = 2t + c <= MMAX: protection from EVERY proper group (by colour counts and
filler membership), compared with (329.1); partition existence by exact search (r disjoint sum-u pairs and s disjoint
sum-(u+1) pairs, all disjoint; the filler takes the rest); failures compared with ranges A and B.
PREDICTIONS (before any run): (329.1) equals the all-group protection exactly (0.9); failures equal A union B (0.85).
"""
import sys
from functools import lru_cache
T = lambda n: n * (n + 1) // 2

def protected(r, s, c, M, q, u):
    t = r + s; tot = T(M) - q; w = tot - r * u - s * (u + 1)
    for mr in range(r + 1):
        for mb in range(s + 1):
            for f in (0, 1):
                if (mr, mb, f) in ((0, 0, 0), (r, s, 1)): continue
                size = 2 * (mr + mb) + f * c; tg = mr * u + mb * (u + 1) + f * w
                if tg < T(size): return False
    return True

def formula(r, s, c, M, q, u):
    t = r + s
    return u >= 2 * t + 1 and q <= min(2 * M - u - 2, t * (2 * M - 2 * t + 1 - u) - s)

def partition_exists(r, s, M, q, u):
    P = [x for x in range(M + 1) if x != q]; Ps = set(P)
    red = [(x, u - x) for x in P if x < u - x and (u - x) in Ps]
    blue = [(x, u + 1 - x) for x in P if x < u + 1 - x and (u + 1 - x) in Ps]
    edges = [(e, 0) for e in red] + [(e, 1) for e in blue]
    @lru_cache(None)
    def go(i, nr, nb, used):
        if nr == 0 and nb == 0: return True
        if i == len(edges): return False
        (x, y), col = edges[i]
        if (col == 0 and nr > 0 or col == 1 and nb > 0) and not (used >> x & 1) and not (used >> y & 1):
            if go(i + 1, nr - (col == 0), nb - (col == 1), used | (1 << x) | (1 << y)): return True
        return go(i + 1, nr, nb, used)
    return go(0, r, s, 0)

def failure_pred(r, s, c, M, q, u):
    t = r + s
    A = (u == 2 * M - 2 * t and c <= q <= r)
    B = (u == 2 * M - 2 * t - 1 and c + r <= q <= t + min(r, c - 1))
    return A or B

if __name__ == '__main__':
    Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    n = nf = 0; bad_cut = []; bad_cls = []
    for t in range(2, Mmax):
        for r in range(1, t):
            s = t - r
            for c in range(1, Mmax - 2 * t + 1):
                M = 2 * t + c
                for q in range(1, M):
                    for u in range(1, 2 * M):
                        pr = protected(r, s, c, M, q, u)
                        if pr != formula(r, s, c, M, q, u): bad_cut.append((r, s, c, q, u))
                        if not pr: continue
                        n += 1
                        ok = partition_exists(r, s, M, q, u)
                        if not ok: nf += 1
                        if ok == failure_pred(r, s, c, M, q, u): bad_cls.append((r, s, c, M, q, u, ok))
    print(f'admitted inputs {n}, failures {nf}, (329.1) mismatches {len(bad_cut)} {bad_cut[:3]}, classification mismatches {len(bad_cls)} {bad_cls[:5]}')
