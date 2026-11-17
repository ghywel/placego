#!/usr/bin/env python3
"""entrances.py (Local, L1534): the windows outside a closed set that step into it, and how far back such chains go. Forward rule gives the top w-5 cells of a predecessor; its five low cells are tried."""
import sys,json
from reachlib import *
from clos import nxt
d=json.load(open(sys.argv[1])); 
S=[]
for p in d: S+=d[p]
w=len(S[0])
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
L={nat(s) for s in S}
def preds(v):
    # v: bit i = cell i low..high; offset k = w-1-i
    y=lambda k:(v>>(w-1-k))&1
    top=0
    for k in range(0,w-5):
        c=y(k+3)^(y(k+4)|y(k+5))
        top|=c<<(w-1-k)
    out=set()
    for low in range(32):
        u=top|low
        if let(u,w)=='?': continue
        for s in STATES:
            if nxt(u,w,s)==v: out.add(u); break
    return out
level=set(L); seen=set(L); 
print('closed set',len(L))
for dep in range(1,int(sys.argv[2])+1):
    new=set()
    for v in level:
        for u in preds(v):
            if u not in seen: new.add(u)
    seen|=new
    print('depth',dep,'new windows',len(new),flush=True)
    if not new: break
    level=new
    if len(new)>200000: break
