#!/usr/bin/env python3
"""S0, revision 2 (Local, 2026-10-24, L877; revision 1 was L875's, declined by GPT's GC1786): the control stage for the P1 driver's
persistent `serve` mode (driver revision 6), the evaluator P2 will use. NOT an agreed job until GPT accepts this exact file and the
pinned driver; nothing runs on import.

Revision 2, GC1786's three integration defects and its freeze items:
  1. Ownership: the server is started WITHOUT a new session, so it stays in the W1A step's process group (inside the supervisor's group
     RSS/CPU guard and its final group kill). The client closes each server by SIGTERM, a 3 s wait, SIGKILL and wait on that child
     alone (no killpg after leaving the session), records whether death was verified, and every live server is closed in a run-wide
     `finally`, so a failed comparison or an exception cannot strand one. W1A's group cleanup remains the last stop.
  2. Transport: requests are written by a write-all loop on a non-blocking pipe against ONE deadline per request (10 s) covering the
     write and the response; a short write continues, a blocked reader times out; an EPIPE during a refusal is expected and the
     response is still read. The response buffer is bounded (16 MiB); the server's stderr goes to a file, never a pipe.
  3. Contract: a response must be a JSON object with exactly {id, W, T, deaths} (or exactly {id, error} for an expected refusal); id,
     W and T must be exact ints (type int, never bool or float) equal to the request's; deaths a list of exact ints, each -1 or even in
     [0, T]; the refusal's id must be the request's id when that id was valid, else null, and its error a string. After each good
     response the stream must be live and silent: any buffered byte (partial or whole line) or an end of stream fails.
  Freeze: the consumed P1 helper (p1_lane_engine.py) is pinned too; the stage's matcher requires EXACTLY the named control set, each a
  Boolean pass; failure details (including transport and JSON exceptions) are saved before cleanup.
  Client fault controls (no GPU; a protocol stub in Python plays the server): a sink that reads 7 bytes at a time (the write-all loop
  completes); a sink that never reads (the request times out at the deadline, it does not hang); a malformed response (detected); a
  response followed by partial trailing bytes (detected); a forced exception while a server is live (the server is closed and
  verified dead by the run-wide finally).

GPU controls (unchanged in scope from revision 1): A serve equals list mode on 100,000 seeded indices at W = 64 and at W = 72; B the 40 W = 64
maximizers return 116, death at T and censoring at T - 2; C state reset W64/W66/W64; D the hand fixtures and all 64 W = 12 lanes equal the
scalar engine; E(i) the drop-edge mutant detected by its death vector through serve, E(ii) by the cell trace in rows mode; F fourteen
refusals, each with the exact error schema, the appropriate id and a non-zero exit; G duplicates preserved and no trailing output.
Server configuration (frozen): 32-lane words, W_max 72, T_max 288, G_max 4,096, max_indices 131,072, max_line_bytes 4,194,304, GPU budget
2 GiB. Stage caps (W1A): wall 300 s, CPU 300 s, group RSS 6 GiB (now covering the server), pressure, swap 256 MiB, disk floor, artifacts 50 MiB.

Usage: python3 s0_serve_controls.py stage OUT_DIR | run OUT_DIR | --client-controls
OUTCOME: (to be filled after the run)
"""
import errno, json, os, random, select, signal, subprocess, sys, tempfile, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P

METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec'
P1_HELPER_SHA256 = 'ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
CONFIG = {'lane_bits': 32, 'mode': 'serve', 'T': 0, 'W_max': 72, 'T_max': 288, 'G_max': 4096, 'max_indices': 131072, 'max_line_bytes': 4194304}
DEADLINE_S = 10.0
MAX_RESPONSE = 16 << 20
STAGE_S = 300
LIVE = []          # every live server, closed by the run-wide finally


def close_all():
    """The run-wide cleanup: close every live server; returns the verified-dead flags."""
    return [x.close() for x in list(LIVE)]


class Stop(Exception):
    pass


class Server:
    """A child process speaking one JSON object per line; stays in the caller's process group."""

    def __init__(self, argv, errpath):
        self.err = open(errpath, 'ab')
        t = time.monotonic()
        self.p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.err, bufsize=0)
        os.set_blocking(self.p.stdin.fileno(), False); os.set_blocking(self.p.stdout.fileno(), False)
        self.started = round(time.monotonic() - t, 3); self.buf = b''; self.eof = False; self.closed = False; self.writes = 0; self.partial = 0
        LIVE.append(self)

    @classmethod
    def engine(cls, eng, out, mutant=''):
        job = dict(CONFIG, metal=P.METAL, gpu_budget_bytes=P.GPU_BUDGET)
        if mutant: job['mutant'] = mutant
        jp = os.path.join(out, 'serve_job%s.json' % ('_' + mutant if mutant else '')); json.dump(job, open(jp, 'w'))
        return cls([eng.bin, jp, jp + '.out'], os.path.join(out, 'serve_stderr.log'))

    def close(self):
        """SIGTERM, 3 s, SIGKILL, wait; returns True when the child is verified dead."""
        if self.closed: return self.p.poll() is not None
        self.closed = True
        try:
            if self.p.poll() is None:
                self.p.terminate()
                try: self.p.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    self.p.kill(); self.p.wait(timeout=5)
        except Exception:
            pass
        for f in (self.p.stdin, self.p.stdout):
            try: f.close()
            except Exception: pass
        try: self.err.close()
        except Exception: pass
        if self in LIVE: LIVE.remove(self)
        return self.p.poll() is not None

    def _pump(self, deadline, want_newline):
        """Read what is available until a newline is buffered (want_newline) or the deadline; bounded buffer; marks EOF."""
        while not (want_newline and b'\n' in self.buf):
            left = deadline - time.monotonic()
            if left <= 0: return
            r, _, _ = select.select([self.p.stdout], [], [], left)
            if not r: return
            try:
                chunk = os.read(self.p.stdout.fileno(), 1 << 16)
            except BlockingIOError:
                continue
            if not chunk:
                self.eof = True; return
            self.buf += chunk
            if len(self.buf) > MAX_RESPONSE:
                raise Stop('response buffer exceeds %d bytes' % MAX_RESPONSE)
            if not want_newline: return

    def send(self, data, deadline):
        """Write all of data before the deadline; returns 'ok', 'timeout' or 'epipe' (the server closed its input)."""
        view = memoryview(data); off = 0
        while off < len(view):
            left = deadline - time.monotonic()
            if left <= 0: return 'timeout'
            _, w, _ = select.select([], [self.p.stdin], [], left)
            if not w: return 'timeout'
            try:
                chunk = view[off:off + (1 << 16)]; n = os.write(self.p.stdin.fileno(), chunk); off += n
                self.writes += 1; self.partial += n < len(chunk)
            except BlockingIOError:
                continue
            except (BrokenPipeError, OSError) as e:
                if isinstance(e, BrokenPipeError) or getattr(e, 'errno', None) == errno.EPIPE: return 'epipe'
                raise
        return 'ok'

    def line(self, deadline):
        self._pump(deadline, True)
        if b'\n' not in self.buf:
            return None
        ln, self.buf = self.buf.split(b'\n', 1)
        return ln

    def exchange(self, payload):
        """One request with one deadline over the write and the response. Returns (send status, parsed object or None, raw line)."""
        deadline = time.monotonic() + DEADLINE_S
        st = self.send(payload, deadline)
        ln = self.line(deadline)
        if ln is None:
            return st, None, None
        try:
            return st, json.loads(ln), ln
        except Exception:
            return st, 'MALFORMED', ln

    def quiet(self):
        """'silence' (live, nothing buffered or arriving), 'trailing' (any byte) or 'eof'."""
        if self.buf: return 'trailing'
        self._pump(time.monotonic() + 0.2, False)
        if self.buf: return 'trailing'
        return 'eof' if self.eof else 'silence'


def is_int(x):
    return type(x) is int


def check_response(req, res):
    if not isinstance(res, dict): return ['not an object']
    probs = []
    if set(res) != {'id', 'W', 'T', 'deaths'}: probs.append('keys %s' % sorted(res))
    for k in ('id', 'W', 'T'):
        if not is_int(res.get(k)) or res.get(k) != req[k]: probs.append('echo %s' % k)
    d = res.get('deaths')
    if type(d) is not list: probs.append('deaths not a list'); return probs
    if len(d) != len(req['indices']): probs.append('count')
    if any(not is_int(x) or not (x == -1 or (0 <= x <= req['T'] and x % 2 == 0)) for x in d): probs.append('death domain')
    return probs


def check_error(res, expected_id):
    if not isinstance(res, dict): return ['not an object']
    probs = []
    if set(res) != {'id', 'error'}: probs.append('keys %s' % sorted(res))
    if type(res.get('error')) is not str: probs.append('error not a string')
    if expected_id is None:
        if res.get('id', 'missing') is not None: probs.append('id should be null')
    elif not is_int(res.get('id')) or res.get('id') != expected_id: probs.append('id echo')
    return probs


STUBS = {
    'slow_sink': "import os,sys,time\nbuf=b''\nwhile b'\\n' not in buf:\n    c=os.read(0,7)\n    if not c: break\n    buf+=c\nsys.stdout.write('{\"id\": 1, \"W\": 12, \"T\": 48, \"deaths\": [12]}\\n'); sys.stdout.flush(); time.sleep(5)\n",
    'never_reads': "import time\ntime.sleep(60)\n",
    'malformed': "import os,sys,time\nos.read(0,1<<20)\nsys.stdout.write('{not json\\n'); sys.stdout.flush(); time.sleep(5)\n",
    'trailing': "import os,sys,time\nos.read(0,1<<20)\nsys.stdout.write('{\"id\": 1, \"W\": 12, \"T\": 48, \"deaths\": [12]}\\n{\"id\"'); sys.stdout.flush(); time.sleep(5)\n",
    'bool_echo': "import os,sys,time\nos.read(0,1<<20)\nsys.stdout.write('{\"id\": true, \"W\": 12.0, \"T\": 48, \"deaths\": [12]}\\n'); sys.stdout.flush(); time.sleep(5)\n",
}


def client_controls(tmp):
    """Transport and contract faults against protocol stubs; no GPU. Returns {name: bool}."""
    res = {}
    def stub(name):
        p = os.path.join(tmp, name + '.py'); open(p, 'w').write(STUBS[name]); return Server([sys.executable, p], os.path.join(tmp, name + '.err'))
    req = {'id': 1, 'W': 12, 'T': 48, 'indices': [str(i) for i in range(30000)]}           # about 260 KB, beyond any pipe buffer: the sink reads 7 bytes at a time
    pay = (json.dumps(req) + '\n').encode()
    s = stub('slow_sink'); st, r, _ = s.exchange(pay)
    one = {'id': 1, 'W': 12, 'T': 48, 'indices': ['5']}
    res['short_writes_complete'] = st == 'ok' and isinstance(r, dict) and r.get('id') == 1 and s.writes > 1 and s.partial > 0
    res['_short_write_counts'] = [len(pay), s.writes, s.partial]; res['slow_sink_closed_dead'] = s.close()
    s = stub('never_reads'); t = time.monotonic(); big = (json.dumps({'id': 1, 'W': 12, 'T': 48, 'indices': ['1'] * 200000}) + '\n').encode()
    st, r, _ = s.exchange(big); dt = time.monotonic() - t
    res['blocked_reader_times_out_at_deadline'] = st == 'timeout' and r is None and DEADLINE_S - 0.5 <= dt <= DEADLINE_S + 2; res['never_reads_closed_dead'] = s.close()
    s = stub('malformed'); st, r, _ = s.exchange((json.dumps(one) + '\n').encode())
    res['malformed_response_detected'] = r == 'MALFORMED'; s.close()
    s = stub('trailing'); st, r, _ = s.exchange((json.dumps(one) + '\n').encode())
    res['trailing_partial_bytes_detected'] = not check_response(one, r) and s.quiet() == 'trailing'; s.close()
    s = stub('bool_echo'); st, r, _ = s.exchange((json.dumps(one) + '\n').encode())
    res['bool_and_float_echoes_rejected'] = bool(check_response(one, r)); s.close()
    # a forced exception while a server is live: the run-wide finally must close it
    s = stub('never_reads'); pid = s.p.pid
    try:
        try:
            raise RuntimeError('forced failure while a server is live')
        finally:
            close_all()                                          # the same function run()'s finally calls
    except RuntimeError:
        pass
    try:
        os.kill(pid, 0); alive = s.p.poll() is None
    except ProcessLookupError:
        alive = False
    res['forced_failure_closes_live_server'] = not alive and not LIVE
    res['early_eof_is_not_silence'] = check_eof_distinction(tmp)
    return res


def check_eof_distinction(tmp):
    p = os.path.join(tmp, 'eof.py'); open(p, 'w').write("import os,sys\nos.read(0,1<<20)\nsys.stdout.write('{\"id\": 1, \"W\": 12, \"T\": 48, \"deaths\": [12]}\\n'); sys.stdout.flush()\n")
    s = Server([sys.executable, p], os.path.join(tmp, 'eof.err')); one = {'id': 1, 'W': 12, 'T': 48, 'indices': ['5']}
    st, r, _ = s.exchange((json.dumps(one) + '\n').encode()); time.sleep(0.3); q = s.quiet(); s.close()
    return q == 'eof'


REQUIRED = None   # filled below: the exact control names the matcher requires


def run(out):
    t0 = time.monotonic()
    os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'config': CONFIG, 'checks': {}, 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2)
        tmp = os.path.join(out, 's0_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 's0_result.json'))

    def check(name, ok, **detail):
        R['checks'][name] = {'pass': bool(ok), **detail}; save()
        if not ok:
            raise Stop('%s %s' % (name, json.dumps(detail)[:500]))

    try:
        check('pinned_metal', P.digest(P.METAL) == METAL_SHA256)
        check('pinned_swift', P.digest(P.SWIFT) == SWIFT_SHA256)
        check('pinned_p1_helper', P.digest(P.__file__) == P1_HELPER_SHA256)
        with tempfile.TemporaryDirectory() as tmp:
            for k, v in client_controls(tmp).items():
                if k.startswith('_'): R.setdefault('client_detail', {})[k] = v; save(); continue    # details, not checks
                check('client_' + k, v)
        eng = P.Engine(out); R['build'] = eng.build(); save()
        srv = Server.engine(eng, out); R['server_start_s'] = srv.started
        rid = [0]

        def ask(W, T, idx, name):
            rid[0] += 1; req = {'id': rid[0], 'W': W, 'T': T, 'indices': [str(i) for i in idx]}
            t = time.monotonic(); st, res, raw = srv.exchange((json.dumps(req) + '\n').encode()); dt = round(time.monotonic() - t, 3)
            if st != 'ok' or res is None or res == 'MALFORMED':
                check(name + '_transport', False, send=st, raw=(raw or b'')[:200].decode(errors='replace'))
            probs = check_response(req, res)
            if probs: check(name + '_response_contract', False, problems=probs)
            q = srv.quiet()
            if q != 'silence': check(name + '_stream_live_and_silent', False, state=q)
            return res['deaths'], dt

        timings = {}
        for W, T in ((64, 256), (72, 288)):
            rnd = random.Random(1000003 * W); idx = [rnd.randrange(1 << (W // 2)) for _ in range(100000)]
            d1, t1 = ask(W, T, idx[:65536], 'A_W%d_part1' % W); d2, t2 = ask(W, T, idx[65536:], 'A_W%d_part2' % W)
            lres = eng.run({'lane_bits': 32, 'mode': 'list', 'W': W, 'T': T, 'indices': [str(i) for i in idx]}, 'A_list_W%d' % W)
            lst = {int(x['index']): x['death'] for x in lres['deaths']}
            mism = sum(1 for i, d in zip(idx, d1 + d2) if lst[i] != d); timings['W%d' % W] = [t1, t2]
            check('A_serve_equals_list_W%d' % W, mism == 0, lanes=len(idx), mismatches=mism, request_s=[t1, t2])
        d, _ = ask(64, 256, list(range(2801313472, 2801313512)), 'B_max')
        check('B_W64_maximizers_116', d == [116] * 40)
        a, _ = ask(64, 116, [2801313511], 'B_at_T'); b, _ = ask(64, 114, [2801313511], 'B_before_T')
        check('B_death_at_T_and_censored_before', a == [116] and b == [-1], at_T=a, at_T_minus_2=b)
        x1, _ = ask(64, 256, [12345], 'C1'); x2, _ = ask(66, 264, [12345], 'C2'); x3, _ = ask(64, 256, [12345], 'C3')
        l64 = eng.run({'lane_bits': 32, 'mode': 'list', 'W': 64, 'T': 256, 'indices': ['12345']}, 'C_list64')['deaths'][0]['death']
        l66 = eng.run({'lane_bits': 32, 'mode': 'list', 'W': 66, 'T': 264, 'indices': ['12345']}, 'C_list66')['deaths'][0]['death']
        check('C_state_reset_across_widths', x1 == x3 == [l64] and x2 == [l66], answers=[x1, x2, x3], list=[l64, l66])
        for W, tab in P.HAND_FIXTURE.items():
            d, _ = ask(W, 4 * W, list(tab), 'D_hand_W%d' % W)
            check('D_hand_fixture_W%d' % W, d == [P.death(s, 4 * W) for s in tab.values()], deaths=d)
        d12, _ = ask(12, 48, list(range(64)), 'D_W12'); sc12 = [P.death(P.recon(12, n), 48) for n in range(64)]
        check('D_all_W12_lanes_equal_scalar', d12 == sc12)
        dd, _ = ask(64, 256, [7, 7, 7], 'G_dup')
        check('G_duplicates_preserved', len(dd) == 3 and dd[0] == dd[1] == dd[2])
        check('server_closed_verified_dead', srv.close())
        ms = Server.engine(eng, out, mutant='drop_edge'); rid[0] += 1
        req = {'id': rid[0], 'W': 12, 'T': 48, 'indices': [str(n) for n in range(64)]}
        st, res, _ = ms.exchange((json.dumps(req) + '\n').encode()); dead = ms.close()
        check('E_i_serve_mutant_detected_by_deaths', st == 'ok' and not check_response(req, res) and res['deaths'] != sc12 and dead,
              lane_mismatches=sum(1 for a, b in zip(res['deaths'], sc12) if a != b) if isinstance(res, dict) else None)
        W = 20; rnd = random.Random(97); starts = [(1 << (W - 1)) | rnd.getrandbits(W - 1) for _ in range(32)]
        tr = eng.run({'lane_bits': 32, 'mode': 'rows', 'T': 40, 'Wsup': W, 'starts': [hex(s) for s in starts], 'trace_steps': 10, 'mutant': 'drop_edge'}, 'E_ii_trace_mutant')
        mism = 0
        for t in range(11):
            rows = [int(h, 16) for h in tr['trace'][t]]
            for l, s in enumerate(starts):
                stt = s
                for _ in range(t): stt = P.pstep(stt)
                for k in range(tr['L']):
                    if ((rows[k] >> l) & 1) != (0 if k == 0 else (stt >> (k - 1)) & 1): mism += 1
        check('E_ii_rows_trace_mutant_detected', mism > 0, cell_mismatches=mism)
        cases = [  # (name, payload, expected id in the error: the request's valid id, or None)
            ('fractional_W', b'{"id": 1, "W": 64.5, "T": 256, "indices": ["1"]}\n', 1),
            ('fractional_T', b'{"id": 1, "W": 64, "T": 256.0, "indices": ["1"]}\n', 1),
            ('boolean_T', b'{"id": 1, "W": 64, "T": true, "indices": ["1"]}\n', 1),
            ('boolean_index', b'{"id": 1, "W": 64, "T": 256, "indices": [true]}\n', 1),
            ('numeric_index', b'{"id": 1, "W": 64, "T": 256, "indices": [5]}\n', 1),
            ('missing_id', b'{"W": 64, "T": 256, "indices": ["1"]}\n', None),
            ('boolean_id', b'{"id": true, "W": 64, "T": 256, "indices": ["1"]}\n', None),
            ('leading_zero_index', b'{"id": 1, "W": 64, "T": 256, "indices": ["007"]}\n', 1),
            ('index_beyond_class', b'{"id": 1, "W": 64, "T": 256, "indices": ["4294967296"]}\n', 1),
            ('W_above_W_max', b'{"id": 1, "W": 74, "T": 256, "indices": ["1"]}\n', 1),
            ('malformed', b'{"id": 1, "W": 64, "T"\n', None),
            ('too_many_indices', ('{"id": 1, "W": 64, "T": 256, "indices": [' + ','.join(['"1"'] * (CONFIG['max_indices'] + 1)) + ']}\n').encode(), 1),
            ('over_long_line', b'{"id": 1, "W": 64, "T": 256, "indices": [' + b'"12345678901234567890",' * 200000 + b'"1"]}\n', None),
        ]
        for name, payload, eid in cases:
            s = Server.engine(eng, out); st, res, raw = s.exchange(payload)
            try: rc = s.p.wait(timeout=DEADLINE_S)
            except subprocess.TimeoutExpired: rc = None
            dead = s.close()
            probs = check_error(res, eid) if isinstance(res, dict) else ['no parsable error response']
            check('F_refuses_' + name, not probs and rc not in (0, None) and dead, send=st, response=res if isinstance(res, dict) else str(raw)[:120], exit=rc, problems=probs)
        s = Server.engine(eng, out); st = s.send(b'{"id": 1, "W": 64, "T": 256, "indices": ["1"]}', time.monotonic() + DEADLINE_S)
        s.p.stdin.close(); ln = s.line(time.monotonic() + DEADLINE_S)
        try: rc = s.p.wait(timeout=DEADLINE_S)
        except subprocess.TimeoutExpired: rc = None
        dead = s.close(); res = json.loads(ln) if ln else None
        probs = check_error(res, None) if isinstance(res, dict) else ['no parsable error response']
        check('F_refuses_truncated_request', not probs and 'truncated' in res.get('error', '') and rc not in (0, None) and dead, response=res, exit=rc)
        R['timings'] = timings; R['engine_calls'] = len(eng.log)
        R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
        return R
    except BaseException as e:
        R['failure'] = {'type': type(e).__name__, 'message': str(e)[:1000], 'traceback': traceback.format_exc()[-3000:]}; save()
        raise
    finally:
        R['live_servers_at_finally'] = len(LIVE)
        R['live_servers_closed_dead'] = close_all()
        save()


REQUIRED = (['pinned_metal', 'pinned_swift', 'pinned_p1_helper']
            + ['client_' + k for k in ('short_writes_complete', 'slow_sink_closed_dead', 'blocked_reader_times_out_at_deadline', 'never_reads_closed_dead',
                                       'malformed_response_detected', 'trailing_partial_bytes_detected', 'bool_and_float_echoes_rejected',
                                       'forced_failure_closes_live_server', 'early_eof_is_not_silence')]
            + ['A_serve_equals_list_W64', 'A_serve_equals_list_W72', 'B_W64_maximizers_116', 'B_death_at_T_and_censored_before', 'C_state_reset_across_widths',
               'D_hand_fixture_W4', 'D_hand_fixture_W6', 'D_all_W12_lanes_equal_scalar', 'G_duplicates_preserved', 'server_closed_verified_dead',
               'E_i_serve_mutant_detected_by_deaths', 'E_ii_rows_trace_mutant_detected']
            + ['F_refuses_' + k for k in ('fractional_W', 'fractional_T', 'boolean_T', 'boolean_index', 'numeric_index', 'missing_id', 'boolean_id',
                                          'leading_zero_index', 'index_beyond_class', 'W_above_W_max', 'malformed', 'too_many_indices', 'over_long_line',
                                          'truncated_request')])


def stage(out):
    import w1a_harness as H
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['s0'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'metal_sha256': METAL_SHA256, 'swift_sha256': SWIFT_SHA256, 'p1_helper_sha256': P1_HELPER_SHA256,
                'w1a_sha256': W1A_SHA256, 'config': CONFIG, 'required_checks': REQUIRED, 'nice_inherited': os.nice(0),
                'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 50 << 20,
                         'deadline_s': DEADLINE_S, 'gpu_budget_bytes': P.GPU_BUDGET, 'max_response_bytes': MAX_RESPONSE}}
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
        ch = d.get('checks', {})
        exact = sorted(ch) == sorted(REQUIRED) and all(type(ch[k].get('pass')) is bool and ch[k]['pass'] for k in REQUIRED)
        if rc != 0 or not d.get('complete') or not exact or d.get('live_servers_at_finally') != 0:
            return 'FAIL', 'rc %s complete %s exact-set %s live %s' % (rc, d.get('complete'), exact, d.get('live_servers_at_finally'))
        return 'pass', 'S0 complete: exactly the %d required checks pass' % len(REQUIRED)
    rec = sup.run_step('s0_serve_controls', [sys.executable, os.path.abspath(__file__), 'run', rdir], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--client-controls']:
        with tempfile.TemporaryDirectory() as t:
            r = client_controls(t)
        c = {k: v for k, v in r.items() if not k.startswith('_')}
        print(json.dumps(r, indent=1)); print('CLIENT CONTROLS', 'PASS' if all(c.values()) else 'FAIL', len(c)); sys.exit(0 if all(c.values()) else 1)
    if len(a) == 2 and a[0] == 'run':
        try:
            R = run(a[1]); print('S0 COMPLETE', len(R['checks']), 'checks'); sys.exit(0)
        except (Stop, P.Stop, RuntimeError) as e:
            print('S0 STOPPED:', e); sys.exit(1)
    if len(a) == 2 and a[0] == 'stage':
        sys.exit(stage(a[1]))
    print(__doc__); sys.exit(2)
