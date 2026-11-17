#!/usr/bin/env python3
"""rule30_kick_strain_kissat.py: KT2, part 2 of Cloud's --strain (rule30_kick_bite_sat.py: classes 32, 52 and 42 after
336 and 560 steps on the wheel), taken over by Local with KK's encoding and kissat at Cloud's offer (CL029: "If kissat
is quicker on the M5, it is yours to take instead"). Claimed in CLOUD-LOCAL.md with these predictions pushed before
the run. Cloud's KT-P2 and KT-P3 were published before part 1 ran and are scored here as they stand.

RUN-ON:     cpu, 3 kissat processes beside RK's 6 threads on the M5; kissat on the PATH
COMMAND:    python3 tests/probes/lexicon/rule30_kick_strain_kissat.py start | status | resume
            (start and resume launch a detached run; both skip every instance already in the checkpoint)
COST:       about two hours for the N = 336 stage on 3 cores (most solves end near the 1,800 s cap). Each instance
            is capped at 1,800 s; a capped instance is recorded as UNKNOWN, never as either answer.

The question per instance is KK's (rule30_kick_bite_kissat.py): with the row at t0 free, can column 1 follow the
wheel at even phase d for at least N steps, depart at class a, and follow a new even phase for 21 observations? A
class survives at N if some case (t0, d) is satisfiable; every model is replayed by direct simulation.
ORDER (revised 2026-10-07 23:05, after the first three N = 560 instances all reached their 30-minute cap; methods
only, no prediction changed): for each class, N = 336 runs first, case by case in batches of 3, and stops at the
first replayed SAT. Then N = 560 starts from that case (by GC377 a case unsatisfiable at 336 is unsatisfiable at 560,
so the 336 survivors are the only candidates worth trying first), and continues case by case if it caps. The original
order (560 first) is kept in Git history; its three capped instances stay in the checkpoint as UNKNOWN.

PREDICTIONS:
  Cloud's (KS header, 2026-10-07 21:16 BST): KT-P2, classes 32 and 52 stay satisfiable at N = 336 and 560
         (confidence 0.8); KT-P3, class 42 dies by N = 560 (confidence 0.4).
  Local's (published before this run):
  KT2-C1 (control): every SAT model replays by direct simulation, and every instance reaches the solver (it has at
         least one eligible new phase; the count is logged).
  KT2-C2 (control, GC377): every case found satisfiable at 560 is satisfiable at 336.
  KT2-C3 (negative control, entry 27 with G206): class 12 at N = 336, case (t0 0, d 2), is UNSAT (or capped, which
         is reported and is not a pass).
  KT2-P1: classes 32 and 52 survive at 336 and at 560 (the same claim as Cloud's KT-P2).
  KT2-P2 (diverging from KT-P3): class 42 survives at 560 too.
OUTCOME of the N = 336 stage, 2026-10-08 00:29 (M5; checkpoint and log outside Git). Every class Cloud asked about
survives 336 steps on the wheel, each by a solver model that replays: class 32 at cases (0, 2) and (0, 4), class 52 at
(0, 4), class 42 at (0, 0), (0, 2) and (0, 4); the other 336 instances tried reached the cap (UNKNOWN). KT2-C3 PASS:
class 12 at N = 336, case (0, 2), is UNSAT. KT2-C1 PASS for every SAT found. N = 560: the three class-32 instances of
the first order, (0, 0), (0, 2) and (0, 4), reached the 30-minute cap (UNKNOWN), and a second sweep was stopped at
00:31 before any result, in favour of KT2L (rule30_kick_strain_long.py: the 336-SAT cases at 560 with 4-hour caps).
Scores so far: Cloud's KT-P2 holds at N = 336 (classes 32 and 52 alive) and is untested at 560; KT-P3 is untested
(class 42 is alive at 336); KT2-P1 holds at 336 and is untested at 560; KT2-P2 is untested; KT2-C2 is vacuous.
"""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv

SCRATCH = os.environ.get('NP_SCRATCH_KT2', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-kt2'))
CK = os.path.join(SCRATCH, 'kt2.ck')
LOG = os.path.join(SCRATCH, 'kt2.log')
CAP = 1800
JOBS = 3
P = kk.P
CASES = [(t0, d) for t0 in (0, 1) for d in range(0, P, 2)]


def done():
    res = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 7 and f[-1] == 'END':
                res[int(f[0]), int(f[1]), int(f[2]), int(f[3])] = (f[4], f[5])
    return res


def record(N, a, t0, d, verdict, extra):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:                                        # a kill mid-write left a partial line; never append onto it
            with open(CK, 'a') as f:
                f.write('\n')
    with open(CK, 'a') as f:
        f.write('%d %d %d %d %s %s END\n' % (N, a, t0, d, verdict, extra))


def solve(task):
    N, a, t0, d = task
    nv, clauses, row, s, E = kk.instance(t0, d, a, N)
    nsel = len(clauses[-1])
    path = os.path.join(SCRATCH, 'i_%d_%d_%d_%d.cnf' % task)
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    if nsel == 0:
        os.unlink(path)
        return task, 'LITERAL', 'sel0'
    r = subprocess.run(['kissat', '-q', '--time=%d' % CAP, path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode == 20:
        return task, 'UNSAT', 'sel%d' % nsel
    if r.returncode != 10:
        return task, 'UNKNOWN', 'rc%d' % r.returncode
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    ok = kk.replay(t0, d, s, E, [1 if x in val else 0 for x in row])
    return task, 'SAT', 'replay-pass' if ok else 'replay-FAIL'


def batch(tasks):
    have = done()
    todo = [t for t in tasks if t not in have]
    if todo:
        with ThreadPoolExecutor(JOBS) as ex:       # record each result as it finishes: ex.map yields in order, so
            for fut in as_completed([ex.submit(solve, t) for t in todo]):   # KT2M lost a finished case at a shutdown
                task, verdict, extra = fut.result()
                record(*task, verdict, extra)
                print('%s N %d class %d case (%d, %d): %s %s' % (os.popen('date +%H:%M:%S').read().strip(),
                      task[0], task[1], task[2], task[3], verdict, extra), flush=True)
    have = done()
    return {t: have[t] for t in tasks}


def first_sat(N, a):
    for i in range(0, len(CASES), JOBS):
        res = batch([(N, a, t0, d) for t0, d in CASES[i:i + JOBS]])
        sat = [t for t, v in res.items() if v[0] == 'SAT']
        if sat:
            return min(sat)
    return None


def run():
    os.makedirs(SCRATCH, exist_ok=True)
    found = {}
    for a in (32, 52, 42):
        found[336, a] = first_sat(336, a)
    batch([(336, 12, 0, 2)])
    for a in (32, 52, 42):
        first = found[336, a]
        if first is not None:
            _, _, t0, d = first
            batch([(560, a, t0, d)])
            if done()[560, a, t0, d][0] == 'SAT':
                found[560, a] = (560, a, t0, d)
                continue
        found[560, a] = first_sat(560, a)
        if found[560, a] is not None:                   # KT2-C2 needs that case at 336 as well
            batch([(336, a, found[560, a][2], found[560, a][3])])
    have = done()
    c1 = all(v[1] == 'replay-pass' for v in have.values() if v[0] == 'SAT') and \
        not any(v[0] == 'LITERAL' for v in have.values())
    c2 = all(have.get((336, a, t[2], t[3]), ('',))[0] == 'SAT' for a in (32, 52, 42)
             for t in [found[560, a]] if t is not None)
    c3 = have[336, 12, 0, 2]
    print('survival:', {'%d@%d' % (a, N): (found[N, a] is not None) for N in (336, 560) for a in (32, 52, 42)})
    print('UNKNOWN (capped) instances:', sum(1 for v in have.values() if v[0] == 'UNKNOWN'))
    print('KT2-C1', 'PASS' if c1 else 'FAIL')
    print('KT2-C2', 'PASS' if c2 else 'FAIL')
    print('KT2-C3', 'PASS' if c3[0] == 'UNSAT' else ('CAPPED' if c3[0] == 'UNKNOWN' else 'FAIL'), c3)
    alive = lambda N, a: found[N, a] is not None
    print('KT-P2 (Cloud)', 'HELD' if all(alive(N, a) for N in (336, 560) for a in (32, 52)) else 'REFUTED')
    print('KT-P3 (Cloud)', 'HELD' if not alive(560, 42) else 'REFUTED')
    print('KT2-P1', 'HELD' if all(alive(N, a) for N in (336, 560) for a in (32, 52)) else 'REFUTED')
    print('KT2-P2', 'HELD' if alive(560, 42) else 'REFUTED')
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (CK, LOG))


def status():
    print('%d instances checkpointed' % len(done()))
    if os.path.exists(LOG):
        print(open(LOG).read()[-1500:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run}[cmd]()
