# Collatz-Wielandt integer certificates for the channel automaton at width M (port of entropy2.c's cert routine).
import json, sys, math
from fractions import Fraction
def build(M):
    MASK=(1<<M)-1
    def nxt(s,tv,u): return (((s<<1)|tv) ^ (s | ((s>>1) | (u<<(M-1))))) & MASK
    root=tuple(range(1<<M)); index={root:0}; sets=[root]; succ=[]; q=0
    while q<len(sets):
        cur=sets[q]; sq=[]
        for bit in (0,1):
            l1=set()
            for s in cur:
                if (s&1)!=bit: continue
                l1.add(nxt(s,0,0)); l1.add(nxt(s,0,1))
            l2=set()
            for t in l1: l2.add(nxt(t,1,0)); l2.add(nxt(t,1,1))
            if not l2: sq.append(-1); continue
            key=tuple(sorted(l2))
            if key not in index: index[key]=len(sets); sets.append(key)
            sq.append(index[key])
        succ.append(sq); q+=1
    return sets,succ
def certify(succ, delta=2e-4, D=10**9):
    N=len(succ); v=[1.0]*N
    for _ in range(300):
        w=[0.0]*N
        for i,(a,b) in enumerate(succ):
            if a>=0: w[a]+=v[i]
            if b>=0: w[b]+=v[i]
        s=sum(w); lam=s/sum(v); v=[x/s for x in w]
    lp=lam*(1+delta); t=[1.0]*N; ws=[0.0]*N; rounds=0; maxt=1.0
    while maxt>=0.25 and rounds<10**7:
        for i in range(N): ws[i]+=t[i]
        t2=[0.0]*N; maxt=0
        for i,(a,b) in enumerate(succ):
            x=0.0
            if a>=0: x+=t[a]
            if b>=0: x+=t[b]
            t2[i]=x/lp; maxt=max(maxt,t2[i])
        t=t2; rounds+=1
    R=math.ceil(lp*D)
    # integer weights: scale and round up; verify exactly, bumping scale if needed
    for scale in (10**6,10**7,10**8,10**9):
        w=[math.ceil(x*scale) for x in ws]
        ok=all(w[i]>0 and D*((w[a] if a>=0 else 0)+(w[b] if b>=0 else 0))<=R*w[i] for i,(a,b) in enumerate(succ))
        if ok: break
    return lam, lp, R, w, ok, rounds
for M in [int(x) for x in sys.argv[1:]]:
    sets,succ=build(M); lam,lp,R,w,ok,rounds=certify(succ)
    N=len(succ); C=-(-w[0]//min(w))
    print(f'M={M}: N={N} lambda={lam:.7f} R/D={R/1e9:.9f} ok={ok} rounds={rounds} wmin={min(w)} wroot={w[0]} C={C} log2(R/D)={math.log2(R/1e9):.4f}')
    json.dump({'M':M,'succ':succ,'weights':w,'D':10**9,'R':R,'C':C}, open(f'cert-m{M}.json','w'))
