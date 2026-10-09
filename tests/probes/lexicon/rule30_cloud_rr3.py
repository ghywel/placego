#!/usr/bin/env python3
"""rule30_cloud_rr3.py: RR3, deciding RR2's capped depths 98 .. 120 of the realizable records R_real(d) (row Q6).

RUN-ON:     cpu, four kissat processes at a time (KISSAT names the binary; kissat 4.0.4 built from source here)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_rr3.py start | status | resume     [JOBS=4] [CAP=10800]
COST:       unknown in advance; each call is capped at CAP seconds (three hours by default). Resumable.

Why. The owner asked Cloud to pick a task that needs compute and suits this machine (four 2.1 GHz cores, 15 GB, no
GPU). RR2 (Local's rule30_records_real_sweep.py, M5, one kissat process, 1,800 s cap) decided R_real(d) for
d = 20 .. 97. Every call from d = 98 hit its cap, so 98 .. 120 are lower bounds only, and GPT's qualifier (GC764)
notes they could exceed the decided maximum, 17 at d = 94. RR2 is finished and no one is running these depths. RR3
continues RR2's climb there with a cap six times longer, on four cores at once.

The query is RR's, unchanged (rule30_records_real_sat.py: cnf and check are imported): is there a configuration whose
column 0 follows 0101 (either phase) for times 0 .. d + L - 1 and whose time-0 cells at depths d .. d + L - 1 are white?
SAT at L means R_real(d) >= L; R_real(d) is the largest SAT L. Each depth starts at RR2's lower bound plus one and
climbs: SAT moves to L + 1, UNSAT decides R_real(d) = L - 1, a capped call leaves a lower bound. Every SAT row is
checked by direct simulation. Calls run four at a time; every finished call is written to a checkpoint outside git.

PREDICTIONS, written 2026-10-09 13:57 BST, before any run of this script. A smoke test of solve() alone, at
depths 13 and 21 (outside the predicted range), reproduced ZR2's 4 and RR's 15, SAT at the record and UNSAT
one above, with every witness checked; it took under a second.
  RR3-C0 (control, run first): d = 97 reproduces RR2: SAT at L = 14 with a witness that checks, UNSAT at L = 15.
  RR3-C1 (control): the plateau law, R_real(d + 1) >= R_real(d) - 1, at every consecutive decided pair, RR2's values
         included; and every SAT witness's column 1 has no 11 among its white-clock samples (two lines: if column 1
         is black at a white-clock row t, it is black at t + 1, so at t + 2 it is the NOR of a black cell, white).
  RR3-P1 (blind, 0.6): every depth RR3 decides has R_real(d) <= 17, so the decided maximum stays d = 94's 17.
  RR3-P2 (blind, cost, 0.5): fewer than half of the 23 capped depths are decided in the first 12 hours of the run.
  RR3-P3 (the unexpected check, 0.6): the deciding (UNSAT) call times are not monotone in d: some newly decided
         depth takes less than half as long as a decided depth below it.
  Counterfactual. If some depth has R_real(d) >= 18, the slow rise RR2 saw continues past 94 and the growth
  question sharpens. If every decided depth is at most 17, with values near RR2's lower bounds, the decided record is
  consistent with a ceiling near 17. Neither would settle Q6, which asks about every depth.
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_records_real_sat as rr
sys.argv = _argv

MODE = sys.argv[1] if len(sys.argv) > 1 else 'status'
JOBS = int(sys.argv[2]) if len(sys.argv) > 2 else 4
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 10800
KISSAT = os.environ.get('KISSAT', 'kissat')
SCRATCH = os.environ.get('NP_SCRATCH_RR3', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-rr3'))
CK = os.path.join(SCRATCH, 'rr3.ck')
RR2 = {20: 16, 21: 15, 22: 14, 23: 13, 24: 12, 25: 11, 26: 10, 27: 9, 28: 8, 29: 7, 30: 8, 31: 8, 32: 8, 33: 8,
       34: 8, 35: 7, 36: 7, 37: 8, 38: 8, 39: 9, 40: 9, 41: 8, 42: 9, 43: 9, 44: 8, 45: 9, 46: 11, 47: 10, 48: 11,
       49: 11, 50: 10, 51: 9, 52: 11, 53: 10, 54: 10, 55: 11, 56: 12, 57: 11, 58: 10, 59: 10, 60: 9, 61: 9, 62: 12,
       63: 11, 64: 12, 65: 11, 66: 10, 67: 14, 68: 13, 69: 12, 70: 11, 71: 12, 72: 11, 73: 10, 74: 10, 75: 10,
       76: 10, 77: 10, 78: 11, 79: 10, 80: 10, 81: 12, 82: 11, 83: 14, 84: 13, 85: 12, 86: 13, 87: 16, 88: 15,
       89: 14, 90: 13, 91: 12, 92: 12, 93: 16, 94: 17, 95: 16, 96: 15, 97: 14}
LOWER = {98: 14, 99: 13, 100: 15, 101: 14, 102: 14, 103: 13, 104: 12, 105: 12, 106: 12, 107: 13, 108: 14, 109: 14,
         110: 14, 111: 14, 112: 14, 113: 14, 114: 13, 115: 12, 116: 13, 117: 13, 118: 13, 119: 13, 120: 13}


def solve(d, L):
    nv, cl, row, T = rr.cnf(d, L)
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, 'rr3_%d_%d.cnf' % (d, L))
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(cl)))
        for c in cl:
            f.write(' '.join(map(str, c)) + ' 0\n')
    t0 = time.time()
    r = subprocess.run([KISSAT, '-q', '--time=%d' % CAP, path], capture_output=True, text=True)
    secs = time.time() - t0
    os.unlink(path)
    if r.returncode == 20:
        return 'UNSAT', secs, True
    if r.returncode != 10:
        return 'UNKNOWN', secs, True
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    bits = [1 if x in val else 0 for x in row]
    return 'SAT', secs, rr.check(bits, T, d, L) and no11(bits, T)


def no11(row, T):
    """column 1 of the witness has no 11 among its white-clock samples (RR3-C1's two-line law)"""
    cur, off = [0, 0] + row + [0, 0], T + 2
    c0, c1 = [cur[off]], [cur[off + 1]]
    for t in range(1, T + 1):
        cur = [0] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
        c0.append(cur[off])
        c1.append(cur[off + 1])
    white = [t for t in range(T + 1) if c0[t] == 0]
    return not any(c1[t] and t + 2 <= T and c1[t + 2] for t in white)


def calls():
    out = []
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 6 and f[-1] == 'END':
                out.append((int(f[0]), int(f[1]), f[2], f[3] == 'True', float(f[4])))
    return out


def record(d, L, verdict, ok, secs):
    os.makedirs(SCRATCH, exist_ok=True)
    with open(CK, 'a') as f:
        f.write('%d %d %s %s %.1f END\n' % (d, L, verdict, ok, secs))
        f.flush()
        os.fsync(f.fileno())


def state():
    """per depth: ('decided', R) or ('open', next L) or ('capped', lower bound), from the checkpoint"""
    st = {97: ('open', 14)}
    st.update({d: ('open', lo + 1) for d, lo in LOWER.items()})
    for d, L, v, ok, secs in calls():
        if d not in st or st[d][0] != 'open' or st[d][1] != L:
            continue
        if v == 'SAT' and ok:
            st[d] = ('open', L + 1)
        elif v == 'UNSAT':
            st[d] = ('decided', L - 1)
        else:
            st[d] = ('capped', L - 1)
    return st


def status():
    st = state()
    print('RR3 checkpoint:', CK)
    for d in sorted(st):
        print('  d %d: %s %s' % (d, st[d][0], st[d][1]))
    for c in calls():
        print('  call', c)


def run():
    st = state()
    queue = [d for d in sorted(st) if st[d][0] == 'open']          # 97 first (the control), then 98 .. 120
    running = {}
    with ThreadPoolExecutor(JOBS) as ex:
        while queue or running:
            while queue and len(running) < JOBS:
                d = queue.pop(0)
                L = state()[d][1]
                running[ex.submit(solve, d, L)] = (d, L)
            done, _ = wait(running, return_when=FIRST_COMPLETED)
            for fut in done:
                d, L = running.pop(fut)
                verdict, secs, ok = fut.result()
                record(d, L, verdict, ok, secs)
                print('%s d %d L %d: %s ok=%s %.0f s' % (time.strftime('%H:%M:%S'), d, L, verdict, ok, secs),
                      flush=True)
                if verdict == 'SAT' and ok:
                    queue.insert(0, d)                                 # climb this depth next
    status()


if __name__ == '__main__':
    if MODE in ('start', 'resume'):
        run()
    else:
        status()
