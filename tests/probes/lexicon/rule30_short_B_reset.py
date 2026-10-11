"""GC1085: a B label alone does not close the core's mixed history.

Missing inference: can inherited S-B restart A through its high101 image?
GC1052 already makes B always SL; GC1084's proposed B-toSS target was
vacuous. Its mature A/B table classifies SL sources, not every S image.
Record searched:1110011011|111010011 with return.*B|SS|short.*short|core
->23 hits in8 files; GC1052/1056/1074/1083 read, no B-reset obstruction.
P1 BEFORE controls: B-to101 cannot satisfy the A antecedent11100/1101*.
REFUTED:30 of512 complete six-tick cones satisfy it, all with11011.
P2 BEFORE controls: reported core-like1011000*/10111110 packets force
the subsequent B10 OR11=1. REFUTED:32 of256 and64 of128 complete high
cones have B10,11=00. Fresh high packets do not certify a core past.
Stop these B-label shortcuts; do not repair them by a prefix sweep.
P3 BEFORE controls: the20-bit cylinder below gives B-to101-toA-to001
for every tail. Six exact prefix updates plus reviewed GC1083 prove it.
Counterfactual: a B label can be made absorbing by excluding SS alone.
Unexpected: the all-white f,g,h,i gate still selects high (GC1074);
both reported core-like packets also admit white B10,11, defeating P2.
Independent controls: literal versus packed;64 chosen farther patterns
check the composed witness. No core-origin existence, membership,
solver, relaxed-record or Local run. Full mixed closure remains OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import update

PREFIXES = (
    '11101001100111010000',
    '1000111101110001100',
    '010110000100101101',
    '11010100111110100',
    '0001011110000011',
    '001101000100011',
    '11100110111011',
)


def main():
    # Actual wall input at site0 is t mod2. Each complete retained prefix
    # updates to the next; unknown farther cells cannot affect it.
    for t, (old, new) in enumerate(zip(PREFIXES, PREFIXES[1:])):
        assert update((t % 2,) + bits(old)) == bits(new)
    positive = 0
    for far in product((0, 1), repeat=6):
        rows = run(bits(PREFIXES[0]) + far + tuple(1-x for x in far), 22)
        assert rows[6][:14] == bits(PREFIXES[-1])
        assert rows[16][:10] == bits('1110100011')
        assert rows[16][11] == 1
        assert rows[22][:9] == bits('111001001')
        positive += 1
    # Keep one literal witness for each refuted shortcut; the exploratory
    # cone counts in the docstring are evidence, not the all-tail proof.
    for high in ('111001101100000100000', '111001101111100000000'):
        rows = run(bits(high), 10)
        assert rows[10][:11] == bits('11101001100')
    assert run(bits('1110100110000000') + (0,)*8, 6)[6][6:9] == bits('101')
    print(dict(prefix_implications=6, composed_controls=positive,
               literal_packed='PASS', P1='REFUTED', P2='REFUTED',
               B_SS_target='already barred by GC1052',
               actual_core_reset='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
