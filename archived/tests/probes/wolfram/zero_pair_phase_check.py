#!/usr/bin/env python3
"""GC2210: eight fixed phase controls; no seed census or period search.

The universal statement and predictions are in rule30-zero-pair-phase.md.
Compare algebra on retained temporal words with literal physical Rule30 rows.
Only H=256/root prefix16 and H=2/edge code5 are used. No automatic extension.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time

START = time.monotonic()
ap = argparse.ArgumentParser()
ap.add_argument('--witness', required=True)
args = ap.parse_args()
raw = Path(args.witness).read_bytes()
assert len(raw) < 16384
assert hashlib.sha256(raw).hexdigest() == 'fcdf3b5b6de5375a30a7f9ece88ab85d05eefcd1fa6c2087615012772fd9a3f0'
retained = json.loads(raw)
assert retained['bounds'] == {'H': 256, 'diagonals': [14, 15, 16, 17, 18], 'seed': 1}
RULE = (0, 1, 1, 1, 1, 0, 0, 0)


def guard():
    assert time.monotonic() - START < 240, 'internal wall stop'


def physical(seed, ticks, depths):
    """Finite physical row, cell p=-d initially reads bit d of edge code."""
    lo = -(seed.bit_length() - 1)
    row = {-d: (seed >> d) & 1 for d in range(seed.bit_length())}
    words = {d: [] for d in depths}
    for t in range(ticks + 1):
        for d in depths:
            words[d].append(row.get(t - d, 0))
        if t != ticks:
            nxt = {}
            for p in range(lo - t - 1, t + 2):
                idx = 4 * row.get(p - 1, 0) + 2 * row.get(p, 0) + row.get(p + 1, 0)
                nxt[p] = RULE[idx]
            row = nxt
        if t % 16 == 0:
            guard()
    return words


def parity(bits):
    return sum(bits) % 2


def audit(name, seed, j, H, a, b, c, ticks):
    assert H in (2, 256) and len(a) == len(b) == len(c) == H
    assert all(c[(t + 1) % H] == (c[t] ^ (a[t] | b[t])) for t in range(H))
    h = [0]
    for t in range(ticks):
        h.append(h[-1] ^ (1 ^ a[t % H]))
    alpha, B = parity(a), parity(b)
    A = parity([c[t] ^ (b[t] & h[t]) for t in range(H)])
    F = parity([b[t] | c[t] for t in range(H)])
    E = parity([a[t] | b[t] for t in range(0, H, 2)])
    assert parity(c) == E
    assert A == (E ^ parity([b[t] & h[t] for t in range(H)]))
    assert h[H] == alpha
    if name == 'retained_root256':
        assert alpha == 0, 'fixed source must preserve H for all four phases'
    rows = []
    for beta in range(2):
        for gamma in range(2):
            changed = seed ^ (beta << (j + 1)) ^ (gamma << (j + 2))
            depths = list(range(14, 20)) if H == 256 else [1, 2, 3, 4]
            words = physical(changed, ticks, depths)
            for t in range(ticks + 1):
                assert words[j][t] == a[t % H]
                assert words[j + 1][t] == (b[t % H] ^ beta)
                assert words[j + 2][t] == (c[t % H] ^ gamma ^ (beta & h[t]))
            second = words[j + 2][H] ^ words[j + 2][0]
            assert second == (beta & alpha)
            first_H = parity([words[j + 1][t] | words[j + 2][t] for t in range(H)])
            assert first_H == (F ^ (beta & A) ^ (gamma & B))
            period = H if not second else 2 * H
            assert period <= ticks
            next_flag = words[j + 3][period] ^ words[j + 3][0]
            expected = first_H if not second else B
            assert next_flag == expected
            assert words[j + 3][H] ^ words[j + 3][0] == first_H
            if H == 256 and beta == gamma == 0:
                for d in range(14, 19):
                    assert ''.join(map(str, words[d][:H])) == retained['time_words'][str(d)]
            rows.append({'beta': beta, 'gamma': gamma, 'seed_edge_code': changed,
                         'second_doubling': second, 'prefix_period_after_c': period,
                         'first_H_parity': first_H, 'next_flag': next_flag})
    return {'case': name, 'seed': seed, 'j': j, 'H': H, 'ticks': ticks,
            'alpha': alpha, 'A': A, 'B': B, 'F': F,
            'weights': {'a': sum(a), 'b': sum(b), 'c': sum(c),
                        'b_and_h': sum(b[t] & h[t] for t in range(H))},
            'h_word': ''.join(map(str, h[:H])), 'phases': rows}


root = audit('retained_root256', 1, 16, 256,
             *[[int(x) for x in retained['time_words'][str(d)]] for d in (16, 17, 18)], 256)
small = audit('finite_seed5_H2', 5, 1, 2, [0, 1], [1, 0], [0, 1], 4)
assert (small['alpha'], small['A'], small['B'], small['F']) == (1, 1, 1, 0)
assert [r['second_doubling'] for r in small['phases']] == [0, 0, 1, 1]
assert [r['next_flag'] for r in small['phases']] == [0, 1, 1, 1]
print(json.dumps({'status': 'PASS', 'scope': 'eight fixed controls, not universal or density evidence',
                  'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'input_sha256': hashlib.sha256(raw).hexdigest(),
                  'P1_formula_and_closure': True,
                  'P2_root256_invariant': root['A'] == root['B'] == 0,
                  'physical_rows': 4 * 257 + 4 * 5,
                  'cases': [root, small], 'elapsed_seconds': time.monotonic() - START}, indent=2))
