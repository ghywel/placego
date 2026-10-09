#!/usr/bin/env python3
"""rule30_layer_product.py: LP, the 0101 channel bounded by a layer automaton and the true forbidden words at once
(Cloud's CL113 suggestion; GPT's GC883 audit of the route). Local, chat L503; predictions pushed before any run of a
layer with F.

RUN-ON:     cpu (C, one core); minutes; under 2 GB at width 22
COMMAND:    python3 tests/probes/lexicon/rule30_layer_product.py FWORDS [WIDTHS=16,18,20,22]
            (needs ~/np-scratch-int/rule30-oh/ohc and lp, built from rule30_one_hole_widths.c and
            rule30_layer_product.c; FWORDS is TC2's list of true minimal forbidden words, one per line)

Why. §8.20 bounds column 1 next to 0101 by layer relaxations (certified 0.1236 bits per visible bit at m = 28, SQ6;
OHC at p = 2 reproduces the table to width 22, XC). TC2 (rule30_cloud_channel_truecount.py, CL113) found 746 true
minimal forbidden words F to 39 visible bits, but F alone certifies only 0.1517. A word of F that the layer allows is
a constraint the layer misses. The synchronized product of the layer's subset automaton with F's Aho-Corasick
automaton accepts the layer's words that avoid F, so it bounds the true language by both at once (GC883: sound;
it inherits the better factor's bound by lifting, so only a NEW integer certificate below the target counts).
The visible bit is cell 1 at even times, read before each white-then-black macro, in OHC, TC and entropy2 alike
(GC883); one product transition is one visible bit, two Rule 30 updates.

Method (rule30_layer_product.c). OHC_DUMP writes OHC's labelled transitions (node 0 = the full set). LP builds
the product by BFS from (0, root), keeping both labelled successors, prunes nothing from the matrix but splits it
into strongly connected components; per cyclic component, a power iteration of A + I gives a positive vector,
scaled to integers u (at most 2^50, at least 1), and R = max ceil(D (A u)_i / u_i) with D = 10^9 is checked in
128-bit integers (D A u <= R u), so rho <= R / D. The bound is the largest R over components. This script then tests
log2(R / D) < 0.1236 exactly in integers (R^2500 < 2^309 D^2500), and < 0.120 (R^1000 < 2^120 D^1000).

Record searched: 'product|Aho' with 'layer|automaton' and 'channel|forbidden' -> GC857 (an exemption bound for one
direct automaton), GC877 and GC883 (TC2's automaton; the product route audited, no run), TC2's docstring
(the suggestion), rule30_cloud_hole_freepairs.py (AC over pairs). No product of a layer with F has been run.

SMOKE (instrument only, before these predictions; 22:51 BST): the one-node layer with F empty, {11}, {11, 111} and
{00, 01} gives certified 2, 1.618033989, 1.618033989 and 1 (live states 1, 2, 2, 1), GC883's and TC2's hand controls.

PREDICTIONS (Local's, 2026-10-09 22:53 BST, before any run of a layer with F):
  LP-C1 (control, must hold): with F empty, the product at widths 16 .. 22 reproduces OHC's growth (word-count
        ratio to 1e-9; certificate within 1e-6 above it): 0.211584, 0.184569, 0.151866, 0.137234 bits.
  LP-C2 (control, must hold): F split into F_red (words the layer forbids) and F_new (words it allows). The product
        with F_red alone has exactly the layer's language, so its word-count ratio agrees to 1e-10 at every width
        (GC883's redundant-list example).
  LP-C3 (replay of TC2, must hold): the one-node layer with F gives TC2's 8,030 live states and a certificate of
        log2 rho = 0.151730 to 1e-5.
  LP-P1 (blind, confidence 0.35): at width 22 the product certifies below 0.1236 bits per visible bit, beating §8.20.
  LP-P2 (blind, confidence 0.85): at width 22 the product certifies at least 0.002 below the layer's 0.137234.
  LP-P3 (blind, confidence 0.2): at width 22 it certifies below 0.120.
  LP-U, the unexpected check (blind, confidence 0.5): the shortest word of F that the width-22 layer allows has
        length at least 24 (the width-12 layer's counts already equal TC2's true counts to n = 16).
  LP-D (descriptive): by width, the certificate, live states, and how many F words the layer allows, by length.
  Counterfactual. If P1 fails, the record keeps 0.1236, and P2 is decided on its own test (GC884: P1's failure
  implies nothing about P2); a longer F or a wider layer (24 fits in about 2 GB) is the next step, not a different
  route.
  AMENDED per GPT's GC884 (22:57 BST, before any run with F): verdicts are gated on C1, C2 and C3 (NOT DECIDED if any
  fails); P2 is tested exactly as R0^500 >= 2 R1^500; the counterfactual above no longer assumes P2. split_f's premise
  (the layer language is factorial from the full-set root, so F_red changes nothing) is GC884's hand proof.
C1 FIRST RUN, 2026-10-09 22:54 BST (M5, F empty, widths 16 .. 22): C1 FAILED AS REGISTERED at widths 20 and 22; the
  fault is in the registered comparison, not in either instrument.
  - Widths 16 and 18 agree (ratio and certificate). At 20 and 22, OHC's "growth" 1.111005219364 and 1.099794457745 lie
    above LP's certified radii 1.111005204 and 1.099794104.
  - Diagnosis (22:55). OHC's printed growth is its count ratio at n = 1500 (GC858: a finite ratio, not a certificate).
    Run at the same n, LP reproduces both values to all 12 digits. The ratios converge to 1.111005203474 and
    1.099794103997 by n = 6000 (unchanged at 12000), inside LP's power-iteration brackets.
  - So OHC's n = 1500 values at widths 20 and 22 were not yet converged, by 1.6e-8 and 3.2e-7 (4.6e-7 bits at width
    22). XC's 3-decimal agreement with §8.20 is unaffected.
  - C1 is amended accordingly (in main(), marked): compare at equal n, and require the certificate within 1e-6 above
    the n = 12000 ratio.
ODD (registered 2026-10-09 22:57 BST, before running; the one-hole walls 0 1^(p-1), p = 5, 7, 9, layer alone, F empty):
  Record searched: '1\.543759' -> RECORD-MAP (L481), OHC's SCOPE CORRECTION block, TC (rule30_cloud_hole_truecount.py)
  and TC2. The record's certified width-22 bounds 1.543759, 1.652210, 1.742260 are c_60^(1/60), a count bound. OHC's
  float ratios at width 22 are 1.47123, 1.59941, 1.71445 (not certificates). CL113 compares TC's spectral certificates
  1.512835 (p = 5) and 1.642221 (p = 7) with the count bounds and concludes that "the true words do beat the layer".
  LP-O1 (blind, confidence 0.85): LP certifies the width-22 layer's radius within 1e-4 above OHC's float ratios at
        p = 5, 7 and 9, so below 1.4713, 1.5995 and 1.7146.
  LP-O2 (consequence of O1, confidence 0.85): at p = 5 and 7 the width-22 layer's certified radius is below TC's
        1.512835 and 1.642221, reversing CL113's comparison; the record's best certified bounds become the layer's.
  Counterfactual. If O1 fails, the float ratios hide a slow transient or a larger component, and CL113's comparison
  stands.
"""
import os
import subprocess
import sys

BIN = os.path.expanduser('~/np-scratch-int/rule30-oh')
OHC, LP = os.path.join(BIN, 'ohc'), os.path.join(BIN, 'lp')
D = 10 ** 9


def run(cmd, env=None):
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if r.returncode:
        raise SystemExit('FAILED: %s\n%s%s' % (' '.join(cmd), r.stdout, r.stderr))
    return r.stdout


def cert(out):
    line = [x for x in out.splitlines() if x.startswith('CERTIFIED')][0]
    R = int(line.split('<=')[1].split('/')[0])
    ratio = float([x for x in out.splitlines() if x.startswith('word-count ratio')][0].split(':')[1])
    live = int([x for x in out.splitlines() if 'live (infinite future)' in x][0].split()[-1])
    return R, ratio, live


def below(R, num, den, bits_num):
    """exact: log2(R / D) < bits_num / den, i.e. R^den < 2^bits_num D^den"""
    return R ** den < 2 ** bits_num * D ** den


def split_f(fpath, dump, tmp):
    """F_red: words the layer forbids (walking the dump from node 0); F_new: the rest"""
    import struct
    with open(dump, 'rb') as f:
        n = struct.unpack('<q', f.read(8))[0]
        tr = struct.unpack('<%dq' % (2 * n), f.read(16 * n))
    red, new = [], []
    for w in open(fpath).read().split():
        if w.startswith('#'):
            continue
        s = 0
        for c in w:
            s = tr[2 * s + int(c)]
            if s < 0:
                break
        (red if s < 0 else new).append(w)
    pr, pn = tmp + '.red', tmp + '.new'
    open(pr, 'w').write('\n'.join(red) + '\n')
    open(pn, 'w').write('\n'.join(new) + '\n')
    return pr, pn, len(red), len(new)


def main():
    import math
    fpath = sys.argv[1]
    widths = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else '16,18,20,22').split(',')]
    tmpdir = os.path.expanduser('~/np-scratch-int/rule30-lp')
    os.makedirs(tmpdir, exist_ok=True)
    out = run([LP, '-', fpath])
    R, ratio, live = cert(out)
    print('one-node layer with F:', out.splitlines()[0])
    print('  live %d, certified R = %d, log2 <= %.6f' % (live, R, math.log2(R / D)))
    c3 = live == 8030 and abs(math.log2(R / D) - 0.151730) < 1e-5
    print('LP-C3', 'PASS' if c3 else 'FAIL')
    c1 = c2 = True
    res = {}
    for k in widths:
        dump = os.path.join(tmpdir, 'k%d.dump' % k)
        o = run([OHC, str(k), '2'], env=dict(os.environ, OHC_DUMP=dump))
        g = float([x for x in o.splitlines() if ' growth ' in x and 'nodes' in x][0].split('growth')[1].split()[0])
        R0, r0, l0 = cert(run([LP, dump, '-']))
        # C1 as amended after its first run (OUTCOME): OHC's growth is its ratio at n = 1500, so compare at equal n;
        # the certificate must lie within 1e-6 above the converged ratio (n = 12000)
        _, r1500, _ = cert(run([LP, dump, '-'], env=dict(os.environ, LP_N='1500')))
        _, rinf, _ = cert(run([LP, dump, '-'], env=dict(os.environ, LP_N='12000')))
        ok1 = abs(r1500 - g) < 1e-11 and 0 <= R0 / D - rinf < 1e-6
        c1 &= ok1
        pr, pn, nred, nnew = split_f(fpath, dump, os.path.join(tmpdir, 'k%d' % k))
        Rr, rr, lr = cert(run([LP, dump, pr]))
        ok2 = abs(rr - r0) < 1e-10
        c2 &= ok2
        o = run([LP, dump, fpath])
        R1, r1, l1 = cert(o)
        allowed = [x for x in o.splitlines() if x.startswith('allowed by length') or 'F words the layer allows' in x]
        res[k] = (R0, R1, l1, allowed)
        print('width %d: layer %.6f bits (ratio %.12f, C1 %s); F_red %d, F_new %d (C2 %s); product live %d, '
              'certified R = %d, %.6f bits, ratio %.12f' % (k, math.log2(R0 / D), r0, 'ok' if ok1 else 'FAIL', nred,
                                                             nnew, 'ok' if ok2 else 'FAIL', l1, R1,
                                                             math.log2(R1 / D), r1), flush=True)
        for a in allowed:
            print('   ', a)
    print('LP-C1', 'PASS' if c1 else 'FAIL')
    print('LP-C2', 'PASS' if c2 else 'FAIL')
    if 22 in res:
        # GC884: a failed control makes every verdict NOT DECIDED (the arithmetic is still printed above); P2's gap of
        # 0.002 = 1/500 bits is tested exactly, R0^500 >= 2 R1^500 (common D)
        ctl = c1 and c2 and c3
        R0, R1, l1, allowed = res[22]

        def verdict(ok):
            return ('HELD' if ok else 'REFUTED') if ctl else 'NOT DECIDED (a control failed; %s)' % ('held' if ok else 'refuted')
        print('LP-P1', verdict(below(R1, 1, 2500, 309)))
        print('LP-P2', verdict(R0 ** 500 >= 2 * R1 ** 500))
        print('LP-P3', verdict(below(R1, 1, 1000, 120)))
        sh = [x for x in allowed if 'shortest' in x]
        m = int(sh[0].split('shortest')[1].strip(' )')) if sh else None
        print('LP-U', verdict(m >= 24) + ' (shortest %d)' % m if m else verdict(True) + ' (no F word allowed)')
    print('COMPLETE')


if __name__ == '__main__':
    main()
