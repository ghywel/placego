#!/usr/bin/env python3
"""The missing physical truth-table corner for pulse-to-input transport."""
import argparse
import json
from pathlib import Path
from pysat.solvers import Cadical195
import e_short_guard as short
import physical_47 as phys
import physical_ancestry as anc


def parity(rr, m, j, a, b):
    terms = []
    for s in range(a, b):
        p = j + 1 - m + s
        assert p >= 1
        terms.append((rr[s] >> (p-1) | rr[s] >> p) & 1)
    return sum(terms) % 2, terms


def record(root):
    rr = anc.rows(root, 85)
    assert anc.ancestry(rr[-1], 85)['rows'] == rr
    assert anc.complete_tail(rr[-1] >> 85, 85) == (root, rr[-1])
    p, terms_p = parity(rr, 85, 83, 3, 10)
    q, terms_q = parity(rr, 85, 80, 5, 13)
    assert p == ((rr[3] & 1) ^ (rr[10] >> 7 & 1))
    assert q == (rr[13] >> 7 & 1)  # time5 boundary is white
    wanted = short.head_word('253353')
    assert all(rr[t] & 1 == bit for t, bit in wanted.items() if t != 3)
    assert rr[10] >> 7 & 1 == 0
    return {'root': str(root), 'pulse': rr[3] & 1, 'white_input': rr[10] >> 7 & 1,
            'black_input': rr[13] >> 7 & 1, 'P': p, 'Q': q,
            'P_terms': terms_p, 'Q_terms': terms_q,
            'seam85_hex': hex(rr[-1]), 'full_ancestry_replay': True}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    c, ids, true = short.build('253353')
    # Keep every original head except change the older pulse from black to
    # white. Ask whether the later black input can nevertheless be black.
    c = [cl[:] for cl in c if cl != [ids[3][0]]]
    c += [[-ids[3][0]], [ids[13][7]]]
    fixture = short.rows(2135555, 74)[-1] & ((1 << 46) - 1)
    controls = [record(52777231658405), record(fixture)]
    assert [(x['P'], x['Q']) for x in controls] == [(0, 0), (1, 1)]
    stem = args.out / 'parity-01'
    cnf = phys.dimacs(stem.with_suffix('.cnf'), c, true)
    result = {'query': 'P=0,Q=1', 'controls': controls, 'cnf': cnf}
    with Cadical195(bootstrap_with=c, with_proof=True) as solver:
        solver.conf_budget(5000)
        answer = solver.solve_limited()
        result['answer'] = 'SAT' if answer is True else 'UNSAT_UNCHECKED' if answer is False else 'UNKNOWN'
        result['stats'] = solver.accum_stats()
        if answer is False:
            stem.with_suffix('.drat').write_text('\n'.join(solver.get_proof()) + '\n')
        elif answer is True:
            positives = set(v for v in solver.get_model() if v > 0)
            root = sum(int(v in positives) << i for i, v in enumerate(ids[0]))
            vals, rr = short.assignment(root, ids, true)
            assert short.satisfied(c, vals)
            assert rr == phys.scalar_rows(root, 45, 46)
            result['witness'] = record(root)
            assert (result['witness']['P'], result['witness']['Q']) == (0, 1)
            assert not short.satisfied(c + [[ids[3][0]]], vals)
            result['all_original_case_clauses_scalar_and_parity'] = True
    (args.out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
