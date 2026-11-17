#!/usr/bin/env python3
"""spec_cols.py (Local, L1552): the corridor's cells at offsets 118 to 170 against the third lock's strip, tick by tick; and the witness's. A lower-case letter marks a cell that differs from the strip."""
import json,re
ref=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
S=[];cur=None
for l in open('spec_run/out.txt'):
    if l.startswith('SPEC'):
        cur=[];S.append(cur);continue
    m=re.match(r'(-?\d+) (\d+) (\d+) ([#.]+)$',l)
    if m and cur is not None: cur.append((int(m[1]),int(m[2]),int(m[3]),m[4]))
S=[s for s in S if len(s)==96]
LO,HI=118,172
print('offset ruler        ',''.join(str((k//10)%10) if k%10==0 else ' ' for k in range(LO,HI)))
def show(r,p):
    o=''
    for k in range(LO,HI):
        c=r[k]; x=ref[p][k] if k<len(ref[p]) else '?'
        if x=='?': o+={'#':'H','.':','}[c]
        elif c==x: o+=c
        else: o+={'#':'X','.':'o'}[c]
    return o
s0=S[0]
print('corridor, X and o differ from the strip, H and , are cells the strip leaves open')
for i in range(-13,9):
    r=next(q for q in s0 if q[0]==i)
    # phase by tick: continue the phase cycle from the hit (phase 2 at tick 0)
    p=(2+i)%6
    print(f'{i:4d} ph{p} best{r[2]}:{r[1]:3d}',show(r[3],p))
W=json.load(open('witness_tops.json'))
print('witness')
for k in range(21,5,-1):
    p=(1-k)%6
    print(f'{k:4d} ph{p}          ',show(W[str(k)],p))
