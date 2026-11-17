#!/usr/bin/env python3
"""gate131.py (Local, L1552): the rise rule around column 131 of the third lock's strip. For each (phase, D) the allowed rises, whether an exception is open, and the strip cells that decide it; then which nodes feed phase 4 and 5 past column 131."""
rows=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
P=6;N=175
x=lambda p,k: rows[p][k]=='#'
def options(p,D):
    if not x(p,D-1): return [5],False
    if not x(p,D):
        if not x(p,D+1): return [4],False
        return [3],True
    if x(p,D+1) or x(p,D+2): return [4,3],False
    return [4],True
for p in range(6):
    print('phase',p,'cells 124..146:',rows[p][124:147])
print()
print('(p,D): rises; ! exception open')
for p in (3,4,5,0,1,2):
    print(p,' '.join(f'{D}:{"/".join(map(str,options(p,D)[0]))}{"!" if options(p,D)[1] else ""}' for D in range(126,150)))
print()
print('what feeds each node forward: (p,D) goes to (p-1,D-r)')
for p in (4,5):
    print('into phase',p,'past column 131:',[(D,[D-r for r in options(p,D)[0]]) for D in range(132,150)])
print('exception nodes in phases 3,4,5 between 120 and 150:')
for p in (3,4,5):
    print(p,[D for D in range(120,150) if options(p,D)[1]])
