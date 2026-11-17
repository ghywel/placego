#!/usr/bin/env python3
"""om186_influence.py: openai/math family 186, a uniform influence bound for symmetric Boolean properties.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om186_influence.py
COST:       about a minute.

The claim (preprint "A uniform influence bound for hypergraph properties", 2026-10-05). For r >= 3 there is C_r such
that every property f of r-uniform hypergraphs on n vertices (a Boolean function of the C(n, r) edge bits,
invariant under relabelling the vertices), at every edge probability 0 < p < 1, satisfies
    Var_p(f) <= C_r I_p(f) / (log n)^(r/(r-1)),        I_p(f) = sum over edges of P(flipping the edge changes f),
with no monotonicity needed. For increasing properties this gives the Friedgut-Kalai threshold width
p_(1-eps) - p_eps <= 2 C_r log((1-eps)/eps) / (log n)^(r/(r-1)).

Cloud read the whole proof (four short sections) and found it correct. Its steps that can be computed are checked
here by Cloud's own code:
  F1  the one-coordinate fourth-moment bound E(a + rho b chi)^4 <= (a^2 + b^2)^2 with rho = sigma/4, exactly on a
      grid of p, a, b;
  F2  the two-to-four bound ||T g||_4 <= ||g||_2 (T damps degree-j Fourier terms by rho^j) on random real g of up to
      6 bits at several p;
  F3  the weighted Parseval identity sum |S| f^(S)^2 = p(1-p) I_p(f), exactly, on random Boolean f;
  F4  every r-uniform hypergraph with s edges has a vertex of degree between 1 and r s^((r-1)/r): all 3-uniform
      hypergraphs on 6 vertices (2^20 of them);
  F5  the capture probability P(B meets the support only at u) >= m/(2n), exactly by counting, on small cases;
  F6  Margulis-Russo, q'(p) = I_p(f), exactly for every monotone function of 4 bits.
Predictions (written before the run): all pass. Fail: any inequality broken or identity off.
Unexpected check: the proof's constant is not numerical, because it takes n beyond some N_r. Cloud computes about
the least n from which the proof's four conditions hold, and so an explicit C_r, for r = 3 to 6. Guess before
the run: log N_3 lies between 40 and 60, so the proof only bites for n above about 10^17.
Control: F2's ratio is exactly 1 for constant g, and F5's count is checked against a direct enumeration.
Added after the first run, when Cloud read the graph companion ("A Sharp Threshold Bound for Monotone Graph
Properties"): F7 checks its explicit constants, Var <= 2^17 I / (log n)^2 for every n >= 2 and threshold width
<= 2^19 log(1/(2 eps)) / (log n)^2.
"""
import itertools, math, random
from fractions import Fraction as Fr


def f1():
    ok = True
    for p in [Fr(k, 20) for k in range(1, 20)]:
        sig2 = p * (1 - p)
        # chi takes (1-p)/sigma w.p. p and -p/sigma w.p. 1-p; with rho = sigma/4, rho chi takes (1-p)/4 or -p/4.
        for a, b in itertools.product([Fr(k, 4) for k in range(-8, 9)], repeat=2):
            lhs = p * (a + b * (1 - p) / 4) ** 4 + (1 - p) * (a - b * p / 4) ** 4
            ok &= lhs <= (a * a + b * b) ** 2
            bound = a ** 4 + Fr(13, 32) * sig2 * a * a * b * b + Fr(9, 256) * sig2 * b ** 4   # the preprint's middle
            ok &= lhs <= bound <= (a * a + b * b) ** 2
    return ok


def f2(rng):
    worst = 0.0
    for n in range(1, 7):
        N = 1 << n
        for p in (0.05, 0.2, 0.5, 0.8):
            sig = math.sqrt(p * (1 - p))
            rho = sig / 4
            w = [p ** bin(x).count("1") * (1 - p) ** (n - bin(x).count("1")) for x in range(N)]
            chi = [[math.prod(((((x >> i) & 1) - p) / sig) for i in range(n) if S >> i & 1) for x in range(N)]
                   for S in range(N)]
            for trial in range(6):
                g = [1.0] * N if trial == 0 else [rng.gauss(0, 1) for _ in range(N)]
                coef = [sum(w[x] * g[x] * chi[S][x] for x in range(N)) for S in range(N)]
                Tg = [sum(coef[S] * rho ** bin(S).count("1") * chi[S][x] for S in range(N)) for x in range(N)]
                n4 = sum(w[x] * Tg[x] ** 4 for x in range(N)) ** 0.25
                n2 = sum(w[x] * g[x] ** 2 for x in range(N)) ** 0.5
                if trial == 0:
                    assert abs(n4 / n2 - 1) < 1e-12                      # control: constants are fixed
                else:
                    worst = max(worst, n4 / n2)
    return worst


def f3(rng):
    ok = True
    for n in (2, 3, 4):
        N = 1 << n
        for _ in range(5):
            p = Fr(rng.randint(1, 9), 10)
            f = [rng.randint(0, 1) for _ in range(N)]
            w = [p ** bin(x).count("1") * (1 - p) ** (n - bin(x).count("1")) for x in range(N)]
            lhs = Fr(0)
            for S in range(1, N):
                c = sum(w[x] * f[x] * math.prod(Fr((x >> i) & 1) - p for i in range(n) if S >> i & 1)
                        for x in range(N))                               # sigma^|S| f^(S), rational
                lhs += bin(S).count("1") * c * c / (p * (1 - p)) ** bin(S).count("1")
            inf = sum(sum(w[x] + w[x | 1 << i] for x in range(N) if not x >> i & 1 and f[x] != f[x | 1 << i])
                      for i in range(n))
            ok &= lhs == p * (1 - p) * inf
    return ok


def f4():
    r, v = 3, 6
    edges = list(itertools.combinations(range(v), r))
    ok = True
    for mask in range(1, 1 << len(edges)):
        deg = [0] * v
        s = 0
        for i, e in enumerate(edges):
            if mask >> i & 1:
                s += 1
                for x in e:
                    deg[x] += 1
        cap = r * s ** ((r - 1) / r) + 1e-9
        ok &= any(1 <= d <= cap for d in deg)
    return ok


def f5():
    ok = True
    for n, m in [(12, 2), (15, 3), (20, 3), (30, 4)]:
        for vs in range(1, 6):
            V = list(range(vs))
            # exact P(B intersect V = {0}) for a uniform m-subset B of [n]
            exact = Fr(math.comb(n - vs, m - 1), math.comb(n, m))
            brute = Fr(sum(1 for B in itertools.combinations(range(n), m) if set(B) & set(V) == {0}),
                       math.comb(n, m)) if math.comb(n, m) < 50000 else exact
            assert exact == brute                                         # control
            if (vs - 1) * Fr(m - 1, n - 1) <= Fr(1, 2):
                ok &= exact >= Fr(m, 2 * n)
    return ok


def f6():
    n = 4
    N = 1 << n
    mono = [f for f in itertools.product((0, 1), repeat=N)
            if all(f[x] <= f[x | 1 << i] for x in range(N) for i in range(n))]
    ok = True
    for f in mono:
        for p in (Fr(1, 3), Fr(1, 2), Fr(5, 7)):
            # q(p) is a polynomial; differentiate term by term exactly
            dq = sum(f[x] * (k * p ** (k - 1) * (1 - p) ** (n - k) - (n - k) * p ** k * (1 - p) ** (n - k - 1))
                     for x in range(N) for k in [bin(x).count("1")])
            inf = Fr(0)
            for i in range(n):
                for x in range(N):
                    if not x >> i & 1 and f[x] != f[x | 1 << i]:
                        k = bin(x).count("1")                         # weight of the other coordinates
                        inf += p ** k * (1 - p) ** (n - 1 - k)
            ok &= dq == inf
    return ok, len(mono)


def threshold(r):
    """About the least n from which the proof's four conditions hold (on a grid of ratio 1.0023 up to 10^60, then
    refined by bisection). Approximate: the floor in m = isqrt(n) can flip a condition inside a grid step."""
    al = r / (r - 1)

    def conds(n):
        m = math.isqrt(n)
        L = math.log(n)
        return (m >= r + 1 and math.log(m) >= L / 3 and r * L ** al * n ** -0.5 <= 0.5
                and m ** -0.25 * L ** al <= 1)
    # scan log n on a grid to find the last failure, then refine by bisection on integers
    last_fail = 1
    for k in range(1, 60 * 1000):
        n = int(math.exp(k / 1000 * math.log(10) * 1.0) + 0.5)
        if not conds(n):
            last_fail = n
    lo, hi = last_fail, int(last_fail * 1.01) + 2
    while not all(conds(x) for x in range(hi, hi + 50)):
        hi = hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if all(conds(x) for x in (mid, mid + 1, mid + 2)):
            hi = mid
        else:
            lo = mid
    Nr = hi
    C = max(2 * r + (192 * r) ** al, math.log(Nr) ** al / 4)
    return Nr, C


def main():
    rng = random.Random(186)
    res = {"F1  one-coordinate fourth-moment bound, exact on a grid": f1()}
    worst = f2(rng)
    res["F2  two-to-four bound ||T g||_4 <= ||g||_2 on random g, up to 6 bits"] = worst <= 1 + 1e-12
    print(f"   worst ||Tg||_4 / ||g||_2 seen: {worst:.4f}")
    res["F3  weighted Parseval, exact"] = f3(rng)
    res["F4  degree lemma on all 2^20 3-uniform hypergraphs on 6 vertices"] = f4()
    res["F5  capture probability >= m/(2n) under the preprint's condition"] = f5()
    ok6, cnt = f6()
    res[f"F6  Margulis-Russo exact for all {cnt} monotone functions of 4 bits"] = ok6
    e = math.e
    ok7 = (256 * e ** -8 < 0.5 and 4 * 2 ** 0.25 * 256 * e ** -2 < 256 and 8192 * 9 == 73728
           and 73728 + 256 <= 2 ** 17 and 64 / 16 ** 2 >= 0.25 and 4 * 2 ** 17 == 2 ** 19
           and all(4 * ep * (1 - ep) <= 1 for ep in [Fr(k, 1000) for k in range(1, 500)])
           and all(math.log((1 - x) / x) <= 2 * math.log(1 / (2 * x)) + 1e-12
                   for x in [k / 1000 for k in range(1, 500)])
           and all((t * t * math.exp(-t / 8)) >= ((t + 0.5) ** 2 * math.exp(-(t + 0.5) / 8)) for t in range(16, 400))
           and all(m ** 0.5 / 2 <= math.isqrt(m) for m in range(4, 100000)))
    res["F7  the graph companion's explicit constants (2^17 and 2^19)"] = ok7
    for r in (3, 4, 5, 6):
        Nr, C = threshold(r)
        print(f"   r = {r}: the proof's conditions hold for good from n = {Nr:.3e} (log n = {math.log(Nr):.1f}); "
              f"explicit C_r = {C:.4g}")
        if r == 3:
            print(f"   guess (40 <= log N_3 <= 60): {'right' if 40 <= math.log(Nr) <= 60 else 'wrong'}")
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
