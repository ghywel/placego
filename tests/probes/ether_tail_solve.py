#!/usr/bin/env python3
"""GC2433: separately frozen controls+one original exact-tail SAT/LRAT pilot.

Sequential single-thread tools; actual worker reaped+live child CPU guard95s.
No alternate input, timeout extension or proof-output retry.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import resource
import signal
import subprocess
import time

OUT = Path(os.environ['CAPPED_OUT'])
INPUT = Path(os.environ['TAIL_CNF_INPUT'])
STOP = []
REPORT = {'commands': [], 'status': 'STARTED'}
CADICAL = '/usr/local/bin/cadical'
CHECKER = '/usr/local/bin/cake_lpr'


def save():
    REPORT['worker_cpu_s'] = cpu()
    (OUT/'solve.json').write_text(json.dumps(REPORT, indent=2)+'\n')


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def thermal():
    r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=4)
    with (OUT/'thermal.txt').open('a') as f:
        f.write(r.stdout+r.stderr)
    limits = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)', r.stdout+r.stderr)
    if r.returncode or len(limits) != 2 or any(x != '100' for x in limits):
        raise RuntimeError('THERMAL_MONITOR_STOP')


def command(name, args, cap, wall):
    if STOP or cpu() >= 95:
        raise RuntimeError('WORKER_STOP')
    thermal()
    before = cpu()
    start = time.monotonic()
    reason = 'EXIT'
    last = start-1
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (cap, cap))
    with (OUT/(name+'.stdout')).open('w') as fo, (OUT/(name+'.stderr')).open('w') as fe:
        p = subprocess.Popen(args, stdout=fo, stderr=fe, preexec_fn=limit)
        try:
            while p.poll() is None:
                now = time.monotonic()
                if STOP:
                    reason = 'EXTERNAL_STOP'
                    break
                if now-start >= wall:
                    reason = 'CHILD_WALL_STOP'
                    break
                if now-last >= .5:
                    r = subprocess.run(['ps', '-p', str(p.pid), '-o', 'time='],
                                       capture_output=True, text=True, timeout=3)
                    if p.poll() is not None:
                        break
                    fields = r.stdout.strip().split(':')
                    if r.returncode or len(fields) != 2:
                        raise RuntimeError('CPU_MONITOR_FAILURE')
                    live = 60*int(fields[0])+float(fields[1])
                    total = cpu()+live
                    (OUT/'cpu-live.json').write_text(json.dumps({'worker_live_cpu_s': total, 'child': name})+'\n')
                    if total >= 95:
                        reason = 'AGGREGATE_CPU_STOP'
                        break
                    if int(now-start)//5 > int(last-start)//5:
                        thermal()
                    last = now
                time.sleep(.05)
        except BaseException as e:
            reason = repr(e)
            STOP.append(reason)
            raise
        finally:
            if p.poll() is None:
                p.terminate()
                try:
                    p.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    p.kill()
                    p.wait()
            REPORT['commands'].append({'name': name, 'args': args, 'returncode': p.returncode,
                'reason': reason, 'wall_s': time.monotonic()-start,
                'aggregate_worker_increment_s': cpu()-before})
            save()
    if STOP or reason == 'AGGREGATE_CPU_STOP' or p.returncode == -25:
        raise RuntimeError('STAGE_STOP:'+reason+':'+str(p.returncode))
    text = (OUT/(name+'.stdout')).read_text()+'\n'+(OUT/(name+'.stderr')).read_text()
    return p.returncode, text, reason


def check_proof(name, cnf, proof, cap, wall):
    rc, text, why = command(name, [CHECKER, '--CML_HEAP_SIZE=384', '--CML_STACK_SIZE=64',
                                  str(cnf), str(proof)], cap, wall)
    assert rc == 0 and why == 'EXIT' and 's VERIFIED UNSAT' in text, 'CERTIFICATE_NOT_VERIFIED'


def parse_model(text, nv):
    assert 's SATISFIABLE' in text
    values = {}
    for line in text.splitlines():
        if line.startswith('v '):
            for word in line[2:].split():
                literal = int(word)
                if not literal:
                    continue
                var, value = abs(literal), int(literal > 0)
                assert 1 <= var <= nv and (var not in values or values[var] == value)
                values[var] = value
    assert set(values) == set(range(1, nv+1)), 'INCOMPLETE_MODEL'
    return bytearray([0]+[values[i] for i in range(1, nv+1)])


def load_encoder():
    p = Path('tests/probes/ether_tail_cnf.py')
    assert hashlib.sha256(p.read_bytes()).hexdigest() == '0a0ab05fab78bfd99941e5574c7488f30e212ecdae36afb088a527a03ff18425'
    spec = importlib.util.spec_from_file_location('encoder', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def solve(name, cnf, cap, wall):
    proof = OUT/(name+'.lrat')
    rc, text, reason = command(name, [CADICAL, '--lrat', '--no-binary', '-q', str(cnf), str(proof)], cap, wall)
    if reason != 'EXIT' or rc not in (10, 20):
        assert rc in (-9, -24, -15, 0) or reason == 'CHILD_WALL_STOP', ('SOLVER_FAILURE', rc, reason)
        return 'UNKNOWN', text, proof
    if rc == 20:
        assert 's UNSATISFIABLE' in text
        return 'UNSAT', text, proof
    return 'SAT', text, proof


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 90))
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda s, f: STOP.append(s))
    for p, expected in [(Path(CADICAL), '7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
                        (Path(CHECKER), '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
                        (INPUT/'tail111.cnf', '063ae6aed31305155b3a3115eb2fb443990afc3c916d4f1f1d85b63a7c4a3338'),
                        (INPUT/'tail112.cnf', 'ffb52b7f598bec4c7dc07ab56828b67b1f03262dd68fa6789a2f0c98235f271e'),
                        (INPUT/'010.cnf', 'ad4f2afcfaad0c7d46f277c3d46dff23184ef504d84f968b294e77d519c0ae4e'),
                        (INPUT/'110-gap.cnf', 'e78928354d3e7d5fd4f013404867a2dcbe69e730616201c85a9ab6a21ef60250')]:
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
    m = load_encoder()
    small = m.Cone(-3, 2, 2, 0, lambda x: [0, 1, 1, 0, 0, 0][x+3])
    status, text, _ = solve('small-sat', INPUT/'110-gap.cnf', 1, 3)
    assert status == 'SAT'
    bits = parse_model(text, small.nv)
    assert not m.disk_unsatisfied(INPUT/'110-gap.cnf', bits)
    assert bits == small.scalar_model({1: bits[small.var(0, 1)], 2: bits[small.var(0, 2)]})
    status, _, proof = solve('small-unsat', INPUT/'010.cnf', 1, 3)
    assert status == 'UNSAT'
    check_proof('small-check', INPUT/'010.cnf', proof, 1, 3)
    empty = OUT/'empty.lrat'
    empty.write_bytes(b'')
    rc, text, _ = command('reject-empty', [CHECKER, '--CML_HEAP_SIZE=64', '--CML_STACK_SIZE=32',
                                          str(INPUT/'010.cnf'), str(empty)], 1, 3)
    assert 's VERIFIED UNSAT' not in text and 'empty clause not derived' in text
    REPORT['micro_controls'] = 'SAT model replay, UNSAT checked, empty rejected'
    status, _, proof = solve('protected', INPUT/'tail112.cnf', 4, 8)
    assert status == 'UNSAT', 'PROTECTED_CONTROL_FAILED'
    check_proof('protected-check', INPUT/'tail112.cnf', proof, 10, 15)
    REPORT['protected_control'] = {'status': 'LRAT_CHECKED_UNSAT',
                                 'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest()}
    save()
    status, text, proof = solve('original', INPUT/'tail111.cnf', 25, 40)
    REPORT['original_status'] = status
    if status == 'SAT':
        bits = parse_model(text, 68907)
        assert not m.disk_unsatisfied(INPUT/'tail111.cnf', bits)
        table = [[0,0,1,1],[0,1,1,0],[1,1,0,1],[0,1,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
        initial = lambda x: table[(x+4)%7][3] if x < 0 else int(x == 0)
        cone = m.Cone(-332, 198, 222, 111, initial)
        free = {x: bits[cone.var(0, x)] for x in range(112, 199)}
        assert bits == cone.scalar_model(free), 'ACTUAL_ROW_REPLAY_FAILED'
        cone.packed_control(bits)
        differences = [x for x in range(-110, -23) if bits[cone.var(222, x)] != cone.reference[cone.var(222, x)]]
        assert differences
        (OUT/'model.bits').write_bytes(bits)
        REPORT['witness'] = {'free_bits': [free[x] for x in range(112,199)],
                             'differing_targets': differences, 'all_original_clauses_checked': True,
                             'actual_scalar_and_packed_replay': True,
                             'sha256': hashlib.sha256(bits).hexdigest()}
    elif status == 'UNSAT':
        check_proof('original-check', INPUT/'tail111.cnf', proof, 30, 50)
        REPORT['original_certificate'] = {'status': 'LRAT_CHECKED_UNSAT',
            'proof_bytes': proof.stat().st_size, 'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest()}
    REPORT['status'] = 'FINITE_QUERY_'+status
    thermal()
    save()
    print(json.dumps(REPORT))


try:
    main()
except BaseException as e:
    REPORT['failure'] = repr(e)
    REPORT['status'] = 'FAILED'
    save()
    raise
