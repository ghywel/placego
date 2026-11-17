#!/usr/bin/env python3
"""Cloud, 2026-10-30 (CL649). Does a run of non-doublings build pressure?

Reads an edge_lift output (lines "seed=... E_n: e1 e2 ...", block period exponents of a finite seed's edge code) and
prints, over the window n = LO..HI, f(m) = frequency of a doubling given that the previous m letters d = E_n - E_(n-1)
are all 0, and the distribution of zero-run lengths. Usage: edge_zero_runs.py FILE [LO HI]  (default 13 56).
Predictions were written before the run (CL649): fair model, f(m) flat near 1/2 and geometric runs of ratio 1/2.
"""
import collections
import re
import sys

path = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 13
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 56
seqs = []
for line in open(path):
    m = re.search(r"seed=(\S+) E_n: (.*)", line)
    if m:
        seqs.append((m.group(1), [int(x) for x in m.group(2).split()]))
cnt, tot, runs = collections.Counter(), collections.Counter(), collections.Counter()
long_runs = []
for seed, s in seqs:
    d = [s[i] - s[i - 1] for i in range(1, len(s))]  # d[k] is the letter at n = k + 1
    for k in range(len(d)):
        n = k + 1
        if n < lo or n > hi:
            continue
        for m in range(1, 8):
            if k - m < 0:
                break
            if all(d[k - i] == 0 for i in range(1, m + 1)):
                tot[m] += 1
                cnt[m] += d[k]
    r, start = 0, 0
    for k in range(len(d)):
        n = k + 1
        if n < lo or n > hi:
            continue
        if d[k] == 0:
            if r == 0:
                start = n
            r += 1
        else:
            if r:
                runs[r] += 1
                if r >= 8:
                    long_runs.append((seed, s[start - 1], start, start + r - 1, r))
            r = 0
    if r:
        runs[r] += 1
        if r >= 8:
            long_runs.append((seed, s[start - 1], start, start + r - 1, r))
print(f"{len(seqs)} seeds, window n = {lo}..{hi}")
for m in range(1, 8):
    if tot[m]:
        print(f" m={m}: cases {tot[m]:4d}  f(m) = {cnt[m] / tot[m]:.3f}")
print(" zero-run lengths (length, count):", sorted(runs.items()))
nruns = sum(runs.values())
print(f" geometric expectation (ratio 1/2) for length >= 8: {nruns / 2 ** 8:.1f}, >= 9: {nruns / 2 ** 9:.1f}")
for seed, e, a, b, r in long_runs:
    print(f" plateau: seed {seed} E = {e} over n = {a}..{b} (length {r})")
