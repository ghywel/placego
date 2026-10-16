#!/usr/bin/env python3
"""B49/MI115 preregistered2066fae6: exact three-surplus coverage audit.

Sorted even E28 t4<112,t5=112,t6>112; five disjoint regimes predicted
999/11/20/1478/2760, total5268. Reuse B42-48 witnesses only, verifying
raw digests. Independent direct target domain, multiset and integer-bitset
partition checkers. Dropping any regime, duplicated token, outside-slice
control reject. Unexpected equal-step counts by s and regime (112 traps
are not the whole equal-step slice). Caps6000 certificates/three CPU
seconds; no certificate generation, search or fallback. Raw outside git.
OUTCOME: all5268 exact target keys equal the independent direct domain;
regime counts999/11/20/1478/2760 agree with no overlap. Both literal
checkers and omission/duplicate/outside-slice controls pass. Equal-step
totals for s1..5 are239/195/148/108/72, total762, not112.
CPU0.519423 s. Raw outside git SHA256
1603e5f50221531c9b6823fa6b9015337216ce72d6bd5882a7d8b24aba7a8bcd.
Full named finite subfamily COMPUTED; full E28 and L8 remain OPEN.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
from pathlib import Path
import hashlib
import json
import sys
import time
from path_forest_receiving_chains import certificate_ok

SOURCES={
 'matching':('math-instinct-b42-matching-three.json','d03a0e92d5878e200535ec0c8016220a328668f1d3e16c328d341d6ede0573c8'),
 'maximal':('math-instinct-b43-max-edge.json','34293beaf38b5cee6559cb376daa1ad09e0b0894088a824e26f97ab539c1cef8'),
 'dominant':('math-instinct-b44-prefix-compatibility.json','0dbafbbd7fcf3ce822ebc5effc442e4cd0f9f074a817c84f5af7daa96fed612c'),
 'endpoint':('math-instinct-b45-prefix-endpoint-repair.json','833895ffcbfe85b3a4c0502ef9eea476e8f0ca9ae302cebd1dd664059ff12908'),
 'two_donor':('math-instinct-b46-two-donor.json','f7c46c9182bd125ef2159022b9cf1f5949bfba75f95d524aec0c42b06f2c05a0'),
 'small':('math-instinct-b47-small-remainder.json','a989a08e571ff50a5668fc70c9b320eda257f3e02323dd5dab0f5b77cd688633'),
 'cancelling':('math-instinct-b48-cancelling-traps.json','5c0790e809234bd0df79cdc4c8ce4a580bc0233f65713bf4edd34d6142e79e7d')}
COUNTS={'matching':999,'maximal':11,'two_donor':20,'dominant':1478,'small':2760}


def bitset_ok(bins,t):
    if len(bins)!=8 or tuple(map(sum,bins))!=t:return False
    if sorted(map(len,bins))!=[2,2,4,4,4,4,4,4]:return False
    used=0
    for bucket in bins:
        for x in bucket:
            if not isinstance(x,int) or not 1<=x<=55 or x%2!=1:return False
            bit=1<<((x-1)//2)
            if used&bit:return False
            used|=bit
    return used==(1<<28)-1


def regime(t):
    u,v=(t[0]-56)//2,(t[1]-56)//2
    W,Z=(112-t[2])//2,(112-t[3])//2
    q=sum((x-112)//2 for x in t[5:])
    if {u,v}&{W,Z}:return 'matching'
    if W==22:return 'maximal'
    if W<=q:return 'two_donor'
    if W-q>=Z:return 'dominant'
    assert 0<W-q<Z and W<22
    return 'small'


def direct_domain():
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    return {xs+(112,)+hi for hi in combinations_with_replacement(range(114,123,2),3)
            for xs in lows[784-112-sum(hi)]}


def main():
    start=time.process_time();folder=Path(sys.argv[1]);data={};source_digests={}
    for key,(name,digest) in SOURCES.items():
        raw=(folder/name).read_bytes();actual=hashlib.sha256(raw).hexdigest()
        assert actual==digest;source_digests[key]=actual;data[key]=json.loads(raw)
    groups={k:{} for k in COUNTS}
    def add(group,e):
        t=tuple(e['targets']);w=e['chosen']['witness'] if 'chosen' in e else e['witness']
        assert regime(t)==group
        groups[group].setdefault(t,w['bins'])
    for k in ('matching','maximal','two_donor'):
        for e in data[k]['results']:add(k,e)
    for e in data['dominant']['results']:
        if 'chosen' in e:add('dominant',e)
    before=set(groups['dominant'])
    for e in data['endpoint']['stripe']:add('dominant',e)
    assert len(set(groups['dominant'])-before)==2
    for e in data['small']['results']:
        if 'chosen' in e:add('small',e)
    before=set(groups['small'])
    for e in data['cancelling']['results']:add('small',e)
    assert len(set(groups['small'])-before)==112
    assert {k:len(g) for k,g in groups.items()}==COUNTS
    joined={t:bins for g in groups.values() for t,bins in g.items()}
    assert len(joined)==sum(map(len,groups.values()))==5268
    direct=direct_domain();assert set(joined)==direct
    for k in groups:
        reduced=set().union(*(set(g) for name,g in groups.items() if name!=k))
        assert reduced<direct and len(direct-reduced)==COUNTS[k]
    assert (68,68,96,100,112,112,114,114) not in direct
    certificates=[];equal=Counter();equal_regime=defaultdict(Counter)
    for t,bins in sorted(joined.items()):
        if len(certificates)>=6000 or time.process_time()-start>=3:
            print(json.dumps(dict(status='UNKNOWN',completed=len(certificates))));return
        assert certificate_ok(bins,t) and bitset_ok(bins,t)
        group=regime(t);certificates.append(dict(targets=t,regime=group,bins=bins))
        if t[5]==t[6]==t[7]:
            s=(t[5]-112)//2;equal[s]+=1;equal_regime[group][s]+=1
    t,bins=next(iter(joined.items()));bad=[list(b) for b in bins]
    bad[0][0]=bad[1][0]
    assert not certificate_ok(bad,t) and not bitset_ok(bad,t)
    assert sum(equal.values())>112
    print(json.dumps(dict(status='ALL_5268_THREE_SURPLUS',certificates=certificates,
        regimes={k:len(g) for k,g in groups.items()},equal_steps=dict(equal),
        equal_steps_by_regime={k:dict(c) for k,c in equal_regime.items()},
        source_digests=source_digests,controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
