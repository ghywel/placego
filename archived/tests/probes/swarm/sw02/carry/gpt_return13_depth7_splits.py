#!/usr/bin/env python3
"""Check one next-bit split for each of the six pending depth-seven roots."""
import json
import os
import resource
import signal

from gpt_return13_factor_split import check_parent, join
from gpt_return13_prefix_control import write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, check_leaf, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof

FACTORS = ('0011011', '0100110', '0110000', '0110110', '1010011', '1011110')


def main():
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    worker_soft = 12 if soft == resource.RLIM_INFINITY else min(12, soft)
    resource.setrlimit(resource.RLIMIT_CPU, (worker_soft, hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in [
        (guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
        (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
        (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1'),
    ]:
        pin(path, digest)
    prior = json.loads(pin(os.environ['RETURN13_DEPTH7_BATCH_RECEIPT'],
        '6a7ee8caf4139766102b1dff095d3b54865d78fff747ff9dc137e25827d9f53b'))
    assert prior['status'] == 'DEPTH7_ROOT_CASES_RECORDED'
    assert tuple(item['prefix_in_variable_order'] for item in prior['leaves']
                 if item['status'] == 'CONFLICT_LIMIT_UNKNOWN') == FACTORS
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'],
        'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    parents = REPORT['parents'] = []
    for factor in FACTORS:
        children = []
        for bit in '01':
            child = factor + bit
            label = f'child-{child}'
            check_leaf(label, child, base, body)
            if REPORT['leaves'][-1]['status'] == 'ABSENT_PREFIX_CHECKED':
                children.append(read_proof((OUT/f'{label}-discharged.lrat').read_bytes(), base, child))
        if len(children) < 2:
            parents.append({'status': 'SPLIT_INCOMPLETE', 'factor': factor})
        else:
            proof = join(base, children)
            label = f'parent-{factor}'
            write_proof(OUT/f'{label}-discharged.lrat', proof)
            check_parent(base, body, proof, label)
            parents.append({'status': 'JOINED_FACTOR_CHECKED', 'factor': factor,
                            'lifted_steps': len(proof), 'lifted_clause': proof[-1][1],
                            'shifts': audit_shifts(base, proof)})
        guard.save()
    REPORT['status'] = 'DEPTH7_SPLITS_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_DEPTH7_SPLITS_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
