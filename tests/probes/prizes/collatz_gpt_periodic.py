"""G33 exact cycle, geometric inverse and repeat-budget controls."""
from fractions import Fraction
from itertools import product
from collatz_gpt_signed_bound import step, word


def affine(bits):
    b = s = 0
    for j, e in enumerate(bits):
        b = (3 if e else 1)*b+e*(1 << j)
        s += e
    return s, b


def main():
    cycles = repetitions = high = low = zero = 0
    for p in range(1, 7):
        for bits in product((0, 1), repeat=p):
            s, b = affine(bits)
            den = (1 << p)-3**s
            c = Fraction(b, den)
            assert c.denominator % 2 == 1
            assert word(c.numerator, c.denominator, p) == bits
            x = c.numerator
            for _ in bits:
                x = step(x, c.denominator)
            assert x == c.numerator
            r = Fraction(1 << p, 3**s)
            f = Fraction(b, 3**s)
            assert -f/(1-r) == c
            sk, bk = affine(bits*4)
            assert Fraction(bk, 3**sk) == f*(1-r**4)/(1-r)
            if not s:
                zero += 1; assert f == 0 and c == 0
            elif r < 1:
                high += 1; assert c < 0
            else:
                low += 1; assert c > 0
            cycles += 1
            for d in (1, 3, 5):
                for n in range(-16, 17):
                    m = n*den-d*b
                    for k in range(1, 5):
                        assert (word(n, d, k*p) == bits*k) == (m % (1 << (k*p)) == 0)
                        repetitions += 1
    assert Fraction(affine((1,0))[1],4-3) == Fraction(affine((1,0,1,0))[1],16-9) == 1
    assert word(17,1,4) == (1,0,1,0) and word(17,1,5)[4] == 0
    print(f'PB1 PASS: {cycles} cycles/geometric controls ({high} high-density, {low} low-density, {zero} zero)')
    print(f'PB2 PASS: {repetitions} exact repetition/divisibility comparisons')
    print('Unexpected PB3 PASS: start17 gives two copies of10, one copy of1010')
    print('CF REJECTED analytically: word10 gives cycle1,2; real inverse ratio4/3 diverges')


if __name__ == '__main__':
    main()
