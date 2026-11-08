# Arbitrary-precision continuation of the cycle lift (Cloud, CL755): the uint64 probe is exact only to width 62 (at 63 the second
# exterior cell is shifted out). This version uses Python ints and sets, resumes from a width-w0 checkpoint and lifts on.
# Usage: python3 -I cycle_lift_big.py WMAX CKDIR BUDGET_S WORD   (reads core_W{w0}.npz, the largest w0 <= 62 present; writes core_W{W}.npz for W > w0)
import sys, os, time, re
import numpy as np
A=[2,5]; E=[3,3,5,3,5,5,5,5]
def parse_word(spec):
    out=[]
    for m in re.finditer(r'(A|E)(\d*)', spec):
        n=int(m.group(2)) if m.group(2) else 1; out += (A if m.group(1)=='A' else E)*n
    return out
Wmax, ckdir, budget, spec = int(sys.argv[1]), sys.argv[2], float(sys.argv[3]), sys.argv[4]
WORD=parse_word(spec); P=sum(WORD)
u=[0]*P; t=0
for g in WORD: u[t%P]=1; t+=g
PQ = os.environ.get("PQ", "0") == "1"
def move(x, e, W):
    if PQ:                                             # rule30-open's rule: column W+1 free at each of the two ticks
        y = x | ((e & 1) << W)
        y = (((y << 1) ^ (y | (y >> 1))) & ((1 << W) - 1))
        y = y | ((e >> 1) << W)
        return ((((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << W) - 1))
    y = x | (e << W)                                   # W+2 cells
    y = (((y << 1) ^ (y | (y >> 1))) & ((1 << (W + 1)) - 1))        # centre white: left = y<<1 | 0
    y = ((((y << 1) | 1) ^ (y | (y >> 1))) & ((1 << W) - 1))        # centre black
    return y
def core(sets, W):
    rounds=0; changed=True
    while changed:
        changed=False; rounds+=1; new=[]
        for s in range(P):
            a=sets[s]; nxt=sets[(s+1)%P]; prv=sets[(s-1)%P]
            keep=set()
            for x in a:
                if (x & 1) != u[s]: continue
                if any(move(x,e,W) in nxt for e in range(4)): keep.add(x)
            preds=set()
            for x in prv:
                for e in range(4): preds.add(move(x,e,W))
            keep &= preds
            if len(keep)!=len(a): changed=True
            new.append(keep)
        sets=new
    return sets, rounds
w0=None
for W in range(62, 0, -1):
    if os.path.exists(os.path.join(ckdir, f"core_W{W}.npz")): w0=W; break
assert w0 is not None
z=np.load(os.path.join(ckdir, f"core_W{w0}.npz")); sets=[set(int(v) for v in z[f"s{s}"].tolist()) for s in range(P)]
print(f"word {spec}: period {P}; resuming from the uint64 checkpoint at width {w0} with {sum(len(s) for s in sets)} windows (big-int code)", flush=True)
t0=time.time()
for W in range(w0+1, Wmax+1):
    if time.time()-t0 > budget: print("budget reached before W", W, flush=True); break
    tw=time.time(); hi=1<<(W-1)
    sets, r = core([s_ | {x|hi for x in s_} for s_ in sets], W)
    sizes=[len(s_) for s_ in sets]; tot=sum(sizes)
    line=f"W={W} core sizes min/max/total {min(sizes)}/{max(sizes)}/{tot} rounds {r} time {time.time()-tw:.1f}s"
    np.savez_compressed(os.path.join(ckdir, f"core_W{W}.npz"), **{f"s{s}": np.array(sorted(sets[s]), dtype=object) for s in range(P)})
    if tot==0: print(line+"  EMPTY: this periodic word has no bi-infinite window path at this width (big-int code)", flush=True); break
    print(line, flush=True)
print(f"done; wall {time.time()-t0:.1f}s", flush=True)
