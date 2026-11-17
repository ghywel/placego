# In GPT's M=28 domain (N<=6, d<=11, K 14..25, odd p<=q<=25, any gcd): among questions with a cycle (exhaustive truth),
# how many does MI180's single-pair contraction reach (two entries >= k+2, k = 12-N), and how many does the full-label
# case cover (N = 12)? Sizes the gap GPT must close with a distributed contraction or another route.
import itertools, math, sys, collections
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion
M = 28; n = 14
tot = solv = reach = 0; byN = collections.Counter(); byN_reach = collections.Counter(); unreached = []
for N in range(1, 7):
    k = n - N - 2
    for d in itertools.combinations_with_replacement(range(1, 12), N):
        K = sum(d)
        if not (14 <= K <= 25): continue
        for p in range(1, 26, 2):
            q = 2*K - p
            if q < p or q > 25: continue
            tot += 1
            if not criterion(M, p, q, d) or p == q == 25: continue
            if not exists_cycle(M, p, q, list(d)): print("unexpected refusal", p, q, d); continue
            solv += 1; byN[N] += 1
            big = sorted(d, reverse=True)
            if len(big) >= 2 and big[1] >= k + 2: reach += 1; byN_reach[N] += 1
            else: unreached.append((p, q, d))
print(f"questions {tot}; solvable (capacity, not doubled 25) {solv}; single-pair contraction reaches {reach}")
print("solvable by N:", dict(sorted(byN.items())), " reached by N:", dict(sorted(byN_reach.items())))
print("unreached examples:", unreached[:6])
print("unreached with max entry <= 7:", sum(1 for p, q, d in unreached if max(d) <= 7))
