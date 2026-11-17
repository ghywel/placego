# L_simple(n) (Lemma A, best prime y <= 60) for every n <= 10^4, against exact f(n) from allf.txt
import numpy as np, time
t0=time.time()
rows=[tuple(map(int,l.split())) for l in open('allf.txt') if l.strip() and l[0].isdigit()]
F=dict(rows); NMAX=10000; N=4*NMAX+10
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
rem=np.arange(N+1,dtype=np.int64); g=np.zeros(N+1,np.int16)
for p in P:
    g[p::p]=p; pe=p
    while pe<=N: rem[pe::pe]//=p; pe*=p
sm=(rem==1)
C={y:np.cumsum(sm&(g<=y)) for y in P[:-1]}
out=[]
for n in range(20,NMAX+1):
    best=0;by=None
    for i,y in enumerate(P[:-1]):
        q=P[i+1]; c=C[y]
        def viol(L):
            lo=-(-(n+L)//q); A=c[n]-c[lo-1] if lo<=n else 0
            return A > c[n+L-1]-c[n]
        if not viol(n): continue
        lo,hi=n,3*n
        while hi-lo>1:
            mid=(lo+hi)//2
            if viol(mid): lo=mid
            else: hi=mid
        if lo>best: best=lo;by=y
    Ls=best+1; out.append((n,F[n],Ls,by))
r=np.array([f/L for n,f,L,y in out]); W=np.array([(n+f)/(n+L) for n,f,L,y in out])
ns=np.array([o[0] for o in out])
for a,b in [(20,100),(100,1000),(1000,3000),(3000,10001)]:
    s=(ns>=a)&(ns<b)
    print('n in [%d,%d): f/L_simple min %.4f mean %.4f max %.4f | (n+f)/(n+L_s) mean %.4f'%(a,b,r[s].min(),r[s].mean(),r[s].max(),W[s].mean()))
print('global min ratio at n=%d: %s'%(ns[r.argmin()], out[r.argmin()]))
print('L_simple > f anywhere (would be a bug):', int(np.sum(r<1)))
print('secs %.0f'%(time.time()-t0))
