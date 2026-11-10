#!/usr/bin/env python3
"""Measure two fixed absent-prefix proofs in the original P13 strip geometry."""
import hashlib
import json
import os
from pathlib import Path
import resource
import signal

from gpt_return13_prefix_control import discharge, read_cnf, rup_hints, write_proof
from gpt_return13_binary_cert import compact, guard, pin

OUT = guard.OUT
REPORT = {'status': 'STARTED', 'commands': [], 'leaves': []}
guard.REPORT = REPORT
WIDTH = 65


def column(literal):
    return (abs(literal) - 1) % WIDTH


def shifted(literal, delta):
    if not 0 <= column(literal) + delta < WIDTH:
        raise ValueError('SHIFT_LEAVES_STRIP')
    return literal + (delta if literal > 0 else -delta)


def audit_shifts(base, proof):
    original = len(base)
    support = sorted({hint for _, _, hints in proof for hint in hints if hint <= original})
    literals = [literal for hint in support for literal in base[hint - 1]]
    literals.extend(literal for _, clause, _ in proof for literal in clause)
    low = min(map(column, literals))
    high = max(map(column, literals))
    clause_ids = {tuple(sorted(clause)): i for i, clause in enumerate(base, 1)}
    tested = sorted({-low, 0, WIDTH - 1 - high})
    for delta in tested:
        mapping = {hint: clause_ids[tuple(sorted(shifted(literal, delta) for literal in base[hint - 1]))]
                   for hint in support}
        database = dict(enumerate(base, 1))
        for index, clause, hints in proof:
            new_clause = [shifted(literal, delta) for literal in clause]
            rup_hints(new_clause, [mapping[hint] for hint in hints], database)
            database[index] = new_clause
            mapping[index] = index
        assert database[proof[-1][0]] == [shifted(literal, delta) for literal in proof[-1][1]]
    return {'original_support_clauses': len(support), 'used_columns': [low, high],
            'in_bounds_shift_interval': [-low, WIDTH - 1 - high], 'replayed_shifts': tested}


def check_leaf(label, prefix, base, body):
    entry = {'label': label, 'prefix_in_variable_order': prefix, 'status': 'STARTED'}
    REPORT['leaves'].append(entry)
    assumptions = [(7 + index) * (1 if bit == '1' else -1) for index, bit in enumerate(prefix)]
    cnf = OUT/f'{label}.cnf'
    binary = OUT/f'{label}.clrat'
    cone = OUT/f'{label}-cone.lrat'
    units = ''.join(f'{literal} 0\n' for literal in assumptions).encode()
    cnf.write_bytes(f'p cnf 910 {len(base) + len(assumptions)}\n'.encode() + body + units)
    entry['cnf_sha256'] = hashlib.sha256(cnf.read_bytes()).hexdigest()
    guard.save()
    rc, output = guard.call(f'{label}-solve', [guard.CADICAL, '-q', '-c', '3000', '--lrat', '--binary',
                                              str(cnf), str(binary)], 12, 25)
    if rc == 0:
        assert 's UNKNOWN' in output
        entry.update(status='CONFLICT_LIMIT_UNKNOWN', binary_bytes=binary.stat().st_size)
        guard.save()
        return
    assert rc == 20, (label, rc, output[-1000:])
    guard.cake(f'{label}-cake', cnf, binary, True, 10, 20)
    info = compact(cnf, binary, cone)
    assert info['status'] == 'POSITIVE_CONE'
    _, output = guard.call(f'{label}-independent', [guard.LRAT_CHECK, str(cnf), str(cone)], 5, 15, 0)
    assert 'c VERIFIED' in output.splitlines()
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
    resource.setrlimit(resource.RLIMIT_CPU, (12, 120))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in [(guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                      (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                      (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1')]:
        pin(path, sha)
    data = pin(os.environ['RETURN13_ORIGINAL_CNF'], 'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    leaves = json.loads(pin(os.environ['RETURN13_PREFIX_LEAVES'], '4fd926b2b495dd046f1b24a5e67700f7823f79208cc219be23b4751992a19884'))
    absent = [leaf['prefix_in_variable_order'] for leaf in leaves if not leaf['retained']]
    deep = min(absent, key=lambda p: (-len(p), p))
    shallow = min(absent, key=lambda p: (len(p), p))
    assert (deep, shallow) == ('0000000000000001', '0000100')
    variables, original = read_cnf(data)
    assert (variables, len(original)) == (910, 5214)
    base = original[:5044]
    body = b''.join(data.splitlines(keepends=True)[1:5045])
    (OUT/'strip-base.cnf').write_bytes(b'p cnf 910 5044\n' + body)
    assert read_cnf((OUT/'strip-base.cnf').read_bytes())[1] == base
    for label, prefix in [('depth16', deep), ('depth7', shallow)]:
        check_leaf(label, prefix, base, body)
    REPORT['status'] = 'TWO_FIXED_LEAVES_RECORDED'
    guard.thermal()
    guard.save()
    print('RETURN13_FIXED_LEAVES_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
