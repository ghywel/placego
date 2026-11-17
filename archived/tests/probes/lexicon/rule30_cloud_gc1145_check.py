#!/usr/bin/env python3
"""rule30_cloud_gc1145_check.py: Cloud's independent second read of GPT's GC1145 (the original white-A source
1110100011011 on its high-111 branch has only two possible first thirteen cells at tick 16: 1110011111110 on the 676
non-LL source-25 assignments and 1110011111000 on the 28 high-LL ones), own code (CL342).

RUN-ON:     cpu (Python 3 standard library; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1145_check.py

WHAT. For all 4,096 source-25 assignments of sites 14..25 and all 16 completions of sites 26..29 (the 13 cells at tick
16 depend on exactly the 29 cells at tick 0, so this is the complete statement for every tail), the 13-cell image at 16,
grouped by GC1136's selector (LL) and by whether the image begins 111001111 (high). Also an own fresh-right certificate
cover from the 13-cell white-A root, splitting the next source bit until the 13 cells at 16 are known (or 9 are known
and not high): leaves and dyadic weights per image.

PREDICTIONS (written before the run, in Cloud's scratch): every one of the 676 non-LL high sources gives 1110011111110
and every one of the 28 LL sources gives 1110011111000 for all 16 completions (0.8); the 3,392 C sources give images
beginning 111001010 or 111001100 (0.9). Counterfactual: an image that varies with sites 26..29, or a non-LL source with
the LL image, refutes GC1145. Unexpected check: the full image distribution and whether GC1144's pin 1110011110100 is
ever a tick-16 image of a white-A origin.

RESULT (CL342): both predictions held; no image varies with sites 26..29; the C sources give thirteen images, all
beginning 111001010 or 111001100; the pin never appears. The own cover has 37 leaves of weight 676 for 1110011111110
and 9 leaves of weight 28 for 1110011111000, GPT's 46 high-branch leaves (its 81 nodes count only the eleven high
roots)."""
import itertools
from collections import Counter
B=lambda s: tuple(int(c) for c in s)
def fwd(x,left):
    f=[left]+list(x); return tuple(f[i-1]^(f[i]|f[i+1]) for i in range(1,len(f)-1))
def run(start,n):
    rows=[tuple(start)]
    for t in range(n): rows.append(fwd(rows[-1],t%2))
    return rows
def family(s):
    a,b,c,d,e,f,g,h,i,j,k,l=s
    f1=(a,b,c,d,e,f)==(0,1,1,0,1,1) and ((g==1 and h==1 and i==0 and j==0) or (g==1 and h==0 and (i or j)==1)
        or (g==0 and h==1 and i==0 and j==0 and (k or l)==1))
    f2=(a,b,c,d,e,f,g,h)==(0,1,1,1,0,0,0,0) and (((i^j)==1) or (i==1 and j==1 and k==0 and l==0))
    return f1 or f2
WA=B('1110100011011')
by_class=Counter(); varies=0; allimg=Counter(); pin=0
for far in itertools.product((0,1),repeat=12):
    imgs=set()
    for ext in itertools.product((0,1),repeat=4):
        r=run(WA+far+ext,16)[16]; imgs.add(''.join(map(str,r[:13])))
    for w in imgs: allimg[w]+=1
    high=all(w[:9]=='111001111' for w in imgs)
    cls='LL' if family(far) else ('nonLL-high' if high else 'C')
    if len(imgs)>1: varies+=1
    by_class[(cls,tuple(sorted(imgs)))]+=1
    if '1110011110100' in imgs: pin+=1
print('sources whose 13-cell image at 16 varies with sites 26..29:',varies)
for (cls,imgs),n in sorted(by_class.items(),key=lambda kv:(-kv[1])):
    print('  %-11s %5d  images %s'%(cls,n,' '.join(imgs)))
print('GC1144 pin 1110011110100 as a tick-16 image of a white-A origin:',pin)
# an own all-tail cover with the fresh-right certificate: leaf when the first 13 cells at 16 are known, or 9 known and
# not high
def certificate(src,steps):
    rows=[tuple(src)]
    for t in range(steps):
        old=rows[-1]
        if not old: rows.append(()); continue
        new=fwd(old,t%2)
        if old[-1]==1: new=new+(((old[-2] if len(old)>1 else t%2)^1),)
        rows.append(new)
    return rows
from fractions import Fraction
nodes=0; leaves=Counter(); weights=Counter(); stack=[WA]
while stack:
    src=stack.pop(); nodes+=1; r=certificate(src,16)[16]
    w=Fraction(1,1<<(len(src)-13))
    if len(r)>=13:
        k=''.join(map(str,r[:13])); leaves[k]+=1; weights[k]+=w
    elif len(r)>=9 and r[:9]!=B('111001111'):
        k='C:'+''.join(map(str,r[:9])); leaves[k]+=1; weights[k]+=w
    else: stack.extend([src+(1,),src+(0,)])
print('own cover: nodes',nodes,'leaves',sum(leaves.values()),'(GPT 81 nodes, 46 leaves)')
for k,v in sorted(weights.items(),key=lambda kv:-kv[1]):
    print('  leaf class %-16s leaves %3d  weight x 4096 = %s'%(k,leaves[k],v*4096))
