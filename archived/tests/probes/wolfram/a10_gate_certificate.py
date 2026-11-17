#!/usr/bin/env python3
"""GC2581: fixed a10 RUP template; four tiny checker calls, NO SAT solver.

Check the gate-only lemma independently of the already-UNSAT cylinder.
Then match five fixed translations to the pinned original DIMACS gates.
No root/path units are permitted in the translated implication proofs.
"""
import ast
import hashlib
import itertools
import json
import os
from pathlib import Path
import re
import resource
import signal
import subprocess
import time

OUT = Path(os.environ['CAPPED_OUT'])
STOP = []
REPORT = {'status': 'STARTED', 'commands': []}
CHECKER = '/usr/local/bin/cake_lpr'
HELPER = Path(__file__).parents[1] / 'ether_gap_solve.py'
assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
names = {'save', 'cpu', 'thermal', 'command'}
selected = [n for n in ast.parse(HELPER.read_bytes()).body
            if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(selected) == 4
# Same monitored sequential checker helper, with a LOWER worker aggregate stop.
class LowerBudget(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(20), node) if node.value == 95 else node
tree = ast.Module(body=selected, type_ignores=[])
exec(compile(ast.fix_missing_locations(LowerBudget().visit(tree)), str(HELPER), 'exec'), globals())

RULE = (0, 1, 1, 1, 1, 0, 0, 0)
# A,B,C,U,V,P,Q,R,Z = 1,...,9. Four gates: ABC->P, BCU->Q,
# CUV->R, PQR->Z, each in increasing truth-table index j=0,...,7.
GATES = ((1, 2, 3, 6), (2, 3, 4, 7), (3, 4, 5, 8), (6, 7, 8, 9))
# IDs 33..38; every hint is an original gate or an earlier addition.
ADDITIONS = (
    ((6, -7, 9), (27, 28)),
    ((6, -8, 9), (26, 28)),
    ((-6, -7, -9), (31, 32)),
    ((-6, -8, -9), (30, 32)),
    ((-1, -2, 3, 9), (7, 33, 34, 13, 19, 20)),
    ((1, -2, 3, -9), (3, 35, 36, 13, 19, 20)),
)


def gate(a, b, c, d):
    return [tuple(-v if bit else v for v, bit in
                  zip((a, b, c), ((j >> 2) & 1, (j >> 1) & 1, j & 1)))
            + (d if RULE[j] else -d,) for j in range(8)]


def sat(clause, assignment):
    return any(assignment[abs(v)] == (v > 0) for v in clause)


def rup(clause, hints, database):
    assert len(set(map(abs, clause))) == len(clause)
    assigned = {abs(v): v < 0 for v in clause}
    for h in hints:
        assert h > 0 and h in database
        source = database[h]
        if any(assigned.get(abs(v)) == (v > 0) for v in source if abs(v) in assigned):
            return False
        unset = [v for v in source if abs(v) not in assigned]
        if not unset:
            return True
        if len(unset) != 1:
            return False
        assigned[abs(unset[0])] = unset[0] > 0
    return False


def propagation_conflict(clause, original):
    """Full unhinted UP, solely to test the predicted direct-RUP failure."""
    assigned = {abs(v): v < 0 for v in clause}
    while True:
        changed = False
        for source in original:
            if any(assigned.get(abs(v)) == (v > 0) for v in source if abs(v) in assigned):
                continue
            unset = [v for v in source if abs(v) not in assigned]
            if not unset:
                return True
            if len(unset) == 1:
                assigned[abs(unset[0])] = unset[0] > 0
                changed = True
        if not changed:
            return False


def write_cnf(path, nv, clauses):
    path.write_text('p cnf %d %d\n' % (nv, len(clauses)) +
                    ''.join(' '.join(map(str, c)) + ' 0\n' for c in clauses))


def line(cid, clause, hints):
    return '%d %s0 %s0\n' % (cid, ''.join('%d ' % v for v in clause),
                             ''.join('%d ' % h for h in hints))


def original_maps():
    # Lazy allocation in the independently read GC2555 reconstruction.
    variables = {}; gates = {}; cid = 0
    def var(t, x):
        if (t, x) not in variables:
            variables[t, x] = len(variables) + 1
        return variables[t, x]
    for x in range(-86, 17):
        var(0, x); cid += 1
    for t in range(83):
        for x in range(-85, 99 - t):
            vs = tuple(var(s, y) for s, y in ((t, x-1), (t, x), (t, x+1), (t+1, x)))
            assert cid + 1 == 104 + 1473*t - 4*t*(t-1) + 8*(x+85)
            gates[t, x] = (cid + 1, vs); cid += 8
        var(t+1, -86); cid += 1
    assert cid == 95138 and len(variables) == 12138
    return variables, gates


def translate(t, x, variables, gates, original):
    if not (0 <= t <= 81 and -84 <= x <= 97-t):
        raise ValueError('incomplete two-tick gate support')
    coords = [(t, x+i) for i in (-2, -1, 0, 1, 2)]
    coords += [(t+1, x+i) for i in (-1, 0, 1)] + [(t+2, x)]
    vm = {i+1: variables[c] for i, c in enumerate(coords)}
    assert len(set(vm.values())) == 9
    cm = {}; support = {}
    for k, key in enumerate(((t, x-1), (t, x), (t, x+1), (t+1, x))):
        first, vs = gates[key]
        for j, expected in enumerate(gate(*vs)):
            oid = first+j
            assert original[oid] == expected
            cm[1+8*k+j] = oid; support[oid] = expected
    text = ''; emitted = []
    for k, (clause, hints) in enumerate(ADDITIONS):
        cid = 95175+k; cm[33+k] = cid
        translated = tuple(vm[abs(v)] * (1 if v > 0 else -1) for v in clause)
        translated_hints = tuple(cm[h] for h in hints)
        assert rup(translated, translated_hints, support)
        support[cid] = translated
        text += line(cid, translated, translated_hints)
        emitted.append({'id': cid, 'clause': translated, 'hints': translated_hints})
    return text, {'time': t, 'endpoint': x, 'variables': vm,
                  'original_gate_clause_ids': sorted(set(cm.values()) - set(range(95175, 95181))),
                  'additions': emitted}


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (6, 6))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    assert hashlib.sha256(Path(CHECKER).read_bytes()).hexdigest() == '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'
    thermal()
    original = [c for g in GATES for c in gate(*g)]
    # Independent scalar semantics over ALL 512 assignments to the nine variables.
    models = 0
    for values in itertools.product((False, True), repeat=9):
        a = dict(enumerate(values, 1))
        semantic = all(a[d] == (a[l] ^ (a[c] or a[r])) for l, c, r, d in GATES)
        assert all(sat(c, a) for c in original) == semantic
        if semantic:
            models += 1
            assert all(sat(c, a) for c, _ in ADDITIONS)
    assert models == 32
    db = dict(enumerate(original, 1))
    for cid, (clause, hints) in enumerate(ADDITIONS, 33):
        assert rup(clause, hints, db)
        db[cid] = clause
    for clause, _ in ADDITIONS[-2:]:
        assert not propagation_conflict(clause, original)
    # Missing B or C guards have concrete scalar counterexamples, both colours.
    witnesses = []
    for a in (0, 1):
        for root in ((a, 0, 0, 1, 0), (a, 1, 1, 1, 0)):
            row = root
            for _ in range(2):
                row = tuple(row[i] ^ (row[i+1] | row[i+2]) for i in range(len(row)-2))
            assert row == (1-a,)
            witnesses.append({'root': root, 'output': row[0]})
    for clause, hints in ADDITIONS[-2:]:
        for guard in (-2, 3):
            weakened = tuple(v for v in clause if v != guard)
            assert not rup(weakened, hints, db)
    assert not rup(ADDITIONS[4][0], (7, 27, 34, 13, 19, 20), db)
    # Four tiny, sequential checker invocations. No solver at any point.
    good = OUT/'unit.cnf'; write_cnf(good, 1, [(1,), (-1,)])
    for name, proof, accept in [('unit-good', '3 0 1 2 0\n', True),
                                ('unit-bad', '3 0 1 1 0\n', False)]:
        p = OUT/(name+'.lrat'); p.write_text(proof)
        rc, text, reason = command(name, [CHECKER, '--CML_HEAP_SIZE=64', '--CML_STACK_SIZE=32', str(good), str(p)], 1, 4)
        assert reason == 'EXIT'
        assert ('s VERIFIED UNSAT' in text) == accept
        if accept: assert rc == 0
    for n, target in enumerate((ADDITIONS[4][0], ADDITIONS[5][0])):
        cnf = OUT/('a10-%d.cnf' % n); proof = OUT/('a10-%d.lrat' % n)
        write_cnf(cnf, 9, original + [(-v,) for v in target])
        def shift(h): return h+4 if h >= 33 else h
        proof.write_text(''.join(line(cid+4, c, tuple(shift(h) for h in hs))
                                 for cid, (c, hs) in enumerate(ADDITIONS, 33)) +
                         line(43, (), (33, 34, 35, 36, 41+n)))
        rc, text, reason = command('a10-%d' % n, [CHECKER, '--CML_HEAP_SIZE=64', '--CML_STACK_SIZE=32', str(cnf), str(proof)], 1, 4)
        assert rc == 0 and reason == 'EXIT' and 's VERIFIED UNSAT' in text
    raw = Path(os.environ['A10_ORIGINAL_CNF']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == '902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9'
    lines = raw.decode().splitlines(); assert lines[0] == 'p cnf 12138 95174'
    orig = {i: tuple(map(int, s.split()))[:-1] for i, s in enumerate(lines[1:], 1)}
    assert len(orig) == 95174
    variables, gates = original_maps(); translations = []
    for t, x in ((0, -84), (0, 97), (81, -84), (81, 16), (17, 10)):
        fragment, receipt = translate(t, x, variables, gates, orig)
        (OUT/('template-t%d-x%d.lrat' % (t, x))).write_text(fragment)
        translations.append(receipt)
    for t, x in ((-1, 0), (82, 0), (0, -85), (0, 98), (81, 17)):
        try: translate(t, x, variables, gates, orig)
        except ValueError: pass
        else: raise AssertionError('missing support guard')
    thermal()
    REPORT.update(status='GATE_ONLY_A10_CERTIFIED_AND_FIVE_ORIGINAL_TRANSLATIONS_CHECKED',
                  gate_models=models, guard_counterexamples=witnesses,
                  direct_rup_without_masking=False, translations=translations,
                  scope='Two local implications certified by cake_lpr; translated fragments are RUP-checked against original gate clauses only. No new cylinder proof, solver or trajectory.',
                  controls='scalar full-gate semantics, positive/negative checker controls, missing-guard witnesses, invalid hint and incomplete support rejected')
    save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error)); save(); raise
