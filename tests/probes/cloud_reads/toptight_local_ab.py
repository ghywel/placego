"""CL530: CL529's localisation for small bins of sizes (a, b), big bin X >= 6.  sigma_AB < sigma_A gives
u_B <= L(b) + ab + hb - 1 (and u_A <= L(a) + ab + ha - 1); writing u = L(c) + hc + e: 0 <= e_A, e_B <= ab - 1 and
e_A + e_B >= ab.  Any element used is at most max(u - L(c - 1)) <= b(a + h + 1) - 2 =: W (b >= a).  Check: every hole set
of size <= h in [0, W] (and truncated pools M in [n_min - 1 + h, W - 1], n_min = a + b + 6, with the big-bin H(h) cuts)
admits disjoint a- and b-sets with sums u_A, u_B.  Run: python3 toptight_local_ab.py a b HMAX.

OUTCOME (CL530): (3,3) h <= 4 reproduces CL529's pool counts (1, 28, 470, 4,831, 40,184), 0 failures; (3,4) h <= 4
(200,180 pools at h = 4) and (4,4) h <= 3 (34,077 at h = 3): 0 failures.
"""
import sys
from itertools import combinations

def L(r): return r * (r - 1) // 2

def subsets_with_sum(T, c, s, start=0, acc=()):
    """all c-subsets of sorted list T (indices >= start) with sum s"""
    if c == 0:
        if s == 0: yield acc
        return
    for i in range(start, len(T) - c + 1):
        x = T[i]
        if x * c + c * (c - 1) // 2 > s: break          # even the smallest completion is too big
        yield from subsets_with_sum(T, c - 1, s - x, i + 1, acc + (x,))

def has_sum(T, c, s):
    for _ in subsets_with_sum(T, c, s): return True
    return False

def ok(T, a, b, uA, uB):
    for X in subsets_with_sum(T, a, uA):
        rest = [x for x in T if x not in X]
        if has_sum(rest, b, uB): return True
    return False

def check(a, b, h):
    W = b * (a + h + 1) - 2; fails = []; cfg = 0
    pairs = [(eA, eB) for eA in range(a * b) for eB in range(a * b) if eA + eB >= a * b]
    def run_pool(T, cuts_tot=None):
        nonlocal cfg
        cfg += 1
        for eA, eB in pairs:
            uA, uB = L(a) + h * a + eA, L(b) + h * b + eB
            if cuts_tot is not None:
                n, tot = cuts_tot; X = n - a - b; uC = tot - uA - uB
                if uC - L(X) - h * X < 0 or uA + uC - L(a + X) - h * (a + X) < 0 or uB + uC - L(b + X) - h * (b + X) < 0: continue
            if not ok(T, a, b, uA, uB): fails.append((tuple(x for x in range(T[-1] + 1) if x not in T), eA, eB))
    for k in range(h + 1):
        for H in combinations(range(W + 1), k):
            run_pool([x for x in range(W + 1) if x not in H])
    nmin = a + b + 6
    for Mt in range(nmin - 1 + h, W):
        for H in combinations(range(Mt + 1), h):
            T = [x for x in range(Mt + 1) if x not in H]
            run_pool(T, (len(T), sum(T)))
    return W, cfg, fails

if __name__ == '__main__':
    a, b, hmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    for h in range(int(sys.argv[4]) if len(sys.argv) > 4 else 0, hmax + 1):
        W, cfg, fails = check(a, b, h)
        print('sizes', (a, b), 'h', h, 'W', W, 'pools', cfg, 'failures', len(fails), fails[:3], flush=True)
