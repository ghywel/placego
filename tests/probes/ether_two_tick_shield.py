#!/usr/bin/env python3
"""GC2426 fixed28-entry correlated two-tick threshold pilot.

Prediction: the common cutoff is strictly below112; no-worse112 is a control.
No new time/alignment/target/cutoff search. Exact input hashes are mandatory.
"""
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path

BASE_HASH = 'f1fccc493af4fe3538a89b3dcc8d12d7f56f9279b5074afb5b197afa210ee85a'
DATA_HASH = '867b5a59388806aaf49b970429cb786b1a9abf3eb2665c9c3bc147ec977081e3'


def load_base():
    p = Path('tests/probes/ether_adaptive_shield.py')
    assert hashlib.sha256(p.read_bytes()).hexdigest() == BASE_HASH
    spec = importlib.util.spec_from_file_location('frozen_base', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def local_controls(base):
    # All causally relevant right completions of every five-bit prefix.
    groups = {}
    for bits in itertools.product([0, 1], repeat=7):
        future = base.lit_step(base.lit_step(bits))
        groups.setdefault(bits[:5], []).append(future)
    recovered = 0
    for prefix, futures in groups.items():
        if prefix[-3:] == (0, 1, 0):
            assert all(w == futures[0] for w in futures)
            assert futures[0][-2:] == [prefix[-4], 0]
            recovered += len(futures)
        if prefix[-3:] == (1, 1, 0):
            assert {w[-1] for w in futures} == {1}
            assert {w[-2] for w in futures} == {0, 1}
    assert recovered == 16
    # The actual-orbit guard matters: an arbitrary second field violates g monotonicity.
    fake = [{-2: 0, -1: 1, 0: 0, 1: 0}, {}]
    bit = lambda t, p: fake[t].get(p, 0)
    f = lambda t, p: p - 1 + bit(t, p)
    g = lambda p: p if [bit(0, p-i) for i in [2, 1, 0]] == [0, 1, 0] else f(1, f(0, p))
    assert (g(0), g(1)) == (0, -1)
    return {'seven_bit_cases': 128, '010_completions': recovered,
            '110_gap_varies': True, 'non_orbit_monotonicity_counter': [0, -1]}


def word_one(base, w):
    assert len(w) >= 2
    return base.lit_step(w) + ([1-w[-2]] if w[-1] else [])


def main():
    base = load_base()
    raw = Path(os.environ['SHIELD_FORWARD_DATA']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == DATA_HASH
    old = json.loads(raw)
    assert old['summary']['maximum_cutoff'] == 112
    assert len(old['results']) == 28
    assert hashlib.sha256(Path('tests/probes/lean/EtherEdgeZero.lean').read_bytes()).hexdigest() == base.ENTRY_HASH
    controls = local_controls(base)
    grid_hash = hashlib.sha256()
    results = []
    query_count = 0
    for record in old['results']:
        c0, c1, T, xB = (record[k] for k in ['c0', 'c1', 'T', 'xB'])
        assert 0 <= c0 < 7 and 0 <= c1 < 4 and 0 < T <= 222
        initial = [base.TABLE[(x+c0)%7][c1] if x < 0 else int(x == 0)
                   for x in range(base.LO, base.HI+1)]
        rows = [initial]
        z = sum(b << i for i, b in enumerate(initial))
        n = len(initial)
        for t in range(T+1):
            assert rows[t] == [(z >> i) & 1 for i in range(n)]
            grid_hash.update(bytes(rows[t]))
            if t < T:
                rows.append(base.lit_step(rows[t]))
                z = base.packed_step(z, n)
                n -= 2

        def bit(t, p):
            nonlocal query_count
            assert 0 <= t <= T
            i = p - (base.LO+t)
            assert 0 <= i < len(rows[t]), (t, p)
            query_count += 1
            return rows[t][i]

        def f(t, p):
            return p - 1 + bit(t, p)

        def F(t, p):
            return f(t+1, f(t, p))

        def pattern(t, p):
            return [bit(t, p-i) for i in [2, 1, 0]] == [0, 1, 0]

        def g(t, p):
            return p if pattern(t, p) else F(t, p)

        def h(t, q):
            return q + 1 - bit(t, q)

        def j(t, q):
            return q if pattern(t, q) else h(t, h(t+1, q))

        q = xB+13
        t = T
        trace = []
        if t % 2:
            q_old = q
            q = h(t-1, q)
            assert all((f(t-1, p) >= q_old) == (p >= q) for p in range(q_old-2, q_old+3))
            trace.append({'time': t-1, 'duration': 1, 'target': q_old, 'threshold': q})
            t -= 1
        while t:
            t -= 2
            q_old = q
            used = pattern(t, q)
            q = j(t, q)
            assert q_old <= q <= q_old+2
            points = list(range(q_old-3, q_old+4))
            values = [g(t, p) for p in points]
            assert all(a <= b for a, b in zip(values, values[1:]))
            assert all((g(t, p) >= q_old) == (p >= q) for p in points)
            assert all(g(t, p) >= F(t, p) for p in points)
            if used:
                assert h(t, h(t+1, q_old)) == q_old+1 and q == q_old
            trace.append({'time': t, 'duration': 2, 'target': q_old,
                          'threshold': q, '010_used': used})
        cutoff = q
        assert cutoff <= record['minimum_cutoff']

        def forward(b, finite_word=False):
            p = ordinary = b
            w = initial[:b-base.LO+1]
            path = []
            for t in range(0, T-1, 2):
                used = pattern(t, p)
                newp = g(t, p)
                ordinary = F(t, ordinary)
                assert newp >= ordinary
                if finite_word:
                    assert len(w) >= 4
                    if w[-3:] == [0, 1, 0]:
                        w = base.lit_step(base.lit_step(w)) + [w[-4], 0]
                    else:
                        w = word_one(base, word_one(base, w))
                    assert base.LO+t+2+len(w)-1 == newp
                    assert w == rows[t+2][:len(w)]
                path.append([t, p, newp, used])
                p = newp
            if T % 2:
                p = f(T-1, p)
                ordinary = f(T-1, ordinary)
                assert p >= ordinary
                if finite_word:
                    w = word_one(base, w)
                    assert base.LO+T+len(w)-1 == p
                    assert w == rows[T][:len(w)]
            return p, path

        winning, path = forward(cutoff, finite_word=True)
        losing, _ = forward(cutoff-1)
        old_b_endpoint, _ = forward(record['minimum_cutoff'], finite_word=True)
        assert losing < xB+13 <= winning
        assert old_b_endpoint >= xB+13
        assert cutoff >= record['first_initial_difference']
        results.append({'c0': c0, 'c1': c1, 'T': T, 'xB': xB,
                        'ordinary_cutoff': record['minimum_cutoff'], 'macro_cutoff': cutoff,
                        'endpoint': winning, 'preceding_endpoint': losing,
                        'backward_trace': trace, 'forward_trace': path})
    assert grid_hash.hexdigest() == old['summary']['grid_sha256']
    maximum = max(r['macro_cutoff'] for r in results)
    summary = {'status': 'PASS', 'maximum_cutoff': maximum,
               'strict_improvement_prediction': 'HELD' if maximum < 112 else 'REFUTED',
               'alignments': len(results), 'horizon_max': max(r['T'] for r in results),
               'grid_sha256': grid_hash.hexdigest(), 'old_data_sha256': DATA_HASH,
               'cone_checked_queries': query_count,
               'scope': 'fixed disjoint two-tick blocks and retained entry times, not optimal shielding'}
    out = Path(os.environ['CAPPED_OUT'])
    (out/'two-tick-shield.json').write_text(json.dumps({'summary': summary,
        'controls': controls, 'results': results}, indent=2)+'\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
