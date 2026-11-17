#!/usr/bin/env python3
"""One fixed GC2614 host-binding test; no search, solver or original refutation.

Five declared placements, four outside placements, six metadata mutations;
one checker call on the primary placement's extracted gate-only query.
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
import types

OUT = Path(os.environ['CAPPED_OUT'])
STOP = []
REPORT = {'status': 'STARTED', 'commands': []}
CHECKER = '/usr/local/bin/cake_lpr'
EXPORT_SHA = 'a6f1a2a76f73c3cec9909de16db4c7c6724a9f54497fefbf0faff68ee1ed3387'


def pinned(path, sha):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == sha, 'INPUT_HASH_MISMATCH'
    return raw


helper = Path(__file__).parents[1] / 'ether_gap_solve.py'
raw = pinned(helper, '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d')
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in {'save', 'cpu', 'thermal', 'command'}]
assert len(nodes) == 4


class LowerBudget(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(10), node) if node.value == 95 else node


exec(compile(ast.fix_missing_locations(LowerBudget().visit(ast.Module(body=nodes, type_ignores=[]))), str(helper), 'exec'), globals())
primitive = Path(__file__).with_name('a10_gate_certificate.py')
raw = pinned(primitive, '2ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874')
names = {'rup', 'line', 'original_maps', 'write_cnf'}
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(nodes) == 4
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(primitive), 'exec'), globals())


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pinned(CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    module = types.ModuleType('strict_export')
    ep = Path(__file__).with_name('a4_six_guard_export.py')
    exec(compile(pinned(ep, EXPORT_SHA), str(ep), 'exec'), module.__dict__)
    # Ensure the copied proof template is exactly the already checked template.
    oldp = Path(__file__).with_name('a4_six_guard_certificate.py')
    oldraw = pinned(oldp, 'ded529abe6946ee7766d9c5dd452d3cb4ce50daee67d983e2cff498f3b57c4bc')
    names = {'COORDS', 'GATE_COORDS', 'H', 'ADDITIONS'}
    nodes = [n for n in ast.parse(oldraw).body if isinstance(n, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id in names for t in n.targets)]
    assert len(nodes) == 4
    old = {};exec(compile(ast.Module(body=nodes, type_ignores=[]), str(oldp), 'exec'), old)
    assert all(old[k] == getattr(module, k) for k in names)
    raw = pinned(os.environ['SIX_HOST_CNF'], '902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9')
    lines = raw.decode().splitlines(); assert lines[0] == 'p cnf 12138 95174'
    host = {}
    for i, row in enumerate(lines[1:], 1):
        ls = tuple(map(int, row.split()));assert ls[-1] == 0 and 0 not in ls[:-1]
        host[i] = ls[:-1]
    assert len(host) == 95174
    cells, gates = original_maps()
    gate_rows = {key: tuple(range(value[0], value[0]+8)) for key, value in gates.items()}
    accepted = []
    for t, x in [(0, 11), (0, -86), (0, 91), (79, -86), (79, 12)]:
        result = module.export(host, cells, gate_rows, t, x)
        db = {i: host[i] for i in result['support_ids']}
        assert len(db) == 112 and all(len(c) == 4 for c in db.values())
        for cid, clause, hints in result['proof']:
            assert cid not in db and rup(clause, hints, db)
            db[cid] = clause
        expected = tuple(cells[t, x+j] * sign for j, sign in enumerate((-1, -1, -1, 1, -1, -1))) + (cells[t+4, x+4],)
        assert result['clause'] == expected
        accepted.append(result)
    rejected = []
    def reject(name, h, c, g, t, x, first=None):
        try:
            module.export(h, c, g, t, x, first)
        except module.Unsupported as error:
            rejected.append({'case': name, 'reason': str(error)})
        else:
            raise AssertionError('BAD_PLACEMENT_ACCEPTED:' + name)
    for t, x in [(-1, 11), (80, 0), (0, -87), (0, 92)]:
        reject('outside_%d_%d' % (t, x), host, cells, gate_rows, t, x)
    alias = dict(cells);alias[0, 11] = alias[0, 12]
    reject('alias', host, alias, gate_rows, 0, 11)
    negative = dict(cells);negative[0, 11] *= -1
    reject('negative_variable', host, negative, gate_rows, 0, 11)
    wrong = dict(host);first = gate_rows[0, 12][0];c = wrong[first]
    wrong[first] = (-c[0],) + c[1:]
    reject('wrong_gate_sign', wrong, cells, gate_rows, 0, 11)
    missing = dict(gate_rows);missing[0, 12] = missing[0, 12][:-1]
    reject('missing_truth_row', host, cells, missing, 0, 11)
    borrowed = dict(gate_rows);borrowed[0, 12] = (1,) + borrowed[0, 12][1:]
    reject('borrowed_root_unit', host, cells, borrowed, 0, 11)
    reject('addition_id_collision', host, cells, gate_rows, 0, 11, max(host))
    # The host's actual root does not supply the sixth antecedent bit.
    primary = accepted[0]
    root_units = {abs(c[0]): c[0] > 0 for i, c in host.items() if i <= 103}
    actual = ''.join(str(int(root_units[cells[0, 11+j]])) for j in range(6))
    assert actual == '111010'
    # Compress only the byte-matched gate subset, not the already-UNSAT host.
    ids = primary['support_ids'];query = [host[i] for i in ids] + [(-v,) for v in primary['clause']]
    remap = {old: new for new, old in enumerate(ids, 1)}
    restricted = {i: query[i-1] for i in range(1, 113)}
    proof = []
    for oldid, clause, hints in primary['proof']:
        new = len(query) + len(proof) + 1
        hs = tuple(remap[h] for h in hints)
        assert rup(clause, hs, restricted)
        remap[oldid] = new;restricted[new] = clause;proof.append((new, clause, hs))
    final = (len(query)+len(proof)+1, (), tuple(range(113, 120)) + (proof[-1][0],))
    assert rup(final[1], final[2], {**dict(enumerate(query, 1)), **restricted})
    write_cnf(OUT/'mapped.cnf', 12138, query)
    (OUT/'mapped.lrat').write_text(''.join(line(*p) for p in proof+[final]))
    (OUT/'original-id-prefix.lrat').write_text(''.join(line(*p) for p in primary['proof']))
    REPORT.update(placements=accepted, rejected=rejected, actual_root_word=actual,
                  full_host_refutation='NOT RUN; original-CNF result not used as a checker shortcut')
    save()
    rc, txt, why = command('mapped-good', [CHECKER, '--CML_HEAP_SIZE=128', '--CML_STACK_SIZE=32',
                                         str(OUT/'mapped.cnf'), str(OUT/'mapped.lrat')], 2, 5)
    assert why == 'EXIT' and rc == 0 and 's VERIFIED UNSAT' in txt
    REPORT.update(status='PASS', scope='Five fixed bindings and10 rejection controls; primary gate-only mapped implication certified; no new original-path exclusion')
    save()


try:
    main()
except BaseException as e:
    REPORT.update(status='FAILED', error=repr(e));save();raise
