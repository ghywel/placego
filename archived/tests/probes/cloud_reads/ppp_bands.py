"""CL488: gap depth of Sigma_a(P) for the balanced prefix-plus-pair P (M = 12).  OUTCOME: 686,280 cases; max depth 0..8, mostly 4..8: the bands are NOT an interval."""
import sys, itertools
from collections import Counter
sys.argv=['x']
exec(open('/home/user/placego/tests/probes/cloud_reads/ppp_rules.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
M=12; depth=Counter(); n=0
for C in itertools.product(range(3, M - 8), repeat=4):
    if sum(C) != M: continue
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for q in range(1, M):
        S=[x for x in range(M+1) if x!=q]; tot=sum(S); N=len(S); sp=spectra(S)
        mins=lambda c: sum(S[:c]); maxs=lambda c: sum(S[N-c:]); R=[M-x for x in reversed(S)]
        for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i])+1) for i in range(3)]):
            t=t3+(tot-sum(t3),); tJ={J: sum(t[i] for i in J) for J in SUB}
            if not all(tJ[J] in sp[CJ[J]] and tJ[J]-mins(CJ[J])>=2 and maxs(CJ[J])-tJ[J]>=2 for J in SUB): continue
            for pr in PAIRS:
                for side in ('lo','up'):
                    Z = S if side=='lo' else R
                    tt = t if side=='lo' else tuple(C[i]*M-t[i] for i in range(4))
                    X,Y = pr; m=C[X]+C[Y]
                    cands = ppp_candidates(Z, m, tt[X]+tt[Y])
                    if not cands: continue
                    x,y,P = max(cands, key=lambda c: c[0])
                    for a in (C[X], C[Y]):
                        s=spectra(P)[a]; lo,hi=min(s),max(s); n+=1
                        d=max([min(v-lo,hi-v) for v in range(lo,hi+1) if v not in s], default=0)
                        depth[d]+=1
print('balanced PPP sets, M=12: (pair, frame, bin) cases', n, ' max gap depth of Sigma_a(P):', sorted(depth.items()))
