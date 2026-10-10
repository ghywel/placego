#!/usr/bin/env python3
"""rule30_cut45_strip_pins.py: SWP, the least strip width that forces the length-45 cut's common pins (Cloud's CL208).

RUN-ON:     cpu (Python 3, kissat 4.0.4 as KISSAT); one core, minutes
COMMAND:    python3 tests/probes/lexicon/rule30_cut45_strip_pins.py [WMIN=24] [WMAX=40]
            python3 tests/probes/lexicon/rule30_cut45_strip_pins.py cert W WORD   (strip exclusion -> cake_lpr)

The question (CL208). q = 00001000101000010101010101010101010001000010 is the length-45 cut f (L593) without its
final 1: the leading 0, the entry, ten cars, nine exit bits. Over all actual realizers, q forces sites 1 .. 24 at
t = 30 to 100110011001100000000010 (CL198, exact SAT census); with its leading symbol made 1, sites 16, 20, 21, 22,
24 come free. GC1038 showed that 18 of those pins, sites 1 .. 15 and 17, 18, 19, already carry GC1037's backward
exclusion. Strip model of width W: sites 1 .. W, every row allowed at t = 0, a free input at site W + 1 at every
tick, the wall clamped to t mod 2 (phase 0), q imposed at the white ticks t = 0, 2, .., 86 and nothing else. This
is sound (every actual history restricted to 1 .. W is a strip history). Which cells at t = 30 are common to every
strip history, and what is the least W at which the 18 pins appear? A W <= 40 makes the cut's certificate bounded:
[strip W forces the 18 pins] -> [GC1037/1038 backward] -> [GC1036 guard] -> final 0.

Method. One CNF per W (literal Rule 30: y = l XOR (c OR r), three auxiliary clauses for the OR); a site i is forced
to v at t = 30 when the CNF with x(30, i) = 1 - v is UNSAT and with x(30, i) = v is SAT (kissat).

Record searched: `record_find.py strip "common.*pin|pins"` -> GC1036 .. GC1038 (RULE30-GPT.md), CL207's forward
test in rule30_cloud_train_block.py (first eight sites fixed, q's past dropped), rule30_cut45_origin_past.py,
rule30_cut45_pin_guard.py; `record_find.py width "cut45|length-45"` -> the same and rule30_cut45_past_support.py.
None runs the joint entry-and-exit strip at W = 24 .. 40.

PREDICTIONS (pushed before any run):
  SWP-C1 (control): at W = 87 (the full cone of the samples) all 24 sites are forced, to CL198's values.
  SWP-C2 (control): with the leading symbol 1, at W = 87, exactly sites 16, 20, 21, 22, 24 are free (CL198).
  SWP-C3 (control): q is admitted (SAT) at every width tested.
  Cloud's CL208 prediction (0.5): the least W is in 28 .. 36.
  SWP-P1 (Local's, blind, 0.55): some W <= 40 forces all 18 pins.
  SWP-P2 (Local's, blind, 0.4): at the least such W, site 23 (the pin GC1038 found dispensable) is not yet forced.
OUTCOME, 2026-10-10 18:16 BST (M5, one core, minutes): C1, C2, C3 PASS; Cloud's 28 .. 36 REFUTED; P1 HELD; P2 HELD
(degenerately, see below).
  - Forced cells at t = 30 (a dot is free), with the default range 24 .. 40 and an extension 19 .. 23 (same code):
    W = 19 .. 22: 100110011001100.000 (and free beyond 19): all 18 pins forced, site 16 free.
    W = 23: 10011001100110000000001, every site 1 .. 23 forced, 16 = 20 = 0 and 23 = 1 included.
    W = 24 .. 26: sites 1 .. 23 forced, site 24 free. W >= 27: all 24 forced, equal to the full cone (C1).
  - So the least width forcing the 18 pins is 19, the smallest strip that contains them. P2 holds only because
    site 23 lies outside a width-19 strip.
  - SW's own question settles the cut outright: w_min(f) = 24 (rule30_strip_width.wmin). The width-24 strip with a
    free site 25 excludes the whole length-45 word, and width 23 admits it. `cert` below rebuilds that CNF (hash
    a2ecb11d63068b92): kissat UNSAT, drat-trim VERIFIED, cake_lpr VERIFIED UNSAT, LRAT 0.47 MB. Width 23 is SAT
    (828a58f36f6bc5d2). Every actual history restricted to sites 1 .. 24 is such a strip history, so f is absent from
    L by a formally checked bounded certificate, with no SAT census and no hand lemma in the chain.
TABLE (registered 18:17 before its run; L605's offer): `table` gives w_min (rule30_strip_width.wmin) for every learned
cut, CUT's (cuts40_p0.txt) and SLC's (cuts40_sl.txt), each checked by cake_lpr at its w_min (phase 0, as SW).
  SWT-C1 (control): f's w_min is 24, as above.
  SWT-P1 (blind, 0.5): the median w_min/|f| over the learned cuts is at most 0.62 (SW's median for minimal words of
         length >= 25).
  SWT-P2 (blind, 0.6): every learned cut has w_min <= |f|.
"""
import os
import subprocess
import sys
import tempfile

KISSAT = os.environ.get('KISSAT', 'kissat')
Q = '00001000101000010101010101010101010001000010'
PINS30 = '100110011001100000000010'                        # CL198: sites 1 .. 24 at t = 30
FREE_LEAD1 = {16, 20, 21, 22, 24}
PIN18 = list(range(1, 16)) + [17, 18, 19]


def cnf(word, W, extra):
    T = 2 * (len(word) - 1)
    var, nv, cl = {}, [0], []

    def x(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    for t in range(T):
        for i in range(1, W + 1):
            y, c, r = x(t + 1, i), x(t, i), x(t, i + 1)            # site W + 1: a free input, a variable per tick
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:
                cl += ([[-y, -o], [y, o]] if t % 2 else [[-y, o], [y, -o]])   # wall t mod 2: 1 inverts, 0 copies
            else:
                l = x(t, i - 1)
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for s, b in enumerate(word):
        v = x(2 * s, 1)
        cl.append([v] if b == '1' else [-v])
    for (t, i), b in extra:
        cl.append([x(t, i)] if b else [-x(t, i)])
    return 'p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)


def sat(text):
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as f:
        f.write(text)
        name = f.name
    try:
        rc = subprocess.run([KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return rc == 10


def forced(word, W, sites, t0=30):
    """{site: forced value or None (free)} at t0, plus whether the word is admitted at all."""
    if not sat(cnf(word, W, [])):
        return None
    out = {}
    for i in sites:
        can = [sat(cnf(word, W, [((t0, i), v)])) for v in (0, 1)]
        out[i] = None if all(can) else (0 if can[0] else 1)
    return out


def main():
    wmin = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    wmax = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    sites = list(range(1, 25))
    full = forced(Q, 87, sites)
    c1 = full is not None and all(full[i] == int(PINS30[i - 1]) for i in sites)
    print('SWP-C1', 'PASS' if c1 else 'FAIL', ''.join('.' if full[i] is None else str(full[i]) for i in sites), flush=True)
    lead1 = forced('1' + Q[1:], 87, sites)
    c2 = lead1 is not None and {i for i in sites if lead1[i] is None} == FREE_LEAD1
    print('SWP-C2', 'PASS' if c2 else 'FAIL', 'free:', sorted(i for i in sites if lead1[i] is None), flush=True)
    least, c3 = None, True
    for W in range(wmin, wmax + 1):
        f = forced(Q, W, sites)
        if f is None:
            c3 = False
            print('W=%d: q NOT admitted' % W, flush=True)
            continue
        row = ''.join('.' if f[i] is None else str(f[i]) for i in sites)
        ok18 = all(f[i] == int(PINS30[i - 1]) for i in PIN18)
        wrong = [i for i in sites if f[i] is not None and f[i] != int(PINS30[i - 1])]
        assert not wrong, ('a forced value contradicts CL198', W, wrong)
        print('W=%d: forced at t = 30 (sites 1 .. 24) %s; 18 pins %s; site 23 %s' % (
            W, row, 'ALL' if ok18 else 'not all', f[23]), flush=True)
        if ok18 and least is None:
            least = W
    print('SWP-C3', 'PASS' if c3 else 'FAIL')
    print('least W in %d .. %d forcing the 18 pins: %s' % (wmin, wmax, least))


def cert(W, word):
    """kissat DRAT -> drat-trim -L -> cake_lpr (the lockf wrapper) on the width-W strip CNF of word."""
    import hashlib
    text = cnf(word, W, [])
    d = tempfile.mkdtemp()
    base = os.path.join(d, 'strip')
    open(base + '.cnf', 'w').write(text)
    k = subprocess.run([KISSAT, '-q', '-f', '--no-binary', base + '.cnf', base + '.drat'], capture_output=True)
    out = 'W=%d cnf %s kissat %s' % (W, hashlib.sha256(text.encode()).hexdigest()[:16], {10: 'SAT', 20: 'UNSAT'}.get(k.returncode))
    if k.returncode == 20:
        v = subprocess.run(['drat-trim', base + '.cnf', base + '.drat', '-L', base + '.lrat'], capture_output=True, text=True)
        c = subprocess.run([os.path.expanduser('~/np-build/cake_lpr/cake_lpr'), '--CML_HEAP_SIZE=2000', '--CML_STACK_SIZE=1000',
                            base + '.cnf', base + '.lrat'], capture_output=True, text=True)
        out += '; drat-trim %s; cake_lpr %s' % ('VERIFIED' if 's VERIFIED' in v.stdout else 'FAILED',
                                                'VERIFIED UNSAT' if 's VERIFIED UNSAT' in c.stdout else 'FAILED')
    for e in ('.cnf', '.drat', '.lrat'):
        if os.path.exists(base + e):
            os.unlink(base + e)
    os.rmdir(d)
    print(out)


def table():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    _a = sys.argv
    sys.argv = sys.argv[:1]
    import rule30_strip_width as sw                           # wmin: least width excluding a word
    import rule30_relaxed_records_k as rlk
    sys.argv = _a
    rows = []
    for stem in ('cuts40_p0', 'cuts40_sl'):
        for line in open(os.path.join(rlk.DIR, stem + '.txt')):
            w = line.split()[0]
            _, wm = sw.wmin(w)
            rows.append((stem, w, wm))
    c1 = dict((w, wm) for _, w, wm in rows).get('000010001010000101010101010101010100010000101') == 24
    print('SWT-C1', 'PASS' if c1 else 'FAIL', flush=True)
    for stem, w, wm in rows:
        cert(wm, w)                                            # prints the cake receipt at w_min
        print('  %s |f| = %d  w_min = %s  ratio %.2f' % (stem, len(w), wm, wm / len(w)), flush=True)
    ratios = sorted(wm / len(w) for _, w, wm in rows)
    med = ratios[len(ratios) // 2]
    print('SWT-P1', 'HELD' if med <= 0.62 else 'REFUTED', '(median w_min/|f| = %.3f over %d cuts)' % (med, len(rows)))
    print('SWT-P2', 'HELD' if all(wm <= len(w) for _, w, wm in rows) else 'REFUTED')


if __name__ == '__main__':
    if sys.argv[1:2] == ['table']:
        table()
        raise SystemExit(0)
    if sys.argv[1:2] == ['cert']:
        cert(int(sys.argv[2]), sys.argv[3])
    else:
        main()
