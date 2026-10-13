#!/usr/bin/env python3
"""rule30_history_cone.py: history-restricted real records R^(n)(d) (L698's (H)), by RR's exact light cone grown n ticks
into the past. Local's second block as the maths lead (AGENTS.md item 19).

Definition. R^(n)(d) is the largest L such that some configuration X_(-n) keeps the clock at column 0 from time -n
through T = d + L - 1 and X_0 has the white band [d, d + L - 1] in its forced left half. R^(0) = R_real (RR), and
R^(n+1)(d) <= R^(n)(d), because an (n + 1)-tick past contains an n-tick past.

The cone. Height H = T + n, base row X_(-n) on cells -H .. H, RR's rule y(t, i) = x(t-1, i-1) XOR (x(t-1, i) OR
x(t-1, i+1)) with RR's variable order, column 0 equal to the wall (phase (p + n) mod 2 at the base) for cone times
0 .. H, and the band white at cone time n (the cells exist there: depth E = T = H - n). Column 0 at time <= H depends
only on the cone, so a zero-padded SAT model is a real configuration, checked by direct simulation; UNSAT is exact.
No certified-word clauses are added: the census uses the pure cone.

RUN-ON:     cpu, kissat (wall-clock --time), a 6-process pool; minutes.
COMMAND:    python3 tests/probes/lexicon/rule30_history_cone.py controls
            python3 tests/probes/lexicon/rule30_history_cone.py census [DMIN=20] [DMAX=100]

Record searched (record_find, 2026-10-13 23:00 BST): 'Garden of Eden|garden-of-eden' -> 8 hits in 5 files (CL010's
catalogue note, G24's periodic Garden-of-Eden density; no record use); 'n-tick past|tick past|history-restricted|
R\\^\\(n\\)' -> 12 hits in 7 files (GC1054/1055 mature forks need an ordinary past, GC1134/1135 two clamped past ticks
exclude a fresh counter; no history-restricted record); 'preimage.*record|record.*preimage|pre-image' -> 34 hits in 15
files (two-tick normalisation and refork probes, no record census); 'real past|wall-keeping past|keeping past' -> 1 hit
(L698). RR (rule30_records_real_sat.py) and its exact fixture (depths 20 .. 100 exact) read.

PREDICTIONS (written 2026-10-13 23:01 BST, before any run; first written as 23:08, ahead of the clock, corrected to the commit time).
  H1 must hold (instrument): for n = 0 the clause list equals RR's cnf plus the phase unit, at (21, 15, 1), (41, 8, 0)
     and (60, 9, 0); and the n = 0 search reproduces the fixture's exact R_real(d) at d = 20 .. 30.
  H2 must hold: every SAT model passes the direct simulation (clock from the base through H, band white at time n).
  H3 must hold (cross-instrument with rule30_record_real_parent.py): at every depth 20 .. 100 whose fixture witness has
     a real age-1 parent (0w or 1w), R^(1)(d) = R_real(d).
  H4 blind (0.45): at least one of d = 41, 43, 44, 80, 86 (the witnesses with no real parent) has R^(1)(d) < R_real(d).
  H5 blind (0.6): history lowers the records slowly: R^(8)(d) >= R_real(d) - 1 at a majority of depths 20 .. 100.
     Counterfactual: the records fall by 2 or more at most depths by n = 8 (a short history already carries a price).
  H6 must hold (unexpected check, a theorem used as a control): R^(n+1)(d+1) >= R^(n)(d) - 2 wherever both are
     computed (X_1 of a witness has one more tick of past and keeps cells d+1 .. E-1 white).
  Reported, no prediction: the table of R^(n)(d) - R_real(d) for n = 1, 2, 4, 8, and the UNKNOWNs (900 s cap).
"""
import json, os, subprocess, sys, tempfile, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]                                # RR parses sys.argv at import
from rule30_records_real_sat import cnf as rr_cnf                       # noqa: E402
sys.argv = _argv
SCRATCH = os.path.expanduser('~/np-scratch-int/rule30-history')
CAP = 900


def cone(d, L, n, p):
    """CNF for: X_(-n) keeps the clock from -n through T, X_0 has [d, E] white, X_0's wall phase p."""
    T = d + L - 1
    H = T + n
    var, nv = {}, [0]

    def v(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    nv[0] += 1
    ph = nv[0]                                          # column 0 at cone time 0 (= X_(-n))
    cl = []
    for t in range(1, H + 1):
        for i in range(-(H - t), H - t + 1):
            y, l, c, r = v(t, i), v(t - 1, i - 1), v(t - 1, i), v(t - 1, i + 1)
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for t in range(H + 1):
        y = v(t, 0)
        if t % 2 == 0:
            cl += [[-y, ph], [y, -ph]]
        else:
            cl += [[y, ph], [-y, -ph]]
    for j in range(d, d + L):
        cl.append([-v(n, -j)])
    cl.append([ph] if (p + n) % 2 == 1 else [-ph])
    row = [v(0, i) for i in range(-H, H + 1)]
    return nv[0], cl, row, H


def simulate(bits, H, d, L, n, p):
    cur = [0, 0] + bits + [0, 0]
    off = H + 2
    ok = True
    for t in range(H + 1):
        if cur[off] != (p + n + t) % 2:
            ok = False
        if t == n and any(cur[off - j] for j in range(d, d + L)):
            ok = False
        cur = [0] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
    return ok


def solve(args):
    d, L, n, p = args
    nv, cl, row, H = cone(d, L, n, p)
    os.makedirs(SCRATCH, exist_ok=True)
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=SCRATCH)
    with os.fdopen(fd, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(cl)))
        f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    t0 = time.time()
    r = subprocess.run(['kissat', '-q', '--time=%d' % CAP, path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode == 20:
        return args, 'UNSAT', time.time() - t0
    if r.returncode != 10:
        return args, 'UNKNOWN', time.time() - t0
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    bits = [1 if x in val else 0 for x in row]
    return args, ('SAT' if simulate(bits, H, d, L, n, p) else 'SAT-CHECK-FAILED'), time.time() - t0


def fixture():
    rows = json.load(open(os.path.join(HERE, '..', '..', '..', 'site', 'wolframcollatzmahler', 'data', 'records.json')))['rows']
    return {r['depth']: r for r in rows}


def controls():
    ok = True
    for d, L, p in ((21, 15, 1), (41, 8, 0), (60, 9, 0)):
        nv, cl, row, H = cone(d, L, 0, p)
        rnv, rcl, rrow, rT = rr_cnf(d, L)
        ok &= nv == rnv and cl == list(rcl) + [[1] if p == 1 else [-1]] and row == rrow
    print('H1 clause lists equal RR + phase unit:', ok, flush=True)
    fx = fixture()
    jobs = [(d, L, 0, p) for d in range(20, 31) for L in (fx[d]['L'], fx[d]['L'] + 1) for p in (0, 1)]
    with Pool(6) as pool:
        res = {a: v for a, v, _ in pool.imap_unordered(solve, jobs)}
    rep = all(any(res[(d, fx[d]['L'], 0, p)] == 'SAT' for p in (0, 1)) and
              all(res[(d, fx[d]['L'] + 1, 0, p)] == 'UNSAT' for p in (0, 1)) for d in range(20, 31))
    bad = [a for a, v in res.items() if v == 'SAT-CHECK-FAILED']
    print('H1 n = 0 reproduces R_real(20 .. 30):', rep, '| check failures:', bad, flush=True)


def census(dmin, dmax):
    fx = fixture()
    ds = [d for d in range(dmin, dmax + 1) if fx[d]['status'] == 'exact']
    best = {(d, 0): fx[d]['L'] for d in ds}            # R^(0) = R_real, exact
    failed, unknown = [], []
    with Pool(6) as pool:
        prev = 0
        for n in (1, 2, 4, 8):
            cur = {d: best[(d, prev)] for d in ds}     # R^(n) <= R^(prev)
            done = {}
            while len(done) < len(ds):
                jobs = [(d, cur[d], n, p) for d in ds if d not in done for p in (0, 1)]
                res = {}
                for a, v, s in pool.imap_unordered(solve, jobs):
                    res[a] = v
                    if v == 'SAT-CHECK-FAILED':
                        failed.append(a)
                for d in ds:
                    if d in done:
                        continue
                    vs = [res[(d, cur[d], n, p)] for p in (0, 1)]
                    if 'SAT' in vs:
                        done[d] = cur[d]
                    elif 'UNKNOWN' in vs:
                        unknown.append((d, cur[d], n))
                        done[d] = None                 # undecided at this L; reported, not lowered
                    else:
                        cur[d] -= 1
            for d in ds:
                best[(d, n)] = done[d] if done[d] is not None else best[(d, prev)]
            print('n=%d:' % n, ' '.join('%d:%s' % (d, '?' if done[d] is None else done[d] - fx[d]['L']) for d in ds),
                  flush=True)
            prev = n
    real_parent_missing = {41, 43, 44, 80, 86}
    h3 = all(best[(d, 1)] == fx[d]['L'] for d in ds if d not in real_parent_missing)
    h4 = [d for d in sorted(real_parent_missing) if d in ds and best[(d, 1)] < fx[d]['L']]
    h5 = sum(1 for d in ds if best[(d, 8)] >= fx[d]['L'] - 1)
    h6 = all(best[(d + 1, m)] >= best[(d, k)] - 2 for d in ds if d + 1 in ds
             for k, m in ((0, 1), (1, 2)))
    print('H2 every SAT model simulates:', 'HELD' if not failed else 'FAILED %s' % failed)
    print('H3 real-parent depths keep R^(1) = R_real:', 'HELD' if h3 else 'FAILED')
    print('H4 a no-parent depth has R^(1) < R_real:', 'HELD %s' % h4 if h4 else 'REFUTED')
    print('H5 R^(8) >= R_real - 1 at a majority: %d of %d' % (h5, len(ds)), 'HELD' if 2 * h5 > len(ds) else 'REFUTED')
    print('H6 R^(n+1)(d+1) >= R^(n)(d) - 2 (n = 0, 1):', 'HELD' if h6 else 'FAILED')
    print('UNKNOWN (cap %d s):' % CAP, unknown)
    json.dump({'%d_%d' % k: v for k, v in best.items()}, open(os.path.join(SCRATCH, 'census_%d_%d.json' % (dmin, dmax)), 'w'))


if __name__ == '__main__':
    if sys.argv[1] == 'controls':
        controls()
    else:
        census(int(sys.argv[2]) if len(sys.argv) > 2 else 20, int(sys.argv[3]) if len(sys.argv) > 3 else 100)
