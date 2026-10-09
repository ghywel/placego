#!/usr/bin/env python3
"""rule30_layer_product.py: LP, the 0101 channel bounded by a layer automaton and the true forbidden words at once
(Cloud's CL113 suggestion; GPT's GC883 audit of the route). Local, chat L503; predictions pushed before any run of a
layer with F.

RUN-ON:     cpu (C, one core); minutes; under 2 GB at width 22
COMMAND:    python3 tests/probes/lexicon/rule30_layer_product.py FWORDS [WIDTHS=16,18,20,22]
            python3 tests/probes/lexicon/rule30_layer_product.py verify DUMP FWORDS CERT   (GC885's verifier)
            python3 tests/probes/lexicon/rule30_layer_product.py odd P FWORDS TC_CEILING   (ODD3, width 22)
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
ODD OUTCOME, 2026-10-09 22:59 BST (M5, about 1 GB and a minute per wall, at commit 1927de3b's code): LP-O1 HELD, LP-O2
  HELD.
  - Width 22, certified in integers (D A u <= R u, D = 10^9), per hole:
    - p = 5: rho <= 1.471226748 (0.557020 bits); main component 17,546 of 25,870 states;
    - p = 7: rho <= 1.599413180 (0.677543 bits); 18,586 of 25,306;
    - p = 9: rho <= 1.714446202 (0.777743 bits); 17,077 of 18,046.
  - Each is within 1e-9 of the count ratio at n = 12000, and OHC's n = 1500 ratios agree to 12 digits here.
  - These replace the record's c_60 bounds 1.543759, 1.652210 and 1.742260 as the certified width-22 bounds. They rest
    on the same premises: every true right half's state lies in the relaxation, and OHC identifies subsets by a
    128-bit hash with no full comparison (no collision known).
  - At p = 5 and 7 the layer is sharper than TC's true-word certificates 1.512835 and 1.642221 (CL113). CL113's
    "the true words do beat the layer" compared TC's spectral certificate with the layer's count bound; it reverses.
    The product of the width-22 layer with TC's odd-wall F is the natural next step, as at p = 2.
ODD2 (registered 2026-10-09 23:00 BST, before running; the board's other open walls p = 3, 4, 6, layer alone, width 22):
  OHC's TB block gives float ratios 1.2204, 1.2318, 1.3839 with c_60 bounds 1.302223, 1.290796, 1.407029.
  LP-O3 (blind, confidence 0.85): LP certifies each width-22 radius within 1e-4 above the float ratio, so below
        1.2205, 1.2319 and 1.3840.
ODD2 OUTCOME, 2026-10-09 23:04 BST (M5, at most 1.3 GB, at commit 994486ef's code): LP-O3 HELD. Width 22, per hole:
  - p = 3: rho <= 1.220381225 (0.287332 bits; was c_60's 1.302223);
  - p = 4: rho <= 1.231762860 (0.300725 bits; was 1.290796);
  - p = 6: rho <= 1.383946733 (0.468788 bits; was 1.407029).
  Each is within 1e-9 of the n = 12000 count ratio. Cloud's CL116 notes that at p = 9 TC's 1.709537 stays below the
  layer's 1.714447, so there the true-word certificate is the record's best; at p = 5 and 7 the layer's is.
VERIFIER (GC885, built 23:06 BST, before the run with F): LP_CERT retains the product graph, the block of every
  state (Tarjan's order), each block's R and every u_i; `verify` rebuilds the product from the dump and F with a
  string Aho-Corasick written separately, and checks the graph, the block-triangular order and every inequality in
  Python integers. Smoke: it reproduces LP's R on the four toy controls and on p = 5's width-22 layer (0.1 s).
  Tamper controls fail closed: R - 1 in the top block ("inequality at state 279"), one successor changed ("graph
  differs"), state 0 moved to block 0 ("a cross-block edge does not descend"). In the main run every certificate is
  verified, and a failed or missing one makes the verdicts NOT DECIDED (LP-V).
OUTCOME, 2026-10-09 23:08 BST (M5, 35 s, 640 MB, at commit 35c472b8; F = CL115's file, SHA-256 2f8eba0f...dd23b checked):
  LP-C1 PASS (as amended), LP-C2 PASS, LP-C3 PASS, LP-V PASS; LP-P1 REFUTED, LP-P2 HELD, LP-P3 REFUTED, LP-U HELD.
  - C3, F alone: 8,030 live states and log2 rho <= 0.151721 (R = 1110894238), against TC2's 0.151730; the vector
    is better converged here, and the difference is within the registered 1e-5.
  - Certified and independently verified bits per visible bit (the layer alone, then the product with F):
    - width 16: 0.211584, then 0.146168 (F_new: 568 of 746 words, the shortest of length 18);
    - width 18: 0.184569, then 0.141207 (477 words; shortest 22);
    - width 20: 0.151866, then 0.135971 (344 words; shortest 22);
    - width 22: 0.137233, then 0.130284 (242 words, lengths 27 .. 40; 32,481 live product states).
  - So at every width the product beats both factors. Its gain over the layer shrinks: 0.0654, 0.0434, 0.0159 and
    0.0069 bits.
  - P1. The width-22 product does not reach §8.20's certified 0.1236 at m = 28. That figure carries SQ's chosen margin
    lambda' = lambda (1 + 10^-3), about 0.0014 bits; m = 28's radius is 0.1222 by power iteration.
  - So beating 0.1236 is mostly a question of the certificate's margin. The informative quantity is the product's gain
    at equal width, and that falls by a third to two thirds for each two cells.
  - The count ratio at n = 3000 (1.094512465) lies above the width-22 certificate (1.094509113). It converges to
    1.094509112407 by n = 12000, below it: a finite-n transient, as in C1.
  - Reading. F's words up to 40 visible bits carry constraints that the layer only reaches about four to six cells
    wider. They do not change the picture of the channel levelling off near 0.12. A tight certificate on entropy2's
    m = 28 automaton (about 0.1222), or that automaton times F, would sharpen the record's figure by a few
    thousandths at most, at SQ6's 6 GB.
ODD3 (registered 2026-10-09 23:11 BST, before Cloud's odd-wall lists are seen): the width-22 layer times TC's true
  minimal forbidden words at the walls 0 1^(p-1), p = 5, 7, 9 (CL114: 1,328, 641 and 270 words, to 17, 15 and 14
  holes; TC's ceilings 1.512835, 1.642221, 1.709537; the layer's radii 1.471227, 1.599414, 1.714447 from ODD). The
  hole is x1 at times kp in both TC and OHC (TC-C1 matched OHC's counts).
  Record searched: as for ODD, plus 'free pair' -> CL114's FP (pairs free to 14 .. 17 holes).
  LP-O4-C (controls, must hold at each p): F_red changes nothing (C2's test); the one-node layer with F replays TC's
        ceiling, log2 within 1e-4 below it and at most 1e-6 above; every certificate verifies.
  LP-O4-P1 (blind, confidence 0.7): at p = 5 the product certifies at least 0.005 below the layer's 1.471227.
  LP-O4-P2 (blind, confidence 0.5): at p = 9 the product beats both factors, certifying below TC's 1.709537.
  LP-O4-P3 (blind, confidence 0.6): at p = 7 the product certifies at least 0.005 below the layer's 1.599414.
  LP-O4-U (blind, confidence 0.4): at p = 5, CL114 says the truth pulls ahead of the width-22 relaxation's minimal
        forbidden counts only from length 13; still, some word of F_new has length 12 or less.
  Counterfactual. If P1 and P3 fail, TC's short true words (to 14 .. 17 holes) add little beyond the width-22 layer,
  and the next step is longer true words, not wider layers.
  (The lists, CL117, were committed by Cloud at 23:11 and merged here only after this block was pushed, 9153db1a.)
ODD3 OUTCOME, 2026-10-09 23:14 BST (M5, under 1 GB, a minute per wall, at commit 9153db1a; digests checked against
  CL117): LP-O4-C PASS at p = 5, 7 and 9; LP-O4-P1 HELD, LP-O4-P2 HELD, LP-O4-P3 HELD, LP-O4-U REFUTED.
  - Certified and verified, per hole (the layer, F alone, then the product):
    - p = 5: 1.471226748, 1.512834968, then 1.461899294 (0.547844 bits); F_new 493 of 1,328 words, lengths 13 .. 18;
    - p = 7: 1.599413180, 1.642221323, then 1.590414302 (0.669403 bits); F_new 288 of 641, lengths 10 .. 16;
    - p = 9: 1.714446202, 1.709537420, then 1.697624906 (0.763518 bits); F_new 150 of 270, lengths 10 .. 15.
  - The product beats the better factor by 0.0092, 0.0081 and 0.0101 bits a hole.
  - C3: F alone replays TC's ceilings; the differences, below 3e-7 bits, are TC's rounding to 6 decimals.
  - U refuted: at p = 5 the shortest F word the layer allows has length 13, as CL114 found from the counts. At p = 7
    and 9 it is 10.
  - These are the record's best certified ceilings on the true one-hole languages. Zero entropy stays open: these
    are upper bounds, and Cloud's free pairs (CL114) are the lower-bound side.

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


def verify(dump, fpath, certpath):
    """GC885's retained-certificate check, written separately from the C. Rebuilds the labelled product from the
    dump and F with a string Aho-Corasick (state = the longest suffix of the input that is a prefix of a word of F;
    an edge dies if a suffix of the extended input is in F), compares it with the certificate's graph, then checks
    in Python integers: every cross-block edge goes to a strictly smaller block id (block-triangular), every block
    marked acyclic is one state without a self-loop, and every cyclic block has u_i >= 1 and D (A u)_i <= R_c u_i.
    Then rho <= max R_c / D. Returns that R, or raises on any failure."""
    import array
    import struct
    if dump == '-':
        tr = [0, 0]
    else:
        with open(dump, 'rb') as f:
            n = struct.unpack('<q', f.read(8))[0]
            tr = array.array('q')
            tr.fromfile(f, 2 * n)
    words = set() if fpath == '-' else {w for w in open(fpath).read().split() if not w.startswith('#')}
    pref = {w[:i] for w in words for i in range(len(w) + 1)} | {''}

    def ac(sv, b):
        t = sv + b
        if any(t[i:] in words for i in range(len(t))):
            return None
        for i in range(len(t) + 1):
            if t[i:] in pref:
                return t[i:]
    keys, index, suc = [(0, '')], {(0, ''): 0}, []
    i = 0
    while i < len(keys):
        l, sv = keys[i]
        for b in (0, 1):
            l2 = tr[2 * l + b]
            s2 = ac(sv, str(b)) if l2 >= 0 else None
            if s2 is None:
                suc.append(-1)
                continue
            j = index.get((l2, s2))
            if j is None:
                j = index[(l2, s2)] = len(keys)
                keys.append((l2, s2))
            suc.append(j)
        i += 1
    with open(certpath, 'rb') as f:
        magic, ns, na, nl, ncomp = struct.unpack('<5q', f.read(40))
        Dc = struct.unpack('<Q', f.read(8))[0]
        ck = array.array('q'); ck.fromfile(f, ns)
        cs = array.array('i'); cs.fromfile(f, 2 * ns)
        cc = array.array('i'); cc.fromfile(f, ns)
        cy = f.read(ncomp)
        cR = array.array('Q'); cR.fromfile(f, ncomp)
        cu = array.array('Q'); cu.fromfile(f, ns)
        if f.read(1):
            raise SystemExit('VERIFY FAILED: trailing bytes')
    if magic != 0x3143504C or Dc != D or ns != len(keys) or list(cs) != suc:
        raise SystemExit('VERIFY FAILED: graph differs (states %d against %d)' % (ns, len(keys)))
    amap, smap = {}, {}
    for (l, sv), k in zip(keys, ck):
        if k // na != l or amap.setdefault(k % na, sv) != sv or smap.setdefault(sv, k % na) != k % na:
            raise SystemExit('VERIFY FAILED: state keys differ')
    size = [0] * ncomp
    for c in cc:
        size[c] += 1
    for v in range(ns):
        for b in (0, 1):
            t = suc[2 * v + b]
            if t >= 0 and cc[t] != cc[v] and not cc[t] < cc[v]:
                raise SystemExit('VERIFY FAILED: a cross-block edge does not descend')
        c = cc[v]
        inner = sum(cu[t] for t in suc[2 * v:2 * v + 2] if t >= 0 and cc[t] == c)
        if cy[c]:
            if cu[v] < 1 or D * inner > cR[c] * cu[v]:
                raise SystemExit('VERIFY FAILED: inequality at state %d' % v)
        elif size[c] != 1 or v in suc[2 * v:2 * v + 2]:
            raise SystemExit('VERIFY FAILED: a block marked acyclic has a cycle')
    return max((cR[c] for c in range(ncomp) if cy[c]), default=0)


def cert(out):
    if not any(x.startswith('CERTIFIED') for x in out.splitlines()):
        return None
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


def lpv(tmp, dump, fpath, name, env_extra=None):
    """run LP with a retained certificate, then verify it independently; returns (R, ratio, live, out), with R None
    when the run was not decided or the verified R differs from the printed one"""
    cpath = os.path.join(tmp, name + '.cert')
    env = dict(os.environ, LP_CERT=cpath, **(env_extra or {}))
    out = run([LP, dump, fpath], env=env)
    c = cert(out)
    if c is None:
        print('   ', name, 'NOT DECIDED:', [x for x in out.splitlines() if 'NOT DECIDED' in x])
        return None, None, None, out
    R, ratio, live = c
    Rv = verify(dump, fpath, cpath)
    if Rv != R:
        print('   ', name, 'VERIFIED R %d differs from the printed %d' % (Rv, R))
        return None, ratio, live, out
    os.remove(cpath)
    return R, ratio, live, out


def odd(p, fpath, tc_ceiling):
    """ODD3: the width-22 layer at the wall 0 1^(p-1) times TC's F, with controls and verification"""
    import math
    tmpdir = os.path.expanduser('~/np-scratch-int/rule30-lp')
    os.makedirs(tmpdir, exist_ok=True)
    dump = os.path.join(tmpdir, 'p%dk22.dump' % p)
    run([OHC, '22', str(p)], env=dict(os.environ, OHC_DUMP=dump))
    R0, r0, l0, _ = lpv(tmpdir, dump, '-', 'p%d-layer' % p)
    pr, pn, nred, nnew = split_f(fpath, dump, os.path.join(tmpdir, 'p%d' % p))
    rr = cert(run([LP, dump, pr]))
    c2 = rr is not None and r0 is not None and abs(rr[1] - r0) < 1e-10
    Rf, rf, lf, of = lpv(tmpdir, '-', fpath, 'p%d-F' % p)
    c3 = Rf is not None and -1e-4 <= math.log2(Rf / D) - math.log2(tc_ceiling) <= 1e-6
    R1, r1, l1, o = lpv(tmpdir, dump, fpath, 'p%d-product' % p)
    vok = None not in (R0, Rf, R1)
    print('p = %d: F %s' % (p, of.splitlines()[0]))
    if vok:
        print('  layer %.9f; F alone %.9f (TC %.6f; C3 %s); F_red %d, F_new %d (C2 %s); product %.9f, live %d' % (
            R0 / D, Rf / D, tc_ceiling, 'ok' if c3 else 'FAIL', nred, nnew, 'ok' if c2 else 'FAIL', R1 / D, l1))
    for x in o.splitlines():
        if x.startswith('allowed by length') or 'F words the layer allows' in x:
            print('   ', x)
    ok = c2 and c3 and vok
    print('LP-O4-C p = %d' % p, 'PASS' if ok else 'FAIL')
    return ok, R0, Rf, R1, o


def main():
    import math
    if sys.argv[1] == 'odd':
        odd(int(sys.argv[2]), sys.argv[3], float(sys.argv[4]))
        return
    if sys.argv[1] == 'verify':
        print('verified rho <= %d/%d' % (verify(sys.argv[2], sys.argv[3], sys.argv[4]), D))
        return
    fpath = sys.argv[1]
    widths = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else '16,18,20,22').split(',')]
    tmpdir = os.path.expanduser('~/np-scratch-int/rule30-lp')
    os.makedirs(tmpdir, exist_ok=True)
    R, ratio, live, out = lpv(tmpdir, '-', fpath, 'c3')
    print('one-node layer with F:', out.splitlines()[0])
    c3 = R is not None and live == 8030 and abs(math.log2(R / D) - 0.151730) < 1e-5
    if R is not None:
        print('  live %d, certified and verified R = %d, log2 <= %.6f' % (live, R, math.log2(R / D)))
    print('LP-C3', 'PASS' if c3 else 'FAIL')
    c1 = c2 = vok = True
    res = {}
    for k in widths:
        dump = os.path.join(tmpdir, 'k%d.dump' % k)
        o = run([OHC, str(k), '2'], env=dict(os.environ, OHC_DUMP=dump))
        g = float([x for x in o.splitlines() if ' growth ' in x and 'nodes' in x][0].split('growth')[1].split()[0])
        R0, r0, l0, _ = lpv(tmpdir, dump, '-', 'k%d-layer' % k)
        # C1 as amended after its first run (OUTCOME): OHC's growth is its ratio at n = 1500, so compare at equal n;
        # the certificate must lie within 1e-6 above the converged ratio (n = 12000)
        _, r1500, _ = cert(run([LP, dump, '-'], env=dict(os.environ, LP_N='1500')))
        _, rinf, _ = cert(run([LP, dump, '-'], env=dict(os.environ, LP_N='12000')))
        ok1 = R0 is not None and abs(r1500 - g) < 1e-11 and 0 <= R0 / D - rinf < 1e-6
        c1 &= ok1
        pr, pn, nred, nnew = split_f(fpath, dump, os.path.join(tmpdir, 'k%d' % k))
        rr = cert(run([LP, dump, pr]))
        ok2 = rr is not None and r0 is not None and abs(rr[1] - r0) < 1e-10
        c2 &= ok2
        R1, r1, l1, o = lpv(tmpdir, dump, fpath, 'k%d-product' % k)
        vok &= R0 is not None and R1 is not None
        allowed = [x for x in o.splitlines() if x.startswith('allowed by length') or 'F words the layer allows' in x]
        res[k] = (R0, R1, l1, allowed)
        if R0 is None or R1 is None:
            print('width %d: NOT DECIDED (a certificate is missing or failed verification)' % k, flush=True)
            continue
        print('width %d: layer %.6f bits (ratio %.12f, C1 %s); F_red %d, F_new %d (C2 %s); product live %d, '
              'certified and verified R = %d, %.6f bits, ratio %.12f' % (k, math.log2(R0 / D), r0,
                                                                         'ok' if ok1 else 'FAIL', nred, nnew,
                                                                         'ok' if ok2 else 'FAIL', l1, R1,
                                                                         math.log2(R1 / D), r1), flush=True)
        for a in allowed:
            print('   ', a)
    print('LP-C1', 'PASS' if c1 else 'FAIL')
    print('LP-C2', 'PASS' if c2 else 'FAIL')
    print('LP-V (every certificate verified independently, GC885)', 'PASS' if vok else 'FAIL')
    if 22 in res and res[22][0] is not None and res[22][1] is not None:
        # GC884: a failed control makes every verdict NOT DECIDED (the arithmetic is still printed above); P2's gap of
        # 0.002 = 1/500 bits is tested exactly, R0^500 >= 2 R1^500 (common D)
        ctl = c1 and c2 and c3 and vok
        R0, R1, l1, allowed = res[22]

        def verdict(ok):
            return ('HELD' if ok else 'REFUTED') if ctl else 'NOT DECIDED (a control failed; %s)' % ('held' if ok else 'refuted')
        print('LP-P1', verdict(below(R1, 1, 2500, 309)))
        print('LP-P2', verdict(R0 ** 500 >= 2 * R1 ** 500))
        print('LP-P3', verdict(below(R1, 1, 1000, 120)))
        sh = [x for x in allowed if 'shortest' in x]
        m = int(sh[0].split('shortest')[1].strip(' )')) if sh else None
        print('LP-U', verdict(m >= 24) + ' (shortest %d)' % m if m else verdict(True) + ' (no F word allowed)')
    elif 22 in res:
        print('LP-P1, P2, P3, U: NOT DECIDED (width 22 has no verified certificate)')
    print('COMPLETE')


if __name__ == '__main__':
    main()
