#!/usr/bin/env python3
"""The rare survivors' late-bit patterns: a frozen transfer test to the sealed widths 44 and 48, revision 1 (Local, 2026-10-25, L944;
designed in L943, GC1874's scope repairs). NOT an agreed job until GPT accepts this exact file; nothing runs on import; `--controls`
runs the small CPU controls only, with no data.

If this holds, it changes the all-width D(W) row: L942 found the rare long survivors concentrated in few late-bit classes in-sample
(GC1873: at W = 40 all 537 positives in 66 of 1,024 late-10 classes, 15.515-fold). This asks whether that frozen selector, chosen at
W = 40, still concentrates the survivors at the unseen widths 44 and 48. A success supports ENRICHMENT, not a necessary condition; one
positive outside S40 disproves the exact S40 necessary condition at that width, however strong the enrichment; a failure rejects this
frozen transfer, not every end-bit route (GC1874). Finite, per width; no theorem follows.

The frozen rule (RULE, fixed before either held-out array is opened): n = W/2; lane l carries b_i = a(2i + 1) = bit i of l (CL632);
the late-10 word is w(l) = l >> (n - 10), the bits b_(n-10)..b_(n-1), trace times W - 19, W - 17, .., W - 1, in relative position; the
label is A(l) = 1[2 d(l) > 3W] in integers; S_W = the set of words w(l) over the A-positive lanes. The selector is S40, exactly.

Two supervised phases under one agreement, in this order (GC1874's training-before-held-out ordering):
  1. `stage-select OUT INDIR`: opens only the in-sample tables W = 28, 32, 36, 40 (from INDIR, byte-checked as in death_info_loss.py).
     Computes S_W at each, their sizes (bound to L942's retained counts 10, 21, 43, 66: the late-10 mixed-class counts with e01 = P_A,
     GC1873), the three adjacent nesting transitions |S_W ∩ S_(W+4)| / |S_W| (exploratory: they cannot change the selector), each set's
     word-weight histogram, and writes s40.json (canonical bytes) with its sha256.
  2. Between the phases, Local records S40's 66 words and its sha256 in the ledger and commits; only then are deaths_44.npy and
     deaths_48.npy fetched, into a separate HELDDIR.
  The source must be byte-identical across both phases: the transfer re-validates the select result against its own digest.
  3. `stage-transfer OUT INDIR HELDDIR SELECTOUT S40SHA`: re-validates the select result through its own gate, refuses unless s40.json's
     sha256 equals S40SHA (the committed value), then opens the two held-out tables (pinned digests, histogram bound to GPT's
     file-audit.json) and scores the frozen selector. W = 52 stays sealed and is never opened.
Scored per held-out width W (exact integers; fractions reduced [numerator, denominator]): N = 2^n; P = #A, the prevalence P/N; the
selected lanes #{w(l) in S40} = 66 * 2^(n-10) by the product structure; TP = #{A and selected}; FN = P - TP; recall TP/P (null when
P = 0: undefined, never 1); precision TP/selected; enrichment recall / (66/1024); the exact necessary condition holds iff FN = 0; every
missed positive's word with its count, and the least missed lane as an example; the descriptive negative control: the same recall for
CONTROL_WORDS, a fixed seeded 66-word set (random.Random(20261025).sample(range(1024), 66), its digest pinned), whose expectation over
the draw is 66/1024 but whose single realized value is a description, not a threshold; the maximizers (d = D(W)), how many have their
word in S40, each listed.
Verdicts (fixed now): W = 44 is primary: recall >= 1/2 SUPPORTED (enrichment transfers), recall <= 3/20 REJECTED, otherwise INCONCLUSIVE.
W = 48 corroborates with the same frozen rule: >= 3/10 SUPPORTED, <= 3/20 REJECTED, otherwise INCONCLUSIVE. No tuning after 44, no
automatic follow-up.

Controls (`--controls`, CPU, no data; all must pass before a stage):
  - the word against first principles (each bit read by division) for n = 10..14, every lane; the label edge 2d = 3W is negative;
  - the selected count equals 66 * 2^(n - 10) on synthetic tables, and the scores against a direct per-lane count;
  - S_W, the nesting and the weight histogram against brute force on synthetic tables at W = 20, 24;
  - the control set's digest equals its pin; s40.json's canonical bytes round-trip;
  - five mutants, each of which must fail a control: 'wordlow' (the low ten bits), 'shift' (l >> (n - 9)), 'labelge' (2d >= 3W),
    'swap' (recall and precision exchanged), 'missed' (the missed positives counted among the selected).
The result gates (GC1813's method, GC1870's discipline): bounded bytes, strict reading, one explicit schema per phase in the order types,
exact key sets, domains, input bindings, arithmetic, completion, inside one fail-closed matcher; every comparison type-strict (same());
the control roll-ups recomputed from their Boolean details; the select gate re-reads s40.json from disk and requires its canonical bytes
and digest; the transfer gate recomputes every fraction and verdict from the integers. Valid synthetic packets for both phases are
assembled by the phases' own code from synthetic tables; every negative fixture names its exact diagnostic.
Caps for each phase: W1A stage, step wall and CPU 300 s, group RSS 2 GiB, artifacts 10 MiB, log 5 MiB, the inherited pressure,
swap-growth, free-disk and monitor-failure stops; fresh host headroom and no other research stage.
Predictions (written before any word or held-out value was seen; seen: L942's counts, GC1873's enrichment figures, GPT's histograms):
  N1 (exploratory) at each of the three transitions 28 -> 32, 32 -> 36, 36 -> 40, at least 80% of S_W lies in S_(W+4).
  T1 W = 44: recall >= 1/2 (SUPPORTED); counterfactual <= 3/20 (REJECTED).
  T2 W = 48: recall >= 3/10 (SUPPORTED); counterfactual <= 3/20 (REJECTED).
  T3 the exact S40 necessary condition FAILS at both widths (FN > 0): the set grows with W (10, 21, 43, 66).
  T4 (low confidence) every maximizer at W = 44 (12 lanes) and W = 48 (32 lanes) has its word in S40.
Usage: python3 survivor_transfer.py --controls | select OUT INDIR | transfer OUT INDIR HELDDIR SELECTOUT S40SHA
       | stage-select OUT INDIR | stage-transfer OUT INDIR HELDDIR SELECTOUT S40SHA
"""
import hashlib, io, json, math, os, random, re, sys, tempfile, time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
MANIFEST_V2_SHA256 = '0913be6442cecfaac1d6be52b98bbf260bae8d608868237e82aaaa94ef90b65d'
FILE_AUDIT_SHA256 = '6ee0978f90db553859ee92c4a0dea56a3f056b429d6045eb0eb5f99d2ed5c899'
ARRAY_SHA256 = {28: 'bc08cb56a6a078a0d7ea021d2488e3b8c7c7202ab4a929cfd634404ef1f76b93',
                32: '97be06aaa0f5590c210c6627b50528a0f0573b38602d5b64133996056ff9e7a9',
                36: 'b481d03751b19c7b23cb0963817a1b472669bab145cc3996dd248c788536b712',
                40: '7fe7cfbc6200e52ec749c53d20950539364a3cf283d387b38e2befde44a395b8',
                44: 'cacdf831dda919ab768fc3a2214882bfb4e013eddd07e99091572ebfe3d0450e',
                48: 'a032d6d6e25a798db2f000e063dfe6a8cfd63b30eb49d85151ebf5ccbac9bdcf'}   # copied from manifest-v2 by script
CONTROL_SHA256 = 'c466e178fdcf9fd5472d53614c4a189ac9579e0e8229ed3143d7f9ea38aa6db5'   # words_digest(control_words()), computed by script from the seed
RULE = ('late-10 word w(l) = l >> (n - 10), n = W/2 (bits b_(n-10)..b_(n-1), trace times W - 19 .. W - 1); A = 1[2d > 3W]; '
        'S_W = {w(l) : A(l)}; selector S40')
K = 10
INSAMPLE = (28, 32, 36, 40)
HELDOUT = (44, 48)
SEALED = (52,)
S_COUNTS = {28: 10, 32: 21, 36: 43, 40: 66}
CONTROL_SEED = 20261025
THRESH = {44: (Fraction(1, 2), Fraction(3, 20)), 48: (Fraction(3, 10), Fraction(3, 20))}
STAGE_S = 300
JSON_MAX_BYTES = 64 << 10
MAX_RESULT_BYTES = 4 << 20
MUTANTS = ('wordlow', 'shift', 'labelge', 'swap', 'missed')
BASE_KEYS = ('word_first_principles', 'label_edge', 'scores_direct_count', 'select_brute_force', 'control_pin_and_canonical')
PARSE_FAIL = 'parse: nonfinite or invalid JSON'
HEX64 = re.compile(r'[0-9a-f]{64}')


def same(a, b):
    """Type-strict deep equality (GC1870): 1 is not True and 1.0 is not 1."""
    if type(a) is not type(b): return False
    if isinstance(a, dict): return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list): return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def read_bounded(path, limit):
    with open(path, 'rb') as f:
        raw = f.read(limit + 1)
    if len(raw) > limit: raise SystemExit('REFUSED: %s exceeds %d bytes' % (os.path.basename(path), limit))
    return raw


def verified_json(path, pin):
    raw = read_bounded(path, JSON_MAX_BYTES)
    if hashlib.sha256(raw).hexdigest() != pin: raise SystemExit('REFUSED: %s digest' % os.path.basename(path))
    return json.loads(raw)


def strict_loads(raw):
    def const(tok): raise ValueError('nonfinite constant')
    def flt(tok):
        x = float(tok)
        if not math.isfinite(x): raise ValueError('nonfinite number')
        return x
    return json.loads(raw, parse_constant=const, parse_float=flt)


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def frac(x):
    return None if x is None else [x.numerator, x.denominator]


def control_words():
    return sorted(random.Random(CONTROL_SEED).sample(range(1 << K), 66))


def words_digest(ws):
    return hashlib.sha256(json.dumps(ws, separators=(',', ':')).encode()).hexdigest()


def canonical_s40(ws):
    return json.dumps({'W': 40, 'rule': RULE, 'words': ws}, sort_keys=True, separators=(',', ':')).encode()


def word_of(lanes, n, mutant=''):
    if mutant == 'wordlow': return lanes & ((1 << K) - 1)
    return lanes >> (n - K + 1 if mutant == 'shift' else n - K)


def label_A(d, W, mutant=''):
    return (2 * d >= 3 * W) if mutant == 'labelge' else (2 * d > 3 * W)


def select_width(d, W, mutant=''):
    """S_W as a sorted list of ints, and P_A."""
    import numpy as np
    n = W // 2; lanes = np.arange(1 << n, dtype=np.int64); A = label_A(d, W, mutant)
    return sorted(int(x) for x in np.unique(word_of(lanes[A], n, mutant))), int(A.sum())


def weights(ws):
    h = {}
    for w in ws:
        c = bin(w).count('1'); h[str(c)] = h.get(str(c), 0) + 1
    return dict(sorted(h.items(), key=lambda kv: int(kv[0])))


def nesting(sets):
    return {'%d-%d' % (a, b): [len(set(sets[a]) & set(sets[b])), len(sets[a])] for a, b in zip(INSAMPLE, INSAMPLE[1:])}


def score(d, W, S, thresh, mutant=''):
    """The frozen selector S scored on one table: integers, reduced fractions, the verdict and the missed positives."""
    import numpy as np
    n = W // 2; N = 1 << n; lanes = np.arange(N, dtype=np.int64)
    wd = word_of(lanes, n, mutant); A = label_A(d, W, mutant)
    inS = np.isin(wd, np.array(S, dtype=np.int64)); inC = np.isin(wd, np.array(control_words(), dtype=np.int64))
    P = int(A.sum()); sel = int(inS.sum()); TP = int((A & inS).sum())
    FN = P - TP
    miss = A & ~inS if mutant != 'missed' else A & inS
    mw, mc = np.unique(wd[miss], return_counts=True)
    recall = Fraction(TP, P) if P else None; precision = Fraction(TP, sel) if sel else None
    if mutant == 'swap': recall, precision = precision, recall
    enrich = recall * Fraction(1 << K, len(S)) if (recall is not None and S) else None
    up, down = thresh
    verdict = 'UNDEFINED' if recall is None else ('SUPPORTED' if recall >= up else 'REJECTED' if recall <= down else 'INCONCLUSIVE')
    D = int(d.max()); mx = np.flatnonzero(d == D)
    TPc = int((A & inC).sum())
    return {'N': N, 'P': P, 'prevalence': frac(Fraction(P, N)), 'selected': sel, 'TP': TP, 'FN': FN, 'recall': frac(recall),
            'precision': frac(precision), 'enrichment': frac(enrich), 'verdict': verdict, 'necessary': FN == 0,
            'missed_words': {str(int(a)): int(b) for a, b in zip(mw, mc)},
            'missed_example': (int(np.flatnonzero(miss)[0]) if bool(miss.any()) else None),
            'control': {'TP': TPc, 'recall': frac(Fraction(TPc, P) if P else None)},
            'maximizers': {'D': D, 'count': int(mx.size), 'in_S': int(inS[mx].sum()), 'lanes': [[int(l), int(wd[l]), bool(inS[l])] for l in mx[:64]]}}


def synth_table(W, seed):
    """A synthetic death table (even values in [W, 4W]) with a deliberate concentration of long deaths in a few late words."""
    import numpy as np
    n = W // 2; N = 1 << n; rng = np.random.default_rng(seed)
    d = (W + 2 * rng.integers(0, W // 4, size=N)).astype(np.int64)
    hot = np.isin(np.arange(N, dtype=np.int64) >> (n - K), np.array([3, 77, 500, 900]))
    d[hot] = np.where(rng.random(int(hot.sum())) < 0.6, 2 * W, d[hot])
    stray = rng.random(N) < 0.003
    d[stray] = 2 * W
    return d


def controls(mutant=''):
    import numpy as np
    R = {}
    ok = True
    for n in range(10, 15):
        lanes = np.arange(1 << n, dtype=np.int64); w = word_of(lanes, n, mutant)
        ok = ok and all(int(w[l]) == sum(((l // (1 << (n - K + j))) % 2) << j for j in range(K)) for l in range(0, 1 << n, 37))
    R[BASE_KEYS[0]] = ok
    R[BASE_KEYS[1]] = label_A(np.array([58, 60, 62], dtype=np.int64), 40, mutant).tolist() == [False, False, True]
    d = synth_table(24, 7); S = [3, 77, 500, 900] + list(range(10, 72)); S = sorted(S)
    s = score(d, 24, S, (Fraction(1, 2), Fraction(3, 20)), mutant); n = 12; lanes = np.arange(1 << n)
    A = [2 * int(x) > 72 for x in d]; inS = [int(l) >> (n - K) in set(S) for l in lanes]
    TP = sum(1 for a, i in zip(A, inS) if a and i); P = sum(A)
    R[BASE_KEYS[2]] = (s['selected'] == len(S) * (1 << (n - K)) and s['TP'] == TP and s['FN'] == P - TP and s['P'] == P
                       and s['recall'] == frac(Fraction(TP, P)) and s['precision'] == frac(Fraction(TP, s['selected']))
                       and sum(s['missed_words'].values()) == P - TP and all(int(k) not in set(S) for k in s['missed_words']))
    sets = {}
    for W, seed in ((20, 1), (24, 2)):
        dd = synth_table(W, seed); nn = W // 2
        sets[W] = sorted({l >> (nn - K) for l in range(1 << nn) if 2 * int(dd[l]) > 3 * W})
    got = {W: select_width(synth_table(W, seed), W, mutant)[0] for W, seed in ((20, 1), (24, 2))}
    R[BASE_KEYS[3]] = got == sets and weights(sets[20]) == {str(c): sum(1 for w in sets[20] if bin(w).count('1') == c) for c in sorted({bin(w).count('1') for w in sets[20]})}
    cw = control_words()
    R[BASE_KEYS[4]] = words_digest(cw) == CONTROL_SHA256 and len(cw) == 66 and json.loads(canonical_s40([1, 2]))['words'] == [1, 2]
    return {k: bool(v) for k, v in R.items()}


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def control_problem(c, gc, gate_keys):
    if set(c) != {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}: return 'keys: controls'
    if not all(isinstance(c.get(k), dict) and set(c[k]) == set(BASE_KEYS) and all(type(v) is bool for v in c[k].values()) for k in ('base',) + MUTANTS):
        return 'types: control reports'
    if not all(type(c.get(k)) is bool for k in ('base_all_pass', 'ok') + tuple(m + '_caught' for m in MUTANTS)): return 'types: control roll-ups'
    if set(gc) != set(gate_keys) or not all(type(v) is bool for v in gc.values()): return 'types: gate controls'
    return None


def rollups_problem(c, gc):
    base_all = all(c['base'].values()); caught = {m: not all(c[m].values()) for m in MUTANTS}; ok = base_all and all(caught.values())
    if c['base_all_pass'] is not base_all or c['ok'] is not ok or any(c[m + '_caught'] is not caught[m] for m in MUTANTS): return 'completion: control roll-ups'
    if not ok: return 'completion: controls'
    if not all(v is True for v in gc.values()): return 'completion: gate controls'
    return None


def load_table(path, W, pin, nbytes):
    import numpy as np
    raw = read_bounded(path, nbytes); h = hashlib.sha256(raw).hexdigest()
    if h != pin or len(raw) != nbytes: raise SystemExit('REFUSED: deaths_%d.npy digest' % W)
    a = np.load(io.BytesIO(raw), allow_pickle=False)
    if a.dtype != np.dtype('<u2') or a.shape != (1 << (W // 2),) or np.isfortran(a): raise SystemExit('REFUSED: deaths_%d.npy format' % W)
    d = a.astype(np.int64)
    if bool((d % 2).any()) or int(d.min()) < W or int(d.max()) > 4 * W: raise SystemExit('REFUSED: deaths_%d.npy values' % W)
    return d


def manifest_and_audit(indir):
    man = {f['name']: f for f in verified_json(os.path.join(indir, 'manifest-v2.json'), MANIFEST_V2_SHA256)['files']}
    audit = {f['W']: f for f in verified_json(os.path.join(indir, 'file-audit.json'), FILE_AUDIT_SHA256)['files']}
    return man, audit


def pos_from_hist(h, W):
    return sum(v for k, v in h.items() if 2 * int(k) > 3 * W)


# ---------- phase 1: select ----------

def assemble_select(tabs):
    sets, P = {}, {}
    for W in sorted(tabs):
        sets[W], P[W] = select_width(tabs[W], W)
    top = max(tabs); s40 = sets[top]
    return {'widths': {str(W): {'P_A': P[W], 'S': sets[W], 'count': len(sets[W]), 'weights': weights(sets[W])} for W in sorted(tabs)},
            'nesting': {'%d-%d' % (a, b): [len(set(sets[a]) & set(sets[b])), len(sets[a])] for a, b in zip(sorted(tabs), sorted(tabs)[1:])},
            's40': {'words': s40, 'sha256': hashlib.sha256(canonical_s40(s40)).hexdigest(), 'file': 's40.json'}}


def run_select(out, indir):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': sha(os.path.abspath(__file__)), 'phase': 'select', 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'select_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'select_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    try:
        man, audit = manifest_and_audit(indir)
        tabs = {W: load_table(os.path.join(indir, 'deaths_%d.npy' % W), W, ARRAY_SHA256[W], man['deaths_%d.npy' % W]['bytes']) for W in INSAMPLE}
    except SystemExit as e:
        R['stopped'] = str(e); save(); raise
    R['inputs'] = {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256, 'arrays': {str(W): ARRAY_SHA256[W] for W in INSAMPLE}}
    R.update(assemble_select(tabs))
    open(os.path.join(out, 's40.json'), 'wb').write(canonical_s40(R['s40']['words']))
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    prob = validate_select(R | {'complete': True, 'elapsed_s': 0.0}, R['this_sha256'], expect_select(audit), out)
    R['complete'] = prob is None
    if prob: R['stopped'] = 'incomplete: %s (no retry)' % prob
    save()
    return R


def expect_select(audit):
    return {'widths': INSAMPLE, 'counts': S_COUNTS, 'sha': {W: ARRAY_SHA256[W] for W in INSAMPLE},
            'P': {W: pos_from_hist(audit[W]['histogram'], W) for W in INSAMPLE},
            'inputs': {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256}}


SELECT_KEYS = {'started', 'this_sha256', 'phase', 'controls', 'gate_controls', 'inputs', 'widths', 'nesting', 's40', 'finished', 'complete', 'elapsed_s'}


def validate_select(d, src_sha, ex, outdir):
    isint = lambda x: type(x) is int
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('started', str), ('this_sha256', str), ('phase', str), ('controls', dict), ('gate_controls', dict), ('inputs', dict),
                   ('widths', dict), ('nesting', dict), ('s40', dict), ('finished', str), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float) or not math.isfinite(d['elapsed_s']) or d['elapsed_s'] < 0: return 'types: elapsed_s'
    p = control_problem(d['controls'], d['gate_controls'], SELECT_GATE_KEYS)
    if p: return p
    for W in ex['widths']:
        w = d['widths'].get(str(W))
        if not (isinstance(w, dict) and set(w) == {'P_A', 'S', 'count', 'weights'} and isint(w['P_A']) and isint(w['count'])
                and isinstance(w['S'], list) and all(isint(x) for x in w['S']) and isinstance(w['weights'], dict) and all(isint(v) for v in w['weights'].values())):
            return 'types: W=%d' % W
    s = d['s40']
    if not (set(s) == {'words', 'sha256', 'file'} and isinstance(s['words'], list) and all(isint(x) for x in s['words']) and type(s['sha256']) is str
            and s['file'] == 's40.json'):
        return 'types: s40'
    if set(d) != SELECT_KEYS or d['phase'] != 'select': return 'keys: top level'
    if set(d['widths']) != {str(W) for W in ex['widths']}: return 'keys: widths'
    pairs = ['%d-%d' % (a, b) for a, b in zip(ex['widths'], ex['widths'][1:])]
    if set(d['nesting']) != set(pairs) or not all(isinstance(v, list) and len(v) == 2 and all(isint(x) for x in v) for v in d['nesting'].values()):
        return 'keys: nesting'
    for W in ex['widths']:
        w = d['widths'][str(W)]; S = w['S']
        if S != sorted(set(S)) or not all(0 <= x < (1 << K) for x in S) or w['count'] != len(S) or not 0 <= w['P_A'] <= 1 << (W // 2):
            return 'domains: W=%d' % W
    if not HEX64.fullmatch(s['sha256']): return 'domains: s40 digest'
    if not same(d['inputs'], {**ex['inputs'], 'arrays': {str(W): ex['sha'][W] for W in ex['widths']}}): return 'bindings: input digests'
    for W in ex['widths']:
        w = d['widths'][str(W)]
        if w['P_A'] != ex['P'][W]: return 'bindings: P_A W=%d' % W
        if ex['counts'] is not None and w['count'] != ex['counts'][W]: return 'bindings: S count W=%d' % W
    top = str(max(ex['widths']))
    if not same(s['words'], d['widths'][top]['S']): return 'bindings: s40 words'
    if s['sha256'] != hashlib.sha256(canonical_s40(s['words'])).hexdigest(): return 'bindings: s40 digest'
    try:
        disk = read_bounded(os.path.join(outdir, 's40.json'), JSON_MAX_BYTES)
    except (OSError, SystemExit):
        return 'bindings: s40 file missing'
    if disk != canonical_s40(s['words']): return 'bindings: s40 file bytes'
    for W in ex['widths']:
        w = d['widths'][str(W)]
        if not same(w['weights'], weights(w['S'])): return 'arithmetic: weights W=%d' % W
    for a, b in zip(ex['widths'], ex['widths'][1:]):
        if not same(d['nesting']['%d-%d' % (a, b)], [len(set(d['widths'][str(a)]['S']) & set(d['widths'][str(b)]['S'])), len(d['widths'][str(a)]['S'])]):
            return 'arithmetic: nesting %d-%d' % (a, b)
    p = rollups_problem(d['controls'], d['gate_controls'])
    if p: return p
    if d['this_sha256'] != src_sha: return 'completion: source digest'
    if d['complete'] is not True: return 'completion: complete flag'
    return None


# ---------- phase 3: transfer ----------

def run_transfer(out, indir, helddir, selectout, s40sha):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': sha(os.path.abspath(__file__)), 'phase': 'transfer', 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'transfer_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'transfer_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    try:
        man, audit = manifest_and_audit(indir)
        raw = read_bounded(os.path.join(selectout, 'select_result.json'), MAX_RESULT_BYTES)
        sel = strict_loads(raw)
        prob = validate_select(sel, R['this_sha256'], expect_select(audit), selectout)
        if prob: raise SystemExit('REFUSED: the select result fails its gate: %s' % prob)
        if sel['s40']['sha256'] != s40sha or sha(os.path.join(selectout, 's40.json')) != s40sha: raise SystemExit('REFUSED: s40.json is not the committed digest')
        S = sel['s40']['words']
        tabs = {W: load_table(os.path.join(helddir, 'deaths_%d.npy' % W), W, ARRAY_SHA256[W], man['deaths_%d.npy' % W]['bytes']) for W in HELDOUT}
    except SystemExit as e:
        R['stopped'] = str(e); save(); raise
    R['inputs'] = {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256, 'arrays': {str(W): ARRAY_SHA256[W] for W in HELDOUT}}
    R['select'] = {'result_sha256': hashlib.sha256(raw).hexdigest(), 's40_sha256': s40sha, 'words': S}
    R['control_words_sha256'] = words_digest(control_words())
    R['widths'] = {str(W): score(tabs[W], W, S, THRESH[W]) for W in HELDOUT}
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    prob = validate_transfer(R | {'complete': True, 'elapsed_s': 0.0}, R['this_sha256'], expect_transfer(audit, s40sha))
    R['complete'] = prob is None
    if prob: R['stopped'] = 'incomplete: %s (no retry)' % prob
    save()
    return R


def expect_transfer(audit, s40sha):
    return {'widths': HELDOUT, 'sha': {W: ARRAY_SHA256[W] for W in HELDOUT}, 'audit': {W: audit[W] for W in HELDOUT},
            's40_sha256': s40sha, 'inputs': {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256}, 'thresh': THRESH}


TRANSFER_KEYS = {'started', 'this_sha256', 'phase', 'controls', 'gate_controls', 'inputs', 'select', 'control_words_sha256', 'widths', 'finished',
                 'complete', 'elapsed_s'}
SCORE_KEYS = {'N', 'P', 'prevalence', 'selected', 'TP', 'FN', 'recall', 'precision', 'enrichment', 'verdict', 'necessary', 'missed_words',
              'missed_example', 'control', 'maximizers'}


def fr(x):
    return None if x is None else Fraction(x[0], x[1])


def validate_transfer(d, src_sha, ex):
    isint = lambda x: type(x) is int
    isfrac = lambda x: x is None or (isinstance(x, list) and len(x) == 2 and all(isint(v) for v in x) and x[1] > 0)
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('started', str), ('this_sha256', str), ('phase', str), ('controls', dict), ('gate_controls', dict), ('inputs', dict),
                   ('select', dict), ('control_words_sha256', str), ('widths', dict), ('finished', str), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float) or not math.isfinite(d['elapsed_s']) or d['elapsed_s'] < 0: return 'types: elapsed_s'
    p = control_problem(d['controls'], d['gate_controls'], TRANSFER_GATE_KEYS)
    if p: return p
    sl = d['select']
    if not (set(sl) == {'result_sha256', 's40_sha256', 'words'} and type(sl['result_sha256']) is str and type(sl['s40_sha256']) is str
            and isinstance(sl['words'], list) and all(isint(x) for x in sl['words'])):
        return 'types: select'
    for W in ex['widths']:
        s = d['widths'].get(str(W))
        if not (isinstance(s, dict) and set(s) == SCORE_KEYS): return 'keys: W=%d' % W
        if not (all(isint(s[k]) for k in ('N', 'P', 'selected', 'TP', 'FN')) and all(isfrac(s[k]) for k in ('prevalence', 'recall', 'precision', 'enrichment'))
                and type(s['verdict']) is str and type(s['necessary']) is bool and isinstance(s['missed_words'], dict)
                and all(isint(v) for v in s['missed_words'].values()) and (s['missed_example'] is None or isint(s['missed_example']))
                and isinstance(s['control'], dict) and set(s['control']) == {'TP', 'recall'} and isint(s['control']['TP']) and isfrac(s['control']['recall'])
                and isinstance(s['maximizers'], dict) and set(s['maximizers']) == {'D', 'count', 'in_S', 'lanes'}
                and all(isint(s['maximizers'][k]) for k in ('D', 'count', 'in_S')) and isinstance(s['maximizers']['lanes'], list)
                and all(isinstance(r, list) and len(r) == 3 and isint(r[0]) and isint(r[1]) and type(r[2]) is bool for r in s['maximizers']['lanes'])):
            return 'types: W=%d' % W
    if set(d) != TRANSFER_KEYS or d['phase'] != 'transfer': return 'keys: top level'
    if set(d['widths']) != {str(W) for W in ex['widths']}: return 'keys: widths'
    S = sl['words']
    if S != sorted(set(S)) or not all(0 <= x < (1 << K) for x in S) or not HEX64.fullmatch(sl['s40_sha256']): return 'domains: select'
    for W in ex['widths']:
        s = d['widths'][str(W)]; N = 1 << (W // 2)
        if not (s['N'] == N and 0 <= s['TP'] <= s['P'] <= N and 0 <= s['FN'] and 0 <= s['selected'] <= N and s['verdict'] in ('SUPPORTED', 'REJECTED', 'INCONCLUSIVE', 'UNDEFINED')):
            return 'domains: W=%d' % W
    if not same(d['inputs'], {**ex['inputs'], 'arrays': {str(W): ex['sha'][W] for W in ex['widths']}}): return 'bindings: input digests'
    if sl['s40_sha256'] != ex['s40_sha256'] or sl['s40_sha256'] != hashlib.sha256(canonical_s40(S)).hexdigest(): return 'bindings: s40 digest'
    if d['control_words_sha256'] != CONTROL_SHA256: return 'bindings: control words'
    for W in ex['widths']:
        s = d['widths'][str(W)]; a = ex['audit'][W]; n = W // 2
        if s['P'] != pos_from_hist(a['histogram'], W): return 'bindings: P W=%d' % W
        if s['maximizers']['D'] != a['D'] or s['maximizers']['count'] != a['maximizers']: return 'bindings: maximizers W=%d' % W
        if s['selected'] != len(S) * (1 << (n - K)): return 'bindings: selected W=%d' % W
    for W in ex['widths']:
        s = d['widths'][str(W)]; P, TP, FN = s['P'], s['TP'], s['FN']; up, down = ex['thresh'][W]
        rec = Fraction(TP, P) if P else None
        if FN != P - TP: return 'arithmetic: W=%d TP + FN' % W
        if not same(s['prevalence'], frac(Fraction(P, s['N']))) or not same(s['recall'], frac(rec)) or not same(s['precision'], frac(Fraction(TP, s['selected']) if s['selected'] else None)):
            return 'arithmetic: W=%d fractions' % W
        if not same(s['enrichment'], frac(rec * Fraction(1 << K, len(S)) if rec is not None else None)): return 'arithmetic: W=%d enrichment' % W
        v = 'UNDEFINED' if rec is None else ('SUPPORTED' if rec >= up else 'REJECTED' if rec <= down else 'INCONCLUSIVE')
        if s['verdict'] != v or s['necessary'] is not (FN == 0): return 'arithmetic: W=%d verdict' % W
        mw = s['missed_words']
        if sum(mw.values()) != FN or any(int(k) in set(S) for k in mw) or (FN == 0) != (s['missed_example'] is None):
            return 'arithmetic: W=%d missed' % W
        if s['missed_example'] is not None and str(s['missed_example'] >> (W // 2 - K)) not in mw: return 'arithmetic: W=%d missed' % W
        c = s['control']
        if not same(c['recall'], frac(Fraction(c['TP'], P) if P else None)) or c['TP'] > P: return 'arithmetic: W=%d control' % W
        mxl = s['maximizers']['lanes']
        cnt = s['maximizers']['count']; ins = sum(1 for r in mxl if r[2])
        if (len(mxl) != min(64, cnt) or (s['maximizers']['in_S'] != ins if cnt <= 64 else s['maximizers']['in_S'] < ins)
                or any(r[1] != r[0] >> (W // 2 - K) or r[2] != (r[1] in set(S)) for r in mxl)):
            return 'arithmetic: W=%d maximizers' % W
    p = rollups_problem(d['controls'], d['gate_controls'])
    if p: return p
    if d['this_sha256'] != src_sha: return 'completion: source digest'
    if d['complete'] is not True: return 'completion: complete flag'
    return None


# ---------- gates ----------

def make_matcher(result_path, validate):
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate(d)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'survivor transfer phase complete, every binding held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


def synthetic_controls(gate_keys):
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    return ({'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            {k: True for k in gate_keys})


def synthetic_select(outdir):
    """A valid select packet from synthetic tables at W = 20, 24 (the select rule unchanged; counts unbound)."""
    tabs = {20: synth_table(20, 1), 24: synth_table(24, 2)}
    sec = assemble_select(tabs)
    c, gc = synthetic_controls(SELECT_GATE_KEYS)
    good = {'started': 's', 'this_sha256': 'S', 'phase': 'select', 'controls': c, 'gate_controls': gc, 'finished': 'f', 'complete': True, 'elapsed_s': 0.1,
            'inputs': {'manifest_v2': 'M', 'file_audit': 'F', 'arrays': {'20': 'a20', '24': 'a24'}}, **sec}
    open(os.path.join(outdir, 's40.json'), 'wb').write(canonical_s40(sec['s40']['words']))
    ex = {'widths': (20, 24), 'counts': None, 'sha': {20: 'a20', 24: 'a24'}, 'P': {W: sec['widths'][str(W)]['P_A'] for W in (20, 24)},
          'inputs': {'manifest_v2': 'M', 'file_audit': 'F'}}
    return json.loads(json.dumps(good, allow_nan=False)), ex


def synthetic_transfer():
    """A valid transfer packet: the synthetic W = 24 selector scored on synthetic tables at W = 24 and 28 (as if held out)."""
    S = select_width(synth_table(24, 2), 24)[0]
    tabs = {24: synth_table(24, 3), 28: synth_table(28, 4)}
    audit = {}
    for W in tabs:
        d = tabs[W]; vals = sorted(set(int(x) for x in d)); h = {str(v): int((d == v).sum()) for v in vals}
        audit[W] = {'histogram': h, 'D': max(vals), 'maximizers': h[str(max(vals))]}
    c, gc = synthetic_controls(TRANSFER_GATE_KEYS)
    s40sha = hashlib.sha256(canonical_s40(S)).hexdigest()
    th = {24: (Fraction(1, 2), Fraction(3, 20)), 28: (Fraction(3, 10), Fraction(3, 20))}
    good = {'started': 's', 'this_sha256': 'S', 'phase': 'transfer', 'controls': c, 'gate_controls': gc, 'finished': 'f', 'complete': True,
            'elapsed_s': 0.1, 'inputs': {'manifest_v2': 'M', 'file_audit': 'F', 'arrays': {'24': 'b24', '28': 'b28'}},
            'select': {'result_sha256': '0' * 64, 's40_sha256': s40sha, 'words': S}, 'control_words_sha256': CONTROL_SHA256,
            'widths': {str(W): score(tabs[W], W, S, th[W]) for W in tabs}}
    ex = {'widths': (24, 28), 'sha': {24: 'b24', 28: 'b28'}, 'audit': audit, 's40_sha256': s40sha, 'inputs': {'manifest_v2': 'M', 'file_audit': 'F'},
          'thresh': th}
    return json.loads(json.dumps(good, allow_nan=False)), ex


def put(path, val):
    def f(d):
        x = d
        for p in path[:-1]: x = x[p]
        x[path[-1]] = val
    return f


def select_fixtures():
    def bump_P(d): d['widths']['24']['P_A'] += 1
    def nest(d): d['nesting']['20-24'][0] += 1
    return [
        ('good_select_passes', put(['finished'], 'f'), None),
        ('types_s40_not_dict', put(['s40'], []), 'types: s40'),
        ('types_rollup_integer', put(['controls', 'ok'], 1), 'types: control roll-ups'),
        ('keys_extra_top', put(['extra'], 1), 'keys: top level'),
        ('keys_nesting_missing', lambda d: d['nesting'].clear(), 'keys: nesting'),
        ('domains_unsorted_words', lambda d: d['widths']['20']['S'].reverse() if len(d['widths']['20']['S']) > 1 else None, 'domains: W=20'),
        ('domains_s40_digest_empty', put(['s40', 'sha256'], ''), 'domains: s40 digest'),
        ('bindings_input', put(['inputs', 'manifest_v2'], 'X'), 'bindings: input digests'),
        ('bindings_P_A', bump_P, 'bindings: P_A W=24'),
        ('bindings_s40_words', lambda d: d['s40']['words'].pop(), 'bindings: s40 words'),
        ('bindings_s40_digest_wrong_hex', put(['s40', 'sha256'], '0' * 64), 'bindings: s40 digest'),
        ('arithmetic_weights', put(['widths', '20', 'weights'], {}), 'arithmetic: weights W=20'),
        ('arithmetic_nesting', nest, 'arithmetic: nesting 20-24'),
        ('completion_base_false_rollup_true', put(['controls', 'base', BASE_KEYS[0]], False), 'completion: control roll-ups'),
        ('completion_mutant_uncaught', lambda d: d['controls'].__setitem__('swap', {k: True for k in BASE_KEYS}), 'completion: control roll-ups'),
        ('completion_source', put(['this_sha256'], 'T'), 'completion: source digest'),
        ('completion_flag', put(['complete'], False), 'completion: complete flag'),
    ]


def transfer_fixtures():
    def tp_up(d): d['widths']['24']['TP'] += 1
    def verdict(d): d['widths']['24']['verdict'] = 'SUPPORTED' if d['widths']['24']['verdict'] != 'SUPPORTED' else 'REJECTED'
    def miss(d):
        mw = d['widths']['28']['missed_words']
        if mw: k = sorted(mw)[0]; mw[k] += 1
        else: mw['1023'] = 1
    def mx(d):
        r = d['widths']['24']['maximizers']['lanes'][0]; r[2] = not r[2]
    return [
        ('good_transfer_passes', put(['finished'], 'f'), None),
        ('types_select_null', put(['select'], None), 'types: select'),
        ('types_necessary_integer', put(['widths', '24', 'necessary'], 1), 'types: W=24'),
        ('types_recall_float', put(['widths', '24', 'recall'], 0.5), 'types: W=24'),
        ('keys_extra_score', put(['widths', '24', 'extra'], 1), 'keys: W=24'),
        ('domains_verdict', put(['widths', '24', 'verdict'], 'MAYBE'), 'domains: W=24'),
        ('bindings_s40_digest', put(['select', 's40_sha256'], '0' * 64), 'bindings: s40 digest'),
        ('bindings_control_words', put(['control_words_sha256'], '0' * 64), 'bindings: control words'),
        ('bindings_P', lambda d: d['widths']['24'].__setitem__('P', d['widths']['24']['P'] + 1), 'bindings: P W=24'),
        ('bindings_selected', lambda d: d['widths']['28'].__setitem__('selected', d['widths']['28']['selected'] + 1), 'bindings: selected W=28'),
        ('arithmetic_tp', tp_up, 'arithmetic: W=24 TP + FN'),
        ('arithmetic_verdict', verdict, 'arithmetic: W=24 verdict'),
        ('arithmetic_missed', miss, 'arithmetic: W=28 missed'),
        ('arithmetic_maximizer_flag', mx, 'arithmetic: W=24 maximizers'),
        ('completion_rollup', put(['controls', 'base', BASE_KEYS[1]], False), 'completion: control roll-ups'),
        ('completion_flag', put(['complete'], False), 'completion: complete flag'),
    ]


GATE_KEYS = (tuple('select:' + f[0] for f in select_fixtures()) + ('select:parse_nan_text', 'select:s40_file_missing')
             + tuple('transfer:' + f[0] for f in transfer_fixtures()) + ('transfer:parse_nan_text',))
SELECT_GATE_KEYS = TRANSFER_GATE_KEYS = GATE_KEYS


def gate_controls():
    """Every fixture of both gates must produce EXACTLY its stated diagnostic, the positive ones a pass."""
    import copy
    res = {}
    with tempfile.TemporaryDirectory() as t:
        good, ex = synthetic_select(t); rp = os.path.join(t, 'select_result.json')
        m = make_matcher(rp, lambda d: validate_select(d, 'S', ex, t))
        for name, f, want in select_fixtures():
            bad = copy.deepcopy(good); f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            v, note = m(0, ''); res['select:' + name] = (v == 'pass') if want is None else (v == 'FAIL' and note == 'rc 0: ' + want)
        open(rp, 'w').write(json.dumps(good, allow_nan=False).replace('"elapsed_s": 0.1', '"elapsed_s": NaN'))
        v, note = m(0, ''); res['select:parse_nan_text'] = v == 'FAIL' and note == PARSE_FAIL
        os.remove(os.path.join(t, 's40.json')); json.dump(good, open(rp, 'w'), allow_nan=False)
        v, note = m(0, ''); res['select:s40_file_missing'] = v == 'FAIL' and note == 'rc 0: bindings: s40 file missing'
        good, ex = synthetic_transfer(); rp = os.path.join(t, 'transfer_result.json')
        m = make_matcher(rp, lambda d: validate_transfer(d, 'S', ex))
        for name, f, want in transfer_fixtures():
            bad = copy.deepcopy(good); f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            v, note = m(0, ''); res['transfer:' + name] = (v == 'pass') if want is None else (v == 'FAIL' and note == 'rc 0: ' + want)
        open(rp, 'w').write(json.dumps(good, allow_nan=False).replace('"elapsed_s": 0.1', '"elapsed_s": NaN'))
        v, note = m(0, ''); res['transfer:parse_nan_text'] = v == 'FAIL' and note == PARSE_FAIL
    return res


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('SURVIVOR TRANSFER CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def supervised(out, step, argv, result_name, validate):
    import w1a_harness as H
    if sha(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    src_sha = sha(os.path.abspath(__file__))
    caps = {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 2 << 30, 'artifacts_max_bytes': 10 << 20,
            'log_max_bytes': 5 << 20}
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 2 << 30; H.CAPS['artifacts_max_bytes'] = 10 << 20; H.CAPS['log_max_bytes'] = 5 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['survivor_transfer'] = {'this_sha256': src_sha, 'w1a_sha256': W1A_SHA256, 'phase': step, 'argv_tail': argv[-3:] if step == 'transfer' else [],
                               'sealed': list(SEALED), 'caps': caps}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, result_name), lambda d: validate(d, src_sha, rdir))
    rec = sup.run_step('survivor_' + step, [sys.executable, os.path.abspath(__file__), step, rdir] + argv, out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


def stage_select(out, indir):
    if not os.path.isabs(indir): print('REFUSED: INDIR absolute'); return 3
    try:
        _, audit = manifest_and_audit(indir)
    except SystemExit as e:
        print('STOP:', e); return 1
    return supervised(out, 'select', [indir], 'select_result.json', lambda d, s, rdir: validate_select(d, s, expect_select(audit), rdir))


def stage_transfer(out, indir, helddir, selectout, s40sha):
    if not all(os.path.isabs(p) for p in (indir, helddir, selectout)) or not HEX64.fullmatch(s40sha):
        print('REFUSED: INDIR, HELDDIR, SELECTOUT absolute and S40SHA 64-hex'); return 3
    try:
        _, audit = manifest_and_audit(indir)
    except SystemExit as e:
        print('STOP:', e); return 1
    return supervised(out, 'transfer', [indir, helddir, selectout, s40sha], 'transfer_result.json',
                      lambda d, s, rdir: validate_transfer(d, s, expect_transfer(audit, s40sha)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 3 and a[0] == 'select':
        R = run_select(a[1], a[2]); print('SURVIVOR SELECT', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 6 and a[0] == 'transfer':
        R = run_transfer(*a[1:]); print('SURVIVOR TRANSFER', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 3 and a[0] == 'stage-select':
        sys.exit(stage_select(a[1], a[2]))
    if len(a) == 6 and a[0] == 'stage-transfer':
        sys.exit(stage_transfer(*a[1:]))
    print(__doc__); sys.exit(2)
