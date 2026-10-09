#!/usr/bin/env python3
"""GC855 source audit of Cloud's SL, registered before execution in the ledger.
P1: internal Boolean and projected-boundary clauses match the literal rule.
P2: separate model checker rejects an all-zero model violating imposed units.
Unexpected U1: an unrecognized solver return must not be treated as SAT.
OUTCOME: P1 PASS; P2 REFUTED (checker accepts;153 fixed units fail at phase0).
U1 source audit finds every return other than20 treated as a model. This is a
checker/verdict coverage issue, not a claim that a real SL solve failed.
No SAT solver is invoked. Peer source is never modified.
"""
from itertools import product
from pathlib import Path
import runpy


def check():
    for y, a, b, c, o in product((0, 1), repeat=5):
        clauses = (((not o) or b or c) and (o or not b) and (o or not c)
                   and ((not y) or a or o) and ((not y) or (not a) or (not o))
                   and (y or (not a) or o) and (y or a or (not o)))
        assert bool(clauses) == (o == (b | c) and y == (a ^ o))
    for y, a, b in product((0, 1), repeat=3):
        clauses = ((not b) or y or a) and ((not b) or (not y) or (not a))
        assert bool(clauses) == any(y == (a ^ (b | c)) for c in (0, 1))
    source = Path(__file__).with_name('rule30_cloud_wheel_slab.py')
    m = runpy.run_path(str(source), run_name='slab_audit_import')
    cl, n, var = m['build'](0)
    zero = set()
    bad = sum(not any(lit < 0 for lit in c) for c in cl)
    assert bad == 153 and m['check'](zero, var) is True
    # Inject a non-SAT/non-UNSAT status, with no executable invoked.
    glob = m['solve'].__globals__
    old = glob['subprocess'].run
    class Unknown:
        returncode = 0
        stdout = ''
    try:
        glob['subprocess'].run = lambda *a, **kw: Unknown()
        assert m['solve'](cl, n) == set()
    finally:
        glob['subprocess'].run = old
    print('GC855: clause templates PASS; model checker misses153 units; unknown status becomes empty model')

if __name__ == '__main__':
    check()
