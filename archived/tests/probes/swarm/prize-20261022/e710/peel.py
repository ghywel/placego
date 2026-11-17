# Refined family by peeling: start from Lemma A's region S_y ∩ [ceil((n+L)/q), n] and repeatedly delete any k
# with >= 2 private multiples (multiples in (n,n+L) that no other member divides). Report deficiency |K|-|N(K)|.
import sys, collections, math
def gpf_sieve(N):
    g=list(range(N+1))
    sp=[0]*(N+1)
    for p in range(2,N+1):
        if sp[p]==0:
            for q in range(p,N+1,p):
                if sp[q]==0: sp[q]=p
    # largest prime factor
    P=[1]*(N+1)
    for x in range(2,N+1):
        p=sp[x]; P[x]=max(p,P[x//p])
    return P
def nextprime(y):
    z=y+1
    while any(z%d==0 for d in range(2,int(z**.5)+1)): z+=1
    return z
n=int(sys.argv[1]); f=int(sys.argv[2])
P=gpf_sieve(n+f+5)
def run(L,y):
    q=nextprime(y); lo=-(-(n+L)//q)
    K=set(k for k in range(lo,n+1) if P[k]<=y)
    mult={k:[x for x in range((n//k+1)*k, n+L, k)] for k in K}
    cnt=collections.Counter(x for k in K for x in mult[k])
    changed=True
    while changed:
        changed=False
        for k in list(K):
            priv=sum(1 for x in mult[k] if cnt[x]==1)
            if priv>=2:
                K.discard(k)
                for x in mult[k]:
                    cnt[x]-=1
                    if cnt[x]==0: del cnt[x]
                changed=True
    return len(K)-len(cnt), len(K)
for y in [int(a) for a in sys.argv[3:]]:
    D,ks=run(f-1,y)
    print('n=%d L=f-1 y=%d: peeled |K|=%d deficiency=%d'%(n,y,ks,D))
    # find largest L with deficiency>=1 by scanning down in steps
    lo_L=None
    for L in range(f-1, f-1-int(0.12*f), -max(1,f//400)):
        D,_=run(L,y)
        if D>=1: lo_L=L; break
    print('   largest scanned L with peeled deficiency>=1: %s  (f=%d, ratio f/(L+1)=%s)'%(lo_L,f, '%.4f'%(f/(lo_L+1)) if lo_L else None))
