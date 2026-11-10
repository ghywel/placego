#!/usr/bin/env python3
"""GC2859: one retained original-CNF proof export, no SAT enumeration/search sweep."""
import ast
import hashlib
import json
import os
from pathlib import Path
import resource
import signal

OUT = Path(os.environ['CAPPED_OUT'])
ROOT = Path(__file__).resolve().parents[5]
STOP = []
REPORT = {'status': 'STARTED', 'commands': []}
CADICAL = '/usr/local/bin/cadical'
CHECKER = '/usr/local/bin/cake_lpr'
LRAT_CHECK = '/usr/local/bin/lrat-check'

# Already exercised sequential external-command guard: counts reaped children AND
# the sole live computational child, with its own95CPU aggregate stop. The enclosing
# stage additionally counts itself and the outer resource/thermal monitor.
helper = ROOT/'tests/probes/ether_gap_solve.py'
raw = helper.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
names = {'save', 'cpu', 'thermal', 'command'}
nodes = [n for n in ast.parse(raw).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(nodes) == 4
# The imported functions use these globals; no old experiment or helper main runs.
import re
import subprocess
import time
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(helper), 'exec'), globals())


def cpu():
    # The helper's direct live solver is added by command(). Here also include the
    # enclosing Python stage's own live CPU and the outer monitor's reaped CPU.
    # Neither ancestor has reaped this worker while it is executing this function.
    ancestor = subprocess.run(['ps', '-p', str(os.getppid()), '-o', 'time='],
                              capture_output=True, text=True, timeout=3)
    fields = ancestor.stdout.strip().split(':')
    assert ancestor.returncode == 0 and len(fields) == 2, 'ANCESTOR_CPU_MONITOR_FAILURE'
    parent_cpu = 60*int(fields[0])+float(fields[1])
    monitor = json.loads(Path(os.environ['CAPPED_MONITOR_CPU_FILE']).read_text())
    assert time.time()-monitor['at'] < 10, 'STALE_MONITOR_CPU'
    own = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return (own.ru_utime+own.ru_stime+children.ru_utime+children.ru_stime+
            parent_cpu+monitor['cpu_s'])


def call(name, args, cpu_cap, wall_cap, expect=None):
    rc, text, why = command(name, args, cpu_cap, wall_cap)
    assert why == 'EXIT', (name, rc, why)
    if expect is not None:
        assert rc == expect, (name, rc, text[-2000:])
    return rc, text


def cake(name, cnf, proof, accepted, cpu_cap=2, wall_cap=5):
    rc, text = call(name, [CHECKER, '--CML_HEAP_SIZE=256', '--CML_STACK_SIZE=64',
                           str(cnf), str(proof)], cpu_cap, wall_cap)
    assert ('s VERIFIED UNSAT' in text) == accepted, (name, rc, text[-2000:])
    if accepted:
        assert rc == 0


def literal_mask(clause):
    return sum(1 << (2*(abs(l)-1) + int(l > 0)) for l in set(clause))


def audit_rup(cnf, lrat):
    """Replay the used positive LRAT cone, then AUDIT packed bounds before encoding."""
    original = []
    for line in cnf.read_text().splitlines():
        if line.startswith(('c', 'p')):
            continue
        ns = list(map(int, line.split()))
        assert ns[-1] == 0 and 0 not in ns[:-1]
        original.append(ns[:-1])
    db = dict(enumerate(original, 1))
    hints = {}
    order = []
    empty = None
    deletions = 0
    for line in lrat.read_text().splitlines():
        ns = line.split()
        if not ns:
            continue
        cid = int(ns[0])
        if ns[1] == 'd':
            deletions += 1
            continue
        rest = list(map(int, ns[1:])); z = rest.index(0)
        assert rest[-1] == 0 and cid not in db
        db[cid] = rest[:z]; hints[cid] = rest[z+1:-1]; order.append(cid)
        if not db[cid]:
            empty = cid
    assert empty is not None
    needed = set()
    todo = [empty]
    while todo:
        cid = todo.pop()
        if cid <= len(original) or cid in needed:
            continue
        needed.add(cid)
        if any(h <= 0 for h in hints[cid]):
            return {'packable': False, 'reason': 'USED_RAT_NOT_PLAIN_RUP',
                    'original_clauses': len(original), 'lrat_additions': len(order)}
        assert all(h in db and h < cid for h in hints[cid])
        todo.extend(hints[cid])
    used = [cid for cid in order if cid in needed]
    remap = {i: i-1 for i in range(1, len(original)+1)}
    remap.update({cid: len(original)+i for i, cid in enumerate(used)})
    masks = [literal_mask(c) for c in original]
    steps = []
    max_hint = max_literal = max_chain = 0
    for cid in used:
        clause = db[cid]
        assigned = {abs(l): l < 0 for l in clause}
        assert len(assigned) == len(clause), 'DUPLICATE_OR_TAUTOLOGICAL_CLAUSE'
        units = []
        conflict = None
        for h in hints[cid]:
            source = db[h]
            assert not any(assigned.get(abs(l)) == (l > 0) for l in source), 'SATISFIED_HINT'
            unset = [l for l in source if abs(l) not in assigned]
            if not unset:
                conflict = remap[h]
                break
            assert len(unset) == 1, 'NONUNIT_HINT'
            u = unset[0]
            units.append((remap[h], 2*(abs(u)-1)+int(u > 0)))
            assigned[abs(u)] = u > 0
        assert conflict is not None, 'NO_RUP_CONFLICT'
        assert all(h < remap[cid] for h, _ in units) and conflict < remap[cid]
        max_hint = max(max_hint, conflict, *(h for h, _ in units))
        max_literal = max([max_literal]+[u for _, u in units]+
                          [2*(abs(l)-1)+int(l > 0) for l in clause])
        max_chain = max(max_chain, len(units))
        masks.append(literal_mask(clause))
        steps.append((conflict, units))
    packable = max_hint < 2**14 and max_literal < 2**11 and max_chain < 2**10
    result = {'packable': packable, 'original_clauses': len(original),
              'lrat_additions': len(order), 'deletions': deletions,
              'used_additions': len(used), 'max_hint': max_hint,
              'max_literal': max_literal, 'max_unit_chain': max_chain,
              'final_empty_index': remap[empty], 'python_rup_replayed': True}
    if packable:
        packed = []
        for conflict, units in steps:
            data = conflict | (len(units) << 14)
            for j, (h, u) in enumerate(units):
                data |= (h | (u << 14)) << (24+25*j)
            packed.append(data)
        # Every decoded packed step is replayed against actual literal masks too.
        for i, data in enumerate(packed):
            bound = len(original)+i
            conflict = data & 0x3fff
            count = (data >> 14) & 0x3ff
            trail = data >> 24
            xs = masks[bound]
            for _ in range(count):
                h = trail & 0x3fff; u = (trail >> 14) & 0x7ff
                assert h < bound and masks[h] & (xs | (1 << u)) == masks[h]
                xs |= 1 << (u ^ 1); trail >>= 25
            assert conflict < bound and masks[conflict] & xs == masks[conflict]
        assert masks[-1] == 0 and remap[empty] == len(masks)-1
        # Decimal Python limits are irrelevant to the Lean binary natural encoding.
        (OUT/'packed-rup.json').write_text(json.dumps({'masks_hex': [hex(m) for m in masks],
            'steps_hex': [hex(p) for p in packed], 'original_cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest()}, indent=2)+'\n')
    return result


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 20))
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda s, f: STOP.append(s))
    for path, sha in [(CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                      (CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                      (LRAT_CHECK, '87429b8c50afdba643e83ea6ab712d36f49d5e4f47f488bd5d9ebc332bd204f1')]:
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha
    target = Path(os.environ['RETURN13_ORIGINAL_CNF'])
    raw = target.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == 'badadbb38e00fb0c01991563f3fb6664ed2b78c9ab7254a36fa1bd818313fcd0'
    assert raw.startswith(b'p cnf 910 5214\n')
    (OUT/'original.cnf').write_bytes(raw)
    thermal()
    (OUT/'unit.cnf').write_text('p cnf 1 2\n1 0\n-1 0\n')
    (OUT/'sat.cnf').write_text('p cnf 1 1\n1 0\n')
    (OUT/'good.lrat').write_text('3 0 1 2 0\n')
    (OUT/'bad.lrat').write_text('3 0 1 1 0\n')
    (OUT/'empty.lrat').write_text('')
    call('sat-control', [CADICAL, '-q', str(OUT/'sat.cnf')], 1, 3, 10)
    call('unsat-control', [CADICAL, '--lrat', '--no-binary', '-q',
                          str(OUT/'unit.cnf'), str(OUT/'unit.lrat')], 1, 3, 20)
    cake('unit-good', OUT/'unit.cnf', OUT/'unit.lrat', True)
    cake('unit-bad', OUT/'unit.cnf', OUT/'bad.lrat', False)
    cake('unit-empty', OUT/'unit.cnf', OUT/'empty.lrat', False)
    REPORT['controls'] = 'SAT, generated UNSAT accepted, corrupt hint rejected, empty rejected'
    save()
    call('target-solve', [CADICAL, '--lrat', '--no-binary', '-q',
                         str(OUT/'original.cnf'), str(OUT/'original.lrat')], 45, 100, 20)
    cake('target-cake', OUT/'original.cnf', OUT/'original.lrat', True, 15, 40)
    _, text = call('target-lrat-check', [LRAT_CHECK, str(OUT/'original.cnf'),
                                        str(OUT/'original.lrat')], 10, 30, 0)
    assert 'VERIFIED' in text
    REPORT['finite_cnf'] = 'ORIGINAL_CNF_LRAT_CHECKED_UNSAT'
    REPORT['rup_audit'] = audit_rup(OUT/'original.cnf', OUT/'original.lrat')
    REPORT['status'] = 'CERTIFIED_FINITE_CNF_AND_PACKING_AUDITED'
    REPORT['sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in OUT.iterdir() if p.suffix in ['.cnf', '.lrat']}
    thermal(); save()
    print('RETURN13_LRAT_STAGE_RECORDED', flush=True)


if __name__ == '__main__':
    try:
        main()
    finally:
        save()
