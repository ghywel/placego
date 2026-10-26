#!/usr/bin/env python3
"""certificate_influence_posthoc.py: POST HOC (Local, 2026-10-26, L991), written after certificate_shuffle.c's outcome; no prediction was frozen.
Reads the retained certificate_witness.c stdout (the ALL-population LANE rows carry each lane's target Y) and prints, per width, the mean
sensitivity of Y to the n diary bits and each bit's influence Pr[Y(l) != Y(l XOR 2^i)], oldest to newest. Reads data only; no dynamics run.
Usage: python3 certificate_influence_posthoc.py <certificate_witness out.txt>
Theorem used as a guard (standard): every sensitive bit lies in every certificate for the ALL population, so mincert >= sensitivity lane by lane.
"""
import re, sys, collections
Y = collections.defaultdict(dict); D = collections.defaultdict(dict)
for line in open(sys.argv[1]):
    m = re.match(r'LANE W=(\d+) pop=ALL lane=(\d+) Y=(\d) D=(\d+)', line)
    if m: Y[int(m[1])][int(m[2])] = int(m[3]); D[int(m[1])][int(m[2])] = int(m[4])
for W in sorted(Y):
    n = W // 2; y = Y[W]; N = 1 << n
    assert len(y) == N
    sens = [sum(y[l] != y[l ^ (1 << i)] for i in range(n)) for l in range(N)]
    assert all(D[W][l] >= sens[l] for l in range(N)), "certificate >= sensitivity violated"
    inf = [sum(y[l] != y[l ^ (1 << i)] for l in range(N)) / N for i in range(n)]
    print(f"W={W} n={n} mean sensitivity {sum(sens)/N:.3f} (n/2 = {n/2:.1f}) influence oldest..newest:", " ".join(f"{v:.2f}" for v in inf))
