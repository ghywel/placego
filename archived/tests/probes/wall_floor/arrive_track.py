#!/usr/bin/env python3
"""arrive_track.py (Local, L1540): the past of chain rows that reach agreement 145: forward ticks on their top 256 cells give past letters and agreement, next to the verified witness."""
refs=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
A=[1,1,0,0,0,1,1,1,1,0,0]
def best(c):
    b=0
    for r in refs:
        k=0
        while k<len(r) and k<len(c) and (r[k]=='?' or (r[k]=='#')==bool(c[k])): k+=1
        b=max(b,k)
    return b
L=[l.split()[0] for l in open('arrive145.txt')]
seen=set()
for x in L:
    key=x[:200]
    if key in seen: continue
    seen.add(key)
    if len(seen)>4: break
    c=[1 if ch=='#' else 0 for ch in x]
    series=[];lets=''
    s=0
    while len(c)>=16:
        series.append(best(c)); lets=('A' if c[8]==1 else 'B')+lets
        c=[c[k+3]^(c[k+4]|c[k+5]) for k in range(len(c)-5)]
        s+=1
    print('letters oldest first',lets)
    print('agreement going back:',series)
