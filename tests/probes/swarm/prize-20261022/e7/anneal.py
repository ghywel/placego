#!/usr/bin/env python3
"""Falsification attempt: simulated annealing for distinct systems (one residue per divisor d>1 of N)
minimising the uncovered count.  Theorem prediction for {3,5,7}-smooth N: uncovered density >= 1/16.
Usage: anneal.py N seconds seed"""
import sys, random, time, math
N = int(sys.argv[1]); secs = float(sys.argv[2]); random.seed(int(sys.argv[3]))
divs = [d for d in range(2, N + 1) if N % d == 0]
cnt = [0] * N
res = {d: random.randrange(d) for d in divs}
def add(d, r, s):
    for x in range(r, N, d): cnt[x] += s
for d in divs: add(d, res[d], 1)
unc = sum(1 for x in cnt if x == 0)
best = unc; t0 = time.time(); T = 2.0; it = 0
while time.time() - t0 < secs:
    it += 1
    d = random.choice(divs); r_old = res[d]; r_new = random.randrange(d)
    if r_new == r_old: continue
    # delta
    delta = 0
    for x in range(r_old, N, d):
        if cnt[x] == 1: delta += 1
    add(d, r_old, -1)
    for x in range(r_new, N, d):
        if cnt[x] == 0: delta -= 1
    add(d, r_new, 1)
    if delta <= 0 or random.random() < math.exp(-delta / T):
        unc += delta; res[d] = r_new
        if unc < best: best = unc
    else:
        add(d, r_new, -1); add(d, r_old, 1)
    T = max(0.05, 2.0 * (1 - (time.time() - t0) / secs))
print(f"N={N} divisors>1={len(divs)} best uncovered={best} density={best/N:.4f} (bound 1/16={N/16:.1f} residues) iters={it}")
