#!/usr/bin/env python3
"""sat_lock6.py (Local, L1538): a witness row: settled past of L rows, stepping into the third lock from outside. Saves the row and verifies it by direct forward and backward ticks."""
import sys,json,time
from sat_past import *
L=int(sys.argv[1]); idx=int(sys.argv[2]); secs=int(sys.argv[3])
S=[l.strip() for l in open('lock175.txt') if l.strip()]
W=175
T=sorted({s[len(s)-W:] for s in S})
nv,cl,var,K0=build(T[idx],W,L,T,True)
st,model,el=solve(nv,cl,secs)
print(f'L {L} window {idx}: vars {nv} clauses {len(cl)}: {st} in {el:.1f}s',flush=True)
if st=='SATISFIABLE':
    y0=[1 if var[(0,k)] in model else 0 for k in range(K0+1)]
    json.dump({'L':L,'idx':idx,'y0_by_offset':y0},open(f'witness6_L{L}.json','w'))
    word=''.join('A' if var[(s,8)] in model else 'B' for s in range(L,-1,-1))
    print('letters oldest first',word)
