#!/usr/bin/env python3
"""Read the old guard proof cores and test removal of the preceding A.

Two fixed small local queries, not a full4,7 solve. SAT countermodels replay
all cells and identify violated A head premises. UNSAT needs native checking.
"""
import argparse
import json
from pathlib import Path

from pysat.solvers import Cadical195

import e_short_guard as short
import physical_47 as phys


def read_cnf(p):
    return [list(map(int, s.split()[:-1])) for s in p.read_text().splitlines()
            if s and s[0] not in 'cp']


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    base, ids, true = short.build('253353')
    wanted = short.head_word('253353')
    A = {t: bit for t, bit in wanted.items() if t < 17}
    E = {t: bit for t, bit in wanted.items() if t >= 17}
    assert list(A) == list(range(3, 17, 2)) and E[17] == E[45] == 1
    early = {ids[t][0] if bit else -ids[t][0] for t, bit in A.items()}
    relaxed = [c for c in base if not (len(c) == 1 and c[0] in early)]
    assert len(base) - len(relaxed) == 7
    result = {'removed_A_heads': A, 'retained_E_heads': E, 'source_core_heads': {}, 'proofs': []}
    for t, opposite in ((10, 1), (13, 0)):
        old, _, _ = short.build('253353', (t, opposite))
        core = read_cnf(a.out / f'core{t}.cnf')
        assert {tuple(sorted(set(c))) for c in core} <= {tuple(sorted(set(c))) for c in old}
        units = {c[0] for c in core if len(c) == 1}
        result['source_core_heads'][t] = {'clauses': len(core),
            'head_support': {s: bit for s, bit in wanted.items()
                             if (ids[s][0] if bit else -ids[s][0]) in units}}
        C = relaxed + [[ids[t][7] if opposite else -ids[t][7]]]
        phys.dimacs(a.out / f'guard{t}.cnf', C, true)
        with Cadical195(bootstrap_with=C, with_proof=True) as solver:
            solver.conf_budget(5000)
            answer = solver.solve_limited()
            r = {'time': t, 'opposite': opposite, 'answer': answer, 'stats': solver.accum_stats()}
            if answer is False:
                (a.out / f'guard{t}.drat').write_text('\n'.join(solver.get_proof()) + '\n')
            elif answer is True:
                positives = {v for v in solver.get_model() if v > 0}
                root = sum(int(v in positives) << i for i, v in enumerate(ids[0]))
                vals, rows = short.assignment(root, ids, true)
                assert short.satisfied(C, vals)
                scalar = phys.scalar_rows(root, 45, 46)
                assert rows == scalar
                assert all(bool(rows[s] & 1) == bool(bit) for s, bit in E.items())
                assert (rows[t] >> 7 & 1) == opposite
                lost = {s: {'wanted': bit, 'observed': rows[s] & 1}
                        for s, bit in A.items() if (rows[s] & 1) != bit}
                assert lost, 'countermodel contradicts the original guard certificate'
                wrong = [row[:] for row in C]
                wrong[-1] = [-wrong[-1][0]]
                assert not short.satisfied(wrong, vals)
                r['witness'] = {'root': str(root), 'opposite_guard': opposite, 'all_E_heads': True,
                                'all_original_case_clauses': True, 'all_cone_cells': True,
                                'independent_scalar_replay': True, 'wrong_bit_rejected': True,
                                'violated_A_heads': lost}
            result['proofs'].append(r)
    (a.out / 'guard-result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
