#!/usr/bin/env python3
"""rule30_cloud_solid_rows.py: the owner's question (2026-10-11 17:40 BST): can a Rule 30 pattern ever die, its bottom
row becoming one solid colour? The proof is three lines (CL363); this file is the brute-force companion for rings and
for finite patterns.

RUN-ON:     cpu (Python 3 standard library; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_solid_rows.py

PROPOSITION (proved in CL363 by the local rule alone). (i) The only rows that map to an all-white row are the all-white
row and the all-black row. (ii) The only rows that map to an all-black row are the three shifts of 100100... .
(iii) Hence no finite pattern (finitely many black cells) ever reaches a solid row of either colour, and the single-seed
pyramid never dies; its leftmost black cell survives and moves left one cell a step for ever. (iv) A finite pattern can
show a solid BLACK row across its support only one step after a seed 1(001)^j, giving 1^(3j+3), and such a row maps to
1 1 0^(m-1) 1, which restarts the pattern from two seeds; row 1 of the single-seed pyramid is the case j = 0.
(v) Infinite rows can die: all-black in one step, 100100... in two, and since Rule 30 is surjective there is a row that
dies at exactly step T for every T, all of them with infinitely many black cells until the end.

WHAT. Rings of size 3..14: the preimages of all-white and all-black, the set of rows that eventually die and the
longest death. Finite patterns: which solid rows 1^m have a finite preimage, whether those have one, and the image of a
solid row. Predictions (CL363): rings die beyond the trivial pair only when 3 divides the size (0.9); finite solid rows
only at m = 3j + 3 from 1(001)^j, with no earlier ancestor (0.85).
"""
import itertools
def step_ring(x):
    n=len(x); return tuple(x[(i-1)%n]^(x[i]|x[(i+1)%n]) for i in range(n))
print('rings: preimages of the two solid rows; rows that eventually die; longest death')
for n in range(3,15):
    img={}
    for x in itertools.product((0,1),repeat=n): img.setdefault(step_ring(x),[]).append(x)
    zero=(0,)*n; one=(1,)*n; pre0=img.get(zero,[]); pre1=img.get(one,[])
    basin={zero}; frontier=[zero]; depth={zero:0}
    while frontier:
        nxt=[]
        for y in frontier:
            for x in img.get(y,[]):
                if x not in basin: basin.add(x); depth[x]=depth[y]+1; nxt.append(x)
        frontier=nxt
    print('  n=%2d | preimages of all-white: %s | of all-black: %d | dying rows %d of %d | longest death %d steps'
          %(n,'all-white, all-black' if sorted(pre0)==sorted([zero,one]) else pre0,len(pre1),len(basin),2**n,
            max(depth.values())))
def step_fin(x):   # finite support, x[0] = x[-1] = 1; the support grows by one cell each side
    z=(0,0)+x+(0,0); return tuple(z[i-1]^(z[i]|z[i+1]) for i in range(1,len(z)-1))
print('finite patterns: solid rows 1^m with a finite preimage, and whether that preimage has one')
for m in range(3,16):
    pre=[x for x in itertools.product((0,1),repeat=m-2) if x and x[0]==1 and x[-1]==1 and step_fin(x)==(1,)*m]
    anc=0
    for x in pre:
        k=len(x)-2
        if k>=1: anc+=sum(1 for w in itertools.product((0,1),repeat=k) if w[0]==1 and w[-1]==1 and step_fin(w)==x)
    if pre: print('  m=%2d | preimages %s | ancestors of those: %d'%(m,[''.join(map(str,x)) for x in pre],anc))
print('image of a solid row 1^m, m = 3..6:',[''.join(map(str,step_fin((1,)*m))) for m in range(3,7)])
