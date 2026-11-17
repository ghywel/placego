"""CL490: exhaustive check of the exact depth>=3 gap list after <=3 deletions (N 10..22, k 3..6). OUTCOME: 35,328 (pool,k) cases; 4 gaps outside the literal list, all the k=3 {4,5,6} depth-4 pattern seen through complementation k <-> n-k; with that symmetry, 0 outside."""
# Check the conjectured exact list for depth>=3 gaps (k-sums, <=3 internal deletions, n>=7), N up to 22, k<=6
import itertools
def sig(R,k):
    s=set()
    for c in itertools.combinations(R,k): s.add(sum(c))
    return s
pats=lambda k: [ {k-2,k+2,k+3}, {k-1,k,k+4}, {k-1,k+1,k+3}, {k,k+1,k+2} ]
bad=0; n_checked=0
for N in range(10,23):
    for d in (0,1,2,3):
        for D in itertools.combinations(range(1,N),d):
            R=[x for x in range(N+1) if x not in D]; n=len(R)
            if n<7: continue
            for k in range(3,min(6,n-3)+1):
                s=sig(R,k); a,b=min(s),max(s); n_checked+=1
                for v in range(a+3,b-2):
                    if v in s: continue
                    dl,du=v-a,b-v
                    Dset=set(D)
                    if dl<=du:
                        ok = (dl==3 and any(p<=Dset for p in pats(k)) and len(Dset)==3 and Dset in pats(k)) or (dl==4 and k==3 and Dset=={4,5,6})
                    else:
                        Dr={N-x for x in D}
                        ok = (du==3 and Dr in pats(k)) or (du==4 and k==3 and Dr=={4,5,6})
                    if not ok:
                        bad+=1
                        if bad<=5: print('outside list:',N,D,k,v,'depths',dl,du)
print('checked',n_checked,'(pool,k) cases; gaps outside the list:',bad)
