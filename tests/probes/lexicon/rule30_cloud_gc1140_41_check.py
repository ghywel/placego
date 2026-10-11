#!/usr/bin/env python3
"""rule30_cloud_gc1140_41_check.py: Cloud's independent second read of GPT's GC1140 (positive white-A entrances admit by 52
or exit X at 26, a 1,512-leaf all-tail cover) and GC1141 (non-LL white-A dispatch at 16 and the black SS marker), with
GPT's definitions re-implemented here rather than imported (CL334).

RUN-ON:     cpu (Python 3 standard library plus numpy; about three minutes at LOG2N = 24, one at 22)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1140_41_check.py 22

WHAT. GC1141: the dispatch of all 4,096 source-25 white-A cylinders 1110100011011 + sites 14..25 at tick 16 (the nine
cells at 16 depend on the 25 cells), the six-bit guard and five cubes for the 704 high-111 sources, the white-13th
control; for the 676 non-LL high sources, all 16,384 completions of sites 26..39 to tick 26 (site 6, the H track on site
5 over 16..25, the first nine cells); the declared witness and its 39-cell prefix (B at 44 for all 2^20 tails, the class
at 50 for all 2^25 tails). GC1140: the 33-cell counter's forced rows at 16, 26, 36 by exhaustive completion; the cover
re-derived with an own fresh-right certificate (nodes, leaves by type, lengths, high pairs, sha256 digest, X weight per
root); and a real-cone Monte Carlo with 2^LOG2N random exteriors per root, 67 cells wide (first 15 cells exact to tick
52), classifying every cone as X26, core36, B46, core52 or UNCOVERED by the actual rows, with no certificate.

PREDICTIONS (written before the run, in Cloud's scratch): (1) GC1141's dispatch reproduces exactly: 3,392 C (2,624 C010,
768 C100), 676 high 111, no 101, 704 high in all, decided by sites 14..19 as the eleven words (0.9); (2) the 676 non-LL
high sources have site 6 black at tick 26 in every completion (0.8); (3) the GC1140 cover re-derived gives 3,012 nodes,
1,512 leaves (12 X26, 1,185 core36, 109 B46, 206 core52), max length 38 and GPT's digest 9b78f672... (0.7); (4) the
Monte Carlo finds no cone outside the four leaf types, X cones have high pair 01 and admission cones 11 (0.8).
Counterfactual: a single uncovered real cone or a digest mismatch is a defect in GC1140 to report. Unexpected check: the
type shares (X, core36, B46, core52) in real cones.

RESULT (CL334, 2026-10-11): every prediction held; the digest matches; the X weight per root (1, 1, 1, 1, 1, 1/2, 1/2, 0
x 5) is exactly CL332's X cylinders; in 201,326,592 real cones none is uncovered and none needs core52 (every admission
is core36 or B46), so the 206 core52 leaves are where the certificate's knowledge ran out, not where real cones admit;
the 39-cell prefix's class at 50 is C010 for all 2^25 tails.
"""
import itertools, sys, time, hashlib
from collections import Counter
from fractions import Fraction
import numpy as np
B=lambda s: tuple(int(c) for c in s)
CORE={B('010'),B('011'),B('100')}
J=(B('111001101100'),B('11100110111110'))
def fwd(x,left):
    f=[left]+list(x); return tuple(f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1))
def run(start,n):
    rows=[tuple(start)]
    for t in range(n): rows.append(fwd(rows[-1],t%2))
    return rows
def certificate(src,steps):
    rows=[tuple(src)]
    for t in range(steps):
        old=rows[-1]
        if not old: rows.append(()); continue
        new=fwd(old,t%2)
        if old[-1]==1: new=new+(((old[-2] if len(old)>1 else t%2)^1),)
        rows.append(new)
    return rows
def admitted(row): return row[6:9] in CORE or row[:12]==J[0] or row[:14]==J[1]
def mixed_long(row): return row[:6]==B('111001') and admitted(row)
def guarded_B(row): return len(row)>=12 and row[:10]==B('1110100110') and (row[10]==1 or row[11]==0)
def family(s):
    a,b,c,d,e,f,g,h,i,j,k,l=s
    f1=(a,b,c,d,e,f)==(0,1,1,0,1,1) and ((g==1 and h==1 and i==0 and j==0) or (g==1 and h==0 and (i or j)==1)
                                        or (g==0 and h==1 and i==0 and j==0 and (k or l)==1))
    f2=(a,b,c,d,e,f,g,h)==(0,1,1,1,0,0,0,0) and (((i^j)==1) or (i==1 and j==1 and k==0 and l==0))
    return f1 or f2
WA=B('1110100011011')
t0=time.time()
# ---------- GC1141 (1): dispatch at 16 over all 4096 far patterns ----------
cnt=Counter(); high=set(); nonLL_101=0; w13=Counter()
for far in itertools.product((0,1),repeat=12):
    end=run(WA+far,16)[16]
    if end[6:9]==(1,1,1): high.add(far)
    if not family(far):
        cnt[''.join(map(str,end[6:9]))]+=1
        if end[6:9]==(1,0,1): nonLL_101+=1
    q=run(B('1110100011010')+far,16)[16]; w13[''.join(map(str,q[6:9]))]+=1
print('GC1141 dispatch outside the 28 (4068):',dict(cnt),'| unguarded 101:',nonLL_101,'| high 111 in all 4096:',
    len(high),
      '| white13 control:',dict(w13))
words=sorted({''.join(map(str,far[:6])) for far in high})
dec6=all(((far in high)==(''.join(map(str,far[:6])) in words)) for far in itertools.product((0,1),repeat=12))
print('   high decided by sites 14..19:',dec6,'| words',len(words),words)
cubes=['1001--','011100','01-01-','100-01','0100-1']
def incube(w,c): return all(cc=='-' or cc==ww for ww,cc in zip(w,c))
print('   eleven words == union of the five cubes:',set(words)=={''.join(b) for b in itertools.product('01',
    repeat=6) if any(incube(''.join(b),c) for c in cubes)})
# ---------- GC1141 (2): the 676 non-LL high sources at tick 26, all completions of sites 26..39 ----------
nonLL=[far for far in high if not family(far)]; print('   non-LL high sources:',len(nonLL))
NB=14; N=1<<NB; idx=np.arange(N,dtype=np.int64)
site6=Counter(); pref=Counter(); htrack=Counter(); pref28=Counter()
HT=[0,1,0,1,1,0,1,0,1,0]
for far in high:
    cells=[np.full(N,b,dtype=np.uint8) for b in WA+far]+[((idx>>k)&1).astype(np.uint8) for k in range(NB)]
    s5=[]
    for t in range(26):
        s5.append(cells[4].copy())
        wall=np.full(N,t%2,dtype=np.uint8)
        cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
    ok=np.ones(N,dtype=bool)
    for k in range(10): ok&=(s5[16+k]==HT[k])
    words9=np.zeros(N,dtype=np.int64)
    for i in range(9): words9|=cells[i].astype(np.int64)<<i
    target=pref if far in nonLL else pref28
    for w in set(words9.tolist()): target[''.join(str((w>>i)&1) for i in range(9))]+=int((words9==w).sum())
    if far in nonLL:
        site6.update(Counter(cells[5].tolist())); htrack.update(Counter(ok.tolist()))
print('   676 x 16384 cones at tick 26: site 6 black',dict(site6),'| H track realised',dict(htrack))
print('   first 9 cells at 26 (676 non-LL):',pref.most_common(6))
print('   first 9 cells at 26 (28 LL):',pref28.most_common(6))
# ---------- GC1141 (3): the witness ----------
wit=B('1110100011011010001000000'); r=run(wit+(0,)*55,52)
print('   witness: 16',''.join(map(str,r[16][:9])),'| 26',''.join(map(str,r[26][:13])),'| 32',''.join(map(str,
    r[32][:13])),
      '| 38',''.join(map(str,r[38][:13])),'| 44',''.join(map(str,
          r[44][:15])),'guardedB',guarded_B(r[44]),'| 50 mixed_long',mixed_long(r[50]))
pre39=B('111010001101101000100000000000000000000')
def forced(prefix,tick,ncells,nfree):
    N=1<<nfree; idx=np.arange(N,dtype=np.int64)
    cells=[np.full(N,b,dtype=np.uint8) for b in prefix]+[((idx>>k)&1).astype(np.uint8) for k in range(nfree)]
    assert len(cells)>=ncells+tick
    for t in range(tick):
        wall=np.full(N,t%2,dtype=np.uint8)
        cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
    out=[]
    for i in range(ncells):
        u=np.unique(cells[i]); out.append(str(int(u[0])) if len(u)==1 else '?')
    return ''.join(out), cells
f44,_=forced(pre39,44,15,20); print('   39-cell prefix forces at 44:',f44,'(GPT: 111010011011011)')
f50,c50=forced(pre39,50,14,25)
ok=np.ones(1<<25,dtype=bool)
for i,b in enumerate(B('111001')): ok&=(c50[i]==b)
w3=c50[6].astype(np.int64)|(c50[7].astype(np.int64)<<1)|(c50[8].astype(np.int64)<<2)
# careful: encode (s7,s8,s9) as s7 + 2 s8 + 4 s9 ; CORE words 010 -> s7=0,s8=1,s9=0 -> 2 ; 011 -> 0+2+4=6 ; 100 -> 1
core=np.isin(w3,[2,6,1])
j1=np.ones(1<<25,dtype=bool)
for i,b in enumerate(J[0]): j1&=(c50[i]==b)
j2=np.ones(1<<25,dtype=bool)
for i,b in enumerate(J[1]): j2&=(c50[i]==b)
print('   39-cell prefix at 50, all 2^25 tails: forced cells',f50,'| mixed_long everywhere:',
    bool((ok&(core|j1|j2)).all()),
      '| class split C/J1/J2:',int((ok&core).sum()),int((ok&j1).sum()),int((ok&j2).sum()))
# ---------- GC1140 counter ----------
ctr=B('111010001101101101101000100010000')
for tick,nc,nf,gpt in ((16,27,10,'111001111100011001001111100'),(26,22,15,'1110010010001101001010'),(36,17,20,
    '11100110111000110')):
    f,_=forced(ctr,tick,nc,nf); print('   GC1140 counter 33 cells, tick',tick,'forced',f,'| GPT',gpt,'| match',f==gpt)
# ---------- GC1140 (3): the cover re-derived ----------
roots=[WA+far for far in itertools.product((0,1),repeat=12) if family(far) and run(WA+far,6)[6][17:19]==(0,1)]
assert len(roots)==12
cover={p:[] for p in roots}; nodes=0; bad=None
for root in roots:
    stack=[root]
    while stack:
        src=stack.pop(); nodes+=1; r=certificate(src,52)
        typ=('X26' if len(r[26])>=11 and r[26][9:11]==(1,
            1) else 'core36' if mixed_long(r[36]) else 'B46' if guarded_B(r[46])
             else 'core52' if mixed_long(r[52]) else None)
        if typ: cover[root].append((src,typ)); continue
        if len(src)>60: bad=src; break
        stack.extend([src+(1,),src+(0,)])
    if bad: break
counts=Counter(); lengths=Counter(); pairs=Counter()
for root,leaves in cover.items():
    words=sorted(''.join(map(str,p)) for p,_ in leaves)
    assert all(not b.startswith(a) for a,b in zip(words,words[1:]))
    assert sum(Fraction(1,1<<(len(p)-25)) for p,_ in leaves)==1
    for src,typ in leaves:
        counts[typ]+=1; lengths[len(src)]+=1; r=certificate(src,16); pairs[(typ,
            r[16][13:15] if len(r[16])>=15 else '?')]+=1
payload='\n'.join(sorted(''.join(map(str,p))+' '+typ for v in cover.values() for p,typ in v))+'\n'
print('GC1140 cover (own certificate): nodes',nodes,'leaves',sum(counts.values()),dict(counts),'max length',
    max(lengths),'bad',bad)
print('   high pairs by type:',dict(pairs)); print('   digest',hashlib.sha256(payload.encode()).hexdigest(),
    '(GPT 9b78f6724c72bfdad6c8bb9abbe0f5378f0ee13a3b79f5127a88aa45bf11f308)')
# X leaf weights per root
for root,leaves in cover.items():
    xw=sum(Fraction(1,1<<(len(p)-25)) for p,typ in leaves if typ=='X26')
    print('   root',''.join(map(str,root[13:])),'X weight',xw,'leaves',len(leaves),Counter(t for _,t in leaves))
# ---------- GC1140 (4): real-cone Monte Carlo, no certificate ----------
LOG2N=int(sys.argv[1]) if len(sys.argv)>1 else 22   # the CL334 run used 24
N=1<<LOG2N; M=N//64; ONES=np.uint64(0xFFFFFFFFFFFFFFFF); rng=np.random.default_rng(1140)
def pc(m): return int(np.bitwise_count(m).sum())
def match(cells,pattern,mask):
    m=mask.copy()
    for i,b in enumerate(pattern): m&= cells[i] if b else ~cells[i]
    return m
def mixed_mask(cells,mask):
    base=match(cells,B('111001'),mask); m=np.zeros(M,dtype=np.uint64)
    for w in CORE: m|=match(cells[6:],w,base)
    m|=match(cells,J[0],mask); m|=match(cells,J[1],mask); return m
def gB_mask(cells,mask):
    m=match(cells,B('1110100110'),mask); return m&(cells[10]|~cells[11])
tot=Counter()
for root in roots:
    cells=[np.full(M,ONES if b else 0,dtype=np.uint64) for b in root]+[rng.integers(0,2**64,size=M,dtype=np.uint64,
        endpoint=False) for _ in range(67-25)]
    rem=np.full(M,ONES,dtype=np.uint64); got={}; pair=None
    for t in range(53):
        if t==16: pair=(cells[13].copy(),cells[14].copy())
        if t==26:
            x=cells[9]&cells[10]&rem; got['X26']=x; rem&=~x
            got['X26 pair01']=x&~pair[0]&pair[1]
        if t==36:
            c=mixed_mask(cells,rem); got['core36']=c; rem&=~c
        if t==46:
            g=gB_mask(cells,rem); got['B46']=g; rem&=~g
        if t==52:
            c=mixed_mask(cells,rem); got['core52']=c; rem&=~c; got['UNCOVERED']=rem.copy()
            adm=got['core36']|got['B46']|got['core52']; got['admission pair11']=adm&pair[0]&pair[1]
            got['admission']=adm
        if t==52: break
        wall=np.full(M,ONES if t%2 else 0,dtype=np.uint64)
        cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
    for k,v in got.items(): tot[k]+=pc(v)
print('GC1140 real cones, 12 x 2^%d:'%LOG2N,{k:tot[k] for k in ('X26','core36','B46','core52','UNCOVERED')},
      '| X with pair 01:',tot['X26 pair01'],'of',tot['X26'],
      '| admission with pair 11:',tot['admission pair11'],'of',tot['admission'])
print('done %.0fs'%(time.time()-t0))
