# Distribution of |J(a)|*a/N over consecutive odd a (criterion only), and where J(a) starts relative to a.
# PREDICTION: a positive proportion (>= 30%) of a in [N^0.55, N^0.6] have |J(a)|*a/N >= 0.1; J(a) is always one run.
import sys
sys.path.insert(0, 'e470')
from wlib import *
def crit(N, a, b):
    M = N // 2
    u, v = divmod((a - 1) * (b + 1), N)
    L = (a - b - 4) // 2 + u
    return L >= 0 and L * b <= v <= M - (L + 1) * a - 1
for k in (26, 30):
    budget()
    N = 1 << (k + 2); M = N // 2
    A0 = int(N ** 0.55) | 1; A1 = int(N ** 0.6)
    vals = []; maxruns = 0; offs = []
    step = 2 * max(1, (A1 - A0) // 1200)
    for a in range(A0, A1, step):
        lo = max(1, a - 3 * N // a - 10); hi = min(M - a, a + 8 * a * a // N + 3 * N // a + 10)
        runs = []; prev = None
        for b in range(lo | 1, hi + 1, 2):
            if crit(N, a, b):
                if prev is not None and b == prev + 2: runs[-1][1] = b
                else: runs.append([b, b])
                prev = b
        maxruns = max(maxruns, len(runs))
        tot = sum(r[1] - r[0] + 2 for r in runs)
        vals.append(tot * a / N)
        if runs: offs.append((runs[0][0] - a) * a / N)
    vals.sort()
    n = len(vals)
    print(f"k={k}: a in [N^0.55,N^0.6], {n} values; max runs per a = {maxruns}; "
          f"fraction with |J|a/N >= 0.1: {sum(v >= 0.1 for v in vals)/n:.3f}, >= 0.2: {sum(v >= 0.2 for v in vals)/n:.3f}, "
          f"empty: {sum(v == 0 for v in vals)/n:.3f}; median {vals[n//2]:.3f}, max {vals[-1]:.3f}; "
          f"start offset (b_start - a)*a/N range [{min(offs):.2f}, {max(offs):.2f}]", flush=True)
