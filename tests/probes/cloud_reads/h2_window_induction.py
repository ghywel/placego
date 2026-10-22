"""CL519: can H2 for r >= 4 be reduced to r = 3 by window arithmetic?  For S = [0,M] minus h holes (0, M kept after the
CL516 reductions), the r-subsets containing 0 cover the (shifted) H2 window of index r - 1 on S minus 0, if H2 holds
there; likewise those containing M, and the complements (index n - r).  Test: is W_r(S) contained in the union of
these inductive windows, for every S, 4 <= r <= n - 4?  Pure interval arithmetic (no subset sums).  Run: python3 h2_window_induction.py NMAX [--all].

OUTCOME (CL519): NOT enough.  n = 8, 9, 10 (h <= 2n - 8): 453, 2,947, 14,242 uncovered (S, r) cases, all with window
width < n (max 9 at n = 10); anchoring at every element changes nothing.  Example S = {0,1,2,3,5,6,8,9}, r = 4:
window [14,20], inductive windows miss 17 = 0+3+5+9.  Window induction is lossy at the inner ends.
"""
import sys
from itertools import combinations

ALL_ANCHORS = '--all' in sys.argv

def L(r): return r * (r - 1) // 2

def window(S, r):
    """H2 window of index r on a pool S (any integers, sorted); returns (lo, hi) in S's own coordinates"""
    a, b = S[0], S[-1]; n = len(S); h = (b - a + 1) - n
    sh = [x - a for x in S]
    lo = L(r) + h * r; hi = sum(sh) - L(n - r) - h * (n - r)
    return lo + r * a, hi + r * a

def covered(S, r):
    n = len(S); tot = sum(S); lo, hi = window(S, r)
    if lo > hi: return True, 0
    ivs = []
    anchors = (S[0], S[-1]) if not ALL_ANCHORS else S
    for z in anchors:
        T = [x for x in S if x != z]
        if 3 <= r - 1 <= len(T) - 3:
            l2, h2 = window(T, r - 1); ivs.append((z + l2, z + h2))
        if 3 <= n - r - 1 <= len(T) - 3:   # complement (n-r)-subsets containing z
            l2, h2 = window(T, n - r - 1); ivs.append((tot - (z + h2), tot - (z + l2)))
    miss = [u for u in range(lo, hi + 1) if not any(a <= u <= b for a, b in ivs)]
    return not miss, hi - lo + 1

if __name__ == '__main__':
    bad = 0; tot_cases = 0; widths = []
    for n in range(8, int(sys.argv[1]) + 1):
        for h in range(0, 2 * n - 7):
            M = n + h - 1
            for H in combinations(range(1, M), h):
                S = [x for x in range(M + 1) if x not in H]
                for r in range(4, n - 3):
                    ok, w = covered(S, r); tot_cases += 1
                    if not ok:
                        bad += 1; widths.append((w, n))
                        if bad <= 5: print('uncovered:', n, h, H, r, 'window width', w, flush=True)
        print('n', n, 'cases so far', tot_cases, 'uncovered', bad, flush=True)
    print('max window width among uncovered cases:', max(widths) if widths else None)
