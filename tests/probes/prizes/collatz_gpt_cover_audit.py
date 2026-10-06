"""G88 RC1-RC2 preregistered before running in this publication.
RC1 independently simulate rejected prefixes, rebuild extrema by odd
positions, and require disjoint classes covering all 2^33 residues.
RC2 reject deleted/duplicated/root-cut corruptions. Certificate outside Git.
The producer only exports cuts; no producer bounds are reused by audit.
BN1 a=22..24, cumulative 100000-node/five-second tree budget. Require
span<8 for displacement reduction; blind no collision, stop on cap/witness.
"""
from collections import Counter
import json
from pathlib import Path
from time import monotonic
from collatz_gpt_collision_tree import tree

A, HORIZON, DELTA = 21, 33, 4


def prefix(n,s):
    positions = []
    ok = True
    start = n
    for k in range(s):
        if n%2:
            positions.append(k)
            n = (3*n+1)//2
        else:
            n //= 2
        ok &= 3**len(positions) >= 2**(k+1)
    B = 2**s*n-3**len(positions)*start
    assert B == sum(3**(len(positions)-1-i)*2**p for i,p in enumerate(positions))
    return positions,ok,B


def extrema_by_positions(positions,s,a):
    remaining = a-len(positions)
    early = positions+list(range(s,s+remaining))
    late = list(positions)
    for i in range(len(positions),a):
        power,p = 3**i,0
        while 2**(p+1) <= power:
            p += 1
        assert p >= s
        late.append(p)
    def offset(pp):
        return sum(3**(a-1-i)*2**p for i,p in enumerate(pp))
    return offset(early),offset(late)


def reason(s,r,a,t,delta):
    assert 0 <= s <= t and 0 <= r < 2**s
    n = r+2**(t+1)
    low,ok,B = prefix(n,s)
    high,ok2,C = prefix(n+delta,s)
    if not ok or not ok2:
        return 'admission'
    if len(low) > a or len(high) > a:
        return 'count'
    if a-len(low) > t-s or a-len(high) > t-s:
        return 'capacity'
    lo,hi = extrema_by_positions(low,s,a)
    lo2,hi2 = extrema_by_positions(high,s,a)
    if not lo-hi2 <= delta*3**a <= hi-lo2:
        return 'offset interval'
    raise AssertionError('invalid cut')


def audit(cuts,a=21,t=33,delta=4):
    reasons = [reason(s,r,a,t,delta) for s,r in cuts]
    for i,(s,r) in enumerate(cuts):
        for q,u in cuts[:i]:
            assert (r-u)%2**min(s,q) != 0, 'overlap'
    assert sum(2**(t-s) for s,r in cuts) == 2**t, 'coverage'
    return Counter(reasons)


def must_reject(cuts,expected):
    try:
        audit(cuts)
    except AssertionError as exc:
        assert expected in str(exc),(expected,str(exc))
    else:
        raise AssertionError('corruption accepted')


def main():
    cuts = []
    result = tree(A,HORIZON,DELTA,True,cuts=cuts)
    assert result['complete'] and not result['witnesses'] and len(cuts) == 30
    counts = audit(cuts)
    must_reject(cuts[:-1],'coverage')
    must_reject(cuts+[cuts[0]],'overlap')
    must_reject([(0,0)],'invalid cut')
    target = Path('/private/tmp/placego-gpt-collision-cover-a21.json')
    target.write_text(json.dumps(dict(a=A,horizon=HORIZON,displacement=DELTA,
                                     cuts=cuts,producer=result,reasons=dict(counts)),indent=2))
    print('RC1 PASS:',len(cuts),'disjoint residue classes cover',2**HORIZON,'starts modulo 2^33')
    print('Independent rejection reasons:',dict(counts))
    print('RC2 PASS: missing coverage, overlap and invalid root rejected')
    print('Certificate saved outside Git; independent model review pending')
    deadline,remaining = monotonic()+5,100000
    for a in range(22,25):
        t = (3**a).bit_length()-1
        maximal = sum(3**(a-1-i)*2**((3**i).bit_length()-1) for i in range(a))
        span_numerator = maximal-(3**a-2**a)
        if span_numerator >= 8*3**a:
            print('BN1 STOP: displacement-four reduction not certified at',a)
            break
        cuts = []
        result = tree(a,t,4,True,cap=remaining,seconds=max(0,deadline-monotonic()),cuts=cuts)
        remaining -= result['nodes']
        if not result['complete'] or result['witnesses']:
            for r in result['witnesses']:
                n = r+2**(t+1)
                pp,ok,B = prefix(n,t)
                qq,ok2,C = prefix(n+4,t)
                assert ok and ok2 and len(pp) == len(qq) == a and B-C == 4*3**a
                assert n.bit_length() == (n+4).bit_length()
                print('BN1 verified witness starts:',n,n+4)
            print('BN1 STOP',a,result)
            break
        counts = audit(cuts,a,t,4)
        Path('/private/tmp/placego-gpt-collision-cover-a%d.json'%a).write_text(json.dumps(
            dict(a=a,horizon=t,displacement=4,cuts=cuts,producer=result,reasons=dict(counts)),indent=2))
        print('BN1 PASS',a,'horizon',t,'nodes',result['nodes'],'cuts',len(cuts),
              'covered',2**t,'reasons',dict(counts))


if __name__ == '__main__':
    main()
