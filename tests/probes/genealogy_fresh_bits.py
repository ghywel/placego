#!/usr/bin/env python3
"""GC2354: exact finite cylinders, not a random simulation.
64 six-bit left words; fixed right111000...; two episodes; hard stop32 updates.
Predictions and scope in genealogy report section11.
"""
from collections import defaultdict
from itertools import product


def step(row):
    return {j for j in range(min(row)-1,max(row)+2)
            if (30 >> (4*int(j-1 in row)+2*int(j in row)+int(j+1 in row))) & 1}


def move(row,b):
    nxt=step(row)
    return nxt,max(j for j in nxt if j<=b+1)


groups=defaultdict(list)
for word in product(range(2),repeat=6):
    row={0,1,2}|{-j-1 for j,v in enumerate(word) if v}
    b=t=0
    ls=[]
    for k in range(2):
        q=min(j for j in row if j>b)
        r=(q-b-1)//2
        assert t+r+1<=32, 'fixed time cap'
        for _ in range(r):
            row,nb=move(row,b)
            assert nb==b+1
            b,t=nb,t+1
        a=b
        while a-1 in row:
            a-=1
        length=b-a+1
        row,nb=move(row,b)
        assert nb==a
        b,t=nb,t+1
        ls.append(length)
        assert b-t==-sum(ls)
    groups[tuple(ls)].append(word)

assert all(key[0]==1 for key,ws in groups.items() for w in ws if w[0]==0)

for l1,l2 in product(range(1,4),repeat=2):
    s=l1+l2
    ws=groups[l1,l2]
    assert len(ws)==2**(6-s), (l1,l2,len(ws))
    prefixes={w[:s] for w in ws}
    assert len(prefixes)==1
    assert {w[s:] for w in ws}==set(product(range(2),repeat=6-s))
    print(f'L=({l1},{l2}), count={len(ws)}, consumed prefix={"".join(map(str,next(iter(prefixes))))}')
print('PASS: nine cylinder counts and unique consumed prefixes; 64 finite left words; frontier identity at both resets')
