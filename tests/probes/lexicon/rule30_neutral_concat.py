#!/usr/bin/env python3
"""rule30_neutral_concat.py: NL, do G239's neutral choices repeat freely in actual clamped right rows?
(portfolio question 4's lower direction; GPT's GC605, GC606 and GC607 leave "mixed repeated choices" OPEN.)
Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before it started.

RUN-ON:     cpu, up to 5 kissat processes (drat-trim for UNSAT proofs); resumable
COMMAND:    NP_SCRATCH_NL=<data folder> python3 tests/probes/lexicon/rule30_neutral_concat.py start | status | resume
            python3 tests/probes/lexicon/rule30_neutral_concat.py controls      (C1 and C2 only, about a minute)
COST:       to be recorded; expected under an hour (the largest instances have about 13,000 cells).

The model is GC499's: Rule 30 on the right half, sites 1, 2, ..., with the wall at site 0 clamped to 0 at even times
and 1 at odd times; the initial right row is arbitrary and the rest is autonomous. The visible trace is site 1 at even
times. G239's blocks are S = 100 and L = 10000. A word w over {S, L} with K blocks is realized when some initial row
has visible symbols, from visible index s0 on, equal to the blocks of w followed by a closing 1 (so every gap is
exactly 2 or 4). GC606 (short, prefix 11101) and GC607 (long, prefixes 111001 and 111000001) give single returns to
1110; whether the returns can be chained in every order is the open question this probe measures.

Modes. A: w at s0 = 0 (a visible prefix from time 0). B: as A, and also sites 1 .. 3 read 111 at every visible 1 of
w and at the closing 1 (G239's width-3 common state, through which GC605 to GC607's returns pass). Each mode searches
the word tree level by level: a level-K word is tried only when its level-(K - 1) parent was SAT. The visible target
of w is a prefix of every extension's target, so an UNSAT word kills its whole subtree; nothing is lost by pruning.
A4: every UNSAT word of A again at s0 = 4 (time 8), to separate a startup effect from an obstruction (GC603).
G: the 216 words of three of G239's six neutral length-28 blocks (18 S/L blocks, 85 visible symbols), mode A.
Late: 32 fixed random words of 8 blocks at s0 = 64 (time 128), mode A.

Method. One SAT instance per word over the light cone (cells x_t(i), 1 <= i <= sites + T - t, the wall a constant,
the initial cells free), with unit clauses for the targets; kissat (cap per call). A SAT model is replayed by direct
simulation from its initial row; an UNSAT is re-solved with a DRAT proof checked by drat-trim (the first 64 per mode).

PREDICTIONS (Local's, published before the run):
  NL-C1 (control): by simulation, every right row beginning 11101 (zero tail, and 2,000 random tails of 1 .. 40 bits)
         shows visible 1, 0, 0 and returns sites 1 .. 4 to 1110 at time 6 (GC606); every row beginning 111001 or
         111000001 shows 1, 0, 0, 0, 0 and returns to 1110 at time 10 (GC607); 111000000 with zero tail has site 2
         equal to 0 at time 10 (GC606's guard).
  NL-C2 (control): the encoder agrees with simulation: for 100 random initial rows with their own simulated visible
         bits (and the B-mode sites at every even time) as targets plus the initial row as units, the CNF is SAT;
         with one target bit flipped it is UNSAT (the instance can say no).
  NL-C3 (control): every SAT model replays by simulation; every UNSAT proof that is checked is VERIFIED.
  NL-P1 (blind, confidence 0.6): mode A realizes every word with K <= 16 (no UNSAT, no UNKNOWN).
  NL-P2 (blind, confidence 0.55): mode B realizes every word with K <= 14.
  NL-P3 (blind, confidence 0.6): all 216 three-block G239 words are realized (mode G).
  NL-P4 (blind, confidence 0.5): all 32 late words are realized at time 128 within the cap.
  D1 (descriptive): per mode and level, the SAT, UNSAT and UNKNOWN counts and solve times; every UNSAT word with its
         proof status, and its A4 verdict.
Counterfactual: an UNSAT in mode A at small K is an actual obstruction to free repetition, a concrete word for GPT's
hand mechanism to explain; failures only in mode B mean the choices repeat but not through one shared state 111.
Either way a finite K says nothing about all lengths: full realization to K = 16 is evidence for, not a proof of,
positive entropy; no uniform construction follows from it.
"""
import os
import random
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRATCH = os.environ.get('NP_SCRATCH_NL', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-nl'))
CK = os.path.join(SCRATCH, 'nl.ck')
LOG = os.path.join(SCRATCH, 'nl.log')
CAP = 600
CAP_LATE = 1800
CAP_PROOF = 3600
DRAT_CAP = 20000
PROOFS_PER_MODE = 64
JOBS = 5
KMAX = {'A': 16, 'B': 14}
BLOCK = {'S': (1, 0, 0), 'L': (1, 0, 0, 0, 0)}
G239 = ['L' * p + 'S' + 'L' * (5 - p) for p in range(6)]


# ---------------------------------------------------------------- simulation (RV3's coding: bit i is site i, bit 0 the wall)
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


def site(row, i):
    return (row >> i) & 1


# ---------------------------------------------------------------- targets
def targets(word, mode, s0):
    """unit targets (time, site, value) and the last time: the blocks of `word` and a closing 1 from visible s0"""
    vis = [v for b in word for v in BLOCK[b]] + [1]
    cons = [(2 * (s0 + k), 1, v) for k, v in enumerate(vis)]
    if mode == 'B':
        cons += [(2 * (s0 + k), i, 1) for k, v in enumerate(vis) if v == 1 for i in (2, 3)]
    return cons, 2 * (s0 + len(vis) - 1)


# ---------------------------------------------------------------- CNF over the light cone
_base, _lock = {}, threading.Lock()


def base(Tend, sites):
    """the cone's clauses as DIMACS text without header, the variable map's offsets and the widths"""
    key = (Tend, sites)
    with _lock:
        if key in _base:
            return _base[key]
    width = [sites + Tend - t for t in range(Tend + 1)]
    off, n = [], 0
    for t in range(Tend + 1):
        off.append(n)
        n += width[t]
    lines = []
    for t in range(1, Tend + 1):
        wall = (t - 1) % 2
        for i in range(1, width[t] + 1):
            y, c, r = off[t] + i, off[t - 1] + i, off[t - 1] + i + 1
            if i == 1:                                  # y = wall XOR (c OR r)
                if wall == 0:
                    lines += ['%d %d 0' % (-c, y), '%d %d 0' % (-r, y), '%d %d %d 0' % (c, r, -y)]
                else:
                    lines += ['%d %d 0' % (-c, -y), '%d %d 0' % (-r, -y), '%d %d %d 0' % (c, r, y)]
                continue
            l = off[t - 1] + i - 1
            for a in (0, 1):
                for b in (0, 1):
                    for d in (0, 1):
                        f = a ^ (b | d)
                        lines.append('%d %d %d %d 0' % ((l if a == 0 else -l), (c if b == 0 else -c),
                                                        (r if d == 0 else -r), (y if f == 1 else -y)))
    val = ('\n'.join(lines) + '\n', len(lines), n, off, width)
    with _lock:
        _base[key] = val
    return val


def cnf_text(cons, Tend, extra_units=()):
    sites = max(i for _, i, _ in cons)
    body, ncl, nv, off, width = base(Tend, sites)
    units = ['%d 0' % (off[t] + i if v else -(off[t] + i)) for t, i, v in cons] + list(extra_units)
    return 'p cnf %d %d\n' % (nv, ncl + len(units)) + body + '\n'.join(units) + '\n', width[0]


def replay(cons, Tend, init):
    right = sum(v << k for k, v in enumerate(init))
    rows = rows_from(right, Tend + 1)
    return all(site(rows[t], i) == v for t, i, v in cons)


def kissat(text, cap, proof=None):
    if proof is None:
        return subprocess.run(['kissat', '-q', '--time=%d' % cap], input=text, capture_output=True, text=True)
    cnf = proof[:-5] + '.cnf'
    with open(cnf, 'w') as f:
        f.write(text)
    r = subprocess.run(['kissat', '-q', '-f', '--no-binary', '--time=%d' % cap, cnf, proof],
                       capture_output=True, text=True)
    return r


def model(stdout, ninit):
    val = set()
    for line in stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    return [1 if (i + 1) in val else 0 for i in range(ninit)]    # time-0 cells are variables 1 .. ninit


def solve(task, cap=CAP):
    mode, word, s0 = task
    t0 = time.time()
    cons, Tend = targets(word, 'B' if mode == 'B' else 'A', s0)
    text, ninit = cnf_text(cons, Tend)
    r = kissat(text, cap)
    secs = time.time() - t0
    if r.returncode == 10:
        init = model(r.stdout, ninit)
        ok = replay(cons, Tend, init)
        return task, 'SAT', 'replay-pass' if ok else 'replay-FAIL', secs, '%x' % sum(v << k for k, v in enumerate(init))
    if r.returncode == 20:
        return task, 'UNSAT', 'noproof', secs, '-'
    return task, 'UNKNOWN', 'rc%d' % r.returncode, secs, '-'


def prove(task):
    mode, word, s0 = task
    t0 = time.time()
    cons, Tend = targets(word, 'B' if mode == 'B' else 'A', s0)
    text, _ = cnf_text(cons, Tend)
    prf = os.path.join(SCRATCH, 'p_%s_%s_%d.drat' % (mode, word, s0))
    r = kissat(text, CAP_PROOF, prf)
    cnf = prf[:-5] + '.cnf'
    extra = 'proof-rc%d' % r.returncode
    if r.returncode == 20:
        d = subprocess.run(['drat-trim', cnf, prf, '-t', str(DRAT_CAP)], capture_output=True, text=True)
        extra = 'VERIFIED' if 's VERIFIED' in d.stdout else 'NOT-VERIFIED'
    for p in (cnf, prf):
        if os.path.exists(p):
            os.unlink(p)
    return task, 'UNSAT', extra, time.time() - t0, '-'


# ---------------------------------------------------------------- checkpoint
def done():
    res = {}
    if os.path.exists(CK):
        for line in open(CK):
            f = line.split()
            if len(f) == 8 and f[-1] == 'END':
                res[f[0], f[1], int(f[2])] = (f[3], f[4], float(f[5]), f[6])
    return res


def record(task, verdict, extra, secs, hexrow, kind=''):
    if os.path.exists(CK) and os.path.getsize(CK) > 0:
        with open(CK, 'rb') as f:
            f.seek(-1, 2)
            torn = f.read(1) != b'\n'
        if torn:
            with open(CK, 'a') as f:
                f.write('\n')
    mode, word, s0 = task
    with open(CK, 'a') as f:
        f.write('%s%s %s %d %s %s %.2f %s END\n' % (kind, mode, word or '-', s0, verdict, extra, secs, hexrow))


def say(msg):
    print('%s %s' % (time.strftime('%H:%M:%S'), msg), flush=True)


def run_tasks(tasks, fn=solve, kind='', cap=None):
    have = done()
    todo = [t for t in tasks if (kind + t[0], t[1] or '-', t[2]) not in have]
    if todo:
        with ThreadPoolExecutor(JOBS) as ex:
            futs = [ex.submit(fn, t) if cap is None else ex.submit(fn, t, cap) for t in todo]
            for fut in as_completed(futs):                  # record each result as it finishes
                task, verdict, extra, secs, hexrow = fut.result()
                record(task, verdict, extra, secs, hexrow, kind)
                if verdict != 'SAT' or extra != 'replay-pass':
                    say('%s%s %s s0 %d: %s %s %.1f s' % (kind, task[0], task[1], task[2], verdict, extra, secs))
    have = done()
    return {t: have[(kind + t[0], t[1] or '-', t[2])] for t in tasks}


# ---------------------------------------------------------------- controls
def controls():
    rng = random.Random(20261008)
    bad = 0
    cyl = [('11101', 6, (1, 0, 0)), ('111001', 10, (1, 0, 0, 0, 0)), ('111000001', 10, (1, 0, 0, 0, 0))]
    n = 0
    for pre, dur, vis in cyl:
        for k in range(2001):
            tl = 0 if k == 0 else rng.randint(1, 40)
            tail = 0 if k == 0 else rng.getrandbits(tl)
            right = sum(int(ch) << j for j, ch in enumerate(pre)) | (tail << len(pre))
            rows = rows_from(right, dur + 1)
            got = tuple(site(rows[2 * j], 1) for j in range(len(vis)))
            ret = tuple(site(rows[dur], i) for i in (1, 2, 3, 4))
            n += 1
            if got != vis or ret != (1, 1, 1, 0):
                bad += 1
    rows = rows_from(sum(int(ch) << j for j, ch in enumerate('111000000')), 11)
    guard = site(rows[10], 2) == 0
    c1 = bad == 0 and guard
    say('NL-C1 %s (%d cylinder rows, %d failures; 111000000 guard %s)' % ('PASS' if c1 else 'FAIL', n, bad, guard))
    # C2: the encoder against simulation, both answers
    ok2, n2 = True, 0
    for k in range(100):
        mode = 'B' if k % 2 else 'A'
        sites = 3 if mode == 'B' else 1
        Tend = 2 * rng.randint(1, 30)
        ninit = sites + Tend
        init = [rng.getrandbits(1) for _ in range(ninit)]
        rows = rows_from(sum(v << j for j, v in enumerate(init)), Tend + 1)
        cons = [(t, i, site(rows[t], i)) for t in range(0, Tend + 1, 2) for i in range(1, sites + 1)]
        units = ['%d 0' % (j + 1 if v else -(j + 1)) for j, v in enumerate(init)]
        text, _ = cnf_text(cons, Tend, units)
        yes = kissat(text, 60).returncode == 10
        j = rng.randrange(len(cons))
        flip = cons[:j] + [(cons[j][0], cons[j][1], 1 - cons[j][2])] + cons[j + 1:]
        text, _ = cnf_text(flip, Tend, units)
        no = kissat(text, 60).returncode == 20
        n2 += 2
        if not (yes and no):
            ok2 = False
    say('NL-C2 %s (%d encoder checks)' % ('PASS' if ok2 else 'FAIL', n2))
    return c1 and ok2


# ---------------------------------------------------------------- the run
def tree(mode):
    level, per = [''], {}
    for K in range(1, KMAX[mode] + 1):
        cand = [w + b for w in level for b in 'SL']
        res = run_tasks([(mode, w, 0) for w in cand])
        level = [w for w in cand if res[(mode, w, 0)][0] == 'SAT']
        cnt = {v: sum(1 for w in cand if res[(mode, w, 0)][0] == v) for v in ('SAT', 'UNSAT', 'UNKNOWN')}
        secs = [res[(mode, w, 0)][2] for w in cand]
        per[K] = (len(cand), cnt, max(secs), sum(secs) / len(secs))
        say('%s K %d: %d words, SAT %d, UNSAT %d, UNKNOWN %d, max %.2f s, mean %.3f s'
            % (mode, K, len(cand), cnt['SAT'], cnt['UNSAT'], cnt['UNKNOWN'], max(secs), sum(secs) / len(secs)))
        if not level:
            break
    return per


def run():
    os.makedirs(SCRATCH, exist_ok=True)
    c = controls()
    if not c:
        say('controls failed: stopping')
        return
    per = {m: tree(m) for m in ('A', 'B')}
    have = done()
    for m in ('A', 'B'):
        uns = sorted(k[1] for k, v in have.items() if k[0] == m and k[2] == 0 and v[0] == 'UNSAT')
        run_tasks([(m, w, 0) for w in uns[:PROOFS_PER_MODE]], fn=prove, kind='P')
        if m == 'A' and uns:
            run_tasks([('A', w, 4) for w in uns])
    g = [a + b + c for a in G239 for b in G239 for c in G239]
    run_tasks([('G', w, 0) for w in g])
    rng = random.Random(1281008)
    late = sorted({''.join(rng.choice('SL') for _ in range(8)) for _ in range(40)})[:32]
    run_tasks([('Late', w, 64) for w in late], cap=CAP_LATE)
    report()


def report():
    have = done()
    say('---- report')
    fails = [k for k, v in have.items() if v[0] == 'SAT' and v[1] != 'replay-pass']
    proofs = [v[1] for k, v in have.items() if k[0].startswith('P')]
    say('NL-C3 %s (%d SAT replays, %d failures; proofs %s)' % (
        'PASS' if not fails and all(p == 'VERIFIED' for p in proofs) else 'FAIL',
        sum(1 for v in have.values() if v[0] == 'SAT'), len(fails),
        {p: proofs.count(p) for p in set(proofs)}))

    def tally(mode, s0=0, kmax=None):
        rows = [(k[1], v[0]) for k, v in have.items() if k[0] == mode and k[2] == s0
                and (kmax is None or len(k[1]) <= kmax)]
        return {x: sum(1 for _, y in rows if y == x) for x in ('SAT', 'UNSAT', 'UNKNOWN')}, rows

    for m, P in (('A', 'NL-P1'), ('B', 'NL-P2')):
        cnt, rows = tally(m, 0, KMAX[m])
        full = sum(1 for w, v in rows if len(w) == KMAX[m] and v == 'SAT') == 2 ** KMAX[m]
        say('%s %s: %s; level %d complete: %s' % (P, 'HELD' if full and cnt['UNSAT'] == cnt['UNKNOWN'] == 0
                                                 else 'REFUTED or undecided', cnt, KMAX[m], full))
        uns = sorted(w for w, v in rows if v == 'UNSAT')
        if uns:
            say('%s UNSAT words (%d), shortest first: %s' % (m, len(uns), sorted(uns, key=len)[:20]))
            if m == 'A':
                say('A4 at s0 = 4: %s' % {w: have.get(('A', w, 4), ('-',))[0] for w in sorted(uns, key=len)[:20]})
    cnt, _ = tally('G')
    say('NL-P3 %s: %s of 216' % ('HELD' if cnt['SAT'] == 216 else 'REFUTED or undecided', cnt))
    cnt, _ = tally('Late', 64)
    say('NL-P4 %s: %s of 32' % ('HELD' if cnt['SAT'] == 32 else 'REFUTED or undecided', cnt))
    say('COMPLETE')


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    with open(LOG, 'a') as lg:
        subprocess.Popen([sys.executable, os.path.abspath(__file__), 'run'], stdout=lg, stderr=subprocess.STDOUT,
                         start_new_session=True)
    print('started; log at', LOG)


def status():
    have = done()
    for m in ('A', 'B', 'G', 'Late', 'PA', 'PB'):
        rows = [v[0] for k, v in have.items() if k[0] == m]
        print(m, {x: rows.count(x) for x in set(rows)})


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd in ('start', 'resume'):
        launch()
    elif cmd == 'run':
        run()
    elif cmd == 'controls':
        os.makedirs(SCRATCH, exist_ok=True)
        controls()
    elif cmd == 'report':
        report()
    else:
        status()
