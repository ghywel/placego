#!/usr/bin/env python3
"""GC511 fixed three-tick exposure controls, registered before execution.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_front_exposure.py
EX0 independent literal and XOR rules on 8192 patches (-6..6).
EX1 conditional fresh groups balance before and after gap reveals.
EX2 pathwise exposure accounting and finite-time expectation bounds.
CF reused groups all fair must fail; unexpected GC506 histories checked.
OUTCOME: all 8192 patches and 24576 prefixes PASS; 800 pre-gap and
1312 post-gap fresh groups balance. Reused-fairness CF REFUTED.
No longer horizon, speed fit or asymptotic inference.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from rule30_gpt_front_selection import step


def main():
    groups = [defaultdict(Counter), defaultdict(Counter)]
    reused = defaultdict(Counter)
    histories = defaultdict(Counter)
    sums = [Counter() for _ in range(3)]
    for seed in range(8192):
        initial = {i - 6 for i in range(13) if seed >> i & 1}
        x, y = set(initial), initial ^ {0}
        a, b = set(x), set(y)
        fronts = [0]
        exposed = set()
        fresh_count = fresh_left = tie_left = 0
        for t in range(3):
            lower = min(exposed, default=0)
            j = fronts[-1] - 1 - t
            z = j - lower
            fresh = j < lower
            x, y = step(x, False), step(y, False)
            a, b = step(a, True), step(b, True)
            assert (x, y) == (a, b)
            next_front = min(x ^ y)
            delta = next_front - fronts[-1]
            left = delta == -1
            assert delta >= -1
            if fresh:
                for mode, start in enumerate((lower, j + 1)):
                    bits = tuple(int(i in initial) for i in range(start, 7))
                    key = (t, tuple(fronts), lower, j, bits)
                    groups[mode][key][left] += 1
            else:
                bits = tuple(int(i in initial) for i in range(lower, 7))
                reused[(t, tuple(fronts), lower, j, bits)][left] += 1
            if t == 2 and fronts[-1] == 0:
                histories[(fronts[1], fresh)][left] += 1
            fresh_count += fresh
            fresh_left += fresh and left
            tie_left += z == 0 and left
            exposed.update(range(j, lower))
            next_lower = min(exposed, default=0)
            next_z = next_front - 1 - (t + 1) - next_lower
            assert next_z == max(z, 0) + delta - 1
            assert len(exposed) == fresh_count + fresh_left + tie_left - (next_z == -2)
            assert next_front == t + 2 - len(exposed) + next_z
            assert next_front >= -fresh_left
            sums[t].update(F=fresh_count, A=fresh_left, L=next_front)
            fronts.append(next_front)
    for mode, table in enumerate(groups):
        assert all(c[True] == c[False] for c in table.values())
        print('EX1 mode', mode, 'balanced groups', len(table))
    assert any(c[True] != c[False] for c in reused.values())
    assert set(k for k in histories if k[0] == -1) == {(-1, False)}
    assert set(k for k in histories if k[0] == 0) == {(0, True)}
    for key, expected in (((-1, False), Fraction(1)), ((0, True), Fraction(1, 2))):
        counts = histories[key]
        assert Fraction(counts[True], sum(counts.values())) == expected
    for n, totals in enumerate(sums, 1):
        assert 2 * totals['A'] == totals['F']
        assert 2 * totals['L'] >= -n * 8192
        print('EX2 N', n, 'mean L', Fraction(totals['L'], 8192),
              'mean F', Fraction(totals['F'], 8192))
    print('EX0 PASS: 8192 patches, three ticks, independent rules')
    print('EX2 PASS: 24576 prefixes; CF reused fairness REFUTED')
    print('Unexpected GC506 exposure histories PASS; ALL CHECKS PASS')


if __name__ == '__main__':
    main()
