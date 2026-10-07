#!/usr/bin/env python3
"""om088_projection_body.py: openai/math family 088, the product counterexample to the simplex maximum.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om088_projection_body.py
COST:       a few seconds.

The claim (preprint "A product counterexample to the simplex maximum for projection-body volume", 2026-09-24):
R_d(K) = |Pi K| / |K|^(d-1), where Pi K is the projection body (its support function in direction u is the volume of
the shadow of K on the hyperplane orthogonal to u). Brannen (1996) conjectured R_d(K) <= c_d = (d+1) d^d / d!, the
simplex value. The preprint shows R_(r+s)(A x B) = R_r(A) R_s(B) for polytopes, so the product of two 10-simplices
has R_20 / c_20 = 121 binom(20,10) / (21 2^20) = 22355476 / 22020096 > 1.

Cloud read the whole proof (five pages) and checks every step that can be computed, by routes that do not reuse it:
  1. The Cauchy formula for polytopes, h_PiP(u) = (1/2) sum over facets of area |<normal, u>|, against shadows
     computed directly as convex hulls (a tetrahedron's shadow is a polygon; the 4-polytope T2 x T2 casts a
     3-dimensional shadow), at random directions.
  2. The facets of T_r x T_s, found by brute force from the vertices (every supporting hyperplane through enough
     vertices), against the preprint's list (facet of one factor times the whole other factor).
  3. The simplex value R_d(T_d) = c_d for d = 2..14, with |Pi T_d| from the general zonotope volume formula
     (the sum of |det| over every d-subset of generators, Shephard and McMullen), not the preprint's cube argument.
  4. The product identity for T_r x T_s, r, s = 2..6, by the same zonotope formula on the product's own facets.
  5. The final arithmetic, and the constants in the preprint's corollary (exponential excess in high dimension).
Predictions (written before the run): every check passes; the ratio is exactly 22355476/22020096, about 1.0152;
the product test first beats the simplex at r = s = 10 among equal splits. Fail: any mismatch, or a shadow volume
off by more than 1e-9.
Control: the unit cube, whose shadow in a coordinate direction has area 1 and whose R_d is 2^d (its projection body
is the cube [-1, 1]^d, of volume 2^d).
"""
import itertools, math, random
from fractions import Fraction as Fr


def det(m):
    """Exact determinant by fraction-free elimination (Bareiss)."""
    a = [list(map(Fr, row)) for row in m]
    n, sign, prev = len(a), 1, Fr(1)
    for k in range(n - 1):
        if a[k][k] == 0:
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    a[k], a[i] = a[i], a[k]
                    sign = -sign
                    break
            else:
                return Fr(0)
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) / prev
        prev = a[k][k]
    return sign * a[-1][-1]


def zonotope_volume(gens):
    d = len(gens[0])
    return sum(abs(det(list(S))) for S in itertools.combinations(gens, d))


def simplex_vertices(d):
    return [tuple(Fr(int(i == j)) for j in range(d)) for i in range(-1, d)]


def product(A, B):
    return [a + b for a in A for b in B]


def facets(V):
    """Supporting hyperplanes (n, c) with <n, x> <= c on V, each spanned by vertices; n is primitive integer."""
    d, out = len(V[0]), set()
    for S in itertools.combinations(range(len(V)), d):
        rows = [[V[i][k] - V[S[0]][k] for k in range(d)] for i in S[1:]]
        # normal = generalised cross product of the d-1 rows
        n = [(-1) ** k * det([r[:k] + r[k + 1:] for r in rows]) for k in range(d)] if d > 1 else [Fr(1)]
        if all(x == 0 for x in n):
            continue
        den = math.lcm(*[x.denominator for x in n])
        n = [int(x * den) for x in n]
        g = math.gcd(*n)
        n = tuple(x // g for x in n)
        c = sum(a * b for a, b in zip(n, V[S[0]]))
        vals = [sum(a * b for a, b in zip(n, v)) for v in V]
        if all(x <= c for x in vals):
            out.add((n, c))
        elif all(x >= c for x in vals):
            out.add((tuple(-x for x in n), -c))
    return sorted(out)


def simplex_area_normals(d):
    """Area-normal vectors (area times outward unit normal) of T_d, each computed from its own vertices."""
    V = simplex_vertices(d)
    out = []
    for skip in range(d + 1):
        F = [v for i, v in enumerate(V) if i != skip]
        rows = [[F[i][k] - F[0][k] for k in range(d)] for i in range(1, d)]
        n = [(-1) ** k * det([r[:k] + r[k + 1:] for r in rows]) for k in range(d)]  # |n| = (d-1)! area
        n = [x / math.factorial(d - 1) for x in n]
        if sum(a * (b - c) for a, b, c in zip(n, V[skip], F[0])) > 0:  # point outward, away from the far vertex
            n = [-x for x in n]
        out.append(n)
    return out


def hull_volume_3d(P):
    """Volume of the convex hull of points in R^3 (float), by its facets and a centroid fan."""
    c = [sum(p[k] for p in P) / len(P) for k in range(3)]
    vol, seen = 0.0, set()
    for i, j, k in itertools.combinations(range(len(P)), 3):
        a, b, e = P[i], P[j], P[k]
        u = [b[t] - a[t] for t in range(3)]
        v = [e[t] - a[t] for t in range(3)]
        n = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
        nn = math.sqrt(sum(x * x for x in n))
        if nn < 1e-12:
            continue
        n = [x / nn for x in n]
        h = sum(n[t] * a[t] for t in range(3))
        s = [sum(n[t] * p[t] for t in range(3)) - h for p in P]
        if max(s) > 1e-9 and min(s) < -1e-9:
            continue
        if max(s) > 1e-9:
            n, h = [-x for x in n], -h
        key = (round(n[0], 9), round(n[1], 9), round(n[2], 9))
        if key in seen:
            continue
        seen.add(key)
        on = [p for p in P if abs(sum(n[t] * p[t] for t in range(3)) - h) < 1e-9]
        # area of the planar convex polygon 'on', by angle sort about its centroid
        q = [sum(p[t] for p in on) / len(on) for t in range(3)]
        e1 = [on[0][t] - q[t] for t in range(3)]
        if math.sqrt(sum(x * x for x in e1)) < 1e-12:
            e1 = [on[1][t] - q[t] for t in range(3)]
        m1 = math.sqrt(sum(x * x for x in e1))
        e1 = [x / m1 for x in e1]
        e2 = [n[1] * e1[2] - n[2] * e1[1], n[2] * e1[0] - n[0] * e1[2], n[0] * e1[1] - n[1] * e1[0]]
        pts = sorted(((sum((p[t] - q[t]) * e1[t] for t in range(3)), sum((p[t] - q[t]) * e2[t] for t in range(3)))
                      for p in on), key=lambda z: math.atan2(z[1], z[0]))
        area = 0.5 * abs(sum(pts[i][0] * pts[i - 1][1] - pts[i - 1][0] * pts[i][1] for i in range(len(pts))))
        vol += area * abs(h - sum(n[t] * c[t] for t in range(3))) / 3
    return vol


def polygon_area(P):
    c = [sum(p[k] for p in P) / len(P) for k in range(2)]
    pts = sorted(P, key=lambda p: math.atan2(p[1] - c[1], p[0] - c[0]))
    hull = []
    for p in sorted(set(pts)):
        while len(hull) >= 2 and ((hull[-1][0] - hull[-2][0]) * (p[1] - hull[-2][1])
                                  - (hull[-1][1] - hull[-2][1]) * (p[0] - hull[-2][0])) <= 0:
            hull.pop()
        hull.append(p)
    low = hull
    hull = []
    for p in sorted(set(pts), reverse=True):
        while len(hull) >= 2 and ((hull[-1][0] - hull[-2][0]) * (p[1] - hull[-2][1])
                                  - (hull[-1][1] - hull[-2][1]) * (p[0] - hull[-2][0])) <= 0:
            hull.pop()
        hull.append(p)
    h = low[:-1] + hull[:-1]
    return 0.5 * abs(sum(h[i][0] * h[i - 1][1] - h[i - 1][0] * h[i][1] for i in range(len(h))))


def orthonormal_complement(u):
    """An orthonormal basis of the hyperplane orthogonal to the unit vector u (Gram-Schmidt)."""
    d, basis = len(u), []
    for k in range(d):
        v = [float(i == k) for i in range(d)]
        for b in [u] + basis:
            dot = sum(x * y for x, y in zip(v, b))
            v = [x - dot * y for x, y in zip(v, b)]
        m = math.sqrt(sum(x * x for x in v))
        if m > 1e-8:
            basis.append([x / m for x in v])
        if len(basis) == d - 1:
            return basis


def c(d):
    return Fr((d + 1) * d ** d, math.factorial(d))


def main():
    rng = random.Random(30)
    results = {}
    # Control: the unit square/cube. Pi of [0,1]^d is [-1,1]^d, so R_d = 2^d.
    for d in (2, 3, 4):
        gens = [tuple(Fr(int(i == k)) for k in range(d)) for i in range(d) for _ in (0, 1)]  # two facets per axis
        assert zonotope_volume(gens) == 2 ** d
    # 1. Cauchy's formula against direct shadows.
    worst = 0.0
    an3 = simplex_area_normals(3)
    T3 = [[float(x) for x in v] for v in simplex_vertices(3)]
    for _ in range(50):
        u = [rng.gauss(0, 1) for _ in range(3)]
        m = math.sqrt(sum(x * x for x in u)); u = [x / m for x in u]
        e1, e2 = orthonormal_complement(u)
        shadow = polygon_area([(sum(p[k] * e1[k] for k in range(3)), sum(p[k] * e2[k] for k in range(3))) for p in T3])
        cauchy = 0.5 * sum(abs(sum(float(n[k]) * u[k] for k in range(3))) for n in an3)
        worst = max(worst, abs(shadow - cauchy))
    an2 = simplex_area_normals(2)
    K = [[float(x) for x in a + b] for a in simplex_vertices(2) for b in simplex_vertices(2)]
    gens22 = [tuple(Fr(1, 2) * x for x in n) + (0, 0) for n in an2] + [(0, 0) + tuple(Fr(1, 2) * x for x in n)
                                                                      for n in an2]  # |T2| = 1/2 times each
    for _ in range(30):
        u = [rng.gauss(0, 1) for _ in range(4)]
        m = math.sqrt(sum(x * x for x in u)); u = [x / m for x in u]
        B = orthonormal_complement(u)
        shadow = hull_volume_3d([[sum(p[k] * b[k] for k in range(4)) for b in B] for p in K])
        cauchy = 0.5 * sum(abs(sum(float(g[k]) * u[k] for k in range(4))) for g in gens22)
        worst = max(worst, abs(shadow - cauchy))
    results["1. Cauchy formula matches direct shadows (T3 in R^3, T2 x T2 in R^4)"] = worst < 1e-9
    print(f"   largest shadow discrepancy {worst:.2e}")
    # 2. Facets of products, by brute force from vertices.
    ok2 = True
    for r, s in [(2, 2), (2, 3), (3, 3), (2, 4)]:
        F = facets(product(simplex_vertices(r), simplex_vertices(s)))
        want = sorted({(tuple(n) + (0,) * s, cc) for n, cc in facets(simplex_vertices(r))}
                      | {((0,) * r + tuple(n), cc) for n, cc in facets(simplex_vertices(s))})
        ok2 &= F == want and len(F) == r + s + 2
    results["2. facets of T_r x T_s are (facet x whole) and (whole x facet), r + s + 2 of them"] = ok2
    # 3. Simplex value.
    ok3 = True
    for d in range(2, 15):
        vol = Fr(1, math.factorial(d))
        pi = zonotope_volume(simplex_area_normals(d))
        ok3 &= pi == Fr(d + 1, math.factorial(d - 1) ** d) and pi / vol ** (d - 1) == c(d)
    results["3. |Pi T_d| = (d+1)/((d-1)!)^d and R_d(T_d) = (d+1) d^d / d!, d = 2..14"] = ok3
    # 4. Product identity.
    ok4 = True
    for r in range(2, 7):
        for s in range(2, 7):
            vA, vB = Fr(1, math.factorial(r)), Fr(1, math.factorial(s))
            gens = ([tuple(vB * x for x in n) + (0,) * s for n in simplex_area_normals(r)]
                    + [(0,) * r + tuple(vA * x for x in n) for n in simplex_area_normals(s)])
            R = zonotope_volume(gens) / (vA * vB) ** (r + s - 1)
            ok4 &= R == c(r) * c(s)
            closed = Fr((r + 1) * (s + 1), r + s + 1) * math.comb(r + s, r) * Fr(r ** r * s ** s, (r + s) ** (r + s))
            ok4 &= R / c(r + s) == closed
    results["4. R(T_r x T_s) = c_r c_s, and the preprint's closed form for the ratio (r, s <= 6)"] = ok4
    # 5. Arithmetic.
    ratio = c(10) ** 2 / c(20)
    ok5 = (ratio == Fr(121 * math.comb(20, 10), 21 * 2 ** 20) == Fr(22355476, 22020096)
           and 121 * 184756 - 21 * 1048576 == 335380 and c(10) == Fr(17187500, 567)
           and c(10) / Fr(11, 4) ** 10 == Fr(1638400000000, 1336956340797) > 1)
    first = next(k for k in range(2, 40) if c(k) ** 2 > c(2 * k))
    results["5. arithmetic: ratio 22355476/22020096, certificate 335380, corollary constants"] = ok5
    print(f"   R_20(T10 x T10) / c_20 = {ratio} = {float(ratio):.6f}; first equal split that wins: r = s = {first}")
    for k, v in results.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(results.values()) else "FAIL")


if __name__ == "__main__":
    main()
