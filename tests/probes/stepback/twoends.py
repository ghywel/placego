#!/usr/bin/env python3
"""twoends.py (Local, step back, 5 Nov 2026): Q01's integer form, F(Y) = (Y>>1) ^ (Y | (Y<<1)). How many numbers of width at most W stay odd at the even ticks through tick t, against 2^(W - t/2)?"""
import numpy as np,collections
F=lambda y:(y>>1)^(y|(y<<1))
def census(W):
    y=np.arange(1,1<<W,dtype=np.uint64)
    out=[]
    t=0
    y=y[(y&np.uint64(1))==1]
    out.append((0,len(y)))
    while len(y) and t<4*W:
        for _ in range(2):
            y=(y>>np.uint64(1))^(y|(y<<np.uint64(1)))
        t+=2
        y=y[(y&np.uint64(1))==1]
        out.append((t,len(y)))
    return out
for W in (20,24,26):
    c=census(W)
    print('W',W,' '.join(f'{t}:{n}' for t,n in c if t%4==0 or n<40))
    print('   log2 N + t/2 - W:',' '.join(f'{t}:{(np.log2(n)+t/2-W):.1f}' for t,n in c if n>0 and t%4==0))
