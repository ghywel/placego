#!/usr/bin/env python3
"""CQ01 deep-time rows, revision 1 (Local, 2026-10-24, L914; L913's next job (i)). NOT an agreed job until GPT accepts this exact file;
nothing runs on import; `--controls` runs the small CPU controls only.

If this holds, it changes the CQ01 row: L913 left 82 groups of move classes merged through 1,600 visible bits (depth 3,200), none of them
a delayed move. This job runs each group's members far deeper, as single rows encoded as Python integers (cell x is bit x; the wall at
bit 0), to T = 40,000 steps, that is 20,000 visible bits, and reports which pairs split and when. Persistence through 20,000 bits is still
only unresolved (GC1823): it names candidates for a second mechanism; only a proof of permanent equality refutes the kernel conjecture.

Input: the retained kernel result (cited/cq01-kernel-20261024-2224/cq01_kernel_result.json), given by path and required to have the
sha256 KERNEL_RESULT_SHA256; its merged groups (82, each a sorted list of move-class least lanes, cell p = bit p - 1) are the rows.
Measured, for every row R (lane r, the right half on cells 1..16): its visible word u R s = cell 1 at time 2s + 1, s < T/2, retained as
hex; per group, the classes of its rows by the whole visible word and, for each member against the group's first, the first visible
index s at which they differ (None if equal through T/2).
Controls inside the run and in `--controls`:
  - the integer-row engine equals the lane engine: every visible word for every R supported in 1..8 at K = 400 equals
    cq01_collisions.compute's u lane bits (the kit's definitions), and for B = 16 at K = 32;
  - 40 move pairs (r, move partner of r) drawn by numpy PCG64 seed 20261024 from the lanes supported in 1..16 stay equal through T/2 (the
    move lemma, PROOFS.md L910, HAND/PROVED GC1823);
  - a mutant 'wallphase' (the wall black at odd times) must fail the engine control, and a mutant 'shiftvis' (cell 1 read at even times)
    must fail it too.
The result gate (GC1813, GC1818, GC1821, GC1823): strict reading, one explicit schema in the order types, exact key sets, domains,
cross-field bindings, arithmetic, completion, fail-closed, on bounded bytes; the input digest and the exact row set (every lane of every
group, once) bound; every per-group class and first-difference recomputed from the retained words; the 40 move pairs selected by the same
seeded helper, their words retained too, their differences recomputed from those words and required absent. The valid synthetic packet is a real tiny computation (T = 400 on four retained groups); every
negative fixture states its exact diagnostic.

Proposed stage: T = 40,000 (the only admitted stage scope); W1A caps: stage, step wall and CPU 600 s, group RSS 4 GiB, artifacts 50 MiB,
log 10 MiB. Cost ESTIMATE: one row of 20,000 steps took 0.02 s in a probe; the row grows one bit per step, so a 40,000-step row is about
0.08 s, and about 1,000 rows near 80 s; the retained words are about 1,000 x 2,500 bytes of hex (2.5 MB). `run` also admits 400 <= T
<= 40,000, even, for disclosed tiny development runs.
Predictions (written before any run of this file, after L913):
  - every one of the 40 move pairs stays equal through 20,000 visible bits (the lemma);
  - 11111 and 111101111 (cell 1 first) stay equal through 20,000 visible bits;
  - fewer than 20 of the 82 groups split at all by 20,000 visible bits.
Counterfactual: most groups split between 1,600 and 20,000 visible bits says L913's plateau was a horizon effect, and the kernel
conjecture regains ground; 11111 and 111101111 splitting kills my pull at the 1111 block. Results between are inconclusive.
Usage: python3 cq01_deeptime.py --controls | run OUT KERNEL_RESULT T | stage OUT KERNEL_RESULT T
"""
import hashlib, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
KERNEL_SHA256 = 'de6c178d37c1a78fc17a35c92b0b8ba7f5388c661e3eb3054c931adb5a7bc83b'
KERNEL_RESULT_SHA256 = '16c70bf3832a2aca776f02405020ec964610a2db02df100bab9a2ae3e2f3488e'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_T = 40000
STAGE_S = 600
SEED = 20261024
N_MOVE_PAIRS = 40
B = 16
MUTANTS = ('wallphase', 'shiftvis')
BASE_KEYS = ('int_rows_equal_lane_engine_B8_K400_and_B16_K32', 'move_pairs_equal_T800')
PARSE_FAIL = 'parse: nonfinite or invalid JSON'


def deps():
    import cq01_kernel as KX
    if hashlib.sha256(open(KX.__file__, 'rb').read()).hexdigest() != KERNEL_SHA256:
        raise SystemExit('REFUSED: cq01_kernel.py is not the pinned bytes')
    X, M, C = KX.deps()
    return KX, X, M


def visible_word(r, T, mutant=''):
    """u R s for s < T/2 as an int (bit s), from one row encoded as an int: bit x is cell x, bit 0 the wall."""
    w = r << 1; out = 0
    for t in range(T):
        black = (t % 2 == 1) if mutant == 'wallphase' else (t % 2 == 0)
        w |= 1 if black else 0
        if mutant == 'shiftvis' and t % 2 == 0: out |= ((w >> 1) & 1) << (t // 2)
        w = ((w << 1) ^ (w | (w >> 1))) & ~1
        if mutant != 'shiftvis' and t % 2 == 0: out |= ((w >> 1) & 1) << (t // 2)
    return out


def first_diff(a, b):
    x = a ^ b
    return (x & -x).bit_length() - 1 if x else None


def word_hex(v, V):
    return format(v, 'x').rjust((V + 3) // 4, '0')


def move_pairs(n=N_MOVE_PAIRS):
    """Seeded move pairs from the lanes supported in 1..16 (producer and gate)."""
    import numpy as np
    KX, X, M = deps()
    rng = np.random.Generator(np.random.PCG64(SEED)); out = []
    while len(out) < n:
        r = int(rng.integers(1, 1 << B)); q = KX.move_partner(r, B)
        if q is not None and [r, q] not in out: out.append([r, q])
    return out


def group_report(groups, words, V):
    """Per group: classes of its rows by the whole word (sorted lists of lanes), and each member's first difference from the first."""
    out = []
    for g in groups:
        cls = {}
        for r in g: cls.setdefault(words[r], []).append(r)
        out.append({'classes': sorted(sorted(v) for v in cls.values()), 'first_diff': [first_diff(words[g[0]], words[r]) for r in g[1:]]})
    return out


def load_groups(path):
    raw = open(path, 'rb').read()
    if hashlib.sha256(raw).hexdigest() != KERNEL_RESULT_SHA256: raise SystemExit('REFUSED: the kernel result is not the pinned bytes')
    d = json.loads(raw)
    assert d['merged']['total'] == len(d['merged']['groups'])
    return d['merged']['groups']


def assemble(groups, T, mutant=''):
    V = T // 2; t0 = time.monotonic()
    lanes = sorted({r for g in groups for r in g})
    words = {r: visible_word(r, T, mutant) for r in lanes}
    rows_s = time.monotonic() - t0
    mp = move_pairs()
    mlanes = sorted({x for pr in mp for x in pr})
    mw = {x: (words[x] if x in words else visible_word(x, T, mutant)) for x in mlanes}
    rep = group_report(groups, words, V)
    split = sum(1 for g in rep if len(g['classes']) > 1)
    return ({'rows': {str(r): word_hex(words[r], V) for r in lanes}, 'groups': groups, 'report': rep,
             'move_pairs': {'pairs': mp, 'rows': {str(x): word_hex(mw[x], V) for x in mlanes}, 'first_diff': [first_diff(mw[r], mw[q]) for r, q in mp]},
             'summary': {'groups': len(groups), 'groups_split': split, 'rows': len(lanes)}},
            {'rows_s': round(rows_s, 2), 'total_s': round(time.monotonic() - t0, 2)})


def controls(mutant=''):
    KX, X, M = deps(); res = {}
    ok = True
    for Bc, K in ((8, 400), (16, 32)):
        _, ubits = X.compute(Bc, K)
        for r in range(1 << Bc):
            w = visible_word(r, K, mutant)
            if [(w >> s) & 1 for s in range(K // 2)] != [int(x) for x in ubits[1:, r]]: ok = False; break
    res['int_rows_equal_lane_engine_B8_K400_and_B16_K32'] = ok
    res['move_pairs_equal_T800'] = all(visible_word(r, 800, mutant) == visible_word(q, 800, mutant) for r, q in move_pairs())
    return res


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 DEEPTIME CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, kpath, T):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic(); deps()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'kernel_result_sha256': KERNEL_RESULT_SHA256, 'scope': {'T': T}, 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_deeptime_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'cq01_deeptime_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    sections, timing = assemble(load_groups(kpath), T)
    R.update(sections); R['timing'] = timing
    R['complete'] = all(f is None for f in R['move_pairs']['first_diff'])
    if not R['complete']: R['stopped'] = 'incomplete: a move pair split (no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 16 << 20
TOP_KEYS = {'started', 'finished', 'elapsed_s', 'this_sha256', 'kernel_result_sha256', 'scope', 'controls', 'gate_controls', 'rows', 'groups',
            'report', 'move_pairs', 'summary', 'timing', 'complete'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}


def validate_result(d, src_sha, T, groups_in):
    isint = lambda x: type(x) is int
    fin = lambda x: (type(x) is int or (type(x) is float and math.isfinite(x)))
    V = T // 2; hexlen = (V + 3) // 4
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('this_sha256', str), ('kernel_result_sha256', str), ('started', str), ('finished', str), ('scope', dict), ('controls', dict),
                   ('gate_controls', dict), ('rows', dict), ('groups', list), ('report', list), ('move_pairs', dict), ('summary', dict),
                   ('timing', dict), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float): return 'types: elapsed_s'
    c = d['controls']
    if not isinstance(c.get('base'), dict) or not all(isinstance(c.get(m), dict) for m in MUTANTS): return 'types: control reports'
    if not all(isinstance(g, dict) and isinstance(g.get('classes'), list) and isinstance(g.get('first_diff'), list) for g in d['report']): return 'types: report'
    if not (isinstance(d['move_pairs'].get('pairs'), list) and isinstance(d['move_pairs'].get('first_diff'), list) and isinstance(d['move_pairs'].get('rows'), dict)):
        return 'types: move pairs'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['scope']) != {'T'}: return 'keys: scope'
    if set(c) != CONTROL_KEYS: return 'keys: controls'
    if set(c['base']) != set(BASE_KEYS) or not all(set(c[m]) == set(BASE_KEYS) for m in MUTANTS): return 'keys: base or mutant reports'
    if set(d['gate_controls']) != set(GATE_KEYS): return 'keys: gate controls'
    if not all(set(g) == {'classes', 'first_diff'} for g in d['report']): return 'keys: report'
    if set(d['move_pairs']) != {'pairs', 'rows', 'first_diff'} or set(d['summary']) != {'groups', 'groups_split', 'rows'} or set(d['timing']) != {'rows_s', 'total_s'}:
        return 'keys: sections'
    lanes = sorted({r for g in groups_in for r in g})
    if set(d['rows']) != {str(r) for r in lanes}: return 'keys: rows'
    mp_sel = move_pairs()
    if set(d['move_pairs']['rows']) != {str(x) for pr in mp_sel for x in pr}: return 'keys: move-pair rows'
    # 3. domains
    if d['this_sha256'] != src_sha: return 'domains: source digest'
    if d['kernel_result_sha256'] != KERNEL_RESULT_SHA256: return 'domains: input digest'
    if d['scope'] != {'T': T}: return 'domains: scope'
    if not all(type(v) is bool for v in list(c['base'].values()) + [x for m in MUTANTS for x in c[m].values()] + [c[m + '_caught'] for m in MUTANTS] + [c['base_all_pass'], c['ok']]):
        return 'domains: control values not Boolean'
    if not all(v is True for v in d['gate_controls'].values()): return 'domains: a gate control is not true'
    if not all(fin(x) and x >= 0 for x in [d['elapsed_s']] + list(d['timing'].values())): return 'domains: timing'
    if not all(isinstance(v, str) and len(v) == hexlen and all(ch in '0123456789abcdef' for ch in v) and int(v, 16) < (1 << V)
               for v in list(d['rows'].values()) + list(d['move_pairs']['rows'].values())):
        return 'domains: rows'
    if not all(x is None or (isint(x) and 0 <= x < V) for g in d['report'] for x in g['first_diff']) or not all(x is None or (isint(x) and 0 <= x < V) for x in d['move_pairs']['first_diff']):
        return 'domains: first differences'
    # 4. cross-field bindings
    if not all(c['base'][k] is True for k in BASE_KEYS) or c['base_all_pass'] is not True: return 'bindings: base controls'
    for m in MUTANTS:
        if c[m + '_caught'] is not True or all(c[m][k] for k in BASE_KEYS): return 'bindings: mutant %s not caught by its own outcomes' % m
    if c['ok'] is not True: return 'bindings: controls ok flag'
    if d['groups'] != groups_in: return 'bindings: groups are not the retained kernel groups'
    if d['move_pairs']['pairs'] != mp_sel: return 'bindings: move pairs are not the seeded selection'
    for x, v in d['move_pairs']['rows'].items():
        if x in d['rows'] and d['rows'][x] != v: return 'bindings: a lane has two different words'
    # 5. arithmetic
    words = {int(k): int(v, 16) for k, v in d['rows'].items()}
    if d['report'] != group_report(groups_in, words, V): return 'arithmetic: group report vs retained words'
    mw = {int(k): int(v, 16) for k, v in d['move_pairs']['rows'].items()}
    if d['move_pairs']['first_diff'] != [first_diff(mw[r], mw[q]) for r, q in mp_sel]: return 'arithmetic: move-pair differences vs retained words'
    if any(f is not None for f in d['move_pairs']['first_diff']): return 'arithmetic: a move pair split'
    split = sum(1 for g in d['report'] if len(g['classes']) > 1)
    if d['summary'] != {'groups': len(groups_in), 'groups_split': split, 'rows': len(lanes)}: return 'arithmetic: summary'
    # 6. completion
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, T, groups_in):
    KX, X, M = deps()
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = M.strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate_result(d, src_sha, T, groups_in)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'CQ01 deep-time rows complete, every move pair equal; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


GATE_T = 400
GATE_GROUPS = [[31, 495, 1167], [37, 39051], [112, 944], [62, 495]]   # synthetic: real lanes, not required to be merged


def gate_fixtures():
    nan = float('nan')
    def flip_word(d):
        k = sorted(d['rows'], key=int)[1]; v = int(d['rows'][k], 16) ^ 1; d['rows'][k] = format(v, 'x').rjust(len(d['rows'][k]), '0')
    def drop_group(d): d['groups'].pop()
    def stale_report(d): d['report'][0]['first_diff'] = [0] * len(d['report'][0]['first_diff'])
    def split_move(d):                # a move pair whose retained words really differ, its difference reported honestly
        r, q = d['move_pairs']['pairs'][0]; w = d['move_pairs']['rows'][str(q)]
        nv = int(w, 16) ^ (1 << 3); d['move_pairs']['rows'][str(q)] = format(nv, 'x').rjust(len(w), '0')
        if str(q) in d['rows']: d['rows'][str(q)] = d['move_pairs']['rows'][str(q)]
        d['move_pairs']['first_diff'][0] = 3
    def bad_pairs(d): d['move_pairs']['pairs'][0] = [1, 3]
    return [
        ('good_full_packet_passes', 'file', lambda d: None, None),
        ('types_rows_list', 'file', lambda d: d.__setitem__('rows', []), 'types: rows'),
        ('types_started_dict', 'file', lambda d: d.__setitem__('started', {}), 'types: started'),
        ('types_elapsed_string', 'file', lambda d: d.__setitem__('elapsed_s', '1'), 'types: elapsed_s'),
        ('keys_extra_top_key', 'file', lambda d: d.__setitem__('extra', 1), "keys: top level ['extra']"),
        ('keys_stopped_present', 'file', lambda d: d.__setitem__('stopped', 'x'), "keys: top level ['stopped']"),
        ('keys_row_missing', 'file', lambda d: d['rows'].pop(sorted(d['rows'], key=int)[0]), 'keys: rows'),
        ('domains_wrong_digest', 'file', lambda d: d.__setitem__('this_sha256', '0' * 64), 'domains: source digest'),
        ('domains_wrong_input', 'file', lambda d: d.__setitem__('kernel_result_sha256', '0' * 64), 'domains: input digest'),
        ('domains_wrong_scope', 'file', lambda d: d['scope'].__setitem__('T', 402), 'domains: scope'),
        ('domains_negative_timing', 'file', lambda d: d['timing'].__setitem__('rows_s', -1.0), 'domains: timing'),
        ('domains_nan_elapsed', 'memory', lambda d: d.__setitem__('elapsed_s', nan), 'domains: timing'),
        ('domains_inf_timing', 'memory', lambda d: d['timing'].__setitem__('total_s', float('inf')), 'domains: timing'),
        ('domains_row_not_hex', 'file', lambda d: d['rows'].__setitem__(sorted(d['rows'], key=int)[0], 'z' * len(d['rows'][sorted(d['rows'], key=int)[0]])), 'domains: rows'),
        ('domains_first_diff_range', 'file', lambda d: d['move_pairs']['first_diff'].__setitem__(0, GATE_T), 'domains: first differences'),
        ('parse_nan_token', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": NaN, "x_": ', 1), PARSE_FAIL),
        ('parse_exponent_overflow', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": 1e999, "x_": ', 1), PARSE_FAIL),
        ('bindings_explicit_false_base', 'file', lambda d: d['controls']['base'].__setitem__(BASE_KEYS[0], False), 'bindings: base controls'),
        ('bindings_mutant_all_true', 'file', lambda d: [d['controls'].__setitem__(m, {k: True for k in BASE_KEYS}) for m in MUTANTS],
         'bindings: mutant %s not caught by its own outcomes' % MUTANTS[0]),
        ('bindings_group_dropped', 'file', drop_group, 'bindings: groups are not the retained kernel groups'),
        ('bindings_move_pairs_changed', 'file', bad_pairs, 'bindings: move pairs are not the seeded selection'),
        ('arithmetic_word_changed', 'file', flip_word, 'arithmetic: group report vs retained words'),
        ('arithmetic_stale_report', 'file', stale_report, 'arithmetic: group report vs retained words'),
        ('arithmetic_move_pair_split', 'file', split_move, 'arithmetic: a move pair split'),
        ('arithmetic_move_pair_unbacked', 'file', lambda d: d['move_pairs']['first_diff'].__setitem__(0, 3), 'arithmetic: move-pair differences vs retained words'),
        ('keys_move_row_missing', 'file', lambda d: d['move_pairs']['rows'].pop(sorted(d['move_pairs']['rows'], key=int)[0]), 'keys: move-pair rows'),
        ('arithmetic_summary', 'file', lambda d: d['summary'].__setitem__('groups_split', d['summary']['groups_split'] + 1), 'arithmetic: summary'),
        ('completion_flag_false', 'file', lambda d: d.__setitem__('complete', False), 'completion: complete flag'),
    ]


GATE_KEYS = tuple(f[0] for f in [('good_full_packet_passes',), ('types_rows_list',), ('types_started_dict',), ('types_elapsed_string',),
                                 ('keys_extra_top_key',), ('keys_stopped_present',), ('keys_row_missing',), ('domains_wrong_digest',),
                                 ('domains_wrong_input',), ('domains_wrong_scope',), ('domains_negative_timing',), ('domains_nan_elapsed',),
                                 ('domains_inf_timing',), ('domains_row_not_hex',), ('domains_first_diff_range',), ('parse_nan_token',),
                                 ('parse_exponent_overflow',), ('bindings_explicit_false_base',), ('bindings_mutant_all_true',),
                                 ('bindings_group_dropped',), ('bindings_move_pairs_changed',), ('arithmetic_word_changed',),
                                 ('arithmetic_stale_report',), ('arithmetic_move_pair_split',), ('arithmetic_move_pair_unbacked',),
                                 ('keys_move_row_missing',), ('arithmetic_summary',), ('completion_flag_false',)])


def gate_controls():
    import copy, tempfile
    sections, timing = assemble(GATE_GROUPS, GATE_T)
    sections = json.loads(json.dumps(sections, allow_nan=False))
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'finished': 'f', 'elapsed_s': 0.1, 'this_sha256': 'S', 'kernel_result_sha256': KERNEL_RESULT_SHA256, 'scope': {'T': GATE_T},
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'timing': timing, 'complete': True, **sections}
    res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', GATE_T, GATE_GROUPS)
        for name, kind, f, want in gate_fixtures():
            bad = copy.deepcopy(good)
            if kind == 'memory':
                f(bad); res[name] = validate_result(bad, 'S', GATE_T, GATE_GROUPS) == want; continue
            if kind == 'text':
                open(rp, 'w').write(f(json.dumps(bad, allow_nan=False)))
            else:
                f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            verdict, note = m(0, '')
            res[name] = (verdict == 'pass') if want is None else (verdict == 'FAIL' and note == (want if kind == 'text' else 'rc 0: ' + want))
    assert set(res) == set(GATE_KEYS) and len(res) == len(GATE_KEYS)
    return res


def stage(out, kpath, T):
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if T != STAGE_T:
        print('REFUSED: the only admitted stage scope is T = 40000'); return 3
    groups = load_groups(kpath); deps()
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01_deeptime'] = {'this_sha256': src_sha, 'kernel_sha256': KERNEL_SHA256, 'kernel_result_sha256': KERNEL_RESULT_SHA256, 'w1a_sha256': W1A_SHA256,
                           'scope': {'T': T}, 'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_deeptime_result.json'), src_sha, T, groups)
    rec = sup.run_step('cq01_deeptime', [sys.executable, os.path.abspath(__file__), 'run', rdir, os.path.abspath(kpath), str(T)], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 4 and a[0] in ('run', 'stage'):
        T = int(a[3])
        if a[0] == 'run':
            if not (400 <= T <= STAGE_T and T % 2 == 0): print('REFUSED: run admits 400 <= T <= 40000, T even'); sys.exit(3)
            R = run(a[1], a[2], T); print('CQ01 DEEPTIME RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
        sys.exit(stage(a[1], a[2], T))
    print(__doc__); sys.exit(2)
