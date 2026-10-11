#!/usr/bin/env python3
"""rule30_cloud_gc1146_check.py: Cloud's second read of GPT's GC1146 (CL345): the two-time boundary contradiction on EVERY
width-20 H path from each named source to its macro endpoint, and a complete bit-sliced enumeration of all 2^28 real
exteriors (cells 21..48 at tick 0) asking which reach the four macro rows of each named 28-tick path with the site-5
track at every tick.

RUN-ON:     cpu (Python 3 standard library plus numpy; about a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1146_check.py

PREDICTIONS (written before the run): (a) the contradiction holds on every H path (0.6); (b) no real exterior realises
a 28-tick path from either source through its four macro states (0.7). RESULT (CL345): (a) refuted, 2 of 4 paths pass
for GC1143's source and 3 of 15 for GC1145's; (b) held for GC1143 (every exterior dies at the tick-22 macro state) and
refuted for GC1145 (933,888 exteriors reach the unguarded B at tick 28).
"""
import itertools, sys, time
import numpy as np
B=lambda s: tuple(int(c) for c in s)
W=20; H=B('0101101010'); SS=B('111010'); TRACK=H+SS*3
def imgs(row,t):
    out=set()
    for b in (0,1):
        s=(t%2,)+tuple(row)+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out
def paths(src,target,track,t0):
    res=[]
    def rec(path,t):
        if len(path)==len(track)+1:
            if path[-1]==target: res.append(list(path))
            return
        r=path[-1]
        if r[4]!=track[len(path)-1]: return
        for s in imgs(r,t): rec(path+[s],t+1)
    rec([src],t0); return res
def domains(path): return [{b for b in (0,1) if y[-1]==x[-2]^(x[-1]|b)} for x,y in zip(path,path[1:])]
def compatible(path):
    allowed=domains(path); live=allowed[0]; counts=[len(live)]
    for t in range(len(allowed)-1):
        live={bb for b in live for bb in allowed[t+1] if b==0 or bb==1-path[t][19]}
        counts.append(len(live))
        if not live: return False,t+1,counts
    return True,None,counts
CASES=(('GC1143','11100111100001111110',('11101110111100111000','11101111011111000000','11101011001110010000',
    '11101001100101011000')),
       ('GC1145','11100111111101001000',('11101110111100111001','11101111011111000100','11101011001110011100',
           '11101001100101110000')))
ONES=np.uint64(0xFFFFFFFFFFFFFFFF)
def pc(m): return int(np.bitwise_count(m).sum())
def real_counts(src,cps,T=28,nfree=28):
    """bit-sliced over all 2^nfree assignments of cells 21..20+nfree (chunked over the top two bits): survivors of the
    site-5 track at every tick and of each checkpoint row, cumulatively"""
    NB=nfree-2; N=1<<NB; M=N//64; idx=np.arange(M,dtype=np.uint64)
    tot={k:0 for k in sorted(cps)}; tot['track only']=0
    for hi in range(4):
        cells=[np.full(M,ONES if b else 0,dtype=np.uint64) for b in src]
        for k in range(NB):
            if k<6: cells.append(np.tile(np.array([ (1 if (j>>k)&1 else 0) for j in range(64)],dtype=np.uint64),
                1).__class__ and np.frombuffer(np.packbits([(j>>k)&1 for j in range(64)][::-1]).tobytes(),dtype='>u8').astype(np.uint64).repeat(M))
            else: cells.append(np.where(((idx>>np.uint64(k-6))&np.uint64(1)).astype(bool),ONES,np.uint64(0)))
        cells.append(np.full(M,ONES if hi&1 else 0,dtype=np.uint64)); cells.append(np.full(M,
            ONES if hi&2 else 0,dtype=np.uint64))
        alive=np.full(M,ONES,dtype=np.uint64)
        for t in range(T+1):
            if t<T: alive&= cells[4] if TRACK[t] else ~cells[4]
            if t in cps:
                m=alive.copy()
                for i,b in enumerate(cps[t]): m&= cells[i] if b else ~cells[i]
                alive=m; tot[t]+=pc(alive)
            if t==T: break
            wall=np.full(M,ONES if t%2 else 0,dtype=np.uint64)
            cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
    return tot
# sanity of the bit layout: the 64 bits of a word carry cells 21..26, the word index cells 27..46, the chunk cells 47, 48
t0=time.time()
for name,source,mac in CASES:
    src=B(source); macs=[B(m) for m in mac]
    hp=paths(src,macs[0],H,0)
    pairs=set(); fails=0; ff=set()
    for p in hp:
        pairs.add(tuple(r[18:20] for r in p[3:6])); ok,t,c=compatible(p)
        if not ok: fails+=1; ff.add(t)
    print(name,'| H paths to the macro endpoint:',len(hp),'| right pairs at ticks 3,4,5:',sorted(pairs),
        '| failing the two-time check:',fails,'of',len(hp),'first failing tick',sorted(ff),flush=True)
    segs=[len(paths(macs[i],macs[i+1],SS,
        10+6*i)) for i in range(3)]; print('    SS paths between macro states:',segs,flush=True)
    cps={10:macs[0],16:macs[1],22:macs[2],28:macs[3]}
    tot=real_counts(src,cps)
    print('    real exteriors (all 2^28 of cells 21..48) with the track at every tick reaching, cumulatively: tick 10',tot[10],'| 16',tot[16],'| 22',tot[22],'| 28 (bad B)',tot[28],'| %.0fs'%(time.time()-t0),flush=True)
