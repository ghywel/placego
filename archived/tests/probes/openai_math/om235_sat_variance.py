#!/usr/bin/env python3
"""om235_sat_variance.py: openai/math family 235, the random 3-SAT hitting time has variance Theta(n).

RUN-ON:     cpu (Python 3; the simulation needs python-sat: pip install python-sat)
COMMAND:    python3 tests/probes/openai_math/om235_sat_variance.py
COST:       a few minutes (the simulation dominates).

The claim (preprint "Linear Variance of the Random 3-SAT Hitting Time", 2026-10-05). Add independent uniform proper
3-clauses on n variables until the formula first becomes unsatisfiable; call that index H_n. Then Var(H_n) <= C n
for an absolute C, and (with Wilson's 2002 window theorem) Var(H_n) >= c n for large n; so the window in which
satisfiability falls from 1 - eta to eta has width Theta(sqrt n). The earlier bound was O(n log n).

Cloud read the whole proof of the upper bound (a potential for killing assignment sets, Efron-Stein by clause
omission, independent root-flip tests, an occupation estimate) and found it correct, constants included. The lower
bound uses Wilson's theorem as a cited input, not reproved. Checks by Cloud's own code:
  P1  the one-clause comparison h_2(S)^(3/2) <= 3 h_3(S) + u^-3, with h_a = (b)_a / (2^a (u)_a) for b frozen
      coordinates, exactly for every 0 <= b <= u <= 300;
  P2  the potential-drift inequality 1{S nonempty} q_d(S)^(3/2) <= d^(1/2) (3 E[P_d(S[C]) - P_d(S)] + d u^-3),
      exactly for random assignment sets S on u = 3 and 4 variables and d = 1..4, by exact dynamic programming over
      surviving sets;
  P3  the tail constants: sum (2j+1)(7/8)^j = 120 and 2 (7/8)^10 < 1;
  S   a simulation, not a proof: Var(H_n) / n for n = 20, 40, 80, 160, 300 samples each (binary search on the first
      unsatisfiable prefix, Glucose through python-sat).
Predictions (written before the run): P1 to P3 pass. For S, the ratio Var(H_n)/n stays within a factor of 2 across
the five sizes, and E H_n / n approaches the threshold near 4.27 from above (finite-size effects).
Unexpected check: Cloud's guess before the run, loosely held: Var(H_n)/n lies between 1 and 30 at every size.
Control: P2's dynamic programme reproduces q_1 = h_2 exactly, and the simulation's hitting index is re-checked by
two extra solves (unsatisfiable at H, satisfiable at H - 1).
"""
import itertools, math, random, statistics, sys
from fractions import Fraction as Fr


def falling(t, a):
    out = 1
    for k in range(a):
        out *= t - k
    return out


def p1():
    for u in range(3, 301):
        for b in range(0, u + 1):
            h2 = Fr(falling(b, 2), 4 * falling(u, 2))
            h3 = Fr(falling(b, 3), 8 * falling(u, 3))
            if h2 ** 3 > (3 * h3 + Fr(1, u ** 3)) ** 2:
                return False
    return True


def clauses(u, a):
    out = []
    for vs in itertools.combinations(range(u), a):
        for signs in itertools.product((0, 1), repeat=a):
            out.append(tuple(zip(vs, signs)))            # literal (v, s) is satisfied when z_v == s
    return out


def survive(S, c):
    return frozenset(z for z in S if any((z >> v & 1) == s for v, s in c))


def q_table(S, u, dmax):
    """q_j(S) for j = 0..dmax: probability that j random proper 2-clauses leave nothing of S."""
    two = clauses(u, 2)
    dist = {frozenset(S): Fr(1)}
    out = []
    for j in range(dmax + 1):
        out.append(dist.get(frozenset(), Fr(0)))
        new = {}
        for T, pr in dist.items():
            for c in two:
                R = survive(T, c)
                new[R] = new.get(R, 0) + pr / len(two)
        dist = new
    return out


def p2(rng):
    ok = True
    for u in (3, 4):
        three = clauses(u, 3)
        for _ in range(12):
            S = frozenset(z for z in range(1 << u) if rng.random() < rng.choice([0.2, 0.4, 0.7]))
            if not S:
                continue
            dmax = 4
            q = q_table(S, u, dmax)
            # control: q_1 equals h_2, from the frozen-coordinate formula
            b = sum(1 for v in range(u) if len({z >> v & 1 for z in S}) == 1)
            ok &= q[1] == Fr(falling(b, 2), 4 * falling(u, 2))
            qC = [q_table(survive(S, c), u, dmax) for c in three]
            for d in range(1, dmax + 1):
                P = sum(q[:d])
                EPC = sum(sum(t[:d]) for t in qC) / len(three)
                lhs = q[d] ** 3                              # compare squares of q^(3/2) and the right side
                rhs = (Fr(d) * (3 * (EPC - P) + Fr(d, u ** 3)) ** 2)  # (d^(1/2) x)^2 = d x^2
                ok &= lhs <= rhs
    return ok


def simulate(rng, sizes, samples):
    from pysat.solvers import Solver
    rows = []
    for n in sizes:
        hs = []
        for _ in range(samples):
            cl = []
            for _ in range(12 * n):
                vs = rng.sample(range(1, n + 1), 3)
                cl.append([v if rng.random() < 0.5 else -v for v in vs])

            def sat(m):
                with Solver(name="glucose4", bootstrap_with=cl[:m]) as s:
                    return s.solve()
            lo, hi = 0, 12 * n                               # sat(lo) is True; find the first m with sat(m) False
            assert not sat(hi), "12n clauses still satisfiable"
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if sat(mid):
                    lo = mid
                else:
                    hi = mid
            assert not sat(hi) and sat(hi - 1)               # control
            hs.append(hi)
        rows.append((n, statistics.mean(hs) / n, statistics.variance(hs) / n))
    return rows


def main():
    rng = random.Random(235)
    res = {"P1  one-clause comparison, exact for all b <= u <= 300": p1(),
           "P2  potential-drift inequality, exact on random sets (u = 3, 4; d = 1..4)": p2(rng),
           "P3  tail constants": (sum((2 * j + 1) * Fr(7, 8) ** j for j in range(2000)) < 120
                                  < sum((2 * j + 1) * Fr(7, 8) ** j for j in range(2000)) + Fr(1, 10 ** 30)
                                  and 2 * Fr(7, 8) ** 10 < 1)}
    rows = simulate(rng, (20, 40, 80, 160), 300)
    for n, m, v in rows:
        print(f"   n = {n:3d}: E H / n = {m:.3f}, Var H / n = {v:.2f}")
    ratios = [v for _, _, v in rows]
    res["S   Var(H_n)/n within a factor 2 across sizes (simulation, not proof)"] = max(ratios) <= 2 * min(ratios)
    print(f"   guess (1 <= Var/n <= 30 at every size): {'right' if all(1 <= v <= 30 for v in ratios) else 'wrong'}")
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
