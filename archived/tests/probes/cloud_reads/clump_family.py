"""CL513: the two-clump equal-sum family.  Pool S = [0, s-1] u [s+h, M] (one run of h holes after a small clump of s
values), k bins of size 3, targets: one light t and k-1 equal heavy T (total conserved).  For each k, the least h at
which some (s, t) member is in H(h) (u_J >= L(r) + h r for every proper group) and infeasible.  Feasibility by exact
search; H(h) by the 2^k - 2 group cuts.
Run: python3 clump_family.py KMAX [KMIN [HMAX]].

OUTCOME (CL513): least failing h for k = 3..10: 3, 3, 7, 9, 10, 12, 13, 15 (s = 4, 6, then 2).  For s = 2 the hand window
h >= 1.5k - 1 + 1/(k-1) predicted 12, 13, 15 for k = 8, 9, 10 before the run.
"""
import sys
from itertools import combinations
from functools import lru_cache

def key(t, k):
    mu = 10 ** 9
    for j in range(1, k):
        for J in combinations(range(k), j):
            r = 3 * j; u = sum(t[i] for i in J)
            mu = min(mu, (u - r * (r - 1) // 2) // r if u >= r * (r - 1) // 2 else -1)
    return mu

def feasible(pool, targets):
    targets = sorted(targets)
    @lru_cache(maxsize=None)
    def go(rest, ts):
        if not ts: return True
        t0 = ts[0]; rest_l = list(rest)
        x = rest_l[0]   # the smallest remaining value must go somewhere: try every bin it can join (dedupe equal targets)
        seen = set()
        for bi, tb in enumerate(ts):
            if tb in seen: continue
            seen.add(tb)
            others = rest_l[1:]
            for a, b in combinations(others, 2):
                if x + a + b == tb:
                    nr = tuple(v for v in others if v != a and v != b)
                    if go(nr, ts[:bi] + ts[bi + 1:]): return True
        return False
    return go(tuple(sorted(pool)), tuple(targets))

def first_failure(k, hmax=12):
    n = 3 * k
    for h in range(0, hmax + 1):
        M = n + h - 1; found = []
        for s in range(1, n):
            S = list(range(0, s)) + list(range(s + h, M + 1))
            if len(S) != n: continue
            tot = sum(S)
            for t in range(3, 3 * M):
                if (tot - t) % (k - 1): continue
                T = (tot - t) // (k - 1)
                tg = [t] + [T] * (k - 1)
                if key(tg, k) < h: continue
                if not feasible(S, tg): found.append((s, t, T))
        if found: return h, found[:4]
    return None, []

if __name__ == '__main__':
    for k in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3, int(sys.argv[1]) + 1):
        h, ex = first_failure(k, int(sys.argv[3]) if len(sys.argv) > 3 else 12)
        print('k', k, 'first failing h in the clump family:', h, 'examples (s, t, T):', ex, flush=True)
