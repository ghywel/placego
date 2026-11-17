"""GC1081: an inherited high LL repeats after one D renewal.
Missing inference: actual preimage of GC1080 B. Record searched:
00110000|11100100100110000|high.*low.*high with inherited/origin
guards ->29 hits in11 files; exact new source or100011000001111
with origin/shield/return/repeat ->0 hits. GC1080 leaves B open.
P1 BEFORE controls: source111001111011111110011101 (24 bits),
any farther tail, has H,D,H with BOTH H returns L0. At10 its
ordinary001 origin lies in B; at20 its prefix is1110011111000.
P2: a finite one-step shield through20 plus the reviewed GC1080
decoder proves the all-tail third return; a sampled far tail alone
does not. Each shield is checked with a fresh arbitrary right bit.
P3 BEFORE joint-band controls: on time5prefix10001100, B at10
iff sites14..20=0001111, sites21 OR22=1, and the pair21,22 is
not11 or sites23,24 are00. At10 sites18,19 then read01.
Counterfactual: every inherited H-D-H ends its third H in S.
Unexpected check: flip only initialsite21 to0; the resulting
GC1079 sibling has the same H,D,H tracks but its third H ends S.
Controls:40 local one-step implications,2048 local Boolean-band
assignments,64 selected actual sibling histories, literal and packed
engines. No solver, language membership or relaxed-record census.
OUTCOME is recorded after execution in RULE30-GPT.md GC1081.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_001_high_return_gate import band

H = bits('0101101010')
D = bits('0101100000')
TRACK = H + D + H
ORIGIN = '111001111011111110011101'
PREFIXES = (
    '1111011111110011101', '1000010000001110001',
    '0100111000011001011', '1111100100110111010',
    '000001111110010001', '100011000001111011',
    '110110100011000010', '00010011011010011',
    '00111110010011110', '1110000111111000',
    '100100110000010', '11111110100011',
    '00000000110110', '0000000110010',
    '100000110111', '010001100100',
    '11101101111', '10001001000',
    '1101111110', '100100000', '11111000',
)


def update(row):
    return tuple(row[k-1] ^ (row[k] | row[k+1])
                 for k in range(1, len(row)-1))


def inherited_gate(tail):
    return (tail[:7] == bits('0001111') and bool(tail[7] | tail[8])
            and (tail[7:9] != (1, 1) or tail[9:11] == (0, 0)))


def main():
    shields = bands = positives = actual = 0
    for t, (old, new) in enumerate(zip(PREFIXES, PREFIXES[1:])):
        for fresh in (0, 1):
            out = update((TRACK[t],) + bits(old) + (fresh,))
            assert out[:len(new)] == bits(new), (t, fresh, out, new)
            shields += 1
    for tail in product((0, 1), repeat=11):
        rows = band(bits('10001100') + tail + (0,)*8, 5, 10, H)
        target = (rows[10][4:12] == bits('00110000')
                  and bool(rows[10][12] | rows[10][13]))
        assert target == inherited_gate(tail), tail
        if target:
            assert rows[10][12:14] == (0, 1)
            positives += 1
        bands += 1
    sibling = list(bits(ORIGIN))
    sibling[20] = 0
    for root, expected in ((bits(ORIGIN), True), (tuple(sibling), False)):
        for tail in product((0, 1), repeat=4):
            for far in (0, 1):
                rows = run(root + tail + (far,)*40, 30)
                assert tuple(r[4] for r in rows[:30]) == TRACK
                assert rows[10][:9] == bits('111001001')
                assert rows[20][:9] == bits('111001111')
                assert (rows[30][:6] == bits('111001')) == expected
                if expected:
                    for t, prefix in enumerate(PREFIXES):
                        assert rows[t][5:5+len(prefix)] == bits(prefix)
                    assert rows[10][9:19] == bits('0011000001')
                    assert rows[20][:13] == bits('1110011111000')
                else:
                    assert rows[30][4] == 1
                actual += 1
    assert (shields, bands, positives, actual) == (40, 2048, 9, 64)
    print({'one_step_shields': shields, 'joint_band_controls': bands,
           'positive_joint_bands': positives, 'actual_siblings': actual,
           'unexpected_single_bit_S_sibling': 'PASS',
           'literal_packed': 'PASS'})


if __name__ == '__main__':
    main()
