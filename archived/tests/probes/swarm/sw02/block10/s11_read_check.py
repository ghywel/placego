#!/usr/bin/env python3
"""Small independent finite-premise replay for HX-2.1 / S-11, GPT GC2803.

Prediction: C9 has 32 states, excludes129 but its low8 projection contains129
at phase16; C13 has64 states and excludes all13 black-ended ether prefixes.
The deepest ether prefix survives12 cells at phase55. Counterfactual: any
mismatch blocks the carrying verdict and the proposed Lean module.
Record searched: GC2802/L1619, full HX-2 and SKM-HX-2-1 reports, current kit
FrozenRuler/RightPeriods/ZeroBoundaryBarriers, outside SeedPastPeriods,
record_find c7cut+seed and known_find ether+seed; exact source hashes in report.

Independent representations: literal eight-entry truth table on whole-line
cells; kit-shaped three-case edge map on tuples; packed polynomial as a third
oracle. No original swarm script is imported or executed. Fixed small bounds.
"""
import json
import resource

RULE = (0, 1, 1, 1, 1, 0, 0, 0)


def rule(a, b, c):
    return RULE[4 * a + 2 * b + c]


def step(row):
    padded = [0, 0] + row + [0, 0]
    return [rule(*padded[i - 1:i + 2]) for i in range(1, len(padded) - 1)]


def bits(value, n):
    return tuple((value >> i) & 1 for i in range(n))


def number(word):
    return sum(b << i for i, b in enumerate(word))


def edge(word):
    return tuple(word[0] if i == 0 else word[1] ^ word[0] if i == 1
                 else word[i] ^ (word[i - 1] | word[i - 2])
                 for i in range(len(word)))


def cycle(n):
    start = bits(1, n)
    word = start
    result = []
    for _ in range(65):
        result.append(number(word))
        word = edge(word)
        if word == start:
            return result
    raise AssertionError("fixed 65-step cycle cap exceeded")


def main():
    c9, c13 = cycle(9), cycle(13)
    assert len(c9) == len(set(c9)) == 32 and 129 not in c9
    assert len(c13) == len(set(c13)) == 64
    assert [i for i, x in enumerate(c9) if x & 255 == 129] == [16]
    assert c9[16] == 385
    # Exhaustive odd-residue permutation and complement-invariance controls.
    odd = list(range(1, 512, 2))
    image = {x: number(edge(bits(x, 9))) for x in odd}
    assert set(image.values()) == set(odd)
    assert all((x in c9) == (image[x] in c9) for x in odd)
    assert all(image[x] == (x ^ ((x << 1) | (x << 2))) & 511 for x in odd)
    # Whole-line oracle, only rows0..204; every right-edge bit matches the map.
    rows = [[1]]
    for _ in range(204):
        rows.append(step(rows[-1]))
    prefixes = [number((r[::-1] + [0] * 13)[:13]) for r in rows]
    assert all(prefixes[t] == c13[t % 64] for t in range(205))
    ring = [int((p + 1) % 7 == 0) for p in range(7)]
    phases = [ring]
    for _ in range(4):
        r = phases[-1]
        phases.append([rule(r[(i - 1) % 7], r[i], r[(i + 1) % 7]) for i in range(7)])
    assert phases[4] == phases[0]
    ether = [(phase, p, tuple(phases[phase][(p - j) % 7] for j in range(13)))
             for phase in range(4) for p in range(7) if phases[phase][p]]
    assert len(ether) == 13
    exits = []
    for phase, p, word in ether:
        assert number(word) not in c13
        first = next(k for k in range(1, 14)
                     if number(word[:k]) not in {x & ((1 << k) - 1) for x in c13})
        exits.append(first)
    assert exits == [9, 9, 6, 3, 9, 9, 3, 3, 9, 9, 6, 13, 3]
    deep = ether[exits.index(13)][2]
    assert prefixes[55] & 4095 == number(deep[:12])
    assert all(len(r) == 2 * t + 1 and r[0] == r[-1] == 1 for t, r in enumerate(rows))
    # Physical c7cut N, finite control only: the universal residue is hand-derived.
    for n in range(4):
        lo, hi = -(7 * n + 1), 7 * n + 6
        row = [int((p + 1) % 7 == 0) for p in range(lo, hi + 1)]
        assert number((row[::-1] + [0] * 9)[:9]) == 129
        for t in range(33):
            value = number((row[::-1] + [0] * 9)[:9])
            assert value not in c9
            assert value & 255 == c9[(16 + t) % 32] & 255
            assert ((value ^ c9[(16 + t) % 32]) >> 8) & 1
            row = step(row)
    # Scope negatives: offset ether words occur, despite the flush exclusion.
    b204 = rows[204][::-1]
    assert tuple(b204[7:20]) == tuple(phases[2][(1 - j) % 7] for j in range(13))
    b80 = rows[80][::-1]
    assert tuple(b80[3:17]) == tuple(phases[1][(4 - j) % 7] for j in range(14))
    # Unexpected control: odd span alone cannot explain exclusion of a cut.
    # Remove only the last black pulse of c7cut1: the remaining span is15,
    # but its flush9 residue is still129 (unlike the original even-span family).
    trim = [int((p + 1) % 7 == 0) for p in range(-8, 7)]
    assert len(trim) == 15 and trim[0] == trim[-1] == 1
    assert number(trim[::-1][:9]) == 129
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(json.dumps({"C9": c9, "C13_count": len(c13), "ether_exits": exits,
                      "exact_depth_phase": [8, 16], "sharp12_phase": 55,
                      "offset_controls": [[204, 7, 13], [80, 3, 14]],
                      "odd_span_control": 15, "cpu_s": usage.ru_utime + usage.ru_stime}))
    print("S11_FINITE_PREMISES_PASS")


if __name__ == "__main__":
    main()
