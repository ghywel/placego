#!/usr/bin/env python3
"""GC2217: fixed boundary controls for GC2216; not a population census.

Bit 0 represents depth 1; depth 0 is clamped white at EVERY update.
One literal forward table on inputs 0..7 supplies all finite parents of
the eight named outputs, since a nonzero row's last depth grows by one.
An independently written inverse recurrence and substring scanner agree.
"""
import hashlib
import json
from pathlib import Path
import time

START = time.monotonic()
TARGETS = (0, 1, 3, 5, 6, 7, 13, 15)
EXPECTED = {0: [0], 1: [], 3: [1], 5: [], 6: [3], 7: [2], 13: [5, 6], 15: []}
RULE = (0, 1, 1, 1, 1, 0, 0, 0)


def literal_forward(x):
    # Physical left parent is farther from the wall; use the rule table.
    row = [0] + [(x >> j) & 1 for j in range(3)] + [0, 0]
    out = [RULE[4 * row[k + 1] + 2 * row[k] + row[k - 1]] for k in range(1, 5)]
    assert RULE[4 * 0 + 2 * row[5] + row[4]] == 0
    return sum(v << j for j, v in enumerate(out))


def inverse(y, b):
    q = [0, b]
    # At depth 5 output is zero forever; check the exact zero-tail pair 4,5.
    for k in range(1, 8):
        q.append(((y >> (k - 1)) & 1) ^ (q[k] | q[k - 1]))
    finite = q[4:6] == [0, 0]
    assert q[7:9] == ([0, 0] if finite else [1, 1])
    parent = sum(v << j for j, v in enumerate(q[1:])) if finite else None
    return finite, parent, q


def reset_factors(y):
    row = [0] + [(y >> j) & 1 for j in range(4)] + [0]
    return [(i, j - i - 1) for i in range(len(row)) for j in range(i + 2, len(row))
            if row[i] == row[j] == 0 and (j - i - 1) % 3 == 1
            and all(row[k] == 1 for k in range(i + 1, j))]


forward = {x: literal_forward(x) for x in range(8)}
assert forward == {0: 0, 1: 3, 2: 7, 3: 6, 4: 14, 5: 13, 6: 13, 7: 12}
cases = []
for y in TARGETS:
    direct = sorted(x for x, out in forward.items() if out == y)
    backwards = [inverse(y, b) for b in (0, 1)]
    recovered = sorted(parent for finite, parent, _ in backwards if finite)
    resets = reset_factors(y)
    assert direct == recovered == EXPECTED[y], (y, direct, recovered)
    assert (len(direct) == 1) == (not resets)
    cases.append({'output': y, 'finite_parents': direct, 'reset_factors': resets,
                  'inverse_prefixes_including_wall': [q for _, _, q in backwards]})
assert [forward[x] for x in (1, 3, 6)] == [3, 6, 13]
assert [len(EXPECTED[y]) for y in (3, 6, 13)] == [1, 1, 2]
assert EXPECTED[1] == EXPECTED[5] == []
assert time.monotonic() - START < 10, 'internal wall stop'
print(json.dumps({'status': 'PASS', 'scope': 'eight named outputs only; universal hand claim separate',
                  'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'P1_parent_counts': [len(EXPECTED[y]) for y in TARGETS],
                  'P2_exact_tree13': True, 'zero_row_guard': True,
                  'literal_forward': forward, 'cases': cases,
                  'elapsed_seconds': time.monotonic() - START}, indent=2))
