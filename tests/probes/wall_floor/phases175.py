#!/usr/bin/env python3
"""phases175.py (Local, L1534): the consensus cells of the third lock by phase, the highest cell the lower states reach, and the moves between windows."""
import json
from reachlib import *
from clos import nxt
d=json.load(open('lock175.json'))
w=175
idx={}
for p in sorted(d,key=int):
    for s in d[p]:
        idx[sum(1<<i for i,c in enumerate(s) if c=='#')]=(int(p),s)
for p in sorted(d,key=int):
    ws=d[p]
    cons=''.join(ws[0][i] if len({x[i] for x in ws})==1 else '?' for i in range(w))
    hi=max(i for i in range(w) if cons[i]=='?')
    print(p,len(ws),'highest reachable offset',w-1-hi,cons)
