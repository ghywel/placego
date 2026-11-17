#!/usr/bin/env python3
"""Numerical checks for the n=14 reduction: profiles of R13, R12+centre, and the lattice star W (13 points, 6 distances);
the R13 extension: p on the symmetry axis through q, y = -7/6 from the sum identity; and a brute-force scan of y."""
import math, itertools
from collections import Counter
def prof(P, nd=9):
    c = Counter(round(math.dist(a, b), nd) for a, b in itertools.combinations(P, 2))
    return dict(sorted(c.items()))
R13 = [(math.cos(2*math.pi*k/13 + math.pi/2), math.sin(2*math.pi*k/13 + math.pi/2)) for k in range(13)]
R12c = [(math.cos(2*math.pi*k/12), math.sin(2*math.pi*k/12)) for k in range(12)] + [(0.0, 0.0)]
h = math.sqrt(3)/2
ax = lambda a, b: (a + b/2, b*h)
W = [ax(a, b) for a, b in [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1),(2,-1),(-2,1),(1,-2),(-1,2)]]
for name, P in [('R13', R13), ('R12+c', R12c), ('W', W)]:
    pr = prof(P); print(name, len(P), 'points', len(pr), 'distances', 'mults', list(pr.values()), 'sum', sum(pr.values()),
                       'max mult', max(pr.values()), '(>15 kills n=14)' if max(pr.values()) > 15 else '')
# R13 extension
chords2 = sorted(2 - 2*math.cos(2*math.pi*m/13) for m in range(1, 7))
s = sum(math.cos(2*math.pi*k/13) for k in range(1, 7)); print('sum cos(2 pi k/13), k=1..6 =', round(s, 12))
y = -7/6
f2 = sorted(1 + y*y - 2*y*math.cos(2*math.pi*k/13) for k in range(1, 7))
print('y=-7/6 pair dist^2', [round(v, 5) for v in f2]); print('chord^2       ', [round(v, 5) for v in chords2])
print('|pq|^2 =', (1 - y)**2)
# brute scan: best match over y in [-20, 0): max |f2 - chords2| sorted
best = min((max(abs(a - b) for a, b in zip(sorted(1 + yy*yy - 2*yy*math.cos(2*math.pi*k/13) for k in range(1, 7)), chords2)), yy)
           for yy in [-(i+1)/10000 for i in range(200000)])
print('scan y in [-20,0): min over y of max mismatch =', round(best[0], 6), 'at y =', best[1])
