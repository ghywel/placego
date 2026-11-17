#!/usr/bin/env python3
"""GC2553: ONE fixed whole-row extension test for the retained83-step cylinder.

A4_DATA63 and A4_EMPTYING locate SHA-pinned inputs. No target/horizon knobs.
run_capped.py supplies CAPPED_OUT. Known single-process tool controls and
aggregate/thermal monitoring are imported from the previously pinned driver.
"""
import ast
import builtins
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import subprocess
import symtable
import time

OUT = Path(os.environ['CAPPED_OUT'])
STOP = []
REPORT = {'status': 'STARTED', 'commands': []}
CADICAL = '/usr/local/bin/cadical'
CHECKER = '/usr/local/bin/cake_lpr'
HELPER = Path(__file__).parents[1] / 'ether_gap_solve.py'
assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
names = {'save', 'cpu', 'thermal', 'command', 'check_proof', 'parse_model', 'solve'}
selected = [n for n in ast.parse(HELPER.read_bytes()).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(selected) == 7
exec(compile(ast.Module(body=selected, type_ignores=[]), str(HELPER), 'exec'), globals())
# Reused helper dependencies must all exist before any tool process starts.
def missing(namespace):
    table = symtable.symtable(ast.unparse(ast.Module(body=selected, type_ignores=[])), str(HELPER), 'exec')
    absent = set()
    def walk(scope):
        for s in scope.get_symbols():
            if s.is_referenced() and s.is_global() and s.get_name() not in namespace and not hasattr(builtins, s.get_name()):
                absent.add(s.get_name())
        for child in scope.get_children():
            walk(child)
    walk(table)
    return absent
assert missing(globals()) == set()
assert missing({k: v for k, v in globals().items() if k != 're'}) == {'re'}

RULE = (0, 1, 1, 1, 1, 0, 0, 0)
H, LEFT, RIGHT = 83, -166, 99


def gate(a, b, c, d):
    clauses = []
    for j in range(8):
        bits = ((j >> 2) & 1, (j >> 1) & 1, j & 1)
        clauses.append(tuple(-v if bit else v for v, bit in zip((a, b, c), bits)) +
                       ((d if RULE[j] else -d),))
    return clauses


def satisfied(clause, model):
    return any(model[abs(lit)] == (lit > 0) for lit in clause)


def write_cnf(path, nv, clauses):
    with path.open('w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for clause in clauses:
            f.write(' '.join(map(str, clause)) + ' 0\n')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (20, 90))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pins = {'A4_DATA63': '528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b',
            'A4_EMPTYING': '30dee77c511774708e64873b7272df4a4a31a8408ed53b110a8eab0cb81b2ece'}
    inputs = {}
    for k, pin in pins.items():
        raw = Path(os.environ[k]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == pin
        inputs[k] = json.loads(raw)
    for binary, pin in [(CADICAL, '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                        (CHECKER, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')]:
        assert hashlib.sha256(Path(binary).read_bytes()).hexdigest() == pin
    data, saved = inputs['A4_DATA63'], inputs['A4_EMPTYING']
    assert (data['N'], data['q'], data['W'], data['r'], data['s']) == (7, 63, 16, 0, 4)
    assert (saved['T0'], saved['pattern'], saved['W'], saved['start']) == (3000, 3, 16, [39, 0, '0011011100111010'])
    assert len(saved['word']) == len(saved['path']) == H
    orb = data['orb']
    assert len(orb) == 63 and all(len(r) == 7 and set(r) <= {0, 1} for r in orb)
    for t in range(63):
        for j in range(7):
            assert orb[(t + 1) % 63][j] == RULE[4 * orb[t][j] + 2 * orb[t][(j - 1) % 7] + orb[t][(j - 2) % 7]]
    # Relative to the saved anchor: dq0=0, local time0 has global tq39.
    E = lambda t, x: orb[(39 + t + 4) % 63][(t - x) % 7]
    initial_strip = tuple(map(int, saved['start'][2]))

    def step(st, b):
        tq, dq, bits = st
        ref = lambda dt, i: orb[(tq + dt + 4) % 63][(dq + dt - i) % 7]
        cell = lambda i: ref(0, i) if i <= 0 else (bits[i - 1] if i <= 16 else b)
        new = tuple(RULE[4 * cell(i - 1) + 2 * cell(i) + cell(i + 1)] for i in range(17))
        mv = -int(new[0] != ref(1, 0))
        strip = new[:16] if mv else new[1:]
        ndq = (dq + 1 - mv) % 7
        nxt = ((tq + 1) % 63, ndq, strip)
        alive = any(v != orb[(nxt[0] + 4) % 63][(ndq - i) % 7] for i, v in enumerate(strip, 1))
        return nxt, mv, alive

    dec = lambda st: (st[0], st[1], tuple(map(int, st[2])))
    st = dec(saved['start']); anchor = 0; active = []; anchors = []; mask = []
    for t, (raw_st, b, mv) in enumerate(saved['path']):
        assert st == dec(raw_st) and b == saved['word'][t]
        s0, s1 = step(st, 0), step(st, 1)
        nxt, move, alive = step(st, b)
        assert (s0 != s1) == (move == 0 and st[2][-1] == 0)
        assert mv == move if t < H - 1 else mv is None
        assert alive == (t < H - 1)
        anchors.append(anchor)
        if s0 != s1:
            active.append((t, anchor + 17, b)); mask.append(str(b))
        else:
            mask.append('*')
        st = nxt; anchor += move
    assert mask[:6] == ['*'] * 6 and active[0][0] == 6 and len(active) == 36
    terminal_anchor = anchor
    REPORT['path_audit'] = {'active_reads': len(active), 'masked_word': ''.join(mask),
                            'terminal_anchor': anchor, 'first_active': active[0], 'active_cells': active}

    # Verify all16 input/output truth-table assignments for the CNF gate.
    for j in range(16):
        bits = bytearray([0] + [(j >> i) & 1 for i in range(4)])
        expected = bits[4] == RULE[4 * bits[1] + 2 * bits[2] + bits[3]]
        assert all(satisfied(c, bits) for c in gate(1, 2, 3, 4)) == expected
    # Clause-construction corruption is rejected by a planted000->0 assignment.
    g = gate(1, 2, 3, 4)
    wrong = [(1, 2, 3, 4)] + g[1:]
    assert all(satisfied(c, bytearray(5)) for c in g)
    assert not all(satisfied(c, bytearray(5)) for c in wrong)

    variables = {}; rows = []; nv = 0
    for t in range(H + 1):
        xs = range(LEFT + t, RIGHT - t + 1); rows.append(xs)
        for x in xs:
            nv += 1; variables[t, x] = nv
    clauses = []
    for t in range(H):
        for x in rows[t + 1]:
            clauses.extend(gate(variables[t, x - 1], variables[t, x], variables[t, x + 1], variables[t + 1, x]))
    for x in range(LEFT, 17):
        value = E(0, x) if x <= 0 else initial_strip[x - 1]
        clauses.append((variables[0, x] if value else -variables[0, x],))
    # A planted whole-row extension checks the ENTIRE unguarded circuit.
    planted = bytearray(nv + 1)
    first = {x: E(0, x) if x <= 0 else (initial_strip[x - 1] if x <= 16 else 0) for x in rows[0]}
    current = first
    for t in range(H + 1):
        for x, v in current.items():
            planted[variables[t, x]] = v
        if t < H:
            current = {x: RULE[4 * current[x - 1] + 2 * current[x] + current[x + 1]] for x in rows[t + 1]}
    assert all(satisfied(c, planted) for c in clauses)
    REPORT['base_cnf_sha256'] = write_cnf(OUT/'base.cnf', nv, clauses)
    # Only active digits are forced; no arbitrary canonical zeros are imposed.
    for t, x, b in active:
        assert (t, x) in variables
        clauses.append((variables[t, x] if b else -variables[t, x],))
    # Terminal equality is an implied consequence, checked rather than assumed:
    # it is not added as a unit, so UNSAT certifies the original active cylinder.
    cnf = OUT/'cylinder.cnf'
    assert nv == 15372 and len(clauses) == 121067
    REPORT.update(input_sha256=pins, variables=nv, clauses=len(clauses),
                  cnf_sha256=write_cnf(cnf, nv, clauses), initial_unknown_cells=[17, 99])
    save()

    # Solver/checker known-answer controls, with a rejected empty proof.
    micro = gate(1, 2, 3, 4) + [(1,), (-2,), (3,)]
    write_cnf(OUT/'micro-sat.cnf', 4, micro + [(-4,)])
    status, text, _ = solve('micro-sat', OUT/'micro-sat.cnf', 1, 4)
    assert status == 'SAT'
    witness = parse_model(text, 4)
    assert all(satisfied(c, witness) for c in micro + [(-4,)])
    write_cnf(OUT/'micro-unsat.cnf', 4, micro + [(4,)])
    status, _, proof = solve('micro-unsat', OUT/'micro-unsat.cnf', 1, 4)
    assert status == 'UNSAT'
    check_proof('micro-check', OUT/'micro-unsat.cnf', proof, 1, 4)
    empty = OUT/'empty.lrat'; empty.write_bytes(b'')
    rc, text, reason = command('reject-empty', [CHECKER, '--CML_HEAP_SIZE=64', '--CML_STACK_SIZE=32', str(OUT/'micro-unsat.cnf'), str(empty)], 1, 4)
    assert reason == 'EXIT' and 's VERIFIED UNSAT' not in text and 'empty clause not derived' in text
    REPORT['controls'] = '16 gate assignments, corrupted gate rejected, full planted base replay, micro SAT model, checked micro UNSAT, empty proof rejected'
    status, text, proof = solve('original', cnf, 45, 65)
    REPORT['original_status'] = status
    if status == 'SAT':
        model = parse_model(text, nv)
        assert all(satisfied(c, model) for c in clauses)
        free = {x: model[variables[0, x]] for x in range(17, 100)}
        # Wider whole-row replay uses the XOR/OR formula, not the CNF truth table.
        left, right = -200, 200
        physical = {x: E(0, x) if x <= 0 else (initial_strip[x - 1] if x <= 16 else free.get(x, E(0, x))) for x in range(left, right + 1)}
        trace = []; a = 0
        for t in range(H + 1):
            assert all(physical[x] == model[variables[t, x]] for x in rows[t])
            assert all(physical[x] == E(t, x) for x in range(left + t + 1, a + 1))
            if t < H:
                assert tuple(physical[a + i] for i in range(1, 17)) == dec(saved['path'][t][0])[2]
                incoming = physical[a + 17]
                if mask[t] != '*':
                    assert incoming == int(mask[t])
                trace.append({'t': t, 'anchor': a, 'incoming': incoming, 'active': mask[t] != '*'})
                movement = -int((physical[a - 1] ^ (physical[a] | physical[a + 1])) != E(t + 1, a))
                a += movement
                physical = {x: physical[x - 1] ^ (physical[x] | physical[x + 1]) for x in range(left + t + 1, right - t)}
            else:
                assert a == terminal_anchor
                assert all(physical[a + i] == E(t, a + i) for i in range(1, 17))
        bits = ''.join(map(str, (free[x] for x in range(17, 100))))
        (OUT/'extension-witness.json').write_text(json.dumps({'relative_initial_free_range': [17, 99], 'bits': bits,
            'outside_right': 'phase-correct background', 'known_strip': saved['start'][2], 'trace': trace,
            'terminal_anchor': a, 'terminal_time': H, 'scope': 'Local whole-row extension only, not width12 time0 reachability.'}, indent=2) + '\n')
        REPORT['witness_sha256'] = hashlib.sha256((OUT/'extension-witness.json').read_bytes()).hexdigest()
        REPORT['status'] = 'SAT_WHOLE_ROW_EXTENSION_REPLAYED'
    elif status == 'UNSAT':
        check_proof('original-check', cnf, proof, 25, 45)
        REPORT.update(status='ORIGINAL_CYLINDER_LRAT_CHECKED_UNSAT', proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(), proof_bytes=proof.stat().st_size)
    else:
        REPORT['status'] = 'UNKNOWN_UNDER_FROZEN_CAPS'
    thermal(); save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error))
    save()
    raise
