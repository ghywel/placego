#!/usr/bin/env python3
"""Check the tensor 'volume' lemma: if P,Q subset Z[i]/M with M | N(p-q) for all pairs (M squarefree, split primes),
then |P||Q| <= M^2. Enumerate bicliques as closures Q=N(S), P=N(Q) from seeds S of size 1 and 2 (all pairs for M=5,13;
random pairs for M=65)."""
import itertools, random, time
import numpy as np
T0=time.time()
def run(M, allpairs=True, npairs=20000):
    a=np.arange(M); A,B=np.meshgrid(a,a,indexing='ij'); A=A.ravel(); B=B.ravel()   # residue a+bi mod M
    dA=(A[:,None]-A[None,:])%M; dB=(B[:,None]-B[None,:])%M
    ok=((dA*dA+dB*dB)%M==0)
    nres=M*M; best=0; bestbal=0; arg=None
    seeds=[(i,) for i in range(nres)]
    if allpairs: seeds+=list(itertools.combinations(range(nres),2))
    else:
        rnd=random.Random(1); seeds+=[tuple(rnd.sample(range(nres),2)) for _ in range(npairs)]
    for S in seeds:
        if time.time()-T0>400: break
        Q=np.all(ok[list(S),:],axis=0)
        if not Q.any(): continue
        P=np.all(ok[:,Q],axis=1)
        v=int(P.sum())*int(Q.sum())
        if v>best: best=v; arg=(int(P.sum()),int(Q.sum()))
        bestbal=max(bestbal,min(int(P.sum()),int(Q.sum())))
    print(f'M={M}: max volume found {best} (sizes {arg}); M^2={M*M}; max balanced side {bestbal} (M={M})', flush=True)
run(5); run(13); run(65, allpairs=False)
print('time', round(time.time()-T0,1))
