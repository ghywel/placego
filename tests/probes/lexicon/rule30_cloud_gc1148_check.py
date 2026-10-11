#!/usr/bin/env python3
"""rule30_cloud_gc1148_check.py: Cloud's second read of GPT's GC1148 (an all-depth record-conditioned SS residence
budget, L <= 2a+5 OR N <= d+a+5) and of the proof step it rests on, by brute force (CL348).

RUN-ON:     cpu (Python 3 standard library; about two minutes)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1148_check.py

WHAT. (1) GC686's 84-cell ring R (RING = 0x688eb74a45efb082671ee, bit i = site i): a Rule 30 travelling wave, its
columns 0 and 1, its largest cyclic white gap. (2) The proof step "the first N column-1 samples determine the row at
the anchor to depth N-1": for N = 1..18, every row of sites 1..N+1 beside the alternating wall (white at the anchor)
whose N samples equal the ring's trace, compared with R at sites 1..N-1. (3) The inequality itself on small instances:
a white interval at sites d..d+L-1 at time 0, a white-wall anchor a, and N samples of 110100 from the anchor, by brute
force over the free cells, for d = 1..7, a = 0, 2, 4, L = 2a+4..2a+8, N = d+a+4..d+a+7.

PREDICTIONS (written before the run): (1) the ring facts and gap 5 (0.8); (2) the determination step holds (0.6); (3)
the inequality holds on every small instance (0.7). RESULT (CL348): (1) held (shift 14, columns 0101 and 110100, gap
5); (2) REFUTED for every N from 3 to 18: the N samples fix sites 1..3 only (for N = 11, 240 rows match and only sites
1..3 are constant); (3) REFUTED: 24 violations among 357 instances, e.g. the row 111100000000 at a white-wall time with
sites 5..10 white gives the samples 11010011010, the first eleven of (110100)^inf, while the ring reads 111011110001
there. The proof reads left permutivity in the wrong direction: the trace fixes the row leftward, not to its right.
"""
import itertools
RING=0x688eb74a45efb082671ee; P=84
R=[(RING>>i)&1 for i in range(P)]
def step_ring(x): return [x[(i-1)%P]^(x[i]|x[(i+1)%P]) for i in range(P)]
y=step_ring(R)
shifts=[s for s in range(P) if y==[R[(i-s)%P] for i in range(P)]]
shifts=shifts or [s for s in range(P) if y==[R[(i+s)%P] for i in range(P)]]
print('(1) ring: F(R) is a shift of R by',shifts if shifts else 'NONE')
cols=[]; x=R[:]
for t in range(12): cols.append((x[0],x[1])); x=step_ring(x)
print('    column 0 over 12 ticks',''.join(str(c[0]) for c in cols),'| column 1',''.join(str(c[1]) for c in cols))
runs=[]; s=R+R; i=0
mx=0
for i in range(P):
    if R[i]==0:
        j=0
        while s[i+j]==0 and j<P: j+=1
        mx=max(mx,j)
print('    largest cyclic white gap in R:',mx,'(GPT 5) | weight',sum(R),'of',P)
# (2) finite determination beside the alternating wall (white at the anchor time)
def fwd(x,left):
    f=[left]+list(x); return tuple(f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1))
pat=[1,1,0,1,0,0]
bad=0; checked=0
for N in range(1,19):
    width=N+1   # sites 1..N+1 at the anchor: column 1 over N ticks depends on sites <= N
    target=tuple(pat[t%6] for t in range(N))
    agree=True; cnt=0
    for row in itertools.product((0,1),repeat=width):
        r=row; samples=[]
        for t in range(N):
            samples.append(r[0]); r=fwd(r,t%2)
        if tuple(samples)==target:
            cnt+=1
            if tuple(row[:N-1])!=tuple(R[1:N]): agree=False
    checked+=1
    if not agree: bad+=1; print('    N =',N,
        ': a row with R\'s samples differs from R inside sites 1..N-1; rows matching',cnt)
print('(2) finite determination holds for all N in 1..18:',bad==0)
# (3) the inequality on small instances: white interval [d, d+L-1] at time 0, anchor a (even,
# white wall), N samples of 110100
viol=0; attained=0; tested=0
for d in range(1,8):
    for a in (0,2,4):
        for L in range(2*a+4,2*a+9):
            for N in range(d+a+4,d+a+8):
                width=a+N+1     # sites 1..a+N+1 at time 0 (column 1 at time a+N-1 depends on sites <= a+N)
                if d+L-1>width: continue
                free=[i for i in range(1,width+1) if not (d<=i<=d+L-1)]
                target=tuple(pat[t%6] for t in range(N)); ok=False
                for bits in itertools.product((0,1),repeat=len(free)):
                    row=[0]*(width+1)
                    for i,b in zip(free,bits): row[i]=b
                    r=tuple(row[1:]); 
                    for t in range(a): r=fwd(r,t%2)
                    samples=[]
                    for t in range(a,a+N):
                        samples.append(r[0]); r=fwd(r,t%2)
                    if tuple(samples)==target: ok=True; break
                tested+=1
                if ok and L>=2*a+6 and N>=d+a+6: viol+=1; print('    VIOLATION d',d,'a',a,'L',L,'N',N)
                if ok and (L==2*a+5 or N==d+a+5) and (L>=2*a+5 and N>=d+a+5): attained+=1
print('(3) instances tested',tested,'| violations of L<=2a+5 OR N<=d+a+5:',viol,
    '| boundary cases realised (L = 2a+5 or N = d+a+5):',attained)
