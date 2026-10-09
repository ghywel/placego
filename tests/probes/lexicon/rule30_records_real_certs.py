#!/usr/bin/env python3
"""rule30_records_real_certs.py: RRC, DRAT certificates for the realizable records' deciding UNSAT calls (Cloud's CL084,
the owner's foundations audit: "no UNSAT verdict of RR, RR2 or RR3 has a checked certificate"). Local's run (chat L419),
with these predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat, drat-trim; RR's encoder rule30_records_real_sat.py); hours (the deep calls)
COMMAND:    python3 tests/probes/lexicon/rule30_records_real_certs.py run [JOBS=2]     (resumable; more processes may
            join with the same command: each depth is claimed by a lock file)
            python3 tests/probes/lexicon/rule30_records_real_certs.py status
            python3 tests/probes/lexicon/rule30_records_real_certs.py unlock          (clears stale locks after a crash)

For each decided depth d the deciding call is RR's query at L = R_real(d) + 1 (column 0 follows 0101 for times
0 .. d + L - 1, the time-0 cells at depths d .. d + L - 1 white, the whole light cone free). Its CNF is rebuilt by RR's
own `cnf` (the encoding RR, RR2 and RR3 share), kissat writes a binary DRAT proof, and drat-trim checks it. The
checkpoint line keeps d, L, both verdicts, the CNF's SHA-256 prefix, the proof's size and both times; the CNF and the
proof are then deleted (scratch only, ~/np-scratch-int/rule30-rr/certs; nothing in the repository). Rerunning rebuilds
identical CNFs, so anyone can regenerate a proof and compare hashes.
Depths and values: RR-C0's controls d = 3 .. 19 at ZR2's values, and RR2's decided d = 20 .. 97 (its OUTCOME table;
RR's decided depths 21, 25, .., 81 are among them, with the same values). RR3's depths are Cloud's (CL084 item 3).
The SAT side needs no certificate: RR and RR2 replayed every SAT witness by direct simulation (RR-C0, RR2-C1).
Order: the shallow depths first (3 .. 60, cheap), then the record-setting depths CL084 names (67, 83, 87, 93, 94), then
the rest of 61 .. 97.

PREDICTIONS (Local's, published before the run):
  RRC-C0 (control): d = 3 .. 19 re-solve UNSAT at ZR2(d) + 1 and verify (RR-C0's UNSAT half, now certified).
  RRC-P1 (blind, confidence 0.9): every deciding call d = 3 .. 97 re-solves UNSAT and drat-trim prints s VERIFIED.
  RRC-D1 (descriptive): proof sizes and checking times against solving times, by depth.
  Counterfactual: a deciding call that came back SAT, or a proof that failed to verify, would reopen R_real(d) at that
  depth, and RR2's climb at every later depth (it starts from R_real(d - 1) - 1, the plateau law) would be suspect.
"""
import hashlib
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_records_real_sat as rr                                  # noqa: E402
sys.argv = _argv

DIR = os.path.expanduser('~/np-scratch-int/rule30-rr/certs')
CK = os.path.join(DIR, 'rrc.ck')
RR2 = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 8, 8, 8, 8, 7, 7, 8, 8, 9, 9,             # d = 20 .. 40
       8, 9, 9, 8, 9, 11, 10, 11, 11, 10, 9, 11, 10, 10, 11, 12, 11, 10, 10, 9,          # 41 .. 60
       9, 12, 11, 12, 11, 10, 14, 13, 12, 11, 12, 11, 10, 10, 10, 10, 10, 11, 10, 10,    # 61 .. 80
       12, 11, 14, 13, 12, 13, 16, 15, 14, 13, 12, 12, 16, 17, 16, 15, 14]               # 81 .. 97
REAL = dict(rr.ZR2)
REAL.update({d: v for d, v in zip(range(20, 98), RR2)})
ORDER = list(range(3, 61)) + [67, 83, 87, 93, 94] + [d for d in range(61, 98) if d not in (67, 83, 87, 93, 94)]


def done():
    out = {}
    if os.path.exists(CK):
        for line in open(CK):
            p = line.split()
            if len(p) >= 8 and line.endswith('\n'):
                out[int(p[0])] = p
    return out


def certify(d):
    L = REAL[d] + 1
    lock = os.path.join(DIR, 'd%d.lock' % d)
    try:
        os.close(os.open(lock, os.O_CREAT | os.O_EXCL))
    except FileExistsError:
        return None
    try:
        nv, cl, row, T = rr.cnf(d, L)
        text = 'p cnf %d %d\n' % (nv, len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)
        sha = hashlib.sha256(text.encode()).hexdigest()[:16]
        cnf, proof = os.path.join(DIR, 'rrc_%d_%d.cnf' % (d, L)), os.path.join(DIR, 'rrc_%d_%d.drat' % (d, L))
        with open(cnf, 'w') as f:
            f.write(text)
        t0 = time.time()
        r = subprocess.run(['kissat', '-q', '-f', cnf, proof], capture_output=True, text=True)
        t1 = time.time()
        verdict = {20: 'UNSAT', 10: 'SAT'}.get(r.returncode, 'UNKNOWN%d' % r.returncode)
        size = os.path.getsize(proof) if os.path.exists(proof) else 0
        check = 'SKIPPED'
        if verdict == 'UNSAT':
            v = subprocess.run(['drat-trim', cnf, proof, '-t', '400000'], capture_output=True, text=True)
            lines = [l.replace('\r', '').strip() for l in v.stdout.splitlines()]
            check = 'VERIFIED' if 's VERIFIED' in lines else 'NOT-VERIFIED'
        t2 = time.time()
        line = '%d %d %s %s %s %d %.1f %.1f\n' % (d, L, verdict, check, sha, size, t1 - t0, t2 - t1)
        with open(CK, 'a') as f:
            f.write(line)
        for p in (cnf, proof):
            if os.path.exists(p):
                os.unlink(p)
        print(line, end='', flush=True)
        return line
    finally:
        os.unlink(lock)


def run(jobs):
    os.makedirs(DIR, exist_ok=True)
    have = done()
    todo = [d for d in ORDER if d not in have]
    with ThreadPoolExecutor(jobs) as ex:
        list(ex.map(certify, todo))
    status()


def status():
    have = done()
    ok = [d for d in have if have[d][2] == 'UNSAT' and have[d][3] == 'VERIFIED']
    bad = [d for d in have if d not in ok]
    print('certified %d of %d deciding calls; failures %s; missing %s' % (
        len(ok), len(ORDER), sorted(bad) or 'none', sorted(set(ORDER) - set(have)) or 'none'))
    if not bad and len(ok) == len(ORDER):
        print('RRC-C0', 'PASS' if all(d in ok for d in range(3, 20)) else 'FAIL')
        print('RRC-P1 HELD')
        print('COMPLETE')
    elif bad:
        print('RRC-C0', 'FAIL' if any(d in bad for d in range(3, 20)) else 'PASS so far')
        print('RRC-P1 REFUTED at d = %s' % sorted(bad))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'run':
        run(int(sys.argv[2]) if len(sys.argv) > 2 else 2)
    elif cmd == 'unlock':
        for f in os.listdir(DIR):
            if f.endswith('.lock'):
                os.unlink(os.path.join(DIR, f))
    else:
        status()
