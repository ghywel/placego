# Carry of GC2768 (Cloud, CL755): the width-43 candidate graph lifted from my own core_W42 checkpoint of the periodic 4,7 word:
# vertices, distinct edges, acyclicity and the longest path, by own code; and the deletion ranks from my logs.
import sys, re, numpy as np
sys.setrecursionlimit(100000)
A=[2,5]; E=[3,3,5,3,5,5,5,5]; WORD=A*4+E+A*7+E; P=sum(WORD)
u=np.zeros(P,dtype=np.uint8); t=0
for g in WORD: u[t%P]=1; t+=g
MASK=lambda w:(np.uint64(1)<<np.uint64(w))-np.uint64(1)
def Bstep(x,b,w):
    one=np.uint64(1); left=(x<<one)|np.uint64(b); return (left^(x|(x>>one)))&MASK(w)
def move(x,e,W):
    y=x|(np.uint64(e)<<np.uint64(W)); y=Bstep(y,0,W+2)&MASK(W+1); return Bstep(y,1,W+1)&MASK(W)
ck=sys.argv[1]; W=43
z=np.load(ck); core42=[z[f"s{s}"] for s in range(P)]
print("core_W42 total", sum(x.size for x in core42))
hi=np.uint64(1)<<np.uint64(42)
cand=[np.unique(np.concatenate([c, c|hi])) for c in core42]
print("candidates at 43:", sum(c.size for c in cand))
# bit check: every candidate has the right column-1 bit
assert all(((c & np.uint64(1)) == np.uint64(u[s])).all() for s,c in enumerate(cand))
edges=set(); succ={}
for s in range(P):
    nxt=cand[(s+1)%P]; nxtset=set(int(v) for v in nxt.tolist())
    for a in cand[s].tolist():
        a64=np.uint64(a); outs=set()
        for e in range(4):
            b=int(move(a64,e,W))
            if b in nxtset: outs.add(b)
        succ[(s,a)]=[((s+1)%P,b) for b in sorted(outs)]
        for b in outs: edges.add((s,a,b))
print("distinct edges:", len(edges))
# acyclicity + longest path (memoised DFS with colours)
colour={}; best={}
cyc=[False]
def dfs(v):
    colour[v]=1; m=0
    for w in succ[v]:
        if colour.get(w,0)==1: cyc[0]=True; continue
        if w not in best: dfs(w)
        m=max(m,1+best[w])
    best[v]=m; colour[v]=2
for v in succ:
    if v not in best: dfs(v)
print("cycle found:", cyc[0])
L=max(best.values()); print("longest path (edges):", L)
# where do the longest paths start/end (phases)?
starts=[v for v,b in best.items() if b==L]
print("longest-path starts (phase, count):", sorted(set(s for s,_ in starts)))
# vertices with no successor / no predecessor
nosucc=sum(1 for v in succ if not succ[v]); print("vertices with no candidate successor:", nosucc)
haspred=set(w for v in succ for w in succ[v]); print("vertices with no candidate predecessor:", len(succ)-len(haspred))
