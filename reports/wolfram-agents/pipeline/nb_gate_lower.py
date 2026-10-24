#!/usr/bin/env python3
"""Output-cell gate for the lower-bound submission d-lower-64-72 (Local, 2026-10-24, L868). There is no earlier build of this
notebook to compare against, so the gate checks each output cell in full against semantic predicates written BEFORE the
build (README.md of the submission): exact strings that must occur, per cell, in the cell's full InputForm text.
usage: python3 nb_gate_lower.py CELLS_DIR      (the folder read_nb_full.wl wrote)
Revision 2 (after the first run): the axiom-name pattern corrected; revision 1 failed the axioms cell on its own regex, not on content."""
import json, os, re, sys

WIDTHS = [(64, 116), (66, 120), (68, 122), (70, 124), (72, 130)]
EXPECT = [   # (label, list of needles that must ALL occur in that output cell)
    ('bit lengths', ['RowBox[{"{", RowBox[{"64", ",", "65", ",", "67", ",", "70", ",", "72"}], "}"}]']),
    ('first even white times', ['RowBox[{"{", RowBox[{"116", ",", "120", ",", "122", ",", "124", ",", "130"}], "}"}]']),
    ('orbit plot', ['GraphicsBox']),
    ('kit directory', ['BoxData["True"]']),
    ('environment (assignment)', ['LeanEnvironment']),
    ('environment head', ['BoxData["LeanEnvironment"]']),
    ('headline statements', ['%d < k' % W for W, _ in WIDTHS] + ['t < %d' % D for _, D in WIDTHS]),
    ('axioms', ['propext']),
    ('w72 survival and death', ['t < 130', 'zrow (toFun w72) 130 1 = false']),
    ('bridge lemmas', ['zrow (toFun r) t 1 = (prun r t).testBit 0', 'toFun r k = false']),
    ('kernel check', ['TagBox["Success", "SummaryHead"]', 'The kernel accepts all']),
]
ALLOWED_AXIOMS = {'propext', 'Quot.sound', 'Classical.choice'}


def main(cells):
    n = int(open(os.path.join(cells, 'count.txt')).read().strip())
    out = {'count': n, 'expected_count': len(EXPECT), 'cells': {}, 'problems': []}
    if n != len(EXPECT):
        out['problems'].append('cell count %d, expected %d' % (n, len(EXPECT)))
    for i, (label, needles) in enumerate(EXPECT, 1):
        p = os.path.join(cells, 'cell-%02d.txt' % i)
        if not os.path.exists(p):
            out['problems'].append('cell %d missing' % i); continue
        t = open(p, encoding='utf-8').read()
        miss = [x for x in needles if x not in t]
        out['cells'][i] = {'label': label, 'bytes': len(t.encode()), 'missing': miss}
        if miss: out['problems'].append('cell %d (%s) lacks %r' % (i, label, miss[:3]))
        if label == 'axioms':
            names = set(re.findall(r'\\"([A-Za-z.]+)\\"', t))   # revision 2: one backslash before each quote (revision 1 expected two and found none)
            bad = {x for x in names if x not in ALLOWED_AXIOMS}
            out['cells'][i]['axiom_names'] = sorted(names)
            if bad or not names: out['problems'].append('axioms cell names %r' % sorted(names))
    out['verdict'] = 'PASS' if not out['problems'] else 'FAIL'
    print(json.dumps(out, indent=1)); return 0 if out['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
