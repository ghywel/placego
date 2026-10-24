#!/usr/bin/env python3
"""CQ01 census, revision 1 (Local, 2026-10-24, L899; CL624 item 4, job 2; GPT's GC1804 finite specification, Local's carrying read L898).
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

Proposed stage: L_MAX = 80, B_MAX = 20, K = 400; W1A caps: stage, step wall and CPU 1,800 s, group RSS 4 GiB, artifacts 50 MiB.
Predictions (written before any agreed run, L899): complete, no censoring at K = 400, monotone, every witness re-simulates to E;
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


def all_controls():
    base = controls(); report = {'base': base}
    report['base_all_pass'] = all(base.values())
    for m in ('complement', 'step', 'clamp', 'multiplicity'):
        r = controls(m); report[m] = r; report[m + '_caught'] = not all(r.values())
    ok = report['base_all_pass'] and all(report[m + '_caught'] for m in ('complement', 'step', 'clamp', 'multiplicity'))
    print(json.dumps(report, indent=1)); print('CQ01 CONTROLS', 'PASS' if ok else 'FAIL'); return ok


W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_S = 1800


def run(out, L_MAX, B_MAX, K):
    """The grid: E(L, B) for 0 <= L <= L_MAX, 0 <= B <= B_MAX at horizon K; one lane pass per B serves every L."""
    import hashlib
    os.makedirs(out, exist_ok=True); t0 = time.monotonic()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'scope': {'L_MAX': L_MAX, 'B_MAX': B_MAX, 'K': K}, 'controls': controls(), 'rows': [], 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_result.json.tmp'); json.dump(R, open(tmp, 'w')); os.replace(tmp, os.path.join(out, 'cq01_result.json'))
    save()
    if not all(R['controls'].values()):
        R['stopped'] = 'a control failed'; save(); raise SystemExit(1)
    for B in range(B_MAX + 1):
        tb = time.monotonic(); psi, U, ALL = lane_psi(B, K)
        for L in range(L_MAX + 1):
            m, mw, alive = death_summary(psi, L, K, ALL)
            row = {'L': L, 'B': B, 'E': m, 'maximizers': popcount(mw), 'min_lane': (mw & -mw).bit_length() - 1 if mw else None, 'censored': popcount(alive)}
            if mw:
                r = row['min_lane']; row['witness_right'] = [(r >> j) & 1 for j in range(B)]; row['witness_left'] = [(psi[k] >> r) & 1 for k in range(1, L + 1)]
            R['rows'].append(row)
        R.setdefault('lane_pass_s', {})[str(B)] = round(time.monotonic() - tb, 2); save()
    # each B's witness at L_MAX, re-simulated by the independent whole-line engine, must fail exactly at E (an exact consistency check)
    wit_ok = True; R['witness_resim'] = {}
    for r in R['rows']:
        if r['L'] == L_MAX and r.get('witness_left') is not None:
            f, _ = whole_line(r['witness_left'], r['witness_right'], r['E'] + 2)
            R['witness_resim'][str(r['B'])] = f; wit_ok = wit_ok and f == r['E']
    R['witnesses_fail_at_E'] = wit_ok
    tab = {(r['L'], r['B']): r['E'] for r in R['rows']}
    R['monotone_in_L_and_B'] = all((tab[(L, B)] is not None and (L == 0 or tab[(L - 1, B)] <= tab[(L, B)]) and (B == 0 or tab[(L, B - 1)] <= tab[(L, B)]))
                                   for L in range(L_MAX + 1) for B in range(B_MAX + 1))
    R['censored_total'] = sum(r['censored'] for r in R['rows'])
    R['complete'] = R['monotone_in_L_and_B'] and R['censored_total'] == 0 and R['witnesses_fail_at_E']; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


def stage(out, L_MAX, B_MAX, K):
    import hashlib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if not (0 <= L_MAX <= 80 and 0 <= B_MAX <= 20 and 1 <= K <= 400):
        print('REFUSED: scope outside L_MAX <= 80, B_MAX <= 20, K <= 400'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01'] = {'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'w1a_sha256': W1A_SHA256,
                  'scope': {'L_MAX': L_MAX, 'B_MAX': B_MAX, 'K': K}, 'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'cq01_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        rows = {(x['L'], x['B']) for x in d.get('rows', [])}
        want = {(L, B) for L in range(L_MAX + 1) for B in range(B_MAX + 1)}
        if rc != 0 or d.get('complete') is not True or rows != want or not all(d.get('controls', {}).values()):
            return 'FAIL', 'rc %s complete %s rows %d' % (rc, d.get('complete'), len(rows))
        return 'pass', 'CQ01 census complete: %d (L, B) values, none censored, monotone' % len(rows)
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
