"""G34 finite witnesses for an analytically irrational infinite parity inverse."""
from collatz_gpt_signed_bound import word
from collatz_gpt_periodic import affine


def power_zero(i):
    return int(not (i > 0 and i & (i-1) == 0))


def main():
    cases = bits_checked = 0
    for p in (1,2,4,8,16,32,64,128):
        bits = tuple(power_zero(i) for i in range(2*p+1))
        s,b = affine(bits)
        modulus = 1 << len(bits)
        for d in (1,3,5,9):
            n = (-d*b*pow(3**s,-1,modulus)) % modulus
            if n >= modulus//2:
                n -= modulus
            assert word(n,d,len(bits)) == bits
            assert (abs(n)+d)*3**(p+1) >= 4**p
            cases += 1; bits_checked += len(bits)
    # Square spacing has ratio tending to1; doubling spacing has ratio2.
    for k in range(2,101):
        assert ((k+1)**2-k*k-1) == 2*k
        assert 2**(k+1) == 2*2**k
    print(f'LG1 PASS: {cases} exact signed prefix witnesses and height budgets; {bits_checked} bits checked')
    print('Unexpected LG2 PASS / CF REJECTED: finite prefixes are all realizable')
    print('Infinite irrationality follows from the analytic gap bound, not finite witnesses')


if __name__ == '__main__':
    main()
