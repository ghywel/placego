#!/usr/bin/env python3
"""sat_break.py (Local, L1538): can a row whose letters broke S ticks ago enter the third lock now? Rows y_1 .. y_S read the lock's letters, y_(S+1) reads the other letter, and the past stays settled to L. Usage: LOCKFILE W S L INDEX SECONDS."""
import sys,json,time
from sat_past import *
f=sys.argv[1]; W=int(sys.argv[2]); Sb=int(sys.argv[3]); L=int(sys.argv[4]); idx=int(sys.argv[5]); secs=int(sys.argv[6])
S=[l.strip() for l in open(f) if l.strip()]
T=sorted({s[len(s)-W:] for s in S})
v=T[idx]
# the letters of the past by the forward rule on the window
y=[1 if v[W-1-k]=='#' else 0 for k in range(W)]
lets=[]
cur=y
while len(cur)>=11:
    lets.append(cur[9]); 
    if len(cur)<16: break
    cur=[cur[k+3]^(cur[k+4]|cur[k+5]) for k in range(len(cur)-5)]
per=None
for p in (2,3,6):
    if all(lets[i]==lets[i+p] for i in range(len(lets)-p)): per=p;break
exp=lambda s:lets[s%per]
nv,cl,var,K0=build(v,W,L,T,False)
def x(s,k): return var[(s,k)]
for s in range(0,Sb+1):
    cl.append([x(s,9) if exp(s) else -x(s,9)])
cl.append([-x(Sb+1,9) if exp(Sb+1) else x(Sb+1,9)])
st,model,el=solve(nv,cl,secs)
print(f'S {Sb} L {L} window {idx}: {st} in {el:.1f}s',flush=True)
if st=='SATISFIABLE':
    word=''.join('A' if var[(s,8)] in model else 'B' for s in range(L,-1,-1))
    print('  letters oldest first',word)
    y0=[1 if var[(0,k)] in model else 0 for k in range(K0+1)]
    json.dump({'S':Sb,'L':L,'idx':idx,'W':W,'y0_by_offset':y0,'letters':word},open(f'witness_break_{W}_{Sb}.json','w'))
