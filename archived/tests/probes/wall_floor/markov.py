#!/usr/bin/env python3
"""markov.py (Local, L1532): the cloud as a chain, each of the four lower states with weight 1/4. Stationary letter statistics, and the rate at which AAB breaks: the leading eigenvalue of the chain killed on leaving A,A,B.
Compares with the measured rate on real rows, about 1.04e-4 a tick."""
import sys
import numpy as np
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
    nodes=[i for i in range(len(V)) if part[i]==cloud]
    idx={v:k for k,v in enumerate(nodes)}
    n=len(nodes)
    A=np.array([[idx[j] for j in adj[i]] for i in nodes])
    let=np.array([0 if ((V[i]>>(w-11))&2047)==WA else 1 for i in nodes])
    # stationary: power iteration
    pi=np.ones(n)/n
    for it in range(4000):
        q=np.zeros(n)
        for s in range(4): np.add.at(q,A[:,s],pi/4)
        d=np.abs(q-pi).sum(); pi=q
        if d<1e-13: break
    PB=pi[let==1].sum()
    # P(next letter B | A)
    pa=0.0
    for s in range(4):
        m=(let==0)&(let[A[:,s]]==1)
        pa+=pi[m].sum()/4
    # killed chain on A,A,B: required letters by phase
    mu=pi*(let==1); mu/=mu.sum()
    req=[0,0,1]
    lam=[]
    for t in range(3*600):
        q=np.zeros(n)
        for s in range(4): np.add.at(q,A[:,s],mu/4)
        q=q*(let==req[t%3])
        tot=q.sum()
        lam.append(tot); mu=q/tot
    l3=np.prod(lam[-3:])
    rate=(1-l3)/3
    print(f'w {w}: cloud {n}, stationary P(B) {PB:.4f}, P(B|A) {pa/pi[let==0].sum():.4f}, AAB killed rate per tick {rate:.3e}, mean stay {1/rate if rate>0 else 0:.0f} ticks (iterations {it})',flush=True)
