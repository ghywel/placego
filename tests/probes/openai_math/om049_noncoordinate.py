#!/usr/bin/env python3
"""om049_noncoordinate.py: openai/math family 049, a polynomial whose zero fibre is affine 3-space but which is not
a coordinate (a counterexample to the Abhyankar-Sathaye embedding conjecture in four variables).

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om049_noncoordinate.py
COST:       under a minute.

The claim (preprint "An explicit noncoordinate polynomial with affine three-space zero fibre", 2026-09-24). In
R = C[h,u,v,w] put x = u^3 + h v, y = -u^2 + h w, s = 2u^3 v + 3u^4 w + h(v^2 - 3u^2 w^2) + h^2 w^3, so that
x^2 + y^3 = h s; put p = -2 s^2 x + 3 s y^2 - 3 s^3 y and F = h - p - 1. Then R/(F) is a polynomial ring in three
variables, yet the gradient of F vanishes at P = (2, 0, -1/2, 1/2). A coordinate (the first component of a
polynomial automorphism) has a nowhere-zero gradient, because the automorphism's Jacobian is invertible
everywhere, so F is not one.

Cloud read the whole proof (one lifting lemma, three pages) and checks here every identity it rests on, as exact
integer polynomial identities, then tests the explicit maps both ways at points:
  I1  x^2 + y^3 = h s in R.
  I2  (x + s^3)^2 + (y - s^2)^3 = x^2 + y^3 - s p for independent x, y, s (the shift that flattens the cusp).
  I3  alpha h + beta y - 1 = (1 + 2 s^2 x)(h - 1 - p) - 4 s^4 (x^2 + y^3 - s h), the unit-ideal certificate.
  I4  S(h, U, G - U W, W) = h G^2 - 2 U y G + y^2 W once y = h W - U^2 (the lemma's linearising substitution).
  I5  U^3 + h (G - U W) - x = h G - y U - x once y = h W - U^2.
  I6  y^2 a - h b = (h G - y U)^2 + y^3 - h s, with a = y + U^2, b = s - h G^2 + 2 U y G.
  I7  r h + q y^2 - 1 = (1 + beta y)(alpha h + beta y - 1), with r = alpha (1 + beta y), q = beta^2.
  I8  h G - y U - x and alpha U + beta G - T are multiples of alpha h + beta y - 1 under U = hT - beta x,
      G = y T + alpha x (the inverse pair of the lemma).
  I9  X^2 + Y^3 = s (1 + F) in R, with X = x + s^3, Y = y - s^2.
  I10 F(P) = -1 and every partial derivative of F vanishes at P.
  Round trips: Phi(Psi(t)) = t and F(Psi(t)) = 0 at random rational t = (X, Y, T); Psi(Phi(q)) = q at random points
  q of the zero fibre over the field with 1009 elements.
Predictions (written before the run): all pass. Fail: any identity off by a nonzero polynomial, or a round trip off.
Unexpected check (for the record, AGENTS.md item 6): count the points of every fibre F = c over the field F_p,
p = 3, 5, 7, 11, 13. The maps have integer coefficients both ways, so the zero fibre must have exactly p^3 points;
a coordinate would give p^3 on every fibre. Cloud's guess, even odds, written before the run: the critical fibre
F = -1 differs from p^3 for some p in the list.
Control: the polynomial h itself (a coordinate) has p^3 points on every fibre and a nowhere-zero gradient.
"""
import itertools, random
from fractions import Fraction as Fr


class Poly:
    """Integer polynomials in named variables, as {exponent tuple: coefficient}."""
    def __init__(self, terms, names):
        self.t = {k: c for k, c in terms.items() if c}
        self.names = names

    @classmethod
    def var(cls, names, i):
        return cls({tuple(int(j == i) for j in range(len(names))): 1}, names)

    def _lift(self, o):
        return o if isinstance(o, Poly) else Poly({(0,) * len(self.names): o}, self.names)

    def __add__(self, o):
        o, out = self._lift(o), dict(self.t)
        for k, c in o.t.items():
            out[k] = out.get(k, 0) + c
        return Poly(out, self.names)
    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -c for k, c in self.t.items()}, self.names)

    def __sub__(self, o):
        return self + (-self._lift(o))

    def __rsub__(self, o):
        return self._lift(o) - self

    def __mul__(self, o):
        o, out = self._lift(o), {}
        for k1, c1 in self.t.items():
            for k2, c2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                out[k] = out.get(k, 0) + c1 * c2
        return Poly(out, self.names)
    __rmul__ = __mul__

    def __pow__(self, n):
        out = self._lift(1)
        for _ in range(n):
            out = out * self
        return out

    def is_zero(self):
        return not self.t

    def diff(self, i):
        out = {}
        for k, c in self.t.items():
            if k[i]:
                kk = list(k); kk[i] -= 1
                out[tuple(kk)] = out.get(tuple(kk), 0) + c * k[i]
        return Poly(out, self.names)

    def __call__(self, *vals):
        tot = 0
        for k, c in self.t.items():
            m = c
            for v, e in zip(vals, k):
                m = m * v ** e
            tot = tot + m
        return tot


class Mod:
    """Integers modulo a prime, enough for the generic formulas below."""
    p = 1009

    def __init__(self, a):
        self.a = a % Mod.p

    def _v(self, o):
        return o.a if isinstance(o, Mod) else o

    def __add__(self, o): return Mod(self.a + self._v(o))
    __radd__ = __add__
    def __sub__(self, o): return Mod(self.a - self._v(o))
    def __rsub__(self, o): return Mod(self._v(o) - self.a)
    def __mul__(self, o): return Mod(self.a * self._v(o))
    __rmul__ = __mul__
    def __neg__(self): return Mod(-self.a)
    def __pow__(self, n): return Mod(pow(self.a, n, Mod.p))
    def __eq__(self, o): return self.a == self._v(o) % Mod.p
    def __hash__(self): return hash(self.a)


def xys(h, u, v, w):
    s = 2 * u ** 3 * v + 3 * u ** 4 * w + h * (v ** 2 - 3 * u ** 2 * w ** 2) + h ** 2 * w ** 3
    return u ** 3 + h * v, -u ** 2 + h * w, s


def S(h, U, V, W):
    return 2 * U ** 3 * V + 3 * U ** 4 * W + h * (V ** 2 - 3 * U ** 2 * W ** 2) + h ** 2 * W ** 3


def pp(x, y, s):
    return -2 * s ** 2 * x + 3 * s * y ** 2 - 3 * s ** 3 * y


def alpha(x, y, s):
    return 1 + 2 * s ** 2 * x + 4 * s ** 5


def beta(x, y, s):
    return (3 * s ** 3 - 3 * s * y) * (1 + 2 * s ** 2 * x) - 4 * s ** 4 * y ** 2


def F(h, u, v, w):
    x, y, s = xys(h, u, v, w)
    return h - pp(x, y, s) - 1


def Phi(h, u, v, w):
    x, y, s = xys(h, u, v, w)
    return x + s ** 3, y - s ** 2, alpha(x, y, s) * u + beta(x, y, s) * (v + u * w)


def Psi(X, Y, T):
    s = X ** 2 + Y ** 3
    x, y = X - s ** 3, Y + s ** 2
    h = 1 + pp(x, y, s)
    a, b = alpha(x, y, s), beta(x, y, s)
    u, g = h * T - b * x, y * T + a * x
    w = a * (1 + b * y) * (y + u ** 2) + b ** 2 * (s - h * g ** 2 + 2 * u * y * g)
    return h, u, g - u * w, w


def ring(names):
    return [Poly.var(names, i) for i in range(len(names))]


def main():
    res = {}
    h, u, v, w = R = ring("huvw")
    x, y, s = xys(h, u, v, w)
    res["I1  x^2 + y^3 = h s"] = (x ** 2 + y ** 3 - h * s).is_zero()
    X, Y, Sv = ring("xys")
    res["I2  cusp shift"] = ((X + Sv ** 3) ** 2 + (Y - Sv ** 2) ** 3 - (X ** 2 + Y ** 3 - Sv * pp(X, Y, Sv))).is_zero()
    H, X, Y, Sv = ring("hxys")
    lhs = alpha(X, Y, Sv) * H + beta(X, Y, Sv) * Y - 1
    rhs = (1 + 2 * Sv ** 2 * X) * (H - 1 - pp(X, Y, Sv)) - 4 * Sv ** 4 * (X ** 2 + Y ** 3 - Sv * H)
    res["I3  unit-ideal certificate"] = (lhs - rhs).is_zero()
    H, U, G, W, X = ring("hUGWx")
    yy = H * W - U ** 2
    lin = H * G ** 2 - 2 * U * yy * G + yy ** 2 * W
    res["I4  linearising substitution"] = (S(H, U, G - U * W, W) - lin).is_zero()
    res["I5  first relation becomes h G - y U - x"] = ((U ** 3 + H * (G - U * W) - X) - (H * G - yy * U - X)).is_zero()
    H, Y, Sv, U, G = ring("hysUG")
    a, b = Y + U ** 2, Sv - H * G ** 2 + 2 * U * Y * G
    res["I6  compatibility"] = (Y ** 2 * a - H * b - ((H * G - Y * U) ** 2 + Y ** 3 - H * Sv)).is_zero()
    A, B, H, Y, X, T = ring("abhyxT")
    res["I7  r h + q y^2 - 1 is a multiple"] = ((A * (1 + B * Y)) * H + B ** 2 * Y ** 2 - 1
                                            - (1 + B * Y) * (A * H + B * Y - 1)).is_zero()
    Uq, Gq, e = H * T - B * X, Y * T + A * X, A * H + B * Y - 1
    res["I8  inverse pair of the lemma"] = ((H * Gq - Y * Uq - X - e * X).is_zero()
                                          and (A * Uq + B * Gq - T - e * T).is_zero())
    Fp = h - pp(x, y, s) - 1
    res["I9  X^2 + Y^3 = s (1 + F)"] = ((x + s ** 3) ** 2 + (y - s ** 2) ** 3 - s * (1 + Fp)).is_zero()
    P = (Fr(2), Fr(0), Fr(-1, 2), Fr(1, 2))
    grads = [Fp.diff(i)(*P) for i in range(4)]
    res["I10 F(P) = -1, grad F(P) = 0"] = Fp(*P) == -1 and all(g == 0 for g in grads)
    print(f"   F has degree {max(sum(k) for k in Fp.t)} and {len(Fp.t)} terms; values at P: x, y, s = "
          f"{[str(t) for t in xys(*P)]}, F = {Fp(*P)}, gradient {[str(g) for g in grads]}")
    rng = random.Random(49)
    ok = True
    for _ in range(12):
        t = tuple(Fr(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(3))
        q = Psi(*t)
        ok &= F(*q) == 0 and Phi(*q) == t
    res["R1  F(Psi(t)) = 0 and Phi(Psi(t)) = t at 12 random rational t"] = ok
    ok, n = True, 0
    while n < 300:
        hh, uu, vv = (Mod(rng.randrange(Mod.p)) for _ in range(3))
        for ww in range(Mod.p):
            q = (hh, uu, vv, Mod(ww))
            if F(*q) == 0:
                n += 1
                ok &= Psi(*Phi(*q)) == q
    res[f"R2  Psi(Phi(q)) = q at {n} random points of the zero fibre over F_{Mod.p}"] = ok
    print("   fibre point counts over F_p (count of points with F = c, as c runs over F_p):")
    zero_ok, crit = True, []
    for p in (3, 5, 7, 11, 13):
        Mod.p = p
        cnt = {c: 0 for c in range(p)}
        ctl = {c: 0 for c in range(p)}
        for q in itertools.product(range(p), repeat=4):
            cnt[F(*(Mod(t) for t in q)).a] += 1
            ctl[q[0]] += 1
        assert all(v == p ** 3 for v in ctl.values())
        zero_ok &= cnt[0] == p ** 3
        crit.append(cnt[(-1) % p] != p ** 3)
        print(f"   p = {p:2d}: p^3 = {p ** 3}; zero fibre {cnt[0]}; F = -1: {cnt[(-1) % p]}; "
              f"all fibres {[cnt[c] for c in range(p)]}")
    res["U   zero fibre has exactly p^3 points for p = 3..13"] = zero_ok
    print(f"   guess (critical fibre differs from p^3 for some p): {'right' if any(crit) else 'wrong'}")
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
