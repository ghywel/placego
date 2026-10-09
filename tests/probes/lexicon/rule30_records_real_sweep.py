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
OUTCOME, 2026-10-09 11:49 BST (M5, one kissat process; began 2026-10-08, restarted from its checkpoint on the internal
disk after the external drive dropped that evening; 308 calls, 23 of them capped):
  RR2-C0 PASS (every depth RR decided agrees). RR2-C1 PASS (the plateau law at every consecutive decided pair, every
  SAT witness replayed).
  RR2-P1 HELD: R_real(d) <= 20 at every decided depth (d = 20 .. 97). RR2-P2 HELD: the largest over d = 61 .. 120 is
  17 (d = 94), against 15 over d = 21 .. 60 (d = 21).
  R_real(d), d = 20 .. 120 (+ marks a lower bound from a capped call):
  20:16 21:15 22:14 23:13 24:12 25:11 26:10 27:9 28:8 29:7 30:8 31:8 32:8 33:8 34:8 35:7 36:7 37:8 38:8 39:9 40:9
  41:8 42:9 43:9 44:8 45:9 46:11 47:10 48:11 49:11 50:10 51:9 52:11 53:10 54:10 55:11 56:12 57:11 58:10 59:10 60:9
  61:9 62:12 63:11 64:12 65:11 66:10 67:14 68:13 69:12 70:11 71:12 72:11 73:10 74:10 75:10 76:10 77:10 78:11 79:10
  80:10 81:12 82:11 83:14 84:13 85:12 86:13 87:16 88:15 89:14 90:13 91:12 92:12 93:16 94:17 95:16 96:15 97:14
  98:14+ 99:13+ 100:15+ 101:14+ 102:14+ 103:13+ 104:12+ 105:12+ 106:12+ 107:13+ 108:14+ 109:14+ 110:14+ 111:14+
  112:14+ 113:14+ 114:13+ 115:12+ 116:13+ 117:13+ 118:13+ 119:13+ 120:13+
  From d = 98 every depth stopped at a 1,800 s cap, so those are lower bounds only. The decided record climbs slowly
  and unevenly (local peaks 16 at 87, 17 at 94), well under the free-column-1 records; no growth law is claimed.
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
