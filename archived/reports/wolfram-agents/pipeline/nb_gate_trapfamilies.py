#!/usr/bin/env python3
"""Output-cell gate for the trap-families submission (Local, 2026-10-25, L933; made ready while GPT reads L931/L932): nb_gate_trappair.py
(ac52375a, PASS at first contact on the trap-pair build's real cells, L930) with the families' bindings: the families essay's ten code
cells (a new cell 3, the four-member family illustration, bound to the families expected_numbers.py), the eight headlines and their
predicted TypeForms, the call-graph route of CQ01_prefix31, and CHECK_SHA256 left UNSET (fail-closed) until the families Check writes its
check.json; it is then pinned in a one-line change, disclosed. The trap-pair gate's method is unchanged: GC1813's ordered fail-closed
schema, a full synthetic packet (here with a synthetic checker JSON built from the module's own declarations) and one exact-diagnostic
fixture per obligation. Box formats are the ones read from the trap-pair build; the eight statement texts are PREDICTIONS until read.

Order (the first failing stage stops the gate with its diagnostic; later stages are not evaluated):
  S1 bytes: CHECK_SHA256 is set and the checker JSON's SHA-256 equals it; expected_numbers.py's equals EXPECTED_SHA256;
  S2 the checker JSON: strict parse; types and keys; a clean partial pass with an integer replay count; exactly the eight headlines,
     each found, ok and type-matching, on the standard three axioms only; `declared` a list of distinct {name, kind}, def or theorem;
  S3 the packet: count.txt is exactly the integer 10; cell-01 .. cell-10 exist; the cell-*.txt inventory is exactly those ten;
  S4 the cells, one obligation each:
     O1, O2 as in trap-pair (the seeds' visible columns and R31 at time 4; the entry rows and the ether columns);
     O3 (families): EQUAL to [the visible columns of the four first-family members, those of the four second-family members], twenty
        white steps each, values from expected_numbers.py;
     O4 (moves), O5 (True): as trap-pair's O3, O4;
     O6 (the LeanEnvironment summary): the displayed (Name, Kind) pairs, with no repeats, equal the checker's declared list minus the
        generated match_ auxiliaries; every displayed total and per-kind count, in every copy, equals that list's;
     O7 (the eight headline statements): EQUAL to TYPES, in the essay's order;
     O8: EQUAL to the checker's CQ01_prefix31 axiom list, sorted as printed;
     O9 (the call graph): a network graph whose first vertex is Rule30Submission.CQ01_prefix31 and whose vertices include the kit's
        absorption lemma and u_prefix31;
     O10 (KernelCheck): Success, no Failure, and every displayed declaration count equal to the checker's replay count.
usage: python3 nb_gate_trapfamilies.py CELLS_DIR CHECK_JSON            (exit 0 only on PASS)
       python3 nb_gate_trapfamilies.py --controls [CELLS_DIR CHECK_JSON] (the synthetic packet and its fixtures; with real cells, those too)"""
import contextlib, hashlib, io, json, os, re, shutil, sys, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(HERE, '..', 'submissions', 'trap-families')
CHECK_SHA256 = 'ef140fcd64fc5530a841ca4601262c4c44196ebcbfa0efe569dca18c9d5d4263'   # the families Check PASS (L935), pinned in one disclosed line
EXPECTED_SHA256 = 'ad875335e3cbb72db8b40a1103964d6561e2812eff23826173f292b923248efa'
HEAD = ['Rule30Submission.' + n for n in ('CQ01_prefix31', 'CQ01_prefix495', 'Psi_prefix31', 'Psi_prefix495', 'Psi_eq', 'CQ01_fam', 'fam_injective',
                                       'not_move_equivalent')]
STD = {'propext', 'Quot.sound', 'Classical.choice'}
TYPES = ['∀ (R : ℕ → Bool), AgreesPrefix 28 R R31 → ¬FinSupp (Psi R)', '∀ (R : ℕ → Bool), AgreesPrefix 24 R R495 → ¬FinSupp (Psi R)',
         '∀ (R : ℕ → Bool), AgreesPrefix 28 R R31 → Psi R = Psi R31', '∀ (R : ℕ → Bool), AgreesPrefix 24 R R495 → Psi R = Psi R495',
         'Psi R31 = Psi R495', '∀ (n : ℕ), FinSupp (fam n) ∧ ¬FinSupp (Psi (fam n)) ∧ Psi (fam n) = Psi R31', 'Function.Injective fam',
         '¬Relation.EqvGen Move cells31.reverse cells495.reverse']
ROUTE = ['Ruliology.CellularAutomata.Rule30PeriodTwoSideways.not_finSupp_Psi_of_eventuallyPeriodic', 'Rule30Submission.u_prefix31']
NCELLS = 10


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_expected():
    p = os.path.join(SUB, 'expected_numbers.py')
    spec = importlib.util.spec_from_file_location('trap_families_expected', p); m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def strict_json(b):
    def no_const(x): raise ValueError('non-finite constant %s' % x)
    def no_dup(pairs):
        keys = [k for k, _ in pairs]
        if len(keys) != len(set(keys)): raise ValueError('duplicate key')
        return dict(pairs)
    return json.loads(b.decode('utf-8'), parse_constant=no_const, object_pairs_hook=no_dup)


def lst(items):
    if len(items) == 1:                       # a one-element list is boxed without the inner RowBox (read from submission 16's build)
        return 'RowBox[{"{", ' + items[0] + ', "}"}]'
    return 'RowBox[{"{", RowBox[{' + ', ",", '.join(items) + '}], "}"}]'


def box(x):
    return lst([box(y) for y in x]) if isinstance(x, list) else '"%d"' % x


def esc(s):
    return '"\\"' + s.replace('\n', '\\\\n') + '\\""'


def expected(check, E):
    ax = sorted(next(h['axioms'] for h in check['headlines'] if h['name'] == HEAD[0]))
    ether6 = [E.ETHER[(3 + p) % 7][12 % 4] for p in range(1, 7)]
    return {1: 'BoxData[' + box([E.u31, E.u495, E.r31[4][:9]]) + ']',
            2: 'BoxData[' + box([E.r31[9][:19], E.r495[5][:19], ether6]) + ']',
            3: 'BoxData[' + box([E.famu31, E.famu495]) + ']',
            4: 'BoxData[' + box([E.chain, E.root([1, 1, 1, 1, 1]), E.root([1, 1, 1, 1, 0, 1, 1, 1, 1][::-1])]) + ']',
            5: 'BoxData["True"]',
            7: 'BoxData[' + lst([esc(x) for x in TYPES]) + ']',
            8: 'BoxData[' + lst(['"\\"%s\\""' % x for x in ax]) + ']'}


def summary_list(check):
    return sorted((x['name'], x['kind']) for x in check['declared'] if not x['name'].rsplit('.', 1)[-1].startswith('match_'))


def check_schema(check):
    """S2: returns the first problem or None."""
    if not isinstance(check, dict): return 'S2: the checker JSON is not an object'
    need = {'verdict': str, 'claim': str, 'newAxioms': list, 'reasons': list, 'replay': dict, 'headlines': list, 'declared': list}
    for k, t in need.items():
        if not isinstance(check.get(k), t): return 'S2: key %s missing or not %s' % (k, t.__name__)
    rc = check['replay'].get('constants')
    if not (check['verdict'] == 'pass' and check['claim'] == 'partial' and check['newAxioms'] == [] and check['reasons'] == []
            and check['replay'].get('ok') is True and type(rc) is int and rc > 0):
        return 'S2: the checker JSON is not a clean partial pass with an integer replay count'
    hs = check['headlines']
    if not all(isinstance(h, dict) and isinstance(h.get('name'), str) and isinstance(h.get('axioms'), list) for h in hs):
        return 'S2: a headline is malformed'
    if sorted(h['name'] for h in hs) != sorted(HEAD) or not all(h.get('found') is True and h.get('ok') is True and h.get('typeMatches') is True for h in hs):
        return 'S2: the headlines are not exactly the eight, each found, ok and type-matching'
    if any(not all(isinstance(a, str) for a in h['axioms']) or set(h['axioms']) - STD for h in hs):
        return 'S2: a headline axiom outside the standard three'
    if not all(isinstance(x, dict) and isinstance(x.get('name'), str) and x.get('kind') in ('def', 'theorem') for x in check['declared']):
        return 'S2: a declared entry is malformed or of another kind'
    if len({x['name'] for x in check['declared']}) != len(check['declared']):
        return 'S2: a declared name repeats'
    return None


def summary_copies(t):
    """The (Name, Kind) pairs of a LeanEnvironment summary (the box holds the constants association once; edge-sep's real cell 4 gave
    its 279 pairs, equal to its checker list minus match_)."""
    return re.findall(r'"Name" -> "([^"]+)", "Kind" -> "(\w+)"', t)


def graph_vertices(t):
    m = re.search(r'HoldComplete\[Graph\[\{((?:"[^"]*"(?:, )?)+)\}', t)
    return re.findall(r'"([^"]*)"', m.group(1)) if m else []


def gate(cells, check_bytes, pin=CHECK_SHA256, expected_path=None):
    """Returns (verdict, report). The first failing stage stops the gate; report['problems'][0] is its exact diagnostic."""
    rep = {}
    def fail(msg): return 'FAIL', {'cells': rep, 'problems': [msg]}
    # S1 bytes
    if pin == 'UNSET': return fail('S1: no checker JSON is pinned yet')
    if pin is not None and sha(check_bytes) != pin: return fail('S1: the checker JSON is not the committed check.json')
    ep = expected_path or os.path.join(SUB, 'expected_numbers.py')
    if sha(open(ep, 'rb').read()) != EXPECTED_SHA256: return fail('S1: expected_numbers.py is not the pinned bytes')
    # S2 checker
    try:
        check = strict_json(check_bytes)
    except Exception as e:
        return fail('S2: the checker JSON does not parse strictly (%s)' % e)
    why = check_schema(check)
    if why: return fail(why)
    # S3 packet
    try:
        n_txt = open(os.path.join(cells, 'count.txt')).read()
    except OSError:
        return fail('S3: count.txt missing')
    if not re.fullmatch(r'\d+\n?', n_txt) or int(n_txt) != NCELLS: return fail('S3: the cell count is not exactly %d' % NCELLS)
    txt = {}
    for i in range(1, NCELLS + 1):
        p = os.path.join(cells, 'cell-%02d.txt' % i)
        if not os.path.exists(p): return fail('S3: cell %d missing' % i)
        txt[i] = open(p, encoding='utf-8').read()
    expected_files = {'cell-%02d.txt' % i for i in range(1, NCELLS + 1)}
    actual_files = {n for n in os.listdir(cells) if n.startswith('cell-') and n.endswith('.txt')}
    if actual_files != expected_files: return fail('S3: unexpected cell output file')
    # S4 cells, in order
    probs = []
    exp = expected(check, load_expected())
    for i in (1, 2, 3, 4, 5):
        ok = txt[i] == exp[i]; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('O%d: cell %d is not the expected text' % (i, i))
    want = summary_list(check); nk = {k: sum(1 for _, kk in want if kk == k) for k in ('def', 'theorem')}
    t5 = txt[6]; pairs = summary_copies(t5)
    totals = re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t5)
    kinds = re.findall(r'"(\d+)", "\\" \\"", StyleBox\["\\"(\w+)\\""', t5)
    ok5 = ('TagBox["LeanEnvironment", "SummaryHead"]' in t5 and len(pairs) == len(set(pairs)) and sorted(pairs) == want
           and totals and all(int(x) == len(want) for x in totals)
           and kinds and {k for _, k in kinds} <= {'def', 'theorem'} and all(int(c) == nk[k] for c, k in kinds))
    rep[6] = ('bound to the checker by name (%d constants: %d theorem, %d def; %d match_ auxiliaries excluded; %d total copies, %d kind copies)'
              % (len(want), nk['theorem'], nk['def'], len(check['declared']) - len(want), len(totals), len(kinds))) if ok5 else 'MISMATCH'
    if not ok5: probs.append('O6: cell 6 does not list exactly the checker constants with matching counts in every copy')
    for i in (7, 8):
        ok = txt[i] == exp[i]; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('O%d: cell %d is not the expected text' % (i, i))
    t8 = txt[9]; vs = graph_vertices(t8)
    ok8 = t8.startswith('BoxData[GraphicsBox[NamespaceBox["NetworkGraphics"') and vs[:1] == [HEAD[0]] and all(v in vs for v in ROUTE)
    rep[9] = 'a network graph rooted at CQ01_prefix31 through the absorption lemma and u_prefix31 (%d vertices)' % len(vs) if ok8 else 'MISMATCH'
    if not ok8: probs.append('O9: cell 9 is not the call graph of CQ01_prefix31 through the absorption route')
    t9 = txt[10]; rc = check['replay']['constants']
    msgs = re.findall(r'accepts all (\d+) declarations', t9); decls = re.findall(r'"Declarations" -> (\d+)', t9)
    every = msgs + re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t9) + re.findall(r'"MessageParameters" -> \{(\d+),', t9) + decls
    ok9 = 'TagBox["Success", "SummaryHead"]' in t9 and 'Failure' not in t9 and msgs and decls and all(int(x) == rc for x in every)
    rep[10] = 'Success, %d declarations (= checker replay) in every one of %d displayed copies' % (rc, len(every)) if ok9 else 'MISMATCH'
    if not ok9: probs.append('O10: cell 10 is not Success with the checker replay count in every copy')
    return ('PASS' if not probs else 'FAIL'), {'cells': rep, 'problems': probs}


def synthetic(check):
    """A full synthetic packet in the observed formats: cells 1-4, 6, 7 from the expected texts; 5, 8 and 9 shaped like edge-sep's real
    cells (two views of the summary, the graph's HoldComplete vertex list, the KernelCheck copies) with this module's names and counts."""
    exp = expected(check, load_expected()); want = summary_list(check); rc = check['replay']['constants']
    nk = {k: sum(1 for _, kk in want if kk == k) for k in ('def', 'theorem')}
    view = ('GridBox[{{RowBox[{TagBox["\\"Constants: \\"", "SummaryItemAnnotation"], "", TagBox["%d", "SummaryItem"]}]}, '
            '{RowBox[{TagBox["\\"Kinds: \\"", "SummaryItemAnnotation"], "", TagBox[TemplateBox[{"  ", "\\"  \\"", '
            'TemplateBox[{"%d", "\\" \\"", StyleBox["\\"theorem\\"", GrayLevel[0.5], StripOnInput -> False]}, "RowDefault"], '
            'TemplateBox[{"%d", "\\" \\"", StyleBox["\\"def\\"", GrayLevel[0.5], StripOnInput -> False]}, "RowDefault"]}, "RowWithSeparators"], "SummaryItem"]}]}}]'
            % (len(want), nk['theorem'], nk['def']))
    assoc = ', '.join('"%s" -> Wolfram`LeanLink`LeanTerm[Association["Name" -> "%s", "Kind" -> "%s", "_Handle" -> 1]]' % (n, n, k) for n, k in want)
    c5 = ('BoxData[InterpretationBox[RowBox[{TagBox["LeanEnvironment", "SummaryHead"], "[", %s, %s, "]"}], '
          'Wolfram`LeanLink`LeanEnvironment[Association["Constants" -> Association[%s]]]]]' % (view, view, assoc))
    c8 = ('BoxData[GraphicsBox[NamespaceBox["NetworkGraphics", DynamicModuleBox[{Typeset`graph = HoldComplete[Graph[{"%s", "%s", "%s", "Not"}, '
          '{Null, {{1, 2}, {1, 3}, {1, 4}}}]]}, {}]]]]' % (HEAD[0], ROUTE[0], ROUTE[1]))
    c9 = ('BoxData[InterpretationBox[RowBox[{TagBox["Success", "SummaryHead"], "[", TagBox["\\"The kernel accepts all %d declarations of M.\\"", "SummaryItem"], '
          'TagBox["\\"The kernel accepts all %d declarations of M.\\"", "SummaryItem"], TagBox["%d", "SummaryItem"], "]"}], '
          'Success["KernelCheck", Association["MessageTemplate" -> "x", "MessageParameters" -> {%d, "M"}, "Declarations" -> %d]]]]' % (rc, rc, rc, rc, rc))
    cells = dict(exp); cells.update({6: c5, 9: c8, 10: c9})
    return cells


def write_packet(d, cells, count=NCELLS):
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'count.txt'), 'w').write('%d\n' % count)
    for i, t in cells.items(): open(os.path.join(d, 'cell-%02d.txt' % i), 'w', encoding='utf-8').write(t)


def fixtures(cells_dir, check_bytes, res, tag):
    """One negative fixture per obligation, each with its exact diagnostic; every cell mutation reads before it writes and must change it."""
    def mutated(i, f, want):
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(cells_dir, t + '/c'); p = t + '/c/cell-%02d.txt' % i
            before = open(p, encoding='utf-8').read(); after = f(before)
            assert after and after != before, 'fixture on cell %d did not change it' % i
            open(p, 'w', encoding='utf-8').write(after)
            v, r = gate(t + '/c', check_bytes, pin=None)
            return v == 'FAIL' and r['problems'][:1] == [want]
    check = strict_json(check_bytes); rc = check['replay']['constants']; want = summary_list(check)
    last1 = lambda s: s[::-1].replace('"1"'[::-1], '"0"'[::-1], 1)[::-1]
    res[tag + 'O1_one_visible_bit'] = mutated(1, lambda s: s.replace('"0", ",", "1"', '"1", ",", "1"', 1), 'O1: cell 1 is not the expected text')
    res[tag + 'O2_one_ether_bit'] = mutated(2, last1, 'O2: cell 2 is not the expected text')
    res[tag + 'O3_one_family_bit'] = mutated(3, last1, 'O3: cell 3 is not the expected text')
    res[tag + 'O4_root_changed'] = mutated(4, last1, 'O4: cell 4 is not the expected text')
    res[tag + 'O5_false'] = mutated(5, lambda s: s.replace('True', 'False'), 'O5: cell 5 is not the expected text')
    n0, k0 = want[0]
    o6 = 'O6: cell 6 does not list exactly the checker constants with matching counts in every copy'
    res[tag + 'O6_name_dropped'] = mutated(6, lambda s: s.replace('"Name" -> "%s", "Kind" -> "%s"' % (n0, k0), '"Name" -> "Rule30Submission.zz", "Kind" -> "%s"' % k0, 1), o6)
    res[tag + 'O6_total_first_copy'] = mutated(6, lambda s: s.replace('TagBox["%d", "SummaryItem"]' % len(want), 'TagBox["%d", "SummaryItem"]' % (len(want) + 6), 1), o6)
    res[tag + 'O7_statement_changed'] = mutated(7, lambda s: s.replace('AgreesPrefix 28 R R31 → ¬FinSupp', 'AgreesPrefix 27 R R31 → ¬FinSupp', 1), 'O7: cell 7 is not the expected text')
    res[tag + 'O8_extra_axiom'] = mutated(8, lambda s: s.replace('"\\"propext\\""', '"\\"propext\\"", ",", "\\"sorryAx\\""', 1), 'O8: cell 8 is not the expected text')
    o9 = 'O9: cell 9 is not the call graph of CQ01_prefix31 through the absorption route'
    res[tag + 'O9_wrong_root'] = mutated(9, lambda s: s.replace('Graph[{"%s", ' % HEAD[0], 'Graph[{"%s", ' % HEAD[1], 1), o9)
    res[tag + 'O9_route_missing'] = mutated(9, lambda s: s.replace('"%s"' % ROUTE[1], '"Rule30Submission.elsewhere"', 1), o9)
    o10 = 'O10: cell 10 is not Success with the checker replay count in every copy'
    res[tag + 'O10_first_message_copy'] = mutated(10, lambda s: s.replace('accepts all %d declarations' % rc, 'accepts all %d declarations' % (rc - 1), 1), o10)
    res[tag + 'O10_declarations_field'] = mutated(10, lambda s: s.replace('"Declarations" -> %d' % rc, '"Declarations" -> %d' % (rc + 7), 1), o10)
    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(cells_dir, t + '/c'); open(t + '/c/count.txt', 'w').write('11\n')
        res[tag + 'S3_count'] = gate(t + '/c', check_bytes, pin=None)[1]['problems'][:1] == ['S3: the cell count is not exactly 10']
        open(t + '/c/count.txt', 'w').write('10\n'); os.remove(t + '/c/cell-06.txt')
        res[tag + 'S3_missing_cell'] = gate(t + '/c', check_bytes, pin=None)[1]['problems'][:1] == ['S3: cell 6 missing']
        shutil.copy(t + '/c/cell-05.txt', t + '/c/cell-06.txt'); shutil.copy(t + '/c/cell-05.txt', t + '/c/cell-11.txt')
        res[tag + 'S3_extra_cell'] = gate(t + '/c', check_bytes, pin=None)[1]['problems'][:1] == ['S3: unexpected cell output file']
        os.remove(t + '/c/cell-11.txt')
        for name in ('cell-12.txt', 'cell-1.txt', 'cell-00.txt'):
            p = os.path.join(t + '/c', name)
            open(p, 'w').write('unexpected output')
            v, r = gate(t + '/c', check_bytes, pin=None)
            res[tag + 'S3_extra_' + name] = v == 'FAIL' and r['problems'][:1] == ['S3: unexpected cell output file']
            os.remove(p)


def synthetic_check():
    """A synthetic checker JSON for the controls before the real Check: the module's own def/theorem names (read from its source), one
    generated match_ auxiliary (excluded by the summary rule), the eight headlines clean on the standard axioms, replay 99."""
    src = open(os.path.join(SUB, 'Rule30Submission.lean'), encoding='utf-8').read()
    dec = [{'kind': k, 'name': 'Rule30Submission.' + n, 'standardAxioms': True} for k, n in re.findall(r'^(def|theorem) (\S+)', src, re.M)]
    dec.append({'kind': 'def', 'name': 'Rule30Submission.S.match_1', 'standardAxioms': True})
    hs = [{'axioms': ['propext', 'Classical.choice', 'Quot.sound'], 'found': True, 'kind': 'theorem', 'name': h, 'ok': True, 'problems': [], 'typeMatches': True} for h in HEAD]
    return json.dumps({'claim': 'partial', 'declared': dec, 'headlines': hs, 'importsStatements': True, 'module': 'Rule30Submission', 'newAxioms': [],
                       'official': [], 'reasons': [], 'replay': {'constants': 99, 'ok': True}, 'verdict': 'pass', 'verifiedTargets': []}).encode()


def controls(real_cells=None, real_check=None):
    res = {}
    check_bytes = synthetic_check(); check = strict_json(check_bytes)
    with tempfile.TemporaryDirectory() as t:
        write_packet(t + '/syn', synthetic(check))
        res['unset_pin_refuses'] = gate(t + '/syn', check_bytes, pin='UNSET')[1]['problems'] == ['S1: no checker JSON is pinned yet']
        res['pinned_rejects_synthetic_checker'] = gate(t + '/syn', check_bytes)[1]['problems'] == ['S1: the checker JSON is not the committed check.json']
        res['pinned_check_json_true_file'] = sha(open(os.path.join(SUB, 'check.json'), 'rb').read()) == CHECK_SHA256
        v, r = gate(t + '/syn', check_bytes, pin=sha(check_bytes)); res['synthetic_packet_passes'] = v == 'PASS'
        if v != 'PASS': print(json.dumps(r, indent=1, ensure_ascii=False))
        fixtures(t + '/syn', check_bytes, res, 'syn_')
        res['S1_other_bytes'] = gate(t + '/syn', check_bytes + b' ', pin=sha(check_bytes))[1]['problems'] == ['S1: the checker JSON is not the committed check.json']
        def s2(mut, want):
            c = json.loads(check_bytes); mut(c); b = json.dumps(c).encode()
            return gate(t + '/syn', b, pin=None)[1]['problems'] == [want]
        def raw(old, new):
            assert check_bytes.count(old) == 1, old
            return gate(t + '/syn', check_bytes.replace(old, new), pin=None)[1]['problems'][:1]
        res['S2_nan_count'] = raw(b'"constants": 99', b'"constants": NaN') == ['S2: the checker JSON does not parse strictly (non-finite constant NaN)']
        res['S2_duplicate_key'] = raw(b'"verdict": "pass"', b'"verdict": "pass", "verdict": "pass"') == ['S2: the checker JSON does not parse strictly (duplicate key)']
        res['S2_verdict_fail'] = s2(lambda c: c.update(verdict='fail'), 'S2: the checker JSON is not a clean partial pass with an integer replay count')
        res['S2_float_count'] = s2(lambda c: c['replay'].update(constants=99.0), 'S2: the checker JSON is not a clean partial pass with an integer replay count')
        res['S2_headline_missing'] = s2(lambda c: c.update(headlines=c['headlines'][:-1]), 'S2: the headlines are not exactly the eight, each found, ok and type-matching')
        res['S2_bad_axiom'] = s2(lambda c: c['headlines'][0].update(axioms=c['headlines'][0]['axioms'] + ['sorryAx']), 'S2: a headline axiom outside the standard three')
        res['S2_other_kind'] = s2(lambda c: c['declared'][0].update(kind='axiom'), 'S2: a declared entry is malformed or of another kind')
        res['S2_declared_repeat'] = s2(lambda c: c.update(declared=c['declared'] + c['declared'][:1]), 'S2: a declared name repeats')
        res['S2_missing_key'] = s2(lambda c: c.pop('reasons'), 'S2: key reasons missing or not list')
        bad = t + '/expected_other.py'; open(bad, 'w').write(open(os.path.join(SUB, 'expected_numbers.py')).read() + '\n')
        res['S1_expected_numbers_other_bytes'] = gate(t + '/syn', check_bytes, pin=None, expected_path=bad)[1]['problems'] == ['S1: expected_numbers.py is not the pinned bytes']
    if real_cells:
        rb = open(real_check, 'rb').read()
        v, r = gate(real_cells, rb); res['real_cells_pass'] = v == 'PASS'
        if v != 'PASS': print(json.dumps(r, indent=1, ensure_ascii=False))
        fixtures(real_cells, rb, res, 'real_')
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('GATE CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--controls'] and len(a) in (1, 3):
        sys.exit(0 if controls(*(a[1:] or [None, None])) else 1)
    if len(a) == 2:
        v, r = gate(a[0], open(a[1], 'rb').read()); print(json.dumps({'verdict': v, **r}, indent=1, ensure_ascii=False)); sys.exit(0 if v == 'PASS' else 1)
    print(__doc__); sys.exit(2)
