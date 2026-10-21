"""CL488: in the first completing balanced PPP of each pair-least instance (M = 12), how many of {x, y} does X use?  OUTCOME: 8,274: j=1 only 7,050; j in {0,1} 510; {1,2} 510; j=0 only 102; j=2 only 102."""
import sys, itertools
from collections import Counter
sys.argv=['x']
exec(open('/home/user/placego/tests/probes/cloud_reads/ppp_rules.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
M=12; js=Counter(); n=0
for C in itertools.product(range(3, M - 8), repeat=4):
    if sum(C) != M: continue
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for q in range(1, M):
        S=[x for x in range(M+1) if x!=q]; tot=sum(S); N=len(S); sp=spectra(S)
        mins=lambda c: sum(S[:c]); maxs=lambda c: sum(S[N-c:]); R=[M-x for x in reversed(S)]
        for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i])+1) for i in range(3)]):
            t=t3+(tot-sum(t3),); tJ={J: sum(t[i] for i in J) for J in SUB}
            if not all(tJ[J] in sp[CJ[J]] and tJ[J]-mins(CJ[J])>=2 and maxs(CJ[J])-tJ[J]>=2 for J in SUB): continue
            sl=sorted([(tJ[p]-mins(CJ[p]),'lo',p) for p in PAIRS]+[(maxs(CJ[p])-tJ[p],'up',p) for p in PAIRS])
            sing=min(min(t[i]-mins(C[i]),maxs(C[i])-t[i]) for i in range(4))
            if not sl[0][0] < sing: continue
            h,side,(X,Y)=sl[0]; Z,tt=(S,t) if side=='lo' else (R,tuple(C[i]*M-t[i] for i in range(4)))
            for x,y,P in sorted(ppp_candidates(Z,C[X]+C[Y],tt[X]+tt[Y]), key=lambda c:-c[0]):
                if not completes(Z,P,C,tt,X,Y): continue
                pre=[v for v in P if v not in (x,y)]
                # which j in {0,1,2} realise t_X: j = number of x,y used by X
                J=set()
                for j,extra in ((0,0),(1,x),(1,y),(2,x+y)):
                    if C[X]-j>=0 and tt[X]-extra in spectra(pre)[C[X]-j]: J.add(j)
                js[tuple(sorted(J))]+=1; n+=1; break
print('pair-least, first completing PPP (balanced order), M=12:', n, ' X realisable using j of {x,y}:', sorted(js.items()))
