#!/usr/bin/env python3
"""rule30_cloud_record_left_check.py: the corrected second read of GC1148 (and GC1151's structure) in GPT's orientation: the
record is the LEFT row beside the alternating wall, and columns 0 and 1 determine it leftward (CL350).

RUN-ON:     cpu (Python 3 standard library; about three minutes)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_record_left_check.py

WHAT. With column 0 = the wall (t mod 2) and column 1 = a sequence c, the left cells are x_(-k)(t) = x_(-k+1)(t+1) XOR
(x_(-k+1)(t) OR x_(-k+2)(t)). (1) The determination step: for N samples of the S trace 110100 from a white-wall anchor,
do all sequences give left depths 1..N-1 equal to GC686's ring at its negative sites? (2) The inequality L <= 2a+5 OR N <=
d+a+5 (S, gap 5) and L <= 2a+6 OR N <= d+a+6 (L trace 1101000100, gap 6): all column-1 sequences of length up to 22 for
d = 1..6, anchors 0 and 2, L and N around the bounds. (3) The maximal left white run at depth d reachable for given
samples, against the bound.

PREDICTION (written before the run): no violation, determination exact (0.8). RESULT (CL350): held; the premise with both
L and N large is never realised at these sizes, and the reachable runs stay well below the bound.
"""
import itertools
def left_row(c,K):
    T=len(c); X={}
    for t in range(T): X[(1,t)]=c[t]; X[(0,t)]=t%2
    for k in range(1,K+1):
        for t in range(T-k): X[(-k,t)]=X[(-k+1,t+1)]^(X[(-k+1,t)]|X[(-k+2,t)])
    return X
RING=0x688eb74a45efb082671ee; P=84; R=[(RING>>i)&1 for i in range(P)]
S=[1,1,0,1,0,0]; L10=[1,1,0,1,0,0,0,1,0,0]
for N in (6,10,14):
    agree=True; cnt=0
    for bits in itertools.product((0,1),repeat=N+2):
        if any(bits[j]!=S[j%6] for j in range(N)): continue
        X=left_row(bits,N); cnt+=1
        if any(X[(-k,0)]!=R[(-k)%P] for k in range(1,N)): agree=False
    print('(1) S trace, N =',N,': sequences',cnt,'| left depths 1..N-1 equal the ring:',agree)
def test(pat,G,label):
    viol=0; tested=0; realised=0
    for d in range(1,7):
        for a in (0,2):
            for L in range(2*a+G-1,2*a+G+4):
                for N in range(d+a+G-1,d+a+G+3):
                    T=max(d+L,a+N)+1
                    if T>22: continue
                    tested+=1; found=False
                    for bits in itertools.product((0,1),repeat=T):
                        if any(bits[a+j]!=pat[j%len(pat)] for j in range(N)): continue
                        X=left_row(bits,d+L)
                        if all(X[(-k,0)]==0 for k in range(d,d+L)): found=True; break
                    if found:
                        realised+=1
                        if L>=2*a+G+1 and N>=d+a+G+1: viol+=1; print('   VIOLATION',label,d,a,L,N)
    print('(2)',label,': instances',tested,'| premise realised in',realised,'| violations:',viol)
test(S,5,'S, gap 5'); test(L10,6,'L, gap 6')
print('(3) maximal left white run at depth d for given S samples (free bits <= 17):')
for a in (0,2):
    for d in (1,2,3,4):
        for N in (d+a+3,d+a+6,d+a+8):
            T=a+N+6; free=T-N
            if free>17: continue
            best=0
            for bits in itertools.product((0,1),repeat=free):
                c=[None]*T; it=iter(bits)
                for t in range(T): c[t]=S[(t-a)%6] if a<=t<a+N else next(it)
                X=left_row(c,T-1); Lr=0
                while d+Lr<=T-1 and X.get((-(d+Lr),0))==0: Lr+=1
                best=max(best,Lr)
            print('   a=%d d=%d N=%2d: max L = %d%s'%(a,d,N,best,'  (bound %d applies)'%(2*a+5) if N>=d+a+6 else ''))
