#!/usr/bin/env python3
"""L1048: data for the Rule 30 Past Worlds page: the 122 exact depth-12 pasts of the single seed, with edge periods.

Local, 2026-10-27. Same exact construction as root_pasts_exact.py, keeping cells far to the left as well. Asserts
122 chains and that every displayed row evolves into the next. Usage: past_worlds_data.py OUT.json
"""
import json
LO=-400          # leftmost stored position
HALF=32         # display window -32..32 (65 columns)
DEPTH=12; FUT=52
def G(b,s): c,r=s; return (b^(c|r), c)
class Row:
    """cells on [LO, inf): win = cells LO..R-1, tail = periodic block from R"""
    def __init__(s, win, R, tail): s.win, s.R, s.tail = win, R, tuple(tail)
    def at(s,i):
        if i < s.R: return s.win[i-LO]
        return s.tail[(i-s.R) % len(s.tail)]
def parents(y):
    p,R=len(y.tail),y.R
    def comp(st):
        for i in range(R+p,R,-1): st=G(y.at(i),st)
        return st
    cyc=set()
    for st in [(a,b) for a in (0,1) for b in (0,1)]:
        seen=[];v=st
        while v not in seen: seen.append(v); v=comp(v)
        cyc.update(seen[seen.index(v):])
    pred={comp(u):u for u in cyc}
    out=[]
    for st in sorted(cyc):
        c=1;v=comp(st)
        while v!=st: v=comp(v); c+=1
        x={}
        for k in range(1,c+1):
            top=st
            for _ in range(k): top=pred[top]
            v=top; pos=R+k*p; x[pos],x[pos+1]=v
            for i in range(pos,pos-p,-1): v=G(y.at(i),v); x[i-1]=v[0]
        x[R],x[R+1]=st
        tail=tuple(x[R+j] for j in range(c*p))
        for i in range(R-1,LO-1,-1): x[i]=y.at(i+1)^(x[i+1]|x[i+2])
        row=Row([x[i] for i in range(LO,R)],R,tail)
        for i in range(LO+1,R+3*len(tail)+3): assert y.at(i)==row.at(i-1)^(row.at(i)|row.at(i+1))
        out.append(row)
    return out
def minp(seq):
    for p in range(1,len(seq)//2+1):
        if all(seq[i]==seq[i+p] for i in range(len(seq)-p)): return p
    return None
def show(row): return ''.join(str(row.at(i)) for i in range(-HALF,HALF+1))
seed=Row([0]*(0-LO)+[1],1,[0])     # cells LO..0 with a 1 at 0; zeros from 1
# depth-first tree order, children in parents() order (sorted pair states)
chains=[]
def dfs(row, chain, d):
    if d==DEPTH: chains.append(chain); return
    for x in parents(row): dfs(x, [x]+chain, d+1)
dfs(seed, [], 0)
assert len(chains)==122, len(chains)
# seed's future on the window (exact: the window's light cone stays inside the white background)
fut=[]; cur={i:(1 if i==0 else 0) for i in range(-200,201)}
for t in range(FUT+1):
    fut.append(''.join(str(cur[i]) for i in range(-HALF,HALF+1)))
    cur={i:(cur.get(i-1,0)^(cur.get(i,0)|cur.get(i+1,0))) for i in range(-200+t+1,201-t-1)}
pasts=[]
for ch in chains:
    rows=[]
    for r in ch:   # depth 12 .. 1
        left=[r.at(i) for i in range(LO,LO+240)]
        rows.append(dict(cells=show(r), right=len(r.tail) if minp(list(r.tail)*2) is None else minp(list(r.tail)*2), left=minp(left)))
    pasts.append(dict(rows=rows, first=('A' if ch[-1].at(0)==0 else 'B')))
# consistency: each displayed past row evolves into the next one (interior of the window)
for p in pasts:
    seq=[r['cells'] for r in p['rows']]+[fut[0]]
    for a,b in zip(seq,seq[1:]):
        for i in range(1,len(a)-1):
            assert int(b[i])==int(a[i-1])^(int(a[i])|int(a[i+1]))
json.dump(dict(half=HALF,depth=DEPTH,future=fut,pasts=pasts), open(__import__('sys').argv[1],'w'), separators=(',',':'))
print('ok: 122 chains; first-step parents A/B counts:', sum(p['first']=='A' for p in pasts), sum(p['first']=='B' for p in pasts))
print('right-edge periods seen at depth 12:', sorted({p['rows'][0]['right'] for p in pasts}), ' left periods:', sorted({str(p['rows'][0]['left']) for p in pasts}))
