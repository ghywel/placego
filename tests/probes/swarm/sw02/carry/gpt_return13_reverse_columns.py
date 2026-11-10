#!/usr/bin/env python3
"""Query the last P13 branch with reversed DIMACS columns and restore the exact original proof."""
import json
import os
from pathlib import Path
import resource
import signal
import sys

from gpt_return13_binary_cert import c_check, compact
from gpt_return13_factor_split import check_parent
from gpt_return13_final_splits import join
from gpt_return13_prefix_control import discharge, write_proof
from gpt_return13_prefix_leaves import OUT, REPORT, audit_shifts, guard, pin, read_cnf
from gpt_return13_prefix_replay import read_proof

TARGET = '100000000'
SIBLING = '100000001'


def reverse(literal):
    row, col = divmod(abs(literal) - 1, 65)
    return (65 * row + 65 - col) * (1 if literal > 0 else -1)


def write_cnf(path, clauses):
    with path.open('w') as output:
        output.write(f'p cnf 910 {len(clauses)}\n')
        for clause in clauses:
            output.write(' '.join(map(str, [*clause, 0])) + '\n')


def restore_cone(source, target):
    with source.open() as input_proof, target.open('w') as output_proof:
        for line in input_proof:
            index, *rest = map(int, line.split())
            end = rest.index(0)
            assert rest[-1] == 0 and all(0 < hint < index for hint in rest[end+1:-1])
            clause = [reverse(literal) for literal in rest[:end]]
            output_proof.write(' '.join(map(str, [index, *clause, *rest[end:]]))+'\n')


def main():
    plan = json.loads(Path(sys.argv[1]).read_bytes())
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (12 if soft == resource.RLIM_INFINITY else min(12, soft), hard))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, digest in plan['tool_sha256'].items():
        pin(path, digest)
    source = Path(os.environ['RETURN13_SOURCE_ROOT'])
    previous = json.loads(pin(source/plan['guided_receipt']['file'], plan['guided_receipt']['sha256']))
    assert previous['status'] == 'LEMMA_GUIDED_CONFLICT_LIMIT_UNKNOWN'
    original = pin(os.environ['RETURN13_ORIGINAL_CNF'], plan['original_cnf_sha256'])
    variables, clauses = read_cnf(original)
    assert (variables, len(clauses)) == (910, 5214)
    base = clauses[:5044]
    body = b''.join(original.splitlines(keepends=True)[1:5045])
    sibling = read_proof(pin(source/plan['sibling']['file'], plan['sibling']['sha256']), base, SIBLING)
    branch = base + [[(7 + i) * (1 if bit == '1' else -1)] for i, bit in enumerate(TARGET)]
    assert all(reverse(reverse(v)) == v and reverse(-v) == -reverse(v) for v in range(1,911))
    permuted = [[reverse(literal) for literal in clause] for clause in branch]
    assert [[reverse(literal) for literal in clause] for clause in permuted] == branch
    assert permuted != branch and len(permuted) == 5053
    raw = OUT/'reversed.clrat'
    cnf = OUT/'reversed.cnf'
    write_cnf(cnf, permuted)
    rc, output = guard.call('reverse-column-solve', [guard.CADICAL, '-q', '-c', '3000', '--lrat', '--binary',
                                                     str(cnf), str(raw)], 12, 25)
    if rc == 0:
        assert output.strip() in {'s UNKNOWN', 'c UNKNOWN'}
        REPORT['status'] = 'REVERSE_COLUMNS_CONFLICT_LIMIT_UNKNOWN'
    else:
        assert rc == 20, (rc, output[-1000:])
        guard.cake('reverse-column-cake', cnf, raw, True, 10, 20)
        cone = OUT/'reversed-cone.lrat'
        info = compact(cnf, raw, cone)
        assert info['status'] == 'POSITIVE_CONE'
        original_cnf = OUT/'original-child.cnf'
        original_cone = OUT/'original-child-cone.lrat'
        write_cnf(original_cnf, branch)
        expected_child = pin(source/plan['original_child']['file'], plan['original_child']['sha256'])
        assert original_cnf.read_bytes() == expected_child
        restore_cone(cone, original_cone)
        guard.cake('restored-child-cake', original_cnf, original_cone, True, 10, 20)
        c_check('restored-child-independent', original_cnf, original_cone)
        child = []
        database = dict(enumerate(base, 1))
        discharge(base, branch, [unit[0] for unit in branch[len(base):]], original_cone, database, child)
        write_proof(OUT/f'parent-{TARGET}-discharged.lrat', child)
        parent = join(base, '10000000', [child, sibling])
        write_proof(OUT/'parent-10000000-discharged.lrat', parent)
        check_parent(base, body, parent, 'parent-10000000')
        REPORT.update(status='ORIGINAL_BASE_BRANCH_AND_PARENT_CHECKED', child_steps=len(child),
                      parent_steps=len(parent), child_shifts=audit_shifts(base, child),
                      parent_shifts=audit_shifts(base, parent), cone=info)
    guard.thermal()
    guard.save()
    print('RETURN13_REVERSE_COLUMNS_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
