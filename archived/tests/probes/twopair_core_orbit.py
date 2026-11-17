#!/usr/bin/env python3
"""Follow the rain episode maximisers: print rows at their least top, in the rain frame, and the top wall as a function of time."""
W=80
M=(1<<W)-1
def phi(x): return (x ^ ((x<<1)|(x<<2))) & M
def inv(y):
    x=y&1
    for j in range(1,W):
        a=(x>>(j-1))&1; b=(x>>(j-2))&1 if j>=2 else 0
        x|=(((y>>j)&1)^(a|b))<<j
    return x
def top(x):
    k=W-3
    while k>=1:
        if ((x>>k)&1)==((x>>(k+1))&1): return k
        k-=1
    return 0
def low(x):
    for k in range(1,W-2):
        if ((x>>k)&1)==((x>>(k+1))&1): return k
    return 0
def extend(x,w):
    """rain above bit w-1"""
    b=(x>>(w-1))&1
    for j in range(w,W):
        b^=1
        if b: x|=1<<j
    return x
def bits(x,n): return ''.join(str((x>>j)&1) for j in range(n))
for (start,k) in ((0x2c79f0f7,28),(0xb27d3f,22),(0x2c4a2f,21),(0x58e1309,25)):
    x=extend(start,k+2)
    tr=[];y=x
    for t in range(0,90):
        tr.append(top(y)); y=phi(y)
    m=min(tr);tm=tr.index(m)
    y=x
    for _ in range(tm): y=phi(y)
    print(hex(start),'k',k,'least top',m,'at',tm,'row at least top',bits(y,m+6),'low wall',low(y))
    print('  top(t):',tr[:80])
    z=y;back=[]
    for t in range(60):
        z=inv(z);back.append(top(z))
    print('  backward from least top:',back[:50])
