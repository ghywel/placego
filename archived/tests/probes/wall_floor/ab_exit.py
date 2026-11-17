#!/usr/bin/env python3
"""ab_exit.py (Local, L1542): every row that steps into the AB lock from outside with the longest settled past, by SAT with the model printed: for each past row its phase, letter, and the first offset where it leaves the strip."""
import sys,json
from sat_past import *
S=[l.strip() for l in open('lock45.txt') if l.strip()]
W=45
T=sorted(set(S))
strip={'A':None,'B':None}
for s in T:
    k=s[::-1]
    if k[:11]=='##...####..' : strip.setdefault('A',k)
A=[s[::-1] for s in T if s[::-1][8:10]=='#.']; B=[s[::-1] for s in T if s[::-1][8:10]=='.#']
sA=A[0]; sB=B[0]
print('A',sA); print('B',sB)
def first(row,ref):
    for k in range(min(len(row),len(ref))):
        if k>=len(ref)-3: return None     # scar cells of the strip vary
        if ('#' if row[k] else '.')!=ref[k]: return k
    return None
for L in (14,13,12):
  for i in range(len(T)):
    nv,cl,var,K0=build(T[i],W,L,T,True)
    st,model,el=solve(nv,cl,10)
    if st!='SATISFIABLE': continue
    rows=[]
    for s in range(0,L+1):
        r=[]
        k=0
        while (s,k) in var:
            r.append(1 if var[(s,k)] in model else 0); k+=1
        rows.append(r)
    lets=''.join('A' if rows[s][8] else 'B' for s in range(L,-1,-1))
    print('L',L,'window',i,'letters oldest first',lets)
    ph0=T[i][::-1]
    isA=ph0[8:10]=='#.'
    out=[]
    for s in range(0,L+1):
        ref=(sA if (isA==(s%2==0)) else sB)
        out.append((s,'A' if rows[s][8] else 'B',first(rows[s],ref),len(rows[s])))
    print('   row, letter, first offset off the strip, cells known:',out)
    break
