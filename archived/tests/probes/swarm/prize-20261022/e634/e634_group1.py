#!/usr/bin/env python3
"""Group 1 (3alpha+2beta=pi) area formulas, checked by exact Heron arithmetic.
Tile (a,b,c) = (mk, k^2-m^2, k^2), gcd(m,k)=1, 0<m<k  (2 sin(alpha/2) = m/k).
Hand-derived ABC side vectors (base scale s=1) and predicted N(s=1):
  (2a,b,a+b)   triquadratic : sides (m(2k^2-m^2), k(k^2-m^2), k^3)      N0 = 2k^2-m^2
  (b,b,3a)     isosceles-beta: sides (k^3, k^3, m(3k^2-m^2))             N0 = 3k^2-m^2
  (a,2a,2b)                  : sides (k^4, k^2(2k^2-m^2), (k^2-m^2)(3k^2-m^2))  N0 = (2k^2-m^2)(3k^2-m^2)
  (a,a,a+2b)                 : sides (k^2, k^2, 2k^2-m^2)                N0 = (2k^2-m^2)/(k^2-m^2)
  (a+b,a+b,a)                : sides (k, k, m)                           N0 = 1/(k^2-m^2)
Check: angles of ABC equal the claimed combinations; N(s=1)=area ratio equals N0 exactly."""
import math
from fractions import Fraction as F

def h16(x, y, z):
    return (x + y + z) * (-x + y + z) * (x - y + z) * (x + y - z)

def ang(x, y, z):  # angle opposite x
    return math.acos((y * y + z * z - x * x) / (2 * y * z))

bad = 0; checked = 0
for k in range(2, 30):
    for m in range(1, k):
        if math.gcd(m, k) != 1: continue
        a, b, c = m * k, k * k - m * m, k * k
        al, be = ang(a, b, c), ang(b, a, c)
        assert abs(3 * al + 2 * be - math.pi) < 1e-9, (k, m)
        shapes = {
            'tri(2a,b,a+b)': ((m * (2*k*k - m*m), k * (k*k - m*m), k**3), (2*al, be, al + be), F(2*k*k - m*m)),
            'isoB(b,b,3a)': ((k**3, k**3, m * (3*k*k - m*m)), (be, be, 3*al), F(3*k*k - m*m)),
            '(a,2a,2b)': ((k**4, k*k*(2*k*k - m*m), (k*k - m*m)*(3*k*k - m*m)), (al, 2*al, 2*be),
                          F((2*k*k - m*m)*(3*k*k - m*m))),
            '(a,a,a+2b)': ((k*k, k*k, 2*k*k - m*m), (al, al, al + 2*be), F(2*k*k - m*m, k*k - m*m)),
            '(a+b,a+b,a)': ((k, k, m), (al + be, al + be, al), F(1, k*k - m*m)),
        }
        for name, (sides, angs, N0) in shapes.items():
            x, y, z = sides
            ratio2 = F(h16(x, y, z), h16(a, b, c))   # = N^2
            okN = (ratio2 == N0 * N0)
            A = (ang(x, y, z), ang(y, x, z), ang(z, x, y))
            okA = all(abs(A[i] - angs[i]) < 1e-9 for i in range(3))
            checked += 1
            if not (okN and okA):
                bad += 1
                print("MISMATCH", k, m, name, sides, ratio2, N0, okA)
print(f"checked {checked} (shape, k, m) cases, mismatches {bad}")

# N=19 in each shape: N = s^2 * N0 with s a positive integer (sides integral, gcd of base sides = 1)
sols = {}
for k in range(2, 400):
    for m in range(1, k):
        if math.gcd(m, k) != 1: continue
        N0s = {'tri': F(2*k*k - m*m), 'isoB': F(3*k*k - m*m), '(a,2a,2b)': F((2*k*k-m*m)*(3*k*k-m*m)),
               '(a,a,a+2b)': F(2*k*k - m*m, k*k - m*m), '(a+b,a+b,a)': F(1, k*k - m*m)}
        for name, N0 in N0s.items():
            s2 = F(19) / N0
            if s2.denominator == 1:
                s = math.isqrt(s2.numerator)
                if s * s == s2.numerator:
                    sols.setdefault(name, []).append((k, m, s))
print("N=19 arithmetic solutions per Group-1 shape (k<400):", {kk: v[:4] for kk, v in sols.items()})
