#!/usr/bin/env python3
"""S0, revision 1 (Local, 2026-10-24, L875): the control stage for the P1 driver's persistent `serve` mode (driver revision 5), the
evaluator P2 will use (L872), with GPT's GC1785 corrections: strict input, bounded host memory, and this frozen client. NOT an agreed
job until GPT accepts this exact file and the pinned driver; nothing runs on import.

The client: starts `p1engine JOB serve` in its own session and process group; one request per line; a 10 s deadline per response
(select on stdout); checks every response for exactly the keys {id, W, T, deaths} (or {id, error} where a refusal is expected), the
echoed id, W and T, the count and order against the request (duplicates preserved), and every death an integer that is -1 or an even
number in [0, T]; after each good response checks that no further line is waiting (no stale or trailing output); on any violation,
timeout or unexpected exit kills the server's process group and stops the stage. Refusals are checked by their error response AND
the server's non-zero exit; a fresh server is started after each.

Controls (each must pass; the first failure stops):
  A  equality with one-shot `list` mode: 100,000 seeded indices at W = 64 (T = 256) and at W = 72 (T = 288), in requests of 65,536 and
     34,464 indices, lane for lane.
  B  the 40 W = 64 census maximizers return 116; the CPU census's witness at T = 116 returns 116 and at T = 114 is censored (-1).
  C  state reset across widths: index 12345 at W = 64, then W = 66, then W = 64 again: the two W = 64 answers equal, and each equals list mode.
  D  scalar and literal fixtures through serve: the hand fixtures at W = 4 and 6 (p1_lane_engine.HAND_FIXTURE) and all 64 lanes at
     W = 12, each death equal to the scalar engine's.
  E  mutants, split as GPT noted: (i) through serve, a server built with MUTANT_DROP_EDGE answers the 64 W = 12 lanes with a death vector
     that DIFFERS from the scalar engine's (the mutant detected by deaths); (ii) the cell trace stays in its own `rows` mode: the mutant's
     ten-step trace of 32 edge starts at W = 20 differs from the scalar evolution (it cannot run through serve, which returns deaths only).
  F  refusals (an error response and a non-zero exit, each): fractional W; fractional T; Boolean T; a Boolean index; a numeric (not
     string) index; a missing id; a Boolean id; a leading-zero index "007"; an index >= 2^(W/2); W above the server's W_max; a malformed
     line; more than max_indices indices; a line longer than max_line_bytes (sent in pieces, refused while read); a truncated request
     (the stream closed before its newline).
  G  no trailing output after a good response; the response to a duplicated index list has the request's length.
Server configuration (frozen): 32-lane words, W_max 72, T_max 288, G_max 4,096 groups per batch, max_indices 131,072, max_line_bytes
4,194,304, GPU budget 2 GiB. Stage caps (the W1A supervisor): wall 300 s, CPU 300 s, group RSS 6 GiB, pressure, swap 256 MiB, disk
floor, artifacts 50 MiB; server start-up and Metal compilation are inside the stage and counted apart from the per-request deadline.

Usage: python3 s0_serve_controls.py stage OUT_DIR    (absolute, new or empty)
       python3 s0_serve_controls.py run OUT_DIR      (the step the stage runs)
OUTCOME: (to be filled after the run)
"""
import json, os, random, select, signal, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P

METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '4a6cda6031625dabce3c0ed051d4ef3fc88c2c03cfffbb4c94267bdbc64c97dd'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
CONFIG = {'lane_bits': 32, 'mode': 'serve', 'T': 0, 'W_max': 72, 'T_max': 288, 'G_max': 4096, 'max_indices': 131072, 'max_line_bytes': 4194304}
DEADLINE_S = 10.0
STAGE_S = 300


class Stop(Exception):
    pass


class Server:
    def __init__(self, eng, out, mutant=''):
        job = dict(CONFIG, metal=P.METAL, gpu_budget_bytes=P.GPU_BUDGET)
        if mutant: job['mutant'] = mutant
        self.jp = os.path.join(out, 'serve_job%s.json' % ('_' + mutant if mutant else '')); json.dump(job, open(self.jp, 'w'))
        t = time.monotonic()
        self.p = subprocess.Popen([eng.bin, self.jp, self.jp + '.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  start_new_session=True, bufsize=0)
        self.started = round(time.monotonic() - t, 3); self.buf = b''

    def kill(self):
        try:
            os.killpg(self.p.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            self.p.wait(timeout=5)
        except Exception:
            pass

    def _line(self, timeout):
        end = time.monotonic() + timeout
        while b'\n' not in self.buf:
            left = end - time.monotonic()
            if left <= 0:
                return None
            r, _, _ = select.select([self.p.stdout], [], [], left)
            if not r:
                return None
            chunk = os.read(self.p.stdout.fileno(), 1 << 16)
            if not chunk:
                return None
            self.buf += chunk
        line, self.buf = self.buf.split(b'\n', 1)
        return line

    def send_raw(self, data):
        self.p.stdin.write(data); self.p.stdin.flush()

    def ask(self, req):
        self.send_raw((json.dumps(req) + '\n').encode())
        line = self._line(DEADLINE_S)
        if line is None:
            self.kill(); raise Stop('no response within %s s to request %s' % (DEADLINE_S, req.get('id')))
        return json.loads(line)

    def no_trailing(self):
        return self._line(0.2) is None


def check_response(req, res):
    probs = []
    if set(res) != {'id', 'W', 'T', 'deaths'}: probs.append('keys %s' % sorted(res))
    if res.get('id') != req['id'] or res.get('W') != req['W'] or res.get('T') != req['T']: probs.append('echo')
    d = res.get('deaths', [])
    if len(d) != len(req['indices']): probs.append('count')
    if any(not isinstance(x, int) or isinstance(x, bool) or not (x == -1 or (0 <= x <= req['T'] and x % 2 == 0)) for x in d): probs.append('death domain')
    return probs


def run(out):
    t0 = time.monotonic()
    os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'harness_sha256': P.digest(P.__file__),
         'config': CONFIG, 'checks': {}, 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2)
        tmp = os.path.join(out, 's0_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 's0_result.json'))

    def check(name, ok, **detail):
        R['checks'][name] = {'pass': bool(ok), **detail}; save()
        if not ok:
            raise Stop('%s %s' % (name, json.dumps(detail)[:500]))

    check('pinned_metal', P.digest(P.METAL) == METAL_SHA256)
    check('pinned_swift', P.digest(P.SWIFT) == SWIFT_SHA256)
    eng = P.Engine(out); R['build'] = eng.build(); save()
    srv = Server(eng, out); R['server_start_s'] = srv.started
    rid = [0]

    def ask(W, T, idx, name):
        rid[0] += 1; req = {'id': rid[0], 'W': W, 'T': T, 'indices': [str(i) for i in idx]}
        t = time.monotonic(); res = srv.ask(req); dt = round(time.monotonic() - t, 3)
        probs = check_response(req, res)
        if probs:
            srv.kill(); check(name + '_response_contract', False, problems=probs)
        if not srv.no_trailing():
            srv.kill(); check(name + '_no_trailing', False)
        return res['deaths'], dt

    # A: equality with list mode
    timings = {}
    for W, T in ((64, 256), (72, 288)):
        rnd = random.Random(1000003 * W); idx = [rnd.randrange(1 << (W // 2)) for _ in range(100000)]
        d1, t1 = ask(W, T, idx[:65536], 'A_W%d_part1' % W); d2, t2 = ask(W, T, idx[65536:], 'A_W%d_part2' % W)
        lres = eng.run({'lane_bits': 32, 'mode': 'list', 'W': W, 'T': T, 'indices': [str(i) for i in idx]}, 'A_list_W%d' % W)
        lst = {int(x['index']): x['death'] for x in lres['deaths']}
        mism = sum(1 for i, d in zip(idx, d1 + d2) if lst[i] != d); timings['W%d' % W] = [t1, t2]
        check('A_serve_equals_list_W%d' % W, mism == 0, lanes=len(idx), mismatches=mism, request_s=[t1, t2])
    # B: maximizers and the horizon
    d, _ = ask(64, 256, list(range(2801313472, 2801313512)), 'B_max')
    check('B_W64_maximizers_116', d == [116] * 40)
    a, _ = ask(64, 116, [2801313511], 'B_at_T'); b, _ = ask(64, 114, [2801313511], 'B_before_T')
    check('B_death_at_T_and_censored_before', a == [116] and b == [-1], at_T=a, at_T_minus_2=b)
    # C: state reset across widths
    x1, _ = ask(64, 256, [12345], 'C1'); x2, _ = ask(66, 264, [12345], 'C2'); x3, _ = ask(64, 256, [12345], 'C3')
    l64 = eng.run({'lane_bits': 32, 'mode': 'list', 'W': 64, 'T': 256, 'indices': ['12345']}, 'C_list64')['deaths'][0]['death']
    l66 = eng.run({'lane_bits': 32, 'mode': 'list', 'W': 66, 'T': 264, 'indices': ['12345']}, 'C_list66')['deaths'][0]['death']
    check('C_state_reset_across_widths', x1 == x3 == [l64] and x2 == [l66], answers=[x1, x2, x3], list=[l64, l66])
    # D: scalar and literal fixtures
    for W, tab in P.HAND_FIXTURE.items():
        d, _ = ask(W, 4 * W, list(tab), 'D_hand_W%d' % W)
        check('D_hand_fixture_W%d' % W, d == [P.death(s, 4 * W) for s in tab.values()], deaths=d)
    d12, _ = ask(12, 48, list(range(64)), 'D_W12')
    sc12 = [P.death(P.recon(12, n), 48) for n in range(64)]
    check('D_all_W12_lanes_equal_scalar', d12 == sc12)
    # G: duplicates keep the request's length
    dd, _ = ask(64, 256, [7, 7, 7], 'G_dup')
    check('G_duplicates_preserved', len(dd) == 3 and dd[0] == dd[1] == dd[2])
    srv.kill(); R['server_exit_after_kill'] = srv.p.returncode
    # E(i): the mutant through serve, detected by its death vector
    ms = Server(eng, out, mutant='drop_edge'); rid[0] += 1
    req = {'id': rid[0], 'W': 12, 'T': 48, 'indices': [str(n) for n in range(64)]}
    res = ms.ask(req); ms.kill()
    check('E_i_serve_mutant_detected_by_deaths', not check_response(req, res) and res['deaths'] != sc12,
          lane_mismatches=sum(1 for a, b in zip(res['deaths'], sc12) if a != b))
    # E(ii): the cell trace in rows mode, as before
    W = 20; rnd = random.Random(97); starts = [(1 << (W - 1)) | rnd.getrandbits(W - 1) for _ in range(32)]
    tr = eng.run({'lane_bits': 32, 'mode': 'rows', 'T': 40, 'Wsup': W, 'starts': [hex(s) for s in starts], 'trace_steps': 10, 'mutant': 'drop_edge'}, 'E_ii_trace_mutant')
    mism = 0
    for t in range(11):
        rows = [int(h, 16) for h in tr['trace'][t]]
        for l, s in enumerate(starts):
            st = s
            for _ in range(t): st = P.pstep(st)
            for k in range(tr['L']):
                if ((rows[k] >> l) & 1) != (0 if k == 0 else (st >> (k - 1)) & 1): mism += 1
    check('E_ii_rows_trace_mutant_detected', mism > 0, cell_mismatches=mism)
    # F: refusals, one fresh server each
    big = '"' + '1' * 20 + '"'
    cases = [
        ('fractional_W', b'{"id": 1, "W": 64.5, "T": 256, "indices": ["1"]}\n'),
        ('fractional_T', b'{"id": 1, "W": 64, "T": 256.0, "indices": ["1"]}\n'),
        ('boolean_T', b'{"id": 1, "W": 64, "T": true, "indices": ["1"]}\n'),
        ('boolean_index', b'{"id": 1, "W": 64, "T": 256, "indices": [true]}\n'),
        ('numeric_index', b'{"id": 1, "W": 64, "T": 256, "indices": [5]}\n'),
        ('missing_id', b'{"W": 64, "T": 256, "indices": ["1"]}\n'),
        ('boolean_id', b'{"id": true, "W": 64, "T": 256, "indices": ["1"]}\n'),
        ('leading_zero_index', b'{"id": 1, "W": 64, "T": 256, "indices": ["007"]}\n'),
        ('index_beyond_class', b'{"id": 1, "W": 64, "T": 256, "indices": ["4294967296"]}\n'),
        ('W_above_W_max', b'{"id": 1, "W": 74, "T": 256, "indices": ["1"]}\n'),
        ('malformed', b'{"id": 1, "W": 64, "T"\n'),
        ('too_many_indices', ('{"id": 1, "W": 64, "T": 256, "indices": [' + ','.join(['"1"'] * (CONFIG['max_indices'] + 1)) + ']}\n').encode()),
    ]
    for name, payload in cases:
        s = Server(eng, out); s.send_raw(payload); line = s._line(DEADLINE_S)
        try:
            s.p.stdin.close()
        except Exception:
            pass
        try:
            rc = s.p.wait(timeout=DEADLINE_S)
        except subprocess.TimeoutExpired:
            s.kill(); rc = None
        res = json.loads(line) if line else {}
        check('F_refuses_' + name, 'error' in res and rc not in (0, None), response=res, exit=rc)
    # an over-long line, sent in pieces, refused while being read
    s = Server(eng, out); refused = False
    try:
        piece = b'{"id": 1, "W": 64, "T": 256, "indices": [' + b'"12345678901234567890",' * 40000
        for _ in range(12):
            s.send_raw(piece)
            r, _, _ = select.select([s.p.stdout], [], [], 0)
            if r: break
    except BrokenPipeError:
        pass
    line = s._line(DEADLINE_S)
    try:
        rc = s.p.wait(timeout=DEADLINE_S)
    except subprocess.TimeoutExpired:
        s.kill(); rc = None
    res = json.loads(line) if line else {}
    check('F_refuses_over_long_line_while_reading', 'error' in res and 'exceeds' in res.get('error', '') and rc not in (0, None), response=res, exit=rc)
    # a truncated request: the stream closed before the newline
    s = Server(eng, out); s.send_raw(b'{"id": 1, "W": 64, "T": 256, "indices": ["1"]}'); s.p.stdin.close()
    line = s._line(DEADLINE_S); rc = s.p.wait(timeout=DEADLINE_S); res = json.loads(line) if line else {}
    check('F_refuses_truncated_request', 'error' in res and 'truncated' in res.get('error', '') and rc not in (0, None), response=res, exit=rc)
    R['timings'] = timings; R['engine_calls'] = len(eng.log)
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


def stage(out):
    import w1a_harness as H
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['s0'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'metal_sha256': METAL_SHA256, 'swift_sha256': SWIFT_SHA256, 'w1a_sha256': W1A_SHA256,
                'config': CONFIG, 'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 50 << 20,
                'deadline_s': DEADLINE_S, 'gpu_budget_bytes': P.GPU_BUDGET}, 'nice_inherited': os.nice(0)}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 's0_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        if rc != 0 or not d.get('complete') or not all(v['pass'] for v in d['checks'].values()):
            return 'FAIL', 'rc %s complete %s' % (rc, d.get('complete'))
        return 'pass', 'S0 complete: %d checks pass' % len(d['checks'])
    rec = sup.run_step('s0_serve_controls', [sys.executable, os.path.abspath(__file__), 'run', rdir], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == 'run':
        try:
            R = run(a[1]); print('S0 COMPLETE', len(R['checks']), 'checks'); sys.exit(0)
        except (Stop, P.Stop, RuntimeError) as e:
            print('S0 STOPPED:', e); sys.exit(1)
    if len(a) == 2 and a[0] == 'stage':
        sys.exit(stage(a[1]))
    print(__doc__); sys.exit(2)
