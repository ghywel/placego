#!/usr/bin/env python3
"""Check learned-clause discharge on PHP and audit the retained P13 prefix partition."""
from collections import Counter
import json
import os
from pathlib import Path
import resource
import signal

from gpt_return13_binary_cert import c_check, compact, guard, pin

OUT = guard.OUT
REPORT = {'status': 'STARTED', 'commands': []}
guard.REPORT = REPORT


def read_cnf(data):
    header, *lines = data.decode().splitlines()
    magic, kind, variables, count = header.split()
    assert (magic, kind) == ('p', 'cnf')
    clauses = []
    for line in lines:
        *clause, terminator = map(int, line.split())
        assert terminator == 0 and all(0 < abs(literal) <= int(variables) for literal in clause)
        clauses.append(clause)
    assert len(clauses) == int(count)
    return int(variables), clauses


def rup_hints(clause, hints, database):
    """Retain just the ordered unit steps through the first conflict."""
    assigned = {abs(literal): literal < 0 for literal in clause}
    assert len(assigned) == len(clause)
    used = []
    for hint in hints:
        premise = database[hint]
        if any(assigned.get(abs(literal)) == (literal > 0) for literal in premise):
            continue
        unset = [literal for literal in premise if abs(literal) not in assigned]
        if len(unset) > 1:
            raise ValueError('NON_UNIT_HINT')
        used.append(hint)
        if not unset:
            return used
        literal = unset[0]
        assigned[abs(literal)] = literal > 0
    raise ValueError('NO_RUP_CONFLICT')


def add_step(clause, hints, database, proof):
    checked = rup_hints(clause, hints, database)
    index = len(database) + 1
    database[index] = clause
    proof.append((index, clause, checked))
    return index


def discharge(base, branch, assumptions, cone, database, proof):
    expected_units = [[literal] for literal in assumptions]
    if branch != base + expected_units:
        raise ValueError('ASSUMPTION_OR_BASE_MISMATCH')
    assert len({abs(literal) for literal in assumptions}) == len(assumptions)
    guard_clause = [-literal for literal in assumptions]
    assumed = set(assumptions)
    mapping = {i: i for i in range(1, len(base) + 1)}
    mapping.update({i: None for i in range(len(base) + 1, len(branch) + 1)})
    last_original = None
    skipped = 0
    for line in cone.read_text().splitlines():
        index, *rest = map(int, line.split())
        end = rest.index(0)
        clause, hints = rest[:end], rest[end + 1:-1]
        assert rest[-1] == 0 and all(0 < hint < index for hint in hints)
        assert index > len(branch) and index not in mapping
        assert len({abs(literal) for literal in clause}) == len(clause)
        if assumed.intersection(clause):
            mapping[index] = None
            skipped += 1
        else:
            lifted = list(dict.fromkeys(clause + guard_clause))
            kept = [mapping[hint] for hint in hints if mapping[hint] is not None]
            mapping[index] = add_step(lifted, kept, database, proof)
        last_original = clause
    assert last_original == [] and database[mapping[index]] == guard_clause
    return mapping[index], skipped


def write_proof(path, proof):
    with path.open('w') as output:
        for index, clause, hints in proof:
            output.write(' '.join(map(str, [index, *clause, 0, *hints, 0])) + '\n')


def check_join():
    control_dir = Path(os.environ['LRAT_FORMAT_CONTROL_DIR'])
    data = pin(control_dir/'php.cnf', '4fa2e5d8b36454ba6b01e1a92161e90e46cd16b0f19b41cdf148e49a87c741a1')
    variables, base = read_cnf(data)
    assert (variables, len(base)) == (20, 75)
    original = OUT/'php-original.cnf'
    original.write_bytes(data)
    database = dict(enumerate(base, 1))
    proof, exclusions = [], []
    REPORT['branches'] = []
    for label, assumption in [('positive', 1), ('negative', -1)]:
        cnf = OUT/f'{label}.cnf'
        cnf.write_bytes(f'p cnf {variables} {len(base) + 1}\n'.encode()
                        + data.split(b'\n', 1)[1] + f'{assumption} 0\n'.encode())
        branch = read_cnf(cnf.read_bytes())[1]
        binary = OUT/f'{label}.clrat'
        cone = OUT/f'{label}-cone.lrat'
        guard.call(f'{label}-solve', [guard.CADICAL, '-q', '--lrat', '--binary', str(cnf), str(binary)], 3, 6, 20)
        guard.cake(f'{label}-cake', cnf, binary, True)
        info = compact(cnf, binary, cone)
        assert info['status'] == 'POSITIVE_CONE' and info['used_additions'] > 1
        c_check(f'{label}-cone', cnf, cone)
        try:
            discharge(base, branch, [-assumption], cone, database, proof)
        except ValueError as error:
            assert str(error) == 'ASSUMPTION_OR_BASE_MISMATCH'
        else:
            raise AssertionError('ASSUMPTION_POLARITY_ACCEPTED')
        exclusion, skipped = discharge(base, branch, [assumption], cone, database, proof)
        exclusions.append(exclusion)
        REPORT['branches'].append({'assumption': assumption, 'cone': info,
                                    'discharged_clause': database[exclusion], 'tautologies_skipped': skipped})
        guard.save()
    try:
        rup_hints([], exclusions[:1], database)
    except ValueError as error:
        assert str(error) == 'NO_RUP_CONFLICT'
    else:
        raise AssertionError('MISSING_CHILD_ACCEPTED')
    mutant = OUT/'one-child.lrat'
    write_proof(mutant, proof + [(len(database) + 1, [], exclusions[:1])])
    guard.cake('one-child-reject', original, mutant, False)
    add_step([], exclusions, database, proof)
    joined = OUT/'joined-original.lrat'
    write_proof(joined, proof)
    guard.cake('join-cake', original, joined, True)
    c_check('join-independent', original, joined)
    REPORT['joined'] = {'steps': len(proof), 'bytes': joined.stat().st_size,
                        'original_clauses': len(base), 'checkers': 'cake_lpr and lrat-check',
                        'one_child_and_wrong_polarity_rejected': True}


def prefix_partition(words, width):
    """Yield each allowed word and every first absent prefix exactly once."""
    stack = [('', words)]
    while stack:
        prefix, extensions = stack.pop()
        if not extensions or len(prefix) == width:
            yield prefix, bool(extensions)
            continue
        depth = len(prefix)
        for bit in (1, 0):
            stack.append((prefix + str(bit), [word for word in extensions if (word >> depth) & 1 == bit]))


def audit_trie():
    data = pin(os.environ['RETURN13_ORIGINAL_CNF'], 'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0')
    projection = json.loads(pin(os.environ['RETURN13_PROJECTION_JSON'], '35564e639dc174896d35263580f10f9ee11336b789dd55588202d6d22dae5592'))
    variables, clauses = read_cnf(data)
    target = projection['target']
    assert target['complete'] and (target['p'], target['q'], target['offset'], target['w']) == (13, 65, 6, 16)
    words = target['words']
    assert (variables, len(clauses), len(words), len(set(words))) == (910, 5214, 170, 170)
    assert all(0 <= word < 2**16 for word in words)
    expected = [[-(7 + bit) if word & (1 << bit) else 7 + bit for bit in range(16)] for word in words]
    assert clauses[5044:] == expected
    leaves = list(prefix_partition(words, 16))
    cursor = 0
    absent = Counter()
    found = set()
    entries = []
    for prefix, retained in leaves:
        depth = len(prefix)
        start = int(prefix, 2) << (16 - depth)
        stop = start + (1 << (16 - depth))
        assert start == cursor
        cursor = stop
        if retained:
            assert depth == 16
            word = int(prefix[::-1], 2)
            assert word in words and word not in found
            found.add(word)
        else:
            assert not any(format(word, '016b')[::-1].startswith(prefix) for word in words)
            absent[depth] += 1
        entries.append({'prefix_in_variable_order': prefix, 'retained': retained})
    assert cursor == 2**16 and found == set(words)
    (OUT/'prefix-leaves.json').write_text(json.dumps(entries, indent=2)+'\n')
    REPORT['partition'] = {'retained': len(found), 'absent': sum(absent.values()),
                           'absent_by_depth': dict(sorted(absent.items())),
                           'intervals_cover_16_bits': True, 'exact_original_blockers': True}


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 120))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: guard.STOP.append(s))
    for path, sha in [(guard.CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                      (guard.CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                      (guard.LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1')]:
        pin(path, sha)
    check_join()
    audit_trie()
    REPORT['status'] = 'CONTROL_AND_PARTITION_CHECKED'
    guard.thermal()
    guard.save()
    print('RETURN13_PREFIX_CONTROL_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        guard.save()
