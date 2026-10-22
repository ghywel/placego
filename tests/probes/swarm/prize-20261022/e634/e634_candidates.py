#!/usr/bin/env python3
"""Explicit Group-2 candidate triangles for composite non-classical n <= 100 (necessary conditions only):
exact area ratio (Heron) and angle shape. A tiling of any of these would make n a new good value."""
import math
from fractions import Fraction as F
def h16(x, y, z): return (x+y+z)*(-x+y+z)*(x-y+z)*(x+y-z)
def ang(x, y, z): return math.acos((y*y + z*z - x*x) / (2*y*z))
cands = [  # (n, shape, tile (a,b,c), triangle sides)
    (21, '(al, al+be, al+2be)', (5, 16, 19), (20, 76, 84)),
    (30, '(al, al+be, al+2be)', (7, 8, 13), (28, 52, 60)),
    (55, '(al, al+be, al+2be)', (39, 16, 49), (156, 196, 220)),
    (84, '(al, al+be, al+2be)', (5, 16, 19), (40, 152, 168)),
    (33, '(al, al, al+3be)', (5, 3, 7), (21, 21, 33)),
    (46, '(al, al, al+3be)', (7, 8, 13), (52, 52, 92)),
    (88, '(al, 2be, 2al+be)', (3, 5, 7), (21, 55, 56)),
    (71, '(al, al, al+3be) [prime 3 mod 4: arithmetic alive]', (39, 16, 49), (196, 196, 284)),
]
for n, shape, (a, b, c), (x, y, z) in cands:
    assert a*a + a*b + b*b == c*c
    r = F(h16(x, y, z), h16(a, b, c))
    N = math.isqrt(r.numerator) if r.denominator == 1 and math.isqrt(r.numerator)**2 == r.numerator else None
    al, be = ang(a, b, c), ang(b, a, c)
    combos = []
    for t in (ang(x, y, z), ang(y, x, z), ang(z, x, y)):
        combos.append(next(((i, j) for i in range(5) for j in range(5) if abs(i*al + j*be - t) < 1e-9), None))
    print(f"n={n:3d} {shape}: tile {(a,b,c)} triangle {(x,y,z)} -> N={N} (ok={N==n}); angles (i,j) for i*al+j*be: {combos}")
