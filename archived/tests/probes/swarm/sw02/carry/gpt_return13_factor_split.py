#!/usr/bin/env python3
"""Check the two next-bit cases of one capped P13 factor and join their proofs."""
import json
import os
from pathlib import Path
import resource
import signal

from gpt_return13_prefix_control import add_step, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, check_leaf, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof
from gpt_return13_binary_cert import c_check

FACTOR = '0001111'


def join(base, children):
    database = dict(enumerate(base, 1))
    proof = []
    conclusions = []
    for child in children:
        mapping = {index: index for index in range(1, len(base) + 1)}
        for index, clause, hints in child:
            mapping[index] = add_step(clause, [mapping[hint] for hint in hints], database, proof)
        conclusions.append(mapping[child[-1][0]])
    left, right = (database[index] for index in conclusions)
    assert left[:-1] == right[:-1] and (left[-1], right[-1]) == (14, -14)
    add_step(left[:-1], conclusions, database, proof)
    return proof


def check_parent(base, body, proof, label='parent'):
    parent_clause = proof[-1][1]
    cube = [-literal for literal in parent_clause]
    cnf = OUT/f'{label}.cnf'
    units = ''.join(f'{literal} 0\n' for literal in cube).encode()
    cnf.write_bytes(f'p cnf 910 {len(base) + len(cube)}\n'.encode() + body + units)
    count = len(cube)
    remapped = [(index + count, clause, [hint + count if hint > len(base) else hint for hint in hints])
                for index, clause, hints in proof]
    unit_ids = list(range(len(base) + 1, len(base) + count + 1))
    database = dict(enumerate(base + [[literal] for literal in cube], 1))
    for index, clause, _ in remapped:
        database[index] = clause
    add_step([], unit_ids + [remapped[-1][0]], database, remapped)
    certificate = OUT/f'{label}.lrat'
    write_proof(certificate, remapped)
    guard.cake(f'{label}-cake', cnf, certificate, True, 10, 20)
    c_check(f'{label}-independent', cnf, certificate)


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 120))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in [
        (guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
        (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
        (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1'),
    ]:
        pin(path, digest)
    prior = json.loads(pin(os.environ['RETURN13_PANEL_RECEIPT'],
        '8121d57eb7868cf140237ac7fa8c5e327321c010ef11420b0230548ac8899027'))
    assert [(item['prefix_in_variable_order'], item['status']) for item in prior['leaves']
            if item['status'] == 'CONFLICT_LIMIT_UNKNOWN'] == [(FACTOR, 'CONFLICT_LIMIT_UNKNOWN')]
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'],
        'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    children = []
    for bit in '01':
        label = f'next{bit}'
        check_leaf(label, FACTOR + bit, base, body)
        if REPORT['leaves'][-1]['status'] == 'ABSENT_PREFIX_CHECKED':
            children.append(read_proof((OUT/f'{label}-discharged.lrat').read_bytes(), base, FACTOR + bit))
    if len(children) == 2:
        proof = join(base, children)
        write_proof(OUT/'parent-discharged.lrat', proof)
        check_parent(base, body, proof)
        REPORT['parent'] = {'status': 'JOINED_FACTOR_CHECKED', 'factor': FACTOR,
                            'lifted_steps': len(proof), 'lifted_clause': proof[-1][1],
                            'shifts': audit_shifts(base, proof)}
    else:
        REPORT['parent'] = {'status': 'SPLIT_INCOMPLETE', 'factor': FACTOR}
    REPORT['status'] = 'TWO_SPLIT_BRANCHES_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_FACTOR_SPLIT_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
