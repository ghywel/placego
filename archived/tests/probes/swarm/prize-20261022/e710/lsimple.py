# Exact lower bound from the simple smooth family (PROOF-SKETCH lemma A in REPORT.md):
# for prime y with q = nextprime(y), K = {y-smooth k in [ceil((n+L)/q), n]} has every multiple in (n,n+L)
# y-smooth, so f(n) > L whenever #K > #{y-smooth m in [n+1, n+L-1]}.
import sys, time, numpy as np
t0=time.time()
ns=[int(x) for x in sys.argv[1:]]
YMAX=300
def primes_upto(N):
    s=np.ones(N+1,bool); s[:2]=False
    for p in range(2,int(N**.5)+1):
        if s[p]: s[p*p::p]=False
    return np.nonzero(s)[0]
P=[int(p) for p in primes_upto(YMAX+50)]
for n in ns:
    N=4*n+10
    rem=np.arange(N+1,dtype=np.int32); g=np.zeros(N+1,np.int16)
    for p in P:
        if p>YMAX: break
        g[p::p]=p
        pe=p
        while pe<=N:
            rem[pe::pe]//=p; pe*=p
    smooth=(rem==1)
    best=(0,None)
    for i,y in enumerate(P):
        if y>YMAX: break
        q=P[i+1]
        c=np.cumsum(smooth & (g<=y), dtype=np.int32)  # c[x] = #y-smooth in [1..x] (c[0]=0 since rem[0]=0)
        def viol(L):
            lo=-(-(n+L)//q)  # ceil
            A = c[n]-c[lo-1] if lo<=n else 0
            B = c[n+L-1]-c[n]
            return A>B
        if not viol(n): continue
        lo,hi=n,3*n
        if viol(hi): print('warn: violation at 3n for y',y); 
        while hi-lo>1:
            mid=(lo+hi)//2
            if viol(mid): lo=mid
            else: hi=mid
        if lo>best[0]: best=(lo,y)
        if time.time()-t0>500: print('TIME'); break
    Lb=best[0]+1
    print('n=%d L_simple=%d (y=%s) L_simple/n=%.4f'%(n,Lb,best[1],Lb/n), flush=True)
