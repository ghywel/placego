#!/usr/bin/env python3
"""L1667 addendum 2 (Local, 12 November 2026): the arc certificate for the unconditional first check.

O_w = #{n < 2^w : T^w(n) odd}, T(n) = ceil(3n/2).  GC2936 section 2 proves 1/4 <= O_w / 2^w <= 3/4.
Here every prefix is allowed, so the family after a prefix p'' of length l is all 2^k words s, and
    #{s : chi(p''s) = 1} = #{y in theta Y_k : y in [a, a + 2^k)}   in Z/2^(k+1),
with Y_k = {n < 2^(k+1) : T^k(n) odd}, theta = 3^(-l), a = theta x''.  So for every w >= k
    lo_k 2^(w-k) <= O_w <= hi_k 2^(w-k),
lo_k and hi_k the least and greatest half-circle counts over every multiplier and rotation.
Section j = 2: the same for each of the four forced pairs, arcs of length 2^k in Z/2^(k+2).

Exact integers.  Nothing above 2^(KMAX+2) is walked.
Run: python3 tests/probes/mahler/local_arc_unconditional.py [KMAX [KMAX2]]
"""
import sys
import time

import numpy as np


def thetas(K):
    M = 1 << K
    inv3 = pow(3, -1, M)
    out, th = [], 1
    while True:
        out.append(th)
        th = th * inv3 % M
        if th == 1:
            return np.array(out, dtype=np.int64)


def iterate(K, k):
    """T^k(n) for every n < 2^K."""
    x = np.arange(1 << K, dtype=np.int64)
    for _ in range(k):
        x = (3 * x + 1) >> 1
    return x


def arc_extremes(Y, K, k):
    """Least and greatest number of points of theta Y in an arc of 2^k residues of Z/2^K, over
    every power theta of 3 and every rotation; and where the least sits."""
    M, h = 1 << K, 1 << k
    ths = thetas(K)
    Y = np.asarray(Y, dtype=np.int64)
    lo, hi, lo_at = None, None, None
    step = max(1, (1 << 24) // (2 * M))
    for s0 in range(0, len(ths), step):
        t = ths[s0:s0 + step]
        R = len(t)
        P = (t[:, None] * Y[None, :]) % M
        ind = np.zeros((R, 2 * M + 1), dtype=np.int32)
        rows = np.repeat(np.arange(R), len(Y))
        ind[rows, P.ravel() + 1] = 1
        ind[rows, P.ravel() + 1 + M] = 1
        cs = np.cumsum(ind, axis=1, dtype=np.int32)
        cnt = cs[:, h:h + M] - cs[:, 0:M]
        mn, mx = cnt.min(axis=1), cnt.max(axis=1)
        q = int(np.argmin(mn))
        if lo is None or mn[q] < lo:
            lo, lo_at = int(mn[q]), (s0 + q, int(t[q]), int(np.argmin(cnt[q])))
        hi = int(mx.max()) if hi is None else max(hi, int(mx.max()))
    return lo, hi, lo_at


def main():
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    kmax2 = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    assert kmax <= 16 and kmax2 <= 14
    t0 = time.time()

    # controls: O_w itself, against GC2936's bounds and Cloud's excess table
    print('== controls')
    excess = []
    for w in range(2, 21):
        x = iterate(w, w)
        O = int((x & 1).sum())
        d = (2 ** w + 2 * (-1) ** w) // 3
        assert d <= O <= 2 ** w - d and O % 2 == 0
        excess.append(O - 2 ** (w - 1))
    cloud = [0, -2, -2, -6, -2, -2, -2, 14, 10, 2, -2, -30, -146, -94, -174, -74, -102, -94, -78]
    print('   O_w - 2^(w-1), w = 2..20: %s' % excess)
    print('   equal to CL782\'s table: %s; inside GC2936\'s bounds d_w <= O_w <= 2^w - d_w: True' % (excess == cloud))
    assert excess == cloud

    print('\n== one forced bit: for every w >= k, lo/2^k <= O_w / 2^w <= hi/2^k')
    rows = {}
    for k in range(1, kmax + 1):
        K = k + 1
        Y = np.nonzero(iterate(K, k) & 1)[0]
        assert len(Y) == 1 << k
        lo, hi, at = arc_extremes(Y, K, k)
        assert lo + hi == 1 << k
        rows[k] = (lo, hi)
        print('   k = %2d: lo = %6d, hi = %6d of %6d: share in [%.5f, %.5f]; half-width %.5f '
              '(least at prefix length %d mod %d, multiplier %d, rotation %d)   %.0f s'
              % (k, lo, hi, 1 << k, lo / 2 ** k, hi / 2 ** k, 0.5 - lo / 2 ** k, at[0], 1 << max(k - 1, 0),
                 at[1], at[2], time.time() - t0))
        sys.stdout.flush()
    # the bound against the truth
    ok = True
    for k, (lo, hi) in rows.items():
        for w in range(max(k, 2), 21):
            O = excess[w - 2] + 2 ** (w - 1)
            if not lo * 2 ** (w - k) <= O <= hi * 2 ** (w - k):
                ok = False
    print('   every row bounds the true O_w for k <= w <= 20: %s' % ok)
    if 12 in rows:
        print('U1 half-width at k = 12: %.5f (predicted at most 0.10)' % (0.5 - rows[12][0] / 4096))
    if 14 in rows:
        print('U2 half-width at k = 14: %.5f (predicted at most 0.06)' % (0.5 - rows[14][0] / 16384))

    print('\n== two forced bits: share of each forced pair among all n < 2^w, w >= k')
    for k in range(2, kmax2 + 1):
        K = k + 2
        x = iterate(K, k)
        pair = (x & 1) + 2 * (((3 * x + 1) >> 1) & 1)
        out = []
        for v in range(4):
            Y = np.nonzero(pair == v)[0]
            lo, hi, at = arc_extremes(Y, K, k)
            out.append((lo / 2 ** k, hi / 2 ** k))
        print('   k = %2d: pairs 00, 10, 01, 11 in %s   %.0f s'
              % (k, ', '.join('[%.4f, %.4f]' % o for o in out), time.time() - t0))
        sys.stdout.flush()
    print('elapsed %.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
