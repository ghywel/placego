#!/usr/bin/env python3
"""rule30_kick_bite_drat.py: DT, certificates for the class-12 bite. Every UNSAT verdict that KS and KK report for
class 12 at N = 140 and N = 168 is re-solved by kissat with a DRAT proof, and each proof is checked by drat-trim
(Local's run; the owner installed poppler and authorised drat-trim on 2026-10-07; claimed in CLOUD-LOCAL.md with
these predictions pushed before the run).

RUN-ON:     cpu; kissat and drat-trim on the PATH (drat-trim built from github.com/marijnheule/drat-trim at 2e3b2dc)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_bite_drat.py [JOBS=8] [PROOFDIR=/tmp]
COST:       minutes to an hour (to be recorded); proofs are written to PROOFDIR and deleted once checked.

The instances are KK's (rule30_kick_bite_kissat.instance): class 12, N in {140, 168}, t0 in {0, 1}, the 28 even
phases, 112 in all. For each, kissat writes a DRAT proof, and drat-trim checks it against the same CNF. A verdict is
certified when kissat exits 20 and drat-trim reports "s VERIFIED".

PREDICTIONS (Local's, published before the run):
  DT-C1 (control, the checker can say no): the class-12 proof for (t0 0, d 0, N 140), checked against the CNF of the
         satisfiable class-32 instance with the same (t0, d) at N = 168, is NOT verified (a satisfiable formula has no
         refutation; a cut-down proof was rejected as a control because a trivial formula verifies from a single
         lemma, seen in a smoke on a 2-variable formula).
  DT-C2 (control): one satisfiable instance (class 32, N = 168, t0 = 0, d = 0) exits 10 and writes no refutation.
  DT-P1: all 112 class-12 instances at N = 140 and 168 are UNSAT, with proofs that drat-trim verifies.
OUTCOME, 2026-10-07 21:47 (M5, one run at commit b1ddf91, 35 s with 8 jobs; proofs written to np-scratch and deleted
once checked). DT-C2 PASS: the class-32 instance exits 10. DT-C1 PASS: the class-12 proof for (t0 0, d 0, N 140),
checked against the satisfiable class-32 CNF, is not verified. DT-P1 HELD: all 112 class-12 instances at N = 140 and
168 are UNSAT, and drat-trim verifies every proof. With GPT's monotonicity argument (GC373: all-case UNSAT is monotone
in N), the certified N = 140 case covers every N >= 140.
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv

JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 8
PROOFDIR = sys.argv[2] if len(sys.argv) > 2 else tempfile.gettempdir()


def write_cnf(args, path):
    t0, d, a, N = args
    nv, clauses, row, s, E = kk.instance(t0, d, a, N)
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')


def certify(args, against=None):
    """solve args with a DRAT proof and check it; with against = other instance args, check the proof against that
    instance's CNF instead (the negative control)."""
    tag = 'c%d_N%d_t%d_d%d' % (args[2], args[3], args[0], args[1])
    cnf = os.path.join(PROOFDIR, tag + '.cnf')
    prf = os.path.join(PROOFDIR, tag + '.drat')
    write_cnf(args, cnf)
    r = subprocess.run(['kissat', '-q', '-n', '-f', '--no-binary', cnf, prf], capture_output=True, text=True)
    out = {'tag': tag, 'kissat': r.returncode, 'verified': False}
    if r.returncode == 20:
        target = cnf
        if against is not None:
            target = os.path.join(PROOFDIR, tag + '.against.cnf')
            write_cnf(against, target)
        v = subprocess.run(['drat-trim', target, prf, '-t', '20000'], capture_output=True, text=True)
        out['verified'] = 's VERIFIED' in v.stdout
        if against is not None:
            os.unlink(target)
    for p in (cnf, prf):
        if os.path.exists(p):
            os.unlink(p)
    return out


def main():
    c2 = certify((0, 0, 32, 168))
    print('DT-C2', 'PASS' if c2['kissat'] == 10 else 'FAIL', c2, flush=True)
    c1 = certify((0, 0, 12, 140), against=(0, 0, 32, 168))
    print('DT-C1', 'PASS' if c1['kissat'] == 20 and not c1['verified'] else 'FAIL', c1, flush=True)
    cases = [(t0, d, 12, N) for N in (140, 168) for t0 in (0, 1) for d in range(0, kk.P, 2)]
    with ThreadPoolExecutor(JOBS) as ex:
        res = list(ex.map(certify, cases))
    unsat = sum(1 for r in res if r['kissat'] == 20)
    ver = sum(1 for r in res if r['verified'])
    bad = [r['tag'] for r in res if not (r['kissat'] == 20 and r['verified'])]
    print('class 12, N 140 and 168: %d instances, UNSAT %d, drat-trim VERIFIED %d; not certified: %s'
          % (len(res), unsat, ver, bad[:6]), flush=True)
    print('DT-P1', 'HELD' if unsat == 112 and ver == 112 else 'REFUTED')


if __name__ == '__main__':
    main()
