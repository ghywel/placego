#!/usr/bin/env python3
"""R13 one-point extensions: p = (0, y) on the symmetry axis through vertex q = (0, 1) (circumradius 1). Distances from p:
g = |1 - y| (to q) and f_k (k = 1..6, to the symmetric pair at angle +-2 pi k/13 from q). For an n=15 counterexample
(c = 2 case) every value must be a chord c_m (m = 1..6) or a common value D > c_6. Scan y finely; report the best y
by the number of values that are chords (within tol) with the rest equal and > c_6."""
import math
ch = [2*math.sin(math.pi*m/13) for m in range(1, 7)]
c6 = max(ch)
def vals(y):
    return [abs(1 - y)] + [math.sqrt(1 + y*y - 2*y*math.cos(2*math.pi*k/13)) for k in range(1, 7)]
def score(y, tol=1e-6):
    v = vals(y)
    nonch = [a for a in v if min(abs(a - c) for c in ch) > tol]
    ok = (not nonch) or (min(nonch) > c6 + tol and max(nonch) - min(nonch) < tol)
    return ok, len(v) - len(nonch), nonch
best = []
N = 400000
for i in range(-N, N + 1):
    y = i * (8.0 / N)       # y in [-8, 8]
    if abs(y) < 1e-12 or abs(y - 1) < 1e-12: continue
    v = vals(y)
    nch = sum(1 for a in v if min(abs(a - c) for c in ch) < 2e-4)
    best.append((nch, y))
best.sort(reverse=True)
print('max number of chord-valued distances on a grid of 8e5 y-values in [-8,8] (tol 2e-4):', best[0][0])
print('top y candidates:', [(n, round(y, 5)) for n, y in best[:8]])
# refine: a full solution needs >= 7 - (#values equal to D); values equal to D must all be equal; check top candidates
for n, y in best[:20]:
    print(round(y, 5), [round(a, 4) for a in vals(y)], 'chords', [round(c, 4) for c in ch]) if n >= 4 else None
