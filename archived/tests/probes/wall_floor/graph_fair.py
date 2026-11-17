#!/usr/bin/env python3
"""graph_fair.py (Local, L1556): are the cells below the top-K word fair? For each word the sweep has four possible states at its foot, so a fair law gives each successor a multiple of 1/4. Compares that with the chain's measured transition law at K = 128."""
import numpy as np,collections,sys
K=int(sys.argv[1]) if len(sys.argv)>1 else 128
ref=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
ids=np.fromfile(f'graph_data/g.{K}.ids',dtype=np.uint32)
word={};dep={}
for l in open(f'graph_data/g.{K}.nodes'):
    a=l.split(); word[a[3]]=int(a[0]); dep[int(a[0])]=int(a[1])
inv={v:k for k,v in word.items()}
c=collections.defaultdict(collections.Counter)
a=ids[:-1].tolist();b=ids[1:].tolist()
for x,y in zip(a,b):
    if x: c[x][y]+=1
def depth(r):
    best=0
    for x in ref:
        k=0
        while k<len(r) and k<len(x) and (x[k]=='?' or x[k]==r[k]): k+=1
        best=max(best,k)
    return best
def succ(w,s):
    """w top first, offsets 0..K-1. Returns the new top-K word under foot state s."""
    old={j:(1 if w[j]=='#' else 0) for j in range(K)}
    t=old[0]
    for j in range(-1,-8,-1):
        t^=1; old[j]=t
    p1,p2=s
    new={K+3:p1,K+4:p2}
    for j in range(K-1,-4,-1):
        z=old[j]^(new[j+4]|new[j+5])
        new[j+3]=z
    return ''.join('#' if new[j] else '.' for j in range(K))
tv=0;wt=0;rows=[]
single_fair=0
for v,d in c.items():
    n=sum(d.values())
    w=inv[v]
    fair=collections.Counter()
    for s in ((0,0),(0,1),(1,0),(1,1)):
        x=succ(w,s)
        if depth(x)<100: fair[0]+=.25
        else: fair[word.get(x,-1)]+=.25
    keys=set(fair)|set(d)
    t=.5*sum(abs(fair.get(k,0)-d.get(k,0)/n) for k in keys)
    tv+=t*n;wt+=n
    rows.append((n,t,dep[v],sorted((round(x/n,3) for x in d.values()),reverse=True),sorted(fair.values(),reverse=True)))
print('K',K,'visits',wt,'mean total variation between measured and fair successors',round(tv/wt,4))
rows.sort(reverse=True)
for r in rows[:24]: print(r)
b=[r for r in rows if len(r[3])>1]
vals=collections.Counter()
for n,t,dd,m,f in b:
    for p in m: vals[round(p*16)/16]+=n*p
tot=sum(vals.values())
print('measured branch probabilities, nearest 1/16, by weight:',[(k,round(v/tot,3)) for k,v in sorted(vals.items())])
