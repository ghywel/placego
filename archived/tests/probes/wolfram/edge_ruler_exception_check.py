#!/usr/bin/env python3
"""GC2204: one fixed actual-root prefix, independent period and block readers.
Prediction and caps are frozen in reports/GPT-OVERNIGHT-20261029.md.
No random seeds, fitting, horizon expansion or infinite conclusion.
"""
import json, os
from pathlib import Path
DEPTH=24
T=65536
mask=(1<<(DEPTH+1))-1
row=1
rows=[]
for t in range(T):
    rows.append(row)
    row=(row ^ ((row<<1)|(row<<2))) & mask
assert row==1, 'fixed horizon does not close the actual prefix; stop, no widening'
# The exact prefix return proves all later repetition because this map is triangular.
periods=[]
for j in range(DEPTH+1):
    mj=(1<<(j+1))-1
    p=next(t for t in range(1,T+1) if (rows[t%T]&mj)==1)
    assert p & (p-1)==0
    periods.append(p)
# Independent least-period reader: each temporal column, tested by dyadic halving.
# Taking the LCM of the columns gives a prefix period without using first returns.
check=[]
prefix=1
for j in range(DEPTH+1):
    p=T
    while p>1:
        h=p//2
        if any(((rows[t]^rows[t+h])>>j)&1 for t in range(h)):
            break
        p=h
    prefix=max(prefix,p)
    check.append(prefix)
assert periods==check
E=[p.bit_length()-1 for p in periods]
x=[None]+[E[j]-E[j-1] for j in range(1,DEPTH+1)]
assert set(x[1:]) <= {0,1}
# Direct substring reader, with the closing pair wholly within the retained prefix.
direct=[]
for s in range(1,DEPTH):
    for m in range(1,DEPTH):
        w=[1]+[1,0]*m+[1,1]
        if s+len(w)-1<=DEPTH and x[s:s+len(w)]==w:
            q=periods[s-1]
            assert m+1==q, (s,m,q)
            direct.append((s,s+2*m+1,E[s-1],m))
# Independent reader: consecutive starts of 11 with no other equal adjacent pair between.
pairs=[s for s in range(1,DEPTH) if x[s:s+2]==[1,1]]
parsed=[]
for s,u in zip(pairs,pairs[1:]):
    if all(x[k]!=x[k+1] for k in range(s+1,u)):
        assert (u-s)%2==1 and u-s>=3
        m=(u-s-1)//2
        assert periods[s-1]==m+1
        parsed.append((s,u,E[s-1],m))
assert direct==parsed
assert (3,6,1,1) in direct, 'known universal-start control'
for a,b in zip(direct,direct[1:]):
    assert b[0]>=a[1]
    assert b[2]>=a[2]+(1<<a[2])
# Theoretical negative control: a word can satisfy local 111/11011 exclusions yet
# violate the longer guarded closure. Check the actual seven-symbol antecedent.
assert [1]+[1,0]*2+[1,1]==[1,1,0,1,0,1,1]
result=dict(status='PASS',depth=DEPTH,ticks=T,prefix_return=row,periods=periods,
            flags=''.join(map(str,x[1:])),closures=direct,
            readers='first-prefix-return vs column-halving; substrings vs consecutive-11 parse',
            scope='finite actual-root control; no infinite proof or density fit')
out=Path(os.environ['CAPPED_OUT'])/'result.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
