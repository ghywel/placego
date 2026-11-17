#!/usr/bin/env python3
"""rule30_cloud_actual_carrier.py: the width-20 SS carrier (GC1144 / GC1145 style, Cloud's machinery) started from the
ACTUAL tick-16 images of white-A origins instead of free packets (CL346): all 2^23 completions of 1110100011011 give
198 distinct 20-cell rows at tick 16, 38 of them high-111 (29 with the non-LL image 1110011111110, 9 with the LL
image 1110011111000); the H flow, the SS least fixed point and the terminals by class from each set.

RUN-ON:     cpu (Python 3 standard library plus numpy; under a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_actual_carrier.py

PREDICTION (written before the run): no bad-B terminal from the 29 actual non-LL rows (0.5). RESULT (CL346): refuted in
the relaxation, 13 bad-B terminals at SS depth 3 (614 states, 1,377 edges, 459 terminals: 68 black A, 349 guarded B, 13
bad B, 12 + 17 white A); the 9 LL rows end H in the low row 111001001 with no SS entrant. The lift probe then shows one
of the 13 is real.
"""
import itertools, numpy as np
from collections import Counter, deque
B=lambda s: tuple(int(c) for c in s)
W=20; H=B('0101101010'); SS=B('111010')
WHITE_SS={B('11101'+w) for w in ('0000','0100','0101','0110','0111')}
SS_TYPES=WHITE_SS|{B('111011101'),B('111011110'),B('111011111')}
HIGH={'010001','010010','010011','011010','011011','011100','100001','100100','100101','100110','100111'}
fmt=lambda r: ''.join(map(str,r))
def imgs(row,t):
    out=set()
    for b in (0,1):
        s=(t%2,)+tuple(row)+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out
def flow(states,track,t0=0):
    cur=set(states)
    for k,b in enumerate(track):
        nxt=set()
        for r in cur:
            if r[4]!=b: continue
            nxt|=imgs(r,t0+k)
        cur=nxt
    return cur
def classify(r):
    s=fmt(r)
    if s[:9]=='111010001':
        if s[10]=='1': return 'black_A'
        if s[12]=='0': return 'white_A_white13'
        if s[13:19] in HIGH: return 'white_A_high111'
        return 'white_A_C16'
    if s[:9]=='111010011': return 'bad_B' if (s[9]=='0' and s[10]=='0' and s[11]=='1') else 'guarded_B'
    return s[:9]
# the actual images: all 2^23 completions of a white-A origin, 20 cells at tick 16
WA=B('1110100011011'); NB=23; N=1<<NB; idx=np.arange(N,dtype=np.int64)
cells=[np.full(N,b,dtype=np.uint8) for b in WA]+[((idx>>k)&1).astype(np.uint8) for k in range(NB)]
for t in range(16):
    wall=np.full(N,t%2,dtype=np.uint8)
    cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
w20=np.zeros(N,dtype=np.int64)
for i in range(20): w20|=cells[i].astype(np.int64)<<i
rows={tuple((int(v)>>i)&1 for i in range(20)) for v in set(w20.tolist())}
high=[r for r in rows if r[:9]==B('111001111')]
nonLL=[r for r in high if r[:13]==B('1110011111110')]; LL=[r for r in high if r[:13]==B('1110011111000')]
print('actual tick-16 rows of white-A origins:',len(rows),'| high-111 rows:',len(high),'| non-LL image rows',
    len(nonLL),'| LL image rows',len(LL),'| other high rows',len(high)-len(nonLL)-len(LL))
for label,starts in (('29 actual non-LL rows',nonLL),('9 actual LL rows',LL)):
    ends=flow(starts,H,16)
    ent={r for r in ends if r[:9] in SS_TYPES}
    graph={}; depth={r:0 for r in ent}; todo=deque(sorted(ent,key=fmt)); terms={}
    while todo:
        a=todo.popleft(); out=flow({a},SS,26+6*depth[a])
        graph[a]={z for z in out if z[:9] in SS_TYPES}
        for z in out:
            if z[:9] in SS_TYPES:
                if z not in depth: depth[z]=depth[a]+1; todo.append(z)
            elif z not in terms: terms[z]=depth[a]+1
    cnt=Counter(classify(z) for z in terms); first={}
    for z,d in terms.items(): c=classify(z); first[c]=min(first.get(c,99),d)
    print(label,'| H ends',len(ends),'| SS entrants',len(ent),'| non-SS H ends',
        dict(Counter(classify(r) for r in ends-ent)),
          '| SS states',len(graph),'edges',sum(map(len,
              graph.values())),'| terminals',len(terms),dict(cnt),'| first SS depth per class',first)
    bad=[z for z in terms if classify(z)=='bad_B']
    if bad: print('   bad-B terminals:',[fmt(z) for z in bad][:6],'at depths',
        sorted(Counter(terms[z] for z in bad).items()))
