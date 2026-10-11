"""GC1091: black-eleventh SS reset permits high LL before an X exit.

Missing inference: GC1090's remaining black-eleventh admission branch.
Record searched: black.SS|black.eleventh|00011111 with
001|gate|past|admission ->37 hits in19 files; GC1080/1088/1090 read.
P1 before controls: actual A6..13=00011111 forces low6..11=100100.
HELD by the six-row Boolean shield, not by an admission census.
P2 before controls: this low cannot return111 through D. REFUTED:
the actual source below reaches111 at22. Selected composed controls
found61 such cases; their count is evidence only and not used here.
P3 before certificate: fixed30 cells of that witness force GC1080
family A at12, hence a high LL22..32 for every farther tail. HELD.
P4 before controls: returned32 low10,11=11 forces X32..41. HELD.
Counterfactual: black resets immediately enter C or bar high LL.
This all-tail cylinder refutes it, while itself exiting the S/L scope.
Unexpected: fresh A11=1,A13=0 source1110100011110 with white tail
was predicted to escape P1. REFUTED: it also has low6..11=100100.
No necessity of A13=1 for P1 is claimed, and no broader census made.
Independent controls: fresh-right prefix implications, scalar local
transport, then literal/packed complete histories with variable tails.
No solver, CUT, membership or record run. Universal admission and
the all-depth record bound remain OPEN. Next reassess check-free
hand target after CL263's replicated definition; no source extension.
"""
from itertools import product
from rule30_core_short_bridge import bits, update, propagate, S, D
from rule30_sl_no_refork import run

SOURCE = bits('111011111111000000100011110111')
SS = bits('111010')
H = bits('0101101010')
X = bits('0101100101')
CHECKPOINTS = {
    6: '1110100011111111010010000010',
    12: '1110010010010000100101100',
    22: '111001111100001101001',
    32: '1110010011101000',
    42: '111000101',
}


def certificate():
    rows = [SOURCE]
    for t in range(42):
        old = rows[-1]
        new = update((t % 2,) + old)
        if old[-1]:
            new += (old[-2] ^ 1,)
        for right in (0, 1):
            assert update((t % 2,) + old + (right,))[:len(new)] == new
        rows.append(new)
    for t, expected in CHECKPOINTS.items():
        assert rows[t] == bits(expected)
    assert tuple(r[4] for r in rows[:42]) == SS + S + D + H + X
    assert rows[12][9:17] == bits('00100001')
    return rows


def main():
    local = identity = composed = 0
    for q, r, s in product((0, 1), repeat=3):
        a = 1 - (q | r)
        h = (1-q) & (r | s)
        assert (a | h) == 1-q
        assert (q | r | (1-q)) == 1
        identity += 1
    for far in product((0, 1), repeat=8):
        rows = propagate(bits('00011111') + far, S)
        assert rows[1][:8] == bits('10110000')
        assert rows[2][:7] == bits('0010100')
        assert rows[3][:6] == bits('111011')
        assert rows[4][:6] == bits('100010')
        assert rows[5][:5] == bits('11011')
        assert rows[6][:6] == bits('100100')
        local += 1
    prefixes = certificate()
    for far in product((0, 1), repeat=5):
        for distant in (far*10, tuple(1-x for x in far)*10):
            rows = run(SOURCE + far + distant, 42)
            for t, prefix in enumerate(prefixes):
                assert rows[t][:len(prefix)] == prefix
            assert rows[6][10] == rows[6][12] == 1
            assert rows[22][6:9] == bits('111')
            assert rows[32][:6] == bits('111001')
            assert rows[34][9] == 1  # ordinary selector p: X, not D.
            composed += 1
    unexpected = run(bits('1110100011110') + (0,)*40, 6)
    assert unexpected[0][10] == 1 and unexpected[0][12] == 0
    assert unexpected[6][5:11] == bits('100100')
    print(dict(local_packets=local, boolean_identities=identity,
               prefix_implications=84, composed=composed,
               literal_packed='PASS', high_LL='ALL-TAIL at22..32',
               following_X='ALL-TAIL at32..42',
               universal_black_admission='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
