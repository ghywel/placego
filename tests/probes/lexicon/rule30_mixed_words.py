#!/usr/bin/env python3
"""rule30_mixed_words.py: membership of the mixed-recurrence generators' visible words in L and L1 (CL297) (MW).

RUN-ON:     cpu (Python 3; kissat with models; drat-trim and cake_lpr through rule30_mfw_certify.certify)
COMMAND:    python3 tests/probes/lexicon/rule30_mixed_words.py [NAME ...]      (default: all ten words, short first)

Why (CL297, the owner's room switch this morning). Every object of the mixed recurrence (GC1097 .. GC1118) is built from
two closed walks whose column-1 words are known bit for bit; tests/probes/lexicon/rule30_mixed_generator_words.txt holds
ten phase-0 visible words: M1, M2, M3 (16, 19, 22), the bridge E (76), FE and EF (117), FEFE, EFEF, FEEF, EFFE (234).
Present: an actual right half beside the wall repeats them, and the question moves to the left side. Absent: certified
cuts close GPT's typed regime.

How, per word and phase (L: phase 0; L1: phase 1, the same visible bits read at the odd times):
  1. Containment: does the word contain a certified absent word (mfw40, cuts40_p0, cuts40_sl, the two M2C cuts; and
     for phase 1 also mfw40p1, cuts40_p1)? Every list word is cake_lpr-verified (MFC, M2C).
  2. Cone SAT with a model: the same encoding as rule30_mfw_certify.cnf, built here with its variable map. SAT: the
     right half at time 0 (sites 1 .. 2k - 1 + phase) is read from the model and re-simulated by a plain loop against
     the clamped wall (column 0 = (t + phase) mod 2); column 1 at times phase + 2s must spell the word. The witness
     goes to mw_witnesses.txt as "MW name phase RIGHT".
  3. UNSAT: rule30_mfw_certify.certify gives the cake_lpr receipt; then the least n with an absent factor of length n
     inside the word (monotone in n) by binary search, and every absent factor of that length, each certified.
Receipts in mw.ck (np-scratch).

PREDICTIONS, registered 2026-10-11 08:02 BST before the run (Cloud's, in CL297: M1 .. M3 present 0.9 each; FE, EF present 0.4
each; the 234-words present 0.3):
  MW0 (control, must hold): the known-absent 11 is VERIFIED-UNSAT and 1001 is SAT with a valid re-simulated witness.
  MW1 (blind, 0.95): M1, M2, M3 are present in both phases.
  MW2 (blind, 0.55): E is present in phase 0.
  MW3 (blind, 0.4): FE and EF are both present in phase 0.
  MW4 (blind, 0.25): at least one 234-word is present in phase 0.
  MW5 (blind, 0.6): every word absent in phase 0 is absent because it contains an already-certified cut, or a new
      minimal cut of length <= 120.
  Record searched: 'mixed_generator_words' -> PERIOD-TWO.md (CL297's board row) only; '\bFEFE\b' -> CL297 only.
REFUTED-BY: MW0 failing (the instrument); MW1 .. MW5 as stated.

OUTCOME, 2026-10-11 09:55 BST (first pass 08:02 .. 08:18, stopped by a temp-file collision with CC on MFC's fixed
mfc_tmp name, caught by this probe's assert, no receipt from the overlap kept; MFC fixed at 0e4f5747; full rerun 08:20 ..
09:55). Every verdict SAT with a re-simulated witness, or VERIFIED-UNSAT by cake_lpr:
  MW0 PASS.
  M1, M2, M3: PRESENT in both phases (witnesses in mw_witnesses.txt).
  E: ABSENT in both phases. Shortest absent factor: phase 0 length 69 (SLC2 round-8 cut), phase 1 length 68
      (10000100001001001000010000100100100100001000010010010010000100001001, a phase-1-only cut).
  FE, EF: ABSENT in both phases; shortest absent factors 54 and 61 (SLC cuts) in each phase.
  FEFE, EFEF, FEEF, EFFE: ABSENT in both phases; shortest absent factor 54 in each.
  MW1 HELD. MW2 REFUTED (E absent). MW3 REFUTED. MW4 REFUTED. MW5 HELD (every absence is an already-certified cut of
      length <= 69, or in phase 1 the new 68-bit one). Posted as L630 (phase 0), L632 (phase 1's 68). (recorded 09:55)
"""
import os
import re
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_mfw_certify as mfc                               # noqa: E402  (certify, DIR, KISSAT)
sys.argv = _argv

WORDS = os.path.join(HERE, 'rule30_mixed_generator_words.txt')
CK = os.path.join(mfc.DIR, 'mw.ck')
WIT = os.path.join(mfc.DIR, 'mw_witnesses.txt')
S, L = '001', '00001'
M2C_CUTS = [(L + L + S + S + S) * 6, (S + S + S + L + L) * 6 + S]   # L627, L628: absent in both phases


def words():
    text = open(WORDS).read()
    out = []
    for m in re.finditer(r'^(\w+) \S+ \d+ (\d+)\n((?:[01]+\n?)+)', text, re.M):
        w = m.group(3).replace('\n', '')
        assert len(w) == int(m.group(2)), m.group(1)
        out.append((m.group(1), w))
    return out


def certified(phase):
    lists = ['mfw40', 'cuts40_p0', 'cuts40_sl'] + (['mfw40p1', 'cuts40_p1'] if phase == 1 else [])
    ws = set(M2C_CUTS)
    for n in lists:
        for line in open(os.path.join(mfc.DIR, n + '.txt')):
            if line.strip():
                ws.add(line.split()[0])
    return ws


def cnf_with_map(w, phase):
    k = len(w)
    last = phase + 2 * k - 2
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
    for s, b in enumerate(w):
        v = x(phase + 2 * s, 1)
        cl.append([v] if b == '1' else [-v])
    text = 'p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)
    return text, var, last


def solve_model(w, phase):
    text, var, last = cnf_with_map(w, phase)
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=mfc.DIR, delete=False) as f:
        f.write(text)
        name = f.name
    try:
        p = subprocess.run([mfc.KISSAT, '-q', name], capture_output=True, text=True)
    finally:
        os.unlink(name)
    if p.returncode == 20:
        return None
    assert p.returncode == 10, p.returncode
    vals = set()
    for line in p.stdout.split('\n'):
        if line.startswith('v '):
            vals.update(int(t) for t in line.split()[1:] if int(t) > 0)
    return ''.join('1' if var[(0, i)] in vals else '0' for i in range(1, last + 2) if (0, i) in var)


def resimulate(right, phase, w):
    """Plain loop: the right half against the clamped wall; column 1 at times phase + 2s must spell w."""
    row = [int(b) for b in right] + [0] * 4
    seen = []
    last = phase + 2 * len(w) - 2
    for t in range(last + 1):
        if t >= phase and (t - phase) % 2 == 0 and len(seen) < len(w):
            seen.append(str(row[0]))
        wall = (t + phase) % 2
        row = [(wall if i == 0 else row[i - 1]) ^ (row[i] | row[i + 1]) for i in range(len(row) - 1)] + [0]
    return ''.join(seen) == w


def receipt(name, w, ph, verdict, extra=''):
    with open(CK, 'a') as f:
        f.write('%s %d %d %s %s %s\n' % (name, ph, len(w), verdict, extra, time.strftime('%H:%M')))


def absent(w, ph):
    v = mfc.certify(w, ph)
    assert v in ('SAT', 'VERIFIED-UNSAT'), (w, ph, v)
    return v == 'VERIFIED-UNSAT'


def minimal_cuts(w, ph):
    def any_absent(n):
        return [i for i in range(len(w) - n + 1) if absent(w[i:i + n], ph)]
    lo, hi = 2, len(w)
    while lo < hi:
        mid = (lo + hi) // 2
        if any_absent(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo, sorted({w[i:i + lo] for i in any_absent(lo)})


def run(name, w, ph, cuts):
    inside = sorted({c for c in cuts if c in w}, key=len)
    if inside:
        print('  %s phase %d: contains certified cut(s) of length %s' % (name, ph, [len(c) for c in inside]), flush=True)
    t0 = time.time()
    right = solve_model(w, ph)
    if right is not None:
        ok = resimulate(right, ph, w)
        receipt(name, w, ph, 'PRESENT' if ok else 'SAT-BUT-RESIM-FAILED', right)
        if ok:
            with open(WIT, 'a') as f:
                f.write('MW %s %d %s\n' % (name, ph, right))
        print('  %s phase %d: PRESENT (%.0f s), witness re-simulated %s' % (name, ph, time.time() - t0, ok), flush=True)
        return 'present' if ok else 'error'
    v = absent(w, ph)
    receipt(name, w, ph, 'VERIFIED-UNSAT' if v else 'SAT-ON-RECHECK')
    if not v:
        print('  %s phase %d: solver disagreement' % (name, ph), flush=True)
        return 'error'
    n, mins = minimal_cuts(w, ph)
    for c in mins:
        receipt(name, c, ph, 'MINIMAL-CUT', 'len%d' % n)
    print('  %s phase %d: ABSENT, cake_lpr VERIFIED (%.0f s); shortest absent factor length %d: %s' % (
        name, ph, time.time() - t0, n, mins), flush=True)
    return 'absent'


def main():
    ok0 = absent('11', 0) and solve_model('1001', 0) is not None and resimulate(solve_model('1001', 0), 0, '1001')
    print('MW0 %s' % ('PASS' if ok0 else 'FAIL'), flush=True)
    sel = sys.argv[1:]
    ws = [(n, w) for n, w in words() if not sel or n in sel]
    ws.sort(key=lambda nw: len(nw[1]))
    res = {}
    for ph in (0, 1):
        cuts = certified(ph)
        for n, w in ws:
            res[(n, ph)] = run(n, w, ph, cuts)
    print('results: ' + ' '.join('%s/p%d=%s' % (n, ph, v) for (n, ph), v in sorted(res.items())))


if __name__ == '__main__':
    main()
