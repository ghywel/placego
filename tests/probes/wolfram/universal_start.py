#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): the doubling word always begins 110110 once a period exceeds 2. Exhaustive proof check.

Every right diagonal of any row with a rightmost black cell obeys D_d(t+1) = D_d(t) XOR (D_(d-1)(t) OR D_(d-2)(t)),
with D_0 = 1, D_-1 = 0 and arbitrary start bits D_d(0) (8.27). Let j be the first diagonal with least period > 2. Its
feeders D_(j-1), D_(j-2) have least period <= 2 (by minimality), so each is one of 0, 1, 01, 10. Everything from D_j
up depends only on that pair and on the start bits of D_j, D_(j+1), ... Genuine pairs (hand): D_1 and D_2 always
alternate (their forcing is identically 1), so j >= 3; no diagonal d >= 1 is constant, so both feeders alternate;
and their OR has odd weight over 2 only if they are the SAME alternating sequence (opposite phases OR to 1, which
gives period 2). So the genuine pairs are (01, 01) and (10, 10). The script first enumerates all 16 pairs (a
superset, to show the restriction matters), then the genuine two, with all 2^7 start bits for D_j .. D_(j+6).
Claim: for genuine pairs, D_j .. D_(j+5) have periods 4, 8, 8, 16, 32, 32 in every case.
"""
import itertools, collections
def lp(s):
    n = len(s)
    while n > 1 and n % 2 == 0 and s[:n//2] == s[n//2:]: n //= 2
    return s[:n]
def step(p2, p1, bit):
    q = max(len(p1), len(p2))
    g = [p1[t % len(p1)] | p2[t % len(p2)] for t in range(q)]
    D = [bit]
    for t in range(q - 1): D.append(D[-1] ^ g[t])
    if sum(g) % 2: D = D + [1 - v for v in D]
    return lp(D)
base = [[0], [1], [0, 1], [1, 0]]
seen = collections.Counter(); cases = 0
for f2, f1 in itertools.product(base, base):
    for bits in itertools.product([0, 1], repeat=7):
        p2, p1 = f2, f1; pers = []
        for b in bits:
            D = step(p2, p1, b); pers.append(len(D)); p2, p1 = p1, D
        if pers[0] <= 2: continue
        cases += 1; seen[tuple(pers)] += 1
print("cases with period > 2 at D_j:", cases)
for k, v in seen.most_common(): print("  periods D_j..D_(j+6):", k, v)
print("all 16 pairs: prefix universal?", all(k[:6] == (4, 8, 8, 16, 32, 32) for k in seen))
gen = collections.Counter()
for f in ([0, 1], [1, 0]):
    for bits in itertools.product([0, 1], repeat=7):
        p2, p1 = f, f; pers = []
        for b in bits:
            D = step(p2, p1, b); pers.append(len(D)); p2, p1 = p1, D
        gen[tuple(pers)] += 1
for k, v in gen.most_common(): print("  genuine pairs, periods D_j..D_(j+6):", k, v)
ok = all(k[:6] == (4, 8, 8, 16, 32, 32) for k in gen)
print("CLAIM HOLDS FOR EVERY GENUINE CASE (256)" if ok else "CLAIM FAILS ON A GENUINE CASE")
