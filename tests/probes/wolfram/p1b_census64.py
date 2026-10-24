#!/usr/bin/env python3
"""P1b, revision 1 (Local, 2026-10-24, L865): one GPU census at width 64, an independent second engine for D(64) = 116
(the CPU census of L820: d1 revision 4, maximum level 116 attained by exactly one chunk, 10686, lane 42727, start
0x88b46d66afc2fbd5, index (10686 << 18) | 42727 = 2,801,313,511). Built to GPT's six requirements of GC1778
(GPT-P1-ENGINE-REVIEW.md); the owner's word to proceed, 2026-10-24 afternoon. Nothing runs on import.

The engine is P1's (`p1_engine/lanes.metal`, `p1_engine/main.swift`), whose digests are PINNED below; the runner refuses if
either differs, and records the harness's and the built binary's digests and every job JSON. Scope: W = 64, T = 256, 32-lane
words, G = 2^19 lane-groups per batch, GPU budget 2 GiB, GPU reduction, trace disabled. Nothing else: no other width.

Steps, all inside one step of the W1A supervisor (stage 900 s wall and CPU, group RSS 6 GiB, pressure, swap 256 MiB,
artifacts 100 MiB, log 10 MiB), each engine call at most 120 s:
  1. Gate (before anything is trusted): lanes [0, 2^24) with the full death dump, compared lane for lane with d1's exact
     levels of chunks 0..63; its 64 samples re-simulated by the scalar engine. The dump is deleted after its digest.
  2. The census: [0, 2^32) exactly once, as 8 calls of 2^29 lanes (32 batches of 2^24 lanes each). Every call's result is
     checked before the next call starts: status, mode, W, T, word width, mutant empty, reduction gpu, its lo/hi, 2^29
     lanes, histogram sum plus censored equal to the lanes, 32 batches whose ranges are contiguous and 2^24 lanes each,
     64 samples per batch re-simulated by the scalar engine (2,048 per call). The calls' ranges are recorded and their
     union checked to be [0, 2^32) without gap or overlap.
  3. Finalization: censored must be 0 (otherwise the maximum is not D(64) and the outcome is "unresolved at T"); the maximum
     and its count aggregated over the calls; the maximizer list is complete only if no call truncated it and its length
     equals the count, otherwise it is reported as partial; EVERY retained maximizer is reconstructed, re-simulated by the
     scalar engine and checked by d1_engine.validate_witness at the maximum; d1 is run on every chunk holding a maximizer
     and the set of lanes at the maximum there must equal the GPU's maximizers in those chunks; if the maximum is 116 the
     known witness index must be among them.
  4. The result is written with `complete: true` only after all checks pass and disposable files are deleted.
Any engine error, failed check or disagreement stops the stage; the offending lanes are kept in the result as diagnostics,
never as a table value.

Predictions (L864, written before the run): maximum 116; the maximizer lanes all in chunk 10686, including 2,801,313,511; no
lane censored at 256; GPU wall 60 to 150 s; zero two-engine disagreements. Counterfactual: any other maximum or a maximizer
outside chunk 10686 means one of the two engines is wrong on some lane; the stage stops and both are re-examined.

Usage: python3 p1b_census64.py stage OUT_DIR     (absolute, new or empty)
       python3 p1b_census64.py run OUT_DIR       (the step the stage runs; not for direct use)
OUTCOME (run p1b-census64-20261024-1345 under the W1A supervisor, at this file ed372227..., harness ea9b7cc2..., lanes.metal
17a81e66..., main.swift 7f5c1b33..., binary aa629874...; this docstring is the only change since): PASS, 28 of 28 checks, stage 65 s.
Gate: all 16,777,216 lanes of [0, 2^24) equal d1's exact levels. Census: [0, 2^32) exactly once in 8 calls, 4,294,967,296 lanes,
censored 0, 16,384 sampled lanes re-simulated with no disagreement; maximum 116, attained by exactly 40 lanes, all in chunk
10686 (lanes 42,688 to 42,727, contiguous), including the known witness 2,801,313,511; every one re-simulated by the scalar
engine and validated at 116; d1 on chunk 10686 finds exactly the same 40 lanes. GPU 55.3 s (prediction 60 to 150 s: missed
low), census wall 60.4 s. So D(64) = 116 by two independent engines (numerical, not a kernel certificate).
"""
import hashlib, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import d1_engine as E

METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '7f5c1b339d52674d25576e77ece0f372157d6c2f38a88549c72984f620a0c419'
D1_SHA256 = 'e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
W, T, LB, G = 64, 256, 32, 1 << 19
CALL_LANES, CALLS, BATCH_LANES = 1 << 29, 8, 1 << 24
KNOWN = {'max': 116, 'chunk': 10686, 'index': (10686 << 18) | 42727, 'start': 0x88b46d66afc2fbd5}
STAGE_S = 900


class Stop(Exception):
    pass


def run(out):
    t0 = time.monotonic()
    os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'harness_sha256': P.digest(P.__file__),
         'scope': {'W': W, 'T': T, 'lane_bits': LB, 'G_max': G, 'gpu_budget_bytes': P.GPU_BUDGET, 'call_lanes': CALL_LANES, 'calls': CALLS},
         'checks': {}, 'calls': [], 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2)
        tmp = os.path.join(out, 'p1b_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 'p1b_result.json'))

    def check(name, ok, **detail):
        R['checks'][name] = {'pass': bool(ok), **detail}; save()
        if not ok:
            raise Stop('%s %s' % (name, json.dumps(detail)[:600]))

    check('pinned_metal', P.digest(P.METAL) == METAL_SHA256)
    check('pinned_swift', P.digest(P.SWIFT) == SWIFT_SHA256)
    check('pinned_d1', P.digest(E.__file__) == D1_SHA256)
    eng = P.Engine(out)
    R['build'] = eng.build(); save()

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

    # 1. the gate
    dp = os.path.join(out, 'gate_dump.u16')
    res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(BATCH_LANES), 'G_max': G, 'deaths_out': dp}, 'gate_W64')
    ok_fields, contiguous, bad, nsamp = validate_call(res, 0, BATCH_LANES, 1)
    dump = P.read_dump(dp); dd = P.digest(dp); os.remove(dp)
    import numpy as np
    t_ref = time.monotonic()
    lv = np.concatenate([P.d1_levels(W, c, KNOWN['max'] + 1) for c in range(64)])
    agree = int((dump == lv).sum())
    R['gate'] = {'lanes': int(len(dump)), 'agree_with_d1': agree, 'dump_sha256': dd, 'd1_reference_s': round(time.monotonic() - t_ref, 2),
                 'engine_wall_s': res['wall_total_s'], 'samples': nsamp}
    check('gate_fields', ok_fields and contiguous)
    check('gate_two_engine', not bad, disagreements=bad[:10])
    check('gate_d1_lane_for_lane', agree == BATCH_LANES, agree=agree)

    # 2. the census
    hist, censored, lanes = {}, 0, 0
    call_max = []
    t_census = time.monotonic()
    for j in range(CALLS):
        lo, hi = j * CALL_LANES, (j + 1) * CALL_LANES
        res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': str(lo), 'hi': str(hi), 'G_max': G}, 'census_W64_call%d' % j)
        ok_fields, contiguous, bad, nsamp = validate_call(res, lo, hi, CALL_LANES // BATCH_LANES)
        gpu = sum(b['t_build_gpu_s'] + b['t_sim_gpu_s'] for b in res['batches'])
        R['calls'].append({'call': j, 'lo': str(lo), 'hi': str(hi), 'lanes': int(res['lanes_total']), 'max': res['max'], 'max_count': int(res['max_count']),
                           'censored': int(res['censored']), 'maximizers': res['maximizers'], 'maximizers_truncated': res['maximizers_truncated'],
                           'samples': nsamp, 'gpu_s': round(gpu, 3), 'engine_wall_s': round(res['wall_total_s'], 3), 'setup_s': round(res['setup_s'], 3),
                           'process_wall_s': round(res['process_wall_s'], 3)})
        check('call%d_fields' % j, ok_fields and contiguous)
        check('call%d_two_engine' % j, not bad, disagreements=bad[:10])
        for k, v in res['histogram'].items():
            hist[int(k)] = hist.get(int(k), 0) + int(v)
        censored += int(res['censored']); lanes += int(res['lanes_total'])
        call_max.append((res['max'], int(res['max_count']), res['maximizers'], res['maximizers_truncated']))
    R['census_wall_s'] = round(time.monotonic() - t_census, 2)
    ranges = [(int(c['lo']), int(c['hi'])) for c in R['calls']]
    check('coverage_exact', ranges[0][0] == 0 and ranges[-1][1] == 1 << 32 and all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
          and lanes == 1 << 32 and sum(hist.values()) + censored == 1 << 32, lanes=lanes)

    # 3. finalization
    M = max(m for m, _, _, _ in call_max)
    count = sum(c for m, c, _, _ in call_max if m == M)
    mx = [int(n) for m, _, lst, _ in call_max if m == M for n in lst]
    truncated = any(t for m, _, _, t in call_max if m == M) or len(mx) != count
    R['census'] = {'lanes': lanes, 'censored': censored, 'max': M, 'max_count': count, 'maximizers': [str(n) for n in mx],
                   'maximizer_list_complete': not truncated, 'histogram': {str(k): hist[k] for k in sorted(hist)}}
    check('censored_zero', censored == 0, censored=censored)
    check('maximizer_list_complete', not truncated, count=count, retained=len(mx))
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
    if M == KNOWN['max']:
        check('known_witness_present', KNOWN['index'] in mx and P.recon(W, KNOWN['index']) == KNOWN['start'])
    R['predictions'] = {'max_116': M == 116, 'all_maximizers_in_chunk_10686': chunks == [10686], 'known_index_present': KNOWN['index'] in mx,
                        'no_censoring': censored == 0, 'gpu_wall_60_150_s': None, 'zero_disagreements': True}
    gpu_total = sum(c['gpu_s'] for c in R['calls'])
    R['predictions']['gpu_wall_60_150_s'] = 60 <= gpu_total <= 150
    R['gpu_total_s'] = round(gpu_total, 2)
    R['engine_calls'] = eng.log
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


def stage(out):
    import w1a_harness as H
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 100 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['p1b'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'harness_sha256': P.digest(P.__file__), 'metal_sha256': METAL_SHA256,
                 'swift_sha256': SWIFT_SHA256, 'd1_sha256': D1_SHA256, 'w1a_sha256': W1A_SHA256, 'nice_inherited': os.nice(0),
                 'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 100 << 20,
                          'call_timeout_s': P.CALL_TIMEOUT_S, 'gpu_budget_bytes': P.GPU_BUDGET}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'p1b_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        if rc != 0 or not d.get('complete') or not all(v['pass'] for v in d['checks'].values()):
            return 'FAIL', 'rc %s complete %s' % (rc, d.get('complete'))
        c = d['census']
        return 'pass', 'W64 census complete: max %d x%d, censored %d, %d lanes, maximizers complete %s' % (c['max'], c['max_count'], c['censored'], c['lanes'], c['maximizer_list_complete'])
    rec = sup.run_step('p1b_census64', [sys.executable, os.path.abspath(__file__), 'run', rdir], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == 'run':
        try:
            R = run(a[1]); print('P1B COMPLETE max', R['census']['max'], 'x', R['census']['max_count']); sys.exit(0)
        except (Stop, P.Stop, RuntimeError) as e:
            print('P1B STOPPED:', e); sys.exit(1)
    if len(a) == 2 and a[0] == 'stage':
        sys.exit(stage(a[1]))
    print(__doc__); sys.exit(2)
