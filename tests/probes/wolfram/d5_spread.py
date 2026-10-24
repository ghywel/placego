#!/usr/bin/env python3
"""D5, revision 3 (2026-10-24; revision 2 answered GC1766, this revision reconciles the decision layer with the declared stop,
GC1767): the record-holders
in free-bit coordinates. How much do the shallowest free bits move a lane's elimination level? NOT an agreed job until
GPT accepts this exact file; nothing runs on import; `--test` runs the instrument's controls at width 14 only.

Population and statistic (GC1766). The ensemble is the kit's CONSTRAINED LANE ensemble: 2^(W/2) lanes, one per free-bit
string y1, y3, ..., y(W-1) (d1_engine's `y_free`: lane bit s is y(2s+1)); one chunk, n = W/2, c = 0. A lane's level is its
elimination level in the kit's `run` (recorded only at even k with W < k + 1, so every level lies in [W, D(W)]); it equals
the physical first even white time at depth 1 of the reconstructed start, which the bounded physical control below checks
on predeclared lanes at each width (the exhaustive equality of the record holds to width 12 and is not assumed beyond).
For k in (4, 6), lanes are grouped by their deep prefix P = p >> k (free bits y(2k+1) and above fixed, the k shallowest
free). Per prefix: spread = max - min of its 2^k completions' levels, the prefix's maximum, its attaining count. Reported:
the spread histogram, median and mean, the fraction of spread-0 prefixes, the record prefixes AT EACH k with their
individual attaining counts (several k = 4 prefixes may attain D(W)), the median spread by prefix maximum (the
unexpected check), and a DESCRIPTIVE null: the same statistic on one seeded permutation of the levels across lanes
(seed and mechanism recorded; it preserves the marginal distribution and claims no significance).

Correctness controls (any failure: a FAIL receipt, nonzero exit, the stage stops): every lane eliminated below K and
every level defined; the maximum level equals the table's D(W) (known value); the global number of lanes attaining D(W)
equals the retained checkpoint's holder count (4, 13, 13, 13 at 30, 32, 34, 36); grouping: the quotient/remainder
domain check agrees with the slicing for every prefix; the physical control: for the predeclared lanes (the first
record lane, lanes 0, 1, 2^(n-1), 2^n - 1 and four seeded pseudo-random lanes, including non-maximal levels), the
reconstructed start's physical death time equals its level, and the record lane's start passes `validate_witness`.
A prediction miss is NOT a software failure: the data are retained and the trajectory rule applies.

Predeclared falsification rule (written before the run): at k = 4, R(W) = measured median spread / null median spread.
The reading "the deep free bits determine the elimination level at typical prefixes" SURVIVES only if all four widths
complete with R(W) <= 0.5 at each; CLOSES at the first width with a DEFINED R(W) >= 0.8, applied after each width (a
scientific stop: the stage ends successfully there, the later widths are not run, the executed widths are retained);
an UNDEFINED R (a zero null median, 0/0: a degenerate baseline, e.g. a constant level array) is an undefined-baseline
INCONCLUSIVE stop, never a refutation; a complete four-width sequence not meeting SURVIVES or CLOSES is INCONCLUSIVE.
The receipt keeps all_widths_completed, executed_widths, stop_width and hypothesis_verdict distinct, so an intended early
stop cannot look like four completed widths. The physical sample supports only the lanes it checked (distinct coverage
is reported; seeded lanes may repeat). Separately predicted:
the record prefixes' attaining counts sum to the holder count (a control), and at k = 6 there is exactly one record
prefix at 32, 34, 36 (the plateau's thirteen share y13 and above) and at k = 4 more than one (a prediction, not a
control). No law of D(W) is claimed from any outcome: the bulk statistic is about typical prefixes; record selection
(6 of 16, 12 of 16 completions) already differs from full independence.

Bounded execution (`stage`): sequential children of the unchanged W1A supervisor, one per width in the fixed order
30, 32, 34, 36 at K = D(W) + 1 (53, 67, 67, 67): step wall 60 s / CPU 60 s; stage 300 s; group RSS stop 2 GiB; pressure
level 2 (free-percent fallback); swap growth 256 MiB; disk floor 5 GiB; new artifacts 16 MiB; log 1 MiB per step; one
child, no concurrent job, a new empty OUT, no retries; the first correctness or guard failure stops the stage; receipts
and partial outputs retained. Bindings: this file's digest and d1_engine's (e924602e...) and W1A's (3f908914...) are
recorded, and the stage refuses if d1_engine or W1A is not the pinned bytes.

Usage: python3 d5_spread.py measure W K OUT.json     (one width; W in the allow-list)
       python3 d5_spread.py stage OUT_DIR             (the four widths under the supervisor)
       python3 d5_spread.py --test                    (width 14, D(14) from the physical engine; the controls)
OUTCOME (run d5-spread-20261024-0425, the accepted stage at e8019862..., 2026-10-24 04:25 BST; this docstring is the only
change since): stage complete in 8.1 s, four widths, every correctness control passed (max levels 52, 66, 66, 66; attaining
4, 13, 13, 13; grouping agreed; nine distinct physical lanes per width equal to their levels, record witnesses validated);
CPU 0.07 + 0.17 + 0.63 + 2.44 s, peak RSS 61 MB. The predeclared rule returned SURVIVES at the boundary exactly: R(k=4) =
4/8 = 0.5 at every width (k = 6: 8/12). Scientific reading, kept separate (wording corrected for GC1769): the statistic is
floor-sensitive. A measured fraction near one half of the lanes (0.507, 0.499, 0.505, 0.497: measured, not a theorem for
this constrained population; section 8.51's halving is proved for the fresh-left-cell phase only) dies at the first level
beyond the cone, W; spread <= block max - W with equality when the block touches W, and the conditional median spread equal
to m - W at prefix maximum m shows that at least half of that stratum's blocks touch the floor (not almost all; occupancy
itself was not measured). So R compares block maxima above the floor as much as within-block variation; a deep prefix
correlates the levels in its block (the spread-0 fraction rises with width against 0 for the null), but SURVIVES means only
that the predeclared inequality passed, not that the deep bits determine the level. At the record it is the reverse: the
record prefixes have the largest spreads (22; 34; 32; 26 to 30) with 2 to 5 of 16 completions attaining. The spread-0
fraction rises with width (0.06, 0.08, 0.10, 0.14; null 0); the ratio of mean spreads falls (0.59, 0.56, 0.51, 0.48).
"""
import hashlib, json, os, random, statistics, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_engine as E

D1_SHA256 = 'e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
TABLE = {24: 42, 26: 44, 28: 48, 30: 52, 32: 66, 34: 66, 36: 66, 38: 72, 40: 76, 42: 78, 44: 78}   # D(W) from the record (L844, L846)
HOLDERS = {30: 4, 32: 13, 34: 13, 36: 13, 38: 16, 40: 6, 42: 12, 44: 12}                       # retained checkpoints' holder counts
ALLOW = {30: 53, 32: 67, 34: 67, 36: 67}                                                          # production widths and their K
SEED = 1000003
R_SURVIVE, R_CLOSE = 0.5, 0.8
STEP_WALL_S, STEP_CPU_S, STAGE_S = 60, 60, 300
GIB, MIB = 1 << 30, 1 << 20


def digest(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def levels_of(W, K):
    """Per-lane elimination level (one chunk, n = W/2). Returns (levels, alive, lasts)."""
    n = W // 2
    alive, elim, lasts = E.run_lanes(W, n, 0, K, record=True)
    levels = [None] * (1 << n)
    for k, m in elim.items():
        while m:
            low = m & -m; p = low.bit_length() - 1; levels[p] = k; m ^= low
    return levels, alive, lasts


def spreads(levels, k):
    """Per deep prefix P = p >> k: (spread, prefix max, attaining count)."""
    out = {}
    for P in range(len(levels) >> k):
        block = levels[P << k:(P + 1) << k]
        mx = max(block); mn = min(block)
        out[P] = (mx - mn, mx, block.count(mx))
    return out


def grouping_by_divmod(levels, k):
    """The same grouping expressed independently: divmod on each lane index."""
    groups = {}
    for p, l in enumerate(levels):
        P, q = divmod(p, 1 << k)
        groups.setdefault(P, {})[q] = l
    out = {}
    for P, d in groups.items():
        vals = [d[q] for q in sorted(d)]
        out[P] = (max(vals) - min(vals), max(vals), vals.count(max(vals)))
    return out


def summarise(per_prefix, D):
    sp = [v[0] for v in per_prefix.values()]
    hist = {}
    for s in sp: hist[s] = hist.get(s, 0) + 1
    rec = [(P, v) for P, v in per_prefix.items() if v[1] == D]
    by_max = {}
    for v in per_prefix.values():
        by_max.setdefault(v[1], []).append(v[0])
    return {'prefixes': len(sp), 'median_spread': statistics.median(sp), 'mean_spread': round(statistics.fmean(sp), 3),
            'max_spread': max(sp), 'fraction_spread_zero': round(sum(1 for s in sp if s == 0) / len(sp), 4),
            'spread_histogram': {str(k): hist[k] for k in sorted(hist)},
            'record_prefixes': [{'prefix_hex': hex(P), 'spread': v[0], 'attaining': v[2]} for P, v in rec],
            'record_prefix_count': len(rec), 'record_attaining_total': sum(v[2] for _, v in rec),
            'median_spread_by_prefix_max': {str(m): statistics.median(v) for m, v in sorted(by_max.items())}}


def physical_control(W, levels, lasts, D, rnd):
    """Predeclared lanes: the first record lane, 0, 1, 2^(n-1), 2^n - 1, four seeded pseudo-random lanes. Each reconstructed
    start's physical death time must equal its level; the record lane's start must pass validate_witness at D."""
    n = W // 2
    rec_lane = levels.index(D)
    lanes = [rec_lane, 0, 1, 1 << (n - 1), (1 << n) - 1] + [rnd.randrange(1 << n) for _ in range(4)]
    checks = []
    for p in lanes:
        r = E.reconstruct(W, lasts, p)
        t = E.death_phys(r, D + 2)
        checks.append({'lane': p, 'start_hex': hex(r), 'bits': r.bit_length(), 'level': levels[p], 'physical_death': t, 'equal': t == levels[p]})
    ok_w, why = E.validate_witness(W, D, E.reconstruct(W, lasts, rec_lane))
    nonmax = any(c['level'] < D for c in checks)
    return {'lanes': checks, 'lanes_listed': len(lanes), 'distinct_lanes_checked': len(set(lanes)), 'all_equal': all(c['equal'] for c in checks),
            'record_witness_validated': ok_w, 'record_witness_note': why, 'includes_nonmaximal_level': nonmax,
            'scope': 'supports the physical-time reading for these lanes only'}, all(c['equal'] for c in checks) and ok_w and nonmax


def measure(W, K, table_D, holders, seed=SEED):
    """One width. Returns the result dict with 'status' in ('complete', 'FAIL') and 'failures'."""
    t0 = time.monotonic(); wall0 = time.strftime('%Y-%m-%dT%H:%M:%S')
    res = {'W': W, 'K': K, 'n': W // 2, 'lanes': 1 << (W // 2), 'started': wall0, 'd1_sha256': digest(E.__file__), 'this_sha256': digest(os.path.abspath(__file__)),
           'python': sys.version.split()[0], 'seed': seed, 'null_mechanism': 'random.Random(seed * W).shuffle of the level array (CPython Mersenne Twister)',
           'population': 'constrained lane ensemble, levels in [W, D(W)]', 'failures': []}
    levels, alive, lasts = levels_of(W, K)
    res['all_dead'] = alive == 0; res['undefined_levels'] = levels.count(None)
    if not res['all_dead'] or res['undefined_levels']:
        res['failures'].append('not every lane eliminated below K'); res['status'] = 'FAIL'; res['elapsed_s'] = round(time.monotonic() - t0, 3); return res
    res['max_level'] = max(levels); res['min_level'] = min(levels); res['table_D'] = table_D
    if res['max_level'] != table_D: res['failures'].append('max level %d != table D %d' % (res['max_level'], table_D))
    D = res['max_level']
    res['level_histogram'] = {str(l): levels.count(l) for l in sorted(set(levels))}
    att = levels.count(D); res['holders'] = {'checkpoint': holders, 'measured': att}
    if holders is not None and att != holders: res['failures'].append('attaining count %d != checkpoint %d' % (att, holders))
    rnd = random.Random(seed * W)
    perm = levels[:]; rnd.shuffle(perm)
    res['by_k'] = {}
    for k in (4, 6):
        if k >= W // 2: continue
        sl = spreads(levels, k); dm = grouping_by_divmod(levels, k)
        if sl != dm: res['failures'].append('grouping disagreement at k=%d' % k)
        real = summarise(sl, D); null = summarise(spreads(perm, k), D)
        R = (real['median_spread'] / null['median_spread']) if null['median_spread'] else None
        res['by_k'][str(k)] = {'measured': real, 'permuted_null': {kk: null[kk] for kk in ('median_spread', 'mean_spread', 'fraction_spread_zero', 'max_spread')},
                               'R_measured_over_null_median': None if R is None else round(R, 4), 'grouping_divmod_agrees': sl == dm}
    phys, ok_phys = physical_control(W, levels, lasts, D, random.Random(seed + W))
    res['physical_control'] = phys
    if not ok_phys: res['failures'].append('physical control failed')
    res['status'] = 'FAIL' if res['failures'] else 'complete'
    res['elapsed_s'] = round(time.monotonic() - t0, 3); res['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    return res


def decide(Rs, all_done):
    """The predeclared rule on the ratios so far (in width order). Returns (verdict, stop_now).
    CLOSES at the first defined R >= R_CLOSE; UNDEFINED-BASELINE at the first None; SURVIVES only when all widths are
    done and every R <= R_SURVIVE; INCONCLUSIVE when all are done otherwise; CONTINUE while widths remain."""
    for W in sorted(Rs):
        R = Rs[W]
        if R is None: return 'INCONCLUSIVE-undefined-baseline', True
        if R >= R_CLOSE: return 'CLOSES', True
    if not all_done: return 'CONTINUE', False
    return ('SURVIVES' if all(R <= R_SURVIVE for R in Rs.values()) else 'INCONCLUSIVE'), False


def atomic_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f: json.dump(obj, f, indent=1)
    os.replace(tmp, path)


def cli_measure(W, K, out):
    if W not in ALLOW or ALLOW[W] != K:
        print('REFUSED: (W, K) not in the allow-list %s' % ALLOW); return 3
    if os.path.exists(out):
        print('REFUSED: output exists'); return 3
    if digest(E.__file__) != D1_SHA256:
        print('REFUSED: d1_engine is not the pinned bytes'); return 3
    atomic_json(out, {'W': W, 'K': K, 'status': 'started', 'started': time.strftime('%Y-%m-%dT%H:%M:%S')})
    try:
        r = measure(W, K, TABLE[W], HOLDERS.get(W))
    except BaseException as e:
        atomic_json(out, {'W': W, 'K': K, 'status': 'FAIL', 'failures': ['exception: %r' % e]}); print('FAIL exception', repr(e)); return 1
    atomic_json(out, r)
    print(json.dumps({k: r.get(k) for k in ('W', 'K', 'lanes', 'status', 'failures', 'max_level', 'table_D', 'holders', 'elapsed_s')}))
    for k, v in r.get('by_k', {}).items():
        m = v['measured']
        print('k =', k, '| prefixes', m['prefixes'], '| median spread', m['median_spread'], '| spread-0 fraction', m['fraction_spread_zero'],
              '| record prefixes', m['record_prefix_count'], 'attaining', m['record_attaining_total'], '| null median', v['permuted_null']['median_spread'], '| R', v['R_measured_over_null_median'])
    return 0 if r['status'] == 'complete' else 1


def stage(out_dir):
    import w1a_harness as H
    if digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if digest(E.__file__) != D1_SHA256:
        print('REFUSED: d1_engine is not the pinned bytes'); return 3
    if not os.path.isabs(out_dir):
        print('REFUSED: OUT_DIR must be absolute'); return 3
    if os.path.exists(out_dir) and os.listdir(out_dir):
        print('REFUSED: output folder exists and is not empty'); return 3
    os.makedirs(out_dir, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 2 * GIB; H.CAPS['artifacts_max_bytes'] = 16 * MIB; H.CAPS['log_max_bytes'] = 1 * MIB
    sup = H.Supervisor(out_dir, out_dir); R = sup.receipts
    R['d5'] = {'this_sha256': digest(os.path.abspath(__file__)), 'd1_sha256': D1_SHA256, 'w1a_sha256': W1A_SHA256, 'widths': list(ALLOW.items()),
               'caps': {'step_wall_s': STEP_WALL_S, 'step_cpu_s': STEP_CPU_S, 'stage_s': STAGE_S, 'group_rss_stop_bytes': 2 * GIB, 'artifacts_max_bytes': 16 * MIB, 'log_max_bytes': 1 * MIB},
               'falsification_rule': {'R_survive_at_most': R_SURVIVE, 'R_close_at_least': R_CLOSE, 'k': 4}, 'nice_inherited': os.nice(0), 'steps_done': []}
    sup.save()
    if H.pressure_bad(sup.baseline):
        R['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        R['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    Rs = {}; executed = []; stop_width = None; verdict = 'CONTINUE'
    for W, K in sorted(ALLOW.items()):
        outj = os.path.join(out_dir, 'd5_W%d_K%d.json' % (W, K))

        def matcher(rc, text, outj=outj):
            try: d = json.load(open(outj))
            except Exception as e: return 'FAIL', 'no result file: %r' % e
            if rc != 0 or d.get('status') != 'complete' or d.get('failures'):
                return 'FAIL', 'rc %s status %s failures %s' % (rc, d.get('status'), d.get('failures'))
            return 'pass', 'complete; R(k=4) %s; record prefixes k4 %s k6 %s' % (d['by_k']['4']['R_measured_over_null_median'], d['by_k']['4']['measured']['record_prefix_count'], d['by_k'].get('6', {}).get('measured', {}).get('record_prefix_count'))
        rec = sup.run_step('d5_W%d' % W, [sys.executable, os.path.abspath(__file__), 'measure', str(W), str(K), outj], out_dir, STEP_WALL_S, STEP_CPU_S, matcher)
        R['d5']['steps_done'].append({'W': W, 'verdict': rec['verdict'], 'reason': rec['reason'], 'note': rec.get('match_note')}); sup.save()
        if rec['verdict'] != 'pass':
            R['stopped'] = 'step W=%d: %s (%s) %s' % (W, rec['verdict'], rec['reason'], rec.get('match_note')); sup.save(); print('STOP:', R['stopped']); return 1
        executed.append(W)
        d = json.load(open(outj)); Rs[W] = d['by_k']['4']['R_measured_over_null_median']
        all_done = (len(executed) == len(ALLOW))
        verdict, stop_now = decide(Rs, all_done)
        R['d5'].update({'R_by_width': dict(Rs), 'executed_widths': list(executed), 'all_widths_completed': all_done, 'hypothesis_verdict': verdict,
                        'stop_width': W if stop_now else None, 'scientific_stop': stop_now}); sup.save()
        if stop_now:
            break                                                   # the declared scientific stop: later widths are not run
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: executed widths', executed, '| all four completed:', R['d5']['all_widths_completed'], '| R by width', Rs, '| verdict', R['d5']['hypothesis_verdict'],
          '| scientific stop at', R['d5']['stop_width'])
    return 0


def test():
    notes = {}
    lit = [30, 34, 30, 32, 40, 40, 40, 40]                                   # literal nonconstant array, n = 3, k = 2: two hand-specified groups
    want = {0: (4, 34, 1), 1: (0, 40, 4)}
    notes['literal_groups_slicing'] = spreads(lit, 2) == want; notes['literal_groups_divmod'] = grouping_by_divmod(lit, 2) == want
    lit2 = [40, 34, 30, 32, 40, 40, 30, 40]                                  # same multiset, permuted: max and count preserved, grouping changed
    notes['permutation_changes_grouping'] = spreads(lit2, 2) != want
    const = summarise(spreads([5] * 128, 4), 5); notes['constant_array_spread_zero'] = const['median_spread'] == 0 and const['fraction_spread_zero'] == 1.0
    W = 14; D14 = E.D_phys(W, 200)[0]                                        # the small width's D from the physical engine, not from memory
    r = measure(W, D14 + 1, D14, None)
    notes['W14_status_complete'] = r['status'] == 'complete' and r['failures'] == []
    notes['W14_levels_at_least_W'] = r['min_level'] >= W
    notes['W14_prefix_count'] = r['by_k']['4']['measured']['prefixes'] == (1 << (W // 2 - 4))
    notes['W14_physical_control'] = r['physical_control']['all_equal'] and r['physical_control']['record_witness_validated'] and r['physical_control']['includes_nonmaximal_level']
    notes['W14_grouping_agrees'] = r['by_k']['4']['grouping_divmod_agrees']
    r2 = measure(W, D14 + 1, D14 - 2, None); notes['wrong_table_fails'] = r2['status'] == 'FAIL' and any('table' in f for f in r2['failures'])
    r3 = measure(W, D14 + 1, D14, 999); notes['wrong_holders_fails'] = r3['status'] == 'FAIL' and any('attaining' in f for f in r3['failures'])
    r4 = measure(W, D14 - 10, D14, None); notes['small_K_fails'] = r4['status'] == 'FAIL'
    import tempfile
    t = tempfile.mkdtemp(); p = os.path.join(t, 'x.json'); open(p, 'w').write('{}')
    notes['cli_refuses_existing_output'] = cli_measure(30, 53, p) == 3
    notes['cli_refuses_disallowed_width'] = cli_measure(14, D14 + 1, os.path.join(t, 'y.json')) == 3
    # the decision layer: a constant array (0/0) is an undefined-baseline stop, never CLOSES; the early threshold stops before later widths
    notes['decide_undefined_is_inconclusive_stop'] = decide({30: None}, False) == ('INCONCLUSIVE-undefined-baseline', True)
    notes['decide_early_threshold_closes_and_stops'] = decide({30: 0.3, 32: 0.85}, False) == ('CLOSES', True)
    notes['decide_continue_below_threshold'] = decide({30: 0.3, 32: 0.6}, False) == ('CONTINUE', False)
    notes['decide_survives_needs_all_four'] = decide({30: 0.3, 32: 0.4, 34: 0.2, 36: 0.5}, True) == ('SURVIVES', False) and decide({30: 0.3}, False) == ('CONTINUE', False)
    notes['decide_inconclusive_when_complete_between'] = decide({30: 0.3, 32: 0.6, 34: 0.2, 36: 0.5}, True) == ('INCONCLUSIVE', False)
    notes['decide_undefined_after_defined_stops'] = decide({30: 0.3, 32: None}, False) == ('INCONCLUSIVE-undefined-baseline', True)
    const_R = summarise(spreads([5] * 128, 4), 5)['median_spread']; notes['constant_array_gives_zero_over_zero'] = const_R == 0
    notes['W14_physical_distinct_coverage_reported'] = 'distinct_lanes_checked' in r['physical_control'] and r['physical_control']['distinct_lanes_checked'] <= r['physical_control']['lanes_listed']
    ok = all(v is True for v in notes.values())
    print(json.dumps({'notes': notes, 'W14': {k: r[k] for k in ('max_level', 'min_level', 'level_histogram', 'holders', 'elapsed_s')}, 'W14_k4': r['by_k']['4'], 'W14_physical': r['physical_control']}, indent=1)[:4000])
    print('D5 TEST', 'PASS' if ok else 'FAIL', len(notes)); return ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--test']:
        sys.exit(0 if test() else 1)
    if len(a) == 4 and a[0] == 'measure':
        sys.exit(cli_measure(int(a[1]), int(a[2]), a[3]))
    if len(a) == 2 and a[0] == 'stage':
        sys.exit(stage(a[1]))
    print(__doc__); sys.exit(2)
