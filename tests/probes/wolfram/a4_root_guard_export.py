#!/usr/bin/env python3
"""GC2590: discharge the fixed root units in the retained positive-RUP proof.

No new trace, closure, solver or root search. Export one 26-literal clause
with an original-gate-only proof prefix; certify its two fixed compositions.
"""
import ast
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
INPUT = Path(os.environ['GUARD_INPUT'])
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
        return ast.copy_location(ast.Constant(20), node) if node.value == 95 else node
exec(compile(ast.fix_missing_locations(LowerBudget().visit(ast.Module(body=nodes, type_ignores=[]))), str(helper), 'exec'), globals())

for filename, sha, names in [
    ('a10_gate_certificate.py', '2ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874', {'rup', 'line', 'write_cnf', 'sat'}),
    ('a4_root_lrat_compile.py', '2e827139bdee0e79d8f217b6eefa93a336982b527f123f8a20f524b777c06a81', {'local_hints'}),
]:
    path = Path(__file__).with_name(filename)
    nodes = [n for n in ast.parse(pinned(path, sha)).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert len(nodes) == len(names)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), globals())


def parse_proof(raw):
    proof = []
    for row in raw.decode().splitlines():
        ns = tuple(map(int, row.split())); z = ns.index(0)
        assert ns[-1] == 0 and ns.count(0) == 2 and z >= 1
        cid, clause, hints = ns[0], ns[1:z], ns[z+1:-1]
        assert cid > 0 and all(0 < h < cid for h in hints)
        proof.append((cid, clause, hints))
    return proof


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (6, 6))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pinned(CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    thermal()
    # Extra root assumptions can satisfy an old hint. Regeneration must skip it.
    toy = {1: (-1, 2), 2: (-2, 3)}
    assert not rup((-1, -2, 3), (1, 2), toy)
    assert local_hints((-1, -2, 3), (1, 2), toy) == (2,)
    assert rup((-1, -2, 3), (2,), toy)
    original_raw = pinned(INPUT/'original.cnf', '902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9')
    rows = original_raw.decode().splitlines()
    assert rows[0] == 'p cnf 12138 95174'
    original = {}
    for i, row in enumerate(rows[1:], 1):
        ns = tuple(map(int, row.split())); assert ns[-1] == 0 and 0 not in ns[:-1]
        original[i] = ns[:-1]
    assert len(original) == 95174
    old = parse_proof(pinned(INPUT/'original.lrat', '044e2d2295ca3616bf98c0e7441960af10559586fdabdc2a0190c8fece7f5d48'))
    assert len(old) == 540 and [p[0] for p in old] == list(range(95175, 95715))
    assert old[-2][1] == (3459,) and old[-1] == (95714, (), (95713, 95143))
    inventory = json.loads(pinned(INPUT/'support-map.json', 'dfe0609bd5468507fc1d440286869fcff3156925bc51b882ba86d43a5e9fe295'))
    support_ids = inventory['original_support_ids']
    roots = set(range(78, 103)); gates = set(support_ids)-roots
    assert len(support_ids) == 1857 and roots <= set(support_ids)
    assert all(len(original[h]) == 4 for h in gates)
    assert all(len(original[h]) == 1 for h in roots)
    guard = tuple(-original[h][0] for h in sorted(roots))
    assert len(set(map(abs, guard))) == 25 and 3459 not in map(abs, guard)
    db = {h: original[h] for h in gates}
    prefix = []; guarded = 0; omitted = 0; hint_changes = 0
    for cid, clause, hints in old[:-1]:
        assert all(h in roots or h in db for h in hints)
        if len(clause) == 1:
            guarded += 1
            target = guard + clause
            candidates = tuple(h for h in hints if h not in roots)
            omitted += len(hints)-len(candidates)
            hs = local_hints(target, candidates, db)
            hint_changes += hs != candidates
        else:
            assert len(clause) in (3, 4) and all(h not in roots for h in hints)
            target, hs = clause, hints
        assert cid not in db and rup(target, hs, db), ('BAD_GUARDED_STEP', cid)
        db[cid] = target; prefix.append((cid, target, hs))
    assert guarded == 209 and len(prefix) == 539 and prefix[-1][1] == guard+(3459,)
    assert all(h in gates or 95175 <= h < cid for cid, _, hs in prefix for h in hs)
    # A root hint is forbidden even if the host CNF happens to contain it.
    try: rup(prefix[0][1], (79,), {h: original[h] for h in gates})
    except AssertionError: pass
    else: raise AssertionError('ROOT_DEPENDENCY_NOT_REJECTED')
    # Dropping the entire antecedent would assert an untrue unconditional bit.
    all_white = dict.fromkeys(range(1, 12139), False)
    assert all(sat(original[h], all_white) for h in gates)
    assert not sat((3459,), all_white) and sat(prefix[-1][1], all_white)
    (OUT/'guarded-prefix.lrat').write_text(''.join(line(*p) for p in prefix))
    (OUT/'guarded-clause.json').write_text(json.dumps({'clause': prefix[-1][1], 'id': 95713,
                                                    'root_ids_disallowed': sorted(roots), 'original_gate_ids': sorted(gates)}, indent=2)+'\n')
    # Compose with the unchanged original CNF, using root/path units ONLY here.
    final_hints = tuple(sorted(roots)) + (95143, 95713)
    full_db = {**original, **db}
    assert rup((), final_hints, full_db)
    (OUT/'original.lrat').write_text(''.join(line(*p) for p in prefix)+line(95714, (), final_hints))
    (OUT/'original.cnf').write_bytes(original_raw)
    # Separate implication query: gates + negated clause (25 roots, negative bit).
    ids = sorted(gates)
    reduced = [original[h] for h in ids] + [(original[h][0],) for h in sorted(roots)] + [(-3459,)]
    n = len(reduced); assert n == 1858
    remap = {h: i+1 for i, h in enumerate(ids)}; rp = []
    rdb = dict(enumerate(reduced, 1))
    for cid, clause, hints in prefix:
        new = n+len(rp)+1; remap[cid] = new
        hs = tuple(remap[h] for h in hints)
        # Restricted replay still excludes every root/negative-target input.
        allowed = {i: c for i, c in rdb.items() if i <= len(gates) or i > n}
        assert rup(clause, hs, allowed)
        rp.append((new, clause, hs)); rdb[new] = clause
    final = (n+len(rp)+1, (), tuple(range(len(gates)+1, n+1)) + (remap[95713],))
    assert rup(final[1], final[2], rdb); rp.append(final)
    write_cnf(OUT/'implication.cnf', 12138, reduced)
    (OUT/'implication.lrat').write_text(''.join(line(*p) for p in rp))
    bad = list(rp); bad[0] = (bad[0][0], bad[0][1], ())
    assert not rup(bad[0][1], bad[0][2], rdb)
    (OUT/'bad.lrat').write_text(''.join(line(*p) for p in bad))
    write_cnf(OUT/'unit.cnf', 1, [(1,), (-1,)])
    (OUT/'unit.lrat').write_text('3 0 1 2 0\n')
    calls = [('unit-good', 'unit.cnf', 'unit.lrat', True),
             ('guard-bad', 'implication.cnf', 'bad.lrat', False),
             ('guard-good', 'implication.cnf', 'implication.lrat', True),
             ('original-good', 'original.cnf', 'original.lrat', True)]
    for name, cnf, proof, accept in calls:
        rc, text, reason = command(name, [CHECKER, '--CML_HEAP_SIZE=128', '--CML_STACK_SIZE=32',
                                        str(OUT/cnf), str(OUT/proof)], 2, 6)
        assert reason == 'EXIT' and ('s VERIFIED UNSAT' in text) == accept, name
        if accept: assert rc == 0
    thermal()
    REPORT.update(status='GUARDED_IMPLICATION_GATE_ONLY_PREFIX_CHECKED',
                  guarded_units=guarded, unchanged_gate_lemmas=330, prefix_additions=539,
                  original_gates=229, implication_literals=26, omitted_root_hints=omitted,
                  regenerated_hint_lists_changed=hint_changes,
                  controls='Satisfied-hint toy, forbidden-root hint, all-white countermodel to unconditional target, corrupted prefix rejected, positive checker control.',
                  scope='One pinned original-variable/clause embedding. Prefix uses gates only; no general translator, minimality, Lean verification or universal capture claim.',
                  artifacts={p.name: {'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                             for p in sorted(OUT.iterdir()) if p.suffix in {'.cnf', '.lrat', '.json'} and p.name != 'solve.json'})
    save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error)); save(); raise
