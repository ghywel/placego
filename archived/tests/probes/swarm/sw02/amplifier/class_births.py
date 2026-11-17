# M(W): distinct rows at late ticks among rows of exact width W. m(W) = M(W) - M(W-1). Exact integers, dedup every 8 ticks.
import sys,time
def F(y): return (y>>1)^(y|(y<<1))
TMAX=int(sys.argv[2]); prev=0
for W in range(1,int(sys.argv[1])+1):
    ys=set(range(1<<(W-1),1<<W)) if W>1 else {1}
    t=0;last=0;t0=time.time();mid=None
    while t<TMAX:
        n=len(ys); nx=set()
        for y in ys:
            z=y
            for _ in range(8): z=F(z)
            nx.add(z)
        t+=8
        if len(nx)<n: last=t
        ys=nx
        if mid is None and t>=TMAX//2: mid=len(ys)
    M=len(ys)
    import math
    print('W',W,'M',M,'m',M-prev,'log2M/W',round(math.log2(M)/W,4),'last merge by',last,'at T/2',mid,'sec',round(time.time()-t0,1),flush=True)
    prev=M
