#!/usr/bin/env python3
"""rule30_verified_certs.py: VC, today's UNSAT certificates re-checked by a formally verified checker. drat-trim is
unverified C; cake_lpr (CakeML, proved correct in HOL4) checks LRAT. Installed 2026-10-09 on the owner's word. Local's
run (chat L443), with these predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat, drat-trim, ~/np-build/cake_lpr/cake_lpr); hours for the deep records calls
COMMAND:    python3 tests/probes/lexicon/rule30_verified_certs.py run [JOBS=4] [TIER ...]    (resumable)
            python3 tests/probes/lexicon/rule30_verified_certs.py status

The pipeline per instance: rebuild the CNF with the instance's own builder, kissat writes a text DRAT proof, drat-trim
converts it to LRAT (-L, an untrusted elaboration), and cake_lpr checks the LRAT against the CNF. Only cake_lpr's
"s VERIFIED UNSAT" counts. A wrong proof cannot pass, because cake_lpr is verified; a failure at the drat-trim stage
leaves the instance unresolved, not refuted. Files are deleted after a pass and kept after a failure (scratch only,
~/np-scratch-int/rule30-vc).
Tiers:
  cx   CX and CXE: the 100 critical all-L bridge instances (rule30_critical_bridge_sat.py, L404).
  al   ALC's four all-L slab cases (rule30_all_l_certs.py) and ASF's certificate (rule30_all_s_future.py: S^10, loop 2,
       sites 6 .. 13).
  rr   RRC's 95 deciding calls of the realizable records (rule30_records_real_certs.py, L438).
Hash controls: each rebuilt CNF's SHA-256 prefix is compared with the one recorded when the instance was first
certified (RRC's checkpoint; ALC's and ASF's headers; CX's saved CNF files in ~/np-scratch-int/rule30-al/cx-drat).

PREDICTIONS (Local's, published before the run):
  VC-C1 (control): every rebuilt CNF has the recorded hash (or equals the saved CNF file).
  VC-P1 (blind, confidence 0.95): every instance in every tier ends "s VERIFIED UNSAT" under cake_lpr.
  VC-D1 (descriptive): LRAT sizes and cake_lpr's time against drat-trim's.
"""
import hashlib
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_records_real_sat as rr                                  # noqa: E402
import rule30_records_real_certs as rrc                               # noqa: E402
import rule30_critical_bridge_sat as cx                               # noqa: E402
import rule30_all_l_certs as alc                                      # noqa: E402
import rule30_all_l_slab_sat as alx                                   # noqa: E402
import rule30_all_s_future as asf                                     # noqa: E402
import rule30_neutral_concat as nl                                    # noqa: E402
sys.argv = _argv

DIR = os.path.expanduser('~/np-scratch-int/rule30-vc')
CK = os.path.join(DIR, 'vc.ck')
CAKE = os.path.expanduser('~/np-build/cake_lpr/cake_lpr')
ALC_SHA = {'C10-3': '89bee028ebc399bf', 'C10-2': '379d841d2d39e029', 'C7-5': 'd9839e060ebe33a3', 'C2-0': 'f90a48385863bdcd'}
ASF_SHA = 'eccb9f681ba207bb'


def asf_text():
    K, k, sites = 10, 2, tuple(range(6, 14))
    ref = asf.ring_cols(13)
    cons, Tend = nl.targets('S' * K, 'A', 0)
    cons = cons + [(0, i, v) for i, v in zip(range(2, 6), asf.ENTRANCE)]
    body, ncl, nv, off, width = nl.base(Tend, max(max(sites), 5, max(i for _, i, _ in cons)))
    lits = []
    for s in range(asf.LOOP):
        t = asf.LOOP * k + s
        for i in sites:
            lits.append(-(off[t] + i) if ref[(s, i)] else off[t] + i)
    units = ['%d 0' % (off[t] + i if v else -(off[t] + i)) for t, i, v in cons] + [' '.join(map(str, lits)) + ' 0']
    return 'p cnf %d %d\n' % (nv, ncl + len(units)) + body + '\n'.join(units) + '\n'


def instances(tiers):
    out = []
    if 'cx' in tiers:
        R = [(cx.RING >> i) & 1 for i in range(cx.N)]
        prof = cx.g_profiles(R, range(-1, 3), 310)
        left = {-1: prof[-1], 0: prof[0]}
        saved = os.path.expanduser('~/np-scratch-int/rule30-al/cx-drat')
        for q, tag in ((155, 'q155'), (None, 'q310')):
            for W in (0, 4, 8, 16, 24):
                for P in range(1, 11):
                    name = 'cx-%s-%d-%d' % (tag, W, P)

                    def make(q=q, W=W, P=P):
                        return cx.build(310, left, W, P, q_tail=q)[0].text()
                    f = os.path.join(saved, '%s-%d-%d.cnf' % (tag, W, P))
                    g = os.path.expanduser('~/np-scratch-int/rule30-al/cxe/%s_W%d_P%d.cnf' % (tag, W, P))
                    out.append((name, make, ('file', f) if os.path.exists(f) else ('file', g) if os.path.exists(g)
                                else None))
    if 'al' in tiers:
        ref = alx.ring_cols(8)
        for name, K, k, sites in alc.CASES:
            out.append(('alc-' + name, lambda K=K, k=k, sites=sites: alc.cnf(K, k, sites, ref), ('sha', ALC_SHA[name])))
        out.append(('asf-S10-loop2-sites6-13', asf_text, ('sha', ASF_SHA)))
    if 'rr' in tiers:
        recorded = {int(p[0]): p[4] for p in rrc.receipts() if len(p) == 9}
        for d in rrc.ORDER:
            L = rrc.REAL[d] + 1

            def make(d=d, L=L):
                nv, cl, row, T = rr.cnf(d, L)
                return 'p cnf %d %d\n' % (nv, len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)
            out.append(('rr-%d-%d' % (d, L), make, ('sha', recorded.get(d))))
    return out


def done():
    got = {}
    if os.path.exists(CK):
        for line in open(CK):
            p = line.split()
            if line.endswith('\n') and len(p) == 9:
                got[p[0]] = p
    return got


def append(line):
    with open(CK, 'a+') as f:
        f.seek(0, 2)
        if f.tell() > 0:
            f.seek(f.tell() - 1)
            if f.read(1) != '\n':
                f.write('\n')
        f.write(line)


def run_one(item):
    name, make, ctrl = item
    lock = os.path.join(DIR, name + '.lock')
    try:
        os.close(os.open(lock, os.O_CREAT | os.O_EXCL))
    except FileExistsError:
        return
    try:
        text = make()
        sha = hashlib.sha256(text.encode()).hexdigest()[:16]
        cnf, drat, lrat = (os.path.join(DIR, name + e) for e in ('.cnf', '.drat', '.lrat'))
        open(cnf, 'w').write(text)
        if ctrl is None:
            hashok = 'NA'
        elif ctrl[0] == 'file':
            hashok = 'MATCH' if open(ctrl[1]).read() == text else 'DIFF'
        else:
            hashok = 'MATCH' if ctrl[1] == sha else ('NA' if ctrl[1] is None else 'DIFF')
        t0 = time.time()
        k = subprocess.run(['kissat', '-q', '-f', '--no-binary', cnf, drat], capture_output=True, text=True)
        t1 = time.time()
        stage, verdict = 'kissat', 'UNKNOWN%d' % k.returncode
        if k.returncode == 20:
            v = subprocess.run(['drat-trim', cnf, drat, '-L', lrat, '-t', '400000'], capture_output=True, text=True)
            if 's VERIFIED' in [l.replace('\r', '').strip() for l in v.stdout.splitlines()] and os.path.exists(lrat):
                stage = 'cake'
                c = subprocess.run([CAKE, '--CML_HEAP_SIZE=6000', '--CML_STACK_SIZE=2000', cnf, lrat],
                                   capture_output=True, text=True)
                verdict = 'VERIFIED-UNSAT' if 's VERIFIED UNSAT' in c.stdout else 'CAKE-FAILED'
                diag = c.stdout + c.stderr
            else:
                stage, verdict, diag = 'drat-trim', 'ELAB-FAILED', v.stdout + v.stderr
        else:
            diag = k.stdout + k.stderr
        t2 = time.time()
        size = os.path.getsize(lrat) if os.path.exists(lrat) else 0
        append('%s %s %s %s %s %d %.1f %.1f %s\n' % (name, verdict, stage, sha, hashok, size, t1 - t0, t2 - t1,
                                                    time.strftime('%H:%M')))
        if verdict == 'VERIFIED-UNSAT':
            for f in (cnf, drat, lrat):
                os.unlink(f)
        else:
            open(os.path.join(DIR, name + '.diag'), 'w').write(diag[-8000:])
        print(name, verdict, hashok, flush=True)
    finally:
        os.unlink(lock)


def status(tiers):
    got = done()
    items = instances(tiers)
    names = [n for n, _, _ in items]
    ok = [n for n in names if n in got and got[n][1] == 'VERIFIED-UNSAT']
    bad = [n for n in names if n in got and got[n][1] != 'VERIFIED-UNSAT']
    diff = [n for n in names if n in got and got[n][4] == 'DIFF']
    print('tiers %s: %d of %d VERIFIED-UNSAT by cake_lpr; not verified %s; hash DIFF %s; missing %d' % (
        '+'.join(tiers), len(ok), len(names), bad or 'none', diff or 'none', len(names) - len(ok) - len(bad)))
    if len(ok) == len(names):
        print('VC-C1', 'PASS' if not diff else 'FAIL')
        print('VC-P1 HELD')
        print('COMPLETE')


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    jobs = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 4
    tiers = [a for a in sys.argv[2:] if a in ('cx', 'al', 'rr')] or ['cx', 'al', 'rr']
    os.makedirs(DIR, exist_ok=True)
    if cmd == 'run':
        got = done()
        todo = [it for it in instances(tiers) if it[0] not in got]
        with ThreadPoolExecutor(jobs) as ex:
            list(ex.map(run_one, todo))
    status(tiers)


if __name__ == '__main__':
    main()
