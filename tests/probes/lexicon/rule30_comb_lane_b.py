#!/usr/bin/env python3
"""rule30_comb_lane_b.py: the record comb, lane B (CLAUDE-INTEL-HANDOVER.md section 7): the stored SAT certificates
behind RECORD-MAP.md's COMPUTED lines, re-checked on the M5 where they are kept (Local, at the owner's word, 2026-10-14
17:38 BST: "'Lane B' the stored proofs are your machine to tackle"; RULE30-PRIZE.md 8.106).

RUN-ON:     cpu, M5; drat-trim (rebuilt 2026-10-14 at 2e3b2dc on the owner's word, L728), cadical, and
            ~/np-build/cake_lpr/cake_lpr (the lockf wrapper: one check at a time). Reads the stored files under
            ~/np-scratch-int and writes only under ~/np-scratch-int/rule30-comb-b.
COMMAND:    python3 tests/probes/lexicon/rule30_comb_lane_b.py stored    (B1, B3: stored proofs, CNF hashes, controls)
            python3 tests/probes/lexicon/rule30_comb_lane_b.py cross12   (U: entry 27 through a second solver)
            B2 (the regenerations) runs the committed probes in a sandbox: a scratch clone, with HOME and the probes'
            NP_SCRATCH_* variables pointed under rule30-comb-b, so no receipt in the record's data is touched. Each
            command is recorded with its outcome.

Record searched (record_find, 2026-10-14 17:53 BST): 'record comb' -> 10 hits (8.104, the brief, CL374); 'lane B' -> 8
hits (the brief; no lane-B result); 'cross-solver|second solver' -> 2 hits (GC775; rule30_cadical_certify.py's note
that CaDiCaL is used as a second solver); 'cert_d132_L18_p1_40p1' -> 1 hit (INSTINCT-LOCAL.md S8 only); 'rr3 106|106,
108' -> 0 hits.

THE INVENTORY (a read-only sub-agent's listing, re-checked where it matters; a self-check, not a second read).
- Stored proofs: 42 LRAT with their CNFs (the four mfw controls and cuts in rule30-rlk, TWC's 38 trace words) and 170
  DRAT proofs of UNSAT claims with their CNFs (TWC 38; rule30-al 106: cx 80, cxe 20, ALC 4, ASF 1, ALF 1; NL 22; the
  four mfw). 76 more TWC pairs are leftovers of SAT runs and claim nothing.
- Most certificates were checked when made and their proofs deleted (LRAT up to 49 GB). For those the record keeps a
  receipt (a .ck line or a docstring with the CNF's SHA-256), and some CNFs are kept.
- Two large proofs back no claim: cert_d132_L18_p1_40p1.drat (6.8 GiB, complete; its drat-trim -L conversion was
  stopped by the halt of 2026-10-11, and 132 phase 1 rests on K3's CaDiCaL certificate instead) and rr3-112-16.drat
  (9.7 GiB, truncated by the same halt).

Observed while planning, so not predictions:
- VC3 (rule30_verified_certs.py's rr3 tier) has 16 cake_lpr receipts in rule30-vc/vc.ck (98 .. 111, 113, 114), but
  RECORD-MAP.md lists 10 (98 .. 105, 107, 109), and the probe has no VC3 OUTCOME. The halt row (CLOUD-LOCAL.md,
  2026-10-11 18:03) records "VC3 (16 of 23 done)" without naming them. A derived-layer lag, to be corrected in place.
- INSTINCT-LOCAL.md S8 is explained by the inventory above.

PREDICTIONS (written 2026-10-14 17:59 BST, before any check of this lane).
  B1 (stored proofs, checked as stored)
  P1 (0.9): all 42 stored LRAT proofs are "s VERIFIED UNSAT" under cake_lpr against their CNFs.
  P2 (0.85): all 170 stored DRAT proofs of UNSAT claims are "s VERIFIED" under drat-trim against their CNFs. That
     includes cx-q155-4-1 and cx-q310-4-1, whose LRAT conversion drat-trim rejected (a converter limit, VC's note):
     plain checking is a different path. Four cx proofs carry no explicit empty clause (those two and q155-0-2,
     q310-0-2); they pass only if unit propagation refutes the formula with their lemmas.
  P3 (0.9): every stored certificate CNF for a record bound at d >= 107 (cert_*, cad_cert_*, exact_*) has its
     SHA-256 prefix in a receipt or a docstring, so the kept file is the certified one.
  C1 (control, must hold): a stored TWC refutation checked against a satisfiable TWC CNF is "s NOT VERIFIED".
  C2 (control, must hold): a stored TWC LRAT with one hint removed from its first addition step is rejected by cake_lpr.
  B2 (regenerated within the brief's 15-minute cap, in the sandbox)
  P4 (0.8): each regeneration returns its recorded verdict: DT (entry 27, 112/112), KX, the first 15 minutes of KT2C
     (every finished case VERIFIED), MW's 69-bit cut, M2C's 114-bit cut, the 178-bit pure-M3 cut, K12/K15's 50- and
     70-bit cuts, SWP's cut-45 pins, RLK's CUT certificate at d = 107, a seeded sample of the MFC words, and
     sl_cuts' replay. At most two items fail to run for reasons of environment (a default path moved since), and
     none returns a contrary verdict.
  P5 (0.85): VC's `status rr3` rebuilds the 16 received rr3 CNFs to their recorded hashes.
  B3 (beyond the cap): listed, not re-solved: the 33 record-bound certificates at d >= 121 (20 minutes to 6.7 hours
     each), VC3's deep rr3 calls, KT2N/KT2M's SAT runs, CUT44, and KS (python-sat is not installed).
  U, the unexpected check (0.85): entry 27's 112 class-12 instances (class 12 dead after 140 steps), rebuilt from KK's
     committed encoder, are UNSAT under CaDiCaL, and its LRAT is VERIFIED by cake_lpr: a second solver and a verified
     checker, where the record used kissat and drat-trim. Control U-C: class 32 at N = 168, t0 = 0, d = 0 is SAT.
  Counterfactual: a stored proof that fails where its receipt says VERIFIED means the file changed after its check
  (then its hash differs from the receipt) or the checker build differs; a regeneration with a contrary verdict is a
  record error, corrected in place with both lines quoted.
"""
import glob
import hashlib
import os
import random
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))     # tests/probes/lexicon -> the repo root
SCR = os.path.expanduser('~/np-scratch-int')
EXT = os.path.join(SCR, 'extnvme-2026-10-12')
OUT = os.path.join(SCR, 'rule30-comb-b')
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')
CAP = 900                                                   # the brief's 15-minute cap, per check


def verdict_lines(text):
    return [l.strip() for l in text.replace('\r', '\n').splitlines()]   # drat-trim's verdict follows a carriage return


def drat_check(cnf, prf):
    try:
        r = subprocess.run(['drat-trim', cnf, prf, '-t', str(CAP)], capture_output=True, text=True, timeout=CAP + 60)
    except subprocess.TimeoutExpired:
        return 'TIMEOUT'
    v = verdict_lines(r.stdout)
    return 'VERIFIED' if 's VERIFIED' in v else ('NOT-VERIFIED' if 's NOT VERIFIED' in v else 'ERROR')


def cake_check(cnf, lrat):
    try:
        r = subprocess.run([CAKE, '--CML_HEAP_SIZE=6000', '--CML_STACK_SIZE=2000', cnf, lrat], capture_output=True,
                           text=True, timeout=CAP + 60)
    except subprocess.TimeoutExpired:
        return 'TIMEOUT'
    return 'VERIFIED' if 's VERIFIED UNSAT' in r.stdout else 'REJECTED'


def claims_refutation(prf):
    with open(prf, 'rb') as f:
        f.seek(max(0, os.path.getsize(prf) - 65536))
        t = f.read()
    return b'\n0\n' in t or t.startswith(b'0\n')


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def stored_sets():
    """(family, cnf, proof) for every stored proof of an UNSAT claim, as the inventory lists them."""
    out = []
    twc = os.path.join(SCR, 'rule30-twc')
    for l in sorted(glob.glob(os.path.join(twc, '*.lrat'))):
        out.append(('TWC', l[:-5] + '.cnf', l[:-5] + '.drat', l))
    rlk = os.path.join(SCR, 'rule30-rlk')
    for s in ('mfw2', 'mfw42', 'mfw46', 'mfw81'):
        b = os.path.join(rlk, s)
        out.append(('MFW', b + '.cnf', b + '.drat', b + '.lrat'))
    al = os.path.join(SCR, 'rule30-al')
    for sub, fam in (('', 'AL'), ('cx-drat', 'CX'), ('cxe', 'CXE')):
        for d in sorted(glob.glob(os.path.join(al, sub, '*.drat'))):
            out.append((fam, d[:-5] + '.cnf', d, None))
    for sub in ('cert', os.path.join('cert', 'all')):
        for d in sorted(glob.glob(os.path.join(EXT, 'rule30-nl', sub, '*.drat'))):
            out.append(('NL', d[:-5] + '.cnf', d, None))
    return out


def receipt_hashes():
    """Every hex token of 16 or more characters in the receipts and the git record, cut to its first 16."""
    toks = set()
    pat = re.compile(r'\b[0-9a-f]{16,64}\b')
    files = []
    for d in ('rule30-rlk', 'rule30-twc', 'rule30-al', 'rule30-vc', 'rule30-rr', 'rule30-rr3'):
        for ext in ('ck', 'log', 'out', 'txt', 'json'):
            files += glob.glob(os.path.join(SCR, d, '**', '*.' + ext), recursive=True)
    files += glob.glob(os.path.join(EXT, '**', '*.txt'), recursive=True) + glob.glob(os.path.join(EXT, '**', '*.ck'),
                                                                                      recursive=True)
    files += glob.glob(os.path.join(REPO, 'tests', 'probes', '**', '*.py'), recursive=True)
    files += glob.glob(os.path.join(REPO, '*.md'))
    for p in files:
        try:
            if os.path.getsize(p) > 50e6:
                continue
            for m in pat.findall(open(p, errors='replace').read()):
                toks.add(m[:16])
        except OSError:
            pass
    return toks


def stored():
    os.makedirs(OUT, exist_ok=True)
    sets = stored_sets()
    missing = [s for s in sets if not os.path.exists(s[1]) or not os.path.exists(s[2])]
    print('stored sets: %d (%d with LRAT); missing files: %d' % (len(sets), sum(1 for s in sets if s[3]), len(missing)),
          flush=True)
    noclaim = [os.path.basename(s[2]) for s in sets if not claims_refutation(s[2])]
    print('DRAT proofs without an explicit empty clause: %s' % noclaim, flush=True)

    # controls first
    sat_cnfs = sorted(p for p in glob.glob(os.path.join(SCR, 'rule30-twc', '*.cnf'))
                      if not os.path.exists(p[:-4] + '.lrat'))
    twc = [s for s in sets if s[0] == 'TWC']
    c1_proof, c1_target = twc[0][2], sat_cnfs[0]
    r = subprocess.run(['cadical', '-q', '-n', c1_target], capture_output=True, text=True)
    c1 = drat_check(c1_target, c1_proof)
    print('C1 %s: proof %s against %s (cadical exit %d, 10 = SAT): %s' % (
        'PASS' if c1 == 'NOT-VERIFIED' and r.returncode == 10 else 'FAIL', os.path.basename(c1_proof),
        os.path.basename(c1_target), r.returncode, c1), flush=True)
    lines = open(twc[0][3]).read().splitlines()
    bad, done = [], False
    for line in lines:
        parts = line.split()
        if not done and len(parts) >= 4 and parts[1] != 'd':
            z = parts.index('0')
            if len(parts) > z + 2:
                parts = parts[:z + 1] + parts[z + 2:]
                done = True
        bad.append(' '.join(parts))
    badp = os.path.join(OUT, 'c2_bad.lrat')
    open(badp, 'w').write('\n'.join(bad) + '\n')
    c2 = cake_check(twc[0][1], badp)
    print('C2 %s: one hint removed from %s: cake_lpr %s' % ('PASS' if c2 == 'REJECTED' else 'FAIL',
                                                             os.path.basename(twc[0][3]), c2), flush=True)

    # P1: cake_lpr on the LRATs, one at a time
    p1 = []
    for fam, cnf, prf, lrat in sets:
        if lrat:
            p1.append((fam, os.path.basename(lrat), cake_check(cnf, lrat)))
    bad1 = [x for x in p1 if x[2] != 'VERIFIED']
    print('P1 %s: %d LRAT, %d VERIFIED UNSAT; not verified: %s' % ('HELD' if not bad1 else 'REFUTED', len(p1),
                                                                   len(p1) - len(bad1), bad1), flush=True)

    # P2: drat-trim on the DRATs, in parallel (small proofs)
    with ThreadPoolExecutor(6) as ex:
        p2 = list(ex.map(lambda s: (s[0], os.path.basename(s[2]), drat_check(s[1], s[2])), sets))
    bad2 = [x for x in p2 if x[2] != 'VERIFIED']
    byfam = {}
    for fam, name, v in p2:
        byfam.setdefault(fam, [0, 0])
        byfam[fam][0] += 1
        byfam[fam][1] += v == 'VERIFIED'
    print('P2 %s: %d DRAT, %d VERIFIED; by family %s; not verified: %s' % (
        'HELD' if not bad2 else 'REFUTED', len(p2), len(p2) - len(bad2), byfam, bad2), flush=True)

    # P3 and the hash survey
    toks = receipt_hashes()
    print('receipt tokens: %d' % len(toks), flush=True)
    certs = sorted(glob.glob(os.path.join(SCR, 'rule30-rlk', 'cert_d*.cnf')) +
                   glob.glob(os.path.join(SCR, 'rule30-rlk', 'cad_cert_d*.cnf')) +
                   glob.glob(os.path.join(SCR, 'rule30-rlk', 'exact_d*.cnf')))
    certs = [c for c in certs if int(re.search(r'_d(\d+)_', c).group(1)) >= 107]
    p3 = [(os.path.basename(c), sha(c)[:16]) for c in certs]
    unmatched = [n for n, h in p3 if h not in toks]
    print('P3 %s: %d certificate CNFs at d >= 107; hash in a receipt: %d; unmatched: %s' % (
        'HELD' if not unmatched else 'REFUTED', len(p3), len(p3) - len(unmatched), unmatched), flush=True)
    fam_hash = {}
    for fam, cnf, prf, lrat in sets:
        fam_hash.setdefault(fam, [0, 0])
        fam_hash[fam][0] += 1
        fam_hash[fam][1] += sha(cnf)[:16] in toks
    print('stored-proof CNFs with a recorded hash, by family (not scored): %s' % fam_hash, flush=True)
    with open(os.path.join(OUT, 'stored.txt'), 'w') as f:
        for x in p1:
            f.write('LRAT %s %s %s\n' % x)
        for x in p2:
            f.write('DRAT %s %s %s\n' % x)
        for n, h in p3:
            f.write('CNF %s %s %s\n' % (n, h, 'receipt' if h in toks else 'no-receipt'))


def cross12():
    sys.path.insert(0, HERE)
    _argv, sys.argv = sys.argv, sys.argv[:1]
    import rule30_kick_bite_kissat as kk
    sys.argv = _argv
    d = os.path.join(OUT, 'cross12')
    os.makedirs(d, exist_ok=True)

    def one(args):
        t0, dd, a, N = args
        tag = 'c%d_N%d_t%d_d%d' % (a, N, t0, dd)
        cnf, lrat = os.path.join(d, tag + '.cnf'), os.path.join(d, tag + '.lrat')
        nv, clauses, row, s, E = kk.instance(t0, dd, a, N)
        with open(cnf, 'w') as f:
            f.write('p cnf %d %d\n' % (nv, len(clauses)))
            for c in clauses:
                f.write(' '.join(map(str, c)) + ' 0\n')
        r = subprocess.run(['cadical', '-q', '--lrat', '--no-binary', cnf, lrat], capture_output=True, text=True,
                           timeout=CAP)
        v = cake_check(cnf, lrat) if r.returncode == 20 else '-'
        for p in (cnf, lrat):
            if os.path.exists(p):
                os.unlink(p)
        return tag, r.returncode, v

    c = one((0, 0, 32, 168))
    print('U-C %s: %s (cadical exit 10 = SAT)' % ('PASS' if c[1] == 10 else 'FAIL', c), flush=True)
    cases = [(t0, dd, 12, N) for N in (140, 168) for t0 in (0, 1) for dd in range(0, kk.P, 2)]
    res = [one(a) for a in cases]                           # sequential: cake_lpr takes one check at a time anyway
    unsat = sum(1 for r in res if r[1] == 20)
    ver = sum(1 for r in res if r[2] == 'VERIFIED')
    bad = [r for r in res if not (r[1] == 20 and r[2] == 'VERIFIED')]
    print('U %s: %d instances, CaDiCaL UNSAT %d, cake_lpr VERIFIED %d; not certified: %s' % (
        'HELD' if unsat == ver == len(cases) == 112 else 'REFUTED', len(res), unsat, ver, bad[:6]), flush=True)


W69 = '010000100001001001000010000100100100100001000010010010010000100001001'        # SLC2 round 8 (L630)
W114 = '0000100001001001001' * 6                                                        # (LLSSS)^6 (L627)
W178 = ('01001001001000010000100100100100100001000010010010010010000100001001001001001000010000100'
        '10010010010000100001001001001001000010000100100100100100001000010010010010010000100001001')  # pure M3 (L637)
W50 = '00001000010101010001000010010010000100001001001000'                             # K12
W70 = '0100010001010101000100001001001000010000100100100001000010000100001001'         # K15
MFC_STEMS = ('mfw40', 'mfw40p1', 'cuts40_p0', 'cuts40_p1', 'cuts40_sl', 'mfw44', 'mfw44p1', 'mfw48')


def b2cut(ph, w):
    """Run inside the sandbox (HOME pointed there): certify one word by MFC's committed pipeline."""
    import time
    sys.path.insert(0, HERE)
    _argv, sys.argv = sys.argv, sys.argv[:1]
    import rule30_mfw_certify as mfc
    sys.argv = _argv
    t0 = time.time()
    print('CUT len %d phase %d: %s (%.1f s)' % (len(w), ph, mfc.certify(w, ph), time.time() - t0), flush=True)


def b2mfc(n):
    """Run inside the sandbox: a seeded sample of n list words, each certified by MFC's pipeline."""
    sys.path.insert(0, HERE)
    _argv, sys.argv = sys.argv, sys.argv[:1]
    import rule30_mfw_certify as mfc
    sys.argv = _argv
    pool = [(s, line.split()[0]) for s in MFC_STEMS for line in open(os.path.join(mfc.DIR, s + '.txt')) if line.strip()]
    for s, w in random.Random(20261014).sample(pool, n):
        print('MFC %s %s %s' % (s, w, mfc.certify(w, mfc.PHASE[s])), flush=True)


def b2():
    """B2: the committed probes, run from a scratch clone with HOME pointed at a sandbox that holds copies of the
    lists only, so no receipt in the record's data is read as done or overwritten."""
    import shutil
    import signal
    import time
    home = os.path.join(OUT, 'home')
    clone = os.path.join(OUT, 'placego')
    if not os.path.isdir(clone):
        subprocess.run(['git', 'clone', '-q', '--no-hardlinks', REPO, clone], check=True)
    subprocess.run(['git', '-C', clone, 'pull', '-q', REPO, 'HEAD'], check=True)
    lex = os.path.join(clone, 'tests', 'probes', 'lexicon')
    env = dict(os.environ, HOME=home, NP_SCRATCH_KT2C=os.path.join(OUT, 'kt2c'))
    me = os.path.join(lex, 'rule30_comb_lane_b.py')
    for sub in ('dt', 'kx', 'kt2c'):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)

    def run(name, cmd, cap=CAP):
        t0 = time.time()
        p = subprocess.Popen(cmd, cwd=lex, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                             start_new_session=True)
        try:
            out, _ = p.communicate(timeout=cap)
            tail = 'exit %d' % p.returncode
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            out, _ = p.communicate()
            tail = 'STOPPED at the %d s cap' % cap
        with open(os.path.join(OUT, 'b2_%s.log' % name), 'w') as f:
            f.write(out)
        keep = [l for l in out.splitlines() if re.search(r'PASS|FAIL|HELD|REFUTED|VERIFIED|SAT|CUT |MFC |cut|status|'
                                                         r'entropy|DIFF|COMPLETE|SWT|done|case', l)]
        print('== %s (%s, %.0f s)' % (name, tail, time.time() - t0), flush=True)
        for l in keep[-40:]:
            print('   ' + l[:220], flush=True)

    run('DT', ['python3', 'rule30_kick_bite_drat.py', '8', os.path.join(OUT, 'dt')])
    for name, ph, w in (('W69', 0, W69), ('W114p0', 0, W114), ('W114p1', 1, W114), ('W178', 0, W178)):
        run(name, ['python3', me, 'b2cut', str(ph), w])
    run('K12', ['python3', 'rule30_cadical_certify.py', 'cut', W50, '0'])
    run('K15', ['python3', 'rule30_cadical_certify.py', 'cut', W70, '0'])
    run('MFC', ['python3', me, 'b2mfc', '60'])
    run('SWT', ['python3', 'rule30_cut45_strip_pins.py', 'table'])
    run('SLREPLAY', ['python3', 'rule30_sl_cuts.py', 'replay'])
    run('VCSTATUS', ['python3', 'rule30_verified_certs.py', 'status', 'rr3'])
    run('KX', ['python3', 'rule30_kick_alphabet_exact.py', '8', os.path.join(OUT, 'kx')])
    run('KT2C', ['python3', 'rule30_kick_class42_560.py', 'run'])          # foreground: `start` detaches past the cap
    run('KT2CSTATUS', ['python3', 'rule30_kick_class42_560.py', 'status'], 120)
    # RLK's CUT certificate at d = 107 from its kept CNF (hash checked against rlk_cert.ck first), by RLK's pipeline
    d = os.path.join(OUT, 'd107')
    os.makedirs(d, exist_ok=True)
    src = os.path.join(SCR, 'rule30-rlk', 'cert_d107_L15_p0_40.cnf')
    cnf = os.path.join(d, 'cert_d107_L15_p0_40.cnf')
    shutil.copyfile(src, cnf)
    print('== D107 cnf sha256 %s (receipt 7eb6367d4bdd7dd4)' % sha(cnf)[:16], flush=True)
    run('D107kissat', ['kissat', '-q', '-f', '--no-binary', cnf, cnf[:-4] + '.drat'])
    run('D107drat', ['drat-trim', cnf, cnf[:-4] + '.drat', '-L', cnf[:-4] + '.lrat'])
    run('D107cake', [CAKE, '--CML_HEAP_SIZE=6000', '--CML_STACK_SIZE=2000', cnf, cnf[:-4] + '.lrat'])
    for e in ('.drat', '.lrat'):
        if os.path.exists(cnf[:-4] + e):
            os.unlink(cnf[:-4] + e)


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'stored'
    if a == 'b2cut':
        b2cut(int(sys.argv[2]), sys.argv[3])
    elif a == 'b2mfc':
        b2mfc(int(sys.argv[2]))
    else:
        {'stored': stored, 'cross12': cross12, 'b2': b2}[a]()
