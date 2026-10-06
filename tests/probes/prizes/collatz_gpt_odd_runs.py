"""G31 exact odd-run checks and an abstract-word shortcut counterexample."""
from math import isqrt
from collatz_gpt_signed_bound import step, word


def main():
    cases = 0
    for d in (1, 3, 5, 9):
        for start in range(-128, 129):
            for length in range(1, 11):
                allodd = all(word(start, d, length))
                assert allodd == ((start+d) % (1 << length) == 0)
                if allodd:
                    x = start
                    for _ in range(length):
                        x = step(x, d)
                    assert (1 << length)*(x+d) == 3**length*(start+d)
                    if start != -d:
                        assert (1 << length) <= abs(start)+d
                cases += 1
        assert step(-d, d) == -d
        assert all(word(-d, d, 20)) and (1 << 20) > 2*d
    # Zero at every square; a finite-word control, not a Collatz orbit.
    for i in range(10001):
        k = isqrt(i)
        run = 0 if k*k == i else (k+1)**2-i
        assert run <= 2*k
        # Rational slope 1/2, constant2: 2sqrt(i)<=i/2+2.
        assert 2*run <= i+4
    for m in range(1, 10001):
        zeros = isqrt(m-1)+1
        assert zeros == sum(k*k < m for k in range(isqrt(m-1)+1))
    print(f'OR1 PASS: {cases} signed congruence cases and affine/height implications')
    print('CF REJECTED: fixed numerator -D has arbitrarily long odd runs at bounded height')
    print('Unexpected OR2 PASS: 10001 run controls, 10000 square-count controls')
    print('Square-zero word has no asserted rational Collatz realization')


if __name__ == '__main__':
    main()
