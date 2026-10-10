#!/usr/bin/env python3
"""rule30_mfw_certify.py: MFC, every forbidden word behind relax40, CUT and SLC checked absent by cake_lpr.

RUN-ON:     cpu (Python 3, kissat 4.0.4, drat-trim, ~/np-build/cake_lpr/cake_lpr: the lockf wrapper, one check at a
            time); one core, about a second a word
COMMAND:    python3 tests/probes/lexicon/rule30_mfw_certify.py [LIST ...]   (default: mfw40 mfw40p1 cuts40_p0 cuts40_p1
            cuts40_sl; a LIST is a file stem in the RLK scratch, NP_SCRATCH_RLK)
DATA:       the lists in the RLK scratch; receipts appended to mfc.ck there, one line a word:
            `LIST WORD PHASE VERIFIED-UNSAT|FAILED-<stage> SECONDS END`; words already VERIFIED are skipped

Why (Cloud's CL184, condition 1). A relaxed UNSAT certifies an actual upper bound only if every forbidden word it
uses is truly absent. The 771 + 832 minimal forbidden words to length 40 came from SAT-grown languages (kissat
verdicts), and CUT's and SLC's cuts from kissat membership calls. This re-checks each word's absence with a formally
verified checker: the word's cone CNF (right_half_for's encoding: time-0 sites 1 .. 2k - 1 + phase, the wall clamped
to (t + phase) mod 2, column 1 fixed at the visible times), kissat with a DRAT proof, drat-trim -L to LRAT (untrusted
elaboration), cake_lpr on the CNF and LRAT. Phase: mfw40, cuts40_p0 and cuts40_sl words are absent from L (phase 0;
then from L1 too, L1 c L); mfw40p1 and cuts40_p1 words are checked in phase 1.
The trust that remains is the encoding, shared with right_half_for, whose SAT side is simulation-checked in every
lift and whose UNSAT side GPT reviewed (eeb45660).

Record searched: `record_find.py cake_lpr forbidden` -> VC (rule30_verified_certs.py: records' certificates, not
list words) and L584 (one word, f); no list-wide check on record.

PREDICTIONS (Local's, pushed before any run of this script):
  MFC-C1 (control): the known-forbidden 11 (phase 0) and L584's f verify; the present words 1 and f[:-1] are SAT
         (no proof), and are reported as such, not as failures.
  MFC-P1 (blind, 0.9): every word of mfw40 and mfw40p1 verifies.
  MFC-P2 (blind, 0.9): every CUT and SLC cut verifies.
OUTCOME, 2026-10-10 13:01 BST (M5, one core, about 4 minutes in all; mfc.ck): C1 PASS; P1 HELD; P2 HELD so far.
  - mfw40: 771 of 771 VERIFIED-UNSAT. mfw40p1: 832 of 832. cuts40_p0 (L584's f): 1 of 1. cuts40_sl (SLC and SLC2
    round 7): 39 of 39. cuts40_p1: none yet.
  - So every forbidden word behind relax40, CUT and SLC to this time is formally absent. Re-run after new cuts; it
    skips verified words.
"""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_relaxed_records_k as rlk                         # noqa: E402  (DIR, KISSAT)
sys.argv = _argv
DIR = rlk.DIR
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')
KISSAT = os.environ.get('KISSAT', 'kissat')
PHASE = {'mfw40': 0, 'mfw40p1': 1, 'cuts40_p0': 0, 'cuts40_p1': 1, 'cuts40_sl': 0}


def cnf(w, phase):
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
    return 'p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)


def certify(w, phase):
    base = os.path.join(DIR, 'mfc_tmp')
    open(base + '.cnf', 'w').write(cnf(w, phase))
    try:
        k = subprocess.run([KISSAT, '-q', '-f', '--no-binary', base + '.cnf', base + '.drat'], capture_output=True)
        if k.returncode == 10:
            return 'SAT'
        if k.returncode != 20:
            return 'FAILED-kissat%d' % k.returncode
        d = subprocess.run(['drat-trim', base + '.cnf', base + '.drat', '-L', base + '.lrat'], capture_output=True,
                           text=True)
        if 's VERIFIED' not in [z.strip() for z in d.stdout.splitlines()]:
            return 'FAILED-drat-trim'
        c = subprocess.run([CAKE, '--CML_HEAP_SIZE=1000', '--CML_STACK_SIZE=500', base + '.cnf', base + '.lrat'],
                           capture_output=True, text=True)
        return 'VERIFIED-UNSAT' if 's VERIFIED UNSAT' in c.stdout else 'FAILED-cake'
    finally:
        for e in ('.cnf', '.drat', '.lrat'):
            if os.path.exists(base + e):
                os.unlink(base + e)


def main():
    stems = sys.argv[1:] or ['mfw40', 'mfw40p1', 'cuts40_p0', 'cuts40_p1', 'cuts40_sl']
    ck = os.path.join(DIR, 'mfc.ck')
    done = set()
    if os.path.exists(ck):
        for line in open(ck):
            f = line.split()
            if len(f) == 6 and f[5] == 'END' and f[3] == 'VERIFIED-UNSAT':
                done.add((f[0], f[1]))
    f46 = '0010001000100010100001010100010000101000010101'
    ctl = [certify('11', 0), certify(f46, 0), certify('1', 0), certify(f46[:-1], 0)]
    c1 = ctl == ['VERIFIED-UNSAT', 'VERIFIED-UNSAT', 'SAT', 'SAT']
    print('MFC-C1', 'PASS' if c1 else 'FAIL', ctl, flush=True)
    if not c1:
        raise SystemExit(1)
    for stem in stems:
        path = os.path.join(DIR, stem + '.txt')
        if not os.path.exists(path):
            print('%s: no file, skipped' % stem, flush=True)
            continue
        words = [line.split()[0] for line in open(path) if line.strip()]
        ok = bad = 0
        for w in words:
            if (stem, w) in done:
                ok += 1
                continue
            t0 = time.time()
            v = certify(w, PHASE[stem])
            with open(ck, 'a') as f:
                f.write('%s %s %d %s %.1f END\n' % (stem, w, PHASE[stem], v, time.time() - t0))
            if v == 'VERIFIED-UNSAT':
                ok += 1
            else:
                bad += 1
                print('  %s %s: %s' % (stem, w, v), flush=True)
        print('%s: %d words, %d VERIFIED-UNSAT, %d not' % (stem, len(words), ok, bad), flush=True)


if __name__ == '__main__':
    main()
