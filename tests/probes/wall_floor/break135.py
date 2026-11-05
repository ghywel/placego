#!/usr/bin/env python3
"""break135.py (Local, L1533): at width 135 the lock's windows do not close: a shortest path of lower states from each phase to a letter off the cycle."""
import json
from collections import deque
from reachlib import *
from clos import nxt
S=json.load(open('lock136.json'))
w=135
for name,i in (('phase A, next A',5),('phase A, next B',3),('phase B',1)):
    s=S[i][1:]
    x=sum(1<<k for k,c in enumerate(s) if c=='#')
    seq=[]; y=x
    for t in range(3):
        seq.append(let(y,w)); y=nxt(y,w,(0,0))
    q=deque([(x,0,())]); seen={(x,0)}; found=None; n=0
    while q and n<400000:
        v,ph,path=q.popleft(); n+=1
        for si,st in enumerate(STATES):
            u=nxt(v,w,st); e=(ph+1)%3
            if let(u,w)!=seq[e]:
                found=path+(si,); break
            if (u,e) not in seen:
                seen.add((u,e)); q.append((u,e,path+(si,)))
        if found: break
    print(name,'letters',''.join(seq),'break after',len(found) if found else None,'ticks; searched',n,'; lower states',found[:60] if found else None)
