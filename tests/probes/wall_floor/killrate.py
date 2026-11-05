#!/usr/bin/env python3
"""killrate.py (Local, L1532): the rate at which AAB breaks on the cloud chain, each lower state with weight 1/4, at wide windows. Starts from uniform on the B windows of the cloud; 900 ticks."""
import sys
import numpy as np
from collections import defaultdict
WAv=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1))); WBv=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
for w in [int(a) for a in sys.argv[2:]]:
    V=[];part=[];term=[];adj=[]
    for l in open(f'E{w}.txt'):
        h,p,t,c,a,b,cc,d=l.split()
        V.append(int(h,16)); part.append(int(p)); term.append(int(t)); adj.append((int(a),int(b),int(cc),int(d)))
    n0=len(V)
    part=np.array(part); term=np.array(term); adj=np.array(adj)
    sizes=np.bincount(part)
    cloud=max(set(part[term==1].tolist()),key=lambda p:sizes[p])
    keep=np.nonzero(part==cloud)[0]
    idx=-np.ones(n0,dtype=np.int64); idx[keep]=np.arange(len(keep))
    A=idx[adj[keep]]
    let=np.array([1 if ((V[i]>>(w-11))&2047)==WBv else 0 for i in keep])
    n=len(keep)
    mu=(let==1).astype(float); mu/=mu.sum()
    req=[0,0,1]; lam=[]
    for t in range(int(sys.argv[1])):
        q=np.zeros(n)
        for s in range(4): q+=np.bincount(A[:,s],weights=mu/4,minlength=n)
        q=q*(let==req[t%3]); tot=q.sum(); lam.append(tot); mu=q/tot
    l3=np.prod(lam[-3:]); print(f'w {w}: cloud {n}, AAB break rate on the chain {(1-l3)/3:.3e} a tick',flush=True)
