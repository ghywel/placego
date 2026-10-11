#!/usr/bin/env python3
"""rule30_cloud_gc1142_check.py: Cloud's independent second read of GPT's GC1142 (the first SS after a high-111 origin
cannot exit through unguarded B), with GPT's definitions re-implemented rather than imported (CL336).

RUN-ON:     cpu (Python 3 standard library plus numpy; under a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1142_check.py

WHAT. (1) The 1,536 black-S cones (prefixes 111011101, 111011110, 111011111 with 512 exteriors) through one SS block: B
outputs, white-tenth B, bad B (B prefix, tenth white, eleventh white, twelfth black), whitening and whitening-SS
outputs. (2) A FORWARD census of every actual high-111 origin: 111001111 plus all 2^19 completions of sites 10..28 with
the white wall, ten ticks, the H track on site 5, GC1076's shields, and which time-10 rows are bad-B, whitening-SS or
guarded-B sources (the 18 cells at time 10 depend on the 28 cells at time 0, so this census is complete). (3) The two
28-cell sources by exhaustive completion (the guarded-B certificate at 16 and mixed admission at 22; the whitening into
a white SS at 16). (4) The retained failures. (5) An own left-permutive inverse through the H block with the shields:
the layer counts for the 17 bad-B sources, the time-1 prefixes before the shield, the whitening antecedents, the
two-step pasts.

PREDICTIONS (written before the run, in Cloud's scratch): (1) 240 B, 228 white tenth, 17 bad B, 768 whitening, 480
whitening SS (0.8); (2) the shields hold in every H-track cone and no time-10 row is a bad-B source (0.8); (3) the
whitening-SS sources are reached from actual high-111 origins (0.7); (4) both 28-cell certificates hold for every
completion (0.8); (5) the inverse reproduces 52, 48, 68, 160, 484, 224, 896, 2880, 0, 0 (0.5). Counterfactual: a forward
cone reaching a bad-B source refutes GC1142's main claim. Unexpected check: how many of the 2^19 completions realise the
H track, and the split of their time-10 rows.

RESULT (CL336): all five held. Every one of the 524,288 completions realises the H track and the shields; the time-10
rows are 111011101 (176,128), 111001001 (139,264), 111011111 (110,592) or 111001010 (98,304), never 111011110; none is
a bad-B source, 80,256 are whitening-SS sources (45 distinct of the 480), 16,896 guarded-B sources; the inverse layer
counts, the time-1 prefixes 0000 / 0100, the 80,256 and the two-step pasts 48 / 2,560 all match GPT.
"""
import itertools, numpy as np
from collections import Counter
B=lambda s: tuple(int(c) for c in s)
CORE={B('010'),B('011'),B('100')}; J=(B('111001101100'),B('11100110111110'))
def fwd(x,left):
    f=[left]+list(x); return tuple(f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1))
def run(start,n,phase=0):
    rows=[tuple(start)]
    for t in range(n): rows.append(fwd(rows[-1],(t+phase)%2))
    return rows
def admitted(row): return row[6:9] in CORE or row[:12]==J[0] or row[:14]==J[1]
def mixed_long(row): return row[:6]==B('111001') and admitted(row)
def guarded_B(row): return len(row)>=12 and row[:10]==B('1110100110') and (row[10]==1 or row[11]==0)
H=B('0101101010')
# (1) the 1,536 black-S cones, six ticks (even start)
counts=Counter(); bad=set(); whiten=set(); goodB=set()
for pre in ('111011101','111011110','111011111'):
    for far in itertools.product((0,1),repeat=9):
        src=B(pre)+far; r=run(src,6); end=r[6]
        assert tuple(x[4] for x in r[:6])==B('111010')
        if end[:9]==B('111010011'):
            counts['B']+=1
            if guarded_B(end): goodB.add(src)
            if end[9]==0:
                counts['B10white']+=1
                if not guarded_B(end): counts['badB']+=1; bad.add(src)
        if end[5]==0:
            counts['whiten']+=1
            if end[:9] not in (B('111010001'),B('111010011')): counts['whitenSS']+=1; whiten.add(src)
print('(1) 1536 cones:',dict(counts),'| bad-B sources',len(bad),'| whitening-SS sources',len(whiten),
    '| guarded-B sources',len(goodB))
# (2) FORWARD census of actual H111 origins: 111001111 + sites 10..28 free (2^19), white wall at time 0
NB=19; N=1<<NB; idx=np.arange(N,dtype=np.int64)
cells=[np.full(N,b,dtype=np.uint8) for b in B('111001111')]+[((idx>>k)&1).astype(np.uint8) for k in range(NB)]
rows=[]
for t in range(11):
    rows.append(cells)
    if t==10: break
    wall=np.full(N,t%2,dtype=np.uint8)
    cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
htrack=np.ones(N,dtype=bool)
for t in range(10): htrack&=(rows[t][4]==H[t])
print('(2) H111 origins with the H track on site 5:',int(htrack.sum()),'of',N)
sh=np.ones(N,dtype=bool)
for t,pat in ((0,'1111'),(1,'1000'),(4,'000'),(5,'10')):
    for k,b in enumerate(B(pat)): sh&=(rows[t][5+k]==int(b))
print('    shields (t0 6..9=1111, t1=1000, t4 6..8=000, t5 6,7=10) hold in all H-track cones:',bool((~htrack|sh).all()),
      '| cones with shields but no H track:',int((sh&~htrack).sum()))
w18=np.zeros(N,dtype=np.int64)
for i in range(18): w18|=rows[10][i].astype(np.int64)<<i
def enc(src): return sum(b<<i for i,b in enumerate(src))
badset={enc(s) for s in bad}; whset={enc(s) for s in whiten}; goodset={enc(s) for s in goodB}
sel=w18[htrack]
hits_bad=int(np.isin(sel,list(badset)).sum()); hits_wh=int(np.isin(sel,list(whset)).sum()); hits_good=int(np.isin(sel,
    list(goodset)).sum())
pref9=Counter()
for v in sel.tolist(): pref9[''.join(str((v>>i)&1) for i in range(9))]+=1
print('    time-10 rows of H-track cones reaching: bad-B sources',hits_bad,'| whitening-SS sources',hits_wh,
    '| guarded-B sources',hits_good)
print('    first 9 cells at time 10 over H-track cones:',pref9.most_common(6))
distinct_wh=len(set(sel.tolist())&whset); distinct_bad=len(set(sel.tolist())&badset)
print('    distinct whitening-SS sources reached',distinct_wh,'of',len(whiten),'| distinct bad-B reached',
    distinct_bad,'of',len(bad))
# (4) the two 28-cell sources, all completions
def forced(prefix,tick,ncells,nfree):
    N=1<<nfree; idx=np.arange(N,dtype=np.int64)
    cells=[np.full(N,b,dtype=np.uint8) for b in prefix]+[((idx>>k)&1).astype(np.uint8) for k in range(nfree)]
    assert len(cells)>=ncells+tick
    for t in range(tick):
        wall=np.full(N,t%2,dtype=np.uint8)
        cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
    return ''.join(str(int(np.unique(c)[0])) if len(np.unique(c))==1 else '?' for c in cells[:ncells]), cells
pos=B('1110011110000000001101000000'); f16,_=forced(pos,16,17,6); f22,c22=forced(pos,22,14,9)
ok=np.ones(1<<9,dtype=bool)
for i,b in enumerate(B('111001')): ok&=(c22[i]==b)
w3=c22[6].astype(np.int64)|(c22[7].astype(np.int64)<<1)|(c22[8].astype(np.int64)<<2)
core=np.isin(w3,[2,6,1]); j1=np.ones(1<<9,dtype=bool); j2=np.ones(1<<9,dtype=bool)
for i,b in enumerate(J[0]): j1&=(c22[i]==b)
for i,b in enumerate(J[1]): j2&=(c22[i]==b)
r=run(pos+(0,)*42,22)
print('(4) positive 28-cell H source: forced at 16',f16,'(GPT 11101001101000111) guarded',guarded_B(B(f16.replace('?',
    '0'))),
      '| at 22 mixed_long for all 2^9 tails:',bool((ok&(core|j1|j2)).all()),
      '| site-5 track 0..15:',''.join(str(x[4]) for x in r[:16]))
wh=B('1110011110000000000100000000'); f10,_=forced(wh,10,13,4); f16w,_=forced(wh,16,18,6)
print('    whitening 28-cell H source: forced at 10',f10,'| at 16',f16w,'(GPT 111010000011000100) sixth white:',
    f16w[5]=='0')
# (5) failures retained
for s,label in (('111011111111010000','badB after SS'),('111011110100000000','whitens into SS')):
    e=run(B(s),6)[6]; print('    retained',label,s,'-> end',''.join(map(str,e[:12])),'guarded_B',guarded_B(e),'sixth',
        e[5])
# (6) own inverse: predecessors on sites 6.. with the fifth site prescribed, two rightmost bits free
def inverse(y,fifth):
    n=len(y); out=set()
    for a,b in itertools.product((0,1),repeat=2):
        x=[0]*(n+1); x[n-1]=a; x[n]=b
        for i in range(n-1,0,-1):      # y[i] = x[i-1] ^ (x[i] | x[i+1])  (y on sites 6..6+n-1, x on sites 6..6+n)
            x[i-1]=y[i]^(x[i]|x[i+1])
        if (y[0]^(x[0]|x[1]))==fifth: out.add(tuple(x))
    return out
shields={0:B('1111'),1:B('1000'),4:B('000'),5:B('10')}
layer={x[5:] for x in bad}; sizes=[]; pre1=None
for t in range(9,-1,-1):
    cand={x for y in layer for x in inverse(y,H[t])}
    if t==1: pre1=sorted({''.join(map(str,x[:4])) for x in cand})
    layer={x for x in cand if t not in shields or x[:len(shields[t])]==shields[t]}; sizes.append(len(layer))
print('(6) own inverse of the 17 bad-B sources through H with the shields: layer sizes t=9..0',sizes,
    '(GPT 52,48,68,160,484,224,896,2880,0,0)',
      '| time-1 prefixes before the shield',pre1)
layer={x[5:] for x in whiten}; sizes=[]
for t in range(9,-1,-1):
    cand={x for y in layer for x in inverse(y,H[t])}
    layer={x for x in cand if t not in shields or x[:len(shields[t])]==shields[t]}; sizes.append(len(layer))
    if len(layer)>300000: print('   cap'); break
print('    whitening-SS sources: H111 antecedents at time 0',sizes[-1],'(GPT 80256) sizes',sizes)
for label,targets in (('bad-B',bad),('whitening-SS',whiten)):
    layer={x[5:] for x in targets}; sz=[]
    for t in (9,8):
        layer={x for y in layer for x in inverse(y,H[t])}; sz.append(len(layer))
    print('    two-step past of',label,'sources:',sz,'(GPT 48 / 2560 parents)')
