"""GC1134: can an untyped white SS prepare the known white-A escape?

Missing inference: GC1104 and GC1130 admit white-A exits only with
their A-S-D-H ancestry. Is the preceding white SS alone sufficient?
Test the already retained GC1090 fresh counter, rather than widening
a strip, enumerating words, or making another bare-age origin scan.
Record searched: 11101000110110100010|fresh.white.A AND
SS|parent|counter -> 5 hits in 3 files; GC1090, GC1104 and GC1131
read. None supplies this counter's white-SS antecedent.
P1 BEFORE run: GC1090's 20-cell counter, padded with eight whites
to fix the next 16-tick causal cone, has no six-tick white-SS past.
Counterfactual: a retained white-SS ancestor reaches high111 after
the next S-D without any old black-A origin; white SS alone cannot
import the admission theorem. If no ancestor exists, exclude only
this fixed cylinder, not all white-A escapes or all pad choices.
Controls: every inverse edge forward checked; wall phases retained;
literal and packed full trajectory; GC1090's admitted black-SS
source remains a contrasting positive for the narrower theorem.
Unexpected check: a six-tick ancestor might use a different fifth
track or a black sixth marker. Require both realized SS and white
marker before accepting the entrance. Enumerate all six inverse
layers, at most 4**6 parents, not a chosen free-boundary strip path.
No solver, CUT, membership, record or wider-strip run. No infinite
right-half realization search or global admission conclusion.

First outcome: the padded TARGET has four one-step parents but no
two-step parent. P1 HELD vacuously for white SS, so it does not
identify an SS-specific admission guard. Do not use its padding.
P2 BEFORE the exact cone check: after releasing all incidental
padding, the original 20-cell counter has a white-SS parent, and
some assignment to the remaining five causal source cells gives
high111 at22. This would refute admission from white SS alone.
The complete six-step inverse of the 20-cell word fixes 26 cells;
adding five gives the full 31-cell cone of the endpoint's nine
cells. Check every such five-bit extension, not repeated padding
variants or an age scan. If none works, stop this named entrance.
Second outcome: the unpadded counter also has counts 4,0,0,0,0,0.
P2 REFUTED before the SS filter; no forward extension is tested.
P3 BEFORE compressing this certificate: the four first parents'
common 17-cell prefix 00101110100010111 has no white-wall parent.
If false, retain the complete four-parent table instead; no shorter
prefix search or broader maturity claim follows from this check.
P3 HELD. Hand deduction before controls: its first four cells 0010
already have no white-wall parent. An output 0010 against wall0
forces successive parent cells a1=a2=a3=0, a4=1, then a4 OR a5=0.
Check all 32 five-cell inputs independently. Contrast GC1131's
white-A packet 11101000110110110111: predict it has a two-tick past,
so this exclusion cannot be promoted to all mature white-A states.
REFUTED-BY: any retained white-wall parent of 0010 or a two-step
parent of the original 20-cell counter invalidates the exclusion.
OUTCOME: fixed and unpadded counter counts 4,0,0,0,0,0; P1 HELD,
P2 REFUTED, P3 HELD. No white-SS-specific absence was established.
"""
from itertools import product
from rule30_black_A_ancestry_guard import inverse
from rule30_core_short_bridge import S, D
from rule30_sl_no_refork import bits, run

SS = bits('111010')
TARGET = bits('11101000110110100010' + '00000000')


def main():
    assert tuple(y[4] for y in run(TARGET, 16)[:16]) == S + D
    assert run(TARGET, 16)[16][:9] == bits('111001111')
    rows = {TARGET}
    counts = []
    for t in range(5, -1, -1):
        rows = {x for y in rows for x in inverse(y, t % 2)}
        counts.append(len(rows))
    selected = []
    other_track = black_marker = 0
    for x in sorted(rows):
        past = run(x, 6)
        assert past[6] == TARGET
        if tuple(y[4] for y in past[:6]) != SS:
            other_track += 1
        elif x[5]:
            black_marker += 1
        else:
            selected.append(x)
    print('inverse_counts', counts, 'white_SS', len(selected),
          'other_track', other_track, 'black_SS', black_marker,
          'P1_no_white_SS_parent', not selected, flush=True)
    if selected:
        source = selected[0]
        complete = run(source, 22)
        assert complete[6] == TARGET
        assert complete[22][:9] == bits('111001111')
        assert tuple(y[4] for y in complete[:22]) == SS + S + D
        checked = 0
        for tail in product((0, 1), repeat=5):
            full = run(source + tail, 22)
            for t, prefix in enumerate(complete):
                assert full[t][:len(prefix)] == prefix
            checked += 1
        print('source', ''.join(map(str, source)), 'ticks', 22,
              'white_A6', ''.join(map(str, complete[6])),
              'high11122', ''.join(map(str, complete[22])),
              'visible_even', ''.join(str(y[0]) for y in complete[::2]),
              'exterior_controls', checked, 'scalar_packed_PASS', flush=True)
    controls = 0
    for source in ('11101111111100', '1110111111101'):
        for far in product((0, 1), repeat=5):
            full = run(bits(source) + far + (0,) * 30, 22)
            if not full[6][10]:
                assert full[22][6:9] in {bits(w) for w in ('010', '011')}
                controls += 1
    print('narrower_black_SS_admission_controls', controls,
          'all_depth_bound', 'OPEN', flush=True)
    rows = {TARGET[:20]}
    counts = []
    for t in range(5, -1, -1):
        rows = {x for y in rows for x in inverse(y, t % 2)}
        counts.append(len(rows))
    whites = []
    for x in sorted(rows):
        past = run(x, 6)
        assert past[6] == TARGET[:20]
        if not x[5] and tuple(y[4] for y in past[:6]) == SS:
            whites.append(x)
    good = []
    tested = 0
    for x in whites:
        for far in product((0, 1), repeat=5):
            full = run(x + far, 22)
            tested += 1
            if (tuple(y[4] for y in full[:22]) == SS + S + D
                    and full[22][:9] == bits('111001111')):
                good.append((x + far, full))
    print('unpadded_inverse_counts', counts,
          'unpadded_white_SS_parents', len(whites),
          'complete_31_cell_cones', tested, 'high111_cones', len(good),
          'P2_white_SS_escape', bool(good), flush=True)
    if good:
        source, full = good[0]
        print('unpadded_source', ''.join(map(str, source)),
              'white_A6', ''.join(map(str, full[6])),
              'low12', ''.join(map(str, full[12])),
              'high11122', ''.join(map(str, full[22])),
              'visible_even', ''.join(str(y[0]) for y in full[::2]),
              'scalar_packed_PASS', flush=True)
    first = inverse(TARGET[:20], 1)
    expected = {
        bits('001011101000101110101'),
        bits('001011101000101110110'),
        bits('001011101000101110111'),
        bits('001011101000101111000'),
    }
    assert first == expected
    assert all(x[:4] == bits('0010') for x in first)
    assert not inverse(bits('0010'), 0)
    local = 0
    for x in product((0, 1), repeat=5):
        image = run(x, 1)[1]
        assert image != bits('0010')
        local += 1
    contrast = bits('11101000110110110111')
    parents = {x for y in inverse(contrast, 1) for x in inverse(y, 0)}
    assert parents
    for x in parents:
        assert run(x, 2)[2] == contrast
    print('first_parent_table_PASS', 'white_wall_local_controls', local,
          'mature_contrast_parents', len(parents), flush=True)


if __name__ == '__main__':
    main()
