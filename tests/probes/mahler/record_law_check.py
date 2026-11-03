#!/usr/bin/env python3
"""L1399/L1400 (Local, 2026-11-03): a record law for the threshold set E of the greedy 3/2 map G(x) = 3x/2 mod 1.
Run: python3 tests/probes/mahler/record_law_check.py N

tau(X) = the first k >= 1 with G^k(X) > X. E (in the doubled coordinate X = 2a) is {X : tau(X) = infinity} (GC2485).
Conjecture (L1398): Leb{X in (0, 1) : tau(X) > n} ~ c / n, where c = sum_k (2/3)^k z_k = 1.93418 is the Parry
normalisation (z_0 = 1, z_k = G^k-orbit of 1), because a G-orbit near 1 falls to about 1/2 (no clustering of high values),
so tau behaves like an i.i.d. record time (mu-probability ~ 1/n), and the Parry density h tends to 1 at 1.

Prediction, written before the run (L1399): n * Leb{tau > n} is within sampling error of the Poisson value
P_n = n * integral_0^1 exp(-n mu(X, 1)) dX, which the exact density puts at 1.9258 (n = 100) and 1.9334 (n = 200) and
1.9342 from n = 400 on. Counterfactual: values stuck near a constant fraction of c (W3 of band_width_sum_check gave
1.79 +- 0.07 at n = 200) would mean clustering or a failure of the decorrelation the heuristic assumes.

R1 for each n, M exact dyadic starts X = 1 - (D / n) * U, U uniform with K = n + 64 bits, D = 60 (the region below
   1 - D/n contributes about c/n * exp(-D/c), a relative 3e-14); n * Leb = D * (fraction with tau > n). Exact integer
   arithmetic: X = m / 2^K, G^k(X) = m_k / 2^(K+k) with m_(k+1) = 3 m_k mod 2^(K+k+1); G^k(X) > X iff m_k > m * 2^k.
R2 control without the window: uniform X on (2/3, 1) at n = 200, as in W3 with a different seed.
R3 sampler validation: uniform X on (0, 1) at n = 20, 50, 100 (200,000 samples each). At n = 20 the exact value is
   2 * 20 * (1/6 - W1 cumulative through L = 20) = 1.8222 (band_width_sum_check), given R4's identity.
R4 (added after the R1 run) plateau word length versus tau: for 3,000 random ceilings a in (1/3, 1/2) (60-bit dyadic)
   that fall in a band (S_w, T_w] with |w| <= 14, compare |w| with tau(2a). Equality for all of them would make the
   band-width tail beyond length n exactly Leb_a{tau(2a) > n}.
"""
from fractions import Fraction as Fr
import math
import random
import sys

M = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
D = 60
NS = [100, 200, 400, 800, 1600, 3200]


def survives(m, K, n):
    """True iff G^k(m / 2^K) <= m / 2^K for k = 1..n."""
    x, bits = m, K
    for k in range(1, n + 1):
        bits += 1
        x = (3 * x) & ((1 << bits) - 1)
        if x > (m << k):
            return False
    return True


def poisson(n):
    zs, num, den = [1.0], 1, 1
    for _ in range(90):
        num *= 3; den *= 2
        num %= den
        zs.append(num / den)
    w = [(2 / 3) ** k for k in range(len(zs))]
    c = sum(a * b for a, b in zip(w, zs))
    h = lambda X: sum(a for a, b in zip(w, zs) if X < b)
    mu = lambda X: sum(a * max(0.0, b - X) for a, b in zip(w, zs)) / c
    bps = sorted(set([0.0, 1.0] + [t for t in zs if 0 < t < 1]))
    tot = 0.0
    for a, b in zip(bps, bps[1:]):
        s = h((a + b) / 2) / c
        # integral over [a, b] of exp(-n (mu(b) + s (b - X))), written from the right end to avoid overflow
        tot += math.exp(-n * mu(b)) * (1 - math.exp(-n * s * (b - a))) / (n * s)
    return c, n * tot


rng = random.Random(1399)
c, _ = poisson(100)
print('c = %.6f' % c)
for n in NS:
    K = n + 64
    hits = 0
    for _ in range(M):
        u = rng.getrandbits(K)                         # U = u / 2^K
        # X = 1 - (D/n) U, as an exact dyadic m / 2^K' with K' = K + 7 (D/n = 60/n, rounded to a dyadic step)
        Kp = K + 7
        step = (D << Kp) // n                          # (D / n) * 2^Kp, rounded down
        m = (1 << Kp) - ((step * u) >> K) - 1
        if survives(m, Kp, n):
            hits += 1
    p = hits / M
    se = math.sqrt(p * (1 - p) / M)
    Dn = ((D << (K + 7)) // n) / 2 ** (K + 7) * n       # the exact window width times n
    print('R1 n=%5d: %6d of %d survive; n * Leb = %.4f +- %.4f; Poisson P_n = %.4f; ratio %.4f' % (
        n, hits, M, Dn * p, Dn * se, poisson(n)[1], Dn * p / poisson(n)[1]), flush=True)
n = 200; K = n + 64; hits = 0
for _ in range(M):
    m = (2 << K) // 3 + rng.randrange((1 << K) - (2 << K) // 3)
    if survives(m, K, n):
        hits += 1
p = hits / M
print('R2 n=200, X uniform on (2/3, 1): %d of %d survive; n * Leb = %.4f +- %.4f' % (
    hits, M, n * p / 3, n * math.sqrt(p * (1 - p) / M) / 3))
for n in (20, 50, 100):
    K = n + 64; Mv = 200000
    hits = sum(survives(rng.getrandbits(K), K, n) for _ in range(Mv)); p = hits / Mv
    print('R3 n=%3d, X uniform on (0, 1): n * Leb = %.4f +- %.4f; Poisson P_n = %.4f' % (
        n, n * p, n * math.sqrt(p * (1 - p) / Mv), poisson(n)[1]))
r = Fr(2, 3); bands = []
for L in range(2, 15):
    for v in range(1 << (L - 2)):
        w = [1] + [(v >> i) & 1 for i in range(L - 2)] + [0]
        s_ = [1 - b for b in w]
        if any(not s_[i:] > s_[:L - i] for i in range(1, L)):
            continue
        A = sum(r ** j for j in range(L) if w[j]) / 3
        S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
        if S < Fr(1, 2):
            bands.append((S, T, L))
inband = agree = 0
for _ in range(3000):
    a = Fr(1, 3) + Fr(rng.getrandbits(60), 2 ** 60) / 6
    hit = [b for b in bands if b[0] < a <= b[1]]
    if not hit:
        continue
    X = 2 * a; x = X; tau = None
    for k in range(1, 200):
        y = 3 * x / 2; x = y - (y.numerator // y.denominator)
        if x > X:
            tau = k; break
    inband += 1; agree += (hit[0][2] == tau)
print('R4 %d bands with |w| <= 14; %d of 3000 ceilings fall in one; |w| == tau(2a) for %d of them' % (len(bands), inband, agree))
print('RECORD_LAW_DONE')
