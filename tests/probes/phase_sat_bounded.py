#!/usr/bin/env python3
"""GC2363: retained, capped single-thread SAT jobs; direct phase/model checks.
Run only inside run_capped.py, with a committed JSON job list. No retries.
The sum of solver hard CPU allocations is bounded in the plan; this driver has
its own 10-second CPU limit. Solver wall limits also bound one-thread work.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
from phase_sat import Enc


def direct_check(cols, p, m, s, mode):
    def bit(k, t):
        wraps, k = divmod(k, m)
        return (cols[k] >> ((t + wraps * s) % p)) & 1
    assert all(bit(k+1, t+1) ^ bit(k+1, t) ==
               (bit(k-1, t) | bit(k, t)) for k in range(m) for t in range(p))
    periods = [next(d for d in range(1, p+1) if p % d == 0 and
                    all(bit(k, t+d) == bit(k, t) for t in range(p))) for k in range(m)]
    assert p in periods
    q = p // 4
    fronts = [k for k in range(m) if all(
        sum(bit(k, t+j*q) for j in range(4)) % 2 == 1 for t in range(q))]
    if mode == 'neg':
        assert not fronts
    return {'least_periods': periods, 'front_columns': fronts,
            'direct_equations': True}


def thermal(out):
    r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=4)
    with (out/'thermal.txt').open('a') as f:
        f.write(r.stdout+r.stderr)
    if r.returncode or 'CPU_Speed_Limit' not in r.stdout:
        raise RuntimeError('THERMAL_MONITOR_FAILURE')
    for line in r.stdout.splitlines():
        if 'CPU_Speed_Limit' in line or 'CPU_Scheduler_Limit' in line:
            if int(line.split('=')[1]) != 100:
                raise RuntimeError('THERMAL_OR_SCHEDULER_STOP')


def run(job, out):
    mode, p, m, s = (job[k] for k in ('mode', 'p', 'm', 's'))
    assert p >= 4 and p & (p-1) == 0 and m > 0 and 0 <= s < p
    e = Enc(p, m, s, mode)
    stem = out/job['name']; cnf = stem.with_suffix('.cnf')
    with cnf.open('w') as f:
        f.write(f'p cnf {e.nv} {len(e.cl)}\n')
        for clause in e.cl:
            f.write(' '.join(map(str, clause))+' 0\n')
    solver = job['solver']
    command = [solver, '-q', str(cnf)]
    if job.get('proof'):
        assert solver.endswith('cadical')
        command = [solver, '--lrat', '--no-binary', str(cnf), str(stem.with_suffix('.lrat'))]
    cpu = job['cpu']; wall = job['wall']
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
    usage0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    t0 = time.monotonic(); reason = 'EXIT'; lastthermal = t0
    with stem.with_suffix('.stdout').open('w') as stdout, stem.with_suffix('.stderr').open('w') as stderr:
        proc = subprocess.Popen(command, stdout=stdout, stderr=stderr, preexec_fn=limits)
        try:
            while proc.poll() is None:
                if time.monotonic()-t0 >= wall:
                    reason = 'WALL_LIMIT'; break
                if time.monotonic()-lastthermal >= 5:
                    thermal(out); lastthermal = time.monotonic()
                time.sleep(.2)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try: proc.wait(timeout=1)
                except subprocess.TimeoutExpired: proc.kill(); proc.wait()
    elapsed = time.monotonic()-t0
    usage1 = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_used = usage1.ru_utime+usage1.ru_stime-usage0.ru_utime-usage0.ru_stime
    text = stem.with_suffix('.stdout').read_text()
    status = 'SAT' if proc.returncode == 10 else 'UNSAT' if proc.returncode == 20 else 'UNKNOWN'
    result = dict(job, status=status, returncode=proc.returncode, reason=reason,
                  wall_s=elapsed, child_cpu_s=cpu_used,
                  cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),
                  variables=e.nv, clauses=len(e.cl))
    if status == 'SAT':
        assert 's SATISFIABLE' in text
        model = [int(x) for line in text.splitlines() if line.startswith('v ') for x in line[2:].split() if x != '0']
        assignment = set(model)
        assert not any(-x in assignment for x in assignment)
        assert all(any(x in assignment for x in clause) for clause in e.cl)
        cols = [sum(1 << t for t in range(p) if 1+k*p+t in assignment) for k in range(m)]
        result.update(columns_hex=[hex(c) for c in cols], cnf_model_checked=True,
                      **direct_check(cols, p, m, s, mode))
    if status == 'UNSAT':
        assert 's UNSATISFIABLE' in text
        result['certified'] = False
    stem.with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)
    if job.get('expected') and status != job['expected']:
        raise RuntimeError('CONTROL_FAILED')
    if status == 'UNKNOWN' and reason == 'EXIT' and proc.returncode not in (-9, -24):
        raise RuntimeError('ABNORMAL_SOLVER_EXIT')
    return result


def main():
    out = Path(os.environ['CAPPED_OUT'])
    plan = json.loads(Path(sys.argv[1]).read_text())
    assert sum(j['cpu'] for j in plan['jobs']) + 10 <= plan['aggregate_cpu_ceiling']
    assert sum(j['wall']+1 for j in plan['jobs'])+10 <= plan['stage_wall']
    resource.setrlimit(resource.RLIMIT_CPU, (10, plan['aggregate_cpu_ceiling']))
    thermal(out)
    results = []
    for job in plan['jobs']:
        results.append(run(job, out))
        if job['mode'] == 'neg' and results[-1]['status'] == 'SAT': break
    thermal(out)
    me = resource.getrusage(resource.RUSAGE_SELF); kids = resource.getrusage(resource.RUSAGE_CHILDREN)
    (out/'summary.json').write_text(json.dumps({'results': results,
        'driver_cpu_s': me.ru_utime+me.ru_stime,
        'children_cpu_s': kids.ru_utime+kids.ru_stime}, indent=2)+'\n')

if __name__ == '__main__':
    main()
