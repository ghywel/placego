#!/usr/bin/env python3
"""L1669 addendum 2 (Local, 12 November 2026): a first look at the exponential sums over valid words.

For the boundary words p of length m (valid, cannot take a 1) put y(p) = N_(m+1)(p1) in Z/2^(m+1), so that
D_m = #{p : y(p) < 2^m}.  G(h) = sum_p e(-h y(p)/M), gamma(h) = |G(h)| / B_m, n = h 3^(-m) mod M, and
NS(n) = #{u < m : || n 3^u / 2^(u+2) || >= 1/5}.  For all 2^m words gamma is the Riesz product and is at
most cos(pi/5)^NS.  The question: does gamma fall with NS on the valid words too?
Predictions K1, K2 are in L1669's second addendum, written before this file was run.
Exact integers for the points; floats in the transform.  Nothing above 2^19 is walked.
"""
import sys
import time

import numpy as np

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from local_arc_certificate import census, tower   # noqa: E402


def ns_count(m):
    M = 1 << (m + 1)
    n = np.arange(M, dtype=np.int64)
    c = np.zeros(M, dtype=np.int64)
    for u in range(m):
        mm = 1 << (u + 2)
        x = ((n % mm) * pow(3, u, mm)) % mm
        d = np.minimum(x, mm - x)
        c += (5 * d >= mm)
    return c


def main():
    t0 = time.time()
    cs, ds = tower(64)
    mmax = 18
    levels = census(mmax, ds)
    for m in (12, 14, 16, 18):
        M = 1 << (m + 1)
        pts = [r + (((x & 1) ^ 1) << m) for r, x, st, C, par in levels[m] if ds[st] == 0]
        B = len(pts)
        D = sum(1 for y in pts if y < (1 << m))
        ind = np.zeros(M)
        ind[pts] = 1.0
        gam = np.abs(np.fft.fft(ind)) / B
        g = pow(3, -m, M)
        h = np.arange(M, dtype=np.int64)
        nn = (h * g) % M
        ns = ns_count(m)[nn]
        odd = (h % 2 == 1)
        go, no = gam[odd], ns[odd]
        j = int(np.argmax(go))
        cmin = int(no.min())
        # the Fourier bound for the count itself
        hh = h[odd]
        up = float((go / (M * np.abs(np.sin(np.pi * hh / M)))).sum())
        print('m = %d: B = %d, D = %d, |D/B - 1/2| = %.4f <= Fourier sum %.4f; typical gamma 1/sqrt(B) = %.3f'
              % (m, B, D, abs(D / B - 0.5), up, B ** -0.5))
        print('   largest gamma over odd h: %.4f at h = %d, with NS = %d (least NS over odd n: %d)'
              % (go[j], int(hh[j]), int(no[j]), cmin))
        print('   NS : number of odd h, largest gamma, root mean square gamma')
        for c in range(cmin, m + 1):
            sel = no == c
            if sel.any():
                print('   %2d : %7d  %.4f  %.4f' % (c, int(sel.sum()), float(go[sel].max()),
                                                  float(np.sqrt((go[sel] ** 2).mean()))))
        big = no >= (m + 1) // 2
        print('   K1 largest gamma over NS >= m/2: %.4f;   K2 NS at the largest gamma minus the least NS: %d'
              % (float(go[big].max()), int(no[j]) - cmin))
    print('elapsed %.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
