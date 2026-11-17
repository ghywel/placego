#!/usr/bin/env python3
"""GC1007: bounded initial-left forcing for its two relaxed return loops.
Prediction and scope in RULE30-GPT.md. No all-depth or realizability claim.
"""
from itertools import product
ROOT = '1000010010000100100001'
LOOPS = {'A':'SLLLSLSL', 'B':'LLSLSL'}
TRUTH = (0,1,1,1,1,0,0,0)
DEPTH = 180
rows = []
for choices in product('AB',repeat=3):
    word = ROOT + ''.join('001' if g=='S' else '00001'
                          for c in choices for g in LOOPS[c])
    pulse = [int(word[t//2]) if t%2==0 else 0
             for t in range(2*len(word)-1)]
    # GC709: c1=1-q. All inter-pulse gaps are6 or10 physical ticks.
    prev = [t%2 for t in range(len(pulse))]
    cur = [1-b for b in pulse]
    initial = []
    assert len(cur)>DEPTH
    for d in range(1,DEPTH+1):
        initial.append(cur[0])
        nxt = [cur[t+1] ^ (cur[t] | prev[t])
               for t in range(len(cur)-1)]
        assert all(TRUTH[4*nxt[t]+2*cur[t]+prev[t]]==cur[t+1]
                   for t in range(len(nxt)))
        prev,cur = cur,nxt
    rows.append(initial)
ones = [d+1 for d in range(DEPTH) if all(r[d]==1 for r in rows)]
assert max(ones)==146 and all(d in ones for d in (125,132,136,146))
print('Common initial black depths:',ones)
print('Literal triangle controls PASS; all eight choices, depth180')
