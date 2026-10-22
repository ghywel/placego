"""CL535: how common is the SMALL-bin top-tight case once a big bin is present?  Sizes (3, 3, 3, X); count H(h)
instances whose least slack is attained only by co-singletons, and split by whether the top-tight bin (the
complement) is a size-3 bin or the big bin.  Also decide feasibility of the small-top-tight ones (backtracking).

OUTCOME (CL535): small-top-tight is COMMON (X = 4, 6, 8; h <= 2): 1,135 .. 133,684 per domain, 30-55% of admitted
(sorted small targets), all feasible.  Big-bin top-tight at h = 0 is exactly 235 for every X (= CL531's admissible
triples: localisation, independent of X).
"""
import sys
from itertools import combinations
from collections import Counter

def L(r): return r * (r - 1) // 2

def feasible(pool, sizes, t):
    order = sorted(range(len(sizes)), key=lambda i: sizes[i])
    sizes = [sizes[i] for i in order]; t = [t[i] for i in order]
    def go(p, i):
        if i == len(sizes) - 1: return True
        for A in combinations(p, sizes[i]):
            if sum(A) == t[i]:
                if go([x for x in p if x not in A], i + 1): return True
        return False
    return go(list(pool), 0)

def run(M, h, X):
    C = (3, 3, 3, X); n = 9 + X; assert M + 1 - h == n
    cnt = Counter(); ex = []
    groups = [J for s in (1, 2, 3) for J in combinations(range(4), s)]
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        lo3 = 3 + 3 * h
        for u1 in range(lo3, 3 * M):
            for u2 in range(u1, 3 * M):
                for u3 in range(u2, 3 * M):
                    u4 = tot - u1 - u2 - u3
                    t = (u1, u2, u3, u4)
                    sig = {}
                    bad = False
                    for J in groups:
                        r = sum(C[i] for i in J); u = sum(t[i] for i in J)
                        s_ = u - L(r) - h * r
                        if s_ < 0: bad = True; break
                        sig[J] = s_
                    if bad: continue
                    mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
                    cnt['admitted'] += 1
                    if any(len(J) <= 2 for J in arg): continue
                    tops = {[i for i in range(4) if i not in J][0] for J in arg}
                    if 3 in tops and len(tops) == 1: cnt['bigbin_toptight'] += 1; continue
                    cnt['small_toptight'] += 1
                    if not feasible(S, C, t):
                        cnt['small_toptight_INFEASIBLE'] += 1
                        if len(ex) < 4: ex.append((H, t))
    return cnt, ex

if __name__ == '__main__':
    for M, h, X in ((12, 0, 4), (13, 1, 4), (14, 2, 4), (14, 0, 6), (15, 1, 6), (16, 2, 6), (16, 0, 8), (17, 1, 8)):
        cnt, ex = run(M, h, X)
        print('X', X, 'h', h, 'M', M, dict(cnt), ex, flush=True)
