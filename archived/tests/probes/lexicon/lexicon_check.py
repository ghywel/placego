#!/usr/bin/env python3
"""lexicon_check.py: every claim of LEXICON.md that a computer can check, checked against literal ports of the shader.

RUN-ON:     cpu (pure Python 3, standard library only; no GPU, no numpy)
COMMAND:    python3 tests/probes/lexicon/lexicon_check.py
PREDICTION: every check prints PASS and the script exits 0; every counterfactual is caught (prints CAUGHT).
REFUTED-BY: any FAIL line, or any counterfactual that is not caught (a check that cannot fail proves nothing).
COST:       under a minute.

Written by Cloud on 2026-10-04 for LEXICON.md. Each check is one claim of that document:

  C1  The coarse search (bidirectional-interpolation.glsl, the pass whose //!DESC is line 175 on be6fd30) is a chain of five margin folds, and with
      the margin set to zero each fold is a tropical sum: the lexicon's formula and a line-by-line port of the GLSL
      loop return the same vector on every block.
  C2  The coarse result is a five-site spin-1 chain: d = sum_i h_i s_i with s_i in {-1,0,+1}^2, exactly, and the
      reachable set is the 63 multiples of 3/64 per axis.
  C3  The margin fold is order-dependent (so not a semiring sum) when the margin is non-zero, and order-free when it
      is zero.
  C4  The vector median (the pass whose //!DESC is line 1394 on be6fd30) is a linear product followed by a tropical sum.
  C5  Every finite program is a matrix: the 0/1 matrix of a map f on n states has characteristic polynomial
      x^(n-c) * prod over cycles (x^L - 1), so its spectrum is exactly the cycle structure of f.
  C6  Rule 30 is the GF(2) polynomial l + c + r + c*r; the simulator reproduces OEIS A051023 ("Middle column of
      rule-30 1-D cellular automaton, from a lone 1 cell"); and that column has no period p <= 1024 on its last 3072
      of 4096 steps (a demonstration, not a proof).
  C7  Machine arithmetic: fl32 addition is not associative; Knuth's TwoSum recovers the rounding error exactly; the
      same algorithm after an algebraic "simplification" (what a fast-math compiler may do) does not.
"""
import math, random, struct, sys
from fractions import Fraction as Fr
from itertools import product

FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def caught(name, differs, detail=""):
    global FAILS
    FAILS += not differs
    print(f"{'CAUGHT' if differs else 'MISSED'}  counterfactual: {name}" + (f"  ({detail})" if detail else ""))


# ----------------------------------------------------------------------------------------------------------------
# A bilinear sampler with clamp-to-edge, in normalised coordinates, as BIDIRECTIONAL-AS-MATHEMATICS.md section 1.
def sample(T, W, H, u, v):
    x, y = u * W - 0.5, v * H - 0.5
    x0, y0 = math.floor(x), math.floor(y)
    fx, fy = x - x0, y - y0
    def at(i, j):
        return T[min(max(j, 0), H - 1)][min(max(i, 0), W - 1)]
    return ((1 - fx) * (1 - fy) * at(x0, y0) + fx * (1 - fy) * at(x0 + 1, y0)
            + (1 - fx) * fy * at(x0, y0 + 1) + fx * fy * at(x0 + 1, y0 + 1))


def textured_pair(W, H, rng, shift=(0.9, -0.4)):
    """A smooth random texture A and B = A moved by a fractional shift (texels), both in [0,1]."""
    waves = [(rng.uniform(0.2, 1.4), rng.uniform(0.2, 1.4), rng.uniform(0, 6.3), rng.uniform(0.05, 0.25))
             for _ in range(6)]
    def f(x, y):
        return min(1.0, max(0.0, 0.5 + sum(a * math.sin(kx * x + ky * y + ph) for kx, ky, ph, a in waves)))
    A = [[f(i, j) for i in range(W)] for j in range(H)]
    B = [[f(i - shift[0], j - shift[1]) for i in range(W)] for j in range(H)]
    return A, B


R1 = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1) if (x, y) != (0, 0)]   # row-major, y outer: the GLSL order
TIE, LAM, MINC = 1.0e-4, 0.06, 0.02


# ---- the GLSL loop, line by line (bidirectional-interpolation.glsl, coarse A->B search) -------------------------
def coarse_glsl(A, B, W, H, i, j, lam=LAM, tie=TIE, step0=0.75):
    pt = (1.0 / W, 1.0 / H)
    uv = ((i + 0.5) / W, (j + 0.5) / H)
    def sad(ua, ub):
        s = 0.0
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                o = (x * pt[0], y * pt[1])
                s += abs(sample(A, W, H, ua[0] + o[0], ua[1] + o[1]) - sample(B, W, H, ub[0] + o[0], ub[1] + o[1]))
        return s
    lo, hi = 1.0, 0.0
    for y in range(-2, 3):
        for x in range(-2, 3):
            v = sample(A, W, H, uv[0] + x * pt[0], uv[1] + y * pt[1])
            lo, hi = min(lo, v), max(hi, v)
    if hi - lo < MINC:
        return (0.0, 0.0), None
    best_off = (0.0, 0.0)
    best_cost = sad(uv, uv)
    step = step0
    digits = []
    for it in range(5):
        cand_best, win = best_off, (0, 0)
        for (x, y) in R1:
            off = (best_off[0] + x * step * pt[0], best_off[1] + y * step * pt[1])
            cost = sad(uv, (uv[0] + off[0], uv[1] + off[1])) + lam * math.hypot(off[0] / pt[0], off[1] / pt[1])
            if cost < best_cost * (1.0 - tie):
                best_cost, cand_best, win = cost, off, (x, y)
        best_off = cand_best
        digits.append(win)
        step *= 0.5
    return (best_off[0] / pt[0], best_off[1] / pt[1]), digits


# ---- the lexicon's form: a chain of margin folds over a cost J, in texel units --------------------------------
def margin_fold(incumbent, candidates, J, eps):
    """The margin scan of BIDIRECTIONAL-AS-MATHEMATICS.md section 1 (written as a fold in LEXICON.md)."""
    d, c = incumbent
    for x in candidates:
        cx = J(x)
        if cx < (1.0 - eps) * c:
            d, c = x, cx
    return d, c


def coarse_lexicon(A, B, W, H, i, j, eps=TIE, combine=None):
    u = ((i + 0.5) / W, (j + 0.5) / H)
    def C(d):
        s = 0.0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                s += abs(sample(A, W, H, u[0] + dx / W, u[1] + dy / H)
                         - sample(B, W, H, u[0] + (d[0] + dx) / W, u[1] + (d[1] + dy) / H))
        return s
    J = lambda d: C(d) + LAM * math.hypot(*d)
    vals = [sample(A, W, H, u[0] + x / W, u[1] + y / H) for y in range(-2, 3) for x in range(-2, 3)]
    if max(0.0, max(vals)) - min(1.0, min(vals)) < MINC:
        return (0.0, 0.0)
    d, c = (0.0, 0.0), C((0.0, 0.0))
    for k in range(5):
        h = 0.75 * 2.0 ** -k
        cands = [(d[0] + h * s[0], d[1] + h * s[1]) for s in R1]
        if combine is None:
            d, c = margin_fold((d, c), cands, J, eps)
        else:                                     # a counterfactual "addition" in place of the fold
            d = combine(d, cands, J)
            c = J(d)
    return d


def tropical_argmin(points, J):
    """The tropical sum with its witness: the first point of least cost (min is the semiring's addition)."""
    best = min(range(len(points)), key=lambda k: (J(points[k]), k))
    return points[best]


# ----------------------------------------------------------------------------------------------------------------
def check_c1_c2(rng):
    W, H = 40, 24
    A, B = textured_pair(W, H, rng)
    blocks = [(i, j) for j in range(2, H - 2, 2) for i in range(2, W - 2, 2)]
    agree = searched = spin_ok = 0
    fold_vs_trop_rounds = fold_vs_trop_same = 0
    reach = set()
    for (i, j) in blocks:
        g, digits = coarse_glsl(A, B, W, H, i, j)
        lx = coarse_lexicon(A, B, W, H, i, j)
        agree += max(abs(g[0] - lx[0]), abs(g[1] - lx[1])) < 1e-12
        if digits is None:
            continue
        searched += 1
        # C2: the result is sum_i h_i s_i exactly, h_i = (3/4) 2^-i, s_i the digit the round chose
        exact = (sum(Fr(3, 4) / 2 ** k * s[0] for k, s in enumerate(digits)),
                 sum(Fr(3, 4) / 2 ** k * s[1] for k, s in enumerate(digits)))
        spin_ok += abs(float(exact[0]) - g[0]) < 1e-12 and abs(float(exact[1]) - g[1]) < 1e-12
        for comp in exact:
            m = comp / Fr(3, 64)
            reach.add(m.denominator == 1 and abs(m) <= 31)
    report("C1 coarse search: lexicon formula == GLSL loop, every block", agree == len(blocks),
           f"{agree} of {len(blocks)} blocks, {searched} past the contrast gate")
    report("C2 coarse result == sum_i h_i s_i, s_i in {-1,0,+1}^2 (a spin-1 chain of 5 sites)",
           spin_ok == searched and reach == {True}, f"{spin_ok} of {searched}; every component a multiple of 3/64, |m| <= 31")
    # the reachable set: every signed-digit word of length 5 over {-1,0,1}, weights 16,8,4,2,1
    ms = {sum(s * w for s, w in zip(word, (16, 8, 4, 2, 1))) for word in product((-1, 0, 1), repeat=5)}
    report("C2 reachable set per axis is exactly the 63 integers -31..31 (times 3/64)",
           ms == set(range(-31, 32)), f"{len(ms)} values")
    # with the margin at zero, every round's fold is the tropical sum (first minimum in scan order)
    u = (0.5, 0.5)
    for _ in range(400):
        costs = [rng.random() for _ in range(9)]
        pts = list(range(9))
        J = lambda k: costs[k]
        f, _ = margin_fold((pts[0], J(pts[0])), pts[1:], J, 0.0)
        t = tropical_argmin(pts, J)
        fold_vs_trop_rounds += 1
        fold_vs_trop_same += f == t
    report("C1 with margin 0, a fold == the tropical sum (min, first in order)",
           fold_vs_trop_same == fold_vs_trop_rounds, f"{fold_vs_trop_same} of {fold_vs_trop_rounds} random rounds")
    # counterfactual: replace the fold by an ordinary sum (average the candidates) -- must disagree somewhere
    mean = lambda d, cands, J: (sum(c[0] for c in cands) / 8.0, sum(c[1] for c in cands) / 8.0)
    diff = sum(1 for (i, j) in blocks
               if max(map(abs, (a - b for a, b in zip(coarse_glsl(A, B, W, H, i, j)[0],
                                                      coarse_lexicon(A, B, W, H, i, j, combine=mean))))) > 1e-9)
    caught("the fold replaced by an ordinary (+) average", diff > 0, f"{diff} of {len(blocks)} blocks differ")
    diff = sum(1 for (i, j) in blocks
               if max(map(abs, (a - b for a, b in zip(coarse_glsl(A, B, W, H, i, j)[0],
                                                      coarse_glsl(A, B, W, H, i, j, lam=0.3)[0])))) > 1e-9)
    caught("REG_LAMBDA 0.06 -> 0.3 in the GLSL port", diff > 0, f"{diff} of {len(blocks)} blocks differ")


def check_c3():
    eps = 1.0e-4
    J = {"x": 0.99985, "y": 0.9998}.__getitem__
    inc = ("o", 1.0)
    a = margin_fold(inc, ["x", "y"], J, eps)[0]
    b = margin_fold(inc, ["y", "x"], J, eps)[0]
    a0 = margin_fold(inc, ["x", "y"], J, 0.0)[0]
    b0 = margin_fold(inc, ["y", "x"], J, 0.0)[0]
    report("C3 margin fold depends on candidate order when eps > 0", a != b, f"order x,y -> {a}; order y,x -> {b}")
    report("C3 ... and not when eps = 0 (distinct costs)", a0 == b0 == "y", f"both -> {a0}")


def check_c4(rng):
    same = total = 0
    for _ in range(500):
        v = [(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(9)]
        if rng.random() < 0.3:                  # near-agreeing clusters, where the order matters most
            v = [(round(a, 1), round(b, 1)) for a, b in v]
        # GLSL port (the pass whose //!DESC is line 1394 on be6fd30)
        best_cost, best = 1e30, v[4]
        for i in range(9):
            cost = sum(math.hypot(v[i][0] - v[j][0], v[i][1] - v[j][1]) for j in range(9))
            if cost < best_cost * (1.0 - TIE):
                best_cost, best = cost, v[i]
        # lexicon: Phi = D 1 (an ordinary matrix-vector product), then a margin fold over Phi
        D = [[math.hypot(a[0] - b[0], a[1] - b[1]) for b in v] for a in v]
        Phi = [sum(row) for row in D]
        lx = v[margin_fold((4, 1e30), list(range(9)), lambda k: Phi[k], TIE)[0]]
        same += lx == best
        total += 1
    report("C4 vector median == (D times 1 in (+,x)) then a margin fold", same == total, f"{same} of {total}")


# ---- C5: every finite program is a matrix; its spectrum is its cycle structure ---------------------------------
def charpoly(M):
    """Characteristic polynomial det(xI - M) by the Faddeev-LeVerrier recurrence, in exact rationals.
    Returns coefficients [1, c1, ..., cn] of x^n + c1 x^(n-1) + ... + cn."""
    n = len(M)
    I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    Mk = [[Fr(0)] * n for _ in range(n)]
    coeffs = [Fr(1)]
    for k in range(1, n + 1):
        Mk = [[sum(Fr(M[i][t]) * Mk[t][j] for t in range(n)) + coeffs[-1] * I[i][j] for j in range(n)] for i in range(n)]
        AM = [[sum(Fr(M[i][t]) * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        coeffs.append(-sum(AM[i][i] for i in range(n)) / k)
    return coeffs


def polymul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def cycles_of(f):
    n, seen, cyc = len(f), set(), []
    for s in range(n):
        path, x = {}, s
        while x not in path and x not in seen:
            path[x] = len(path)
            x = f[x]
        if x in path:
            cyc.append(len(path) - path[x])
        seen |= set(path)
    return cyc


def check_c5(rng):
    ok = total = 0
    for _ in range(60):
        n = rng.randint(2, 8)
        f = [rng.randrange(n) for _ in range(n)]
        P = [[int(f[i] == j) for j in range(n)] for i in range(n)]
        cyc = cycles_of(f)
        pred = [Fr(1)]
        for L in cyc:
            pred = polymul(pred, [Fr(1)] + [Fr(0)] * (L - 1) + [Fr(-1)])
        pred = pred + [Fr(0)] * (n - sum(cyc))
        ok += charpoly(P) == pred
        total += 1
    report("C5 char poly of a program's 0/1 matrix == x^(n-c) prod (x^L - 1) over its cycles", ok == total,
           f"{ok} of {total} random maps on up to 8 states")
    # counterfactual: the same prediction with one cycle length off by one must fail
    f = [1, 2, 0, 0]
    P = [[int(f[i] == j) for j in range(4)] for i in range(4)]
    wrong = polymul([Fr(1), Fr(0), Fr(-1)], [Fr(1), Fr(0)])        # a 2-cycle claimed where there is a 3-cycle
    caught("a cycle length off by one in the predicted polynomial", charpoly(P) != wrong + [Fr(0)] * 0)


# ---- C6: Rule 30 ------------------------------------------------------------------------------------------------
def check_c6():
    table = {(l, c, r): (30 >> (4 * l + 2 * c + r)) & 1 for l, c, r in product((0, 1), repeat=3)}
    poly = {(l, c, r): (l + c + r + c * r) % 2 for l, c, r in product((0, 1), repeat=3)}
    report("C6 Rule 30 == l + c + r + c*r over GF(2) on all 8 neighbourhoods", table == poly)
    caught("Rule 90 (l + r) in place of Rule 30", {k: (k[0] + k[2]) % 2 for k in table} != table)
    n = 4096
    row, col = {0: 1}, []
    for t in range(n):
        col.append(row.get(0, 0))
        keys = range(min(row) - 1, max(row) + 2) if row else range(0)
        new = {}
        for x in keys:
            v = (row.get(x - 1, 0) + row.get(x, 0) + row.get(x + 1, 0) + row.get(x, 0) * row.get(x + 1, 0)) % 2
            if v:
                new[x] = 1
        row = new
    a051023 = ("1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,"
               "0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1")
    ref = [int(x) for x in a051023.split(",")]       # the DATA line of oeis.org/A051023, fetched 2026-10-04
    report("C6 the simulator reproduces OEIS A051023 (known answer)", col[:len(ref)] == ref, f"{len(ref)} terms")
    tail = col[1024:]
    periodic = [p for p in range(1, 1025) if all(tail[k] == tail[k + p] for k in range(len(tail) - p))]
    report("C6 Rule 30 centre column, steps 1024-4095: no period p <= 1024 (demonstration only)", not periodic,
           f"first 32 cells {''.join(map(str, col[:32]))}")


# ---- C7: the machine's arithmetic --------------------------------------------------------------------------------
def fl32(x):
    """Round an exact rational to the nearest float32, ties to even (normal range only; asserted)."""
    x = Fr(x)
    if x == 0:
        return Fr(0)
    s = -1 if x < 0 else 1
    a = abs(x)
    e = math.floor(math.log2(a.numerator) - math.log2(a.denominator))
    while Fr(2) ** e > a:
        e -= 1
    while Fr(2) ** (e + 1) <= a:
        e += 1
    assert -126 <= e <= 127, "outside the normal float32 range"
    q = a / Fr(2) ** (e - 23)                  # 2^23 <= q < 2^24
    n, r = divmod(q.numerator, q.denominator)
    rem = Fr(r, q.denominator)
    if rem > Fr(1, 2) or (rem == Fr(1, 2) and n % 2 == 1):
        n += 1
    return s * Fr(n) * Fr(2) ** (e - 23)


def rand32(rng):
    v = struct.unpack("f", struct.pack("f", rng.uniform(-1, 1) * 2.0 ** rng.randint(-20, 20)))[0]
    return Fr(v)


def two_sum(a, b):
    s = fl32(a + b)
    bp = fl32(s - a)
    ap = fl32(s - bp)
    db = fl32(b - bp)
    da = fl32(a - ap)
    return s, fl32(da + db)


def two_sum_fastmath(a, b):
    """TwoSum after a compiler applies real-number algebra: s - (s - b) == b, so the error term folds to zero."""
    s = fl32(a + b)
    return s, fl32(fl32(b - b) + fl32(a - a))


def check_c7(rng):
    a, b, c = Fr(2) ** 24, Fr(1), Fr(1)
    left, right = fl32(fl32(a + b) + c), fl32(a + fl32(b + c))
    report("C7 fl32 addition is not associative", left != right,
           f"(2^24 + 1) + 1 = {int(left)}, 2^24 + (1 + 1) = {int(right)}")
    exact = fast_ok = total = 0
    for _ in range(3000):
        x, y = rand32(rng), rand32(rng)
        s, e = two_sum(x, y)
        exact += (s + e == x + y)
        s2, e2 = two_sum_fastmath(x, y)
        fast_ok += (s2 + e2 == x + y)
        total += 1
    report("C7 TwoSum: a + b == s + e exactly, for every pair", exact == total, f"{exact} of {total} random float32 pairs")
    caught("TwoSum after fast-math simplification", fast_ok < total, f"exact on only {fast_ok} of {total}")


def main():
    rng = random.Random(20261004)
    check_c1_c2(rng)
    check_c3()
    check_c4(rng)
    check_c5(rng)
    check_c6()
    check_c7(rng)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
