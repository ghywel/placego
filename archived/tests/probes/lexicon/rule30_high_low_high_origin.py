"""GC1079: actual inherited001 can renew high after one low unit.
Missing inference: does GC1078's C closure absorb the b=0 high-LL
branch after its001-to-D continuation? Hand reconstruction instead
produced an explicit all-tail HDH cylinder, before controls.
Record searched:111001001|001.*high|high.*001 with
inherit|transport|renew|shield|origin ->29 hits in9 files;
exact111001111011111110010|100011000001 with origin|shield|return
->no hit. GC1077/78 leave this branch open.
P1 BEFORE controls: origin111001111011111110010, any farther tail,
has H then D then H as consecutive ordinary-long fifth tracks.
First H returns001 on marker b=0; D returns111. Therefore high
cannot be made a permanent transient using C closure alone.
The following finite prefix certificate supplies every universal
step; it is not a finite sample extrapolated to arbitrary tails.
P2: current time5 prefix100011000001 and next time15 prefix010001
carry the exceptional x=y=0 low band from GC1078 on an ACTUAL
history. This is the unexpected check: the relaxed111 transition
is excluded from C but is realizable with the other inherited past.
Counterfactual: every inherited001-to-D continuation enters C.
Controls:40 one-step prefix implications with fresh right bits;
32 selected actual21-bit cylinder controls,4 more initial bits and
two far constants,30 ticks, independent literal and packed engines.
Third H's return is observed, not presumed in the prediction.
No solver, membership census, longer scan or relaxed-record run.
OUTCOME:40 universal one-step gates and32 actual cylinder controls
PASS. All third H returns in these controls have prefix111011;
that return statement is sampled only, not the all-tail theorem.
The proposed absorption of inherited001 into C is REFUTED by
the all-tail HDH certificate; repeated high LL remains undecided.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

H = bits('0101101010')
D = bits('0101100000')
ORIGIN = '111001111011111110010'
TRACK = H + D + H
# Prefixes at sites6 onward, before each update. Beyond a prefix
# the right bit is arbitrary; black OR inputs may retain its length.
PREFIXES = (
    '1111011111110010',
    '100001000000111',
    '010011100001100',
    '11111001001101',
    '0000011111100',
    '100011000001',
    '110110100011',
    '000100110110',
    '00111110010',
    '1110000111',
    '1001001100',
    '111111101',
    '000000001',
    '000000011',
    '100000110',
    '01000110',
    '11101',
    '10001',
    '1101',
    '1001',
    '1111',
)


def update(row):
    return tuple(row[k-1] ^ (row[k] | row[k+1])
                 for k in range(1, len(row)-1))


def main():
    gates = origins = 0
    for t, (old, new) in enumerate(zip(PREFIXES, PREFIXES[1:])):
        for fresh in (0, 1):
            out = update((TRACK[t],) + bits(old) + (fresh,))
            assert out[:len(new)] == bits(new), (t, fresh, out, new)
            gates += 1
    third_returns = {}
    for tail in product((0, 1), repeat=4):
        for far in (0, 1):
            rows = run(bits(ORIGIN) + tail + (far,)*36, 30)
            assert tuple(r[4] for r in rows[:30]) == TRACK
            for t, prefix in enumerate(PREFIXES):
                assert rows[t][5:5+len(prefix)] == bits(prefix)
            assert rows[5][8] == 0
            assert rows[10][:12] == bits('111001001001')
            assert rows[15][5:11] == bits('010001')
            assert rows[20][:9] == bits('111001111')
            kind = ''.join(map(str, rows[30][:6]))
            third_returns[kind] = third_returns.get(kind, 0) + 1
            origins += 1
    assert (gates, origins) == (40, 32)
    print({'one_step_shields': gates, 'selected_origins': origins,
           'third_H_returns': third_returns,
           'HDH_all_tail_certificate': 'PASS',
           'actual_exceptional_low_band': 'PASS', 'literal_packed': 'PASS'})


if __name__ == '__main__':
    main()
