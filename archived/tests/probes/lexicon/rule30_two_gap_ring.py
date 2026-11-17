#!/usr/bin/env python3
"""All-length TG guard from the existing seven-ring (RULE30-PRIZE sections5/8.3).
Prediction and prior-art search: RULE30-GPT TG all-length guard, 2026-10-10.
The four-row witness is an infinite periodic configuration, not a finite seed.
No train-length sweep or SAT. Controls: literal/packed update, phase rebasing,
finite-cone truncation; unexpected check rejects finite-support periodicity.
"""
ROWS=('0100110','1111101','0000001','1000011')

def step(row):
    return ''.join(str(int(row[(i-1)%7]) ^ (int(row[i])|int(row[(i+1)%7])))
                   for i in range(7))

def packed(q):
    left=((q<<1)&127)|(q>>6)
    right=(q>>1)|((q&1)<<6)
    return left ^ (q|right)

for t,row in enumerate(ROWS):
    nxt=ROWS[(t+1)%4]
    assert step(row)==nxt
    q=sum(int(b)<<i for i,b in enumerate(row))
    assert packed(q)==sum(int(b)<<i for i,b in enumerate(nxt))
assert ''.join(r[0] for r in ROWS)=='0101'
assert ''.join(r[1] for r in ROWS)=='1100'
# Same code 10..., starting white at orbit0 or black at orbit3.
for origin,first_white in ((0,0),(3,1)):
    assert all(ROWS[(origin+t)%4][0]==str((t+origin)%2) for t in range(4))
    assert ''.join(ROWS[(origin+first_white+2*s)%4][1] for s in range(8))=='10'*4
# Independent finite zero-extended row agrees on the target cone.
T=9
row={i:int(ROWS[0][i%7]) for i in range(-T,T+2)}
for t in range(T+1):
    assert [row.get(i,0) for i in (0,1)]==[int(ROWS[t%4][i]) for i in (0,1)]
    row={i:row.get(i-1,0) ^ (row.get(i,0)|row.get(i+1,0))
         for i in range(-T-t-1,T+t+3)}
# A single seven-cell copy with zeros outside is not this periodic orbit.
seed={i for i,b in enumerate(ROWS[0]) if b=='1'}
a=set(seed)
for t in range(4):
    a={i for i in range(min(a)-1,max(a)+2)
       if ((i-1 in a) ^ ((i in a) or (i+1 in a)))}
assert a!=seed
print('Four-row orbit, both phases, finite light cone and nonperiodic finite-seed controls PASS')
print('Rows:', ', '.join(ROWS))
