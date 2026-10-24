#!/usr/bin/env python3
"""Output-cell gate for the width-74 lower-bound submission d-lower-74 (Local, 2026-10-24, L889): nb_gate_lower.py revision 4 with the
witness list taken from d6_lower74_submission.py and its negative controls written for the width-74 witness (W, D read from it, not
fixed at 72 and 130), and `lst` boxes a one-element list as the front end does, RowBox[{"{", item, "}"}] without the inner
RowBox (read from this submission's first build; submission 15 never had a one-element list). Everything else is revision 4 unchanged. Revision 4's notes follow.

Output-cell gate for the lower-bound submission d-lower-64-72, revision 4 (Local, 2026-10-24, L874; GPT's GC1784: revision 3's
control helper truncated each cell before reading it, so its mutation controls tested empty cells; and a change to only ONE displayed
copy of a count in cells 5 or 11 passed the substring test. Revision 4 requires EVERY displayed copy to agree and its controls read
before they write. Revision 3 notes: (Local, 2026-10-24, L871; GPT's GC1782: revision 2's
axiom extractor dropped identifiers with underscores or digits, so an extra axiom could pass, and its substring checks were
presence tests, not a full output check).

Revision 3 compares the cells EXACTLY wherever the output is determined by the module, and binds the rest to the kit checker's
JSON for the same module:
  - cells 1, 2 (witness bit lengths, first even white times), 4 (True), 6 (the head), 7 (the five headline statements), 8 (the
    five axiom lists), 9 (the width-72 survival and death statements), 10 (the two bridge lemmas): the full InputForm text must
    EQUAL a string built here from the widths, the bounds, the witnesses and the checker's per-headline axiom lists (the box
    format, RowBox lists of escaped strings, was read from the first build's cells; the content is computed, not copied);
  - cell 3 (the orbit plot): a GraphicsBox holding a RasterBox;
  - cell 5 (the environment summary): its constant count, definition count and theorem count equal the checker's `declared`
    list (count and kinds);
  - cell 11 (KernelCheck): `Success`, and "The kernel accepts all N declarations" with N equal to the checker's `replay.constants`.
usage: python3 nb_gate_lower74.py CELLS_DIR CHECK_JSON      (exit 0 only on PASS)
       python3 nb_gate_lower74.py --controls CELLS_DIR CHECK_JSON   (negative controls on copies of the cells)"""
import json, os, re, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tests', 'probes', 'wolfram'))
import d6_lower74_submission as G

WIT = [(W, D, s) for W, D, s in G.WITNESSES]
HEAD = ['Rule30Submission.width%d_lower' % W for W, _, _ in WIT]


def esc(s):
    return '"\\"' + s + '\\""'


def lst(items):
    if len(items) == 1:                       # a one-element list is boxed without the inner RowBox (read from this submission's build 1)
        return 'RowBox[{"{", ' + items[0] + ', "}"}]'
    return 'RowBox[{"{", RowBox[{' + ', ",", '.join(items) + '}], "}"}]'


def expected(check):
    ax = {h['name']: sorted(h['axioms']) for h in check['headlines']}
    stmt = ['∃ x, (∀ (k : ℕ), %d < k → x k = false) ∧ ∀ t < %d, t %% 2 = 0 → zrow x t 1 = true' % (W, D) for W, D, _ in WIT]
    W72, D72 = WIT[-1][0], WIT[-1][1]
    return {
        1: 'BoxData[' + lst(['"%d"' % s.bit_length() for _, _, s in WIT]) + ']',
        2: 'BoxData[' + lst(['"%d"' % D for _, D, _ in WIT]) + ']',
        4: 'BoxData["True"]',
        6: 'BoxData["LeanEnvironment"]',
        7: 'BoxData[' + lst([esc(x) for x in stmt]) + ']',
        8: 'BoxData[' + lst([lst([esc(a) for a in ax[h]]) for h in HEAD]) + ']',
        9: 'BoxData[' + lst([esc('∀ t < %d, t %% 2 = 0 → zrow (toFun w%d) t 1 = true' % (D72, W72)), esc('zrow (toFun w%d) %d 1 = false' % (W72, D72))]) + ']',
        10: 'BoxData[' + lst([esc('∀ (r t : ℕ), zrow (toFun r) t 1 = (prun r t).testBit 0'), esc('∀ {r W : ℕ}, r < 2 ^ W → ∀ (k : ℕ), W < k → toFun r k = false')]) + ']',
    }


def gate(cells, check):
    probs, rep = [], {}
    if check.get('verdict') != 'pass' or check.get('newAxioms') != [] or not check.get('replay', {}).get('ok'):
        probs.append('the checker JSON is not a pass with no new axioms and a good replay')
    if sorted(h['name'] for h in check.get('headlines', [])) != sorted(HEAD) or not all(h.get('ok') and h.get('found') and h.get('typeMatches') for h in check['headlines']):
        probs.append('the checker JSON headlines are not exactly the five, all found, ok and type-matching')
    allowed = {'propext', 'Quot.sound', 'Classical.choice'}
    if any(set(h['axioms']) - allowed for h in check.get('headlines', [])):
        probs.append('a headline axiom outside the standard three in the checker JSON')
    n = int(open(os.path.join(cells, 'count.txt')).read().strip())
    if n != 11: probs.append('cell count %d, expected 11' % n)
    txt = {}
    for i in range(1, 12):
        p = os.path.join(cells, 'cell-%02d.txt' % i)
        txt[i] = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if txt[i] is None: probs.append('cell %d missing' % i)
    for i, want in expected(check).items():
        ok = txt.get(i) == want; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('cell %d is not the expected text' % i)
    t3 = txt.get(3) or ''
    rep[3] = 'graphics' if ('GraphicsBox' in t3 and 'RasterBox' in t3) else 'MISSING'
    if rep[3] != 'graphics': probs.append('cell 3 is not a raster plot')
    dec = check.get('declared', []); nd = len(dec)
    nk = {k: sum(1 for x in dec if x['kind'] == k) for k in ('def', 'theorem')}
    t5 = txt.get(5) or ''
    totals = re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t5)                       # every displayed total (collapsed and expanded views)
    kinds = re.findall(r'"(\d+)", "\\" \\"", StyleBox\["\\"(def|theorem)\\""', t5)   # every displayed per-kind count
    ok5 = ('LeanEnvironment' in t5 and totals and all(int(x) == nd for x in totals)
           and {k for _, k in kinds} == {'def', 'theorem'} and all(int(c) == nk[k] for c, k in kinds))
    rep[5] = 'bound to the checker, every copy (%d constants: %d def, %d theorem; %d total copies, %d kind copies)' % (nd, nk['def'], nk['theorem'], len(totals), len(kinds)) if ok5 else 'MISMATCH'
    if not ok5: probs.append('cell 5 summary counts differ from the checker JSON in some displayed copy')
    t11 = txt.get(11) or ''
    rc = check.get('replay', {}).get('constants')
    msgs = re.findall(r'accepts all (\d+) declarations', t11)
    items = re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t11)
    params = re.findall(r'"MessageParameters" -> \{(\d+),', t11)
    decls = re.findall(r'"Declarations" -> (\d+)', t11)
    every = msgs + items + params + decls
    ok11 = ('TagBox["Success", "SummaryHead"]' in t11 and 'Failure' not in t11 and msgs and params and decls
            and all(int(x) == rc for x in every))
    rep[11] = 'Success, %d declarations (= checker replay) in every one of %d displayed copies' % (rc, len(every)) if ok11 else 'MISMATCH'
    if not ok11: probs.append('cell 11 is not Success with the checker replay count')
    return ('PASS' if not probs else 'FAIL'), {'cells': rep, 'problems': probs}


def controls(cells, check):
    res = {}
    v, _ = gate(cells, check); res['real_cells_pass'] = v == 'PASS'
    def mutated(i, f):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(cells, t + '/c'); p = t + '/c/cell-%02d.txt' % i
            before = open(p, encoding='utf-8').read()            # read FIRST (revision 3 opened for writing first and truncated the cell)
            after = f(before)
            assert after and after != before, 'control %d did not change the cell' % i
            open(p, 'w', encoding='utf-8').write(after)
            return gate(t + '/c', check)[0]
    # GPT's counterexample: an extra axiom with an underscore and digit in one list
    res['extra_axiom_fails'] = mutated(8, lambda s: s.replace('"\\"propext\\""', '"\\"propext\\"", ",", "\\"unexpected_axiom1\\""', 1)) == 'FAIL'
    Wl, Dl = WIT[-1][0], WIT[-1][1]
    res['changed_bound_fails'] = mutated(7, lambda s: s.replace('t < %d' % Dl, 't < %d' % (Dl - 2), 1)) == 'FAIL'
    res['changed_width_fails'] = mutated(7, lambda s: s.replace('%d < k' % Wl, '%d < k' % (Wl - 1), 1)) == 'FAIL'
    res['wrong_declaration_count_fails'] = mutated(11, lambda s: s.replace('accepts all %d' % check['replay']['constants'], 'accepts all %d' % (check['replay']['constants'] - 1))) == 'FAIL'   # every copy
    res['wrong_summary_count_fails'] = mutated(5, lambda s: s.replace('TagBox["%d", "SummaryItem"]' % len(check['declared']), 'TagBox["%d", "SummaryItem"]' % (len(check['declared']) + 1))) == 'FAIL'
    res['changed_death_list_fails'] = mutated(2, lambda s: s.replace('"%d"' % Dl, '"%d"' % (Dl - 2))) == 'FAIL'
    nd = len(check['declared']); rc = check['replay']['constants']
    res['first_copy_only_cell5_total_fails'] = mutated(5, lambda s: s.replace('TagBox["%d", "SummaryItem"]' % nd, 'TagBox["%d", "SummaryItem"]' % (nd + 1), 1)) == 'FAIL'
    res['first_copy_only_cell11_message_fails'] = mutated(11, lambda s: s.replace('accepts all %d declarations' % rc, 'accepts all %d declarations' % (rc - 1), 1)) == 'FAIL'
    res['cell11_declarations_field_only_fails'] = mutated(11, lambda s: s.replace('"Declarations" -> %d' % rc, '"Declarations" -> %d' % (rc + 7), 1)) == 'FAIL'
    bad = dict(check); bad['headlines'] = [dict(h, axioms=h['axioms'] + ['sorryAx']) if i == 0 else h for i, h in enumerate(check['headlines'])]
    res['checker_json_with_bad_axiom_fails'] = gate(cells, bad)[0] == 'FAIL'
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('GATE CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == '--controls':
        sys.exit(0 if controls(a[1], json.load(open(a[2]))) else 1)
    if len(a) == 2:
        v, r = gate(a[0], json.load(open(a[1]))); print(json.dumps({'verdict': v, **r}, indent=1, ensure_ascii=False)); sys.exit(0 if v == 'PASS' else 1)
    print(__doc__); sys.exit(2)
