#!/usr/bin/env python3
"""graph_node.py (Local, L1556): a test of the Markov reading that flow conservation cannot pass for it. For each node with enough held-out visits, the share of visits whose excursion goes on to reach depth T, against the Markov value from the fitted half. Reports chi-square per node, and the worst nodes. Peak counts alone are a flow across a cut and have no power."""
import numpy as np,collections,sys
import scipy.sparse as sp, scipy.sparse.linalg as sl
stem=sys.argv[1] if len(sys.argv)>1 else 'graph_data2/g'
Ks=[int(k) for k in sys.argv[2].split(',')] if len(sys.argv)>2 else [112,120,128,136,144]
def load(K):
    ids=np.fromfile(f'{stem}.{K}.ids',dtype=np.uint32)
    dep={}
    for l in open(f'{stem}.{K}.nodes'):
        a=l.split(); dep[int(a[0])]=int(a[1])
    return ids,dep
def exc(ids):
    z=np.flatnonzero(ids==0);o=[];p=0
    for e in z: o.append(ids[p:e].tolist()); p=e+1
    return o
def trans(ex):
    c=collections.defaultdict(collections.Counter)
    for x in ex:
        for a,b in zip(x,x[1:]+[0]): c[a][b]+=1
    return c
def hit(c,dep,T):
    nodes=[v for v in c if dep.get(v,0)<T]; ix={v:i for i,v in enumerate(nodes)}; n=len(nodes)
    r=[];q=[];w=[];b=np.zeros(n)
    for v in nodes:
        t=sum(c[v].values()); i=ix[v]
        for y,cn in c[v].items():
            if y==0: continue
            if dep.get(y,0)>=T: b[i]+=cn/t
            elif y in ix: r.append(i);q.append(ix[y]);w.append(cn/t)
    A=sp.csr_matrix((w,(r,q)),shape=(n,n))
    h=sl.spsolve((sp.identity(n,format='csc')-A.tocsc()*(1-1e-9)),b)
    return {v:h[ix[v]] for v in nodes}
for K in Ks:
    ids,dep=load(K); ex=exc(ids); hf=len(ex)//2; tr,te=ex[:hf],ex[hf:]
    c=trans(tr)
    for T in [t for t in (110,120,125,130,135) if t<=K]:
        h=hit(c,dep,T)
        n=collections.Counter(); m=collections.Counter()
        for x in te:
            last=-1
            for i,v in enumerate(x):
                if dep.get(v,0)>=T: last=i
            for i,v in enumerate(x):
                if dep.get(v,0)<T:
                    n[v]+=1
                    if i<last: m[v]+=1
        chi=0;dof=0;rows=[]
        for v,nv in n.items():
            hv=h.get(v)
            if hv is None: continue
            e=nv*hv
            if e<5 and m[v]<5: continue
            var=max(e*(1-hv),1.0)
            z=(m[v]-e)/var**.5
            chi+=z*z;dof+=1
            rows.append((abs(z),z,dep[v],nv,m[v],round(e,1)))
        rows.sort(reverse=True)
        print(f'K={K} T={T}: nodes tested {dof}, chi-square per node {chi/max(dof,1):.2f}; worst (z, depth, visits, hits, Markov):',[(round(z,1),d,nv,mv,e) for _,z,d,nv,mv,e in rows[:4]])
