#!/usr/bin/env python3
"""SEP gap, step 2 (Local, 8 November 2026): the death hazard by free-bit context beyond the free horizon.
Same frame as death_pairs.py. For all starts of exact width w in [WMIN, WMAX], take every check at step s + 1 with
s + 1 >= ceil(w / 2) (beyond the horizon where count_constrained makes the free bits uniform), and tabulate the
hazard of death at that check by the last two free bits (f(s - 1), f(s)), pooled over widths.
Prediction, before the run: beyond the horizon the hazards by pair differ by more than 3 standard errors for at least
one pair, P = 0.5; 00 has the highest hazard, P = 0.3. Counterfactual: all four hazards agree within noise, and free
pairs carry no information about death anywhere in the finite range."""
import math, sys
def F(y): return (y >> 1) ^ (y | (y << 1))
def run(y):
    f = []
    while True:
        if y & 1 == 0: return f
        y = F(y); f.append(y & 1); y = F(y)
wmin, wmax = int(sys.argv[1]), int(sys.argv[2])
hz = {}
for w in range(wmin, wmax + 1):
    h0 = -(-w // 2)
    for y in range((1 << (w - 1)) | 1, 1 << w, 2):
        f = run(y); N = len(f)          # death at the check after f(N - 1)
        for s in range(max(1, h0 - 1), N):
            p = (f[s - 1], f[s]); d = hz.setdefault(p, [0, 0]); d[1] += 1
            if s == N - 1: d[0] += 1
for p, (k, n) in sorted(hz.items()):
    q = k / n; se = math.sqrt(q * (1 - q) / n)
    print(''.join(map(str, p)), 'checks', n, 'deaths', k, 'hazard %.4f +- %.4f' % (q, se))
