"""Exact bounded-time test on six supplied windows; quantify all physical shallow histories.

At a backward horizon r, invert the r-tick map spatially. Its jth digit is
its initial digit XOR a function of only the preceding 2r digits. Thus all
possible low inputs to the fixed high word are represented at L=2r+1 by
putting a black anchor at 0 and letting bits 1,...,2r range freely.
"""
import hashlib
import json
import os
from pathlib import Path

from rain_six_windows import B11, PATTERNS, encode


def phi(x):
    return x ^ ((x << 1) | (x << 2))


def iterate(x, ticks):
    for _ in range(ticks):
        x = phi(x)
    return x


def invert_window(word, carry, r):
    low = 2*r + 1
    top = low + 9
    end = top + 3*r + 4
    state = 1 | carry << 1
    target = word << low
    for j in range(low + 11, end + 1):
        if ((word >> 10) & 1) ^ ((j - (top+1)) % 2):
            target |= 1 << j
    # Reconstruct the earliest row inside the observation cone, low to high.
    for j in range(low, end + 1):
        if ((iterate(state, r) ^ target) >> j) & 1:
            state |= 1 << j
    mask = (1 << (end + 1)) - 1
    replay = iterate(state, r) & mask
    assert replay >> low == target >> low
    # Verify all intermediate rows independently by single-tick low-to-high inversion.
    v = replay
    for _ in range(r):
        parent = 0
        for j in range(end + 1):
            if ((v ^ (parent << 1 | parent << 2)) >> j) & 1:
                parent |= 1 << j
        v = parent
    assert v == state and v & 1
    expected_top = top + 3*r
    assert all(((state >> i) ^ (state >> (i+1))) & 1 for i in range(expected_top+1, end))
    walls = (~(state ^ (state >> 1))) & ((1 << (expected_top+1))-1)
    actual_top = walls.bit_length()-1
    suffix = (state >> (expected_top - 9)) & 2047
    return (actual_top == expected_top, actual_top == expected_top and suffix in B11,
            dict(carry=carry, L=low, source_low=replay & ((1 << low)-1),
                 top=top, expected=expected_top, actual=actual_top))


def main():
    results = {}
    for pattern in PATTERNS + (".#..#....##",):
        encoded = encode(pattern)
        stats = []
        for r in (1,2,3,4,5):
            failed = []
            outside = 0
            for carry in range(1 << (2*r)):
                speed, inside, witness = invert_window(encoded, carry, r)
                if not speed:
                    failed.append(witness)
                if not inside:
                    outside += 1
            stats.append(dict(ticks=r, cases=1 << (2*r), missed_speed=len(failed),
                              outside_B11=outside, first_failure=failed[0] if failed else None))
        results[pattern] = stats
        print(pattern, [(s["missed_speed"],s["outside_B11"]) for s in stats])
    assert all(s['outside_B11']==0 for s in results[".#..#....##"])
    # Positive control for a physical failure at r=1 (a white upper pair with an alternating tail).
    assert not invert_window(0,0,1)[0]
    data=(json.dumps(results,sort_keys=True,indent=2)+"\n").encode()
    (Path(os.environ['CAPPED_OUT'])/'histories.json').write_bytes(data)
    print(hashlib.sha256(data).hexdigest())


if __name__=="__main__":
    main()
