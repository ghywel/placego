#!/usr/bin/env python3
"""CQ01 census, revision 2 (Local, 2026-10-24, L900; GPT's GC1812: the four mutants run inside the stage and are required; the final
gate binds the source digest, scope, exact controls, the mutation report, one row per grid point, finite L < E <= K with zero censoring,
maximizers, witnesses and recomputed monotonicity, on bounded result bytes; K > L_MAX required; a censored row has E unknown (E > K) and
only a max_observed_death; GC1812's false-acceptance packets are gate controls). Revision 1 (Local, 2026-10-24, L899; CL624 item 4, job 2; GPT's GC1804 finite specification, Local's carrying read L898).
NOT an agreed job until GPT accepts this exact file; nothing runs on import; `--controls` runs the small CPU controls only.

The object. For a finitely supported right half R (positions 1..B) and a left support bound L, the kit's `truncation_death`
(Rule30PeriodTwoSideways, 3eca23c) says: the left row `truncate (Psi R) L` keeps the center of `glue . R` alternating at every time
t < d and fails at d, where d is the first depth k > L with `Psi R k = true`. Every left row with support within L first differs from
`Psi R` at a depth <= d (it is white at d), so by `exact_death_center` it fails by time d. Hence
    E(L, B) = max over R supported in 1..B of d(R, L)
is the longest-surviving alternation from finite configurations with left support within L and right support within B: the
two-sided analogue of D(W). CQ01 says d(R, L) is finite for every finite R and every L. Over all supports there is no bound (the kit's
`alternates_long`), so E grows with L + B; the census measures how.

The method, exactly the kit's definitions, computed for all 2^B right halves at once as lane words (lane r: R p = bit p-1 of r):
  1. drive the right half by the alternating column (`drv altCol R`: column 0 black at even times, white at odd; new(p) =
     rule(old(p-1), old(p), old(p+1)), rule(a, b, c) = a xor (b or c)), on positions 1..B+T+1, exact because black cells start within
     1..B and spread at most one cell per step;
  2. read u R s = column 1 at time 2s+1 (s < S), the visible word;
  3. form the trace a(2s) = black, a(2s+1) = not u R s (`Psi_col`), and reconstruct `Psi R k = recon a k 0` for k = 1..K (K <= 2S),
     the kit's `recon` (depth 0 the wall; recon a 1 t = a t; recon a (k+2) t = xor (recon a (k+1) (t+1)) (recon a (k+1) t || recon a k t)),
     keeping three rows of the triangle;
  4. for each L, d(R, L) = the first k in (L, K] with Psi R k black; lanes with none are CENSORED (d > K), never a value.
Reported per (L, B): E(L, B), its maximizing lanes (count, smallest lane, the right row), and the censored count. The witness for a
maximizer is the configuration glue(truncate(Psi R, L), R), re-simulated by the independent whole-line engine below.

Controls (`--controls`, CPU only, small), all of which must pass before a stage:
  - independent whole-line brute force: every left row with support in 1..L and every right row in 1..B (L, B <= 4), a black center,
    plain rule 30 on a finite window wide enough to be exact, the first time the center differs from 1, 0, 1, 0, ...; its maximum over
    all configurations must equal E(L, B) from the lane path, with the same failure time per lane for the truncated-Psi row;
  - the word sets of GC1804: for L, B <= 3 and n <= 3, the distinct visible words of whole-line configurations alternating through 2n
    must equal J(L, B, n) = { R's word : Psi R k white for L < k <= 2n };
  - GC1804's n = 1 endpoint: F_v(2) = v(0), and the row with black cells at -1, 0, 1 has v(0) = 0 and alternates through time 2;
  - GC1804's four mutants, each of which must make a control fail: the complement (a(2s+1) = u R s); one extra step (failure read at
    k + 1); an artificial tail clamp (the right row cut to B positions every step); multiplicity (words counted with repetition).
Also in the controls: the whole-word summary used by the census equals the per-lane path (L <= 7, B <= 6). In the run: each B's
maximizing witness at L = L_MAX is re-simulated by the whole-line engine and must fail exactly at E; E must be monotone in L and in B
(nested supports); no lane may be censored; any failure leaves the run incomplete.

Finite E is the FIRST FAILURE time; the longest inclusive alternation is E - 1 (GC1812).
Proposed stage: L_MAX = 80, B_MAX = 20, K = 400; W1A caps: stage, step wall and CPU 1,800 s, group RSS 4 GiB, artifacts 50 MiB.
Predictions (written before any agreed run, L899, BUT after seeing the development table for L <= 12, B <= 10 and the censoring and
monotonicity of an unagreed timing run at L <= 80, B <= 14, K = 400, whose values were not read and whose output was deleted; GC1812): complete, no censoring at K = 400, monotone, every witness re-simulates to E;
E(L, B) <= 1.5 L + 10 everywhere on the grid; E(80, 20) in [85, 130]; the gain from the right half small, E(L, 20) - E(L, 0) <= 20 for
every L; and, unlike D(W) (about 1.8 W with the white wall), the coupled alternation fails within about 1.2 L + 10 of its support for
most L. Counterfactual: E(L, B) close to 2 L or more would say the right half buys a lot of alternation, and the D(W) comparison would
reverse; censoring at K = 400 would say K was too small, not a value.
Usage: python3 cq01_census.py --controls | run OUT L_MAX B_MAX K | stage OUT L_MAX B_MAX K
OUTCOME: (to be filled after the run)
"""
import json, os, sys, time


def popcount(x):
    return bin(x).count('1')               # Python 3.9 has no int.bit_count


def pat(B, j):
    return sum(1 << r for r in range(1 << B) if (r >> j) & 1)


def lane_psi(B, K, mutant=''):
    """Psi R k for k = 1..K as lane words over all 2^B right halves; also the visible-word lanes U_s."""
    n = 1 << B; ALL = (1 << n) - 1; S = (K + 1) // 2; T = 2 * S
    P = B + T + 1
    w = [0] * (P + 2)
    for p in range(1, B + 1): w[p] = pat(B, p - 1)
    U = []
    for t in range(T):
        col0 = ALL if t % 2 == 0 else 0
        if mutant == 'clamp':
            for p in range(B + 1, P + 2): w[p] = 0
        nw = [0] * (P + 2)
        prev = col0
        for p in range(1, P + 1):
            nw[p] = prev ^ (w[p] | w[p + 1])
            prev = w[p]
        w = nw
        if t % 2 == 0:                       # w now holds time t + 1, an odd time
            U.append(w[1])
    a = []
    for s in range(S):
        a.append(ALL)
        a.append(U[s] if mutant == 'complement' else ALL ^ U[s])
    psi = [0] * (K + 1)
    r0 = [0] * (K + 1); r1 = a[:K + 1] + [0] * max(0, K + 1 - len(a))
    psi[1] = r1[0]
    for k in range(0, K - 1):                # build depth k + 2 from depths k + 1 and k
        m = K - (k + 2) + 1
        r2 = [r1[t + 1] ^ (r1[t] | r0[t]) for t in range(m)]
        psi[k + 2] = r2[0]
        r0, r1 = r1, r2
    return psi, U, ALL


def death_by_lane(psi, L, K, ALL, mutant=''):
    alive = ALL; d = {}
    for k in range(L + 1, K + 1):
        dead = alive & psi[k]
        if dead:
            kk = k + 1 if mutant == 'step' else k
            x = dead
            while x:
                low = x & -x; d[low.bit_length() - 1] = kk; x ^= low
            alive &= ~psi[k]
        if not alive: break
    censored = [i for i in range(ALL.bit_length()) if (alive >> i) & 1]
    return d, censored


def death_summary(psi, L, K, ALL):
    """The census's whole-word path: E (the largest first-black depth beyond L over all lanes), the word of lanes attaining it, and the
    censored word (no black depth in (L, K]). Equal to death_by_lane's per-lane maximum by construction; checked in the controls."""
    alive = ALL; best = None; bestw = 0
    for k in range(L + 1, K + 1):
        dead = alive & psi[k]
        if dead:
            best, bestw = k, dead; alive &= ~psi[k]
        if not alive: break
    return best, bestw, alive


def E(L, B, K, mutant=''):
    psi, U, ALL = lane_psi(B, K, mutant)
    d, cens = death_by_lane(psi, L, K, ALL, mutant)
    m = max(d.values()) if d else None
    mx = sorted(r for r, v in d.items() if v == m)
    return {'L': L, 'B': B, 'K': K, 'E': m, 'maximizers': len(mx), 'min_lane': mx[0] if mx else None, 'censored': len(cens), 'per_lane': d, 'psi': psi, 'U': U}


def whole_line(left, right, Tmax):
    """Plain rule 30 from glue(left, right) with a black center; the first time the center is not 1, 0, 1, 0, ... (None if alternating
    through Tmax); and the visible word, column 1 at times 1, 3, 5, ... while the center alternates."""
    Lw = len(left); Bw = len(right); off = Lw + Tmax + 2
    cells = [0] * (off + Bw + Tmax + 3)
    for k in range(1, Lw + 1): cells[off - k] = left[k - 1]
    cells[off] = 1
    for p in range(1, Bw + 1): cells[off + p] = right[p - 1]
    word = []
    for t in range(Tmax + 1):
        if cells[off] != (1 if t % 2 == 0 else 0): return t, word
        if t % 2 == 1: word.append(cells[off + 1])
        cells = [0] + [cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(cells) - 1)] + [0]
    return None, word


def brute_E(L, B, Tmax):
    best = None
    for lm in range(1 << L):
        left = [(lm >> j) & 1 for j in range(L)]
        for rm in range(1 << B):
            right = [(rm >> j) & 1 for j in range(B)]
            f, _ = whole_line(left, right, Tmax)
            if f is None: return 'censored'
            best = f if best is None else max(best, f)
    return best


def J_lane(L, B, n, K, mutant=''):
    psi, U, ALL = lane_psi(B, K, mutant)
    out = []
    for r in range(1 << B):
        if all(not ((psi[k] >> r) & 1) for k in range(L + 1, 2 * n + 1)):
            out.append(tuple((U[s] >> r) & 1 for s in range(n)))
    return out if mutant == 'multiplicity' else sorted(set(out))


def J_brute(L, B, n):
    words = set()
    for lm in range(1 << L):
        left = [(lm >> j) & 1 for j in range(L)]
        for rm in range(1 << B):
            right = [(rm >> j) & 1 for j in range(B)]
            f, word = whole_line(left, right, 2 * n)
            if f is None or f > 2 * n:
                words.add(tuple(word[:n]))
    return sorted(words)


def controls(mutant=''):
    res = {}; K = 40; T = 60
    ok = True
    for L in range(0, 5):
        for B in range(0, 5):
            e = E(L, B, K, mutant); b = brute_E(L, B, T)
            ok = ok and e['censored'] == 0 and b != 'censored' and e['E'] == b
    res['E_equals_whole_line_brute_force_L_B_le_4'] = ok
    ok = True                                              # per lane: the truncated-Psi row fails exactly at d(R, L)
    for L in range(0, 6):
        for B in range(0, 6):
            e = E(L, B, K, mutant)
            for r, dv in e['per_lane'].items():
                left = [(e['psi'][k] >> r) & 1 for k in range(1, L + 1)]; right = [(r >> j) & 1 for j in range(B)]
                f, _ = whole_line(left, right, T)
                ok = ok and f == dv
    res['per_lane_truncated_psi_fails_at_d_L_B_le_5'] = ok
    ok = True                                              # the whole-word summary equals the per-lane path
    for L in range(0, 8):
        for B in range(0, 7):
            e = E(L, B, K, mutant); best, bw, alive = death_summary(e['psi'], L, K, (1 << (1 << B)) - 1)
            mx = sorted(r for r, v in e['per_lane'].items() if v == e['E'])
            ok = ok and best == (e['E'] if mutant != 'step' else (e['E'] - 1 if e['E'] else None)) and popcount(bw) == len(mx) and popcount(alive) == e['censored']
    res['summary_equals_per_lane_L_le_7_B_le_6'] = ok
    ok = True
    for L in range(0, 4):
        for B in range(0, 4):
            for n in range(0, 4):
                ok = ok and J_lane(L, B, n, K, mutant) == J_brute(L, B, n)
    res['J_equals_whole_line_words_L_B_n_le_3'] = ok
    e = E(1, 1, K, mutant)
    psi, U = e['psi'], e['U']
    lane = 1                                               # R = {1}
    v0 = (U[0] >> lane) & 1; F2 = (psi[2] >> lane) & 1
    f, _ = whole_line([1], [1], 2)
    res['endpoint_n1_F2_equals_v0_and_row_alternates'] = F2 == v0 and v0 == 0 and (f is None or f > 2)
    return res


MUTANTS = ('complement', 'step', 'clamp', 'multiplicity')
BASE_KEYS = ('E_equals_whole_line_brute_force_L_B_le_4', 'per_lane_truncated_psi_fails_at_d_L_B_le_5', 'summary_equals_per_lane_L_le_7_B_le_6',
             'J_equals_whole_line_words_L_B_n_le_3', 'endpoint_n1_F2_equals_v0_and_row_alternates')


def control_report():
    base = controls(); report = {'base': base, 'base_all_pass': sorted(base) == sorted(BASE_KEYS) and all(v is True for v in base.values())}
    for m in MUTANTS:
        r = controls(m); report[m] = r; report[m + '_caught'] = not all(r.values())
    report['ok'] = report['base_all_pass'] and all(report[m + '_caught'] is True for m in MUTANTS)
    return report


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, L_MAX, B_MAX, K):
    """The grid: E(L, B) for 0 <= L <= L_MAX, 0 <= B <= B_MAX at horizon K (K > L_MAX); one lane pass per B serves every L."""
    import hashlib
    os.makedirs(out, exist_ok=True); t0 = time.monotonic()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'scope': {'L_MAX': L_MAX, 'B_MAX': B_MAX, 'K': K}, 'rows': [], 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_result.json.tmp'); json.dump(R, open(tmp, 'w')); os.replace(tmp, os.path.join(out, 'cq01_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    for B in range(B_MAX + 1):
        tb = time.monotonic(); psi, U, ALL = lane_psi(B, K)
        for L in range(L_MAX + 1):
            m, mw, alive = death_summary(psi, L, K, ALL)
            row = {'L': L, 'B': B, 'censored': popcount(alive)}
            if alive:                                          # censored: E unknown (E > K); a finite maximum is only an observed one
                row['E'] = None; row['max_observed_death'] = m
            else:
                row['E'] = m; row['maximizers'] = popcount(mw); row['min_lane'] = (mw & -mw).bit_length() - 1
                r = row['min_lane']; row['witness_right'] = [(r >> j) & 1 for j in range(B)]; row['witness_left'] = [(psi[k] >> r) & 1 for k in range(1, L + 1)]
            R['rows'].append(row)
        R.setdefault('lane_pass_s', {})[str(B)] = round(time.monotonic() - tb, 2); save()
    R['censored_total'] = sum(r['censored'] for r in R['rows'])
    R['witness_resim'] = {}
    for r in R['rows']:
        if r['L'] == L_MAX and r.get('E') is not None:
            f, _ = whole_line(r['witness_left'], r['witness_right'], r['E'] + 2); R['witness_resim'][str(r['B'])] = f
    tab = {(r['L'], r['B']): r['E'] for r in R['rows']}
    fin = all(v is not None for v in tab.values())
    R['monotone_in_L_and_B'] = fin and all((L == 0 or tab[(L - 1, B)] <= tab[(L, B)]) and (B == 0 or tab[(L, B - 1)] <= tab[(L, B)])
                                           for L in range(L_MAX + 1) for B in range(B_MAX + 1))
    R['complete'] = R['censored_total'] == 0 and R['monotone_in_L_and_B'] and all(R['witness_resim'].get(str(B)) == tab[(L_MAX, B)] for B in range(B_MAX + 1))
    if not R['complete']: R['stopped'] = 'incomplete: censoring, monotonicity or a witness mismatch (no K raise, no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 64 << 20


def make_matcher(result_path, src_sha, L_MAX, B_MAX, K):
    """The final gate (GC1812): the exact contract, checked structurally on bounded result bytes."""
    def check(d):
        probs = []
        if d.get('this_sha256') != src_sha: probs.append('source digest')
        if d.get('scope') != {'L_MAX': L_MAX, 'B_MAX': B_MAX, 'K': K}: probs.append('scope')
        c = d.get('controls') or {}
        base = c.get('base') or {}
        if sorted(base) != sorted(BASE_KEYS) or not all(base.get(k) is True for k in BASE_KEYS): probs.append('base controls')
        if not all(isinstance(c.get(m), dict) and c.get(m + '_caught') is True for m in MUTANTS): probs.append('mutation report')
        gc = d.get('gate_controls') or {}
        if not gc or not all(v is True for v in gc.values()): probs.append('gate controls')
        rows = d.get('rows') if isinstance(d.get('rows'), list) else []
        keys = [(r.get('L'), r.get('B')) for r in rows]
        want = [(L, B) for B in range(B_MAX + 1) for L in range(L_MAX + 1)]
        if sorted(keys) != sorted(want) or len(set(keys)) != len(keys): probs.append('grid rows')
        tab = {}
        for r in rows:
            E, L, B = r.get('E'), r.get('L'), r.get('B')
            ok = (type(E) is int and type(L) is int and type(B) is int and L < E <= K and r.get('censored') == 0
                  and type(r.get('maximizers')) is int and r['maximizers'] >= 1 and type(r.get('min_lane')) is int and 0 <= r['min_lane'] < (1 << (1 << B))
                  and isinstance(r.get('witness_left'), list) and len(r['witness_left']) == L and isinstance(r.get('witness_right'), list) and len(r['witness_right']) == B)
            if not ok: probs.append('row %s' % ((L, B),)); break
            tab[(L, B)] = E
        if len(tab) == len(want):
            mono = all((L == 0 or tab[(L - 1, B)] <= tab[(L, B)]) and (B == 0 or tab[(L, B - 1)] <= tab[(L, B)]) for L in range(L_MAX + 1) for B in range(B_MAX + 1))
            if not mono: probs.append('monotonicity')
            ws = d.get('witness_resim') or {}
            if sorted(ws) != sorted(str(B) for B in range(B_MAX + 1)) or not all(ws[str(B)] == tab[(L_MAX, B)] for B in range(B_MAX + 1)): probs.append('witness re-simulation')
        if d.get('complete') is not True: probs.append('complete flag')
        return probs

    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            d = json.loads(raw)
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        probs = check(d) if isinstance(d, dict) else ['not an object']
        if rc != 0 or probs:
            return 'FAIL', 'rc %s problems %s' % (rc, probs[:6])
        import hashlib
        return 'pass', 'CQ01 census complete: %d values, none censored, monotone; result sha256 %s' % (len(d['rows']), hashlib.sha256(raw).hexdigest())
    matcher.check = check
    return matcher


def gate_controls():
    """GC1812's synthetic packets at a one-cell grid (L_MAX = 0, B_MAX = 0, K = 4): the good one passes, each defect fails."""
    import copy, tempfile
    res = {}
    good = {'this_sha256': 'S', 'scope': {'L_MAX': 0, 'B_MAX': 0, 'K': 4}, 'complete': True,
            'controls': {'base': {k: True for k in BASE_KEYS}, **{m: {'x': False} for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {'g': True},
            'rows': [{'L': 0, 'B': 0, 'E': 1, 'censored': 0, 'maximizers': 1, 'min_lane': 0, 'witness_left': [], 'witness_right': []}],
            'witness_resim': {'0': 1}}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', 0, 0, 4)
        def v(doc):
            json.dump(doc, open(rp, 'w')); return m(0, '')[0]
        res['good_one_cell_packet_passes'] = v(good) == 'pass'
        bad = copy.deepcopy(good); bad['controls'] = {'base': {'x': True}}; res['minimal_arbitrary_control_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); del bad['controls']; res['controls_absent_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['scope'] = {'L_MAX': 1, 'B_MAX': 0, 'K': 4}; bad['this_sha256'] = '0' * 64; res['wrong_scope_and_digest_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['rows'][0]['censored'] = 1; res['censored_lane_with_complete_true_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['rows'].append(copy.deepcopy(bad['rows'][0])); res['duplicate_grid_row_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['controls']['base'][BASE_KEYS[0]] = False; res['explicit_false_control_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['rows'] = []; res['missing_grid_row_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['controls']['clamp_caught'] = False; res['uncaught_mutant_fails'] = v(bad) == 'FAIL'
        bad = copy.deepcopy(good); bad['witness_resim'] = {'0': 2}; res['witness_mismatch_fails'] = v(bad) == 'FAIL'
    return res


W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_S = 1800


def stage(out, L_MAX, B_MAX, K):
    import hashlib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if not (0 <= L_MAX <= 80 and 0 <= B_MAX <= 20 and L_MAX < K <= 400):
        print('REFUSED: scope outside 0 <= L_MAX <= 80, 0 <= B_MAX <= 20, L_MAX < K <= 400'); return 3
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01'] = {'this_sha256': src_sha, 'w1a_sha256': W1A_SHA256, 'scope': {'L_MAX': L_MAX, 'B_MAX': B_MAX, 'K': K},
                  'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_result.json'), src_sha, L_MAX, B_MAX, K)
    rec = sup.run_step('cq01_census', [sys.executable, os.path.abspath(__file__), 'run', rdir, str(L_MAX), str(B_MAX), str(K)], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 5 and a[0] == 'run':
        R = run(a[1], int(a[2]), int(a[3]), int(a[4])); print('CQ01 RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 5 and a[0] == 'stage':
        sys.exit(stage(a[1], int(a[2]), int(a[3]), int(a[4])))
    print(__doc__); sys.exit(2)
