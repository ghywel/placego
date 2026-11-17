#!/usr/bin/env python3
"""Block 3: write targets.txt, the small fixed inputs of the window lift, from their sources.

Usage: make_targets.py KIT_DIR BN13_DIR R02_DIR SEVENLOCK_LEAN OUT
Sources, with sha-256 digests written into the header of OUT:
  kit  Rule30Certificates/GateTrap.lean  trapCodes (829 windows of 16 columns)
  kit  Rule30Ether.lean                  etherTable by hand below, wallStates (109 pairs of phase and 13-bit strip)
  BN-13 lock7.txt (66 windows, 30 columns), lock7_w45.txt (33 windows, 45 columns), lock5.txt (34 columns)
  rule30-open PeriodTwo/SevenLock.lean   lockCls (195 windows, 32 columns, seven classes), read as text, not built
Bit i of a window is column i + 1, at an odd tick. The run needs only OUT.
"""
import hashlib, re, sys

kit, bn13, r02, lean, out = sys.argv[1:6]
def read(p): return open(p, encoding='utf-8').read()
gate_p = kit + '/lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean'
ether_p = kit + '/lean/Ruliology/CellularAutomata/Rule30Ether.lean'
srcs = [gate_p, ether_p, bn13 + '/lock7.txt', bn13 + '/lock7_w45.txt', bn13 + '/lock5.txt', lean]
gate = read(gate_p)
trap = sorted(int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', gate, re.S).group(1)))
assert len(trap) == 829
eth = read(ether_p)
i, j = eth.index('def wallStates'), eth.index('def wallOK')
wall = []
for m in re.finditer(r'\((\d), \[([a-z, ]+)\]\)', eth[i:j]):
    b = [x.strip() == 'true' for x in m.group(2).split(',')]
    assert len(b) == 13
    wall.append((int(m.group(1)), sum(1 << n for n, x in enumerate(b) if x)))
wall = sorted(set(wall))
assert len(wall) == 109, len(wall)
ints = lambda p: sorted(int(x) for x in read(p).split())
l7, l7b, l5 = ints(bn13 + '/lock7.txt'), ints(bn13 + '/lock7_w45.txt'), ints(bn13 + '/lock5.txt')
src = read(lean)
body = src[src.index('def lockCls'):src.index('def lockCheck')]
cls = [[int(x) for x in re.findall(r'\d+', m)] for m in re.findall(r'\[([\d,\s]+)\]', body)]
assert [len(c) for c in cls] == [22, 22, 24, 34, 37, 32, 24], [len(c) for c in cls]
with open(out, 'w') as f:
    f.write('# Block 3 fixed inputs. Bit i of a window is column i + 1 at an odd tick.\n')
    for p in srcs:
        f.write('# sha256 %s %s\n' % (hashlib.sha256(open(p, 'rb').read()).hexdigest(), '/'.join(p.split('/')[-2:])))
    f.write('trap %d %s\n' % (len(trap), ' '.join(map(str, trap))))
    f.write('wall %d %s\n' % (len(wall), ' '.join('%d %d' % w for w in wall)))
    f.write('lock7 30 %d %s\n' % (len(l7), ' '.join(map(str, l7))))
    f.write('lock7b 45 %d %s\n' % (len(l7b), ' '.join(map(str, l7b))))
    f.write('lock5 34 %d %s\n' % (len(l5), ' '.join(map(str, l5))))
    flat = sorted(x for c in cls for x in c)
    f.write('sevenlock 32 %d %s\n' % (len(flat), ' '.join(map(str, flat))))
print('trap', len(trap), 'wall', len(wall), 'lock7', len(l7), 'lock7b', len(l7b), 'lock5', len(l5), 'sevenlock', sum(map(len, cls)))
