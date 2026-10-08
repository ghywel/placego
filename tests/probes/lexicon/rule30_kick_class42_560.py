#!/usr/bin/env python3
"""rule30_kick_class42_560.py: KT2C, does class 42 die by N = 560? All 56 cases of KK's class-42 instance at N = 560,
each UNSAT certified by drat-trim (row 6.1; Cloud's KT-P3 against Local's KT2-P2; Local's claim in CLOUD-LOCAL.md
with these predictions pushed before the run).

RUN-ON:     cpu, 3 kissat/drat-trim processes beside RK; resumable
COMMAND:    python3 tests/probes/lexicon/rule30_kick_class42_560.py start | status | resume
COST:       to be recorded. kissat capped at 14,400 s per case; drat-trim at 20,000 s per proof.

Why now. KT2L (rule30_kick_strain_long.py) found class 42 UNSAT at N = 560 in all three cases that were SAT at
N = 336, each within minutes. If every one of the 56 cases is UNSAT at 560, no right side can make a class-42 kick
after 560 steps on the wheel, and by G206 (all-case UNSAT is monotone in N) none after any longer stretch either.

Each case: KK's CNF (rule30_kick_bite_kissat.instance), solved by kissat writing a text DRAT proof
(kissat -q -n -f --no-binary), and, if UNSAT, the proof checked by drat-trim against the same CNF; certified when
kissat exits 20 and drat-trim prints "s VERIFIED". A SAT answer is replayed by direct simulation. Proofs are written to
np-scratch and deleted once checked.

PREDICTIONS (Local's, published before the run):
  KT2C-C1 (control): the three cases KT2L found UNSAT, (t0 0, d 0, 2, 4), come back UNSAT with verified proofs.
  KT2C-C2 (control, the checker can say no): the case (0, 0) proof, checked against the CNF of the satisfiable
          instance class 42, N = 336, case (0, 0) (SAT in KT2), is NOT verified.
  KT2C-P1 (blind, confidence 0.6): all 56 cases are UNSAT at N = 560 with verified proofs, so class 42 dies by 560:
          Cloud's KT-P3 holds and Local's KT2-P2 is refuted.
  KT2C-P2 (blind): every case's kissat run finishes within 30 minutes.
OUTCOME, 2026-10-08 05:19 (M5; launched 04:35; checkpoint and log outside Git). Every one of the 56 cases is UNSAT
with a drat-trim verified proof; no SAT, no UNKNOWN. KT2C-C1 PASS (cases (0, 0), (0, 2), (0, 4) verified UNSAT).
KT2C-C2 PASS: the case (0, 0) proof checked against the satisfiable N = 336 CNF is not verified, so the checker
can say no. KT2C-P1 HELD: class 42 dies by N = 560, and by G206 after any longer stretch: Cloud's KT-P3 holds and
Local's KT2-P2 is refuted. KT2C-P2 HELD: kissat times 50 s to 443 s, median 87 s, total 5,734 s on 3 cores.
Classes 32 and 52 are untouched by this run (both SAT at 336, UNKNOWN at 560 under KT2L's 4-hour caps).
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv

SCRATCH = '/Volumes/extnvme/nframe-project/np-scratch/rule30-kt2c'
CK = os.path.join(SCRATCH, 'kt2c.ck')
LOG = os.path.join(SCRATCH, 'kt2c.log')
CAP, DCAP, JOBS, P = 14400, 20000, 3, kk.P
CASES = [(t0, d) for t0 in (0, 1) for d in range(0, P, 2)]


def done():
    out = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 6 and f[-1] == 'END':
                out[int(f[0]), int(f[1])] = (f[2], f[3], float(f[4]))
    return out


def record(t0, d, verdict, extra, secs):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:
            with open(CK, 'a') as f:
                f.write('\n')
    with open(CK, 'a') as f:
        f.write('%d %d %s %s %.1f END\n' % (t0, d, verdict, extra, secs))


def write_cnf(N, a, t0, d, path):
    nv, clauses, row, s, E = kk.instance(t0, d, a, N)
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    return row, s, E


def certify(t0, d, against=None):
    tag = '%d_%d' % (t0, d)
    cnf = os.path.join(SCRATCH, 'c_%s.cnf' % tag)
    prf = os.path.join(SCRATCH, 'c_%s.drat' % tag)
    row, s, E = write_cnf(560, 42, t0, d, cnf)
    t = time.time()
    r = subprocess.run(['kissat', '-q', '-n', '-f', '--no-binary', '--time=%d' % CAP, cnf, prf],
                       capture_output=True, text=True)
    secs = time.time() - t
    if r.returncode == 10:
        val = set()
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                val.update(int(x) for x in line[2:].split())
        ok = kk.replay(t0, d, s, E, [1 if x in val else 0 for x in row])
        verdict, extra = 'SAT', 'replay-pass' if ok else 'replay-FAIL'
    elif r.returncode == 20:
        target = cnf
        if against is not None:
            target = os.path.join(SCRATCH, 'against.cnf')
            write_cnf(*against, target)
        v = subprocess.run(['drat-trim', target, prf, '-t', str(DCAP)], capture_output=True, text=True)
        verdict, extra = 'UNSAT', 'VERIFIED' if 's VERIFIED' in v.stdout else 'not-verified'
        if against is not None:
            os.unlink(target)
    else:
        verdict, extra = 'UNKNOWN', 'rc%d' % r.returncode
    for p in (cnf, prf):
        if os.path.exists(p):
            os.unlink(p)
    return verdict, extra, secs


def run():
    os.makedirs(SCRATCH, exist_ok=True)
    c2 = certify(0, 0, against=(336, 42, 0, 0))
    print('KT2C-C2 control: case (0, 0) proof against the satisfiable N = 336 CNF: %s %s' % (c2[0], c2[1]), flush=True)
    todo = [c for c in CASES if c not in done()]

    def one(c):
        v, e, s = certify(*c)
        record(c[0], c[1], v, e, s)
        print('%s case (%d, %d): %s %s %.0f s' % (time.strftime('%H:%M:%S'), c[0], c[1], v, e, s), flush=True)

    with ThreadPoolExecutor(JOBS) as ex:
        list(ex.map(one, todo))
    have = done()
    c1 = all(have.get((0, d), ('',))[0] == 'UNSAT' and have[0, d][1] == 'VERIFIED' for d in (0, 2, 4))
    allu = all(have.get(c, ('',))[0] == 'UNSAT' and have[c][1] == 'VERIFIED' for c in CASES)
    fast = all(have[c][2] <= 1800 for c in CASES if c in have)
    print('cases: %d; UNSAT verified: %d; SAT: %d; UNKNOWN: %d' % (len(have),
          sum(1 for v in have.values() if v[0] == 'UNSAT' and v[1] == 'VERIFIED'),
          sum(1 for v in have.values() if v[0] == 'SAT'), sum(1 for v in have.values() if v[0] == 'UNKNOWN')))
    print('KT2C-C1', 'PASS' if c1 else 'FAIL')
    print('KT2C-C2', 'PASS' if c2[0] == 'UNSAT' and c2[1] != 'VERIFIED' else 'FAIL %s' % (c2,))
    print('KT2C-P1', 'HELD' if allu else 'REFUTED')
    print('KT2C-P2', 'HELD' if fast else 'REFUTED')
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (CK, LOG))


def status():
    print('%d of %d cases checkpointed' % (len(done()), len(CASES)))
    if os.path.exists(LOG):
        print(open(LOG).read()[-1500:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run}[cmd]()
