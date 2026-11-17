#!/usr/bin/env python3
"""Finish the interrupted proof from its saved LRAT, then query untouched P13 roots."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_binary_cert import c_check, compact
from gpt_return13_prefix_control import discharge, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, check_leaf, guard, pin, read_cnf


def finish_saved_proof(source, saved, base, body):
    prefix = saved['prefix_in_variable_order']
    label = saved['label']
    cnf, binary, cone = (OUT/f'{label}{suffix}' for suffix in ('.cnf', '.clrat', '-cone.lrat'))
    cnf.write_bytes(pin(source/cnf.name, saved['cnf_sha256']))
    binary.write_bytes(pin(source/binary.name, saved['binary_sha256']))
    prior_checker = pin(source/f'{label}-cake.stdout', saved['checker_stdout_sha256'])
    assert b's VERIFIED UNSAT' in prior_checker.splitlines()
    assumptions = [(7 + index) * (1 if bit == '1' else -1) for index, bit in enumerate(prefix)]
    units = ''.join(f'{literal} 0\n' for literal in assumptions).encode()
    assert cnf.read_bytes() == f'p cnf 910 {len(base) + len(assumptions)}\n'.encode() + body + units
    entry = {'label': label, 'prefix_in_variable_order': prefix, 'status': 'REPLAYING_SAVED_PROOF',
             'cnf_sha256': saved['cnf_sha256'], 'binary_sha256': saved['binary_sha256']}
    REPORT['leaves'].append(entry)
    guard.save()
    info = compact(cnf, binary, cone)
    assert info['status'] == 'POSITIVE_CONE'
    c_check(f'{label}-independent', cnf, cone)
    database = dict(enumerate(base, 1))
    proof = []
    conclusion, skipped = discharge(base, read_cnf(cnf.read_bytes())[1], assumptions, cone, database, proof)
    lifted = OUT/f'{label}-discharged.lrat'
    write_proof(lifted, proof)
    entry.update(status='ABSENT_PREFIX_CHECKED', binary_bytes=binary.stat().st_size,
                 cone=info, lifted_steps=len(proof), lifted_bytes=lifted.stat().st_size,
                 tautologies_skipped=skipped, lifted_clause=database[conclusion],
                 shifts=audit_shifts(base, proof))
    guard.save()


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
    source = Path(os.environ['RETURN13_DEEP_PRIOR'])
    prior = json.loads(pin(source/'solve.json', plan['prior_receipt_sha256']))
    planned = json.loads(pin(Path(__file__).with_name('gpt_return13_deep_roots_plan.json'),
                             plan['full_plan_sha256']))['factors']
    seen = [item['prefix_in_variable_order'] for item in prior['leaves']]
    assert planned == seen + plan['factors'] and len(seen) == 57 and len(plan['factors']) == 15
    assert [item['prefix_in_variable_order'] for item in prior['leaves']
            if item['status'] == 'CONFLICT_LIMIT_UNKNOWN'] == ['000100000', '000111000']
    assert sum(item['status'] == 'ABSENT_PREFIX_CHECKED' for item in prior['leaves']) == 54
    saved = plan['interrupted']
    assert prior['leaves'][-1]['status'] == 'STARTED'
    assert all(prior['leaves'][-1][key] == saved[key] for key in
               ('label', 'prefix_in_variable_order', 'cnf_sha256'))
    assert [(item['name'], item['returncode'], item['reason']) for item in prior['commands'][-2:]] == [
        (saved['label'] + '-solve', 20, 'EXIT'), (saved['label'] + '-cake', 0, 'EXIT')]
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    base_path = OUT/'strip-base.cnf'
    base_path.write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf(base_path.read_bytes())[1] == base
    finish_saved_proof(source, saved, base, body)
    for factor in plan['factors']:
        check_leaf(f'factor-{factor}', factor, base, body)
    REPORT['status'] = 'DEEP_ROOT_RESUME_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_DEEP_RESUME_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
