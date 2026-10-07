#!/usr/bin/env python3
"""rule30_kick_alphabet_exact.py: KX, the exact kick alphabet after 140 steps on the wheel (row 6.1, drawn under
draw-and-work; Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before the run).

RUN-ON:     cpu; kissat and drat-trim on the PATH
COMMAND:    python3 tests/probes/lexicon/rule30_kick_alphabet_exact.py [JOBS=8] [PROOFDIR=/tmp]
COST:       minutes to an hour (to be recorded).

Entry 26 (KL) bounds the kicks from above with a 16-column automaton: after a settled wheel, class 12: +4..+8,
32: +2..+6, 42: +1..+5, 52: -6..-1. KS, KK and DT showed that at full width class 12 is impossible after 140
steps. KX asks the same full-width question size by size: for class a in {32, 42, 52} and each size k of KL's
alphabet, is there a row (t0 in {0, 1}, an even phase d) such that column 1 follows U at phase d for N = 140 steps,
departs at the first class-a time s >= t0 + 140, and follows U at a new even phase d' with kick k, where kick(d' - d)
= -17 (d' - d)/2 mod 28 signed into -14 .. 13 (KL's convention), for 21 observations? The encoding is KK's
(rule30_kick_bite_kissat.instance) with the new-phase selectors restricted to the d' of kick k. A SAT answer is
replayed by direct simulation; an UNSAT answer for all 56 (t0, d) cases is certified with drat-trim.

PREDICTIONS (Local's, published before the run; blind unless marked):
  KX-C1 (control): every SAT answer replays, and every UNSAT proof verifies.
  KX-C2 (control): sizes outside KL's alphabet are impossible: class 32 with kick +7 and class 52 with kick +1 are
        UNSAT at all 56 cases (KL's settled automaton excludes them, and full width only removes solutions).
  KX-P1 (blind): every size of the measured alphabets (class 32: +2..+6; class 52: -6..-1) is SAT at some case.
  KX-P2 (blind, uncertain): at least one size of class 42's KL alphabet (+1..+5) is UNSAT at full width.
OUTCOME: not yet run.
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

U, P = kk.U, kk.P
JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 8
PROOFDIR = sys.argv[2] if len(sys.argv) > 2 else tempfile.gettempdir()
N = 140


def kick_of(delta):
    k = (-17 * ((delta % P) // 2)) % 28
    return k if k < 14 else k - 28


def instance_sized(t0, d, a, k):
    """KK's instance, but the new phase must give kick k; returns None when no eligible d' gives kick k."""
    nv, clauses, row, s, E = kk.instance(t0, d, a, N)
    eligible = [dn for dn in range(0, P, 2) if U[(s - dn) % P] != U[(s - d) % P]]
    keep = [dn for dn in eligible if kick_of(dn - d) == k]
    if not keep:
        return None
    # KK appended one selector per eligible d' (in order) and then their disjunction as the last clause.
    sels = clauses[-1]
    assert len(sels) == len(eligible)
    allowed = {sel for sel, dn in zip(sels, eligible) if dn in keep}
    clauses = clauses[:-1] + [[sel for sel in sels if sel in allowed]]
    return nv, clauses, row, s, E, keep


def replay_k(t0, d, s, E, rowbits, keep):
    """direct simulation of the row at t0: column 1 on U at phase d over [t0, s), and on U at one of the phases in
    keep (the new phases of kick k) over [s, E]."""
    cur = [t0 % 2] + list(rowbits) + [0]
    col1 = {t0: cur[1]}
    for t in range(t0 + 1, E + 1):
        cur = [t % 2] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
        col1[t] = cur[1]
    if any(col1[t] != U[(t - d) % P] for t in range(t0, s)):
        return False
    return any(all(col1[t] == U[(t - dn) % P] for t in range(s, E + 1)) for dn in keep)


def solve(args):
    t0, d, a, k = args
    inst = instance_sized(t0, d, a, k)
    if inst is None:
        return (args, 'NONE', True)
    nv, clauses, row, s, E, keep = inst
    tag = 'kx_a%d_k%d_t%d_d%d' % (a, k, t0, d)
    cnf, prf = os.path.join(PROOFDIR, tag + '.cnf'), os.path.join(PROOFDIR, tag + '.drat')
    with open(cnf, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    r = subprocess.run(['kissat', '-q', '-f', '--no-binary', cnf, prf], capture_output=True, text=True)
    if r.returncode == 10:
        val = set()
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                val.update(int(x) for x in line[2:].split())
        ok = replay_k(t0, d, s, E, [1 if x in val else 0 for x in row], keep)
        res = (args, 'SAT', ok)
    elif r.returncode == 20:
        v = subprocess.run(['drat-trim', cnf, prf, '-t', '20000'], capture_output=True, text=True)
        res = (args, 'UNSAT', 's VERIFIED' in v.stdout)
    else:
        res = (args, 'ERROR %d' % r.returncode, False)
    for p in (cnf, prf):
        if os.path.exists(p):
            os.unlink(p)
    return res


def run(a, k, ex):
    res = list(ex.map(solve, [(t0, d, a, k) for t0 in (0, 1) for d in range(0, P, 2)]))
    sat = sum(1 for r in res if r[1] == 'SAT')
    checked = all(r[2] for r in res)
    err = any(r[1].startswith('ERROR') for r in res)
    print('class %d kick %+d: SAT at %d of 56 cases; all answers checked: %s%s' % (a, k, sat, checked,
          '; SOLVER ERROR' if err else ''), flush=True)
    return sat, checked and not err


def main():
    alpha = {32: [2, 3, 4, 5, 6], 52: [-6, -5, -4, -3, -2, -1], 42: [1, 2, 3, 4, 5]}
    table, okall = {}, True
    with ThreadPoolExecutor(JOBS) as ex:
        for a, ks in alpha.items():
            for k in ks:
                table[(a, k)], ok = run(a, k, ex)
                okall &= ok
        c2a, ok1 = run(32, 7, ex)
        c2b, ok2 = run(52, 1, ex)
        okall &= ok1 and ok2
    print('KX-C1', 'PASS' if okall else 'FAIL')
    print('KX-C2', 'PASS' if c2a == 0 and c2b == 0 else 'FAIL')
    print('KX-P1', 'HELD' if all(table[(a, k)] > 0 for a in (32, 52) for k in alpha[a]) else 'REFUTED')
    print('KX-P2', 'HELD' if any(table[(42, k)] == 0 for k in alpha[42]) else 'REFUTED')
    print('exact alphabet after 140 steps:', {a: [k for k in alpha[a] if table[(a, k)] > 0] for a in alpha})


if __name__ == '__main__':
    main()
