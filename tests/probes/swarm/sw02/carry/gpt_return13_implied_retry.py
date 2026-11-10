#!/usr/bin/env python3
"""Try the last P13 branch with checked shifted lemmas, then expand the used proofs."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_binary_cert import c_check, compact
from gpt_return13_factor_split import check_parent
from gpt_return13_final_splits import join
from gpt_return13_prefix_control import add_step, discharge, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, guard, pin, read_cnf, shifted
from gpt_return13_prefix_replay import read_proof

TARGET = '100000000'
SIBLING = '100000001'


def write_cnf(path, clauses):
    with path.open('w') as output:
        output.write(f'p cnf 910 {len(clauses)}\n')
        for clause in clauses:
            output.write(' '.join(map(str, [*clause, 0])) + '\n')


def translated_premises(base, index, proof, delta):
    support = {hint for _, _, hints in proof for hint in hints if hint <= len(base)}
    return {hint: index[tuple(sorted(shifted(literal, delta) for literal in base[hint - 1]))]
            for hint in sorted(support)}


def add_translated_proof(proof, delta, mapping, database, expanded):
    for index, clause, hints in proof:
        mapping[index] = add_step([shifted(literal, delta) for literal in clause],
                                  [mapping[hint] for hint in hints], database, expanded)
    return mapping[proof[-1][0]]


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in plan['tool_sha256'].items():
        pin(path, digest)
    source = Path(os.environ['RETURN13_SOURCE_ROOT'])
    last = json.loads(pin(source/plan['final_splits']['file'], plan['final_splits']['sha256']))
    assert [row['prefix_in_variable_order'] for row in last['leaves']
            if row['status']=='CONFLICT_LIMIT_UNKNOWN'] == [TARGET]
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    base_index = {tuple(sorted(clause)): i for i, clause in enumerate(base, 1)}
    expected = {word for word in json.loads(pin(source/plan['factors']['file'],
                                                plan['factors']['sha256'])).values() if len(word)==7}
    assert len(expected) == 22 and set(plan['proofs']) == expected
    proofs = {factor: read_proof(pin(source/spec['file'], spec['sha256']), base, factor)
              for factor, spec in plan['proofs'].items()}
    sibling = read_proof(pin(source/plan['sibling']['file'], plan['sibling']['sha256']), base, SIBLING)
    try:
        translated_premises(base, base_index, proofs['0000100'], 41)
    except KeyError as error:
        assert error.args == ((-65, 64, 129),)
    else:
        raise AssertionError('MISSING_TRANSLATED_PREMISE_ACCEPTED')
    candidates = {}
    for factor, proof in proofs.items():
        for delta in range(10):
            mapping = translated_premises(base, base_index, proof, delta)
            exclusion = [shifted(literal, delta) for literal in proof[-1][1]]
            candidates[len(base) + len(candidates) + 1] = (factor, delta, exclusion, mapping)
    assert len(candidates) == 220
    augmented = base + [item[2] for item in candidates.values()]
    units = [[(7 + i) * (1 if bit == '1' else -1)] for i, bit in enumerate(TARGET)]
    branch = augmented + units
    cnf, binary, cone = (OUT/name for name in ('augmented.cnf', 'augmented.clrat', 'augmented-cone.lrat'))
    write_cnf(cnf, branch)
    rc, output = guard.call('lemma-guided-solve', [guard.CADICAL, '-q', '-c', '3000', '--lrat', '--binary',
                                                   str(cnf), str(binary)], 12, 25)
    if rc == 0:
        assert output.strip() in {'s UNKNOWN', 'c UNKNOWN'}
        REPORT['status'] = 'LEMMA_GUIDED_CONFLICT_LIMIT_UNKNOWN'
    else:
        assert rc == 20, (rc, output[-1000:])
        guard.cake('augmented-cake', cnf, binary, True, 10, 20)
        info = compact(cnf, binary, cone)
        assert info['status'] == 'POSITIVE_CONE'
        c_check('augmented-independent', cnf, cone)
        augmented_proof = []
        augmented_database = dict(enumerate(augmented, 1))
        discharge(augmented, branch, [unit[0] for unit in units], cone, augmented_database, augmented_proof)
        used = sorted({hint for _, _, hints in augmented_proof for hint in hints if hint in candidates})
        database = dict(enumerate(base, 1))
        expanded = []
        mapping = {index: index for index in database}
        for clause_id in used:
            factor, delta, exclusion, premises = candidates[clause_id]
            mapped = add_translated_proof(proofs[factor], delta, premises.copy(), database, expanded)
            assert database[mapped] == exclusion
            mapping[clause_id] = mapped
        for index, clause, hints in augmented_proof:
            mapping[index] = add_step(clause, [mapping[hint] for hint in hints], database, expanded)
        assert expanded[-1][1] == [-unit[0] for unit in units]
        write_proof(OUT/f'parent-{TARGET}-discharged.lrat', expanded)
        check_parent(base, body, expanded, f'parent-{TARGET}')
        child_shifts = audit_shifts(base, expanded)
        parent = join(base, '10000000', [expanded, sibling])
        write_proof(OUT/'parent-10000000-discharged.lrat', parent)
        check_parent(base, body, parent, 'parent-10000000')
        parent_shifts = audit_shifts(base, parent)
        REPORT.update(status='ORIGINAL_BASE_BRANCH_AND_PARENT_CHECKED', expanded_steps=len(expanded),
                      parent_steps=len(parent), used_shifted_lemmas=[candidates[index][:2] for index in used],
                      child_shifts=child_shifts, parent_shifts=parent_shifts)
    guard.thermal()
    guard.save()
    print('RETURN13_IMPLIED_RETRY_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
