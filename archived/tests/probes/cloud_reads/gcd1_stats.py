import itertools, math, collections, sys
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion
M = 28; n = 14
def outside(p, q, d):
    K = sum(d)
    for mask in range(1 << len(d)):
        s = sum(d[i] for i in range(len(d)) if mask >> i & 1); t = K - s
        if s > n - 1 or t > n - 1: continue
        w = p - 2*s; L = max(0, -w); R = min(M - 1 - p, M - 1 - 2*t); H = (M - 1 - w) // 2
        if R > H or L < H - K: return True
    return False
cnt = collections.Counter(); byp = collections.Counter(); refs = collections.Counter(); out_ok = 0; out_total = 0
for N in range(1, 7):
    for d in itertools.combinations_with_replacement(range(1, 12), N):
        K = sum(d)
        if not (14 <= K <= 25) or math.gcd(*d) != 1: continue
        for p in range(1, 26, 2):
            q = 2*K - p
            if q < p or q > 25 or not criterion(M, p, q, d): continue
            ex = exists_cycle(M, p, q, list(d)); byp[(p, q)] += 1
            if outside(p, q, d):
                out_total += 1; out_ok += ex
            if not ex: refs[(p, q)] += 1; cnt[N] += 1
print("genuine gcd-1 refusals by (p,q):", dict(sorted(refs.items())))
print("capacity-feasible questions by (p,q) with q=25:", {k: v for k, v in sorted(byp.items()) if k[1] == 25})
print("refusals by N:", dict(sorted(cnt.items())))
print("outside-root rule applies to", out_total, "questions; truth has a cycle in", out_ok, "of them (rule sound iff equal)")
