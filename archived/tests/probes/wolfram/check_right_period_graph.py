#!/usr/bin/env python3
"""GC2013: independent retained-certificate check and exact branch distribution.

No constructor import and no new graph search. Read the frozen P=32 certificate,
check all cyclic truth-table equations, closure, ancestry, and a decreasing rank
off the known rain component. Derive a longest-path witness and exact fair-bit
exit distribution. Fixed input digest; no period extension or random sampling.
"""
import collections
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import sys

EXPECTED = '1bf71d6668171fb26af75d329b15ff7226a8166e2a100584369f82d0337f1327'
TRUTH = (0, 1, 1, 1, 1, 0, 0, 0)


def main():
    raw = Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    cert = json.loads(raw)
    assert cert['period_cap'] == 32
    pairs = cert['nodes']
    edges = cert['edges']
    n = len(pairs)
    assert len(set(map(tuple, pairs))) == n
    assert pairs[0] == [0, 2**32 - 1]
    words = [[[(a >> t) & 1 for t in range(32)], [(b >> t) & 1 for t in range(32)]]
             for a, b in pairs]
    exit_set = set(map(tuple, cert['exits']))
    periods = []
    checks = 0
    for i, (aa, bb) in enumerate(words):
        periods.append(next(q for q in (1, 2, 4, 8, 16, 32)
                            if all(bb[t] == bb[(t + q) % 32] for t in range(32))))
        choices = {}
        for target in edges[i]:
            assert 0 <= target < n
            a, c = words[target]
            assert a == bb
            assert c[0] not in choices
            choices[c[0]] = target
            for t in range(32):
                assert c[(t + 1) % 32] == TRUTH[4 * c[t] + 2 * bb[t] + aa[t]]
                checks += 1
        for initial in (0, 1):
            value = initial
            for a, b in zip(aa, bb):
                value = TRUTH[4 * value + 2 * b + a]
            if value == initial:
                assert initial in choices and (i, initial) not in exit_set
            else:
                assert initial not in choices and (i, initial) in exit_set
        if i:
            parent, initial = cert['parents'][i]
            assert 0 <= parent < i and i in edges[parent]
            assert words[i][1][0] == initial
    assert exit_set == {(i, initial) for i in range(n) for initial in (0, 1)
                        if not any(words[j][1][0] == initial for j in edges[i])}
    drops = [(i, j) for i in range(n) for j in edges[i] if periods[j] < periods[i]]
    assert not drops

    # No SCC algorithm: explicitly remove the two known alternating feeder states,
    # then topologically rank every other vertex and check every edge.
    rain = {i for i, (a, b) in enumerate(words)
            if all(a[t] != a[(t + 1) % 32] and b[t] != b[(t + 1) % 32]
                   and a[t] != b[t] for t in range(32))}
    assert len(rain) == 2
    assert all(sum(j in rain for j in edges[i]) == 1 for i in rain)
    outside = set(range(n)) - rain
    reverse = [[] for _ in pairs]
    remaining = {i: 0 for i in outside}
    for i in outside:
        for j in edges[i]:
            if j in outside:
                remaining[i] += 1
                reverse[j].append(i)
    queue = collections.deque(i for i in outside if remaining[i] == 0)
    rank, successor = {}, {}
    while queue:
        i = queue.popleft()
        children = [j for j in edges[i] if j in outside]
        best = max(children, key=lambda j: rank[j], default=None)
        rank[i] = 1 + (rank[best] if best is not None else 0)
        successor[i] = best
        for parent in reverse[i]:
            remaining[parent] -= 1
            if remaining[parent] == 0:
                queue.append(parent)
    assert set(rank) == outside, 'an additional cycle exists'
    assert all(rank[j] < rank[i] for i in outside for j in edges[i] if j in outside)
    high = {i for i in outside if periods[i] > 2}
    assert not any(j in rain for i in high for j in edges[i])
    assert max(rank[i] for i in high) == 14

    starts = [i for i in high if periods[i] == 4]
    assert len(starts) == 4
    mass = {i: Fraction(1, len(starts)) for i in starts}
    exits_by_offset = collections.defaultdict(Fraction)
    for offset in range(15):
        following = collections.defaultdict(Fraction)
        for i, weight in mass.items():
            for bit in (0, 1):
                if (i, bit) in exit_set:
                    exits_by_offset[offset + 1] += weight / 2
                else:
                    target = next(j for j in edges[i] if words[j][1][0] == bit)
                    following[target] += weight / 2
        mass = dict(following)
    assert not mass and sum(exits_by_offset.values()) == 1

    i = max(starts, key=lambda j: rank[j])
    tail = []
    while i is not None:
        tail.append(i)
        i = successor[i]
    i = tail[0]
    access = []
    while i:
        access.append(i)
        i = cert['parents'][i][0]
    access.reverse()
    path = access + tail[1:]
    bits = [1] + [words[i][1][0] for i in path]
    seed = sum(b << d for d, b in enumerate(bits))
    # Independent evolution of this finite seed in the moving-edge frame,
    # via a literal spatial truth table on d=-2..len(bits)+1 with white exterior.
    trace = [[] for _ in range(len(bits) + 1)]
    row = bits + [0] * 140
    for t in range(128):
        for d in range(len(trace)):
            trace[d].append(row[d])
        row = [TRUTH[4 * row[d] + 2 * (row[d - 1] if d >= 1 else 0)
                     + (row[d - 2] if d >= 2 else 0)] for d in range(len(row))]
    for d, i in enumerate(path, 1):
        assert all(trace[d][t] == words[i][1][t % 32] for t in range(128))
    assert all(trace[0])
    next_period = next(q for q in (1, 2, 4, 8, 16, 32, 64, 128)
                       if all(trace[-1][t] == trace[-1][(t + q) % 128] for t in range(128)))
    assert next_period == 64

    out = Path(os.environ['CAPPED_OUT'])
    result = {'input_sha256': EXPECTED, 'verified_states': n,
              'verified_transition_cells': checks, 'rain_states': sorted(rain),
              'ranked_nonrain_states': len(rank), 'max_after_first_period4': 14,
              'exit_offset_from_first_period4_distribution': {str(k): str(v) for k, v in sorted(exits_by_offset.items())},
              'expected_offset': str(sum(k*v for k, v in exits_by_offset.items())),
              'witness_seed_integer': seed, 'witness_right_to_left_bits': ''.join(map(str, bits)),
              'witness_periods': [1] + [periods[i] for i in path],
              'next_diagonal_period': next_period,
              'witness_literal_cell_checks': 128 * len(trace)}
    (out/'verified.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    (out/'rank.json').write_text(json.dumps(rank, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
