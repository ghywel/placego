#!/usr/bin/env python3
"""Cloud CL778, item Q: the uniform Pearson statistic on OVERLAPPING pairs, under its right reference law.

GPT's correction (GC2931): the pair tables of CL776/CL777 count overlapping pairs (c(t), c(t+1)).  For a fair
P-sided die the Pearson statistic of such a table against the uniform law is not chi-square with P^2 - 1 degrees of
freedom.  It is distributed as  X + 2 Y,  X ~ chi-square((P-1)^2),  Y ~ chi-square(P-1), independent
(I. J. Good, The serial test for sampling numbers and other tests for randomness, Proc. Cambridge Philos. Soc. 49
(1953) 276-284: psi^2_2 - 2 psi^2_1 and psi^2_1 are asymptotically independent chi-squares; GPT's hand decomposition
into row/column modes and interaction modes says the same).  Mean P^2 - 1 as before, variance 2(P-1)^2 + 8(P-1)
instead of 2(P^2 - 1).

This probe (1) checks that law on simulated fair dice, (2) recomputes the tail of every raw pair table saved by
cloud_lift_centre_modp.c under the right law, next to the naive one, and Good's two differences.
Prediction (CL778, before the run): every published raw-pair tail moves toward one half; the value at 7 on the first
2^16 ticks, published as 0.018, lands between 0.02 and 0.06; no corrected value is below 0.01.
Usage: cloud_pair_reference.py P RAWFILE [P RAWFILE]...
"""
import importlib.util, math, pathlib, sys
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lift", here / "cloud_integer_lift_primes.py")
lift = importlib.util.module_from_spec(spec); spec.loader.exec_module(lift)


def chi2_tail(dof, x):
    return 1.0 if x <= 0 else lift.gammq(dof / 2, x / 2)


def mixture_tail(P, x, steps=4000):
    """P(X + 2Y > x), X ~ chi2((P-1)^2), Y ~ chi2(P-1): Simpson's rule in y on [0, x/2], plus P(Y > x/2)."""
    a, b = (P - 1) ** 2, P - 1
    lg = math.lgamma(b / 2) + (b / 2) * math.log(2)
    dens = lambda y: 0.0 if y <= 0 and b > 2 else math.exp((b / 2 - 1) * math.log(y) - y / 2 - lg) if y > 0 else 0.5
    h = (x / 2) / steps
    tot = 0.0
    for i in range(steps + 1):
        y = i * h
        w = 1 if i in (0, steps) else (4 if i % 2 else 2)
        tot += w * dens(y) * chi2_tail(a, x - 2 * y)
    return chi2_tail(b, x / 2) + tot * h / 3


def stats(tab, P):
    tab = np.asarray(tab, dtype=np.float64).reshape(P, P)
    n = tab.sum()
    psi2 = float(((tab - n / P ** 2) ** 2 / (n / P ** 2)).sum())
    row = tab.sum(axis=1)                               # first members: the single-symbol counts, up to one end term
    psi1 = float(((row - n / P) ** 2 / (n / P)).sum())
    return int(n), psi2, psi1


def simulate(P, n, trials, rng):
    vals = np.empty(trials)
    for i in range(trials):
        a = rng.integers(0, P, size=n, dtype=np.int64)
        tab = np.bincount(a[:-1] * P + a[1:], minlength=P * P)
        vals[i] = stats(tab, P)[1]
    return vals


def main():
    print("== 1. the law on simulated fair dice (2^16 ticks each)")
    rng = np.random.default_rng(20261111)
    for P, trials in ((3, 4000), (5, 4000), (7, 4000)):
        v = simulate(P, 1 << 16, trials, rng)
        dof = P * P - 1
        var_right = 2 * (P - 1) ** 2 + 8 * (P - 1)
        q = np.quantile(v, 0.98)
        emp = float((v > q).mean())
        print(f"   P = {P}: {trials} dice | mean {v.mean():.2f} (law {dof}) | variance {v.var():.1f} (right law {var_right}, naive {2 * dof})"
              f" | at the empirical 98th centile {q:.1f}: right law tail {mixture_tail(P, q):.4f}, naive tail {chi2_tail(dof, q):.4f}, empirical {emp:.4f}")
        for level in (0.05, 0.01):
            # how often the naive reference cries wolf at this level, against the right one
            naive = float(np.mean([chi2_tail(dof, x) < level for x in v]))
            right = float(np.mean([mixture_tail(P, x, 400) < level for x in v[:1000]]))
            print(f"        rejections at level {level}: naive reference {naive:.4f}, right reference {right:.4f} (first 1000 dice)")
    print("== 2. the saved pair tables of the lift's centre, recomputed")
    worst = 1.0; moved = []
    args = sys.argv[1:]
    for i in range(0, len(args), 2):
        P = int(args[i]); path = pathlib.Path(args[i + 1])
        for line in path.read_text().splitlines():
            w = line.split()
            if not w or w[0] not in ("segpairs", "pairs"):
                continue
            tab = [int(x) for x in w[4:]]
            n, psi2, psi1 = stats(tab, P)
            dof = P * P - 1
            naive = chi2_tail(dof, psi2); right = mixture_tail(P, psi2)
            d2 = psi2 - 2 * psi1; d1 = psi2 - psi1
            print(f"   modulo {P}, {w[0]} {w[1]}..{w[2]} ({n} pairs): uniform statistic {psi2:.2f} | naive tail on {dof} dof {naive:.4f}"
                  f" | right tail {right:.4f} | Good: psi2 - 2 psi1 = {d2:.2f} on {(P - 1) ** 2} dof, tail {chi2_tail((P - 1) ** 2, d2):.4f};"
                  f" psi2 - psi1 = {d1:.2f} on {P * P - P} dof, tail {chi2_tail(P * P - P, d1):.4f}")
            worst = min(worst, right, 1 - right)
            moved.append(abs(right - 0.5) <= abs(naive - 0.5) + 1e-12)
    if moved:
        print(f"Q: every right-law tail is at least as close to one half as the naive one: {all(moved)} ({sum(moved)} of {len(moved)})")
        print(f"Q: smallest right-law tail (either side) over all tables: {worst:.4f}; none below 0.01: {worst >= 0.01}")


if __name__ == "__main__":
    main()
