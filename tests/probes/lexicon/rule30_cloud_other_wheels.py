#!/usr/bin/env python3
"""rule30_cloud_other_wheels.py: EXPLORATORY LOOK (the owner, 2026-10-11): are there other wheels in other columns of
the real single-seed pattern? Labelled exploratory as section 3 of WORKING-TOGETHER.md requires; not evidence.

RUN-ON:     cpu (Python 3 standard library plus numpy; about a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_other_wheels.py 16

WHAT. The real Rule 30 pattern from one black cell, 2^LOG2T rows. For each column x in -40..40 (x = 0 the centre, x = 1
the column that is the wheel beside a clamped 0101 centre), the time sequence of the column from row |x| on: (a) the
factor complexity p(n) for n = 8 and 16 (a coding of a rotation has p(n) = n + 1; a kicked wheel stays near linear; a
coin-like column approaches 2^n); (b) the wheel coverage: the largest fraction of the sequence covered by maximal
stretches that are exactly periodic with one period P in 2..120 and at least 3P long, with that P (the clamped wheel is
period 56 in even time, 112 in full time, between kicks; P = 1 is excluded since constant runs cover about half of any
coin-like sequence, which a first run of this probe showed); (c) the same for the even-time subsequence. CONTROLS, run
first: the clamped wheel itself (column 0 held at t mod 2, a 12-cell random right half then white, as rule30_wheel.py
builds it; the metric must find it) and a fair coin of the same length (the metric's floor). The coverage at the fixed
period 56 (the wheel's window in rule30_wheel.py) is printed as well. A first run with the controls showed the metric
reads the clamped column as period 10 with coverage 1.0: that column is made of the L ring's 10-step column-1 word
1101000100 and the S ring's 6-step word 110100 (CL351), and the best single period is the L word, not the 56-step wheel.

LIGHT PREDICTION (exploratory, written before the run): no column x >= 0 shows wheel coverage above 0.3 at any P; the
left columns x <= -2 show high coverage at small P from the striped side; column 0 and column 1 are coin-like (0.6).
"""
import sys, numpy as np
LOG2T=int(sys.argv[1]) if len(sys.argv)>1 else 14
T=1<<LOG2T; W=2*T+3
row=np.zeros(W,dtype=np.uint8); row[T+1]=1
cols={x:np.zeros(T,dtype=np.uint8) for x in range(-40,41)}
for t in range(T):
    for x in cols: cols[x][t]=row[T+1+x]
    left=np.concatenate(([0],row[:-1])); right=np.concatenate((row[1:],[0]))
    row=left^(row|right)
def complexity(seq,n):
    v=np.zeros(len(seq)-n+1,dtype=np.int64)
    for i in range(n): v|=seq[i:len(seq)-n+1+i].astype(np.int64)<<i
    return len(np.unique(v))
def cover_at(seq,P,minlen=3):
    n=len(seq); eq=(seq[P:]==seq[:-P]).astype(np.int8)
    d=np.diff(np.concatenate(([0],eq,[0]))); starts=np.flatnonzero(d==1); ends=np.flatnonzero(d==-1)
    lens=ends-starts+P
    return lens[lens>=minlen*P].sum()/n
def coverage(seq,Pmax=120,minlen=3):
    best=(0.0,None); n=len(seq)
    for P in range(2,Pmax+1):      # P = 1 excluded: constant runs cover half of any coin-like column
        eq=(seq[P:]==seq[:-P]).astype(np.int8)     # eq[t]=1 iff seq[t]==seq[t+P]
        # maximal runs of eq ones; a run of length r means a periodic stretch of length r+P
        d=np.diff(np.concatenate(([0],eq,[0]))); starts=np.flatnonzero(d==1); ends=np.flatnonzero(d==-1)
        lens=ends-starts+P
        cov=lens[lens>=minlen*P].sum()/n
        if cov>best[0]: best=(cov,P)
    return best
rng=np.random.default_rng(20261011)
def clamped_col1(right,T):
    row=np.zeros(T+len(right)+2,dtype=np.uint8); row[:len(right)]=right; c=np.zeros(T,dtype=np.uint8)
    for t in range(T):
        c[t]=row[0]; wall=np.array([t%2],dtype=np.uint8)
        left=np.concatenate((wall,row[:-1])); rightn=np.concatenate((row[1:],[0])); row=left^(row|rightn)
    return c
for k in range(3):
    c=clamped_col1(rng.integers(0,2,12,dtype=np.uint8),T)
    print('control: clamped-wall column 1, right half',k,
          '| p(8) %d p(16) %d | cover(full) %.3f P %s | cover(even) %.3f P %s | cover at P=56 %.3f'
          %(complexity(c,8),complexity(c,16),*coverage(c),*coverage(c[::2]),cover_at(c,56)))
coin=rng.integers(0,2,T,dtype=np.uint8)
print('control: fair coin | p(8) %d p(16) %d | cover(full) %.3f P %s | cover(even) %.3f P %s | cover at P=56 %.3f'
      %(complexity(coin,8),complexity(coin,16),*coverage(coin),*coverage(coin[::2]),cover_at(coin,56)))
print('rows',T,'| columns -40..40 | sequence from row |x| on')
print('%5s %8s %8s %12s %6s %12s %6s %8s'%('x','p(8)','p(16)','cover(full)','P','cover(even)','P','at P=56'))
for x in range(-40,41):
    seq=cols[x][abs(x):]
    if len(seq)<2000: continue
    p8=complexity(seq,8); p16=complexity(seq,16); cf,Pf=coverage(seq); ce,Pe=coverage(seq[::2])
    flag=' <- wheel-like' if (cf>0.3 or ce>0.3) and x>=0 else ''
    print('%5d %8d %8d %12.3f %6s %12.3f %6s %8.3f%s'%(x,p8,p16,cf,Pf,ce,Pe,cover_at(seq,56),flag))
