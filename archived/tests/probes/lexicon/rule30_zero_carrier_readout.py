"""GC1063: a forced-zero carrier is read back from its future trace.
Missing inference: handle GC1060's Q0,R0 guard, outside GC1062's merger.
Record searched:00110|11001100|1001000|1001001 with time.?5|time.?8|
readout|halfwidth|repair|first.*nine ->27 hits. GC1019 is the known
prepared100110 delay; it does not give this root1001 past normal form.
P1 before controls: every white-start controlled width4 row000r emits
00110r through time5. At time6, r1 gives0; r0 gives
b=NOT E AND(F OR G), first three exterior samples E,F,G.
P2: every free width5 row1001p emits11001100b through time8,
b=NOT S AND(H OR I), S=(p OR E) AND NOT G; E,G are its first
two samples and H,I the next two. Actual initial100100(NOT b),
with arbitrary farther tail, has the same trace, retaining first4 cells.
Counterfactual: the readout depends on later inputs, so matching future
traces cannot force R0. Controls: independent literal/packed updates;
32 selected width4 streams,32 root parameter cases with two actual tails.
Unexpected: white prefix010r emits1 at time5 for both r, even though
its penultimate is also0. Readout needs the full000 collar, not just Q0.
No solver, word-membership, width sweep or old delay-proof rerun.
The rootW5 cylinder closes; translation to arbitrary j remains missing.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_forced_zero_bridge import strip


def main():
    streams = origins = 0
    for r, E, F, G, later in product((0, 1), repeat=5):
        rows = strip(bits('000')+(r,), (E, F, G)+(later,)*3)
        b = (1-E) & (F | G) if r == 0 else 0
        assert tuple(row[0] for row in rows) == bits('00110')+(r, b)
        streams += 1
    for p, E, G, H, I in product((0, 1), repeat=5):
        S = (p | E) & (1-G)
        b = (1-S) & (H | I)
        rows = strip(bits('1001')+(p,), (E, G, H, I)+(0,)*4)
        wanted = bits('11001100')+(b,)
        assert rows[2][:5] == bits('0000')+(S,)
        assert tuple(row[0] for row in rows) == wanted
        for farther in (0, 1):
            actual = run(bits('100100')+(1-b,)+(farther,)*2, 8)
            assert tuple(row[0] for row in actual) == wanted
            assert actual[2][4] == 0
            assert actual[2][5] | actual[2][6] == b
            origins += 1
    for r, exterior in product((0, 1), repeat=2):
        rows = strip(bits('010')+(r,), (exterior,)*6)
        assert rows[5][0] == 1
    print({'readout_streams': streams, 'root_parameter_cases': 32,
           'actual_origin_controls': origins, 'wrong_collar_controls': 4,
           'literal_packed': 'PASS', 'time5_readout': 'PASS',
           'nine_symbol_repair': 'PASS'})


if __name__ == '__main__':
    main()
