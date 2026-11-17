"""CL502-503: merge the sharded raw output of khole.c (H/E/F/S lines)."""
import sys
from collections import defaultdict
H=defaultdict(int); E={}; S=0
for f in sys.argv[1:]:
    for line in open(f):
        p=line.split()
        if p[0]=='H': H[tuple(map(int,p[1:4]))]+=int(p[4])
        elif p[0]=='E': E.setdefault(tuple(map(int,p[1:4])),' '.join(p[4:]))
        elif p[0]=='S': S+=int(p[1])
print('spectrum-feasible',S)
for r in range(0,8):
    for rep in (0,1):
        ks=sorted(g for (rr,re,g) in H if rr==r and re==rep)
        if ks: print('  run',r,'rep' if rep else 'nonrep',' '.join(f'{g}:{H[(r,rep,g)]}' for g in ks),' | top',E[(r,rep,ks[-1])])
FF={}
for f in sys.argv[1:]:
    for line in open(f):
        p=line.split()
        if p[0]=='F': FF[int(p[1])]=FF.get(int(p[1]),0)+int(p[2])
if FF: print('  spectrum-INfeasible by key:', ' '.join(f'{g}:{FF[g]}' for g in sorted(FF)))
