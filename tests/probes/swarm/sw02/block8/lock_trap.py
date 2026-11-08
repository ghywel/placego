#!/usr/bin/env python3
"""Block 8 (Local): how the locks sit against the kit's gate trap (829 windows of 16 columns) and each other.
Usage: lock_trap.py KIT_DIR BN13_DIR. Bit i of a window is column i + 1 at an odd tick."""
import re, sys
kit, bn = sys.argv[1:3]
src = open(kit + '/lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read()
trap = set(int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1)))
assert len(trap) == 829
def ints(p): return set(int(x) for x in open(bn + '/' + p).read().split())
L5, L7, L7b = ints('lock5.txt'), ints('lock7.txt'), ints('lock7_w45.txt')
m16 = (1 << 16) - 1
for name, S in (('lock5', L5), ('lock7', L7), ('lock7b', L7b)):
    print(name, 'windows', len(S), '16-column projections in the gate trap:', sum((w & m16) in trap for w in S), 'of', len(S))
for k in (16, 20, 25, 30):
    m = (1 << k) - 1
    print('first %d columns: lock7 and lock7b share %d projections; lock5 and lock7 share %d' % (k, len({w & m for w in L7} & {w & m for w in L7b}), len({w & m for w in L5} & {w & m for w in L7})))
