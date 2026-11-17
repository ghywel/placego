#!/usr/bin/env python3
"""Equilateral ABC, 120-degree tile with integer sides, prime N=19 witness: (a,b,c)=(272^2, 19*105^2, 254659),
L=19*272*105.  Enumerate side decompositions n_a a + n_b b + n_c c = L, then all corner configurations:
each corner has one alpha-tile (its b- or c-side on one side of ABC) and one beta-tile (a- or c-side on the other).
A one-edge side must be a c-edge (c joins the alpha- and beta-vertices). Prediction: some configuration survives
(the corner test alone does not close the integer-c case)."""
import itertools
a, b, c = 272**2, 19 * 105**2, 254659
assert a*a + a*b + b*b == c*c
L = 19 * 272 * 105
assert L*L == 19*a*b
decs = []
for nc in range(L // c + 1):
    for nb in range((L - nc*c) // b + 1):
        r = L - nc*c - nb*b
        if r % a == 0:
            decs.append((r // a, nb, nc))
print("L =", L, " decompositions (n_a, n_b, n_c):", decs)
E = {'a': 0, 'b': 1, 'c': 2}
def ends(dec):
    """possible (first, last) end-edge pairs for a side with this multiset"""
    names = ['a'] * dec[0] + ['b'] * dec[1] + ['c'] * dec[2]
    out = set()
    if len(names) == 1:
        if names[0] == 'c': out.add(('c', 'c', True))
        return out
    for i, j in itertools.permutations(range(len(names)), 2):
        out.add((names[i], names[j], False))
    return out
side_opts = set()
for d in decs:
    for e in ends(d):
        side_opts.add((d, e))
ALPHA, BETA = {'b', 'c'}, {'a', 'c'}
surv = []
# sides: S0 = P->Q, S1 = Q->R, S2 = R->P ; first end at the start corner, last end at the end corner
for s0, s1, s2 in itertools.product(side_opts, repeat=3):
    ok = True
    # corner Q: last of S0, first of S1 ; corner R: last of S1, first of S2 ; corner P: last of S2, first of S0
    for (u, v) in ((s0[1][1], s1[1][0]), (s1[1][1], s2[1][0]), (s2[1][1], s0[1][0])):
        if not ((u in ALPHA and v in BETA) or (u in BETA and v in ALPHA)):
            ok = False; break
    if ok:
        surv.append((s0, s1, s2))
print("surviving corner configurations:", len(surv))
for x in surv[:6]:
    print("  ", x)
