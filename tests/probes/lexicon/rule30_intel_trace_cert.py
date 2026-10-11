#!/usr/bin/env python3
"""rule30_intel_trace_cert.py: SX-P11, the certificate of SX-P10's census (rule30_intel_trace_grow.py with --witness).

RUN-ON:     the Intel MacBook; Python 3 with numpy; the cadical 3.0.1 binary and drat-trim; a pool of workers
COMMAND:    python3 tests/probes/lexicon/rule30_intel_trace_cert.py PHASE LMAX [WORKERS]
            (reads NP_SCRATCH_SX/grow_p{PHASE}_l{LMAX}.log and witness_p{PHASE}_l{LMAX}.txt; writes cert_p{...}.txt)

(1) Realness: each witness row (sites 1..LMAX at time 0) is simulated directly beside the wall and must give its trace;
the prefix sets of the length-LMAX traces must reproduce every |T(l)| of the log (every real trace is a prefix of a
real trace of length LMAX). (2) Completeness: at every length l + 1 the candidates (g + b, g in T(l), (g + b)[2:] in
T(l - 1)) outside T(l + 1) must be exactly the logged minimal absent traces. (3) Absence: for each, the light-cone CNF
of its length with the trace as unit clauses is refuted by cadical with a DRAT proof that drat-trim verifies. (4)
Widths: each logged w(f) has a strip witness at width w(f) - 1, simulated directly, and a verified DRAT refutation of
the width-w(f) strip CNF with the trace as units. Proof files are deleted after checking; the SHA-256 of every CNF is
kept in scratch, and their combined digest is printed.
"""
import hashlib, os, subprocess, sys, tempfile, time
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rule30_intel_trace_grow import _cone_clauses

DRAT_TRIM = os.environ.get('DRAT_TRIM', os.path.join(os.path.expanduser('~'), 'intel-scratch', 'tools', 'drat-trim',
                                                      'drat-trim'))


def simulate(rows, phase, n):
    """rows: uint8 array (k, n) of sites 1..n at time 0; returns the column-1 traces of length n"""
    x = rows.copy(); out = np.zeros_like(rows)
    for t in range(n):
        out[:, t] = x[:, 0]
        wall = (t + phase) & 1
        left = np.concatenate([np.full((x.shape[0], 1), wall, dtype=np.uint8), x[:, :-1]], axis=1)
        right = np.concatenate([x[:, 1:], np.zeros((x.shape[0], 1), dtype=np.uint8)], axis=1)
        x = left ^ (x | right)
    return out


def strip_trace(row, inputs, phase, n):
    W = len(row); x = [int(c) for c in row]; tr = ''
    for t in range(n):
        tr += str(x[0])
        if t == n - 1: break
        wall = (t + phase) & 1; e = int(inputs[t])
        x = [(wall if i == 0 else x[i - 1]) ^ (x[i] | (x[i + 1] if i + 1 < W else e)) for i in range(W)]
    return tr


def refute(job):
    """cadical with a DRAT proof, checked by drat-trim; returns (trace, kind, cnf digest, verdict)"""
    f, phase, width, kind = job
    cl, col1, var = _cone_clauses(phase, len(f), width=width)
    units = [[col1[t] if c == '1' else -col1[t]] for t, c in enumerate(f)]
    nv = max(abs(x) for c in cl + units for x in c)
    text = f'p cnf {nv} {len(cl) + len(units)}\n' + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl + units)
    dig = hashlib.sha256(text.encode()).hexdigest()
    with tempfile.TemporaryDirectory() as d:
        cnf, prf = os.path.join(d, 'f.cnf'), os.path.join(d, 'f.drat')
        open(cnf, 'w').write(text)
        r = subprocess.run(['cadical', '-q', '--binary=false', cnf, prf], capture_output=True, text=True)
        if r.returncode != 20: return f, kind, dig, f'cadical exit {r.returncode}'
        v = subprocess.run([DRAT_TRIM, cnf, prf, '-t', '400000'], capture_output=True, text=True).stdout
        return f, kind, dig, 'VERIFIED' if 's VERIFIED' in v else 'NOT VERIFIED'


def main(phase, lmax, workers):
    sc = os.environ.get('NP_SCRATCH_SX', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-sx'))
    log = os.path.join(sc, f'grow_p{phase}_l{lmax}.log'); wit = os.path.join(sc, f'witness_p{phase}_l{lmax}.txt')
    out = open(os.path.join(sc, f'cert_p{phase}_l{lmax}.txt'), 'w')
    t0 = time.time()
    say = lambda *a: (print(*a, file=out, flush=True), print(*a, flush=True))
    Tc = {}; M = {}
    for line in open(log):
        p = line.split()
        if p[0] == 'T': Tc[int(p[1])] = int(p[2])
        elif p[0] == 'M': M[p[2]] = int(p[3])
    R = []; S = []
    for line in open(wit):
        p = line.split()
        if p[0] == 'R': R.append((p[1], p[2]))
        elif p[0] == 'S': S.append((p[1], int(p[2]), p[3], p[4] if len(p) > 4 else ''))
    say(f'phase {phase}, LMAX {lmax}: {len(R)} witness rows, {len(S)} strip witnesses, {len(M)} minimal absent traces')
    for name in (log, wit):
        say(f'sha256 {os.path.basename(name)} {hashlib.sha256(open(name, "rb").read()).hexdigest()}')
    # (1) realness
    rows = np.array([[int(c) for c in r] for f, r in R], dtype=np.uint8)
    traces = simulate(rows, phase, lmax)
    ok1 = all(''.join(map(str, traces[k])) == f for k, (f, r) in enumerate(R))
    T = {l: {f[:l] for f, r in R} for l in range(1, lmax + 1)}
    ok1b = all(len(T[l]) == Tc[l] for l in range(1, lmax + 1))
    say(f'(1) every witness row re-simulates to its trace: {ok1}; prefix sets reproduce |T(l)|, l = 1..{lmax}: {ok1b}')
    # (2) completeness
    absent = set()
    for l in range(1, lmax):
        for g in T[l]:
            for b in '01':
                h = g + b
                if (l + 1 < 3 or h[2:] in T[l - 1]) and h not in T[l + 1]: absent.add(h)
    say(f'(2) the candidates outside the prefix sets are exactly the logged minimal absent traces: {absent == set(M)} '
        f'({len(absent)} against {len(M)})')
    # (4a) strip witnesses
    ok4 = all(strip_trace(row, inp, phase, len(f)) == f and W == M[f] - 1 for f, W, row, inp in S)
    need = {f for f, w in M.items() if w >= 2}
    say(f'(4a) every strip witness re-simulates at width w(f) - 1: {ok4}; '
        f'one for every w(f) >= 2: {need == {s[0] for s in S}}')
    # (3) and (4b) DRAT
    jobs = [(f, phase, None, 'absent') for f in sorted(M)] + [(f, phase, w, 'width') for f, w in sorted(M.items())]
    res = []
    with Pool(workers) as pool:
        for k, r in enumerate(pool.imap_unordered(refute, jobs, chunksize=1)):
            res.append(r)
            if (k + 1) % 500 == 0: print(f'  {k + 1}/{len(jobs)} refutations, {time.time() - t0:.0f} s', flush=True)
    bad = [r for r in res if r[3] != 'VERIFIED']
    with open(os.path.join(sc, f'cert_digests_p{phase}_l{lmax}.txt'), 'w') as dg:
        for f, kind, d, v in sorted(res): print(kind, f, d, v, file=dg)
    comb = hashlib.sha256(''.join(f'{kind} {f} {d}\n' for f, kind, d, v in sorted(res)).encode()).hexdigest()
    n3 = sum(1 for r in res if r[1] == 'absent' and r[3] == 'VERIFIED')
    say(f'(3) absences verified by drat-trim: {n3} of {len(M)}')
    n4 = sum(1 for r in res if r[1] == 'width' and r[3] == 'VERIFIED')
    say(f'(4b) width refutations verified by drat-trim: {n4} of {len(M)}')
    say(f'failures: {bad[:10]}')
    say(f'combined digest of the {len(res)} CNFs: {comb}; {time.time() - t0:.0f} s')


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 8)
