#!/usr/bin/env python3
"""rule30_cloud_hole_freepairs_long_selftest.py: FP2's verdict fixtures (GC902), with no solver and no PySAT.

RUN-ON:     cpu, one core (Python 3 standard library); instant
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_hole_freepairs_long_selftest.py

Only the functions sample_verdict and verdicts are compiled from FP2's source (by AST, as GPT's GC902 harness did), and
fed mocked run_family results. F1 to F3 are GC902's three reporting counterexamples to the earlier source; F4 to F7
are Cloud's. Prints PASS or FAIL for each, then ALL.
"""
import ast
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rule30_cloud_hole_freepairs_long.py')
_tree = ast.parse(open(SRC).read())
_mod = ast.Module(body=[n for n in _tree.body if isinstance(n, ast.FunctionDef)
                        and n.name in ('sample_verdict', 'verdicts')], type_ignores=[])
NS = {}
exec(compile(_mod, SRC, 'exec'), NS)


def C(a=0, s=0, u=0, k=0):
    return {'attempted': a, 'sat': s, 'unsat': u, 'unknown': k}


def fam(main, total, fails, extra=False, long=None, lf=(), uu=None, uf=(), c2=None, rb=0, tb=0):
    r = {'c2': c2 or C(6, 6), 'c2_total': 6, 'main': main, 'total': total, 'fails': list(fails),
         'replay_bad': rb, 'tail_bad': tb, 'long': C(), 'u': C()}
    if extra:
        r.update({'long': long or C(), 'long_total': 30, 'long_fails': list(lf),
                  'u': uu or C(), 'u_total': 32, 'u_fails': list(uf)})
    return r


def full_ok(p):
    return fam(C(1024, 1024), 1024, []) if p != 5 else fam(C(64, 64), 64, [])


def res(f9, **kw):
    d = {9: f9, 7: full_ok(7), 5: full_ok(5)}
    d.update(kw)
    return d

cases = {
 'F1': res(fam(C(109, 109), 1024, [], extra=True)),
 'F2': res(fam(C(1024, 1023, 0, 1), 1024, [], extra=True, long=C(30, 30), uu=C(32, 32))),
 'F3': res(fam(C(109, 108, 1), 1024, ['w'], extra=True)),
 'F4': res(fam(C(1024, 1024), 1024, [], extra=True, long=C(2, 0, 1, 1), lf=['x'], uu=C(32, 32))),
 'F5': res(fam(C(1024, 1024), 1024, [], extra=True, long=C(30, 30), uu=C(32, 32), c2=C(6, 5, 0, 1))),
 'F6': res(fam(C(1024, 1024), 1024, [], extra=True, long=C(30, 30), uu=C(32, 32), tb=1)),
 'F7': res(fam(C(1024, 1024), 1024, [], extra=True, long=C(30, 30), uu=C(32, 32))),
}
expect = {
 'F1': {'P1': 'NOT DECIDED', 'P4': 'NOT DECIDED', 'U': 'NOT DECIDED'},
 'F2': {'P1': 'NOT DECIDED'},
 'F3': {'P1': 'REFUTED', 'P4': 'NOT DECIDED', 'U': 'NOT DECIDED'},
 'F4': {'P4': 'REFUTED'},
 'F5': {'C2': 'NOT DECIDED', 'P1': 'NOT DECIDED', 'P2': 'NOT DECIDED', 'P3': 'NOT DECIDED', 'P4': 'NOT DECIDED',
        'U': 'NOT DECIDED'},
 'F6': {'C1': 'FAIL'},
 'F7': {'C1': 'PASS', 'C2': 'PASS', 'P1': 'HELD', 'P2': 'HELD', 'P3': 'HELD', 'P4': 'HELD', 'U': 'HELD'},
}
allok = True
for k, r in cases.items():
    v = NS['verdicts'](r)
    bad = {x: (v[x], e) for x, e in expect[k].items() if v[x] != e}
    allok &= not bad
    print(k, 'PASS' if not bad else 'FAIL %s' % bad, v)
print('ALL', 'PASS' if allok else 'FAIL')
