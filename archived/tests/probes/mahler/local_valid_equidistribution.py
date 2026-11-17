#!/usr/bin/env python3
"""L1670 (Local, 12 November 2026): toggles, the renewal inequality and the equidistribution of the valid starts.

T(n) = ceil(3n/2).  A word q of length w has the start r(q) in [0, 2^w), the residue whose first w parities are q:
r(q) = -sum q_i 2^i 3^(-(i+1)) mod 2^w.  Valid words are the paths of the automaton of the 3/2-shift: from state s
the letter d_s leads to s + 1, and where d_s = 1 the letter 0 leads to state 0 (full).  d = digits of 1 in base 3/2.

Tests T1 to T6, their predictions and counterfactuals are in L1670, written and pushed before this file existed.
Exact integers everywhere except inside the exponential sums.  Census to w = 40; direct walk to 2^28 starts.
"""
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

LAM = math.cos(math.pi / 5)
KAP = 1.0 - LAM
K_HAND = 8 * (1 + 2 / LAM) / (1 - 1 / (2 * LAM))
MU_HAND = 1 - 2 * KAP / K_HAND
C0 = 6.2
T0 = time.time()
FAILS = []


def say(*a):
    print(*a)
    sys.stdout.flush()


def verdict(name, ok, text):
    say('%s %s: %s' % (name, 'HELD' if ok else 'REFUTED', text))
    if not ok:
        FAILS.append(name)


def digits(n):
    """d_0 .. d_(n-1).  c_i = a/2^i, d_i = [c_i > 2/3], c_(i+1) = 3 c_i/2 - d_i."""
    a, out = 1, []
    for i in range(n):
        di = 1 if 3 * a > (2 << i) else 0
        out.append(di)
        a = 3 * a - (di << (i + 1))
    return out


def renewal(ds, n):
    F = [1]
    for k in range(1, n + 1):
        F.append(sum(F[k - 1 - j] for j in range(k) if ds[j]))
    A = [sum(F[m - i] for i in range(m + 1)) for m in range(n + 1)]
    B = [sum(F[m - i] for i in range(1, m + 1) if ds[i] == 0) for m in range(n + 1)]
    return F, A, B


def census(wmax, ds, wbits):
    """Yield (w, R, st, W, FM) for w = 0 .. wmax.  R = -sum q_i 2^i 3^(-(i+1)) mod 2^64, st = state,
    W = the word's bits, FM = bit i set when the prefix of length i is full.  W and FM are kept for w <= wbits."""
    D = np.array(ds, dtype=np.uint8)
    R = np.zeros(1, dtype=np.uint64)
    st = np.zeros(1, dtype=np.int32)
    W = np.zeros(1, dtype=np.uint64)
    FM = np.zeros(1, dtype=np.uint64)
    yield 0, R, st, W, FM
    for w in range(wmax):
        dS = D[st]
        one = dS == 1
        inv = np.uint64(pow(3, -(w + 1), 1 << 64))
        sh = np.uint64(w)
        bit = dS.astype(np.uint64) << sh
        RA = R - bit * inv
        RB = R[one]
        if w < wbits:
            full = (st == 0).astype(np.uint64) << sh
            FM2 = FM | full
            W = np.concatenate([W | bit, W[one]])
            FM = np.concatenate([FM2, FM2[one]])
        else:
            W = FM = None
        st = np.concatenate([st + 1, np.zeros(int(one.sum()), dtype=np.int32)])
        R = np.concatenate([RA, RB])
        yield w + 1, R, st, W, FM


def site_mask(W, FM, w):
    """Bit i set when i <= w - 3, the prefix of length i is full and q_(i+1) = q_(i+2) = 0."""
    if w < 3:
        return np.zeros(len(W), dtype=np.uint64)
    low = np.uint64((1 << (w - 2)) - 1)
    return FM & ~(W >> np.uint64(1)) & ~(W >> np.uint64(2)) & low


def separated_sets(npos):
    """All subsets of {0 .. npos-1} with any two elements at least 3 apart, as bit masks."""
    out = [0]
    def rec(start, mask):
        for i in range(start, npos):
            m2 = mask | (1 << i)
            out.append(m2)
            rec(i + 3, m2)
    rec(0, 0)
    return out


def angles_int(w, h):
    """a[i] with alpha_i = a[i]/2^(w-i): alpha_i = -h 3^(-(i+1)) / 2^(w-i) mod 1.  h: int64 array."""
    out = []
    for i in range(w):
        mod = 1 << (w - i)
        out.append((-(h % mod) * pow(3, -(i + 1), mod)) % mod)
    return out


def controls(ds, F, A, B, lev):
    say('--- controls')
    ok = all(len(lev[w][0]) == A[w] for w in lev)
    okb = True
    D = np.array(ds, dtype=np.uint8)
    for w in lev:
        st = lev[w][1]
        if int(((st >= 1) & (D[st] == 0)).sum()) != B[w]:
            okb = False
    say('C1 census sizes equal the renewal sums A(w), B_w for every w <= %d: %s, %s' % (max(lev), ok, okb))
    # C2: starts and words against a direct walk
    ok2 = True
    for w in range(1, 17):
        R, st, W, FM = lev[w]
        r = (R & np.uint64((1 << w) - 1)).astype(np.int64)
        got = dict(zip(r.tolist(), W.tolist()))
        want = {}
        for n in range(1 << w):
            x, s, word, good = n, 0, 0, True
            for i in range(w):
                b = x & 1
                if b == ds[s]:
                    s += 1
                elif b == 0:
                    s = 0
                else:
                    good = False
                    break
                word |= b << i
                x = (3 * x + b) >> 1
            if good:
                want[n] = word
        if got != want:
            ok2 = False
    say('C2 starts and words equal a direct walk of every n < 2^w, w <= 16: %s' % ok2)
    # C3: CL782's table
    cl = {10: (46, 26), 14: (226, 112), 18: (1144, 561), 22: (5804, 2924)}
    ok3 = True
    for m, (b0, d0) in cl.items():
        R, st = lev[m][0], lev[m][1]
        bd = (st >= 1) & (D[st] == 0)
        dd = int((((R[bd] >> np.uint64(m)) & np.uint64(1)) == 1).sum())
        if (int(bd.sum()), dd) != (b0, d0):
            ok3 = False
        say('   m = %d: B = %d, D = %d (CL782: %d, %d)' % (m, int(bd.sum()), dd, b0, d0))
    say('C3 (B, D) equal CL782 at m = 10, 14, 18, 22: %s' % ok3)
    v = [Fr(F[n] * 2 ** n, 3 ** n) for n in range(401)]
    vmin = min(v)
    prod = 1.0
    for k in range(1, 400):
        prod *= 1 - (2 / 3) ** k
    say('C4 least F(n)(2/3)^n for n <= 400: %s = %.6f at n = %d; hand floor prod(1 - (2/3)^k) = %.6f; v_400 = %.9f'
        % (vmin, float(vmin), v.index(vmin), prod, float(v[400])))
    okc = ok and okb and ok2 and ok3 and vmin == Fr(4, 9) and prod > 0.06
    verdict('CONTROLS', okc, 'C1 to C4')
    return okc


def test_T1(lev):
    say('--- T1: Lemma T (toggles)')
    nflip, bad = 0, 0
    for w in range(3, 17):
        R, st, W, FM = lev[w]
        S = site_mask(W, FM, w)
        order = np.argsort(W)
        Ws = W[order]
        for c in range(3):
            cm = np.uint64(sum(1 << i for i in range(c, w, 3)))
            Sc = S & cm
            for i in range(c, w - 2, 3):
                sel = ((Sc >> np.uint64(i)) & np.uint64(1)) == 1
                if not sel.any():
                    continue
                W2 = W[sel] ^ np.uint64(1 << i)
                idx = np.searchsorted(Ws, W2)
                idx2 = np.minimum(idx, len(Ws) - 1)
                found = Ws[idx2] == W2
                j = order[idx2]
                good = found & (st[j] == st[sel]) & (Sc[j] == Sc[sel])
                nflip += int(sel.sum())
                bad += int((~good).sum())
    say('flips at sites, w = 3 .. 16, three classes: %d checked, %d fail (valid, same state, same sites)' % (nflip, bad))
    worst_a = worst_f = 0.0
    viol = 0
    slack = float('inf')
    for w in range(8, 15):
        R, st, W, FM = lev[w]
        A = len(W)
        H = 1 << w
        h = np.arange(H, dtype=np.int64)
        r = (R & np.uint64(H - 1)).astype(np.int64)
        ind = np.zeros(H)
        ind[r] = 1.0
        G0 = np.conj(np.fft.fft(ind))                       # sum_q e(h r(q)/2^w)
        ai = angles_int(w, h)
        alpha = np.array([ai[i] / float(1 << (w - i)) for i in range(w)])     # w x H
        Qb = np.array([((W >> np.uint64(i)) & np.uint64(1)).astype(np.float64) for i in range(w)]).T   # A x w
        G1 = np.exp(2j * np.pi * (Qb @ alpha)).sum(axis=0)
        worst_a = max(worst_a, float(np.abs(G1 - G0).max()))
        S = site_mask(W, FM, w)
        cosabs = np.abs(np.cos(np.pi * alpha))
        one_e = 1 + np.exp(2j * np.pi * alpha)
        for c in range(3):
            cm = np.uint64(sum(1 << i for i in range(c, w, 3)))
            Sc = S & cm
            Sb = np.array([((Sc >> np.uint64(i)) & np.uint64(1)) == 1 for i in range(w)]).T     # A x w
            rep = (W & Sc) == 0
            prod = np.exp(2j * np.pi * (Qb[rep] @ alpha))
            for i in range(c, w - 2, 3):
                col = Sb[rep, i]
                if col.any():
                    prod[col] *= one_e[i][None, :]
            G2 = prod.sum(axis=0)
            worst_f = max(worst_f, float(np.abs(G2 - G0).max()))
            bound = np.ones((A, H))
            for i in range(c, w - 2, 3):
                col = Sb[:, i]
                if col.any():
                    bound[col] *= cosabs[i][None, :]
            bsum = bound.sum(axis=0)
            viol += int((np.abs(G0) > bsum + 1e-9).sum())
            nz = np.abs(G0[1:]) > 1e-9
            slack = min(slack, float((bsum[1:][nz] / np.abs(G0[1:][nz])).min()))
    say('w = 8 .. 14, every h: |G from starts - G from angles| <= %.2e; |G - sum of fibre products| <= %.2e'
        % (worst_a, worst_f))
    say('   |G(h)| <= sum_q prod_sites |cos|: %d violations; least ratio bound/|G| over h != 0: %.4f' % (viol, slack))
    verdict('T1', bad == 0 and worst_a < 1e-9 and worst_f < 1e-9 and viol == 0, 'Lemma T on every word and frequency tested')


def test_T2(lev, F, ds):
    say('--- T2: Lemma R (renewal inequality), lambda = cos(pi/5) = %.6f, K_hand = %.4f, mu_hand = %.6f'
        % (LAM, K_HAND, MU_HAND))
    # sharp series constant
    # E_s(r) = sum over k < r of d_(s+k) F(r-1-k): the words of length r leading from state s to state 0
    kstar, rstar = 0.0, None
    kr = {}
    Ff = np.array([float(x) for x in F[:1101]])
    dsf = np.array(ds, dtype=np.float64)
    wgt = np.array([1.0 / (Ff[s] * LAM ** math.ceil(s / 3)) for s in range(700)])
    for r in range(3, 401):
        E = np.correlate(dsf[:699 + r], Ff[r - 1::-1], mode='valid')      # E[s], s = 0 .. 699
        tot = float((E * wgt).sum() / Ff[r - 3])
        kr[r] = tot
        if tot > kstar:
            kstar, rstar = tot, r
    # exact spot check of E_s(r) against a brute-force count of words, small sizes
    e_ok = True
    for s0 in range(0, 9):
        for r0 in range(1, 11):
            n = 0
            for word in range(1 << r0):
                st = s0
                for i in range(r0):
                    b = (word >> i) & 1
                    if b == ds[st]:
                        st += 1
                    elif b == 0:
                        st = 0
                    else:
                        st = -1
                        break
                n += (st == 0)
            if n != int(round(float(np.correlate(dsf[:s0 + r0], Ff[r0 - 1::-1], mode='valid')[s0]))):
                e_ok = False
    say('E_s(r) by the formula equals a brute-force count for s <= 8, r <= 10: %s' % e_ok)
    if not e_ok:
        FAILS.append('E_s')
    mustar = 1 - 2 * KAP / kstar
    say('sharp series K(r), r = 3 .. 400 (s < 700): sup = %.6f at r = %d; K(3) = %.4f, K(4) = %.4f, K(5) = %.4f, '
        'K(6) = %.4f, K(400) = %.6f; mu* = %.6f' % (kstar, rstar, kr[3], kr[4], kr[5], kr[6], kr[400], mustar))
    TM = 26
    hist = {}
    lam_pow = LAM ** np.arange(0, 12)
    for t in range(0, TM + 1):
        R, st, W, FM = lev[t]
        fullw = st == 0
        S = site_mask(W[fullw], FM[fullw], t)
        assert len(S) == F[t]
        sets = separated_sets(max(t - 2, 0))
        U = np.array(sets, dtype=np.uint64)
        for a in range(0, len(U), 512):
            cnt = np.bitwise_count(S[None, :] & U[a:a + 512, None])
            for k, row in enumerate(cnt):
                hist[(t, sets[a + k])] = np.bincount(row, minlength=12)
    say('histograms of site counts: %d pairs (t, U), t <= %d; at t = %d: %d sets, %d full words'
        % (len(hist), TM, TM, len(separated_sets(TM - 2)), F[TM]))
    bad_a = bad_b = bad_c = bad_s = 0
    kemp = 0.0
    worst = {}
    for (t, U), hv in hist.items():
        V = float((hv * lam_pow).sum())
        size = bin(U).count('1')
        if V > MU_HAND ** size * F[t] * (1 + 1e-12):
            bad_c += 1
        if V > mustar ** size * F[t] * (1 + 1e-12):
            bad_s += 1
        if size:
            f = (V / F[t]) ** (1.0 / size)
            if f > worst.get(t, (0, 0))[0]:
                worst[t] = (f, U)
            i = U.bit_length() - 1
            U2 = U ^ (1 << i)
            h2 = hist[(t, U2)]
            hi = hist[(i, U2)]
            # identity (a): P_(t,U) = P_(t,U'') - 2 (1 - lam) F(t-i-3) P_(i,U'') as integer polynomials
            rhs = [int(x) for x in h2] + [0]
            for k, x in enumerate(hi):
                rhs[k] -= 2 * F[t - i - 3] * int(x)
                rhs[k + 1] += 2 * F[t - i - 3] * int(x)
            if rhs[:12] != [int(x) for x in hv] or rhs[12] != 0:
                bad_a += 1
            V2 = float((h2 * lam_pow).sum())
            Vi = float((hi * lam_pow).sum())
            ratio = V2 / (Vi * F[t - i - 3])
            kemp = max(kemp, ratio)
            if ratio > K_HAND:
                bad_b += 1
    say('identity (a) as integer polynomials in lambda: %d failures' % bad_a)
    say('V(t;U\'\') <= K V(i;U\'\') F(t-i-3): largest ratio seen %.4f (K_hand %.2f, sharp series %.4f); %d above K_hand'
        % (kemp, K_HAND, kstar, bad_b))
    say('V(t;U) <= mu^|U| F(t): %d failures with mu_hand, %d with mu* = 1 - 2 kappa/K*' % (bad_c, bad_s))
    for t in (12, 16, 20, 24, 26):
        f, U = worst[t]
        say('   t = %d: largest per-site factor %.5f at U = %s' % (t, f, [i for i in range(t) if (U >> i) & 1]))
    f26 = worst[TM][0]
    verdict('T2', bad_a == 0 and bad_b == 0 and bad_c == 0 and kemp <= kstar * (1 + 1e-9),
            'Lemma R: identity, the K inequality and the bound, every 3-separated U, t <= %d' % TM)
    verdict('T2-sharpness', 0.93 <= f26 <= 0.96 and 12 <= kstar <= 14,
            'largest per-site factor at t = 26 is %.4f (predicted 0.93 to 0.96); K* = %.3f (predicted 12 to 14)' % (f26, kstar))
    return mustar


def test_T3(lev):
    say('--- T3: one frequency (Lemmas N and F, and the bound of step 3)')
    okN = okF = okG1 = okG2 = True
    for w in (10, 12, 14, 16):
        R, st, W, FM = lev[w]
        A = len(W)
        H = 1 << w
        h = np.arange(H, dtype=np.int64)
        r = (R & np.uint64(H - 1)).astype(np.int64)
        ind = np.zeros(H)
        ind[r] = 1.0
        gam = np.abs(np.fft.fft(ind)) / A
        ai = angles_int(w, h)
        # beta_u = alpha_(w-1-u), denominator 2^(u+1)
        dist = []
        for u in range(w):
            a = ai[w - 1 - u]
            mod = 1 << (u + 1)
            dist.append(np.minimum(a, mod - a))
        ns_flag = [5 * dist[u] >= (1 << (u + 1)) for u in range(w)]
        for u in range(w - 1):
            mod = 1 << (u + 1)
            if not np.array_equal(ai[w - 2 - u] % mod, (3 * ai[w - 1 - u]) % mod):
                okN = False
            both = (~ns_flag[u]) & (~ns_flag[u + 1]) & (dist[u] > 0)
            if not np.array_equal(dist[u + 1][both], 3 * dist[u][both]):
                okN = False
        NS = np.zeros(H, dtype=np.int64)
        for u in range(w):
            NS += ns_flag[u]
        val = np.zeros(H, dtype=np.int64)
        hh = h.copy()
        hh[0] = 1
        for a in range(w):
            even = (hh & 1) == 0
            val[even] += 1
            hh[even] >>= 1
            if not even.any():
                break
        nz = h != 0
        low = np.log((w - val[nz]) / 0.85) / np.log(2.71)
        if not (NS[nz] > low).all():
            okN = False
        worstF = 0.0
        for a in range(0, w):
            cls = nz & (val == a)
            if not cls.any():
                continue
            for L in range(1, w + 1):
                n = int((NS[cls] <= L).sum())
                bnd = (2.0 * w) ** (L - 1)
                if n > bnd:
                    okF = False
                if n:
                    worstF = max(worstF, n / bnd)
        # greedy 3-separated U(h) among the non-small positions i <= w - 3
        Umask = np.zeros(H, dtype=np.uint64)
        last = np.full(H, -10, dtype=np.int64)
        for i in range(0, w - 2):
            take = ns_flag[w - 1 - i] & (i - last >= 3)
            Umask[take] |= np.uint64(1 << i)
            last[take] = i
        usize = np.bitwise_count(Umask).astype(np.int64)
        S = site_mask(W, FM, w)
        b1 = np.zeros(H)
        lam_pow = LAM ** np.arange(0, 12)
        for a in range(0, H, 2048):
            cnt = np.bitwise_count(S[None, :] & Umask[a:a + 2048, None])
            b1[a:a + 2048] = lam_pow[cnt].sum(axis=1) / A
        b2 = C0 * MU_HAND ** usize
        if (gam[nz] > b1[nz] + 1e-12).any():
            okG1 = False
        if (b1[nz] > b2[nz] * (1 + 1e-12)).any():
            okG2 = False
        j = int(np.argmax(np.where(nz, gam / b1, 0)))
        say('w = %d: least NS over odd h %d (Lemma N floor %.2f), over all h != 0 %d; Lemma F worst count/bound %.3f; '
            'largest gamma/bound1 = %.4f at h = %d (gamma %.4f, |U| = %d); least |U| = %d, largest bound1 = %.4f'
            % (w, int(NS[nz & (val == 0)].min()), math.log(w / 0.85) / math.log(2.71), int(NS[nz].min()), worstF,
               float(gam[j] / b1[j]), j, float(gam[j]), int(usize[j]), int(usize[nz].min()), float(b1[nz].max())))
        tab = []
        for k in range(int(usize[nz].min()), int(usize[nz].max()) + 1):
            c = nz & (usize == k)
            if c.any():
                tab.append('%d: %.3f/%.3f' % (k, float(gam[c].max()), float(b1[c].max())))
        say('   |U| : largest gamma / largest bound1   ' + ', '.join(tab))
    verdict('T3', okN and okF and okG1 and okG2,
            'Lemma N %s, Lemma F %s, gamma <= bound1 %s, bound1 <= 6.2 mu^|U| %s' % (okN, okF, okG1, okG2))


def direct_walk(m, ds, limit=700):
    """cnt[k] = #{n < 2^m : first k parities valid}; life of the longest-lived n >= 1."""
    D = np.array(ds, dtype=np.int64)
    kint = min(int((60 - m) / 0.585), m + 36)      # 3x + 1 stays below 2^62 in the int64 phase
    cnt = [0] * (limit + 2)
    pool = []
    life = {}
    unrec = -1
    chunk = 1 << min(m, 22)
    for lo in range(0, 1 << m, chunk):
        n0 = np.arange(lo, lo + chunk, dtype=np.int64)
        x = n0.copy()
        st = np.zeros(chunk, dtype=np.int64)
        for k in range(kint):
            b = x & 1
            follow = b == D[st]
            alive = follow | (b == 0)
            if len(n0) <= 4096:
                for n in n0[~alive].tolist():
                    life[n] = k
            elif not alive.all():
                unrec = max(unrec, k)
            st = np.where(follow, st + 1, 0)[alive]
            x = ((3 * x + b) >> 1)[alive]
            n0 = n0[alive]
            cnt[k + 1] += len(n0)
        pool += list(zip(n0.tolist(), x.tolist(), st.tolist()))
    cnt[0] = 1 << m
    k = kint
    while k < limit and len(pool) > 1:
        nxt = []
        for n, x, s in pool:
            b = x & 1
            if b == ds[s]:
                s += 1
            elif b == 0:
                s = 0
            else:
                life[n] = k
                continue
            nxt.append((n, (3 * x + b) >> 1, s))
        pool = nxt
        k += 1
        cnt[k] = len(pool)
    if life and max(life.values()) <= unrec:
        FAILS.append('direct walk m = %d: the longest life was not recorded' % m)
    return cnt, kint, life, pool, k


def main():
    ds = digits(1200)
    F, A, B = renewal(ds, 1100)
    say('L1670 probe.  d = %s...' % ''.join(map(str, ds[:40])))
    say('F(0..12) = %s' % F[:13])
    WMAX, WBITS = 40, 26
    lev = {}
    disc = {}
    Scen = {}
    DB = {}
    gsmall = {}
    D = np.array(ds, dtype=np.uint8)
    for w, R, st, W, FM in census(WMAX, ds, WBITS):
        if w <= WBITS:
            lev[w] = (R, st, W, FM)
        if len(R) != A[w]:
            say('census size mismatch at w = %d' % w)
            FAILS.append('census')
        if w >= 1:
            bd = (st >= 1) & (D[st] == 0)
            dd = int((((R[bd] >> np.uint64(w)) & np.uint64(1)) == 1).sum())
            DB[w] = (int(bd.sum()), dd)
        if w >= 4:
            r = np.sort(R & np.uint64((1 << w) - 1))
            n = len(r)
            x = r.astype(np.float64) / float(1 << w)
            k = np.arange(1, n + 1, dtype=np.float64)
            up = float((k / n - x - 1.0 / (1 << w)).max())
            dn = float((x - (k - 1) / n).max())
            disc[w] = (n, max(up, 0.0), max(dn, 0.0))
            for j in range(0, min(w, 14) + 1):
                Scen[(w - j, j)] = int(np.searchsorted(r, np.uint64(1 << (w - j))))
            if w in (12, 16, 20, 24, 28, 32, 36, 40):
                mask = np.uint64((1 << w) - 1)
                sc = 2 * math.pi / float(1 << w)
                g = []
                for h in range(1, 64):
                    ang = ((np.uint64(h) * r) & mask).astype(np.float64) * sc
                    g.append(math.hypot(float(np.cos(ang).sum()), float(np.sin(ang).sum())) / n)
                gsmall[w] = g
        if w % 8 == 0:
            say('   census at w = %d: %d words (%.0f s)' % (w, len(R), time.time() - T0))
    del R, st, W, FM

    controls(ds, F, A, B, lev)
    test_T1(lev)
    mustar = test_T2(lev, F, ds)
    test_T3(lev)

    say('--- T4: the largest deviation over intervals of the valid starts (Theorem V, measured)')
    say('   w : A(w), sup(count/A - length/2^w), sup(length/2^w - count/A), over all intervals, times sqrt(A)')
    arc = {}
    for w in sorted(disc):
        n, up, dn = disc[w]
        arc[w] = up + dn
        if w % 2 == 0:
            say('   %2d : %9d  %.5f  %.5f  %.5f  %.3f' % (w, n, up, dn, up + dn, (up + dn) * math.sqrt(n)))
    okth = all(arc[w] <= b for w, b in ((12, 0.12), (16, 0.06), (20, 0.03), (24, 0.015)))
    ratios = [(w, arc[w + 4] / arc[w]) for w in range(8, 37, 4)]
    okr = all(q <= 0.75 for w, q in ratios)
    say('   ratios over four steps: ' + ', '.join('%d: %.3f' % wq for wq in ratios))
    verdict('T4', okth and okr, 'thresholds at w = 12, 16, 20, 24: %s; every four-step ratio <= 0.75: %s' % (okth, okr))

    say('--- the first check on valid words: D_m/B_m (V1)')
    say('   ' + ', '.join('%d: %d/%d = %.5f' % (m, DB[m][1], DB[m][0], DB[m][1] / DB[m][0]) for m in range(8, 40, 4)))
    say('   ' + ', '.join('%d: %.5f' % (m, DB[m][1] / DB[m][0]) for m in range(33, 41)))

    say('--- T5: the share of valid words of length m that pass j more checks, against (3/4)^j (V2)')
    worst_all, worst32 = 0.0, 0.0
    for m in (12, 16, 20, 24, 28, 32):
        row = []
        for j in range(1, 9):
            s = Scen[(m, j)] / A[m]
            row.append('%.4f' % s)
            if m >= 20:
                worst_all = max(worst_all, abs(s - 0.75 ** j))
            if m == 32:
                worst32 = max(worst32, abs(s - 0.75 ** j))
        say('   m = %2d (A = %d): %s' % (m, A[m], ' '.join(row)))
    say('   (3/4)^j          : %s' % ' '.join('%.4f' % 0.75 ** j for j in range(1, 9)))
    okd = True
    lives = {}
    for m in (12, 16, 20, 24, 28):
        cnt, kint, life, pool, kend = direct_walk(m, ds)
        for j in range(0, 15):
            if (m, j) in Scen and Scen[(m, j)] != cnt[m + j]:
                okd = False
        if cnt[m] != A[m]:
            okd = False
        best = max(life.values()) if life else None
        who = sorted(n for n, v in life.items() if v == best)[:3] if life else []
        lives[m] = (best, who, len(pool), kend, kint)
        say('   direct walk m = %d: A = %d; survivors after m + j steps, j = 0, 4, 8, 12, 16, 20: %s (%.0f s)'
            % (m, cnt[m], [cnt[m + j] for j in (0, 4, 8, 12, 16, 20)], time.time() - T0))
    say('   census and direct walk agree on every S(m, m + j) both computed: %s' % okd)
    verdict('T5', worst_all <= 0.02 and worst32 <= 0.005 and okd,
            'largest |share - (3/4)^j| for m = 20, 24, 28, 32 and j <= 8: %.4f (limit 0.02); at m = 32: %.4f (limit 0.005)'
            % (worst_all, worst32))

    say('--- T6: the small frequencies, gamma_w(h) for 0 < h < 64')
    for w in sorted(gsmall):
        g = gsmall[w]
        jm = int(np.argmax(g))
        say('   w = %2d: largest %.5f at h = %d; 1/sqrt(A) = %.5f; gamma at h = 1, 2, 3, 9, 27: %.5f %.5f %.5f %.5f %.5f'
            % (w, g[jm], jm + 1, A[w] ** -0.5, g[0], g[1], g[2], g[8], g[26]))
    verdict('T6', max(gsmall[32]) <= 0.03 and max(gsmall[40]) <= 0.01,
            'largest gamma over 0 < h < 64: %.5f at w = 32 (limit 0.03), %.5f at w = 40 (limit 0.01)'
            % (max(gsmall[32]), max(gsmall[40])))

    say('--- no prediction: the longest-lived n >= 1 below 2^m (life = number of valid parities)')
    for m in sorted(lives):
        best, who, left, kend, kint = lives[m]
        say('   m = %d: longest life %s = m + %s, at n = %s; left at the end: %d (n = 0 only expected); int64 walk to step %d'
            % (m, best, None if best is None else best - m, who, left, kint))

    say('--- constants: K_hand = %.4f, mu_hand = %.6f, K* = see T2, mu* = %.6f' % (K_HAND, MU_HAND, mustar))
    say('failures: %s' % (FAILS if FAILS else 'none'))
    say('done in %.0f s' % (time.time() - T0))


if __name__ == '__main__':
    main()
