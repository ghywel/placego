#!/usr/bin/env python3
"""GC2807 fixed S06 review controls; literal finite cones, no producer imports/ANF library.
Record searched: XP1.1/SKM-XP1.1/SKG5, Berzai d9cb3d57, kit03a19bf6.
Prediction: kit-phase top parity n%2 and omitted-f1 coefficient (n+1)%2;
other phase has odd top parity. Alternating physical wall is masked in the
other phase, but incorrectly attaching it to the kit phase kills that parity.
S_2n(2n)=2^n-wt(C_n) by independent literal-row enumeration for n<=6.
Counterfactual: any mismatch blocks the corresponding carry; diagnose, no retry/enlargement.
Controls: literal tuple triangle, finite rows, phase swap, checksum n1 exception,
finite row5 outside the finite image. Fixed n<=12, literal-triangle n<=5, width<=12.
"""
import json,time,resource
from itertools import product


def cell_triangle(a, wall, depth):
    prev=list(wall)
    cur=list(a)
    for k in range(2,depth+1):
        new=[cur[t+1] ^ (cur[t] | prev[t]) for t in range(len(cur)-1)]
        prev,cur=cur,new
    return cur[0]


def packed(a,wall,depth):
    cur=sum(b<<t for t,b in enumerate(a));prev=sum(b<<t for t,b in enumerate(wall))
    for k in range(2,depth+1):
        prev,cur=cur,((cur>>1) ^ (cur | prev)) & ((1<<(len(a)-k+1))-1)
    return cur&1


def table(n,phase,physical=False):
    depth=2*n+1 if phase=='kit' else 2*n
    values=[]
    for bits in range(1<<n):
        a=[(1 if t%2==0 else (bits>>(t//2))&1) if phase=='kit'
           else ((bits>>(t//2))&1 if t%2==0 else 1) for t in range(depth)]
        wall=[t%2 if physical else 0 for t in range(depth)]
        v=packed(a,wall,depth)
        if n<=5:assert v==cell_triangle(a,wall,depth)
        values.append(v)
    return values


def step(y):
    return (y>>1) ^ (y | (y<<1))


def survivors(n):
    count=0
    for y in range(1<<(2*n)):
        z=y;ok=True
        for t in range(2*n+1):
            if t%2==0 and not (z&1):ok=False;break
            z=step(z)
        count+=ok
    return count


def literal_step(y):
    row=[0]+[(y>>i)&1 for i in range(y.bit_length())]+[0,0]
    new=[row[k+1] ^ (row[k] | row[k-1]) for k in range(1,len(row)-1)]
    return sum(b<<i for i,b in enumerate(new))

start=time.process_time();rows=[]
for n in range(1,13):
    k=table(n,'kit');b=table(n,'other');physical_b=table(n,'other',True);wrong_k=table(n,'kit',True)
    assert b==physical_b
    assert sum(k)%2==n%2 and sum(b)%2==1
    assert sum(wrong_k)%2==0
    omitted=sum(v for i,v in enumerate(k) if not (i&2))%2 if n>=2 else None
    if n>=2:assert omitted==(n+1)%2
    walsh=(1<<n)-2*sum(k)
    if n>=2:assert walsh%4==2*(n%2)
    else:assert walsh==0  # refutes the unguarded original wording
    s=survivors(n) if n<=6 else None
    if s is not None:assert s==(1<<n)-sum(k)
    rows.append({'n':n,'kit_weight':sum(k),'other_weight':sum(b),'omitted_f1':omitted,'survivors':s,'walsh':walsh})
for y in range(64):assert step(y)==literal_step(y)
# F of every finite nonzero exact-width2 row has width3; neither parent gives5.
assert 5 not in [step(2),step(3)]
assert 5&1 and step(step(5))&1
assert any(sum(table(2,p))%2 != sum(table(2,q))%2 for p,q in [('kit','other')])
print(json.dumps({'PASS':True,'rows':rows,'controls':'literal cone/row oracle; physical phase mask; bad clock; n1 Walsh guard; finite row5 not in finite image','cpu_seconds':time.process_time()-start,'self_peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}))
print('S06 READ CONTROLS PASS')
