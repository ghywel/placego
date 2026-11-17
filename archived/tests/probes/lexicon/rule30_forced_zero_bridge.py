"""GC1062: forced-zero next-bit repair includes its first future input.
Missing inference: GC1060's wrong future bit must be corrected together
with a compatible two-tick past, not by a free mid-orbit restart.
Record searched:0001|1010 with forced.zero|three.bit.*lift|
prefix.condition|next.bit.*lift|first.*exterior.*repair ->6 hits;
GC1060 supplies pair guard, GC1057 merger, GC605/606 old return gates.
P1 before controls: these are exactly the mixed-pair forced-R0,Q1
suffixes u,a,b,c:0001 and1010. Appending d=e=1 gives (Q,R,S)=101,
S=time2 next exterior, for either phase and every farther tail.
For S=0 use d=e=0 for0001, d=0,e=1 for1010; f arbitrary.
P2: a future controlled strip with final interior bit1 and penultimate1
can replace final bit by0 AND first exterior by1, copying later inputs;
all updated interiors then coincide at every future time. GC1057's
merger is reused. P1 supplies its actual two-tick origin, including input1.
This lifts a prefix plus ONE future input, not an arbitrary whole tail.
P3 white-phase root case: every free width5 strip initial0001p has
nine-symbol trace00110100b, b=(p OR E) AND NOT G, first inputs E,G.
Actual initial0001bb with arbitrary farther tail gives that same trace.
P3a: width4 initial111r has trace110100(r OR first exterior);
eight selected r,input and farther-input extremes check its mask identity.
Counterfactual: the forced-R0 repair still fails because input1 has no past.
Independent controls:32 local seven-cell cones,8 explicit three-bit lifts;
four selected translated controlled trajectories;16 root strip controls.
Unexpected: initial00010 and free inputs10 give endpoint1 at time8,
whereas every actual initial00010 gives endpoint0: the last initial
bit must change. Also changing the future bit while keeping first input0
fails the whole-child merger. No word, solver or width census.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def strip(start, inputs, phase=0):
    rows = [tuple(start)]
    value = sum(b << j for j, b in enumerate(start))
    mask = (1 << len(start))-1
    for t, exterior in enumerate(inputs):
        old = ((t+phase) & 1,) + rows[-1] + (exterior,)
        new = tuple(TABLE[4*old[j]+2*old[j+1]+old[j+2]]
                    for j in range(len(start)))
        value = (((value << 1) | ((t+phase) & 1)) ^
                 (value | (value >> 1) | (exterior << (len(start)-1)))) & mask
        assert new == tuple((value >> j) & 1 for j in range(len(start)))
        rows.append(new)
    return rows


def main():
    cones = lifts = root_cases = 0
    for suffix, phase in product(('0001', '1010'), (0, 1)):
        for d, e, f in product((0, 1), repeat=3):
            child = run(bits(suffix)+(d, e, f), 2, phase)[2]
            assert child[2:4] == (1, 0)
            if d == e == 1:
                assert child[4] == 1
            cones += 1
        for S in (0, 1):
            d, e = ((1, 1) if S else
                    ((0, 0) if suffix == '0001' else (0, 1)))
            child = run(bits(suffix)+(d, e, 0), 2, phase)[2]
            assert child[2:5] == (1, 0, S)
            lifts += 1
    for prefix, phase in product(('10101', '00110'), (0, 1)):
        inputs = (0, 0, 1, 1, 0, 1, 0, 0, 1)
        old = strip(bits(prefix+'11'), inputs, phase)
        new = strip(bits(prefix+'10'), (1,)+inputs[1:], phase)
        assert old[1:] == new[1:]
        unpaired = strip(bits(prefix+'10'), inputs, phase)
        assert unpaired[1] != old[1]
    for r, d, later in product((0, 1), repeat=3):
        controlled = strip(bits('111')+(r,), (d,)+(later,)*5)
        assert tuple(row[0] for row in controlled) == bits('110100')+(r | d,)
    for p, E, G, later in product((0, 1), repeat=4):
        b = (p | E) & (1-G)
        controlled = strip(bits('0001')+(p,), (E, G)+(later,)*6)
        actual = run(bits('0001')+(b, b)+(later,)*3, 8)
        wanted = bits('00110100')+(b,)
        assert tuple(r[0] for r in controlled) == wanted
        assert tuple(r[0] for r in actual) == wanted
        root_cases += 1
    print({'local_cones': cones, 'three_bit_lifts': lifts,
           'translated_mergers': 4, 'mask_identity_controls': 8,
           'root_controls': root_cases,
           'literal_packed': 'PASS', 'coupled_input_guard': 'PASS',
           'frozen_last_bit_counterexample': 'PASS'})


if __name__ == '__main__':
    main()
