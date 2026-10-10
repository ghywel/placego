"""GC1051: hand exclusion of the typed L1-S-L0-L1 refork.
Missing inference: intersect GC1050's fork cylinders with actual L1-S past.
Record searched: L1.S.L0|1110010001 with ancestr|preimage|no.refork|
successor -> five hits, GC619/1047/1049; no complete image exclusion.
Predictions were recorded before each control in this order:
P1: S111011100 returns1110010001 iff sites10,11=11 and12 OR13=1.
P2: actual L1 returns that ten-bit prefix at16 iff time5 begins
011111000000011. REFUTED by constructed111000001110011100 plus zeros.
P3: constructed1110000011010001001 plus zeros has the target prefix.
REFUTED; the corrected P3b above also failed. These were informed hand
constructions, not random searches. A shifted intermediate coefficient
in GC1048 was isolated and corrected; its conclusions still pass.
P4, after corrected hand derivation: actual L1-S never enters the ten-bit
fork prefix, so typed L1-S-L0-L1 is impossible for every farther tail.
Proof: h=0 forces k=0 and time3 prefix1100001001. Translated GC1047
ancestry shield forbids time5sites11..14=0011, whereas the short
successor's required first11 bits force exactly that tuple.
Independent controls: literal and packed, both starting wall phases;
128 S cones,64 local black-phase gates,64 translated shields,64 L1
antecedents. These verify local implications, not an absence census.
Unexpected: relaxed1110111001110000000000000 reforks and passes the
GC1049 Horn clause, proving that retained L1 past is essential.
OUTCOME: P1/P4 local controls PASS; P2/P3/P3b REFUTED and retained.
The universal no-refork conclusion is a hand proof awaiting review.
"""
from itertools import product
from rule30_sl_collar import literal, packed


def bits(word):
    return tuple(map(int, word))


def run(start, duration, phase=0):
    if phase == 0:
        rows = literal(start, duration)
        assert rows == packed(start, duration)
        return rows
    rows = [tuple(start)]
    value = sum(bit << j for j, bit in enumerate(start))
    width = len(start)
    for t in range(duration):
        old = rows[-1]
        rows.append(tuple((((t + phase) & 1) if j == 0 else old[j-1])
                          ^ (old[j] | old[j+1])
                          for j in range(len(old)-1)))
        width -= 1
        value = (((value << 1) | ((t + phase) & 1))
                 ^ (value | (value >> 1))) & ((1 << width)-1)
        assert rows[-1] == tuple((value >> j) & 1 for j in range(width))
    return rows


def main():
    for tail in product((0, 1), repeat=7):
        row = bits("111011100") + tail
        end = run(row, 6)[-1]
        gate = tail[0] == tail[1] == 1 and bool(tail[2] | tail[3])
        assert (end[:10] == bits("1110010001")) == gate
    positives = 0
    for tail in product((0, 1), repeat=6):
        end = run(bits("0111110000") + tail, 5, 1)[-1]
        gate = tail[:4] == (0, 0, 1, 1) and bool(tail[4] | tail[5])
        assert (end[:11] == bits("11101110011")) == gate
        positives += gate
    shields = 0
    for tail in product((0, 1), repeat=6):
        end = run(bits("1100001001") + tail, 2, 1)[-1]
        if end[10:12] == (0, 0):
            shields += 1
            assert end[12:14] != (1, 1)
        rows = run(bits("111000001") + tail, 5)
        assert rows[2][:9] == bits("011110110")
        if rows[5][8] == 0:
            assert rows[5][9] == 0
            assert rows[3][:10] == bits("1100001001")
    for prefix in ("1110000011010001001", "111000001110011100"):
        rows = run(bits(prefix) + (0,)*(39-len(prefix)), 26)
        assert rows[16][:10] != bits("1110010001")
        if prefix.endswith("110011100"):
            assert rows[5][:15] == bits("011111000000011")
    old = bits("1110111001110000000000000")
    assert (old[9] & old[10]) <= old[11]
    assert run(old, 16)[-1][:9] == bits("111000001")
    print({"S_gate": 128, "black_gate": (64, positives),
           "shield": (64, shields), "L1_antecedents": 64,
           "independent_engines": "PASS", "relaxed_refork": "PASS",
           "P2_P3_P3b": "REFUTED", "P1_P4_controls": "PASS"})


if __name__ == "__main__":
    main()
