#!/usr/bin/env python3
"""P2 latency pilot (Local, 2026-10-24, L880; option (b) of L879). NOT an agreed job until GPT accepts this exact file; nothing runs on
import. It measures what L879 left unmeasured: the wall time of a SMALL request through P2's exact evaluator path (S0's accepted
transport and response check, P2's zero-wait poll) on the GPU, so the P2 stage's 5,400 s deadline is set against a measurement.

Per width (64, then 72; one server each, as P2): 2,000 hill-step-shaped requests (a random index and its W/2 single-bit neighbours,
W/2 lanes) and 200 restart-shaped requests (one lane), interleaved 10:1, with numpy PCG64 seed 7 x W + 3 (disjoint from P2's seeds).
Every result goes through P2's Budgeted wrapper (domain, censor and count checks; budget 10^7, never binding). Nothing is scored and no
census is read. Per shape: median, 90th percentile, maximum and mean request time; then the projection the pilot exists for:
median step time x 32,045 (W = 64) and x 28,492 (W = 72), the hill-climbing request counts of seed 1 against the stub (L879), times
five seeds, as an ESTIMATE of P2's hill-climbing time, labelled as such (seeds differ in their request counts).

Bindings: P2 (p2_search.py) pinned; through it S0, the driver, the kernels and the helper, and the S0 stage receipt and result; the
binary must equal the one S0 passed. Stage caps (W1A): wall 180 s, CPU 180 s, group RSS 6 GiB, GPU budget 2 GiB, artifacts 10 MiB,
nothing else on the M5, no retry. Controls (`--controls`, CPU only): the measurement loop against P2's stub server produces the full
statistics with the exact request counts, and a censor from the stub stops it.
Usage: python3 p2_latency_pilot.py --controls | stage OUT_DIR S0_STAGE_DIR
OUTCOME: (to be filled after the run)
"""
import json, os, sys, tempfile, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import s0_serve_controls as S0
import p2_search as P2

P2_SHA256 = '385c0d8bbb326bc13436b98b04afe5101887deddcd99cf51dbfa44744a0f20b3'
STEPS, RESTARTS = 2000, 200
HILL_REQUESTS = {64: 32045, 72: 28492}     # seed 1 against the stub (L879)
STAGE_S = 180


def stats(xs):
    s = sorted(xs); n = len(s)
    return {'n': n, 'median_ms': round(1000 * s[n // 2], 4), 'p90_ms': round(1000 * s[(9 * n) // 10], 4), 'max_ms': round(1000 * s[-1], 4),
            'mean_ms': round(1000 * sum(s) / n, 4)}


def measure(server_for, steps=STEPS, restarts=RESTARTS):
    import numpy as np
    out = {}
    for W, T in P2.WIDTHS.items():
        srv = server_for(W); ev = P2.Budgeted(P2.make_evaluator(srv, W, T), W, 10 ** 7)
        rng = np.random.Generator(np.random.PCG64(7 * W + 3)); n = W // 2; tim = {'step': [], 'restart': []}
        for k in range(steps + restarts):
            shape = 'restart' if k % 11 == 10 and len(tim['restart']) < restarts else 'step' if len(tim['step']) < steps else 'restart'
            x = int(rng.integers(0, 1 << n, dtype='uint64'))
            idx = [x] if shape == 'restart' else [x ^ (1 << b) for b in range(n)]
            t = time.monotonic(); ev(idx); tim[shape].append(time.monotonic() - t)
        q = srv.quiet()
        if q != 'silence': raise P2.Stop('the W = %d server was not live and silent before closing: %s' % (W, q))
        if not srv.close(): raise P2.Stop('the W = %d server was not verified dead' % W)
        st = {s: stats(v) for s, v in tim.items()}
        est = st['step']['median_ms'] * HILL_REQUESTS[W] * 5 / 1000
        out[str(W)] = {'stats': st, 'requests': ev.requests, 'gross': ev.gross,
                       'ESTIMATE_hill_five_seeds_s': round(est, 1), 'estimate_basis': 'median step time x %d requests x 5 seeds' % HILL_REQUESTS[W]}
    out['ESTIMATE_hill_total_s'] = round(sum(out[str(W)]['ESTIMATE_hill_five_seeds_s'] for W in P2.WIDTHS), 1)
    return out


def controls():
    res = {}
    with tempfile.TemporaryDirectory() as tmp:
        def stub(mode, n_at):
            p = os.path.join(tmp, 'stub.py'); open(p, 'w').write(P2.STUB_SERVER)
            return lambda W: S0.Server([sys.executable, p, mode, str(n_at)], os.path.join(tmp, 'e'))
        m = measure(stub('ok', 0), steps=50, restarts=5)
        res['stub_run_full_statistics'] = (all(m[str(W)]['stats']['step']['n'] == 50 and m[str(W)]['stats']['restart']['n'] == 5 and m[str(W)]['requests'] == 55
                                               and m[str(W)]['gross'] == 50 * (W // 2) + 5 for W in P2.WIDTHS) and not S0.LIVE and m['ESTIMATE_hill_total_s'] > 0)
        try:
            measure(stub('censor', 7), steps=50, restarts=5); res['stub_censor_stops'] = False
        except P2.Censored:
            res['stub_censor_stops'] = True
        S0.close_all(); res['no_live_server_left'] = not S0.LIVE
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('PILOT CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


def run(out, s0_dir):
    t0 = time.monotonic(); os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); P2.atomic_json(os.path.join(out, 'pilot_result.json'), R, indent=1)
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
        R['latency'] = measure(lambda W: S0.Server.engine(eng, out))
        R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save(); return R
    except BaseException as e:
        R['failure'] = {'type': type(e).__name__, 'message': str(e)[:1000], 'traceback': traceback.format_exc()[-3000:]}; save(); raise
    finally:
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
        good = (rc == 0 and d.get('complete') is True and d.get('live_servers_at_finally') == 0 and d.get('failure') is None
                and all(L.get(str(W), {}).get('stats', {}).get('step', {}).get('n') == STEPS and L[str(W)]['stats'].get('restart', {}).get('n') == RESTARTS for W in P2.WIDTHS))
        return ('pass', 'pilot complete: estimate %s s for the ten hill cases' % L.get('ESTIMATE_hill_total_s')) if good else ('FAIL', 'rc %s complete %s' % (rc, d.get('complete')))
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
