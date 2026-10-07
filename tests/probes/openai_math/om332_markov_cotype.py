#!/usr/bin/env python3
"""om332_markov_cotype.py: openai/math family 332, l_1 has metric Markov cotype two, with constant 12 sqrt 21.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om332_markov_cotype.py
COST:       about a minute (exact rational arithmetic throughout).

The claim (preprint "Metric Markov Cotype Two of l1", 2026-10-05). For every finite stationary Markov chain (A, pi)
(reversible or not), every t >= 1 and every points x_1..x_n in l_1, there are points y_1..y_n in l_1 with
    sum_i pi_i |x_i - y_i|^2 + t sum_ij pi_i a_ij |y_i - y_j|^2
        <= 3024 sum_ij pi_i ((1/t) sum_{s<=t} A^s)_ij |x_i - x_j|^2,
norms in l_1. This answers Mendel and Naor's question; through their theorem it solves Ball's extension problem for
maps from subsets of Hilbert space into l_1. The y_i are explicit: y_i is the expected coordinatewise median of three
independent endpoints of a walk from i stopped after a geometric number of steps of mean t.

Cloud read the whole proof (a cut representation, a cubic flattening phi(r) = 3r^2 - 2r^3 with a quartic potential,
a geometric-versus-Cesaro comparison, a killed-walk martingale) and found it correct. Checks by Cloud's own code:
  M1  the cut representation: |x_i - x_j|_1 = sum_B w_B |z_i(B) - z_j(B)| and T(z_i) = x_i, exactly;
  M2  the flattening lemma |Phi(u') - Phi(u)|_{1,w}^2 <= 108 (F_e(u') - F_e(u) - 4|a|^2 <a, delta>), and its exact
      remainder identity R = 2|a|^2|delta|^2 + (2<a, delta> + |delta|^2)^2;
  M3  the comparison E d(x_{X_S}, x_{X_0})^2 <= (28/t) sum_{s<=t} E d(x_{X_s}, x_{X_0})^2, exactly on random chains;
  M4  the expected-median formula y_i = T(Phi(h_i)), against a direct sum over all triples of endpoints, exactly;
  M5  the theorem itself on random chains, points and t, exactly: the ratio of the two sides is at most 3024;
  M6  the constants: E S^2 = 2t^2 + t, q^t <= 1/2, 2*3*4 + 2*2 = 28, 108 * 28 = 3024 = (12 sqrt 21)^2.
Predictions (written before the run): all pass.
Unexpected check: the largest ratio of the two sides of the theorem over the random instances. Cloud's guess before
the run: below 50, so the constant 3024 is very loose in practice.
Control: with y = x the left side is t times the one-step energy, which can exceed the right side's 3024 multiple
only if the chain mixes slowly; M5 also reports that ratio, to show the y's are doing the work.
"""
import itertools, random
from fractions import Fraction as Fr


def cuts(xs):
    n, k = len(xs), len(xs[0])
    v = [min(x[c] for x in xs) for c in range(k)]
    out = []
    for r in range(1, n):
        for B in itertools.combinations(range(n), r):
            Bs = set(B)
            b = [max(min(xs[i][c] for i in B) - max(xs[i][c] for i in range(n) if i not in Bs), 0) for c in range(k)]
            if sum(b) > 0:
                out.append((Bs, b))
    return v, out


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def phi(r):
    return 3 * r * r - 2 * r ** 3


def matinv(M):
    n = len(M)
    A = [list(map(Fr, row)) + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def random_chain(rng, n, reversible):
    if reversible:
        W = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                W[i][j] = W[j][i] = rng.choice([0, 0, 1, 2, 3])
            W[i][i] += 1
        tot = sum(map(sum, W))
        pi = [Fr(sum(W[i]), tot) for i in range(n)]
        A = [[Fr(W[i][j], sum(W[i])) for j in range(n)] for i in range(n)]
    else:                                              # a doubly stochastic chain: uniform pi is stationary
        perms = [rng.sample(range(n), n) for _ in range(3)]
        wts = [Fr(rng.randint(1, 4)) for _ in range(3)]
        A = [[sum(w for w, P in zip(wts, perms) if P[i] == j) / sum(wts) for j in range(n)] for i in range(n)]
        pi = [Fr(1, n)] * n
    return A, pi


def sides(A, pi, xs, t, ys):
    n = len(A)
    P = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    ces = [[Fr(0)] * n for _ in range(n)]
    for _ in range(t):
        P = matmul(P, A)
        ces = [[c + p / t for c, p in zip(cr, pr)] for cr, pr in zip(ces, P)]
    rhs = sum(pi[i] * ces[i][j] * l1(xs[i], xs[j]) ** 2 for i in range(n) for j in range(n))
    lhs = (sum(pi[i] * l1(xs[i], ys[i]) ** 2 for i in range(n))
           + t * sum(pi[i] * A[i][j] * l1(ys[i], ys[j]) ** 2 for i in range(n) for j in range(n)))
    return lhs, rhs


def construct(A, xs, t):
    n = len(A)
    p = Fr(1, t + 1)
    q = 1 - p
    G = [[p * g for g in row] for row in matinv([[Fr(int(i == j)) - q * A[i][j] for j in range(n)] for i in range(n)])]
    v, cs = cuts(xs)
    ys = []
    for i in range(n):
        y = list(v)
        for B, b in cs:
            h = sum(G[i][j] for j in B)
            y = [yc + phi(h) * bc for yc, bc in zip(y, b)]
        ys.append(y)
    return G, ys


def main():
    rng = random.Random(332)
    res = {}
    ok1 = True
    for _ in range(100):
        n, k = rng.randint(2, 6), rng.randint(1, 4)
        xs = [[rng.randint(-5, 5) for _ in range(k)] for _ in range(n)]
        v, cs = cuts(xs)
        for i, j in itertools.combinations(range(n), 2):
            ok1 &= l1(xs[i], xs[j]) == sum(sum(b) * ((i in B) != (j in B)) for B, b in cs)
        for i in range(n):
            ok1 &= [vc + sum(bc for B, bb in cs if i in B for bc in [bb[c]]) for c, vc in enumerate(v)] == xs[i]
    res["M1  cut representation, exact"] = ok1
    ok2 = True
    for _ in range(3000):
        m = rng.randint(1, 5)
        w = [Fr(rng.randint(1, 5)) for _ in range(m)]
        u = [Fr(rng.randint(0, 20), 20) for _ in range(m)]
        up = [Fr(rng.randint(0, 20), 20) for _ in range(m)]
        e = [rng.randint(0, 1) for _ in range(m)]
        a = [x - y for x, y in zip(u, e)]
        dl = [x - y for x, y in zip(up, u)]
        ip = lambda X, Y: sum(wb * x * y for wb, x, y in zip(w, X, Y))
        F = lambda X: ip([x - y for x, y in zip(X, e)], [x - y for x, y in zip(X, e)]) ** 2
        R = F(up) - F(u) - 4 * ip(a, a) * ip(a, dl)
        ok2 &= R == 2 * ip(a, a) * ip(dl, dl) + (2 * ip(a, dl) + ip(dl, dl)) ** 2
        lhs = sum(wb * abs(phi(x) - phi(y)) for wb, x, y in zip(w, up, u)) ** 2
        ok2 &= lhs <= 108 * R
    res["M2  flattening lemma and its exact remainder"] = ok2
    ok3, ok4, worst, worst_ctl = True, True, Fr(0), Fr(0)
    for trial in range(60):
        n, k = rng.randint(2, 5), rng.randint(1, 3)
        A, pi = random_chain(rng, n, reversible=trial % 2 == 0)
        assert all(sum(pi[i] * A[i][j] for i in range(n)) == pi[j] for j in range(n))
        xs = [[rng.randint(-4, 4) for _ in range(k)] for _ in range(n)]
        t = rng.choice([1, 2, 3, 5, 8])
        G, ys = construct(A, xs, t)
        geo = sum(pi[i] * G[i][j] * l1(xs[i], xs[j]) ** 2 for i in range(n) for j in range(n))
        _, rhs = sides(A, pi, xs, t, xs)
        ok3 &= geo <= 28 * rhs
        if trial < 20:                                   # M4: the expected median, directly over all triples
            for i in range(n):
                med = [Fr(0)] * k
                for J in itertools.product(range(n), repeat=3):
                    pr = G[i][J[0]] * G[i][J[1]] * G[i][J[2]]
                    med = [m + pr * sorted(xs[j][c] for j in J)[1] for c, m in enumerate(med)]
                ok4 &= med == ys[i]
        lhs, rhs = sides(A, pi, xs, t, ys)
        if rhs > 0:
            worst = max(worst, lhs / rhs)
            l0, _ = sides(A, pi, xs, t, xs)
            worst_ctl = max(worst_ctl, l0 / rhs)
        else:
            ok3 &= lhs == 0
    res["M3  geometric-versus-Cesaro comparison with 28"] = ok3
    res["M4  y_i is the expected median of three geometric endpoints"] = ok4
    res["M5  the theorem's inequality, ratio <= 3024"] = worst <= 3024
    print(f"   largest ratio (left side / right side) over 60 random instances: {float(worst):.3f}; "
          f"with y = x instead: {float(worst_ctl):.3f}")
    print(f"   guess (largest ratio below 50): {'right' if worst < 50 else 'wrong'}")
    ok6 = True
    for t in range(1, 200):
        p = Fr(1, t + 1)
        q = 1 - p
        ES2 = q / p ** 2 + (q / p) ** 2
        ok6 &= ES2 == 2 * t * t + t and q ** t <= Fr(1, 2) and p * q ** 0 / (1 - q ** t) <= Fr(2, t)
    ok6 &= 2 * 3 * 4 + 2 * 2 == 28 and 108 * 28 == 3024 == 144 * 21
    res["M6  constants"] = ok6
    for k_, v in res.items():
        print(("PASS " if v else "FAIL ") + k_)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
