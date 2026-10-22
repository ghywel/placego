"""First-moment threshold of the Cramer model for covering the window [M, 2M) by t translates a in [1, R).

E[#covers] ~ C(R-1, t) * exp(-sum_n P(n uncovered)), with P(n uncovered) ~ exp(-t * qbar(n)), qbar(n) the average
over a in [1, R) of -log(1 - q_{n-a}) (q_m = 1/log m for m >= 3, q_2 = 1, q_m = 0 below 2 or for a >= n).
t* = least t with log E[#covers] >= 0 (fewer translates than t* are not expected to cover)."""
import math, sys
import numpy as np
from math import lgamma

def tstar(M, R):
    n = np.arange(M, 2 * M, max(1, M // 2000))
    a = np.arange(1, R, max(1, R // 4000))
    qbar = np.zeros(len(n))
    for i, nn in enumerate(n):
        m = nn - a
        q = np.zeros(len(m))
        ok = m >= 3
        q[ok] = -np.log1p(-1.0 / np.log(m[ok]))
        q[m == 2] = 50.0  # certain
        qbar[i] = q.mean()
    for t in range(1, 2000):
        lc = lgamma(R) - lgamma(t + 1) - lgamma(R - t)
        S = M * np.mean(np.exp(-t * qbar))
        if lc - S >= 0:
            return t
    return None

for M in [int(x) for x in sys.argv[1:]]:
    lm = math.log(M)
    t1 = tstar(M, 2 * M); t2 = tstar(M, M)
    print(f"M={M} lnM={lm:.3f} t*(a<2M)={t1} t*(a<M)={t2} t*/lnM^2={t1/lm**2:.3f} {t2/lm**2:.3f}", flush=True)
