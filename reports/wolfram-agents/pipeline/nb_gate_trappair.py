#!/usr/bin/env python3
"""Output-cell gate for the trap-pair submission (Local, 2026-10-25, the next job made ready while GPT reads L928; GC1813's method:
one ordered explicit schema, fail-closed, a full synthetic packet and one exact-diagnostic negative fixture per obligation).
Written BEFORE the notebook exists, from the essay's nine code cells, the committed checker JSON and the real edge-sep cells' box
formats (submission 18's build). Every box format and every pretty-printed statement below is a PREDICTION until the trap-pair build's
cells are read; a change after that read is a format reading, disclosed with the cells, never a change of what is bound.

Order (the first failing stage stops the gate with its diagnostic; later stages are not evaluated):
  S1 bytes: the checker JSON's SHA-256 equals CHECK_SHA256 (the committed check.json, Check PASS at L925), and expected_numbers.py's
     equals EXPECTED_SHA256;
  S2 the checker JSON: strict parse (no NaN/Infinity, no duplicate keys); types and keys; verdict pass, claim partial, no new axioms,
     no reasons, replay ok with an integer constant count; exactly the five headlines, each found, ok and type-matching, on the
     standard three axioms only; `declared` a list of {name, kind} with kinds def or theorem;
  S3 the packet: count.txt is exactly the integer 9; cell-01 .. cell-09 exist; no cell-10;
  S4 the cells, one obligation each:
     O1 (drive illustration): EQUAL to the box text of [u R31 for s < 12, u R495 for s < 12, cells 1..9 of R31 at time 4], values from
        expected_numbers.py (independent plain Python, no shared code with the cells or the module);
     O2 (trap entries): EQUAL to [R31 at time 9, R495 at time 5 (columns 1..19), the ether columns 1..6 at phase 12];
     O3 (moves): EQUAL to [the S-chain from [1] (five words), root of R31, root of reversed R495];
     O4: exactly BoxData["True"] (the kit directory exists);
     O5 (the LeanEnvironment summary): the displayed (Name, Kind) pairs, with no repeats, equal the
        checker's `declared` list minus the compiler's generated `match_` auxiliaries (excluded by name, as edge-sep's build showed);
        every displayed total and per-kind count, in every copy, equals that list's;
     O6 (the five headline statements): EQUAL to TYPES, in the essay's order;
     O7: EQUAL to the checker's CQ01_R31 axiom list, sorted as printed;
     O8 (the call graph): a network graph whose first vertex is Rule30Submission.CQ01_R31 and whose vertices include the kit's
        absorption lemma and u_R31_periodic (the route the essay names);
     O9 (KernelCheck): Success, no Failure, and every displayed declaration count equal to the checker's replay count.
usage: python3 nb_gate_trappair.py CELLS_DIR CHECK_JSON            (exit 0 only on PASS)
       python3 nb_gate_trappair.py --controls [CELLS_DIR CHECK_JSON] (the synthetic packet and its fixtures; with real cells, those too)"""
import contextlib, hashlib, io, json, os, re, shutil, sys, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(HERE, '..', 'submissions', 'trap-pair')
CHECK_SHA256 = '86abca97a1ecbf29da3f0c7d3ff79297e04ee09bd8c8e92f609342cb22f2839c'
EXPECTED_SHA256 = 'f3169078fda72d692a1a01ff23d71927359016f2bd9f812165379666ea104a64'
HEAD = ['Rule30Submission.' + n for n in ('CQ01_R31', 'CQ01_R495', 'Psi_eq', 'u_R31', 'not_move_equivalent')]
STD = {'propext', 'Quot.sound', 'Classical.choice'}
TYPES = ['¬FinSupp (Psi R31)', '¬FinSupp (Psi R495)', 'Psi R31 = Psi R495', '∀ (q : ℕ), u R31 q = (q % 2 == 1)',
         '¬Relation.EqvGen Move cells31.reverse cells495.reverse']
ROUTE = ['Ruliology.CellularAutomata.Rule30PeriodTwoSideways.not_finSupp_Psi_of_eventuallyPeriodic', 'Rule30Submission.u_R31_periodic']
NCELLS = 9


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_expected():
    p = os.path.join(SUB, 'expected_numbers.py')
    spec = importlib.util.spec_from_file_location('trap_pair_expected', p); m = importlib.util.module_from_spec(spec)
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
            3: 'BoxData[' + box([E.chain, E.root([1, 1, 1, 1, 1]), E.root([1, 1, 1, 1, 0, 1, 1, 1, 1][::-1])]) + ']',
            4: 'BoxData["True"]',
            6: 'BoxData[' + lst([esc(x) for x in TYPES]) + ']',
            7: 'BoxData[' + lst(['"\\"%s\\""' % x for x in ax]) + ']'}


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
        return 'S2: the headlines are not exactly the five, each found, ok and type-matching'
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
    if os.path.exists(os.path.join(cells, 'cell-%02d.txt' % (NCELLS + 1))): return fail('S3: a cell beyond %d exists' % NCELLS)
    # S4 cells, in order
    probs = []
    exp = expected(check, load_expected())
    for i in (1, 2, 3, 4):
        ok = txt[i] == exp[i]; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('O%d: cell %d is not the expected text' % (i, i))
    want = summary_list(check); nk = {k: sum(1 for _, kk in want if kk == k) for k in ('def', 'theorem')}
    t5 = txt[5]; pairs = summary_copies(t5)
    totals = re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t5)
    kinds = re.findall(r'"(\d+)", "\\" \\"", StyleBox\["\\"(\w+)\\""', t5)
    ok5 = ('TagBox["LeanEnvironment", "SummaryHead"]' in t5 and len(pairs) == len(set(pairs)) and sorted(pairs) == want
           and totals and all(int(x) == len(want) for x in totals)
           and kinds and {k for _, k in kinds} <= {'def', 'theorem'} and all(int(c) == nk[k] for c, k in kinds))
    rep[5] = ('bound to the checker by name (%d constants: %d theorem, %d def; %d match_ auxiliaries excluded; %d total copies, %d kind copies)'
              % (len(want), nk['theorem'], nk['def'], len(check['declared']) - len(want), len(totals), len(kinds))) if ok5 else 'MISMATCH'
    if not ok5: probs.append('O5: cell 5 does not list exactly the checker constants with matching counts in every copy')
    for i in (6, 7):
        ok = txt[i] == exp[i]; rep[i] = 'exact' if ok else 'MISMATCH'
        if not ok: probs.append('O%d: cell %d is not the expected text' % (i, i))
    t8 = txt[8]; vs = graph_vertices(t8)
    ok8 = t8.startswith('BoxData[GraphicsBox[NamespaceBox["NetworkGraphics"') and vs[:1] == [HEAD[0]] and all(v in vs for v in ROUTE)
    rep[8] = 'a network graph rooted at CQ01_R31 through the absorption lemma (%d vertices)' % len(vs) if ok8 else 'MISMATCH'
    if not ok8: probs.append('O8: cell 8 is not the call graph of CQ01_R31 through the absorption route')
    t9 = txt[9]; rc = check['replay']['constants']
    msgs = re.findall(r'accepts all (\d+) declarations', t9); decls = re.findall(r'"Declarations" -> (\d+)', t9)
    every = msgs + re.findall(r'TagBox\["(\d+)", "SummaryItem"\]', t9) + re.findall(r'"MessageParameters" -> \{(\d+),', t9) + decls
    ok9 = 'TagBox["Success", "SummaryHead"]' in t9 and 'Failure' not in t9 and msgs and decls and all(int(x) == rc for x in every)
    rep[9] = 'Success, %d declarations (= checker replay) in every one of %d displayed copies' % (rc, len(every)) if ok9 else 'MISMATCH'
    if not ok9: probs.append('O9: cell 9 is not Success with the checker replay count in every copy')
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
    cells = dict(exp); cells.update({5: c5, 8: c8, 9: c9})
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
    res[tag + 'O1_one_visible_bit'] = mutated(1, lambda s: s.replace('"0", ",", "1"', '"1", ",", "1"', 1), 'O1: cell 1 is not the expected text')
    res[tag + 'O2_one_ether_bit'] = mutated(2, lambda s: s[::-1].replace('"1"'[::-1], '"0"'[::-1], 1)[::-1], 'O2: cell 2 is not the expected text')
    res[tag + 'O3_root_changed'] = mutated(3, lambda s: s[::-1].replace('"1"'[::-1], '"0"'[::-1], 1)[::-1], 'O3: cell 3 is not the expected text')
    res[tag + 'O4_false'] = mutated(4, lambda s: s.replace('True', 'False'), 'O4: cell 4 is not the expected text')
    n0, k0 = want[0]
    res[tag + 'O5_name_dropped_one_copy'] = mutated(5, lambda s: s.replace('"Name" -> "%s", "Kind" -> "%s"' % (n0, k0), '"Name" -> "Rule30Submission.zz", "Kind" -> "%s"' % k0, 1),
                                                  'O5: cell 5 does not list exactly the checker constants with matching counts in every copy')
    res[tag + 'O5_total_first_copy'] = mutated(5, lambda s: s.replace('TagBox["%d", "SummaryItem"]' % len(want), 'TagBox["%d", "SummaryItem"]' % (len(want) + 6), 1),
                                             'O5: cell 5 does not list exactly the checker constants with matching counts in every copy')
    res[tag + 'O6_statement_changed'] = mutated(6, lambda s: s.replace('Psi R31 = Psi R495', 'Psi R31 = Psi R31', 1), 'O6: cell 6 is not the expected text')
    res[tag + 'O7_extra_axiom'] = mutated(7, lambda s: s.replace('"\\"propext\\""', '"\\"propext\\"", ",", "\\"sorryAx\\""', 1), 'O7: cell 7 is not the expected text')
    res[tag + 'O8_wrong_root'] = mutated(8, lambda s: s.replace('Graph[{"%s", ' % HEAD[0], 'Graph[{"%s", ' % HEAD[1], 1),
                                         'O8: cell 8 is not the call graph of CQ01_R31 through the absorption route')
    res[tag + 'O8_route_missing'] = mutated(8, lambda s: s.replace('"%s"' % ROUTE[0], '"Rule30Submission.elsewhere"', 1),
                                            'O8: cell 8 is not the call graph of CQ01_R31 through the absorption route')
    res[tag + 'O9_first_message_copy'] = mutated(9, lambda s: s.replace('accepts all %d declarations' % rc, 'accepts all %d declarations' % (rc - 1), 1),
                                                 'O9: cell 9 is not Success with the checker replay count in every copy')
    res[tag + 'O9_declarations_field'] = mutated(9, lambda s: s.replace('"Declarations" -> %d' % rc, '"Declarations" -> %d' % (rc + 7), 1),
                                                 'O9: cell 9 is not Success with the checker replay count in every copy')
    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(cells_dir, t + '/c'); open(t + '/c/count.txt', 'w').write('10\n')
        res[tag + 'S3_count'] = gate(t + '/c', check_bytes, pin=None)[1]['problems'][:1] == ['S3: the cell count is not exactly 9']
        open(t + '/c/count.txt', 'w').write('9\n'); os.remove(t + '/c/cell-05.txt')
        res[tag + 'S3_missing_cell'] = gate(t + '/c', check_bytes, pin=None)[1]['problems'][:1] == ['S3: cell 5 missing']


def controls(real_cells=None, real_check=None):
    res = {}
    check_bytes = open(os.path.join(SUB, 'check.json'), 'rb').read(); check = strict_json(check_bytes)
    res['pinned_check_json_true_file'] = sha(check_bytes) == CHECK_SHA256
    with tempfile.TemporaryDirectory() as t:
        write_packet(t + '/syn', synthetic(check))
        v, r = gate(t + '/syn', check_bytes); res['synthetic_packet_passes'] = v == 'PASS'
        if v != 'PASS': print(json.dumps(r, indent=1, ensure_ascii=False))
        fixtures(t + '/syn', check_bytes, res, 'syn_')
        # S1 and S2 fixtures, each with its exact diagnostic
        res['S1_other_bytes'] = gate(t + '/syn', check_bytes + b' ')[1]['problems'] == ['S1: the checker JSON is not the committed check.json']
        def s2(mut, want):
            c = json.loads(check_bytes); mut(c); b = json.dumps(c).encode()
            return gate(t + '/syn', b, pin=None)[1]['problems'] == [want]
        def raw(old, new):
            assert check_bytes.count(old) == 1, old
            return gate(t + '/syn', check_bytes.replace(old, new), pin=None)[1]['problems'][:1]
        res['S2_nan_count'] = raw(b'"constants":66', b'"constants":NaN') == ['S2: the checker JSON does not parse strictly (non-finite constant NaN)']
        res['S2_duplicate_key'] = raw(b'"verdict":"pass"', b'"verdict":"pass","verdict":"pass"') == ['S2: the checker JSON does not parse strictly (duplicate key)']
        res['S2_verdict_fail'] = s2(lambda c: c.update(verdict='fail'), 'S2: the checker JSON is not a clean partial pass with an integer replay count')
        res['S2_float_count'] = s2(lambda c: c['replay'].update(constants=66.0), 'S2: the checker JSON is not a clean partial pass with an integer replay count')
        res['S2_headline_missing'] = s2(lambda c: c.update(headlines=c['headlines'][:-1]), 'S2: the headlines are not exactly the five, each found, ok and type-matching')
        res['S2_bad_axiom'] = s2(lambda c: c['headlines'][0].update(axioms=c['headlines'][0]['axioms'] + ['sorryAx']), 'S2: a headline axiom outside the standard three')
        res['S2_other_kind'] = s2(lambda c: c['declared'][0].update(kind='axiom'), 'S2: a declared entry is malformed or of another kind')
        res['S2_declared_repeat'] = s2(lambda c: c.update(declared=c['declared'] + c['declared'][:1]), 'S2: a declared name repeats')
        res['S2_missing_key'] = s2(lambda c: c.pop('reasons'), 'S2: key reasons missing or not list')
        # the expected-numbers pin
        bad = t + '/expected_other.py'; open(bad, 'w').write(open(os.path.join(SUB, 'expected_numbers.py')).read() + '\n')
        res['S1_expected_numbers_other_bytes'] = gate(t + '/syn', check_bytes, expected_path=bad)[1]['problems'] == ['S1: expected_numbers.py is not the pinned bytes']
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
