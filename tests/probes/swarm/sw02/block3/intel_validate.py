#!/usr/bin/env python3
"""Fail-closed acceptance of the frozen smoke/main controls, before a verdict."""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]); smoke = sys.argv[2] == 'smoke'
previous = Path(sys.argv[3]) if len(sys.argv) > 3 else root
def located(relative):
    p = root / relative
    return p if p.is_file() else previous / relative
def text(name):
    p = located(name + '.stdout')
    assert p.is_file() and p.stat().st_size, ('missing output', name)
    s = p.read_text()
    assert 'DISAGREE' not in s and 'DIFFERENT' not in s and 'FAIL ' not in s, name
    return s

s = text('base22')
assert re.search(r'basin 7617642 .*outside 4965270 sweeps 39\b', s), 'external W22 baseline'
for name in ('checkxx', 'checkpq', 'tails'):
    assert text(name).rstrip().endswith('PASS'), name
rows = text('rows')
assert re.search(r'ROWS B \d+ none 0 by tick 4400', rows), 'unassigned real rows'
if not smoke:
    for cls, n in [('gate', 4057307), ('family', 107736), ('lock7', 29260), ('lock7b', 1)]:
        assert re.search(r'ROWS B 22 ' + cls + r' ' + str(n) + r' latest tick ', rows), cls
    assert re.search(r'W 31 core 688649\b', text('r02'))
    assert re.search(r'PROJ W 31 w16=1259\b', text('r02'))
    gate = re.search(r'ROWS B 22 gate \d+ latest tick (\d+)', rows)
    assert int(gate[1]) <= 4189
for mode in ('xx', 'pq'):
    s = text(mode)
    expected_bad7b = 0 if mode == 'xx' else 2
    assert re.search(r'closure failures: lock-7 set 0, lock-7b set ' + str(expected_bad7b) + r'\b', s), mode

def unresolved(path):
    result = {}
    for line in path.read_text().splitlines():
        r = json.loads(line)
        if r['stage'] == 'CORE':
            result.setdefault(r['W'], [])
            if r['kind'] == 'UNRESOLVED':
                # Parent ranks differ after harmless parents are omitted.
                result[r['W']].append(tuple(r[k] for k in ('nodes', 'edges', 'gcd', 'gaps', 'first', 'black')))
    return {w: sorted(v) for w, v in result.items()}
a = unresolved(located('xx/scc_xx.jsonl'))
b = unresolved(located('xxp/scc_xx_pruned.jsonl'))
shared = sorted(a.keys() & b.keys())
assert shared, 'missing full/pruned overlap'
for w in shared:
    assert a[w] == b[w], ('full/pruned discrepancy', w)
for name in ('base', 'r02', 'rows', 'xx', 'xxp', 'pq', 'checkxx', 'checkpq', 'tails', 'reentry'):
    r = json.loads(located(name + '.receipt.json').read_text())
    if name == 'xxp' and previous != root:
        assert r['returncode'] == -24 and 500 <= r['cpu_s'] <= 505, r
        completed = max(map(int, re.findall(r'^W (\d+) analysed ', text('xxp'), re.M)))
        assert completed >= 40
        b = {w: rows for w, rows in b.items() if w <= completed}
    else:
        assert r['returncode'] == 0 and r['reason'] == 'EXIT', name
print(json.dumps({'controls': 'PASS', 'phase': 'smoke' if smoke else 'main', 'pruned_overlap': shared,
                  'independent_replay_through': {'xx': 22 if smoke else 36, 'pq': 20 if smoke else 32},
                  'unresolved_at_max_xx': a[max(a)], 'unresolved_at_max_pruned': b[max(b)],
                  'partial_pruned_extraction': previous != root}, sort_keys=True))
