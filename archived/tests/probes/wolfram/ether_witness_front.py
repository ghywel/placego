#!/usr/bin/env python3
"""ether_witness_front.py: the exact mismatch front of the GC2328 ether witness, as a finite periodic-patch certificate (Cloud, CL669).

Frame (PR69 / L1258): X_0 = 1 for ever, X_1(t+1) = X_1(t) XOR X_0(t), X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) for j >= 2.
Reference ether E_j(t) = ether(j+3, t+1), ether(i, t) = bit (t mod 8) of (43, 202, 178, 172)[i mod 4]. Witness: X_j(0) = E_j(0) for j >= 1.
Mismatch set D(t) = {j : X_j(t) != E_j(t)}; front R*(t) = max D(t).

Claim (PROOF-SKETCH, Cloud): R*(0) = 0, D(1) = D(2) = empty, R*(3) = 0, and R*(t) = 2 floor((3t-8)/4) for every t >= 4.
Proof: (A) direct exact computation for t <= 12 (prefix autonomy makes it exact); (B) for t >= 12, the band of depths
[b(t), R*(t)+1] evolves on its own: X_j(t+1) needs X_(j-2)(t) only when X_(j-1)(t) = 0, so the bottom rises by 1 when the
bottom cell is black and by 2 otherwise; cells above the band equal E by the two-party front lemma (L1258/GC2330:
D_j(t) = 0 for j > ceil(3(t-3)/2), and ceil(3(t-3)/2) <= R*(t)+1 for all t >= 4, checked below); the band content at
t = 20 equals the content at t = 12 shifted by 12 depths, and ether(i, t) = ether(i+2, t+4) makes E invariant under the
shift (12 depths, 8 ticks); so the eight-tick evolution repeats for ever, and at every tick of the cycle the band's maximal
mismatch is R*(t). (C) Corollary: the witness's ether-pair episode at depths (k, k+1) has length exactly
L_w(k) = min{t : R*(t) >= k} = ceil((4 ceil(k/2) + 8)/3) for k >= 1, i.e. floor(2k/3)+4 for k not congruent to 0, 2 mod 6
and floor(2k/3)+3 for k congruent to 0, 2 mod 6, since the front moves by 0 or 2 from even depths and never rests on an odd
depth. With GC2327 (M(k) <= floor(2k/3)+4, two-party) this gives M(k) = floor(2k/3)+4 for all k not congruent to 0, 2 mod 6.
"""
import numpy as np

WORDS = (43, 202, 178, 172)


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def E(j, t):
    return ether(j + 3, t + 1)


def Rstar(t):
    return 2 * ((3 * t - 8) // 4)


def Lw(k):
    return -(-(4 * (-(-k // 2)) + 8) // 3)


def main():
    assert all(ether(i + 2, t + 4) == ether(i, t) for i in range(4) for t in range(8)), "ether glide symmetry"
    assert all(ether(i, t + 1) == ether(i, t) ^ (ether(i + 3, t) | ether(i + 2, t)) for i in range(4) for t in range(8)), "ether_step"
    # (A) direct exact computation to t = 12
    T, J = 40, 120
    X = np.zeros((T + 1, J + 1), dtype=np.uint8)
    X[0, 0] = 1
    for j in range(1, J + 1):
        X[0, j] = E(j, 0)
    for t in range(T):
        Y = np.zeros(J + 1, dtype=np.uint8)
        Y[0] = 1
        Y[1] = X[t, 1] ^ X[t, 0]
        Y[2:] = X[t, 2:] ^ (X[t, 1:-1] | X[t, :-2])
        X[t + 1] = Y
    expect = {0: 0, 1: -1, 2: -1, 3: 0}
    for t in range(0, 13):
        D = [j for j in range(J + 1 - 2 * t) if X[t, j] != E(j, t)]   # exact: X_j(t) depends on X_0..X_j(0) only
        mx = max(D, default=-1)
        want = expect[t] if t < 4 else Rstar(t)
        assert mx == want, (t, mx, want)
    print("(A) direct: max mismatched depth is 0, none, none, 0 for t = 0..3 and 2 floor((3t-8)/4) for t = 4..12: PASS")
    # the two-party front lemma bound never exceeds R*(t)+1
    assert all(-(-3 * (t - 3) // 2) <= Rstar(t) + 1 for t in range(4, 10000)), "lemma bound vs R*+1"
    print("(A') ceil(3(t-3)/2) <= R*(t)+1 for 4 <= t < 10000: PASS")
    # (B) the band induction from t0 = 12
    t0 = 12
    band = {j: int(X[t0, j]) for j in range(Rstar(t0) - 7, Rstar(t0) + 2)}
    print(f"(B) band at t = {t0}: depths {min(band)}..{max(band)}, content {''.join(str(band[j]) for j in sorted(band))}")

    def step_band(band, t):
        b, top = min(band), max(band)

        def xt(j):
            if j in band:
                return band[j]
            assert j > top
            return E(j, t)
        bn = b + 1 if band[b] == 1 else b + 2
        nb = {}
        for j in range(bn, Rstar(t + 1) + 2):
            m = xt(j - 1)
            o = 1 if m == 1 else xt(j - 2)       # the deeper input is read only when the nearer one is white
            nb[j] = xt(j) ^ o
        return nb
    cur = dict(band)
    for t in range(t0, t0 + 8):
        cur = step_band(cur, t)
        R = Rstar(t + 1)
        mism = [j for j in cur if cur[j] != E(j, t + 1)]
        assert mism and max(mism) == R, (t + 1, mism, R)
        print(f"    t = {t + 1:2d}: band {min(cur)}..{max(cur)}, mismatches {mism}, front {R}, lemma bound {-(-3 * (t + 1 - 3) // 2)}")
    shifted = {j + 12: v for j, v in band.items()}
    assert cur == shifted, "band did not return shifted"
    print("(B) after eight ticks the band equals the band at t0 shifted by 12 depths: PASS (induction closes)")
    # (C) the corollary against the law and Local's table
    local = [4, 4, 6, 6, 7, 7, 8, 8, 10, 10, 11, 11, 12, 12, 14, 14, 15, 15, 16, 16]
    for k in range(1, 400):
        t = next(t for t in range(4, 4000) if Rstar(t) >= k)
        assert t == Lw(k), (k, t, Lw(k))
        f = (2 * k) // 3 + 4 - (1 if k % 6 in (0, 2) else 0)
        assert Lw(k) == f, (k, Lw(k), f)
    assert [Lw(k) for k in range(1, 21)] == local
    print("(C) L_w(k) = min{t : R*(t) >= k} = ceil((4 ceil(k/2)+8)/3) = floor(2k/3)+4-[k = 0,2 mod 6] for k < 400; equals Local's M(k) for k <= 20: PASS")
    print("ETHER_WITNESS_FRONT_DONE")


if __name__ == "__main__":
    main()
