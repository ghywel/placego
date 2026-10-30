#!/usr/bin/env python3
"""GC2260 frozen finite controls: B1/F1, B4/F6, E1 and gate initialization.
One process/thread, no subprocesses. All output under CAPPED_OUT.
"""
import json, os, resource, time
from pathlib import Path
OUT=Path(os.environ['CAPPED_OUT'])
assert resource.getrlimit(resource.RLIMIT_CPU)==(120,120)
START=time.process_time()
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
    print(name, 'saved', flush=True)
def edge(x,n,gate):
    b=x<<1;s=x<<2;m=(1<<n)-1
    return (x ^ ((b|s) if gate=='OR' else (b&s)))&m
def literal(x,n,tt):
    return sum((((x>>j)&1)^((tt>>((2*((x>>(j-1))&1) if j else 0)+((x>>(j-2))&1 if j>1 else 0)))&1))<<j for j in range(n))
def period(x,n,tt):
    y=literal(x,n,tt);p=1
    while y!=x:
        y=literal(y,n,tt);p+=1
        assert p<=1<<n
    return p
# All16 small maps, direct bit truth table vs the historical prefix-clock initialization.
audit=[]
for tt in range(16):
    first=None;bad=0
    for a in range(1,64,2):
        L=1
        for j in range(1,6):
            x=a
            for _ in range(L):x=literal(x,6,tt)
            if ((x^a)>>j)&1:L*=2
            true=period(a&((1<<(j+1))-1),j+1,tt)
            if L!=true:
                bad+=1
                if first is None:first={'seed':a,'index':j,'reported_period':L,'actual_period':true}
    audit.append({'truth_table':tt,'mismatched_seed_depths':bad,'first':first})
assert next(a for a in audit if a['truth_table']==1)['first'] is not None
save('gate_initialization.json',audit)
# Each finite edge map is a permutation. Count each cycle once, then weight by length.
counts=[]
for n in range(1,22):
    row={'prefix_bits':n}
    for gate,tt in [('OR',14),('AND',8)]:
        N=1<<n;seen=bytearray(N);C={}
        if n<=7:
            for x in range(N):assert edge(x,n,gate)==literal(x,n,tt)
        for a in range(N):
            if seen[a]:continue
            x=a;p=0
            while not seen[x]:
                seen[x]=1;p+=1;x=edge(x,n,gate)
            assert x==a and p&(p-1)==0
            e=p.bit_length()-1;C[e]=C.get(e,0)+p
        assert sum(C.values())==N
        row[gate]=C
    counts.append(row)
assert counts[0]['OR']==counts[0]['AND']
assert counts[1]['OR']=={0:2,1:2} and counts[1]['AND']=={0:4}
save('edge_distributions.json',{'full_prefix':counts,'convention':'n bits means indices0..n-1. For n-bit seeds observed through index n with bit n initially0, take width n+1 counts /2: highest-bit complementation preserves period.'})
# Physical finite-parent image count and independently reconstructed criterion.
parents=[]
for w in range(1,13):
    images=set()
    if w>=3:
        m=w-2
        for p in range(1,1<<m):
            if p&1 and p>>(m-1):images.add((p<<2)^((p<<1)|p))
    selected=set()
    for y in range(1,1<<w):
        if not (y&1 and y>>(w-1)):continue
        a={w:0,w-1:0}
        for i in range(w-1,-1,-1):a[i-1]=((y>>i)&1)^(a[i]|a[i+1])
        if w>=2 and (y>>1)&1 and a.get(1,0)==1:selected.add(y)
    assert selected==images
    expected=0 if w<3 else (1 if w==3 else 1<<(w-4))
    assert len(images)==expected
    parents.append({'width':w,'count':len(images)})
save('finite_parent_counts.json',parents)
# First three failed even pins completely determine every one/two-release lifetime.
TMAX=100
def fails(r):
    out=[];x=r
    for t in range(TMAX+1):
        if t%2==0 and x&1==0:
            out.append(t)
            if len(out)==3:return tuple(out)
        x=(x>>1)^(x|(x<<1))
    raise AssertionError(('temporal_cap',r,out))
def literal_fails(r):
    a=[(r>>i)&1 for i in range(140)];out=[]
    for t in range(TMAX+1):
        if t%2==0 and a[0]==0:
            out.append(t)
            if len(out)==3:return tuple(out)
        a=[a[i+1]^(a[i]|(a[i-1] if i else 0)) for i in range(139)]+[0]
    raise AssertionError('literal cap')
for r in range(1,64):assert fails(r)==literal_fails(r)
assert fails(1)==(2,6,10)
D=[0]*23;one=[{} for _ in range(23)];two=[{} for _ in range(23)]
for r in range(1,1<<22):
    w=r.bit_length();a,b,c=fails(r)
    D[w]=max(D[w],a)
    if b>one[w].get(a,(-1,0))[0]:one[w][a]=(b,r)
    if c>two[w].get((a,b),(-1,0))[0]:two[w][a,b]=(c,r)
rows=[];O={};Q={};base=0
for w in range(1,23):
    base=max(base,D[w])
    for a,v in one[w].items():
        if v[0]>O.get(a,(-1,0))[0]:O[a]=v
    for ab,v in two[w].items():
        if v[0]>Q.get(ab,(-1,0))[0]:Q[ab]=v
    best1=max(v[0] for v in O.values());best2=max(v[0] for v in Q.values())
    times=[a for a,v in O.items() if v[0]==best1]
    pairs=[]
    for (a,b),(c,r) in Q.items():
        if c==best2:
            da=max(base,O.get(a,(0,0))[0]);db=max(base,O.get(b,(0,0))[0])
            pairs.append({'pins':[a,b],'seed':r,'life':c,'gain':c-base,'sum_single_gains':da+db-2*base})
    rows.append({'width':w,'perfect_life':base,'best_one':best1,'best_one_times':times,'best_two':best2,'best_pairs':pairs})
assert rows[0]['best_pairs'][0]['gain']!=rows[0]['best_pairs'][0]['sum_single_gains']
save('two_hiccups.json',{'rows':rows,'definition':'First white even time after ignoring the requested pin(s); all nonzero seeds of at most W bits; time0 releases allowed; no temporal cap reached.'})
save('summary.json',{'status':'PASS','payload_cpu_s':time.process_time()-START,'B1_max_prefix_bits':21,'B4_max_width':22,'E1_max_width':12,'no_rerun':True})
