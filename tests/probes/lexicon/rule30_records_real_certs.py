#!/usr/bin/env python3
"""rule30_records_real_certs.py: RRC, DRAT certificates for the realizable records' deciding UNSAT calls (Cloud's CL084,
the owner's foundations audit: "no UNSAT verdict of RR, RR2 or RR3 has a checked certificate"). Local's run (chat L419),
with these predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat, drat-trim; RR's encoder rule30_records_real_sat.py); hours (the deep calls)
COMMAND:    python3 tests/probes/lexicon/rule30_records_real_certs.py run [JOBS=2]     (resumable; more processes may
            join with the same command: each depth is claimed by a lock file)
            python3 tests/probes/lexicon/rule30_records_real_certs.py status
            python3 tests/probes/lexicon/rule30_records_real_certs.py retry [JOBS]    (re-runs depths with no certified
            receipt; every earlier receipt stays in the checkpoint)
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
Hardening (GPT's GC791 and GC795 audits, applied 2026-10-09; the instrument is unchanged): a receipt
is read only if it has the full schema and L = R_real(d) + 1; a torn last line is closed before the next append; `run`
skips only certified depths and leaves failures to an explicit `retry`, which keeps the history; a failed call keeps
its CNF, proof and the solver's and checker's output tails (diag_d_L.txt); new receipts carry drat-trim's return code
as a ninth field (the first process's receipts have eight). A SAT verdict would reopen the record; an UNKNOWN verdict
or a failed check leaves that depth unresolved, not refuted. Only nine-field receipts certify (GC795: the first
process's eight-field receipts lack the checker's exit status, so it was stopped at 15:0x and its depths redone), and any
SAT receipt in the history blocks completion until diagnosed.
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


def receipts():
    """Every well-formed receipt, in order: d L verdict check sha size solve_s check_s [checker_rc]."""
    out = []
    if not os.path.exists(CK):
        return out
    for line in open(CK):
        if not line.endswith('\n'):
            continue
        p = line.split()
        if len(p) not in (8, 9):
            continue
        try:
            d, L, size, a, b = int(p[0]), int(p[1]), int(p[5]), float(p[6]), float(p[7])
            rc = int(p[8]) if len(p) == 9 else None
        except ValueError:
            continue
        if d not in REAL or L != REAL[d] + 1 or len(p[4]) != 16:
            continue
        if p[2] not in ('UNSAT', 'SAT') and not p[2].startswith('UNKNOWN'):
            continue
        if p[3] not in ('VERIFIED', 'NOT-VERIFIED', 'SKIPPED'):
            continue
        out.append(p)
    return out


def done():
    """The certified depths: a nine-field receipt that is UNSAT, VERIFIED and has checker return code 0. Eight-field
    receipts (the first process, before GC791) lack the checker's exit status and do not count (GC795)."""
    return {int(p[0]): p for p in receipts() if len(p) == 9 and p[2] == 'UNSAT' and p[3] == 'VERIFIED' and p[8] == '0'}


def append(line):
    with open(CK, 'a+') as f:
        f.seek(0, 2)
        if f.tell() > 0:
            f.seek(f.tell() - 1)
            if f.read(1) != '\n':
                f.write('\n')
        f.write(line)


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
        check, rc, vout = 'SKIPPED', -1, ''
        if verdict == 'UNSAT':
            v = subprocess.run(['drat-trim', cnf, proof, '-t', '400000'], capture_output=True, text=True)
            lines = [l.replace('\r', '').strip() for l in v.stdout.splitlines()]
            check = 'VERIFIED' if 's VERIFIED' in lines else 'NOT-VERIFIED'
            rc, vout = v.returncode, v.stdout + v.stderr
        t2 = time.time()
        line = '%d %d %s %s %s %d %.1f %.1f %d\n' % (d, L, verdict, check, sha, size, t1 - t0, t2 - t1, rc)
        append(line)
        if verdict == 'UNSAT' and check == 'VERIFIED' and rc == 0:
            for p in (cnf, proof):
                if os.path.exists(p):
                    os.unlink(p)
        else:
            with open(os.path.join(DIR, 'diag_%d_%d.txt' % (d, L)), 'w') as f:
                f.write('kissat rc %d\n%s\n%s\n--- drat-trim rc %d\n%s\n' % (
                    r.returncode, r.stdout[-4000:], r.stderr[-4000:], rc, vout.replace('\r', '')[-8000:]))
        print(line, end='', flush=True)
        return line
    finally:
        os.unlink(lock)


def run(jobs, retry=False):
    os.makedirs(DIR, exist_ok=True)
    have, tried = done(), {int(p[0]) for p in receipts() if len(p) == 9}
    todo = [d for d in ORDER if d not in have and (retry or d not in tried)]
    with ThreadPoolExecutor(jobs) as ex:
        list(ex.map(certify, todo))
    status()


def status():
    ok = done()
    tried, legacy = {}, set()
    for p in receipts():
        if len(p) == 8:
            legacy.add(int(p[0]))
            if p[2] != 'SAT':
                continue                               # a legacy SAT receipt still counts as a conflict below
        tried.setdefault(int(p[0]), []).append(p)
    sat = sorted(d for d in tried if any(p[2] == 'SAT' for p in tried[d]))
    unresolved = sorted(d for d in tried if d not in ok and d not in sat)
    missing = sorted(set(ORDER) - set(tried))
    print('certified %d of %d deciding calls; SAT (would reopen the record) %s; unresolved (UNKNOWN or failed check) '
          '%s; not yet tried %s' % (len(ok), len(ORDER), sat or 'none', unresolved or 'none', missing or 'none'))
    print('legacy eight-field receipts (no checker exit status; not counted): %d depths' % len(legacy))
    if sat:
        print('CONFLICT: SAT receipts at d = %s; no completion while any SAT history stands (GC795)' % sat)
    if len(ok) == len(ORDER) and not sat:
        print('RRC-C0 PASS')
        print('RRC-P1 HELD')
        print('COMPLETE')
    elif sat or unresolved:
        print('RRC-C0', 'NOT PASSED' if any(d in sat or d in unresolved for d in range(3, 20)) else 'PASS so far')
        print('RRC-P1 not held at d = %s (SAT: a refutation of the record there; otherwise unresolved)' % (
            sorted(sat + unresolved)))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd in ('run', 'retry'):
        run(int(sys.argv[2]) if len(sys.argv) > 2 else 2, retry=cmd == 'retry')
    elif cmd == 'unlock':
        for f in os.listdir(DIR):
            if f.endswith('.lock'):
                os.unlink(os.path.join(DIR, f))
    else:
        status()
