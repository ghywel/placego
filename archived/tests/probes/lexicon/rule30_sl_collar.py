"""GC1046: controls for the mixed S/L four-column collar, not a language census.

Missing inference: which finite coefficient types suffice for the synchronized
mixed S/L collar in CL213's proposed typed exterior composition?
Record searched: 1011011100 -> GC744; 0110010011|1010110101 with
S/L|long|slab|column -> no mixed alternative-L collar theorem. GC606/607,
corrected GC609, GC622/623/625/626 and GC706 supply the prior return facts.

Registered before execution (GPT, 2026-10-10):
P1: all complete cones of the three cylinder types have the four-column
profiles below and return to 1110. Alternative L returns with fifth bit1.
P2: ordinary L has both a following S entrance and a following ordinary L
entrance, while retaining the same collar. Thus GC744's following-L premise
is unnecessary for this four-column conclusion.
Counterfactual: the common first two tracks determine the third/fourth tracks.
Unexpected check: 111000000 still emits a visible L but misses hidden1110;
exclude a terminal unsynchronized L from the collar theorem.
Independent controls: shrinking literal cones versus packed cones, with six
columns retained at the closing time. No SAT, width sweep or cut extraction.
OUTCOME: P1/P2 HELD. 1,280 complete cylinder cones and128 terminal
countercontrols pass both engines. Ordinary L can also return outside the
two simple cylinders; that outcome is retained, not called an L1 entrance.
The common first two L tracks do not determine their third/fourth tracks.
"""

from itertools import product


TYPES = {
    "S": ("11101", 6, ("110100", "101100", "100001", "001111")),
    "L0": ("111001", 10,
           ("1101000100", "1011011100", "1010110001", "0110101111")),
    "L1": ("111000001", 10,
           ("1101000100", "1011011100", "1010110101", "0110010011")),
}
INTERFACE = {
    "S": {0: 1, 1: 1},
    "L0": {0: 0, 3: 1, 5: 0},
    "L1": {0: 0, 3: 0, 4: 0, 6: 0, 7: 0},
}


def literal(row, duration):
    rows = [tuple(row)]
    for t in range(duration):
        old = rows[-1]
        rows.append(tuple(((t & 1) if j == 0 else old[j - 1])
                          ^ (old[j] | old[j + 1])
                          for j in range(len(old) - 1)))
    return rows


def packed(row, duration):
    value = sum(bit << j for j, bit in enumerate(row))
    width = len(row)
    rows = [tuple((value >> j) & 1 for j in range(width))]
    for t in range(duration):
        width -= 1
        value = (((value << 1) | (t & 1)) ^ (value | (value >> 1))) \
            & ((1 << width) - 1)
        rows.append(tuple((value >> j) & 1 for j in range(width)))
    return rows


def all_rows(prefix, duration):
    start = tuple(map(int, prefix))
    # The cone for site6 at the closing time has exactly duration+6 inputs.
    for suffix in product((0, 1), repeat=duration + 6 - len(start)):
        row = start + suffix
        a, b = literal(row, duration), packed(row, duration)
        assert a == b
        yield row, a


def main():
    count = 0
    following = {}
    for name, (prefix, duration, profiles) in TYPES.items():
        modes = set()
        third, fourth = profiles[2], profiles[3] + "0"
        assert {t: int(fourth[t + 1]) ^ int(third[t])
                for t in range(duration) if fourth[t] == "0"} == INTERFACE[name]
        assert all(int(fourth[t + 1]) == (1 ^ int(third[t]))
                   for t in range(duration) if fourth[t] == "1")
        for _, rows in all_rows(prefix, duration):
            got = tuple("".join(str(rows[t][j]) for t in range(duration))
                        for j in range(4))
            assert got == profiles, (name, got)
            assert all(rows[t][4] == bit for t, bit in INTERFACE[name].items())
            end = rows[-1]
            assert end[:4] == (1, 1, 1, 0)
            if name == "L1":
                assert end[4] == 1
            if end[4] == 1:
                modes.add("S")
            elif end[5] == 1:
                modes.add("L0")
            else:
                modes.add("other")
            count += 1
        following[name] = sorted(modes)
    assert {"S", "L0"}.issubset(following["L0"])
    assert following["S"] == ["L0", "S"]
    assert following["L1"] == ["S"]
    negative = 0
    for _, rows in all_rows("111000000", 10):
        assert tuple(rows[t][0] for t in range(0, 11, 2)) == (1, 0, 0, 0, 0, 1)
        assert rows[-1][:4] != (1, 1, 1, 0)
        negative += 1
    assert TYPES["L0"][2][:2] == TYPES["L1"][2][:2]
    assert TYPES["L0"][2][2][7] != TYPES["L1"][2][2][7]
    print({"cylinder_cones": count, "terminal_countercontrols": negative,
           "following": following, "P1": "HELD", "P2": "HELD",
           "literal_packed": "PASS"})


if __name__ == "__main__":
    main()
