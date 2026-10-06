"""G32 exact affine normalization and separate-metric controls."""
from fractions import Fraction
from math import isqrt
from collatz_gpt_signed_bound import step, word


def v2(n):
    assert n
    return (abs(n) & -abs(n)).bit_length()-1


def main():
    identities = residues = 0
    for d in (1, 3, 5, 9):
        for start in range(-32, 33):
            x, s, f = start, 0, Fraction(0)
            for j in range(32):
                e = x % 2
                s += e
                if e:
                    f += Fraction(1 << j, 3**s)
                x = step(x, d)
                assert Fraction((1 << (j+1))*x, 3**s) == start+d*f
                identities += 1
        f, s, bits = Fraction(0), 0, []
        for j in range(32):
            e = int(isqrt(j)**2 != j)
            bits.append(e); s += e
            if e:
                f += Fraction(1 << j, 3**s)
            modulus = 1 << (j+1)
            r = (-d*f.numerator*pow(f.denominator, -1, modulus)) % modulus
            assert word(r, d, j+1) == tuple(bits)
            residues += 1
    # The rational partial sums are of the SAME telescoping series in both metrics.
    previous, total = Fraction(0), Fraction(0)
    for m in range(1, 65):
        a = Fraction(1 << m, (1 << m)+1)
        total += a-previous
        assert total == a
        assert 1-a == Fraction(1, (1 << m)+1)
        assert v2(a.numerator)-v2(a.denominator) == m
        previous = a
    # Actual fixed -1: F_m=1-(2/3)^m, real normalization coefficient zero.
    f = sum((Fraction(2**j, 3**(j+1)) for j in range(32)), Fraction(0))
    assert -1+f == -Fraction(2, 3)**32
    print(f'NF1 PASS: {identities} exact signed normalization identities')
    print(f'NF2 PASS: {residues} finite square-zero residue realizations')
    print('Unexpected NF3 PASS: 64 telescoping sums, real error and exact 2-adic valuation')
    print('CF REJECTED: both metrics converge, to real1 and 2-adic0; fixed -1 cancellation retained')


if __name__ == '__main__':
    main()
