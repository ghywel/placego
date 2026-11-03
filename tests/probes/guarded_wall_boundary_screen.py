#!/usr/bin/env python3
"""GC2410 fixed original-CNF unit-closure screen; no SAT search or new CNF.

Inputs are the retained GC2399 export, pinned by digest. Output reasons certify
each forced literal; a second sequential replay checks that trace. Unresolved
clauses are not SAT witnesses or independent bits. See the frozen pilot report.
"""
import hashlib
import json
import os
from pathlib import Path

BASE = 'fcb4dd1374cc63643a22caf0f1f1ebdefb124a6114173cb65722387f55861e96'
OBS = 'a1c848b726b2cbb2b618e425ebcd3fda099eadca994468eb896a52fed36c728b'


def unit_closure(clauses, nv):
    values = [0] * (nv + 1)
    trail = []
    passes = 0
    while True:
        passes += 1
        changed = False
        for cid, clause in enumerate(clauses, 1):
            live = []
            for lit in clause:
                v = values[abs(lit)]
                if v == (1 if lit > 0 else -1):
                    break
                if not v:
                    live.append(lit)
            else:
                if not live:
                    return values, trail, passes, cid
                if len(live) == 1:
                    lit = live[0]
                    values[abs(lit)] = 1 if lit > 0 else -1
                    trail.append((lit, cid))
                    changed = True
        if not changed:
            return values, trail, passes, None


def replay(clauses, trail, conflict=None):
    known = {}
    for lit, cid in trail:
        assert abs(lit) not in known
        unknown = []
        for v in clauses[cid-1]:
            if abs(v) not in known:
                unknown.append(v)
            else:
                assert known[abs(v)] != (v > 0)
        assert unknown == [lit]
        known[abs(lit)] = lit > 0
    if conflict is not None:
        assert all(abs(v) in known and known[abs(v)] != (v > 0)
                   for v in clauses[conflict-1])
    return known


def main():
    # Independent fixed controls: propagation, contradiction, and incompleteness.
    for cs, expected, bad in [([[1], [-1, 2], [-2, 3]], [0, 1, 1, 1], False),
                              ([[1], [-1]], [0, 1, 0, 0], True),
                              ([[1, 2], [-1, 2]], [0, 0, 0, 0], False)]:
        vals, tr, _, conflict = unit_closure(cs, 3)
        assert vals == expected and (conflict is not None) == bad
        replay(cs, tr, conflict)
    # Last control logically forces variable2, but unit propagation leaves it
    # unresolved. Never label an unresolved output a satisfying assignment.
    out = Path(os.environ['CAPPED_OUT'])
    src = Path(os.environ['GUARDED_EXPORT'])
    raw = (src/'original.cnf').read_bytes()
    obs_raw = (src/'obligations.jsonl').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == BASE
    assert hashlib.sha256(obs_raw).hexdigest() == OBS
    lines = raw.decode().splitlines()
    assert lines[0] == 'p cnf 28672 95233'
    clauses = []
    for line in lines[1:]:
        a = list(map(int, line.split()))
        assert a[-1] == 0 and all(1 <= abs(v) <= 28672 for v in a[:-1])
        assert len(set(a[:-1])) == len(a[:-1])
        clauses.append(a[:-1])
    assert len(clauses) == 95233
    obs = [json.loads(line) for line in obs_raw.decode().splitlines()]
    assert len(obs) == 389
    vals, trail, passes, conflict = unit_closure(clauses, 28672)
    known = replay(clauses, trail, conflict)
    assert len(known) == sum(v != 0 for v in vals)
    for v, value in known.items():
        assert vals[v] == (1 if value else -1)
    (out/'unit-trail.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in trail))
    summary = {'original_sha256': BASE, 'obligations_sha256': OBS,
               'solver_calls': 0, 'controls': '3 fixed unit-trace controls PASS',
               'forced_variables': len(trail), 'passes': passes,
               'original_conflict_clause': conflict,
               'global_deviation_clause_used_as_reason': any(cid == 95233 for _, cid in trail)}
    if conflict is not None:
        summary['status'] = 'UNEXPECTED_ORIGINAL_UNIT_CONTRADICTION_NOT_EXTERNALLY_CHECKED'
    else:
        # Independent full fixed-point check: every unsatisfied input clause
        # has at least two unassigned literals.
        for c in clauses:
            if any(vals[abs(v)] == (1 if v > 0 else -1) for v in c):
                continue
            assert sum(vals[abs(v)] == 0 for v in c) >= 2
        groups = {'satisfied_by_original_units': [], 'unresolved': [], 'falsified': []}
        reasons = {abs(lit): cid for lit, cid in trail}
        for o in obs:
            assert o['original_sha256'] == BASE
            assert o['negated_clause_units'] == [[-v] for v in o['clause']]
            yes = [v for v in o['clause'] if vals[abs(v)] == (1 if v > 0 else -1)]
            unknown = [v for v in o['clause'] if vals[abs(v)] == 0]
            kind = 'satisfied_by_original_units' if yes else 'unresolved' if unknown else 'falsified'
            groups[kind].append({'phase': o['phase'], 'word': o['word'], 'time': o['time'],
                                 'j': o['j'], 'satisfying_literals': yes,
                                 'literal_reasons': [reasons[abs(v)] for v in yes],
                                 'unassigned_literals': len(unknown)})
        selected = [o for o in groups['satisfied_by_original_units']
                    if (o['phase'], o['word']) == (882, 0)]
        assert len(selected) == 1 and -2297 in selected[0]['satisfying_literals']
        summary['counts'] = {k: len(v) for k, v in groups.items()}
        summary['canonical_survivor'] = min(groups['unresolved'],
            key=lambda o: (o['phase'], o['word'])) if groups['unresolved'] else None
        summary['status'] = 'ORIGINAL_UNIT_CLOSURE_SCREENED_NOT_SAT_OR_ALL_CLAUSE_CERTIFICATE'
        (out/'classification.json').write_text(json.dumps(groups, indent=2)+'\n')
    (out/'screen.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('GUARDED_BOUNDARY_SCREEN_DONE')


if __name__ == '__main__':
    main()
