# Saddle-point (Hildebrand-Tenenbaum) model of the one-cutoff smooth family (Lemma A):
# boundary 2 Psi(n,y) = Psi(nW,y) + Psi(nW/q,y); W_y solved per prime y, W_model = max_y W_y.
# All in logs so n can be astronomically large. HEURISTIC model; calibrated against exact L_simple.
import numpy as np, math, sys, time
t0=time.time()
def primes_upto(N):
    s=np.ones(N+1,bool); s[:2]=False
    for p in range(2,int(N**.5)+1):
        if s[p]: s[p*p::p]=False
    return np.nonzero(s)[0].astype(float)
PR=primes_upto(200000)
LP=np.log(PR)
def logpsi(X,k):  # X = log x, primes PR[:k]
    lp=LP[:k]
    lo,hi=1e-9,3.0
    for _ in range(70):
        a=(lo+hi)/2
        v=np.sum(lp/np.expm1(a*lp))
        if v>X: lo=a
        else: hi=a
    a=(lo+hi)/2
    pa=np.exp(a*lp)
    phi=-np.sum(np.log1p(-1/pa))
    phi2=np.sum(lp*lp*pa/(pa-1)**2)
    return a*X+phi-math.log(a)-0.5*math.log(2*math.pi*phi2)
def W_for(X,k):
    q=PR[k]  # next prime after y=PR[k-1]
    base=math.log(2)+logpsi(X,k)
    def F(w):  # log W = w ; returns log(Psi(nW)+Psi(nW/q)) - base
        a=logpsi(X+w,k); b=logpsi(X+w-math.log(q),k)
        m=max(a,b); return m+math.log(math.exp(a-m)+math.exp(b-m))-base
    lo,hi=0.0,1.0
    if F(lo)>0: return None
    while F(hi)<0:
        hi*=2
        if hi>60: return None
    for _ in range(60):
        mid=(lo+hi)/2
        if F(mid)<0: lo=mid
        else: hi=mid
    return math.exp(lo)
exps=[float(e) for e in sys.argv[1:]] or [4,5,6,6.69897,10,20,50,100,300,1000]
for e in exps:
    X=e*math.log(10)
    best=(0,None)
    # scan k (number of primes) over a range around the predicted optimum y ~ 4 log n/loglog n
    ypred=4*X/math.log(X)
    kmax=int(np.searchsorted(PR,4*ypred+50))
    stride=max(1,kmax//40)
    ks=list(range(2,kmax,stride))
    for k in ks:
        W=W_for(X,k)
        if W and W>best[0]: best=(W,int(PR[k-1])); kb=k
        if time.time()-t0>500: break
    for k in range(max(2,kb-stride),kb+stride+1):
        W=W_for(X,k)
        if W and W>best[0]: best=(W,int(PR[k-1]))
    W,y=best
    h=math.sqrt(X/math.log(X))
    print('n=10^%g  W_model=%.4f (y*=%d, 4logn/loglogn=%.0f)  L/n=%.4f  W/sqrt(l/ll)=%.4f  (2/sqrt e=1.2131)'%(e,W,y,ypred,W-1,W/h),flush=True)
