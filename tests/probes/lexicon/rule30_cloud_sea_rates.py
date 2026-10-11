#!/usr/bin/env python3
"""rule30_cloud_sea_rates.py: how often the untyped sea beside the alternating wall produces the typed shapes (CL337).

RUN-ON:     cpu (Python 3 standard library plus numpy; about two minutes at LOG2N = 24)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_sea_rates.py 24

WHAT. Rule 30 beside the wall x_t(0) = t mod 2, 2^LOG2N random rows of 226 cells (every cell a fair coin, the first
thirteen included), run 212 ticks so that the first thirteen cells stay exact throughout. At every tick the first cells
are classified: black AP13 (1110100011111, 1110100011100, 1110100011101), the white-A origin row 1110100011011, a
white-eleventh A (1110100011 then 0), a white SS entrance (first nine cells 11101 + 0000, 0100, 0101, 0110, 0111), the
pin shape 1110011110100, a high-111 row (first nine 111001111) and a black-marker S (111011101 or 111011111). Counts are
kept for even (white-wall) and odd ticks, over all ticks and over ticks 48..212, and reported as rates per row per tick.
These are the control for CL335's rates in the X cones over the even ticks 48..212 (black AP13 7.4 x 10^-4, white-A
origin 3.2 x 10^-5 per cone per even tick) and the fair-coin reference (3/8192 and 1/8192 for thirteen fair cells).

PREDICTIONS (CL337, registered before the run). S1: the sea's black AP13 rate at even ticks 48..212 lies between the
fair-coin 3.7 x 10^-4 and 10^-3, nearer the X cones' 7.4 x 10^-4 than the fair coin (0.6). S2: the sea's white-A origin
rate at even ticks is at least 10^-4 (0.6) and above the X cones' 3.2 x 10^-5 (0.7). S3: the pin shape at even ticks has
a rate within a factor two of 2^-13 (0.5). Counterfactual: sea rates equal to the X-cone rates would mean the X cones
are sea-like over 108..212; a gap of a factor three or more means the X exit keeps structure for a hundred ticks.
Unexpected check: the odd-tick (black-wall) rates of the same shapes, which the typed grammar never uses."""
import sys, time
import numpy as np
B=lambda s: tuple(int(c) for c in s)
TYPES=[B('1110100011111'),B('1110100011100'),B('1110100011101')]
VALID=[B('11101')+B(w) for w in ('0000','0100','0101','0110','0111')]
LOG2N=int(sys.argv[1]) if len(sys.argv)>1 else 22
N=1<<LOG2N; M=N//64; TMAX=212; WIDTH=13+TMAX+1
ONES=np.uint64(0xFFFFFFFFFFFFFFFF)
def pc(m): return int(np.bitwise_count(m).sum())
def match(cells,pattern):
    m=np.full(M,ONES,dtype=np.uint64)
    for i,b in enumerate(pattern): m&= cells[i] if b else ~cells[i]
    return m
rng=np.random.default_rng(20261011)
cells=[rng.integers(0,2**64,size=M,dtype=np.uint64,endpoint=False) for _ in range(WIDTH)]
SHAPES={'black AP13':TYPES,'white-A origin':[B('1110100011011')],
        'white-eleventh A':[B('11101000110')],'white SS entrance':VALID,
        'pin 1110011110100':[B('1110011110100')],'high 111001111':[B('111001111')],
        'black-marker S':[B('111011101'),B('111011111')]}
cnt={(k,par,late):0 for k in SHAPES for par in (0,1) for late in (0,1)}
ticks={(par,late):0 for par in (0,1) for late in (0,1)}
t0=time.time()
for t in range(TMAX+1):
    par=t%2; late=1 if t>=48 else 0
    ticks[(par,late)]+=1
    for k,pats in SHAPES.items():
        m=np.zeros(M,dtype=np.uint64)
        for p in pats: m|=match(cells,p)
        cnt[(k,par,late)]+=pc(m)
    if t==TMAX: break
    wall=np.full(M,ONES if par else 0,dtype=np.uint64)
    cells=[(cells[i-1] if i>0 else wall)^(cells[i]|cells[i+1]) for i in range(len(cells)-1)]
print('rows',N,'ticks 0..%d'%TMAX,'| %.0fs'%(time.time()-t0))
print('%-20s %14s %14s %14s %14s'%('shape','even all','even 48..212','odd all','odd 48..212'),
      '  (rate per row per tick; count)')
for k in SHAPES:
    row=[]
    for par in (0,1):
        for late in (0,1):
            n=cnt[(k,par,late)] if late==0 else cnt[(k,par,1)]
            T=ticks[(par,0)]+ticks[(par,1)] if late==0 else ticks[(par,1)]
            c=cnt[(k,par,0)]+cnt[(k,par,1)] if late==0 else cnt[(k,par,1)]
            row.append('%.2e (%d)'%(c/(N*T),c))
    print('%-20s %s'%(k,'  '.join('%22s'%x for x in row)))
print('fair-coin references: black AP13 3/8192 = %.2e, a single 13-cell word 1/8192 = %.2e,'%(3/8192,1/8192),
      'a 9-cell word 1/512 = %.2e'%(1/512))
