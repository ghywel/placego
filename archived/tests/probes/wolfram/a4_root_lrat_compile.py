#!/usr/bin/env python3
"""GC2588: compile ONE retained root DAG; no search, SAT solver or census.

Certify both the 25-cell consequence and the original cylinder, separately.
Only root leaves and byte-matched original gates may support the consequence.
"""
import ast
from collections import Counter
import hashlib
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


def pinned(path, digest):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest, 'INPUT_HASH_MISMATCH'
    return raw


# Reuse the monitored sequential command helper with its aggregate stop LOWERED.
helper = Path(__file__).parents[1] / 'ether_gap_solve.py'
raw = pinned(helper, '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d')
names = {'save', 'cpu', 'thermal', 'command'}
selected = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(selected) == 4
class LowerBudget(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(20), node) if node.value == 95 else node
exec(compile(ast.fix_missing_locations(LowerBudget().visit(ast.Module(body=selected, type_ignores=[]))), str(helper), 'exec'), globals())

# Import only pure definitions/constants from the already checked template.
primitive = Path(__file__).with_name('a10_gate_certificate.py')
raw = pinned(primitive, '2ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874')
names = {'gate', 'rup', 'line', 'original_maps', 'write_cnf', 'sat'}
selected = [n for n in ast.parse(raw).body
            if (isinstance(n, ast.FunctionDef) and n.name in names)
            or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in {'RULE', 'ADDITIONS'} for t in n.targets))]
assert len(selected) == 8
exec(compile(ast.Module(body=selected, type_ignores=[]), str(primitive), 'exec'), globals())


def local_hints(clause, candidates, db):
    """Ordered unit propagation on a fixed local support, not a SAT search."""
    assigned = {abs(v): v < 0 for v in clause}
    hints = []
    for _ in range(len(candidates) + 1):
        changed = False
        for h in candidates:
            source = db[h]
            if any(assigned.get(abs(v)) == (v > 0) for v in source if abs(v) in assigned):
                continue
            unset = [v for v in source if abs(v) not in assigned]
            if not unset:
                return tuple(hints + [h])
            if len(unset) == 1:
                assigned[abs(unset[0])] = unset[0] > 0
                hints.append(h); changed = True
        if not changed:
            break
    raise AssertionError('LOCAL_RUP_FAILED')


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (6, 6))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pinned(CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    thermal()
    cnf_raw = pinned(os.environ['ROOT_ORIGINAL_CNF'], '902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9')
    rows = cnf_raw.decode().splitlines()
    assert rows[0] == 'p cnf 12138 95174'
    original = {}
    for i, row in enumerate(rows[1:], 1):
        literals = tuple(map(int, row.split()))
        assert literals[-1] == 0 and 0 not in literals[:-1]
        original[i] = literals[:-1]
    assert len(original) == 95174
    trace = json.loads(pinned(os.environ['ROOT_TRACE'], '2b3b5d8c554b9bb218bf71441b61c0143f075d2b2e2fa11be95ebd07f7cd5a5e'))
    assert Counter(n['rule'] for n in trace) == {'initial': 25, 'gate': 154, 'a10': 55}
    variables, gates = original_maps()
    db = {}; support = {}; facts = {}; proof = []; node_ids = []
    def add(clause, hints):
        cid = 95175 + len(proof)
        assert cid not in db and rup(clause, hints, db), ('BAD_ADDITION', cid)
        db[cid] = clause; proof.append((cid, clause, hints))
        return cid
    def use_gate(key):
        first, vs = gates[key]
        for j, clause in enumerate(gate(*vs)):
            cid = first + j
            assert original[cid] == clause
            db[cid] = clause; support[cid] = clause
        return tuple(range(first, first + 8))
    for node in trace:
        t, x, bit = node['t'], node['x'], node['value']
        key = (t, x); parents = [tuple(p) for p in node['parents']]
        assert 0 <= t <= 19 and abs(x - 10) <= 19-t and bit in (0, 1)
        assert key not in facts and all(p in facts for p in parents)
        literal = variables[key] * (1 if bit else -1)
        if node['rule'] == 'initial':
            assert t == 0 and not parents and -9 <= x <= 15
            cid = x + 87
            assert original[cid] == (literal,)
            db[cid] = (literal,); support[cid] = (literal,)
        elif node['rule'] == 'gate':
            assert all(pt == t-1 and abs(px-x) <= 1 for pt, px in parents)
            candidates = tuple(facts[p] for p in parents) + use_gate((t-1, x))
            cid = add((literal,), local_hints((literal,), candidates, db))
        elif node['rule'] == 'a10':
            assert parents == [(t-2, x-2), (t-2, x-1), (t-2, x)]
            assert db[facts[parents[0]]] == (variables[parents[0]] * (1 if bit else -1),)
            assert db[facts[parents[1]]] == (variables[parents[1]],)
            assert db[facts[parents[2]]] == (-variables[parents[2]],)
            assert 0 <= t-2 <= 81 and -84 <= x <= 97-(t-2)
            coords = [(t-2, x+i) for i in (-2, -1, 0, 1, 2)]
            coords += [(t-1, x+i) for i in (-1, 0, 1)] + [key]
            vm = dict(enumerate((variables[c] for c in coords), 1))
            cm = {}
            for k, g in enumerate(((t-2, x-1), (t-2, x), (t-2, x+1), (t-1, x))):
                for j, oid in enumerate(use_gate(g)):
                    cm[1+8*k+j] = oid
            for k, (clause, hints) in enumerate(ADDITIONS):
                translated = tuple(vm[abs(v)] * (1 if v > 0 else -1) for v in clause)
                cm[33+k] = add(translated, tuple(cm[h] for h in hints))
            cid = add((literal,), tuple(facts[p] for p in parents) + (cm[37 if bit else 38],))
        else:
            raise AssertionError('UNKNOWN_RULE')
        facts[key] = cid; node_ids.append({'t': t, 'x': x, 'id': cid})
    assert len(proof) == 539 and len(facts) == 234
    assert variables[19, 10] == 3459 and db[facts[19, 10]] == (3459,)
    leaves = [i for i, c in support.items() if len(c) == 1]
    assert sorted(leaves) == list(range(78, 103))
    assert original[95143] == (-3459,) and 95143 not in support
    assert all(h in support or h >= 95175 for _, _, hs in proof for h in hs)

    # Non-vacuity: one independent scalar completion models every root/gate
    # premise and has the predicted black target. No completion enumeration.
    model = {i: False for i in range(1, 12139)}
    row = {x: False for x in range(-9, 30)}
    for n in trace:
        if n['rule'] == 'initial': row[n['x']] = bool(n['value'])
    for t in range(20):
        for x, b in row.items(): model[variables[t, x]] = b
        if t < 19:
            row = {x: bool((int(row[x-1])+int(row[x])+int(row[x+1])+int(row[x])*int(row[x+1])) % 2)
                   for x in range(min(row)+1, max(row))}
    assert model[3459] and all(sat(c, model) for c in support.values())
    assert all(sat(c, model) for _, c, _ in proof)
    (OUT/'premise-model.json').write_text(json.dumps({str(k): int(v) for k, v in model.items()})+'\n')

    # Rewrite all original support IDs and all derived IDs into a standalone
    # root/gates query. The opposite target is its ONLY non-root unit.
    ids = sorted(support); remap = {oid: i+1 for i, oid in enumerate(ids)}
    opposite = len(ids)+1
    reduced = [support[i] for i in ids] + [(-3459,)]
    write_cnf(OUT/'root.cnf', 12138, reduced)
    rp = []
    for cid, clause, hints in proof:
        new = opposite+len(rp)+1
        remap[cid] = new
        rp.append((new, clause, tuple(remap[h] for h in hints)))
    rp.append((opposite+len(rp)+1, (), (remap[facts[19, 10]], opposite)))
    reduced_db = dict(enumerate(reduced, 1))
    for cid, clause, hints in rp:
        assert rup(clause, hints, reduced_db)
        reduced_db[cid] = clause
    (OUT/'root.lrat').write_text(''.join(line(*p) for p in rp))
    # Deliberately insufficient first hint: one parent unit cannot imply
    # the different cell literal. This must be rejected externally as well.
    bad = list(rp); cid, clause, hints = bad[0]
    bad[0] = (cid, clause, (hints[0],))
    assert not rup(clause, bad[0][2], dict(enumerate(reduced, 1)))
    (OUT/'root-bad.lrat').write_text(''.join(line(*p) for p in bad))
    db[95143] = original[95143]
    add((), (facts[19, 10], 95143))
    (OUT/'original.lrat').write_text(''.join(line(*p) for p in proof))
    (OUT/'support-map.json').write_text(json.dumps({'original_support_ids': ids, 'node_ids': node_ids,
                                                   'root_clause_remap': remap}, indent=2)+'\n')
    (OUT/'original.cnf').write_bytes(cnf_raw)
    write_cnf(OUT/'unit.cnf', 1, [(1,), (-1,)])
    (OUT/'unit-good.lrat').write_text('3 0 1 2 0\n')
    calls = [('unit-good', 'unit.cnf', 'unit-good.lrat', True),
             ('root-bad', 'root.cnf', 'root-bad.lrat', False),
             ('root-good', 'root.cnf', 'root.lrat', True),
             ('original-good', 'original.cnf', 'original.lrat', True)]
    for name, cnf, lrat, accept in calls:
        rc, text, reason = command(name, [CHECKER, '--CML_HEAP_SIZE=128', '--CML_STACK_SIZE=32',
                                        str(OUT/cnf), str(OUT/lrat)], 2, 6)
        assert reason == 'EXIT' and ('s VERIFIED UNSAT' in text) == accept, name
        if accept: assert rc == 0
    thermal()
    REPORT.update(status='ROOT_CONSEQUENCE_AND_ORIGINAL_CNF_LRAT_VERIFIED',
                  dag_nodes=234, root_leaves=25, a10_nodes=55, gate_nodes=154,
                  proof_additions=len(proof), used_original_gates=(len(ids)-25)//8,
                  support_clauses=len(ids), reduced_clauses=len(reduced), target=[19, 10, 1],
                  target_variable=3459, original_opposite_clause=95143,
                  premise_model='Single independent scalar completion satisfies all 25 root units and all used gates, and the positive target.',
                  controls='Good unit accepted; insufficient first hint rejected by independent ordered replay and cake_lpr; byte-exact gates and root-only dependency restriction checked.',
                  artifacts={p.name: {'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                             for p in sorted(OUT.iterdir()) if p.suffix in {'.cnf', '.lrat', '.json'}},
                  scope='One retained 25-cell finite consequence and a new proof of the already checked original CNF; no universal capture or proof-minimality claim.')
    save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error)); save(); raise
