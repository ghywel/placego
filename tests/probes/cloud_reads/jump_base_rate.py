"""CL483 unexpected check: share of ALL m-subsets of the one-hole pool that have the staircase / one-jump shape (base rate)."""
import itertools, sys, re
sys.argv=['x']
src=open('tests/probes/cloud_reads/staircase_boundary.py').read().split("if __name__")[0]
exec(src)
# base rate: over all P in S (size m) for M=12, fraction with each shape
from collections import Counter
M=12
for q in (3,6):
    S=[x for x in range(M+1) if x!=q]
    for m in (6,7):
        c=Counter(); n=0
        for P in itertools.combinations(S,m):
            st,sr,jp=shapes(list(P),S); n+=1; c['stair']+=st; c['jump']+=jp
        print('q',q,'m',m,'all m-subsets',n,'staircase share',round(c['stair']/n,3),'jump<=6 share',round(c['jump']/n,3))
