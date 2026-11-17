#!/usr/bin/env python3
"""Cloud CL769/CL770: own checks for the three short reads LN-02.1, RS-4 (c2)/(c3), LN-03.1.

Frame: zero-boundary half-row. F(Y) = (Y >> 1) xor (Y or (Y << 1)); bit i of Y is depth i + 1;
a_t(Y) = bit 0 of F^t(Y), a function of the row bits y_0..y_t.
"""
import itertools, math, random, time
from fractions import Fraction
import numpy as np


def F_int(Y):
    return (Y >> 1) ^ (Y | (Y << 1))


# ---------------------------------------------------------------- LN-02.1
def prefix_xor(w, L):
    p = w; sh = 1
    while sh < L:
        p ^= p << sh; sh <<= 1
    return p & ((1 << L) - 1)


def chain(t):
    """The weighted anti-diagonal chain. Returns (kind, k, S): D_S a_t is identically 1 if kind is
    'odd', or the constant c if kind is ('vanish', c)."""
    L = t - 1
    w = (1 << L) - 1          # bit i-1 is w_i, i = 1..L
    S = [t - 1]
    while True:
        if bin(w).count("1") % 2 == 1:
            S.append(L - 1)
            return "odd", len(S), S
        if L < 2:
            return ("vanish", None), len(S), S
        P = prefix_xor(w, L)                      # bit k-1 is W_k
        c = bin(P & ((1 << (L - 1)) - 1)).count("1") % 2    # |W| over k = 1..L-1
        S.append(L - 2)
        w = (P >> 1) & ((1 << (L - 2)) - 1)       # w'_j = W_(j+1), j = 1..L-2
        L -= 2
        if w == 0:
            return ("vanish", c), len(S), S


def tip_table(t):
    Y = np.arange(1 << (t + 1), dtype=np.uint64)
    X = Y.copy()
    for _ in range(t):
        X = (X >> np.uint64(1)) ^ (X | (X << np.uint64(1)))
    return (X & np.uint64(1)).astype(np.uint8)


def ln02():
    print("== LN-02.1")
    bad = []; pow2 = {}
    for t in range(2, 2000):
        kind, k, S = chain(t)
        if (t + 1) & t == 0:                      # t + 1 a power of two
            pow2[t] = (kind, k)
            if not (kind == ("vanish", 1) and k == (t + 1) // 2):
                bad.append((t, kind, k))
        else:
            v2 = ((t + 1) & -(t + 1)).bit_length() - 1
            if not (kind == "odd" and k == 1 + 2 ** v2):
                bad.append((t, kind, k))
    print("R1 chain, 2 <= t < 2000: mismatches with k_t = 1 + 2^v2(t+1) (and the power-of-two rule):", len(bad), bad[:4])
    print("   at t = 2^m - 1:", pow2)
    print("   first chain sets:", {t: chain(t)[2] for t in (2, 3, 4, 5, 7, 9, 11, 13, 15)})

    ok2 = True; nrows = 0
    tables = {}
    for t in range(2, 17):
        a = tip_table(t); tables[t] = a
        kind, k, S = chain(t)
        idx = np.arange(1 << (t + 1), dtype=np.int64)
        d = np.zeros(1 << (t + 1), dtype=np.uint8)
        for sub in itertools.product((0, 1), repeat=len(S)):
            m = sum(1 << s for s, b in zip(S, sub) if b)
            d ^= a[idx ^ m]
        ok2 &= bool((d == 1).all()); nrows += 1 << (t + 1)
        # the pair law itself
        m1, m2 = 1 << (t - 1), 1 << (t - 2)
        dd = a ^ a[idx ^ m1] ^ a[idx ^ m2] ^ a[idx ^ m1 ^ m2]
        ok2 &= bool((dd == (t - 1) % 2).all())
    print("R2 exhaustive t = 2..16: derivative over the chain set is 1 on every row, and the pair law "
          "D_(t-1) D_(t-2) a_t = (t-1) mod 2 holds:", ok2, "| rows", nrows)

    ok3 = True; rowsF = []
    for t in range(1, 17):
        a = tip_table(t) if t not in tables else tables[t]
        g = 1.0 - 2.0 * a.astype(np.float64)
        f = np.abs(np.fft.fft(g)) / len(g)
        sup = float(f.max()); even = float(f[0::2].max())
        bound = 1.0 / (2 ** t * math.sin(math.pi / 2 ** (t + 1)))
        ok3 &= sup <= bound + 1e-9 and even < 1e-9
        rowsF.append((t, round(sup, 5), round(bound, 5)))
    print("R3 additive coefficients t = 1..16: sup <= bound and even frequencies vanish:", ok3)
    print("   (t, sup, bound):", rowsF[:4], rowsF[7], rowsF[11], rowsF[15], "| limit 2/pi =", round(2 / math.pi, 5))

    # R4: inclusion-maximal monomials of the algebraic normal form
    print("R4 smallest inclusion-maximal monomial of size >= 2 (best constant-derivative certificate):")
    out = []
    for t in range(2, 20):
        n = t + 1
        c = tip_table(t).copy()
        for i in range(n):                          # Moebius transform
            v = c.reshape(-1, 2, 1 << i)
            v[:, 1, :] ^= v[:, 0, :]
        h = c.copy()
        for i in range(n):                          # h(S) = OR of c over supersets of S
            v = h.reshape(-1, 2, 1 << i)
            v[:, 0, :] |= v[:, 1, :]
        p = np.zeros_like(c)
        for i in range(n):                          # a proper superset in the support exists
            v = h.reshape(-1, 2, 1 << i); u = p.reshape(-1, 2, 1 << i)
            u[:, 0, :] |= v[:, 1, :]
        maxi = np.nonzero((c == 1) & (p == 0))[0]
        sizes = np.array([bin(int(s)).count("1") for s in maxi])
        big = sizes[sizes >= 2]
        least = int(big.min())
        ex = [int(s) for s, z in zip(maxi, sizes) if z == least][:2]
        exs = [[i for i in range(n) if (s >> i) & 1] for s in ex]
        kind, k, S = chain(t)
        chain_is_max = int(sum(1 << s for s in S)) in set(int(s) for s in maxi)
        out.append((t, k, least, int((sizes == least).sum()), int(sizes.max()), chain_is_max))
        print("   t", t, "| chain k_t", k, "| least size", least, "| how many of that size", int((sizes == least).sum()),
              "| largest maximal monomial", int(sizes.max()), "| chain set is a maximal monomial:", chain_is_max,
              "| example", exs[0])
    odd = [(t, k, l) for t, k, l, *_ in out if t % 2 == 1 and t >= 5]
    print("   odd t >= 5: (t, k_t, least):", odd)
    print("R4 verdict (least = k_t at every odd t from 5 to 19):", all(k == l for _, k, l in odd))
    print("   Walsh bound 1 - 2^(1-least) at odd t:", [(t, 1 - 2.0 ** (1 - l)) for t, _, l in odd])


# ---------------------------------------------------------------- RS-4 (c2)
def enc(x, y, nblocks):
    s = []
    for j in range(nblocks):
        s += [1, 1, 0, y[j], 0, x[j], 0]
    return s


def block_map(s, kind):
    """Forward window-8 block map. kind 'A': (x, y) -> (sigma x, y); 'B': (x, y) -> (sigma x, y + x)."""
    out = []
    for p in range(len(s) - 7):
        j = next((j for j in range(7) if s[p + j] == 1 and s[p + j + 1] == 1), None)
        if j is None:
            out.append(0); continue
        ph = (7 - j) % 7
        if ph in (0, 1):
            out.append(1)
        elif ph == 3:
            out.append(s[p] ^ (s[p + 2] if kind == "B" else 0))
        elif ph == 5:
            out.append(s[p + 7])
        else:
            out.append(0)
    return out


def rs4():
    print("== RS-4 (c2)")
    rng = random.Random(4)
    M = 60
    x = [rng.randrange(2) for _ in range(M)]; y = [rng.randrange(2) for _ in range(M)]
    okb = True
    for e in range(7):
        s = enc(x, y, M)[e:]
        for kind in "AB":
            want = enc(x[1:], [a ^ (b if kind == "B" else 0) for a, b in zip(y, x)][:M - 1], M - 1)[e:]
            got = block_map(s, kind)
            n = min(len(got), len(want)) - 7
            okb &= got[:n] == want[:n]
    print("R5a block maps A, B act as (sigma x, y) and (sigma x, y + x) at all seven phases:", okb)

    def element(x, y, a, word, nsym):
        """sigma^a word(h) by the closed form; word is a string in 'AB', first letter applied first."""
        n = len(word)
        yy = list(y)
        for j, ch in enumerate(word):
            if ch == "B":
                for i in range(len(yy) - j):
                    yy[i] ^= x[i + j]
        xx = x[n:]
        nb = (a + nsym) // 7 + 2
        return bytes(enc(xx, yy, nb)[a:a + nsym])

    # closed form against the block maps on one word
    Mx = 760
    xs = [1 if i in (1, 4, 16, 64, 256) else 0 for i in range(Mx)]
    ys = [1 if i in (2, 8, 32, 128, 512) else 0 for i in range(Mx)]
    s = enc(xs, ys, 80)
    for ch in "BAB":
        s = block_map(s, ch)
    print("   closed form agrees with the block maps on the word BAB:", bytes(s[:300]) == element(xs, ys, 0, "BAB", 300))

    def box(xv, yv):
        seen = {}; coll = []
        for n in range(0, 9):
            for word in itertools.product("AB", repeat=n):
                wd = "".join(word)
                for a in range(0, 21):
                    el = element(xv, yv, a, wd, 7 * 600)
                    if el in seen:
                        coll.append((seen[el], (a, wd)))
                    else:
                        seen[el] = (a, wd)
        return len(seen), coll
    nd, coll = box(xs, ys)
    print("R5b box (words in A, B of length <= 8, a <= 20; 4200 symbols compared): distinct", nd,
          "of", 511 * 21, "| collisions", len(coll))
    nd0, coll0 = box(xs, [0] * Mx)
    first = min(coll0, key=lambda c: (c[1][0] + len(c[1][1]), c)) if coll0 else None
    print("   control y = 0: distinct", nd0, "| collisions", len(coll0), "| a smallest one:", first,
          "| sigma^7 h = A h:", element(xs, [0] * Mx, 7, "", 4200) == element(xs, [0] * Mx, 0, "A", 4200))

    # R6 the count
    def kappa_le_1(ws):
        P = Fraction(0); Q = Fraction(0)
        for w in ws:
            if w % 2 == 0:
                P += Fraction(1, 2 ** (w // 2))
            else:
                Q += Fraction(1, 2 ** ((w + 1) // 2))        # times sqrt 2
        return 1 - P >= 0 and 2 * Q * Q <= (1 - P) ** 2, (2 * Q * Q == (1 - P) ** 2 and 1 - P >= 0)
    fam = 0; eq = []; worst = Fraction(0); okc = True
    for q in range(1, 5):
        for ws in itertools.combinations_with_replacement(range(1, 11), q):
            le, is_eq = kappa_le_1(ws)
            if not le:
                continue
            fam += 1
            if is_eq:
                eq.append(ws)
            a = [0] * 201; a[0] = 1
            for c in range(1, 201):
                a[c] = sum(a[c - w] for w in ws if c - w >= 0)
            N = list(itertools.accumulate(a))
            for c in range(201):
                okc &= a[c] * a[c] <= 2 ** c
                T = sum(N[c - 2 * k] for k in range(0, c // 2 + 1))
                okc &= T * T < 64 * 2 ** c
                worst = max(worst, Fraction(T * T, 2 ** c))
    print("R6 families q <= 4, 1 <= w_i <= 10, kappa <= 1:", fam, "| with kappa = 1:", eq,
          "| a_c^2 <= 2^c and T(s)^2 < 64 * 2^s for c, s <= 200:", okc,
          "| largest T(s)/2^(s/2):", round(float(worst) ** 0.5, 4))

    # R7 the prefix datum in the (c2) model, w = (3, 3): sizes 7 + 2a + 3|u|
    els = {"h": element(xs, ys, 0, "", 40), "sigma h": element(xs, ys, 1, "", 40),
           "g0 h": element(xs, ys, 0, "B", 40), "g1 h": element(xs, ys, 0, "BA", 40)}
    same = [(p, q) for p, q in itertools.combinations(els, 2) if els[p][:5] == els[q][:5] and els[p] != els[q]]
    print("R7 (c2) model, w = (3,3), sizes at most 10 (h 7, sigma h 9, g0 h 10, g1 h 10): distinct elements "
          "with the same first 5 symbols:", same)


# ---------------------------------------------------------------- LN-03.1
def ln03():
    print("== LN-03.1")
    N = 6000
    def row(prefix, period):
        bits = list(prefix)
        while len(bits) < N:
            bits += period
        return sum(b << i for i, b in enumerate(bits[:N]))
    A = row([], [1, 0, 1, 1, 1, 1, 1]); C = row([], [1, 1, 0, 0, 0, 0, 1])
    B = row([1, 1], [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0])
    Fw = lambda Y: F_int(Y) & ((1 << N) - 1)
    mask = (1 << 4000) - 1
    G = lambda Y: Fw(Fw(Y))
    print("R8 on the first 4000 depths: G A = C:", G(A) & mask == C & mask, "| G C = A:", G(C) & mask == A & mask,
          "| G B = C:", G(B) & mask == C & mask,
          "| depth 1 of F A, F B, F C:", Fw(A) & 1, Fw(B) & 1, Fw(C) & 1, "| of A, B, C:", A & 1, B & 1, C & 1)
    def per(Y, lo=100, hi=3900):
        return min(p for p in range(1, 200) if all(((Y >> i) & 1) == ((Y >> (i + p)) & 1) for i in range(lo, hi)))
    print("   tail periods of F A, F B, F C, G A, G B:", per(Fw(A)), per(Fw(B)), per(Fw(C)), per(G(A)), per(G(B)),
          "(equality on 4000 depths past preperiod plus period is equality everywhere)")
    def free(Y, n):
        out = []; even = []
        for s in range(n):
            even.append(Y & 1); Y = Fw(Y); out.append(Y & 1); Y = Fw(Y)
        return out, all(even)
    for name, Y, want in (("A", A, [1, 0] * 60), ("B", B, [0] + [0, 1] * 60), ("C", C, [0, 1] * 60)):
        f, alive = free(Y, 100)
        print("   row", name, "black at even ticks 0..198:", alive, "| free word starts", f[:8],
              "| matches the stated word on 100 terms:", f == want[:100])
    diff = [i for i in range(140) if ((A >> i) & 1) != ((B >> i) & 1)]
    print("   A and B differ at", len(diff), "of the first 140 depths; G A = G B")


if __name__ == "__main__":
    t0 = time.time()
    ln02(); rs4(); ln03()
    print("seconds", round(time.time() - t0, 1))
