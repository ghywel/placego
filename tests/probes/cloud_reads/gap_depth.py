"""CL479: how deep can a gap in the k-subset sums of an interval-with-deletions sit?

Pool R = [0, N] minus a set D of deletions (0 <= |D| <= 5, deletions internal), n = |R|, 3 <= k <= n - 3.
depth(gap) = min(gap - alpha, beta - gap) where alpha, beta are the least and greatest k-sums.
Tabulate, for each (n, |D|), the maximum depth over all deletion patterns and all k, and the pools attaining
depth >= 3.  Prediction: central gaps (depth >= 3) occur only for n = 6 (the cores) and perhaps n = 7 with
|D| >= 3; for n >= 8 every gap is within 2|D| ... of an edge, and for n >= 9 within 2 of an edge when
|D| <= 2.  Counterfactual: a deep gap at n >= 9 would mean the A2 remainder can fail far from the edges.

OUTCOME (N <= 18, |D| <= 7; 37 s).  Maximum gap depth stabilises in n and depends only on |D|:
  |D| = 1: 1 (n >= 6)      |D| = 2: 2 (n >= 6)      |D| = 3: 4 (n >= 7; 9 at n = 6, the cores)
  |D| = 4: 5 (n >= 8)      |D| = 5: 7 (n >= 9)      |D| = 6: 9 (n >= 10)     |D| = 7: 11 (n >= 11)
Stable witnesses are clumps: e.g. |D| = 6, deletions {3,4,5,9,10,11}: {0,1,2} u {6,7,8} u [12,N] has no
3-sum 12 (two-from-the-first clump maxes at 11, one-from-the-first starts at 13).  Prediction partly held:
depth is bounded for each |D| once n is large, but the bound grows with |D| (not "within 2 of an edge").
"""
import itertools, sys
from collections import defaultdict

def sig(R, k):
    s = set()
    for c in itertools.combinations(R, k): s.add(sum(c))
    return s

def run(NMAX, DMAX):
    best = defaultdict(int); witness = {}
    for N in range(5, NMAX + 1):
        for d in range(0, DMAX + 1):
            for D in itertools.combinations(range(1, N), d):
                R = [x for x in range(N + 1) if x not in D]; n = len(R)
                if n < 6: continue
                for k in range(3, n // 2 + 1):          # k and n-k give the same gap depths
                    s = sig(R, k); a, b = min(s), max(s)
                    for v in range(a + 1, b):
                        if v in s: continue
                        dep = min(v - a, b - v)
                        if dep > best[(n, d)]:
                            best[(n, d)] = dep; witness[(n, d)] = (N, D, k, v)
    for key in sorted(best):
        print(key, 'max depth', best[key], 'witness (N, deletions, k, gap)', witness[key])

if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]))
