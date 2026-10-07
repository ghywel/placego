#!/usr/bin/env python3
"""rule30_tm6_backward.py: TM6-B, an independent backward certificate for Proposition 9's minimizing history (PROOFS.md
entry 22). Local's check, claimed in CLOUD-LOCAL.md with these predictions pushed before the script was run.

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_tm6_backward.py
COST:       about a minute expected (about 6.6 x 10^7 steps of three bit operations each); cap 900 CPU s.

Method. Solving the compatibility equation S z = x XOR (y OR z) for its first profile gives the backward pair map
B(y, z) = (S z XOR (y OR z), y), which sends the literal state at depth d, (w_(d-1), w_d), to the state at depth d - 1.
It is deterministic and uses neither the forward child constructor nor TM6's C kernel. Start from the exit state that
TM6 (and TM6b) printed for the minimum, (a, 0) at depth 65,821,412 with a = 3,864,731,681 (32-bit, time 0 in the low
bit), in TM6's absolute frame, and apply B that many times.

PREDICTIONS, Local's, published before the run:
  BK-P1: after exactly 65,821,412 steps the state is the root (0, 1^32), and one more step gives (0, 0), as FBR16 found
         for its witness.
  BK-P2: the zero drivers met (states (x, 0)), the starting exit at 65,821,412 included, are exactly at depths
         65,821,412, 667,051, 537,692, 485,619, 445,474,
         350,243, 243,767, 174,449, 165,748, 72,575, 53,207, 399, 28, 7, 2: this history's events in Proposition 8
         (TM5b's history exiting period 16 at 667,051), the doublings below 400, and nothing between 667,052 and the
         exit.
  BK-C1 (control): the exit driver a has odd parity over 32 bits, and every other zero driver met has even parity.
  BK-CF (counterfactual): flipping one bit of a (bit 0) gives a start state whose backward walk does not reach the root
         at depth 0, so the landing is not automatic.
OUTCOME: not yet run.
"""
import resource
import sys

Q, FULL = 32, (1 << 32) - 1
DEPTH, A = 65821412, 3864731681
EXPECT = [65821412, 667051, 537692, 485619, 445474, 350243, 243767, 174449, 165748, 72575, 53207, 399, 28, 7, 2]


def back(y, z, steps):
    zeros = []
    d = steps
    for _ in range(steps):
        if z == 0:
            zeros.append((d, y))
        y, z = (((z >> 1) | (z << 31)) & FULL) ^ (y | z), y
        d -= 1
    return y, z, zeros


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


y, z, zeros = back(A, 0, DEPTH)
p1 = (y, z) == (0, FULL)
y2, z2, _ = back(y, z, 1)
p1 &= (y2, z2) == (0, 0)
print('BK-P1', 'HELD' if p1 else 'REFUTED', '(state at depth 0: %d, %d)' % (y, z))
depths = [d for d, _ in zeros]
p2 = depths == EXPECT
print('BK-P2', 'HELD' if p2 else 'REFUTED', depths)
par = lambda u: bin(u).count('1') & 1
c1 = par(A) == 1 and all(par(x) == 0 for d, x in zeros if d != DEPTH)
print('BK-C1', 'PASS' if c1 else 'FAIL', '(the exit driver itself is the first zero, at %d)' % zeros[0][0] if zeros else '')
yc, zc, _ = back(A ^ 1, 0, DEPTH)
cf = (yc, zc) != (0, FULL)
print('BK-CF', 'PASS' if cf else 'FAIL')
print('CPU %.1f s' % cpu())
if cpu() > 900:
    print('CAP EXCEEDED')
    sys.exit(1)
