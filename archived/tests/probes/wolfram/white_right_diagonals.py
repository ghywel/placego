#!/usr/bin/env python3
"""L1051: the white-right past is the pyramid's right diagonals repeated backwards in time.

Local, 2026-10-28. Finds each right diagonal's least period in 8192 forward steps (8.27: purely periodic, a power
of 2), then compares every cell of the exact white-right past (white_right_past.py output) on that diagonal with
the periodic continuation. Measured: diagonals 0..28, 14,848 cells, no mismatch.
Usage: white_right_diagonals.py WHITE_RIGHT_PAST.json
"""
import json, base64
# the seed's future as big integers (bit index = position + OFF)
T=8192; OFF=T+2
x=1<<OFF; fut=[]
for t in range(T+1):
    fut.append(x); x=(x<<1)^(x|(x>>1))
cell=lambda t,pos: (fut[t]>>(pos+OFF))&1
# right diagonal d: D_d(t) = cell(t, t-d), t >= 0; find its least period on [0, T-d]
def period(d, need=3):
    seq=[cell(t,t-d) for t in range(0, T+1)]
    for p in range(1, (T+1)//need):
        if all(seq[i]==seq[i+p] for i in range(len(seq)-p)): return p, seq
    return None, seq
# the exact white-right past from the large view
B=json.load(open(__import__('sys').argv[1])); raw=base64.b64decode(B['bits'])
def past(t,pos):   # t in [t0, -1]
    y=t-B['t0']; xi=pos-B['x0']; return (raw[y*B['stride']+(xi>>3)]>>(7-(xi&7)))&1
checked=0; mism=0; per={}
for d in range(0, 400):
    p,seq=period(d)
    if p is None: continue
    per[d]=p
    for k in range(1, 513):
        pos=-k-d
        if pos < B['x0']: break
        want=seq[(-k) % p]
        checked+=1; mism+= (past(-k,pos)!=want)
print('diagonals with a period visible in 8192 steps:', len(per), '(d = 0 ..', max(per), ')')
print('past cells compared with the periodic continuation:', checked, ' mismatches:', mism)
print('periods of diagonals 0..40:', [per.get(d) for d in range(41)])
