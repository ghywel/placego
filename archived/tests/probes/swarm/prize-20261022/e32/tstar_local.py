"""First-moment threshold with local structure: a 'typical' A equidistributed mod P(z) leaves each n with t/kappa
alive shifts, each prime with probability kappa*q (q = 1/log(n-a)).  P(n uncovered) ~ exp((t/kappa) log(1 - kappa q)).
t*_z = least t with log C(M-1, t) >= M * mean_n P(n uncovered); shifts a < M (the better family in tstar.py)."""
import math, sys
import numpy as np
from math import lgamma
def tstar_z(M, kappa):
    n = np.arange(M, 2 * M, max(1, M // 1000))
    a = np.arange(1, M, max(1, M // 2000))
    Lbar = np.zeros(len(n))
    for i, nn in enumerate(n):
        m = (nn - a).astype(float)
        x = np.minimum(0.999, kappa / np.log(np.maximum(m, 3.0)))
        Lbar[i] = np.mean(-np.log1p(-x)) / kappa   # per-shift exponent after dividing alive share
    for t in range(1, 3000):
        lc = lgamma(M) - lgamma(t + 1) - lgamma(M - t)
        if lc >= M * np.mean(np.exp(-t * Lbar)):
            return t
for M in [int(x) for x in sys.argv[1:]]:
    out = [tstar_z(M, k) for k in (1.0, 3.75, 5.2135)]
    print(f"M={M} t*: kappa=1 (Cramer) {out[0]}  z=5 {out[1]}  z=13 {out[2]}", flush=True)
