"""G42 UR1-UR3: exact unit resonance and an infinite cosine-product bound."""
from fractions import Fraction
from itertools import product
from math import cos, gcd, pi
from collatz_gpt_pair_cancellation import direct, phase


def inverse_sum(w):
    s = 0
    total = Fraction(0)
    for j, b in enumerate(w):
        s += b
        if b:
            total += Fraction(2**j, 3**s)
    return total


def main():
    identities = cubes = orientations = 0
    worst = 0.0
    for T in range(1, 13):
        for r in range(2**T):
            w, q, valid = direct(r, T)
            if not valid:
                continue
            M = 3**sum(w)
            F = inverse_sum(w)
            assert Fraction(2**T*q, M)-F == r
            for t in range(0, T-1, 2):
                if w[t] != w[t+1]:
                    s = sum(w[:t])
                    delta = (3**(sum(w)-s-1)*pow(2, -(T-t), M)) % M
                    x = Fraction(2**t, 3**(s+1))
                    assert Fraction((2**T*delta) % M, M) == x % 1
            identities += 1
    square_sum = Fraction(64, 2187)**2/(1-Fraction(16, 27)**2)
    assert 5*square_sum < Fraction(1, 100)  # Entire infinite tail, integer comparison.
    for n in range(4):
        T, a = 4+4*n, 4+3*n
        M, h = 3**a, 2**T
        assert 0 < h < M and gcd(h, 3) == 1
        wanted = {(1,)*4+sum(((1, 1)+(1, 0) if b == 0 else (1, 1)+(0, 1)
                              for b in bits), ()) for bits in product((0, 1), repeat=n)}
        values = []
        for r in range(2**T):
            w, q, valid = direct(r, T)
            if w in wanted:
                assert valid
                values.append(q)
        assert len(values) == 2**n
        observed = abs(sum(phase(h, q, M) for q in values)/len(values))
        expected = 1.0
        for k in range(n):
            expected *= cos(pi*float(Fraction(64, 2187)*Fraction(16, 27)**k))
        error = abs(observed-expected)
        worst = max(worst, error)
        assert error < 1e-9 and observed > 0.99
        cubes += 1
        orientations += len(values)
    print(f'UR1: {identities} exact residue/inverse-sum identities through T12')
    print(f'UR2: {cubes} cubes/{orientations} orientations; max complex residual {worst:.3g}')
    print(f'infinite certificate: 5*sum(x_k^2) = {5*square_sum} < 1/100')
    print('Unexpected UR3: nonzero unit harmonics retain modulus>0.99 with n free pairs')
    print('ALL CHECKS PASS; explicit family, no aggregate-mass or decay conclusion')


if __name__ == '__main__':
    main()
