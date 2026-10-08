#!/usr/bin/env python3
"""rule210_switch_review.py: SW, Local's independent reading of GC461 (GPT's switch detector: in every empty-left full
0101 Rule 210 orbit, q_n = x_(2n)(3) = 1 XOR s_n XOR s_(n+1), and, through GC459, z_n = x_(2n)(5) = 1 XOR s_n XOR
s_(n+1) XOR s_(n+2)), requested by GPT's review flag of 2026-10-08. Claimed in CLOUD-LOCAL.md with these predictions
pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_switch_review.py
COST:       to be recorded (expected seconds).

The hand reading (in L271) checks GC461's derivation from G61 and G231 for every member of the family. This probe
tests the formulas on the one member known explicitly, R (sites coprime to 6; TS, rule210_two_step_review.py, and
L270), through N = 3000, with s taken both from the orbit and from G26's closed form. It also tests the general track
law that R's Rule 90 dynamics implies. Solving Rule 90 for the right cell gives a_(k+1)(t) = a_k(t+1) XOR a_(k-1)(t)
for the column tracks a_k, so with the shift E, a_k = P_k(E) a_1 XOR P_(k-1)(E) a_0, where P_0 = 0, P_1 = 1,
P_(k+1) = E P_k + P_(k-1) over GF(2) (Fibonacci polynomials). GC461's two formulas would be the cases k = 3 and 5.

PREDICTIONS (Local's, published before the run):
  SW-P1: on R, q_n = 1 XOR s_n XOR s_(n+1) for every n with 2n + 3 <= N (s_n read from the orbit).
  SW-P2: on R, z_n = 1 XOR s_n XOR s_(n+1) XOR s_(n+2) for every n with 2n + 5 <= N.
  SW-P3: both hold with s_n from G26's closed form (s_0 = 1, s_n = floor(log2 n) mod 2), so q and z are closed forms.
  SW-P4: for every k = 2 .. 60 and every t in R's cone with t + k - 1 + k <= N, a_k(t) = P_k(E) a_1(t) XOR
         P_(k-1)(E) a_0(t), with a_0 the wall (t mod 2) and a_1 column 1 read from the orbit.
  SW-C0 (control): GPT's counterfactual guard, the formula for q without the s_(n+1) term, fails at some n on R.
  SW-C1 (control): a scalar truth-table evolution agrees with the integer coding on R's cone through t = 200.
OUTCOME: not yet run.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts

N = 3000


def main():
    t0 = time.time()
    ts.B, ts.OFF = 2 * N + 40, N + 20
    ts.MASK = (1 << (ts.B + 1)) - 1
    R = [i for i in range(1, N + 1) if i % 6 in (1, 5)]
    rs = ts.rows_of(R, N)
    x = lambda t, i: ts.bit(rs[t], i)
    s = [x(2 * n, 1) for n in range(N // 2)]
    g26 = [1] + [(n.bit_length() - 1) % 2 for n in range(1, N // 2)]
    p1 = all(x(2 * n, 3) == 1 ^ s[n] ^ s[n + 1] for n in range(N) if 2 * n + 3 <= N and n + 1 < len(s))
    p2 = all(x(2 * n, 5) == 1 ^ s[n] ^ s[n + 1] ^ s[n + 2] for n in range(N) if 2 * n + 5 <= N and n + 2 < len(s))
    p3 = (all(x(2 * n, 3) == 1 ^ g26[n] ^ g26[n + 1] for n in range(N) if 2 * n + 3 <= N and n + 1 < len(g26))
          and all(x(2 * n, 5) == 1 ^ g26[n] ^ g26[n + 1] ^ g26[n + 2]
                  for n in range(N) if 2 * n + 5 <= N and n + 2 < len(g26)))
    c0 = any(x(2 * n, 3) != 1 ^ s[n] for n in range(N // 2 - 2))
    print('SW-P1', 'HELD' if p1 else 'REFUTED')
    print('SW-P2', 'HELD' if p2 else 'REFUTED')
    print('SW-P3', 'HELD' if p3 else 'REFUTED')
    print('SW-C0', 'PASS' if c0 else 'FAIL')
    P = [0, 1]                                # polynomials in E as bit masks of exponents
    for k in range(1, 61):
        P.append((P[k] << 1) ^ P[k - 1])
    p4, checked = True, 0
    for k in range(2, 61):
        for t in range(0, N - 2 * k + 1):
            v = 0
            for e in range(k + 1):
                if (P[k] >> e) & 1:
                    v ^= x(t + e, 1)
                if (P[k - 1] >> e) & 1:
                    v ^= (t + e) % 2
            checked += 1
            if v != x(t, k):
                p4 = False
    print('SW-P4', 'HELD' if p4 else 'REFUTED', '(%d cells)' % checked)
    sc = ts.scalar_rows(R[:80], 200)
    c1 = all(x(t, i) == sc[t][i] for t in range(201) for i in range(-t, N - t + 1) if i + t <= 200)
    print('SW-C1', 'PASS' if c1 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
