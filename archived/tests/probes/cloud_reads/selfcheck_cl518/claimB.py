"""Claim B: two-bin subset-sum base. Pool S = [0,M] \\ H, M = n+h-1, |S| = n.
BAD if for some r in [3, n-3] some u in [L(r)+h r, sum(S)-L(n-r)-h(n-r)] is not an r-subset sum."""
import itertools, sys, time

def L(r): return r*(r-1)//2

def rsums(S, r):
    # DP over elements: reach[j] = set of sums of j-element subsets
    reach = [set() for _ in range(r+1)]; reach[0].add(0)
    for x in S:
        for j in range(r, 0, -1):
            reach[j] |= {s + x for s in reach[j-1]}
    return reach[r]

def rsums_brute(S, r):
    return {sum(c) for c in itertools.combinations(S, r)}

def bad_pools(n, h, brute=False):
    M = n + h - 1; out = []
    for H in itertools.combinations(range(M+1), h):
        Hs = set(H); S = [x for x in range(M+1) if x not in Hs]
        assert len(S) == n
        tot = sum(S); bad = []
        for r in range(3, n-2):
            sums = (rsums_brute if brute else rsums)(S, r)
            lo = L(r) + h*r; hi = tot - L(n-r) - h*(n-r)
            miss = [u for u in range(lo, hi+1) if u not in sums]
            if miss: bad.append((r, miss))
        if bad: out.append((H, bad))
    return out

if __name__ == '__main__':
    for n, hs in [(7, range(0, 9)), (8, range(0, 11))]:
        for h in hs:
            t = time.time(); b = bad_pools(n, h)
            print(f'n={n} h={h}: bad={len(b)} ({time.time()-t:.1f}s)')
            for H, info in b: print('   holes', H, 'missing (r, u-list):', info)
    # brute-force cross-check of the DP at the claimed thresholds
    print('brute n=7 h=7:', [(H) for H, _ in bad_pools(7, 7, brute=True)])
    print('brute n=8 h=9:', [(H) for H, _ in bad_pools(8, 9, brute=True)])
