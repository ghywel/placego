#!/usr/bin/env python3
"""om003b_siegel_determinant.py: openai/math family 003, second preprint: no Landau-Siegel zeros, by an
interpolation determinant in a biquadratic field.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om003b_siegel_determinant.py
            python3 tests/probes/openai_math/om003b_siegel_determinant.py --n3 -163 -1   (post hoc: N = 3, 81 rows)
COST:       seconds; the post-hoc N = 3 mode about half a minute per field (exact arithmetic in Q(sqrt d, sqrt 2)).

The claim (preprint "Uniform exclusion of Landau-Siegel zeros", 2026-10-01): there is an absolute c > 0 such that
every real zero beta of every primitive nonprincipal real Dirichlet L-function of conductor q >= 3 has
(1 - beta) log q >= c. (The family's other preprint, a zero-free half-plane Re s > 7/8, would also imply it; this one
is an independent, elementary proof.)

The proof (read in full by Cloud; no error found): a zero with (1 - beta) log q small makes almost every prime up to
any fixed power of q inert in Q(sqrt d). In R = Z[a, b] with a^2 = d, b^2 = 2, take theta_n = n1 + n2 a + n3 b + n4 ab
for n in {0..N-1}^4, and rows (theta^x sigma(theta)^y sigma tau(theta)^z) over the N^4 columns, ordered by the
weight x + H y + H z and kept greedily while they raise the rank. An interpolation lemma guarantees N^4 kept rows of
weight at most 96 H^(2/3) N^(4/3), so the determinant Delta is nonzero. At an inert prime p > H, the Frobenius
congruence theta^p = sigma(theta) or sigma tau(theta) mod p lets each row shed p^floor(x/p) by subtracting rows of
smaller weight, so Delta lies in p^(E_p) R. With almost all primes inert, that divisibility (about S1 log U) beats
Hadamard's bound (about (3/4)(S1 + S2) log U), a contradiction.
Checks here, on small cases, by Cloud's own code (the contradiction itself needs astronomically large N and H):
  D1  the Frobenius congruence theta^p - g_p(theta) in pR, for random theta and every inert prime below 60, in
      several fields;
  D2  the actual determinant Delta for N = 2 (16 kept rows), H = 2: nonzero, in R, with a nonzero integer norm;
  D3  the divisibility Delta in p^(E_p) R for every admissible prime p below 60 (p > H, p not dividing 2q, chi(p) = -1);
  D4  Hadamard's bound (1/4) log|Nm Delta| <= (M/2) log M + (S1 + S2)(log N + (1/2) log q + log 8), and the integer
      Nm(Delta) divisible by the product of p^(4 E_p);
  D5  the interpolation lemma's spanning claim at its own budget (t_j = 11 for N = 2): the rows with every exponent at
      most 11 have rank 16, in every field; the smallest such box is also reported.
Predictions (written before the run): all pass. Fail: any congruence, divisibility or bound off.
Cloud's own consistency observation, tested as D6, not in the preprint: primes that split completely in K
(chi(p) = 1 and (2/p) = 1) satisfy theta^p = theta mod p, so they divide Delta to the same power E_p. Together with
the inert primes they have density 3/4, which matches the 3/4 in Hadamard's bound: without a Siegel zero the method
is exactly balanced, and only the zero's prime bias tips it.
Unexpected check: the share of log|Nm Delta| / 4 accounted for by the forced divisibility. Cloud's guess before the
run: largest for d = -163, whose primes below 41 are all inert.
Control: at primes with chi(p) = 1 and (2/p) = -1 (where theta^p = tau(theta) mod p) the congruence with sigma must
fail for most random theta, so D1's test can tell the cases apart.
"""
import itertools, math, random
from fractions import Fraction as Fr


class Field:
    def __init__(self, d):
        self.d = d

    def mul(self, x, y):
        d = self.d
        return (x[0] * y[0] + d * x[1] * y[1] + 2 * x[2] * y[2] + 2 * d * x[3] * y[3],
                x[0] * y[1] + x[1] * y[0] + 2 * (x[2] * y[3] + x[3] * y[2]),
                x[0] * y[2] + x[2] * y[0] + d * (x[1] * y[3] + x[3] * y[1]),
                x[0] * y[3] + x[3] * y[0] + x[1] * y[2] + x[2] * y[1])

    def pw(self, x, k):
        out, base = (1, 0, 0, 0), x
        while k:
            if k & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            k >>= 1
        return out

    @staticmethod
    def sig(x): return (x[0], -x[1], x[2], -x[3])

    @staticmethod
    def tau(x): return (x[0], x[1], -x[2], -x[3])

    @staticmethod
    def sigtau(x): return (x[0], -x[1], -x[2], x[3])

    def norm(self, x):
        n = self.mul(self.mul(x, self.sig(x)), self.mul(self.tau(x), self.sigtau(x)))
        assert n[1] == n[2] == n[3] == 0
        return n[0]

    def inv(self, x):
        c = self.mul(self.sig(x), self.mul(self.tau(x), self.sigtau(x)))
        n = self.norm(x)
        return tuple(Fr(ci) / n for ci in c)


def add(x, y): return tuple(a + b for a, b in zip(x, y))
def sub(x, y): return tuple(a - b for a, b in zip(x, y))
def iszero(x): return all(c == 0 for c in x)


def conductor(d):
    D = d if d % 4 == 1 else 4 * d
    return abs(D)


def legendre(d, p):
    r = pow(d % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


def primes(n):
    return [p for p in range(2, n) if all(p % k for k in range(2, int(p ** 0.5) + 1))]


def kept_rows(F, N, H):
    cols = list(itertools.product(range(N), repeat=4))
    th = [(n[0], n[1], n[2], n[3]) for n in cols]
    M = len(cols)
    basis, kept, W = [], [], 0
    pc = {}

    def entry(n, al):
        key = (n, al)
        if key not in pc:
            t = th[n]
            pc[key] = F.mul(F.mul(F.pw(t, al[0]), F.pw(F.sig(t), al[1])), F.pw(F.sigtau(t), al[2]))
        return pc[key]
    while len(kept) < M:
        cands = sorted((al for al in itertools.product(range(W + 1), repeat=3)
                        if al[0] + H * al[1] + H * al[2] == W))
        for al in cands:
            row = [entry(n, al) for n in range(M)]
            v = list(row)
            for piv, brow in basis:                          # reduce against the echelon basis over K
                if not iszero(v[piv]):
                    f = F.mul(v[piv], F.inv(brow[piv]))
                    v = [sub(x, F.mul(f, y)) for x, y in zip(v, brow)]
            nz = next((i for i, x in enumerate(v) if not iszero(x)), None)
            if nz is not None:
                basis.append((nz, v))
                kept.append((al, row))
                if len(kept) == M:
                    break
        W += 1
    return kept


def det(F, rows):
    A = [list(r) for r in rows]
    n, sign, out = len(A), 1, (1, 0, 0, 0)
    for c in range(n):
        piv = next(r for r in range(c, n) if not iszero(A[r][c]))
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            sign = -sign
        iv = F.inv(A[c][c])
        out = F.mul(out, A[c][c])
        for r in range(c + 1, n):
            if not iszero(A[r][c]):
                f = F.mul(A[r][c], iv)
                A[r] = [sub(x, F.mul(f, y)) for x, y in zip(A[r], A[c])]
    return tuple(sign * x for x in out)


def in_pkR(x, pk):
    return all(Fr(c).denominator == 1 and int(c) % pk == 0 for c in x)


def main():
    rng = random.Random(3)
    fields = [-1, -7, 5, 3, -163]
    res, okF, okS = {}, True, True
    for d in fields:
        F, q = Field(d), conductor(d)
        for p in primes(60):
            if p == 2 or q % p == 0:
                continue
            chi, two = legendre(d, p), legendre(2, p)
            for _ in range(8):
                t = tuple(rng.randint(-9, 9) for _ in range(4))
                tp = F.pw(t, p)
                if chi == -1:
                    g = F.sig(t) if two == 1 else F.sigtau(t)
                    okF &= in_pkR(sub(tp, g), p)
                elif two == 1:
                    okS &= in_pkR(sub(tp, t), p)               # Cloud's D6: split completely
    res["D1  Frobenius congruence at every inert prime below 60"] = okF
    res["D6  (Cloud) theta^p = theta mod p at primes split completely in K"] = okS
    okD2 = okD3 = okD4 = True
    N, H = 2, 2
    for d in fields:
        F, q = Field(d), conductor(d)
        kept = kept_rows(F, N, H)
        M = len(kept)
        Dl = det(F, [r for _, r in kept])
        nm = F.norm(Dl)
        okD2 &= not iszero(Dl) and all(Fr(c).denominator == 1 for c in Dl) and nm != 0 and Fr(nm).denominator == 1
        S1 = sum(al[0] for al, _ in kept)
        S2 = sum(al[1] + al[2] for al, _ in kept)
        logdiv, logdiv_split, prod = 0.0, 0.0, 1
        for p in primes(60):
            if p <= H or q % p == 0 or p == 2:
                continue
            Ep = sum(al[0] // p for al, _ in kept)
            if Ep == 0:
                continue
            if legendre(d, p) == -1:
                okD3 &= in_pkR(Dl, p ** Ep)
                logdiv += Ep * math.log(p)
                prod *= p ** (4 * Ep)
            elif legendre(2, p) == 1:
                okS &= in_pkR(Dl, p ** Ep)                 # D6 on the determinant itself
                logdiv_split += Ep * math.log(p)
        quarter = math.log(abs(nm)) / 4
        upper = M / 2 * math.log(M) + (S1 + S2) * (math.log(N) + 0.5 * math.log(q) + math.log(8))
        okD4 &= quarter <= upper and int(nm) % prod == 0
        print(f"   d = {d:5d} (q = {q:3d}): {M} rows, S1 = {S1}, S2 = {S2}, max x = {max(a[0] for a, _ in kept)}; "
              f"(1/4) log|Nm Delta| = {quarter:.1f} <= Hadamard {upper:.1f}; forced inert divisibility "
              f"{logdiv:.1f} ({100 * logdiv / quarter:.0f}%), split-completely {logdiv_split:.1f}")
        res.setdefault("_share", []).append((d, logdiv / quarter))
    res["D2  Delta nonzero, in R, with a nonzero integer norm (N = 2, H = 2)"] = okD2
    res["D3  Delta in p^(E_p) R at every admissible prime below 60"] = okD3
    res["D4  Hadamard's bound, and Nm(Delta) divisible by the product of p^(4 E_p)"] = okD4
    res["D6  (Cloud) theta^p = theta mod p at primes split completely in K"] = okS
    share = res.pop("_share")
    best = max(share, key=lambda s: s[1])[0]
    print(f"   guess (largest share at d = -163): {'right' if best == -163 else 'wrong'} (largest at d = {best})")
    # D5: rank of the box of rows with every exponent at most tb, for N = 2
    okD5, smallest = True, []
    cols = list(itertools.product(range(2), repeat=4))
    for d in fields:
        F = Field(d)
        def rank(tb):
            basis = []
            for al in itertools.product(range(tb + 1), repeat=3):
                v = [F.mul(F.mul(F.pw(n, al[0]), F.pw(F.sig(n), al[1])), F.pw(F.sigtau(n), al[2])) for n in cols]
                for piv, brow in basis:
                    if not iszero(v[piv]):
                        f = F.mul(v[piv], F.inv(brow[piv]))
                        v = [sub(x, F.mul(f, y)) for x, y in zip(v, brow)]
                nz = next((i for i, x in enumerate(v) if not iszero(x)), None)
                if nz is not None:
                    basis.append((nz, v))
                    if len(basis) == 16:
                        break
            return len(basis)
        okD5 &= rank(11) == 16
        smallest.append(next(tb for tb in range(12) if rank(tb) == 16))
    res["D5  rows with every exponent at most 11 span all 16 columns (N = 2), every field"] = okD5
    print(f"   smallest box that spans, by field {fields}: exponents up to {smallest} (the lemma's budget is 11)")
    ctl, tot = 0, 0
    for d in fields:
        F, q = Field(d), conductor(d)
        for p in primes(60):
            if p > 2 and q % p and legendre(d, p) == 1 and legendre(2, p) == -1:
                for _ in range(8):
                    t0 = tuple(rng.randint(-9, 9) for _ in range(4))
                    tot += 1
                    ctl += not in_pkR(sub(F.pw(t0, p), F.sig(t0)), p)
    res["    control: the sigma congruence fails at split primes with (2/p) = -1"] = ctl > 0.8 * tot
    print(f"   control: sigma congruence fails at {ctl} of {tot} such tests")
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


def post_hoc_n3(ds):
    """Added after the first run, whose N = 2 determinants reach exponents of only 5: the same checks at N = 3."""
    N, H = 3, 2
    for d in ds:
        F, q = Field(d), conductor(d)
        kept = kept_rows(F, N, H)
        Dl = det(F, [r for _, r in kept])
        nm = int(F.norm(Dl))
        S1 = sum(a[0] for a, _ in kept)
        S2 = sum(a[1] + a[2] for a, _ in kept)
        ok, logdiv, prod, tested = all(Fr(c).denominator == 1 for c in Dl) and nm != 0, 0.0, 1, []
        for p in primes(80):
            if p <= H or q % p == 0:
                continue
            Ep = sum(a[0] // p for a, _ in kept)
            if Ep and (legendre(d, p) == -1 or legendre(2, p) == 1):
                ok &= in_pkR(Dl, p ** Ep)
                tested.append((p, Ep))
                if legendre(d, p) == -1:
                    logdiv += Ep * math.log(p)
                    prod *= p ** (4 * Ep)
        quarter = math.log(abs(nm)) / 4
        upper = len(kept) / 2 * math.log(len(kept)) + (S1 + S2) * (math.log(N) + 0.5 * math.log(q) + math.log(8))
        ok &= nm % prod == 0 and quarter <= upper
        print(f"d = {d} (q = {q}): {len(kept)} rows, S1 = {S1}, S2 = {S2}, max x = {max(a[0] for a, _ in kept)}; "
              f"divisibility (p, E_p) {tested}; (1/4) log|Nm| = {quarter:.1f} <= {upper:.1f}; "
              f"inert share {100 * logdiv / quarter:.0f}%: {'PASS' if ok else 'FAIL'}", flush=True)


if __name__ == "__main__":
    import sys
    if sys.argv[1:2] == ["--n3"]:
        post_hoc_n3([int(x) for x in sys.argv[2:]])
    else:
        main()
