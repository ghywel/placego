"""GC459: preregistered32 local controls, not an orbit census.
White intervening input predicts y=s XOR((1-h)*z).
Dropping h*z alone should fail; spatial translation is the unexpected guard.
"""
from itertools import product


def scalar(left, centre, right):
    return (210 >> (4 * left + 2 * centre + right)) & 1


def algebra(left, centre, right):
    return left ^ ((1 - centre) * right)


def twice(patch, rule):
    intermediate = [rule(*patch[i:i + 3]) for i in range(3)]
    return rule(*intermediate)


def main():
    white = 0
    correction = []
    for patch in product((0, 1), repeat=5):
        y = twice(patch, scalar)
        assert y == twice(patch, algebra)
        row = [1, 0] + list(patch) + [0, 1]
        step = [scalar(*row[i:i + 3]) for i in range(7)]
        step2 = [scalar(*step[i:i + 3]) for i in range(5)]
        assert step2[2] == y
        s, b, q, h, z = patch
        if b == 0:
            white += 1
            assert y == (s ^ ((1 - h) * z))
            assert y == (s ^ z ^ (h * z))
            if y != (s ^ z):
                correction.append(patch)
    assert white == 16 and len(correction) == 4
    assert (0, 0, 0, 1, 1) in correction
    print('PASS32 scalar/algebra and translated controls;16 white inputs;4 correction guards')


if __name__ == '__main__':
    main()
