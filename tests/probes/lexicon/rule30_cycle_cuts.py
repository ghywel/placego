#!/usr/bin/env python3
"""rule30_cycle_cuts.py: certified minimal cuts of the 111 branch's periodic visible words (CL300) (CC).

RUN-ON:     cpu (Python 3; kissat, drat-trim, cake_lpr through rule30_mfw_certify.certify)
COMMAND:    python3 tests/probes/lexicon/rule30_cycle_cuts.py [NAME ...]

Why (CL300, after L630's verdict). The collar lane's other recurrent objects are the 111 diversion's: GC1105's named
M3 self-return S-D111-H-SS^3 (column-1 word h(SLLSSS), visible word M3, present by MW) and the mixed M2/M3 recurrent
component (CL284). M3 itself is present; the question is whether its repetitions, alone or mixed with M2, can occur
for ever beside the wall. M2C answered it for M2: (LLSSS)^6 (114 bits) and (SSSLL)^6 S (117 bits) exclude it.

How, as M2C, for each periodic visible word P (M3 from rule30_mixed_generator_words.txt, M2 likewise; phase-0 spelling)
and each phase: (1) the certified absent words (mfw40, cuts40_p0, cuts40_sl, M2C's two cuts, MW's minimal cuts; plus
mfw40p1, cuts40_p1 in phase 1) that occur in P repeated; (2) the least n such that some factor of length n of P's
bi-infinite repetition is absent (monotone in n), by binary search up to CAP = 300, and every absent factor of that
length that is minimal (both its length-(n - 1) factors present); each through rule30_mfw_certify.certify (cone CNF,
kissat, DRAT, drat-trim -L, cake_lpr). Receipts in cc.ck. "Present to 300" if nothing is absent up to the cap.

PREDICTIONS, registered 2026-10-11 08:18 BST before the run:
  CC0 (control, must hold): M2's periodic word returns M2C's least length 114 and the cut (LLSSS)^6 in phase 0.
  CC1 (blind, 0.6): M3's periodic word (period 22) has an absent factor of length <= 150 in phase 0.
  CC2 (blind, 0.5): every mixed word ((M2 M3), (M2 M2 M3), (M2 M3 M3), repeated) has an absent factor of length <= 150
      in phase 0.
  CC3 (blind, 0.5): at least one of the four words already contains a cut certified before today's run (a list word, an
      M2C cut or an MW cut).
  Record searched: 'SLLSSS' -> GC1105 (RULE30-GPT.md) and rule30_black_A_111_diversion.py only (no membership test).
REFUTED-BY: CC0 failing (the instrument); CC1 .. CC3 as stated.

PREDICTIONS, registered 2026-10-11 08:26 BST before their run (CL301 adds five cycles; periods 35, 57, 79, 101, 92):
  CC4 (blind, 0.5): the (1,2) word, M1 M2 repeated (period 35), has an absent factor of length <= 300 in phase 0.
  CC5 (blind, 0.4): all five CL301 words have an absent factor of length <= 300 in phase 0 (with CC1, the 111 branch
      of GC1105 would then be cut everywhere).
  CC6 (blind, 0.6): none of the five contains one of the 54-, 61-, 65- or 69-bit SLC cuts (CL301 says none contains
      two consecutive M2, and those cuts came from the M2-rich walks).

PREDICTIONS, registered 2026-10-11 09:28 BST before their run (CL305: N's periodic word and N-with-M3 splices; periods
29, 51, 73, 95):
  CC7 (blind, 0.5): N repeated (period 29) has an absent factor of length <= 300 in phase 0.
  CC8 (blind, 0.6): each N-with-M3 splice repeated has an absent factor of length <= 300 in phase 0.
  CC9 (blind, 0.4): at least one of the four already contains a certified cut (list, M2C, or MW), before any search.

FAST note (2026-10-11 10:50 BST, before its use): the certified search was too slow for pure M3 under load (certify
writes a DRAT proof even for present words; about 5 minutes a length-189 window). `fast NAME PHASE LO HI [WORKERS]`
keeps the method and the cone CNF but decides membership during the search with kissat alone (no proof), three
rotations at a time, ending a step at its first absent rotation. It starts from bounds already certified in cc.ck
(pure M3, phase 0: every length-151 factor SAT, so LO = 152; 22 of 22 length-226 factors VERIFIED-UNSAT, so HI = 226).
Every minimal cut it reports is then certified by cake_lpr, and length n - 1 is checked to have no absent factor.
  CC10 (blind, 0.5): pure M3's least absent length is <= 189 in phase 0.
"""
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_mfw_certify as mfc                               # noqa: E402  (certify, DIR)
import rule30_mixed_words as mw                                # noqa: E402  (words, M2C_CUTS)
sys.argv = _argv

CK = os.path.join(mfc.DIR, 'cc.ck')
CAP = 300
G = dict(mw.words())
N29 = '100' + '10000' * 4 + '100' * 2                         # GC1126's N; N29 + '1' is its completed 30-bit word
assert N29 + '1' == '100100001000010000100001001001'
CYCLES = [('M2', G['M2']), ('M3', G['M3']), ('M2M3', G['M2'] + G['M3']), ('M2M2M3', G['M2'] * 2 + G['M3']),
          ('M2M3M3', G['M2'] + G['M3'] * 2),
          # CL301: the cycles of the width-28 component's 97 states (k-words (1,2), (1,2,3), (1,2,3,3), (1,2,3,3,3), (1,2,1,2,3))
          ('M1M2', G['M1'] + G['M2']), ('M1M2M3', G['M1'] + G['M2'] + G['M3']),
          ('M1M2M3M3', G['M1'] + G['M2'] + G['M3'] * 2), ('M1M2M3M3M3', G['M1'] + G['M2'] + G['M3'] * 3),
          ('M1M2M1M2M3', (G['M1'] + G['M2']) * 2 + G['M3']),
          # CL305: GC1126's macro N = S L L L L S S (29 bits; GPT's 30-bit word is N followed by the next macro's marker)
          ('N', N29), ('NM3', N29 + G['M3']), ('NM3M3', N29 + G['M3'] * 2), ('NM3M3M3', N29 + G['M3'] * 3)]


def fac(c, r, n):
    return (c * (n // len(c) + 3))[r:r + n]


def absent(w, ph, tag):
    t0 = time.time()
    v = mfc.certify(w, ph)
    with open(CK, 'a') as f:
        f.write('%s %d %d %s %s %.1f\n' % (tag, ph, len(w), w, v, time.time() - t0))
    assert v in ('SAT', 'VERIFIED-UNSAT'), (tag, w, ph, v)
    return v == 'VERIFIED-UNSAT'


def absent_rot(c, n, ph, tag):
    return {r for r in range(len(c)) if absent(fac(c, r, n), ph, tag)}


def run(name, c, ph):
    cuts = mw.certified(ph)
    rep = c * (300 // len(c) + 3)
    inside = sorted({len(x) for x in cuts if x in rep})
    print('%s phase %d: period %d; certified cuts inside its repetition: %s' % (name, ph, len(c), inside or 'none'),
          flush=True)
    if not absent_rot(c, CAP, ph, name):
        print('%s phase %d: PRESENT to %d (every factor of length %d is in the language)' % (name, ph, CAP, CAP), flush=True)
        return None
    lo, hi = 2, CAP
    while lo < hi:
        mid = (lo + hi) // 2
        if absent_rot(c, mid, ph, name):
            hi = mid
        else:
            lo = mid + 1
    a, b = absent_rot(c, lo, ph, name), absent_rot(c, lo - 1, ph, name)
    mins = sorted({fac(c, r, lo) for r in a if r not in b and (r + 1) % len(c) not in b})
    print('%s phase %d: least absent length %d; minimal cuts (cake_lpr VERIFIED): %s' % (name, ph, lo, mins), flush=True)
    return lo, mins


def member(args):
    """Fast membership for the search only: the same cone CNF as rule30_mfw_certify.cnf, kissat without a proof.
    Returns (r, present). Minimal cuts found this way are certified afterwards by mfc.certify (cake_lpr)."""
    import subprocess
    import tempfile
    w, ph, r = args
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=mfc.DIR, delete=False) as f:
        f.write(mfc.cnf(w, ph))
        name = f.name
    try:
        rc = subprocess.run([mfc.KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return r, rc == 10


def absent_fast(pool, c, n, ph, tag, stop_early):
    out = set()
    for r, present in pool.imap_unordered(member, [(fac(c, r, n), ph, r) for r in range(len(c))]):
        with open(CK, 'a') as f:
            f.write('%s %d %d r%d %s fast\n' % (tag, ph, n, r, 'SAT' if present else 'UNSAT'))
        if not present:
            out.add(r)
            if stop_early:
                pool.terminate()
                return out
    return out


def fast(name, ph, lo, hi, workers):
    """FAST mode (registered 2026-10-11 10:50 BST; see the header's FAST note): binary search between certified
    bounds lo (every factor of length lo - 1 present) and hi (some factor of length hi absent), kissat without proofs,
    WORKERS rotations at a time, stopping a step at its first absent rotation; then the full absent sets at the least
    length n and at n - 1, and every minimal cut certified by mfc.certify (cake_lpr)."""
    from multiprocessing import Pool
    c = dict(CYCLES)[name]
    while lo < hi:
        mid = (lo + hi) // 2
        with Pool(workers) as pool:
            got = absent_fast(pool, c, mid, ph, name, True)
        print('  %s phase %d: length %d %s' % (name, ph, mid, 'has an absent factor' if got else 'all present'), flush=True)
        if got:
            hi = mid
        else:
            lo = mid + 1
    with Pool(workers) as pool:
        a = absent_fast(pool, c, lo, ph, name, False)
    with Pool(workers) as pool:
        b = absent_fast(pool, c, lo - 1, ph, name, False)
    mins = sorted({fac(c, r, lo) for r in a if r not in b and (r + 1) % len(c) not in b})
    assert not b, 'length %d must have no absent factor' % (lo - 1)
    cert = {m: absent(m, ph, name + '-mincut') for m in mins}
    print('%s phase %d: least absent length %d; minimal cuts: %s; cake_lpr VERIFIED: %s' % (
        name, ph, lo, mins, all(cert.values())), flush=True)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'fast':
        fast(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]) if len(sys.argv) > 6 else 3)
        return
    sel = sys.argv[1:]
    res = {}
    for ph in (0, 1):
        for name, c in CYCLES:
            if sel and name not in sel:
                continue
            res[(name, ph)] = run(name, c, ph)
    m2 = res.get(('M2', 0))
    if m2:
        ok = m2[0] == 114 and mw.M2C_CUTS[0] in m2[1]
        print('CC0 %s  (M2 phase 0: least %d; (LLSSS)^6 among the minimal cuts: %s)' % (
            'PASS' if ok else 'FAIL', m2[0], mw.M2C_CUTS[0] in m2[1]))
    print('results: ' + ' '.join('%s/p%d=%s' % (n, ph, 'present>%d' % CAP if v is None else v[0])
                                 for (n, ph), v in sorted(res.items())))


if __name__ == '__main__':
    main()
