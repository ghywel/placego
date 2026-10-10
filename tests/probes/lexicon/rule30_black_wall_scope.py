"""GC1043: the other-wall-phase data in KIMI-QUESTIONS-3 use the wrong game.

Missing inference: does WA3 support question D's black-start free record?
Source inspection shows first_failure always checks ODD times, even when
the wall phase is1. A black-start alternating clock instead requires its
left neighbour black at EVEN times, starting at0. Predictions are informed
by that inspection and a hand recurrence, not blind.
Record searched: R°|other.phase|opposite.phase|black.start + record|free
-> KIMI-QUESTIONS-3 D, WA3, RULE30-PRIZE8.39, GC549 checkpoint22.
P1: the correctly defined black-start free record at depth3 is4, not1.
P2: the existing WA3 data belong to the odd-time test under a black wall;
    do not reject that measurement, but reject its transfer to D.
Counterfactual: WA3's unchanged odd-time test is the mandatory black-clock
test. The explicit empty and11 patterns should expose that false transfer.
Controls: literal seven-cell shrinking left cones, the independent packed
wall update, and the independent inverse-column construction. Only the
four rows with five proposed zeros and the retained positive are checked;
no new record census, SAT call or right-language membership query.
Unexpected check: the empty black-wall pattern passes the first WRONG
odd-time test but fails the mandatory even-time test at0.
OUTCOME: P1 HELD; positive1100001 has near track1011101, black at
even0,2,4,6. Every seven-bit row ending in five zeros fails: first two
bits00/01 at0,10 at2,11 at6. Three independent controls PASS. P2 is
a source-scope finding, confirmed by the two explicit parity controls.
"""

from itertools import product


def cone(bits, phase):
    row = list(bits)
    near = [row[0]]
    for t in range(len(bits)-1):
        wall = (t+phase) % 2
        row = [(30 >> (4*row[k+1] + 2*row[k] +
                       (wall if k == 0 else row[k-1]))) & 1
               for k in range(len(row)-1)]
        near.append(row[0])
    return tuple(near)


def packed(bits, phase):
    width = len(bits)
    mask = (1 << width)-1
    row = sum(b << k for k, b in enumerate(bits))
    near = []
    for t in range(width):
        near.append(row & 1)
        row = ((row >> 1) ^ (row | (row << 1) | ((t+phase) % 2))) & mask
    return tuple(near)


def forced(v, phase, depth):
    N = depth+2
    right = [(t+phase) % 2 for t in range(N)]
    far = [v[t//2] if right[t] == 0 else 0 for t in range(N)]
    initial = []
    for _ in range(depth):
        left = [right[t+1] ^ (right[t] | far[t])
                for t in range(len(right)-1)]
        initial.append(left[0])
        far, right = right, left
    return tuple(initial)


def main():
    positive = (1, 1, 0, 0, 0, 0, 1)
    near = cone(positive, 1)
    assert near == packed(positive, 1)
    assert all(near[t] == 1 for t in (0, 2, 4, 6))
    assert forced((1, 0, 1, 0, 0), 1, 7) == positive
    failures = []
    for a, b in product((0, 1), repeat=2):
        bits = (a, b, 0, 0, 0, 0, 0)
        values = cone(bits, 1)
        assert values == packed(bits, 1)
        failure = next(t for t in (0, 2, 4, 6) if values[t] == 0)
        failures.append((a, b, failure))
    empty = cone((0,)*7, 1)
    assert empty[0] == 0 and empty[1] == 1
    assert near[0] == 1 and near[1] == 0
    print('P1 PASS: black-start Rdegree(3)=4; positive1100001, near', near)
    print('Every length5 zero band at depth3 fails:', failures)
    print('P2 scope control PASS: empty fails even0, passes odd1')
    print('Literal, packed and inverse-column controls PASS')


if __name__ == '__main__':
    main()
