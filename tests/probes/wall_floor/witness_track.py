#!/usr/bin/env python3
"""witness_track.py (Local, L1540): agreement with the third lock along the verified witness, oldest row first: for each past row, the deepest agreement with any phase word, and the smallest over the last six ticks."""
import json
d=json.load(open('witness_break_175_56.json')); y=d['y0_by_offset']
refs=[l.strip() for l in open('ref6.txt') if l.strip()]
refs=[r[::-1] for r in refs]   # by offset
rows=[y]
while len(rows[-1])>=60:
    c=rows[-1]; rows.append([c[k+3]^(c[k+4]|c[k+5]) for k in range(len(c)-5)])
def best(c):
    b=0
    for r in refs:
        k=0
        while k<len(r) and k<len(c) and (r[k]=='?' or (r[k]=='#')==bool(c[k])): k+=1
        b=max(b,k)
    return b
series=[(s,best(rows[s]),len(rows[s])) for s in range(len(rows)-1,-1,-1)]
print('row back, agreement, cells known:')
print(' '.join(f'{s}:{b}' + ('*' if b>=n else '') for s,b,n in series))
bs=[b for s,b,n in series]
print('smallest over six ticks, from oldest:',[min(bs[max(0,i-5):i+1]) for i in range(len(bs))])
