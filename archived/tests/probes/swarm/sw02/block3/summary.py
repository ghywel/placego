#!/usr/bin/env python3
"""Block 3: gather a run folder into one page. Usage: summary.py OUT_DIR"""
import json, os, re, sys
out = sys.argv[1]
def read(p):
    return open(p, errors='replace').read() if os.path.exists(p) else ''
print('# Block 3 summary\n')
print(read(out + '/steps.log'))
print('## Controls')
for w in (19, 20, 21, 22):
    print(''.join(l + '\n' for l in read('%s/base/base%d.log' % (out, w)).splitlines() if l.startswith('DENSE')), end='')
rows = read(out + '/rows/rows.log')
print(''.join(l + '\n' for l in rows.splitlines() if l.startswith('ROW')), end='')
r02 = read(out + '/r02/r02.log')
print(''.join(l + '\n' for l in r02.splitlines() if re.match(r'(W (16|20|24|28|31) core| PROJ W (16|20|24|28|31) )', l)), end='')
for n in ('checkxx', 'checkpq'):
    d = 'xx' if n == 'checkxx' else 'pq'
    print(n, (read('%s/%s/%s.log' % (out, d, n)).strip().splitlines() or ['no log'])[-2:])
print('tails', (read(out + '/xx/tails.log').strip().splitlines() or ['no log'])[-2:])
print('\n## Components by width')
for folder, name in (('xx', 'scc_xx.jsonl'), ('xxp', 'scc_xx_pruned.jsonl'), ('pq', 'scc_pq.jsonl')):
    p = '%s/%s/%s' % (out, folder, name)
    if not os.path.exists(p): continue
    print('\n###', folder)
    R = [json.loads(l) for l in open(p)]
    for W in sorted(set(r['W'] for r in R)):
        c = [r for r in R if r['W'] == W and r['stage'] == 'CORE']
        un = [(r['nodes'], r['gaps'], 'parent %d' % r['parent']) for r in c if r['kind'] == 'UNRESOLVED']
        e = [(r['nodes'], r['kind'], r['gcd'], r['gaps']) for r in c if r['ether']]
        cl = [(r['nodes'], r['word'][:24]) for r in c if r['closed']]
        print('W', W, 'components', len(c), 'kinds', {k: sum(r['kind'] == k for r in c) for k in ('LOCKED', 'GAP35', 'UNRESOLVED')}, 'unresolved', un, 'ether', e, 'closed', cl)
print('\n## Gap words, counts by length 1..16, and projections')
for folder in ('xx', 'xxp', 'pq'):
    for l in read('%s/%s/%s.log' % (out, folder, folder)).splitlines():
        if l.startswith((' GAPWORDS', ' PROJ', 'W ', 'STOP', 'DONE')) and 'analysed' not in l: print(folder, l)
print('\n## Re-entry\n' + read(out + '/rows/reentry.log'))
