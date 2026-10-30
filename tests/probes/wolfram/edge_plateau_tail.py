#!/usr/bin/env python3
"""Cloud, 2026-10-30 (CL650): zero-run (plateau) length distributions of block exponents, run A (256 48-bit seeds to n = 60,
edge_lift48.out) and run B (the 64 24-bit seeds to n = 68, edge_lift24_68.out). Usage: edge_plateau_tail.py DIR."""
import re, collections, sys
def load(p):
    out=[]
    for line in open(p):
        m=re.search(r'seed=(\S+) E_n: (.*)',line)
        if m: out.append((m.group(1),[int(x) for x in m.group(2).split()]))
    return out
def runs(seqs,lo,hi):
    R=collections.Counter(); long=[]
    for s,E in seqs:
        d=[E[i]-E[i-1] for i in range(1,len(E))]; r=0; start=0
        for k in range(len(d)):
            n=k+1
            if n<lo or n>hi: continue
            if d[k]==0:
                if r==0: start=n
                r+=1
            else:
                if r: R[r]+=1
                if r>=8: long.append((s,E[start-1],start,start+r-1,r))
                r=0
        if r:
            R[r]+=1
            if r>=8: long.append((s,E[start-1],start,start+r-1,r,'cut'))
    return sorted(R.items()), long
for name,path,windows in [("A (48-bit seeds)",f"{sys.argv[1]}/edge_lift48.out",[(13,48),(49,60)]),("B (24-bit seeds)",f"{sys.argv[1]}/edge_lift24_68.out",[(13,56),(57,68),(13,68)])]:
    try: seqs=load(path)
    except FileNotFoundError: continue
    print(name, len(seqs), "seeds")
    for lo,hi in windows:
        R,long=runs(seqs,lo,hi); n=sum(c for _,c in R)
        print(f"  window {lo}..{hi}: runs {R}; total {n}; geometric expectation >=9: {n/512:.1f}")
        for L in long: print("    long:",L)
