#!/usr/bin/env python3
"""GC2559: two retained L1454 proofs, original-CNF audit and bounded FIFO replay.

NO solver. A4_ROBUST_INPUT locates four gzip inputs; A4_DATA63 the pinned
background. Uses a separately controlled packed row to reconstruct bands.
"""
import ast
import gc
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import shutil
import signal
import subprocess
import threading
import time

OUT = Path(os.environ['CAPPED_OUT'])
INPUT = Path(os.environ['A4_ROBUST_INPUT'])
STOP = []
REPORT = {'status': 'STARTED', 'commands': [], 'checks': []}
PLAN = {'proof_expanded_mib': 64, 'proof_chunk_mib': 0}
CHECKER = '/usr/local/bin/cake_lpr'
helper = Path(__file__).parents[1] / 'ether_gap_solve.py'
transport = Path(__file__).parents[1] / 'intel_phase_review.py'
assert hashlib.sha256(helper.read_bytes()).hexdigest() == '11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
assert hashlib.sha256(transport.read_bytes()).hexdigest() == 'c7cf04f5250e2cef2b95a0d908dd2233b3222aacac163f4de97f96f22ac6ca01'
for path, names in [(helper, {'cpu', 'thermal', 'command'}), (transport, {'proof_stream'})]:
    functions = [n for n in ast.parse(path.read_bytes()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert len(functions) == len(names)
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(path), 'exec'), globals())


def save(name=None, value=None):
    if name is None:
        REPORT['worker_cpu_s'] = cpu()
        name, value = 'solve.json', REPORT
    (OUT/name).write_text(json.dumps(value, indent=2) + '\n')


TAB = (0, 1, 1, 1, 1, 0, 0, 0)
JOBS = [
    {'name': 'robust_p3_H83', 'H': 83, 'side': 'both', 'vars': 12221, 'clauses': 102170, 'heap': 384, 'cpu': 15, 'wall': 30,
     'cnf_gz_sha256': '04d8a2f5ceef9a131c40d9e2a33019343275a55e93104e2b79d2fa3ee04f15f0',
     'cnf_sha256': 'dde2748f4234a347960e5c2b0bccc4cf712a1f3109345d3eaa21cac4db6cf693',
     'proof_gz_sha256': '3061211bc4cf8a81b9b31ecc1d06b625c9c2103f4ea3b3cc2baa7d07e3dd7b35', 'proof_bytes': 3443869},
    {'name': 'robust_p3_H162_ahead', 'H': 162, 'side': 'ahead', 'vars': 42869, 'clauses': 339249, 'heap': 512, 'cpu': 45, 'wall': 65,
     'cnf_gz_sha256': '24958ef6f562e9fbf4cfca1e2c69859c58cc71c1c09c20dd0be64262f7b637cf',
     'cnf_sha256': '5d425d377f0186b5131073eb85125f4dc8c69685167f9b302d8e6ea2ae2d388e',
     'proof_gz_sha256': 'a92940530d77360fa7458640802195709568633ad89b065302fb7a897b686286', 'proof_bytes': 63692572}
]


def packed(x, mask):
    return ((x << 1) ^ (x | (x >> 1))) & mask


def trace(orbit):
    E = lambda t, x: orbit[(t + 4) % 63][(t - x) % 7]
    lo, hi = -7000, 4000
    mask = (1 << (hi - lo + 1)) - 1
    bg = sum(E(0, x) << (x - lo) for x in range(lo, hi + 1))
    row = bg ^ (3 << -lo)
    fronts = []; initial = None
    for t in range(1, 3163):
        row, bg = packed(row, mask), packed(bg, mask)
        if t >= 3000:
            diff = row ^ bg
            assert diff
            fi = (diff & -diff).bit_length() - 1
            F = fi + lo
            assert lo + t + 1 < F and F + 25 < hi - t - 1
            fronts.append(F)
            if t == 3000:
                A = F - 1
                bits = ''.join(str((row >> (fi + i)) & 1) for i in range(16))
                assert (t % 63, (t - A) % 7, bits) == (39, 0, '0011011100111010')
                assert all(((bg >> (x - lo)) & 1) == E(t, x) for x in range(A - 170, A + 180))
                initial = bits
    assert len(fronts) == 163
    return fronts, tuple(map(int, initial))


def reconstruct(job, orbit, fronts, strip, target):
    H = job['H']; A0 = fronts[0] - 1
    # Reproduce Local's actual floating preprocessing, then audit it against
    # exact integer-scaled rational bounds; never silently change the CNF.
    line = [fronts[0] - 11 * k / 81 for k in range(H + 1)]
    dev = [fronts[k] - line[k] for k in range(H + 1)]
    low = [math.ceil(line[k] + min(dev) - 3) - A0 for k in range(H + 1)]
    high = [math.floor(line[k] + max(dev) + 3) - A0 for k in range(H + 1)]
    scaled = [81 * (fronts[k] - fronts[0]) + 11 * k for k in range(H + 1)]
    exactlow = [1 - ((-(min(scaled) - 11 * k - 243)) // 81) for k in range(H + 1)]
    exacthigh = [1 + (max(scaled) - 11 * k + 243) // 81 for k in range(H + 1)]
    mismatch = [[k, low[k], exactlow[k], high[k], exacthigh[k]] for k in range(H + 1)
                if low[k] != exactlow[k] or high[k] != exacthigh[k]]
    E = lambda t, x: orbit[(39 + t + 4) % 63][(t - x) % 7]
    varmap = {}
    def v(t, x):
        if (t, x) not in varmap:
            varmap[t, x] = len(varmap) + 1
        return varmap[t, x]
    XL = -H - 3; XR = lambda t: 16 + H - t
    clauses = []
    for x in range(XL, XR(0) + 1):
        if x <= 16:
            bit = E(0, x) if x <= 0 else strip[x - 1]
            clauses.append([v(0, x) if bit else -v(0, x)])
    for t in range(H):
        for x in range(XL + 1, XR(t + 1) + 1):
            a, b, c, d = v(t, x - 1), v(t, x), v(t, x + 1), v(t + 1, x)
            for j in range(8):
                ins = ((j >> 2) & 1, (j >> 1) & 1, j & 1)
                clauses.append([-z if bit else z for z, bit in zip((a, b, c), ins)] + [d if TAB[j] else -d])
        clauses.append([v(t + 1, XL) if E(t + 1, XL) else -v(t + 1, XL)])
    D = lambda t, x: v(t, x) if E(t, x) == 0 else -v(t, x)
    violation = []
    for t in range(1, H + 1):
        assert low[t] - 1 >= XL and high[t] <= XR(t)
        violation.extend(D(t, x) for x in range(XL + 1, low[t]))
        if job['side'] == 'both':
            varmap['y', t] = len(varmap) + 1; y = varmap['y', t]
            clauses.extend([-y, -D(t, x)] for x in range(XL + 1, high[t] + 1))
            violation.append(y)
    clauses.append(violation)
    assert (len(varmap), len(clauses)) == (job['vars'], job['clauses'])
    path = OUT/(job['name'] + '-rebuilt.cnf')
    with path.open('w') as f:
        f.write('p cnf %d %d\n' % (len(varmap), len(clauses)))
        for clause in clauses:
            f.write(' '.join(map(str, clause)) + ' 0\n')
    assert path.read_bytes() == target.read_bytes(), 'ORIGINAL_BAND_CNF_MISMATCH'
    return {'original_cnf_byte_exact': True, 'relative_lower': low, 'relative_upper': high,
            'exact_scaled_deviation': [min(scaled), max(scaled)],
            'float_vs_exact_disagreements': mismatch, 'fixed_initial_anchor': A0}


def stream_check(name, cnf, expected_bytes, cap, wall, heap, should_verify, raw_hash=None):
    fifo, thread, receipt = proof_stream(name, False)
    try:
        rc, text, reason = command(name + '-check', [CHECKER, '--CML_HEAP_SIZE=%d' % heap,
            '--CML_STACK_SIZE=64', str(cnf), str(fifo)], cap, wall)
    finally:
        thread.join(timeout=3)
        if thread.is_alive() or not receipt.get('complete'):
            raise RuntimeError('INCOMPLETE_OR_FAILED_PROOF_STREAM')
        fifo.unlink(missing_ok=True)
    assert reason == 'EXIT' and rc == 0
    assert receipt['bytes'] == expected_bytes and receipt['bytes'] <= 64 << 20
    if raw_hash:
        assert receipt['sha256'] == raw_hash
    assert ('s VERIFIED UNSAT' in text) == should_verify
    return receipt


def main():
    os.nice(10); resource.setrlimit(resource.RLIMIT_CPU, (20, 90))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    assert hashlib.sha256(Path(CHECKER).read_bytes()).hexdigest() == '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'
    data_raw = Path(os.environ['A4_DATA63']).read_bytes()
    assert hashlib.sha256(data_raw).hexdigest() == '528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b'
    orbit = json.loads(data_raw)['orb']
    assert len(orbit) == 63 and all(len(r) == 7 for r in orbit)
    # Independent literal oracle for packed physical-row bit orientation.
    for p in range(256):
        vec = [0] * 8 + [(p >> j) & 1 for j in range(8)] + [0] * 8
        word = sum(b << j for j, b in enumerate(vec))
        for tick in range(1, 5):
            vec = [0] + [TAB[4 * vec[j - 1] + 2 * vec[j] + vec[j + 1]] for j in range(1, 23)] + [0]
            word = packed(word, (1 << 24) - 1)
            assert all(((word >> j) & 1) == vec[j] for j in range(tick, 24 - tick))
    fronts, strip = trace(orbit)
    unit = OUT/'unit.cnf'; unit.write_text('p cnf 1 2\n1 0\n-1 0\n')
    for name, raw, accepted in [('unit-good', b'3 0 1 2 0\n', True), ('unit-bad', b'3 0 1 1 0\n', False), ('unit-empty', b'', False)]:
        (OUT/(name + '.lrat.gz')).write_bytes(gzip.compress(raw, mtime=0))
        stream_check(name, unit, len(raw), 2, 5, 64, accepted, hashlib.sha256(raw).hexdigest())
    REPORT['controls'] = 'All256 width8/four-tick literal oracle; FIFO valid proof accepted, corrupt hint and empty proof rejected.'
    for job in JOBS:
        name = job['name']
        cinput, pinput = INPUT/(name + '.cnf.gz'), INPUT/(name + '.lrat.gz')
        assert hashlib.sha256(cinput.read_bytes()).hexdigest() == job['cnf_gz_sha256']
        assert hashlib.sha256(pinput.read_bytes()).hexdigest() == job['proof_gz_sha256']
        target = OUT/(name + '.cnf'); count = 0
        with gzip.open(cinput, 'rb') as source, target.open('wb') as dest:
            while block := source.read(65536):
                count += len(block); assert count <= 16 << 20
                dest.write(block)
        assert hashlib.sha256(target.read_bytes()).hexdigest() == job['cnf_sha256']
        audit = reconstruct(job, orbit, fronts, strip, target); gc.collect()
        shutil.copyfile(pinput, OUT/(name + '.lrat.gz'))
        receipt = stream_check(name, target, job['proof_bytes'], job['cpu'], job['wall'], job['heap'], True)
        REPORT['checks'].append({'name': name, 'status': 'ORIGINAL_CNF_BYTE_EXACT_AND_LRAT_VERIFIED_UNSAT',
                                 'cnf_sha256': job['cnf_sha256'], 'stream': receipt, 'predicate_audit': audit})
        save()
    REPORT['status'] = 'BOTH_ORIGINAL_ROBUSTNESS_PROOFS_VERIFIED'
    thermal(); save(); print(json.dumps(REPORT, indent=2))


try:
    main()
except BaseException as error:
    REPORT.update(status='FAILED', failure=repr(error)); save(); raise
