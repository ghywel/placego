#!/usr/bin/env python3
"""Cloud, 2026-10-30 (CL652): analysis of the owner's three breaks (edge_break.c outputs). Usage: analyze_breaks.py DIR BASELINE_LIFT64"""
import re, sys, collections, math
D=sys.argv[1]; base_path=sys.argv[2]
def load(p):
    recs=[]; L=open(p).read().split('\n'); i=0
    while i<len(L):
        m=re.match(r'seed=(\S+) mods:(.*) E_n: (.*)',L[i])
        if m:
            E=[int(x) for x in m.group(3).split()]
            w1=[int(x) for x in L[i+1].split(':')[1].split()]; w2=[int(x) for x in L[i+2].split(':')[1].split()]; ov=[int(x) for x in L[i+3].split(':')[1].split()]
            recs.append((m.group(1),m.group(2).split(),E,w1,w2,ov)); i+=4
        else: i+=1
    return recs
base={}
for line in open(base_path):
    m=re.search(r'seed=(\S+) E_n: (.*)',line)
    if m: base[m.group(1)]=[int(x) for x in m.group(2).split()]
def density(E,lo,hi): 
    d=[E[n-1]-E[n-2] for n in range(lo,hi+1)]; return sum(d)/len(d)
plat={'0x2e5ccb':(20,28),'0xaf5f4f':(29,37),'0xa8b6f3':(45,53),'0x415459':(34,41),'0x7ca56d':(24,32),'0x6af979':(40,48)}
# ---- Break 1
recs=load(f"{D}/edge_break1.out")
single={ (s,int(m[0][1:])):r for r in recs for s,m in [(r[0],r[1])] if len(m)==1 }
pair={ (s,int(m[1][1:])):r for r in recs for s,m in [(r[0],r[1])] if len(m)==2 }
ok=bad=0; pbroke=ptot=0; sbroke=0
for (s,k),r in pair.items():
    rs=single[(s,k-1)]; Es=rs[2]; Ep=r[2]; w2s=rs[4]
    changed = Ep[k] != Es[k]          # E_(k+1)
    pred = w2s[k]==1                  # w2 at n=k+1 is index k
    ok += (changed==pred); bad += (changed!=pred)
    a,b=plat[s]
    if a-1<=k<=b-1:
        ptot+=1
        E0=base[s]
        firstp=next((n for n in range(1,57) if Ep[n-1]!=E0[n-1]),None)
        if firstp is not None and firstp<=b: pbroke+=1
print(f"Break 1: P21 composition rule: agree {ok}, disagree {bad} (of {ok+bad} pairs)")
print(f"Break 1: P22 pairs inside plateaus breaking before the end: {pbroke} of {ptot} (singles were 43 of 53)")
# ---- Breaks 2, 3, controls
for mod in ['c30','a30','x30','A','X']:
    recs=load(f"{D}/edge_break_{mod}.out")
    print(f"--- {mod}: {len(recs)} seeds")
    if mod=='c30':
        e30=sum(1 for r in recs if r[2][29]==r[2][28]); 
        p1=sum(1 for r in recs if (r[2][30]-r[2][29])==r[4][30]); p2=sum(1 for r in recs if (r[2][31]-r[2][30])==r[3][31])
        print(f" P23: d_31 = weight parity of wheel 29: {p1} of {len(recs)}; d_32 = weight parity of wheel 31: {p2} of {len(recs)}")
        print(f" P24: E_30 = E_29 in {e30} of {len(recs)}; density n=33..56 {sum(density(r[2],33,56) for r in recs)/len(recs):.3f} (baseline {sum(density(base[s],33,56) for s in base)/len(base):.3f})")
        f31=sum(r[2][30]-r[2][29] for r in recs)/len(recs); f32=sum(r[2][31]-r[2][30] for r in recs)/len(recs)
        print(f" PU: doubling frequency at wheel 31: {f31:.2f}, at wheel 32: {f32:.2f} (baseline at 31: {sum(base[s][30]-base[s][29] for s in base)/len(base):.2f})")
    elif mod in ('a30','x30'):
        if mod=='x30': p=sum(1 for r in recs if (r[2][29]-r[2][28])==(r[3][29]^r[4][29]))
        else: p=sum(1 for r in recs if (r[2][29]-r[2][28])==r[5][29])
        print(f" P25: hand rule for d_30 holds in {p} of {len(recs)}; d_30 frequency {sum(r[2][29]-r[2][28] for r in recs)/len(recs):.2f} (baseline {sum(base[s][29]-base[s][28] for s in base)/len(base):.2f})")
        print(f" P26: density n=33..56 {sum(density(r[2],33,56) for r in recs)/len(recs):.3f}")
    elif mod=='X':
        p=sum(1 for r in recs if all(r[2][n-1]==math.ceil(math.log2(n+1)) for n in range(1,57)))
        print(f" P27: E_n = ceil(log2(n+1)) for all n <= 56 in {p} of {len(recs)} seeds")
    else:
        print(f" P27: AND everywhere, density n=13..56 {sum(density(r[2],13,56) for r in recs)/len(recs):.3f}; E_56 mean {sum(r[2][55] for r in recs)/len(recs):.1f} (baseline E_56 mean {sum(base[s][55] for s in base)/len(base):.1f})")
