#!/usr/bin/env python3
"""(1) Inequality check: D(P,Q) >= n * E_{PxQ}[1/r2(N(p-q))] for lattice families (square lattice, r2 = full count).
(2) Unexpected check: alternating regular 2n-gon (x = even vertices, y = odd vertices) vs lattice half-shift family."""
import math, time
import numpy as np
T0=time.time()
def r2full(X):
    a=np.arange(-int(math.isqrt(X)),int(math.isqrt(X))+1); A,B=np.meshgrid(a,a,indexing='ij'); N=(A*A+B*B).ravel(); N=N[N<=X]
    r=np.zeros(X+1,np.int64); np.add.at(r,N,1); return r
def npts(n, s, sh):
    R=int(math.sqrt(n)*1.3+5)*s; a=np.arange(-R,R+1); A,B=np.meshgrid(a,a,indexing='ij'); A=A.ravel(); B=B.ravel()
    m=((A-sh[0])%s==0)&((B-sh[1])%s==0); A=A[m]; B=B[m]; N=A*A+B*B; o=np.lexsort((np.arctan2(B,A),N))[:n]; return A[o],B[o]
print('(1) inequality D >= n*E[1/r2]  (square lattice P=Q, and half-shift scaled by 2 so r2 of the scaled norm)')
for n in [100,400,1600]:
    for name,s,sh in [('P=Q',1,(0,0)),('half-shift',2,(1,1))]:
        PA,PB=npts(n,s,(0,0)); QA,QB=npts(n,s,sh)
        Nz=(PA[:,None]-QA[None,:])**2+(PB[:,None]-QB[None,:])**2
        r=r2full(int(Nz.max())+1)
        rr=r[Nz].astype(float); rr[Nz==0]=1.0
        lb=n*np.mean(1.0/rr); D=len(np.unique(Nz))
        print(f'  n={n:5d} {name:10s} D={D:5d}  n*E[1/r2]={lb:8.1f}  ratio D/lb={D/lb:.3f}')
print('(2) alternating regular 2n-gon: D = #distinct chord lengths for odd steps; vs lattice half-shift D')
for n in [2,3,4,5,6,8,10,12,16,20,24,32,40,48,64,96,128]:
    th=2*np.pi*np.arange(2*n)/(2*n); X=np.exp(1j*th[0::2]); Y=np.exp(1j*th[1::2])
    d=np.abs(X[:,None]-Y[None,:]).ravel(); Dpoly=len(np.unique(np.round(d,9)))
    PA,PB=npts(n,2,(0,0)); QA,QB=npts(n,2,(1,1)); Dlat=len(np.unique((PA[:,None]-QA[None,:])**2+(PB[:,None]-QB[None,:])**2))
    PA,PB=npts(n,1,(0,0)); Dsame=len(np.unique((PA[:,None]-PA[None,:])**2+(PB[:,None]-PB[None,:])**2))
    print(f'  n={n:4d}  polygon D={Dpoly:4d}   square half-shift D={Dlat:4d}   square P=Q (with 0) D={Dsame:4d}')
print('time',round(time.time()-T0,1))
