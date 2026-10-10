"""GC1078: an actual finite low-renewal core closes at every run length.
Missing inference: transport GC1077's returned010 through arbitrarily
many low L renewals, without assigning a fresh returned111.
Record searched: 111001010|H.D.H|high.*low.*high with
ancestr|inherit|transport|shield ->14 hits in7 files;
010.*011.*100|11100101 with ordinary|L0 and clos|invariant|shield
->21 hits in10 files. GC1053 supplies the closing map, GC1077 only
the first010-to-D step; neither supplies the finite core closure.
P1 BEFORE controls: C={010,011,100}, at origin sites7..9 after111001.
Each gives time1 sites6..8=101, then001,011,010,01 at times2..5.
The ordinary-L selector is D=0101100000. At time4 write E,F at9,10;
time5 sites8,9 are x=NOT E,y=E OR F, so x OR y=1.
P2: from this guard, time6 sites6..9=110B, time7=(1,0,NOT B,B OR K),
time8 sites6..8=(1,B,1), hence time9site8 Q=NOT B.
Q=0 forces time7 1001 and time8 1111, so time9site9 R=0.
GC1053 returns (NOT Q,Q OR R,Q XOR(R OR Z)), therefore C or101.
Every C origin renews D to L0; the only possible escape101 makes
H and returns S by GC1075. Induction gives an all-length invariant
component until its S escape; no later high LL after entering C.
Counterfactual: a generic mid01 D row can return111; the actual
x OR y guard is the information that excludes its renewal.
Unexpected check: relaxed time5 band010001000 (x=y=0,z=0,U=1)
returns111 under D; retain it as a non-origin relaxation witness.
Controls:6 initial local gates,8 one-step chain implications,
4 pair gates;96 guarded mid01 bands and32 unguarded bands;
48 selected actual origins (3 triples,8 tails,2 far constants)
with two successive returns, independent literal and packed engines.
These are local algebra controls, not language or record scans.
No solver or Local computation duplicated. Second reading pending.
OUTCOME: all predicted controls PASS. Eight free bands return111;
none of the96 guarded bands does. Selected actual returns:011=18,
010=13,100=11,101=6. All6 actual101 escapes have H then S;
the other42 have D then L0. No failed prediction in this block.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

D = bits('0101100000')
H = bits('0101101010')
CORE = {bits(w) for w in ('010', '011', '100')}
EXIT = bits('101')


def update(row):
    return tuple(row[k-1] ^ (row[k] | row[k+1])
                 for k in range(1, len(row)-1))


def band(row, start, end):
    rows = {start: row}
    for t in range(start, end):
        rows[t+1] = update((D[t],) + rows[t])
    return rows


def main():
    gates = chains = pairs = guarded = relaxed = origins = 0
    for tri in sorted(CORE):
        for far in (0, 1):
            assert update((D[0], 1) + tri + (far,))[:3] == bits('101')
            gates += 1
    for t, old, new in ((1, '101', '001'), (2, '001', '011'),
                        (3, '011', '010'), (4, '010', '01')):
        for far in (0, 1):
            assert update((D[t],) + bits(old) + (far,))[:len(new)] == bits(new)
            chains += 1
    for E, F in product((0, 1), repeat=2):
        out = update((D[4],) + bits('010') + (E, F))
        assert out[2:4] == (1-E, E | F)
        assert out[2] | out[3] == 1
        pairs += 1
    relaxed_high = 0
    for x, y in product((0, 1), repeat=2):
        for tail in product((0, 1), repeat=5):
            rows = band(bits('01') + (x, y) + tail, 5, 10)
            Q, R, Z = rows[9][2:5]
            out = rows[10][1:4]
            assert out == (1-Q, Q | R, Q ^ (R | Z))
            if x | y:
                B = x ^ (y | tail[0])
                assert rows[6][:4] == (1, 1, 0, B)
                assert rows[7][:4] == (1, 0, 1-B, B | rows[6][4])
                assert rows[8][:3] == (1, B, 1)
                assert Q == 1-B
                if Q == 0:
                    assert rows[7][:4] == bits('1001')
                    assert rows[8][:4] == bits('1111')
                    assert R == 0
                assert out in CORE | {EXIT}
                guarded += 1
            else:
                relaxed_high += out == bits('111')
                relaxed += 1
    assert relaxed_high > 0
    assert band(bits('010001000'), 5, 10)[10][1:4] == bits('111')
    outcomes = {}
    for tri in sorted(CORE):
        for tail in product((0, 1), repeat=3):
            for far in (0, 1):
                rows = run(bits('111001') + tri + tail + (far,)*24, 20)
                assert tuple(r[4] for r in rows[:10]) == D
                assert rows[10][:6] == bits('111001')
                returned = rows[10][6:9]
                assert returned in CORE | {EXIT}
                assert rows[5][7] | rows[5][8] == 1
                next_track = tuple(r[4] for r in rows[10:20])
                if returned == EXIT:
                    assert next_track == H
                    assert rows[20][:6] == bits('111010')
                else:
                    assert next_track == D
                    assert rows[20][:6] == bits('111001')
                key = ''.join(map(str, returned))
                outcomes[key] = outcomes.get(key, 0) + 1
                origins += 1
    assert (gates, chains, pairs, guarded, relaxed, origins) == (6, 8, 4, 96, 32, 48)
    print({'initial_gates': gates, 'chain_implications': chains,
           'pair_gates': pairs, 'guarded_bands': guarded,
           'relaxed_bands': relaxed, 'relaxed_111': relaxed_high,
           'selected_origins': origins, 'returned_triples': outcomes,
           'unexpected_free_band': 'PASS', 'literal_packed': 'PASS'})


if __name__ == '__main__':
    main()
