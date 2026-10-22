#!/usr/bin/env python3
"""One centre vs a lattice disk: how few circles (norm values m <= X, ranked by r2(m) descending) cover a fraction
phi of the lattice points z with N(z) <= X?  Heuristic prediction: phi -> 1 needs only X/(log X)^{ln 2 + o(1)} circles,
versus all ~K X/sqrt(log X) representable values. Also the pair-correlation of omega_1(N(p-q1)), omega_1(N(p-q2))."""
import math, time, sys
import numpy as np
T0=time.time()
for X in [10**4, 10**5, 10**6, 4*10**6, 16*10**6]:
    if time.time()-T0>300: print('TIME LIMIT'); break
    r=np.zeros(X+1,np.int64); s=int(math.isqrt(X))
    for a in range(-s,s+1):
        b=np.arange(-int(math.isqrt(X-a*a)),int(math.isqrt(X-a*a))+1); np.add.at(r,a*a+b*b,1)
    r[0]=0
    vals=r[r>0]; tot=vals.sum(); nv=len(vals)
    srt=np.sort(vals)[::-1]; cum=np.cumsum(srt)/tot
    out=[]
    for phi in [0.5,0.9,0.99]:
        k=int(np.searchsorted(cum,phi))+1; out.append(f'phi={phi}: {k} circles = {k/nv:.3f} of values')
    LR=0.7642*X/math.sqrt(math.log(X))
    print(f'X={X:9d} points={tot:9d} values={nv:8d} (LR approx {LR:.0f}) | '+' | '.join(out)+
          f' | X/(lnX)^ln2={X/math.log(X)**math.log(2):.0f}', flush=True)
print('time',round(time.time()-T0,1))
