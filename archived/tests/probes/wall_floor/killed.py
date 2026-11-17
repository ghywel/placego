#!/usr/bin/env python3
"""killed.py (Local, L1532): inside the cloud, the windows from which the letters can stay A,A,B for ever. Is that set closed under some choices only, how large is it, does it hold a closed part?"""
import sys
from collections import defaultdict
WA=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1))); WB=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
for w in [int(a) for a in sys.argv[1:]]:
    V=[];part=[];term=[];adj=[]
    for l in open(f'E{w}.txt'):
        h,p,t,c,a,b,cc,d=l.split()
        V.append(int(h,16)); part.append(int(p)); term.append(int(t)); adj.append((int(a),int(b),int(cc),int(d)))
    size=defaultdict(int)
    for p in part: size[p]+=1
    cloud=max({part[i] for i in range(len(V)) if term[i]},key=lambda p:size[p])
    let=[ (V[i]>>(w-11))&2047==WB for i in range(len(V))]
    nodes=[i for i in range(len(V)) if part[i]==cloud]
    # nodes with phase: phase 0 = A after B, 1 = A after A, 2 = B
    S={(i,ph) for i in nodes for ph in ((2,) if let[i] else (0,1))}
    while True:
        rem=[]
        for (i,ph) in S:
            nxt=(ph+1)%3
            if not any((j,nxt) in S for j in adj[i]): rem.append((i,ph))
        if not rem: break
        S.difference_update(rem)
    # how many lower states keep the phase, on average
    full=sum(1 for (i,ph) in S if all((j,(ph+1)%3) in S for j in adj[i]))
    print(f'w {w}: cloud {len(nodes)}, windows that can hold AAB for ever {len({i for i,_ in S})}, of which every lower state holds {full}',flush=True)
