#!/usr/bin/env python3
"""replay.py: re-check records.json from the file alone, in seconds, with a plain Rule 30 loop and nothing else.
For every row: (1) run the right half with column 0 held to the wall and read column 1; it must equal the stored trace.
(2) Compute the left row at time 0 from the wall and the trace by left permutivity; it must equal the stored left row.
(3) Depths depth .. depth+L-1 of that row must be white. (4) The visible word must be the trace at the white ticks.
Usage: python3 replay.py [records.json]
"""
import json, sys, os
p=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'records.json')
D=json.load(open(p)); bad=0
def column1(right,T,phase):
    row=list(right)+[0]*(T+2); c=[]
    for t in range(T):
        c.append(row[0]); w=(t+phase)%2
        row=[(row[j-1] if j else w)^(row[j]|row[j+1]) for j in range(len(row)-1)]
    return c
def left_row(c,K,phase):
    T=len(c); prev=[(t+phase)%2 for t in range(T)]; prev2=list(c); out=[]
    for k in range(1,K+1):
        cur=[prev[t+1]^(prev[t]|prev2[t]) for t in range(T-k)]
        out.append(cur[0]); prev2,prev=prev,cur
    return out
for r in D['rows']:
    tr=[int(b) for b in r['trace']]; right=[int(b) for b in r['right']]; left=[int(b) for b in r['left']]; T=r['T']; ph=r['phase']
    c=column1(right,T+1,ph); ok1=c==tr
    Lr=left_row(tr+[0],T,ph); ok2=Lr==left
    ok3=all(left[k-1]==0 for k in range(r['depth'],r['depth']+r['L']))
    vis=''.join(str(tr[t]) for t in range(T+1) if (t+ph)%2==0); ok4=vis.startswith(r['visible']) or r['visible'].startswith(vis)
    if not (ok1 and ok2 and ok3 and ok4): bad+=1; print('FAIL depth',r['depth'],'phase',ph,ok1,ok2,ok3,ok4)
print('rows',len(D['rows']),'| failures',bad,'| PASS' if not bad else '| FAIL')
