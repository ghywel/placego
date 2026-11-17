# Test the conjectured exact criterion for ALL d (gcd 1 included): a folded-distinct cycle for (p,q,-2d) on 0..M-1 exists
# iff max(p,q) <= M-3, not (p = q = M-3), N+2 <= M/2 (label count), and the d's split into two groups of sum <= M/2-1. Exhaustive on small windows.
import itertools, math, sys, collections
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion
res = collections.Counter(); mism = []
for M in (6, 8, 10, 12, 14, 16, 18):
    n = M // 2
    for N in range(1, 5):
        for d in itertools.combinations_with_replacement(range(1, n), N):
            K = sum(d)
            for p in range(1, 2*K, 2):
                q = 2*K - p
                if q < p or q > M - 3: continue
                conj = criterion(M, p, q, d) and not (p == q == M - 3) and N + 2 <= n   # condition 3: label count
                truth = exists_cycle(M, p, q, list(d))
                res[(M, conj == truth)] += 1
                if conj != truth: mism.append((M, p, q, d, truth, conj))
print({M: (res[(M, True)], res[(M, False)]) for M in (6, 8, 10, 12, 14, 16, 18)})
print("mismatches (M,p,q,d,truth,conjecture):", mism[:15], "total", len(mism))
