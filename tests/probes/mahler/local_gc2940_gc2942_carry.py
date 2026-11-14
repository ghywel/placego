#!/usr/bin/env python3
"""L1672 (Local, 14 November 2026): tests for the carrying reads of GPT's GC2940 (sections 3-5) and GC2942.

Independent of GPT's probes: own enumeration of valid words (the slack automaton of the digits of 1 in base 3/2),
own starts r(q) checked against a literal walk of T(n) = ceil(3n/2), own numerators B, own Fourier sums.
Predictions are in L1672, pushed before this file existed.  Exact integers and fractions wherever an identity
is claimed; floats only inside exponential sums, compared to 1e-9.
"""
import math
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import local_valid_equidistribution as LV   # noqa: E402  (Local's own L1670 probe: census, sites, digits)

T0 = time.time()
FAILS = []
BETA = 1.5
LAM = math.cos(math.pi / 5)
KAP = 1 - LAM


def say(*a):
    print(*a)
    sys.stdout.flush()


def check(name, ok, text):
    say('%s %s: %s' % (name, 'PASS' if ok else 'FAIL', text))
    if not ok:
        FAILS.append(name)


def e(x):
    return complex(math.cos(2 * math.pi * x), math.sin(2 * math.pi * x))


# ---------------------------------------------------------------- words
DS = LV.digits(2300)


def slacks(n):
    c, out = Fr(1), []
    for i in range(n):
        out.append(c)
        c = Fr(3, 2) * c - DS[i]
    return out


CS = slacks(60)


def words_from(s0, n):
    """All words of length n valid from state s0: list of (bits tuple, final state)."""
    out = [((), s0)]
    for _ in range(n):
        nxt = []
        for b, s in out:
            nxt.append((b + (DS[s],), s + 1))
            if DS[s] == 1:
                nxt.append((b + (0,), 0))
        out = nxt
    return out


def start(q):
    w = len(q)
    M = 1 << w
    return (-sum(qi * (1 << i) * pow(3, -(i + 1), M) for i, qi in enumerate(q))) % M if w else 0


def numer(q):
    w = len(q)
    return sum(qi * (1 << i) * 3 ** (w - 1 - i) for i, qi in enumerate(q))


def T(n):
    return (3 * n + 1) // 2 if n & 1 else 3 * n // 2


def parity_word(n, k):
    out = []
    for _ in range(k):
        out.append(n & 1)
        n = T(n)
    return tuple(out), n


def valid_from(word, s0=0):
    s = s0
    for b in word:
        if b == DS[s]:
            s += 1
        elif b == 0:
            s = 0
        else:
            return None
    return s


F_, A_, B_ = LV.renewal(DS, 2200)


def A_from(s, n, memo={}):
    """Number of words of length n valid from state s: 1 + sum_t d_(s+t) A(n-1-t)."""
    key = (s, n)
    if key not in memo:
        memo[key] = 1 + sum(DS[s + t] * A_[n - 1 - t] for t in range(n))
    return memo[key]


def fourier(points, N):
    ind = np.zeros(N)
    ind[np.array(points, dtype=np.int64)] = 1.0
    return np.conj(np.fft.fft(ind))           # G(h) = sum e(h r / N)


def fejer_energy(G, A, H, mult=1):
    N = len(G)
    if H <= 1:
        return 1.0
    h = np.arange(1, H, dtype=np.int64)
    g = np.abs(G[(mult * h) % N]) / A
    return 1.0 + float((2 * (1 - h / H) * g * g).sum())     # Q_b(H), including h = 0


def KH(x, H):
    s = math.sin(math.pi * x)
    if abs(s) < 1e-15:
        return float(H)
    return math.sin(math.pi * H * x) ** 2 / (H * s * s)


# ---------------------------------------------------------------- controls
def controls():
    say('--- controls')
    ok = True
    for w in range(1, 13):
        W = words_from(0, w)
        if len(W) != A_[w]:
            ok = False
        for q, s in W:
            r = start(q)
            pw, x = parity_word(r, w)
            if pw != q:
                ok = False
            if (1 << w) * x != 3 ** w * r + numer(q):
                ok = False
    check('C0', ok, 'word counts = A(w); starts give their words by literal walk; 2^w T^w(r) = 3^w r + B_w, w <= 12')
    ok = all(CS[i].denominator == 2 ** i for i in range(40)) and all(DS[i] == (1 if CS[i] > Fr(2, 3) else 0) for i in range(40))
    check('C1', ok, 'slack c_i has denominator 2^i and d_i = [c_i > 2/3], i < 40')


# ---------------------------------------------------------------- GC2940
def gc2940():
    say('--- GC2940 section 3')
    ok = all(F_[n + 2] <= F_[n + 1] + F_[n] for n in range(0, 2000)) and all(F_[n + 3] <= 5 * F_[n] for n in range(0, 2000))
    gaps = [j for j in range(400) if DS[j] == 1]
    ok2 = all(b - a >= 2 for a, b in zip(gaps, gaps[1:]))
    check('G1', ok and ok2, 'F(n+2) <= F(n+1) + F(n) and F(n+3) <= 5F(n) for n < 2000; ones of d at least 2 apart (first 400 digits)')
    K5 = 5 * (1 + 2 / LAM) / (1 - 1 / (2 * LAM))
    mu5 = 1 - 2 * KAP / K5
    d5 = math.log(1 / mu5) / (3 * math.log(2.71))
    C5 = mu5 ** (-2 / 3) / (2 * mu5 - 1)
    c5 = d5 * math.log2(4 / 3)
    CZ = (9 * math.pi ** 2 / 8) * (1 + 3 * C5 * 0.85 ** d5)
    say('   K_5 = %.5f, mu_5 = %.8f, delta_5 = %.8f, C_5 = %.6f, c_5 = %.6f, C_Z = %.4f' % (K5, mu5, d5, C5, c5, CZ))
    check('G2', abs(K5 - 45.45085) < 1e-4 and abs(mu5 - 0.99159606) < 1e-7 and abs(d5 - 0.00282176) < 1e-7
          and abs(C5 - 1.022834) < 1e-5 and CZ < 46, 'GC2940 constants as quoted')
    worst = {}
    okz = True
    for mu in (1 - 2 * KAP / (8 * (1 + 2 / LAM) / (1 - 1 / (2 * LAM))), mu5):
        bound = 1 / (2 * mu - 1)
        mx = 0.0
        for w in range(1, 301):
            Ez = sum(F_[w - s] * mu ** (-math.ceil(s / 3)) for s in range(w + 1)) / A_[w]
            mx = max(mx, Ez)
            if Ez > bound * (1 + 1e-12):
                okz = False
        worst[mu] = (mx, bound)
    okt = all(A_[w - s] * F_[s] <= A_[w] for w in range(0, 200) for s in range(w + 1))
    check('G3', okz and okt, 'E[mu^(-ceil(S/3))] <= 1/(2mu - 1) for w <= 300 (largest %s against bounds %s); A(w-s)F(s) <= A(w)'
          % (['%.6f' % v[0] for v in worst.values()], ['%.6f' % v[1] for v in worst.values()]))
    # Lemma R with mu_5, and gamma <= mu5^|U| / (2 mu5 - 1)
    lev = {}
    for w, R, st, W, FM in LV.census(22, DS, 22):
        lev[w] = (R, st, W, FM)
    lam_pow = LAM ** np.arange(12)
    okR = True
    worstR = 0.0
    for t in range(3, 23):
        R, st, W, FM = lev[t]
        full = st == 0
        S = LV.site_mask(W[full], FM[full], t)
        sets = LV.separated_sets(t - 2)
        U = np.array(sets, dtype=np.uint64)
        for a in range(0, len(U), 512):
            cnt = np.bitwise_count(S[None, :] & U[a:a + 512, None])
            V = lam_pow[cnt].sum(axis=1)
            for k, v in enumerate(V):
                sz = bin(sets[a + k]).count('1')
                ratio = v / (mu5 ** sz * F_[t])
                worstR = max(worstR, ratio)
                if ratio > 1 + 1e-12:
                    okR = False
    check('G4', okR, 'Lemma R with mu_5: V(t;U) <= mu_5^|U| F(t) for every 3-separated U, t <= 22 (largest ratio %.4f)' % worstR)
    okG = True
    worstG = 0.0
    for w in range(8, 15):
        R, st, W, FM = lev[w]
        Aw = len(W)
        N = 1 << w
        r = (R & np.uint64(N - 1)).astype(np.int64)
        G = fourier(r, N)
        h = np.arange(N, dtype=np.int64)
        ai = LV.angles_int(w, h)
        dist = []
        for u in range(w):
            a_ = ai[w - 1 - u]
            mod = 1 << (u + 1)
            dist.append(np.minimum(a_, mod - a_))
        flag = [5 * dist[u] >= (1 << (u + 1)) for u in range(w)]
        last = np.full(N, -10, dtype=np.int64)
        usize = np.zeros(N, dtype=np.int64)
        for i in range(0, w - 2):
            take = flag[w - 1 - i] & (i - last >= 3)
            usize[take] += 1
            last[take] = i
        gam = np.abs(G) / Aw
        bnd = mu5 ** usize / (2 * mu5 - 1)
        rat = gam[1:] / bnd[1:]
        worstG = max(worstG, float(rat.max()))
        if (rat > 1 + 1e-9).any():
            okG = False
    check('G5', okG, 'gamma_w(h) <= mu_5^|U(h)| / (2 mu_5 - 1) at every h != 0, 8 <= w <= 14 (largest ratio %.4f)' % worstG)

    say('--- GC2940 section 4 (no prediction: the renewal rate)')
    f = [0.0] + [DS[k - 1] * BETA ** (-k) for k in range(1, 400)]
    m1 = sum(k * f[k] for k in range(len(f)))
    v = [Fr(F_[n] * 2 ** n, 3 ** n) for n in range(0, 421)]
    errs = [abs(float(v[n]) - 1 / m1) for n in range(0, 421)]
    rates = []
    for n0 in (40, 80, 160, 320):
        a_ = max(errs[n0:n0 + 40])
        b_ = max(errs[n0 + 40:n0 + 80]) if n0 + 80 <= 420 else None
        if b_:
            rates.append((n0, (a_ / b_) ** (1 / 40) if b_ > 0 else float('inf')))
    say('   1/m_1 = %.12f, v_400 = %.12f; per-step decay of max|v_n - 1/m_1| over blocks of 40: %s'
        % (1 / m1, float(v[400]), ', '.join('%d: %.4f' % x for x in rates)))
    s1 = sum(f)
    check('G6', abs(s1 - 1) < 1e-12, 'P(1) = sum f_k = 1 (to 1e-12, 399 terms)')

    say('--- GC2940 section 5')
    okT = okC = ok0 = okB = True
    ncase = 0
    for ell in range(0, 10):
        for p, s in words_from(0, ell):
            if s != 0:
                continue
            rp = start(p)
            gp = parity_word(rp, ell)[1]
            for k in range(1, 6):
                for j in range(0, 4):
                    Vkj = set(start(q) for q, _ in words_from(0, k + j))
                    direct = 0
                    for t in range(1 << k):
                        n = rp + (1 << ell) * t
                        pw, x = parity_word(n, ell)
                        if pw != p or x != gp + 3 ** ell * t:
                            okT = False
                        if valid_from(parity_word(n, ell + k + j)[0]) is not None:
                            direct += 1
                    M = 1 << (k + j)
                    inv = pow(3, -ell, M)
                    form = sum(1 for vv in Vkj if (inv * (vv - gp)) % M < (1 << k))
                    if direct != form:
                        okC = False
                    if j == 0 and direct != A_[k]:
                        ok0 = False
                    if j == 1:
                        D = 0
                        for t in range(1 << k):
                            n = rp + (1 << ell) * t
                            st = valid_from(parity_word(n, ell + k)[0])
                            if st is not None and st >= 1 and DS[st] == 0 and (parity_word(n, ell + k + 1)[0][-1] == 1):
                                D += 1
                        if A_[k] - D != direct:
                            okB = False
                    ncase += 1
    check('G7', okT and okC and ok0 and okB, 'every full prefix of length <= 9, k <= 5, j <= 3 (%d cases): T^l(r_p + 2^l t) = g_p + 3^l t; '
          'count = residue formula; C_p(k,0) = A(k); A(k) - D_(p,k) = C_p(k,1)' % ncase)
    rnd = random.Random(1672)
    p = ()
    while len(p) < 240:
        p += (0, 0, 0) if rnd.random() < 0.5 else (1, 0, 0)
    okL = valid_from(p) == 0
    rp = start(p)
    gp = parity_word(rp, 240)[1]
    for k, j in ((4, 0), (4, 2), (5, 3)):
        M = 1 << (k + j)
        inv = pow(3, -240, M)
        Vkj = set(start(q) for q, _ in words_from(0, k + j))
        direct = sum(1 for t in range(1 << k) if valid_from(parity_word(rp + (1 << 240) * t, 240 + k + j)[0]) is not None)
        form = sum(1 for vv in Vkj if (inv * (vv - gp)) % M < (1 << k))
        okL = okL and direct == form and (j > 0 or direct == A_[k])
    check('G8', okL, 'a random full prefix of length 240 (blocks 000 and 100, seed 1672): the same transport at (k, j) = (4,0), (4,2), (5,3)')
    p = (1, 0, 1)
    rp = start(p)
    nxt = [parity_word(rp + 8 * t, 4)[0] for t in (0, 1)]
    ext = [valid_from(q) is not None for q in nxt]
    check('G9', valid_from(p) == 3 and rp == 1 and parity_word(1, 3)[1] == 5 and parity_word(9, 3)[1] == 32 and ext == [False, True],
          'the guard: 101 has state 3 (slack %s), r = 1, T^3(1) = 5, T^3(9) = 32, only t = 1 extends' % CS[3])


# ---------------------------------------------------------------- GC2942
def gc2942():
    say('--- GC2942 sections 3 and 4')
    ok = True
    for w in range(2, 13):
        for ell in range(1, w):
            n = w - ell
            M = 1 << w
            for q, s in words_from(0, w):
                u, v = q[:ell], q[ell:]
                if (3 ** ell * start(q) - (2 ** ell * start(v) - numer(u))) % M != 0:
                    ok = False
                if not (2 * numer(u) < 3 ** ell):
                    ok = False
                if valid_from(v) is None:
                    ok = False
    check('E1', ok, 'prefix phase 3^l r(uv) = 2^l r(v) - B_l(u) mod 2^w, B_l(u) < 3^l/2, suffix valid, w <= 12, every split')
    okC = True
    ncase = 0
    worst = float('inf')
    for w in range(8, 17):
        W = words_from(0, w)
        N = 1 << w
        rr = [start(q) for q, _ in W]
        G = fourier(rr, N)
        Aw = len(W)
        for ell in range(1, w - 1):
            n = w - ell
            b = 3 ** ell
            cls = {}
            for q, _ in W:
                cls[q[ell:]] = cls.get(q[ell:], 0) + 1
            sumM2 = sum(m * m for m in cls.values())
            H = 1
            while H * b <= N:
                Q = fejer_energy(G, Aw, H, b % N)
                lo1 = (4 * H / math.pi ** 2) * sumM2 / Aw ** 2
                lo2 = 4 * H / (math.pi ** 2 * A_[n])
                if not (Q >= lo1 - 1e-9 and lo1 >= lo2 - 1e-12):
                    okC = False
                worst = min(worst, Q / lo1)
                ncase += 1
                H += 1 if H < 8 else H // 4
    check('E2', okC, '(C) Q_(3^l)(H) >= (4H/pi^2) sum M_v^2 / A^2 >= 4H/(pi^2 A(n)) whenever H 3^l <= 2^w, 8 <= w <= 16 (%d cases; least ratio %.3f)' % (ncase, worst))
    # null model, exact over all odd b, w = 10
    w = 10
    N = 1 << w
    W = words_from(0, w)
    rr = [start(q) for q, _ in W]
    Aw = len(W)
    G = fourier(rr, N)
    okN = True
    for J in range(1, 8):
        H = 1 << J
        mean = np.mean([fejer_energy(G, Aw, H, b) - 1 for b in range(1, N, 2)])
        m = w - J
        Cm = sum(c * c for c in np.bincount(np.array(rr) % (1 << m), minlength=1 << m))
        exact = H / Aw - Cm / Aw ** 2
        if abs(mean - exact) > 1e-9 or exact > H * (1 / Aw - 1 / N) + 1e-12:
            okN = False
    pow3 = np.mean([fejer_energy(G, Aw, 8, s * pow(3, k, N) % N) - 1 for k in range(1 << (w - 2)) for s in (1, N - 1)])
    allodd = np.mean([fejer_energy(G, Aw, 8, b) - 1 for b in range(1, N, 2)])
    check('E3', okN and abs(pow3 - allodd) < 1e-9, 'null model at w = 10: mean over odd b of Q_b(2^J) - 1 = H/A - C_(w-J)/A^2 <= H(1/A - 1/N), J <= 7; '
          'the +-3^k cycle has the same mean')
    # odd-shell formula
    okS = True
    for w in (10, 12, 14):
        N = 1 << w
        W = words_from(0, w)
        Aw = len(W)
        G = fourier([start(q) for q, _ in W], N)
        for a in range(0, w - 1):
            m = w - a
            hs = [(1 << a) * u for u in range(1, 1 << m, 2)]
            mean = np.mean([abs(G[h]) ** 2 for h in hs])
            tot = 0
            for p, s in words_from(0, m - 1):
                # bit 0: if d_s = 0 the letter 0 follows d (state s+1); if d_s = 1 the letter 0 resets (state 0)
                a0 = A_from(s + 1, a) if DS[s] == 0 else A_from(0, a)
                a1 = A_from(s + 1, a) if DS[s] == 1 else 0
                tot += (a0 - a1) ** 2
            if abs(mean - tot) > 1e-6 * max(1, tot):
                okS = False
    lim0 = [B_[w - 1] / A_[w] for w in (40, 200, 1000)]
    check('E4a', okS and abs(lim0[-1] - 1 / 3) < 1e-6,
          'odd-shell formula mean_(v2 h = a) |G(h)|^2 = sum_p Delta_(s_p)(a)^2 at w = 10, 12, 14, every valuation; '
          'A(w) x odd-shell mean = B_(w-1)/A(w): %s -> 1/3' % ['%.6f' % x for x in lim0])
    rows = []
    ok1 = True
    for w in (8, 10, 12, 14):
        N = 1 << w
        W = words_from(0, w)
        G = fourier([start(q) for q, _ in W], N)
        direct = float(np.mean([abs(G[2 * u]) ** 2 for u in range(1, N >> 1, 2)]))
        gpt = A_[w - 2] + 3 * (F_[w] - F_[w - 1])
        mine = B_[w - 2]
        rows.append('w = %d: direct %.4f, B_(w-2) = %d, A(w-2) + 3(F(w) - F(w-1)) = %d' % (w, direct, mine, gpt))
        if abs(direct - gpt) > 1e-6:
            ok1 = False
    for r_ in rows:
        say('   ' + r_)
    lim1 = [(A_[w - 2] + 3 * (F_[w] - F_[w - 1])) / A_[w] for w in (40, 200, 1000)]
    lim1b = [B_[w - 2] / A_[w] for w in (40, 200, 1000)]
    check('E4b', ok1 and abs(lim1[-1] - 7 / 9) < 1e-6,
          'GPT\'s valuation-one numerator A(w-2) + 3(F(w) - F(w-1)) equals the direct mean of |G(2u)|^2 over odd u; its ratio to A(w): %s (claimed -> 7/9); '
          'B_(w-2)/A(w): %s' % (['%.6f' % x for x in lim1], ['%.6f' % x for x in lim1b]))

    say('--- GC2942 sections 5 and 6')
    okV = True
    for (w, ell, H) in ((14, 4, 8), (16, 5, 8), (16, 6, 4)):
        N = 1 << w
        n = w - ell
        W = words_from(0, w)
        Aw = len(W)
        G = fourier([start(q) for q, _ in W], N)
        pref = {}
        for u, s in words_from(0, ell):
            pref.setdefault(s, []).append(numer(u))
        Gs = {}
        for s in pref:
            Gs[s] = fourier([start(v) for v, _ in words_from(s, n)], 1 << n)
        for h in range(1, H):
            direct = G[(3 ** ell * h) % N]
            viaB = sum(e(-h * B / N) * Gs[s][h % (1 << n)] for s in pref for B in pref[s])
            Th = 0
            err = 0.0
            for s, Bs in pref.items():
                C = len(Bs)
                m = Fr(sum(Bs), C)
                var = float(sum((Fr(B) - m) ** 2 for B in Bs) / C)
                Th += C * e(-h * float(m) / N) * Gs[s][h % (1 << n)]
                err += C * var * A_from(s, n)
            bound = 2 * math.pi ** 2 * h * h / N ** 2 * err
            if abs(direct - viaB) > 1e-7 or abs(direct - Th) > bound * (1 + 1e-9) + 1e-9:
                okV = False
    check('E5', okV, '(V) and the exact prefix Fourier form: |G(3^l h) - T(h)| <= (2 pi^2 h^2/N^2) sum C_s v_s A_s(n), three cases')
    okD = okSlot = True
    worstD = 0.0
    for w in (10, 12, 14):
        N = 1 << w
        W = words_from(0, w)
        Aw = len(W)
        for ell in range(1, w):
            q = 3 ** ell
            if q > N:
                break
            n = w - ell
            cls = {}
            for wd, _ in W:
                cls.setdefault(wd[ell:], []).append(wd)
            for H in (q, 2 * q, 4 * q):
                if H > N:
                    continue
                tot = 0.0
                for v, members in cls.items():
                    rs = [start(m) for m in members]
                    for r1 in rs:
                        for r2 in rs:
                            tot += KH((r1 - r2) / N, H)
                    ks = []
                    for m in members:
                        r = start(m)
                        num_ = q * r + numer(m[:ell]) - (2 ** ell) * start(v)    # q r = 2^l r(v) - B + k N
                        if num_ % N:
                            okSlot = False
                        kk = num_ // N
                        ks.append(kk % q)
                    if len(set(ks)) != len(ks):
                        okSlot = False
                lhs = tot / Aw ** 2
                rhs = (1 + math.pi ** 2 / 3) * H / Aw
                worstD = max(worstD, lhs / rhs)
                if lhs > rhs * (1 + 1e-9):
                    okD = False
    check('E6', okD and okSlot, '(D) same-suffix energy <= (1 + pi^2/3) H/A for q = 3^l <= H <= 4q <= N, w = 10, 12, 14 (largest ratio %.3f); '
          'one point per grid slot in every class' % worstD)
    okI = True
    for w in range(4, 13):
        N = 1 << w
        Vs = sorted(start(q) for q, _ in words_from(0, w))
        mark = np.zeros(N, dtype=np.int64)
        mark[Vs] = 1
        cum = np.concatenate([[0], np.cumsum(np.concatenate([mark, mark]))])
        for L in range(1, N + 1):
            r = max(0, math.ceil(math.log2(L)))
            mx = int((cum[L:L + N] - cum[:N]).max())
            if mx > A_[r]:
                okI = False
    check('E7', okI, 'truncation baseline: every circular interval of L residues holds at most A(ceil(log2 L)) valid starts, w <= 12')
    okT3 = True
    w, H = 12, 8
    N = 1 << w
    W = words_from(0, w)
    Aw = len(W)
    rs = [start(q) for q, _ in W]
    for i in range(0, len(W), 7):
        for j2 in range(0, len(W), 5):
            p1, p2 = W[i][0], W[j2][0]
            if p1 == p2:
                continue
            nn = 0
            while nn < w and p1[w - 1 - nn] == p2[w - 1 - nn]:
                nn += 1
            dB = numer(p1) - numer(p2)
            v3 = 0
            while dB % 3 == 0:
                dB //= 3
                v3 += 1
            if v3 != nn:
                okT3 = False
    En = []
    for n in range(0, w + 1):
        cls = {}
        for (q, _), r in zip(W, rs):
            cls.setdefault(q[w - n:] if n else (), []).append(r)
        D = sum(KH((a_ - b_) / N, H) for c in cls.values() for a_ in c for b_ in c) / Aw ** 2
        P = sum(len(c) ** 2 for c in cls.values()) / Aw ** 2
        En.append(D - P)
    G = fourier(rs, N)
    Q1 = fejer_energy(G, Aw, H)
    okE = abs(En[0] - (Q1 - 1)) < 1e-9 and abs(En[w] - (H - 1) / Aw) < 1e-12 and min(En) > -1e-12
    check('E8', okT3 and okE, 'ternary valuation: v3(B(p) - B(p\')) = number of common trailing bits (sampled pairs, w = 12); E_0 = Q - 1, '
          'E_w = (H-1)/A, every E_n >= 0')

    say('--- GC2942 section 7')
    okT = True
    worstT = 0.0
    for w in (10, 12, 14):
        N = 1 << w
        Rr = 3 ** w
        W = words_from(0, w)
        Aw = len(W)
        rs, ks = [], []
        for q, _ in W:
            r = start(q)
            k = parity_word(r, w)[1]
            if Rr * r + numer(q) != N * k or k % Rr != (pow(2, -w, Rr) * numer(q)) % Rr:
                okT = False
            n_ = 4
            if k % 3 ** n_ != (pow(2, -n_, 3 ** n_) * numer(q[w - n_:])) % 3 ** n_:
                okT = False
            rs.append(r)
            ks.append(k % Rr)
        if len(set(ks)) != len(ks):
            okT = False
        G = fourier(rs, N)
        for H in (4, 16, 64):
            Q1 = fejer_energy(G, Aw, H)
            Qt = 1.0
            for h in range(1, H):
                g = abs(sum(e(h * k / Rr) for k in ks)) / Aw
                Qt += 2 * (1 - h / H) * g * g
            lhs = abs(math.sqrt(max(Q1 - 1, 0)) - math.sqrt(max(Qt - 1, 0)))
            rhs = (math.pi / N) * math.sqrt(H * (H * H - 1) / 6)
            worstT = max(worstT, lhs / rhs if rhs else 0)
            if lhs > rhs * (1 + 1e-9):
                okT = False
    check('E9', okT, '(T): R r + B = N k with k = T^w(r) = 2^(-w) B mod 3^w, injective, k mod 3^4 from the last 4 bits; energy error within '
          '(pi/N) sqrt(H(H^2-1)/6) at w = 10, 12, 14, H = 4, 16, 64 (largest ratio %.3f)' % worstT)
    okF = True
    for w in range(2, 15):
        N = 1 << w
        W = words_from(0, w)
        order = sorted(W, key=lambda x: numer(x[0]))
        nums = [numer(q) for q, _ in order]
        okgap = nums[0] == 0 and all(Fr(nums[i + 1] - nums[i]) == Fr(2 ** (w - 1)) * CS[order[i][1]] for i in range(len(nums) - 1)) \
            and Fr(nums[-1]) + Fr(2 ** (w - 1)) * CS[order[-1][1]] == Fr(3 ** w, 2)
        a = pow(3, -w, 2 * N)
        qs = [CS[s] * 2 ** s for s in range(w + 1)]
        if not all(x.denominator == 1 and x.numerator % 2 == 1 for x in qs):
            okgap = False
        Gs = {}
        for q, s in W:
            Gs.setdefault(s, []).append(start(q))
        hh = np.arange(2 * N, dtype=np.int64)
        lhs = np.zeros(2 * N, dtype=complex)
        for s_, rs_ in Gs.items():
            Gf = fourier(rs_, N)
            coef = 1 - np.exp(-2j * np.pi * ((a * int(qs[s_]) * hh) % (2 ** (s_ + 1))) / 2 ** (s_ + 1))
            lhs += coef * Gf[hh % N]
        rhs = 1 - np.exp(-2j * np.pi * hh / (2 * N))
        if np.abs(lhs - rhs).max() > 1e-8:
            okF = False
        okF = okF and okgap
    check('E10', okF, '(F): cylinders tile [0, 3^w/2) in numerator coordinates with gaps 2^(w-1) c_s, q_s odd, and the identity holds '
          'for every h modulo 2^(w+1), w <= 14')
    okG = True
    for (w, ell, H) in ((10, 4, 6), (12, 5, 5), (12, 7, 9)):
        N = 1 << w
        Rr = 3 ** w
        n = w - ell
        W = words_from(0, w)
        Aw = len(W)
        cls = {}
        for q, _ in W:
            cls.setdefault(q[ell:], []).append(q)
        Eter = 0.0
        for h in range(1, H):
            tot = 0.0
            for v, mem in cls.items():
                z = sum(e(h * ((pow(2, -w, Rr) * numer(m)) % Rr) / Rr) for m in mem)
                tot += abs(z) ** 2
            Eter += 2 * (1 - h / H) * tot
        Eter /= Aw ** 2
        aP = pow(2, -w, 3 ** ell)
        pref = words_from(0, ell)
        Eg = 0.0
        Egp = 0.0
        thr = sorted(set(CS[s] for _, s in pref))
        acount = {c: A_from([s for s in range(len(CS)) if CS[s] == c][0], n) for c in thr}
        for h in range(1, H):
            ph = {u: e(h * aP * numer(u) / 3 ** ell) for u, _ in pref}
            sl = {u: CS[s] for u, s in pref}
            tot = 0.0
            for u1, _ in pref:
                for u2, _ in pref:
                    tot += (acount[min(sl[u1], sl[u2])] * ph[u1] * ph[u2].conjugate()).real
            Eg += 2 * (1 - h / H) * tot
            totp = 0.0
            prev = 0
            for c in thr:
                da = acount[c] - prev
                prev = acount[c]
                totp += da * abs(sum(ph[u] for u, _ in pref if sl[u] >= c)) ** 2
            Egp += 2 * (1 - h / H) * totp
        Eg /= Aw ** 2
        Egp /= Aw ** 2
        if abs(Eter - Eg) > 1e-9 or abs(Eg - Egp) > 1e-9:
            okG = False
    check('E11', okG, '(G) and (G\'): the ternary same-suffix energy equals the minimum-slack kernel sum and its threshold factorisation, three cases')

    say('--- GC2942 section 7: the transfer operator')
    okH = okI = okJ = True
    for (w, ell, h) in ((10, 6, 1), (10, 6, 5), (12, 8, 3)):
        Rr = 3 ** ell
        a = pow(2, -w, Rr)
        if a % 2:
            a += Rr
        om = h * a / 2
        P = {0: (lambda t: 1.0 + 0j)}
        W_by = {k: words_from(0, k) for k in range(ell + 1)}

        def Pk(k, t):
            return sum(e(h * a * numer(u) / 3 ** k) for u, s in W_by[k] if CS[s] >= t)
        rnd = random.Random(w * 100 + h)
        for k in range(1, ell + 1):
            zk = e(om * BETA ** (-k))
            for _ in range(6):
                t = Fr(rnd.randint(1, 10 ** 6), 10 ** 6)
                lhs = Pk(k, t)
                rhs = Pk(k - 1, t / Fr(3, 2)) + (zk * Pk(k - 1, (1 + t) / Fr(3, 2)) if t <= Fr(1, 2) else 0)
                if abs(lhs - rhs) > 1e-9:
                    okH = False

                def LkF(kk, y):
                    if kk == 0:
                        return e(om * float(y))
                    v_ = LkF(kk - 1, y / Fr(3, 2))
                    if y < Fr(1, 2):
                        v_ += LkF(kk - 1, (1 + y) / Fr(3, 2))
                    return v_
                if abs(e(-om * BETA ** (-k) * float(t)) * LkF(k, t) - lhs) > 1e-8:
                    okI = False
            # (H): exact piecewise integration of the step function t -> P_(k,t)
            def integral(f, lo, hi, cuts):
                pts = sorted(set([lo, hi] + [c for c in cuts if lo < c < hi]))
                return sum(f((pts[i] + pts[i + 1]) / 2) * float(pts[i + 1] - pts[i]) for i in range(len(pts) - 1))
            cuts = list(set(CS[:k + 2])) + [c - Fr(2, 3) for c in CS[:k + 2]]
            Ik = integral(lambda t: abs(Pk(k, t)) ** 2, Fr(0), Fr(1), list(set(CS[:k + 2])))
            Ik1 = integral(lambda t: abs(Pk(k - 1, t)) ** 2, Fr(0), Fr(1), list(set(CS[:k + 2])))
            cross = integral(lambda s: Pk(k - 1, s + Fr(2, 3)) * Pk(k - 1, s).conjugate(), Fr(0), Fr(1, 3), cuts)
            if abs(Ik - (1.5 * Ik1 + 3 * (zk * cross).real)) > 1e-8 * max(1, Ik):
                okH = False
    for w in range(3, 13):
        Rr = 3 ** w
        aw = pow(2, -w, Rr)
        if aw % 2:
            aw += Rr
        W = words_from(0, w)
        tsmall = min(CS[s] for _, s in W) / 3
        def branch_sum(f, y, kk):
            if kk == 0:
                return f(y)
            v_ = branch_sum(f, y / Fr(3, 2), kk - 1)
            if y < Fr(1, 2):
                v_ += branch_sum(f, (1 + y) / Fr(3, 2), kk - 1)
            return v_
        for h in (0, 1, 2, 7):
            om = h * aw // 2
            Gter = sum(e(h * ((pow(2, -w, Rr) * numer(q)) % Rr) / Rr) for q, _ in W)
            tt = tsmall
            val = e(-om * BETA ** (-w) * float(tt)) * branch_sum(lambda y: e(om * float(y)), tt, w)
            tt2 = tsmall / 7
            val2 = e(-om * BETA ** (-w) * float(tt2)) * branch_sum(lambda y: e(om * float(y)), tt2, w)
            if abs(val - Gter) > 1e-7 or abs(val2 - Gter) > 1e-7:
                okJ = False
            if h == 0 and abs(val - len(W)) > 1e-9:
                okJ = False
    check('E12', okH and okI and okJ, '(H) exactly by piecewise integration, (I) at random rational points, the recursion for P_(k,t), and (J): '
          'beta^w [L^w e_(h a_w/2)](0+) = G_w^ter(h) and A(w) at h = 0, w <= 12')
    # the one-step identity of section 8 and the renewal guard
    ok8 = True
    for w in range(3, 13):
        N = 1 << w
        for s0 in range(0, 6):
            Gs = fourier([start(q) for q, _ in words_from(s0, w)], N)
            kids = [(DS[s0], s0 + 1)] + ([(0, 0)] if DS[s0] == 1 else [])
            Gk = {t: fourier([start(q) for q, _ in words_from(t, w - 1)], N >> 1) for _, t in kids}
            for h in range(0, N, 3):
                rhs = sum(e(-h * b / N) * Gk[t][h % (N >> 1)] for b, t in kids)
                if abs(Gs[(3 * h) % N] - rhs) > 1e-8:
                    ok8 = False
    okg = all(A_from(s, n) == len(words_from(s, n)) for s in range(0, 8) for n in range(0, 12))
    check('E13', ok8 and okg, 'section 8 one-step identity G_(s,w)(3h) = sum e(-hb/2^w) G_(t,w-1)(h), w <= 12, s <= 5; '
          'A_s(n) = 1 + sum_t d_(s+t) A(n-1-t), s < 8, n < 12')


def main():
    say('L1672 carry tests.  d = %s...' % ''.join(map(str, DS[:30])))
    controls()
    gc2940()
    gc2942()
    say('failures: %s' % (FAILS if FAILS else 'none'))
    say('done in %.0f s' % (time.time() - T0))


if __name__ == '__main__':
    main()
