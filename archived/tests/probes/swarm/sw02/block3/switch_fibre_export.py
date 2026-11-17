#!/usr/bin/env python3
"""RUP export of actual row115/281 switch guards into unchanged target CNFs."""
import argparse
import json
from pathlib import Path
from pysat.solvers import Minisat22
import physical_47 as phys
import physical_ancestry as anc
import sparse_label_certificate as sparse
from image_ancestry_audit import trajectory


def lift(C, goals, proof):
    """Discharge each negated-conjunction refutation to its positive unit."""
    result = []
    with Minisat22(bootstrap_with=C) as solver:
        for goal in goals:
            for clause in proof:
                clause = list(dict.fromkeys(clause + [goal]))
                if any(-v in clause for v in clause):
                    continue
                assert not solver.propagate(assumptions=[-v for v in clause])[0]
                solver.add_clause(clause)
                result.append(clause)
            assert result[-1] == [goal]
    return result


def main(out, compact, labels):
    out.mkdir(parents=True, exist_ok=True)
    fibre113 = []
    for suffix in range(1024):
        root = 72 | (suffix << 7)
        tr = trajectory(root, 113, 9)
        word = sum((tr[k] >> 7 & 1) << k for k in range(10))
        assert (word == 282) == (root & 4095 == 72)
        if word == 282:
            fibre113.append(root)
    assert len(fibre113) == 32
    C, co, cw = phys.generate(35, anc.word_heads('25253', 1))
    cg = [(co[13] + p) * (1 if p == 7 else -1) for p in range(1, 8)]
    cp = sparse.proof_clauses(compact / 'compact.drat')
    assert cp[-1] == []
    proof64 = lift(C, cg, cp)
    L, lo, lw, lg, _, lh, _ = sparse.case('five')
    lp = sparse.proof_clauses(labels / 'five.drat')
    assert lp[-1] == []
    proof4520 = lift(L, lg, lp)
    result = {}
    for H, word, sites in ((193, anc.E + anc.A * 4 + anc.E, (109,)),
                           (359, anc.E + anc.A * 4 + anc.E + anc.A * 7 + anc.E, (109, 275))):
        F, off, W = phys.generate(H, anc.word_heads(word, 1))
        info = phys.dimacs(out / f'original{H}.cnf', F, off[-1])
        if H == 359:
            assert info['sha256'] == '21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
        base = {tuple(cl) for cl in F}
        additions, units, guards, white_units = [], [], [], []
        with Minisat22(bootstrap_with=F) as solver:
            for site in sites:
                for local, localoff, width, delta, proof, goals in (
                    (C, co, cw, site - 13, proof64, cg),
                    (L, lo, lw, site - 28, proof4520, lg)):
                    names = {1: 1}
                    for t in range(width):
                        for p in range(1, width - t + 1):
                            names[localoff[t] + p] = off[t + delta] + p
                    def mapped(cl):
                        return [names[abs(v)] * (1 if v > 0 else -1) for v in cl]
                    assert all(tuple(mapped(cl)) in base for cl in local)
                    for cl in proof:
                        cl = mapped(cl)
                        assert not solver.propagate(assumptions=[-v for v in cl])[0]
                        solver.add_clause(cl)
                        additions.append(cl)
                    units.extend(mapped(goals))
            before = solver.propagate()[1]
            for site in sites:
                t = site + 6
                for p in (11, 12):
                    clause = [-off[t] - 10, -off[t] - p]
                    assert not solver.propagate(assumptions=[-v for v in clause])[0]
                    solver.add_clause(clause)
                    additions.append(clause)
                    guards.append({'time': t, 'cells': [10, p], 'clause': clause})
            for site in sites:
                for p in (10, 11, 12):
                    unit = -off[site + 4] - p
                    assert not solver.propagate(assumptions=[-unit])[0]
                    solver.add_clause([unit])
                    additions.append([unit])
                    white_units.append({'time': site + 4, 'cell': p, 'literal': unit})
            after = solver.propagate()[1]
            # A false unit need not be RUP; reject one whose opposite is fixed.
            assert units
            assert solver.propagate(assumptions=[units[0]])[0]
        path = out / f'guards{H}.drup'
        path.write_text(''.join(' '.join(map(str, cl)) + ' 0\n' for cl in additions))
        assert path.stat().st_size < 16 * 1024 * 1024
        result[str(H)] = {'original': info, 'RUP_additions': len(additions),
                          'guard_clauses': guards, 'white_units': white_units,
                          'incremental_solver_trail_before': len(set(before)),
                          'incremental_solver_trail_after': len(set(after)),
                          'unit_count_note': 'Not total UP counts; use --saved for independent diagnostics.',
                          'all_embeddings_exact': True, 'every_addition_RUP_checked': True}
    result['local113'] = {'cases': 1024, 'accepted': 32, 'accepted_roots': fibre113,
                          'predicate': 'low12=72 iff ten actual column8 bits=282, given low7=72'}
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print('SWITCH_FIBRE_EXPORT_PASS')
    print(json.dumps(result))


def audit_saved(out, saved):
    """Count all UP units independently; solver.propagate returns only new trail."""
    out.mkdir(parents=True, exist_ok=True)
    prior = json.loads((saved / 'result.json').read_text())
    result = {}
    for H, word, sites in ((193, anc.E + anc.A * 4 + anc.E, (109,)),
                           (359, anc.E + anc.A * 4 + anc.E + anc.A * 7 + anc.E, (109, 275))):
        F, off, W = phys.generate(H, anc.word_heads(word, 1))
        source = [(off[t] + p) * (1 if p == 7 else -1) for t in sites for p in range(1, 8)]
        label = [(off[t + k] + 8) * (1 if 4520 >> k & 1 else -1) for t in sites for k in range(14)]
        old4 = [v for t in sites for v in (-off[t + 9] - 8, off[t + 12] + 8)]
        quartet = [(off[t + 10] + p) * (1 if b else -1) for t in sites for p, b in ((6, 1), (7, 1), (8, 0), (9, 1))]
        guards = [g['clause'] for g in prior[str(H)]['guard_clauses']]
        whites = [g['literal'] for g in prior[str(H)]['white_units']]
        proof = {tuple(cl) for cl in sparse.proof_clauses(saved / f'guards{H}.drup')}
        assert all(tuple(c) in proof for c in guards + [[v] for v in source + label + whites])
        views = {'original': [], 'old_union': [[v] for v in label + old4 + quartet],
                 'source_labels': [[v] for v in source + label],
                 'new': [[v] for v in source + label + whites] + guards,
                 'new_union': [[v] for v in source + label + whites + old4 + quartet] + guards}
        maps = {}
        for name, additions in views.items():
            vals, log, bad = phys.propagate(F + additions)
            assert bad is None and phys.replay_units(F + additions, log, bad) == vals
            maps[name] = vals
        where = {off[t] + p: (t, p) for t in range(H + 1) for p in range(1, W - t + 1)}
        def gained(a, b):
            return [{'time': where[v][0], 'cell': where[v][1], 'value': int(bit)}
                    for v, bit in sorted(maps[b].items()) if v not in maps[a] and v in where]
        result[str(H)] = {'unit_counts': {n: len(v) for n, v in maps.items()},
                          'new_over_source_labels': gained('source_labels', 'new'),
                          'new_union_over_old_union': gained('old_union', 'new_union'),
                          'new_seam193': [d for d in gained('old_union', 'new_union') if d['time'] == 193],
                          'independent_UP_reasons_checked': True}
    (out / 'diagnostics.json').write_text(json.dumps(result, indent=2) + '\n')
    print('SWITCH_SAVED_DIAGNOSTICS_PASS')
    print(json.dumps(result))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--compact', type=Path)
    p.add_argument('--labels', type=Path)
    p.add_argument('--saved', type=Path)
    args = p.parse_args()
    if args.saved:
        audit_saved(args.out, args.saved)
    else:
        assert args.compact and args.labels
        main(args.out, args.compact, args.labels)
