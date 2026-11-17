#!/usr/bin/env python3
"""B66/MI153: count-only parity/cardinality model, no constructive search.

Preregistered fe3413be, pre-run control correction52031895.256 parity patterns,
E28 offset totals240/192, independent gap-DP/Gaussian staircase instruments,
direct parity-count marginal DP, exhaustive tiny controls.10CPU sec/256MiB.
Forecast q4 largest, all even q present, mixed>98%, some same-total reversal
mismatch. Necessary cardinality vectors and sufficient split-anchor model in
MI153; no claim of its completeness, anchor placement or partition existence.
Raw outside git. Original too-small negative control retained, not hidden.
OUTCOME: all256 patterns counted (128 nonzero), total24688633; q0/2/4/6/8:
326119/6040756/12680918/5382660/258180. Both pattern algorithms, direct full
q marginals and1650 literal tiny checks agree.102 same-total reversal mismatches.
All forecasts pass.0.085802CPU seconds,12480512bytes peakRSS. Full raw SHA256
104dba0c6e38900f1c1c3fe3f14663dd5b98cbe435b3191816d000c001a30ae8.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement,product
from math import comb
import json
import resource
import signal
import time
from path_forest_exceptional_counts import gaussian_coefficients

START=time.process_time()


def guard(*_):
    if time.process_time()-START>10:raise RuntimeError('CPU_CAP')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:
        raise RuntimeError('RSS_CAP')


@lru_cache(None)
def coefficients(k,bound):
    # Coefficient of u^n v^s in product_(w=1..k)(1-u*v^w)^-1.
    parts=bound//2;degree=k*bound//2
    dp=[[0]*(degree+1) for _ in range(parts+1)];dp[0][0]=1
    for w in range(1,k+1):
        for n in range(1,parts+1):
            for s in range(w,degree+1):dp[n][s]+=dp[n-1][s-w]
    for n in range(1,parts+1):
        for s in range(degree+1):dp[n][s]+=dp[n-1][s]
    guard();return dp


def gaps(k,bound,total,p):
    b=[p[i]^(p[i-1] if i else 0) for i in range(k)]
    residual=total-sum((k-i)*x for i,x in enumerate(b))
    B=(bound-sum(b))//2
    if residual%2 or residual<0 or B<0:return 0
    T=residual//2;table=coefficients(k,bound)
    return table[B][T] if T<len(table[B]) else 0


def staircase(k,bound,total,p):
    q=sum(p)
    if (total-q)%2:return 0
    descents=[];d=0
    for i in range(k):
        if i and p[i-1]>p[i]:d+=1
        descents.append(d)
    H=(bound-p[-1])//2-d
    S=(total-q)//2-sum(descents)
    if H<0 or S<0 or S>k*H:return 0
    return gaussian_coefficients(k,H,S)[S]


def direct_marginal(k,bound,total):
    # Unbounded number of each offset, bounded total length k: sorted multisets.
    dp=[[[0]*(k+1) for _ in range(total+1)] for _ in range(k+1)]
    dp[0][0][0]=1
    for v in range(bound+1):
        bit=v%2
        for length in range(1,k+1):
            for s in range(v,total+1):
                for q in range(bit,length+1):
                    dp[length][s][q]+=dp[length-1][s-v][q-bit]
        guard()
    return dp[k][total]


def compositions(total,k):
    if k==1:yield (total,);return
    for x in range(total+1):
        for tail in compositions(total-x,k-1):yield (x,)+tail


def controls():
    checked=0
    for k in range(1,5):
        for bound in range(6):
            literal=Counter((sum(xs),tuple(x%2 for x in xs))
                            for xs in combinations_with_replacement(range(bound+1),k))
            for total in range(k*bound+1):
                for p in product((0,1),repeat=k):
                    assert gaps(k,bound,total,p)==staircase(k,bound,total,p)==literal[total,p]
                    checked+=1
            for total in range(k*bound+1):
                expected=[sum(n for (s,p),n in literal.items() if s==total and sum(p)==q)
                          for q in range(k+1)]
                assert direct_marginal(k,bound,total)==expected
    # Original control caught by hand BEFORE run, not used as an expected rejection.
    assert gaps(2,3,3,(1,0))==1
    assert gaussian_coefficients(2,1,1)[1]==1
    assert gaps(2,5,5,(1,0))==1
    assert gaussian_coefficients(2,2,2)[2]==2
    for total in range(5):
        for k in range(1,5):assert sum(1 for _ in compositions(total,k))==comb(total+k-1,k-1)
    # Real size vectors, independent small direct compositions; no token allocation.
    size_counts={}
    for q in (0,2,4,6,8):
        r=(28-16-q)//2;p=[1]*q+[0]*(8-q);n=0
        for z in compositions(r,8):
            c=[2+bit+2*x for bit,x in zip(p,z)]
            assert sum(c)==28 and [x%2 for x in c]==p and min(c)>=2
            n+=1
        assert n==comb(r+7,7);size_counts[q]=n
    return checked,size_counts


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(RuntimeError('WALL_CAP_12S')))
    signal.alarm(12)
    checked,sizes=controls();patterns=list(product((0,1),repeat=8));rows=[];marginal=Counter()
    for p in patterns:
        n=gaps(8,54,240,p);ref=staircase(8,54,240,p)
        assert n==ref
        complement=gaps(8,54,192,p[::-1])
        assert complement==n==staircase(8,54,192,p[::-1])
        if sum(p)%2:assert n==0
        rows.append(dict(pattern=p,odd_bins=sum(p),count=n,unfiltered_size_vectors=sizes.get(sum(p),0)))
        marginal[sum(p)]+=n;guard()
    assert sum(marginal.values())==24688633
    assert rows[0]['count']==326119
    independent=direct_marginal(8,54,240)
    assert independent==[marginal[q] for q in range(9)]
    reverse_mismatches=[dict(pattern=p,count=gaps(8,54,240,p),reverse_count=gaps(8,54,240,p[::-1]))
                        for p in patterns if gaps(8,54,240,p)!=gaps(8,54,240,p[::-1])]
    assert reverse_mismatches
    mixed=sum(marginal.values())-marginal[0]
    forecasts=dict(all_even_q_present=all(marginal[q]>0 for q in (0,2,4,6,8)),
                   q4_largest=all(marginal[4]>marginal[q] for q in (0,2,6,8)),
                   mixed_above98_percent=100*mixed>98*sum(marginal.values()),
                   some_reversal_mismatch=bool(reverse_mismatches))
    signal.alarm(0)
    print(json.dumps(dict(status='COUNTS_COMPLETE',preregistration='fe3413be',control_correction='52031895',
                         m=28,offset_bound=54,total_offset=240,total=sum(marginal.values()),
                         mixed=mixed,by_odd_count=dict(marginal),unfiltered_size_vectors=sizes,
                         patterns=rows,forecasts=forecasts,tiny_checks=checked,
                         independent_marginal=independent,reversal_mismatches=len(reverse_mismatches),
                         first_reversal_mismatch=reverse_mismatches[0],controls='PASS',
                         cpu_seconds=time.process_time()-START,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
