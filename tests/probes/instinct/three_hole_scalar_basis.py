#!/usr/bin/env python3
r"""MI354/B182: finite basis for three-hole scalar localization. NOT RUN.

Question: for an integer interval with <=3 deletions and r,t>=4,
are all scalar omissions within distance3 of an actual extremum?
Hand MI353 supplies all offsets>=12 from both ends. MI354 truncates
near-minimum offsets0..11 to r'=min(r,11),t'=min(t,11); reflect
for the upper end. Thus this EXACT finite basis suffices, conditional
on the unreviewed hand reductions. This is not a partition experiment.

DOMAIN: every ordered r,t in4..11; n=r+t; every NORMALIZED pool
with n available integers, endpoints0,U retained, U=n-1+h, h=0..3.
Equivalently delete every h-subset of1..U-1. One invocation only.
PREDICTION B182-P (blind): offsets4..11 occur in ALL basis pools.
A counterexample rejects this sharper premise,not G315/G316/G317.
CONTROL B182-C0: full spectra on three literal small pools agree with
itertools.combinations. All h<=2 full spectra obey the recorded
edge-distance<=h localization; these are known consequences,not blind.
INDEPENDENT B182-C1: primary value-by-value bitset DP versus complete
near-minimum rank-partition enumeration (rank excess<=11). Secondary
DOMAIN uses multisets of rank gaps,not deleted-value combinations.
Compare ALL offsets0..11,including omissions;consume each primary key
exactly once and independently check the binomial case-count formula.
Every retained secondary witness checked literally for size/distinctness/sum.
COUNTERFACTUAL B182-N: permitting r=t=3 must fail on
[0,8] minus{1,4,7}: target12 is missing,7 above min5 and below max19.
UNEXPECTED B182-U: three larger/asymmetric pools and reflections test the
truncation equivalence for ALL offsets0..11 and lift every available
truncated witness with the forced prefix; ranks/translation/sums checked.
STOP: first failed control => INSTRUMENT-FAILED; first blind counterexample
confirmed by independent rank enumeration => REFUTED. ONE unchanged-source
run;20CPU/30wall seconds,128MiB peakRSS,256KiB output,external35s watchdog.
No patch/retry,automatic larger h/domain or cap increase. Local receipt only;
no raw portal upload. Saving/compiling this file is not an execution.
"""
import hashlib
import itertools
import json
import math
import resource
import sys
import time
from functools import lru_cache

CPU = time.process_time()
WALL = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (20, 21))


class Cap(Exception):
    pass


def budget():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    if time.process_time()-CPU > 20 or time.monotonic()-WALL > 30 or peak > 128*1024**2:
        raise Cap('registered CPU/wall/RSS cap')
    return peak


def spectrum(pool, r):
    dp = [1]+[0]*r
    for at, value in enumerate(pool):
        for k in range(min(r, at+1), 0, -1):
            dp[k] |= dp[k-1] << value
    return dp[r]


def edge_mask(pool, r):
    return (spectrum(pool,r) >> sum(pool[:r])) & 4095


@lru_cache(None)
def shapes(r, t):
    """All nondecreasing rank displacements of total<=11, independent of values."""
    out = []

    def partitions(left, ceiling, parts):
        if left == 0:
            increments = (0,)*(r-len(parts))+tuple(reversed(parts))
            indices = tuple(i+v for i,v in enumerate(increments))
            assert len(indices)==r and len(set(indices))==r and max(indices)<r+t
            moves = tuple((i,indices[i]) for i in range(r) if indices[i]!=i)
            out.append((indices, moves))
            return
        if len(parts)==r:
            return
        for value in range(min(left,ceiling,t),0,-1):
            partitions(left-value,value,parts+(value,))

    for total in range(12):
        partitions(total,t,())
    assert len({x[0] for x in out})==len(out)
    return tuple(out)


def rank_map(pool, r):
    lo = sum(pool[:r])
    witnesses = {}
    for indices, moves in shapes(r,len(pool)-r):
        delta = sum(pool[new]-pool[old] for old,new in moves)
        if delta<=11 and delta not in witnesses:
            witness = tuple(pool[i] for i in indices)
            assert len(witness)==r and len(set(witness))==r
            assert set(witness)<=set(pool) and sum(witness)==lo+delta
            witnesses[delta]=witness
    return sum(1<<d for d in witnesses),witnesses


def controls():
    for pool,r in (((0,1,3,5,6,7,8,10),4),
                   ((0,2,3,5,6,8),3),
                   ((3,5,6,7,8,10,11,13,14),4)):
        literal = {sum(a) for a in itertools.combinations(pool,r)}
        bits = spectrum(pool,r)
        assert bits == sum(1<<v for v in literal)
        assert rank_map(pool,r)[0] == edge_mask(pool,r)
    bad = (0,2,3,5,6,8)
    assert sum(bad)==24 and sum(bad[:3])==5 and sum(bad[-3:])==19
    assert not (spectrum(bad,3)>>12)&1
    assert 12 not in {sum(x) for x in itertools.combinations(bad,3)}
    lifts=0
    for r,t,holes in ((17,19,(1,18,30)),(23,7,(5,21,29)),(4,29,(1,16,34))):
        U=r+t+2
        pool=tuple(x for x in range(U+1) if x not in holes)
        assert len(pool)==r+t
        for actual in (pool,tuple(U-x for x in reversed(pool))):
            p=max(0,r-11)
            segment=actual[p:r+min(t,11)]
            shift=segment[0]
            small=tuple(x-shift for x in segment)
            rr=min(r,11)
            mask,witnesses=rank_map(small,rr)
            assert mask==edge_mask(small,rr)==edge_mask(actual,r)
            prefix=actual[:p]
            assert sum(actual[:r])==sum(prefix)+sum(small[:rr])+rr*shift
            for d,w in witnesses.items():
                lifted=prefix+tuple(x+shift for x in w)
                assert len(lifted)==r and len(set(lifted))==r
                assert set(lifted)<=set(actual) and sum(lifted)==sum(actual[:r])+d
                lifts+=1
            budget()
    return lifts


def main():
    lifted=controls()
    primary={}
    count_h=[0]*4
    comparisons=0
    for n in range(8,23):
        eligible=range(max(4,n-11),min(11,n-4)+1)
        for h in range(4):
            U=n+h-1
            for holes in itertools.combinations(range(1,U),h):
                pool=tuple(x for x in range(U+1) if x not in holes)
                for r in eligible:
                    lo,hi=sum(pool[:r]),sum(pool[-r:])
                    bits=spectrum(pool,r)
                    assert (bits>>lo)&1 and (bits>>hi)&1
                    if h<=2:
                        length=hi-lo-2*h-1
                        interior=((1<<length)-1)<<(lo+h+1)
                        assert bits&interior==interior,'known localization control'
                    mask=(bits>>lo)&4095
                    key=(U,holes,r)
                    assert key not in primary
                    primary[key]=mask
                    count_h[h]+=1
                    if mask&4080!=4080:
                        secondary,witnesses=rank_map(pool,r)
                        assert secondary==mask,'counterexample confirmation'
                        missing=[lo+d for d in range(4,12) if not(mask>>d)&1]
                        return dict(status='REFUTED',pool=pool,r=r,t=n-r,
                                    holes=holes,min=lo,max=hi,missing=missing,
                                    primary_cases=count_h,lifted_controls=lifted)
                budget()
    expected=[sum(math.comb(r+t+h-2,h) for r in range(4,12) for t in range(4,12)) for h in range(4)]
    assert count_h==expected
    digest=hashlib.sha256()
    second_h=[0]*4
    for n in range(8,23):
        for h in range(4):
            for gaps in itertools.combinations_with_replacement(range(n-1),h):
                counts={}
                for gap in gaps:
                    counts[gap]=counts.get(gap,0)+1
                pool=[0]
                for at in range(n-1):
                    pool.append(pool[-1]+1+counts.get(at,0))
                U=pool[-1]
                present=set(pool)
                holes=tuple(x for x in range(1,U) if x not in present)
                assert len(holes)==h and len(pool)==n
                for r in range(4,12):
                    if not 4<=n-r<=11:
                        continue
                    key=(U,holes,r)
                    mask,witnesses=rank_map(pool,r)
                    assert primary.pop(key)==mask,'independent near-edge map/domain'
                    assert mask&4080==4080
                    second_h[h]+=1
                    comparisons+=12
                    digest.update(json.dumps((key,mask,tuple(sorted(witnesses.items()))),separators=(',',':')).encode())
                budget()
    assert not primary and second_h==expected
    return dict(status='PASS',cases_by_h=count_h,total_cases=sum(count_h),
                independent_offset_comparisons=comparisons,lifted_controls=lifted,
                literal_controls=3,counterfactual='size3 target12 missing as required',
                witness_digest=digest.hexdigest(),
                scope='finite basis only;universal localization conditional on hand reduction')


if __name__=='__main__':
    try:
        result=main()
    except Cap as exc:
        result=dict(status='UNKNOWN-CAP',reason=str(exc))
    except Exception as exc:
        result=dict(status='INSTRUMENT-FAILED',error=type(exc).__name__,reason=str(exc))
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':
        peak*=1024
    result.update(cpu=time.process_time()-CPU,wall=time.monotonic()-WALL,peak_rss_bytes=peak)
    encoded=json.dumps(result,sort_keys=True)
    assert len(encoded.encode())<=256*1024
    print(encoded)
    sys.exit(0 if result['status']=='PASS' else 2)
