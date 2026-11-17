#!/usr/bin/env python3
"""Block 8 (Local): write the data part of Rule30SidewaysLocks.lean from locks.json (lock_data.py). Usage: gen_locks_lean.py LOCKS_JSON OUT"""
import json, sys
d = json.load(open(sys.argv[1]))
out = []
def lst(xs, ind='  '):
    lines, cur = [], ind
    for i, x in enumerate(xs):
        s = str(x) + (', ' if i + 1 < len(xs) else '')
        if len(cur) + len(s) > 110: lines.append(cur.rstrip()); cur = ind
        cur += s
    lines.append(cur.rstrip()); return '\n'.join(lines)
for name, label in (('lock5', 'lock5'), ('lock7', 'lock7'), ('lock7b', 'lock7b')):
    L = d[name]
    out.append('/-- The windows of `%s`, as codes in %d classes (bit `i` is column `i + 1`). -/' % (label, L['p']))
    out.append('def %sCodes : List (List Nat) := [' % label)
    out.append(',\n'.join('  [' + lst(c, '   ').strip() + ']' for c in L['classes']))
    out.append(']')
    out.append('')
open(sys.argv[2], 'w').write('\n'.join(out))
print('ok')
