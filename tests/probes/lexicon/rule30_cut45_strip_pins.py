#!/usr/bin/env python3
"""rule30_cut45_strip_pins.py: SWP, the least strip width that forces the length-45 cut's common pins (Cloud's CL208).

RUN-ON:     cpu (Python 3, kissat 4.0.4 as KISSAT); one core, minutes
COMMAND:    python3 tests/probes/lexicon/rule30_cut45_strip_pins.py [WMIN=24] [WMAX=40]

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


if __name__ == '__main__':
    main()
