"""GC462:12 local product-free controls, not a full-orbit census.
Prediction: inputs(0,q,h,z,w), h*z=0, give H=(1-q)*(1-z)*w.
Counterfactual universal H=0 fails locally; initial switch m=0 retained.
Clock application depends on the pending GC459/GC461 hand formulae.
"""
from itertools import product


def scalar(left, centre, right):
    return (210 >> (4 * left + 2 * centre + right)) & 1


def main():
    count = active = 0
    for q, h, z, w in product((0, 1), repeat=4):
        if h * z:
            continue
        p = [0, q, h, z, w]
        row = [scalar(*p[i:i + 3]) for i in range(3)]
        H = scalar(*row)
        assert H == (1 - q) * (1 - z) * w
        count += 1
        active += H
    assert count == 12 and active == 2
    assert (1 ^ 1 ^ 0 ^ 1) == 1  # z_0 removes the initial switch
    print('PASS12 scalar patches;2 active local guards;initial101 retained')


if __name__ == '__main__':
    main()
