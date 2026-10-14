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

OUTCOME (census, 2026-10-14 01:31 BST, M5, about 2.5 hours; machine output quoted, no UNKNOWN and no replay failure,
  so GC1213's guard leaves the scoring valid): H1 HELD, H2 HELD, H3 HELD, H4 REFUTED, H5 HELD (75 of 81), H6 HELD.
  Depths 20 .. 100 where R^(n)(d) < R_real(d) (difference shown); every other depth equals R_real:
     n = 1: none
     n = 2: 87:-2 88:-1 89:-1 90:-1 91:-1
     n = 4: 43:-1 44:-1 48:-2 87:-2 88:-1 89:-1 90:-1 91:-1
     n = 8: 43:-1 44:-1 48:-2 67:-5 68:-4 69:-1 87:-2 88:-2 89:-2 90:-1 91:-1
  So the peaks at 87 (16) and 67 (14) are reached only by configurations with at most one and at most seven ticks of
  real past, and 48's 11 by at most three. Most records in 20 .. 100 survive eight ticks unchanged (108 is outside the
  census range; GC1217 corrected a first draft that included it). The drops
  fall on depths whose committed witnesses were real only through 1w (67 .. 69, 87 .. 91) or had no canonical parent
  (43, 44), plus 48.

GPT reporting review (GC1213, 2026-10-13 23:10 BST), registered before synthetic checks:
  Two fixture depths (20,21): UNKNOWN-only results must remain upper bounds and leave H3..H6 unscored;
  SAT-CHECK-FAILED must abort before lowering L. Unexpected control: validated SAT in one phase with UNKNOWN
  in the other still attains the aggregate record when it equals the known upper bound. These are stubbed
  reporter controls, not solver runs. Cone clauses must remain unchanged at n=0,1,2 in both phases.
  Existing running processes retain the earlier reporter; any UNKNOWN or replay failure in their output
  requires these scope guards before interpreting H3..H6. No computation restart is requested.
  OUTCOME: all three two-depth reporter controls PASS; 12 before/after cone comparisons (two named
  depth/length fixtures, n=0,1,2, both phases) have identical clauses and metadata. No solver executed.

ADDENDUM PREDICTIONS (2026-10-14 01:30 BST, before the run; the third and final history block, "young peaks", agreed in
  GC1216 with its horizon and scope). Fixture: X2's phase-0 witness at 147 (rule30_exact_cone_cert.py, its 329-bit
  receipt), T = 164.
  Y0 must hold (control, GC1216's 87 control): the committed 87 witness (phase 1) has a real age-1 parent through 1w
     (rule30_record_real_parent.py P5), and the same membership code returns True on its root.
  Y1 blind (0.5): X2's 82 white-time column-1 samples at child times 0, 2, .., 162 (sample 164 is unused by the
     record query) form a word w in L_1. If so, gluing w's real right realization to C_1(w) gives a child with the same
     forced left row through depth 164, so R_history,0^(1)(147) = 18: a phase-0 maximizer with a real past exists
     (not necessarily the saved whole configuration). Counterfactual: w is not in L_1, so X2's left-prefix and trace
     cylinder has no real past.
  Y2 (run only if Y1 fails; blind 0.5 for SAT): one exact history cone, d = 147, L = 18, n = 1, phase 0 (base phase 1,
     H = 165, the band at cone time 1). SAT gives another history-bearing maximizer; sound UNSAT gives
     R_history,0^(1)(147) <= 17, a peak that needs a configuration with no real past. A cap is UNKNOWN. No further
     query follows in this block.
  OUTCOME (2026-10-14 01:30 BST, M5, seconds; machine output quoted): Y0 HELD, Y1 HELD, so Y2 was not run.
     X2 visible word (82 samples): 0010100001010101000100001001001000010000100100100001000010000100001001000010010000,
     in L_1. So R_history,0^(1)(147) = 18 (GC1216's gluing: w's real right realization on C_1(w) gives a child with
     X2's forced left row through depth 164). The new 147 peak has a phase-0 maximizer with a real past; it is not
     young in the n = 1 sense. The word differs from the round-2 relaxed model's code at visible indices 1, 2, 4 and 5
     only (the last change at sample 5, white time 10; corrected per GC1217). GPT's GC1217 adds: X2 and both rejected
     relaxed origins share the entire clamped left row at time 11.
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
    exact = {(d, 0): True for d in ds}
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
                if failed:
                    raise RuntimeError('SAT replay failed; no UNSAT descent or record verdict: %s' % failed)
                for d in ds:
                    if d in done:
                        continue
                    vs = [res[(d, cur[d], n, p)] for p in (0, 1)]
                    if 'SAT' in vs:
                        done[d] = cur[d]
                    elif 'UNKNOWN' in vs:
                        unknown.append((d, cur[d], n))
                        done[d] = None                 # undecided at this L; reported, not lowered
                    elif all(v == 'UNSAT' for v in vs):
                        cur[d] -= 1
                    else:
                        raise RuntimeError('Unexpected solver verdicts: %s' % vs)
            for d in ds:
                best[(d, n)] = done[d] if done[d] is not None else cur[d]
                exact[(d, n)] = done[d] is not None
            print('n=%d:' % n, ' '.join('%d:%s' % (d, '?' if done[d] is None else done[d] - fx[d]['L']) for d in ds),
                  flush=True)
            prev = n
    output = {'%d_%d' % k: {'upper': v, 'lower': v if exact[k] else 0, 'exact': exact[k]}
              for k, v in best.items()}
    json.dump(output, open(os.path.join(SCRATCH, 'census_%d_%d.json' % (dmin, dmax)), 'w'))
    if unknown:
        print('H2 every SAT model simulates: HELD')
        print('H3 to H6 UNSCORED: incomplete census; UNKNOWN bounds are not measured records')
        print('UNKNOWN (cap %d s):' % CAP, unknown)
        return
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


def young_peak():
    import re
    import rule30_relaxed_records_k as rlk
    fx = fixture()
    r87 = fx[87]
    y0 = r87['phase'] == 1 and bool(rlk.in_language_phase('1' + r87['visible'], 0))
    print('Y0 87 control: root 1w real in L_0:', 'HELD' if y0 else 'FAILED', flush=True)
    src = open(os.path.join(HERE, 'rule30_exact_cone_cert.py')).read()
    block = src[src.index('The witness row, cells -164 .. 164'):]
    row = ''.join(re.findall(r'\n {5}([01]+)', block)[:4])
    assert len(row) == 329
    T, d, L, p = 164, 147, 18, 0
    cur = [0] * 4 + [int(c) for c in row] + [0] * 4
    off = T + 4
    col1 = []
    for t in range(T + 1):
        assert cur[off] == (p + t) % 2
        col1.append(cur[off + 1])
        cur = [0, 0] + [0] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0] + [0, 0]
        off += 2
    w = ''.join(str(col1[t]) for t in range(0, 163, 2))
    assert len(w) == 82
    y1 = bool(rlk.in_language_phase(w, 1))
    print('X2 visible word (82 samples):', w)
    print('Y1 w in L_1 (a phase-0 maximizer at 147 with a real past):', 'HELD' if y1 else 'REFUTED (run Y2)', flush=True)
    return y1


if __name__ == '__main__':
    if sys.argv[1] == 'young':
        young_peak()
        sys.exit(0)
    if sys.argv[1] == 'controls':
        controls()
    else:
        census(int(sys.argv[2]) if len(sys.argv) > 2 else 20, int(sys.argv[3]) if len(sys.argv) > 3 else 100)
