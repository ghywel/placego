"""GC1059: every two-tick free strip can be normalized to an actual cone.
Missing inference (CL222/GC1058): does an inconsistent next exterior
really require the unbounded outer-bit rewrite, or can its effect be
masked while preserving the observed two interior rows?
Record searched: trace/halfwidth/repair with two-tick/two-step/preimage
->59 hits; strip/exterior/repair with two-tick/time2 and initial/prefix
->28 hits. GC1042, GC1057/1058 and known inverse/reset record reused;
no uniform two-tick initial-prefix normalization found.
P1 before controls: for EVERY W>=2, arbitrary initial row and two free
exterior samples, an actual initial cone preserves initial sites1..W-1
and BOTH complete interior rows at times1,2; only initial siteW may flip.
Construction: exterior E=0 permits any next G by F=b XOR G. E=1 forces
next exterior NOT b. If this disagrees with G, flip b only when the
penultimate cell is black; otherwise the common black child masks G.
Counterfactual: a white penultimate cell needs GC1058's unbounded rewrite
to normalize the next exterior. P1's no-flip branch must refute it.
Independent controls: literal Wolfram table and packed strip versus
shrinking actual cones, all64 width3 local cases, not a width census.
Unexpected negative check: W=1, black-start, initial0 and exterior10
emits000, impossible for any actual row retaining initial first0.
Thus W>=2 is essential for preserving the first initial trace bit.
No claim of iteration to 2W-1 samples or any all-depth record bound.
OUTCOME:all64 local controls PASS;8 flip the last initial bit,8 mask
an actually different next exterior. Long white no-flip control and
width1 countercontrol PASS. Universal construction is hand proof
awaiting review, not extrapolation from these controls.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def normalize(initial, E, G):
    assert len(initial) >= 2
    row = list(initial)
    flipped = E == 1 and G == row[-1] and row[-2] == 1
    if flipped:
        row[-1] ^= 1
    F = row[-1] ^ G if E == 0 else 0
    return tuple(row) + (E, F), flipped


def main():
    count = flips = masks = 0
    for initial, E, G, phase in product(product((0, 1), repeat=3),
                                        (0, 1), (0, 1), (0, 1)):
        wanted = strip(initial, (E, G), phase)
        cone, flipped = normalize(initial, E, G)
        assert cone[:2] == initial[:2]
        actual = run(cone, 2, phase)
        assert actual[1][:3] == wanted[1]
        assert actual[2][:3] == wanted[2]
        if E == 1 and G == initial[-1] and initial[-2] == 0:
            assert not flipped and wanted[1][-1] == 1
            assert actual[1][3] != G
            masks += 1
        for farther in (0, 1):
            extended = run(cone + (farther,)*3, 2, phase)
            assert extended[2][:3] == wanted[2]
        count += 1
        flips += flipped
    # Long white penultimate example from GC1058: no large rewrite needed.
    initial = bits('110000001')
    cone, flipped = normalize(initial, 1, 1)
    assert not flipped and cone[:len(initial)] == initial
    wanted = strip(initial, (1, 1))
    actual = run(cone, 2)
    assert actual[1][:len(initial)] == wanted[1]
    assert actual[2][:len(initial)] == wanted[2]
    assert trace(strip((0,), (1, 0), 1)) == bits('000')
    for tail in product((0, 1), repeat=2):
        assert trace(run((0,) + tail, 2, 1)) != bits('000')
    print({'two_tick_local_cases': count, 'one_bit_flips': flips,
           'masked_inconsistent_exteriors': masks,
           'literal_packed_actual': 'PASS', 'long_white_no_flip': 'PASS',
           'W1_countercontrol': 'PASS'})


if __name__ == '__main__':
    main()
