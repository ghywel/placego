#!/usr/bin/env python3
"""Split each outstanding P13 root once and reuse the checked depth-seven sibling."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_factor_split import check_parent
from gpt_return13_prefix_control import add_step, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, check_leaf, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof


def join(base, prefix, children):
    database = dict(enumerate(base, 1))
    proof, conclusions = [], []
    expected = [(7 + i) * (-1 if bit == '1' else 1) for i, bit in enumerate(prefix)]
    pivot = 7 + len(prefix)
    for bit, child in enumerate(children):
        assert child[-1][1] == expected + [pivot * (1 - 2 * bit)]
        mapping = {i: i for i in range(1, len(base) + 1)}
        for index, clause, hints in child:
            mapping[index] = add_step(clause, [mapping[hint] for hint in hints], database, proof)
        conclusions.append(mapping[child[-1][0]])
    add_step(expected, conclusions, database, proof)
    return proof


def record_parent(base, body, prefix, children):
    entry = {'factor': prefix, 'status': 'SPLIT_INCOMPLETE'}
    if len(children) == 2:
        proof = join(base, prefix, children)
        label = f'parent-{prefix}'
        write_proof(OUT/f'{label}-discharged.lrat', proof)
        check_parent(base, body, proof, label)
        entry.update(status='JOINED_FACTOR_CHECKED', lifted_steps=len(proof),
                     lifted_clause=proof[-1][1], shifts=audit_shifts(base, proof))
    REPORT['parents'].append(entry)
    guard.save()
    return entry['status'] == 'JOINED_FACTOR_CHECKED'


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in [
        (guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
        (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
        (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1'),
    ]:
        pin(path, digest)
    history = Path(os.environ['RETURN13_SPLIT_HISTORY'])
    older = json.loads(pin(history/'depth7-splits.json', plan['depth7_sha256']))
    child_states = {item['prefix_in_variable_order']: item['status'] for item in older['leaves']}
    assert [word for word, status in child_states.items() if status == 'CONFLICT_LIMIT_UNKNOWN'] == ['01101100']
    assert child_states['01101101'] == 'ABSENT_PREFIX_CHECKED'
    to_split = ['01101100']
    for name in ('depth8', 'deep'):
        older = json.loads(pin(history/f'{name}.json', plan[f'{name}_sha256']))
        to_split.extend(item['prefix_in_variable_order'] for item in older['leaves']
                        if item['status'] == 'CONFLICT_LIMIT_UNKNOWN')
    assert to_split == plan['split_roots'] and len(set(to_split)) == 6
    resumed = json.loads(pin(history/'deep-resume.json', plan['deep_resume_sha256']))
    assert resumed['status'] == 'DEEP_ROOT_RESUME_RECORDED'
    assert len(resumed['leaves']) == 16 and all(item['status']=='ABSENT_PREFIX_CHECKED' for item in resumed['leaves'])
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    old_sibling = read_proof(pin(history/'sibling.lrat', plan['sibling_sha256']), base, '01101101')
    REPORT['parents'] = []
    for prefix in to_split:
        children = []
        for bit in '01':
            child = prefix + bit
            label = f'child-{child}'
            check_leaf(label, child, base, body)
            if REPORT['leaves'][-1]['status'] == 'ABSENT_PREFIX_CHECKED':
                children.append(read_proof((OUT/f'{label}-discharged.lrat').read_bytes(), base, child))
        if record_parent(base, body, prefix, children) and prefix == '01101100':
            joined_child = read_proof((OUT/f'parent-{prefix}-discharged.lrat').read_bytes(), base, prefix)
            record_parent(base, body, '0110110', [joined_child, old_sibling])
    REPORT['status'] = 'FINAL_ROOT_SPLITS_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_FINAL_ROOT_SPLITS_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
