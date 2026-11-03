#!/usr/bin/env python3
"""L1402 (Local, 2026-11-03): the shape of the record-law deficit. Run: python3 tests/probes/mahler/record_law_scan.py N

tau(X) = first k >= 1 with G^k(X) > X, G(x) = 3x/2 mod 1. N exact dyadic X = m / 2^K uniform on (0, 1), K = 1064 bits
(n <= 1000 needs about 585 leading bits), tau capped at NMAX + 1 = 1001; one survival curve S(n) = #(tau > n) / N for
every n <= NMAX. R(n) = n S(n) / P_n with P_n = n * integral exp(-n mu(X, 1)) dX from the exact Parry density (as in
record_law_check.py). Prediction and counterfactual in L1402. S1 cross-checks n = 10, 16, 20 against the exact band sums
(1.6388, 1.7843, 1.8222); S2 prints R(n) on a grid of about 5% steps with its standard error; S3 prints the local
log-slope of R to show dips.
"""
import math
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
NMAX = 1000
K = 1064


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
        tot += math.exp(-n * mu(b)) * (1 - math.exp(-n * s * (b - a))) / (n * s)
    return n * tot


masks = [(1 << (K + k)) - 1 for k in range(NMAX + 2)]
hist = [0] * (NMAX + 2)
rng = random.Random(1402)
for _ in range(N):
    m = rng.getrandbits(K)
    x, thr, tau = m, m, NMAX + 1
    for k in range(1, NMAX + 1):
        x = (3 * x) & masks[k]
        thr <<= 1
        if x > thr:
            tau = k
            break
    hist[tau] += 1
surv = [0] * (NMAX + 2)                     # surv[n] = #(tau > n)
acc = 0
for n in range(NMAX + 1, -1, -1):
    surv[n] = acc
    acc += hist[n]
S = lambda n: surv[n] / N
for n, exact in ((10, 1.6388), (16, 1.7843), (20, 1.8222)):
    se = n * math.sqrt(S(n) * (1 - S(n)) / N)
    print('S1 n=%2d: n S(n) = %.4f +- %.4f; exact band sum %.4f' % (n, n * S(n), se, exact))
grid = sorted(set(int(round(20 * 1.05 ** i)) for i in range(200) if 20 * 1.05 ** i <= NMAX))
prev = None
for n in grid:
    P = poisson(n)
    R = n * S(n) / P
    se = n * math.sqrt(S(n) * (1 - S(n)) / N) / P
    slope = '' if prev is None else '%+.4f' % ((R - prev[1]) / math.log(n / prev[0]))
    print('S2 n=%4d: n S(n) = %.4f; P_n = %.4f; R = %.4f +- %.4f  S3 dR/dlog n %s' % (n, n * S(n), P, R, se, slope))
    prev = (n, R)
print('RECORD_LAW_SCAN_DONE')
