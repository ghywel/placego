#!/usr/bin/env python3
"""rule30_cloud_badB_lift.py: does any ACTUAL non-LL white-A origin reach an unguarded B after k SS blocks? (CL346.) The
width-20 relaxation layers from the 29 actual tick-16 images of white-A origins, restricted backward to the rows that
can still reach a bad B at tick 26 + 6k, prune a depth-first search over the origin cells; every constraint (the
13-cell image at 16, the site-5 track H then SS^k, the allowed 20-cell row at every tick from 16) is applied the
moment its light cone closes; the first solution exits, so a found origin is an all-tail certificate (its first 20
cells at the end tick depend on the 64 origin cells only).

RUN-ON:     cpu (Python 3 standard library plus numpy; under a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_badB_lift.py

PREDICTION (written before the run): a real origin exists for k = 3 (0.4); counterfactual: none, so the relaxation's 13
bad-B terminals are free-boundary artefacts. RESULT (CL346): FOUND for k = 3 after 413,951 nodes: the origin
1110100011011010010010000100100000000000000000000000000000000000 (sites 14..25 = 010010010000, outside GC1136's gate,
six-bit high word 010010) gives 11100111111101001100 at 16, 11101110111100111001 at 26, 11101111011111000101 at 32,
11101011001110011111 at 38 and the unguarded B 11101001100101110101 at 44, for every farther tail; exactly one of the 29
actual image rows and one tick-26 row lie on a bad-B path. For k = 4..8 the exact-depth layers from the actual sources
reach no bad B.
"""
import sys, time, itertools
import numpy as np
B=lambda s: tuple(int(c) for c in s)
H=B('0101101010'); SS=B('111010'); WA=B('1110100011011'); IMG=B('1110011111110'); BADB=B('111010011001')
W=20
def imgs(row,t):
    out=set()
    for b in (0,1):
        s=(t%2,)+tuple(row)+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out
# the 29 actual image rows at tick 16
NB=23; N=1<<NB; idx=np.arange(N,dtype=np.int64)
cells=[np.full(N,b,dtype=np.uint8) for b in WA]+[((idx>>k)&1).astype(np.uint8) for k in range(NB)]
for t in range(16):
    wall=np.full(N,t%2,dtype=np.uint8)
    cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
w20=np.zeros(N,dtype=np.int64)
for i in range(20): w20|=cells[i].astype(np.int64)<<i
rows={tuple((int(v)>>i)&1 for i in range(20)) for v in set(w20.tolist())}
SRC=[r for r in rows if r[:13]==IMG]; assert len(SRC)==29
def layers(k):
    TR=H+SS*k; TEND=26+6*k
    L={16:set(SRC)}
    for t in range(16,TEND):
        nxt=set()
        for r in L[t]:
            if r[4]!=TR[t-16]: continue
            nxt|=imgs(r,t)
        L[t+1]=nxt
    good={TEND:{r for r in L[TEND] if r[:12]==BADB}}
    for t in range(TEND-1,15,-1):
        good[t]={r for r in L[t] if r[4]==TR[t-16] and (imgs(r,t)&good[t+1])}
    return TR,TEND,good
def search(k,cap=50_000_000):
    TR,TEND,good=layers(k)
    if not good[TEND]: return None,0,0,0,False,{t:len(good[t]) for t in (16,26,TEND)}
    DMAX=TEND+20
    want={(5,16+j):bit for j,bit in enumerate(TR)}
    for i in range(1,14): want[(i,16)]=IMG[i-1]
    nodes=[0]; d36=[0]; found=[]
    def rec(cells,d):
        nodes[0]+=1
        if nodes[0]>cap: return True
        if d==36: d36[0]+=1
        if d==DMAX: found.append(tuple(cells[0])); return True
        for b in (0,1):
            new=[row[:] for row in cells]; new[0].append(b); ok=True; nd=d+1
            for t in range(1,min(nd,TEND+1)):
                i=nd-t; prev=new[t-1]; left=prev[i-2] if i>=2 else ((t-1)%2); v=left^(prev[i-1]|prev[i])
                if len(new)<=t: new.append([])
                new[t].append(v); w=want.get((i,t))
                if w is not None and w!=v: ok=False; break
                if i==20 and t>=16 and tuple(new[t][:20]) not in good[t]: ok=False; break
            if ok and rec(new,nd): return True
        return False
    init=[list(WA)]
    for t in range(1,13):
        prev=init[-1]; init.append([(prev[i-2] if i>=2 else ((t-1)%2))^(prev[i-1]|prev[i]) for i in range(1,13-t+1)])
    t0=time.time(); rec(init,13)
    return found,nodes[0],d36[0],time.time()-t0,nodes[0]>cap,{t:len(good[t]) for t in (16,26,TEND)}
for k in (3,4,5,6,7,8):
    found,n,d36,dt,capped,sizes=search(k)
    if found is None: print('k =',k,': the relaxation itself reaches no bad B at tick',26+6*k,
        '| allowed layer sizes',sizes,flush=True); continue
    status='LIFT FOUND' if found else ('UNKNOWN at the cap' if capped else 'no actual origin')
    print('k =',k,'SS blocks, bad B at tick',26+6*k,'|',status,'| nodes',n,'| 36-cell origins visited',d36,
        '| allowed rows at 16/26/end',sizes,'| %.0fs'%dt,flush=True)
    if found:
        o=found[0]; print('   origin',''.join(map(str,o)),'| sites 14..25',''.join(map(str,o[13:25])),flush=True)
    if capped: break
