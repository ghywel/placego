import sys, math, collections
n=int(sys.argv[1]); fn=sys.argv[2]; f=int(sys.argv[3])
K=set(int(x) for x in open(fn))
def P(k):
    p=2; best=1
    while p*p<=k:
        while k%p==0: best=p; k//=p
        p+=1
    if k>1: best=max(best,k)
    return best
# compare K with smooth sets: for each y, smooth numbers in (min K, n]
kmin=min(K)
byP=collections.Counter(P(k) for k in K)
print('n',n,'f',f,'|K|',len(K),'minK',kmin,'n/minK=%.2f'%(n/kmin),'L/n=%.3f'%(f/n))
print('P(k) histogram:', sorted(byP.items()))
# for each prime y: how many y-smooth numbers in [kmin,n] are NOT in K, how many in K
ps=sorted(byP)
for y in ps:
    sm=[k for k in range(kmin,n+1) if P(k)<=y]
    inK=sum(1 for k in sm if k in K)
    print('y=%d smooth in [minK,n]: %d, of which in K: %d; K elements with P>y: %d'%(y,len(sm),inK,sum(1 for k in K if P(k)>y)))
# relation of P(k) with k: max P(k) as function of k-range
for a,b in [(kmin,2*kmin),(2*kmin,4*kmin),(4*kmin,n+1)]:
    sub=[k for k in K if a<=k<b]
    print('k in [%d,%d): count %d, maxP %d'%(a,b,len(sub),max(P(k) for k in sub) if sub else 0))
