#!/usr/bin/env python3
"""verify_witness.py (Local, L1538): checks a witness row directly, with no solver: forward ticks give its past letters; inverse ticks keep it in the lock; and its past rows' top cells are looked up in the terminal cloud of E(92)."""
import json,sys
from collections import defaultdict
fn=sys.argv[1]; ticks=int(sys.argv[2])
d=json.load(open(fn)); y=d['y0_by_offset']; W=d['W']; K=len(y); Sb=d['S']; L=d['L']
lockset={l.strip() for l in open('lock175.txt') if l.strip()}
# a full row: anchor, white padding, cells low to high, rain above
pad=8
low=[1]+[0]*pad
cells=y[::-1]                    # low..high, top two cells are the wall pair
N=len(low)+K+3*ticks+64
row=low+cells
b=row[-1]
while len(row)<N:
    b^=1; row.append(b)
x=sum(1<<i for i,c in enumerate(row) if c)
MASK=(1<<N)-1
top=len(low)+K-2                # deep cell of the wall pair, index
def fwd(x): return (x^((x<<1)|(x<<2)))&MASK
def inv(y):
    o=0;p1=1;p2=0
    r=y&1
    for j in range(1,N):
        c=((y>>j)&1)^(p1|p2); r|=c<<j; p2=p1;p1=c
    return r
def letter(x,d):
    t=[(x>>(d+1-k))&1 for k in range(11)]
    return 'A' if t==[1,1,0,0,0,1,1,1,1,0,0] else 'B' if t==[1,1,0,0,0,1,1,1,0,1,0] else '?'
def word(x,d,w): return ''.join('#' if (x>>(d+1-(w-1)+i))&1 else '.' for i in range(w))
print('y_0 in the lock:',word(x,top,175) in lockset)
xs=[x]; ds=[top]; lets=letter(x,top)
c=x; dd=top
for s in range(1,L+1):
    c=fwd(c); dd-=3; xs.append(c); ds.append(dd); lets=letter(c,dd)+lets
print('past letters oldest first:',lets)
print('y_1 outside the lock:',word(xs[1],ds[1],175) not in lockset)
# cloud membership of past rows
for w in (92,):
    V={};part=[];term=[]
    for i,l in enumerate(open(f'E{w}.txt')):
        h,p,t,cy,a,b2,c2,d2=l.split(); V[int(h,16)]=i; part.append(int(p)); term.append(int(t))
    size=defaultdict(int)
    for p in part: size[p]+=1
    cloud=max({part[i] for i in range(len(part)) if term[i]},key=lambda p:size[p])
    res=[]
    for s in range(Sb-4,min(L-16,Sb+40)):
        v=sum(((xs[s]>>(ds[s]+1-(w-1)+i))&1)<<i for i in range(w))
        i=V.get(v)
        res.append('C' if i is not None and part[i]==cloud else '.' if i is None else 'p')
    print(f'past rows from tick {Sb-4}, top {w} cells: C in the terminal cloud, p another part, . outside E:',''.join(res))
# future
c=x;dd=top;ok=0
for t in range(ticks):
    c=inv(c);dd+=3
    if word(c,dd,175) in lockset: ok+=1
    else:
        print('left the lock at',t);break
print('future ticks in the lock:',ok,'of',ticks)
