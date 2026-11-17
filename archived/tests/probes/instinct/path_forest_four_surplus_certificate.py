#!/usr/bin/env python3
"""B55/MI128 preregistered0877f361: delivery certificate, no search.

Assemble old factorable7223 and primitive575 witnesses, preserve primitive
30 failures. Independent sorted full domain7828/class partition, exact
missing-set equality, two literal checkers, source digests and omission/
duplicate controls. Cap8000 certificates/three CPU seconds. Raw outside git.
OUTCOME: exact7798 certificate keys (7223 factorable,575 primitive), both
literal checkers and omission/duplicate controls pass. Independent sorted
domain7828 minus keys equals exactly30 retained greedy-order failures.
CPU0.285565 s. Full certificate plus blocked-root lists in shared store,
cited/instinct/b55-four-surplus-ae7e59d8060d5499.json, SHA256
ae7e59d8060d54998898f7682847b34d48f53351aed784a8f75ec9c5eb90f767.
Finite coverage COMPUTED;30 residual targets and full E28/L8 remain OPEN.
"""
from pathlib import Path
import hashlib
import json
import sys
import time
from path_forest_factorization_audit import direct_domain
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


def load(path,digest):
    raw=Path(path).read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
    return json.loads(raw)


def main():
    start=time.process_time()
    first=load(sys.argv[1],'d5648ef86d41ae8360b09c4b147426cf46d9f51763ac85344208ae074d209c65')
    second=load(sys.argv[2],'96edf2cd031e499a38f07e50290d2fa22d43c03c61c2bb7a3360f89619bfca32')
    certificates=[];keys=set();factorable_keys=set();primitive_keys=set()
    for e in first['certificates']:
        t=tuple(e['targets']);assert t not in keys;keys.add(t);factorable_keys.add(t)
        assert certificate_ok(e['bins'],t) and bitset_ok(e['bins'],t)
        certificates.append(dict(targets=t,bins=e['bins'],method='two_cycles',mode=e['mode']))
        assert len(certificates)<=8000 and time.process_time()-start<3
    for e in second['results']:
        if 'chosen' not in e:continue
        t=tuple(e['targets']);assert t not in keys;keys.add(t);primitive_keys.add(t)
        bins=e['chosen']['witness']['bins']
        assert certificate_ok(bins,t) and bitset_ok(bins,t)
        certificates.append(dict(targets=t,bins=bins,method='primitive_greedy'))
        assert len(certificates)<=8000 and time.process_time()-start<3
    full,factorable=direct_domain();failed={tuple(e['targets']) for e in second['failures']}
    assert factorable_keys==factorable and len(factorable_keys)==7223
    assert len(primitive_keys)==575 and primitive_keys<=full-factorable
    assert len(keys)==7798 and len(full)==7828 and full-keys==failed and len(failed)==30
    omit=next(iter(keys));assert len(full-(keys-{omit}))==31
    sample=certificates[0];t=tuple(sample['targets']);bad=[list(b) for b in sample['bins']]
    bad[0][0]=bad[1][0]
    assert not certificate_ok(bad,t) and not bitset_ok(bad,t)
    assert time.process_time()-start<3
    print(json.dumps(dict(status='7798_CERTIFICATES_30_RETAINED',total_domain=7828,
        certified=7798,factorable_certificates=7223,primitive_certificates=575,
        certificates=sorted(certificates,key=lambda e:e['targets']),
        unresolved=second['failures'],source_sha256={
            'factorable':'d5648ef86d41ae8360b09c4b147426cf46d9f51763ac85344208ae074d209c65',
            'primitive':'96edf2cd031e499a38f07e50290d2fa22d43c03c61c2bb7a3360f89619bfca32'},
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
