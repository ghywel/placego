#!/usr/bin/env python3
"""GC2555: proof-only replay of Local's original L1453 CNF. NO solver run.

Reconstruct the exact DIMACS from translated phase/strip/path semantics,
then check the retained LRAT using cake_lpr and known good/bad controls.
A4_PROOF_INPUT holds the retained files; CAPPED_OUT is supplied by supervisor.
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
INPUT = Path(os.environ['A4_PROOF_INPUT'])
STOP = []
REPORT = {'status': 'STARTED', 'commands': []}
CHECKER = '/usr/local/bin/cake_lpr'
p = Path(__file__).parents[1] / 'ether_gap_solve.py'
assert hashlib.sha256(p.read_bytes()).hexdigest() == '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
names = {'save', 'cpu', 'thermal', 'command', 'check_proof'}
sel = [n for n in ast.parse(p.read_bytes()).body if isinstance(n, ast.FunctionDef) and n.name in names]
assert len(sel) == 5
exec(compile(ast.Module(body=sel, type_ignores=[]), str(p), 'exec'), globals())
TAB = (0, 1, 1, 1, 1, 0, 0, 0)


def main():
    os.nice(10)
    resource.setrlimit(resource.RLIMIT_CPU, (10, 30))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    pins = {'realize_p3.cnf': '902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9',
            'realize_p3.lrat': '22b62704bedf66342f392d28aee1049b0ab351c646228b6c2bed8f2759e427ca',
            'a4_s7_63_r0s4.json': '528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b',
            'emptying_word_p3_w16.json': '30dee77c511774708e64873b7272df4a4a31a8408ed53b110a8eab0cb81b2ece'}
    for name, pin in pins.items():
        assert hashlib.sha256((INPUT/name).read_bytes()).hexdigest() == pin
    assert hashlib.sha256(Path(CHECKER).read_bytes()).hexdigest() == '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'
    data = json.loads((INPUT/'a4_s7_63_r0s4.json').read_text())
    path = json.loads((INPUT/'emptying_word_p3_w16.json').read_text())
    assert path['start'] == [39, 0, '0011011100111010']
    assert len(path['path']) == 83 and len(path['word']) == 83
    orbit = data['orb']; strip = tuple(map(int, path['start'][2]))
    E = lambda t, x: orbit[(39 + t + 4) % 63][(t - x) % 7]
    # All coordinates are relative to Local's actual anchor. Lazy allocation
    # follows the exported DIMACS convention, independently of its absolute value.
    varmap = {}
    def var(t, x):
        if (t, x) not in varmap:
            varmap[t, x] = len(varmap) + 1
        return varmap[t, x]
    clauses = []
    for x in range(-86, 100):
        if x <= 16:
            bit = E(0, x) if x <= 0 else strip[x - 1]
            clauses.append((var(0, x) if bit else -var(0, x),))
    for t in range(83):
        for x in range(-85, 99 - t):
            a, b, c, d = var(t, x - 1), var(t, x), var(t, x + 1), var(t + 1, x)
            for j in range(8):
                ins = ((j >> 2) & 1, (j >> 1) & 1, j & 1)
                clause = tuple(-v if bit else v for v, bit in zip((a, b, c), ins))
                clauses.append(clause + ((d if TAB[j] else -d),))
        clauses.append((var(t + 1, -86) if E(t + 1, -86) else -var(t + 1, -86),))
    anchor = 0; active = []
    for t, (st, b, move) in enumerate(path['path']):
        if move == 0 and st[2][-1] == '0' or t == 82:
            # Last step has a null exported move; emptying is possible only
            # on a stay step, and the saved final strip has last bit0.
            if t == 82:
                assert move is None and st[2][-1] == '0'
            active.append((t, anchor + 17, b))
            clauses.append((var(t, anchor + 17) if b else -var(t, anchor + 17),))
        anchor += move or 0
    assert len(active) == 36
    assert len(varmap) == 12138 and len(clauses) == 95174
    rebuilt = OUT/'rebuilt-original.cnf'
    with rebuilt.open('w') as f:
        f.write('p cnf %d %d\n' % (len(varmap), len(clauses)))
        for clause in clauses:
            f.write(' '.join(map(str, clause)) + ' 0\n')
    assert rebuilt.read_bytes() == (INPUT/'realize_p3.cnf').read_bytes(), 'ORIGINAL_CNF_SEMANTICS_MISMATCH'
    REPORT.update(original_cnf_sha256=pins['realize_p3.cnf'], proof_sha256=pins['realize_p3.lrat'],
                  cnf_semantics='Byte-exact translated background/strip/eight-row gates/active inputs; boundary has right cone endpoint -3 at83, entirely within known background.',
                  variables=len(varmap), clauses=len(clauses), active_cells=active)
    # Verified checker controls; no SAT solver is invoked.
    unit = OUT/'unit.cnf'; unit.write_text('p cnf 1 2\n1 0\n-1 0\n')
    good = OUT/'good.lrat'; good.write_text('3 0 1 2 0\n')
    bad = OUT/'bad.lrat'; bad.write_text('3 0 1 1 0\n')
    empty = OUT/'empty.lrat'; empty.write_bytes(b'')
    check_proof('unit-good', unit, good, 1, 4)
    for name, proof in [('unit-bad', bad), ('unit-empty', empty)]:
        rc, text, reason = command(name, [CHECKER, '--CML_HEAP_SIZE=64', '--CML_STACK_SIZE=32', str(unit), str(proof)], 1, 4)
        assert reason == 'EXIT' and 's VERIFIED UNSAT' not in text
    check_proof('original-check', INPUT/'realize_p3.cnf', INPUT/'realize_p3.lrat', 15, 25)
    REPORT['status'] = 'ORIGINAL_CNF_BYTE_EXACT_AND_LRAT_VERIFIED_UNSAT'
    REPORT['controls'] = 'Known good proof verified, corrupted hint rejected, empty proof rejected; no solver run.'
    thermal(); save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error))
    save()
    raise
