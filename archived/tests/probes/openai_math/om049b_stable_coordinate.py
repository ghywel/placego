#!/usr/bin/env python3
"""om049b_stable_coordinate.py: openai/math family 049, second preprint: a degree-5 stable coordinate in four
variables that is not a coordinate.

RUN-ON:     cpu (Python 3, standard library; reuses the polynomial class of om049_noncoordinate.py)
COMMAND:    python3 tests/probes/openai_math/om049b_stable_coordinate.py
COST:       about a minute.

The claim (preprint "A stable coordinate that is not a coordinate in four variables", 2026-10-05). In
R = C[x1, x2, x3, x4] put Q = x2^2 - x4^2 + x1 x3 and f = x1 - 2Q(Q(x2 + x4) + x1 x4). Some automorphism of R[w]
sends f to x1, but no automorphism of R does; every fibre f = c is affine 3-space, so it also disproves the
Abhyankar-Sathaye embedding conjecture in ambient dimension four, with a polynomial of degree 5 (family 049's
first preprint used degree 17).

Cloud read the whole proof (five sections) and found it correct. The non-coordinate half is pure argument (a
filtration, a graded locally nilpotent derivation, a line bundle, a weight contradiction); its computable identities
are checked here. The stable half is explicit, and is checked end to end:
  S1  the presentation A = k[p,s,u,F,J]/(H), x = s^2 - u^2 + pF, H = x^2 F - (1 + 2sx) J - p J^2 - u: the matrix
      change M' = (I - 2 n e^T) M keeps x = -det M, gives H = -J - u', and its inverse turns p into f exactly;
  S2  x y - z(z+1) = p (H + u), with y = s + x(x + u^2), z = s x + p J;
  S3  the derivation Delta (Delta p = 0, Delta u = -p, Delta s = 2pxu, Delta F = -4sxu - 2u, Delta J = -2x^2 u) kills
      x, y, z, sends H to p, and is nilpotent on every generator;
  S4  the unimodular substitution to L, N and H = L - u + p Q0;
  S5  the composite automorphism theta of 5-space (A = R, then exp(-w Delta), then the L, N coordinates), built from
      the formulas and tested both ways at random rational points, with its first coordinate equal to f;
  S6  the line-bundle identities of sections 4 and 5: the relation x y - z(z+1) = d b (a c - b d - 1), the chart
      formulas, I C = (v) with v = a^2 j, and the unit identity behind it;
  S7  every fibre f = c over F_l has exactly l^3 points (l = 3, 5, 7, 11), as fibres isomorphic to 3-space must.
Predictions (written before the run): all pass. Fail: any identity off, any round trip off, any fibre count off.
Unexpected check: the Jacobian determinant of theta, computed exactly at random points with dual numbers. It must be
the same nonzero constant everywhere; Cloud's guess, about 60% confident, is that the constant is 1 or -1.
Control: the identity map's Jacobian through the same dual-number code is 1.
"""
import itertools, math, random, sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from om049_noncoordinate import Poly, ring  # noqa: E402


class Dual:
    """a + b eps with eps^2 = 0, for exact first derivatives."""
    def __init__(self, a, b=0):
        self.a, self.b = a, b

    def _c(self, o):
        return o if isinstance(o, Dual) else Dual(o)

    def __add__(self, o): o = self._c(o); return Dual(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __sub__(self, o): o = self._c(o); return Dual(self.a - o.a, self.b - o.b)
    def __rsub__(self, o): return self._c(o) - self
    def __neg__(self): return Dual(-self.a, -self.b)
    def __mul__(self, o): o = self._c(o); return Dual(self.a * o.a, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def __pow__(self, n):
        out = Dual(1)
        for _ in range(n):
            out = out * self
        return out


def det(m):
    a = [list(r) for r in m]
    n, s = len(a), Fr(1)
    for k in range(n):
        piv = next((i for i in range(k, n) if a[i][k] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            s = -s
        s *= a[k][k]
        for i in range(k + 1, n):
            r = a[i][k] / a[k][k]
            a[i] = [x - r * y for x, y in zip(a[i], a[k])]
    return s


def half(P):
    assert all(c % 2 == 0 for c in P.t.values())
    return Poly({k: c // 2 for k, c in P.t.items()}, P.names)


def matmul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def nilp(n, e, sign):
    """I + sign * 2 n e^T as a 2x2 matrix."""
    return [[1 + sign * 2 * n[0] * e[0], sign * 2 * n[0] * e[1]], [sign * 2 * n[1] * e[0], 1 + sign * 2 * n[1] * e[1]]]


def from_R(x1, x2, x3, x4):
    """Proposition 2.1's inverse: the point (p, s, u, F, J) of H = 0 over (p', s', F', J) = (x1, x2, x3, x4)."""
    J = x4
    x = x2 ** 2 - J ** 2 + x1 * x3
    Mp = [[x3, x2 + J], [x2 - J, -x1]]                       # u' = -J
    M = matmul(nilp((J, x), (x, -J), +1), Mp)
    return -M[1][1], (M[0][1] + M[1][0]) * Fr(1, 2), (M[1][0] - M[0][1]) * Fr(1, 2), M[0][0], J


def main():
    res = {}
    p, s, u, F, J = ring("psuFJ")
    x = s ** 2 - u ** 2 + p * F
    H = x ** 2 * F - (1 + 2 * s * x) * J - p * J ** 2 - u
    # S1
    M = [[F, s - u], [s + u, -p]]
    e, n = (x, -J), (J, x)
    eMe = e[0] * (M[0][0] * e[0] + M[0][1] * e[1]) + e[1] * (M[1][0] * e[0] + M[1][1] * e[1])
    Mp = matmul(nilp(n, e, -1), M)
    ok = ((-(M[0][0] * M[1][1] - M[0][1] * M[1][0]) - x).is_zero() and (eMe - J - u - H).is_zero()
          and (-(Mp[0][0] * Mp[1][1] - Mp[0][1] * Mp[1][0]) - x).is_zero()
          and (Mp[1][0] - Mp[0][1] - 2 * (u - eMe)).is_zero())
    up = half(Mp[1][0] - Mp[0][1])
    ok &= (H + J + up).is_zero()
    X1, X2, X3, X4 = ring("abcd")
    pp, ss, uu, FF, JJ = from_R(X1, X2, X3, X4)                 # coefficients may be halves; Poly allows that
    xx = ss ** 2 - uu ** 2 + pp * FF
    Q = X2 ** 2 - X4 ** 2 + X1 * X3
    f = X1 - 2 * Q * (Q * (X2 + X4) + X1 * X4)
    ok &= (xx ** 2 * FF - (1 + 2 * ss * xx) * JJ - pp * JJ ** 2 - uu).is_zero() and (pp - f).is_zero()
    res["S1  presentation: x kept, H = -J - u', and p becomes f exactly"] = ok
    print(f"   f has degree {max(sum(k) for k in f.t)} and {len(f.t)} terms")
    # S2
    y, z = s + x * (x + u ** 2), s * x + p * J
    res["S2  x y - z(z+1) = p (H + u)"] = (x * y - z * (z + 1) - p * (H + u)).is_zero()
    # S3
    D = {0: Poly({}, p.names), 1: 2 * p * x * u, 2: -p, 3: -4 * s * x * u - 2 * u, 4: -2 * x ** 2 * u}

    def Delta(g):
        out = Poly({}, g.names)
        for i in range(5):
            if D[i].t:
                out = out + g.diff(i) * D[i]
        return out
    ok = all(Delta(t).is_zero() for t in (x, y, z)) and (Delta(H) - p).is_zero()
    orders = []
    for t in (p, s, u, F, J):
        k, g = 0, t
        while not g.is_zero():
            g, k = Delta(g), k + 1
        orders.append(k)
    res["S3  Delta kills x, y, z, sends H to p, and is nilpotent"] = ok
    print(f"   Delta^k kills p, s, u, F, J first at k = {orders}")
    # S4
    x0 = s ** 2 - u ** 2
    L = x0 ** 2 * F - (1 + 2 * s * x0) * J
    N = (1 - 2 * s * x0) * F + 4 * s ** 2 * J
    Q0 = 2 * x0 * F ** 2 + p * F ** 3 - 2 * s * F * J - J ** 2
    ok = ((4 * s ** 2 * x0 ** 2 + (1 + 2 * s * x0) * (1 - 2 * s * x0) - 1).is_zero()
          and (4 * s ** 2 * L + (1 + 2 * s * x0) * N - F).is_zero()
          and (-(1 - 2 * s * x0) * L + x0 ** 2 * N - J).is_zero()
          and (L - u + p * Q0 - H).is_zero())
    res["S4  unimodular L, N and H = L - u + p Q0"] = ok
    # S5: theta (points of (x1..x4, w) to points of (p, s, u, N, w')) and its inverse psi.
    names6 = "psuFJw"
    P6 = ring(names6)
    lift = lambda g: g(*P6[:5])                                  # P into P[w]
    w6 = P6[5]

    def expo(g, sign):
        out, term, k = Poly({}, names6), lift(g), 0
        while not term.is_zero():
            out = out + term * Fr(1, math.factorial(k))
            # next term: (sign w)^(k+1) Delta^(k+1) g; Delta commutes with w
            k += 1
            g = Delta(g)
            term = lift(g) * (sign * w6) ** k
        return out
    Th = [lift(p), expo(s, -1), expo(u, -1), expo(N, -1), w6 + expo(Q0, -1)]
    Mfwd = Mp
    inv = [-Mfwd[1][1], half(Mfwd[0][1] + Mfwd[1][0]), Mfwd[0][0], J]   # p', s', F', J as elements of P
    Ps = [expo(g, +1) for g in inv]

    def theta(q):
        P5 = from_R(*q[:4])
        return [g(*P5, q[4]) for g in Th]

    def psi(t):
        pt, st, ut, Nt, wpt = t
        Lt = ut - pt * wpt
        x0t = st ** 2 - ut ** 2
        Ft = 4 * st ** 2 * Lt + (1 + 2 * st * x0t) * Nt
        Jt = -(1 - 2 * st * x0t) * Lt + x0t ** 2 * Nt
        wt = wpt - (2 * x0t * Ft ** 2 + pt * Ft ** 3 - 2 * st * Ft * Jt - Jt ** 2)
        return [g(pt, st, ut, Ft, Jt, wt) for g in Ps] + [wt]
    rng = random.Random(4905)
    ok = True
    for _ in range(8):
        q = [Fr(rng.randint(-3, 3), rng.randint(1, 2)) for _ in range(5)]
        t = theta(q)
        ok &= psi(t) == q and t[0] == f(*q[:4])
        t2 = [Fr(rng.randint(-3, 3), rng.randint(1, 2)) for _ in range(5)]
        ok &= theta(psi(t2)) == t2
    res["S5  theta and psi are inverse at 16 random points, and theta's first coordinate is f"] = ok
    print(f"   theta's components have total degrees {[max(sum(k) for k in g.t) for g in Th]} in (p, s, u, F, J, w)")
    jac = set()
    assert det([[Fr(int(i == j)) for j in range(5)] for i in range(5)]) == 1     # control
    for _ in range(3):
        q = [Fr(rng.randint(-2, 2), rng.randint(1, 2)) for _ in range(5)]
        cols = []
        for i in range(5):
            qq = [Dual(c, int(k == i)) for k, c in enumerate(q)]
            cols.append([c.b if isinstance(c, Dual) else Fr(0) for c in theta(qq)])
        jac.add(det([[cols[j][i] for j in range(5)] for i in range(5)]))
    print(f"   Jacobian determinant of theta at 3 random points: {sorted(str(j) for j in jac)}")
    res["U   the Jacobian determinant is one nonzero constant"] = len(jac) == 1 and 0 not in jac
    print(f"   guess (the constant is 1 or -1): {'right' if jac <= {1, -1} else 'wrong'}")
    # S6
    a, d, b, c, uC = ring("adbcu")
    xC, yC, zC = a * b, d * c, d * b
    ok = (xC * yC - zC * (zC + 1) - d * b * (a * c - b * d - 1)).is_zero()
    XI, XX, JJ6 = ring("qxj")
    ok &= ((1 - 2 * XI * XX) * (1 + 2 * XI * XX - XX ** 2 * JJ6) + XX ** 2 * (4 * XI ** 2 + JJ6 - 2 * XI * XX * JJ6)
           - 1).is_zero()
    for _ in range(20):
        A_, D_, B_, U_ = (Fr(rng.choice([-3, -2, -1, 1, 2, 3]), rng.randint(1, 3)) for _ in range(4))
        C_ = (1 + B_ * D_) / A_
        x_, y_, z_ = A_ * B_, D_ * C_, D_ * B_
        sB = y_ - x_ * (x_ + U_ ** 2)
        f0, g0 = x_ - sB ** 2 + U_ ** 2, z_ - sB * x_
        v = A_ ** 3 * B_ + A_ ** 2 * U_ ** 2 - D_ ** 2
        xi = D_ / A_
        j = x_ + U_ ** 2 - xi ** 2
        ok &= (z_ == xi * x_ and y_ == xi + xi ** 2 * x_ and sB == xi - x_ * j
               and f0 == (1 + 2 * xi * x_ - x_ ** 2 * j) * j and g0 == x_ ** 2 * j and v == A_ ** 2 * j)
        # at a = 0 the relation forces b d = -1; then g0 = -1 and v = -d^2 are units
        C0 = Fr(rng.randint(-3, 3), rng.randint(1, 3))
        B0 = -1 / D_
        x0_, y0_, z0_ = 0 * B0, D_ * C0, D_ * B0
        sB0 = y0_ - x0_ * (x0_ + U_ ** 2)
        ok &= z0_ - sB0 * x0_ == -1 and 0 ** 3 * B0 + 0 * U_ ** 2 - D_ ** 2 == -D_ ** 2 != 0
    res["S6  line-bundle relation, chart formulas, I C = (v), and the unit identity"] = ok
    # S7
    ok = True
    for l in (3, 5, 7, 11):
        cnt = [0] * l
        for q in itertools.product(range(l), repeat=4):
            cnt[f(*q) % l] += 1
        ok &= all(c == l ** 3 for c in cnt)
        print(f"   l = {l:2d}: fibre sizes {sorted(set(cnt))} (l^3 = {l ** 3})")
    res["S7  every fibre has exactly l^3 points over F_l, l = 3..11"] = ok
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
