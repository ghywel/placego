"""Unexpected check: does a greedy cover tailored to one window keep any covering power on fresh windows?

Compute the primes' greedy cover A of W0 = [M, 2M), M = 2^16. Then for fresh windows [X, X + M) measure the
uncovered fraction (no a in A with n - a prime) and compare with independence predictions:
  Cramer:   mean_n prod_{a<n} (1 - 1/log(n-a))
  local z:  mean_n prod_{a<n, gcd(n-a, P(z))=1} (1 - kappa_z/log(n-a))   (Granville-type, z = 5, 13)
Also report the same quantities on W0 itself (where the uncovered fraction is 0 by construction).
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from greedy import sieve, greedy_cover

M = 1 << 16
Xs = [M, 3 * M, 8 * M, 64 * M, 1024 * M]
Lsieve = 1024 * M + M + 10
isp = sieve(Lsieve)
A, _ = greedy_cover(M, isp)
A = np.array(sorted(A))
print("greedy |A| =", len(A), " A mod 2 counts:", np.bincount(A % 2, minlength=2), " mod 3:", np.bincount(A % 3, minlength=3))

def preds(n, A, z):
    P = 1; kappa = 1.0
    for p in [2, 3, 5, 7, 11, 13]:
        if p <= z:
            P *= p; kappa *= p / (p - 1.0)
    out = np.zeros(len(n))
    for a in A:
        m = n - a
        ok = m >= 3
        if z > 1:
            ok &= (np.gcd(m, P) == 1)
        f = np.zeros(len(n))
        f[ok] = np.log1p(-np.minimum(0.999, kappa / np.log(m[ok].astype(float))))
        out += f
    return np.exp(out).mean()

for X in Xs:
    n = np.arange(X, X + M, dtype=np.int64)
    cov = np.zeros(M, dtype=bool)
    for a in A:
        m = n - a
        okm = (m >= 2)
        cov[okm] |= isp[m[okm]]
    unc = 1.0 - cov.mean()
    lam = np.mean([np.sum(1.0 / np.log((nn - A[A < nn - 2]).astype(float))) for nn in n[::997]])
    print(f"window [{X},{X+M}): uncovered={unc:.5f}  pred Cramer={preds(n, A, 1):.5f}  pred z=5={preds(n, A, 5):.5f}"
          f"  pred z=13={preds(n, A, 13):.5f}  mean lambda={lam:.3f}  e^-lambda={math.exp(-lam):.5f}", flush=True)
