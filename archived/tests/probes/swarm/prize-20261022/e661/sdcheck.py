#!/usr/bin/env python3
"""Test the Selberg-Delange-type input of the single-centre bound:
   S_y(X) = sum_{m<=X} r2(m) y^{Omega_1(m)}  ~  c_y X (log X)^{y-1}   (Omega_1 = # split prime factors with multiplicity)
and the r2-weighted upper tail: (1/(pi X)) sum_{m<=X, Omega_1(m) >= lam + C sqrt(lam)} r2(m)  vs  exp(-C^2/2)-type decay."""
import math, time
import numpy as np
T0=time.time()
XM=16*10**6
r=np.zeros(XM+1,np.int64); s=int(math.isqrt(XM))
for a in range(-s,s+1):
    b=np.arange(-int(math.isqrt(XM-a*a)),int(math.isqrt(XM-a*a))+1); np.add.at(r,a*a+b*b,1)
r[0]=0
# Omega_1 sieve
sv=np.ones(XM+1,bool); sv[:2]=False
for i in range(2,int(math.isqrt(XM))+1):
    if sv[i]: sv[i*i::i]=False
primes=np.nonzero(sv)[0]; sp=primes[primes%4==1]
Om=np.zeros(XM+1,np.int16)
for p in sp:
    p=int(p); q=p
    while q<=XM:
        Om[q::q]+=1; q*=p
print('sieve done', round(time.time()-T0,1), flush=True)
for X in [10**5,10**6,4*10**6,16*10**6]:
    rr=r[1:X+1].astype(float); oo=Om[1:X+1].astype(float)
    lam=math.log(math.log(X))
    line=[f'X={X:9d} lam={lam:.3f}']
    for y in [1.5,2.0]:
        Sy=(rr*y**oo).sum(); line.append(f'S_{y}/(X(logX)^{y-1})={Sy/(X*math.log(X)**(y-1)):.3f}')
    tot=rr.sum()
    for C in [0.0,1.0,2.0]:
        k=lam+C*math.sqrt(lam); frac=rr[oo>=k].sum()/tot; line.append(f'tail(C={C})={frac:.3f}')
    print(' | '.join(line), flush=True)
print('time',round(time.time()-T0,1))
