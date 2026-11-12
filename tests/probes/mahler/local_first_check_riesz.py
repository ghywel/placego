#!/usr/bin/env python3
"""L1669 (Local, 12 November 2026): the unconditional first check as a Riesz product.

T(n) = ceil(3n/2).  Y_w = {n mod 2^(w+1) : T^w(n) odd}, M = 2^(w+1), O_w = #(Y_w in [0, 2^w)).
For odd n put  y_u = n 3^u / 2^(u+2) mod 1  and  rho_w(n) = prod_{u<w} |cos(pi y_u)|.

Claims tested (hand statements in L1669, written before this file was run):
 R1  |sum_{y in Y_w} e(-h y / M)| = 2^w rho_w(h 3^(-w) mod M)   for every h.
 R2  for every power theta of 3 and every rotation a,
       sqrt(2) max_h rho/(M |sin(pi h/M)|)  <=  max_a |#(theta Y_k in arc a)/2^k - 1/2|
                                            <=  (1/M) sum_{h odd} rho_k(h theta 3^(-k)) / |sin(pi h/M)|.
 R3  rho*_k = max over odd n of rho_k(n), against the certified half-widths of run 3.
 R4  the run lemma: if ||y_u|| < 1/5 and ||y_(u+1)|| < 1/5 then ||y_(u+1)|| = 1.5 ||y_u||;
     ||y_u|| >= 2^-(u+2); hence the non-small indices u_1 = 0 < u_2 < ... obey
     u_(r+1) < u_r + 2 + log_1.5(2^(u_r+3)/5), and rho*_k <= cos(pi/5)^N(k).
Exact integers for the residues; floats only in the cosines.  Nothing above 2^23 is walked.
Run: python3 tests/probes/mahler/local_first_check_riesz.py [KMAX_BRUTE [KMAX_BB]]
"""
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np


def iterate(K, k):
    x = np.arange(1 << K, dtype=np.int64)
    for _ in range(k):
        x = (3 * x + 1) >> 1
    return x


def rho_all(k):
    """rho_k(n) for every residue n mod 2^(k+1) (even n included, by the same formula)."""
    M = 1 << (k + 1)
    n = np.arange(M, dtype=np.int64)
    r = np.ones(M)
    for u in range(k):
        m = 1 << (u + 2)
        x = ((n % m) * pow(3, u, m)) % m
        r *= np.abs(np.cos(np.pi * x / m))
    return r


def thetas(K):
    M = 1 << K
    inv3 = pow(3, -1, M)
    out, th = [], 1
    while True:
        out.append(th)
        th = th * inv3 % M
        if th == 1:
            return out


def nonsmall_bound(k):
    """N(k): the least possible number of indices u < k with ||y_u|| >= 1/5, from the run lemma."""
    u, cnt = 0, 1
    while True:
        lim = u + 2 + math.log(2.0 ** (u + 3) / 5) / math.log(1.5)
        nxt = math.ceil(lim) - 1          # the largest integer strictly below lim
        if nxt >= k:
            return cnt
        u, cnt = nxt, cnt + 1


def best_product(k, beam=4000, cap=20000000):
    """rho*_k by depth-first search over the bits of n, pruned by the best product found.
    A beam search supplies the first candidate.  Returns (value, n, nodes, finished)."""
    cosv, pi = math.cos, math.pi
    pw = [pow(3, u, 1 << (u + 2)) for u in range(k)]
    level = [(abs(cosv(pi / 4)), 1)]
    for u in range(1, k):
        m = 1 << (u + 2)
        nxt = []
        for p, n in level:
            for b in (0, 1):
                n2 = n + (b << (u + 1))
                nxt.append((p * abs(cosv(pi * ((n2 * pw[u]) % m) / m)), n2))
        nxt.sort(reverse=True)
        level = nxt[:beam]
    best = list(level[0])
    stack = [(1, 1, abs(cosv(pi / 4)))]          # n mod 2^(u+1), factors done, product
    nodes = 0
    while stack:
        n, u, p = stack.pop()
        nodes += 1
        if nodes > cap:
            return best[0], best[1], nodes, False
        if u == k:
            if p > best[0]:
                best = [p, n]
            continue
        m = 1 << (u + 2)
        for b in (0, 1):
            n2 = n + (b << (u + 1))
            q = p * abs(cosv(pi * ((n2 * pw[u]) % m) / m))
            if q > best[0]:
                stack.append((n2, u + 1, q))
    return best[0], best[1], nodes, True


def main():
    kb = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    kbb = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    assert kb <= 22
    t0 = time.time()
    # certified half-widths from run 3 (lo of 2^k), k = 3..15
    lo3 = {3: 1, 4: 3, 5: 8, 6: 18, 7: 38, 8: 79, 9: 173, 10: 362, 11: 746, 12: 1523, 13: 3149,
           14: 6527, 15: 13600}
    eps = {k: 0.5 - v / 2 ** k for k, v in lo3.items()}

    print('== R1 the Fourier transform of Y_w against the product')
    worst = 0.0
    for w in range(1, 13):
        M = 1 << (w + 1)
        ind = (iterate(w + 1, w) & 1).astype(float)
        F = np.abs(np.fft.fft(ind))
        r = rho_all(w)
        g = pow(3, -w, M)
        h = np.arange(M, dtype=np.int64)
        worst = max(worst, float(np.abs(F - 2 ** w * r[(h * g) % M]).max()) / 2 ** w)
    print('   largest | |FT(h)| / 2^w - rho_w(h 3^-w) | over every h, w = 1..12: %.2e' % worst)
    r1 = worst < 1e-9
    print('R1: %s' % r1)

    print('\n== R2 the two-sided Fourier bound against the exact arc extremes (every multiplier)')
    r2 = True
    for k in range(3, 14):
        M = 1 << (k + 1)
        r = rho_all(k)
        h = np.arange(1, M, 2, dtype=np.int64)
        wgt = 1.0 / (M * np.abs(np.sin(np.pi * h / M)))
        g = pow(3, -k, M)
        up = lo = 0.0
        for th in thetas(k + 1):
            v = r[(h * ((th * g) % M)) % M] * wgt
            up = max(up, float(v.sum()))
            lo = max(lo, math.sqrt(2) * float(v.max()))
        ok = lo <= eps[k] + 1e-12 and eps[k] <= up + 1e-12
        r2 = r2 and ok
        print('   k = %2d: lower %.5f <= certified half-width %.5f <= upper %.5f   %s'
              % (k, lo, eps[k], up, 'ok' if ok else 'FAILS'))
    print('R2: %s' % r2)
    # and for the true O_w
    ok = True
    for w in range(2, 21):
        M = 1 << (w + 1)
        O = int((iterate(w, w) & 1).sum())
        r = rho_all(w)
        h = np.arange(1, M, 2, dtype=np.int64)
        up = float((r[(h * pow(3, -w, M)) % M] / (M * np.abs(np.sin(np.pi * h / M)))).sum())
        if abs(O / 2 ** w - 0.5) > up + 1e-12:
            ok = False
    print('   the same upper bound holds for the true O_w, w = 2..20: %s' % ok)

    print('\n== R3 the largest product rho*_k')
    star = {}
    for k in range(3, kb + 1):
        r = rho_all(k)
        odd = r[1::2]
        j = int(np.argmax(odd))
        star[k] = (float(odd[j]), 2 * j + 1)
    for k in range(3, kb + 1):
        e = eps.get(k)
        print('   k = %2d: rho* = %.6f at n = %d%s%s'
              % (k, star[k][0], star[k][1],
                 '' if k - 1 not in star else '   ratio to k-1: %.4f' % (star[k][0] / star[k - 1][0]),
                 '' if e is None else '   half-width / rho* = %.3f' % (e / star[k][0])))
    ratios = [eps[k] / star[k][0] for k in range(8, 16)]
    steps = [star[k][0] / star[k - 1][0] for k in range(11, kb + 1)]
    print('R3 half-width / rho* for k = 8..15 lies in [%.3f, %.3f] (predicted inside [0.3, 3]); '
          'step ratios for k = 11..%d lie in [%.3f, %.3f] (predicted inside [0.80, 0.92])'
          % (min(ratios), max(ratios), kb, min(steps), max(steps)))
    print('   by search over the bits of n (branch and bound):')
    prev = None
    for k in [16, 20, 22, 24, 28, 32, 40, 48, 56, 64]:
        if k > kbb:
            break
        p, n, nodes, done = best_product(k)
        chk = '' if k not in star else '   (brute force %.6e)' % star[k][0]
        rate = '' if prev is None else '   per step since k = %d: %.4f' % (prev[0], (p / prev[1]) ** (1.0 / (k - prev[0])))
        print('   k = %2d: rho* %s %.6e, nodes %d%s%s   proved bound cos(pi/5)^N = %.4f'
              % (k, '=' if done else '>=', p, nodes, chk, rate, math.cos(math.pi / 5) ** nonsmall_bound(k)))
        prev = (k, p)
        sys.stdout.flush()

    print('\n== R4 the run lemma, every odd n mod 2^(k+1), k = 20')
    k = 20
    M = 1 << (k + 1)
    n = np.arange(1, M, 2, dtype=np.int64)
    dist = []
    for u in range(k):
        m = 1 << (u + 2)
        x = ((n % m) * pow(3, u, m)) % m
        d = np.minimum(x, m - x)                     # ||y_u|| = d / m, exactly
        dist.append(d)
    okA = all(int(dist[u].min()) >= 1 for u in range(k))
    okB = True
    for u in range(k - 1):
        m = 1 << (u + 2)
        both = (5 * dist[u] < m) & (5 * dist[u + 1] < 2 * m)
        if not np.array_equal(dist[u + 1][both], 3 * dist[u][both]):   # d'/(2m) = 1.5 d/m
            okB = False
    small = np.stack([5 * dist[u] < (1 << (u + 2)) for u in range(k)])   # True where ||y_u|| < 1/5
    cnt = (~small).sum(axis=0)
    okC = True
    for kk in range(1, k + 1):
        c = (~small[:kk]).sum(axis=0)
        if int(c.min()) < nonsmall_bound(kk):
            okC = False
    okD = all(star[kk][0] <= math.cos(math.pi / 5) ** nonsmall_bound(kk) + 1e-12 for kk in star)
    print('   ||y_u|| >= 2^-(u+2): %s;  growth by 3/2 inside a run: %s;  non-small count >= N(k) for every '
          'k <= 20: %s (least count at k = 20: %d, N(20) = %d);  rho*_k <= cos(pi/5)^N(k), k <= %d: %s'
          % (okA, okB, okC, int(cnt.min()), nonsmall_bound(20), kb, okD))
    print('R4: %s' % (okA and okB and okC and okD))
    print('   N(k) for k = 10, 100, 1000, 10^4, 10^6: %s'
          % [nonsmall_bound(x) for x in (10, 100, 1000, 10 ** 4, 10 ** 6)])
    print('elapsed %.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
