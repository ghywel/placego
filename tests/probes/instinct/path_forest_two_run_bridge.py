#!/usr/bin/env python3
"""B74/MI169 prereg48d3ad47: primitive8 two-odd-positive/two-parity-run word.

r2..100, all4950 even M in[6r+8,8r+4];198 adjacent-boundary negatives,
99x254 proper-subset checks,one actual central E28 partition.2CPU sec/64MiB.
No order/role search or target census. General hand result remains SKETCH.
OUTCOME:4950 positive and198 predicted boundary failures;99 lists primitive;
one central E28 partition passes dual instruments.0.117607CPU sec,18632704bytes
RSS. Raw SHA256 9c313714569cd6ab4ec1b43be4170271d934264eaa79740d601fa3c60e6dbb6b.
"""
import json
import resource
import time

import path_forest_balanced_bridge as instrument
import path_forest_split_anchor_pilot as pilot


def literal_points(word):
    result=[0]
    for e in word:result.append(result[-1]+e)
    assert result[-1]==0
    return result[:-1]


def main():
    start=time.process_time();rows=[];boundary=[];primitive_checks=0
    for r in range(2,101):
        a,b,c=6*r+3,2*r,2*r+2
        word=(a,-b,-c,-b,a,-c,-b,-c)
        direct=(0,6*r+3,4*r+3,2*r+1,1,6*r+4,4*r+2,2*r+2)
        assert tuple(literal_points(word))==direct
        cross={x+y for x in direct if x%2 for y in direct if y%2==0}
        stated={1,2*r+1,2*r+3,4*r+3,6*r+3,6*r+5,8*r+5,10*r+5,10*r+7,12*r+7}
        assert cross==stated and all(v<=6*r+5 or v>=8*r+5 for v in cross)
        assert sum(x%2 for x in direct)==4
        for mask in range(1,255):
            assert sum(v for i,v in enumerate(word) if mask>>i&1)!=0
            primitive_checks+=1
        for M in range(6*r+8,8*r+5,2):
            assert instrument.literal_geometry(M,set(),direct)
            labels=[min(x,M-1-x) for x in direct]
            assert len(set(labels))==8
            reflected=[M-1-x for x in direct]
            assert instrument.literal_geometry(M,set(),reflected)
            assert [min(x,M-1-x) for x in reflected]==labels
            assert all(reflected[(i+1)%8]-reflected[i]==-word[i] for i in range(8))
            rows.append(dict(r=r,M=M,word=word,positions=direct,labels=labels))
        low=6*r+6;high=8*r+6
        assert 1+(6*r+4)==low-1 and (6*r+3)+(2*r+2)==high-1
        assert not instrument.literal_geometry(low,set(),direct)
        assert not instrument.literal_geometry(high,set(),direct)
        boundary.extend([dict(r=r,M=low,reflected_pair=(1,6*r+4)),
                         dict(r=r,M=high,reflected_pair=(6*r+3,2*r+2))])
        assert time.process_time()-start<2
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<64*1024*1024
    assert len(rows)==4950 and len(boundary)==198 and primitive_checks==99*254
    owners=(0,2,3,4,1,5,6,7);xs=literal_points((21,-6,-8,-6,21,-8,-6,-8))
    selected=dict(zip(owners,xs));h=[1,1,2,2,2,2,2,2]
    e=[21,21,-6,-8,-6,-8,-6,-8];t=[56*s+2*v for s,v in zip(h,e)]
    assert t==[98,98,100,96,100,96,100,96] and sum(t)==784
    assert sorted(t)==[96,96,96,98,98,100,100,100]
    assert all(68<=v<=122 for v in t) and sum(v%4==2 for v in t)==2
    assert sum(v//56 for v in t)==8<13  # MI167 cannot admit this target.
    bins=instrument.materialize(28,set(),[0]*8,h,e,selected,t)
    assert pilot.literal_ok(bins,t,h) and pilot.independent_ok(bins,t)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='48d3ad47',
                         geometry_fixtures=len(rows),boundary_failures=len(boundary),
                         primitive_lists=99,proper_subset_checks=primitive_checks,
                         sign_reversal='PASS',cross_parity_sum_formula='PASS',
                         rows=rows,boundary=boundary,
                         central_E28=dict(targets=t,slots=h,moves=e,selected=selected,bins=bins),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
