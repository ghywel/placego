#!/usr/bin/env python3
"""GC672: bounded GC671 finite-cone certificate audit.

Preregistered: shift k<=3, H<=3, every hole; identity k<=2, H<=3;
Rule30 holes omitting zero k<=2, H<=3. No ergodic-hole search.
Prediction: cone certificates agree with an independent substring oracle;
proper identity holes and holes omitting Rule30's fixed zero never certify.
Unexpected controls: radius zero, an oversized neighbourhood, and H=0.
"""
from itertools import product


def first_avoider(b, radius, rule, k, hole, horizon):
    """Return a finite initial cone missing the hole at every checked time.

    None is an exhaustive certificate of full-space hitting by horizon.
    Words cover positions 1-radius*horizon through k+radius*horizon.
    No boundary clamping or wraparound is used.
    """
    assert b >= 2 and radius >= 0 and k >= 1 and horizon >= 0
    assert all(len(w) == k and all(0 <= x < b for x in w) for w in hole)
    width = k + 2 * radius * horizon
    for initial in product(range(b), repeat=width):
        row = initial
        for t in range(horizon + 1):
            offset = radius * (horizon - t)
            if tuple(row[offset:offset + k]) in hole:
                break
            if t < horizon:
                row = tuple(rule(row[i:i + 2 * radius + 1])
                            for i in range(len(row) - 2 * radius))
                assert all(0 <= x < b for x in row)
        else:
            return initial
    return None


def shift_oracle(k, hole, horizon):
    # Independent formulation: the shift visits successive substrings.
    return all(any(tuple(w[t:t + k]) in hole for t in range(horizon + 1))
               for w in product((0, 1), repeat=k + horizon))


def holes(k):
    words = list(product((0, 1), repeat=k))
    for mask in range(1 << len(words)):
        yield {w for i, w in enumerate(words) if (mask >> i) & 1}


def main():
    shift = lambda w: w[2]
    identity = lambda w: w[0]
    rule30 = lambda w: w[0] ^ (w[1] | w[2])
    three = {(0, 0), (0, 1), (1, 1)}
    equal = {(0, 0), (1, 1)}
    assert first_avoider(2, 1, shift, 2, three, 0) is not None
    assert first_avoider(2, 1, shift, 2, three, 1) is None
    assert first_avoider(2, 1, shift, 2, equal, 3) is not None
    assert first_avoider(2, 2, lambda w: w[3], 2, three, 1) is None
    assert first_avoider(2, 0, identity, 2, three, 3) is not None
    assert first_avoider(2, 0, identity, 1, {(0,), (1,)}, 0) is None
    counts = dict(shift=0, identity=0, zero=0)
    for k in range(1, 4):
        for hole in holes(k):
            for horizon in range(4):
                got = first_avoider(2, 1, shift, k, hole, horizon) is None
                assert got == shift_oracle(k, hole, horizon)
                counts['shift'] += 1
                if k <= 2 and len(hole) < 2**k:
                    assert first_avoider(2, 0, identity, k, hole, horizon) is not None
                    counts['identity'] += 1
                if k <= 2 and (0,) * k not in hole:
                    witness = first_avoider(2, 1, rule30, k, hole, horizon)
                    assert witness == (0,) * (k + 2 * horizon)
                    counts['zero'] += 1
    assert counts == dict(shift=1104, identity=72, zero=40)
    print('PASS: 1104 independent shift-oracle comparisons; 72 identity failures; '
          '40 Rule30 zero witnesses; 6 endpoint/radius controls.')


if __name__ == '__main__':
    main()
