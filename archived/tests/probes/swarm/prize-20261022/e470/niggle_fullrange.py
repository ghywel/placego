# Niggle check: exact structure test vs criterion over the FULL range of b (b <= M - a), all odd a < M/2,
# small k; also the symmetric confinement: for fixed b, the valid a form one run of length <= ~sqrt(N/2).
import sys
sys.path.insert(0, 'e470')
from wlib import *
def crit(N, a, b):
    M = N // 2
    u, v = divmod((a - 1) * (b + 1), N)
    L = (a - b - 4) // 2 + u
    return L >= 0 and L * b <= v <= M - (L + 1) * a - 1
for k in range(5, 12):
    budget()
    N = 1 << (k + 2); M = N // 2
    tested = mism = weird = 0
    for a in range(1, M // 2, 2):
        if not is_prime(N - a): continue
        for b in range(1, M - a + 1, 2):
            if not is_prime(N + b): continue
            ab, prim, w = weird_2kpq(k, N - a, N + b)
            t = ab and w; c = crit(N, a, b); tested += 1; weird += t
            if t != c: mism += 1
    # symmetric confinement (criterion only, all odd b)
    bestA = 0; maxr = 0
    for b in range(1, M // 2, 2):
        runs = []; prev = None
        for a in range(1, min(M // 2, M - b + 1), 2):
            if crit(N, a, b):
                if prev is not None and a == prev + 2: runs[-1][1] = a
                else: runs.append([a, a])
                prev = a
        maxr = max(maxr, len(runs)); bestA = max(bestA, sum(r[1] - r[0] + 2 for r in runs))
    print(f"k={k}: full-range prime pairs tested={tested}, weird={weird}, mismatches={mism}; "
          f"fixed-b: max runs={maxr}, max total length={bestA} (= {bestA/math.sqrt(N):.3f} sqrt N)", flush=True)
