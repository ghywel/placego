#!/usr/bin/env python3
"""GC2406: read-only dependency/RUP audit of the existing one-clause LRAT.

No solver, checker process, trajectory or proof search. Restricts itself to
positive RUP hints in the reachable subproof; RAT would require another audit.
After discovering the small support, validation prediction: exactly five input
clauses and three additions suffice; flipping the final input unit is rejected.
Record searched: GC2400/2401, original generator and retained accepted proof.
"""
import argparse
import hashlib
import json
from pathlib import Path

TARGET = 'bb6da64edc7caff3791df90230132a4a0fdeeb6dc4020d687fffde725b21df2a'
PROOF = 'b2288eebdb9b32591f9ddc8195e11f66fd269a990e44888469f431d29e7a03d3'


def rup(clause, hints, database):
    assigned = {abs(v): v < 0 for v in clause}
    for h in hints:
        if h <= 0:
            raise ValueError('RAT/negative hint unsupported')
        source = database[h]
        if any(assigned.get(abs(v)) == (v > 0) for v in source
               if abs(v) in assigned):
            return False
        unset = [v for v in source if abs(v) not in assigned]
        if not unset:
            return True
        if len(unset) != 1:
            return False
        v = unset[0]
        assigned[abs(v)] = v > 0
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('stage', type=Path)
    args = ap.parse_args()
    target = (args.stage / 'original-plus-negation.cnf').read_bytes()
    proof = (args.stage / 'clause.lrat').read_bytes()
    assert hashlib.sha256(target).hexdigest() == TARGET
    assert hashlib.sha256(proof).hexdigest() == PROOF
    lines = target.decode().splitlines()
    assert lines[0] == 'p cnf 28672 95242'
    original = {n: list(map(int, line.split()))[:-1]
                for n, line in enumerate(lines[1:], 1)}
    added = {}
    for line in proof.decode().splitlines():
        fields = line.split()
        if fields[1] == 'd':
            continue
        values = list(map(int, fields))
        zero = values.index(0, 1)
        assert values[0] not in added and values[-1] == 0
        added[values[0]] = (values[1:zero], values[zero+1:-1])
    final = max(added)
    assert added[final][0] == []
    reachable, todo = set(), [final]
    while todo:
        n = todo.pop()
        if n in reachable:
            continue
        reachable.add(n)
        if n in added:
            hints = added[n][1]
            assert all(0 < h < n for h in hints)
            todo.extend(hints)
        else:
            assert n in original
    inputs = {n: original[n] for n in sorted(reachable) if n in original}
    steps = {n: added[n] for n in sorted(reachable) if n in added}
    assert list(inputs) == [249, 250, 3785, 3788, 95234]
    assert list(steps) == [95728, 95729, 104404]
    database = dict(inputs)
    for n, (clause, hints) in steps.items():
        assert rup(clause, hints, database)
        database[n] = clause
    bad = dict(database)
    bad[95234] = [-2297]
    assert not rup(*added[final], bad)
    print(json.dumps({'status': 'EXISTING_PROOF_SUPPORT_AUDITED_NOT_NEW_SOLVER_RUN',
                      'target_sha256': TARGET, 'proof_sha256': PROOF,
                      'input_clauses': inputs, 'derived_steps': steps,
                      'unused_other_eight_negation_units': True,
                      'uses_global_deviation_clause_95233': False,
                      'negative_control': 'flip unit2297; final RUP rejects'}, indent=2))


if __name__ == '__main__':
    main()
