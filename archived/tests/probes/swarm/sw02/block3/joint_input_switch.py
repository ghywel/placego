#!/usr/bin/env python3
"""Two fixed rooted 808-to-4520 switch questions; no temporal input splice."""
import argparse
import hashlib
import itertools
import json
import random
from pathlib import Path

import physical_47 as phys
import physical_ancestry as anc
from image_ancestry_audit import trajectory

ROOT = 3117140926837386784874684827056780
H, W = 129, 130


def case(name):
    wanted = anc.word_heads(anc.E + anc.A * 4, 1)
    assert max(wanted) == 125
    C, off, width = phys.generate(H, wanted)
    fixed = list(range(1, 36))
    if name == 'band_only':
        fixed += list(range(69, W + 1))
    assert name in ('band_only', 'joint') and width == W
    C += [[(off[0] + p) * (1 if ROOT >> (p - 1) & 1 else -1)] for p in fixed]
    C += [[(off[109] + p) * (1 if 64 >> (p - 1) & 1 else -1)] for p in range(1, 8)]
    C += [[(off[109 + k] + 8) * (1 if 4520 >> k & 1 else -1)] for k in range(14)]
    return C, off, width, fixed


def differential(base, delta, width):
    """Exact difference rule; the center difference is zero."""
    mask = (1 << width) - 1
    return ((delta << 1) ^ (delta & ~(base >> 1)) ^
            ((delta >> 1) & ~base) ^ (delta & (delta >> 1))) & mask


def prepare(out):
    out.mkdir(parents=True, exist_ok=True)
    base = trajectory(ROOT, 0, 193)
    wanted = anc.word_heads(anc.E + anc.A * 4, 1)
    assert all(base[t] & 1 == b for t, b in wanted.items())
    assert base[109] & 127 == 64
    assert sum((base[109 + k] >> 7 & 1) << k for k in range(14)) == 808
    # Exhaustive local truth table for the exact difference equation.
    for a, b, c, da, db, dc in itertools.product(range(2), repeat=6):
        exact = (a ^ (b | c)) ^ ((a ^ da) ^ ((b ^ db) | (c ^ dc)))
        formula = da ^ ((1 ^ c) & db) ^ ((1 ^ b) & dc) ^ (db & dc)
        assert exact == formula
    trunks = {}
    for word in (808, 4520):
        q = 64
        rows = [q]
        for k in range(14):
            q = anc.step(q | (((word >> k) & 1) << 7), anc.drive(109 + k)) & 127
            rows.append(q)
        width = 7
        tail = {123: q}
        for t in range(123, 129):
            width -= 1
            q = anc.step(q, anc.drive(t)) & ((1 << width) - 1)
            tail[t + 1] = q
        trunks[str(word)] = {'low7_109_to_123': rows, 'shrinking_prefix_123_to_129': tail}
    assert trunks['808']['shrinking_prefix_123_to_129'][129] == 1
    assert trunks['4520']['shrinking_prefix_123_to_129'][129] == 0
    assert 808 ^ 4520 == (1 << 7) | (1 << 9) | (1 << 12)
    # Entire 15-cell row115 fibre, given low7=7: no temporal inputs are free.
    fibre = []
    for suffix in range(256):
        row = 7 | (suffix << 7)
        tr = trajectory(row, 115, 7)
        tail = sum((tr[k] >> 7 & 1) << k for k in range(8))
        a, b, c = ((row >> k) & 1 for k in (9, 10, 11))
        guard = (row & 511) == 263 and not (a and (b or c))
        assert (tail == 70) == guard
        if guard:
            fibre.append(row)
    assert len(fibre) == 40
    # One unexpected interaction test, fixed before execution. No redraw/retry.
    rng = random.Random('GC2783-band-tail-interaction')
    band = rng.getrandbits(33) << 35
    high = rng.getrandbits(W - 68) << 68
    roots = {'base': ROOT, 'band': ROOT ^ band, 'high': ROOT ^ high,
             'both': ROOT ^ band ^ high}
    traces = {n: trajectory(r, 0, 193) for n, r in roots.items()}
    for name, tr in traces.items():
        assert all(tr[t] & 1 == b for t, b in anc.word_heads(anc.E, 1).items())
        for t in range(H):
            width = W - t - 1
            assert differential(base[t], tr[t] ^ base[t], width) == ((tr[t + 1] ^ base[t + 1]) & ((1 << width) - 1))
    interaction = [traces['base'][t] ^ traces['band'][t] ^ traces['high'][t] ^ traces['both'][t] for t in range(194)]
    controls = {'truth_table_64': True, 'differential_all_cone_cells': True,
                'all_four_first_Es': True, 'band_mask': str(band), 'higher_mask': str(high),
                'first_interaction_head': next((t for t in range(1, 194, 2) if interaction[t] & 1), None),
                'interaction_input_ticks': [t for t in range(109, 123) if interaction[t] >> 7 & 1],
                'roots': {n: str(r) for n, r in roots.items()},
                'actual_words109': {n: sum((tr[109 + k] >> 7 & 1) << k for k in range(14)) for n, tr in traces.items()},
                'bad_EA4_heads': {n: [t for t, b in wanted.items() if tr[t] & 1 != b] for n, tr in traces.items()}}
    cases = {}
    for name in ('band_only', 'joint'):
        C, off, width, fixed = case(name)
        cases[name] = phys.dimacs(out / (name + '.cnf'), C, off[-1]) | {'fixed_root_cells': fixed, 'W': width, 'H': H}
    (out / 'prepare.json').write_text(json.dumps({'trunks': trunks, 'local_fibre_row115': fibre,
      'local_fibre_cases': 256, 'local_fibre_guard_matches': 40,
      'controls': controls, 'cases': cases}, indent=2) + '\n')
    print('JOINT_SWITCH_PREPARE_PASS')
    print(json.dumps(controls))


def audit(out):
    result = {}
    target = anc.word_heads(anc.E + anc.A * 4 + anc.E, 1)
    for name in ('band_only', 'joint'):
        text = (out.parent / (name + '.stdout')).read_text()
        if 's SATISFIABLE' not in text:
            result[name] = {'status': 'UNSAT_UNCHECKED' if 's UNSATISFIABLE' in text else 'UNKNOWN'}
            continue
        vals = {abs(int(x)): int(x) > 0 for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x != '0'}
        C, off, width, fixed = case(name)
        assert all(any(vals[abs(x)] == (x > 0) for x in cl) for cl in C)
        root = sum(int(vals[off[0] + p]) << (p - 1) for p in range(1, width + 1))
        tr = trajectory(root, 0, 193)
        assert all(vals[off[t] + p] == bool(tr[t] >> (p - 1) & 1) for t in range(H + 1) for p in range(1, W - t + 1))
        assert tr[109] & 127 == 64 and tr[129] & 1 == 0
        assert sum((tr[109 + k] >> 7 & 1) << k for k in range(14)) == 4520
        assert tr[115] & 511 == 263
        result[name] = {'status': 'SAT_CHECKED', 'root_tick0': str(root),
                        'root_changes_36_68': [p for p in range(36, 69) if (root ^ ROOT) >> (p - 1) & 1],
                        'root_changes_69_130': [p for p in range(69, 131) if (root ^ ROOT) >> (p - 1) & 1],
                        'bad_EA4E_heads_zero_completion': [t for t, b in target.items() if tr[t] & 1 != b],
                        'actual_source109_low7': tr[109] & 127, 'actual_label109': 4520,
                        'row115_low9': tr[115] & 511, 'rows_hex': [hex(r) for r in tr],
                        'all_CNF_and_independent_scalar_cells_pass': True}
        assert result[name]['root_changes_36_68']
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print('JOINT_SWITCH_AUDIT_PASS')
    print(json.dumps({n: {k: v for k, v in r.items() if k != 'rows_hex'} for n, r in result.items()}))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('phase', choices=['prepare', 'audit'])
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    globals()[args.phase](args.out)
