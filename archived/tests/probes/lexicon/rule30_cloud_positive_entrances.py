#!/usr/bin/env python3
"""rule30_cloud_positive_entrances.py: the twelve positive white-A entrances of the collar grammar, a complete census
(CL329, CL330) plus the fate of their X route (registered below before its run).

RUN-ON:     cpu (Python 3 standard library plus numpy; about five minutes)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_positive_entrances.py

WHAT. Rule 30 beside the alternating wall x_t(0) = t mod 2. A white-A origin at a white-wall tick has first thirteen
cells 1110100011011; GC1136's two-family predicate on sites 14..25 selects the 28 source cylinders that reach GC1080's
case B after the S block, and GC1137 splits them by the low pair at sites 18, 19 after S: 16 negative (11) and 12
positive (01). Section 1: for the 12 positive cylinders and all 16,384 completions of sites 26..39, the S-D-H
continuation to tick 26 (bit-sliced over every exterior): sites 14, 15 at tick 16, the H track on site 5, the first
thirteen cells at tick 26. Section 2: exact discharges of the three tick-26 low prefixes over all completions (ten
ticks, even start). Section 3: the same path at width 28 with origin labels (strip of 28 cells, cell 29 free), tracks S,
D, H, D, H on site 5, the rows at tick 46 classified, and thirty free ticks from the B-prefix rows watching for any A,
SS entrance or high 111. Section 4: the X branch (site 14 = 0 at tick 16) at width 28 along its observed track, and
thirty free ticks from its tick-46 rows.

RESULTS RECORDED BEFORE THIS FILE (CL330, first computed in Cloud's scratch, 2026-10-11): site 15 = 1 in all 196,608
cones; site 14 splits 98,304 / 98,304; the H track is realised everywhere; tick 26 rows are low rows 1110010010001
(75,520), 1110010010000 (22,784) for site 14 = 1 and 1110010011101 (98,304) for site 14 = 0; discharges 111001010
(C010), 111001101 (the 101 class) and 111000101 (the X route, track 0101100101) at tick 36, each in all 1,024 cones; at
width 28 the 101 branch gives 946 rows at tick 46, all B prefix 111010011, and thirty free ticks show no black AP13,
white A, SS entrance or high 111; the X branch gives 1110010011101 (264 rows), 111000101 (662), 100011001 / 100011011
(1,519) and rows beginning 010... at tick 56.

PREDICTION FOR SECTION 4's LAST PART, registered before its run: from the X rows at tick 46 (1,519 rows at width 28),
thirty free ticks will produce at least one black AP13 row (probability 0.5) and at least one white SS entrance (0.6);
the counterfactual, none of either in thirty ticks, would put the X route beside the B rows as a non-renewing exit at
this width."""
import itertools, sys
import numpy as np
from collections import Counter
sys.setrecursionlimit(100000)
B=lambda s: tuple(int(c) for c in s)
TYPES=[B('1110100011111'),B('1110100011100'),B('1110100011101')]; TYPESET=set(TYPES)
VALID={B('11101')+B(w) for w in ('0000','0100','0101','0110','0111')}
def fwd(x,left):
    f=[left]+list(x); return [f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1)]
def imgs(row,t,W):
    out=set()
    for b in (0,1):
        s=(t%2,)+tuple(row)+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out
base=[1,1,1,0,1,0,0,0,1,1,0,1,1]
def family(s):
    a,b,c,d,e,f,g,h,i,j,k,l=s
    f1=(a,b,c,d,e,f)==(0,1,1,0,1,1) and ((g==1 and h==1 and i==0 and j==0) or (g==1 and h==0 and (i or j)==1)
                                        or (g==0 and h==1 and i==0 and j==0 and (k or l)==1))
    f2=(a,b,c,d,e,f,g,h)==(0,1,1,1,0,0,0,0) and (((i^j)==1) or (i==1 and j==1 and k==0 and l==0))
    return f1 or f2
src=[s for s in itertools.product((0,1),repeat=12) if family(s)]; assert len(src)==28
pos=[]; neg=[]
for s in src:
    x=base+list(s)+[0]*6; rows=[x]
    for t in range(6): rows.append(fwd(rows[-1],t%2))
    (pos if (rows[6][17],rows[6][18])==(0,1) else neg).append(s)
assert len(pos)==12 and len(neg)==16
print('positive cylinders 12, negative 16')
# ---------- section 1: bit-sliced census over all exteriors ----------
NB=14; N=1<<NB; idx=np.arange(N,dtype=np.int64)
s15=Counter(); s14=Counter(); htrack=Counter(); pref_by14={0:Counter(),1:Counter()}
for s in pos:
    cells=[np.full(N,b,dtype=np.uint8) for b in base+list(s)]+[((idx>>k)&1).astype(np.uint8) for k in range(NB)]
    site5=[]; r16=None
    for t in range(26):
        if t==16: r16=cells
        site5.append(cells[4].copy())
        wall=np.full(N,t%2,dtype=np.uint8); new=[]
        for i in range(len(cells)-1):
            left=cells[i-1] if i>0 else wall; new.append(left^(cells[i]|cells[i+1]))
        cells=new
    s15.update(Counter(r16[14].tolist())); s14.update(Counter(r16[13].tolist()))
    ok=np.ones(N,dtype=bool); H=[0,1,0,1,1,0,1,0,1,0]
    for k in range(10): ok&=(site5[16+k]==H[k])
    htrack.update(Counter(ok.tolist()))
    words=np.zeros(N,dtype=np.int64)
    for i in range(13): words|=cells[i].astype(np.int64)<<i
    for w,b14 in zip(words.tolist(),r16[13].tolist()):
        pref_by14[b14][''.join(str((w>>i)&1) for i in range(13))]+=1
print('section 1: site 15 at 16',dict(s15),'| site 14 at 16',dict(s14),'| H track realised',dict(htrack))
print('   tick-26 prefixes, site14=0:',dict(pref_by14[0]),'| site14=1:',dict(pref_by14[1]))
# ---------- section 2: discharges of the tick-26 low prefixes ----------
for P in ('1110010010000','1110010010001','1110010011101'):
    out=Counter(); tr=Counter()
    for ext in itertools.product((0,1),repeat=10):
        x=B(P)+ext; rows=[list(x)]; track=[]
        for t in range(10): track.append(rows[-1][4]); rows.append(fwd(rows[-1],(26+t)%2))
        out[''.join(map(str,rows[10][:9]))]+=1; tr[''.join(map(str,track))]+=1
    print('section 2:',P,'-> tick 36 first 9',dict(out),'| site-5 track',dict(tr))
# ---------- section 3: width 28 with origin labels, the 101 branch ----------
W=28
def flow5(lab,t0,track):
    cur=dict(lab); t=t0
    for bit in track:
        nxt={}
        for r,o in cur.items():
            if r[4]!=bit: continue
            for s in imgs(r,t,W): nxt[s]=nxt.get(s,0)|o
        cur=nxt; t+=1
    return cur,t
def free(lab,t0,n):
    cur=dict(lab); t=t0
    for _ in range(n):
        nxt={}
        for r,o in cur.items():
            for s in imgs(r,t,W): nxt[s]=nxt.get(s,0)|o
        cur=nxt; t+=1
    return cur,t
def cls(r):
    p=''.join(map(str,r[:13]))
    if r[:13] in TYPESET: return 'black AP13'
    if p.startswith('1110100011') and p[10]=='0': return 'white-eleventh A'
    if r[:9] in VALID: return 'white SS entrance'
    if p.startswith('111010011'): return 'B prefix'
    if p.startswith('111001010') or p.startswith('111001100'): return 'C core'
    if p.startswith('1110011111') or p.startswith('111001111'): return 'high 111'
    return 'other '+p[:6]
def watch(rows,t0,n,label):
    cur=dict(rows); t=t0; hits=Counter(); last=0
    for _ in range(n):
        nxt={}
        for r,o in cur.items():
            for s in imgs(r,t,W): nxt[s]=nxt.get(s,0)|o
        cur=nxt; t+=1; last=len(cur)
        for r in cur:
            c=cls(r)
            if c in ('black AP13','white-eleventh A','white SS entrance','high 111'): hits[c]+=1
    seen=dict(hits) if hits else 'NONE'
    print('   %s: %d free ticks from tick %d, final row set %d, renewal-type rows seen: %s'%(label,n,t0,last,seen))
starts=[tuple(base+list(s)+list(e)) for s in pos for e in itertools.product((0,1),repeat=3)]
lab={s:(1<<i) for i,s in enumerate(starts)}
a,t=flow5(lab,0,B('111000')); a,t=flow5(a,t,B('0101100000'))
hi1={r:o for r,o in a.items() if r[13]==1}; hi0={r:o for r,o in a.items() if r[13]==0}
P=lambda rows,k: Counter(''.join(map(str,r[:k])) for r in rows)
print('section 3: tick 16 rows',len(a),'| site14=1',len(hi1),'| site14=0',len(hi0),
      '| site 15 all black',all(r[14]==1 for r in a))
h1,t=flow5(hi1,16,B('0101101010')); d1,t=flow5(h1,26,B('0101100000')); e1,t=flow5(d1,36,B('0101101010'))
print('   101 branch: tick 26 rows',len(h1),P(h1,13),'| tick 36',len(d1),P(d1,9),
      '| tick 46',len(e1),Counter(cls(r) for r in e1))
watch(e1,46,30,'B-prefix rows of the 101 branch')
# ---------- section 4: the X branch ----------
h0,t=flow5(hi0,16,B('0101101010')); x1,t=flow5(h0,26,B('0101100101')); x2,t=flow5(x1,36,B('0000111100'))
print('section 4: X branch tick 26',len(h0),P(h0,13),'| tick 36',len(x1),P(x1,9),'| tick 46',len(x2),P(x2,9))
x1f,_=free(h0,26,10); print('   X track forced (free D-phase classes):',P(x1f,9).most_common(3))
watch(x2,46,30,'X rows')
