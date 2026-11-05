#!/usr/bin/env python3
"""break_at.py (Local, L1534): at one cell narrower than a closed set, a shortest path of lower states to a letter off the cycle. Usage: JSON WIDTH"""
import json,sys
from collections import deque
from reachlib import *
from clos import nxt
d=json.load(open(sys.argv[1])); w=int(sys.argv[2])
for ph in sorted(d,key=int)[:6]:
    s=d[ph][0][len(d[ph][0])-w:]
    x=sum(1<<k for k,c in enumerate(s) if c=='#')
    seq=[];y=x
    for t in range(3):
        seq.append(let(y,w)); y=nxt(y,w,(1,1))
    q=deque([(x,0,0)]); seen={(x,0)}; found=None; n=0
    while q and n<300000 and found is None:
        v,p,dep=q.popleft(); n+=1
        for st in STATES:
            u=nxt(v,w,st); e=(p+1)%3
            if let(u,w)!=seq[e]: found=dep+1; break
            if (u,e) not in seen: seen.add((u,e)); q.append((u,e,dep+1))
    print('phase',ph,'letters',''.join(seq),'leaves after',found,'ticks; windows searched',n,flush=True)
    break
