#!/usr/bin/env python3
"""edgegraph.py (Local, L1538): the graph on E(w) keeping only edges realized by actual rows. Strongly connected parts, and how the classes change."""
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
from clos import sccs
w=int(sys.argv[1]); f=sys.argv[2]; keepcapped=len(sys.argv)>3
V=[];part=[];term=[]
for l in open(f'E{w}.txt'):
    h,p,t,c,a,b,cc,d=l.split()
    V.append(int(h,16)); part.append(int(p)); term.append(int(t))
n=len(V)
size=defaultdict(int)
for p in part: size[p]+=1
tp=sorted({part[i] for i in range(n) if term[i]},key=lambda p:-size[p])
cloud=tp[0]
g={i:[] for i in range(n)}
nreal=0
for l in open(f):
    i,j,r,b=map(int,l.split())
    if r==1 or (keepcapped and r==-1):
        g[i].append(j); nreal+=1
comps=sccs(g)
cid={}
for k,c in enumerate(comps):
    for v in c: cid[v]=k
cyc=[c for c in comps if len(c)>1 or c[0] in g[c[0]]]
term2=[c for k,c in enumerate(comps) if all(cid[u]==k for v in c for u in g[v]) ]
sinks=[c for c in term2 if (len(c)>1 or c[0] in g[c[0]])]
nosucc=sum(1 for v in g if not g[v])
nopred=n-len({u for v in g for u in g[v]})
print(f'w {w}, edges kept {nreal}: windows {n}, parts {len(comps)}, cyclic parts {len(cyc)}, sizes {sorted((len(c) for c in cyc),reverse=True)[:14]}')
print(f'  closed cyclic parts {sorted((len(c) for c in sinks),reverse=True)[:10]}; windows with no real successor {nosucc}, with no real predecessor {nopred}')
big=max(cyc,key=len)
print('  largest cyclic part: size',len(big),'of which in the free cloud',sum(1 for v in big if part[v]==cloud),'; free cloud size',size[cloud])
