#!/usr/bin/env python3
"""GC2868: inspect the retained 170-word graph, no solver or new profile census."""
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLAN = json.loads((ROOT/'gpt_return13_cycle_plan.json').read_text())


def partition(successor):
    visited = set()
    loops = []
    for root in sorted(successor):
        path = []
        at = {}
        u = root
        while u not in visited and u not in at:
            at[u] = len(path); path.append(u)
            u = successor[u]
        if u in at:
            loops.append(path[at[u]:])
        visited.update(path)
    return loops, sorted(set(successor)-{v for loop in loops for v in loop})


def moving(x):
    n = len(x)
    return [x[i] ^ (x[(i+1)%n] | x[(i+2)%n]) for i in range(n)]


def physical(x):
    n = len(x)
    return [(30 >> (4*x[(i-1)%n]+2*x[i]+x[(i+1)%n])) & 1 for i in range(n)]


def action(row, p):
    n = len(row)
    a, b = row, row
    for t in range(1, p+1):
        a, b = moving(a), physical(b)
        assert a == [b[(i+t)%n] for i in range(n)], ('FRAME_ORACLE', row, t)
    return a, b


def main():
    assert partition({0:1, 1:2, 2:1}) == ([[1,2]], [0])
    assert action([0], 13)[0] == [0]
    assert action([1], 13)[0] == [0]
    raw = Path(os.environ['RETURN13_PROJECTION_JSON']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PLAN['projection_sha256']
    result = json.loads(raw); target = result['target']
    assert result['status'] == 'COMPLETE' and target['complete'] and target['p'] == 13
    assert target['q'] == 65 and target['cols'] == 65 and target['offset'] == 6 and target['w'] == 16
    words = target['words']; assert len(set(words)) == len(words) == 170
    prefix = defaultdict(list)
    for w in words:
        assert 0 <= w < 2**16
        prefix[w & (2**15-1)].append(w)
    assert all(len(prefix[w >> 1]) == 1 for w in words)
    successor = {w: prefix[w >> 1][0] for w in words}
    loops, transient = partition(successor)
    result = {'physical_cycles': [], 'nonreturning_cycles': [], 'transient_words': transient,
              'projection_sha256': PLAN['projection_sha256'], 'coverage_certified': False}
    for cycle in loops:
        row = [v & 1 for v in cycle]; n = len(row)
        assert [sum(row[(i+j)%n] << j for j in range(16)) for i in range(n)] == cycle
        after, laboratory = action(row, 13)
        entry = {'spatial_period': n, 'row': row, 'words': cycle}
        if after == row:
            entry['one_tick_fixed'] = moving(row) == row
            if n > 1:
                # A one-cell phase error cannot pass on this primitive spatial cycle.
                assert [laboratory[(i+14)%n] for i in range(n)] != row
            result['physical_cycles'].append(entry)
        else:
            entry['first_bad_site'] = next(i for i in range(n) if after[i] != row[i])
            entry['returned_row'] = after
            result['nonreturning_cycles'].append(entry)
    for tag in ['physical_cycles','nonreturning_cycles']:
        result[tag+'_lengths'] = dict(Counter(x['spatial_period'] for x in result[tag]))
        result[tag+'_words'] = sum(x['spatial_period'] for x in result[tag])
    assert len(transient)+result['physical_cycles_words']+result['nonreturning_cycles_words'] == len(words)
    out = Path(os.environ['CAPPED_OUT'])
    (out/'cycle-audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print('RETURN13_CYCLE_AUDIT_RECORDED')
    print(json.dumps({k:v for k,v in result.items() if k not in ('physical_cycles','nonreturning_cycles','transient_words')}))


if __name__ == '__main__':
    main()
