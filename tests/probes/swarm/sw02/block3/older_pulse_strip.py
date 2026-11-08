#!/usr/bin/env python3
"""Fixed exact-two-tick strip tests and ancestry-bearing diagonal readout.

Widths 8,10,12 only; horizon45, 2000 conflicts/query, no adaptive lift.
Free outer pairs are a sound relaxation, not a physical-history certificate.
UNSAT files require the separate native checker; SAT strips replay every cell.
"""
import argparse
import json
from pathlib import Path

from pysat.solvers import Cadical195

import e_short_guard as short
import physical_47 as phys
import physical_ancestry as anc


def build(width, opposite, removed=()):
    ids, n = [], 0
    for t in range(46):
        size = width + 3 if t == 0 else width + (2 if t % 2 else 1)
        ids.append(list(range(n + 1, n + size + 1)))
        n += size
    true = n + 1
    clauses = [[true]]
    for t in range(45):
        # First tick computes the whole stored odd prefix. Thereafter each
        # odd row has two fresh outer cells; all W inner cells are computed.
        size = len(ids[t + 1]) if t == 0 or t % 2 else width
        for i in range(size):
            left = ids[t][i - 1] if i else (true if t % 2 == 0 else -true)
            clauses.extend(phys.gate(left, ids[t][i], ids[t][i + 1], ids[t + 1][i]))
    wanted = {t: b for t, b in short.head_word('253353').items() if t not in removed}
    clauses.extend([ids[t][0] if b else -ids[t][0]] for t, b in wanted.items())
    t, b = opposite
    clauses.append([ids[t][7] if b else -ids[t][7]])
    return clauses, ids, true, wanted


def scalar_step(row, center, count):
    return [(center if i == 0 else row[i - 1]) ^ (row[i] | row[i + 1])
            for i in range(count)]


def verify_strip(values, ids, wanted, opposite):
    cells = [[int(values[v]) for v in row] for row in ids]
    for t in range(45):
        size = len(ids[t + 1]) if t == 0 or t % 2 else len(ids[t + 1]) - 2
        assert scalar_step(cells[t], int(t % 2 == 0), size) == cells[t + 1][:size]
    assert all(cells[t][0] == b for t, b in wanted.items())
    assert cells[opposite[0]][7] == opposite[1]
    return cells


def diagonal_readout(root, m, events):
    full = anc.rows(root, m)
    seam = full[-1]
    assert anc.ancestry(seam, m)['rows'] == full
    assert anc.complete_tail(seam >> m, m) == (root, seam)
    near, far = [0] * m, [0] * m
    snapshots, reads = {}, {}
    for j in range(max(seam.bit_length(), m + 1), 0, -1):
        value, current = (seam >> (j - 1)) & 1, [0] * m
        for t in range(m - 1, -1, -1):
            pos = j - m + t
            if pos < 0:
                break
            value ^= near[t] | far[t]
            current[t] = value
            if pos == 0:
                assert value == anc.drive(t)
            else:
                assert value == (full[t] >> (pos - 1) & 1)
            if (t, pos) in events:
                reads[f'{t}:{pos}'] = {'seam_cell': j, 'value': value}
        far, near = near, current
        if j in (103, 83, 81, 80, 79, 41):
            first = max(0, m - j + 1)
            snapshots[j] = {'next_input_cell': j - 1, 'first_live_time': first,
                'pair_bits': 2 * (m - first),
                'near': ''.join(map(str, near[first:])),
                'far': ''.join(map(str, far[first:]))}
    assert len(reads) == len(events)
    return {'root': str(root), 'seam_tick': m, 'seam_hex': hex(seam),
            'full_ancestry_and_tail_completion': True, 'event_reads': reads,
            'snapshots': snapshots}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    fixture = short.rows(2135555, 74)[-1] & ((1 << 46) - 1)
    bad = 52777231658405
    result = {'widths': [8, 10, 12], 'horizon': 45, 'conflicts_per_query': 2000,
              'queries': [], 'proof_stems': []}
    jobs = [(w, t, b, ()) for w in (8, 10, 12) for t, b in ((10, 1), (13, 0))]
    jobs += [(12, 10, 1, (3, 5)), (12, 13, 0, (3,))]
    for w, t, b, removed in jobs:
        c, ids, true, wanted = build(w, (t, b), removed)
        # Every genuine finite trajectory must satisfy the relaxed strip.
        control = bad if removed == (3,) else fixture
        rr = short.rows(control, 45)
        vals = {true: True}
        vals.update({v: bool(rr[s] >> i & 1) for s, row in enumerate(ids) for i, v in enumerate(row)})
        assert short.satisfied(c[:-1], vals)
        if removed == (3,):
            assert short.satisfied(c, vals)
        # A wrong sampling phase must reject this genuine control.
        wrong = dict(vals)
        wrong[ids[3][0]] = not wrong[ids[3][0]]
        assert not short.satisfied(c[:-1], wrong)
        name = f'w{w}-t{t}-drop' + ('-'.join(map(str, removed)) or 'none')
        stem = args.out / name
        cnf = phys.dimacs(stem.with_suffix('.cnf'), c, true)
        with Cadical195(bootstrap_with=c, with_proof=True) as solver:
            solver.conf_budget(2000)
            answer = solver.solve_limited()
            item = {'name': name, 'width': w, 'opposite': [t, b], 'removed_heads': removed,
                    'answer': 'SAT' if answer is True else 'UNSAT_UNCHECKED' if answer is False else 'UNKNOWN',
                    'cnf': cnf, 'stats': solver.accum_stats()}
            if answer is False:
                stem.with_suffix('.drat').write_text('\n'.join(solver.get_proof()) + '\n')
                result['proof_stems'].append(name)
            elif answer is True:
                positives = set(v for v in solver.get_model() if v > 0)
                values = {v: v in positives for v in range(1, true + 1)}
                assert short.satisfied(c, values)
                cells = verify_strip(values, ids, wanted, (t, b))
                item['witness'] = {'rows': [''.join(map(str, row)) for row in cells],
                    'all_clauses_and_scalar_cells': True,
                    'physical_lift_claimed': False}
        result['queries'].append(item)
    events = {(3, 1), (5, 1), (7, 1), (10, 8), (13, 8), (45, 1)}
    result['local_frame_controls'] = [diagonal_readout(x, 85, events) for x in (fixture, bad)]
    # Genuine global history: the source frame begins at physical tick74.
    # This control has its full159-tick ancestry, not a rebased arbitrary row.
    events = {(77, 1), (79, 1), (81, 1), (84, 8), (87, 8), (119, 1)}
    result['global_fixture'] = diagonal_readout(2135555, 159, events)
    assert [result['global_fixture']['event_reads'][f'{t+74}:{p}']['value']
            for t, p in sorted({(3, 1), (5, 1), (7, 1), (10, 8), (13, 8), (45, 1)})] == [
            result['local_frame_controls'][0]['event_reads'][f'{t}:{p}']['value']
            for t, p in sorted({(3, 1), (5, 1), (7, 1), (10, 8), (13, 8), (45, 1)})]
    result['controls'] = {'genuine_strip_embedding': True, 'wrong_head_rejected': True,
                          'exact_ancestry_scans': True, 'no_target_solve': True}
    (args.out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'queries': [{k: x[k] for k in ('name', 'answer', 'stats')}
                                  for x in result['queries']], 'proof_stems': result['proof_stems'],
                      'controls': result['controls']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
