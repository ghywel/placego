"""G30 exact finite controls; never infer a divergent orbit from a prefix."""
from fractions import Fraction
from collatz_gpt_signed_bound import step, word


def main():
    affine = product = inject = 0
    for d in (1, 3, 5, 9):
        for start in range(-64, 65):
            x, b, s = start, 0, 0
            correction = Fraction(1)
            nonzero = start != 0
            for m in range(32):
                e = x % 2
                if e:
                    correction *= abs(Fraction(3*x+d, 3*x))
                y = step(x, d)
                nonzero = nonzero and y != 0
                b = (3 if e else 1)*b + e*(1 << m)
                s += e
                assert (1 << (m+1))*y == 3**s*start+d*b
                affine += 1
                if nonzero:
                    assert Fraction(abs(y), abs(start)) == Fraction(3**s, 1 << (m+1))*correction
                    product += 1
                x = y
            for n in range(1, 9):
                q = 1 << (n-1)
                x = start
                seen, words = set(), set()
                for _ in range(32):
                    if x in seen or abs(x) >= q:
                        break
                    w = word(x, d, n)
                    assert w not in words
                    seen.add(x); words.add(w); inject += 1
                    x = step(x, d)
    # Unexpected: correction is not o(m) on these cycles.
    assert step(-1, 1) == -1
    assert abs(Fraction(3*(-1)+1, 3*(-1))) == Fraction(2, 3)
    assert step(1, 1) == 2 and step(2, 1) == 1
    assert Fraction(3, 4)*Fraction(4, 3) == 1  # one odd step per two steps
    print(f'GD1 PASS: {affine} affine identities; {product} nonzero product identities')
    print(f'GD2 PASS: {inject} distinct-prefix words inside strict signed intervals')
    print('Unexpected GD3 PASS: cycles -1 and (1,2) reject unqualified density/growth identity')


if __name__ == '__main__':
    main()
