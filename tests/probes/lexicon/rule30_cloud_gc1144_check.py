#!/usr/bin/env python3
"""rule30_cloud_gc1144_check.py: Cloud's independent second read of GPT's GC1144 (the CL335 pin 1110011110100 has an
all-length white-A / B exit guard on its first short block), with the width-20 carrier rebuilt from Cloud's own strip
machinery and the exit dispatch checked directly on real completions (CL341).

RUN-ON:     cpu (Python 3 standard library; about a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1144_check.py

WHAT. The 20-cell strip with cell 21 free (every actual projection is included): the 128 packets extending the pin, the H
flow (site-5 track 0101101010) to its endpoints, the SS entrants (first nine cells a white SS entrance or a black-marker
S), the least fixed point of the SS flow (site-5 track 111010) with its states, edges and sha256 digest, the terminals by
class (black-eleventh A, guarded or bad B, white-A with white or black 13th cell, white-A whose sites 14..19 are GC1141
high words), topological elimination, the minimal SS depth of each exit class, GPT's shortest black-A counter path and
the four actual 70-cell projection controls. Beyond GPT: every white-A terminal is run 16 ticks over all 2^5 completions
of its 20 cells and every B terminal 6 ticks over all 2^6, so the exit dispatch is checked without GC1141, GC1090 or
GC1087 as premises; and the real chain of CL335 (white SS entrances 1110100001100 / 1110100000110 at 94, 1110100001111
at 100, A rows 1110100011011 / 1110100011010 at 106) is looked for in the exact-depth layers.

PREDICTIONS (written before the run, in Cloud's scratch): (1) the counts reproduce (128, 161 = 87 + 74, 519 states, 1530
edges, 267 = 66 + 172 + 29, GPT's digest 09e5e649...) (0.8); (2) every white-A terminal gives a C core at +16 for all
completions (0.8) and every B terminal is mixed-admitted at +6 for all completions (0.6); (3) the real chain's rows are in
the carrier at SS depth 5 (0.7); (4) 214 vertices survive elimination (0.7). Counterfactual: a white-A terminal in the
high words or a bad B refutes GC1144. Unexpected check: the SS depth at which each exit class first appears.

RESULT (CL341): all four held. White-A terminals: 22 give C010 and 7 give C100 at +16 for every completion; B terminals:
all 172 (105 with a white tenth cell, 67 black) are mixed-admitted at +6 for every completion. First exits: black A after
2 SS, guarded B after 3, white A after 4; the real chain's prefixes sit at exact depths 3, 4 and 5 (the relaxation also
admits the A rows at depths 4 and 6, which the real cones of CL332 do not realise at tick 100).
"""
import itertools, hashlib
from collections import Counter, deque
B=lambda s: tuple(int(c) for c in s)
W=20
def imgs(row,t):
    out=set()
    for b in (0,1):
        s=(t%2,)+tuple(row)+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out
def flow(states,track):
    cur=set(states)
    for t,b in enumerate(track):
        nxt=set()
        for r in cur:
            if r[4]!=b: continue
            nxt|=imgs(r,t)
        cur=nxt
    return cur
H=B('0101101010'); SS=B('111010')
WHITE_SS={B('11101'+w) for w in ('0000','0100','0101','0110','0111')}
SS_TYPES=WHITE_SS|{B('111011101'),B('111011110'),B('111011111')}
HIGH={'010001','010010','010011','011010','011011','011100','100001','100100','100101','100110','100111'}
fmt=lambda r: ''.join(map(str,r)); pack=lambda r: sum(b<<j for j,b in enumerate(r))
def classify(r):
    s=fmt(r)
    if s[:9]=='111010001':
        if s[10]=='1': return 'black_A'
        if s[12]=='0': return 'white_A_white13'
        if s[13:19] in HIGH: return 'white_A_high111'
        return 'white_A_C16'
    if s[:9]=='111010011':
        return 'bad_B' if (s[9]=='0' and s[10]=='0' and s[11]=='1') else 'guarded_B'
    return s[:9]
pin=B('1110011110100')
starts={pin+u for u in itertools.product((0,1),repeat=7)}
ends=flow(starts,H)
ent={r for r in ends if r[:9] in SS_TYPES}
print('starts',len(starts),'H ends',len(ends),'SS entrants',len(ent),'non-SS H ends',
    dict(Counter(classify(r) for r in ends-ent)))
graph={}; depth={r:0 for r in ent}; todo=deque(sorted(ent,key=pack)); terms={}
while todo:
    a=todo.popleft(); out=flow({a},SS)
    graph[a]={z for z in out if z[:9] in SS_TYPES}
    for z in out:
        if z[:9] in SS_TYPES:
            if z not in depth: depth[z]=depth[a]+1; todo.append(z)
        else:
            if z not in terms: terms[z]=depth[a]+1
allout=flow(set(graph),SS)
assert {z for z in allout if z[:9] in SS_TYPES}<=set(graph) and allout-set(graph)==set(terms)
digest=hashlib.sha256(''.join(fmt(z)+'\n' for z in sorted(graph,key=pack)).encode()).hexdigest()
cnt=Counter(classify(z) for z in terms)
print('SS states',len(graph),'SS edges',sum(map(len,graph.values())),'terminals',len(terms),dict(cnt))
print('digest',digest,'(GPT 09e5e64944f334f13b032a3249bed3e1f96f51d514e8157f8d012aabfb8f89b1)')
wa=[z for z in terms if classify(z).startswith('white_A')]
print('white-A terminals all begin 111010001101:',all(fmt(z)[:12]=='111010001101' for z in wa),'| 13th cell split',
    Counter(fmt(z)[12] for z in wa),
      '| any in HIGH:',any(classify(z)=='white_A_high111' for z in wa),'| any bad B:',any(classify(z)=='bad_B' for z in terms))
# topological elimination
indeg={a:0 for a in graph}
for out in graph.values():
    for z in out: indeg[z]+=1
q=deque(a for a,n in indeg.items() if n==0); removed=0
while q:
    a=q.popleft(); removed+=1
    for z in graph[a]:
        indeg[z]-=1
        if indeg[z]==0: q.append(z)
print('vertices surviving topological elimination:',len(graph)-removed,'(GPT 214)')
# depth of first appearance per exit type (SS blocks after the H block)
first={}
for z,d in terms.items():
    c=classify(z); first[c]=min(first.get(c,99),d)
print('first SS depth per exit type:',first,'| depth distribution of white-A terminals:',
    sorted(Counter(terms[z] for z in wa).items()))
print('real-chain prefixes among terminals: 1110100011011',sum(1 for z in wa if fmt(z)[:13]=='1110100011011'),
    '| 1110100011010',sum(1 for z in wa if fmt(z)[:13]=='1110100011010'),
      '| depths of those', sorted(Counter(terms[z] for z in wa if fmt(z)[:13] in ('1110100011011',
          '1110100011010')).items()))
# direct dispatch checks (real cones from the 20-cell terminal rows, even start)
def fwd(x,left):
    f=[left]+list(x); return tuple(f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1))
def run(start,n):
    rows=[tuple(start)]
    for t in range(n): rows.append(fwd(rows[-1],t%2))
    return rows
CORE={B('010'),B('011'),B('100')}; J=(B('111001101100'),B('11100110111110'))
def mixed_long(row): return row[:6]==B('111001') and (row[6:9] in CORE or row[:12]==J[0] or row[:14]==J[1])
okA=Counter()
for z in wa:
    res=set()
    for ext in itertools.product((0,1),repeat=5):
        r=run(z+ext,16)[16]; res.add(fmt(r[:9]))
    okA[tuple(sorted(res))]+=1
print('white-A terminals, first 9 cells at +16 over all 2^5 completions:',dict(okA))
okB=Counter()
for z in terms:
    if classify(z) in ('guarded_B','bad_B'):
        res=set()
        for ext in itertools.product((0,1),repeat=6):
            r=run(z+ext,6)[6]; res.add(mixed_long(r))
        okB[('black10' if z[9]==1 else 'white10',tuple(sorted(res)))]+=1
print('B terminals, mixed admission at +6 over all 2^6 completions:',dict(okB))
# GPT's shortest counter path
src=B('11100111101001100110'); e1=B('11101110100101111110'); e2=B('11101111111011001000'); e3=B('11101000111111110000')
print('counter: start in starts',src in starts,'| H end reached',e1 in flow({src},H),'| SS step',e2 in flow({e1},SS),
    '| SS step to black A',e3 in flow({e2},SS),classify(e3))
# four actual projections
ok=True
for pat in ((0,),(1,),(0,1),(1,0)):
    source=pin+tuple(pat[j%len(pat)] for j in range(57)); rows=run(source,40)
    ok&= rows[0][:20] in starts and rows[10][:20] in ends
    for t in range(40): ok&= rows[t+1][:20] in imgs(rows[t][:20],t)
print('four actual 70-cell projection controls:',ok)
