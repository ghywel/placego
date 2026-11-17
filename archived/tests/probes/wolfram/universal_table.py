#!/usr/bin/env python3
"""universal_table.py [J=53208] [LOG2T=16]: the universal strip generated from C_0 = C_1 = 1 by the reset recurrence alone,
and checked (Cloud, CL724, P-U1/P-U2). Wheel j's word is a function of time with period dividing 16; the child of
(C_(j-2), C_(j-1)) is the forced periodic solution after a black of C_(j-1) when C_(j-1) has a black, and the integrator
x(t+1) = C_(j-2)(t) XOR x(t) when C_(j-1) is white, with the single seed's phase read off its actual diagonal at one late
time T0 (the phase convention; either choice is a time shift of the strip). Reported: the white wheels below J, the weight of
the farther word over the common period L of the strip below, whether L is a period of every lower word, the doublings, the
first even-weight white wheel (the cut), the recurrence check at every wheel and phase, and the match of the seed's actual
row at t = 2^LOG2T with the strip on every wheel below its lag-16 band edge (control P-U2)."""
import sys, time
from math import gcd
J = int(sys.argv[1]) if len(sys.argv) > 1 else 53208
L2T = int(sys.argv[2]) if len(sys.argv) > 2 else 16
P = 16; T0 = 4096; T = 1 << L2T; K = 2 * T + 104; MASK = (1 << K) - 1
def step(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
t0 = time.time()
# the seed's actual rows at T0 (for the phase convention at white wheels) and at T, T + 16 (control)
V = 1; rowsT0 = []; rowT = rowT16 = None
for t in range(T + P + 1):
    if T0 <= t < T0 + P: rowsT0.append(V)
    if t == T: rowT = V
    if t == T + P: rowT16 = V
    V = step(V)
def seed_word(j):  # the seed's diagonal j over ticks T0 .. T0+15, as a 16-bit word, bit i = value at tick T0 + i
    return sum(((rowsT0[i] >> j) & 1) << i for i in range(P))
def lcm(a, b): return a * b // gcd(a, b)
def least_period(w):
    for p in (1, 2, 4, 8, 16):
        if all(((w >> i) & 1) == ((w >> ((i + p) % P)) & 1) for i in range(P)): return p
def bit(w, i): return (w >> (i % P)) & 1
C = [0xFFFF, 0xFFFF]  # C_0 = C_1 = 1 at every phase (the strip's base); phases are ticks mod 16 anchored at T0
white = []; doublings = []; cut = None; Lbelow = [1, 1]  # common period of wheels 0..j
for j in range(2, J):
    a, b = C[j - 2], C[j - 1]
    if b:  # nearer word has a black: forced solution from the black
        tb = next(i for i in range(P) if bit(b, i))
        x = [0] * P; x[(tb + 1) % P] = bit(a, tb) ^ 1
        for k in range(1, P):
            i = (tb + k) % P; x[(i + 1) % P] = bit(a, i) ^ (bit(b, i) | x[i])
        w = sum(x[i] << i for i in range(P))
        # the forced solution must be consistent (period 16 closes): check the recurrence at every phase below
    else:  # white nearer word: integrator; parity of a over the common period L of the strip below
        L = Lbelow[j - 2]; weight = sum(bit(a, i) for i in range(L))
        white.append((j - 1, L, weight))
        if weight % 2 == 0:
            cut = j; break
        x = [0] * P; x[0] = bit(seed_word(j), 0)  # the seed's phase
        for i in range(P - 1): x[i + 1] = bit(a, i) ^ x[i]
        w = sum(x[i] << i for i in range(P))
        doublings.append((j, L, 2 * L))
    C.append(w); Lbelow.append(lcm(Lbelow[j - 1], least_period(w)))
Jgen = len(C)
# recurrence check at every wheel and phase
bad = sum(1 for j in range(2, Jgen) for i in range(P) if bit(C[j], i + 1) != (bit(C[j - 2], i) ^ (bit(C[j - 1], i) | bit(C[j], i))))
print(f"strip generated to wheel {Jgen - 1} (requested below {J}); recurrence violations over all wheels and phases: {bad}")
print(f"white wheels (wheel, common period L of the strip below, farther weight over L): {white}")
print(f"doublings (child wheel, L, new period): {doublings}; strip period below the cut: {Lbelow[-1]}")
print(f"first even-weight white wheel: {white[-1][0] if cut else None}; cut (first forked child) = {cut}")
Lcheck = all(all(least_period(C[k]) and L % least_period(C[k]) == 0 for k in range(0, wj)) for wj, L, _ in white)
print(f"at every white wheel, L is a period of every lower word: {Lcheck}")
# control: the seed's actual row at T against the strip at phase (T - T0) mod 16, below its lag-16 band edge
x = rowT ^ rowT16; B = (x & -x).bit_length() - 1
ph = (T - T0) % P
mism = [j for j in range(min(B, Jgen)) if ((rowT >> j) & 1) != bit(C[j], ph)]
print(f"control: seed row at t = {T}, lag-16 band edge B = {B}; wheels below min(B, {Jgen}) disagreeing with the strip at phase {ph}: {len(mism)} {mism[:5]}")
print(f"total {time.time() - t0:.1f} s")
print("UNIVERSAL_TABLE_DONE")
