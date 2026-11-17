#!/usr/bin/env python3
"""B53/MI124 preregistered6e623788: two forced factor changes and audit.

Two exact selected-owner formulas only. Keep old7221 witnesses unchanged;
predict exact factorable-domain union7223 within7828 four-surplus targets.
Independent sorted target domain and integer-bitset subset sum, two literal
partition checkers. Omission/duplicate/wrong-sum controls. Unexpected all
928 physical root pairs of five OLD sparse-part orders still fail; gap
criterion invariant under their permutations. Cap2 new formulas/2000 old
root checks/four CPU seconds including complete audit; no fallback search.
OUTCOME: both forced formulas pass,7221 old witnesses unchanged; exact
independent sorted/bitset-DP domain equals7223 certificates within7828
targets, primitive605 unchanged. Both partition checkers and all controls
pass. All928 old-root/order checks fail, gap criterion confirmed over all
five orders. CPU0.485571 s. Raw outside git SHA256
d5648ef86d41ae8360b09c4b147426cf46d9f51763ac85344208ae074d209c65.
Factorable four-surplus domain COMPUTED; primitive region unsearched.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement,permutations
from pathlib import Path
import hashlib
import json
import sys
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok

FORMULAS={
 (72,72,72,100,116,116,116,120):{4:0,5:2,0:4,1:12,2:20,6:8,7:10,3:14},
 (72,76,76,96,116,116,116,116):{4:0,5:2,6:4,7:6,1:8,2:18,0:3,3:11}}


def direct_domain():
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    full=set();factorable=set()
    for high in combinations_with_replacement(range(114,123,2),4):
        small=tuple((x-112)//2 for x in high)
        for xs in lows[784-sum(high)]:
            t=xs+high;full.add(t)
            positive=((xs[0]-56)//2,(xs[1]-56)//2)+small;W=(112-xs[2])//2
            reachable=1
            for x in positive:reachable|=reachable<<x
            if reachable&(1<<W):factorable.add(t)
    return full,factorable


def obstruction_controls(start):
    checks=0;orders=0
    for steps,block in (((4,8,8),(0,2,4,6)),((8,10),(0,2,4,6,8))):
        for order in sorted(set(permutations(steps))):
            S=[0]
            for x in order:S.append(S[-1]+x)
            assert max(b-a for a,b in zip(S,S[1:]))//2<=len(block)
            scaled=[x//2 for x in S]
            for r in range(14-scaled[-1]):
                occupied={x+r for x in scaled}
                assert all(occupied&set(range(t,t+len(block))) for t in range(15-len(block)))
            for r in range(28-S[-1]):
                for t in range(28-block[-1]):
                    checks+=1
                    assert checks<=2000 and time.process_time()-start<4
                    labels={min(x+r,27-x-r) for x in S}|{min(x+t,27-x-t) for x in block}
                    assert len(labels)<8
            orders+=1
    assert checks==928 and orders==5
    return checks


def main():
    start=time.process_time();raw=Path(sys.argv[1]).read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='e25cb282fabd0cade077a3482743ff735c94f89cc25af39707358b64b99e66d2'
    previous=json.loads(raw);assert previous['factorable']==7223 and previous['certified']==7221
    failed={tuple(e['targets']) for e in previous['failures']};assert failed==set(FORMULAS)
    new={}
    for t,selected in FORMULAS.items():
        assert len(new)<2 and time.process_time()-start<4
        w=materialize(t,selected);assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
        new[t]=w
    checks=obstruction_controls(start);certificates=[];keys=set()
    for e in previous['results']:
        t=tuple(e['targets']);replacement=t in new
        w=new[t] if replacement else e['chosen']['witness']
        assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
        assert t not in keys;keys.add(t)
        certificates.append(dict(targets=t,bins=w['bins'],mode='forced_factor_change' if replacement else 'canonical'))
        assert time.process_time()-start<4
    full,direct=direct_domain();assert keys==direct and len(keys)==7223 and len(full)==7828
    assert len(full-direct)==605
    assert {tuple(e['targets']) for e in previous['primitive_targets']}==full-direct
    for t in FORMULAS:assert (keys-{t})<direct and len(direct-(keys-{t}))==1
    sample_t,w=next(iter(new.items()));bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,sample_t) and not bitset_ok(bins,sample_t)
    bins=[set(b) for b in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample_t) and not bitset_ok(bins,sample_t)
    assert time.process_time()-start<4
    print(json.dumps(dict(status='ALL_7223_FACTORABLE',total_four_surplus=7828,
        factorable=7223,primitive=605,certificates=certificates,new_formulas=[dict(targets=t,witness=w) for t,w in new.items()],
        source_sha256=digest,old_order_root_checks=checks,controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
