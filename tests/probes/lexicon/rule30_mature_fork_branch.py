"""GC1052: one mature short-to-long branch cannot feed the hidden fork.
Missing inference: locate possible restarts of GC1051's barred refork.
Reuse GC1014/629's three mature S-to-L0 prefixes; test a hand transport
for111010011 rather than sweep longer mixed words or run a solver.
Record searched: S.L0.L1|short.*fork|111010110|111011101 with gate|
preimage|ancestr|successor ->6 hits, GC1049/1051 and references, no
three-branch fork precursor. Broader noisy L1 search was discarded.
Before controls P1:111010011 returns L0 with c7 OR c8=1 for every tail.
P2: for111010001 the fork ten-bit gate was predicted as the union of
 efg hi=00001;
 efg hi=10000 and j OR k=1;
 efg=011, h OR i=1, NOT(h AND i AND j),
with e..k atsites10..16. REFUTED by initial1110100010000100, whose
six-tick first10 are1110010101. The hand time4site6 was mistakenly
made white; it is black. Stop that gate classification this block.
Counterfactual: every mature S-to-L0 branch feeds a further L1. P1
blocks it since GC1050 requires the L0 entrance's sites7,8 both white.
Informed P3 after observing only01/10: w=initialsite10 OR11; w=0
forces q=1, giving H=I=0. Thus returnedpair=(1-w,w). This new hand
selector was predicted before its added assertions.
Controls:128 complete B six-tick cones; literal versus packed.
Unexpected: startup111010010 realizes SL but violates GC1014 maturity;
exclude it from the three-prefix list, not from the actual startup game.
The retained relaxed1110111001110... does refork, preventing extension
of B's obstruction to every S-to-L0 prefix. No age-two lift claimed.
OUTCOME: P1/P3 HELD,128 complete local controls PASS; P2 REFUTED and
retained, no repaired variants or larger mixed-return scan proposed.
"""
from itertools import product
from rule30_sl_collar import literal, packed


def bits(word):
    return tuple(map(int, word))


def run(start, duration):
    rows = literal(start, duration)
    assert rows == packed(start, duration)
    return rows


def main():
    pairs = set()
    for tail in product((0, 1), repeat=7):
        rows = run(bits("111010011") + tail, 6)
        assert rows[2][:8] == bits("01011000")
        w, q = rows[2][8:10]
        assert w == (tail[0] | tail[1])
        assert w or q == 1
        assert rows[3][5:9] == (1, 0, w, w | q)
        assert rows[4][4:8] == (0, 1, 1-w, w | q)
        assert rows[5][5:7] == (1, 0)
        H, I = rows[5][7:9]
        assert rows[6][:6] == bits("111001")
        assert rows[6][6:8] == (1-H, H | I)
        assert rows[6][6] | rows[6][7]
        assert rows[6][6:8] == (1-w, w)
        pairs.add(rows[6][6:8])
    row = bits("1110100010000100") + (0,)*9
    rows = run(row, 16)
    assert rows[4][5] == 1
    assert rows[6][:10] == bits("1110010101")
    startup = bits("111010010") + (0,)*16
    assert run(startup, 6)[-1][:6] == bits("111001")
    a, b, c, d = startup[5:9]
    assert a == b == 0 and c > d  # violates the reviewed maturity gate
    old = bits("1110111001110000000000000")
    assert run(old, 16)[-1][:9] == bits("111000001")
    print({"complete_branch_cones": 128, "returned_pairs": sorted(pairs),
           "P1_P3": "HELD", "P2": "REFUTED", "independent_engines": "PASS",
           "startup_and_relaxed_countercontrols": "PASS"})


if __name__ == "__main__":
    main()
