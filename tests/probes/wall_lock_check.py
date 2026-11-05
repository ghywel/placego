#!/usr/bin/env python3
"""The 45-cell AB lock on literal rows, and the search for a lock of AAB."""
import random,sys,json
from wall_locklib import *
random.seed(3)
rows=None
while rows is None:
    low=40
    x=1|(random.getrandbits(low-1)<<1); b=(x>>(low-1))&1
    for j in range(low,W):
        b^=1
        if b: x|=1<<j
    y=x; seq=''
    for t in range(700):
        d=top(y); seq+=letter(window(y,11,d)); y=inv(y)
    if seq[-200:] in ('AB'*100,'BA'*100):
        rows=[]
        for t in range(40):
            rows.append(y); y=inv(y)
w=45
wins=set(window(r,w) for r in rows); g=closure(wins,w)
S=sorted(g)
print('width 45, closed set of',len(S))
for v in S: print(' ',''.join('#' if b else '.' for b in v),letter(v),'->',[S.index(n) for n in sorted(g[v])])
json.dump([[int(b) for b in v] for v in S],open('lock45.json','w'))
# literal rows: random cells below, 400 backward ticks
fails=0; ticks=0
for v in S:
    for rep in range(60):
        lowlen=random.randint(3,60)
        x=1|(random.getrandbits(lowlen-1)<<1)
        for i,b in enumerate(v):
            if b: x|=1<<(lowlen+i)
        bb=v[-1]
        for j in range(lowlen+w,W):
            bb^=1
            if bb: x|=1<<j
        d=top(x); assert d==lowlen+w-2
        L0=letter(window(x,11,d)); y=x; prev=L0
        for t in range(300):
            z=inv(y); dz=top(z); ticks+=1
            lz=letter(window(z,11,dz))
            if dz!=d+3 or lz==prev or lz=='?' or window(z,45,dz) not in g: fails+=1; break
            d=dz; prev=lz; y=z
print('literal rows: backward ticks',ticks,'failures',fails)
