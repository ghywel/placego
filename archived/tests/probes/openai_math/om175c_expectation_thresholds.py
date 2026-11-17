#!/usr/bin/env python3
"""om175c_expectation_thresholds.py: openai/math family 175, integral and fractional expectation thresholds agree
within the factor 25 * 512^4 (Talagrand's Conjecture 6.3).

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om175c_expectation_thresholds.py
COST:       a few minutes (the exact thresholds of every increasing family on 4 elements dominate).

The claim (preprint "Integral and fractional expectation thresholds are equivalent", 2026-09-23). For an increasing
family F of subsets of a finite set X (not empty, not everything), the integral expectation threshold q(F) is the
largest p at which some family G, with sum over G of p^|S| <= 1/2, has a member inside every set of F; the fractional
threshold q_f(F) allows weights g(S) in [0, 1] with sum over S inside H of g(S) >= 1 for H in F and
sum g(S) p^|S| <= 1/2. Theorem: q_f(F) <= 25 * 512^4 * q(F), with no dependence on |X| or set sizes.

Cloud read the whole proof (a multiscale selector estimate, then a rounding by random colours) and found it correct.
The selector's hypothesis cannot hold on small ground sets (every family on 4 elements is p-small once p < 1/32), so
its probability bound has no small instance. Checks by Cloud's own code:
  T1  the maximal-truncation lemma: the largest admissible cutoff eps has |{x : lambda(x) > eps}| <= m/d, exactly on
      random instances;
  T2  the likelihood identity p^t P(a) = P(z) prod (p/pi_i)^(t_i) prod pi_h^(n_ih), exactly on random colourings;
  T3  the average-colour identity sum a(x) lambda(x) = 1 + sum (1 - lambda(A_i)), exactly;
  T4  the weighted AM-GM step prod (2^-i / alpha_i)^(alpha_i) <= sum 2^-i, on random profiles;
  T5  the constants: rho = sum e/64^i < e/63 < 1/21, rho/(1 - rho) < 1/20, mean of Y <= 5 B^4 p, 9/40 > 1/10.
Predictions (written before the run): all pass.
Unexpected check: exact q and q_f (an exact simplex for the fractional cover, enumeration for the integral one) for
every nonempty proper increasing family on 1 to 4 elements, and the largest ratio q_f/q. Cloud's guess before the
run: at most 2 on these small ground sets, against the theorem's allowance of about 1.7e12.
Control: q <= q_f for every family, and the family of all nonempty sets on n elements has q = q_f = 1/(2n).
"""
import itertools, math, random
from fractions import Fraction as Fr


def truncation_ok(rng):
    for _ in range(300):
        n = rng.randint(1, 7)
        w = [rng.randint(0, 9) for _ in range(n)]
        if sum(w) == 0:
            continue
        lam = [Fr(x, sum(w)) for x in w]
        A = {i for i in range(n) if rng.random() < 0.7}
        m = rng.randint(0, 3)
        d = Fr(rng.randint(1, 9), 10)

        def f(u):
            return sum(min(l, u) * ((1 if i in A else 0) - (1 - d)) for i, l in enumerate(lam)) - m * u

        lo = max([lam[i] for i in range(n) if i not in A] + [Fr(0)])
        # f is piecewise linear with breaks at the weights: test every breakpoint and every segment's end
        pts = sorted({lo, Fr(1)} | {l for l in lam if l >= lo})
        adm = [u for u in pts if f(u) >= 0]
        if not adm:
            continue
        # the largest admissible cutoff lies at a breakpoint or inside a segment where f crosses zero
        best = max(adm)
        for a, b in zip(pts, pts[1:]):
            if f(a) >= 0 > f(b):
                best = max(best, a + f(a) * (b - a) / (f(a) - f(b)))
        R = [l for l in lam if l > best]
        if d * len(R) > m:
            return False
    return True


def likelihood_ok(rng):
    for _ in range(200):
        s = rng.randint(1, 3)
        p = Fr(1, rng.randint(600, 2000))
        D = 256
        if p * sum(D ** i for i in range(1, s + 1)) > Fr(1, 2):
            continue
        pi = {i: D ** i * p for i in range(1, s + 1)}
        pi[s + 1] = 1 - p * sum(D ** i for i in range(1, s + 1))
        n = rng.randint(1, 6)
        a = [rng.randint(1, s + 1) for _ in range(n)]
        z = [rng.randint(1, ai) for ai in a]
        t = {i: sum(1 for x in range(n) if z[x] == i < a[x]) for i in range(1, s + 1)}
        nih = {(i, h): sum(1 for x in range(n) if z[x] == i and a[x] == h) for i in range(1, s + 1)
               for h in range(i + 1, s + 2)}
        P = lambda c: math.prod(pi[v] for v in c)
        lhs = p ** sum(t.values()) * P(a)
        rhs = P(z) * math.prod((p / pi[i]) ** t[i] for i in t) * math.prod(pi[h] ** k for (i, h), k in nih.items())
        if lhs != rhs:
            return False
    return True


def colour_identity_ok(rng):
    for _ in range(200):
        s, n = rng.randint(0, 4), rng.randint(1, 6)
        w = [rng.randint(1, 9) for _ in range(n)]
        lam = [Fr(x, sum(w)) for x in w]
        a = [rng.randint(1, s + 1) for _ in range(n)]
        lhs = sum(ai * l for ai, l in zip(a, lam))
        rhs = 1 + sum(1 - sum(l for ai, l in zip(a, lam) if ai <= i) for i in range(1, s + 1))
        if lhs != rhs:
            return False
    return True


def amgm_ok(rng):
    for _ in range(2000):
        s = rng.randint(1, 8)
        t = [rng.randint(0, 5) for _ in range(s)]
        T = sum(t)
        if T == 0:
            continue
        lhs = math.prod((2.0 ** -(i + 1) / (ti / T)) ** (ti / T) for i, ti in enumerate(t) if ti)
        if lhs > sum(2.0 ** -(i + 1) for i, ti in enumerate(t) if ti) + 1e-12:
            return False
    return True


def constants_ok():
    # rho = e * sum_{i<=s} 64^-i. Exactly: the finite sum is below 1/63 for every s, and e < 3 gives e/63 < 1/21
    # and (e/63)/(1 - e/63) < 1/20 (that is 21 e < 63). (The first run compared floats, whose sum rounds to e/63
    # itself, and failed on that rounding.)
    D, B = 256, 512
    ok = (all(sum(Fr(1, 64 ** i) for i in range(1, s + 1)) < Fr(1, 63) for s in range(1, 60))
          and math.e < 3 and 21 * math.e < 63 and Fr(9, 40) > Fr(1, 10))
    # mean of Y at the extreme s allowed by p, for a range of p: mu <= 5 B^4 p
    for p in [Fr(1, k) for k in (600, 10 ** 4, 10 ** 6, 10 ** 9)]:
        s = 0
        while p * sum(D ** i for i in range(1, s + 2)) <= Fr(1, 2):
            s += 1
        pi_last = 1 - p * sum(D ** i for i in range(1, s + 1))
        mu = B ** 4 * (p * sum(Fr(D, B) ** i for i in range(1, s + 1)) + pi_last * Fr(1, B ** (s + 1)))
        ok &= mu <= 5 * B ** 4 * p and Fr(1, D ** (s + 1)) < 4 * p
    return ok


def simplex_max(c, A, b):
    """max c.y subject to A y <= b, y >= 0, with b >= 0 (Bland's rule, exact). Returns the optimum."""
    m, n = len(A), len(c)
    T = [list(map(Fr, A[i])) + [Fr(int(i == j)) for j in range(m)] + [Fr(b[i])] for i in range(m)]
    obj = [-Fr(x) for x in c] + [Fr(0)] * m + [Fr(0)]
    basis = [n + i for i in range(m)]
    while True:
        col = next((j for j in range(n + m) if obj[j] < 0), None)
        if col is None:
            return obj[-1]
        rows = [(T[i][-1] / T[i][col], basis[i], i) for i in range(m) if T[i][col] > 0]
        if not rows:
            raise ValueError("unbounded")
        _, _, r = min(rows)
        piv = T[r][col]
        T[r] = [x / piv for x in T[r]]
        for i in range(m):
            if i != r and T[i][col] != 0:
                f = T[i][col]
                T[i] = [x - f * y for x, y in zip(T[i], T[r])]
        f = obj[col]
        obj = [x - f * y for x, y in zip(obj, T[r])]
        basis[r] = col


def frac_cost(minimal, n, p):
    """Minimum fractional cover cost at p, by LP duality: max sum y_H s.t. sum over H containing S of y_H <= p^|S|."""
    subsets = range(1 << n)
    A = [[1 if (S & H) == S else 0 for H in minimal] for S in subsets]
    b = [p ** bin(S).count("1") for S in subsets]
    return simplex_max([1] * len(minimal), A, b)


def integral_profiles(minimal, n):
    """Pareto-minimal size profiles (c_1..c_n) of integral covers (generators are nonempty sets)."""
    cands = [S for S in range(1, 1 << n) if any((S & H) == S for H in minimal)]
    full = (1 << len(minimal)) - 1
    cov = [sum(1 << k for k, H in enumerate(minimal) if (S & H) == S) for S in cands]
    best = set()
    # enumerate covers by depth-first search on candidates in order, pruning covered states
    def rec(i, mask, prof):
        if mask == full:
            best.add(tuple(prof))
            return
        if i == len(cands):
            return
        rec(i + 1, mask, prof)
        if cov[i] & ~mask:
            prof2 = list(prof)
            prof2[bin(cands[i]).count("1") - 1] += 1
            rec(i + 1, mask | cov[i], prof2)
    rec(0, 0, [0] * n)
    return [pr for pr in best if not any(o != pr and all(x <= y for x, y in zip(o, pr)) for o in best)]


def threshold(cost, steps=40):
    lo, hi = Fr(0), Fr(1)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if cost(mid) <= Fr(1, 2):
            lo = mid
        else:
            hi = mid
    return lo


def families(n):
    """Minimal-member antichains of the nonempty proper increasing families on n elements."""
    sets = list(range(1, 1 << n))
    out = set()
    for k in range(1, len(sets) + 1):
        for anti in itertools.combinations(sets, k):
            if all((a & b) != a and (a & b) != b for a, b in itertools.combinations(anti, 2)):
                out.add(anti)
        if k > 6:
            break
    return sorted(out)


def main():
    rng = random.Random(1753)
    res = {"T1  maximal truncation |R| <= m/d": truncation_ok(rng),
           "T2  likelihood identity": likelihood_ok(rng),
           "T3  average-colour identity": colour_identity_ok(rng),
           "T4  weighted AM-GM step": amgm_ok(rng),
           "T5  constants": constants_ok()}
    worst, ok_order, count, worst_fam = Fr(1), True, 0, None
    for n in range(1, 5):
        for minimal in families(n):
            count += 1
            qf = threshold(lambda p: frac_cost(minimal, n, p))
            profs = integral_profiles(minimal, n)
            q = threshold(lambda p: min(sum(c * p ** (k + 1) for k, c in enumerate(pr)) for pr in profs))
            ok_order &= q <= qf + Fr(1, 2 ** 38)
            if q > 0 and qf / q > worst:
                worst, worst_fam = qf / q, (n, minimal)
    allsets = threshold(lambda p: frac_cost([1], 1, p))
    ctl = abs(float(allsets) - 0.5) < 1e-9 and all(
        abs(float(threshold(lambda p: frac_cost([1 << i for i in range(n)], n, p))) - 1 / (2 * n)) < 1e-9
        for n in (2, 3, 4))
    res["    control: q <= q_f everywhere, and q_f = 1/(2n) for all nonempty sets"] = ok_order and ctl
    print(f"   {count} increasing families on 1 to 4 elements; largest q_f/q = {float(worst):.4f}, "
          f"at n = {worst_fam[0]} with minimal members {[bin(h)[2:].zfill(worst_fam[0]) for h in worst_fam[1]]}")
    print(f"   guess (largest ratio at most 2): {'right' if worst <= 2 else 'wrong'}")
    res["    the theorem's bound q_f <= 25 * 512^4 q holds on every small family"] = worst <= 25 * 512 ** 4
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
