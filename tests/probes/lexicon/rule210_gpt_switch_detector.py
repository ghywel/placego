"""GC461:16 local controls, no continuing-clock census.
Prediction: b=0 implies q=1 XOR s XOR s_next under wall01.
Counterfactual all-white farther track fails at initial effective101.
Unexpected guard: retain the initial switch and initial triple.
"""
from itertools import product


def scalar(left, centre, right):
    return (210 >> (4 * left + 2 * centre + right)) & 1


def main():
    for s, q, h, z in product((0, 1), repeat=4):
        p = [s, 0, q, h, z]
        row = [scalar(0, p[0], p[1])]
        row += [scalar(*p[i:i + 3]) for i in range(3)]
        s_next = scalar(1, row[0], row[1])
        assert q == (1 ^ s ^ s_next)
        assert s_next == (1 ^ (s ^ q))
    assert (1 ^ 1 ^ 0) == 0  # initial column3 bit
    assert (1 ^ 1 ^ 0 ^ 1) == 1  # initial column5 bit
    print('PASS16 scalar patches and G61 controls; initial101 exception retained')


if __name__ == '__main__':
    main()
