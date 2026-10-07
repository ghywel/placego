#!/usr/bin/env python3
"""om205_tensor_squares.py: openai/math family 205, universal tensor squares for the symmetric groups.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om205_tensor_squares.py [NMAX, default 24]
COST:       about a minute at NMAX = 24 (the character tables dominate; the time grows as their size squared).

The claim (preprint "Universal Tensor Squares for Symmetric Groups", 2026-09-24): for every n other than 2, 4 and 9
there is a partition lambda of n whose Kronecker coefficients g(lambda, lambda, nu) are all positive, that is, one
irreducible representation of S_n whose tensor square contains every irreducible. Its companion proves Saxl's
conjecture: the staircase (m, m-1, ..., 1) is such a lambda for every m. The proofs are long (recurrences,
pruning, analysis, and a C++ search to n = 64); Cloud has not reviewed them. What Cloud replicates here is the
finite core, by its own code: the character table by the Murnaghan-Nakayama rule, then
    g(lambda, mu, nu) = sum over cycle types rho of chi_lambda(rho) chi_mu(rho) chi_nu(rho) / z_rho,
with z_rho = prod_i i^(m_i) m_i!, for every n up to NMAX.
Predictions (written before the run): the n with no universal lambda are exactly 2, 4 and 9; every universal
lambda is self-conjugate (forced, since g(lambda, lambda, 1^n) = 1 only when lambda equals its transpose); the
staircase is universal for each triangular n up to NMAX. Fail: another exception, or a universal lambda at 2, 4 or 9.
Control: the column orthogonality of each table (sum over lambda of chi_lambda(rho)^2 = z_rho), and
g(lambda, lambda, (n)) = 1 for every lambda.
"""
import math, sys
from functools import lru_cache


def partitions(n, top=None):
    top = n if top is None else top
    if n == 0:
        yield ()
        return
    for k in range(min(n, top), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


@lru_cache(maxsize=None)
def chi(lam, mu):
    """Character of the irreducible lam at cycle type mu (both partitions of the same n), Murnaghan-Nakayama."""
    if not mu:
        return 1
    k, rest = mu[0], mu[1:]
    L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]           # distinct beads, decreasing
    bset, tot = set(beta), 0
    for b in beta:
        if b - k >= 0 and b - k not in bset:
            sign = (-1) ** sum(1 for c in beta if b - k < c < b)  # beads jumped = height of the rim hook
            nb = sorted((bset - {b}) | {b - k}, reverse=True)
            new = tuple(x for x in (nb[i] - (L - 1 - i) for i in range(L)) if x > 0)
            tot += sign * chi(new, rest)
    return tot


def z(rho):
    out = 1
    for i in set(rho):
        m = rho.count(i)
        out *= i ** m * math.factorial(m)
    return out


def transpose(lam):
    return tuple(sum(1 for x in lam if x > j) for j in range(lam[0])) if lam else ()


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    exceptions, staircase_ok, control_ok, selfconj_ok = [], True, True, True
    for n in range(1, nmax + 1):
        P = list(partitions(n))
        fac = math.factorial(n)
        w = {r: fac // z(r) for r in P}                        # class sizes
        table = {l: {r: chi(l, r) for r in P} for l in P}
        control_ok &= all(sum(table[l][r] ** 2 for l in P) == z(r) for r in P)

        def universal(l):
            a = {r: w[r] * table[l][r] ** 2 for r in P}
            gs = [sum(a[r] * table[nu][r] for r in P) for nu in P]
            assert all(g % fac == 0 and g >= 0 for g in gs) and gs[0] == fac  # control: trivial rep once
            return all(g > 0 for g in gs)                      # P[0] = (n), the trivial representation

        # The self-conjugate shortcut is proved (see the docstring); it is also tested on every lambda to n = 12.
        cands = P if n <= 12 else [l for l in P if l == transpose(l)]
        good = [l for l in cands if universal(l)]
        selfconj_ok &= all(l == transpose(l) for l in good)
        if not good:
            exceptions.append(n)
        m = int((math.isqrt(8 * n + 1) - 1) // 2)
        stair = tuple(range(m, 0, -1))
        tri = m * (m + 1) // 2 == n
        if tri:
            staircase_ok &= stair in good
        show = ", ".join("".join(map(str, l)) if max(l) < 10 else str(l) for l in good[:4])
        print(f"n = {n:2d}: {len(P):4d} partitions, {len(good):2d} universal"
              f"{' (none)' if not good else ': ' + show + (' ...' if len(good) > 4 else '')}"
              f"{'; staircase ' + ('universal' if stair in good else 'NOT universal') if tri else ''}")
    res = {
        "n with no universal tensor square are exactly 2, 4, 9": exceptions == [2, 4, 9],
        "every universal lambda found is self-conjugate": selfconj_ok,
        f"the staircase is universal for every triangular n <= {nmax}": staircase_ok,
        "control: column orthogonality of every character table, g(l, l, (n)) = 1": control_ok,
    }
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
