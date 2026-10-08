#!/usr/bin/env python3
"""rule30_silence_onset.py: SO, the age at which a near-silent edge event of the forced left half falls silent for good
(row Q6; CL054 ask (a); GPT's ray coverage, GC585; Local's L308 and L309). Local's run; predictions pushed before it.

RUN-ON:     cpu, up to 5 kissat processes (drat-trim for boundary UNSATs); resumable
COMMAND:    python3 tests/probes/lexicon/rule30_silence_onset.py start | status | resume
COST:       to be recorded; expected under an hour (instances have about (a + j)^2 cells).

Question. SS (L309) found the edge events E_j that never fire at age 0 (E_1 black, E_2, E_4 white, E_6, E_14 white
to depth 31). A source that fires at age 0 can still fall silent once the rows have aged, and GPT's frontier ray
reaches depth j at age j - L - 2, so silence with an onset age counts there (L308). The near-silent sources at age 0
are E_10 (white 0.023, black 0.035), E_12 (white 0.088), E_14 black (0.054) and E_15 (white 0.135, black 0.065).

Instance "E_j fires at age a in colour p": the full configuration's light cone of column 0 up to time T = a + j - 1,
cells x_t(i) for |i| <= T - t, Rule 30 updates x_(t+1)(i) = x_t(i - 1) XOR (x_t(i) OR x_t(i + 1)), column 0 equal to
(t + q) mod 2 for t = 0 .. T with q = (p - a) mod 2, and x_a(-j + 2) = 1, x_a(-j + 1) = 0. The clock through T forces
the left cells at time a down to depth j - 1, so this is exactly "some configuration whose clock has run a steps has
E_j(a) = 1". Firing is closed downwards in age within a colour (the row two steps older is again a row of a clock
configuration), so each target has an onset age: the least a of its colour at which it is UNSAT, or none.
Search per target as in RV3: a ladder of ages of the right parity to AMAX, then bisection; SAT models are replayed by
direct simulation; the UNSAT at the onset gets a drat-trim proof.

Targets: (10, white), (10, black), (12, white), (14, black), (15, white), (15, black); AMAX 256 (even ages for white,
odd for black, with q chosen per age). Controls: (14, white) and (6, black) are UNSAT at their least age; (30, white)
is SAT at age 0 and 64.

PREDICTIONS (Local's, published before the run):
  SO-C1 (control): every SAT model replays by simulation (the clock holds through T and E_j(a) = 1); every onset UNSAT
        has a VERIFIED proof.
  SO-C2 (control): (14, white) at age 0 and (6, black) at age 1 are UNSAT (SS's age-0 silences); (30, white) is SAT at
        ages 0 and 64.
  SO-P1 (blind, confidence 0.6): at least one of the six targets falls silent at some age <= 256 (a certified onset).
  SO-P2 (blind, confidence 0.4): E_10 falls silent in both colours by age 64.
  SO-P3 (blind, confidence 0.5): E_12 white and E_15 white are still firing at age 256.
  D1 (descriptive): each target's onset age, or its last firing age before the cap.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRATCH = os.environ.get('NP_SCRATCH_SO', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-so'))
CK = os.path.join(SCRATCH, 'so.ck')
LOG = os.path.join(SCRATCH, 'so.log')
CAP = 3600
CAP_FINAL = 14400
DRAT_CAP = 20000
JOBS = 5
AMAX = 256
TARGETS = [(10, 0), (10, 1), (12, 0), (14, 1), (15, 0), (15, 1)]     # (j, colour): 0 white, 1 black at time a
CONTROLS = [((14, 0), 0), ((6, 1), 1), ((30, 0), 0), ((30, 0), 64)]


def name(target):
    return 'E%d%s' % (target[0], 'w' if target[1] == 0 else 'b')


def instance(target, a):
    j, p = target
    T = a + j - 1
    q = (p - a) % 2
    var = {}
    n = 0
    for t in range(T + 1):
        for i in range(-(T - t), T - t + 1):
            n += 1
            var[t, i] = n
    cl = []
    for t in range(1, T + 1):
        for i in range(-(T - t), T - t + 1):
            y, l, c, r = var[t, i], var[t - 1, i - 1], var[t - 1, i], var[t - 1, i + 1]
            for x in (0, 1):
                for b in (0, 1):
                    for d in (0, 1):
                        f = x ^ (b | d)
                        cl.append([(l if x == 0 else -l), (c if b == 0 else -c), (r if d == 0 else -r),
                                   (y if f == 1 else -y)])
    for t in range(T + 1):
        v = var[t, 0]
        cl.append([v] if (t + q) % 2 else [-v])
    cl.append([var[a, -j + 2]])
    cl.append([-var[a, -j + 1]])
    return n, cl, T, q, var


def replay(target, a, T, q, init):
    """init: dict i -> bit for time-0 cells -T .. T; check the clock through T and E_j(a) = 1 by direct simulation"""
    j, p = target
    row = dict(init)
    lo, hi = -T, T
    for t in range(T + 1):
        if row[0] != (t + q) % 2:
            return False
        if t == a and not (row[-j + 2] == 1 and row[-j + 1] == 0):
            return False
        if t < T:
            row = {i: row[i - 1] ^ (row[i] | row[i + 1]) for i in range(lo + 1, hi)}
            lo, hi = lo + 1, hi - 1
    return True


def solve(task, proof=False):
    target, a = task
    t0 = time.time()
    n, cl, T, q, var = instance(target, a)
    tag = '%s_%d' % (name(target), a)
    cnf = os.path.join(SCRATCH, 'i_%s.cnf' % tag)
    with open(cnf, 'w') as f:
        f.write('p cnf %d %d\n' % (n, len(cl)))
        f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    prf = os.path.join(SCRATCH, 'p_%s.drat' % tag)
    if proof:
        r = subprocess.run(['kissat', '-q', '-f', '--no-binary', '--time=%d' % CAP_FINAL, cnf, prf],
                           capture_output=True, text=True)
    else:
        r = subprocess.run(['kissat', '-q', '--time=%d' % CAP, cnf], capture_output=True, text=True)
    secs = time.time() - t0
    verdict, extra = 'UNKNOWN', 'rc%d' % r.returncode
    if r.returncode == 10:
        val = set()
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                val.update(int(x) for x in line[2:].split())
        init = {i: (1 if var[0, i] in val else 0) for i in range(-T, T + 1)}
        verdict, extra = 'SAT', 'replay-pass' if replay(target, a, T, q, init) else 'replay-FAIL'
    elif r.returncode == 20:
        verdict, extra = 'UNSAT', 'noproof'
        if proof:
            d = subprocess.run(['drat-trim', cnf, prf, '-t', str(DRAT_CAP)], capture_output=True, text=True)
            extra = 'VERIFIED' if 's VERIFIED' in d.stdout else 'NOT-VERIFIED'
    for path in (cnf, prf):
        if os.path.exists(path):
            os.unlink(path)
    return task, verdict, extra, secs


def done():
    res = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 6 and f[-1] == 'END':
                res[f[0], int(f[1])] = (f[2], f[3], float(f[4]))
    return res


def record(key, a, verdict, extra, secs):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:
            with open(CK, 'a') as f:
                f.write('\n')
    with open(CK, 'a') as f:
        f.write('%s %d %s %s %.1f END\n' % (key, a, verdict, extra, secs))
    print('%s %s a %d: %s %s %.1f s' % (time.strftime('%H:%M:%S'), key, a, verdict, extra, secs), flush=True)


def run_tasks(tasks, proof=False, prefix=''):
    have = done()
    todo = [(t, a) for t, a in tasks if (prefix + name(t), a) not in have]
    if todo:
        with ThreadPoolExecutor(JOBS) as ex:
            for fut in as_completed([ex.submit(solve, task, proof) for task in todo]):
                (t, a), verdict, extra, secs = fut.result()
                record(prefix + name(t), a, verdict, extra, secs)


def bounds(key, have, parity):
    st = {a: v[0] for (k, a), v in have.items() if k == key}
    sat = [a for a, v in st.items() if v == 'SAT']
    uns = [a for a, v in st.items() if v == 'UNSAT']
    return st, (max(sat) if sat else parity - 2), (min(uns) if uns else None)


def next_points(target, have, k):
    parity = target[1]                                  # white targets at even ages, black at odd
    st, lo, hi = bounds(name(target), have, parity)
    unknown = [a for a, v in st.items() if v == 'UNKNOWN' and a > lo]
    stops = ([hi] if hi is not None else []) + unknown
    top = min(stops) if stops else None
    if top is not None and top - lo <= 2:
        return []
    if top is None:
        amax = AMAX if AMAX % 2 == parity else AMAX - 1
        pts, a = [], max(parity, lo)
        if parity not in st:
            pts.append(parity)
        while a < amax:
            a = min(2 * a + parity if a > 0 else 2 + parity, amax)
            if a % 2 != parity:
                a -= 1
            if a not in st and a > lo:
                pts.append(a)
        return pts[:k]
    span = [a for a in range(lo + 2, top, 2) if a not in st]
    if len(span) > k:
        span = [span[round(i * (len(span) - 1) / (k - 1))] for i in range(k)]
    return span


def search():
    while True:
        have = done()
        tasks = []
        for t in TARGETS:
            tasks += [(t, a) for a in next_points(t, have, 2)]
        if not tasks:
            return
        run_tasks(tasks)


def run():
    os.makedirs(SCRATCH, exist_ok=True)
    run_tasks([c for c in CONTROLS])
    search()
    have = done()
    finals = []
    for t in TARGETS:
        st, lo, hi = bounds(name(t), have, t[1])
        if hi is not None and hi - lo == 2:
            finals.append((t, hi))
    run_tasks(finals, proof=True, prefix='P')
    report()


def report():
    have = done()
    sats = [v for v in have.values() if v[0] == 'SAT']
    proofs = {(k[1:], a): v for (k, a), v in have.items() if k.startswith('P')}
    c1 = all(v[1] == 'replay-pass' for v in sats) and all(v[1] == 'VERIFIED' for v in proofs.values())
    c2 = (have.get(('E14w', 0), ('',))[0] == 'UNSAT' and have.get(('E6b', 1), ('',))[0] == 'UNSAT'
          and have.get(('E30w', 0), ('',))[0] == 'SAT' and have.get(('E30w', 64), ('',))[0] == 'SAT')
    print('SO-C1', 'PASS' if c1 else 'FAIL', '(%d SAT replays, %d proofs)' % (len(sats), len(proofs)))
    print('SO-C2', 'PASS' if c2 else 'FAIL')
    onset = {}
    for t in TARGETS:
        st, lo, hi = bounds(name(t), have, t[1])
        cert = hi is not None and hi - lo == 2 and proofs.get((name(t), hi), ('', ''))[1] == 'VERIFIED'
        onset[t] = hi if cert else None
        print('%s: last firing age %d, first silent age %s%s, calls %s' % (name(t), lo, hi, ' (certified)' if cert
              else '', sorted(st.items())))
    print('SO-P1', 'HELD' if any(v is not None and v <= 256 for v in onset.values()) else 'REFUTED or undecided')
    e10 = [onset[(10, 0)], onset[(10, 1)]]
    print('SO-P2', 'HELD' if all(v is not None and v <= 64 for v in e10) else 'REFUTED or undecided', e10)
    st12, lo12, _ = bounds('E12w', have, 0)
    st15, lo15, _ = bounds('E15w', have, 0)
    print('SO-P3', 'HELD' if st12.get(256) == 'SAT' and st15.get(256) == 'SAT' else 'REFUTED or undecided')
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (CK, LOG))


def status():
    have = done()
    for t in TARGETS:
        st, lo, hi = bounds(name(t), have, t[1])
        print(name(t), 'last firing', lo, 'first silent', hi, 'calls', len(st))
    if os.path.exists(LOG):
        print(open(LOG).read()[-600:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run, 'report': report}[cmd]()
