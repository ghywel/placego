# Survey for GPT's next question (gcd 1): in the same M=28 domain, how far does an "end-gap" root rule reach?
# Collision condition (MI174/MI175): with split (A,B), root h, w = p-2s, H = (27-w)/2, a collision occurs iff H-h is in U+V,
# where U, V are the prefix-sum sets of the runs. U+V is contained in {0} u [m, K-m] u {K}, m = min d. So any feasible
# split and allowed root with H-h outside [0,K] or inside (0,m) or (K-m,K) is collision-free, whatever the within-run orders.
import itertools, math, time, sys
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion, label
M = 28; n = 14
def endgap(p, q, d):
    K = sum(d); m = min(d)
    for mask in range(1 << len(d)):
        s = sum(d[i] for i in range(len(d)) if mask >> i & 1); t = K - s
        if s > n - 1 or t > n - 1: continue
        w = p - 2*s; L = max(0, -w); R = min(M - 1 - p, M - 1 - 2*t); H = (M - 1 - w) // 2
        for h in range(L, R + 1):
            c = H - h
            if c < 0 or c > K or 0 < c < m or K - m < c < K: return True
    return False
tot = cap = eg = truth_yes = 0; left = []; t0 = time.time()
for N in range(1, 7):
    for d in itertools.combinations_with_replacement(range(1, 12), N):
        K = sum(d)
        if not (14 <= K <= 25) or math.gcd(*d) != 1: continue
        for p in range(1, 26, 2):
            q = 2*K - p
            if q < p or q > 25: continue
            tot += 1
            if not criterion(M, p, q, d): continue
            cap += 1
            if endgap(p, q, d): eg += 1
            else: left.append((p, q, d))
print(f"gcd-1 questions {tot}; capacity-feasible {cap}; end-gap rule constructs {eg}; left for exhaustive check {len(left)}  ({time.time()-t0:.1f}s)")
yes = no = 0; nos = []
for p, q, d in left:
    if time.time() - t0 > 400: print("time cap reached"); break
    if exists_cycle(M, p, q, list(d)): yes += 1
    else: no += 1; nos.append((p, q, d))
print(f"of those: a cycle exists for {yes}, none for {no}  ({time.time()-t0:.1f}s)")
print("first genuine gcd-1 refusals beyond capacity:", nos[:12])
