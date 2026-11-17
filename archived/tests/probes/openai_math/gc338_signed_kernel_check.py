#!/usr/bin/env python3
"""gc338_signed_kernel_check.py: Cloud's second reading of GPT's GC338 (RULE30-GPT.md), the signed local kernel for
Rule 30 suggested by family 175's signed annihilation.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/gc338_signed_kernel_check.py
COST:       a few seconds.

GC338's claims. For local bits (a, b, c, d) Rule 30 requires d = a XOR (b OR c). With chi_U = (-1)^(sum of the bits
in U), K = 2 chi_{a,d} + 1 - chi_b - chi_c - chi_{b,c} is 0 on every valid tuple and +-4 on every invalid one. So for
f supported on valid assignments, every U satisfies
    2 f^(U + {a,d}) + f^(U) - f^(U + {b}) - f^(U + {c}) - f^(U + {b,c}) = 0     (+ is symmetric difference),
and the same holds for moments of any distribution on valid assignments. Opposite invalid tuples cancel in E K, but
E K^2 = 16 P(invalid) for a nonnegative distribution.
Checks (written before the run):
  K1  K on all 16 tuples: 0 exactly on the 8 valid ones, +-4 on the rest; and the two cancelling tuples GPT names.
  K2  on a real spacetime patch (5 cells x_-2..x_2 and the 3 cells below, y_i = x_(i-1) XOR (x_i OR x_(i+1))), the
      shifted relations hold exactly for every U and all three local constraints, for random valid-supported
      functions and random distributions on valid configurations.
  K3  the guard: E K^2 = 16 P(invalid) exactly for random nonnegative distributions on all 256 configurations; and a
      signed weighting can have E K^2 = 0 with invalid support (GPT's "without positivity" caveat).
  K4  Cloud's addition: the relations over all U and all three constraints say exactly "supported on valid
      configurations". As a linear system on the 256 Walsh coefficients their rank is 256 - 32 = 224, since the
      valid configurations are the 32 choices of the top row.
Predictions: all pass, and the rank in K4 is 224. Fail: any relation off, or a rank other than 224.
Control: a function with mass on one invalid configuration must violate some relation.
"""
import itertools, random
from fractions import Fraction as Fr

BITS = 8                       # 0..4: x_-2..x_2 ; 5..7: y_-1..y_1
CONSTRAINTS = [(0, 1, 2, 5), (1, 2, 3, 6), (2, 3, 4, 7)]     # (a, b, c, d): y_i = x_(i-1) XOR (x_i OR x_(i+1))


def chi(U, z):
    return -1 if bin(U & z).count("1") % 2 else 1


def kernel(con, z):
    a, b, c, d = con
    m = lambda *ix: sum(1 << i for i in ix)
    return 2 * chi(m(a, d), z) + 1 - chi(m(b), z) - chi(m(c), z) - chi(m(b, c), z)


def valid(z):
    return all(((z >> d) & 1) == ((z >> a) & 1) ^ (((z >> b) & 1) | ((z >> c) & 1)) for a, b, c, d in CONSTRAINTS)


def walsh(f):
    return [Fr(sum(f[z] * chi(U, z) for z in range(1 << BITS)), 1 << BITS) for U in range(1 << BITS)]


def relations_hold(fh):
    for a, b, c, d in CONSTRAINTS:
        for U in range(1 << BITS):
            s = (2 * fh[U ^ (1 << a | 1 << d)] + fh[U] - fh[U ^ (1 << b)] - fh[U ^ (1 << c)]
                 - fh[U ^ (1 << b | 1 << c)])
            if s != 0:
                return False
    return True


def rank(rows):
    rows = [list(r) for r in rows]
    r, ncol = 0, len(rows[0])
    for c in range(ncol):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = Fr(rows[i][c], 1) / rows[r][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def main():
    rng = random.Random(338)
    res = {}
    ks = {}
    for t in itertools.product((0, 1), repeat=4):
        z = sum(bit << i for i, bit in enumerate(t))
        k = kernel((0, 1, 2, 3), z)
        ok_valid = t[3] == t[0] ^ (t[1] | t[2])
        ks[t] = (k, ok_valid)
    res["K1  K = 0 on the 8 valid tuples, +-4 on the 8 invalid"] = (
        sum(v for _, v in ks.values()) == 8 and all((k == 0) == v and k in (0, 4, -4) for k, v in ks.values())
        and ks[(0, 0, 0, 1)][0] == -4 and ks[(0, 1, 0, 0)][0] == 4)
    V = [z for z in range(1 << BITS) if valid(z)]
    assert len(V) == 32
    ok2 = True
    for _ in range(20):
        f = [0] * (1 << BITS)
        for z in V:
            f[z] = rng.choice([0, 1]) if _ % 2 else Fr(rng.randint(0, 9))
        ok2 &= relations_hold(walsh(f))
    res["K2  shifted relations hold for valid-supported functions and distributions"] = ok2
    ctl = [0] * (1 << BITS)
    ctl[next(z for z in range(1 << BITS) if not valid(z))] = 1
    res["    control: mass on one invalid configuration breaks a relation"] = not relations_hold(walsh(ctl))
    ok3 = True
    for _ in range(20):
        w = [Fr(rng.randint(0, 5)) for _ in range(1 << BITS)]
        tot = sum(w)
        if tot == 0:
            continue
        for con in CONSTRAINTS:
            EK2 = sum(w[z] * kernel(con, z) ** 2 for z in range(1 << BITS)) / tot
            a, b, c, d = con
            inval = sum(w[z] for z in range(1 << BITS)
                        if ((z >> d) & 1) != ((z >> a) & 1) ^ (((z >> b) & 1) | ((z >> c) & 1))) / tot
            ok3 &= EK2 == 16 * inval
    # a signed weighting with E K = 0 and invalid support: GPT's two cancelling tuples, weights +1 and +1 give
    # mean K = 0; E K^2 is then 16 > 0, so positivity is what makes K^2 decisive.
    z1, z2 = 0b1000, 0b0010                                 # (a,b,c,d) = (0,0,0,1) and (0,1,0,0)
    ok3 &= kernel((0, 1, 2, 3), z1) + kernel((0, 1, 2, 3), z2) == 0
    res["K3  E K^2 = 16 P(invalid) for nonnegative weights; E K alone cancels"] = ok3
    rows = []
    for a, b, c, d in CONSTRAINTS:
        for U in range(1 << BITS):
            row = [0] * (1 << BITS)
            for V_, coef in ((U ^ (1 << a | 1 << d), 2), (U, 1), (U ^ (1 << b), -1), (U ^ (1 << c), -1),
                             (U ^ (1 << b | 1 << c), -1)):
                row[V_] += coef
            rows.append(row)
    rk = rank(rows)
    res["K4  the relations have rank 224: they say exactly 'supported on valid configurations'"] = rk == 224
    print(f"   rank of the shifted relations over all U and three constraints: {rk} (prediction 224)")
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(res.values()) else "FAIL")


if __name__ == "__main__":
    main()
