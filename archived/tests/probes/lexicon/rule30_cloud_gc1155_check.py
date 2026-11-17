#!/usr/bin/env python3
"""rule30_cloud_gc1155_check.py: Cloud's targeted (tier 2) check of GPT's GC1155 carrying step: Local's d = 133,
L = 23 witness (rule30_local_witnesses.txt, the real record R_real(139) = 17) has its left cell at depth 156 forced
black by the 78 even-time column-1 samples through tick 154, the odd-time samples being masked, so that no change of
right sites 156 and beyond can extend the run, and making depth 156 white breaks the unclamped wall at tick 156
(CL356).

RUN-ON:     cpu (Python 3 standard library; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1155_check.py

WHAT. (1) Local's right half (158 sites) is run with column 0 clamped to t mod 2 to read column 1, c[t], t = 0..157;
the left row at time 0 to depth 156 is computed by left permutivity,
x(-k, 0) = x(-k+1, 1) XOR (x(-k+1, 0) OR x(-k+2, 0)).
(2) Masking: x(-1, t) = x(0, t+1) XOR (x(0, t) OR c[t]) equals 1 at every odd t whatever c[t], so the whole left row at
time 0 is a function of the even-time samples; each c[t] is flipped singly and the changed left cells recorded. (3) The
light cone: flipping any of sites 156, 157, 158 at time 0 leaves c[0..154] unchanged. (4) The full configuration (left
row, wall cell, right half) is run UNCLAMPED to tick 156 and column 0 compared with t mod 2; the same with the depth-156
cell flipped to white.

PREDICTIONS (CL356, written before the run). P1: depths 133..155 white and depth 156 black (0.85). P2: flipping an
odd c[t], or c[155], changes no left cell at time 0; the set of t that flip depth 156 is a subset of the even t <= 154
(0.9).
P3: sites 156..158 cannot change c[0..154] (0.95). P4: the unclamped run keeps the clock to tick 156 with the forced left
row, and breaks it exactly at tick 156 once depth 156 is made white (0.85). Counterfactual: a white depth 156 or an odd
sample that matters would mean the record's endpoint is not read from the visible samples alone and GC1155's step
fails. Unexpected check: how many of the 78 visible samples flip depth 156 singly, and the earliest one that does.
Record searched: masked, odd-time, visible (0 hits outside the ledgers).
"""
import re
txt=open('tests/probes/lexicon/rule30_local_witnesses.txt').read().split('\n')
i=[k for k,l in enumerate(txt) if l.startswith('d=133 ')][0]
bits=''
for l in txt[i+1:]:
    if not l.strip(): break
    bits+=l.strip()
R=[int(b) for b in bits]; n=len(R); assert n==158, n
def column1(right):
    row=list(right); c=[]
    for t in range(len(right)):
        c.append(row[0]); w=t%2
        row=[(row[j-1] if j else w)^(row[j]|(row[j+1] if j+1<len(row) else 0)) for j in range(len(row)-1)]
    return c   # c[t] exact for t <= n-1 (x(1,t) depends on sites <= t+1)
def left_row(c,K):
    T=len(c); X={}
    for t in range(T): X[(1,t)]=c[t]; X[(0,t)]=t%2
    for k in range(1,K+1):
        for t in range(T-k): X[(-k,t)]=X[(-k+1,t+1)]^(X[(-k+1,t)]|X[(-k+2,t)])
    return [X[(-k,0)] for k in range(1,K+1)]
c=column1(R); K=156
L=left_row(c,K)
whites=[k for k in range(133,156) if L[k-1]==0]
print('(1) depths 133..155 white:',len(whites)==23,'| depth 156:','black' if L[155] else 'WHITE',
      '| first black depth >= 133:',next(k for k in range(133,157) if L[k-1]==1))
odd_change=0; sens=[]; any_change_155=False
for t in range(156):
    c2=c[:]; c2[t]^=1; L2=left_row(c2,K)
    changed=[k for k in range(1,K+1) if L2[k-1]!=L[k-1]]
    if t%2==1 and changed: odd_change+=1
    if t==155 and changed: any_change_155=True
    if L2[155]!=L[155]: sens.append(t)
print('(2) odd-time samples that change any left cell:',odd_change,'| c[155] changes a left cell:',any_change_155)
print('    samples flipping depth 156:',len(sens),'of 78 visible | all even and <= 154:',
      all(t%2==0 and t<=154 for t in sens),'| earliest:',min(sens) if sens else None)
ok3=True
for s in (156,157,158):
    R2=R[:]; R2[s-1]^=1; c3=column1(R2)
    if c3[:155]!=c[:155]: ok3=False
    if c3[155]!=c[155]: print('    site',s,'changes c[155] (masked)')
print('(3) sites 156..158 leave c[0..154] unchanged:',ok3)
def unclamped(left,right,T):
    row=left[::-1]+[0]+list(right)   # sites -156..158 at time 0 (phase 0: wall white at t = 0)
    z=len(left); out=[]
    for t in range(T+1):
        out.append(row[z] if 0<=z<len(row) else None)
        row=[(row[j-1] if j else 0)^(row[j]|(row[j+1] if j+1<len(row) else 0)) for j in range(1,len(row)-1)]
        z-=1
    return out
col0=unclamped(L,R,156); clock=[t%2 for t in range(157)]
bad=[t for t in range(157) if col0[t]!=clock[t]]
Lw=L[:]; Lw[155]=0; col0w=unclamped(Lw,R,156); badw=[t for t in range(157) if col0w[t]!=clock[t]]
print('(4) forced left row keeps the clock to 156:',not bad,'| with depth 156 white, first break at tick:',badw[:3])
