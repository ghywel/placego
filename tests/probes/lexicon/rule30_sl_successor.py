"""GC1048: correlated successor of an alternative long loop.
Missing inference (CL214): transport through L1-S while retaining the
ninth-bit entrance premise, rather than treating the successor as free S.
Record searched: L1|alternative.long|111000001 with fifth|sixth|successor|
correlat|profile -> existing returns, no successor-pair theorem;
0010010010|0000110110|111011100 -> no relevant hand result. GC622 and
corrected GC609 are reused. GC689 is an all-S cross-return gate, distinct.
Predictions registered before execution, 2026-10-10:
P1: all L1 cones have fifth/sixth tracks0010010010/0000110110.
P2: h=c9(5), j=c9(8) give c6(10)=NOT h, c7(10)=1,
      h=1 implies c8(10)=1, and c5(16)=h OR NOT j.
P3: both following S and following L0 occur after L1-S.
Counterfactual: forgetting the ninth entrance bit preserves these facts.
Unexpected check: vary that bit alone in two otherwise identical full
cones and retain a literal violation, without claiming a visible absence.
Controls: literal shrinking cones versus packed cones; complete site22
cone for the sixteen-tick return. No solver or visible-language census.
OUTCOME: P1/P2/P3 HELD on8,192 complete cones; both successors
occur. Independent engines PASS. Ninth-bit countercontrol returns
10011000 versus11101011, so the entrance premise is essential.
"""
from itertools import product
from rule30_sl_collar import literal, packed


def main():
    outcomes = set()
    count = 0
    for tail in product((0, 1), repeat=13):
        start = tuple(map(int, "111000001")) + tail
        rows = literal(start, 16)
        assert rows == packed(start, 16)
        h, j = rows[5][8], rows[8][8]
        k, r, s = rows[5][9:12]
        # GC1051 fixes a shifted coefficient in the original hand text.
        assert rows[6][7:11] == (h, h | k, h ^ (k | r), k ^ (r | s))
        assert rows[7][7:9] == (1-(h | k), h ^ (h | k | r))
        assert "".join(str(r[4]) for r in rows[:10]) == "0010010010"
        assert "".join(str(r[5]) for r in rows[:10]) == "0000110110"
        assert rows[10][5:7] == (1-h, 1)
        assert not h or rows[10][7] == 1
        assert rows[16][:4] == (1, 1, 1, 0)
        assert rows[16][4] == (h | (1-j))
        if rows[16][4] == 0:
            assert rows[16][5] == 1
        outcomes.add("S" if rows[16][4] else "L0")
        count += 1
    assert outcomes == {"S", "L0"}
    counter = []
    for ninth in (0, 1):
        start = tuple(map(int, "11100000" + str(ninth))) + (0,)*13
        rows = literal(start, 16)
        assert rows == packed(start, 16)
        counter.append("".join(map(str, rows[10][:8])))
    assert counter[0][:4] != "1110" and counter[1][:4] == "1110"
    print({"complete_cones": count, "successors": sorted(outcomes),
           "ninth_bit_counter": counter, "P1_P2_P3": "HELD",
           "literal_packed": "PASS"})


if __name__ == "__main__":
    main()
