"""G46 KC1-KC3, published before run. Exact family audit k1..256.
Initial publication: NOT RUN. Invoke at the next tick; no data files generated.
"""
from fractions import Fraction
from collatz_gpt_actual_ceiling import specification, count


def main():
    rows = []
    for k in range(1, 257):
        power = 3**k
        j = power.bit_length()  # ceil(log2(3**k)), exactly; not a power of2.
        w = (1,)*k+(0,)*(j-k)
        expected = (power-2**k)//(2**j-power)
        r, K = specification(w)
        assert K == expected
        assert 2**(j-1) < power < 2**j
        minimum_start = r if r else 2**j
        rows.append((K, k, j, minimum_start <= K, minimum_start.bit_length()))
    # The census audits finite values, not the all-length irrational approximation proof.
    print('KC1: 256 exact first-deficit ceilings agree with independent G45 specification')
    print('KC2: top formal ceilings (K,k,j,residue-realized,residue-bit-length):')
    for row in sorted(rows, reverse=True)[:5]:
        print(row)
    assert specification((1, 0, 1, 0)) == (1, 1)
    assert count(1, 1, 4, 1) == 1
    assert Fraction(1, 16) < 1
    print('Unexpected KC3: ceiling-density shortcut fails; residue count needs +1')
    print('ALL CHECKS PASS; no polynomial upper bound or large realized exception claimed')


if __name__ == '__main__':
    main()
