#!/usr/bin/env python3
"""P2 latency pilot, revision 2 (Local, 2026-10-24, L882; revision 1 was L880's, reviewed in GPT's GC1790: "Choose (b), a supervised
latency pilot first"; persist partial and censor evidence; a shape-aware estimate). NOT an agreed job until GPT accepts this exact file;
nothing runs on import. It measures what L879 left unmeasured: the REQUEST ROUND-TRIP WALL TIME of small requests through P2's exact
evaluator path (P2's attempt recorder, S0's accepted transport and response check, P2's zero-wait poll, the driver and the GPU). It is
not GPU kernel time. Build time, each server's start and each width's end-to-end time are reported separately.

Per width (64, then 72; one server each, as P2): 2,000 hill-step-shaped requests (a random index and its W/2 single-bit neighbours,
W/2 lanes) and 200 restart-shaped requests (one lane), interleaved 10:1, numpy PCG64 seed 7 x W + 3 (disjoint from P2's seeds). Every
result passes through P2's Budgeted checks (domain, censor, counts; budget 10^7, never binding). Nothing is scored; no census is read.

Revision 2, GC1790:
  - Evidence is persisted as it accrues: the result file after every 500 requests and at each width's end, each width marked complete or
    not; a failure at W = 72 keeps W = 64's finished statistics; a censor's indices and deaths (Budgeted's witness) go into the result;
    P2's Recorder writes each attempted request before its send (current_request.json, request_journal.jsonl).
  - Statistics per shape: count, median, 90th percentile, maximum, mean (descriptive). The ESTIMATES use MEANS (medians do not add):
    (i) conservative-count: 5 seeds x sum over widths of (steps_max x mean step + restarts_max x mean restart), with GC1790's bounds
    steps_max = floor(B / n) and restarts_max = floor((B + n) / (n + 1)) for B = 838,860 and n = W/2 (26,214 and 25,420 at W = 64;
    23,301 and 22,672 at W = 72; the two maxima need not be attained together); (ii) stub-count: the same with the seed-1 counts against
    P2's stub (L879: 26,026 steps and 6,019 restarts at W = 64; 23,153 and 5,339 at W = 72, derived exactly from its gross and request
    counts). Both are timing ESTIMATES for P2's ten hill-climbing cases, not upper bounds: real trajectories differ from random
    neighbourhoods and latency varies. Random, beam and cross-entropy requests, scoring, build and cleanup are not measured here.
Negative control (in the stage): afterwards the same requests, through the same path (recorder, transport, checks), go to P2's CPU stub
server (no driver, no GPU) under 'stub_baseline'; the GPU-side share is the difference of the means. The matcher requires both.
Bindings: P2 (p2_search.py) pinned, and through it S0, the driver, kernels, helper, the S0 stage receipt and result; the built binary
must equal the one S0 passed. Stage caps (W1A): wall 180 s, CPU 180 s, group RSS 6 GiB, GPU budget 2 GiB, artifacts 10 MiB, log 10 MiB,
nothing else on the M5, no retry. A successful pilot does not launch P2 or change its cap.
Controls (`--controls`, CPU only, P2's stub server): full statistics at the exact counts; a censor stops and its evidence is retained
with the first width marked incomplete; a W = 72 failure keeps W = 64's finished statistics and leaves the failed request on disk; the
count bounds equal GC1790's table and the estimator's arithmetic is checked on fixed means; the stub-baseline function saves both
widths into the result; no server is left live.
Usage: python3 p2_latency_pilot.py --controls | stage OUT_DIR S0_STAGE_DIR
OUTCOME: (to be filled after the run)
"""
import json, os, sys, tempfile, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import s0_serve_controls as S0
import p2_search as P2

P2_SHA256 = '4556f188a67983f8b5ef9fb629a49bbe628748251db4ca54ebe7cc3d89214cc9'
STEPS, RESTARTS = 2000, 200
CHECKPOINT = 500
STUB_SEED1 = {64: (838851, 32045), 72: (838847, 28492)}    # (gross, requests) of hill climbing, seed 1, against P2's stub (L879)
STAGE_S = 180


def count_bounds(W, B=P2.PER_CASE):
    n = W // 2
    return B // n, (B + n) // (n + 1)


def stub_counts(W):
    n = W // 2; G, R = STUB_SEED1[W]; s, rem = divmod(G - R, n - 1)
    assert rem == 0 and s * n + (R - s) == G
    return s, R - s


def stats(xs):
    if not xs: return {'n': 0}
    s = sorted(xs); n = len(s)
    return {'n': n, 'median_ms': round(1000 * s[n // 2], 4), 'p90_ms': round(1000 * s[(9 * n) // 10], 4), 'max_ms': round(1000 * s[-1], 4),
            'mean_ms': round(1000 * sum(s) / n, 4)}


def estimates(L):
    """From complete per-width statistics: the two hill-climbing time ESTIMATES (seconds), using mean request times."""
    out = {'kind': 'ESTIMATE of request round-trip time for the ten hill-climbing cases; not an upper bound; other methods not included'}
    for name, counts in (('conservative_count', count_bounds), ('stub_count', stub_counts)):
        per = {}
        for W in P2.WIDTHS:
            st = L[str(W)]['stats']; s, r = counts(W)
            per[str(W)] = round(5 * (s * st['step']['mean_ms'] + r * st['restart']['mean_ms']) / 1000, 1)
        out[name] = {'per_width_five_seeds_s': per, 'total_s': round(sum(per.values()), 1),
                     'counts': {str(W): dict(zip(('steps', 'restarts'), counts(W))) for W in P2.WIDTHS}}
    return out


def measure(server_for, R, save, rec=None, steps=STEPS, restarts=RESTARTS):
    import numpy as np
    L = R.setdefault('latency', {})
    for W, T in P2.WIDTHS.items():
        t_w = time.monotonic(); srv = server_for(W); start_s = round(time.monotonic() - t_w, 4)
        ev = P2.Budgeted(P2.make_evaluator(srv, W, T, rec), W, 10 ** 7)
        rng = np.random.Generator(np.random.PCG64(7 * W + 3)); n = W // 2; tim = {'step': [], 'restart': []}

        def summary(complete):
            return {'complete': complete, 'stats': {k: stats(v) for k, v in tim.items()}, 'requests': ev.requests, 'gross': ev.gross,
                    'attempted_lanes': ev.attempted, 'server_spawn_s': start_s, 'width_wall_s': round(time.monotonic() - t_w, 3),
                    'measure': 'request round-trip wall time: recorder, transport, driver and GPU; not GPU kernel time'}
        L[str(W)] = summary(False); save()
        try:
            for k in range(steps + restarts):
                shape = 'restart' if k % 11 == 10 and len(tim['restart']) < restarts else 'step' if len(tim['step']) < steps else 'restart'
                x = int(rng.integers(0, 1 << n, dtype='uint64'))
                idx = [x] if shape == 'restart' else [x ^ (1 << b) for b in range(n)]
                t = time.monotonic(); ev(idx); tim[shape].append(time.monotonic() - t)
                if (k + 1) % CHECKPOINT == 0:
                    L[str(W)] = summary(False); save()
            q = srv.quiet()
            if q != 'silence': raise P2.Stop('the W = %d server was not live and silent before closing: %s' % (W, q))
            if not srv.close(): raise P2.Stop('the W = %d server was not verified dead' % W)
        except BaseException:
            L[str(W)] = summary(False)
            if ev.censor is not None: R['censor_event'] = ev.censor
            save(); raise
        L[str(W)] = summary(True); save()
    R['estimates'] = estimates(L); save()
    return R


def stub_baseline(out, R, save, steps=STEPS, restarts=RESTARTS):
    """The negative control: the same requests through the same path (recorder, transport, checks) to P2's CPU stub; no driver, no GPU."""
    bdir = os.path.join(out, 'stub_baseline'); os.makedirs(bdir, exist_ok=True); sp = os.path.join(bdir, 'stub.py'); open(sp, 'w').write(P2.STUB_SERVER)
    B = {}; brec = P2.Recorder(bdir)
    try:
        measure(lambda W: S0.Server([sys.executable, sp, 'ok', '0'], os.path.join(bdir, 'stub_stderr.log')), B,
                lambda: (R.__setitem__('stub_baseline', B), save()), brec, steps, restarts)
    finally:
        brec.close()
    return B


def controls():
    res = {}
    with tempfile.TemporaryDirectory() as tmp:
        sp = os.path.join(tmp, 'stub.py'); open(sp, 'w').write(P2.STUB_SERVER)
        stub = lambda mode, n_at: (lambda W: S0.Server([sys.executable, sp, mode, str(n_at)], os.path.join(tmp, 'e')))

        def go(server_for, steps=50, restarts=5):
            d = tempfile.mkdtemp(dir=tmp); R = {}; save = lambda: P2.atomic_json(os.path.join(d, 'pilot_result.json'), R)
            rec = P2.Recorder(d); err = None
            try:
                measure(server_for, R, save, rec, steps, restarts)
            except Exception as e:
                err = e
            finally:
                rec.close(); S0.close_all()
            disk = json.load(open(os.path.join(d, 'pilot_result.json')))
            cur = json.load(open(rec.cur)) if os.path.exists(rec.cur) else {}
            return R, err, disk, cur
        R, err, disk, cur = go(stub('ok', 0))
        res['stub_run_full_statistics'] = (err is None and disk == R and all(
            R['latency'][str(W)]['complete'] and R['latency'][str(W)]['stats']['step']['n'] == 50 and R['latency'][str(W)]['stats']['restart']['n'] == 5
            and R['latency'][str(W)]['requests'] == 55 and R['latency'][str(W)]['gross'] == R['latency'][str(W)]['attempted_lanes'] == 50 * (W // 2) + 5
            for W in P2.WIDTHS) and R['estimates']['conservative_count']['total_s'] > 0 and R['estimates']['stub_count']['total_s'] > 0)
        R, err, disk, cur = go(stub('censor', 7))
        ce = disk.get('censor_event') or {}
        res['stub_censor_stops_and_evidence_retained'] = (isinstance(err, P2.Censored) and ce.get('deaths', [None])[0] == -1 and len(ce.get('indices', [])) == 32
                                                          and disk['latency']['64']['complete'] is False and ce.get('request') == 7
                                                          and disk['latency']['64']['requests'] == 7 and disk['latency']['64']['stats']['step']['n'] == 6   # the censored request is charged, not timed
                                                          and '72' not in disk['latency'] and 'estimates' not in disk)
        order = iter(['ok', 'die'])
        R, err, disk, cur = go(lambda W: stub(next(order), 10)(W))
        res['second_width_failure_keeps_first'] = (isinstance(err, P2.Stop) and disk['latency']['64']['complete'] is True
                                                   and disk['latency']['64']['stats']['step']['n'] == 50 and disk['latency']['72']['complete'] is False
                                                   and cur.get('state') == 'failed' and cur.get('W') == 72 and 'estimates' not in disk)
        res['count_bounds_equal_gc1790'] = (count_bounds(64), count_bounds(72)) == ((26214, 25420), (23301, 22672))
        res['stub_counts_exact'] = (stub_counts(64), stub_counts(72)) == ((26026, 6019), (23153, 5339))
        fixed = {str(W): {'stats': {'step': {'mean_ms': 1.0}, 'restart': {'mean_ms': 0.5}}} for W in P2.WIDTHS}
        e = estimates(fixed)
        res['estimator_arithmetic'] = (e['conservative_count']['per_width_five_seeds_s'] == {'64': round(5 * (26214 + 0.5 * 25420) / 1000, 1), '72': round(5 * (23301 + 0.5 * 22672) / 1000, 1)}
                                       and e['stub_count']['per_width_five_seeds_s'] == {'64': round(5 * (26026 + 0.5 * 6019) / 1000, 1), '72': round(5 * (23153 + 0.5 * 5339) / 1000, 1)})
        d = tempfile.mkdtemp(dir=tmp); R = {}; save = lambda: P2.atomic_json(os.path.join(d, 'r.json'), R)
        B = stub_baseline(d, R, save, 50, 5); disk = json.load(open(os.path.join(d, 'r.json')))
        res['stub_baseline_function_saves_both_widths'] = (disk.get('stub_baseline', {}).get('latency', {}).get('72', {}).get('complete') is True
                                                           and disk['stub_baseline']['latency']['64']['stats']['step']['n'] == 50 and B is R['stub_baseline'])
        res['no_live_server_left'] = not S0.LIVE
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('PILOT CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


def run(out, s0_dir):
    t0 = time.monotonic(); os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); P2.atomic_json(os.path.join(out, 'pilot_result.json'), R, indent=1)
    rec = None
    try:
        pins = {'p2': (P.digest(P2.__file__), P2_SHA256), 's0': (P.digest(S0.__file__), P2.S0_SHA256), 'metal': (P.digest(P.METAL), P2.METAL_SHA256),
                'swift': (P.digest(P.SWIFT), P2.SWIFT_SHA256), 'p1_helper': (P.digest(P.__file__), P2.P1_HELPER_SHA256)}
        R['pins'] = {k: v[0] for k, v in pins.items()}
        bad = [k for k, (a, b) in pins.items() if a != b]
        if bad: raise P2.Stop('not the pinned bytes: %s' % bad)
        probs, dig = P2.check_s0_receipt(s0_dir); R['s0_receipt'] = dig
        if probs: raise P2.Stop('S0 receipt: %s' % probs)
        eng = P.Engine(out); R['build'] = eng.build(); save()
        if R['build'].get('binary_sha256') != dig['binary_sha256']: raise P2.Stop('the built binary differs from the one S0 passed')
        rec = P2.Recorder(out)
        measure(lambda W: S0.Server.engine(eng, out), R, save, rec)
        stub_baseline(out, R, save)
        R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save(); return R
    except BaseException as e:
        R['failure'] = {'type': type(e).__name__, 'message': str(e)[:1000], 'traceback': traceback.format_exc()[-3000:]}; save(); raise
    finally:
        if rec: rec.close()
        R['live_servers_at_finally'] = len(S0.LIVE); R['live_servers_closed_dead'] = S0.close_all(); save()


def stage(out, s0_dir):
    import w1a_harness as H
    if P.digest(H.__file__) != P2.W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    probs, dig = P2.check_s0_receipt(s0_dir)
    if probs:
        print('REFUSED: S0 receipt', probs); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 10 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['pilot'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'p2_sha256': P2_SHA256, 's0_receipt': dig, 'steps': STEPS, 'restarts': RESTARTS,
                   'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 10 << 20},
                   'nice_inherited': os.nice(0)}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'pilot_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        L = d.get('latency', {})
        good = (rc == 0 and d.get('complete') is True and d.get('live_servers_at_finally') == 0 and d.get('failure') is None and d.get('censor_event') is None
                and 'estimates' in d and all(X.get(str(W), {}).get('complete') is True and X[str(W)]['stats']['step']['n'] == STEPS
                                             and X[str(W)]['stats']['restart']['n'] == RESTARTS
                                             for X in (L, d.get('stub_baseline', {}).get('latency', {})) for W in P2.WIDTHS))
        if not good:
            return 'FAIL', 'rc %s complete %s failure %s' % (rc, d.get('complete'), (d.get('failure') or {}).get('message'))
        return 'pass', 'pilot complete: conservative-count ESTIMATE %s s, stub-count ESTIMATE %s s' % (
            d['estimates']['conservative_count']['total_s'], d['estimates']['stub_count']['total_s'])
    rec = sup.run_step('p2_latency_pilot', [sys.executable, os.path.abspath(__file__), 'run', rdir, s0_dir], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(a) == 3 and a[0] == 'run':
        try:
            run(a[1], a[2]); print('PILOT COMPLETE'); sys.exit(0)
        except (P2.Stop, P.Stop, RuntimeError) as e:
            print('PILOT STOPPED:', e); sys.exit(1)
    if len(a) == 3 and a[0] == 'stage':
        sys.exit(stage(a[1], a[2]))
    print(__doc__); sys.exit(2)
