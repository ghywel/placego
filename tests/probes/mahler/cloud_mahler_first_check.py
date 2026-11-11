#!/usr/bin/env python3
"""Cloud CL781: the first parity past the free bits of Mahler's census, the twin of the kit's Rule30FirstChecks.

Mahler's map T(n) = ceil(3n/2) = (3n + b)/2 with b = n mod 2.  The parity word b_0 b_1 ... of the T-orbit of n is
"valid" up to length L when every tail of the zero-padded word, u_j = sum_k b_(j+k) 2^k / 3^(k+1), is below 1/2
(G50: a Z-number is a positive integer whose whole word is valid).  For 0 <= n < 2^w the first w parities are free:
each word of length w belongs to exactly one n (G51).  The first parity that n itself decides is
    chi_w(n) = T^w(n) mod 2,
the first check.  This probe replays four hand statements of CL781 and measures the shares.

  H1  chi_w(2^w - 1 - n) = chi_w(n).
  H2  with T(n) = q 2^(w-1) + r, r < 2^(w-1):  q <= 2 and chi_w(n) = chi_(w-1)(r) xor (q mod 2).
  H3  T^w(n) is the least nonnegative residue of C 2^(-w) modulo 3^w, C = sum_k b_k 2^k 3^(w-1-k).
  H4  the share of valid n < 2^w that pass the first check is at least A(w+1)/A(w) - 1.

Validity is tracked exactly by one integer per n.  Let M_L be the least scaled slack min_j (1/2 - u_j)(3/2)^(L-j)
of the first L parities.  Appending the bit e is allowed iff e = 0 or M_L > 1/3, and
M_(L+1) = min(3 M_L / 2, 3/4) - e/2.  The integer kept is M_L 2^(L+1).

Predictions MF1 to MF5 are in CL781, pushed before the run.  Usage: cloud_mahler_first_check.py [WMAX]
"""
import sys, time
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 26
CHUNK = 1 << 22
BIG = np.int64(1) << 60


def run_chunk(lo, hi, w):
    """For n in [lo, hi): alive after w free parities, chi_w, can-take-1, pass flags for checks 1 and 2, T^w(n)."""
    x = np.arange(lo, hi, dtype=np.int64)
    mt = np.full(hi - lo, BIG, dtype=np.int64)
    alive = np.ones(hi - lo, dtype=bool)
    for L in range(w):
        e = x & 1
        if L:
            alive &= (e == 0) | (3 * mt > (np.int64(1) << (L + 1)))
        mt = np.minimum(3 * mt, np.int64(3) << L) - (e << (L + 1))
        x = (3 * x + e) >> 1
    xw = x.copy()
    chi = (x & 1).astype(bool)
    can1 = 3 * mt > (np.int64(1) << (w + 1))
    pass1 = alive & (~chi | can1)
    # one more step, for the second check
    e = x & 1
    mt2 = np.minimum(3 * mt, np.int64(3) << w) - (e << (w + 1))
    x2 = (3 * x + e) >> 1
    chi2 = (x2 & 1).astype(bool)
    can1b = 3 * mt2 > (np.int64(1) << (w + 2))
    pass2 = pass1 & (~chi2 | can1b)
    return alive, chi, can1, pass1, pass2, xw


def main():
    t0 = time.time()
    print("== Mahler's first check: T(n) = ceil(3n/2), n < 2^w; chi_w(n) = T^w(n) mod 2")
    print("   w | A(w) valid | share chi=1, all n | share chi=1, valid | boundary B | deaths D | D/B | pass share | floor A(w+1)/A(w)-1 | second pass share")
    A = {}; rows = []; prev_chi = None
    okH1 = okH2 = okH3 = okQ = okBound = True
    for w in range(1, WMAX + 1):
        N = 1 << w
        tot = dict(A=0, O=0, Ov=0, B=0, D=0, P1=0, P2=0)
        chi_all = np.empty(N, dtype=bool) if w <= 22 else None
        for lo in range(0, N, CHUNK):
            hi = min(N, lo + CHUNK)
            alive, chi, can1, pass1, pass2, xw = run_chunk(lo, hi, w)
            tot["A"] += int(alive.sum()); tot["O"] += int(chi.sum()); tot["Ov"] += int((chi & alive).sum())
            bd = alive & ~can1
            tot["B"] += int(bd.sum()); tot["D"] += int((bd & chi).sum())
            tot["P1"] += int(pass1.sum()); tot["P2"] += int(pass2.sum())
            okBound &= bool((xw < 3 ** w).all())
            if chi_all is not None:
                chi_all[lo:hi] = chi
            if w <= 18:                                   # H3, exact in 64 bits while 3^(2w) < 2^63
                n = np.arange(lo, hi, dtype=np.int64)
                x = n.copy(); C = np.zeros(hi - lo, dtype=np.int64)
                for k in range(w):
                    e = x & 1
                    C = 3 * C + (e << k)
                    x = (3 * x + e) >> 1
                m3 = 3 ** w
                inv = pow(2, -w, m3)
                okH3 &= bool(((C % m3) * inv % m3 == xw).all())
        A[w] = tot["A"]
        if chi_all is not None:
            okH1 &= bool((chi_all == chi_all[::-1]).all())
            if prev_chi is not None:
                n = np.arange(N, dtype=np.int64)
                tn = (3 * n + (n & 1)) >> 1
                q = tn >> (w - 1); r = tn & ((1 << (w - 1)) - 1)
                okQ &= bool((q <= 2).all())
                okH2 &= bool((chi_all == (prev_chi[r] ^ ((q & 1) == 1))).all())
            prev_chi = chi_all
        rows.append((w, tot))
    for w, tot in rows:
        a = tot["A"]; nxt = A.get(w + 1)
        floor = f"{nxt / a - 1:.4f}" if nxt else "   -  "
        db = f"{tot['D'] / tot['B']:.4f}" if tot["B"] else "  -   "
        p2 = f"{tot['P2'] / tot['P1']:.4f}" if tot["P1"] else "  -   "
        print(f"   {w:2d} | {a:10d} | {tot['O'] / (1 << w):.4f} | {tot['Ov'] / a:.4f} | {tot['B']:9d} | {tot['D']:9d} | {db} | {tot['P1'] / a:.4f} | {floor} | {p2}")
    print("MF1 control, A(1..10) = 2, 3, 5, 8, 12, 18, 27, 40, 60, 90:", [A[w] for w in range(1, 11)] == [2, 3, 5, 8, 12, 18, 27, 40, 60, 90])
    print(f"MF2: H1 complement (w <= 22): {okH1} | H2 shift rule with q <= 2 (w <= 22): {okH2 and okQ} | H3 least residue modulo 3^w (w <= 18): {okH3}"
          f" | T^w(n) < 3^w (all w): {okBound}")
    h4 = all(tot["P1"] / tot["A"] >= A[w + 1] / tot["A"] - 1 - 1e-12 for w, tot in rows if w + 1 in A)
    print("MF2: H4 floor at every w:", h4)
    mf3 = all(abs(tot["O"] / (1 << w) - 0.5) <= 0.02 for w, tot in rows if 12 <= w)
    mf4a = all(abs(tot["D"] / tot["B"] - 0.5) <= 0.05 for w, tot in rows if 16 <= w)
    mf4b = all(abs(tot["P1"] / tot["A"] - 0.75) <= 0.03 for w, tot in rows if 16 <= w)
    mf5 = all(abs(tot["P2"] / tot["P1"] - 0.75) <= 0.03 for w, tot in rows if 16 <= w)
    print(f"MF3 (share chi = 1 over all n within 0.02 of 1/2, w >= 12): {mf3}")
    print(f"MF4 (boundary share within 0.05 of 1/2, and pass share within 0.03 of 3/4, w >= 16): {mf4a} and {mf4b}")
    print(f"MF5 (second pass share within 0.03 of 3/4, w >= 16): {mf5}")
    print("parities: number of n < 2^w with chi = 1 is even at every w:", all(tot["O"] % 2 == 0 for _, tot in rows),
          "| parity of the valid ones Ov(w), w = 1..:", "".join(str(tot["Ov"] % 2) for _, tot in rows),
          "| parity of deaths D(w):", "".join(str(tot["D"] % 2) for _, tot in rows))
    print(f"seconds {time.time() - t0:.0f}")


if __name__ == "__main__":
    main()
