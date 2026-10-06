#!/usr/bin/env python3
"""collatz_audit_g93_g94.py: Local's second reading of GPT's G94 (demand log-concavity needs one absorbing-edge
inequality) and of G93's finite outcome, and the search GPT asked for in G081: does the ACTUAL threshold schedule ever
break log-concavity, beyond G93's horizon 64? Exact integers. (Local, 2026-10-06; PROOFS.md notes; chat.)

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/prizes/collatz_audit_g93_g94.py [TMAX=1024]
COST:       a few minutes at TMAX = 1024 on one core (about 10^8 big-integer operations).

The demand law. ell_t = least a with 3^a > 2^t; f_T(a) = [a >= ell_T]; f_r(a) = (f_(r+1)(a) + f_(r+1)(a+1))/2 for
a >= ell_r and 0 below. Scaled by 2^(T-r), F_r(a) = F_(r+1)(a) + F_(r+1)(a+1) are integers. The demand atoms at time r
are P_j = F_r(ell_r + j) - F_r(ell_r + j - 1), j >= 0; the law is log-concave when P_j^2 >= P_(j-1) P_(j+1) for all j
and the support has no internal zero. A step r -> r+1 is critical when ell_(r+1) = ell_r + 1 (then q_0 = 0).

CHECKS, written 2026-10-06 before this script's first run. A smoke at TMAX = 64 checked E0, E2 and E3 and also
printed D1 for T <= 64 (least slack 1.0086, at T = 64, r = 8: close to 1), which was seen before the push; E1 was
written before the smoke and is left unchanged. Nothing beyond horizon 64 was computed before these were pushed.
  E0 (consistency with G93's DS1, not blind): the 2,080 profiles with T <= 64 are all log-concave.
  E1 (blind): every demand law with T <= TMAX and 0 <= r < T is log-concave, with no internal zero.
  E2 (G94's operator, exact): at every step for T <= 64, p_0 = q_0 + q_1/2 and p_j = (q_j + q_(j+1))/2 (scaled),
     with q measured from ell_r, and q_0 = 0 exactly at critical steps.
  E3 (G94's guards): the uniform four-atom law gives (3/8, 1/4, 1/4, 1/8), which is not log-concave, and the edge
     inequality fails for it (1/4 < 3/8); with q_0 = 0 (critical) the edge inequality holds for it.
  D1 (descriptive): the least normalized slack of the edge inequality (q_1 + q_2)^2 / ((2 q_0 + q_1)(q_2 + q_3)) over
     the noncritical steps, and where it occurs.
"""
import sys
from fractions import Fraction as Fr

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


ELL = []
a = 0
for t in range(TMAX + 2):
    while 3 ** a <= 2 ** t:
        a += 1
    ELL.append(a)
# ell_0 is 1 under the strict definition (3^0 = 2^0); G74 uses ellf(0) = 0, every start alive at time 0
ELL[0] = 0
assert ELL[:7] == [0, 1, 2, 2, 3, 4, 4]


def atoms(F, l, top):
    return [F[l + j] - (F[l + j - 1] if l + j - 1 >= 0 else 0) for j in range(top - l + 1)]


def logconcave(P):
    # support: strip leading and trailing zeros; no internal zero; P_j^2 >= P_(j-1) P_(j+1)
    nz = [j for j, x in enumerate(P) if x]
    if not nz:
        return True, None
    lo, hi = nz[0], nz[-1]
    for j in range(lo, hi + 1):
        if P[j] == 0:
            return False, ('gap', j)
    for j in range(lo + 1, hi):
        if P[j] * P[j] < P[j - 1] * P[j + 1]:
            return False, ('triple', j)
    return True, None


profiles = viol = 0
first_violation = None
e0_ok = True
e2_ok = True
crit_q0 = True
best = None
for T in range(1, TMAX + 1):
    top = ELL[T] + 1
    F = [1 if x >= ELL[T] else 0 for x in range(top + 2)]     # time T, scale 2^0
    prevF = None
    for r in range(T - 1, -1, -1):
        l = ELL[r]
        G = [0] * (top + 2)
        for x in range(l, top + 1):
            G[x] = F[x] + F[x + 1] if x + 1 < len(F) else F[x] + 1
        # beyond top every f is 1 (scaled 2^(T-r)); keep the array long enough
        G[top + 1] = 2 ** (T - r)
        P = atoms(G, l, top + 1)
        ok, why = logconcave(P)
        profiles += 1
        if not ok:
            viol += 1
            if first_violation is None:
                first_violation = (T, r, why)
            if T <= 64:
                e0_ok = False
        # G94's operator and the edge inequality, using q from time r+1 measured from l
        q = [F[l + j] - (F[l + j - 1] if l + j - 1 >= 0 else 0) for j in range(top + 1 - l + 1)]
        critical = ELL[r + 1] == l + 1
        if critical and q[0] != 0:
            crit_q0 = False
        if T <= 64:
            p_scaled = [2 * q[0] + q[1]] + [q[j] + q[j + 1] if j + 1 < len(q) else q[j] for j in range(1, len(q))]
            if [x for x in p_scaled] != P[:len(p_scaled)]:
                e2_ok = False
        if not critical and len(q) >= 4 and (2 * q[0] + q[1]) * (q[2] + q[3]) > 0:
            slack = Fr((q[1] + q[2]) ** 2, (2 * q[0] + q[1]) * (q[2] + q[3]))
            if best is None or slack < best[0]:
                best = (slack, T, r)
        F = G
    if T == 64:
        check('E0 the 2,080 profiles with T <= 64 are all log-concave (G93 DS1)', e0_ok and profiles == 2080,
              '%d profiles' % profiles)
check('E1 every demand law log-concave, T <= %d' % TMAX, viol == 0,
      '%d profiles, %d violations, first %s' % (profiles, viol, first_violation))
check('E2 G94 operator reproduces each preceding law (T <= 64); q_0 = 0 exactly at critical steps', e2_ok and crit_q0)
q = [Fr(1, 4)] * 4
p = [q[0] + q[1] / 2, (q[1] + q[2]) / 2, (q[2] + q[3]) / 2, q[3] / 2]
edge = lambda q: (q[1] + q[2]) ** 2 >= (2 * q[0] + q[1]) * (q[2] + q[3])
check('E3 synthetic guard', p == [Fr(3, 8), Fr(1, 4), Fr(1, 4), Fr(1, 8)] and p[1] ** 2 < p[0] * p[2] and not edge(q)
      and (q[1] + q[2]) ** 2 == Fr(1, 4) and (2 * q[0] + q[1]) * (q[2] + q[3]) == Fr(3, 8) and edge([0] + q[1:]))
if best:
    print('D1 least edge slack over noncritical steps: %.6f at T = %d, r = %d' % (float(best[0]), best[1], best[2]))
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
