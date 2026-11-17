"""CL531: four bins (3, 3, 3, X), X >= 6, in H(h), least slack attained by the triple {B, C, D} of size-3 bins and by
none of its proper subgroups (the big bin A is top-tight).  sigma_BCD < sigma_{CD} etc. gives u_i <= 20 + 3h, so every
element used is <= 19 + 3h: LOCAL.  Check every hole set of size <= h in [0, 19 + 3h] and truncated pools
(M in [14 + h, 18 + 3h]) with the big bin's cuts: three disjoint triples with the three sums exist.
Run: python3 toptight_local_333.py HMAX [HMIN].

OUTCOME (CL531): h = 0..4, 235 admissible target triples each, pools 6 / 157 / 2,272 / 24,781 / 231,197: 0 failures.
"""
import sys
from itertools import combinations

def L(r): return r * (r - 1) // 2

def trip_with_sum(T, s):
    n = len(T)
    for i in range(n):
        a = T[i]
        if 3 * a + 3 > s: break
        for j in range(i + 1, n):
            b = T[j]
            c = s - a - b
            if c <= b: break
            yield (a, b, c)

def ok(T, us):
    Ts = set(T)
    def go(avail, k):
        if k == 3: return True
        for (a, b, c) in trip_with_sum(sorted(avail), us[k]):
            if c in avail:
                if go(avail - {a, b, c}, k + 1): return True
        return False
    return go(frozenset(Ts), 0)

def target_triples(h):
    out = []
    lo = 3 + 3 * h; hi = 20 + 3 * h
    for u1 in range(lo, hi + 1):
        for u2 in range(u1, hi + 1):
            for u3 in range(u2, hi + 1):
                s = {(1,): u1, (2,): u2, (3,): u3}
                sig = lambda u, r: u - L(r) - h * r
                singles = [sig(u, 3) for u in (u1, u2, u3)]
                pairs = [sig(u1 + u2, 6), sig(u1 + u3, 6), sig(u2 + u3, 6)]
                tri = sig(u1 + u2 + u3, 9)
                if min(singles + pairs) < 0 or tri < 0: continue
                if not all(tri < x for x in singles + pairs): continue
                out.append((u1, u2, u3))
    return out

if __name__ == '__main__':
    for h in range(int(sys.argv[2]) if len(sys.argv) > 2 else 0, int(sys.argv[1]) + 1):
        W = 19 + 3 * h; tg = target_triples(h); fails = []; pools = 0
        for k in range(h + 1):
            for H in combinations(range(W + 1), k):
                T = [x for x in range(W + 1) if x not in H]; pools += 1
                for us in tg:
                    if not ok(T, us): fails.append((H, us))
        for Mt in range(14 + h, W):
            for H in combinations(range(Mt + 1), h):
                T = [x for x in range(Mt + 1) if x not in H]; pools += 1
                n = len(T); tot = sum(T); X = n - 9
                for us in tg:
                    uA = tot - sum(us)
                    cuts = [uA - L(X) - h * X] + [uA + sum(c) - L(X + 3 * len(c)) - h * (X + 3 * len(c)) for r in (1, 2) for c in combinations(us, r)]
                    if min(cuts) < 0: continue
                    if not ok(T, us): fails.append(('trunc', Mt, H, us))
        eq = sum(1 for f in fails if len(set(f[-1])) < 3)
        print('h', h, 'W', W, 'target triples', len(tg), 'pools', pools, 'failures', len(fails), 'with equal targets', eq, fails[:4], flush=True)
