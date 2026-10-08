#!/usr/bin/env python3
"""rule30_three_gap_death.py: RV3, the death time of the visible 3-gap next to the clamped 0101 wall, and of every
five-site wall window (row 6.1; Cloud's question in CL037, offered to Local's SAT lane; claimed in L286). Local's run,
claimed in CLOUD-LOCAL.md with these predictions pushed before it started.

RUN-ON:     cpu, up to 5 kissat processes (drat-trim for the boundary UNSATs); resumable
COMMAND:    NP_SCRATCH_RV3=<data folder> python3 tests/probes/lexicon/rule30_three_gap_death.py start | status | resume
            python3 tests/probes/lexicon/rule30_three_gap_death.py controls      (C1 only, seconds, no solver)
COST:       to be recorded; expected hours (the largest instances have about 530,000 cells at T = 1024).

The model is GPT's GC499 and Cloud's RV: Rule 30 on the right half, sites 1, 2, ..., with the wall at site 0 clamped
to 0 at even times and 1 at odd times; the initial right row is arbitrary. The visible trace is site 1 at even times.
A window is the five cells at sites 1 .. 5 of the row at an even time T. Since the row at time 2 is again an allowed
initial row with the wall at the same phase, a window that occurs at even time T also occurs at T - 2: the set of
even times at which a window can occur is closed downwards, so each window has a last time (its death time) or none.

The 3-gap. By GC503 (second-read in CL033) the zero run after a visible 1 is decided by sites 1 .. 5 at the 1's time;
Cloud worked out by hand (CL037) that the run has length exactly 3 when sites 2 .. 5 read 0000, 100* or 01**. So a
visible 3-gap whose leading 1 is at even time T exists exactly when the window at T is one of those seven
(control C1 checks this). Its death time T3 is the last even T at which that window set occurs in the T-step image.

Method. Each question "can window set S occur at even time T?" is one SAT instance over the light cone: cells
x_t(i) for 0 <= t <= T and 1 <= i <= 5 + T - t, x_(t+1)(i) = x_t(i - 1) XOR (x_t(i) OR x_t(i + 1)), the wall a
constant; the initial cells are free. kissat solves it (cap per call); a SAT model is replayed by direct simulation
from its initial row; an UNSAT at the boundary is re-solved with a DRAT proof checked by drat-trim. Search per target:
a parallel ladder of even times up to TMAX, then parallel bisection between the last SAT and the first UNSAT. Targets:
'gap3' (the seven windows, TMAX 1024), 'direct' (control: site 1 at T, T + 2, .., T + 8 reads 1, 0, 0, 0, 1, solved at
gap3's boundary only), and the 32 single windows 'wNN' (sites 1 .. 5 as bits 0 .. 4 of NN, TMAX 256).

PREDICTIONS (Local's, published before the run):
  RV3-C1 (control): on every initial row of width 13 at T = 0, 2, 4, and on 3,000 random rows of width 16 .. 64 at
         every even T <= 300, the window at T is in the gap3 set exactly when site 1 at T, T + 2, .., T + 8 reads
         1, 0, 0, 0, 1.
  RV3-C2 (control): every SAT model replays by simulation; every boundary UNSAT has a drat-trim VERIFIED proof; the
         gap3 boundary proof checked against the satisfiable CNF one step earlier is not verified (the checker can
         say no).
  RV3-C3 (control): 'direct' agrees with gap3 at gap3's boundary (SAT at T3, UNSAT at T3 + 2).
  RV3-C4 (control): gap3 is SAT at T = 210 (RV2 saw a 3-gap at time 214 in a random right half of width 64).
  RV3-C5 (control): no target is SAT at an even time above one where it is UNSAT (monotonicity).
  RV3-P1 (blind, confidence 0.5): the 3-gap dies: T3 is finite and at most 1024, with a verified UNSAT at T3 + 2.
  RV3-P2 (blind, confidence 0.5): designed rows beat the random one by at least a factor 2: T3 > 420, or gap3 is
         still SAT at 1024.
  RV3-P3 (blind, confidence 0.6): at T = 256 at least 8 of the 32 windows are still possible and at least 8 have
         died.
  RV3-P4 (blind, confidence 0.4): every window still possible at T = 256 is one the wheel's lock shows at an even
         time (windows read off 400 random right halves at least 112 steps into a lock).
  D1 (descriptive): each window's death time (or survival to 256), and T3 with its witness row.
Counterfactual: if gap3 is SAT at every T up to 1024, column 1's late gap alphabet keeps 3 as far as SAT can see, and
the history condition behind CL041's witness has to be read context by context (as GPT's GC550a does), not as an
age limit on every 3-gap.
OUTCOME, 2026-10-08 19:53 (M5, run from 15:41 at commit b5a8375; 4 h 12 min; 143 SAT replays, 14 drat-trim proofs):
  RV3-C1 PASS (477,576 comparisons, 2,318 of them 3-gaps). RV3-C2 PASS (every SAT model replays; all 14 boundary
  proofs VERIFIED; the say-no control did not apply, as gap3 had no UNSAT boundary). RV3-C3 not run (no gap3
  boundary). RV3-C4 PASS (SAT at 210). RV3-C5 PASS.
  gap3: SAT at 210, 212, 264, 316, 330, 342, 352 (solve times 35 s to 3,045 s); UNKNOWN at the one-hour cap at 354,
  356, 358, 360, 362, 364, 366, 418, 420, 840, 1024 (and at 318, which downward closure makes SAT). No UNSAT.
  RV3-P1 UNDECIDED: the 3-gap is possible at least to T = 352; no death time is certified.
  RV3-P2 UNDECIDED. The run printed REFUTED, but that is a fault in report(): it compared the last SAT time with
  420 without requiring an UNSAT below 420. With no UNSAT, T3 > 420 is neither shown nor excluded.
  RV3-P3 HELD: 18 windows still possible at T = 256 and 14 dead. Twelve die by T = 2 (11000, 10100, 01100, 10010,
  11010, 11110, 11001, 10101, 01101, 11011, 10111, 11111; last time 0, exactly Cloud's CL044 count of 20 survivors
  at T = 2). 00110 dies after T = 2. 10000 dies after T = 52 (UNSAT at 54, proof VERIFIED).
  RV3-P4 REFUTED: only 8 windows appear in 400 random right halves at least 112 steps into a lock, and 10 of the
  18 survivors at 256 are not among them (00000, 01000, 00100, 10110, 00001, 10001, 01001, 00101, 10011, 01111).
  D1, read with L289: the 3-gap has two branches. Its white branch (10000, whose predecessor two steps earlier is
  0000000) dies exactly: 10000 is last possible at T = 52, so seven white cells next to the wall at an even time are
  last possible at T = 50. Every 3-gap after T = 52 uses the 10110 branch (predecessor 00001), which is possible at
  least to 352.
"""
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ.get('NP_SCRATCH_RV3', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-rv3'))
CK = os.path.join(SCRATCH, 'rv3.ck')
LOG = os.path.join(SCRATCH, 'rv3.log')
CAP = 3600
CAP_FINAL = 14400
DRAT_CAP = 20000
JOBS = 5
TMAX_GAP = 1024
TMAX_WIN = 256
WIDTH = 5


# ---------------------------------------------------------------- simulation (Cloud's coding: bit i is site i, bit 0 the wall)
def step(row, t):
    new = (row << 1) ^ (row | (row >> 1))
    return (new & ~1) | ((t + 1) % 2)


def rows_from(right, n):
    """rows at times 0 .. n - 1 from initial right sites (bit k of `right` is site k + 1)"""
    row, out = right << 1, []
    for t in range(n):
        out.append(row)
        row = step(row, t)
    return out


def window(row):
    return tuple((row >> i) & 1 for i in range(1, WIDTH + 1))


def in_gap3(w):
    s1, s2, s3, s4, s5 = w
    return s1 == 1 and ((s2, s3, s4, s5) == (0, 0, 0, 0) or (s2, s3, s4) == (1, 0, 0) or (s2, s3) == (0, 1))


GAP3 = [w for w in ((n >> 0 & 1, n >> 1 & 1, n >> 2 & 1, n >> 3 & 1, n >> 4 & 1) for n in range(32)) if in_gap3(w)]


def wbits(n):
    return tuple((n >> k) & 1 for k in range(WIDTH))


# ---------------------------------------------------------------- CNF over the light cone
def instance(target, T):
    """CNF for: can target occur with its last constrained cell at time Tend? Returns (nvar, clauses, Tend, ninit)."""
    if target == 'direct':
        Tend, sites = T + 8, 1
    else:
        Tend, sites = T, WIDTH
    width = [sites + Tend - t for t in range(Tend + 1)]
    off, n = [], 0
    for t in range(Tend + 1):
        off.append(n)
        n += width[t]
    var = lambda t, i: off[t] + i                       # i = 1 .. width[t]
    cl = []
    for t in range(1, Tend + 1):
        wall = (t - 1) % 2
        for i in range(1, width[t] + 1):
            y, c, r = var(t, i), var(t - 1, i), var(t - 1, i + 1)
            if i == 1:                                  # y = wall XOR (c OR r)
                if wall == 0:
                    cl += [[-c, y], [-r, y], [c, r, -y]]
                else:
                    cl += [[-c, -y], [-r, -y], [c, r, y]]
                continue
            l = var(t - 1, i - 1)
            for a in (0, 1):
                for b in (0, 1):
                    for d in (0, 1):
                        f = a ^ (b | d)
                        cl.append([(l if a == 0 else -l), (c if b == 0 else -c), (r if d == 0 else -r),
                                   (y if f == 1 else -y)])
    if target == 'direct':
        for k, v in enumerate((1, 0, 0, 0, 1)):
            x = var(T + 2 * k, 1)
            cl.append([x if v else -x])
    else:
        allowed = GAP3 if target == 'gap3' else [wbits(int(target[1:]))]
        sel = []
        for w in allowed:
            n += 1
            sel.append(n)
            for k, v in enumerate(w):
                x = var(Tend, k + 1)
                cl.append([-n, x if v else -x])
        cl.append(sel)
    return n, cl, Tend, width[0]


def write_cnf(path, nv, cl):
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(cl)))
        f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))


def check_model(target, T, init_bits):
    right = 0
    for k, v in enumerate(init_bits):
        right |= v << k
    if target == 'direct':
        rows = rows_from(right, T + 9)
        return [(rows[T + 2 * k] >> 1) & 1 for k in range(5)] == [1, 0, 0, 0, 1]
    w = window(rows_from(right, T + 1)[T])
    return in_gap3(w) if target == 'gap3' else w == wbits(int(target[1:]))


def solve(task, proof=False):
    target, T = task
    t0 = time.time()
    nv, cl, Tend, ninit = instance(target, T)
    tag = '%s_%d' % (target, T)
    cnf = os.path.join(SCRATCH, 'i_%s.cnf' % tag)
    write_cnf(cnf, nv, cl)
    if proof:
        prf = os.path.join(SCRATCH, 'p_%s.drat' % tag)
        r = subprocess.run(['kissat', '-q', '-f', '--no-binary', '--time=%d' % CAP_FINAL, cnf, prf],
                           capture_output=True, text=True)
    else:
        r = subprocess.run(['kissat', '-q', '--time=%d' % CAP, cnf], capture_output=True, text=True)
    secs = time.time() - t0
    if r.returncode == 10:
        val = set()
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                val.update(int(x) for x in line[2:].split())
        init = [1 if (i + 1) in val else 0 for i in range(ninit)]   # time-0 cells are variables 1 .. ninit
        ok = check_model(target, T, init)
        hexrow = '%x' % sum(v << k for k, v in enumerate(init))
        os.unlink(cnf)
        if proof and os.path.exists(prf):
            os.unlink(prf)
        return task, 'SAT', 'replay-pass' if ok else 'replay-FAIL', secs, hexrow
    if r.returncode == 20:
        extra = 'noproof'
        if proof:
            d = subprocess.run(['drat-trim', cnf, prf, '-t', str(DRAT_CAP)], capture_output=True, text=True)
            extra = 'VERIFIED' if 's VERIFIED' in d.stdout else 'NOT-VERIFIED'
            if target != 'gap3':                        # gap3's proof is kept for C2's say-no check
                os.unlink(prf)
        os.unlink(cnf)
        return task, 'UNSAT', extra, secs, '-'
    os.unlink(cnf)
    if proof and os.path.exists(prf):
        os.unlink(prf)
    return task, 'UNKNOWN', 'rc%d' % r.returncode, secs, '-'


# ---------------------------------------------------------------- checkpoint
def done():
    res = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 7 and f[-1] == 'END':
                res[f[0], int(f[1])] = (f[2], f[3], float(f[4]), f[5])
    return res


def record(task, verdict, extra, secs, hexrow, kind=''):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:
            with open(CK, 'a') as f:
                f.write('\n')
    with open(CK, 'a') as f:
        f.write('%s%s %d %s %s %.1f %s END\n' % (kind, task[0], task[1], verdict, extra, secs, hexrow))
    print('%s %s%s T %d: %s %s %.1f s' % (time.strftime('%H:%M:%S'), kind, task[0], task[1], verdict, extra, secs),
          flush=True)


def run_tasks(tasks, proof=False, kind=''):
    have = done()
    todo = [t for t in tasks if (kind + t[0], t[1]) not in have]
    if todo:
        with ThreadPoolExecutor(JOBS) as ex:
            futs = [ex.submit(solve, t, proof) for t in todo]
            for fut in as_completed(futs):
                task, verdict, extra, secs, hexrow = fut.result()
                record(task, verdict, extra, secs, hexrow, kind)


def bounds(target, have):
    st = {T: v[0] for (g, T), v in have.items() if g == target}
    sat = [T for T, v in st.items() if v == 'SAT']
    uns = [T for T, v in st.items() if v == 'UNSAT']
    return st, (max(sat) if sat else 0), (min(uns) if uns else None)


def next_points(target, tmax, have, k):
    st, lo, hi = bounds(target, have)
    unknown = [T for T, v in st.items() if v == 'UNKNOWN' and T > lo]
    stops = ([hi] if hi is not None else []) + unknown
    top = min(stops) if stops else None
    if top is not None and top - lo <= 2:
        return []
    if top is None:                                     # ladder: doubling points above lo, and tmax itself
        if lo >= tmax:
            return []
        pts, T = [], max(2, lo)
        while T < tmax:
            T = min(2 * T, tmax)
            if T not in st:
                pts.append(T)
        return pts[:k]
    span = [T for T in range(lo + 2, top, 2) if T not in st]   # bisection below the first UNSAT or UNKNOWN
    if not span:
        return []
    idx = sorted({round(j * (len(span) - 1) / max(1, k - 1)) for j in range(k)}) if len(span) > k else range(len(span))
    return [span[j] for j in idx][:k]


def search(targets, tmax):
    while True:
        have = done()
        tasks = []
        for g in targets:
            tasks += [(g, T) for T in next_points(g, tmax, have, JOBS)]
        if not tasks:
            return
        run_tasks(tasks)


# ---------------------------------------------------------------- controls and the wheel's windows
def controls():
    rng = random.Random(20261008)
    bad = n = 0
    for right in range(1 << 13):
        rows = rows_from(right, 14)
        for T in (0, 2, 4):
            n += 1
            seq = [(rows[T + 2 * k] >> 1) & 1 for k in range(5)]
            bad += in_gap3(window(rows[T])) != (seq == [1, 0, 0, 0, 1])
    hits = 0
    for _ in range(3000):
        right = rng.getrandbits(rng.randint(16, 64))
        rows = rows_from(right, 310)
        for T in range(0, 301, 2):
            n += 1
            seq = [(rows[T + 2 * k] >> 1) & 1 for k in range(5)]
            g = in_gap3(window(rows[T]))
            hits += g
            bad += g != (seq == [1, 0, 0, 0, 1])
    print('RV3-C1', 'PASS' if not bad else 'FAIL (%d)' % bad, '(%d comparisons, %d 3-gaps among them)' % (n, hits),
          flush=True)
    return not bad


def wheel_windows():
    sys.path.insert(0, HERE)
    _argv, sys.argv = sys.argv, sys.argv[:1]
    import rule30_walls as wl
    sys.argv = _argv
    U = [int(c) for c in wl.U]
    P = 56
    rng = random.Random(4242)
    seen = set()
    for i in range(400):
        rows = rows_from(rng.getrandbits((16, 24, 32, 48, 64)[i % 5]) | 1, 3000)
        c1 = [(r >> 1) & 1 for r in rows]
        t = 0
        while t + P < len(c1):
            d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
            if d is None:
                t += 1
                continue
            s = t + P
            while s < len(c1) and c1[s] == U[(s - d) % P]:
                s += 1
            for u in range(t + 2 * P, s - 10):          # at least 112 steps into the lock, away from its end
                if u % 2 == 0:
                    seen.add(window(rows[u]))
            t = s
    return seen


# ---------------------------------------------------------------- the run
def run():
    os.makedirs(SCRATCH, exist_ok=True)
    c1 = controls()
    run_tasks([('gap3', 210)])                          # C4 first
    search(['gap3'], TMAX_GAP)
    have = done()
    st, lo, hi = bounds('gap3', have)
    final = []
    if hi is not None and hi - lo == 2:
        run_tasks([('direct', lo), ('direct', hi)])
        run_tasks([('gap3', hi)], proof=True, kind='P')
        final = [('gap3', lo, hi)]
    search(['w%02d' % n for n in range(32)], TMAX_WIN)
    have = done()
    for n in range(32):
        g = 'w%02d' % n
        s, lo_w, hi_w = bounds(g, have)
        if hi_w is not None and hi_w - lo_w == 2:
            final.append((g, lo_w, hi_w))
    run_tasks([(g, hi_w) for g, lo_w, hi_w in final if g != 'gap3'], proof=True, kind='P')
    report(c1)


def report(c1=None):
    have = done()
    sats = [(k, v) for k, v in have.items() if v[0] == 'SAT']
    c2 = all(v[1] == 'replay-pass' for k, v in sats)
    proofs = {(g[1:], T): v for (g, T), v in have.items() if g.startswith('P')}
    c2 &= all(v[1] == 'VERIFIED' for v in proofs.values())
    st, lo, hi = bounds('gap3', {k: v for k, v in have.items() if not k[0].startswith('P')})
    print('gap3: last SAT', lo, 'first UNSAT', hi, 'status', sorted(st.items()))
    if hi is not None and hi - lo == 2:
        print('T3 =', lo, 'witness row (hex, bit k = site k + 1):', have[('gap3', lo)][3])
        say_no = os.path.join(SCRATCH, 'p_gap3_%d.drat' % hi)
        cnf_lo = os.path.join(SCRATCH, 'i_gap3_%d.cnf' % lo)
        if os.path.exists(say_no):
            nv, cl, _, _ = instance('gap3', lo)
            write_cnf(cnf_lo, nv, cl)
            d = subprocess.run(['drat-trim', cnf_lo, say_no, '-t', str(DRAT_CAP)], capture_output=True, text=True)
            ok = 's VERIFIED' not in d.stdout
            os.unlink(cnf_lo)
            print('RV3-C2 say-no control', 'PASS' if ok else 'FAIL')
            c2 &= ok
        dlo, dhi = have.get(('direct', lo), ('?',))[0], have.get(('direct', hi), ('?',))[0]
        print('RV3-C3', 'PASS' if (dlo, dhi) == ('SAT', 'UNSAT') else 'FAIL', dlo, dhi)
    print('RV3-C2', 'PASS' if c2 else 'FAIL', '(%d SAT replays, %d proofs)' % (len(sats), len(proofs)))
    print('RV3-C4', 'PASS' if have.get(('gap3', 210), ('',))[0] == 'SAT' else 'FAIL')
    mono = True
    for g in {k[0] for k in have if not k[0].startswith('P')}:
        s, lo_g, hi_g = bounds(g, have)
        mono &= hi_g is None or lo_g < hi_g
    print('RV3-C5', 'PASS' if mono else 'FAIL')
    alive, dead, deaths = [], [], {}
    for n in range(32):
        s, lo_w, hi_w = bounds('w%02d' % n, have)
        if s.get(TMAX_WIN) == 'SAT':
            alive.append(n)
        elif hi_w is not None and hi_w <= TMAX_WIN:
            dead.append(n)
            deaths[n] = lo_w if hi_w - lo_w == 2 else (lo_w, hi_w)
    print('windows alive at %d: %s' % (TMAX_WIN, [''.join(map(str, wbits(n))) for n in alive]))
    print('window death times (sites 1..5: last even T):', {''.join(map(str, wbits(n))): v for n, v in deaths.items()})
    if hi is not None and hi - lo == 2:
        print('RV3-P1', 'HELD' if hi <= TMAX_GAP and proofs.get(('gap3', hi), ('', ''))[1] == 'VERIFIED' else 'REFUTED')
    else:
        print('RV3-P1', 'REFUTED (no boundary found up to %d)' % TMAX_GAP if st.get(TMAX_GAP) == 'SAT'
              else 'UNDECIDED (bounds %s, %s)' % (lo, hi))
    print('RV3-P2', 'HELD' if lo > 420 else 'REFUTED')
    print('RV3-P3', 'HELD' if len(alive) >= 8 and len(dead) >= 8 else 'REFUTED', len(alive), len(dead))
    wheel = wheel_windows()
    extra = [n for n in alive if wbits(n) not in wheel]
    print('RV3-P4', 'HELD' if not extra else 'REFUTED', 'wheel windows', len(wheel),
          'alive but not on the wheel', [''.join(map(str, wbits(n))) for n in extra])
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True, env=dict(os.environ, NP_SCRATCH_RV3=SCRATCH))
    print('launched; checkpoint %s; log %s' % (CK, LOG))


def status():
    have = done()
    for g in ['gap3', 'direct'] + ['w%02d' % n for n in range(32)]:
        st, lo, hi = bounds(g, have)
        if st:
            print(g, 'last SAT', lo, 'first UNSAT', hi, 'calls', len(st))
    if os.path.exists(LOG):
        print(open(LOG).read()[-800:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run, 'controls': controls, 'report': report}[cmd]()
