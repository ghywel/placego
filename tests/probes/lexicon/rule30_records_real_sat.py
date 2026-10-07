#!/usr/bin/env python3
"""rule30_records_real_sat.py: RR, the realizable records R_real(d) by satisfiability over the light cone (row Q6,
drawn under draw-and-work on 2026-10-07 23:30; Local's claim in CLOUD-LOCAL.md with these predictions pushed before
the run).

RUN-ON:     cpu, kissat on the PATH, JOBS solver calls at a time
COMMAND:    python3 tests/probes/lexicon/rule30_records_real_sat.py [JOBS=4] [TIMEOUT=600]
COST:       to be recorded.

Section 8.36's records R(d) take column 1 free (every column-1 sequence). A configuration produces only some of
them, so the record a configuration can actually reach, R_real(d), can be smaller. ZR2 (rule30_zero_runs.py)
computed R_real(d) exactly by enumerating every right part to depth 28, which closes the runs only up to d = 19
(R_real(13) = 4 against R(13) = 17). Section 8.12's ladder and section 8.14's samples of real right halves (up to 12
cells) bound it from both sides at larger depths, but neither is exact.

The question asked of the solver: is there a configuration whose column 0 follows 0101 (either phase) for times 0 ..
T = d + L - 1, and whose cells at depths d .. d + L - 1 at time 0 are white? Column 0 up to time T depends only on
the time-0 cells -T .. T, so the light cone's cells are the only variables, and every configuration is covered. By
left permutivity those cells at depth t are the forced left half, so SAT at L means R_real(d) >= L. R_real(d) is
the largest L that is SAT. Every SAT row is checked by direct simulation with zeros outside the cone.

This differs from section 8.36's failed SAT route (rule30_records_sat.py, S1 refuted): there the solver searched for a
free column 1, and the realizable runs it must find are long. Here the whole cone is free, and the runs it must find
are short.

PREDICTIONS (Local's, published before the run):
  RR-C0 (control): for every d from 3 to 19, the call at ZR2's R_real(d) is SAT with a witness that checks, and the
        call at R_real(d) + 1 is UNSAT.
  RR-C1 (control, the plateau law): wherever both are known, R_real(d + 1) >= R_real(d) - 1.
  RR-P1 (blind): every call for d <= 41 finishes within the timeout.
  RR-P2 (blind): R_real(d) <= 12 at every d from 21 to 41 that is decided.
  RR-P3 (blind): R_real(d) < R(d) at every decided d from 21 to 41 (the free-column-1 records of section 8.36).
  Stage 2 (added before any run, after a smoke test showed single calls at depth 13 take hundredths of a second):
  d = 49, 57, .., 97.
  RR-P4 (blind): R_real(d) <= 20 at every decided d from 49 to 97 (section 8.36's records there are 39 to 75).
  RR-P5 (blind, uncertain): the largest R_real(d) over all decided depths exceeds 12.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/Volumes/extnvme/nframe-project/np-scratch/rule30-rr'
JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 4
TIMEOUT = int(sys.argv[2]) if len(sys.argv) > 2 else 600
ZR2 = {1: 1, 2: 6, 3: 5, 4: 4, 5: 3, 6: 3, 7: 3, 8: 2, 9: 8, 10: 7, 11: 6, 12: 5, 13: 4, 14: 3, 15: 5, 16: 6,
       17: 9, 18: 8, 19: 7}
R_REC = [1, 6, 5, 4, 3, 4, 3, 2, 9, 8, 7, 6, 17, 16, 15, 16, 15, 14, 15, 14, 17, 16, 19, 20, 19, 18, 17, 16, 19, 20,
         23, 24, 33, 32, 31, 30, 29, 32, 31, 38, 37, 36, 35, 34, 43, 42, 41, 40, 39, 44, 47, 46, 45, 44, 43, 42, 45, 46,
         51, 50, 49]


def cnf(d, L):
    """the light cone of column 0 up to T = d + L - 1; returns (nvars, clauses, row variables -T .. T)"""
    T = d + L - 1
    var, nv = {}, [0]

    def v(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]

    nv[0] += 1
    ph = nv[0]                                         # the phase of column 0
    cl = []
    for t in range(1, T + 1):
        for i in range(-(T - t), T - t + 1):
            y, l, c, r = v(t, i), v(t - 1, i - 1), v(t - 1, i), v(t - 1, i + 1)
            nv[0] += 1
            o = nv[0]                                  # o = c OR r
            cl += [[-c, o], [-r, o], [c, r, -o]]
            cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]   # y = l XOR o
    for t in range(T + 1):
        y = v(t, 0)                                    # column 0 at time t = ph XOR (t mod 2)
        if t % 2 == 0:
            cl += [[-y, ph], [y, -ph]]
        else:
            cl += [[y, ph], [-y, -ph]]
    for j in range(d, d + L):
        cl.append([-v(0, -j)])
    row = [v(0, i) for i in range(-T, T + 1)]
    return nv[0], cl, row, T


def check(row, T, d, L):
    cur = [0, 0] + row + [0, 0]                        # cells -T-2 .. T+2 at time 0, zeros outside the cone
    off = T + 2
    if any(cur[off - j] for j in range(d, d + L)):
        return False
    c0 = [cur[off]]
    for t in range(1, T + 1):
        cur = [0] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
        c0.append(cur[off])
    return all(c0[t] == c0[0] ^ (t % 2) for t in range(T + 1))


def solve(dl):
    d, L = dl
    nv, cl, row, T = cnf(d, L)
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, 'rr_%d_%d.cnf' % (d, L))
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(cl)))
        for c in cl:
            f.write(' '.join(map(str, c)) + ' 0\n')
    t0 = time.time()
    r = subprocess.run(['kissat', '-q', '--time=%d' % TIMEOUT, path], capture_output=True, text=True)
    secs = time.time() - t0
    os.unlink(path)
    if r.returncode == 20:
        return d, L, 'UNSAT', secs, None
    if r.returncode != 10:
        return d, L, 'UNKNOWN', secs, None
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    return d, L, 'SAT', secs, check([1 if x in val else 0 for x in row], T, d, L)


def record(d, start):
    """climb L from start until UNSAT or UNKNOWN; returns (R_real or None, lower bound, log)"""
    L, log = start, []
    while True:
        _, _, verdict, secs, ok = solve((d, L))
        log.append((L, verdict, round(secs, 1), ok))
        if verdict == 'SAT':
            if not ok:
                return None, L - 1, log
            L += 1
            continue
        return (L - 1 if verdict == 'UNSAT' else None), L - 1, log


def main():
    t0 = time.time()
    with ThreadPoolExecutor(JOBS) as ex:
        ctl = list(ex.map(solve, [(d, ZR2[d]) for d in range(3, 20)] + [(d, ZR2[d] + 1) for d in range(3, 20)]))
    c0 = all(v == 'SAT' and ok for d, L, v, s, ok in ctl[:17]) and all(v == 'UNSAT' for d, L, v, s, ok in ctl[17:])
    print('controls d 3 .. 19: %s (%.0f s; slowest call %.1f s)' % ('PASS' if c0 else 'FAIL', time.time() - t0,
          max(s for *_, s, _ in ctl)), flush=True)
    for row in ctl:
        if not ((row[2] == 'SAT' and row[4]) if row[1] == ZR2[row[0]] else row[2] == 'UNSAT'):
            print('  control failure:', row)
    depths = [21, 25, 29, 33, 37, 41]
    with ThreadPoolExecutor(JOBS) as ex:
        res = dict(zip(depths, ex.map(lambda d: record(d, 1), depths)))
    known = dict(ZR2)
    for d in depths:
        R, lo, log = res[d]
        if R is not None:
            known[d] = R
        print('d %d: R_real %s (lower bound %d), R(d) %d; calls %s' % (d, R, lo, R_REC[d - 1], log), flush=True)
    stage2 = list(range(49, 98, 8))
    with ThreadPoolExecutor(JOBS) as ex:
        res2 = dict(zip(stage2, ex.map(lambda d: record(d, 1), stage2)))
    for d in stage2:
        R, lo, log = res2[d]
        if R is not None:
            known[d] = R
        rec = R_REC[d - 1] if d <= len(R_REC) else None
        print('d %d: R_real %s (lower bound %d), R(d) %s; calls %s' % (d, R, lo, rec, log), flush=True)
    c1 = all(known[d + 1] >= known[d] - 1 for d in known if d + 1 in known)
    decided = [d for d in depths if res[d][0] is not None]
    p1 = len(decided) == len(depths)
    p2 = all(res[d][0] <= 12 for d in decided)
    p3 = all(res[d][0] < R_REC[d - 1] for d in decided)
    print('RR-C0', 'PASS' if c0 else 'FAIL')
    print('RR-C1', 'PASS' if c1 else 'FAIL')
    print('RR-P1', 'HELD' if p1 else 'REFUTED')
    print('RR-P2', 'HELD' if p2 else 'REFUTED', '(decided: %s)' % decided)
    print('RR-P3', 'HELD' if p3 else 'REFUTED')
    dec2 = [d for d in stage2 if res2[d][0] is not None]
    print('RR-P4', 'HELD' if all(res2[d][0] <= 20 for d in dec2) else 'REFUTED', '(decided: %s)' % dec2)
    print('RR-P5', 'HELD' if max(known.values()) > 12 else 'REFUTED', '(largest %d)' % max(known.values()))
    print('total %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
