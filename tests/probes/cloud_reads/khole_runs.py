"""CL503 NOTE: absolute margins, not the record's per-number H(h); see khole.c PERNUM for P1.
CL501: three holes, M = 14, 3333, split by the longest run of adjacent holes.
OUTCOME (99 s): run 1 (165 pools): non-repeat exceptions to margin 5 (holes 5,7,9, targets 10,11,31,32), repeated to 7;
run 2 (110 pools): non-repeat to 7, repeated to 7; run 3 (11 pools): non-repeat to 8, repeated to 18.
"""
import sys, itertools
from collections import Counter
sys.argv=['x']
exec(open('tests/probes/cloud_reads/khole_fourbin.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
C=(3,3,3,3); M=14
def run_q(Qs):
    nr=Counter(); rp=Counter(); spec=0; ex={}
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for Q in Qs:
        pool=[x for x in range(M+1) if x not in Q]; tot=sum(pool); n=len(pool)
        sp=spectra(pool); F=feasible_set(pool,C)
        mins=lambda c: sum(pool[:c]); maxs=lambda c: sum(pool[n-c:])
        for t3 in itertools.product(*[range(mins(C[i]),maxs(C[i])+1) for i in range(3)]):
            t=t3+(tot-sum(t3),); tJ={J: sum(t[i] for i in J) for J in SUB}
            if not all(tJ[J] in sp[CJ[J]] for J in SUB): continue
            spec+=1
            if t3 in F: continue
            m=min(min(tJ[J]-mins(CJ[J]),maxs(CJ[J])-tJ[J]) for J in SUB)
            rep=any(t[i]==t[j] for i in range(4) for j in range(i+1,4))
            (rp if rep else nr)[m]+=1; ex.setdefault(('rep' if rep else 'nr',m),(Q,tuple(sorted(t))))
    return spec,sorted(nr.items()),sorted(rp.items()),ex
def maxrun(Q):
    r=b=0;prev=None
    for q in Q:
        b = b+1 if prev is not None and q==prev+1 else 1; r=max(r,b); prev=q
    return r
for R in (1,2,3):
    Qs=[Q for Q in itertools.combinations(range(1,M),3) if maxrun(Q)==R]
    s,nr,rp,ex=run_q(Qs)
    print('max hole run',R,'pools',len(Qs),'spec',s); print('  nonrepeat',nr); print('  repeat',rp)
    for k in sorted(ex):
        if k[1]>=2: print('   ',k,ex[k])
    sys.stdout.flush()
