#!/usr/bin/env python3
"""sat_edges.py (Local, L1538): every edge of the free graph at width W, tested by SAT on actual rows: a row y_0 with top W cells u, y_1 = F(y_0) with top W cells v, and letters on y_1 .. y_L. One formula, one incremental solver, the edge given as assumptions. Writes i j verdict (1 real, 0 dead, -1 unknown). Usage: W L BUDGET OUT"""
import sys,time
from pysat.solvers import Glucose4
W=int(sys.argv[1]); L=int(sys.argv[2]); budget=int(sys.argv[3]); out=sys.argv[4]
V=[];adj=[]
for l in open(f'E{W}.txt'):
    h,p,t,c,a,b,cc,d=l.split()
    V.append(int(h,16)); adj.append((int(a),int(b),int(cc),int(d)))
K0=max(11+5*L-1,W+5)
var={};n=[0]
def x(s,k):
    if (s,k) not in var:
        n[0]+=1;var[(s,k)]=n[0]
    return var[(s,k)]
S=Glucose4(incr=True)
for s in range(1,L+1):
    for k in range(0,K0-5*s+1):
        r=x(s,k);a=x(s-1,k+3);b=x(s-1,k+4);c=x(s-1,k+5)
        for ra in (0,1):
          for aa in (0,1):
            for bb in (0,1):
              for cc in (0,1):
                if ra!=(aa^(bb|cc)):
                    S.add_clause([(-r if ra else r),(-a if aa else a),(-b if bb else b),(-c if cc else c)])
FIX=[1,1,0,0,0,1,1,1]
for s in range(0,L+1):
    for k in range(8): S.add_clause([x(s,k) if FIX[k] else -x(s,k)])
    S.add_clause([x(s,8),x(s,9)]); S.add_clause([-x(s,8),-x(s,9)]); S.add_clause([-x(s,10)])
def cell(v,k): return (v>>(W-1-k))&1
f=open(out,'w'); cnt={1:0,0:0,-1:0}; t0=time.time()
for i in range(len(V)):
    for j in sorted(set(adj[i])):
        asm=[(x(0,k) if cell(V[j],k) else -x(0,k)) for k in range(W)]+[(x(1,k) if cell(V[i],k) else -x(1,k)) for k in range(W)]
        S.conf_budget(budget)
        r=S.solve_limited(assumptions=asm)
        code=1 if r is True else 0 if r is False else -1
        cnt[code]+=1; f.write(f'{i} {j} {code} 0\n')
    if i%100==0: f.flush()
f.close()
print(f'W {W} L {L}: real {cnt[1]} dead {cnt[0]} unknown {cnt[-1]} time {time.time()-t0:.0f}s',flush=True)
