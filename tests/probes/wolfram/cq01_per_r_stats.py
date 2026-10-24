#!/usr/bin/env python3
"""CQ01 per-R statistics, revision 3 (Local, 2026-10-24, L905: the gate's CDF domain admits rounding within 1e-12 of [0, 1]; the disclosed
tiny development run of revision 2 (B = 3, K = 32) had F = 1.0000000000000004 at ell = K, which the gate refused; the synthetic
packet never reached the cap, so no fixture saw it). Revision 2 (Local, 2026-10-24, L905; GPT's GC1817 design correction, made before any review: the seeded
simulation model of revision 1 is replaced by GPT's exact run-avoidance recurrence at one declared fixed p; the compared statistic is
the longest white run in the window of depths 2..K, open at both ends, which is exactly the recurrence's statistic; the pooled run
histogram counts runs between two actual black depths only; an aggregation policy is declared). Revision 1 (0e41970e) was never
reviewed; its one disclosed tiny development run (B = 3, K = 32) was read only for its gate verdict, size and bound census keys.
NOT an agreed job until GPT accepts this exact file; nothing runs on import; `--controls` runs the small CPU controls only.

If this holds, it changes the CQ01 row (the two-sided channel theorem's census, PERIOD-TWO.md): it decides between two descriptive
readings of L904's table. The coin reading: the ensemble of Psi R looks like iid bits at one density (about 0.57): per-R densities within
binomial spread, inter-black gaps geometric, longest window runs distributed as the exact iid reference, and R -> Psi R injective. The
structure reading: any of these fails by the declared margins; then that structure is the thing to explain or prove. Neither reading is
a theorem: a deterministic ensemble is not a sample, and no finite table proves CQ01 or refutes a bounded-gap form (GC1817).

The object. Psi R k for k = 1..K and every right half R supported in 1..B, from cq01_census.lane_psi (the kit's definitions, checked by
that file's controls; its bytes pinned below). Lane r is R p = bit p-1 of r, so the lanes r < 2^B' are exactly the R supported in 1..B'.
Depth 0 is the wall (white).

Statistics (all R supported in 1..B):
  - closed runs, for the census binding: with b_0 = 0 a virtual boundary and b_1 < b_2 < ... the black depths <= K, the closed white
    runs are b_(i+1) - b_i - 1 (the first counted from b_0); for each R, max over L <= L' of d(R, L) - L is (the longest closed run
    starting at a b_i <= L') + 1, the per-R form of L904's E(L, B) - L. Reported: histogram, lower median, maximum, the least lane
    attaining it and its b_i, lanes whose open tail K - b_last is longer, lanes with no black depth;
  - the window, depths 2..K (K - 1 bits): per-R black count (histogram, mean, sd, min, max) beside the binomial sd at the window
    density p = (window blacks) / (2^B (K - 1)); the number of R black at depth 1; per-R longest white run in the window, counting
    the runs touching depth 2 and depth K (histogram, mean, lower median, maximum);
  - the pooled histogram of closed runs between two actual black depths (b_i >= 1), over all R, beside N x p x (1 - p)^j, where N is the
    number of such runs (an individual gap's law under iid bits; GC1817);
  - the number of distinct prefixes (Psi R 1..k) for k in PREFIX_DEPTHS, k <= K.
The reference (GPT's GC1817 recurrence, no simulation): for iid bits black with the declared fixed p, P(longest white run in the
window < ell) = sum(x) after K - 1 updates of x_0 = 1, x_j = 0 by x_0' = p sum(x), x_j' = (1 - p) x_(j-1) for 1 <= j < ell; computed
for ell = 0..ell_max, where ell_max is the least ell >= (the ensemble's window maximum + 2) with P >= 1 - 1e-12, or K if that comes
first. Compared: the ensemble CDF G(ell) = (lanes with window longest < ell) / 2^B against F(ell); D = max |G - F| and where; the
ensemble mean against the reference mean sum_(ell >= 1) (1 - F(ell)).
Aggregation policy (GC1817): only the ensemble statistics above are compared with references, by the margins written in the
predictions. No per-R test is made and no p-value is computed; individual extreme R are reported descriptively. p is fitted once, from
the whole ensemble's window, and declared as such.
Bindings to the retained L904 census (cited/cq01-census-20261024-2041/, result 645fc352...): E(L, B'), its maximizer count and least
maximizing lane, recomputed from the per-lane bits for B' in (0, 8, 16) and L in (0, 100, 200, 300, 377, 400), must equal CENSUS_L904
(values read from that result by script); at the stage scope, the largest closed run starting at a b_i <= 400 over all R supported in
1..16, plus one, must equal 22, L904's largest E(L, 16) - L over L <= 400.

Controls (`--controls`, CPU only, small; all must pass before a stage):
  - the transpose: per-lane bits equal (psi[k] >> r) & 1 for B = 6, K = 64, every lane and depth, with the wall row white;
  - the census path: E(L, B), maximizers and least lane from per-lane bits equal cq01_census.death_summary for L <= 7, B <= 6, K = 40;
  - the run statistics on four hand-made lanes (closed runs from b_0, an open tail, no black depth, all black, the window);
  - the recurrence against exhaustive enumeration of every word of up to 10 bits at p = 0.3 and 0.57, every ell; and p = 0, 1;
  - four mutants, each of which must fail a control: 'bitorder' (big-endian unpacking), 'shift' (row k reads depth k + 1),
    'complement' (Psi negated), 'threshold' (the recurrence keeps suffixes up to ell, not below it).
The result gate (GC1813's method): one explicit schema checked in the order types, exact key sets, domains, cross-field bindings,
arithmetic, completion, inside one fail-closed matcher on bounded bytes; the valid full synthetic packet is assembled by the run's own
assembly code from two hand-made lanes; one negative fixture per obligation, each required to fail AT its own obligation.

Proposed stage: B = 16, K = 800 (the only admitted stage scope); W1A caps: stage, step wall and CPU 600 s, group RSS 4 GiB, artifacts
50 MiB, log 10 MiB. `run` also admits B <= 16, 8 <= K <= 800 for disclosed tiny development runs, which bind only the census values
their scope can reach.
Predictions (written before any run at the stage scope, after seeing Psi of the empty right half at depths 1..401 and L904's table):
  - the window density p is in [0.55, 0.59];
  - the per-R window count sd is at most 1.5 times the binomial sd sqrt((K - 1) p (1 - p));
  - the pooled run counts are within 10% of N p (1 - p)^j at every length j whose expectation is at least 1,000;
  - D <= 0.10, and the ensemble mean window longest is within 1.0 of the reference mean;
  - all 2^16 Psi R are distinct by depth 64.
Counterfactual: a count sd above twice binomial, a pooled count off by more than 25% at a length with expectation at least 1,000,
D > 0.25 or a mean 3 or more from the reference's, says the ensemble is not iid-like at one density and the structure reading holds;
fewer than 2^16 distinct sequences at depth K says R -> Psi R loses information.
Usage: python3 cq01_per_r_stats.py --controls | run OUT B K | stage OUT B K
"""
import hashlib, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
CENSUS_SHA256 = 'b46a07a31a4ffa3e867fad707ba510a1f84806b345134dd506691bc442216d59'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_SCOPE = (16, 800)
STAGE_S = 600
PREFIX_DEPTHS = (8, 16, 32, 64, 128, 256, 512, 800)
BIND_L = 400
GAP_L904 = 22
CDF_TOL = 1e-12
CENSUS_L904 = {"0,0": [1, 1, 0], "100,0": [102, 1, 0], "200,0": [201, 1, 0], "300,0": [301, 1, 0], "377,0": [380, 1, 0], "400,0": [401, 1, 0],
               "0,8": [1, 256, 0], "100,8": [110, 1, 248], "200,8": [210, 1, 238], "300,8": [307, 1, 155], "377,8": [386, 1, 253],
               "400,8": [408, 1, 240], "0,16": [1, 65536, 0], "100,16": [112, 1, 61237], "200,16": [212, 2, 17035], "300,16": [315, 12, 2364],
               "377,16": [399, 6, 1936], "400,16": [417, 4, 9787]}
MUTANTS = ('bitorder', 'shift', 'complement', 'threshold')
BASE_KEYS = ('transpose_equals_lane_words_B6_K64', 'census_path_equals_death_summary_L_le_7_B_le_6', 'run_stats_hand_fixtures',
             'recurrence_equals_enumeration_n_le_10')


def census():
    import cq01_census as C
    if hashlib.sha256(open(C.__file__, 'rb').read()).hexdigest() != CENSUS_SHA256:
        raise SystemExit('REFUSED: cq01_census.py is not the pinned bytes')
    return C


def census_expected(B, K):
    """The CENSUS_L904 entries this scope can reach: B' <= B, L < K and E <= K."""
    return {key: v for key, v in CENSUS_L904.items() if int(key.split(',')[1]) <= B and int(key.split(',')[0]) < K and v[0] <= K}


def lane_bits(psi, B, K, mutant=''):
    """Per-lane bits, shape (K + 1, 2^B): row k holds Psi R k for every lane r; row 0 is the white wall."""
    import numpy as np
    n = 1 << B; nbytes = (n + 7) // 8
    out = np.zeros((K + 1, n), dtype=np.uint8)
    for k in range(1, K + 1):
        src = psi[k + 1] if (mutant == 'shift' and k < K) else psi[k]
        raw = np.frombuffer(src.to_bytes(nbytes, 'little'), dtype=np.uint8)
        row = np.unpackbits(raw, bitorder='big' if mutant == 'bitorder' else 'little')[:n]
        out[k] = 1 - row if mutant == 'complement' else row
    return out


def run_stats(row, K, n, bind_l=None):
    """Per lane, from row(k), the depth-k bits of every lane, with b_0 = 0 a virtual boundary: longest and start, the longest closed run
    (ending at a black depth <= K, the first counted from b_0; -1 if none) and its b_i; tail, K - b_last; blacks, black depths in 1..K;
    depth1, black at depth 1; bind, the longest closed run with b_i <= bind_l; window, the longest white run in depths 2..K, open at both
    ends. pooled: the histogram of closed runs between two actual black depths (b_i >= 1), over all lanes."""
    import numpy as np
    last = np.zeros(n, dtype=np.int64); longest = np.full(n, -1, dtype=np.int64); start = np.zeros(n, dtype=np.int64)
    blacks = np.zeros(n, dtype=np.int64); pooled = np.zeros(K, dtype=np.int64)
    bind = np.full(n, -1, dtype=np.int64) if bind_l is not None else None
    wrun = np.zeros(n, dtype=np.int64); window = np.zeros(n, dtype=np.int64); depth1 = None
    for k in range(1, K + 1):
        blk = np.asarray(row(k)).astype(bool)
        if k == 1: depth1 = blk.copy()
        run = k - last - 1
        pooled += np.bincount(run[blk & (last >= 1)], minlength=K)[:K]     # a closed run is at most K - 1
        up = blk & (run > longest); longest[up] = run[up]; start[up] = last[up]
        if bind is not None:
            ub = blk & (last <= bind_l) & (run > bind); bind[ub] = run[ub]
        if k >= 2:
            wrun = np.where(blk, 0, wrun + 1); window = np.maximum(window, wrun)
        blacks += blk; last[blk] = k
    return {'longest': longest, 'start': start, 'tail': K - last, 'pooled': pooled, 'blacks': blacks, 'depth1': depth1, 'bind': bind,
            'window': window}


def e_from_bits(bits, L, nl):
    """E(L, B') over the lanes r < nl: [E, maximizer count, least maximizing lane], or None if a lane has no black depth in (L, K]."""
    import numpy as np
    sub = bits[L + 1:, :nl]
    if sub.shape[0] == 0 or not sub.any(axis=0).all(): return None
    d = L + 1 + sub.argmax(axis=0)
    e = int(d.max()); w = np.flatnonzero(d == e)
    return [e, int(w.size), int(w[0])]


def run_cdf(p, nbits, ell, mutant=''):
    """P(the longest white run in nbits iid bits, black with probability p, is < ell): GPT's GC1817 recurrence."""
    if ell <= 0: return 0.0
    width = ell + 1 if mutant == 'threshold' else ell
    x = [1.0] + [0.0] * (width - 1); q = 1.0 - p
    for _ in range(nbits):
        s = sum(x); x = [p * s] + [q * x[j - 1] for j in range(1, width)]
    return sum(x)


def reference_cdf(p, nbits, wmax, mutant=''):
    """F(ell) for ell = 0..ell_max: the least ell >= wmax + 2 with F >= 1 - CDF_TOL, or nbits + 1 if that comes first."""
    F = []; ell = 0
    while True:
        F.append(run_cdf(p, nbits, ell, mutant))
        if ell >= nbits + 1 or (ell >= wmax + 2 and F[-1] >= 1 - CDF_TOL): return F
        ell += 1


def ensemble_cdf(h, n, length):
    """G(ell) = (lanes with window longest < ell) / n for ell = 0..length - 1, from the histogram {str(value): lanes}."""
    items = sorted((int(k), v) for k, v in h.items())
    return [sum(v for x, v in items if x < ell) / n for ell in range(length)]


def hist(a):
    import numpy as np
    v, c = np.unique(np.asarray(a), return_counts=True)
    return {str(int(x)): int(y) for x, y in zip(v, c)}


def lower_median(h):
    items = sorted((int(k), v) for k, v in h.items()); need = (sum(v for _, v in items) - 1) // 2; acc = 0
    for x, v in items:
        acc += v
        if acc > need: return x


def geometric(runs, p, length):
    return [runs * p * (1 - p) ** j for j in range(length)]


def trim(a):
    a = [int(x) for x in a]
    while a and a[-1] == 0: a.pop()
    return a


def compare(F, G):
    diffs = [abs(g - f) for f, g in zip(F, G)]
    D = max(diffs); return D, diffs.index(D)


def assemble(bits, B, K):
    """Every reported section from the per-lane bits; shared by the run and the synthetic gate packet."""
    import numpy as np
    n = 1 << B; t = time.monotonic()
    st = run_stats(lambda k: bits[k], K, n, BIND_L if (B, K) == STAGE_SCOPE else None)
    d1 = st['depth1']; cnt = st['blacks'] - d1                                  # window black counts (depths 2..K)
    mean = float(cnt.mean()); p = mean / (K - 1)
    density = {'count_hist': hist(cnt), 'mean_count': mean, 'sd_count': float(cnt.std()), 'min_count': int(cnt.min()),
               'max_count': int(cnt.max()), 'mean_density': p, 'binomial_sd_count': math.sqrt((K - 1) * p * (1 - p))}
    lg = st['longest']; mx = int(lg.max()); ml = int(np.flatnonzero(lg == mx)[0]); lh = hist(lg)
    longest = {'hist': lh, 'max': mx, 'max_lane': ml, 'max_start': int(st['start'][ml]), 'median': lower_median(lh),
               'open_tail_longer': int((st['tail'] > lg).sum()), 'none_closed': int((lg < 0).sum())}
    ph = trim(st['pooled']); runs = sum(ph)
    pooled = {'hist': ph, 'expected': geometric(runs, p, len(ph)), 'runs': runs}
    prefixes = {str(k): int(np.unique(np.packbits(bits[1:k + 1].T, axis=1), axis=0).shape[0]) for k in PREFIX_DEPTHS if k <= K}
    stats_s = time.monotonic() - t; t = time.monotonic()
    wl = st['window']; wh = hist(wl); wmax = int(wl.max())
    F = reference_cdf(p, K - 1, wmax); G = ensemble_cdf(wh, n, len(F)); D, at = compare(F, G)
    window = {'hist': wh, 'mean': float(wl.mean()), 'median': lower_median(wh), 'max': wmax, 'depth1_black': int(d1.sum()),
              'reference_p': p, 'reference_cdf': F, 'ensemble_cdf': G, 'D': D, 'D_at': at,
              'reference_mean': sum(1 - f for f in F[1:])}
    reference_s = time.monotonic() - t
    want = census_expected(B, K)
    cen = {key: e_from_bits(bits, int(key.split(',')[0]), 1 << int(key.split(',')[1])) for key in want}
    gap = int(st['bind'].max()) + 1 if st['bind'] is not None else None
    bindings = {'census': cen, 'census_equal': cen == want, 'max_gap_le_400': gap, 'max_gap_equal': (gap == GAP_L904) if gap is not None else None}
    return ({'density': density, 'longest': longest, 'pooled': pooled, 'prefixes': prefixes, 'window': window, 'bindings': bindings},
            {'stats_s': round(stats_s, 2), 'reference_s': round(reference_s, 2)})


def controls(mutant=''):
    import itertools
    import numpy as np
    C = census(); res = {}
    B, K = 6, 64; psi, _, _ = C.lane_psi(B, K); bits = lane_bits(psi, B, K, mutant)
    res['transpose_equals_lane_words_B6_K64'] = bool(not bits[0].any()) and all(int(bits[k, r]) == (psi[k] >> r) & 1 for k in range(1, K + 1) for r in range(1 << B))
    ok = True
    for Bc in range(7):
        psi, _, ALL = C.lane_psi(Bc, 40); bits = lane_bits(psi, Bc, 40, mutant)
        for L in range(8):
            best, bw, alive = C.death_summary(psi, L, 40, ALL)
            if e_from_bits(bits, L, 1 << Bc) != (None if alive else [best, C.popcount(bw), (bw & -bw).bit_length() - 1]): ok = False
    res['census_path_equals_death_summary_L_le_7_B_le_6'] = ok
    lanes = [[1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [0] * 8, [1] * 8]
    hb = np.zeros((9, 4), dtype=np.uint8)
    for r, lane in enumerate(lanes): hb[1:, r] = lane
    st = run_stats(lambda k: hb[k], 8, 4, 3)
    res['run_stats_hand_fixtures'] = (st['longest'].tolist() == [3, 2, -1, 0] and st['start'].tolist() == [4, 0, 0, 0]
                                      and st['tail'].tolist() == [0, 5, 8, 0] and st['pooled'].tolist() == [7, 0, 1, 1, 0, 0, 0, 0]
                                      and st['blacks'].tolist() == [3, 1, 0, 8] and st['depth1'].tolist() == [True, False, False, True]
                                      and st['bind'].tolist() == [2, 2, -1, 0] and st['window'].tolist() == [3, 5, 7, 0])
    ok = True
    for p in (0.3, 0.57):
        for nb in range(11):
            prob = {}
            for w in itertools.product((0, 1), repeat=nb):                  # 1 = black
                pr = 1.0; run = best = 0
                for b in w:
                    pr *= p if b else 1 - p
                    run = 0 if b else run + 1; best = max(best, run)
                prob[best] = prob.get(best, 0.0) + pr
            for ell in range(nb + 2):
                if abs(run_cdf(p, nb, ell, mutant) - sum(v for x, v in prob.items() if x < ell)) > 1e-12: ok = False
    ok = ok and run_cdf(1.0, 20, 1, mutant) == 1.0 and run_cdf(0.0, 20, 20, mutant) == 0.0 and run_cdf(0.0, 20, 21, mutant) == 1.0
    res['recurrence_equals_enumeration_n_le_10'] = bool(ok)
    return res


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 PER-R CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, B, K):
    """All right halves supported in 1..B at depths 1..K in one lane pass, then the statistics, the reference and the bindings."""
    os.makedirs(out, exist_ok=True); t0 = time.monotonic(); C = census()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'census_sha256': CENSUS_SHA256, 'scope': {'B': B, 'K': K}, 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_per_r_result.json.tmp')
        json.dump(R, open(tmp, 'w')); os.replace(tmp, os.path.join(out, 'cq01_per_r_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    t = time.monotonic(); psi, _, _ = C.lane_psi(B, K); bits = lane_bits(psi, B, K); del psi
    lane_s = round(time.monotonic() - t, 2)
    sections, timing = assemble(bits, B, K)
    R.update(sections); R['timing'] = {'lane_psi_s': lane_s, **timing}
    b = R['bindings']
    R['complete'] = b['census_equal'] is True and (b['max_gap_equal'] is True if (B, K) == STAGE_SCOPE else b['max_gap_equal'] is None)
    if not R['complete']: R['stopped'] = 'incomplete: a census binding failed (no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 16 << 20
TOP_KEYS = {'started', 'this_sha256', 'census_sha256', 'scope', 'controls', 'gate_controls', 'density', 'longest', 'pooled', 'prefixes',
            'window', 'bindings', 'timing', 'complete', 'elapsed_s', 'finished'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}
SECTION_KEYS = {'density': {'count_hist', 'mean_count', 'sd_count', 'min_count', 'max_count', 'mean_density', 'binomial_sd_count'},
                'longest': {'hist', 'max', 'max_lane', 'max_start', 'median', 'open_tail_longer', 'none_closed'},
                'pooled': {'hist', 'expected', 'runs'},
                'window': {'hist', 'mean', 'median', 'max', 'depth1_black', 'reference_p', 'reference_cdf', 'ensemble_cdf', 'D', 'D_at', 'reference_mean'},
                'bindings': {'census', 'census_equal', 'max_gap_le_400', 'max_gap_equal'},
                'timing': {'lane_psi_s', 'stats_s', 'reference_s'}}


def validate_result(d, src_sha, B, K):
    """One explicit schema (GC1813), checked in order: types, exact key sets, domains, cross-field bindings, arithmetic, completion.
    Returns the first failed obligation as a string, or None."""
    isint = lambda x: type(x) is int
    isnum = lambda x: type(x) in (int, float)
    n = 1 << B
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('this_sha256', str), ('census_sha256', str), ('scope', dict), ('controls', dict), ('gate_controls', dict), ('density', dict),
                   ('longest', dict), ('pooled', dict), ('prefixes', dict), ('window', dict), ('bindings', dict), ('timing', dict), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    c = d['controls']
    if not isinstance(c.get('base'), dict) or not all(isinstance(c.get(m), dict) for m in MUTANTS): return 'types: control reports'
    den, lg, po, pr, wi, bi = (d[k] for k in ('density', 'longest', 'pooled', 'prefixes', 'window', 'bindings'))
    if not (isinstance(den.get('count_hist'), dict) and isinstance(lg.get('hist'), dict) and isinstance(wi.get('hist'), dict)): return 'types: histograms'
    if not all(isinstance(x, list) for x in (po.get('hist'), po.get('expected'), wi.get('reference_cdf'), wi.get('ensemble_cdf'))): return 'types: lists'
    if not isinstance(bi.get('census'), dict): return 'types: census bindings'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['scope']) != {'B', 'K'}: return 'keys: scope'
    if set(c) != CONTROL_KEYS: return 'keys: controls'
    if set(c['base']) != set(BASE_KEYS) or not all(set(c[m]) == set(BASE_KEYS) for m in MUTANTS): return 'keys: base or mutant reports'
    if set(d['gate_controls']) != set(GATE_KEYS): return 'keys: gate controls'
    for name, keys in SECTION_KEYS.items():
        if set(d[name]) != keys: return 'keys: %s' % name
    if set(pr) != {str(k) for k in PREFIX_DEPTHS if k <= K}: return 'keys: prefixes'
    if set(bi['census']) != set(census_expected(B, K)): return 'keys: census bindings'
    # 3. domains
    if d['this_sha256'] != src_sha: return 'domains: source digest'
    if d['census_sha256'] != CENSUS_SHA256: return 'domains: census digest'
    if d['scope'] != {'B': B, 'K': K}: return 'domains: scope'
    if not all(type(v) is bool for v in list(c['base'].values()) + [x for m in MUTANTS for x in c[m].values()] + [c[m + '_caught'] for m in MUTANTS] + [c['base_all_pass'], c['ok']]):
        return 'domains: control values not Boolean'
    if not all(v is True for v in d['gate_controls'].values()): return 'domains: a gate control is not true'
    def hist_ok(h, lo, hi):
        return (all(isinstance(k, str) and k.lstrip('-').isdigit() and lo <= int(k) <= hi and isint(v) and v >= 1 for k, v in h.items())
                and sum(h.values()) == n)
    if not hist_ok(den['count_hist'], 0, K - 1): return 'domains: window count histogram'
    if not hist_ok(lg['hist'], -1, K - 1): return 'domains: longest histogram'
    if not hist_ok(wi['hist'], 0, K - 1): return 'domains: window longest histogram'
    if not (all(isnum(den[k]) for k in ('mean_count', 'sd_count', 'mean_density', 'binomial_sd_count')) and isint(den['min_count']) and isint(den['max_count'])):
        return 'domains: density fields'
    if not (isint(lg['max']) and isint(lg['median']) and isint(lg['max_lane']) and 0 <= lg['max_lane'] < n and isint(lg['max_start']) and 0 <= lg['max_start'] <= K):
        return 'domains: longest fields'
    if not all(isint(lg[k]) and 0 <= lg[k] <= n for k in ('open_tail_longer', 'none_closed')): return 'domains: longest counts'
    if not (all(isint(x) and x >= 0 for x in po['hist']) and isint(po['runs']) and all(isnum(x) for x in po['expected'])): return 'domains: pooled'
    if not all(isint(v) and 1 <= v <= n for v in pr.values()): return 'domains: prefix counts'
    if not (isint(wi['max']) and isint(wi['median']) and isint(wi['depth1_black']) and 0 <= wi['depth1_black'] <= n and isint(wi['D_at'])
            and all(isnum(wi[k]) for k in ('mean', 'reference_p', 'D', 'reference_mean'))
            and all(isnum(x) and -CDF_TOL <= x <= 1 + CDF_TOL for x in wi['reference_cdf'] + wi['ensemble_cdf'])):   # rounding (revision 3)
        return 'domains: window fields'
    if not all(v is None or (isinstance(v, list) and len(v) == 3 and all(isint(x) for x in v)) for v in bi['census'].values()): return 'domains: census values'
    # 4. cross-field bindings
    if not all(c['base'][k] is True for k in BASE_KEYS) or c['base_all_pass'] is not True: return 'bindings: base controls'
    for m in MUTANTS:
        if c[m + '_caught'] is not True or all(c[m][k] for k in BASE_KEYS): return 'bindings: mutant %s not caught by its own outcomes' % m
    if c['ok'] is not True: return 'bindings: controls ok flag'
    if bi['census'] != census_expected(B, K) or bi['census_equal'] is not True: return 'bindings: census values'
    if (B, K) == STAGE_SCOPE:
        if bi['max_gap_le_400'] != GAP_L904 or bi['max_gap_equal'] is not True: return "bindings: the largest gap is not L904's 22"
    elif bi['max_gap_le_400'] is not None or bi['max_gap_equal'] is not None: return 'bindings: a gap binding outside the stage scope'
    ch = {int(k): v for k, v in den['count_hist'].items()}
    wtot = sum(k * v for k, v in ch.items()); mean = wtot / n
    if abs(den['mean_count'] - mean) > 1e-9 * K: return 'bindings: density mean vs its histogram'
    if wi['reference_p'] != den['mean_density'] or abs(wi['reference_p'] - wtot / (n * (K - 1))) > 1e-12: return 'bindings: reference p is not the window density'
    # 5. arithmetic
    sd = math.sqrt(sum(v * (k - mean) ** 2 for k, v in ch.items()) / n); p = wtot / (n * (K - 1))
    if abs(den['sd_count'] - sd) > 1e-6: return 'arithmetic: density sd'
    if den['min_count'] != min(ch) or den['max_count'] != max(ch): return 'arithmetic: density min or max'
    if abs(den['binomial_sd_count'] - math.sqrt((K - 1) * p * (1 - p))) > 1e-9: return 'arithmetic: binomial sd'
    if po['runs'] != sum(po['hist']) or po['runs'] != wtot + wi['depth1_black'] - (n - lg['none_closed']): return 'arithmetic: pooled runs vs black depths'
    if po['hist'] and po['hist'][-1] == 0: return 'arithmetic: pooled histogram not trimmed'
    want = geometric(po['runs'], p, len(po['hist']))
    if len(po['expected']) != len(want) or any(abs(a - b) > 1e-9 * max(1.0, abs(b)) for a, b in zip(po['expected'], want)): return 'arithmetic: expected counts'
    lh = {int(k): v for k, v in lg['hist'].items()}
    if lg['max'] != max(lh) or lg['median'] != lower_median(lg['hist']) or lg['none_closed'] != lh.get(-1, 0): return 'arithmetic: longest summary'
    if lg['max'] >= 0 and (len(po['hist']) - 1 > lg['max'] or lg['max_start'] + lg['max'] + 1 > K): return 'arithmetic: longest vs pooled, or a run past K'
    ks = sorted(int(k) for k in pr)
    if any(pr[str(a)] > pr[str(b)] for a, b in zip(ks, ks[1:])): return 'arithmetic: prefix counts decrease'
    wh = {int(k): v for k, v in wi['hist'].items()}
    if wi['max'] != max(wh) or wi['median'] != lower_median(wi['hist']) or abs(wi['mean'] - sum(k * v for k, v in wh.items()) / n) > 1e-9 * K:
        return 'arithmetic: window summary'
    F = reference_cdf(p, K - 1, wi['max'])
    if len(wi['reference_cdf']) != len(F) or any(abs(a - b) > 1e-12 for a, b in zip(wi['reference_cdf'], F)): return 'arithmetic: reference CDF'
    G = ensemble_cdf(wi['hist'], n, len(F))
    if len(wi['ensemble_cdf']) != len(G) or any(abs(a - b) > 1e-12 for a, b in zip(wi['ensemble_cdf'], G)): return 'arithmetic: ensemble CDF'
    D, at = compare(F, G)
    if abs(wi['D'] - D) > 1e-12 or wi['D_at'] != at: return 'arithmetic: D'
    if abs(wi['reference_mean'] - sum(1 - f for f in F[1:])) > 1e-9: return 'arithmetic: reference mean'
    # 6. completion
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, B, K):
    """The final gate: bounded bytes, then validate_result, inside one fail-closed boundary."""
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            prob = validate_result(json.loads(raw), src_sha, B, K)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'CQ01 per-R statistics complete, every binding held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


GATE_KEYS = ('good_full_packet_passes', 'types_density_null', 'types_controls_list', 'types_window_cdf_not_list',
             'keys_extra_top_key', 'keys_density_missing_key', 'keys_window_missing_key', 'keys_gate_report_replaced', 'keys_stopped_present',
             'keys_census_key_missing', 'keys_mutant_reports_empty',
             'domains_wrong_digest', 'domains_wrong_census_digest', 'domains_wrong_scope', 'domains_count_hist_sum', 'domains_count_out_of_range',
             'domains_max_lane_out_of_range', 'domains_prefix_above_lanes', 'domains_window_hist_sum', 'domains_cdf_above_one',
             'domains_gate_control_false',
             'bindings_explicit_false_base', 'bindings_census_value_changed', 'bindings_gap_present_off_scope', 'bindings_mutant_all_true',
             'bindings_reference_p_not_window_density', 'bindings_mean_not_histogram',
             'arithmetic_sd_changed', 'arithmetic_pooled_runs_not_blacks', 'arithmetic_median_changed', 'arithmetic_expected_changed',
             'arithmetic_prefix_decreasing', 'arithmetic_run_past_K', 'arithmetic_reference_cdf_changed', 'arithmetic_reference_cdf_truncated',
             'arithmetic_ensemble_cdf_changed', 'arithmetic_D_changed', 'arithmetic_reference_mean_changed',
             'completion_flag_false')


def gate_controls():
    """A valid full synthetic packet, assembled by assemble() from two hand-made lanes (B = 1, K = 16), and one negative fixture per
    obligation. Each fixture must FAIL, at its own obligation, with the good packet passing."""
    import copy, tempfile
    import numpy as np
    hb = np.zeros((17, 2), dtype=np.uint8)
    hb[1:, 0] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    hb[1:, 1] = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    sections, timing = assemble(hb, 1, 16)
    sections = json.loads(json.dumps(sections))
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'this_sha256': 'S', 'census_sha256': CENSUS_SHA256, 'scope': {'B': 1, 'K': 16}, 'complete': True, 'elapsed_s': 0.1,
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'timing': {'lane_psi_s': 0.0, **timing}, 'finished': 'f', **sections}
    def bump(h):
        k = sorted(h)[0]; h[k] += 1
    def truncate(d):
        d['window']['reference_cdf'].pop(); d['window']['ensemble_cdf'].pop()
    fx = {
        'types_density_null': lambda d: d.__setitem__('density', None),
        'types_controls_list': lambda d: d.__setitem__('controls', []),
        'types_window_cdf_not_list': lambda d: d['window'].__setitem__('reference_cdf', {}),
        'keys_extra_top_key': lambda d: d.__setitem__('extra', 1),
        'keys_density_missing_key': lambda d: d['density'].pop('sd_count'),
        'keys_window_missing_key': lambda d: d['window'].pop('D_at'),
        'keys_gate_report_replaced': lambda d: d.__setitem__('gate_controls', {'g': True}),
        'keys_stopped_present': lambda d: d.__setitem__('stopped', 'x'),
        'keys_census_key_missing': lambda d: d['bindings'].__setitem__('census', {}),
        'keys_mutant_reports_empty': lambda d: [d['controls'].__setitem__(m, {}) for m in MUTANTS],
        'domains_wrong_digest': lambda d: d.__setitem__('this_sha256', '0' * 64),
        'domains_wrong_census_digest': lambda d: d.__setitem__('census_sha256', '0' * 64),
        'domains_wrong_scope': lambda d: d['scope'].__setitem__('K', 15),
        'domains_count_hist_sum': lambda d: bump(d['density']['count_hist']),
        'domains_count_out_of_range': lambda d: d['density'].__setitem__('count_hist', {'16': 1, '4': 1}),
        'domains_max_lane_out_of_range': lambda d: d['longest'].__setitem__('max_lane', 2),
        'domains_prefix_above_lanes': lambda d: d['prefixes'].__setitem__('16', 3),
        'domains_window_hist_sum': lambda d: bump(d['window']['hist']),
        'domains_cdf_above_one': lambda d: d['window']['reference_cdf'].__setitem__(-1, 1.5),
        'domains_gate_control_false': lambda d: d['gate_controls'].__setitem__(GATE_KEYS[1], False),
        'bindings_explicit_false_base': lambda d: d['controls']['base'].__setitem__(BASE_KEYS[1], False),
        'bindings_census_value_changed': lambda d: d['bindings']['census'].__setitem__('0,0', [2, 1, 0]),
        'bindings_gap_present_off_scope': lambda d: d['bindings'].update({'max_gap_le_400': GAP_L904, 'max_gap_equal': True}),
        'bindings_mutant_all_true': lambda d: [d['controls'].__setitem__(m, dict(base)) for m in MUTANTS],
        'bindings_reference_p_not_window_density': lambda d: d['window'].__setitem__('reference_p', d['window']['reference_p'] + 0.01),
        'bindings_mean_not_histogram': lambda d: d['density'].__setitem__('mean_count', d['density']['mean_count'] + 0.5),
        'arithmetic_sd_changed': lambda d: d['density'].__setitem__('sd_count', d['density']['sd_count'] + 0.5),
        'arithmetic_pooled_runs_not_blacks': lambda d: (d['pooled']['hist'].__setitem__(0, d['pooled']['hist'][0] + 1),
                                                        d['pooled'].__setitem__('runs', d['pooled']['runs'] + 1)),
        'arithmetic_median_changed': lambda d: d['longest'].__setitem__('median', d['longest']['median'] + 1),
        'arithmetic_expected_changed': lambda d: d['pooled']['expected'].__setitem__(0, d['pooled']['expected'][0] * 1.01),
        'arithmetic_prefix_decreasing': lambda d: d['prefixes'].__setitem__('16', d['prefixes']['8'] - 1) if d['prefixes']['8'] > 1 else d['prefixes'].__setitem__('8', 2),
        'arithmetic_run_past_K': lambda d: d['longest'].__setitem__('max_start', 16 - d['longest']['max']),
        'arithmetic_reference_cdf_changed': lambda d: d['window']['reference_cdf'].__setitem__(2, d['window']['reference_cdf'][2] * 0.9),
        'arithmetic_reference_cdf_truncated': truncate,
        'arithmetic_ensemble_cdf_changed': lambda d: d['window']['ensemble_cdf'].__setitem__(1, min(1.0, d['window']['ensemble_cdf'][1] + 0.25)),
        'arithmetic_D_changed': lambda d: d['window'].__setitem__('D', d['window']['D'] + 0.01),
        'arithmetic_reference_mean_changed': lambda d: d['window'].__setitem__('reference_mean', d['window']['reference_mean'] + 0.5),
        'completion_flag_false': lambda d: d.__setitem__('complete', False),
    }
    res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', 1, 16)
        def v(doc):
            json.dump(doc, open(rp, 'w')); return m(0, '')
        res['good_full_packet_passes'] = v(good)[0] == 'pass'
        for name, f in fx.items():                      # each fixture must fail AT its own obligation, not an earlier one (GC1813)
            bad = copy.deepcopy(good); f(bad); verdict, note = v(bad)
            res[name] = verdict == 'FAIL' and note.startswith('rc 0: ' + name.split('_')[0] + ':')
    assert set(res) == set(GATE_KEYS)
    return res


def stage(out, B, K):
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if (B, K) != STAGE_SCOPE:
        print('REFUSED: the only admitted stage scope is B = 16, K = 800'); return 3
    census()
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01_per_r'] = {'this_sha256': src_sha, 'census_sha256': CENSUS_SHA256, 'w1a_sha256': W1A_SHA256, 'scope': {'B': B, 'K': K},
                        'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_per_r_result.json'), src_sha, B, K)
    rec = sup.run_step('cq01_per_r', [sys.executable, os.path.abspath(__file__), 'run', rdir, str(B), str(K)], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 4 and a[0] == 'run':
        B, K = int(a[2]), int(a[3])
        if not (0 <= B <= 16 and 8 <= K <= 800): print('REFUSED: run admits 0 <= B <= 16, 8 <= K <= 800'); sys.exit(3)
        R = run(a[1], B, K); print('CQ01 PER-R RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 4 and a[0] == 'stage':
        sys.exit(stage(a[1], int(a[2]), int(a[3])))
    print(__doc__); sys.exit(2)
