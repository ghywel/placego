"""GC1058: white-penultimate initial rewrite has unbounded one-step cost.
Missing inference (CL222/GC1057): repair the white-penultimate case, and
determine whether a uniformly bounded initial suffix can always suffice
for a one-step coalescing outer-bit repair with the exterior held fixed.
Record searched: coalesc|merg|preimage|inverse with delta/difference/
boundary rewrite ->91 hits; white penultimate/10100/11001/fixed exterior
->42 hits; 11000/10110/0^n/rewrite ->17 hits. G13 and GC1040 read;
their inverse recurrence is reused, not proposed as a new theorem.
P1 before controls: for every n>=2, b in {0,1}, the suffixes
11 0^n b and 10 1^(n-1) 0 (1-b) have the same one-tick interior image
with black exterior, any common prefix and either wall phase.
P2: backward left-permutivity makes the opposite-last-bit preimage
unique, forcing n+1 changes and unbounded distance from the edge.
Counterfactual: every such one-step repair can use a fixed-radius suffix.
P3: n=1 and white exterior must fail; these guards are essential.
Independent controls: literal Wolfram table versus packed one-step;
backward reconstruction; selected n=2,3,7, not a width/language census.
Unexpected check: with the SAME actual farther tail, the two complete
rows still agree on the interior after TWO ticks: the common last child
is black and shields the necessarily different next exterior bits.
This does not persist unconditionally: b=1, farther tail101 makes the
last interior bits differ at time3. No all-trace or all-depth claim.
OUTCOME:36 family controls and108 actual two-tick controls PASS;
inverse uniqueness, n+1 cost and both negative controls PASS; the
third-tick actual divergence is retained. Universal result is hand
algebra awaiting second reading, not a finite scan inference.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def image(row, left, exterior):
    old = (left,) + row + (exterior,)
    literal = tuple((30 >> (4*old[j] + 2*old[j+1] + old[j+2])) & 1
                    for j in range(len(row)))
    w = sum(b << j for j, b in enumerate(row))
    packed = (((w << 1) | left) ^
              (w | (w >> 1) | (exterior << (len(row)-1))))
    assert literal == tuple((packed >> j) & 1 for j in range(len(row)))
    return literal


def reconstruct(child, last, exterior):
    # Existing G13 inverse, scanned right to left.
    old = [0] * (len(child)+2)
    old[-2:] = [last, exterior]
    for i in range(len(child), 0, -1):
        old[i-1] = child[i-1] ^ (old[i] | old[i+1])
    return old[0], tuple(old[1:-1])


def main():
    checked = 0
    actual = 0
    for n, b, phase, prefix in product((2, 3, 7), (0, 1), (0, 1),
                                      ('', '00', '101')):
        x = bits(prefix + '11' + '0'*n + str(b))
        y = bits(prefix + '10' + '1'*(n-1) + '0' + str(1-b))
        child = image(x, phase, 1)
        assert child == image(y, phase, 1)
        left = x[len(prefix)-1] if prefix else phase
        expected = (1-left, 0, 1) + (0,)*(n-2) + (b, 1)
        assert child[len(prefix):] == expected
        assert reconstruct(child, b, 1) == (phase, x)
        assert reconstruct(child, 1-b, 1) == (phase, y)
        assert sum(a != c for a, c in zip(x, y)) == n+1
        assert x[-2] == y[-2] == 0
        assert image(x, phase, 0) != image(y, phase, 0)
        for tail in ('000', '101', '111'):
            xr, yr = run(x + bits('1' + tail), 2, phase), run(y + bits('1' + tail), 2, phase)
            for t in (1, 2):
                assert xr[t][:len(x)] == yr[t][:len(y)]
            actual += 1
        checked += 1
    for b, phase in product((0, 1), repeat=2):
        assert image(bits('110' + str(b)), phase, 1) != image(bits('100' + str(1-b)), phase, 1)
    x, y = bits('11001'), bits('10100')
    xr, yr = run(x + bits('1010'), 3), run(y + bits('1010'), 3)
    assert xr[2][:5] == yr[2][:5]
    assert xr[3][4] != yr[3][4]
    print({'family_controls': checked, 'actual_two_tick_controls': actual,
           'literal_packed_inverse': 'PASS', 'unbounded_cost_formula': 'PASS',
           'n1_white_exterior_countercontrols': 'PASS',
           'third_tick_actual_divergence': 'PASS'})


if __name__ == '__main__':
    main()
