#!/usr/bin/env python3
"""edge_replay.py (Local, L1553): every law of Rule30ErrorEdge on two actual configurations, by plain ticks: a single black cell against the same row with a second black cell D places to its right (the low wheels of the seed include permanently white ones, which hold an edge for ever). Prints the heals by jump, for the notebook's gate."""
import collections,sys
n=int(sys.argv[1]) if len(sys.argv)>1 else 3000
D=int(sys.argv[2]) if len(sys.argv)>2 else 500
w=2*n+D+61; c=n+10          # 0-based centre
def run(init):
    x=0
    for p in init: x|=1<<p
    rows=[x]
    M=(1<<w)-1
    for t in range(n):
        # position p: new(p) = old(p-1) xor (old(p) or old(p+1))
        x=((x<<1)^(x|(x>>1)))&M
        rows.append(x)
    return rows
a=run([c]); b=run([c,c+D])
wheel=lambda r,j,t:(r[t]>>(c-t+j))&1
edge=[0]*(n+1)
e=0
for t in range(n+1):
    while wheel(a,e,t)==wheel(b,e,t): e+=1
    edge[t]=e
bad=collections.Counter(); jumps=collections.Counter()
for t in range(n-1):
    m=edge[t]; m1=edge[t+1]
    assert m1>=m
    par=wheel(a,m-1,t) if m>=1 else None
    if m>=1:
        if (m1>m)!=(par==1): bad['heal_iff']+=1
    if m1>m:
        d=m1-m; jumps[d]+=1
        p1=wheel(a,m1-1,t+1); p2=wheel(a,m1-1,t+2)
        if m>=2 and t+2<=n:
            if d==2 and p1!=0: bad['jump_two']+=1
            if d==3 and p1!=1: bad['jump_three']+=1
            if d==4 and p2!=1: bad['jump_four']+=1
            if d==5 and p1==0 and p2!=1: bad['jump_five']+=1
            if d in (6,7) and p1==0 and p2!=0: bad['jump_six_seven']+=1
print('ticks',n,'final edge',edge[n],'heals',sum(jumps.values()),'jumps',sorted(jumps.items()),'violations',dict(bad))
