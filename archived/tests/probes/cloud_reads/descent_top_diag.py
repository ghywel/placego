"""CL505: the h = 1 top-tight failures of descent_alternation.py: (child holes, lower key, upper key) of the best realization.
OUTCOME: 3,952 failing instances; best child (2,1,1) 3,556, (3,1,2) 219, (3,2,2) 177; lower + upper >= child holes in all.
Reads kholek DUMPEVERY files d1_*.txt from the scratch directory (data outside git).
"""
import sys
from collections import Counter
from itertools import combinations
sys.argv_files = sys.argv[1] if len(sys.argv) > 1 else 'd1_?.txt'; sys.argv=['x']
exec(open('tests/probes/cloud_reads/descent_alternation.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
M,h=15,1; C=(3,3,3,3,3); prof=Counter(); n=0
import glob
for f in sorted(glob.glob(sys.argv_files)):
    for line in open(f):
        if not line.startswith('V'): continue
        hs,ts=line[len('V holes'):].split('|'); H=list(map(int,hs.split())); t=list(map(int,ts.split()))
        S=[x for x in range(M+1) if x not in H]; k=5
        facets=sorted((sum(t[i] for i in J)-sum(C[i] for i in J)*(sum(C[i] for i in J)-1)//2-h*sum(C[i] for i in J), s, J) for s in range(1,k) for J in combinations(range(k),s))
        sl,s,J=facets[0]
        if s!=k-1: continue
        A=[i for i in range(k) if i not in J][0]
        best=None; ok=False
        for R in combinations(S,C[A]):
            if sum(R)!=t[A]: continue
            rest=[x for x in S if x not in R]; a,b=rest[0],rest[-1]; hh=(b-a+1)-len(rest)
            sz=[C[i] for i in range(k) if i!=A]; tt=[t[i] for i in range(k) if i!=A]
            lo=key([u-a*c for u,c in zip(tt,sz)],sz); up=key([c*b-u for u,c in zip(tt,sz)],sz)
            if lo>=hh or up>=hh: ok=True
            cand=(lo+up-hh, hh, lo, up, R)
            if best is None or cand[:1]>best[:1]: best=cand
        if not ok:
            n+=1; prof[(best[1],best[2],best[3])]+=1
            if n<=4: print('example', H, t, 'A', A, 'best child', best)
print('failing top-tight instances', n)
print('(h_child, lowkey, upkey) of best realization:', prof.most_common(12))
print('lo+up >= h_child in all failing?', all(l+u>=hh for (hh,l,u) in prof))
