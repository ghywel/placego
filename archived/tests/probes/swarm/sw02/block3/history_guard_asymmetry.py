#!/usr/bin/env python3
"""Export a strictly weaker white-bit premise and replay one black-bit countermodel.

No search: the old proof is reused by the native checker, and the retained
E-only witness violates precisely the first A pulse while preserving the rest.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

import e_short_guard as short
import physical_47 as phys


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--prior', type=Path, required=True)
    p.add_argument('--old-guards', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    C, ids, true = short.build('253353', (10, 1))
    dropped = {ids[3][0], -ids[5][0]}
    weaker = [c for c in C if not (len(c) == 1 and c[0] in dropped)]
    assert len(C) - len(weaker) == 2
    proof_input = phys.dimacs(a.out / 'white.cnf', weaker, true)
    shutil.copyfile(a.old_guards / 'guard10.drat', a.out / 'white.drat')
    prior = json.loads(a.prior.read_text())
    case = next(x for x in prior['proofs'] if x['time'] == 13)
    assert case['answer'] is True
    root = int(case['witness']['root'])
    C13, ids13, true13 = short.build('253353', (13, 0))
    only_first_removed = [c for c in C13 if c != [ids13[3][0]]]
    assert len(C13) - len(only_first_removed) == 1
    vals, rows = short.assignment(root, ids13, true13)
    assert short.satisfied(only_first_removed, vals)
    assert not short.satisfied(C13, vals)
    assert not (rows[3] & 1)
    assert rows == phys.scalar_rows(root, 45, 46)
    assert (rows[10] >> 7 & 1) == 0 and (rows[13] >> 7 & 1) == 0
    wanted = short.head_word('253353')
    assert all(bool(rows[t] & 1) == bool(bit) for t, bit in wanted.items() if t != 3)
    phys.dimacs(a.out / 'black-first-pulse-removed.cnf', only_first_removed, true13)
    r = {'white_opposite_case': proof_input,
         'white_removed_head_ticks': [3, 5], 'white_retained_word': '5.3353',
         'white_word_first_black_tick': 7, 'E_first_black_tick': 17,
         'white_guard': {'tick': 10, 'column': 8, 'value': 0},
         'old_white_proof_sha256': hashlib.sha256((a.out / 'white.drat').read_bytes()).hexdigest(),
         'black_countermodel': {'root': str(root), 'only_removed_head_tick': 3,
             'head3': 0, 'column8_at10': 0, 'column8_at13': 0,
             'all_other_original_heads': True, 'all_case_clauses': True,
             'all_cone_cells_and_scalar_replay': True},
         'new_search_performed': False}
    (a.out / 'asymmetry.json').write_text(json.dumps(r, indent=2) + '\n')
    print(json.dumps(r, indent=2), flush=True)


if __name__ == '__main__':
    main()
