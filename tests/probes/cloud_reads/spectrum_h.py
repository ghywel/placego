"""CL514: the two-bin base of CL508's reduction, H2(h): for S = [0, M] minus h values (anywhere), n = |S|, and
3 <= r <= n - 3, is every integer u with L(r) + h r <= u <= sum(S) - L(n-r) - h(n-r) an r-subset sum of S?
(Lower cut of the r-bin, lower cut of the complement bin.)  Bitset subset-sum DP per pool.
Run: python3 spectrum_h.py HMIN HMAX NMAX.

OUTCOME (CL514): gaps only at n = 6 (u = 3h + 3, every h >= 3) and at h >= 2n - 7 for n = 7, 8, 9 (h = 7, 9, 11, witness
{0} u [h+1, M], u = 2M); clean otherwise for h <= 8 (n <= 12), n = 9 h <= 10, n = 10 h <= 11.
"""
import sys
from itertools import combinations

def run(n, h):
    M = n + h - 1; gaps = []; pools = 0
    for H in combinations(range(M + 1), h):
        pools += 1
        S = [x for x in range(M + 1) if x not in H]
        sp = [0] * (n + 1); sp[0] = 1
        for x in S:
            for c in range(n - 1, -1, -1):
                if sp[c]: sp[c + 1] |= sp[c] << x
        tot = sum(S)
        for r in range(3, n - 2):
            lo = r * (r - 1) // 2 + h * r; hi = tot - (n - r) * (n - r - 1) // 2 - h * (n - r)
            for u in range(lo, hi + 1):
                if not (sp[r] >> u) & 1: gaps.append((H, r, u)); break
    return pools, gaps

if __name__ == '__main__':
    for h in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        for n in range(6, int(sys.argv[3]) + 1):
            pools, gaps = run(n, h)
            print('h', h, 'n', n, 'pools', pools, 'pools with a gap', len(gaps), gaps[:2], flush=True)
