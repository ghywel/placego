#!/usr/bin/env python3
"""collatz_audit_g91_g92.py: Local's second reading of GPT's G91 (same-label one-step coalescence: the exact grouped
form of the backward-weight increment) and G92 (the coarse curvature bootstrap grows like log d), independent of GPT's
CM1-CM2 controls. Exact rationals; direct trajectories. (Local, 2026-10-06; PROOFS.md notes; chat.)

COMMAND:    python3 tests/probes/prizes/collatz_audit_g91_g92.py      (under a minute)

CHECKS (GPT's claims at 8e6dfee and 4a0d98f):
  M1 (G91's identity): for widths 2..12 and horizons T = m..m+12 (m = w - 1), at every time t, the literal increment
     H_(t+1) - H_t (H_t = sum of f_t(a) over the admitted occurrences at time t, failed children weighing 0) equals the
     grouped sum (1/2) sum_(y,b) [M (Delta(b-1) - Delta(b)) + (O - M) Delta(b-1) - (E - M) Delta(b)].
  M2 (G91): every matched child is admitted; dropping failed children breaks the identity somewhere (must be seen).
  M3 (G91's guard): width 2, T = 4, t = 3: start 3 is at state 4 with odd count 2; its even child fails; Delta_3(2) = 1.
  M4 (G92): c(h) >= min(1/2, 2/h) for h = 1..10,000, and (1/2) sum_(h=0)^(d-1) c(h) >= log(d/4) for d = 5..10,000
     (the bootstrap coefficient with Q_w(t)/Q_w(T) >= 1); c(1) = 1/2.
  M5 (G92's guard): the G90 pair at T = 35: weights at time 34 for counts 21, 22, 23 are 0, 1/2, 1; Delta_33(21) =
     Delta_33(22) = 1/2 (the matched contribution is 0); the common state at time 34 is even and fails the barrier at 35.
  D1 (descriptive, no prediction): the share of admitted parent occurrences that are matched, by width, at T = m + 12.
"""
import math
from fractions import Fraction as Fr

fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


def ellf(j):
    return 0 if j == 0 else next(a for a in range(j + 1) if 3 ** a > 2 ** j)


def weights(T):
    f = {T: {a: Fr(1) if a >= ellf(T) else Fr(0) for a in range(0, T + 2)}}
    for t in range(T - 1, -1, -1):
        f[t] = {a: Fr(0) if a < ellf(t) else (f[t + 1][a] + f[t + 1].get(a + 1, Fr(1))) / 2 for a in range(0, T + 2)}
    return f


def step(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


n1 = 0
broke_if_dropped = False
matched_children_admitted = True
share = {}
for w in range(2, 13):
    m = w - 1
    for T in range(m, m + 13):
        f = weights(T)
        occ = [(n, 0) for n in range(2 ** m, 2 ** w)]         # admitted occurrences (state, odd count) at time t
        for t in range(T):
            D = lambda a: f[t + 1].get(a + 1, Fr(1)) - f[t + 1].get(a, Fr(0))
            H_t = sum(f[t][a] for _, a in occ)
            O, E = {}, {}
            children = []
            for x, a in occ:
                y, b = step(x), a + (x & 1)
                (O if x & 1 else E)[(y, b)] = (O if x & 1 else E).get((y, b), 0) + 1
                children.append((y, b))
            H_next_all = sum(f[t + 1][b] for _, b in children)  # failed children weigh f_(t+1)(b) = 0
            grouped = Fr(0)
            for key in set(O) | set(E):
                y, b = key
                o, e = O.get(key, 0), E.get(key, 0)
                M = min(o, e)
                grouped += Fr(1, 2) * (M * (D(b - 1) - D(b)) + (o - M) * D(b - 1) - (e - M) * D(b))
                if M and 3 ** b < 2 ** (t + 1):
                    matched_children_admitted = False
            if H_next_all - H_t != grouped:
                fails.append('M1 w=%d T=%d t=%d' % (w, T, t))
            # the counterfactual: group only the surviving children
            surv = Fr(0)
            for key in set(O) | set(E):
                y, b = key
                if 3 ** b < 2 ** (t + 1):
                    continue
                o, e = O.get(key, 0), E.get(key, 0)
                M = min(o, e)
                surv += Fr(1, 2) * (M * (D(b - 1) - D(b)) + (o - M) * D(b - 1) - (e - M) * D(b))
            if surv != H_next_all - H_t:
                broke_if_dropped = True
            if T == m + 12 and t >= m:
                tot = len(occ)
                mt = 2 * sum(min(O.get(k, 0), E.get(k, 0)) for k in set(O) | set(E))
                s = share.setdefault(w, [0, 0])
                s[0] += mt
                s[1] += tot
            occ = [(y, b) for y, b in children if 3 ** b >= 2 ** (t + 1)]
            n1 += 1
check('M1 literal increment = grouped matched/unmatched sum', not any(x.startswith('M1') for x in fails),
      '%d (w, T, t) steps' % n1)
check('M2 every matched child admitted', matched_children_admitted)
check('M2 dropping failed children breaks the identity somewhere (counterfactual seen)', broke_if_dropped)
# M3
f4 = weights(4)
x, a, path = 3, 0, []
for t in range(3):
    a += x & 1
    x = step(x)
check('M3 lost-child guard', x == 4 and a == 2 and 3 ** 2 < 2 ** 4 and f4[4][3] - f4[4][2] == 1)
# M4
def c(h):
    if h == 0:
        return 0.5
    return min(0.5, min(2 / (h - K + 1) + min(1.0, 64 * math.exp(-K / 32)) for K in range(1, h + 1)))
cs = [c(h) for h in range(0, 10001)]
ok4 = all(cs[h] >= min(0.5, 2 / h) - 1e-15 for h in range(1, 10001)) and cs[1] == 0.5
run = 0.0
for d in range(1, 10001):
    run += cs[d - 1]
    if d >= 5:
        ok4 &= 0.5 * run >= math.log(d / 4)
check('M4 c(h) >= min(1/2, 2/h); bootstrap coefficient >= log(d/4) for d <= 10,000', ok4,
      'coefficient at d = 10,000: %.3f vs log(2500) = %.3f' % (0.5 * run, math.log(2500)))
# M5
f35 = weights(35)
x1, x2, a1, a2 = 11843133435, 11843133439, 0, 0
for t in range(34):
    a1 += x1 & 1
    a2 += x2 & 1
    x1, x2 = step(x1), step(x2)
ok5 = (f35[34][21], f35[34][22], f35[34][23]) == (0, Fr(1, 2), 1)
ok5 &= f35[34][22] - f35[34][21] == Fr(1, 2) and f35[34][23] - f35[34][22] == Fr(1, 2)
ok5 &= x1 == x2 and x1 % 2 == 0 and a1 == a2 == 22 and 3 ** 22 < 2 ** 35 and ellf(34) == 22 and ellf(35) == 23
check('M5 G92 zero-contribution guard', ok5)
print('D1 share of admitted parent occurrences in matched pairs at T = m + 12 (t >= m):',
      {w: round(s[0] / s[1], 4) for w, s in share.items() if s[1]})
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails[:10]))
