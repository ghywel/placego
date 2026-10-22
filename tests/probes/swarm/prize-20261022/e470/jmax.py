# PREDICTION: for every odd a < N/4, the odd b in (0, M-a] satisfying the exact criterion form one run of length
# <= sqrt(N/2) + O(1) (max near a ~ sqrt(N/2)); counterfactual: any run total > 0.75 sqrt(N), or > 1 run.
import sys
sys.path.insert(0, 'e470')
from wlib import *
def crit(N, a, b):
    M = N // 2
    u, v = divmod((a - 1) * (b + 1), N)
    L = (a - b - 4) // 2 + u
    return L >= 0 and L * b <= v <= M - (L + 1) * a - 1
for k in (12, 14, 16):
    budget()
    N = 1 << (k + 2); M = N // 2
    best = (0, 0); maxruns = 0
    for a in range(1, N // 4, 2 if k <= 12 else 6):
        runs = []; prev = None
        for b in range(1, M - a + 1, 2):   # FULL b range, no window assumption
            if crit(N, a, b):
                if prev is not None and b == prev + 2: runs[-1][1] = b
                else: runs.append([b, b])
                prev = b
        maxruns = max(maxruns, len(runs))
        tot = sum(r[1] - r[0] + 2 for r in runs)
        if tot > best[0]: best = (tot, a)
    print(f"k={k} N={N}: max total |J(a)| = {best[0]} at a = {best[1]}; /sqrt(N) = {best[0]/math.sqrt(N):.3f} "
          f"(sqrt(1/2)=0.707); a/sqrt(N) = {best[1]/math.sqrt(N):.3f}; max runs = {maxruns}", flush=True)
