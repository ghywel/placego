#!/usr/bin/env python3
"""Cloud CL779: numerical self-check of the intermediate identities in the clock-exponent lemma
(reports/CLOUD-LIFT-CLOCK-CARRY-20261111.md, section 7.3).  Not a proof and not a second read.

For several (depth n, level k) past the lemma's threshold, with Q = P_k and the prefix s = (u_1..u_n) computed
modulo 2^(k+2):
  1. the defect b(t) = (s(t+Q) - s(t)) / 2^k obeys b(t+1) = A(s(t)) b(t) modulo 2 (equation (1)), where A is the
     Jacobian of the prefix map (row m: u_(m-1), u_m, 1 in columns m, m-1, m-2);
  2. H = J_(Q/2)(t), the product of the Jacobians over Q/2 ticks, is idempotent modulo 2, and the next Q/2 ticks
     give the same product modulo 4, so J_Q(t) = H^2 modulo 4;
  3. pi b = b modulo 2 for pi = H mod 2, and b(t+Q) = J_Q(t) b(t) modulo 4;
  4. H^(n+2) = H^n modulo 4 (H^2 is the identity on the image part), and H^n (1 - H^n) = 0 modulo 2;
  5. c = (b(t) + b(t+Q)) / 2 is nonzero modulo 2, and the period does double again at level k + 2.
A deliberately wrong Jacobian (the entries u_(m-1) and u_m exchanged) must break identity 1.
Usage: cloud_lift_lemma_check.py
"""
import numpy as np


def orbit(n, bits, T):
    mask = (1 << bits) - 1
    u = np.ones(n + 2, dtype=np.int64); u[1] = 2
    hist = np.empty((T, n), dtype=np.int64)
    for t in range(T):
        hist[t] = u[2:]
        nxt = u.copy()
        nxt[2:] = (u[2:] * u[1:-1] + u[:-2] - 1) & mask
        u = nxt
    return hist


def jac(row, n, wrong=False):
    """Jacobian at the state row = (u_1..u_n), as an integer matrix."""
    A = np.zeros((n, n), dtype=np.int64)
    for m in range(n):                       # coordinate m is depth m + 1
        below = row[m - 1] if m >= 1 else 2  # u_(depth - 1), with u_0 = 2
        if wrong:
            A[m, m] = row[m]
            if m >= 1:
                A[m, m - 1] = below
        else:
            A[m, m] = below
            if m >= 1:
                A[m, m - 1] = row[m]
        if m >= 2:
            A[m, m - 2] = 1
    return A


def period(hist, k, tail0):
    h = hist & ((1 << k) - 1)
    T = len(h)
    for e in range(0, 20):
        P = 1 << e
        if tail0 + 2 * P > T:
            return None
        if (h[tail0:T - P] == h[tail0 + P:T]).all():
            return P
    return None


def prod_mod(hist, t, L, n, mod):
    J = np.eye(n, dtype=np.int64)
    for i in range(L):
        J = (jac(hist[t + i], n) @ J) % mod
    return J


def case(n, k):
    bits = k + 2
    T = 1 << 17
    hist = orbit(n, bits, T)
    tail0 = T // 2
    P1, P2, Q, Qn, Qnn = (period(hist, j, tail0) for j in (1, 2, k, k + 1, k + 2))
    hyp = Q >= 2 * max(P2, n * P1) and Qn == 2 * Q
    t0 = tail0
    d = (hist[t0 + Q] - hist[t0]) & ((1 << bits) - 1)
    assert (d % (1 << k) == 0).all()
    b = (d >> k) % 4
    d2 = (hist[t0 + 2 * Q] - hist[t0 + Q]) & ((1 << bits) - 1)
    bQ = (d2 >> k) % 4
    # 1. the tangent equation modulo 2, and its failure with a wrong Jacobian
    ok1 = True; bad1 = False
    for t in range(t0, t0 + 64):
        bt = (((hist[t + Q] - hist[t]) & ((1 << bits) - 1)) >> k) % 2
        bn = (((hist[t + 1 + Q] - hist[t + 1]) & ((1 << bits) - 1)) >> k) % 2
        ok1 &= bool(((jac(hist[t], n) @ bt) % 2 == bn).all())
        bad1 |= not bool(((jac(hist[t], n, wrong=True) @ bt) % 2 == bn).all())
    # 2. H idempotent modulo 2; the two halves agree modulo 4
    H = prod_mod(hist, t0, Q // 2, n, 4)
    H2 = prod_mod(hist, t0 + Q // 2, Q // 2, n, 4)
    pi = H % 2
    ok2 = bool(((pi @ pi) % 2 == pi).all()) and bool((H == H2).all())
    JQ = (H2 @ H) % 4
    # 3. pi b = b modulo 2; b(t+Q) = J_Q b modulo 4
    ok3 = bool(((pi @ (b % 2)) % 2 == b % 2).all()) and bool(((JQ @ b) % 4 == bQ).all())
    # 4. H^(n+2) = H^n modulo 4; H^n is idempotent modulo 2
    Hn = np.linalg.matrix_power(H.astype(object), n) % 4
    Hn2 = (Hn @ H.astype(object) @ H.astype(object)) % 4
    ok4 = bool((Hn == Hn2).all()) and bool((((Hn % 2) @ (Hn % 2)) % 2 == Hn % 2).all())
    # 5. the next defect is nonzero modulo 2, and the period doubles again
    s = (b + bQ) % 4
    ok5 = bool((s % 2 == 0).all()) and bool(((s // 2) % 2).any()) and Qnn == 2 * Qn
    rank = int(np.linalg.matrix_rank(pi.astype(float))) if n <= 64 else -1
    print(f"   depth {n:3d}, level {k:2d}: P_1 = {P1}, P_2 = {P2}, P_k = {Q}, P_(k+1) = {Qn}, P_(k+2) = {Qnn}; hypothesis of (c): {hyp};"
          f" identities 1 to 5: {ok1} {ok2} {ok3} {ok4} {ok5}; wrong Jacobian breaks 1: {bad1};"
          f" diagonal of pi: {[int(x) for x in np.diag(pi)]}" if n <= 12 else
          f"   depth {n:3d}, level {k:2d}: P_1 = {P1}, P_2 = {P2}, P_k = {Q}, P_(k+1) = {Qn}, P_(k+2) = {Qnn}; hypothesis of (c): {hyp};"
          f" identities 1 to 5: {ok1} {ok2} {ok3} {ok4} {ok5}; wrong Jacobian breaks 1: {bad1}; ones on the diagonal of pi at depths {[int(i) + 1 for i in np.nonzero(np.diag(pi))[0]]}")
    return hyp and ok1 and ok2 and ok3 and ok4 and ok5 and bad1


def main():
    print("== the lemma's intermediate identities, numerically")
    res = [case(n, k) for n, k in ((5, 5), (7, 5), (7, 6), (8, 7), (12, 7), (28, 8), (29, 11), (40, 11))]
    print("ALL HOLD:", all(res))


if __name__ == "__main__":
    main()
