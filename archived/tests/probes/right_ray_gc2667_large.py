#!/usr/bin/env python3
"""right_ray_gc2667_large.py (Local, L1518): GC2667's window test at larger J. The singleton's low-bit periods grow slowly, so the
full test over every launch stays cheap. See right_ray_local_review.py for the claims and the prediction."""
# GC2667 at larger J: the singleton's low-bit periods grow slowly, so the full test stays cheap
import time
def phi(x): return x ^ ((2*x)|(4*x))
t0=time.time(); fails=0; dbl=[]
Jmax=64
W=Jmax+2; M=(1<<W)-1
# one long orbit on W bits, until its period or a cap
CAP=1<<24
seq=[1]; x=phi(1)&M
while x!=1 and len(seq)<CAP:
    seq.append(x); x=phi(x)&M
full = x==1
print('orbit length',len(seq),'closed',full, round(time.time()-t0,1))
n=len(seq)
def per(J):
    m=(1<<J)-1
    for p in (2**k for k in range(0,30)):
        if p>=n: return None
        if seq[p]&m==1: return p
    return None
last=None
for J in range(4,Jmax):
    PJ=per(J); PJ1=per(J+1)
    if PJ is None or PJ1 is None or 2*PJ1+4*J>n: print('stop at J',J,PJ,PJ1); break
    h=J//2; m=(1<<J)-1; bad=0; colour=False; returns=0
    for s in range(PJ1):
        white=True
        for u in range(2*J-h,2*J):
            if (seq[s+u]>>(u//2))&1: white=False; break
        start=seq[s+2*J-h]
        ret=(start&m)==1
        if white!=ret: bad+=1
        if white:
            returns+=1
            nxt=(seq[s+2*J]>>J)&1
            want=(nxt==0) if J%2==0 else (nxt==1)
            if want!=(((start>>J)&1)==1): bad+=1
            colour=colour or want
    doubled=PJ1==2*PJ
    if colour!=doubled: bad+=1
    fails+=bad
    if doubled: dbl.append(J)
    last=J
print('tested J = 4 ..',last,'failures',fails,'seconds',round(time.time()-t0,1))
print('doubling J (P(J+1) = 2 P(J)):',dbl)
