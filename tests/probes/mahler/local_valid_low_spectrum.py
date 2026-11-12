#!/usr/bin/env python3
"""L1670 addendum 3 (Local, 12 November 2026): is the low-frequency spectrum of the valid starts flat?

gamma_w(h) = |sum over valid starts r of e(h r / 2^w)| / A(w).  Parseval makes the mean of A(w) gamma^2 over ALL
frequencies exactly 1.  The question is whether the low frequencies, the ones that decide the count in short
intervals, are typical.  Prediction S1 is in L1670's third addendum, written before this file was run.
Exact starts; floats only in the sums.  At most 7 * 10^8 phases per length.
"""
import math
import sys
import time

import numpy as np

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from local_valid_equidistribution import census, digits, renewal   # noqa: E402


def main():
    t0 = time.time()
    ds = digits(200)
    F, A, B = renewal(ds, 60)
    targets = {24: 12, 28: 10, 32: 9}
    ok = True
    for w, R, st, W, FM in census(32, ds, 0):
        if w not in targets:
            continue
        jmax = targets[w]
        n = len(R)
        assert n == A[w]
        theta = (R & np.uint64((1 << w) - 1)).astype(np.float64) * (2 * math.pi / float(1 << w))
        hmax = 1 << (jmax + 1)
        g2 = np.zeros(hmax)
        step = max(1, (1 << 23) // n)
        for a in range(1, hmax, step):
            hs = np.arange(a, min(a + step, hmax), dtype=np.float64)
            ang = np.outer(hs, theta)
            g2[a:a + len(hs)] = (np.cos(ang).sum(axis=1) ** 2 + np.sin(ang).sum(axis=1) ** 2) / float(n) ** 2
        print('w = %d, A = %d, frequencies 1 .. %d (%.0f s)' % (w, n, hmax - 1, time.time() - t0))
        print('   k : mean of A gamma^2 over 2^k <= h < 2^(k+1), largest sqrt(A) gamma there, '
              'sum of gamma over h < 2^(k+1) divided by 2^(k+1)/sqrt(A)')
        for k in range(0, jmax + 1):
            seg = g2[1 << k: 1 << (k + 1)]
            mean = float(seg.mean() * n)
            big = float(math.sqrt(seg.max() * n))
            tot = float(np.sqrt(g2[1: 1 << (k + 1)]).sum() / ((1 << (k + 1)) / math.sqrt(n)))
            print('   %2d : %.3f  %.3f  %.3f' % (k, mean, big, tot))
            if k >= 3 and not (0.5 <= mean <= 2.0):
                ok = False
        sys.stdout.flush()
    print('S1 %s: the mean of A gamma^2 over every dyadic range with k >= 3 is between 0.5 and 2'
          % ('HELD' if ok else 'REFUTED'))
    print('done in %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
