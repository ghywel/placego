#!/usr/bin/env python3
"""graph_test.py (Local, L1556): tests the Markov reading of the chain's top cells. Reads the id streams of wall_graph (0 marks leaving depth DMIN), splits them in time, fits on the first half and scores on the second.
For each K: nodes, share of visits with one successor, held-out cross-entropy of order 1 and order 2 per tick, and predicted against observed excursions reaching a depth."""
import numpy as np,collections,math,sys
stem='graph_data/g'
def load(K):
    ids=np.fromfile(f'{stem}.{K}.ids',dtype=np.uint32)
    dep={}
    for l in open(f'{stem}.{K}.nodes'):
        a=l.split()
        dep[int(a[0])]=int(a[1])
    return ids,dep
def split_exc(ids):
    z=np.flatnonzero(ids==0)
    out=[];p=0
    for e in z:
        out.append(ids[p:e]); p=e+1
    return out
def fit(exs,order):
    c=collections.defaultdict(collections.Counter)
    for x in exs:
        x=x.tolist()+[0]
        for i in range(len(x)-1):
            key=x[i] if order==1 else ((x[i-1] if i>0 else -1),x[i])
            c[key][x[i+1]]+=1
    return c
def xent(exs,c1,c2=None,alpha=0.1,nout=8):
    tot=0.0;n=0;bra=0.0;nb=0
    t1={k:sum(v.values()) for k,v in c1.items()}
    t2={k:sum(v.values()) for k,v in c2.items()} if c2 else None
    for x in exs:
        x=x.tolist()+[0]
        for i in range(len(x)-1):
            cur=x[i];nx=x[i+1]
            d1=c1.get(cur)
            p1=((d1.get(nx,0)+alpha)/(t1[cur]+alpha*nout)) if d1 else 1.0/nout
            p=p1
            if c2 is not None:
                key=((x[i-1] if i>0 else -1),cur)
                d2=c2.get(key)
                if d2:
                    # back off to order 1 through the prior
                    p=(d2.get(nx,0)+1.0*p1)/(t2[key]+1.0)
            l=-math.log2(p)
            tot+=l;n+=1
            if d1 and len(d1)>1: bra+=l;nb+=1
    return tot/n,n,nb
def hit_prob(c1,dep,thr):
    nodes=list(c1.keys());ix={v:i for i,v in enumerate(nodes)}
    n=len(nodes)
    rows=[];cols=[];vals=[];b=np.zeros(n)
    for v,d in c1.items():
        t=sum(d.values());i=ix[v]
        for w,cn in d.items():
            if w==0: continue
            if dep.get(w,0)>=thr: b[i]+=cn/t
            elif w in ix:
                rows.append(i);cols.append(ix[w]);vals.append(cn/t)
    import scipy.sparse as sp, scipy.sparse.linalg as sl
    A=sp.csr_matrix((vals,(rows,cols)),shape=(n,n))
    h=sl.spsolve((sp.identity(n,format='csc')-A.tocsc()*0.999999),b)
    return {v:h[ix[v]] for v in nodes}
for K in (128,160,192):
    ids,dep=load(K)
    ex=split_exc(ids)
    h=len(ex)//2
    tr,te=ex[:h],ex[h:]
    c1=fit(tr,1);c2=fit(tr,2)
    # shape
    vis=sum(sum(v.values()) for v in c1.values())
    single=sum(sum(v.values()) for v in c1.values() if len(v)==1)
    branch=sorted(((sum(v.values())-max(v.values()),k) for k,v in c1.items() if len(v)>1),reverse=True)
    tb=sum(b for b,_ in branch);acc=0;n99=0
    for b,_ in branch:
        acc+=b;n99+=1
        if acc>=0.99*tb: break
    x1,n,nb=xent(te,c1)
    x2,_,_=xent(te,c1,c2)
    print(f'K={K} excursions {len(ex)} nodes {len(dep)} train nodes {len(c1)} visits {vis} single-successor share {single/vis:.3f} branch nodes {len(branch)} carrying 99% of branching {n99}')
    print(f'   held-out bits per tick: order 1 {x1:.4f}, order 2 {x2:.4f}, gain {100*(x1-x2)/x1:.1f}%, ticks {n}, at branch nodes {nb}')
    # peak depth: predicted and observed on the held-out half
    thrs=[t for t in (105,110,115,120,125,130,135,140,145) if t<=K]
    entry=collections.Counter(int(x[0]) for x in te if len(x))
    nE=sum(entry.values())
    for thr in thrs:
        hp=hit_prob(c1,dep,thr)
        pred=sum(c*(1.0 if dep.get(v,0)>=thr else hp.get(v,0.0)) for v,c in entry.items())
        obs=sum(1 for x in te if len(x) and max(dep[int(v)] for v in np.unique(x))>=thr)
        print(f'   peak>={thr}: predicted {pred:9.1f} observed {obs:7d} ratio {pred/max(obs,1):.2f}')
