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
OUTCOME, 2026-10-10 07:31 BST (M5; the K = 16 language took 40 s on 3 threads, K = 18 2,167 s on one; most SAT calls take seconds,
  a few minutes by d = 85). C1, C2 and C3 PASS; P1, P2 and P3 HELD. The K = 18 extension (L557) gave P4, P4b and P5
  HELD, and L558's gap-length prediction REFUTED.
  - C1. C_1..18 = 2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119, 156, 199, 251, 316, 393, 487. RRL's seven words and
    its gap word are in the list.
  - C2. RRL's relax10 records are reproduced at d = 21 .. 33.
  - C3. No relaxed record falls below the actual R_real (K = 16 or 18). relax18 <= relax16 everywhere.
  - The 25 minimal forbidden words up to length 18 (21 up to length 16; at most 3 of any one length, so P3 HELD):
      11 00000 101001 0100101 010010001 0101000101 0101010000 01010001001 10010001001 010010000101 010100010001
      100100010000 0001000010001 1001000010001 00100010000101 01000010001001 10101000010000 001000100001001
      010000100010000 0101000010000101 1000100001010001 00100010001010100 001000010001010100 010000101000010001
      010001000100010101
  - P2: relax16 equals the actual R_real at every d <= 31 (d <= 19 by RRL's relax10 = actual and actual <= relax16 <=
    relax10).
  - P1: relax16 first exceeds 17 at d = 65 (phase 1, 18). It reaches at least 19 at d = 75 and d = 84.
  - P4: relax18 = relax16 except at d = 65 .. 69. P4b: relax18 is 17 at d = 75. P5: relax18 first exceeds 17 at
    d = 84 (at least 19, against an actual 13).
  - Gap witnesses (`gap`):
    - K = 16, d = 75: shortest absent factor of length 17, 00100010001010100 (gaps 4,4,2,2). Unregistered.
    - K = 18, d = 84: length 21, 000010001000100010001 (gaps 5,4,4,4,4). L558 predicted 19 or 20: REFUTED.
  - Reading (L559). Each longer list moves the first excess past 17 deeper (about 40 to 50 at K = 10, 65 at K = 16, 84
    at K = 18), and the missing word sits just beyond the list each time. It is a moving frontier, not a finite list
    that closes. Per GC549.21 this does not exclude every finite-type certificate. GC984 adds the 4,4,2,2 endpoint
    rule: the core is allowed, and only a chain with no 2-gap on either side is forbidden.
PHASE-1 LANGUAGE (registered before its run; L574). relax40's phase-1 sweep uses the phase-0 language's words,
  which only relaxes phase 1: phase 1's visible word starts one step after a black wall, and not every row is
  reachable then. Its d = 45, L = 11 witness (an unregistered diagnostic) has a visible code in the phase-0 language
  that no right half produces from a black start. The phase-1 language L1 is grown by SAT exactly as SOF grows L
  (in_language_phase(w, 1)), and its minimal forbidden words mfw40p1 drive sweep tag 40p1, phase 1.
  RLKP1-C1 (control): L1 is a subset of L at every length, and prefix- and factor-closed.
  RLKP1-P1 (0.85): with mfw40p1, phase 1's record at d = 45 equals the actual (at most 9).
  RLKP1-P2 (0.5): L1 first differs from L at some length <= 15.
PROBE AT TR's DEPTHS (registered before its run; L575, at Cloud's request CL179). One relaxed call at L = 18 per
  phase at d = 124, 128, .., 168 (mfw40 in phase 0; in phase 1 mfw40 for now, then mfw40p1 when L1 is done, both valid
  since L1 c L). UNSAT in both phases certifies R_real(d) <= 17 at d; SAT in a phase leaves it open there (an upper
  bound >= 18 only).
  RLKPR-P1 (blind, 0.5): at least 6 of the 12 depths are certified (UNSAT in both phases).
  RLKPR-P2 (blind, 0.55; RLK40-P2's restatement): at least one depth stays open (SAT at 18 in some phase).
LIFT (registered before its run; L581). `lift TAG d L ph`: re-solve one relaxed SAT, test its visible code for exact
  membership (right_half_for, SAT over the right cone), and if it is in, glue the model's left half to that right
  half and simulate Rule 30: a VALID simulation is a genuine configuration, R_real(d) >= L. `lift MODEL.txt` redoes
  the test from a saved model (L582; probes and lifts now save every relaxed SAT model).
  RLKLF-P1 (0.4): d = 152, L = 18, phase 0, mfw40: the code is in L and the lift succeeds.
  Controls (L582): R_real(21) >= 15 (phase 1) and R_real(25) >= 10 (phase 0) VALID; K = 16 at d = 65, L = 18,
  phase 1 (relaxed SAT where RR2 has R_real <= 17) ABSENT. Its shortest absent factor is 10000101000010001 in L1
  (length 17), 010000101000010001 in L (length 18, one of the 25 above). Defect fixed before any verdict: the
  extraction omitted the cone's last site (GPT, eeb45660; rule30_lift_controls.py).
FIRST EXCESS OF relax40 (found 2026-10-10 12:20 in the paused sweep; registered before the gap run, L583). Phase 0
  at d = 107 is SAT at L = 16 (52 s), where RR3 has R_real(107) = 14 in both phases: relax40's first excess over the
  actual record, so RLK40-P1 and RLK40-P3 are REFUTED. The code avoids every minimal forbidden word to length 40, so
  any absent factor is longer than 40. `gap 40 107 16 0` finds the shortest.
  Record searched: `record_find.py "minimal forbidden" "longer than 40|beyond 40|length 4[1-9]"` -> no hit;
  `record_find.py "gap witness"` -> RRL's --gap only (CL041).
  RLKGP-C1 (control, certain from RR3): the code has an absent factor (a code in L would lift to R_real(107) >= 16).
  RLKGP-P1 (blind, 0.6): the shortest absent factor has length <= 50.
  RLKGP-P2 (blind, 0.5): exactly one absent factor at that shortest length.
  OUTCOME, 2026-10-10 12:22 BST (M5, about a minute): C1 PASS; P1 HELD; P2 HELD.
  - The code (61 symbols) is 1(0001)^6 then gaps 2,5,2,2,4,5,2,5,2,2,2, trail 3. Its only shortest absent factor is
    f = 0010001000100010100001010100010000101000010101 (length 46, at index 10; lead 2, gaps 4,4,4,2,5,2,2,4,5,2,5,
    2,2, trail 0). No factor of length 41 .. 45 is absent, so f is a minimal forbidden word of L.
  - Independent check (scratch script, 12:23): f[:-1] and f[1:] are present, each by an explicit right half
    simulated forward with the clamped wall; f is absent by kissat's DRAT, drat-trim -> LRAT, cake_lpr VERIFIED
    UNSAT. The same pipeline passes on the control 11.
  - The blocking word moves with K: length 17 for K = 16 (d = 75), 21 for K = 18 (d = 84; L559), 46 for K = 40
    (d = 107). Each is the K-list's first missed constraint on a relaxed record, not a census of longer words.
ADDENDUM K = 40 (registered 2026-10-10 09:15 BST, before any K = 40 run; L573). The forbidden list is now all 771 minimal
  forbidden words to length 40, extracted from SOF's exact language (rule30_sofic_test.py; mfw40.txt in the data
  folder, written from langsat2..40 by RRL's rule; its first 25 are RLK's). Each relaxed UNSAT is a certificate for
  the actual problem, so relax40 gives cheap UPPER bounds on R_real, the complement of Cloud's lower-bound test
  TR-P4. Sweeps `sweep 40 0|1 170 3600`.
  RLK40-C1 (control): relax40 <= relax18 at every depth both reach; relax40 >= the actual R_real (max over phases)
           at every decided depth.
  RLK40-P1 (blind, 0.6): relax40 equals the actual R_real at every decided depth d = 20 .. 119.
  RLK40-P2 (blind, 0.55): over d = 120 .. 170, relax40's maximum over phases exceeds 17 at some depth. If it stays at
           or below 17 there, R_real(d) <= 17 is certified at those depths, against TR-P4.
  RLK40-P3 (the unexpected check, 0.5): relax40's first excess over the actual R_real lies beyond d = 119.
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
    path = os.path.join(DIR, 'mfw%s.txt' % K)
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
        self.code = vis                                               # the visible code, for `gap`
        self.left0 = {i: int(self.x(0, i) in m) for i in range(-T, 1)}    # time-0 left half and wall, for `lift`


def right_half_for(w, phase):
    """A right half (time-0 sites 1 .. 2k - 1 + phase) producing visible word w with the wall clamped to
    (t + phase) mod 2, or None. The witness version of in_language_phase."""
    k = len(w)
    first = phase
    last = first + 2 * k - 2
    var, nv, cl = {}, [0], []

    def x(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    for t in range(last):
        for i in range(1, last - t + 1):
            r, c, y = x(t, i + 1), x(t, i), x(t + 1, i)
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:
                wall = (t + phase) % 2
                cl += ([[-y, -o], [y, o]] if wall else [[-y, o], [y, -o]])
            else:
                l = x(t, i - 1)
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for s_, b in enumerate(w):
        v = x(first + 2 * s_, 1)
        cl.append([v] if b == '1' else [-v])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=DIR, delete=False) as f:
        f.write('p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        name = f.name
    try:
        p = subprocess.run([KISSAT, '-q', name], capture_output=True, text=True)
    finally:
        os.unlink(name)
    if p.returncode == 20:
        return None
    if p.returncode != 10:
        raise RuntimeError('right-half membership UNKNOWN: solver exit %d' % p.returncode)
    m = set()
    for line in p.stdout.splitlines():
        if line.startswith('v'):
            m.update(int(z) for z in line.split()[1:] if int(z) > 0)
    return {i: int(x(0, i) in m) for i in range(1, last + 2)}


def save_model(inst, d, L, ph, tag):
    """Keep a relaxed SAT model (left half, clock and visible code) so membership and the glued simulation can be
    redone without a re-solve; GPT's L581 ACK asks for the visible word even when membership fails."""
    out = os.path.join(DIR, 'model_d%d_L%d_p%d_%s.txt' % (d, L, ph, tag))
    left = ''.join(str(inst.left0[i]) for i in range(min(inst.left0), 1))
    open(out, 'w').write('d=%d L=%d phase=%d T=%d tag=%s\nleft (cells %d .. 0)=%s\nvisible=%s\n'
                         % (d, L, ph, inst.T, tag, min(inst.left0), left, inst.code))
    return out


def load_model(path):
    lines = open(path).read().splitlines()
    head = dict(z.split('=') for z in lines[0].split())
    m = re.match(r'left \(cells (-?\d+) \.\. 0\)=([01]+)$', lines[1])
    left0 = {int(m.group(1)) + j: int(b) for j, b in enumerate(m.group(2))}
    return int(head['d']), int(head['L']), int(head['phase']), int(head['T']), left0, lines[2].split('=', 1)[1]


def simulate_glued(left0, right0, T, phase, d, L, code):
    """Glue a left half (cells <= 0 at time 0) to a right half (sites >= 1) and run Rule 30 for T steps. True if
    column 0 follows (t + phase) mod 2 for t = 0 .. T, the band d .. d + L - 1 is white at time 0, and column 1
    reads `code` at the wall's white times."""
    lo, hi = min(left0) - T - 2, max(right0) + T + 2
    row = {i: 0 for i in range(lo, hi + 1)}
    row.update(left0)
    row.update(right0)
    if any(row[-j] for j in range(d, d + L)):
        return False, 'band not white'
    vis = []
    for t in range(T + 1):
        if row[0] != (t + phase) % 2:
            return False, 'clock fails at t=%d' % t
        if (t + phase) % 2 == 0 and len(vis) < len(code):
            vis.append(str(row[1]))
        if t == T:
            break
        row = {i: row.get(i - 1, 0) ^ (row.get(i, 0) | row.get(i + 1, 0)) for i in range(lo, hi + 1)}
    if ''.join(vis) != code:
        return False, 'column 1 does not read the code'
    return True, 'ok'


def in_language_phase(w, phase):
    """Visible word w (column 1 at the wall's white times) from some right half, the wall clamped to (t + phase) mod 2.
    phase 0 is in_language's white start; phase 1 starts one step after a black wall (visible from t = 1)."""
    k = len(w)
    first = phase
    last = first + 2 * k - 2
    var, nv, cl = {}, [0], []

    def x(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    for t in range(last):
        for i in range(1, last - t + 1):
            r, c, y = x(t, i + 1), x(t, i), x(t + 1, i)
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:
                wall = (t + phase) % 2
                cl += ([[-y, -o], [y, o]] if wall else [[-y, o], [y, -o]])
            else:
                l = x(t, i - 1)
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for s_, b in enumerate(w):
        v = x(first + 2 * s_, 1)
        cl.append([v] if b == '1' else [-v])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=DIR, delete=False) as f:
        f.write('p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        name = f.name
    try:
        rc = subprocess.run([KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return rc == 10


def in_language(w):
    """RRL's in_language, on kissat: is the visible word w (white start, wall clamped) produced by some right half?
    SAT over the cone of column 1 at the last visible time (sites 1 .. 2k - 1), as rule30_cloud_relaxed_records.py."""
    k = len(w)
    last = 2 * k - 2
    var, nv, cl = {}, [0], []

    def x(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    for t in range(last):
        for i in range(1, last - t + 1):
            r, c, y = x(t, i + 1), x(t, i), x(t + 1, i)
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:                                       # left input is the wall, t mod 2
                cl += ([[-y, -o], [y, o]] if t % 2 else [[-y, o], [y, -o]])
            else:
                l = x(t, i - 1)
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for sidx, b in enumerate(w):
        cl.append([x(2 * sidx, 1)] if b == '1' else [-x(2 * sidx, 1)])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=DIR, delete=False) as f:
        f.write('p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        name = f.name
    try:
        rc = subprocess.run([KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return rc == 10


def ck_path(K, phase):
    return os.path.join(DIR, 'rlk_K%s_p%d.ck' % (K, phase))


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
                print('K=%s phase %d d=%d L=%d %s %.0f s' % (K, phase, d, L, v, time.time() - t0), flush=True)
            if v != 'SAT':
                break
            L += 1
        prev = L - 1
        if v == 'UNKNOWN':
            print('K=%s phase %d d=%d: lower bound %d (capped)' % (K, phase, d, prev), flush=True)


def records(K, phase):
    """{d: (value, exact)} with the plateau floor carried from depth to depth, as the sweep uses it."""
    out, prev = {}, None
    got = read_ck(K, phase)
    for d in sorted(got):
        if prev is not None and d != prev[0] + 1:
            break
        floor = max(prev[1] - 1, 0) if prev else 0
        sat = max([floor] + [L for L, v, _ in got[d] if v == 'SAT'])
        exact = any(L == sat + 1 and v == 'UNSAT' for L, v, _ in got[d])
        out[d] = (sat, exact)
        prev = (d, sat)
    return out


# The actual R_real (maximum over phases): RR2's exact values d = 20 .. 97 (rule30_records_real_sweep.py OUTCOME) and
# RR3's decided ones (rule30_cloud_rr3.py checkpoints, mirrored in CLOUD-LOCAL; 112 by the plateau law with 113).
ACTUAL = dict(zip(range(20, 98), [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 8, 8, 8, 8, 7, 7, 8, 8, 9, 9, 8, 9, 9, 8, 9, 11,
                                  10, 11, 11, 10, 9, 11, 10, 10, 11, 12, 11, 10, 10, 9, 9, 12, 11, 12, 11, 10, 14, 13, 12,
                                  11, 12, 11, 10, 10, 10, 10, 10, 11, 10, 10, 12, 11, 14, 13, 12, 13, 16, 15, 14, 13, 12,
                                  12, 16, 17, 16, 15, 14]))
ACTUAL.update({97: 14, 98: 14, 99: 13, 100: 15, 101: 15, 102: 14, 103: 14, 104: 13, 105: 13, 106: 12, 107: 14,
               108: 16, 109: 15, 110: 14, 111: 15, 112: 15, 113: 14, 114: 13})


def status(K):
    rows = {}
    for ph in (0, 1):
        for d, rec in records(K, ph).items():
            rows.setdefault(d, {})[ph] = rec
    for d in sorted(rows):
        r = rows[d]
        cells = ['%2d%s' % (r[ph][0], '' if r[ph][1] else '+') if ph in r else ' -' for ph in (0, 1)]
        best = max(r[ph][0] for ph in r)
        act = ACTUAL.get(d)
        print('d=%3d  phase0 %s  phase1 %s  max %2d  actual %s%s' % (
            d, cells[0], cells[1], best, '%2d' % act if act is not None else ' ?',
            '  GAP %+d' % (best - act) if act is not None and best != act else ''))


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
    elif cmd == 'gap':                                       # gap witness, as RRL's --gap (GC549.26)
        K, d, L, ph = (int(z) for z in sys.argv[2:6])
        forb = load_forbidden(K)
        inst = Relaxed(d, L, ph, forb)
        assert inst.solve(7200, forb) == 'SAT'
        lang16 = language(16)                                      # control: the SAT membership agrees with C
        assert all(not in_language(w) for w in forb[:10]) and all(in_language(w) for w in sorted(lang16[12])[:20])
        code = inst.code
        print('gap witness K=%d phase %d d=%d L=%d horizon T=%d visible code %s' % (K, ph, d, L, inst.T, code))
        for k in range(K + 1, len(code) + 1):
            absent = sorted({code[i:i + k] for i in range(len(code) - k + 1) if not in_language(code[i:i + k])})
            if absent:
                print('shortest absent factor length %d: %s' % (k, absent))
                break
        else:
            print('no absent factor: the visible code is in the actual language')
    elif cmd == 'lift':                                      # L581: relaxed model + actual right half = real witness
        if sys.argv[2].endswith('.txt'):                       # `lift MODEL.txt`: a saved model, no re-solve
            d, L, ph, T, left0, code = load_model(sys.argv[2])
            print('lift d=%d L=%d phase %d: model %s' % (d, L, ph, sys.argv[2]), flush=True)
        else:
            tag, d, L, ph = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
            cap = int(sys.argv[6]) if len(sys.argv) > 6 else 5400
            forb = load_forbidden(tag)
            inst = Relaxed(d, L, ph, forb)
            t0 = time.time()
            v = inst.solve(cap, forb)
            print('lift d=%d L=%d phase %d (%s): relaxed %s %.0f s' % (d, L, ph, tag, v, time.time() - t0), flush=True)
            if v != 'SAT':
                raise SystemExit(0)
            T, left0, code = inst.T, inst.left0, inst.code
            print('model saved: %s' % save_model(inst, d, L, ph, tag), flush=True)
        print('visible code (%d): %s' % (len(code), code), flush=True)
        right = right_half_for(code, ph)
        print('exact membership of the code (phase %d): %s' % (ph, 'IN' if right else 'ABSENT'), flush=True)
        if right:
            ok, why = simulate_glued(left0, right, T, ph, d, L, code)
            print('glued configuration simulated: %s (%s)' % ('VALID' if ok else 'INVALID', why), flush=True)
            if ok:
                out = os.path.join(DIR, 'lift_d%d_L%d_p%d.txt' % (d, L, ph))
                left = ''.join(str(left0[i]) for i in range(min(left0), 1))
                rgt = ''.join(str(right[i]) for i in range(1, max(right) + 1))
                open(out, 'w').write('d=%d L=%d phase=%d T=%d\nleft (cells %d .. 0)=%s\nright (sites 1 .. %d)=%s\n'
                                     'visible=%s\n' % (d, L, ph, T, min(left0), left, max(right), rgt, code))
                print('WITNESS: R_real(%d) >= %d; saved %s' % (d, L, out), flush=True)
    elif cmd == 'probe':                                     # one relaxed call per (depth, phase), for TR's depths
        tag, L = sys.argv[2], int(sys.argv[3])
        tag1 = sys.argv[4]                                     # the phase-1 list's tag (L1 c L, so tag is valid too)
        items = []                                             # "d" (both phases) or "d:phase"
        for z in sys.argv[5].split(','):
            items += [(int(z.split(':')[0]), int(z.split(':')[1]))] if ':' in z else [(int(z), 0), (int(z), 1)]
        cap = int(sys.argv[6]) if len(sys.argv) > 6 else 3600
        forb = {0: load_forbidden(tag), 1: load_forbidden(tag1)}
        done = set()                                           # skip (d, L, phase, list) already decided
        pck = os.path.join(DIR, 'rlk_probe.ck')
        if os.path.exists(pck):
            for line in open(pck):
                f = line.split()
                if line.endswith('\n') and len(f) == 9 and f[8] == 'END' and f[5] in ('SAT', 'UNSAT'):
                    done.add((int(f[2]), int(f[3]), int(f[4]), f[0] if f[4] == '0' else f[1]))
        for d, ph in items:
            if (d, L, ph, tag if ph == 0 else tag1) in done:
                print('probe d=%d L=%d phase %d: already decided, skipped' % (d, L, ph), flush=True)
                continue
            if True:
                t0 = time.time()
                inst = Relaxed(d, L, ph, forb[ph])
                v = inst.solve(cap, forb[ph])
                if v == 'SAT':                                 # keep the model for `lift MODEL.txt`
                    save_model(inst, d, L, ph, tag if ph == 0 else tag1)
                with open(os.path.join(DIR, 'rlk_probe.ck'), 'a') as f:
                    f.write('%s %s %d %d %d %s %.1f %s END\n' % (tag, tag1, d, L, ph, v, time.time() - t0,
                                                                 time.strftime('%H:%M')))
                print('probe d=%d L=%d phase %d (%s/%s) %s %.0f s' % (d, L, ph, tag, tag1, v, time.time() - t0),
                      flush=True)
    elif cmd == 'sweep':
        K, ph = (int(sys.argv[2]) if sys.argv[2].isdigit() else sys.argv[2]), int(sys.argv[3])
        dmax = int(sys.argv[4]) if len(sys.argv) > 4 else 120
        cap = int(sys.argv[5]) if len(sys.argv) > 5 else 3600
        sweep(K, ph, dmax, cap)
    else:
        status((int(sys.argv[2]) if sys.argv[2].isdigit() else sys.argv[2]) if len(sys.argv) > 2 else 16)


if __name__ == '__main__':
    main()
