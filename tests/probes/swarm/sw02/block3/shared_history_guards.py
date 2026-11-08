#!/usr/bin/env python3
"""Lift the four historical guards into the original physical4,7 CNF.

No target solve: map old certificates, check a conditionalized RUP prefix by
unit propagation, and compare the original/augmented shared-row consequences.
The prefix can precede a future augmented-CNF refutation, retaining proof of
the original formula. All data and proofs are written outside git.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

from pysat.solvers import Minisat22

import e_short_guard as short
import physical_47 as phys


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def canon(c):
    return tuple(sorted(set(c)))


def target():
    gaps = phys.E + phys.A * 4 + phys.E + phys.A * 7 + phys.E
    black = {0}
    s = 0
    for g in gaps:
        s += int(g)
        black.add(s)
    assert 1 + 2 * s == 359
    wanted = {1 + 2 * j: j in black for j in range(s + 1)}
    C, off, W = phys.generate(359, wanted)
    return C, off, W, wanted


def mapping(ids, true, off, delta):
    m = {true: 1}
    for t, vs in enumerate(ids):
        for x, v in enumerate(vs, 1):
            m[v] = off[t + delta] + x
    assert len(set(m.values())) == len(m)
    return m


def mapped(c, m):
    return [m[abs(v)] if v > 0 else -m[abs(v)] for v in c]


def write_proof_line(f, c, delete=False):
    f.write(('d ' if delete else '') + ' '.join(map(str, c)) + (' ' if c else '') + '0\n')


def prove_prefix(C, off, guards, out):
    original = {canon(c) for c in C}
    summaries = []
    units = []
    # This solver is used only for propagation, never solve()/solve_limited().
    with Minisat22(bootstrap_with=C) as checker, (out / 'lemma-prefix.drup').open('w') as prefix:
        for delta, t, opposite in itertools.product((108, 274), (10, 13), (0, 1)):
            if opposite != (1 if t == 10 else 0):
                continue
            source, ids, true = short.build('253353', (t, opposite))
            m = mapping(ids, true, off, delta)
            negative = mapped(source[-1], m)[0]
            conclusion = -negative
            units.append(conclusion)
            assert all(canon(mapped(c, m)) in original for c in source[:-1])
            wrong = mapping(ids, true, off, delta + 1)
            assert any(canon(mapped(c, wrong)) not in original for c in source[:-1])
            stem = out / ('guard' + str(delta + t))
            phys.dimacs(stem.with_suffix('.cnf'), C + [[negative]], off[-1])
            additions = 0
            deletions = 0
            last = None
            with (guards / f'guard{t}.drat').open() as src, stem.with_suffix('.drat').open('w') as translated:
                for line in src:
                    tokens = line.split()
                    if not tokens or tokens[0] == 'c':
                        continue
                    delete = tokens[0] == 'd'
                    nums = list(map(int, tokens[1:] if delete else tokens))
                    assert nums[-1] == 0
                    c = mapped(nums[:-1], m)
                    write_proof_line(translated, c, delete)
                    if delete:
                        # Extra clauses preserve RUP. No RAT claim is used.
                        deletions += 1
                        continue
                    conditional = list(dict.fromkeys(c + [conclusion]))
                    ok, _ = checker.propagate(assumptions=[-v for v in conditional])
                    assert not ok, ('not RUP', delta + t, additions, conditional)
                    checker.add_clause(conditional)
                    write_proof_line(prefix, conditional)
                    additions += 1
                    last = conditional
            assert last == [conclusion]
            # A wrong-sign unit must fail this same RUP verifier unless the
            # already checked prefix has exposed a genuine UP refutation.
            root_ok, _ = checker.propagate()
            if root_ok:
                ok, _ = checker.propagate(assumptions=[conclusion])
                assert ok, 'wrong-sign control failed in consistent context'
            summaries.append({'tick': delta + t, 'column': 8, 'value': int(conclusion > 0),
                              'source_tick': t, 'even_shift': delta,
                              'all_source_premises_in_original': True,
                              'wrong_phase_embedding_rejected': True,
                              'RUP_additions_checked': additions,
                              'source_deletions_ignored_in_prefix': deletions,
                              'wrong_sign_RUP_rejected': True if root_ok else 'SKIPPED_UP_UNSAT',
                              'prefix_UP_conflict': not root_ok,
                              'source_proof_sha256': sha(guards / f'guard{t}.drat'),
                              'mapped_proof_sha256': sha(stem.with_suffix('.drat'))})
        root_ok, _ = checker.propagate()
        if not root_ok:
            write_proof_line(prefix, [])
    return units, summaries


def seam(vals, off, W, t):
    return {x: int(vals[off[t] + x]) for x in range(1, W - t + 1) if off[t] + x in vals}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--original', type=Path, required=True)
    p.add_argument('--guards', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    C, off, W, wanted = target()
    original = phys.dimacs(a.out / 'original.cnf', C, off[-1])
    assert original['sha256'] == sha(a.original) == '21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    # Exhaustive gate truth-table control, independent of the CNF generator.
    for u, v, w, z in itertools.product((False, True), repeat=4):
        values = {1: u, 2: v, 3: w, 4: z}
        sat = all(any(values[abs(l)] == (l > 0) for l in c) for c in phys.gate(1, 2, 3, 4))
        assert sat == (z == (u != (v or w)))
    before, log0, conf0 = phys.propagate(C)
    assert conf0 is None and phys.replay_units(C, log0, conf0) == before
    corrupt = [x[:] for x in log0]
    corrupt[0][0] *= -1
    try:
        phys.replay_units(C, corrupt, conf0)
    except AssertionError:
        pass
    else:
        raise AssertionError('corrupt unit reason accepted')
    units, proof_info = prove_prefix(C, off, a.guards, a.out)
    assert [(q['tick'], q['value']) for q in proof_info] == [(118, 0), (121, 1), (284, 0), (287, 1)]
    augmented = C + [[u] for u in units]
    after, log, conflict = phys.propagate(augmented)
    assert phys.replay_units(augmented, log, conflict) == after
    delta = {v: val for v, val in after.items() if v not in before}
    for v, value in before.items():
        if conflict is None or v in after:
            assert after[v] == value
    coordinates = {off[t] + x: [t, x] for t in range(360) for x in range(1, W - t + 1)}
    changes = [{'tick': coordinates[v][0], 'column': coordinates[v][1], 'value': int(val)}
               for v, val in sorted(delta.items())]
    r = {'original': original, 'original_clauses': len(C), 'original_variables': off[-1],
         'guard_proofs': proof_info, 'lemma_prefix_sha256': sha(a.out / 'lemma-prefix.drup'),
         'before_forced': len(before), 'after_forced': len(after), 'new_forced': len(delta),
         'UP_conflict': conflict, 'prefix_UP_conflict': any(q['prefix_UP_conflict'] for q in proof_info),
         'unit_reason_replay': True, 'gate_control': True,
         'corrupt_reason_rejected': True, 'seams': [], 'new_assignments': changes,
         'target_solve_performed': False}
    for t in (69, 193, 359):
        b, c = seam(before, off, W, t), seam(after, off, W, t)
        r['seams'].append({'tick': t, 'width': W - t, 'before': b, 'after': c,
                           'new': {k: v for k, v in c.items() if k not in b}})
    (a.out / 'unit-log.json').write_text(json.dumps({'log': log, 'conflict': conflict}) + '\n')
    if conflict is None:
        D, names = phys.reduced(augmented, after)
        r['reduced'] = phys.dimacs(a.out / 'reduced.cnf', D, len(names))
        r['reduced_variables'] = len(names)
        r['reduced_clauses'] = len(D)
        (a.out / 'variable-map.json').write_text(json.dumps(names) + '\n')
    (a.out / 'result.json').write_text(json.dumps(r, indent=2) + '\n')
    print(json.dumps({k: v for k, v in r.items() if k != 'new_assignments'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
