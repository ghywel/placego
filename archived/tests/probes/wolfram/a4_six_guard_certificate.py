#!/usr/bin/env python3
"""GC2609: one fixed 111011 implication; 18 hand RUP additions, no solver.

Gate-only replay precedes a verified-checker implication query. No original
path/root units, search, observer closure, or symbolic simplification.
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


def pinned(path, sha):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == sha, 'INPUT_HASH_MISMATCH'
    return raw


helper = Path(__file__).parents[1] / 'ether_gap_solve.py'
raw = pinned(helper, '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d')
names = {'save', 'cpu', 'thermal', 'command'}
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(nodes) == 4


class LowerBudget(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(10), node) if node.value == 95 else node


exec(compile(ast.fix_missing_locations(LowerBudget().visit(ast.Module(body=nodes, type_ignores=[]))), str(helper), 'exec'), globals())
template = Path(__file__).with_name('a10_gate_certificate.py')
raw = pinned(template, '2ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874')
names = {'rup', 'gate', 'sat', 'write_cnf', 'line'}
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(nodes) == 5
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(template), 'exec'), globals())

RULE = (0, 1, 1, 1, 1, 0, 0, 0)
COORDS = ([(0, j) for j in range(7)] + [(1, j) for j in range(1, 8)]
          + [(2, j) for j in range(2, 7)] + [(3, j) for j in range(3, 6)] + [(4, 4)])
GATE_COORDS = ([(0, j) for j in range(1, 6)] + [(1, j) for j in range(2, 7)]
               + [(2, j) for j in range(3, 6)] + [(3, 4)])
H = (-1, -2, -3, 4, -5, -6)
ADDITIONS = (
    ((17, -18, 22), (99, 100)),
    ((17, -19, 22), (98, 100)),
    ((-17, -18, -22), (103, 104)),
    ((-17, -19, -22), (102, 104)),
    ((-10, -11, 12, 22), (63, 113, 114, 69, 75, 76)),
    ((10, -11, 12, -22), (59, 115, 116, 69, 75, 76)),
    (H + (-8,), (8,)),
    (H + (-9,), (15,)),
    (H + (-10,), (22,)),
    (H + (11,), (28,)),
    (H + (-12,), (39, 40)),
    (H + (-15,), (119, 120, 121, 41)),
    (H + (16,), (120, 121, 122, 50)),
    (H + (17,), (121, 122, 123, 59)),
    (H + (20,), (124, 125, 126, 84)),
    (H + (-21,), (125, 126, 95, 96)),
    (H + (-22,), (121, 122, 123, 118)),
    (H + (23,), (127, 128, 129, 109)),
)


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pinned(CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    thermal()
    vm = {c: i + 1 for i, c in enumerate(COORDS)}
    gates = [tuple(vm[c] for c in ((t, j-1), (t, j), (t, j+1), (t+1, j)))
             for t, j in GATE_COORDS]
    assert len(vm) == 23 and len(gates) == 14
    original = [c for g in gates for c in gate(*g)]
    assert len(original) == 112
    # Independent four-variable gate truth-table comparison, not a solver.
    for g in gates:
        for bits in itertools.product((False, True), repeat=4):
            a = dict(zip(g, bits))
            assert all(sat(c, a) for c in gate(*g)) == (bits[3] == (bits[0] ^ (bits[1] or bits[2])))
    db = dict(enumerate(original, 1))
    for cid, (clause, hints) in enumerate(ADDITIONS, 113):
        assert all(0 < h < cid and h in db for h in hints)
        assert rup(clause, hints, db), ('BAD_HAND_STEP', cid)
        db[cid] = clause
    assert ADDITIONS[-1][0] == H + (23,)
    # Same-word exterior check; independent literal update, no CNF evaluator.
    outputs = []
    for ext in itertools.product((0, 1), repeat=3):
        row = (1, 1, 1, 0, 1, 1) + ext
        for _ in range(4):
            row = tuple(row[i] ^ (row[i+1] | row[i+2]) for i in range(len(row)-2))
        assert row == (1,)
        outputs.append(row[0])
    # Adversarial query: remove only the sixth root guard; retain all gates.
    weak = H[:-1] + (23,)
    models = []
    for root in itertools.product((False, True), repeat=9):
        rows = [dict(enumerate(root))]
        for _ in range(4):
            r = rows[-1]
            rows.append({j: r[j-1] ^ (r[j] or r[j+1]) for j in range(min(r)+1, max(r))})
        a = {vm[c]: rows[c[0]][c[1]] for c in COORDS}
        assert all(sat(c, a) for c in original)
        assert sat(H + (23,), a)
        if not sat(weak, a):
            models.append({'initial_0_8': ''.join(str(int(x)) for x in root), 'target': int(a[23])})
    assert models, 'MISSING_GUARD_COUNTEREXAMPLE_ABSENT'
    (OUT/'gate-only-prefix.lrat').write_text(''.join(line(cid, c, hs) for cid, (c, hs) in enumerate(ADDITIONS, 113)))
    write_cnf(OUT/'gates.cnf', 23, original)
    # Gate-only prefix is translated past seven fresh assumption units.
    units = [(-x,) for x in H + (23,)]
    query = original + units
    n = len(query)
    remap = {i: i for i in range(1, 113)}
    prefix = []
    restricted = dict(enumerate(original, 1))
    for old, (clause, hints) in enumerate(ADDITIONS, 113):
        cid = n + len(prefix) + 1
        hs = tuple(remap[h] for h in hints)
        assert rup(clause, hs, restricted)
        remap[old] = cid
        prefix.append((cid, clause, hs)); restricted[cid] = clause
    final = (n + len(prefix) + 1, (), tuple(range(113, n+1)) + (remap[130],))
    assert rup(final[1], final[2], {**dict(enumerate(query, 1)), **restricted})
    write_cnf(OUT/'implication.cnf', 23, query)
    (OUT/'implication.lrat').write_text(''.join(line(*p) for p in prefix + [final]))
    # Remove a necessary dependency on the final forcing gate (not a dead lemma).
    bad = prefix.copy()
    bad[-1] = (bad[-1][0], bad[-1][1], bad[-1][2][:-1])
    assert not rup(bad[-1][1], bad[-1][2], restricted)
    (OUT/'bad.lrat').write_text(''.join(line(*p) for p in bad + [final]))
    write_cnf(OUT/'unit.cnf', 1, [(1,), (-1,)])
    (OUT/'unit.lrat').write_text('3 0 1 2 0\n')
    for name, cnf, proof, accept in [('unit', 'unit.cnf', 'unit.lrat', True),
                                    ('bad', 'implication.cnf', 'bad.lrat', False),
                                    ('good', 'implication.cnf', 'implication.lrat', True)]:
        rc, txt, why = command(name, [CHECKER, '--CML_HEAP_SIZE=128', '--CML_STACK_SIZE=32', str(OUT/cnf), str(OUT/proof)], 2, 5)
        assert why == 'EXIT'
        assert (rc == 0 and 's VERIFIED UNSAT' in txt) == accept, (name, rc, txt)
        if not accept:
            assert rc != 0 and 's VERIFIED UNSAT' not in txt
    REPORT.update(status='PASS', variables=23, gates=14, gate_clauses=112,
                  prefix_additions=18, guard=H, conclusion=H+(23,),
                  exterior_outputs=outputs, missing_sixth_guard_counterexamples=models,
                  original_host_embedding='NOT PERFORMED; no original-path exclusion claimed')
    save()


try:
    main()
except BaseException as e:
    REPORT.update(status='FAILED', error=repr(e)); save(); raise
