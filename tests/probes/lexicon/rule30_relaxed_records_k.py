#!/usr/bin/env python3
"""rule30_relaxed_records_k.py: RLK, relaxed realizable records with forbidden words to length K = 16, d to 120.

RUN-ON:     cpu (Python 3, cc, kissat 4.0.4 as KISSAT); one core per (K, phase) sweep
COMMAND:    python3 tests/probes/lexicon/rule30_relaxed_records_k.py lang K           (language, words, C1)
            python3 tests/probes/lexicon/rule30_relaxed_records_k.py control           (C2: relax10 vs RRL)
            python3 tests/probes/lexicon/rule30_relaxed_records_k.py sweep K PHASE [DMAX=120] [CAP=3600]  (resumable)
            python3 tests/probes/lexicon/rule30_relaxed_records_k.py status K
COST:       the language at K = 16 enumerates 2^31 right words (minutes in C); each sweep is unknown in advance,
            capped per SAT call. Data in NP_SCRATCH_RLK (default ~/np-scratch-int/rule30-rlk), never in git.

Why (the owner's steer, 2026-10-10, adopting Cloud's assessment). Period 2 needs R_real(d) finite for every d; the
data puts R_real(d) between 12 and 16 for every decided d from 21 to 116 (RR, RR2, RR3). Cloud's RRL (CL041) showed
that column-1 sequences avoiding the minimal forbidden visible words up to length K reproduce the actual records
exactly up to a depth that grows with K: seven words of length <= 10 are exact to d = 25, and the first gap turns on
one missing word of length 14. Records under the relaxation bound the actual ones from above (a forbidden word is
forbidden for every right half), so if some K keeps relaxK(d) <= 17 to large d, the obstruction looks finite-type,
and boundedness becomes an automaton question with a possible machine-checkable certificate. relaxK is non-increasing
in K, so K = 16 alone answers whether any K <= 16 stays flat.

Method. `lang`: rule30_visible_lang.c enumerates every right word of length 2K - 1 (GC500) and prints the visible
words of length K; shorter languages are their prefixes (the language is prefix- and factor-closed). The minimal
forbidden words are RRL's: w absent, both w[:-1] and w[1:] present. `sweep`: RRL's relaxed model, unchanged (left
half and centre in the centre's light cone to T = d + L - 1, column 1 free, the clock imposed at the centre per
phase, the initial white band at depths d .. d + L - 1), each forbidden word excluded at every visible window, solved
by kissat, every SAT model checked by simulation. Depths climb with the plateau law R(d + 1) >= R(d) - 1 (a band at
depth d of length L contains one at depth d + 1 of length L - 1 under the same horizon), so each depth starts at the
last record and climbs until UNSAT (exact) or the cap (a lower bound).

Record searched: `record_find.py RRL` -> 26 hits (RULE30-PRIZE §8.78, RULE30-GPT GC549.18 .. 26, PROOFS G238); the
relaxed records exist only to d = 41 at K = 10 (RRL); `record_find.py relaxed forbidden K` -> RRL only.

PREDICTIONS (Local's, pushed before any run of this script):
  RLK-C1 (control): C_n for n = 1 .. 10 is 2, 3, 5, 8, 12, 17, 25, 36, 50, 68; the minimal forbidden words of length
         <= 10 are RRL's seven (11, 00000, 101001, 0100101, 010010001, 0101000101, 0101010000); the length-14 list
         contains RRL's gap word 01000010001001.
  RLK-C2 (control): this script's kissat path reproduces RRL's relax10 records per phase at d = 21, 25, 29, 33:
         phase 0: 14, 10, 7, 9; phase 1: 15, 11, 7, 8.
  RLK-C3 (control): wherever both are exact, relax16 >= the actual R_real for that phase's maximum, and relax16 <=
         relax10 at the control depths.
  RLK-P1 (blind, 0.65): relax16 climbs: its maximum over the two phases exceeds 17 at some d <= 120.
  RLK-P2 (blind, 0.6): relax16 (max over phases) equals the actual R_real at every d <= 30.
  RLK-P3 (the unexpected check, 0.5): at most 20 minimal forbidden words have any one length n = 11 .. 16.
  Counterfactual. If relax16 stays <= 17 to d = 120, that is the finite-type signal Cloud named: next is an automaton
  for the relaxed system and a certificate of boundedness. If it climbs, lookahead 16 is insufficient. By GC549.21 a
  climb at fixed K does not prove the obstruction is not of finite type; it says the forbidden words that matter are
  longer than K, and K = 18 is the next step.
"""
import os
import re
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.environ.get('NP_SCRATCH_RLK', os.path.expanduser('~/np-scratch-int/rule30-rlk'))
KISSAT = os.environ.get('KISSAT', 'kissat')
SEVEN = ['11', '00000', '101001', '0100101', '010010001', '0101000101', '0101010000']
C10 = [2, 3, 5, 8, 12, 17, 25, 36, 50, 68]
RRL10 = {21: (14, 15), 25: (10, 11), 29: (7, 7), 33: (9, 8)}


def helper():
    exe = os.path.join(DIR, 'rule30_visible_lang')
    src = os.path.join(HERE, 'rule30_visible_lang.c')
    if not os.path.exists(exe) or os.path.getmtime(exe) < os.path.getmtime(src):
        subprocess.run(['cc', '-O3', '-o', exe, src, '-lpthread'], check=True)
    return exe


def language(K, threads=1):
    path = os.path.join(DIR, 'lang%d.txt' % K)
    if not os.path.exists(path):
        t0 = time.time()
        out = subprocess.run([helper(), str(K), str(threads)], capture_output=True, text=True, check=True).stdout
        open(path + '.tmp', 'w').write(out)
        os.replace(path + '.tmp', path)
        print('language K = %d computed in %.0f s' % (K, time.time() - t0), flush=True)
    top = set(open(path).read().split())
    lang = {K: top}
    for n in range(K - 1, 0, -1):
        lang[n] = {w[:n] for w in lang[n + 1]}
    return lang


def forbidden(lang, K):
    out = []
    for n in range(2, K + 1):
        for m in range(2 ** n):
            w = format(m, '0%db' % n)
            if w not in lang[n] and w[:-1] in lang[n - 1] and w[1:] in lang[n - 1]:
                out.append(w)
    return out


def load_forbidden(K):
    path = os.path.join(DIR, 'mfw%d.txt' % K)
    if not os.path.exists(path):
        return None
    return open(path).read().split()


class Relaxed:
    """RRL's relaxed model (rule30_cloud_relaxed_records.py), as a clause list for an external solver."""

    def __init__(self, d, L, phase, forb):
        self.T = T = d + L - 1
        self.d, self.L, self.phase = d, L, phase
        self.nv, self.var, cl = 0, {}, []
        for t in range(T):
            self.v(('y', t))
        for t in range(T):
            for i in range(-(T - t - 1), 1):
                l, c = self.x(t, i - 1), self.x(t, i)
                r = self.v(('y', t)) if i == 0 else self.x(t, i + 1)
                y, o = self.x(t + 1, i), self.new()
                cl += [[-c, o], [-r, o], [c, r, -o]]
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
        for t in range(T + 1):
            cl.append([self.x(t, 0)] if (t + phase) % 2 else [-self.x(t, 0)])
        for j in range(d, d + L):
            cl.append([-self.x(0, -j)])
        self.vis = [self.v(('y', t)) for t in range(T) if (t + phase) % 2 == 0]
        for w in forb:
            for s in range(len(self.vis) - len(w) + 1):
                cl.append([(-self.vis[s + k] if w[k] == '1' else self.vis[s + k]) for k in range(len(w))])
        self.cl = cl

    def new(self):
        self.nv += 1
        return self.nv

    def v(self, key):
        if key not in self.var:
            self.var[key] = self.new()
        return self.var[key]

    def x(self, t, i):
        return self.v(('x', t, i))

    def solve(self, cap, forb):
        """'SAT' (model checked by simulation), 'UNSAT', or 'UNKNOWN' (cap)."""
        with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=DIR, delete=False) as f:
            f.write('p cnf %d %d\n' % (self.nv, len(self.cl)))
            f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in self.cl))
            name = f.name
        try:
            p = subprocess.run([KISSAT, '-q', '--time=%d' % cap, name], capture_output=True, text=True)
        finally:
            os.unlink(name)
        if p.returncode == 20:
            return 'UNSAT'
        if p.returncode != 10:
            return 'UNKNOWN'
        m = set()
        for line in p.stdout.splitlines():
            if line.startswith('v'):
                m.update(int(z) for z in line.split()[1:] if int(z) > 0)
        self.check(m, forb)
        return 'SAT'

    def check(self, m, forb):
        T = self.T
        y = [int(self.v(('y', t)) in m) for t in range(T)]
        row = {i: int(self.x(0, i) in m) for i in range(-T, 1)}
        for t in range(T + 1):
            if row[0] != (t + self.phase) % 2:
                raise RuntimeError('clock failed in simulation at t=%d' % t)
            if t == T:
                break
            ext = dict(row)
            ext[1] = y[t]
            row = {i: ext.get(i - 1, 0) ^ (ext.get(i, 0) | ext.get(i + 1, 0)) for i in range(-(T - t - 1), 1)}
        if any(int(self.x(0, -j) in m) for j in range(self.d, self.d + self.L)):
            raise RuntimeError('white band failed')
        vis = ''.join(str(y[t]) for t in range(T) if (t + self.phase) % 2 == 0)
        bad = [w for w in forb if w in vis]
        if bad:
            raise RuntimeError('forbidden word in the model: %s' % bad[:3])


def ck_path(K, phase):
    return os.path.join(DIR, 'rlk_K%d_p%d.ck' % (K, phase))


def read_ck(K, phase):
    got = {}
    p = ck_path(K, phase)
    if os.path.exists(p):
        for line in open(p):
            f = line.split()
            if line.endswith('\n') and len(f) == 6 and f[5] == 'END':
                got.setdefault(int(f[0]), []).append((int(f[1]), f[2], float(f[3])))
    return got


def record_of(calls):
    """(value, exact) from a depth's calls: largest SAT L, exact if L + 1 is UNSAT."""
    sat = max([L for L, v, _ in calls if v == 'SAT'] + [0])
    exact = any(L == sat + 1 and v == 'UNSAT' for L, v, _ in calls)
    return sat, exact


def sweep(K, phase, dmax=120, cap=3600):
    forb = load_forbidden(K)
    assert forb is not None, 'run lang %d first' % K
    got = read_ck(K, phase)
    prev = None
    for d in range(3, dmax + 1):
        calls = got.get(d, [])
        known = {L: v for L, v, _ in calls}
        floor = max(prev - 1, 0) if prev is not None else 0          # plateau law: SAT without a call
        L = max([floor] + [L for L, v in known.items() if v == 'SAT']) + 1
        while True:
            if L in known:
                v = known[L]
            else:
                t0 = time.time()
                v = Relaxed(d, L, phase, forb).solve(cap, forb)
                with open(ck_path(K, phase), 'a') as f:
                    f.write('%d %d %s %.1f %s END\n' % (d, L, v, time.time() - t0, time.strftime('%H:%M')))
                print('K=%d phase %d d=%d L=%d %s %.0f s' % (K, phase, d, L, v, time.time() - t0), flush=True)
            if v != 'SAT':
                break
            L += 1
        prev = L - 1
        if v == 'UNKNOWN':
            print('K=%d phase %d d=%d: lower bound %d (capped)' % (K, phase, d, prev), flush=True)


def status(K):
    rows = {}
    for ph in (0, 1):
        for d, calls in read_ck(K, ph).items():
            rows.setdefault(d, {})[ph] = record_of(calls)
    for d in sorted(rows):
        r = rows[d]
        cells = ['%2d%s' % (r[ph][0], '' if r[ph][1] else '+') if ph in r else ' -' for ph in (0, 1)]
        best = max(r[ph][0] for ph in r)
        print('d=%3d  phase0 %s  phase1 %s  max %2d' % (d, cells[0], cells[1], best))


def main():
    os.makedirs(DIR, exist_ok=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'lang':
        K = int(sys.argv[2])
        lang = language(K, int(sys.argv[3]) if len(sys.argv) > 3 else 1)
        forb = forbidden(lang, K)
        open(os.path.join(DIR, 'mfw%d.txt' % K), 'w').write('\n'.join(forb) + '\n')
        sizes = [len(lang[n]) for n in range(1, K + 1)]
        per = {n: sum(len(w) == n for w in forb) for n in range(2, K + 1)}
        print('C_n, n = 1 .. %d: %s' % (K, sizes))
        print('minimal forbidden words per length: %s (total %d)' % (per, len(forb)))
        c1 = sizes[:10] == C10 and [w for w in forb if len(w) <= 10] == SEVEN and \
            (K < 14 or '01000010001001' in forb)
        print('RLK-C1', 'PASS' if c1 else 'FAIL')
        if K >= 16:
            print('RLK-P3', 'HELD' if all(per[n] <= 20 for n in range(11, 17)) else 'REFUTED')
    elif cmd == 'control':
        lang = language(10)
        forb = forbidden(lang, 10)
        ok = True
        for d, want in RRL10.items():
            got = []
            for ph in (0, 1):
                L = 0
                while Relaxed(d, L + 1, ph, forb).solve(3600, forb) == 'SAT':
                    L += 1
                got.append(L)
            ok &= tuple(got) == want
            print('relax10 d=%d: %s (RRL %s)' % (d, tuple(got), want), flush=True)
        print('RLK-C2', 'PASS' if ok else 'FAIL')
    elif cmd == 'sweep':
        K, ph = int(sys.argv[2]), int(sys.argv[3])
        dmax = int(sys.argv[4]) if len(sys.argv) > 4 else 120
        cap = int(sys.argv[5]) if len(sys.argv) > 5 else 3600
        sweep(K, ph, dmax, cap)
    else:
        status(int(sys.argv[2]) if len(sys.argv) > 2 else 16)


if __name__ == '__main__':
    main()
