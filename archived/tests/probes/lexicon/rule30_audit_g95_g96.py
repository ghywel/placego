#!/usr/bin/env python3
"""rule30_audit_g95_g96.py: Local's second reading of GPT's G95 (the barrier has isolated flat steps; the unrestricted
counterexample 00011) and G96 (fixed-cell change and moving-frame change are different observables), independent of
GPT's NS1 and MC1-MC2. Exact; every ring state. (Local, 2026-10-06; PROOFS.md notes; chat.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g95_g96.py      (seconds)

CHECKS (GPT's claims at 588c530 and e2c6a02):
  B1 (G95): ell_r = ceil(beta r), increments in {0, 1}, no two consecutive zero increments, for r <= 10,000.
  B2 (G95): the schedule 00011 gives the demand law (26, 5, 1)/32 by full enumeration, and 5^2 < 26.
  V1 (G96): on every ring of widths 3 to 12, for v = -1, 0, 1 and every state: the pulled-back step
     z_(t+1) = Q^v F(z_t) agrees with the literal Rule 30 evolution read along the frame; at v = 0, F(x) XOR x = R210(x).
  V2 (Local's §8.70 second addendum, for G086): the right-step identity F(x)(i+1) XOR x(i) = x(i+1) OR x(i+2) on every
     ring state of widths 3 to 12.
  V3 (G96's guards): u_0 = {-1, 1}, u_1 = {-2, 0, 1, 2}, R210(u_0) = {-2, 2}; the pulse's fixed-cell samples 1, 0, 0
     have second difference 1 (real and GF(2)), and along i = t every difference is 0; D_v^(2^k) = 1 + S^(2^k) Q^(v 2^k)
     on a random history for k <= 3, v = -1, 0, 1.
"""
import math
import random

fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


beta = math.log(2) / math.log(3)
ell = []
a = 0
for r in range(10001):
    while 3 ** a <= 2 ** r:
        a += 1
    ell.append(a)
ell[0] = 0
inc = [ell[r + 1] - ell[r] for r in range(10000)]
check('B1 ell_r = ceil(beta r), increments 0/1, no two consecutive zeros (r <= 10,000)',
      all(ell[r] == math.ceil(beta * r) for r in range(1, 10001)) and set(inc) <= {0, 1} and
      not any(inc[r] == 0 and inc[r + 1] == 0 for r in range(9999)))
d = [0, 0, 0, 1, 1]
law = [0, 0, 0]
for s in range(32):
    Z = [0]
    for i in range(5):
        Z.append(Z[-1] + ((s >> i) & 1))
    b = [0]
    for x in d:
        b.append(b[-1] + x)
    J = max(b[k] - Z[k] for k in range(6))
    law[J] += 1
check('B2 00011 law (26, 5, 1)/32, not log-concave', law == [26, 5, 1] and law[1] ** 2 < law[0] * law[2], str(law))

R30 = lambda l, c, r: l ^ (c | r)
R210 = lambda l, c, r: (210 >> (l << 2 | c << 1 | r)) & 1


def F(x):
    n = len(x)
    return [R30(x[i - 1], x[i], x[(i + 1) % n]) for i in range(n)]


ok1 = ok2 = ok210 = True
for n in range(3, 13):
    for s in range(2 ** n):
        x = [(s >> i) & 1 for i in range(n)]
        fx = F(x)
        if any(fx[i] ^ x[i] != R210(x[i - 1], x[i], x[(i + 1) % n]) for i in range(n)):
            ok210 = False
        if any(fx[(i + 1) % n] ^ x[i] != (x[(i + 1) % n] | x[(i + 2) % n]) for i in range(n)):
            ok2 = False
        # the frame: z_t(j) = x_t(j + v t); one step from z_0 = x at t = 0
        for v in (-1, 0, 1):
            z1 = [fx[(j + v) % n] for j in range(n)]                    # Q^v F(z_0)
            lit = [F(x)[(j + v * 1) % n] for j in range(n)]              # x_1(j + v) read along the frame
            if z1 != lit:
                ok1 = False
        # two steps, to exercise t > 0: z_2(j) = x_2(j + 2v) and Q^v F(z_1)
        for v in (-1, 0, 1):
            z1 = [fx[(j + v) % n] for j in range(n)]
            z2 = [F(z1)[(j + v) % n] for j in range(n)]
            x2 = F(fx)
            if z2 != [x2[(j + 2 * v) % n] for j in range(n)]:
                ok1 = False
check('V1 pulled-back frame step equals the literal evolution (widths 3..12, v = -1, 0, 1, two steps)', ok1)
check('V1 at v = 0, F(x) XOR x = R210(x) on every ring state', ok210)
check('V2 right-step identity F(x)(i+1) XOR x(i) = x(i+1) OR x(i+2) on every ring state', ok2)


def Fline(black, lo, hi):
    return {i for i in range(lo, hi + 1) if R30(int(i - 1 in black), int(i in black), int(i + 1 in black))}


x0 = {0}
x1 = Fline(x0, -5, 5)
x2 = Fline(x1, -5, 5)
u0 = x1 ^ x0
u1 = x2 ^ x1
r210u0 = {i for i in range(-5, 6) if R210(int(i - 1 in u0), int(i in u0), int(i + 1 in u0))}
pulse = lambda t, i: int(i == t)
fixed = [pulse(t, 0) for t in range(3)]
ok3 = (x1 == {-1, 0, 1} and x2 == {-2, -1, 2} and u0 == {-1, 1} and u1 == {-2, 0, 1, 2} and r210u0 == {-2, 2}
       and fixed == [1, 0, 0] and fixed[0] - 2 * fixed[1] + fixed[2] == 1 and fixed[0] ^ fixed[2] == 1
       and all(pulse(t + 1, t + 1) ^ pulse(t, t) == 0 for t in range(10)))
rng = random.Random(96)
H = {(t, i): rng.randint(0, 1) for t in range(20) for i in range(-40, 41)}
for v in (-1, 0, 1):
    for k in range(4):
        m = 2 ** k
        # apply D_v m times literally, and compare with 1 + S^m Q^(v m)
        cur = dict(H)
        for _ in range(m):
            cur = {(t, i): cur[(t + 1, i + v)] ^ cur[(t, i)] for (t, i) in cur if (t + 1, i + v) in cur}
        ok3 &= all(cur[(t, i)] == H[(t + m, i + v * m)] ^ H[(t, i)] for (t, i) in cur)
check('V3 G96 guards: u_0, u_1, R210(u_0); the pulse; the dyadic worldline identity for k <= 3', ok3)
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
