#!/usr/bin/env python3
"""collatz_demand_unimodal.py: DU, is every ACTUAL Collatz demand law unimodal? Q9 (drawn by Local 2026-10-08).
G218 (GC428, reviewed by Local L256) proves G217's optimized allocation bound is no worse than G74's original sum
when the demand d_a = Delta_t(a) is unimodal, and records that actual demand unimodality is unproved. L048
(collatz_audit_g93_g94.py) found 48,727 of the 524,800 actual laws to T = 1024 not log-concave, every failure at the
edge triple j = 1. An edge failure P_1^2 < P_0 P_2 is a dip (P_0 > P_1 < P_2) exactly when P_0 > P_1, and otherwise
a convex but rising start, which stays unimodal; nobody has checked which. Claimed in CLOUD-LOCAL.md with these
predictions pushed before the run.

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/prizes/collatz_demand_unimodal.py [TMAX=1024]
COST:       a few minutes at TMAX = 1024 on one core (L048's computation plus a linear scan per law).

The laws are L048's, computed by the same exact-integer recursion (copied, not imported, so this file stands alone):
ell_t = least a with 3^a > 2^t (ell_0 = 0); F_T(a) = [a >= ell_T]; F_r(a) = F_(r+1)(a) + F_(r+1)(a+1) for a >= ell_r,
0 below; atoms P_j = F_r(ell_r + j) - F_r(ell_r + j - 1). G74's demand at time t is this atom sequence at r = t + 1,
padded with zeros, so unimodality of d is unimodality of P (zeros at both ends do not matter; an internal zero would).

PREDICTIONS (Local's, published before the run):
  DU-P1 (blind, confidence 0.5): every actual demand law with T <= 1024 is unimodal.
  DU-P2 (blind, confidence 0.6): if any law is not unimodal, its only reversal is a dip at the edge, P_0 > P_1 < P_2,
         right after a noncritical step, and none occurs at T <= 64.
  DU-C0 (control): 524,800 laws, of which exactly 48,727 are not log-concave (L048 reproduced).
  DU-C1 (control, can say no): the unimodality test rejects (2, 1, 2) and (1, 0, 1) and accepts (1, 2, 2, 1),
         (3, 2, 2, 1) and (0, 1, 3, 2, 0).
  D1 (descriptive): the first non-unimodal law (by T, then r downward), if any, and the largest dip depth P_0 / P_1.
OUTCOME, 2026-10-08 05:34 (M5, one run at commit 43b5ca6; transcript outside Git; about three minutes). DU-P1, P2
HELD and DU-C0, C1 PASS: all 524,800 actual demand laws with T <= 1024 are unimodal, including all 48,727 that are not
log-concave. Every edge failure of log-concavity is a convex but rising start (P_0 <= P_1), never a dip. So G218's
comparison (optimized <= original) applies to every actual law through T = 1024. This is a finite certificate, not a
proof for all T. A hand route: the step is P = (2q_0 + q_1, q_1 + q_2, q_2 + q_3, ...); the (1,1) part preserves
unimodality, critical steps have q_0 = 0, and a dip after a noncritical step needs 2q_0 > q_2 and q_3 > q_1, so an
edge invariant that survives the schedule would prove it for all T.
"""
import sys

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1024


def unimodal(P):
    nz = [j for j, x in enumerate(P) if x]
    if not nz:
        return True, None
    lo, hi = nz[0], nz[-1]
    if any(P[j] == 0 for j in range(lo, hi + 1)):
        return False, 'gap'
    j = lo
    while j < hi and P[j + 1] >= P[j]:
        j += 1
    while j < hi and P[j + 1] <= P[j]:
        j += 1
    if j == hi:
        return True, None
    return False, j


def logconcave(P):
    nz = [j for j, x in enumerate(P) if x]
    if not nz:
        return True
    lo, hi = nz[0], nz[-1]
    if any(P[j] == 0 for j in range(lo, hi + 1)):
        return False
    return all(P[j] * P[j] >= P[j - 1] * P[j + 1] for j in range(lo + 1, hi))


def main():
    c1 = (not unimodal([2, 1, 2])[0] and not unimodal([1, 0, 1])[0] and unimodal([1, 2, 2, 1])[0]
          and unimodal([3, 2, 2, 1])[0] and unimodal([0, 1, 3, 2, 0])[0])
    ELL, a = [], 0
    for t in range(TMAX + 2):
        while 3 ** a <= 2 ** t:
            a += 1
        ELL.append(a)
    ELL[0] = 0
    laws = notlc = notuni = 0
    first, edge_only, early, after_noncrit, worst = None, True, False, True, None
    for T in range(1, TMAX + 1):
        top = ELL[T] + 1
        F = [1 if x >= ELL[T] else 0 for x in range(top + 2)]
        for r in range(T - 1, -1, -1):
            l = ELL[r]
            G = [0] * (top + 2)
            for x in range(l, top + 1):
                G[x] = F[x] + F[x + 1] if x + 1 < len(F) else F[x] + 1
            G[top + 1] = 2 ** (T - r)
            P = [G[l + j] - (G[l + j - 1] if l + j - 1 >= 0 else 0) for j in range(top + 1 - l + 1)]
            laws += 1
            if not logconcave(P):
                notlc += 1
            ok, where = unimodal(P)
            if not ok:
                notuni += 1
                if first is None:
                    first = (T, r, where, [str(x) for x in P[:4]])
                nz = [j for j, x in enumerate(P) if x]
                lo = nz[0]
                rest_ok = unimodal(P[lo + 1:])[0]
                if not (where == lo and P[lo] > P[lo + 1] < P[lo + 2] and rest_ok):
                    edge_only = False
                if T <= 64:
                    early = True
                if ELL[r + 1] == l + 1:
                    after_noncrit = False
                ratio = P[lo] / P[lo + 1] if P[lo + 1] else float('inf')
                if worst is None or ratio > worst[0]:
                    worst = (ratio, T, r)
            F = G
    print('laws %d, not log-concave %d, not unimodal %d' % (laws, notlc, notuni))
    print('DU-P1', 'HELD' if notuni == 0 else 'REFUTED')
    print('DU-P2', 'HELD' if (notuni == 0 or (edge_only and not early and after_noncrit)) else 'REFUTED',
          '(edge-only %s, any at T <= 64 %s, all after noncritical steps %s)' % (edge_only, early, after_noncrit))
    print('DU-C0', 'PASS' if (TMAX != 1024 or (laws == 524800 and notlc == 48727)) else 'FAIL')
    print('DU-C1', 'PASS' if c1 else 'FAIL')
    print('D1 first non-unimodal law:', first, '; largest P_0/P_1:', worst)


if __name__ == '__main__':
    main()
