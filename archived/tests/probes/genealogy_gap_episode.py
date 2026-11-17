#!/usr/bin/env python3
"""GC2353: fixed local checks of gap episodes, prediction in genealogy report section9.
All ten-bit finite rows and marked black prefixes, no orbit horizon or random sampling.
"""
from itertools import product


def step(row):
    return {j for j in range(min(row)-1,max(row)+2)
            if (30 >> (4*int(j-1 in row)+2*int(j in row)+int(j+1 in row))) & 1}


def advance(row,b):
    nxt=step(row)
    return nxt,max(j for j in nxt if j<=b+1)


def run_length(row,b):
    a=b
    while a-1 in row:
        a-=1
    return b-a+1


episodes=nonadvances=0
for word in product(range(2),repeat=10):
    row={i for i,v in enumerate(word) if v}
    for p in sorted(row):
        nxt,nb=advance(row,p)
        if p+1 in row or p+2 in row:
            assert nb==p-run_length(row,p)+1
            nonadvances+=1
        later=[j for j in row if j>p]
        if not later:
            continue
        q=min(later)
        m=q-p-1
        r=m//2
        z=int(p-1 in row)
        cur,b=row,p
        for s in range(r+1):
            assert b==p+s and b in cur and q-s in cur
            assert not (cur & set(range(b+1,q-s)))
            assert int(b-1 in cur)==(z^(s%2))
            if s<r:
                cur,b=advance(cur,b)
        nxt,nb=advance(cur,b)
        assert nb<=b
        assert (nb==b)==((z^(r%2))==0)
        episodes+=1

for a in (0,1):
    # Sites -4..2: 0001101 or 0101101, initial prefix boundary at coordinate0.
    word=(0,a,0,1,1,0,1)
    row={j-4 for j,v in enumerate(word) if v}
    b=0
    path=[b]
    for _ in range(3):
        row,b=advance(row,b)
        path.append(b)
    assert path==([0,-1,0,0] if a==0 else [0,-1,0,-1])
    print('witness', ''.join(map(str,word)), 'front', path)

print(f'PASS: {episodes} exact gap episodes and {nonadvances} nonadvance run formulas in 1024 rows')
