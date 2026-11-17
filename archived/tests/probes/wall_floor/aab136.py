#!/usr/bin/env python3
"""aab136.py (Local, L1532): the AAB lock at its smallest width: windows, moves, and the state sets up each window."""
import json
from reachlib import *
from clos import nxt
W153=[l.strip() for l in open('leaves3.txt') if len(l.strip())==153][0]
w=136
s=W153[153-w:]
x=sum(1<<i for i,c in enumerate(s) if c=='#')
g={}; st=[x]
while st:
    v=st.pop()
    if v in g: continue
    g[v]=[nxt(v,w,q) for q in STATES]; st+=g[v]
S=sorted(g)
print('closed set',len(S),'at width',w)
for i,v in enumerate(S):
    print(i,show(v,w),let(v,w),'->',sorted({S.index(u) for u in g[v]}),[S.index(u) for u in g[v]])
def merge(v,n):
    T=set(STATES); out=''
    for i in range(n):
        c=(v>>i)&1
        T={(c^(p1|p2),p1) for p1,p2 in T}
        out+=str(len(T))
    return out
for i,v in enumerate(S): print(i,merge(v,w))
json.dump([show(v,w) for v in S],open('lock136.json','w'))
