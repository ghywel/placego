#!/usr/bin/env python3
"""om175_discrete_convexity.py: openai/math family 175, Talagrand's discrete-convexity conjecture, k = 2^75.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om175_discrete_convexity.py
COST:       about a minute.

The claim (preprint "Talagrand's discrete-convexity conjecture", 2026-09-23). Let mu_p be the product measure on
subsets of [N]. For a family D, E_k(D) is the family of sets contained in no union of k members of D. A family is
p-small if some family G of sets, with sum over G of p^|I| at most 1/2, has a member inside each of its sets.
Theorem: with k = 2^75, for every N, p and every family D (no monotonicity), mu_p(D) >= 1 - 1/k implies that
E_k(D) is p-small. A consequence, for positive selector processes phi(S) = sup over t in T of sum over S of t_i:
{phi >= k^2 E phi} is p-small.

Cloud read the whole proof (an elementary covering lemma, a weight argument, a coupling): correct. The heart is a
signed identity. With
    b(U) = (1-q)^|U| sum over z in {0,1}^U of (-1)^(sum z) E[f(z, Y)]    (Y Bernoulli-q off U, f the indicator of F),
every S in E_(2t)(F) satisfies sum over U inside S of (-1)^|U| b(U)^(2t) = 0. Because b(empty) = mu_q(F) >= 1/2,
this forces the sixteenth powers of w(U) = b(U)^2 to be large on S, while Parseval keeps sum q^|U| w(U) <= 1.
Checks, by Cloud's own code:
  C1  the signed identity, exactly, for t = 1 (Li's kernel) and t = 16 (the preprint's 32 rows), on random families
      of up to 6 coordinates, for every S in E_(2t)(F);
  C2  the weight bound sum over U of q^|U| w(U) <= mu_q(F), exactly, and the identity f^(U) = (q/(1-q))^(|U|/2) b(U)
      squared;
  C3  both couplings of section 3 give each row the law mu_p, and the union the law mu_(Lp) or the full set, exactly
      for small N and L;
  C4  the constants: 6/(2^64 - 1) < 1/4, 1/64 + 6/(2^64 - 1) < 1/2, 16/(15(2^256 - 1)) < 2^-32, and
      4h + 13 r h + 1 <= 18 h^2 <= 2^(4h) for 1 <= r <= h, h >= 64.
Predictions (written before the run): all pass. Fail: any identity off, or a coupling law wrong.
Control: for sets S outside E_(2t)(F) the signed sum must be nonzero for most random families; if it vanished there
too, the identity would be checking nothing.
Unexpected check: Cloud's guess before the run, held loosely: for t = 1 the signed sum is nonzero for at least 90%
of the pairs (F, S) with S outside E_2(F).
"""
import itertools, random
from fractions import Fraction as Fr


def b_weights(f, N, q):
    """b(U) for every U (bitmask), f a set of bitmasks (the family), q a Fraction."""
    out = {}
    for U in range(1 << N):
        rest = [i for i in range(N) if not U >> i & 1]
        tot = Fr(0)
        for x in f:                                    # E[f(z, Y)] summed with signs: iterate members of F
            z = x & U
            sign = -1 if bin(z).count("1") % 2 else 1
            prob = Fr(1)
            for i in rest:
                prob *= q if x >> i & 1 else 1 - q
            tot += sign * prob
        out[U] = (1 - q) ** bin(U).count("1") * tot
    return out


def exceptional(f, N, m):
    unions = {0}
    for _ in range(m):
        unions = {u | x for u in unions for x in f}
    return [S for S in range(1 << N) if not any(S & ~u == 0 for u in unions)]


def main():
    rng = random.Random(175)
    res = {}
    ok1, ctl_nonzero, ctl_total, ok2 = True, 0, 0, True
    for trial in range(60):
        N = rng.randint(2, 6)
        q = Fr(rng.randint(1, 9), 10)
        f = {x for x in range(1 << N) if rng.random() < rng.choice([0.2, 0.4, 0.6])}
        if not f:
            continue
        b = b_weights(f, N, q)
        mu = sum(Fr(1) * eval_mu(x, N, q) for x in f)
        ok2 &= b[0] == mu
        ok2 &= sum(q ** bin(U).count("1") * b[U] ** 2 for U in b) <= mu
        for t in (1, 16):
            E = set(exceptional(f, N, 2 * t))
            for S in range(1 << N):
                val = sum((-1) ** bin(U).count("1") * b[U] ** (2 * t) for U in range(1 << N) if U & ~S == 0)
                if S in E:
                    ok1 &= val == 0
                elif t == 1:
                    ctl_total += 1
                    ctl_nonzero += val != 0
    res["C1  signed identity vanishes on every exceptional set (t = 1 and t = 16)"] = ok1
    res["C2  b(empty) = mu_q(F) and sum q^|U| w(U) <= mu_q(F)"] = ok2
    share = ctl_nonzero / max(1, ctl_total)
    print(f"   control: the t = 1 sum is nonzero for {ctl_nonzero} of {ctl_total} non-exceptional (F, S) "
          f"({100 * share:.0f}%)")
    res["    control: the identity is not vacuous"] = share > 0.5
    print(f"   guess (at least 90% nonzero): {'right' if share >= 0.9 else 'wrong'}")
    res["C3  couplings give rows the law mu_p and the right union law"] = couplings()
    ok4 = (Fr(6, 2 ** 64 - 1) < Fr(1, 4) and Fr(1, 64) + Fr(6, 2 ** 64 - 1) < Fr(1, 2)
           and Fr(16, 15 * (2 ** 256 - 1)) < Fr(1, 2 ** 32)
           and all(4 * h + 13 * r * h + 1 <= 18 * h * h <= 2 ** (4 * h) for h in range(64, 400) for r in (1, h // 2, h))
           and 3 * sum(Fr(1, 2 ** (64 * r)) * 2 for r in range(1, 40)) < Fr(6, 2 ** 64 - 1) + Fr(1, 10 ** 300))
    res["C4  constants"] = ok4
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


def eval_mu(x, N, q):
    out = Fr(1)
    for i in range(N):
        out *= q if x >> i & 1 else 1 - q
    return out


def couplings():
    ok = True
    for L in (2, 3):
        for p in (Fr(1, 7), Fr(1, 4)):                     # case 1 needs L p < 1
            if L * p >= 1:
                continue
            # one coordinate suffices: coordinates are independent by construction
            labels = {0: 1 - L * p, **{j: p for j in range(1, L + 1)}}
            for j in range(1, L + 1):
                ok &= sum(pr for lab, pr in labels.items() if lab == j) == p
            ok &= sum(pr for lab, pr in labels.items() if lab != 0) == L * p
        for p in (Fr(1, 2), Fr(2, 3), Fr(1, L)):            # case 2, L p >= 1
            t = (p - Fr(1, L)) / (1 - Fr(1, L))
            # law of the membership vector (rows 1..L) at one coordinate
            law = {}
            for mand in range(L):
                for extra in itertools.product((0, 1), repeat=L - 1):
                    rows = list(extra[:mand]) + [1] + list(extra[mand:])
                    pr = Fr(1, L)
                    for e in extra:
                        pr *= t if e else 1 - t
                    law[tuple(rows)] = law.get(tuple(rows), 0) + pr
            for j in range(L):
                ok &= sum(pr for v, pr in law.items() if v[j]) == p
            ok &= all(any(v) for v in law)                   # the union is everything
            ok &= sum(law.values()) == 1
    return ok


if __name__ == "__main__":
    main()
