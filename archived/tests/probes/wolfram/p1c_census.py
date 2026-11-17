#!/usr/bin/env python3
"""P1c, revision 4 (Local, 2026-10-24, L889: the width-76 census proposed to GPT; W = 76 admitted with its cap and predicted range, nothing
else changed). Revision 3 (Local, 2026-10-24, L887: the width-74 census, run once under GC1795, D(74) = 134; three changes only, listed below). Revision 2 (Local, 2026-10-24, L870; revision 1 ran W66..W72, L866/L868; revision 2 applies GPT's GC1780 corrections for
reuse: JSON invariants per call, the deep-prefix statistic descriptive only, a gate mismatch packet kept before the dump is deleted): GPU censuses beyond the CPU frontier, W = 66, 68, 70, 72, each giving the exact
D(W) numerically (complete coverage of the class, every maximizer validated), with no known answer to compare against.
The owner's word (2026-10-24 afternoon): proceed, Local solo, without GPT or Cloud. P1b's runner (GC1778's six requirements)
generalized; the known-answer checks are replaced by checks that need no known answer. Nothing runs on import.

Engine: P1's, digests PINNED (`lanes.metal` 17a81e66..., `main.swift` 7f5c1b33...), the binary's digest and every job JSON
recorded. Scope per run: one width W in {66, 68, 70, 72}, T = 4W, 32-lane words, G = 2^19, GPU budget 2 GiB, GPU reduction.

Steps, inside one step of the W1A supervisor (stage cap per width: 66: 900 s, 68: 1,200 s, 70: 1,800 s, 72: 2,700 s; group
RSS 6 GiB; pressure; swap 256 MiB; artifacts 100 MiB), each engine call at most 120 s:
  1. Gate: lanes [0, 2^24) dumped and compared lane for lane with d1's exact levels of chunks 0..63 (K = T + 1); 64 samples
     re-simulated by the scalar engine.
  2. Carried witnesses (needs no known answer): the 40 maximizers of the W = 64 census (P1b, L865) are starts of width <= W;
     at width W their indices are index_of(W, start) and each must die at exactly 116 (list mode, and the scalar engine);
     and if a previous width's result is given (--prev), its maximizers are carried the same way at their maximum.
  3. The census: [0, 2^(W/2)) exactly once in calls of 2^29 lanes (32 batches of 2^24); every call's fields checked before
     the next (status, mode, W, T, word width, mutant empty, gpu reduction, lo/hi, lanes, histogram sum, 32 contiguous
     batches of 2^24), 64 samples per batch re-simulated; the union checked to be the whole class.
  4. Finalization: censored must be 0 (else "unresolved at T", no value); the maximum M and its count over the calls; the
     maximizer list complete only if untruncated and equal to the count; every retained maximizer re-simulated by the scalar
     engine and checked by d1_engine.validate_witness at M; d1 on every chunk holding a maximizer, its lanes at M equal to the
     GPU's; monotonicity M >= 116 and M >= the previous width's maximum (a start of width W is a start of width W + 2).
  5. `complete: true` only after every check passes and disposable files are deleted. Any failure stops; offending lanes are
     kept as diagnostics, never as a table value.

Predictions (written before the runs; the table so far 52: 96, 56: 100, 60: 114, 64: 116, D(W)/W between 1.73 and 1.90 for
W = 20..64): D(66) in [116, 126]; D(68) in [D(66), 130]; D(70) in [D(68), 134]; D(72) in [D(70), 138]; no censoring at 4W;
the fraction dying at W within 0.001 of one half at every width; (revision 2: the shared-prefix length is reported descriptively,
not scored, GC1780); GPU time per lane within 20% of W = 64's 12.9 ns, so about 2, 4.5, 9
and 19 minutes. Counterfactual: a maximum below the previous width's, a carried witness not at its death, or any
two-engine disagreement is an engine fault, and the run stops.

Revision 3 (L887), for the one width W = 74, nothing else changed in the census logic:
  1. W = 74 in scope, stage cap 3,600 s (the ESTIMATE from the measured 16.682 ns per lane at W = 72 is 2,293 to 2,405 s for 2^37
     lanes; 256 calls of 2^29 lanes, each about 9 to 10 s against the 120 s call cap); predicted range [D(72) = 130, 140].
  2. The driver pin moves from revision 3 (7f5c1b33) to revision 6 (6b76fe74). The census path is byte-identical: `git diff
     a9ba9d28 3639a90b` on main.swift is 112 inserted lines, all inside the serve-mode block, which exits before the census code,
     and one changed comment line (the list of modes). The kernels (17a81e66), d1 (e924602e) and W1A (3f908914) are unchanged.
  3. One DESCRIPTIVE field, never a gate: `occupied_4096_blocks`, the number of distinct (index >> 12) among the maximizers, for
     L885's concentration observation (GC1794: not implied at W = 74). Predicted at most 8.
Revision 4 (L889): W = 76 in scope, stage cap 7,200 s. ESTIMATE from width 74's MEASURED 17.194 ns per lane of census wall time: 2^38
lanes take 4,726 to 4,948 s at 17.194 to 18.0 ns, in 512 calls of 2^29 lanes, each about 9 to 10 s against the 120 s call cap.
Predicted range [D(74) = 134, 146] (ratio 1.76 to 1.92). Run with --prev the width-74 result, so its 178 maximizers are carried at 134.
Usage: python3 p1c_census.py stage W OUT_DIR [--prev PREV_RESULT.json]
       python3 p1c_census.py run W OUT_DIR [--prev PREV_RESULT.json]     (the step the stage runs)
OUTCOME (W = 74, the one GC1795-accepted stage at revision 3, c9174d25, 2026-10-24 17:26 to 18:06 BST, L889): W1A pass; complete,
782 checks passed, zero censored; D(74) = 134 with 178 maximizers in 2 blocks of 4,096 indices; census wall 2,363.12 s (17.194 ns
per lane), GPU 2,206.02 s (16.051 ns per lane); fraction dying at W 0.4999942. Earlier widths' outcomes are in L866 and L868.
OUTCOME (W = 76, the one GC1800-accepted stage at revision 4, ddb69cc2, 2026-10-24 18:21 to 19:46 BST, L895): W1A pass; complete,
1,550 checks passed, zero censored; D(76) = 138 with 64 maximizers in 3 blocks of 4,096 indices (no shared high bit); census wall
5,065.3 s (18.427 ns per lane), GPU 4,740.21 s (17.245 ns per lane); fraction dying at W 0.5000026.
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E

METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec'   # driver revision 6; census path identical to revision 3 (L887)
D1_SHA256 = 'e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_CAP = {66: 900, 68: 1200, 70: 1800, 72: 2700, 74: 3600, 76: 7200}
LB, G = 32, 1 << 19
CALL_LANES, BATCH_LANES = 1 << 29, 1 << 24
W64_MAXIMIZER_INDICES = range(2801313472, 2801313512)   # P1b, L865: the 40 lanes of chunk 10686 at death 116
PREDICTED = {66: (116, 126), 68: (None, 130), 70: (None, 134), 72: (None, 138), 74: (None, 140), 76: (None, 146)}


class Stop(Exception):
    pass


def run(W, out, prev_path=None):
    import numpy as np
    t0 = time.monotonic()
    os.makedirs(out, exist_ok=True)
    T = 4 * W; nlanes = 1 << (W // 2); calls = nlanes // CALL_LANES
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'harness_sha256': P.digest(P.__file__),
         'scope': {'W': W, 'T': T, 'lane_bits': LB, 'G_max': G, 'lanes': nlanes, 'calls': calls, 'gpu_budget_bytes': P.GPU_BUDGET}, 'checks': {}, 'calls': [], 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2)
        tmp = os.path.join(out, 'p1c_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 'p1c_result.json'))

    def check(name, ok, **detail):
        R['checks'][name] = {'pass': bool(ok), **detail}; save()
        if not ok:
            raise Stop('%s %s' % (name, json.dumps(detail)[:600]))

    if W not in STAGE_CAP:
        raise Stop('W not in scope')
    check('pinned_metal', P.digest(P.METAL) == METAL_SHA256)
    check('pinned_swift', P.digest(P.SWIFT) == SWIFT_SHA256)
    check('pinned_d1', P.digest(E.__file__) == D1_SHA256)
    eng = P.Engine(out)
    R['build'] = eng.build(); save()

    def invariants(res, lo, hi):
        """GC1780 item 4: cheap consistency of the driver's JSON, independent of how it was produced."""
        h = {int(k): int(v) for k, v in res['histogram'].items()}
        probs = []
        if any(v < 0 for v in h.values()) or int(res['censored']) < 0: probs.append('negative count')
        if any(k % 2 or k < 0 or k > T for k in h): probs.append('histogram level odd or out of [0, T]')
        populated = [k for k, v in h.items() if v > 0]
        mx = max(populated) if populated else -1
        if res['max'] != mx: probs.append('max %s != largest populated level %s' % (res['max'], mx))
        if mx >= 0 and int(res['max_count']) != h[mx]: probs.append('max_count != histogram[max]')
        idx = [int(n) for n in res['maximizers']]
        if len(set(idx)) != len(idx) or any(not (lo <= n < hi) for n in idx): probs.append('maximizers not distinct or out of range')
        for b in res['batches']:
            bl = int(b['first_group_base']); sm = [int(n) for n, _ in b['samples']]
            if len(set(sm)) != len(sm) or any(not (bl <= n < bl + int(b['lanes'])) for n in sm): probs.append('batch %s samples not distinct or outside the batch' % b['batch'])
        return probs

    def validate_call(res, lo, hi, nbatches):
        hsum = sum(int(v) for v in res['histogram'].values()) + int(res['censored'])
        ok_fields = (res['status'] == 'ok' and res['mode'] == 'census' and res['W'] == W and res['T'] == T and res['lane_bits'] == LB
                     and res['mutant'] == '' and res['reduce'] == 'gpu' and res['lo'] == str(lo) and res['hi'] == str(hi)
                     and int(res['lanes_total']) == hi - lo and hsum == hi - lo and len(res['batches']) == nbatches)
        contiguous = all(int(b['first_group_base']) == lo + i * BATCH_LANES and int(b['lanes']) == BATCH_LANES for i, b in enumerate(res['batches']))
        bad, nsamp = [], 0
        for b in res['batches']:
            if len(b['samples']) != 64:
                bad.append(('sample-count', b['batch'], len(b['samples'])))
            for n, d in b['samples']:
                n, d = int(n), int(d); nsamp += 1
                sd = P.death(P.recon(W, n), T)
                if sd != d:
                    bad.append((n, d, sd))
        return ok_fields, contiguous, bad, nsamp

    # 1. gate
    dp = os.path.join(out, 'gate_dump.u16')
    res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(BATCH_LANES), 'G_max': G, 'deaths_out': dp}, 'gate_W%d' % W)
    ok_fields, contiguous, bad, nsamp = validate_call(res, 0, BATCH_LANES, 1)
    dump = P.read_dump(dp); dd = P.digest(dp)
    t_ref = time.monotonic()
    lv = np.concatenate([P.d1_levels(W, c, T + 1) for c in range(64)])
    agree = int((dump == lv).sum())
    if agree != BATCH_LANES:      # GC1780 item 3: keep a diagnostic packet and the dump before anything is deleted
        bad_idx = np.nonzero(dump != lv)[0][:1000]
        json.dump([{'index': int(i), 'start': hex(P.recon(W, int(i))), 'gpu': int(dump[i]), 'd1': int(lv[i])} for i in bad_idx],
                  open(os.path.join(out, 'gate_mismatches.json'), 'w'))
    else:
        os.remove(dp)
    R['gate'] = {'lanes': int(len(dump)), 'agree_with_d1': agree, 'dump_sha256': dd, 'd1_reference_s': round(time.monotonic() - t_ref, 2), 'samples': nsamp}
    check('gate_fields', ok_fields and contiguous)
    check('gate_two_engine', not bad, disagreements=bad[:10])
    check('gate_d1_lane_for_lane', agree == BATCH_LANES, agree=agree)

    # 2. carried witnesses
    carried = [(P.recon(64, n), 116, 'W64') for n in W64_MAXIMIZER_INDICES]
    prev_max = 116
    if prev_path:
        pr = json.load(open(prev_path))
        if not pr.get('complete'):
            raise Stop('the previous result is not complete')
        pW, pM = pr['scope']['W'], pr['census']['max']; prev_max = max(prev_max, pM)
        carried += [(int(w['start'], 16), pM, 'W%d' % pW) for w in pr['census']['witnesses']]
        R['prev'] = {'W': pW, 'max': pM, 'witnesses': len(pr['census']['witnesses']), 'sha256': P.digest(prev_path)}
    idx = [P.index_of(W, s) for s, _, _ in carried]
    check('carried_roundtrip', all(P.recon(W, i) == s for i, (s, _, _) in zip(idx, carried)))
    res = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': T, 'indices': [str(i) for i in idx]}, 'carried_W%d' % W)
    got = {int(x['index']): x['death'] for x in res['deaths']}
    off = [(hex(s), want, got[i], src) for i, (s, want, src) in zip(idx, carried) if got[i] != want or P.death(s, T) != want]
    check('carried_witnesses_at_their_death', not off, n=len(carried), offending=off[:5])

    # 3. census
    hist, censored, lanes, call_max = {}, 0, 0, []
    t_census = time.monotonic()
    for j in range(calls):
        lo, hi = j * CALL_LANES, (j + 1) * CALL_LANES
        res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': str(lo), 'hi': str(hi), 'G_max': G}, 'census_W%d_call%d' % (W, j))
        ok_fields, contiguous, bad, nsamp = validate_call(res, lo, hi, CALL_LANES // BATCH_LANES)
        gpu = sum(b['t_build_gpu_s'] + b['t_sim_gpu_s'] for b in res['batches'])
        R['calls'].append({'call': j, 'lo': str(lo), 'hi': str(hi), 'lanes': int(res['lanes_total']), 'max': res['max'], 'max_count': int(res['max_count']),
                           'censored': int(res['censored']), 'maximizers': res['maximizers'], 'maximizers_truncated': res['maximizers_truncated'],
                           'samples': nsamp, 'gpu_s': round(gpu, 3), 'engine_wall_s': round(res['wall_total_s'], 3), 'process_wall_s': round(res['process_wall_s'], 3)})
        check('call%d_fields' % j, ok_fields and contiguous)
        inv = invariants(res, lo, hi)
        check('call%d_invariants' % j, not inv, problems=inv[:5])
        check('call%d_two_engine' % j, not bad, disagreements=bad[:10])
        for k, v in res['histogram'].items():
            hist[int(k)] = hist.get(int(k), 0) + int(v)
        censored += int(res['censored']); lanes += int(res['lanes_total'])
        call_max.append((res['max'], int(res['max_count']), res['maximizers'], res['maximizers_truncated']))
    R['census_wall_s'] = round(time.monotonic() - t_census, 2)
    ranges = [(int(c['lo']), int(c['hi'])) for c in R['calls']]
    check('coverage_exact', ranges[0][0] == 0 and ranges[-1][1] == nlanes and all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
          and lanes == nlanes and sum(hist.values()) + censored == nlanes, lanes=lanes)

    # 4. finalization
    M = max(m for m, _, _, _ in call_max)
    count = sum(c for m, c, _, _ in call_max if m == M)
    mx = [int(n) for m, _, lst, _ in call_max if m == M for n in lst]
    truncated = any(t for m, _, _, t in call_max if m == M) or len(mx) != count
    R['census'] = {'lanes': lanes, 'censored': censored, 'max': M, 'max_count': count, 'maximizers': [str(n) for n in mx], 'maximizer_list_complete': not truncated,
                   'histogram': {str(k): hist[k] for k in sorted(hist)}, 'fraction_at_W': hist.get(W, 0) / nlanes,
                   'occupied_4096_blocks_DESCRIPTIVE': len({n >> 12 for n in mx})}
    check('censored_zero', censored == 0, censored=censored)
    check('maximizer_list_complete', not truncated, count=count, retained=len(mx))
    check('monotone', M >= 116 and M >= prev_max, max=M, prev_max=prev_max)
    wit = []
    for n in mx:
        s = P.recon(W, n); sd = P.death(s, T); ok, why = E.validate_witness(W, M, s)
        wit.append({'index': str(n), 'chunk': n >> 18, 'lane': n & ((1 << 18) - 1), 'start': hex(s), 'bits': s.bit_length(), 'scalar_death': sd, 'validate_witness': why})
        if sd != M or not ok:
            R['census']['witnesses'] = wit; check('maximizers_scalar_and_validated', False, offending=wit[-1])
    R['census']['witnesses'] = wit
    check('maximizers_scalar_and_validated', True, n=len(wit))
    chunks = sorted({n >> 18 for n in mx})
    d1_at_max = []
    for c in chunks:
        lvc = P.d1_levels(W, c, M + 1)
        d1_at_max += [(c << 18) | int(p) for p in np.nonzero(lvc == M)[0]]
    check('d1_on_maximizer_chunks', sorted(d1_at_max) == sorted(mx), chunks=chunks, d1_lanes_at_max=len(d1_at_max))
    # the deep-prefix observation, DESCRIPTIVE only (GC1780 item 2: any finite set agrees above some k; no threshold was predeclared)
    k = 0
    while len({n >> k for n in mx}) > 1:
        k += 1
    gpu_total = sum(c['gpu_s'] for c in R['calls'])
    lo_p, hi_p = PREDICTED[W]
    R['predictions'] = {'max_in_range': (M >= (lo_p if lo_p is not None else prev_max)) and M <= hi_p, 'predicted_range': [lo_p if lo_p is not None else prev_max, hi_p],
                        'no_censoring': censored == 0, 'fraction_at_W_within_0.001_of_half': abs(hist.get(W, 0) / nlanes - 0.5) <= 0.001,
                        'maximizers_vary_in_lowest_free_bits_DESCRIPTIVE': k, 'common_prefix_free_bits_DESCRIPTIVE': W // 2 - k,
                        'gpu_ns_per_lane': round(gpu_total / nlanes * 1e9, 2), 'gpu_ns_per_lane_within_20pct_of_12.9': abs(gpu_total / nlanes * 1e9 - 12.9) <= 0.2 * 12.9}
    R['gpu_total_s'] = round(gpu_total, 2); R['engine_calls'] = len(eng.log)
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


def stage(W, out, prev_path=None):
    import w1a_harness as H
    if W not in STAGE_CAP:
        print('REFUSED: W must be one of', sorted(STAGE_CAP)); return 3
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    cap = STAGE_CAP[W]
    H.CAPS['stage_s'] = cap; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 100 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['p1c'] = {'W': W, 'this_sha256': P.digest(os.path.abspath(__file__)), 'harness_sha256': P.digest(P.__file__), 'metal_sha256': METAL_SHA256, 'swift_sha256': SWIFT_SHA256,
                 'd1_sha256': D1_SHA256, 'w1a_sha256': W1A_SHA256, 'prev': prev_path and os.path.basename(os.path.dirname(prev_path)), 'nice_inherited': os.nice(0),
                 'caps': {'stage_s': cap, 'step_wall_s': cap, 'step_cpu_s': cap, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 100 << 20, 'call_timeout_s': P.CALL_TIMEOUT_S}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'p1c_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        if rc != 0 or not d.get('complete') or not all(v['pass'] for v in d['checks'].values()):
            return 'FAIL', 'rc %s complete %s' % (rc, d.get('complete'))
        c = d['census']
        return 'pass', 'W%d census complete: max %d x%d, censored %d, %d lanes' % (W, c['max'], c['max_count'], c['censored'], c['lanes'])
    cmd = [sys.executable, os.path.abspath(__file__), 'run', str(W), rdir] + (['--prev', prev_path] if prev_path else [])
    rec = sup.run_step('p1c_census_W%d' % W, cmd, out, cap, cap, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    prev = None
    if '--prev' in a:
        i = a.index('--prev'); prev = a[i + 1]; a = a[:i] + a[i + 2:]
    if len(a) == 3 and a[0] == 'run':
        try:
            R = run(int(a[1]), a[2], prev); print('P1C COMPLETE W', a[1], 'max', R['census']['max'], 'x', R['census']['max_count']); sys.exit(0)
        except (Stop, P.Stop, RuntimeError) as e:
            print('P1C STOPPED:', e); sys.exit(1)
    if len(a) == 3 and a[0] == 'stage':
        sys.exit(stage(int(a[1]), a[2], prev))
    print(__doc__); sys.exit(2)
