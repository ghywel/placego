#!/usr/bin/env python3
"""rule30_cloud_witness_fate.py: what the CL346 witness does after its unguarded B at tick 44 (registered in CL346).

RUN-ON:     cpu (Python 3 standard library plus numpy; about a minute at LOG2N = 24)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_witness_fate.py 24

WHAT. The 64-cell origin 1110100011011010010010000100100000000000000000000000000000000000 (a white-A origin of the 676
class whose first 20 cells run high 111 at 16, a black-marker S at 26, SS at 32 and 38 and the unguarded B
11101001100101110101 at 44 for every tail) with 2^LOG2N random tails, 226 cells wide (first thirteen cells exact to tick
212). At every even tick 46..212 the first cells are classified (black AP13, white-A origin, white-eleventh A, white SS
entrance, pin 1110011110100, high 111001111, black-marker S) and the first appearance of a mixed-core row (first six
cells 111001 with core 010, 011 or 100 at cells 7..9, or the J prefixes 111001101100 / 11100110111110) is recorded per
tail, at any tick. Also the number of distinct first-20-cell rows at tick 50.

PREDICTIONS (CL346). F1: the black AP13 rate over even ticks 46..212 lies within a factor two of the sea's 6.8 x 10^-4
per row per white-wall tick (0.5). F2: at least one white-A origin row appears by tick 212 (0.7). F3: a mixed-core row
appears at some tick <= 80 in more than half of the tails (0.5). Counterfactual: typed shapes at sea rates only and no
early core mean the bad B is an exit to the sea rather than a renewal or a late admission. Unexpected check: the number
of distinct first-20-cell rows at tick 50.
"""
import sys, time
import numpy as np
B=lambda s: tuple(int(c) for c in s)
ORIGIN=B('1110100011011010010010000100100000000000000000000000000000000000')
TYPES=[B('1110100011111'),B('1110100011100'),B('1110100011101')]
VALID=[B('11101')+B(w) for w in ('0000','0100','0101','0110','0111')]
CORE=[B('010'),B('011'),B('100')]; J=(B('111001101100'),B('11100110111110'))
LOG2N=int(sys.argv[1]) if len(sys.argv)>1 else 22
N=1<<LOG2N; M=N//64; TMAX=212; WIDTH=13+TMAX+1
ONES=np.uint64(0xFFFFFFFFFFFFFFFF)
def pc(m): return int(np.bitwise_count(m).sum())
def match(cells,pattern,base=None):
    m=np.full(M,ONES,dtype=np.uint64) if base is None else base.copy()
    for i,b in enumerate(pattern): m&= cells[i] if b else ~cells[i]
    return m
rng=np.random.default_rng(20261011)
cells=[np.full(M,ONES if b else 0,dtype=np.uint64) for b in ORIGIN]
cells+=[rng.integers(0,2**64,size=M,dtype=np.uint64,endpoint=False) for _ in range(WIDTH-len(ORIGIN))]
SHAPES={'black AP13':TYPES,'white-A origin':[B('1110100011011')],'white-eleventh A':[B('11101000110')],
        'white SS entrance':VALID,'pin 1110011110100':[B('1110011110100')],'high 111001111':[B('111001111')],
        'black-marker S':[B('111011101'),B('111011111')]}
cnt={k:0 for k in SHAPES}; nticks=0
core_seen=np.zeros(M,dtype=np.uint64); first_core={}
t0=time.time()
for t in range(TMAX+1):
    if t==44:
        print('tick 44 first 12 cells unguarded B in all tails:',pc(match(cells,B('111010011001')))==N,flush=True)
    if t==50:
        w=np.zeros(N,dtype=np.int64)
        for i in range(20): w|=np.unpackbits(cells[i].view(np.uint8),bitorder='little').astype(np.int64)<<i
        print('distinct first-20-cell rows at tick 50:',len(np.unique(w)),flush=True)
    if t>=45:
        base=match(cells,B('111001')); m=np.zeros(M,dtype=np.uint64)
        for c in CORE: m|=match(cells[6:],c,base)
        m|=match(cells,J[0]); m|=match(cells,J[1])
        new=m&~core_seen
        if pc(new): first_core[t]=pc(new)
        core_seen|=m
    if t>=46 and t%2==0:
        nticks+=1
        for k,pats in SHAPES.items():
            m=np.zeros(M,dtype=np.uint64)
            for p in pats: m|=match(cells,p)
            cnt[k]+=pc(m)
    if t==TMAX: break
    wall=np.full(M,ONES if t%2 else 0,dtype=np.uint64)
    cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
print('tails',N,'| even ticks 46..212:',nticks,'| %.0fs'%(time.time()-t0))
for k in SHAPES: print('  %-20s rate per tail per even tick %.2e (count %d)'%(k,cnt[k]/(N*nticks),cnt[k]))
cum=0
for t in sorted(first_core):
    cum+=first_core[t]
    if t<=80 or t%20==0 or t==max(first_core):
        print('  first mixed-core row at tick %3d in %8d tails (cumulative %.4f)'%(t,first_core[t],cum/N))
by80=sum(v for t,v in first_core.items() if t<=80)/N
print('tails with a mixed-core row by tick 80: %.4f | by 212: %.4f'%(by80,cum/N))
