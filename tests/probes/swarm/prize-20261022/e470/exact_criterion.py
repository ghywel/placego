# PREDICTION: for n = 2^k p q, p = N-a, q = N+b (N=2^{k+2}, M=N/2, a,b odd, a+b<=M, a<M):
#   weird  <=>  L >= 0 and L*b <= v <= M-(L+1)*a-1,
#   where u = floor((a-1)(b+1)/N), v = (a-1)(b+1) - uN, L = (a-b-4)/2 + u.
# Counterfactual: any mismatch with the exact structure test on prime pairs.
# Also: map how far in a the weird region reaches (predicted ~0.63 N^{2/3}, far beyond sqrt N).
import sys
sys.path.insert(0, 'e470')
from wlib import *

def crit(k, a, b):
    N = 1 << (k + 2); M = N // 2
    u, v = divmod((a - 1) * (b + 1), N)
    if (a - b) % 2: return None
    L = (a - b - 4) // 2 + u
    return L >= 0 and L * b <= v <= M - (L + 1) * a - 1

for k in range(6, 19):
    budget()
    N = 1 << (k + 2); M = N // 2
    amax = min(M - 1, int(0.75 * N ** (2 / 3)) + 50)
    pa = [a for a in range(1, amax + 1, 2) if is_prime(N - a)]
    # thin the a-list for large k to keep the run short
    step = max(1, len(pa) // 400)
    pa = pa[::step]
    tested = mism = weird_ct = 0; max_a_weird = 0; prim_fail = 0
    for a in pa:
        lo = max(1, a - (N // max(1, a)) - 60) if a > 64 else 1
        hi = min(M - a, a + 4 * a * a // N + 60)
        for b in range(lo | 1, hi + 1, 2):
            if not is_prime(N + b): continue
            ab, prim, w = weird_2kpq(k, N - a, N + b)
            truth = ab and w
            c = crit(k, a, b)
            tested += 1
            if c != truth:
                mism += 1
                if mism <= 5: print("  MISMATCH k=%d a=%d b=%d truth=%s crit=%s" % (k, a, b, truth, c))
            if truth:
                weird_ct += 1; max_a_weird = max(max_a_weird, a)
                if not prim: prim_fail += 1
    print(f"k={k:2d} N={N} tested={tested} weird={weird_ct} mismatches={mism} weird_but_not_primitive={prim_fail} "
          f"max_a_weird={max_a_weird} sqrtN={math.isqrt(N)} 0.63N^(2/3)={0.63 * N ** (2/3):.0f}", flush=True)
