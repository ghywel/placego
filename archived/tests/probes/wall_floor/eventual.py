#!/usr/bin/env python3
"""eventual.py (Local, L1532): E(w), the width-w windows that survive arbitrarily many settled backward ticks: start from E(w-1) extended by one lower cell, and take images under all four lower states until the set stops shrinking. Then its strongly connected parts."""
import sys,time
from reachlib import *
from clos import nxt,sccs
A=WAi; B=WBi
E={A,B}; w=11
wmax=int(sys.argv[1]); 
prev=None
t0=time.time()
while w<wmax:
    w+=1
    S=set()
    for v in E:
        S.add(v<<1); S.add((v<<1)|1)
    # the windows at width w sit with bit 0 the lowest; next() keeps the top w cells
    it=0
    while True:
        it+=1
        N=set()
        for v in S:
            for s in STATES:
                N.add(nxt(v,w,s))
        N&=S
        if len(N)==len(S): break
        S=N
    E=S
    g={v:[nxt(v,w,s) for s in STATES] for v in E}
    comps=sccs(g)
    cid={}
    for i,c in enumerate(comps):
        for v in c: cid[v]=i
    term=[c for i,c in enumerate(comps) if all(cid[u]==i for v in c for u in g[v])]
    cyc=[c for c in comps if len(c)>1 or c[0] in g[c[0]]]
    print(f'w {w}: E {len(E)} iters {it} comps {len(comps)} cyclic {len(cyc)} terminal {len(term)}: sizes {sorted(len(c) for c in term)} cyclic sizes {sorted(len(c) for c in cyc)[-6:]} t={time.time()-t0:.1f}',flush=True)
