#!/usr/bin/env python3
"""lock175.py (Local, L1534): the closed set of the deep period-6 word at its smallest closing width: phases, cells that vary inside a phase, merge sites, reset words."""
import sys,json
from reachlib import *
from clos import nxt,sccs
W=[l.strip() for l in open(sys.argv[1] if len(sys.argv)>1 else 'deep6.txt')][int(sys.argv[3]) if len(sys.argv)>3 else 0]
w=int(sys.argv[2]) if len(sys.argv)>2 else 175
s=W[len(W)-w:]
x=sum(1<<i for i,c in enumerate(s) if c=='#')
g={}; st=[x]
while st:
    v=st.pop()
    if v in g: continue
    g[v]=[nxt(v,w,q) for q in STATES]; st+=g[v]
print('closure',len(g),'SCCs',sorted(len(c) for c in sccs(g)))
# phase by BFS mod P
P=None
for cand in (12,9,8,6,4,3,2):
    ph={x:0}; q=[x]; ok=True
    while q and ok:
        v=q.pop()
        for u in g[v]:
            e=(ph[v]+1)%cand
            if u in ph:
                if ph[u]!=e: ok=False;break
            else: ph[u]=e;q.append(u)
    if ok: P=cand;break
print('phase period',P)
by={}
for v,p in ph.items(): by.setdefault(p,[]).append(v)
def merge(v,n):
    T=set(STATES); 
    for i in range(n):
        c=(v>>i)&1
        T={(c^(p1|p2),p1) for p1,p2 in T}
        if len(T)==1: return i
    return None
def isF(c): return c[0]==0 and c[1]!=c[2] and c[3]==1 and c[5]==1 and c[6]==0 and c[8]==0 and c[9]==1
for p in sorted(by):
    vs=by[p]
    bits=[[ (v>>i)&1 for i in range(w)] for v in vs]
    vary=[i for i in range(w) if len({b[i] for b in bits})>1]
    letters={let(v,w) for v in vs}
    merges=sorted({merge(v,w) for v in vs})
    fs=[sorted(i for i in range(w-12) if isF(b[i:i+10])) for b in bits]
    common=sorted(set(fs[0]).intersection(*fs))
    print(f'phase {p}: {len(vs)} windows, letters {letters}, cells that vary {len(vary)}: lowest {vary[:3]} highest {vary[-3:]} (offset of highest {w-1-vary[-1] if vary else None}), merge index {merges}, reset words at index in all windows {common}')
json.dump({str(p):[show(v,w) for v in vs] for p,vs in by.items()},open(f'lock{w}.json','w'))
print('out degrees',sorted({len(set(e)) for e in g.values()}))
