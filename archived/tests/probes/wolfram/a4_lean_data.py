#!/usr/bin/env python3
"""L1423 (Local, 2026-11-03): emit the Lean data block for A4 from a4_closure_export.py's JSON.
Run: python3 tests/probes/wolfram/a4_lean_data.py DATA.json OUT.lean
orbRows: row tau of the ring orbit as a 9-bit number (bit j = orb[tau][j]); closure: (key, psi) with
key = (tq * 9 + dq) * 2^24 + strip, strip bit i = cell A + 1 + i.
"""
import json
import sys

d = json.load(open(sys.argv[1]))
assert d['r'] == 0 and d['s'] == 0 and d['N'] == 9 and d['q'] == 57 and d['W'] == 24
rows = [sum(b << j for j, b in enumerate(row)) for row in d['orb']]
keys = []
for (tq, dq, strip), psi in zip(d['states'], d['lo']):
    m = sum(b << i for i, b in enumerate(strip))
    keys.append(((tq * 9 + dq) * (1 << 24) + m, psi))
lines = ['/-- The ring orbit of `100100000`: row `τ` as a 9-bit number, bit `j` the cell at diagonal index `j`. -/',
         'def orbRows : List Nat := [' + ', '.join(map(str, rows)) + ']', '',
         '/-- The closure: `(key, ψ)` with `key = (tq * 9 + dq) * 2 ^ 24 + strip`. -/',
         'def closure : List (Nat × Int) := [']
for k, (key, psi) in enumerate(keys):
    lines.append('  (%d, %d)%s' % (key, psi, ',' if k < len(keys) - 1 else ']'))
open(sys.argv[2], 'w').write('\n'.join(lines) + '\n')
print('rows', len(rows), 'states', len(keys), 'start key', keys[0][0], 'psi range', min(p for _, p in keys), max(p for _, p in keys))
