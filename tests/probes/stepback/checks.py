#!/usr/bin/env python3
"""checks.py (Local, step back, 5 Nov 2026): exact truth tables of the row bits of Theta f over all free bits. Sideways recursion C_(k+1)(t) = C_k(t+1) xor (C_k(t) or C_(k-1)(t)), C_0 = 0, C_1 = a, a even = 1, a odd = free. Are the check bits (odd depths from 3) exactly balanced, and how independent are they?"""
import sys,math
m=int(sys.argv[1]) if len(sys.argv)>1 else 20
N=1<<m
ONES=(1<<N)-1
def var(i):
    # truth table of variable i over N assignments, as a big int
    blk=1<<i
    pat=((1<<blk)-1)<<blk
    period=2*blk
    v=0
    # doubling construction
    v=pat; w=period
    while w<N:
        v|=v<<w; w*=2
    return v&ONES
T=2*m+1              # columns times 0..T-1 use a_0..a_(T-1)
a=[]
for s in range(T):
    if s%2==0: a.append(ONES)
    else: a.append(var((s-1)//2))
prev=[0]*(T+1)      # C_0
cur=a+[None]        # C_1
bits={1:cur[0]}
for k in range(1,T):
    nxt=[None]*(T+1)
    L=T-k
    for t in range(L):
        nxt[t]=cur[t+1]^(cur[t]|prev[t])
    prev,cur=cur,nxt
    bits[k+1]=cur[0]
pc=lambda x:bin(x).count('1')
print('m',m)
chk=[]
for d in range(3,T+1,2):
    n=d//2           # free bits it can depend on: f_0..f_(n-1)
    # count over the n relevant variables exactly: total ones / 2^(m-n)
    c=pc(bits[d])>>(m-n)
    chk.append((d,n,c,(1<<n)))
    print('depth',d,'vars',n,'ones',c,'of',1<<n,'share',round(c/(1<<n),5),'excess from half',c-(1<<(n-1)))
# pairwise correlation among checks at the top
ks=[d for d in range(3,T+1,2)]
worst=[]
for i,d in enumerate(ks[-10:]):
    for e in ks[-10:][i+1:]:
        x=bits[d]^bits[e]
        worst.append((abs(pc(x)/N-.5),d,e,round(pc(x)/N,5)))
worst.sort(reverse=True)
print('largest pair biases among the last ten checks',worst[:5])
# number of assignments with all checks from depth d0 on white, against 2^(m-count)
for d0 in (m,m+4,m+8,m+12):
    if d0%2==0: d0+=1
    s=ONES;c=0
    for d in range(d0,T+1,2):
        s&=~bits[d]&ONES; c+=1
    print('all checks white from depth',d0,': count',pc(s),'of',N,'; fair expectation',N/2**c)
