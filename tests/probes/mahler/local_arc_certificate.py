#!/usr/bin/env python3
"""L1667 (Local, 12 November 2026): rotation ("arc") certificates for Mahler's first check.

T(n) = ceil(3n/2).  A word is valid while every tail of its zero-padded code is below 1/2
(the 3/2 beta-shift).  For a valid word p of length m, r(p) < 2^m is the start with that parity
word, x(p) = T^m(r(p)), and chi(p) = x(p) mod 2 is the first forced parity.  A boundary word is
valid and cannot take a 1.  B_m counts them, D_m those with chi = 1.

The statement tested (L1667).  Write p = p''s with |p''| = l, |s| = k.  Then
    r(p''s) = r'' + 2^l t(s),  t(s) = theta (N_k(s) - x'') mod 2^k,  theta = 3^(-l),
so the prefix acts on the fixed set theta N_k(S) as a rotation of the cycle Z/2^k.
 (a) residues of r modulo 3: all equal for some rotation iff at most one cyclic gap is prime to 3;
 (b) the forced bits: the number of s with chi = 1 is the number of points theta N_(k+1)(s1)
     in an arc of 2^k consecutive residues of Z/2^(k+1);
 (c) with j forced bits: the number of s whose p''s stays valid through j more steps is the
     number of points theta N_(k+j)(w), w valid of length k+j, in an arc of length 2^k of Z/2^(k+j).
Predictions P1..P5 and their counterfactuals are in L1667, pushed before this file was run.

Exact integers and Fractions only.  No start above 2^22 is enumerated.
Run: python3 tests/probes/mahler/local_arc_certificate.py [KMAX1 [KMAX2 [MMAX]]]
"""
from fractions import Fraction as Fr
import json
import sys
import time

import numpy as np

TWO3 = Fr(2, 3)
NSTATE = 40          # prefix states carried; the rest get the trivial bound


def T(n):
    return (3 * n + 1) // 2


def slack_step(c, b):
    """Slack c = 2 M in (0, 1]; None if b cannot be appended."""
    if b == 0:
        c2 = c * 3 / 2
        return c2 if c2 < 1 else Fr(1)
    if c > TWO3:
        return c * 3 / 2 - 1
    return None


def tower(n):
    """c_0 = 1, d_i = [c_i > 2/3], c_(i+1) = 3 c_i / 2 - d_i: the greedy orbit and digits of 1."""
    c, cs, ds = Fr(1), [], []
    for _ in range(n):
        cs.append(c)
        d = 1 if c > TWO3 else 0
        ds.append(d)
        c = c * 3 / 2 - d
    return cs, ds


def extend(r, x, i, b):
    """Append parity b at position i to the start r < 2^i with x = T^i(r)."""
    eps = (x & 1) ^ b
    return r + (eps << i), (3 * x + eps * 3 ** (i + 1) + b) >> 1


def words(c0, n):
    """All valid continuations of length n from slack c0: (N_n(word), T^n(N_n), final slack)."""
    out = [(0, 0, c0)]
    for i in range(n):
        nxt = []
        for r, x, c in out:
            for b in (0, 1):
                c2 = slack_step(c, b)
                if c2 is not None:
                    r2, x2 = extend(r, x, i, b)
                    nxt.append((r2, x2, c2))
        out = nxt
    return out


def thetas(K):
    """3^(-l) mod 2^K for l = 0, 1, ..., ord - 1."""
    M = 1 << K
    inv3 = pow(3, -1, M)
    out, th = [], 1
    while True:
        out.append(th)
        th = th * inv3 % M
        if th == 1:
            return out


def arc_minmax_simple(X, K, k, ths):
    """Per theta: min and max over a of #{x in theta X mod 2^K : x in [a, a + 2^k)}.  One theta at a time."""
    M, h = 1 << K, 1 << k
    X = np.asarray(X, dtype=np.int64)
    n = len(X)
    res = np.zeros((len(ths), 2), dtype=np.int64)
    if n == 0:
        return res
    ar = np.arange(n)
    for q, th in enumerate(ths):
        p = np.sort((X * th) % M)
        dbl = np.concatenate((p, p + M))
        res[q, 1] = (np.searchsorted(dbl, p + h, 'left') - ar).max()
        res[q, 0] = (np.searchsorted(dbl, p + h + 1, 'left') - ar - 1).min()
    return res


def arc_minmax(X, K, k, ths):
    """The same table, many multipliers at a time (run 2).  The maximum is attained by an arc that
    starts at a point, the minimum by one that starts just after a point."""
    M, h = 1 << K, 1 << k
    X = np.asarray(X, dtype=np.int64)
    n, nt = len(X), len(ths)
    res = np.zeros((nt, 2), dtype=np.int64)
    if n == 0:
        return res
    if n == 1:
        res[:, 1] = 1
        return res
    th = np.asarray(ths, dtype=np.int64)
    step = max(1, (1 << 21) // n)
    ar = np.arange(n)
    for s0 in range(0, nt, step):
        t = th[s0:s0 + step]
        R = len(t)
        P = np.sort((t[:, None] * X[None, :]) % M, axis=1)
        off = (np.arange(R, dtype=np.int64) * (4 * M))[:, None]
        flat = (np.concatenate((P, P + M), axis=1) + off).ravel()
        base = (np.arange(R) * (2 * n))[:, None]
        up = np.searchsorted(flat, (P + h + off).ravel(), 'left').reshape(R, n) - base - ar
        dn = np.searchsorted(flat, (P + h + 1 + off).ravel(), 'left').reshape(R, n) - base - ar - 1
        res[s0:s0 + R, 1] = up.max(axis=1)
        res[s0:s0 + R, 0] = dn.min(axis=1)
    return res


def gaps(points, M):
    p = sorted(points)
    return [(p[(i + 1) % len(p)] - p[i]) % M or M for i in range(len(p))]


def renewal(ds, n):
    """F (full words), A (valid words), B (boundary words) of each length < n, from the digits."""
    F = [1]
    for m in range(1, n):
        F.append(sum(F[m - 1 - j] for j in range(m) if ds[j] == 1))
    A = [sum(F[m - j] for j in range(m + 1)) for m in range(n)]
    B = [sum(F[m - j] for j in range(1, m + 1) if ds[j] == 0) for m in range(n)]
    return F, A, B


def census(mmax, ds):
    """Every valid word up to length mmax, level by level.
    Node: (r, x, state, C, parent index).  u = C / 3^m."""
    levels = [[(0, 0, 0, 0, -1)]]
    for i in range(mmax):
        nxt = []
        for idx, (r, x, st, C, _) in enumerate(levels[-1]):
            for b in (0, 1):
                if b == ds[st]:
                    st2 = st + 1
                elif b == 0:
                    st2 = 0
                else:
                    continue
                r2, x2 = extend(r, x, i, b)
                nxt.append((r2, x2, st2, 3 * C + (b << i), idx))
        levels.append(nxt)
    return levels


def main():
    kmax1 = int(sys.argv[1]) if len(sys.argv) > 1 else 17
    kmax2 = int(sys.argv[2]) if len(sys.argv) > 2 else 13
    mmax = int(sys.argv[3]) if len(sys.argv) > 3 else 22
    assert mmax <= 22
    t0 = time.time()
    cs, ds = tower(480)
    print('digits of 1 in base 3/2: %s' % ''.join(map(str, ds[:40])))
    F, A, B = renewal(ds, mmax + 2)
    summary = {}

    # ---- C0: three descriptions of validity agree; the tower state equals the slack
    def oracle(bits):
        u = Fr(0)
        for b in reversed(bits):
            u = (b + 2 * u) / 3
            if u >= Fr(1, 2):
                return False
        return True
    ok = True
    for n in range(1, 15):
        cnt = 0
        for v in range(1 << n):
            bits = [(v >> i) & 1 for i in range(n)]
            c, st, good = Fr(1), 0, True
            for b in bits:
                c = slack_step(c, b)
                if c is None:
                    good = False
                    break
                st = st + 1 if b == ds[st] else 0
                if c != cs[st]:
                    ok = False
            if good != oracle(bits):
                ok = False
            cnt += good
        if cnt != A[n]:
            ok = False
    print('C0 slack rule = direct tail sums = tower automaton, and counts = renewal A(n), n <= 14: %s' % ok)
    print('   A(1..10) = %s (census: 2, 3, 5, 8, 12, 18, 27, 40, 60, 90)' % A[1:11])
    assert ok and A[1:11] == [2, 3, 5, 8, 12, 18, 27, 40, 60, 90]

    # ---- C1: N_k against a direct walk
    ok = True
    for r, x, c in words(Fr(1), 12):
        n, bits = r, []
        for _ in range(12):
            bits.append(n & 1)
            n = T(n)
        if n != x or not oracle(bits) or not 0 <= r < 4096:
            ok = False
    print('C1 N_12 and T^12 against a direct walk on every valid word of length 12: %s' % ok)
    assert ok

    # ---- C2: the vectorised arc routine against the simple one
    ok = True
    for k in range(2, 13):
        for i in (0, 1, 2, 3, 5, 8):
            Sb = [(r, x) for r, x, c in words(cs[i], k) if c <= TWO3]
            X = [r + (((x & 1) ^ 1) << k) for r, x in Sb]
            ths = thetas(k + 1)
            if not np.array_equal(arc_minmax(X, k + 1, k, ths), arc_minmax_simple(X, k + 1, k, ths)):
                ok = False
        X = [r for r, x, c in words(Fr(1), k + 2)]
        ths = thetas(k + 2)
        if k <= 10 and not np.array_equal(arc_minmax(X, k + 2, k, ths), arc_minmax_simple(X, k + 2, k, ths)):
            ok = False
    print('C2 vectorised arc routine = simple routine, k <= 12, six states, one and two forced bits: %s' % ok)
    assert ok

    # ---- (a) the residue certificate
    print('\n== (a) residues of r modulo 3 on the boundary continuations of a full word')
    a_tab = {}
    for k in range(2, 13):
        S = [r for r, x, c in words(Fr(1), k) if c <= TWO3]
        M = 1 << k
        worst_gaps, worst_good, bad_th = None, None, []
        for l, th in enumerate(thetas(k)):
            p = sorted(th * s % M for s in S)
            g = gaps(p, M) if len(p) > 1 else [M]
            prime = sum(1 for y in g if y % 3)
            best = 0
            for cut in p:
                cls = [0, 0, 0]
                for y in p:
                    cls[((y - cut) % M) % 3] += 1
                best = max(best, max(cls))
            good = len(p) - best
            if worst_good is None or good < worst_good:
                worst_good = good
            if worst_gaps is None or prime < worst_gaps:
                worst_gaps = prime
            if prime < 2:
                bad_th.append(th)
            if k == 4:
                print('   k = 4, theta = %2d: points %s, gaps %s' % (th, p, g))
        a_tab[k] = (len(S), worst_gaps, worst_good)
        print('   k = %2d: |S_k| = %4d, multipliers %5d, least number of gaps prime to 3: %d, '
              'guaranteed starts off any one residue: %d%s'
              % (k, len(S), len(thetas(k)), worst_gaps, worst_good,
                 '' if not bad_th else '   FAILS at theta in %s' % bad_th[:6]))
    summary['a'] = {str(k): v for k, v in a_tab.items()}
    p1 = a_tab[4][1] >= 2
    print('P1 (a) holds at k = 4 for every multiplier and rotation: %s' % p1)

    # ---- (b) the first check, every prefix state
    print('\n== (b) first check: deaths among the boundary continuations, per prefix state')
    b_tab, lo_store = {}, {}
    k_first = None
    for k in range(2, kmax1 + 1):
        K = k + 1
        ths = thetas(K)
        num = np.zeros(len(ths))
        tot = 0.0
        row0 = None
        los = []
        for i in range(NSTATE):
            W = words(cs[i], k)
            Sb = [(r, x) for r, x, c in W if c <= TWO3]
            X = [r + (((x & 1) ^ 1) << k) for r, x in Sb]
            mm = arc_minmax(X, K, k, ths)
            los.append((len(Sb), mm))
            num += (2.0 / 3) ** i * mm[:, 0]
            tot += (2.0 / 3) ** i * len(Sb)
            if i == 0:
                row0 = (len(Sb), int(mm[:, 0].min()), int(mm[:, 1].max()))
        lo_store[k] = los
        full = 1.5 ** (k + 1)
        L = float(num.min()) / full
        Lu = sum((2.0 / 3) ** i * int(mm[:, 0].min()) for i, (sz, mm) in enumerate(los)) / full
        l0 = int(np.argmin(los[0][1][:, 0]))
        b_tab[k] = (row0, L, tot / full, Lu, l0, ths[l0])
        if k_first is None and row0[1] >= 1:
            k_first = k
        print('   k = %2d: full state |S| = %4d, deaths between %4d and %4d for every prefix '
              '(least at prefix length %d mod %d, multiplier %d); all states: D/B eventually in '
              '[%.4f, %.4f]; with the worst multiplier taken state by state: [%.4f, %.4f]   (weights carried: %.6f of 1)'
              % (k, row0[0], row0[1], row0[2], l0, len(ths), ths[l0], L, 1 - L, Lu, 1 - Lu, tot / full))
        sys.stdout.flush()
    summary['b'] = {str(k): {'S0': v[0][0], 'lo0': v[0][1], 'hi0': v[0][2], 'L': v[1], 'Lu': v[3]}
                    for k, v in b_tab.items()}
    print('P2 least k whose full-state family is never all-equal: %s (predicted <= 8)' % k_first)
    if 12 in b_tab:
        print('P3 certified interval at k = 12: [%.4f, %.4f] (predicted inside [0.25, 0.75])'
              % (b_tab[12][1], 1 - b_tab[12][1]))
    if 17 in b_tab:
        print('Q1 certified lower end at k = 17: %.4f (predicted between 0.22 and 0.32)' % b_tab[17][1])
    if k_first:
        K = k_first + 1
        W = [(r, x) for r, x, c in words(Fr(1), k_first) if c <= TWO3]
        X = [r + (((x & 1) ^ 1) << k_first) for r, x in W]
        print('   the certificate at k = %d: points theta N(s1) in Z/%d and their largest cyclic gap (<= %d)'
              % (k_first, 1 << K, 1 << k_first))
        worst = 0
        for l, th in enumerate(thetas(K)):
            p = sorted(th * y % (1 << K) for y in X)
            worst = max(worst, max(gaps(p, 1 << K)))
            print('      l = %2d, theta = %3d: %s  largest gap %d' % (l, th, p, max(gaps(p, 1 << K))))
        print('      largest gap over all multipliers: %d' % worst)

    # ---- (c) two and three forced bits
    print('\n== (c) j forced bits: the share of valid words of every long length that pass j checks')
    c_tab = {}
    for j in (1, 2, 3):
        for k in range(4, kmax2 + 1):
            K = k + j
            ths = thetas(K)
            killed = np.zeros(len(ths))
            kept = np.zeros(len(ths))
            for i in range(NSTATE):
                V = len(words(cs[i], k))
                X = [r for r, x, c in words(cs[i], K)]
                mm = arc_minmax(X, K, k, ths)
                killed += (2.0 / 3) ** i * (V - mm[:, 1])
                kept += (2.0 / 3) ** i * mm[:, 0]
            norm = 3 * 1.5 ** k
            up = 1 - float(killed.min()) / norm
            dn = float(kept.min()) / norm
            c_tab[(j, k)] = (dn, up)
            print('   j = %d, k = %2d: pass share eventually in [%.4f, %.4f]   (coin value %.4f)'
                  % (j, k, dn, up, 0.75 ** j))
            sys.stdout.flush()
    summary['c'] = {'%d,%d' % jk: v for jk, v in c_tab.items()}

    # ---- P4: direct enumeration
    print('\n== P4 direct enumeration of the valid words, m <= %d' % mmax)
    levels = census(mmax, ds)
    Bm, Dm, Rm = [], [], []
    for m, lev in enumerate(levels):
        b = d = rr = 0
        bad = (1 - (1 << m)) % 3
        for r, x, st, C, par in lev:
            if ds[st] == 0 and m > 0:
                b += 1
                d += x & 1
                if 4 * C < 3 ** m and r % 3 != bad:
                    rr += 1
        Bm.append(b)
        Dm.append(d)
        Rm.append(rr)
        assert len(lev) == A[m] and b == B[m]
    cloud = {10: (46, 26), 14: (226, 112), 18: (1144, 561), 22: (5804, 2924)}
    okc = all((Bm[w], Dm[w]) == v for w, v in cloud.items() if w <= mmax)
    print('   B and D at w = 10, 14, 18, 22: %s; equal to Cloud\'s table: %s'
          % ([(Bm[w], Dm[w]) for w in cloud if w <= mmax], okc))
    okr = all(Rm[m] >= F[m - 6] for m in range(6, mmax + 1))
    okp = all(Dm[m + 1] >= Rm[m] and Bm[m + 1] - Dm[m + 1] >= Rm[m] for m in range(1, mmax))
    print('   |R_m| >= F(m - 6) for 6 <= m <= %d: %s;  GC2936 pairing D_(m+1) >= |R_m| and '
          'B_(m+1) - D_(m+1) >= |R_m| for m < %d: %s' % (mmax, okr, mmax, okp))
    print('   m: |R_m|, F(m-6), D_m, B_m, D_m/B_m')
    for m in range(6, mmax + 1):
        print('   %2d: %5d %5d %5d %5d  %.4f' % (m, Rm[m], F[m - 6], Dm[m], Bm[m], Dm[m] / Bm[m]))
    # per-prefix check of (b): deaths among the boundary continuations of every prefix
    kcheck = min(10, kmax1)
    dk = [[(1 if (ds[st] == 0 and m > 0) else 0, (x & 1) if (ds[st] == 0 and m > 0) else 0)
           for r, x, st, C, par in lev] for m, lev in enumerate(levels)]
    okb, seen_lo, seen_hi, nfam = True, {}, {}, 0
    for k in range(1, kcheck + 1):
        new = []
        for m in range(mmax - k + 1):
            acc = [[0, 0] for _ in levels[m]]
            for (r, x, st, C, par), (nb, nd) in zip(levels[m + 1], dk[m + 1]):
                acc[par][0] += nb
                acc[par][1] += nd
            new.append(acc)
        dk = new
        if k < 2:
            continue
        ths = thetas(k + 1)
        for m in range(mmax - k + 1):
            q = m % len(ths)
            for (r, x, st, C, par), (nb, nd) in zip(levels[m], dk[m]):
                if st >= NSTATE:
                    continue
                size, mm = lo_store[k][st]
                nfam += 1
                if nb != size or not mm[q, 0] <= nd <= mm[q, 1]:
                    okb = False
                if st == 0:
                    seen_lo[k] = min(seen_lo.get(k, nd), nd)
                    seen_hi[k] = max(seen_hi.get(k, nd), nd)
    print('   every prefix family (k = 2..%d, every prefix of every length up to %d - k: %d families) '
          'inside its certified range: %s' % (kcheck, mmax, nfam, okb))
    print('   full-state families, observed extremes of deaths against the certified ones:')
    for k in range(2, kcheck + 1):
        print('      k = %2d: observed %3d..%3d, certified %3d..%3d of %d'
              % (k, seen_lo[k], seen_hi[k], b_tab[k][0][1], b_tab[k][0][2], b_tab[k][0][0]))
    # the exact per-length inequality
    oke = True
    for k in range(2, kcheck + 1):
        ths = thetas(k + 1)
        for m in range(k, mmax + 1):
            q = (m - k) % len(ths)
            lo = sum(F[m - k - i] * int(lo_store[k][i][1][q, 0]) for i in range(min(NSTATE, m - k + 1)))
            hi = sum(F[m - k - i] * int(lo_store[k][i][1][q, 1]) for i in range(min(NSTATE, m - k + 1)))
            if not lo <= Dm[m] <= hi:
                oke = False
    print('   exact inequality  sum_i F(m-k-i) lo_i <= D_m <= sum_i F(m-k-i) hi_i  for k = 2..%d, m <= %d: %s'
          % (kcheck, mmax, oke))
    # (a) directly: after every full prefix the boundary continuations of length k avoid any one residue
    oka = True
    for k in range(4, 9):
        need = a_tab[k][2]
        res = [[[0, 0, 0] if True else None for _ in lev] for lev in levels[:mmax - k + 1]]
        cur = [[(1 if ds[st] == 0 else 0, r % 3) for r, x, st, C, par in lev] for lev in levels]
        acc = [[[b * (q == 0), b * (q == 1), b * (q == 2)] for b, q in lev] for lev in cur]
        for step in range(k):
            new = []
            for m in range(len(acc) - 1):
                a2 = [[0, 0, 0] for _ in levels[m]]
                for (r, x, st, C, par), v in zip(levels[m + 1], acc[m + 1]):
                    a2[par][0] += v[0]
                    a2[par][1] += v[1]
                    a2[par][2] += v[2]
                new.append(a2)
            acc = new
        for m in range(len(acc)):
            for (r, x, st, C, par), v in zip(levels[m], acc[m]):
                if st == 0 and sum(v) - max(v) < need:
                    oka = False
    print('   (a) directly: after every full prefix, k = 4..8, at least the certified number of boundary '
          'continuations avoid each residue: %s' % oka)
    p4 = okc and okr and okp and okb and oke and oka
    print('P4: %s' % p4)
    summary['P'] = {'P1': bool(p1), 'P2_k': k_first, 'P4': bool(p4)}

    # ---- (E) explicit constants: v_n = F(n) (2/3)^n, exact
    print('\n== (E) explicit constants for every length')
    NN, LL = 400, 60
    FF, AA, BB = renewal(ds, NN + 1)
    v = [Fr(FF[n] * 2 ** n, 3 ** n) for n in range(NN + 1)]
    tail = [Fr(2, 3) ** a * cs[a] for a in range(NN + 1)]          # Fbar(a) = (2/3)^a c_a
    ok_id = all(sum(tail[a] * v[n - a] for a in range(n + 1)) == 1 for n in range(0, NN + 1, 7))
    S_L = sum(tail[1:LL + 1])
    tau = 3 * Fr(2, 3) ** (LL + 1)
    z = 1 / (1 + S_L)
    eps = max(max(abs(v[n] - z) for n in range(NN - LL, NN + 1)), tau / (1 - S_L))
    lo_v, hi_v = z - eps, z + eps
    inside = all(lo_v <= v[n] <= hi_v for n in range(NN - LL, NN + 1))
    cons = (lo_v <= 1 - hi_v * S_L - tau) and (hi_v >= 1 - lo_v * S_L)
    print('   identity sum_a (2/3)^a c_a v_(n-a) = 1 at n = 0, 7, ..., %d: %s' % (NN, ok_id))
    print('   S_L = %.12f (L = %d), z = 1/(1+S_L) = %.12f, eps = %.3e; window values inside: %s; '
          'interval self-consistent: %s' % (float(S_L), LL, float(z), float(eps), inside, cons))
    print('   so v_n lies in [%.9f, %.9f] for every n >= %d;  min v_n = %s at n = %d, max over n >= 2: %.6f'
          % (float(lo_v), float(hi_v), NN - LL, min(v), v.index(min(v)), float(max(v[2:]))))
    exact27 = [m for m in range(7, NN + 1) if 27 * FF[m - 7] < BB[m]]
    tail27 = 27 * Fr(2, 3) ** 7 * lo_v >= Fr(3, 2) * hi_v + 3 * Fr(2, 3) ** (LL + 1)
    small = [(m, Dm[m], Bm[m]) for m in range(3, 10)]
    oks = all(Bm[m] <= 27 * Dm[m] <= 26 * Bm[m] for m in range(3, 10))
    print('   27 F(m-7) >= B_m fails only at m in %s for 7 <= m <= %d; tail inequality for m > %d: %s'
          % (exact27, NN, NN, tail27))
    print('   small lengths directly (m, D, B): %s; inside [1/27, 26/27]: %s' % (small, oks))
    q3 = ok_id and inside and cons and tail27 and oks and exact27 == [9]
    print('Q3 for every m >= 3: 1/27 <= D_m/B_m <= 26/27: %s' % q3)
    summary['E'] = {'lo_v': float(lo_v), 'hi_v': float(hi_v), 'Q3': bool(q3)}
    summary['census'] = {'B': Bm, 'D': Dm, 'R': Rm, 'F': F[:mmax + 1]}
    print('\nJSON %s' % json.dumps(summary, sort_keys=True))
    print('elapsed %.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
