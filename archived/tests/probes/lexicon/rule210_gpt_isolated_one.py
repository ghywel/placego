"""GC458 bounded controls, not a full-clock census.
Prediction (recorded before the run): positive-time even column2 bit1
requires effective010; G26 has none centred at n>=1.
Counterfactual: general-left bit elimination fails locally.
Unexpected check: the initial even bit has no incoming up-gate.
"""
from itertools import product


def scalar(left, centre, right):
    return (210 >> (4 * left + 2 * centre + right)) & 1


def algebra(left, centre, right):
    return left ^ ((1 - centre) * right)


def history(patch, rule):
    rows = [list(patch)]
    for wall in (0, 1, 0, 1):
        row = rows[-1]
        rows.append([rule(wall if i == 0 else row[i - 1], row[i], row[i + 1])
                     for i in range(len(row) - 1)])
    return rows


def stream(n):
    return 1 if n == 0 else (n.bit_length() - 1) % 2


def main():
    active = []
    for patch in product((0, 1), repeat=7):
        rows = history(patch, scalar)
        assert rows == history(patch, algebra)
        if rows[2][1]:
            assert (rows[0][0], rows[2][0], rows[4][0]) == (0, 1, 0)
            active.append(patch)
    assert len(active) == 16
    assert history((0, 0, 0, 1, 0, 0, 0), scalar)[2][1] == 1
    initial = history((1, 1, 0, 0, 0, 0, 0), scalar)
    assert initial[0][1] == 1 and initial[2][0] == 0
    assert all((stream(n - 1), stream(n), stream(n + 1)) != (0, 1, 0)
               for n in range(1, 4096))
    print('PASS128 patches;16 active isolated-one guards;4095 stream controls; initial exception retained')


if __name__ == '__main__':
    main()
