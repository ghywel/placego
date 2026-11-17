#!/usr/bin/env python3
"""GC514 controls registered before execution in CLOUD-LOCAL.
All 341 resonant initial patches (-5..5), five ticks only.
Predict capped duration min(m+d,6); independent literal/XOR rules.
CF right-tail dependence fails. Unexpected m=5 survival check.
OUTCOME: all 341 patches and 31 right-tail groups PASS; CF REFUTED.
Cap 6 means survival through tick 5, not an exact first-black time.
No selected-orbit growth estimate or horizon extension.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_white_certificate.py
"""
from collections import Counter, defaultdict
from rule30_gpt_front_selection import step


def main():
    groups = defaultdict(set)
    counts = Counter()
    for seed in range(2048):
        initial = {i - 5 for i in range(11) if seed >> i & 1}
        if 0 in initial:
            continue
        p = min((-i for i in initial if i < 0), default=99)
        q = min((i for i in initial if i > 0), default=99)
        if p != q or p > 5:
            continue
        m = p
        rows = [initial]
        other = set(initial)
        for _ in range(5):
            rows.append(step(rows[-1], False))
            other = step(other, True)
            assert rows[-1] == other
        at_arrival = rows[m - 1]
        assert -1 in at_arrival and 1 in at_arrival
        assert all(0 not in row for row in rows[:m + 1])
        # Only depths whose first failure is inside the five-tick cone.
        d = next((k for k in range(1, 6 - m)
                  if int(-1 - k in at_arrival) != (1 - k % 2)), None)
        predicted = m + d if d is not None else 6
        observed = next((t for t, row in enumerate(rows) if 0 in row), 6)
        assert observed == predicted
        left = tuple(int(i in initial) for i in range(-5, 0))
        groups[(left, m)].add(observed)
        counts[m] += 1
        if m == 5:
            assert observed == 6
    assert counts == {1:256, 2:64, 3:16, 4:4, 5:1}
    assert all(len(values) == 1 for values in groups.values())
    print('Endpoint and independent rules PASS:', dict(sorted(counts.items())))
    print('Right-tail groups PASS:', len(groups), '; CF REFUTED')
    print('Unexpected m=5 survival PASS; 341 patches; ALL CHECKS PASS')


if __name__ == '__main__':
    main()
