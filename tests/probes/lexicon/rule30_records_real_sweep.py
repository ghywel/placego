#!/usr/bin/env python3
"""rule30_records_real_sweep.py: RR2, the realizable records R_real(d) at every depth from 20 to 120 (row Q6, Local's
block; the step L247 offered). Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one kissat process; resumable
COMMAND:    python3 tests/probes/lexicon/rule30_records_real_sweep.py start | status | resume
COST:       to be recorded; likely a day or more on one core (the deep UNSAT calls take tens of minutes).

The question per call is RR's (rule30_records_real_sat.py): is there a configuration whose column 0 follows 0101 for
times 0 .. d + L - 1 and whose time-0 cells at depths d .. d + L - 1 are white? The climb at depth d starts at
L = R_real(d - 1) - 1, which the plateau law guarantees (a run from d - 1 of length R gives one from d of length
R - 1), and goes up until UNSAT. Each call is capped at 1,800 s. A capped call stops that depth with a lower bound.
Every finished call is written to a checkpoint line, so a restart resumes where it stopped.
Convention (CL041, L286): R_real here is the maximum over both phases (RR's encoding has a phase variable), while
section 8.36's R(d) is the phase-0 record; Cloud's CL038 gives per-phase values at d = 21 .. 41.

PREDICTIONS (Local's, published before the run):
  RR2-C0 (control): wherever RR decided a depth (21, 25, .., 41, 49, .., 81), RR2 gives the same value.
  RR2-C1 (control): the plateau law, R_real(d + 1) >= R_real(d) - 1, at every consecutive decided pair; every SAT
         witness checks by direct simulation.
  RR2-P1 (blind): R_real(d) <= 20 at every decided depth up to 120.
  RR2-P2 (blind, uncertain): the largest R_real over d = 61 .. 120 exceeds the largest over d = 21 .. 60 (a slow
         rise rather than a ceiling).
OUTCOME: not yet run.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_records_real_sat as rr
sys.argv = _argv

rr.TIMEOUT = 1800
SCRATCH = rr.SCRATCH
CK = os.path.join(SCRATCH, 'rr2.ck')
LOG = os.path.join(SCRATCH, 'rr2.log')
RR = {21: 15, 25: 11, 29: 7, 33: 8, 37: 8, 41: 8, 49: 11, 57: 11, 65: 11, 73: 10, 81: 12}


def calls():
    out = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 6 and f[-1] == 'END':
                out[int(f[0]), int(f[1])] = (f[2], f[3] == 'True', float(f[4]))
    return out


def record(d, L, verdict, ok, secs):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:
            with open(CK, 'a') as f:
                f.write('\n')
    with open(CK, 'a') as f:
        f.write('%d %d %s %s %.1f END\n' % (d, L, verdict, ok, secs))


def depth(d, start, have):
    """climb from start; returns (R or None, lower bound)"""
    L = max(1, start)
    while True:
        if (d, L) in have:
            verdict, ok, _ = have[d, L]
        else:
            _, _, verdict, secs, ok = rr.solve((d, L))
            record(d, L, verdict, bool(ok), secs)
            print('d %d L %d %s %.1f s %s' % (d, L, verdict, secs, ok), flush=True)
        if verdict == 'SAT':
            if not ok:
                return None, L - 1
            L += 1
            continue
        return (L - 1 if verdict == 'UNSAT' else None), L - 1


def run():
    os.makedirs(SCRATCH, exist_ok=True)
    known = dict(rr.ZR2)
    lower = {}
    for d in range(20, 121):
        have = calls()
        prev = known.get(d - 1, lower.get(d - 1, 1))
        R, lo = depth(d, prev - 1, have)
        if R is not None:
            known[d] = R
        else:
            lower[d] = lo
    decided = {d: v for d, v in known.items() if d >= 20}
    c0 = all(known.get(d) == v for d, v in RR.items())
    c1 = all(known[d + 1] >= known[d] - 1 for d in known if d + 1 in known)
    c1 &= all(ok for (verdict, ok, _) in calls().values() if verdict == 'SAT')
    p1 = all(v <= 20 for v in decided.values())
    hi = max([v for d, v in decided.items() if 61 <= d <= 120] + [lower.get(d, 0) for d in range(61, 121)])
    lo_max = max(v for d, v in decided.items() if 21 <= d <= 60)
    print('R_real, d = 20 .. 120 (a trailing + marks a lower bound):')
    print(' '.join('%d:%s' % (d, known[d] if d in known else '%d+' % lower[d]) for d in range(20, 121)))
    print('RR2-C0', 'PASS' if c0 else 'FAIL')
    print('RR2-C1', 'PASS' if c1 else 'FAIL')
    print('RR2-P1', 'HELD' if p1 else 'REFUTED')
    print('RR2-P2', 'HELD' if hi > lo_max else 'REFUTED', '(max 61..120: %d, max 21..60: %d)' % (hi, lo_max))
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (CK, LOG))


def status():
    have = calls()
    print('%d calls checkpointed; deepest depth %s' % (len(have), max((d for d, _ in have), default=None)))
    if os.path.exists(LOG):
        print(open(LOG).read()[-800:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run}[cmd]()
