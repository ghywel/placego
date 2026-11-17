#!/usr/bin/env python3
"""GC2831: fixed BR-2 controls and literal XP-3 certificate replays.

Original sources remain outside git. The cert/cert2 adapter only supplies their
relative import layout, redirects generated files below CAPPED_OUT, and sets
HiGHS to one thread. The verify mode uses literal cell updates and tuple-window
counts, never the scripts' packed update/count/elimination routines.
"""
import ast
from collections import Counter
from fractions import Fraction as Q
import hashlib
import itertools
import json
import os
from pathlib import Path
import runpy
import shutil
import sys

SOURCE = Path(os.environ['CARRY_SOURCE'])
BR = Path(os.environ['CARRY_BR'])
OUT = Path(os.environ['CAPPED_OUT'])
REF = Path('tests/probes/swarm/sw02/ref.py').resolve()


def emit(name, data):
    (OUT / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(data), flush=True)


def literal_f(y):
    bits = [0] + [(y >> i) & 1 for i in range(y.bit_length())] + [0, 0]
    return sum((((30 >> (4 * bits[i + 2] + 2 * bits[i + 1] + bits[i])) & 1) << i)
               for i in range(y.bit_length() + 1))


def literal_g(y):
    return literal_f(literal_f(y))


def windows(y, r):
    bits = [0] * (r - 1) + [(y >> i) & 1 for i in range(y.bit_length())] + [0] * (r - 1)
    c = Counter(tuple(bits[i:i + r]) for i in range(len(bits) - r + 1))
    c.pop((0,) * r, None)
    return c


def stripe(n):
    return sum(1 << i for i in range(0, n, 2))


def label(y, w, e):
    return (y & ((1 << w) - 1), y >> max(y.bit_length() - e, 0), min(y.bit_length(), e))


def run_original(mode):
    root = OUT / 'replay'
    dest = root / 'out' / 'XP-3'
    dest.mkdir(parents=True, exist_ok=True)
    (root / 'sw').mkdir(exist_ok=True)
    shutil.copyfile(REF, root / 'sw' / 'ref.py')
    for name in ('cert.py', 'cert2.py', 'certlib.py', 'bb.py'):
        src = SOURCE / 'out' / 'XP-3' / name
        shutil.copyfile(src, dest / name)
        assert (dest / name).read_bytes() == src.read_bytes()
    import scipy.optimize
    original = scipy.optimize.linprog

    def one_thread(*args, **kwargs):
        options = dict(kwargs.get('options') or {})
        options.update(threads=1, parallel=False)
        kwargs['options'] = options
        return original(*args, **kwargs)

    scipy.optimize.linprog = one_thread
    sys.argv = [str(dest / (mode + '.py')), '14'] + (['6'] if mode == 'cert' else [])
    runpy.run_path(sys.argv[0], run_name='__main__')
    print('ATLAS_' + mode.upper() + '_REPLAY_PASS', flush=True)


def build_closure():
    roots = []
    closure = set()
    parents = {}
    for y in range(1, 1 << 14, 2):
        z = y
        for _ in range((y.bit_length() + 1) // 2):
            if not z & 1:
                break
            z = literal_g(z)
        else:
            roots.append(y)
            z = y
            for tick in range(201):
                if not z & 1:
                    break
                closure.add(z)
                parents.setdefault(z, [hex(y), 2 * tick])
                z = literal_g(z)
            else:
                raise AssertionError('FIXED_400_TICK_CLOSURE_STOP')
    return roots, closure, parents


def certificate_checks():
    roots, closure, parents = build_closure()
    emit('closure', {'max_start_width': 14, 'roots': len(roots), 'rows': len(closure),
                     'witnesses': {hex(y): p for y, p in parents.items()}})
    reports = []

    def check(path, tag):
        data = json.loads(path.read_text())
        r, w, e = data['r'], data.get('w', 0), data.get('e', 0)
        terms = [(int(y, 16), Q(q)) for y, q in data['list']]
        assert terms and sum(q for _, q in terms) == 1 and all(q > 0 for _, q in terms)
        assert all(y in closure and y & 1 and literal_g(y) & 1 for y, _ in terms)
        n = 2 * max(r, w, e) + 5
        target = windows(stripe(n + 2), r)
        target.subtract(windows(stripe(n), r))
        again = windows(stripe(n + 4), r)
        again.subtract(windows(stripe(n + 2), r))
        assert all(target[k] == again[k] for k in set(target) | set(again))
        lhs, wall, edge, joint = Counter(), Counter(), Counter(), Counter()
        width = Q(0)
        for y, q in terms:
            g = literal_g(y)
            for k, v in windows(g, r).items(): lhs[k] += q * v
            for k, v in windows(y, r).items(): lhs[k] -= q * v
            width += q * (g.bit_length() - y.bit_length())
            if w:
                a, b = label(y, w, e), label(g, w, e)
                wall[b[0]] += q; wall[a[0]] -= q
                edge[b[1:]] += q; edge[a[1:]] -= q
                joint[b] += q; joint[a] -= q
        assert width == 2
        assert all(lhs[k] == target[k] for k in set(lhs) | set(target))
        assert all(v == 0 for v in wall.values()) and all(v == 0 for v in edge.values())
        bad_joint = sum(v != 0 for v in joint.values())
        if data.get('joint'): assert bad_joint == 0
        # The original +1000 negative LP control has an exact coordinate separator:
        # the width equality forces sum(lambda)=1, and no available pair reaches it.
        first = (1,) + (0,) * (r - 1)  # numerical count-index 1 in original scripts
        cap = max(windows(literal_g(y), r)[first] - windows(y, r)[first]
                  for y in closure if literal_g(y) & 1)
        assert target[first] + 1000 > cap
        # A corrupted coefficient is rejected without asking an LP solver.
        assert sum([terms[0][1] + 1] + [q for _, q in terms[1:]]) != 1
        if w: assert label(stripe(n), w, e) == label(stripe(n + 2), w, e)
        return {'source': tag, 'file': path.name, 'r': r, 'w': w, 'e': e,
                'W0': data['W0'], 'support': len(terms), 'max_denominator': max(q.denominator for _, q in terms),
                'exact_identity': True, 'joint_nonzero': bad_joint,
                'negative_coordinate_upper_bound': cap, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

    for source, tag in ((SOURCE / 'out' / 'XP-3', 'filed'), (OUT / 'replay' / 'out' / 'XP-3', 'rerun')):
        for p in sorted(source.glob('cert*.json')):
            reports.append(check(p, tag))
    for p in sorted((SOURCE / 'out' / 'SC-5').glob('joint_r*_W14.json')):
        reports.append(check(p, 'SC-5-repair'))
    assert len(reports) == 29  # 13 filed, 13 rerun, three joint replacements
    filed = {x['file']: x for x in reports if x['source'] == 'filed'}
    assert [filed[f'cert2_r{r}_w6.json']['joint_nonzero'] for r in (2, 3, 4)] == [8, 10, 14]
    assert all(x['joint_nonzero'] == 0 for x in reports if x['source'] == 'SC-5-repair')
    # The report's Y=3 claim holds only through r=3, not r=4.
    base = []
    for r in range(1, 5):
        a = windows(literal_g(3), r); a.subtract(windows(3, r))
        n = 2 * r + 5
        b = windows(stripe(n + 2), r); b.subtract(windows(stripe(n), r))
        base.append(all(a[k] == b[k] for k in set(a) | set(b)))
    assert base == [True, True, True, False]
    emit('certificates', {'checks': reports, 'Y3_r1_to_4': base, 'all_exact': True})
    print('ATLAS_RATIONAL_CERTIFICATES_PASS', flush=True)


def definitions(path):
    """Load definitions, not a source file's unbounded search driver."""
    tree = ast.parse(path.read_text())
    tree.body = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))]
    ns = {'__name__': 'definitions_only'}
    exec(compile(tree, str(path), 'exec'), ns)
    return ns


def br_checks():
    sys.path.insert(0, str(REF.parent))
    lp = definitions(BR / 'lp.py')
    skeletons = [(0, 0), (0, 1, 1, 0), (0, 1, 0, 1), (1, 0, 2, 1, 3, 2, 0, 3)]
    checks = 0
    for tr in skeletons:
        N = len(tr) // 2
        h = [i - 3 for i in range(2 * N)]; t = [2 - i for i in range(N)]
        for direction in ('wall', 'edge'):
            nodes, edges, ends = lp['build'](tr, N, direction)
            adj = {(a, letter): (b, ex) for a, b, ex, letter, _ in edges}
            end = {a: ex for a, ex, _ in ends}
            values = h + t
            ev = lambda ex: sum(v * values[k[1]] for k, v in ex.items())
            for y in range(1, 1 << 10, 2):
                g = literal_g(y)
                if not g & 1: continue
                a = [(y >> i) & 1 for i in range(y.bit_length())]
                b = [(g >> i) & 1 for i in range(g.bit_length())]
                if direction == 'edge': a.reverse(); b.reverse()
                v = 0; score = 0
                for letter in a:
                    v, ex = adj[v, letter]; score += ev(ex)
                assert v in end
                score += ev(end[v])
                assert score == lp['phi'](b, tr, h, t) - lp['phi'](a, tr, h, t)
                checks += 1
    def transform(bits, k):
        for _ in range(k):
            bits = [bits[i] ^ (bits[i - 1] | bits[i - 2]) for i in range(2, len(bits))]
        return tuple(bits)
    window_checks = 0
    for k in range(1, 9):
        m = [0] * (2 * k); mt = [1] + m[1:]
        assert transform(m + [0], k) == (0,)
        assert transform(mt + [0], k) == (1,)
        for ell in range(1, 7):
            images = set()
            for word in itertools.product((0, 1), repeat=ell):
                a = transform(m + list(word), k); b = transform(mt + list(word), k)
                assert b == (1 ^ a[0],) + a[1:]
                assert (m + list(word))[-2 * k:] == (mt + list(word))[-2 * k:]
                images.add(a); window_checks += 1
            assert len(images) == 1 << ell
    hf = definitions(BR / 'hfs_core.py')
    stakes = {}
    tr = (1, 0, 0, 0)
    for k in range(1, 5):
        for name, fun in (('rule30', lambda a, b: a | b), ('rule210', lambda a, b: (1 ^ a) & b)):
            tab, L = hf['make_g'](fun, k)
            stakes[name, k] = hf['has_stake'](tr, 2, tab, L)
            assert stakes[name, k] == (name == 'rule210')
    emit('br-controls', {'encoding_checks': checks, 'window_memory_checks': window_checks,
                         'stake_countercontrols': {str(k): v for k, v in stakes.items()},
                         'bounded_controls_only': True})
    print('ATLAS_BR_CONTROLS_PASS', flush=True)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode in ('cert', 'cert2'): run_original(mode)
    elif mode == 'verify': certificate_checks()
    elif mode == 'br': br_checks()
    else: raise ValueError(mode)
