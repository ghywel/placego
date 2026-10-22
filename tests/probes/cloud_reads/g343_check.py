#!/usr/bin/env python3
"""Cloud's exact-arithmetic check for the GC1688 review: G343 (an equilateral
rational 120-degree tiling needs N > 18 tiles) and PRIOR-ART MI642's N = 15
interface.  This checks the arithmetic only; the geometric steps of G343 were
read by hand (CL558) and MI642's literature premises are cited, not re-proved.

PREDICTIONS (written before running):
  - every between-squares, non-square and factor-pair claim in G343 and MI642
    holds exactly;
  - (2c+a)^2 - 18ab > 0 for every primitive 120-degree triple, and the two
    displayed algebraic identities hold symbolically;
  - counterfactual: if any claimed non-square were a square, the corresponding
    N = 15 case would stay open and the composition would fail.
"""
from fractions import Fraction as F
from math import gcd, isqrt


def is_square(n):
    return n >= 0 and isqrt(n) ** 2 == n


def strictly_between_squares(n):
    r = isqrt(n)
    return r * r < n < (r + 1) * (r + 1)


ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok &= bool(cond)


# --- G343 ---------------------------------------------------------------
# Identities, checked on an integer grid (polynomials of degree 2).
for a in range(1, 8):
    for b in range(1, 8):
        for c in range(1, 8):
            # the identity holds modulo c^2 = a^2 + ab + b^2
            lhs = (2 * c + a) ** 2 - 18 * a * b - 4 * (c * c - a * a - a * b - b * b)
            assert lhs == 5 * a * a + 4 * b * b - 14 * a * b + 4 * a * c
        assert 7 * a * a + 4 * b * b - 10 * a * b == F((4 * b - 5 * a) ** 2 + 3 * a * a, 4)
check("G343 expansion identities", True)

# Primitive 120-degree triples a<b, c^2=a^2+ab+b^2: c > b + a/2 and the bound.
triples = [(a, b, isqrt(a * a + a * b + b * b)) for b in range(2, 2000) for a in range(1, b)
           if gcd(a, b) == 1 and is_square(a * a + a * b + b * b)]
check(f"G343 c>b+a/2 and (2c+a)^2>18ab on {len(triples)} primitive triples",
      all(2 * c > 2 * b + a and (2 * c + a) ** 2 > 18 * a * b for a, b, c in triples))
check("G343 pairwise coprime", all(gcd(a, c) == gcd(b, c) == 1 for a, b, c in triples))
check("G343 smallest ratio N=(2c+a)^2/(ab) over triples > 18",
      min(F((2 * c + a) ** 2, a * b) for a, b, c in triples) > 18)
# ab | 4: (1,1),(1,2),(1,4) give c^2 = 3, 7, 21.
check("G343 ab|4 gives no integer c",
      all(not is_square(a * a + a * b + b * b) for a, b in [(1, 1), (1, 2), (1, 4)]))
# b = k a: k^2 < k^2+k+1 < (k+1)^2.
check("G343 k^2+k+1 never square (k<=10^5)",
      all(strictly_between_squares(k * k + k + 1) for k in range(1, 100001)))
# alpha/pi irrational: 1 < 2cos(alpha) = (a+2b)/c < 2 and not an integer.
check("G343 1<(a+2b)/c<2 on all triples",
      all(c < a + 2 * b < 2 * c for a, b, c in triples))

# --- MI642, N = 15 ------------------------------------------------------
vals = {M: (135 - M * M) * (15 - M * M) for M in (1, 2, 3)}
check(f"MI642 (1) {vals} strictly between squares",
      vals == {1: 1876, 2: 1441, 3: 756} and all(strictly_between_squares(v) for v in vals.values()))

pairs = [(k, m) for k in range(2, 50) for m in range(1, k) if gcd(k, m) == 1]
A = sorted({2 * k * k - m * m for k, m in pairs if 2 * k * k - m * m <= 15})
B = sorted({3 * k * k - m * m for k, m in pairs if 3 * k * k - m * m <= 15})
check(f"MI642 (2) A<=15 values {A}, B<=15 values {B}", A == [7, 14] and B == [11])
check("MI642 (2) A=17 at k=3,m=1", 2 * 9 - 1 == 17)
check("MI642 (2) A/D>2 and gcd(A,D)=1",
      all(F(2 * k * k - m * m, k * k - m * m) > 2 and gcd(2 * k * k - m * m, k * k - m * m) == 1
          for k, m in pairs))
D = {k * k - m * m for k, m in pairs}
check("MI642 (2) D never 1, 2 or 4", not (D & {1, 2, 4}))
check("MI642 (2) s^2=15D, D<=s forces s=D=15",
      [(s, s * s // 15) for s in range(1, 1000) if s * s % 15 == 0 and s * s // 15 <= s] == [(15, 15)])

# Group 2, lambda = 1 (squarefree), integer a,b >= 1.
g2 = [(a, b) for a in range(1, 20) for b in range(1, 20) if (2 * a + b) * (a + b) == 15]
g4 = [(a, b) for a in range(1, 20) for b in range(1, 20) if (a + 2 * b) * (2 * a + b) == 15]
check(f"MI642 (3) (2a+b)(a+b)=15 -> {g2}, c^2=7", g2 == [(2, 1)] and not is_square(7))
check("MI642 (3) (a+2b)(2a+b)=15 has no integer solution", g4 == [])
check("MI642 (3) 3(a+2b)(a+b) >= 18", min(3 * (a + 2 * b) * (a + b) for a in range(1, 9) for b in range(1, 9)) == 18)
rq = [F(15, l * l) - 1 for l in (1, 2, 3)]
cs = [r.numerator ** 2 + r.numerator * r.denominator + r.denominator ** 2 for r in rq]
check(f"MI642 (3) ratios {rq} give c^2 {cs}, none square",
      rq == [14, F(11, 4), F(2, 3)] and cs == [211, 181, 19] and not any(map(is_square, cs)))
iso = [F(15, l * l) - 2 for l in (1, 2, 3)]
cs2 = [r.numerator ** 2 + r.numerator * r.denominator + r.denominator ** 2 for r in iso if r > 0]
check(f"MI642 (4) 120-degree branch ratios {iso[:2]} give c^2 {cs2}, none square; lambda=3 negative",
      iso[:2] == [13, F(7, 4)] and iso[2] < 0 and cs2 == [183, 93] and not any(map(is_square, cs2)))

print("ALL PASS" if ok else "SOME FAIL")

# OUTCOME (2026-10-22, CL558): ALL PASS, as predicted.  The first run failed on
# my own transcription: the expansion identity holds only modulo c^2=a^2+ab+b^2,
# which G343 uses; the check now subtracts that multiple, as the proof does.  The counterfactual did
# not occur: no claimed non-square is a square.  Arithmetic only; G343's
# geometry read by hand, MI642's literature premises cited, not re-proved.
