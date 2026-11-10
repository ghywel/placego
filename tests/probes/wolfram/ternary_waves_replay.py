#!/usr/bin/env python3
"""ternary_waves_replay.py (Local, 10 November 2026; S-22, Cloud's K-04 with K-09a): the plain-Python replay of the
worked-numbers cell of the ternary travelling-waves essay. Usage: python3 ternary_waves_replay.py

The profile lists are the module's (Rule30TernaryWaves.profiles12 and profiles15, the literal tiles of GPT's GC2830
and GC2848 evidence): bit t of entry r of tile a is the cell at offset r, phase t. Written independently of the Lean
module: the seams are checked in the moving frame x(i, t+1) = x(i) xor (x(i+1) or x(i+2)), and the rings are evolved
by ordinary rule 30 on a cycle, x(i, t+1) = x(i-1) xor (x(i) or x(i+1)).

Prediction (written before the first run, from GC2848's 39-ring control at period 15 and GC2830's 3672 seams): all
3672 and 4185 seam identities hold; every ring made of one to three tiles (3 + 9 + 27 = 39 per period) returns under
ordinary rule 30 to itself moved P cells right after P ticks, and at no tick d in 1..P-1 to itself moved d cells;
the decoder cells at offsets (20, 23) and (6, 23) read (0,1), (0,0), (1,0) and (1,1), (0,0), (1,0).
Counterfactual: a mismatch refutes the certificate data or the essay's description of it.
It prints {seams at 12, seams at 15, rings at 12, rings at 15, decoder pairs at 12, decoder pairs at 15}."""
from itertools import product

P12 = [[2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389,
        1493, 1323, 2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323],
       [2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389,
        1493, 1327, 2864, 3240, 2728, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323],
       [2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323, 2868, 3242, 2734, 2769,
        1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323]]
P15 = [[5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707,
        22058, 21802, 11581, 21154, 11171, 23122, 26226, 5451, 21834, 24238, 8553, 20889, 12629, 10581, 27050],
       [5461, 23930, 21125, 13126, 10949, 10917, 21926, 10837, 30069, 2890, 3277, 2731, 19114, 20310, 10409, 26837,
        5293, 7347, 21194, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717],
       [5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707,
        22058, 21802, 11573, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717]]


def seams(prof, L, P):
    cell = lambda a, r, t: (prof[a][r] >> (t % P)) & 1
    ok = 0
    for a, b in product(range(3), repeat=2):
        row = lambda r, t: cell(a, r, t) if r < L else cell(b, r - L, t)
        for r in range(L):
            for t in range(P):
                ok += cell(a, r, t + 1) == row(r, t) ^ (row(r + 1, t) | row(r + 2, t))
    return ok


def rings(prof, L, P):
    ok = 0
    for k in (1, 2, 3):
        for w in product(range(3), repeat=k):
            x = [(prof[w[i // L]][i % L]) & 1 for i in range(L * k)]
            n, y, good = len(x), x, True
            for d in range(1, P + 1):
                y = [y[i - 1] ^ (y[i] | y[(i + 1) % n]) for i in range(n)]
                back = all(y[(i + d) % n] == x[i] for i in range(n))
                good &= back if d == P else not back
            ok += good
    return ok


dec = lambda prof, o1, o2: '{' + ', '.join('{%d, %d}' % (prof[a][o1] & 1, prof[a][o2] & 1) for a in range(3)) + '}'
print('{%d, %d, %d, %d, %s, %s}' % (seams(P12, 34, 12), seams(P15, 31, 15), rings(P12, 34, 12), rings(P15, 31, 15),
                                    dec(P12, 20, 23), dec(P15, 6, 23)))
