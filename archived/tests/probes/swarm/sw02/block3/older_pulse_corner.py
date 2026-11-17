#!/usr/bin/env python3
"""One fixed boundary-history correction at W12; no further strip lift."""
import argparse
import itertools
import json
from pathlib import Path

from pysat.solvers import Cadical195
import older_pulse_strip as strip
import e_short_guard as short
import physical_47 as phys


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--prior', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    prior = json.loads(args.prior.read_text())
    # Eliminate the unseen right bit of exactly one Rule30 update.
    for a, b, d in itertools.product((0, 1), repeat=3):
        assert (not b or d != a) == any(d == (a ^ (b | c)) for c in (0, 1))
    out = {'width': 12, 'horizon': 45, 'conflicts_per_query': 2000,
           'corner_truth_table_cases': 8, 'old_countermodels_rejected': [],
           'queries': [], 'proof_stems': []}
    for t, b in ((10, 1), (13, 0)):
        clauses, ids, true, wanted = strip.build(12, (t, b))
        added = []
        for s in range(2, 45, 2):
            left, center, nxt = ids[s][11], ids[s][12], ids[s+1][12]
            added.extend([[-center, left, nxt], [-center, -left, -nxt]])
        old = next(q for q in prior['queries'] if q['name'] == f'w12-t{t}-dropnone')
        vals = {true: True}
        vals.update({v: bit == '1' for row, bits in zip(ids, old['witness']['rows'])
                     for v, bit in zip(row, bits)})
        assert short.satisfied(clauses, vals) and not short.satisfied(added, vals)
        out['old_countermodels_rejected'].append(old['name'])
        full = clauses + added
        fixture = short.rows(2135555, 74)[-1] & ((1 << 46) - 1)
        rows = short.rows(fixture, 45)
        control = {true: True}
        control.update({v: bool(rows[s] >> i & 1) for s, row in enumerate(ids) for i, v in enumerate(row)})
        assert short.satisfied(clauses[:-1] + added, control)
        name = f'corner-t{t}'
        stem = args.out / name
        cnf = phys.dimacs(stem.with_suffix('.cnf'), full, true)
        with Cadical195(bootstrap_with=full, with_proof=True) as solver:
            solver.conf_budget(2000)
            answer = solver.solve_limited()
            item = {'name': name, 'answer': 'SAT' if answer is True else
                    'UNSAT_UNCHECKED' if answer is False else 'UNKNOWN',
                    'cnf': cnf, 'added_clauses': len(added), 'stats': solver.accum_stats()}
            if answer is False:
                stem.with_suffix('.drat').write_text('\n'.join(solver.get_proof()) + '\n')
                out['proof_stems'].append(name)
            elif answer is True:
                positives = set(v for v in solver.get_model() if v > 0)
                values = {v: v in positives for v in range(1, true + 1)}
                assert short.satisfied(full, values)
                cells = strip.verify_strip(values, ids, wanted, (t, b))
                for s in range(2, 45, 2):
                    assert not cells[s][12] or cells[s+1][12] != cells[s][11]
                item['witness'] = {'rows': [''.join(map(str, row)) for row in cells],
                    'all_clauses_scalar_and_corner_checks': True, 'physical_lift_claimed': False}
            out['queries'].append(item)
    (args.out / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'queries': [{k: q[k] for k in ('name', 'answer', 'stats')}
                                 for q in out['queries']],
                      'old_countermodels_rejected': out['old_countermodels_rejected']}, indent=2))


if __name__ == '__main__':
    main()
