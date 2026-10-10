"""GC1047: correlated transport into the alternative long entrance.

Missing inference: what backward correlation does an L0 -> L1 switch
impose beyond GC1046's four-column collar?
Record searched: 0101100101 with L|long|return|column -> wheel/slab
substring hits, no switch transport; GC744's 010110zhzk and GC619's
two exceptional prefixes are reused, not claimed anew.

Registered before controls (GPT, 2026-10-10):
P1: for every L0 cylinder cone, its return has sites5,6 both zero iff
z=0, r=0, s OR e=1, where z=c6(5), (r,s,e)=(c6,c7,c8)(8).
This forces the preceding fifth-column profile0101100101.
Counterfactual: that fifth-column profile alone forces a full L1 entrance.
Unexpected control: GC619's actual 13-bit prefixes ending0 or1 have the
same preceding fifth track and first eight return bits, but different
ninth return bits, so one fails to enter L1. Two farther-tail extremes.
Independent controls: literal shrinking cones versus packed updates,
all 1,024 assignments through site16 for the exact pair criterion;
four fixed site19 cones for the ninth-bit countercontrol. No solver,
language census, new width scan or assumption of independent hidden bits.
Informed P3, after P1's three-profile result and before its separate checks:
Further record search of all three strings finds ALS/ALX's two sampled
all-L fifth profiles, not a complete all-tail selector proof.
z=c6(5), a=c7(5) exactly select the fifth-track suffix: 00 -> 0101,
01 -> 0000, 1* -> 1010. Moreover the closing pair is00 iff (z,a)=00.
The new hand obligation is the correlated ancestry shield: (z,a)=00
forces c8(5) XOR c9(5)=1; these are not free row variables.
OUTCOME: P1/P3 HELD on 1,024 cones, 112 with the closing zero pair.
Exactly three fifth profiles occur. Exceptional ninth-bit countercontrol
PASS: the profile forces the closing pair, not the complete L1 entrance.
"""

from rule30_sl_collar import all_rows, literal, packed


def main():
    count = pair00 = 0
    profiles = set()
    for _, rows in all_rows("111001", 10):
        z = rows[5][5]
        r, s, e = rows[8][5:8]
        actual = rows[10][4:6] == (0, 0)
        gate = z == 0 and r == 0 and (s | e) == 1
        assert actual == gate
        fifth = "".join(str(row[4]) for row in rows[:10])
        a = rows[5][6]
        assert fifth == "010110" + ("1010" if z else "0000" if a else "0101")
        assert actual == (z == a == 0)
        if z == a == 0:
            assert rows[5][7] ^ rows[5][8] == 1
        if rows[2][6:8] == (0, 0):
            assert rows[2][8:10] != (1, 1)
        if actual:
            assert fifth == "0101100101"
            pair00 += 1
        profiles.add(fifth)
        count += 1
    assert pair00 > 0
    unexpected = []
    for final in (0, 1):
        for farther in (0, 1):
            start = tuple(map(int, "111001000100" + str(final))) + (farther,) * 6
            rows = literal(start, 10)
            assert rows == packed(start, 10)
            assert "".join(str(row[4]) for row in rows[:10]) == "0101100101"
            end = "".join(map(str, rows[10][:9]))
            assert end == "11100000" + str(1 - final)
            unexpected.append(end)
    print({"complete_pair_cones": count, "pair00": pair00,
           "fifth_profiles": sorted(profiles), "unexpected": unexpected,
           "P1": "HELD", "P3": "HELD", "counterfactual": "REFUTED",
           "literal_packed": "PASS"})


if __name__ == "__main__":
    main()
