"""G47 RC1-RC3; published before run. Initial status NOT RUN."""
from collatz_gpt_actual_ceiling import specification, trajectory


def main():
    returns = []
    for k in range(1, 257):
        j = (3**k).bit_length()
        D, B = 2**j-3**k, 2**(j-k)
        w = (1,)*k+(0,)*(j-k)
        r, K = specification(w)
        minimum = r if r else 2**j
        realizable = minimum <= K
        divisible = (B-1) % D == 0
        assert realizable == divisible, (k, j)
        assert K < 2**j
        if divisible:
            m = (B-1)//D
            n = 2**k*m-1
            assert n == minimum
            assert trajectory(n, j) == (w, True)
            q = n
            for b in w:
                q = (3*q+1)//2 if b else q//2
            assert q == n
            returns.append((k, j, n))
    assert returns == [(1, 2, 1)]  # Finite preregistered prediction only.
    print('RC1: 256 divisibility/realizing-residue controls pass')
    print('RC2: finite candidates return exactly to their start:', returns)
    print('Unexpected RC3: start1 cycle survives a coefficient deficit')
    print('ALL CHECKS PASS; no exclusion of other k or general positive cycles claimed')


if __name__ == '__main__':
    main()
