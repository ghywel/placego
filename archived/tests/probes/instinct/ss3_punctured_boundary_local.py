#!/usr/bin/env python3
"""MI420/B217 fixed construction diagnostic; NOT RUN at registration.
Domain only n14,sizes(3,3,4,4),q1..13;strict minimum pair AB,
no singleton/triple minimum. Canonical MI419 moment pool plus ALL ONE
neutral two-for-two physical boundary exchanges. No closure iteration.
Prediction: canonical fails known q1 controls; expect at least one admitted
target outside the one-exchange family. A complete pass refutes that forecast,
not proves the infinite selector. Counterfactual: a local failure with a full
partition rejects only this construction restriction.
Controls: DP spectra versus literal combinations for every tested family pool;
independent Ferrers staircase and physical moment check; original fourteen cuts;
known q1 h5/h7 repaired and q3 skip fixed. Unexpected: MI350 unprotected
4/18/18/32 example passes all-union feasibility yet must fail protected admission
and independent partition search. On first family failure, complete boundary
oracle and independent recursive original-value allocator must agree.
Stop: one invocation,first local failure (after classifying it),any disagreement,
20 CPU/30 wall seconds,256MiB RSS. No patch/retry,domain or cap increase.
Raw output outside git. Standard Python CPU only. No parent coverage estimate.
"""
import itertools as it
import json, math, resource, sys, time
from functools import lru_cache
T0=time.process_time();W0=time.monotonic()
COUNTS={'moment_pools':0,'family_pools':0,'spectra':0,'targets':0,'canonical_failed':0}
def budget():
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin': rss*=1024
    if time.process_time()-T0>20 or time.monotonic()-W0>30 or rss>256*1024*1024:
        raise RuntimeError('CAP UNKNOWN')
def L(k):return k*(k-1)//2
def staircase(m,H):
    if H==0:return tuple(range(m))
    k=0
    while (k+1)*(k+2)//2<=H:k+=1
    t=H-k*(k+1)//2;p=m-k
    P=tuple(range(p))+tuple(p+2*j+1+(j>=k-t) for j in range(k))
    kr=(math.isqrt(8*H+1)-1)//2;tr=H-kr*(kr+1)//2
    rows=[kr-j+(j<tr) for j in range(kr)]
    shifts=[0]*(m-kr)+list(reversed(rows))
    assert P==tuple(i+d for i,d in enumerate(shifts))
    return P

def boundary(q,h):
    old=None
    for H in range(h+min(q,6)+1):
        P=staircase(6,H);g=H-sum(i<q for i in P)
        if g>=h:
            if g>h:
                assert g==h+1 and old is not None
                R=set(old);p=0
                while p in R:p+=1
                v=p-1 if q!=p else max(R)
                assert v+1 not in R and (v<q)==(v+1<q)
                R.remove(v);R.add(v+1)
            else:R=set(P)
            U=tuple(sorted(i+(i>=q) for i in R))
            assert len(U)==6 and len(set(U))==6 and q not in U
            assert min(U)>=0 and max(U)<=14 and sum(U)==21+h
            return U
        old=P
    raise AssertionError('moment failed')

def spec(P,k):
    d=[{0}]+[set() for _ in range(k)]
    for v in reversed(P):
        for j in range(k,0,-1):d[j].update(s+v for s in d[j-1])
    direct={sum(c) for c in it.combinations(P,k)}
    assert d[k]==direct
    COUNTS['spectra']+=1
    return d[k]

def family(S,U):
    V=sorted(set(S)-set(U));pairs={}
    for p in it.combinations(V,2):pairs.setdefault(sum(p),[]).append(p)
    out={U}
    for p in it.combinations(U,2):
        for v in pairs.get(sum(p),[]):
            out.add(tuple(sorted((set(U)-set(p))|set(v))))
    return sorted(out)

def cuts(sizes,targets,strict=True):
    ds=[]
    for mask in range(1,15):
        r=sum(sizes[i] for i in range(4) if mask>>i&1)
        u=sum(targets[i] for i in range(4) if mask>>i&1)
        ds.append((mask,u-L(r)-r))
    h=dict(ds)[3]
    return h>=0 and all(d>=h for _,d in ds) and (not strict or all(d>h for mask,d in ds if mask.bit_count() in (1,3)))

def literal(S,sizes,targets,U):
    for A in it.combinations(U,sizes[0]):
        if sum(A)!=targets[0]:continue
        B=tuple(sorted(set(U)-set(A)));V=tuple(sorted(set(S)-set(U)))
        for C in it.combinations(V,sizes[2]):
            if sum(C)!=targets[2]:continue
            D=tuple(sorted(set(V)-set(C)));part=(A,B,C,D)
            assert sorted(v for b in part for v in b)==list(S)
            assert tuple(map(len,part))==sizes and tuple(map(sum,part))==targets
            return part
    return None

def all_boundary(S,sizes,targets):
    for U in it.combinations(S,sizes[0]+sizes[1]):
        budget()
        if sum(U)==targets[0]+targets[1]:
            part=literal(S,sizes,targets,U)
            if part:return part
    return None

def allocator(S,sizes,targets):
    # Assign original values descending to named bins; no boundary or spectrum code.
    vals=tuple(reversed(S))
    @lru_cache(None)
    def rec(i,counts,sums):
        budget()
        if i==len(vals):return () if not any(counts) and not any(sums) else None
        if any(c<0 or s<0 for c,s in zip(counts,sums)):return None
        v=vals[i]
        for j in range(4):
            if not counts[j] or sums[j]<v:continue
            cc=list(counts);ss=list(sums);cc[j]-=1;ss[j]-=v
            # Independent actual remaining-extrema bounds.
            rem=vals[i+1:]
            if any(c>len(rem) or (c==0 and s!=0) or
                   (c>0 and not(sum(rem[-c:])<=s<=sum(rem[:c]))) for c,s in zip(cc,ss)):continue
            ans=rec(i+1,tuple(cc),tuple(ss))
            if ans is not None:return (j,)+ans
        return None
    ans=rec(0,sizes,targets)
    if ans is None:return None
    part=tuple(tuple(sorted(v for v,jj in zip(vals,ans) if jj==j)) for j in range(4))
    assert tuple(map(sum,part))==targets and tuple(map(len,part))==sizes
    return part

def run():
    sizes=(3,3,4,4)
    # All-union feasibility is weaker than protected admission.
    negS=tuple(v for v in range(13) if v!=6);negT=(4,18,18,32);negC=(3,3,3,3)
    for mask in range(1,15):
        r=sum(negC[i] for i in range(4) if mask>>i&1)
        u=sum(negT[i] for i in range(4) if mask>>i&1)
        assert u in spec(negS,r)
    assert not cuts(negC,negT)
    assert all_boundary(negS,negC,negT) is None and allocator(negS,negC,negT) is None
    for q,h,x,z,baseok in [(1,5,7,11,False),(1,7,8,12,False),(3,7,8,13,True)]:
        S=tuple(v for v in range(15) if v!=q);U=boundary(q,h)
        targets=(6+x,15+h-x,50-z,34-q-h+z)
        assert cuts(sizes,targets)
        assert (literal(S,sizes,targets,U) is not None)==baseok
        assert any(literal(S,sizes,targets,R) for R in family(S,U))
    print(json.dumps({'controls':'PASS'}),flush=True)
    for q in range(1,14):
        S=tuple(v for v in range(15) if v!=q)
        for h in range(0,min(7,14-q)+1):
            budget();U=boundary(q,h);COUNTS['moment_pools']+=1
            fs=family(S,U);COUNTS['family_pools']+=len(fs)
            spectra=[]
            for R in fs:
                assert sum(R)==sum(U) and len(R)==6 and set(R)<=set(S)
                spectra.append((R,spec(R,3),spec(tuple(sorted(set(S)-set(R))),4)))
            base=next(t for t in spectra if t[0]==U)
            for x in range(h+1,9):
                for z in range(h+q+1,16):
                    targets=(6+x,15+h-x,50-z,34-q-h+z)
                    assert sum(targets)==sum(S)
                    if not cuts(sizes,targets):continue
                    COUNTS['targets']+=1
                    if targets[0] not in base[1] or targets[2] not in base[2]:COUNTS['canonical_failed']+=1
                    good=next((R for R,sa,sc in spectra if targets[0] in sa and targets[2] in sc),None)
                    if good is not None:
                        assert literal(S,sizes,targets,good)
                    else:
                        oracle=all_boundary(S,sizes,targets);ind=allocator(S,sizes,targets)
                        assert (oracle is None)==(ind is None)
                        return {'status':'LOCAL_FAMILY_FAILED','q':q,'h':h,'x':x,'z':z,
                            'targets':targets,'base':U,'family_size':len(fs),
                            'global_witness':oracle,'independent_witness':ind,'counts':COUNTS}
    return {'status':'COMPLETE_FIXED_DOMAIN_PASS','counts':COUNTS}
try:
    result=run()
except Exception as e:
    result={'status':'INSTRUMENT_FAILED_OR_CAP','error':str(e),'counts':COUNTS}
result['cpu_seconds']=time.process_time()-T0
print(json.dumps(result,sort_keys=True),flush=True)
