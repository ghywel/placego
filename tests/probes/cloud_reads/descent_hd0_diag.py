"""CL506: do the h = 1 top-tight failing children fit a hole-aware family HD0 (per size r: lower margin >= r*d_r, upper
>= r*e_r)?  OUTCOME: 3,952 failing; no realization fits HD0 in 2,222; fits HD0 but not HD0+1 in 1,646; both 84.
Reads kholek DUMPEVERY files from the scratch directory (data outside git).
"""
import sys, glob
from collections import Counter
from itertools import combinations
sys.argv=['x']
exec(open('tests/probes/cloud_reads/descent_alternation.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
def keys_by_size(tg, sz, M):
    """per group size r: min over groups of size r of floor((u-L(r))/r) (lower) and floor((T_r(M)-u)/r) (upper)"""
    k=len(sz); lo={}; up={}
    for s in range(1,k):
        for J in combinations(range(k),s):
            r=sum(sz[i] for i in J); u=sum(tg[i] for i in J); Tr=sum(range(M-r+1,M+1))
            lo[r]=min(lo.get(r,99),(u-r*(r-1)//2)//r); up[r]=min(up.get(r,99),(Tr-u)//r)
    return lo,up
def de(pool, M, r):
    holes=[x for x in range(M+1) if x not in pool]
    s=sorted(pool); d=sum(1 for q in holes if q<s[r-1]); e=sum(1 for q in holes if q>s[-r]); return d,e
M,h=15,1; C=(3,3,3,3,3); prof=Counter(); n=0
for f in sorted(glob.glob(sys.argv_files if False else '/tmp/claude-0/-home-user-placego/65b2700f-7c0c-5a5c-bf6d-c51aa7c63cf1/scratchpad/d1_?.txt')):
    for line in open(f):
        if not line.startswith('V'): continue
        hs,ts=line[len('V holes'):].split('|'); H=list(map(int,hs.split())); t=list(map(int,ts.split()))
        S=[x for x in range(M+1) if x not in H]; k=5
        facets=sorted((sum(t[i] for i in J)-sum(C[i] for i in J)*(sum(C[i] for i in J)-1)//2-h*sum(C[i] for i in J), s, J) for s in range(1,k) for J in combinations(range(k),s))
        sl,s,J=facets[0]
        if s!=k-1: continue
        A=[i for i in range(k) if i not in J][0]; ok=False; rows=[]
        for R in combinations(S,C[A]):
            if sum(R)!=t[A]: continue
            rest=[x for x in S if x not in R]; a,b=rest[0],rest[-1]; hh=(b-a+1)-len(rest)
            sz=[C[i] for i in range(k) if i!=A]; tt=[t[i] for i in range(k) if i!=A]
            low=[u-a*c for u,c in zip(tt,sz)]; Mc=b-a; poolc=[x-a for x in rest]
            if key(low,sz)>=hh or key([c*b-u for u,c in zip(tt,sz)],sz)>=hh: ok=True; break
            lo,up=keys_by_size(low,sz,Mc)
            fit=all(lo[r]>=de(poolc,Mc,r)[0] and up[r]>=de(poolc,Mc,r)[1] for r in lo)
            fit1=all(lo[r]>=de(poolc,Mc,r)[0]+ (1 if hh else 0) and up[r]>=de(poolc,Mc,r)[1] for r in lo) or all(lo[r]>=de(poolc,Mc,r)[0] and up[r]>=de(poolc,Mc,r)[1]+(1 if hh else 0) for r in lo)
            rows.append((fit,fit1,tuple(x-a for x in range(a,b+1) if x not in rest)))
        if not ok:
            n+=1; prof[('HD0' if any(r[0] for r in rows) else 'noHD0', 'HD1' if any(r[1] for r in rows) else 'noHD1')]+=1
            if n<=3: print(H,t,'A',A,rows[:3])
print('failing top-tight', n, dict(prof))
