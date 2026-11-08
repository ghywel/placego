# GC2768's finite-margin bound applied to each dead periodic word (Cloud, CL755): from the word's lift log (synchronous rounds
# per width -> deletion ranks d_w = rounds-1, with d_1 = 0: the width-1 round is the bit filter) and its last nonempty core
# checkpoint, the candidate DAG at the death width, its longest path L, and the bound N <= 2 D_(w-1) + L on any block of the
# periodic trace in any right half beside the alternating centre. Own code.
import sys, re, numpy as np
sys.setrecursionlimit(1000000)
A=[2,5]; E=[3,3,5,3,5,5,5,5]
def parse_word(spec):
    out=[]
    for m in re.finditer(r'(A|E)(\d*)', spec):
        n=int(m.group(2)) if m.group(2) else 1; out += (A if m.group(1)=='A' else E)*n
    return out
spec, logs, ckdir = sys.argv[1], sys.argv[2].split(','), sys.argv[3]
WORD=parse_word(spec); P=sum(WORD)
u=np.zeros(P,dtype=np.uint8); t=0
for g in WORD: u[t%P]=1; t+=g
def move(x, e, W):          # Python ints: exact at every width (the uint64 probe is exact only to 62)
    y = x | (e << W)
    y = (((y << 1) ^ (y | (y >> 1))) & ((1 << (W + 1)) - 1))
    return ((((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << W) - 1))
rounds={}; death=None
for lg in logs:
    for line in open(lg):
        m=re.match(r"W=(\d+) core sizes min/max/total (\d+)/(\d+)/(\d+) rounds (\d+)", line)
        if m:
            W=int(m.group(1)); rounds[W]=int(m.group(5))
            if int(m.group(4))==0: death=W
assert death is not None, "no death width in the logs"
assert all(W in rounds for W in range(1, death+1)), "missing widths in the logs"
assert rounds[1] <= 2
d={W:(0 if W==1 else rounds[W]-1) for W in range(1, death+1)}
D={}; acc=0
for W in range(1, death+1): acc+=d[W]; D[W]=acc
z=np.load(f"{ckdir}/core_W{death-1}.npz", allow_pickle=True); core=[[int(v) for v in z[f"s{s}"].tolist()] for s in range(P)]
hi=1<<(death-1)
cand=[np.array(sorted(set(c)|{x|hi for x in c}), dtype=object) for c in core]
succ={}
for s in range(P):
    nxtset=set(int(v) for v in cand[(s+1)%P].tolist())
    for a in cand[s].tolist():
        outs=set()
        for e in range(4):
            b=move(int(a),e,death)
            if b in nxtset: outs.add(b)
        succ[(s,a)]=[((s+1)%P,b) for b in sorted(outs)]
colour={}; best={}; cyc=[False]
def dfs(v):
    colour[v]=1; m=0
    for w in succ[v]:
        if colour.get(w,0)==1: cyc[0]=True; continue
        if w not in best: dfs(w)
        m=max(m,1+best[w])
    best[v]=m; colour[v]=2
for v in succ:
    if v not in best: dfs(v)
L=max(best.values()) if best else 0
nedges=sum(len(v) for v in succ.values())
k=len([g for g in WORD if True]); returns=spec.count('E')
N=2*D[death-1]+L
print(f"{spec}: period {P} sampled steps, {returns} returns per period; dead at width {death}; d_(death)={d[death]}, D_(death-1)={D[death-1]}, D_(death)={D[death]}")
print(f"  candidates at {death}: {sum(c.size for c in cand)} vertices, {nedges} edges, cycle={cyc[0]}, longest path L={L}")
print(f"  bound: any block of this periodic trace has at most N = 2*{D[death-1]} + {L} = {N} sampled edges; "
      f"so at most {N // P} full periods ({(N // P) * returns} returns) fit, and {N // P + 1} consecutive periods are forbidden")
