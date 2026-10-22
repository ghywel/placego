#!/usr/bin/env python3
"""All primitive 120-degree triples (m<MMAX) with ab = N*square for several primes N; for each, side L=sqrt(N ab):
enumerate decompositions n_a a + n_b b + n_c c = L and corner configurations (alpha-tile end in {b,c},
beta-tile end in {a,c} at each corner; a one-edge side must be c). Prediction: every triple fails.
Counterfactual: a triple with a surviving corner configuration (corner test alone would not close the case)."""
import math, itertools, time
T0 = time.time()
MMAX = 5000
PR = [19, 23, 47, 71, 191, 5, 13, 17, 29, 37]
found = []
for m in range(2, MMAX):
    if time.time() - T0 > 420: print("time limit at m", m); break
    mm = m * m
    for n in range(1, m):
        if (m - n) % 3 == 0 or math.gcd(m, n) != 1: continue
        a, b = mm - n * n, 2 * m * n + n * n
        ab = a * b
        for p in PR:
            if ab % p == 0:
                q = ab // p
                r = math.isqrt(q)
                if r * r == q:
                    found.append((p, a, b, mm + m * n + n * n))
ALPHA, BETA = {'b', 'c'}, {'a', 'c'}
def analyse(a, b, c, L):
    decs = []
    for nc in range(L // c + 1):
        for nb in range((L - nc * c) // b + 1):
            r = L - nc * c - nb * b
            if r % a == 0: decs.append((r // a, nb, nc))
    opts = set()
    for d in decs:
        names = ['a'] * d[0] + ['b'] * d[1] + ['c'] * d[2]
        if len(names) == 1:
            if names[0] == 'c': opts.add(('c', 'c'))
            continue
        for i, j in itertools.permutations(range(len(names)), 2):
            opts.add((names[i], names[j]))
    surv = 0
    for s0, s1, s2 in itertools.product(opts, repeat=3):
        if all((u in ALPHA and v in BETA) or (u in BETA and v in ALPHA)
               for (u, v) in ((s0[1], s1[0]), (s1[1], s2[0]), (s2[1], s0[0]))):
            surv += 1
    return decs, surv
for p, a, b, c in found:
    L = math.isqrt(p * a * b); assert L * L == p * a * b
    for (A, B) in ((a, b), (b, a)):
        pass
    decs, surv = analyse(a, b, c, L)
    print(f"N={p}: tile {(a, b, c)}, L={L}: decompositions {decs}; surviving corner configs {surv}")
print(f"done {time.time()-T0:.1f}s, triples {len(found)}")
