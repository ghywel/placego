#!/usr/bin/env python3
"""Cloud CL776/CL777: Rule 30's polynomial read over the integers, seen by each prime.

A_0 = single 1 at site 0;  A_(t+1)(j) = A_t(j-1) + A_t(j) + A_t(j+1) + A_t(j) * A_t(j+1)  over Z.
Modulo 2 this is rule 30 (left xor (centre or right)).  Modulo a prime p it is a p-state automaton.
The lift and its right diagonals are Nersissian's (arXiv 2609.25078, Theorems 12, 13); this probe adds
the left diagonals and the centre column modulo odd primes.  Predictions: CHAT-LEDGER CL776.
"""
import math, sys, time
import numpy as np

A051023 = [1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0]


def gammq(a, x):
    """Upper regularised incomplete gamma Q(a, x) (Numerical Recipes)."""
    if x <= 0:
        return 1.0
    if x < a + 1:
        ap = a; s = d = 1.0 / a
        for _ in range(10000):
            ap += 1; d *= x / ap; s += d
            if abs(d) < abs(s) * 1e-15:
                break
        return max(0.0, 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a)))
    b = x + 1 - a; c = 1e300; d = 1 / b; h = d
    for i in range(1, 10000):
        an = -i * (i - a); b += 2; d = an * d + b
        d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c
        c = 1e-300 if abs(c) < 1e-300 else c
        d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def chi2_p(obs, exp):
    obs = np.asarray(obs, float).ravel(); exp = np.asarray(exp, float).ravel()
    x = float(((obs - exp) ** 2 / exp).sum())
    return x, len(obs) - 1, gammq((len(obs) - 1) / 2, x / 2)


def indep_p(table):
    t = np.asarray(table, float); n = t.sum()
    e = np.outer(t.sum(1), t.sum(0)) / n
    x = float(((t - e) ** 2 / e).sum()); dof = (t.shape[0] - 1) * (t.shape[1] - 1)
    return x, dof, gammq(dof / 2, x / 2)


def exact_rows(T):
    """The integer lift itself, rows 0..T, as dicts site -> int."""
    row = {0: 1}; rows = [row]
    for t in range(T):
        new = {}
        for j in range(-t - 1, t + 2):
            l, c, r = row.get(j - 1, 0), row.get(j, 0), row.get(j + 1, 0)
            v = l + c + r + c * r
            if v:
                new[j] = v
        row = new; rows.append(row)
    return rows


def rows_mod(m, T, dtype=np.int64):
    """Full rows modulo m for t = 0..T; returns array [T+1, 2T+1], site j at column j + T."""
    W = 2 * T + 1
    out = np.zeros((T + 1, W), dtype=dtype)
    a = np.zeros(W + 2, dtype=dtype); a[T + 1] = 1
    out[0] = a[1:-1]
    for t in range(T):
        a[1:-1] = (a[:-2] + a[1:-1] + a[2:] + a[1:-1] * a[2:]) % m
        out[t + 1] = a[1:-1]
    return out


def centre_mod(m, T, dtype=np.int32, wrap=False):
    """Centre column for ticks 0..T-1, updating only the cone that can reach the centre."""
    W = 2 * T + 5; c = T + 2
    a = np.zeros(W, dtype=dtype); a[c] = 1
    out = np.zeros(T, dtype=dtype)
    for t in range(T):
        out[t] = a[c]
        r = min(t + 1, T - 1 - t)
        if r < 0:
            break
        lo, hi = c - r - 1, c + r + 2
        seg = a[lo - 1:hi + 1]
        v = seg[:-2] + seg[1:-1] + seg[2:] + seg[1:-1] * seg[2:]
        if not wrap:
            v %= m
        a[lo:hi] = v
        a[lo - 1] = 0; a[hi] = 0
    return out


def least_eventual_period(s, maxP):
    """(transient, period) with the least period <= maxP supported by at least two further periods."""
    s = np.asarray(s); n = len(s)
    for P in range(1, maxP + 1):
        d = np.nonzero(s[:-P] != s[P:])[0]
        m = int(d[-1]) + 1 if len(d) else 0
        if n - P - m >= max(2 * P, n // 2):      # run 2: the periodic part must cover half the window
            return m, P
    return None


def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return "*".join(f"{q}^{e}" if e > 1 else str(q) for q, e in sorted(f.items())) or "1"


def order(a, p):
    k = 1; x = a % p
    while x != 1:
        x = x * a % p; k += 1
    return k


def main():
    t0 = time.time()
    # ---- H0 and the exact integer lift
    rows = exact_rows(14)
    par = [rows[t].get(0, 0) % 2 for t in range(15)]
    print("H0 exact integer lift, t <= 14: centre parity equals rule 30:", par == A051023[:15])
    print("   centre counts A_t(0), t = 0..6:", [rows[t].get(0, 0) for t in range(7)])
    print("   bit length of A_t(0), t = 8..14:", [rows[t].get(0, 0).bit_length() for t in range(8, 15)])
    okR = all(rows[t].get(t - 1, 0) == t and rows[t].get(t - 2, 0) == t * t for t in range(2, 15))
    okL = all(rows[t].get(-t + 1, 0) == 2 ** t - 1 for t in range(1, 15))
    print("H1 right diagonals: depth 1 is t and depth 2 is t^2 (t = 2..14):", okR)
    print("H2 left diagonal depth 1 is 2^t - 1 exactly (t = 1..14):", okL)
    u = lambda t, n: 1 + rows[t].get(-t + n, 0)
    okU = all(u(t + 1, n) == u(t, n) * u(t, n - 1) + u(t, n - 2) - 1 for t in range(1, 14) for n in range(1, 8))
    print("   left-edge recurrence u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1, depths 1..7, t = 1..13:", okU)
    for p in (3, 5, 7):
        rm = rows_mod(p, 14)
        ok = all(rows[t].get(j, 0) % p == rm[t, j + 14] for t in range(15) for j in range(-t, t + 1))
        print(f"   the mod-{p} automaton equals the integer lift reduced mod {p} (t <= 14):", ok)

    # ---- H1, H2 on the automata modulo p
    Ts = 3000
    print("== edge diagonals of the mod-p automata (t <= 3000)")
    for p in (2, 3, 5, 7, 11, 13):
        rm = rows_mod(p, Ts)
        right = []; left = []
        for n in range(1, 9):
            sr = np.array([rm[t, (t - n) + Ts] for t in range(n, Ts + 1)])
            sl = np.array([rm[t, (-t + n) + Ts] for t in range(n, Ts + 1)])
            right.append(least_eventual_period(sr, 900)); left.append(least_eventual_period(sl, 900))
        fmt = lambda x: "none<=900" if x is None else f"{x[0]}+{factor(x[1])}"
        print(f"   p = {p:2d}: right diagonals depth 1..8 (transient+period): {[fmt(x) for x in right]}")
        print(f"            left diagonals  depth 1..8 (transient+period): {[fmt(x) for x in left]}"
              + (f" | order of 2 mod p = {order(2, p)}" if p > 2 else ""))
    chk = []
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        rm = rows_mod(p, 400)
        sl = np.array([rm[t, (-t + 1) + 400] for t in range(1, 401)])
        tp = least_eventual_period(sl, 100)
        chk.append((p, order(2, p), tp[1] if tp else None, tp[0] if tp else None))
    print("   depth-1 left diagonal, (p, order of 2 mod p, period found, transient):", chk,
          "| all equal:", all(a == b and c == 0 for _, a, b, c in chk))

    # ---- N1 the centre column modulo primes
    T = 1 << 16
    cols = {}
    for p in (2, 3, 5, 7, 11, 13):
        s = time.time(); cols[p] = centre_mod(p, T)
        print(f"centre column modulo {p}: {T} ticks in {time.time() - s:.0f} s", flush=True)
    print("control: the mod-2 column starts as A051023:", cols[2][:50].tolist() == A051023)
    print("first 40 centre residues modulo 3:", "".join(map(str, cols[3][:40].tolist())))
    print("first 40 centre residues modulo 5:", "".join(map(str, cols[5][:40].tolist())))
    print("== N1a residues, N1b eventual period, N1c pairs")
    for p in (3, 5, 7, 11, 13):
        c = cols[p]
        cnt = np.bincount(c, minlength=p)
        x, dof, pv = chi2_p(cnt, [T / p] * p)
        half = c[T // 2:]
        per = None
        for P in range(1, 8193):
            if half[0] == half[P] and np.array_equal(half[:-P], half[P:]):
                per = P; break
        line = f"   p = {p:2d}: counts {cnt.tolist()} chi2 {x:.1f} dof {dof} p-value {pv:.3f} | period <= 8192 in the second half: {per}"
        if p <= 7:
            pair = np.bincount(c[:-1] * p + c[1:], minlength=p * p)
            x2, dof2, pv2 = chi2_p(pair, [(T - 1) / p / p] * (p * p))
            line += f" | pairs chi2 {x2:.1f} dof {dof2} p-value {pv2:.3f}"
        print(line)
    print("== N1d independence across primes")
    for (p, q) in ((2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (3, 5), (3, 7), (5, 7)):
        tab = np.bincount(cols[p] * q + cols[q], minlength=p * q).reshape(p, q)
        x, dof, pv = indep_p(tab)
        print(f"   mod {p} against mod {q}: chi2 {x:.1f} dof {dof} p-value {pv:.3f}")

    # ---- N1e 2-adic valuation of the centre count
    T2 = 1 << 14
    c32 = centre_mod(0, T2, dtype=np.uint32, wrap=True).astype(np.uint64)
    print("== N1e 2-adic valuation of the centre count (lift modulo 2^32, 2^14 ticks)")
    print("   control: low bit equals rule 30:", (c32[:50] & 1).astype(int).tolist() == A051023)
    val = np.full(T2, 32, dtype=np.int64)
    for k in range(31, -1, -1):
        val[(c32 >> np.uint64(k)) & np.uint64(1) == 1] = k
    cnt = [int((val == k).sum()) for k in range(11)] + [int((val >= 11).sum())]
    exp = [T2 / 2 ** (k + 1) for k in range(11)] + [T2 / 2 ** 11]
    x, dof, pv = chi2_p(cnt, exp)
    print("   counts of valuation 0..10 and >= 11:", cnt)
    print("   geometric expectation:              ", [round(e, 1) for e in exp], f"| chi2 {x:.1f} dof {dof} p-value {pv:.3f}")
    tt = np.arange(T2) + 1
    vt = np.zeros(T2, dtype=np.int64)
    for k in range(1, 20):
        vt[tt % (1 << k) == 0] = k
    tab = np.zeros((4, 4))
    for a in range(4):
        for b in range(4):
            tab[a, b] = ((np.minimum(val, 3) == a) & (np.minimum(vt, 3) == b)).sum()
    x, dof, pv = indep_p(tab)
    print("   valuation of the count (rows 0,1,2,>=3) against valuation of t+1 (columns 0,1,2,>=3):")
    for a in range(4):
        print("     ", tab[a].astype(int).tolist())
    print(f"   independence: chi2 {x:.1f} dof {dof} p-value {pv:.3f}")
    # ---- N1f (CL776 addendum 1, written after run 1): primes where 2 has odd order, to 2^18 ticks
    if "--long" in sys.argv:
        T3 = 1 << 18
        print("== N1f centre column modulo 7, 23, 31 to 2^18 ticks; statistics on the fresh part 2^16..2^18")
        for p in (7, 23, 31):
            s = time.time(); c = centre_mod(p, T3); fresh = c[1 << 16:]
            cnt = np.bincount(fresh, minlength=p)
            x, dof, pv = chi2_p(cnt, [len(fresh) / p] * p)
            line = f"   p = {p:2d} (order of 2: {order(2, p)}): fresh residues chi2 {x:.1f} dof {dof} p-value {pv:.3f}"
            allc = np.bincount(c, minlength=p); xa, dofa, pva = chi2_p(allc, [T3 / p] * p)
            line += f" | whole run chi2 {xa:.1f} p-value {pva:.3f}"
            if p == 7:
                pair = np.bincount(fresh[:-1] * p + fresh[1:], minlength=p * p)
                x2, dof2, pv2 = chi2_p(pair, [(len(fresh) - 1) / p / p] * (p * p))
                line += f" | fresh pairs chi2 {x2:.1f} dof {dof2} p-value {pv2:.3f}"
                same = bool(np.array_equal(c[:1 << 16], cols[7]))
                line += f" | first 2^16 ticks agree with the short run: {same}"
            print(line + f" | {time.time() - s:.0f} s", flush=True)
    print("seconds", round(time.time() - t0))


if __name__ == "__main__":
    main()
