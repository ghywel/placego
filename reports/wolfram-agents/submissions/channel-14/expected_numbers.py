#!/usr/bin/env python3
"""Expected outputs of the essay's Wolfram Language cells at width 14, computed in Python (python3 -I expected_numbers.py)."""
import math, re
from functools import lru_cache

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
def growth(succ,its=300):
    N=len(succ); v=[1.0]*N; lam=None
    for _ in range(its):
        w=[0.0]*N
        for i,(a,b) in enumerate(succ):
            if a>=0: w[a]+=v[i]
            if b>=0: w[b]+=v[i]
        s=sum(w); lam=s/sum(v); v=[x/s for x in w]
    return lam
for M in (6,8):
    sets,succ=build(M); print(f'width {M}: states {len(sets)}, dead edges {sum(1 for p in succ for x in p if x<0)}, growth(300) {growth(succ):.6f}')
src=open('essay-template.md').read()
succ=[[int(a),int(b)] for a,b in re.findall(r'\{(-?\d+), (-?\d+)\}', re.search(r'succ14 = (\{.*?\});',src).group(1))]
w=[int(x) for x in re.search(r'weights14 = \{(.*?)\};',src).group(1).split(',')]
R=1184655442; D=10**9; wa=lambda j: 0 if j<0 else w[j]
print('width 14: states',len(succ),'dead edges',sum(1 for p in succ for x in p if x<0),'inequality',all(w[i]>0 and D*(wa(a)+wa(b))<=R*w[i] for i,(a,b) in enumerate(succ)))
@lru_cache(None)
def acc(n,i):
    if i<0: return 0
    if n==0: return 1
    return acc(n-1,succ[i][0])+acc(n-1,succ[i][1])
print('growth(300) %.7f'%growth(succ),'log2(R/D) %.5f'%math.log2(R/D),'acc n=1..20',[acc(n,0) for n in range(1,21)],'bound n=20 %.1f'%(300*(R/D)**20))
sets,s2=build(14); assert s2==succ; print('rows at width 14:', sum(len(s) for s in sets), '; C =', -(-w[0]//min(w)), '; wmin', min(w), '; w0', w[0])
