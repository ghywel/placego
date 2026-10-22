#!/usr/bin/env python3
"""Hypothesis (H) for the two-centre route: the weight g(z) = 1/r2(N(z)) on a lattice disk has its Fourier mass, after
removing the mean times the disk indicator, only near rationals with small denominators coming from split primes
(5, 13, 25, 65, ...). Measure the top peaks of |g^ - mean*1disk^| / g^(0) and their rational locations, for growing L.
Grid G = 1560 = 2^3*3*5*13 so that a/q with q | G sit exactly on the grid."""
import math, time
import numpy as np
from fractions import Fraction
T0 = time.time()
G = 1560
for L in [200, 350, 500, 700]:
    X = L * L
    r = np.zeros(X + 1, np.int64)
    a = np.arange(-L, L + 1); A, B = np.meshgrid(a, a, indexing='ij'); N = A * A + B * B
    inside = (N <= X) & (N > 0)
    np.add.at(r, N[N <= X], 1)
    g = np.zeros((G, G)); d = np.zeros((G, G))
    gi = np.where(inside, 1.0 / np.maximum(r[np.minimum(N, X)], 1), 0.0)
    g[A % G, B % G] = gi; d[A % G, B % G] = inside.astype(float)
    Fg = np.fft.fft2(g); Fd = np.fft.fft2(d)
    mass = Fg[0, 0].real; mean = mass / Fd[0, 0].real
    H = np.abs(Fg - mean * Fd) / mass
    H[0, 0] = 0
    flat = np.argsort(H.ravel())[::-1][:12]
    peaks = []
    for idx in flat:
        i, j = divmod(int(idx), G)
        fi = Fraction(i, G).limit_denominator(60); fj = Fraction(j, G).limit_denominator(60)
        q = math.lcm(fi.denominator, fj.denominator)
        peaks.append(f'({fi},{fj}) q={q}: {H[i, j]:.4f}')
    # largest value at frequencies whose denominator is NOT a product of split primes (5,13 and powers) times 1
    ii, jj = np.meshgrid(np.arange(G), np.arange(G), indexing='ij')
    qi = G // np.gcd(ii, G); qj = G // np.gcd(jj, G); qq = np.lcm(qi, qj)
    splitok = np.isin(qq, [1, 5, 13, 65])
    big_nonsplit = H[~splitok].max()
    print(f'L={L} mean(g)={mean:.4f} (mean*sqrt(ln X)={mean*math.sqrt(math.log(X)):.3f}) | max off split-denominators: {big_nonsplit:.4f}', flush=True)
    print('   top peaks:', '; '.join(peaks[:8]), flush=True)
print('time', round(time.time() - T0, 1))
