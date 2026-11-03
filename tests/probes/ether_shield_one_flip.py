#!/usr/bin/env python3
"""GC2428: two fixed tail completions at the existing worst entry, no search.

Predict flip112 breaks agreement through q=-24 at T222; flip113 is protected.
Any failed engine/entry/causal/protected control ends the stage. No follow-up flips.
"""
import hashlib
import importlib.util
import json
import os
import re
from pathlib import Path


def main():
    src = Path('tests/probes/ether_adaptive_shield.py')
    assert hashlib.sha256(src.read_bytes()).hexdigest() == 'f1fccc493af4fe3538a89b3dcc8d12d7f56f9279b5074afb5b197afa210ee85a'
    spec = importlib.util.spec_from_file_location('frozen', src)
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    entry = Path('tests/probes/lean/EtherEdgeZero.lean').read_bytes()
    assert hashlib.sha256(entry).hexdigest() == base.ENTRY_HASH
    assert re.search(r'theorem entry_4_3 : checkEntry 4 3 222 \(-37\) = true', entry.decode())
    eraw = Path(os.environ['ETHER_KIT_SOURCE']).read_bytes()
    assert hashlib.sha256(eraw).hexdigest() == base.ETHER_HASH
    walls = set()
    text = eraw.decode().split('def wallStates :', 1)[1].split('theorem', 1)[0]
    for phase, bits in re.findall(r'\((\d), \[([a-z, ]+)\]\)', text):
        walls.add((int(phase), tuple(int(s.strip() == 'true') for s in bits.split(','))))
    assert len(walls) == 109
    LO, HI, T, c0, c1, xB, q = base.LO, base.HI, 222, 4, 3, -37, -24
    initial = [base.TABLE[(x+c0)%7][c1] if x < 0 else int(x == 0) for x in range(LO, HI+1)]
    results = []
    reference_hash = None
    for flip in [112, 113]:
        a = initial[:]
        b = initial[:]
        b[flip-LO] ^= 1
        assert sum(x ^ y for x, y in zip(a, b)) == 1
        za = sum(v << i for i, v in enumerate(a))
        zb = sum(v << i for i, v in enumerate(b))
        trace = []
        grid = hashlib.sha256()
        for t in range(T+1):
            n = len(a)
            assert a == [(za >> i) & 1 for i in range(n)]
            assert b == [(zb >> i) & 1 for i in range(n)]
            delta = [u ^ v for u, v in zip(a, b)]
            assert all(not d for i, d in enumerate(delta) if abs(LO+t+i-flip) > t)
            i = q-(LO+t)
            assert 0 <= i < n
            trace.append({'t': t, 'target_difference': delta[i],
                          'leftmost_in_cone': next((LO+t+j for j, d in enumerate(delta) if d), None)})
            grid.update(bytes(a))
            if t == T:
                break
            expected_delta = [dl ^ ((1-c) & db) ^ ((1-b0) & dc) ^ (db & dc)
                for dl, db, dc, b0, c in zip(delta, delta[1:], delta[2:], a[1:], a[2:])]
            a = base.lit_step(a)
            b = base.lit_step(b)
            assert [u ^ v for u, v in zip(a, b)] == expected_delta
            za = base.packed_step(za, n)
            zb = base.packed_step(zb, n)
        if reference_hash is None:
            reference_hash = grid.hexdigest()
        assert grid.hexdigest() == reference_hash
        def at(row, x):
            i = x-(LO+T)
            assert 0 <= i < len(row)
            return row[i]
        phi = (T+c1) % 4
        refwall = tuple(base.TABLE[(xB+i+1+c0)%7][phi] for i in range(13))
        def entry_ok(row):
            wall = tuple(at(row, xB+i+1) for i in range(13))
            return (all(at(row, x) == base.TABLE[(x+c0)%7][phi] for x in range(-T, xB+1))
                    and (phi, wall) in walls and wall != refwall)
        assert entry_ok(a)
        changed = [x for x in range(-T, q+1) if at(a, x) != at(b, x)]
        if flip == 113:
            assert not changed, 'PROTECTED_112_CONTROL_FAILED'
        results.append({'flip': flip, 'changes_through_target': changed,
                        'target_difference': at(a, q) ^ at(b, q),
                        'reference_wall': [at(a, xB+i+1) for i in range(13)],
                        'modified_wall': [at(b, xB+i+1) for i in range(13)],
                        'modified_entry_ok': entry_ok(b), 'trace': trace})
    held = bool(results[0]['changes_through_target'])
    summary = {'status': 'PASS', 'prediction': 'HELD' if held else 'REFUTED',
               'flip112_breaks_full_agreement_at_entry': held,
               'flip113_protected_control': True,
               'entry': [4, 3, T, xB, q], 'reference_grid_sha256': reference_hash,
               'scope': 'two fixed completions at the existing entry, not eventual pinning or optimal wall entry'}
    (Path(os.environ['CAPPED_OUT'])/'one-flip-shield.json').write_text(json.dumps(
        {'summary': summary, 'results': results}, indent=2)+'\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
