#!/usr/bin/env python3
"""Cloud CL781 addendum 1: replay of three hand statements that carry kit theorems to Mahler's map.

T(n) = ceil(3n/2).  A parity word is valid while every tail of its zero-padded code is below 1/2 (G50).
Stripe: s = -1/3 = ...010101 in the 2-adic integers; its truncations t_L = (4^L - 1)/3.

  H5  last-bit rule: chi_w(p0) xor chi_w(p1) = chi_(w-1)(p) xor [w even], chi_w(n) = T^w(n) mod 2.
  B   barrier (twin of the kit's Rule30RecognizableBarrier.no_recognizable_ranking): after j + 1 steps the orbit
      of t_L is at 3^j 2^(2L-1-j), 0 <= j <= 2L-1, every step valid (run 1 tested the range 1 <= j <= 2L-1 at
      time j, my indexing slip in CL781 addendum 1; it failed and is kept as _run1.out); for a morphism into a finite monoid there are times
      j1 < j2 and a shift e >= 1 such that the rows (L, j2) and (L + e, j1) have the same bit length, the same
      image and the same windows for every large L.  A ranking would then descend for ever.
  PS  planted survivor (twin of Rule30PlantedSurvivor): psi_L flips every even bit k >= 2L below which x agrees
      with the stripe; T' = psi T psi^(-1) maps natural numbers to natural numbers, T'(t_L) = 0, and the number of
      n < 2^W valid through t is the same for T' as for T plus one exactly when 2L - 1 <= W and t > 2 ceil(W/2) + 1.
Predictions are in CL781 addendum 1, pushed before the run.  Self-checks of hand arguments, not a second read.
Usage: cloud_mahler_barrier_planted.py
"""
import itertools, math, time
import numpy as np

OK = []


def check(name, cond, detail=""):
    OK.append(bool(cond))
    print(f"   [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def T(n):
    return (3 * n + (n & 1)) >> 1


def valid_len(n, tmax):
    """Number of initial parities of n forming a valid word, capped at tmax (exact integer slack, as in the first probe)."""
    mt = None; x = n
    for L in range(tmax):
        e = x & 1
        if L and e and not (3 * mt > (1 << (L + 1))):
            return L
        mt = (3 << L) - (e << (L + 1)) if mt is None else min(3 * mt, 3 << L) - (e << (L + 1))
        x = T(x)
    return tmax


# ------------------------------------------------------------------ H5
def part_h5():
    print("== H5: the last-bit rule, every word of length w - 1, w <= 20")
    ok = True; prev = None
    for w in range(1, 21):
        n = np.arange(1 << w, dtype=np.int64); x = n.copy()
        for _ in range(w):
            x = (3 * x + (x & 1)) >> 1
        chi = (x & 1).astype(np.int64)
        if prev is not None:
            half = 1 << (w - 1)
            ok &= bool(((chi[:half] ^ chi[half:]) == (prev ^ (1 if w % 2 == 0 else 0))).all())
        prev = chi
    check("chi_w(r) xor chi_w(r + 2^(w-1)) = chi_(w-1)(r) xor [w even] for every r < 2^(w-1), 2 <= w <= 20", ok)
    # the pair count that goes with H2: how many n < 2^w have T(n) in the middle third [2^(w-1), 2^w)
    okc = True; devs = []
    for w in range(2, 21):
        n = np.arange(1 << w, dtype=np.int64); tn = (3 * n + (n & 1)) >> 1
        cnt = int(((tn >= (1 << (w - 1))) & (tn < (1 << w))).sum())
        okc &= (cnt == (2 ** (w + 1) - 2) // 3 - (2 ** w - 2) // 3)
        x = n.copy()
        for _ in range(w):
            x = (3 * x + (x & 1)) >> 1
        devs.append(int((x & 1).sum()) - (1 << (w - 1)))
    check("the check differs from the shifted word's check on exactly floor((2^(w+1) - 2)/3) - floor((2^w - 2)/3) of the n < 2^w, 2 <= w <= 20", okc)
    print("   exact excess of chi = 1 over one half of the n < 2^w, w = 2..20:", devs)


# ------------------------------------------------------------------ B
def part_barrier():
    print("== B: the truncated stripes and the matching of (length, image, windows)")
    ok_orbit = ok_valid = True
    for L in range(1, 31):
        t = (4 ** L - 1) // 3; x = T(t)
        for j in range(0, 2 * L):                      # run 2: after j + 1 steps the orbit is at 3^j 2^(2L-1-j)
            ok_orbit &= (x == 3 ** j * 2 ** (2 * L - 1 - j)); x = T(x)
        ok_valid &= (valid_len(t, 2 * L + 6) == 2 * L + 1)
    check("after j + 1 steps the orbit of t_L is at 3^j 2^(2L-1-j), 0 <= j <= 2L-1, L <= 30", ok_orbit)
    check("t_L is valid through exactly 2L + 1 parities, L <= 30 (word 1 0^(2L-1) 1, then a second 1)", ok_valid)

    def word(L, j):                                   # binary digits from the top
        return bin(3 ** j)[2:] + "0" * (2 * L - 1 - j)

    monoids = {
        "ones modulo 5": (lambda w: w.count("1") % 5),
        "value modulo 7, read from the top": (lambda w: int(w, 2) % 7),
        "the last two letters and the length parity": (lambda w: (w[-2:], len(w) % 2)),
    }
    K = 3                                             # window size at each end
    for name, mu in monoids.items():
        # image of 0^k is eventually periodic: find index k0 and period pi by brute force on this statistic
        vals = [mu("1" + "0" * k) for k in range(200)]
        pi = next(p for p in range(1, 60) if all(vals[k] == vals[k + p] for k in range(60, 120)))
        lam = lambda j: len(bin(3 ** j)[2:]) - j
        key = lambda j: (mu(bin(3 ** j)[2:]), bin(3 ** j)[2:][:K], j % pi, lam(j) % (2 * pi))
        seen = {}; pair = None
        for j in range(4, 4000):
            k = key(j)
            if k in seen and lam(j) > lam(seen[k]):
                pair = (seen[k], j); break
            seen.setdefault(k, j)
        j1, j2 = pair; e = (lam(j2) - lam(j1)) // 2
        good = True
        for L in range(j2 + 40, j2 + 45):
            a, b = word(L, j2), word(L + e, j1)
            good &= (len(a) == len(b) and mu(a) == mu(b) and a[:K] == b[:K] and a[-K:] == b[-K:])
        check(f"monoid '{name}': period {pi}; times j1 = {j1} < j2 = {j2}, shift e = {e}; rows (L, j2) and (L + e, j1) agree at five depths", good and e >= 1)


# ------------------------------------------------------------------ PS
def stripe_agreement(x):
    a = 0
    while ((x >> a) & 1) == (1 if a % 2 == 0 else 0):
        a += 1
    return a


def psi(x, L):
    a = stripe_agreement(x)
    for k in range(2 * L, a + 1, 2):
        x ^= 1 << k
    return x


def psi_inv(y, L):
    """Inverse on natural numbers other than t_L (whose preimage is the stripe itself)."""
    if y % (4 ** L) != (4 ** L - 1) // 3:
        return y
    hi = y >> (2 * L)
    assert hi != 0, "t_L has the infinite stripe as preimage"
    j = 2 * L + ((hi & -hi).bit_length() - 1)          # lowest set bit of y at or above 2L
    for k in range(2 * L, j + 1, 2):
        y ^= 1 << k
    return y


def part_planted():
    print("== PS: the planted survivor")
    for L in (2, 3):
        tL = (4 ** L - 1) // 3
        inv_ok = all(psi(psi_inv(y, L), L) == y for y in range(1 << 16) if y != tL) and \
                 all(psi_inv(psi(x, L), L) == x for x in range(1 << 16) if psi(x, L) != tL)
        check(f"L = {L}: psi and its inverse are mutually inverse on every natural number below 2^16 (t_L = {tL} apart)", inv_ok)
        check(f"L = {L}: psi fixes bit 0 and maps every n < 2^16 to a natural number of at most two more bits",
              all((psi(x, L) & 1) == (x & 1) and psi(x, L).bit_length() <= x.bit_length() + 2 for x in range(1 << 16)))
        Tp = lambda x: 0 if x == tL else psi(T(psi_inv(x, L)), L)
        # itinerary under T' equals itinerary of psi^(-1) x under T (bit 0 is fixed by psi): checked directly on a sample
        samp = True
        for x in list(range(1, 400)) + [tL + 4 ** L * k for k in range(1, 60)]:
            if x == tL:
                continue
            y = psi_inv(x, L); u = x; v = y
            for _ in range(12):
                samp &= ((u & 1) == (v & 1))
                if u == tL:
                    break
                u = Tp(u); v = T(v)
        check(f"L = {L}: the parity word of x under T' is the parity word of psi^(-1)(x) under T (sample of 458 starts, 12 steps)", samp)
        table = True; plus = 0
        for W in range(1, 15):
            for t in range(1, 41):
                nT = sum(valid_len(n, t) == t for n in range(1, 1 << W))
                nTp = sum((n == tL) or (valid_len(psi_inv(n, L), t) == t) for n in range(1, 1 << W))
                want = nT + (1 if (2 * L - 1 <= W and t > 2 * math.ceil(W / 2) + 1) else 0)
                table &= (nTp == want); plus += (nTp != nT)
        check(f"L = {L}: survival table of T' = that of T, plus one exactly when 2L - 1 <= W and t > 2 ceil(W/2) + 1 (W <= 14, t <= 40)", table,
              f"{plus} of 560 cells carry the extra one")


def main():
    t0 = time.time()
    part_h5(); part_barrier(); part_planted()
    print(f"ALL PASS: {all(OK)} ({sum(OK)} of {len(OK)} checks); {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
