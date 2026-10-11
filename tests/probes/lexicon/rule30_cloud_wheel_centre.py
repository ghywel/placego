#!/usr/bin/env python3
"""rule30_cloud_wheel_centre.py: EXPLORATORY LOOK (the owner, 2026-10-11 16:58 BST): the unkicked wheel word U itself
(period 56, the universal word of RULE30-PRIZE.md section 8.4, the two-arc coding of t -> 17t mod 56) as the clamped
centre column in place of 0101. U repeated is a periodic word, so it is as much a candidate periodic centre as 0101 is.
Labelled exploratory as section 3 of WORKING-TOGETHER.md requires; not evidence.

RUN-ON:     cpu (Python 3 standard library plus numpy; about two minutes at LOG2T = 15)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_wheel_centre.py 15

THEORY FIRST. Jen's theorem (Proposition 7, section 8.13) and Theorem B (section 8.54) hold for any periodic pair of
columns 0 and 1, not only for 0101: if column 1 beside U^inf were eventually periodic, the whole left half would be
periodic in time with white runs at most 2P - 2, so no finite configuration has centre U^inf and a periodic column 1.
The wheel word is in the same position as 0101: beside it, a finite configuration needs a non-periodic column 1.

WHAT. Column 0 held at U[(t + s) mod 56] (phases s = 0 and s = 28), a 12-cell random right half then white, 2^LOG2T
steps. Column 1 is measured as in rule30_cloud_other_wheels.py: block complexity p(8) and p(16) (a coin gives 256 and
about 25,900 of 32,753 windows), the best single-period coverage for P in 2..240 (maximal exactly periodic stretches
of length at least 3P), the coverage at P = 56, and an eventual-period test (periodic with some P <= 400 over the last
1,000 steps). The forced left row at time 0 (left permutivity, depth 300) gives its longest white run. The same is
done for the 0101 centre (the known wheel: p(8) about 22, coverage 1.0 at P = 10, the L ring's word) and a fair coin.
Six right halves per centre for the structure metrics; a lock census over 64 right halves per centre at 4,096 steps.

LIGHT PREDICTIONS (exploratory, written before the run). W1: column 1 beside U is structured but less than beside 0101:
p(8) between 30 and 200 for most halves (0.4). W2: no right half locks column 1 into a period <= 400 within 4,096
steps beside U, against about 4% beside 0101 (rule30_wheel.py: 166 of 4,096) (0.5). W3: the longest left white run to
depth 300 beside U is at most that beside 0101 for most halves (0.5). Counterfactual: p(8) = 256 beside U would say the
wheel's structure belongs to the 0101 boundary specifically; a locked column 1 beside U is a periodic pair, allowed
here because these right halves do not give finite configurations (the forced left half is not finite). Unexpected
check: the best coverage period beside U, against 56 and 10. Record searched: wheel centre, U^inf, clamp U (no hits).
"""
import sys, numpy as np
U=[int(b) for b in "00010011010001001101000100110100010011010001001101001101"]
LOG2T=int(sys.argv[1]) if len(sys.argv)>1 else 14
T=1<<LOG2T
def col1(right,T,wall):
    row=np.zeros(T+len(right)+2,dtype=np.uint8); row[:len(right)]=right; c=np.zeros(T,dtype=np.uint8)
    for t in range(T):
        c[t]=row[0]; w=np.array([wall(t)],dtype=np.uint8)
        left=np.concatenate((w,row[:-1])); rightn=np.concatenate((row[1:],[0])); row=left^(row|rightn)
    return c
def complexity(seq,n):
    v=np.zeros(len(seq)-n+1,dtype=np.int64)
    for i in range(n): v|=seq[i:len(seq)-n+1+i].astype(np.int64)<<i
    return len(np.unique(v))
def cover_at(seq,P,minlen=3):
    eq=(seq[P:]==seq[:-P]).astype(np.int8)
    d=np.diff(np.concatenate(([0],eq,[0]))); starts=np.flatnonzero(d==1); ends=np.flatnonzero(d==-1)
    lens=ends-starts+P
    return lens[lens>=minlen*P].sum()/len(seq)
def coverage(seq,Pmax=240):
    best=(0.0,None)
    for P in range(2,Pmax+1):
        cv=cover_at(seq,P)
        if cv>best[0]: best=(cv,P)
    return best
def locked(c,Pmax=400,tail=1000):
    for P in range(1,Pmax+1):
        bad=np.flatnonzero(c[:-P]!=c[P:])
        if (bad.max() if len(bad) else -1)<len(c)-P-tail: return P
    return None
def left_row(c,wall,K):   # x(-k,t) = x(-k+1,t+1) XOR (x(-k+1,t) OR x(-k+2,t))
    T=len(c); prev=[wall(t) for t in range(T)]; prev2=[int(b) for b in c]; out=[]
    for k in range(1,K+1):
        cur=[prev[t+1]^(prev[t]|prev2[t]) for t in range(T-k)]
        out.append(cur[0]); prev2,prev=prev,cur
    return out
def longest_white(L):
    g=m=0
    for b in L:
        g=g+1 if b==0 else 0; m=max(m,g)
    return m
WALLS={'0101':lambda t:t%2,'U phase 0':lambda t:U[t%56],'U phase 28':lambda t:U[(t+28)%56]}
rng=np.random.default_rng(20261011)
halves=[rng.integers(0,2,12,dtype=np.uint8) for _ in range(6)]
for name,wall in WALLS.items():
    print('centre',name)
    for k,h in enumerate(halves):
        c=col1(h,T,wall); cf,Pf=coverage(c); L=left_row(c[:302],wall,300)
        print('  half %d %s | p(8) %3d p(16) %5d | best cover %.3f at P %s | cover at 56 %.3f | lock %s'
              ' | longest left white run to depth 300: %d'
              %(k,''.join(map(str,h)),complexity(c,8),complexity(c,16),cf,Pf,cover_at(c,56),locked(c),longest_white(L)))
coin=rng.integers(0,2,T,dtype=np.uint8)
print('control: fair coin | p(8) %d p(16) %d | best cover %.3f at P %s | cover at 56 %.3f'
      %(complexity(coin,8),complexity(coin,16),*coverage(coin),cover_at(coin,56)))
print('lock census, 64 random right halves per centre, 4,096 steps, period <= 400 over the last 1,000 steps')
cens=[rng.integers(0,2,12,dtype=np.uint8) for _ in range(64)]
for name,wall in WALLS.items():
    locks=[locked(col1(h,4096,wall)) for h in cens]
    found=[p for p in locks if p]
    print('  centre %-10s locked %2d of 64 | periods %s'%(name,len(found),sorted(set(found))))
