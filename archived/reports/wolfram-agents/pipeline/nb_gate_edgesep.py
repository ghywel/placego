#!/usr/bin/env python3
"""Output-cell gate for the edge-sep submission (Local, 2026-10-24, L886; Cloud's CL622 module dd1e9b87, GPT's GC1793 PASS).
Every one of the nine output cells is checked:
  - cells 1 and 2 (the Wolfram Language computations): the full InputForm must EQUAL the box text of the values recomputed by
    edge_sep_expected.py, separate code from the notebook and from Cloud's expected_numbers.py (cell 1 by the essay's list
    semantics; cell 2 shares the essay's lane METHOD, so it is a cross-language check, not an independent mechanism; Cloud's scalar
    expected_numbers.py is that, GC1794);
  - cell 3: exactly BoxData["True"] (the kit directory exists);
  - cell 4 (the LeanEnvironment summary): every displayed total equals the checker's declared theorems plus its source definitions,
    and every displayed per-kind count equals the checker's (theorems 259, definitions 20 here). The summary omits the compiler's
    generated `match_` auxiliaries, which the checker's `declared` list includes (18 here); they are excluded by name;
  - cell 5: EQUAL to the three headline statements built from the edge pairs and deadlines, plus the edge predicate's type;
  - cell 6: EQUAL to attained_8 built from its pair and deadline, separationB and centers_spec as printed (their text is pinned
    here from build 1, for GPT's actual-output read; not computed), and the block theorem built from (m, d, e, block) = (14, 11, 12, 0);
  - cell 7: EQUAL to the checker's sep_8 axiom list, sorted as printed;
  - cell 8 (the call graph): a network graph whose first vertex is Rule30Submission.sep_8;
  - cell 9 (KernelCheck): Success, no Failure, and every displayed declaration count equal to the checker's replay count (583).
The checker JSON must be a pass: claim partial, no new axioms, replay ok, exactly the eight headlines found, ok and type-matching,
on the standard axioms only.
usage: python3 nb_gate_edgesep.py CELLS_DIR CHECK_JSON          (exit 0 only on PASS)
       python3 nb_gate_edgesep.py --controls CELLS_DIR CHECK_JSON  (negative controls on copies of the cells; each reads before writing)"""
import json, os, re, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge_sep_expected as E

HEAD = ['Rule30Submission.' + n for n in ('sep_8', 'sep_13', 'sep_14', 'attained_8', 'attained_13', 'attained_14', 'separationB', 'centers_spec')]
STD = {'propext', 'Quot.sound', 'Classical.choice'}
PAIRS = [(-2, -1, 8), (-4, -3, 13), (-3, -2, 14)]
SEPARATION_B = ('∀ (m d e K : ℕ),\n  d ≤ 2 * m →\n    e ≤ 2 * m →\n      2 ^ (m + 1) ≤ blk * K →\n        BlocksDisjoint m d e K →\n'
                '          ∀ (x y : ℤ → Bool), HasLeftEdge x (↑d - ↑m) → HasLeftEdge y (↑e - ↑m) → ∃ t ≤ m, evol x t 0 ≠ evol y t 0')
CENTERS_SPEC = ('∀ (m d : ℕ),\n  d ≤ 2 * m →\n    ∀ (t ℓ : ℕ),\n      t ≤ m →\n        ℓ < 2 ^ (2 * m - d) →\n'
                '          ((centers m m (initWords m d (2 * m - d))).getD t 0).testBit ℓ =\n            evol (cfg (↑d - ↑m) (2 * m + 1 - d) (laneCode ℓ)) t 0')


def num(n):
    return 'RowBox[{"-", "%d"}]' % -n if n < 0 else '"%d"' % n


def box(x):
    if isinstance(x, list):
        return 'RowBox[{"{", RowBox[{' + ', ",", '.join(box(y) for y in x) + '}], "}"}]'
    return num(x)


def lst(items):
    return 'RowBox[{"{", RowBox[{' + ', ",", '.join(items) + '}], "}"}]'


def esc(s):
    return '"\\"' + s.replace('\n', '\\\\n') + '\\""'


def edge(n):
    return '(%d)' % n if n < 0 else '%d' % n


def expected(check):
    sep = ['∀ (x y : ℤ → Bool), HasLeftEdge x %s → HasLeftEdge y %s → ∃ t ≤ %d, evol x t 0 ≠ evol y t 0' % (edge(a), edge(b), m) for a, b, m in PAIRS]
    a, b, m = PAIRS[0]
    att = '∃ x y, HasLeftEdge x %s ∧ HasLeftEdge y %s ∧ (∀ t < %d, evol x t 0 = evol y t 0) ∧ evol x %d 0 ≠ evol y %d 0' % (edge(a), edge(b), m, m, m)
    mm, dd, ee, k = 14, 14 + PAIRS[2][0], 14 + PAIRS[2][1], 0
    blkthm = '(partSet %d %d %d).land (partSet %d %d %d) = 0' % (mm, dd, k, mm, ee, k)
    ax = sorted(next(h['axioms'] for h in check['headlines'] if h['name'] == HEAD[0]))
    return {1: 'BoxData[' + box(E.cell1()) + ']', 2: 'BoxData[' + box(E.cell2()) + ']', 3: 'BoxData["True"]',
            5: 'BoxData[' + lst([esc(x) for x in sep] + [esc('(ℤ → Bool) → ℤ → Prop')]) + ']',
            6: 'BoxData[' + lst([esc(att), esc(SEPARATION_B), esc(CENTERS_SPEC), esc(blkthm)]) + ']',
            7: 'BoxData[' + lst(['"\\"%s\\""' % x for x in ax]) + ']'}


def gate(cells, check):
    probs, rep = [], {}
    if not (check.get('verdict') == 'pass' and check.get('claim') == 'partial' and check.get('newAxioms') == [] and check.get('replay', {}).get('ok') and check.get('reasons') == []):
        probs.append('the checker JSON is not a clean partial pass')
    hs = check.get('headlines', [])
    if sorted(h['name'] for h in hs) != sorted(HEAD) or not all(h.get('found') and h.get('ok') and h.get('typeMatches') for h in hs) or any(set(h['axioms']) - STD for h in hs):
        probs.append('the checker headlines are not exactly the eight, all found, ok, type-matching, on the standard axioms')
    n = int(open(os.path.join(cells, 'count.txt')).read().strip())
    if n != 9: probs.append('cell count %d, expected 9' % n)
    txt = {}
    for i in range(1, 10):
        p = os.path.join(cells, 'cell-%02d.txt' % i)
        txt[i] = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if txt[i] is None: probs.append('cell %d missing' % i)
    try:
        exp = expected(check)
    except Exception as e:
        exp = {}; probs.append('expected texts could not be built: %r' % e)
    for i, want in exp.items():
        ok = txt.get(i) == want; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('cell %d is not the expected text' % i)
    dec = check.get('declared', [])
    gen = [x for x in dec if x['name'].rsplit('.', 1)[-1].startswith('match_')]
    nk = {'theorem': sum(1 for x in dec if x['kind'] == 'theorem'), 'def': sum(1 for x in dec if x['kind'] == 'def') - sum(1 for x in gen if x['kind'] == 'def')}
    other = [x for x in dec if x['kind'] not in ('def', 'theorem')]
    t4 = txt.get(4) or ''
    totals = re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t4)
    kinds = re.findall(r'"(\d+)", "\\" \\"", StyleBox\["\\"(def|theorem)\\""', t4)
    ok4 = ('TagBox["LeanEnvironment", "SummaryHead"]' in t4 and not other and totals and all(int(x) == nk['theorem'] + nk['def'] for x in totals)
           and {k for _, k in kinds} == {'def', 'theorem'} and all(int(c) == nk[k] for c, k in kinds))
    rep[4] = ('bound to the checker, every copy (%d theorems, %d source definitions; %d generated match_ auxiliaries excluded; %d total copies, %d kind copies)'
              % (nk['theorem'], nk['def'], len(gen), len(totals), len(kinds))) if ok4 else 'MISMATCH'
    if not ok4: probs.append('cell 4 summary counts differ from the checker in some displayed copy')
    t8 = txt.get(8) or ''
    ok8 = t8.startswith('BoxData[GraphicsBox[NamespaceBox["NetworkGraphics"') and 'HoldComplete[Graph[{"Rule30Submission.sep_8", ' in t8
    rep[8] = 'a network graph rooted at sep_8' if ok8 else 'MISMATCH'
    if not ok8: probs.append('cell 8 is not the call graph of sep_8')
    t9 = txt.get(9) or ''
    rc = check.get('replay', {}).get('constants')
    every = (re.findall(r'accepts all (\d+) declarations', t9) + re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t9)
             + re.findall(r'"MessageParameters" -> \{(\d+),', t9) + re.findall(r'"Declarations" -> (\d+)', t9))
    ok9 = ('TagBox["Success", "SummaryHead"]' in t9 and 'Failure' not in t9 and re.findall(r'accepts all (\d+) declarations', t9)
           and re.findall(r'"Declarations" -> (\d+)', t9) and all(int(x) == rc for x in every))
    rep[9] = 'Success, %s declarations (= checker replay) in every one of %d displayed copies' % (rc, len(every)) if ok9 else 'MISMATCH'
    if not ok9: probs.append('cell 9 is not Success with the checker replay count')
    return ('PASS' if not probs else 'FAIL'), {'cells': rep, 'problems': probs}


def controls(cells, check):
    res = {}
    v, r = gate(cells, check); res['real_cells_pass'] = v == 'PASS'

    def mutated(i, f):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(cells, t + '/c'); p = t + '/c/cell-%02d.txt' % i
            before = open(p, encoding='utf-8').read(); after = f(before)
            assert after and after != before, 'control on cell %d did not change it' % i
            open(p, 'w', encoding='utf-8').write(after)
            return gate(t + '/c', check)[0]
    res['cell1_one_center_bit_changed_fails'] = mutated(1, lambda s: s.replace('"1", ",", "1"}], "}"}], ",", "8"', '"1", ",", "0"}], "}"}], ",", "8"', 1)) == 'FAIL'
    res['cell2_saturation_changed_fails'] = mutated(2, lambda s: s.replace('"8", ",", "8", ",", "8"', '"8", ",", "8", ",", "9"', 1)) == 'FAIL'
    res['cell3_false_fails'] = mutated(3, lambda s: s.replace('True', 'False')) == 'FAIL'
    res['cell4_def_count_first_copy_fails'] = mutated(4, lambda s: s.replace('"20", "\\" \\"", StyleBox["\\"def\\""', '"38", "\\" \\"", StyleBox["\\"def\\""', 1)) == 'FAIL'
    res['cell4_total_first_copy_fails'] = mutated(4, lambda s: s.replace('TagBox["279", "SummaryItem"]', 'TagBox["297", "SummaryItem"]', 1)) == 'FAIL'
    res['cell5_deadline_changed_fails'] = mutated(5, lambda s: s.replace('∃ t ≤ 13', '∃ t ≤ 12', 1)) == 'FAIL'
    res['cell5_edge_changed_fails'] = mutated(5, lambda s: s.replace('HasLeftEdge y (-1)', 'HasLeftEdge y (-2)', 1)) == 'FAIL'
    res['cell6_block_index_changed_fails'] = mutated(6, lambda s: s.replace('(partSet 14 12 0)', '(partSet 14 12 1)', 1)) == 'FAIL'
    res['cell6_separation_text_changed_fails'] = mutated(6, lambda s: s.replace('BlocksDisjoint m d e K', 'BlocksDisjoint m e d K', 1)) == 'FAIL'
    res['cell7_extra_axiom_fails'] = mutated(7, lambda s: s.replace('"\\"propext\\""', '"\\"propext\\"", ",", "\\"sorryAx\\""', 1)) == 'FAIL'
    res['cell8_wrong_root_fails'] = mutated(8, lambda s: s.replace('Graph[{"Rule30Submission.sep_8", ', 'Graph[{"Rule30Submission.sep_13", ', 1)) == 'FAIL'
    res['cell9_first_message_copy_fails'] = mutated(9, lambda s: s.replace('accepts all 583 declarations', 'accepts all 582 declarations', 1)) == 'FAIL'
    res['cell9_declarations_field_fails'] = mutated(9, lambda s: s.replace('"Declarations" -> 583', '"Declarations" -> 590', 1)) == 'FAIL'
    bad = dict(check); bad['headlines'] = [dict(h, axioms=h['axioms'] + ['sorryAx']) if k == 0 else h for k, h in enumerate(check['headlines'])]
    res['checker_json_bad_axiom_fails'] = gate(cells, bad)[0] == 'FAIL'
    bad2 = dict(check); bad2['headlines'] = check['headlines'][:-1]
    res['checker_json_missing_headline_fails'] = gate(cells, bad2)[0] == 'FAIL'
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('GATE CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == '--controls':
        sys.exit(0 if controls(a[1], json.load(open(a[2]))) else 1)
    if len(a) == 2:
        v, r = gate(a[0], json.load(open(a[1]))); print(json.dumps({'verdict': v, **r}, indent=1, ensure_ascii=False)); sys.exit(0 if v == 'PASS' else 1)
    print(__doc__); sys.exit(2)
