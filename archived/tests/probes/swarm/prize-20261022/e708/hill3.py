#!/usr/bin/env python3
"""omega=3 stress families (prediction: worst position stays <= 2n; triples ratio near or below 1.5)."""
import sys, itertools, time
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else '400']
import hill
from hill import run
fams = []
P = [11, 13, 17, 19]
fams.append(('triples of (11,13,17,19)', sorted(a*b*c for a, b, c in itertools.combinations(P, 3))))
P = [5, 7, 11, 13]
fams.append(('triples of (5,7,11,13)', sorted(a*b*c for a, b, c in itertools.combinations(P, 3))))
P = [7, 11, 13]
fams.append(('pairs+triple of (7,11,13)', sorted([77, 91, 143, 1001])))
P = [5, 7, 11, 13]
fams.append(('pairs+triples of (5,7,11,13)', sorted([a*b for a, b in itertools.combinations(P, 2)] + [a*b*c for a, b, c in itertools.combinations(P, 3)])))
for name, A in fams:
    run(name, A, iters=120, restarts=4)
