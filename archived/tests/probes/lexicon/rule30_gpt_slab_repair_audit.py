#!/usr/bin/env python3
"""GC860 independent source repair audit; no SAT executable invoked.
P1 strict verdicts; P2 all original/extra clauses; P3 scalar fixed units.
Positive control: literal three-row half-line trajectory.
Unexpected control: clock/wheel unit mutations.
GC855's historical failing probe and record remain unchanged.
"""
from pathlib import Path
import runpy
from types import SimpleNamespace


def main():
    src = Path(__file__).with_name('rule30_cloud_wheel_slab.py')
    m = runpy.run_path(str(src), run_name='slab_repair_audit_import')
    cl, n, var = m['build'](0)
    assert not m['check'](set(), var, 0)
    assert not m['satisfies'](set(), cl)
    glob = m['solve'].__globals__
    old = glob['subprocess'].run
    calls = []
    def mock(code, stdout=''):
        def run(*a, **kw):
            calls.append(code)
            return SimpleNamespace(returncode=code, stdout=stdout, stderr='injected audit verdict')
        glob['subprocess'].run = run
    def rejected(fn, message):
        try:
            fn()
        except RuntimeError as e:
            assert message in str(e), str(e)
        else:
            raise AssertionError('invalid result accepted')
    try:
        for code in (0, 1, -9, 30):
            mock(code)
            rejected(lambda: m['solve'](cl, n), 'exit')
        mock(20)
        assert m['solve'](cl, n) is None
        mock(10)
        rejected(lambda: m['solve'](cl, n), 'violates the CNF')
        mock(10, 's SATISFIABLE\nv 1 -2 0\n')
        assert m['solve']([[1], [-2], [1, -2]], 2) == {1}
        rejected(lambda: m['solve']([[1], [-2]], 2, [[-1]]), 'violates the CNF')
        # Short literal trajectory from a white right half, with 0 clamped 010.
        # Its column 1 is 001; this is a fixture, not the period-56 wheel.
        glob.update(L=3, K=2, P=3, U='001')
        small, nv, v = m['build'](0)
        rows = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
        good = {v[t, k] for t in range(3) for k in range(3) if rows[t][k]}
        for t in range(2):
            if rows[t][1] | rows[t][2]:
                good.add(len(v) + 1 + t)
        assert m['satisfies'](good, small)
        assert m['check'](good, v, 0)
        mock(10, 'v ' + ' '.join(str(i if i in good else -i) for i in range(1, nv + 1)) + ' 0\n')
        assert m['solve'](small, nv) == good
        for key in ((1, 0), (2, 1)):
            bad = good ^ {v[key]}
            assert not m['satisfies'](bad, small)
            assert not m['check'](bad, v, 0)
    finally:
        glob['subprocess'].run = old
    print('GC860 ALL CONTROLS PASS: strict verdicts, original/extra clauses, scalar units, valid literal fixture')
    print('Mock calls only:', len(calls), '; no solver or actual forcing-count replay')


if __name__ == '__main__':
    main()
