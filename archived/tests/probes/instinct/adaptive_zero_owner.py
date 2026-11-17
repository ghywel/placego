#!/usr/bin/env python3
"""MI386/B198: fixed protected low-shape adaptive zero-owner diagnostic.

M11..16, all p and sorted sizes>=3; literal maps through M13.
Predictions/controls/counterfactuals in MI386. 20 CPU second cap;
stop at first scalar/exception-only failure, no automatic retry.
JSON stdout is raw data and belongs outside git.
"""
import itertools as it
import json
import time
from functools import lru_cache

START = time.process_time()
REPORT = {'status': 'RUNNING', 'domains': 0, 'targets': 0,
          'strict_pair_targets': 0, 'literal_domains': 0,
          'literal_targets': 0, 'scalar_owner_false_positives': 0,
          'nonexception_owner_false_positives': 0, 'owner_histogram': {},
          'first_scalar_owner_false_positive': None}


def budget():
    if time.process_time()-START > 20:
        raise TimeoutError('20 CPU second cap; partial only; no retry')


def L(r):
    return r*(r-1)//2


def bounds(M,p,r,k):
    l=r-k
    return 2*r+p*k+L(l)+L(k), (p-1)*l-L(l)+M*k-L(k)


@lru_cache(None)
def counts(M,p,r,u):
    P,Q=p-2,M-p-1
    return tuple(k for k in range(max(0,r-P),min(r,Q)+1)
                 if bounds(M,p,r,k)[0]<=u<=bounds(M,p,r,k)[1])


def exceptional(l,k):
    for row,other in ((l,k),(k,l)):
        support=[i for i in range(3) if row[i]]
        if len(support)==1:
            h=support[0]
            if other[h]==1 and min(other[i] for i in range(3) if i!=h)>=2:
                return True
    return False


def admissions(M,p,s,u):
    Q=M-p-1
    scalar,good,detail=set(),set(),[]
    for owner in range(3):
        r=tuple(x-(i==owner) for i,x in enumerate(s))
        K=tuple(counts(M,p,x,y) for x,y in zip(r,u))
        detail.append(K)
        if not all(K) or sum(x[0] for x in K)>Q or sum(x[-1] for x in K)<Q:
            continue
        scalar.add(owner)
        for k0 in K[0]:
            for k1 in K[1]:
                k=(k0,k1,Q-k0-k1)
                if k[2] not in K[2]:
                    continue
                l=tuple(x-y for x,y in zip(r,k))
                if not exceptional(l,k):
                    good.add(owner)
                    break
            if owner in good:
                break
    return scalar,good,detail


def literal(M,p,s):
    values=tuple(x for x in range(M+1) if x not in (1,p,p+1))
    total=sum(values)
    out={}
    for A in it.combinations(values,s[0]):
        sa=sum(A)
        left=tuple(x for x in values if x not in A)
        for B in it.combinations(left,s[1]):
            sb=sum(B)
            owner=0 if 0 in A else (1 if 0 in B else 2)
            out.setdefault((sa,sb,total-sa-sb),set()).add(owner)
        budget()
    return out


def endpoint_control(M,p,s):
    values=tuple(x for x in range(2,M+1) if x not in (p,p+1))
    for r in sorted(set(s)|{x-1 for x in s}):
        observed={}
        for B in it.combinations(values,r):
            k=sum(x>=p+2 for x in B)
            observed.setdefault(k,[]).append(sum(B))
        for k,totals in observed.items():
            assert bounds(M,p,r,k)==(min(totals),max(totals))
        budget()


def control():
    fixtures=[(11,5,(3,3,3),(16,19,19),
               ((2,3,11),(0,9,10),(4,7,8))),
              (15,3,(5,5,3),(37,38,37),
               ((0,5,7,11,14),(2,6,8,9,13),(10,12,15)))]
    for M,p,s,u,parts in fixtures:
        assert tuple(map(len,parts))==s and tuple(map(sum,parts))==u
        assert sorted(x for B in parts for x in B)==[x for x in range(M+1) if x not in (1,p,p+1)]
        scalar,good,_=admissions(M,p,s,u)
        owner=next(i for i,B in enumerate(parts) if 0 in B)
        assert owner in scalar
        if M==11:
            assert 0 not in scalar
        else:
            assert 2 not in scalar
        for perm in it.permutations(range(3)):
            sp=tuple(s[i] for i in perm);up=tuple(u[i] for i in perm)
            spass,gpass,_=admissions(M,p,sp,up)
            assert spass=={i for i,j in enumerate(perm) if j in scalar}
            assert gpass=={i for i,j in enumerate(perm) if j in good}
    REPORT['controls']='two literal positives, forced-root negatives, all label permutations PASS'


def main():
    control()
    for M in range(11,17):
        n=M-2
        for p in range(2,M-1):
            total=sum(x for x in range(M+1) if x not in (1,p,p+1))
            for a in range(3,n//3+1):
                for b in range(a,(n-a)//2+1):
                    s=(a,b,n-a-b)
                    low=tuple(L(x)+3*x for x in s)
                    high=tuple(total-L(n-x)-3*(n-x) for x in s)
                    actual=None
                    if M<=13:
                        actual=literal(M,p,s)
                        endpoint_control(M,p,s)
                        REPORT['literal_domains']+=1
                    for u0 in range(low[0],high[0]+1):
                        for u1 in range(low[1],high[1]+1):
                            u=(u0,u1,total-u0-u1)
                            if not low[2]<=u[2]<=high[2]:
                                continue
                            scalar,good,detail=admissions(M,p,s,u)
                            REPORT['targets']+=1
                            singles=[x-y for x,y in zip(u,low)]
                            pairs=[total-u[i]-L(n-s[i])-3*(n-s[i]) for i in range(3)]
                            REPORT['strict_pair_targets']+=min(pairs)<min(singles)
                            h=str(len(scalar))
                            REPORT['owner_histogram'][h]=REPORT['owner_histogram'].get(h,0)+1
                            case={'M':M,'p':p,'sizes':s,'targets':u,'K_by_owner':detail,
                                  'scalar_owners':sorted(scalar),'nonexception_owners':sorted(good)}
                            if actual is not None:
                                owners=actual.get(u,set())
                                REPORT['literal_targets']+=1
                                assert owners<=scalar, ('necessary admission failed',case)
                                false_scalar=scalar-owners
                                false_good=good-owners
                                REPORT['scalar_owner_false_positives']+=len(false_scalar)
                                REPORT['nonexception_owner_false_positives']+=len(false_good)
                                if false_scalar and REPORT['first_scalar_owner_false_positive'] is None:
                                    REPORT['first_scalar_owner_false_positive']={**case,'actual_owners':sorted(owners)}
                                if false_good or not owners:
                                    REPORT['failure']={**case,'actual_owners':sorted(owners)}
                                    REPORT['status']='ACTUAL_FAILURE'
                                    return
                            if not scalar or not good:
                                if actual is None:
                                    actual=literal(M,p,s)
                                REPORT['failure']={**case,'actual_owners':sorted(actual.get(u,set()))}
                                REPORT['status']='SCALAR_FAILURE' if not scalar else 'EXCEPTION_ONLY'
                                return
                            budget()
                    REPORT['domains']+=1
    REPORT['status']='COMPLETE'


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        REPORT['status']='PARTIAL_OR_CONTROL_FAILURE'
        REPORT['error']=repr(exc)
    finally:
        REPORT['cpu_seconds']=time.process_time()-START
        print(json.dumps(REPORT,sort_keys=True))
