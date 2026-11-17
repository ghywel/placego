"""GC465: fixed64-by64 linear gate audit, not a seed census.
Blind prediction: no three white adjacent odd-grid cells in the rectangle.
Independent control: integer-binomial parity for all4224 required cells.
Counterfactual empty-left extension must fail; preserve the first failure.
"""
from math import comb


def initial(j):
    return int(j >= 0 and j % 3 != 1)


def main():
    row = {j: initial(j) for j in range(-128, 256)}
    failures = []
    controls = 0
    for n in range(64):
        for j in range(66):
            value = 0
            for k in range(n + 1):
                value ^= (comb(n, k) & 1) * initial(j + n - 2 * k)
            assert value == row[j]
            controls += 1
        for j in range(64):
            if not (row[j] or row[j + 1] or row[j + 2]):
                failures.append((n, j))
        row = {j: row[j - 1] ^ row[j + 1]
               for j in range(-127 + n, 255 - n)}
    assert controls == 4224
    assert len(failures) == 364 and failures[0] == (6, 2)
    assert initial(-3) == initial(-2) == initial(-1) == 0
    print('PASS4224 binomial controls; no-triple prediction REFUTED:364 triples, first n6,j2')


if __name__ == '__main__':
    main()
