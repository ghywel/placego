#!/usr/bin/env python3
"""Lock family, step 3 (Local): the LOCKED components of Block 3's xx cores (GC2696 evidence), by width and period.
Usage: locked_table.py SCC_JSONL. Reads stage CORE rows. A component's period is its gcd (one edge = two ticks), its
word is column 1 around the cycle. Prints, per width, every LOCKED component: period, word, nodes, closed flag,
leaks, and the lock-7/lock-7b cut windows it contains; then the period-7 components alone across widths."""
import json, sys
L = [json.loads(l) for l in open(sys.argv[1])]
core = [r for r in L if r['stage'] == 'CORE']
Ws = sorted({r['W'] for r in core})
rot7 = {'0101000'[k:] + '0101000'[:k] for k in range(7)}
for W in Ws:
    rows = [r for r in core if r['W'] == W and r['kind'] == 'LOCKED']
    per = {}
    for r in rows: per[r['gcd']] = per.get(r['gcd'], 0) + 1
    print('W %2d: LOCKED %2d, by period %s' % (W, len(rows), dict(sorted(per.items()))))
print()
print('period-7 LOCKED components (gcd 7):')
for W in Ws:
    for r in core:
        if r['W'] == W and r['kind'] == 'LOCKED' and r['gcd'] == 7:
            print('  W %2d rank %2d word %s %s nodes %6d closed %d leak_core %d leak_out %d l7cut %d l7bcut %d sevencut %d' % (
                W, r['rank'], r['word'], '(lock-7 word)' if r['word'] in rot7 else '', r['nodes'], r['closed'],
                r['leak_core'], r['leak_out'], r['l7cut'], r['l7bcut'], r['sevencut']))
