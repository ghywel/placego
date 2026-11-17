#!/usr/bin/env python3
"""rule30_cloud_x_route_realcone.py: the X route of the positive white-A entrances in REAL cones (no strip relaxation),
registered in CL331 before its run.

RUN-ON:     cpu (Python 3 standard library plus numpy; about two minutes at LOG2N = 24, 250 MB)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_x_route_realcone.py 24      (add 'smoke' to stop at tick 46)

WHAT. Rule 30 beside the alternating wall x_t(0) = t mod 2. For each of the twelve positive white-A cylinders of CL329
(first thirteen cells 1110100011011, GC1136's family on sites 14..25, low pair 01 after S), 2^LOG2N random exteriors 120
cells wide (132 in mode 'family'), so that the first thirteen (or 25) cells are exact to tick 106 (information moves
left one cell per tick), run bit-sliced in uint64 words with a fixed seed. The X branch is the half with site 14 = 0 at
tick 16. Recorded: the forced rows at 26 and 36, the site-5 track 0000111100 over 36..45 and the two tick-46 prefixes;
the high pin shape 1110011110100 at 66 (and any 111001111); white SS entrances, B prefix, white-eleventh A and the
white-A origin row at 94, 100, 106; black AP13 rows and white-A origin rows at every even tick 48..106 (row-ticks, X
cones only).

WHY. At width 28 with cell 29 free (CL331) the X route's rows reach 1110011110100 at tick 66, white SS entrances at 94
and 100, B-prefix and white-A origin rows at 106: a return to the white collar vocabulary that the relaxation allows.
After twenty ticks the free cell's influence covers the first thirteen cells, so the relaxation cannot say whether a
real exterior produces these rows. This sampler asks the real half-plane.

PREDICTIONS (CL331, registered before the run). P1: the tick-66 row 1110011110100 is realised in the X cones, at a
frequency between 10^-5 and 10^-3 per X cone (0.7). P2: white SS entrances at 94 and 100 are realised (0.7), and the
white-A origin row at 106 is realised (0.6). P3: black AP13 rows appear at some even tick in 48..106 (0.8), at a rate
below 10^-3 per X cone per even tick (0.7). Counterfactual: no real X cone reaching 1110011110100 at 66 would make the
re-entry chain the free cell's artefact, and CL330's reading of X as an exit would stand at this horizon. Unexpected
check: whether every real X cone shows 100011001 or 100011011 at tick 46, as every relaxed row does.

ADDED AFTER THE FIRST RUN (CL332, registered before the family run). Mode 'family' (COMMAND ... 24 family) keeps the
masks of the pin at 66, the SS entrances at 94 and 100 and the white-eleventh A at 106 and counts their joint cones
(Q2), and histograms sites 14..25 of the white-A origin rows at tick 106 over the 4,096 patterns, counting those in
GC1136's 28-pattern family and in the 12 positive cylinders (Q1); predictions and the counterfactual in CL332. The
'distinct patterns' TOTAL line sums the per-cylinder counts (a sum, not a union); the per-cylinder lists are exact.

ADDED AFTER THE FAMILY RUN (CL333, registered before the chain run). Mode 'chain' (COMMAND ... 24 chain) runs to tick
212, 238 cells wide, lists every 12-bit pattern of the origin rows at 106 and the first thirteen cells at 112, 122 and
132 of those cones (GC1141's dispatch ticks), and asks whether the return renews: the pin 1110011110100 at 172, white SS
entrances at 200 and 206 and the origin row at 212 among the cones with the origin at 106, plus their origin and black
AP13 row-ticks over the even ticks 108..212. Predictions Q3..Q6 and the counterfactual in CL333."""
import itertools, sys, time
import numpy as np
B=lambda s: tuple(int(c) for c in s)
TYPES=[B('1110100011111'),B('1110100011100'),B('1110100011101')]
VALID=[B('11101')+B(w) for w in ('0000','0100','0101','0110','0111')]
def fwd(x,left):
    f=[left]+list(x); return [f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1)]
base=[1,1,1,0,1,0,0,0,1,1,0,1,1]
def family(s):
    a,b,c,d,e,f,g,h,i,j,k,l=s
    f1=(a,b,c,d,e,f)==(0,1,1,0,1,1) and ((g==1 and h==1 and i==0 and j==0) or (g==1 and h==0 and (i or j)==1)
                                        or (g==0 and h==1 and i==0 and j==0 and (k or l)==1))
    f2=(a,b,c,d,e,f,g,h)==(0,1,1,1,0,0,0,0) and (((i^j)==1) or (i==1 and j==1 and k==0 and l==0))
    return f1 or f2
src=[s for s in itertools.product((0,1),repeat=12) if family(s)]; assert len(src)==28
pos=[]
for s in src:
    x=base+list(s)+[0]*6; rows=[x]
    for t in range(6): rows.append(fwd(rows[-1],t%2))
    if (rows[6][17],rows[6][18])==(0,1): pos.append(s)
assert len(pos)==12
LOG2N=int(sys.argv[1]); N=1<<LOG2N; M=N//64; MODE=sys.argv[2] if len(sys.argv)>2 else ''
SMOKE=MODE=='smoke'; CHAIN=MODE=='chain'; FAMILY=MODE in ('family','chain')
TMAX=212 if CHAIN else (46 if SMOKE else 106)
WIDTH=(25 if FAMILY else 13)+TMAX+1     # family mode needs sites 14..25 exact at tick 106
ONES=np.uint64(0xFFFFFFFFFFFFFFFF)
def pc(m):
    if hasattr(np,'bitwise_count'): return int(np.bitwise_count(m).sum())
    return int(np.unpackbits(m.view(np.uint8)).sum())
def match(cells,pattern,mask):
    # words where the first len(pattern) cells equal pattern, restricted to mask
    m=mask.copy()
    for i,b in enumerate(pattern):
        m&= cells[i] if b else ~cells[i]
    return m
rng=np.random.default_rng(20261011)
tot={}
def add(k,v): tot[k]=tot.get(k,0)+v
t0=time.time()
for ci,s in enumerate(pos):
    fixed=base+list(s)
    cells=[np.full(M,ONES if b else 0,dtype=np.uint64) for b in fixed]
    cells+=[rng.integers(0,2**64,size=M,dtype=np.uint64,endpoint=False) for _ in range(WIDTH-len(fixed))]
    xmask=None; track=None; site5=[]; keep={}
    cnt={}
    for t in range(TMAX+1):
        if t==16:
            xmask=~cells[13]            # X branch: site 14 = 0
            cnt['X']=pc(xmask)
        if t==26: cnt['26 low 1110010011101']=pc(match(cells,B('1110010011101'),xmask))
        if t==36: cnt['36 111000101']=pc(match(cells,B('111000101'),xmask))
        if 36<=t<46: site5.append(cells[4].copy())
        if t==46:
            tr=xmask.copy()
            for k,b in enumerate(B('0000111100')): tr&= site5[k] if b else ~site5[k]
            cnt['46 track 0000111100']=pc(tr)
            cnt['46 100011001|100011011']=pc(match(cells,B('1000110'),xmask)&cells[8])
        if not SMOKE:
            if t==66:
                keep[66]=match(cells,B('1110011110100'),xmask); cnt['66 high 1110011110100']=pc(keep[66])
                cnt['66 any high 111 (111001111)']=pc(match(cells,B('111001111'),xmask))
            if t in (94,100,106):
                v=np.zeros(M,dtype=np.uint64)
                for w in VALID: v|=match(cells,w,xmask)
                keep[t]=v; cnt['%d white SS entrance'%t]=pc(v)
                cnt['%d B prefix 111010011'%t]=pc(match(cells,B('111010011'),xmask))
                e=match(cells,B('11101000110'),xmask); cnt['%d white-eleventh A'%t]=pc(e)
                o=match(cells,B('1110100011011'),xmask); cnt['%d white-A origin 1110100011011'%t]=pc(o)
                if FAMILY and t==106:
                    cnt['joint pin66 SS94 SS100 eleventhA106']=pc(keep[66]&keep[94]&keep[100]&e)
                    cnt['joint SS94 SS100 eleventhA106']=pc(keep[94]&keep[100]&e)
                    sel=np.flatnonzero(np.unpackbits(o.view(np.uint8),bitorder='little'))
                    pat=np.zeros(len(sel),dtype=np.int64)
                    for k in range(12):
                        pat|=np.unpackbits(cells[13+k].view(np.uint8),bitorder='little')[sel].astype(np.int64)<<k
                    h=np.bincount(pat,minlength=4096)
                    fam=sum(int(h[p]) for p in range(4096) if family(tuple((p>>k)&1 for k in range(12))))
                    posn=sum(int(h[p]) for p in range(4096) if tuple((p>>k)&1 for k in range(12)) in pos)
                    keep['o106']=o; keep['e106']=e
                    cnt['origin106 rows']=len(sel); cnt['origin106 distinct patterns']=int((h>0).sum())
                    cnt['origin106 in GC1136 family']=fam; cnt['origin106 in the 12 positive']=posn
                    top=[p for p in sorted(range(4096),key=lambda p:-h[p]) if h[p]>0][:16]
                    cnt['origin106 top patterns']=' '.join(
                        '%s:%d'%(''.join(str((p>>k)&1) for k in range(12)),h[p]) for p in top)
            if CHAIN and t in (112,122,132):
                sel=np.flatnonzero(np.unpackbits(keep['o106'].view(np.uint8),bitorder='little'))
                pat=np.zeros(len(sel),dtype=np.int64)
                for k in range(13):
                    pat|=np.unpackbits(cells[k].view(np.uint8),bitorder='little')[sel].astype(np.int64)<<k
                h=np.bincount(pat,minlength=8192); top=[p for p in sorted(range(8192),key=lambda p:-h[p]) if h[p]>0][:8]
                cnt['%d first13 of origin106 cones (%d patterns)'%(t,int((h>0).sum()))]=' '.join(
                    '%s:%d'%(''.join(str((p>>k)&1) for k in range(13)),h[p]) for p in top)
            if CHAIN and t==172:
                cnt['172 pin in origin106 cones']=pc(match(cells,B('1110011110100'),keep['o106']))
                cnt['172 pin in eleventhA106 cones']=pc(match(cells,B('1110011110100'),keep['e106']))
                cnt['172 pin in X cones']=pc(match(cells,B('1110011110100'),xmask))
            if CHAIN and t in (200,206,212):
                v=np.zeros(M,dtype=np.uint64)
                for w in VALID: v|=match(cells,w,keep['o106'])
                cnt['%d white SS entrance in origin106 cones'%t]=pc(v)
                cnt['%d white-A origin in origin106 cones'%t]=pc(match(cells,B('1110100011011'),keep['o106']))
            if CHAIN and t%2==0 and 108<=t<=212:
                KO='white-A origin at even ticks 108..212 in origin106 cones (row-ticks)'
                cnt[KO]=cnt.get(KO,0)+pc(match(cells,B('1110100011011'),keep['o106']))
                a=np.zeros(M,dtype=np.uint64)
                for w in TYPES: a|=match(cells,w,keep['o106'])
                KB='black AP13 at even ticks 108..212 in origin106 cones (row-ticks)'
                cnt[KB]=cnt.get(KB,0)+pc(a)
            if t%2==0 and t>=48:
                a=np.zeros(M,dtype=np.uint64)
                for w in TYPES: a|=match(cells,w,xmask)
                n=pc(a)
                KA='black AP13 at even ticks 48..%d (X cones, row-ticks)'%TMAX
                if n: cnt[KA]=cnt.get(KA,0)+n
                KW='white-A origin at even ticks 48..%d (row-ticks)'%TMAX
                cnt[KW]=cnt.get(KW,0)+pc(match(cells,B('1110100011011'),xmask))
        if t==TMAX: break
        wall=np.full(M,ONES if t%2 else 0,dtype=np.uint64)
        new=[]
        for i in range(len(cells)-1):
            left=cells[i-1] if i>0 else wall
            new.append(left^(cells[i]|cells[i+1]))
        cells=new
    for k,v in cnt.items():
        if isinstance(v,int): add(k,v)
    print('cylinder',ci,''.join(map(str,s)),'N',N,'|',' | '.join('%s %s'%(k,v) for k,v in cnt.items()),
          '| %.0fs'%(time.time()-t0),flush=True)
print('TOTAL over 12 cylinders x',N,':')
for k,v in tot.items(): print('  ',k,v)
