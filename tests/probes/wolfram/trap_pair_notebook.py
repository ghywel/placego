#!/usr/bin/env python3
"""trap-pair notebook, revision 3 (Local, 2026-10-24, L928; GPT's GC1837: one owned-step supervision and cleanup path in the main
thread. The kernel watcher never signals another process: on a monitor error or a sample above two kernels it asks the MAIN thread to
stop, once, by SIGUSR1 to this process; the main-thread hook raises KernelLimit only while the main thread holds the watch open, so W1A's
run_step kills its own step group and the stage stops UNKNOWN; a request after the watch closed is only counted. A watcher still alive
after shutdown, or any recorded event, also stops the stage UNKNOWN before the next phase; cleanup of owned groups and the final kernel
inventory with any uncertainty are recorded in the main thread on every exit, including failures and interrupts). Revision 2
(L927; GPT's GC1835: unknown untracked kit paths refused; the installed pipeline
scripts rehashed at the terminal gate; the two-kernel limit made concrete by a Wolfram process inventory with a quiet baseline, a
one-second watcher that stops only this stage's own process groups above two kernels, and a post-step check that every new kernel is
gone (a remaining kernel whose ownership is uncertain is never signalled and stops the stage); the read matcher binds a positive
integer count and the written cell files; recovery locations retained). Revision 1 (L926): the pipeline's notebook build and full-cell read for the submission
trap-pair, under the unchanged W1A supervisor (pinned bytes), after the kit's Check passed (L925). NOT an agreed job until GPT accepts
this exact file; nothing runs on import; `--controls` runs the matcher and binding controls only. No submission, no retry. The full-cell
gate is a separate script, written from these cells (as for edge-sep) and reviewed before any submission request.

Envelope: stage wall 1,500 s; step 1 `wolframscript -file build_sub.wl trap-pair OUT/essay.nb` at most 900 s wall and 900 s child CPU
(edge-sep's build took 111.8 s); step 2 `wolframscript -file read_nb_full.wl trap-pair OUT/cells` at most 300 s and 300 s; sampled group
RSS stop 6 GiB (strictly below half of 16 GiB; LeanLink builds the module against the kit, whose imports put the Check's group near 4 GiB,
L925); new artifacts 64 MiB (the kit's build trees and OUT); the notebook at most 8 MiB; log 10 MiB; W1A's pressure, 256 MiB swap-growth
and 5 GiB disk stops; at most two Wolfram kernels in total (the licence); ordinary priority; one failed step stops the stage.
Bindings: W1A's bytes; the essay (ESSAY_SHA256, the committed essay.md after GC1832), the module (MODULE_SHA256, Check PASS), and the two
committed pipeline scripts (build_sub.wl revision 4, read_nb_full.wl) by sha256 before they are staged and after; the kit copy's commit,
toolchain and pinned sources (W1A PIN) and its `git status` (only the known tracked change and untracked submission copies), recorded
before and required unchanged after the stage. Staging: PIPE/trap-pair must not exist; it receives essay.md and Rule30Submission.lean; the
pipeline folder's existing build_sub.wl and read_nb_full.wl (if any) are preserved in OUT before the committed versions are installed. The
notebook is written inside OUT (covered by artifact sampling), checked fresh and within 8 MiB, then copied to PIPE/trap-pair/essay.nb for
the submit script and read from there; the copy's digest is verified.
Kernel scope: a Wolfram kernel is a process whose executable lies in the Wolfram Engine bundle and is named WolframKernel or wolfram (the
form `ps` shows for wolframscript's kernel and for a LeanLink or MCP kernel). The baseline must hold at most one kernel (so the stage's own
kernel keeps the total within two). During each step a watcher samples the inventory every second; on a monitor error or a sample above
two kernels it requests a stop of the running step through the main-thread hook (above). After the step the MAIN thread closes the watch
(from then on a request is only counted), stops the watcher, verifies it has ended (join, then is_alive), and stops the stage UNKNOWN on
a monitor error, a sample above two kernels, or a watcher still alive. Cleanup is in the main thread only: W1A's own group termination at each step's end;
after each step, new kernels in this process's own groups (its session-leading children; W1A spawns each step in its own session) are
killed and every kernel outside the baseline must be gone, else UNKNOWN; on every exit (pass, stop, exception, SIGTERM) the finally path
kills only remaining owned groups, then records the final kernel inventory, the owned groups and any uncertain kernel, never signalling
an unowned or uncertain process. A process-group scan proves cleanup of that group only.
read_nb_full.wl's printed digests are Wolfram string hashes, not file-byte digests; the later gate uses byte digests.
Persistence and recovery: the staged folder and the installed pipeline scripts stay in place by design (disclosed); the receipt records the
preserved copies and the staged folder as recovery locations on every exit; no automatic retry.
Controls (`--controls`): the build matcher on RESULT OK (pass) and on RESULT FAIL, a missing result line and a nonzero exit (FAIL); the
read matcher on a positive count with its files (pass) and on no count, a negative or non-numeric count and a missing cell file (FAIL);
the four digest gates against one-byte changes; the kit admission on the clean status (pass), an unknown untracked path and an altered
tracked file (FAIL); the terminal script check on clean copies (pass) and on either script changed (FAIL); the kernel inventory logic on
a baseline of one plus one owned (pass), three kernels (stop), and a new kernel left outside the owned groups after a step (uncertain,
stop).
Usage: python3 trap_pair_notebook.py PIPELINE_DIR REPO_DIR OUT_DIR   |   python3 trap_pair_notebook.py --controls
"""
import json, os, shutil, signal, subprocess, sys, threading, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

STAGE_S, BUILD_WALL_S, BUILD_CPU_S, READ_WALL_S, READ_CPU_S = 1500, 900, 900, 300, 300
RSS_STOP_BYTES, ARTIFACTS_MAX_BYTES, LOG_MAX_BYTES, NOTEBOOK_MAX_BYTES = 6 << 30, 64 << 20, 10 << 20, 8 << 20
NAME = 'trap-pair'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
ESSAY_SHA256 = 'e1facac0647c0d2ece7d83c9011e83e3960545ad7865b12b7512b7faea004d16'
MODULE_SHA256 = '27f799f47eecf22f138967ac27ccbc14ab0dffb20f55f5dc29be800aa6b44fd6'
SCRIPTS = {'build_sub.wl': '1771b518d6071fd1537e5857c1a9afde21b449e22d088a7edf608bcd63dac02a',
           'read_nb_full.wl': 'c5b89fb60f57bccee440983eeaaf65edeb37d434cca47025783bf25bd6787f44'}
KNOWN_SUBMISSION_ARTIFACTS = {'Rule30Submission.lean', 'Rule30Submission.template.lean', 'Rule30Submission.prev.lean.bak', 'channel-12.lean', 'corollary-f.lean', 'diagonals.lean', 'README.md', 'build_all.sh', 'comparator',
                              'rule-210-two-sided.lean', 'rule-210.lean', 'sturmian-all.lean', 'sturmian.lean', 'theorem-a4.lean', 'white-end.lean', 'words-A.lean', 'words-B.lean'}
KERNEL_LIMIT = 2
KERNEL_NAMES = ('WolframKernel', 'wolfram')


def kernel_inventory():
    """[(pid, ppid, pgid, path)] of every Wolfram kernel process (time-bounded ps through W1A's checked runner)."""
    out = []
    for line in H.checked(['ps', '-axo', 'pid=,ppid=,pgid=,comm=']).splitlines():
        parts = line.split(None, 3)
        if len(parts) < 4: continue
        pid, ppid, pgid, path = int(parts[0]), int(parts[1]), int(parts[2]), parts[3].strip()
        if 'Wolfram' in path and os.path.basename(path) in KERNEL_NAMES: out.append((pid, ppid, pgid, path))
    return out


def owned_groups(me):
    """The process groups this stage owns: its session-leading children (W1A starts each step with start_new_session)."""
    groups = set()
    for line in H.checked(['ps', '-axo', 'pid=,ppid=,pgid=']).splitlines():
        parts = line.split()
        if len(parts) == 3 and int(parts[1]) == me and int(parts[0]) == int(parts[2]): groups.add(int(parts[2]))
    return groups


def kernel_verdict(inv, baseline_pids, groups, limit=KERNEL_LIMIT):
    """'ok', 'over' (more than limit kernels) or the classification of kernels outside the baseline: owned (in an owned group) or
    uncertain (not in the baseline and not owned)."""
    if len(inv) > limit: return 'over', [k[0] for k in inv]
    new = [k for k in inv if k[0] not in baseline_pids]
    unc = [k[0] for k in new if k[2] not in groups]
    return ('uncertain' if unc else 'ok'), unc


def admission(state):
    """The kit admission: the pinned commit, toolchain and sources, the only tracked change the root Rule30Submission.lean, and every
    untracked path a known submission copy. Returns the list of reasons (empty = admitted)."""
    why = []
    if state['commit'] != H.PIN['commit']: why.append('commit')
    if state['toolchain'] != H.PIN['toolchain']: why.append('toolchain')
    why += ['source %s' % f for f, w in H.PIN['sources'].items() if state['sources'].get(f) != w]
    why += ['tracked %s' % l for l in state['status'] if not l.startswith('??') and l[3:].strip() != 'Rule30Submission.lean']
    why += ['untracked %s' % l[3:].strip() for l in state['status'] if l.startswith('??') and l[3:].strip().rstrip('/') not in KNOWN_SUBMISSION_ARTIFACTS]
    return why


def scripts_check(pipe):
    """Expected and actual digests of the installed pipeline scripts."""
    return {k: {'expected': v, 'actual': (H.digest(os.path.join(pipe, k)) if os.path.exists(os.path.join(pipe, k)) else None)} for k, v in SCRIPTS.items()}


def build_matcher(rc, text):
    try:
        if rc != 0: return 'FAIL', 'build exit %d' % rc
        if 'RESULT FAIL' in text: return 'FAIL', 'RESULT FAIL in the build output'
        if not any(l.strip() == 'RESULT OK' for l in text.splitlines()): return 'FAIL', 'no RESULT OK line'
        return 'pass', 'RESULT OK'
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


def read_count(text):
    """The positive integer count from 'output cells: N  written to ...', or None."""
    for l in reversed(text.splitlines()):
        if l.startswith('output cells: '):
            tok = l[len('output cells: '):].split()
            return int(tok[0]) if tok and tok[0].isdigit() and int(tok[0]) > 0 else None
    return None


def cells_complete(cdir, n):
    """count.txt holds n, and cell-01..cell-n exist."""
    try:
        return (open(os.path.join(cdir, 'count.txt')).read().strip() == str(n)
                and all(os.path.exists(os.path.join(cdir, 'cell-%02d.txt' % i)) for i in range(1, n + 1)))
    except OSError:
        return False


def read_matcher(rc, text):
    try:
        if rc != 0: return 'FAIL', 'read exit %d' % rc
        n = read_count(text)
        if n is None: return 'FAIL', 'no positive integer cell count'
        return 'pass', 'output cells: %d' % n
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


def kit_state(kit):
    st = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True, timeout=H.CAPS['monitor_timeout_s'])
    if st.returncode != 0: raise H.MonitorError('git status exit %d' % st.returncode)
    return {'commit': H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip(), 'status': sorted(l for l in st.stdout.splitlines() if l.strip()),
            'sources': {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}, 'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip()}


class KernelLimit(BaseException):
    """Raised in the main thread by the watch hook; W1A's run_step then kills its own step group and re-raises."""


WATCH = {'active': False, 'fired': False, 'late': 0}


def on_watch_signal(signum, frame):
    """The main-thread hook (SIGUSR1): interrupt the running step once, and only while the main thread holds a watch open."""
    if WATCH['active'] and not WATCH['fired']:
        WATCH['fired'] = True; raise KernelLimit('the kernel watch requested a stop')
    WATCH['late'] += 1


def own_stop_request():
    os.kill(os.getpid(), signal.SIGUSR1)


class KernelWatch:
    """Samples inv_fn every `period` seconds during a step and records the largest count, every sample above the limit and every
    monitor error; on the first such event it calls `notify` once (by default SIGUSR1 to this process: the main-thread hook). It never
    signals another process. The main thread closes the watch, stops the thread and checks that it has ended (decide_watch)."""
    def __init__(self, inv_fn=None, period=1.0, join_s=20.0, notify=None, sink=None, key=None):
        self.inv_fn = inv_fn or kernel_inventory; self.period = period; self.join_s = join_s
        self.notify = notify or own_stop_request; self.sink = sink; self.key = key
        self.stop_evt = threading.Event(); self.over = []; self.errors = []; self.max_seen = 0; self.alive_after = None; self.requested = False
    def run(self):
        while not self.stop_evt.wait(self.period):
            try:
                inv = self.inv_fn(); self.max_seen = max(self.max_seen, len(inv))
                if len(inv) > KERNEL_LIMIT: self.over.append({'time': time.strftime('%H:%M:%S'), 'kernels': [k[0] for k in inv]})
            except Exception as e:
                self.errors.append({'time': time.strftime('%H:%M:%S'), 'monitor_error': repr(e)})
            if (self.over or self.errors) and not self.requested and not self.stop_evt.is_set():
                self.requested = True; self.notify()
    def __enter__(self):
        if self.notify is own_stop_request and signal.getsignal(signal.SIGUSR1) is not on_watch_signal:
            raise RuntimeError('the main-thread watch hook is not installed')
        WATCH['fired'] = False; WATCH['active'] = True
        self.t = threading.Thread(target=self.run, daemon=True); self.t.start(); return self
    def __exit__(self, *a):
        WATCH['active'] = False                     # main thread: from here a stop request is only counted
        self.stop_evt.set(); self.t.join(self.join_s); self.alive_after = self.t.is_alive()
        if self.sink is not None: self.sink[self.key] = self.record()
        return False
    def record(self):
        return {'max_kernels_seen': self.max_seen, 'over_limit': self.over, 'monitor_errors': self.errors, 'stop_requested': self.requested,
                'alive_after_join': self.alive_after}


def decide_watch(kw):
    """The main thread's verdict on a finished watch: None if clean, else the UNKNOWN reason."""
    if kw.alive_after is not False: return 'UNKNOWN: the kernel watcher did not stop'
    if kw.errors: return 'UNKNOWN: kernel monitoring failed during the step'
    if kw.over: return 'UNKNOWN: more than two Wolfram kernels during the step'
    return None


def final_kernel_record(baseline_pids, me, kill=True):
    """On every exit: kill only this process's own remaining groups, then record the inventory and any uncertain kernel."""
    rec = {}
    try:
        gs = owned_groups(me); rec['owned_groups_at_exit'] = sorted(gs)
        if kill:
            for g in gs:
                try: os.killpg(g, signal.SIGKILL)
                except ProcessLookupError: pass
    except Exception as e:
        rec['owned_groups_error'] = repr(e)
    try:
        inv = kernel_inventory(); rec['inventory'] = inv
        bp = set(baseline_pids) if baseline_pids is not None else None
        rec['uncertain'] = [k[0] for k in inv if bp is None or k[0] not in bp]
    except Exception as e:
        rec['inventory_error'] = repr(e); rec['uncertain'] = 'unknown: inventory failed'
    return rec


def controls():
    import tempfile
    res = {}
    repo = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..'))
    res['build_ok_passes'] = build_matcher(0, 'notebook path: x\nbuild seconds: 100\nRESULT OK\n')[0] == 'pass'
    res['build_fail_line_fails'] = build_matcher(0, 'RESULT FAIL conversion failed\n')[0] == 'FAIL'
    res['build_no_result_fails'] = build_matcher(0, 'build seconds: 100\n')[0] == 'FAIL'
    res['build_nonzero_exit_fails'] = build_matcher(1, 'RESULT OK\n')[0] == 'FAIL'
    res['read_count_passes'] = read_matcher(0, 'output cells: 9  written to x\n')[0] == 'pass'
    res['read_no_count_fails'] = read_matcher(0, 'NOT A NOTEBOOK\n')[0] == 'FAIL'
    res['read_negative_count_fails'] = read_matcher(0, 'output cells: -3  written to x\n')[0] == 'FAIL'
    res['read_nonnumeric_count_fails'] = read_matcher(0, 'output cells: nine  written to x\n')[0] == 'FAIL'
    cd = tempfile.mkdtemp(); open(os.path.join(cd, 'count.txt'), 'w').write('2')
    for i in (1, 2): open(os.path.join(cd, 'cell-%02d.txt' % i), 'w').write('x')
    res['cells_complete_passes'] = cells_complete(cd, 2)
    os.remove(os.path.join(cd, 'cell-02.txt')); res['missing_cell_file_fails'] = not cells_complete(cd, 2)
    clean = {'commit': H.PIN['commit'], 'toolchain': H.PIN['toolchain'], 'sources': dict(H.PIN['sources']),
             'status': [' M Rule30Submission.lean', '?? Rule30Submission.template.lean']}
    res['admission_clean_passes'] = admission(clean) == []
    res['admission_unknown_untracked_fails'] = admission(dict(clean, status=clean['status'] + ['?? unknown-input.py'])) != []
    res['admission_altered_tracked_fails'] = admission(dict(clean, status=clean['status'] + [' M lakefile.toml'])) != []
    pd = tempfile.mkdtemp()
    for k in SCRIPTS: shutil.copy2(os.path.join(repo, 'reports/wolfram-agents/pipeline', k), os.path.join(pd, k))
    res['scripts_clean_pass'] = all(v['expected'] == v['actual'] for v in scripts_check(pd).values())
    for k in SCRIPTS:
        q = tempfile.mkdtemp()
        for kk in SCRIPTS: shutil.copy2(os.path.join(pd, kk), os.path.join(q, kk))
        open(os.path.join(q, k), 'a').write(' ')
        res['scripts_changed_%s_fails' % k] = not all(v['expected'] == v['actual'] for v in scripts_check(q).values())
    base_pid, own_g = 100, 500
    inv_ok = [(base_pid, 1, 90, '/Applications/Wolfram Engine.app/x/wolfram'), (501, 500, own_g, '/Applications/Wolfram Engine.app/x/WolframKernel')]
    res['kernels_baseline_plus_owned_ok'] = kernel_verdict(inv_ok, {base_pid}, {own_g})[0] == 'ok'
    res['kernels_three_over'] = kernel_verdict(inv_ok + [(777, 1, 777, '/Applications/Wolfram Engine.app/x/WolframKernel')], {base_pid}, {own_g})[0] == 'over'
    res['kernels_new_unowned_uncertain'] = kernel_verdict([(base_pid, 1, 90, 'p'), (888, 1, 888, 'q')], {base_pid}, {own_g})[0] == 'uncertain'
    real_killpg, real_kill, prev_usr1 = os.killpg, os.kill, signal.getsignal(signal.SIGUSR1)
    targets = []
    def no_killpg(*a): raise AssertionError('the watcher signalled a group')
    def own_only(pid, sig):
        targets.append((pid, sig))
        if pid != os.getpid() or sig != signal.SIGUSR1: raise AssertionError('the watcher signalled another process')
        real_kill(pid, sig)
    os.killpg, os.kill = no_killpg, own_only
    signal.signal(signal.SIGUSR1, on_watch_signal)
    def stage(inv_fn, hold=1.5, join_s=2):
        """A mock stage step: the main thread holds the watch open while it waits, as during run_step."""
        kw = KernelWatch(inv_fn=inv_fn, period=0.05, join_s=join_s)
        try:
            with kw:
                t1 = time.time()
                while time.time() - t1 < hold: time.sleep(0.02)
            return kw, None
        except KernelLimit as e:
            return kw, e
    try:
        def raising(): raise H.MonitorError('ps failed')
        kw, e = stage(raising)
        res['hook_monitor_error_interrupts_step'] = e is not None and (decide_watch(kw) or '').startswith('UNKNOWN: kernel monitoring failed')
        three = lambda: [(1, 0, 1, 'a'), (2, 0, 2, 'b'), (3, 0, 3, 'c')]
        kw, e = stage(three)
        res['hook_three_kernels_interrupts_step'] = e is not None and (decide_watch(kw) or '').startswith('UNKNOWN: more than two')
        one = lambda: [(1, 0, 1, 'a')]
        kw, e = stage(one, hold=0.4)
        res['hook_clean_runs_through'] = e is None and decide_watch(kw) is None and not kw.requested
        late0 = WATCH['late']
        def slow_three(): time.sleep(0.4); return three()
        kw, e = stage(slow_three, hold=0.05, join_s=0.05)
        alive = kw.alive_after
        t1 = time.time(); raised_late = False
        try:
            while time.time() - t1 < 1.0: time.sleep(0.02)
        except KernelLimit:
            raised_late = True
        res['hook_alive_watcher_is_unknown'] = e is None and alive is True and (decide_watch(kw) or '').startswith('UNKNOWN: the kernel watcher did not stop')
        res['hook_no_request_after_close'] = not raised_late and not kw.requested and WATCH['late'] == late0
        try:
            own_stop_request(); time.sleep(0.1); raised_late = False
        except KernelLimit:
            raised_late = True
        res['hook_late_request_only_counted'] = not raised_late and WATCH['late'] == late0 + 1
        res['watcher_signals_only_this_process'] = bool(targets) and all(t == (os.getpid(), signal.SIGUSR1) for t in targets)
    except AssertionError:
        res['watcher_signals_only_this_process'] = False
    finally:
        os.killpg, os.kill = real_killpg, real_kill
        signal.signal(signal.SIGUSR1, prev_usr1)
    res['hook_refuses_without_handler'] = False
    try:
        with KernelWatch(inv_fn=lambda: [], period=0.05): pass
    except RuntimeError:
        res['hook_refuses_without_handler'] = True
    import tempfile
    signal.signal(signal.SIGUSR1, on_watch_signal)
    try:
        with tempfile.TemporaryDirectory() as tk, tempfile.TemporaryDirectory() as to:
            sup = H.Supervisor(tk, to); rec, got = None, None
            try:
                with KernelWatch(inv_fn=lambda: [(1, 0, 1, 'a'), (2, 0, 2, 'b'), (3, 0, 3, 'c')], period=0.2, join_s=2) as kw:
                    rec = sup.run_step('mock_step', ['sleep', '30'], to, 60, 60, H.m_pass)
            except KernelLimit as e:
                got = e
            st = sup.receipts['steps'][-1] if sup.receipts['steps'] else {}
            res['w1a_step_interrupted_and_group_killed'] = (got is not None and rec is None and st.get('reason') == 'exception'
                                                            and st.get('group_members_after') == 0 and st.get('wall_s', 99) < 10)
    finally:
        signal.signal(signal.SIGUSR1, prev_usr1)
    fk = final_kernel_record({base_pid}, os.getpid(), kill=False)
    res['final_record_has_inventory_and_uncertainty'] = 'inventory' in fk and 'uncertain' in fk
    here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.realpath(os.path.join(here, '../../..'))
    files = {'essay': (os.path.join(repo, 'reports/wolfram-agents/submissions', NAME, 'essay.md'), ESSAY_SHA256),
             'module': (os.path.join(repo, 'reports/wolfram-agents/submissions', NAME, 'Rule30Submission.lean'), MODULE_SHA256)}
    files.update({k: (os.path.join(repo, 'reports/wolfram-agents/pipeline', k), v) for k, v in SCRIPTS.items()})
    for k, (p, want) in files.items():
        res['digest_' + k + '_true_file'] = H.digest(p) == want
        t = tempfile.mkdtemp(); q = os.path.join(t, 'x'); data = open(p, 'rb').read(); open(q, 'wb').write(data[:-1] + (b' ' if data[-1:] != b' ' else b'\n'))
        res['digest_' + k + '_rejects_one_byte'] = H.digest(q) != want
    ok = all(res.values())
    print(json.dumps(res, indent=1)); print('TRAP-PAIR NOTEBOOK CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def main():
    if sys.argv[1:] == ['--controls']:
        sys.exit(0 if controls() else 1)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = RSS_STOP_BYTES; H.CAPS['artifacts_max_bytes'] = ARTIFACTS_MAX_BYTES; H.CAPS['log_max_bytes'] = LOG_MAX_BYTES
    if len(sys.argv) != 4 or not all(os.path.isabs(a) for a in sys.argv[1:4]): print('REFUSED: three absolute paths required'); sys.exit(3)
    pipe, repo, out = (os.path.realpath(a) for a in sys.argv[1:4])
    kit = os.path.join(pipe, 'Rule30PrizeKit')
    if out.startswith(pipe + os.sep) or out.startswith(repo + os.sep) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be new or empty, outside the pipeline folder and the repository'); sys.exit(3)
    if os.path.exists(os.path.join(pipe, NAME)): print('REFUSED: the staged folder already exists'); sys.exit(3)
    if H.digest(H.__file__) != W1A_SHA256: print('REFUSED: W1A is not the pinned bytes'); sys.exit(3)
    src = {'essay.md': (os.path.join(repo, 'reports/wolfram-agents/submissions', NAME, 'essay.md'), ESSAY_SHA256),
           'Rule30Submission.lean': (os.path.join(repo, 'reports/wolfram-agents/submissions', NAME, 'Rule30Submission.lean'), MODULE_SHA256)}
    scr = {k: (os.path.join(repo, 'reports/wolfram-agents/pipeline', k), v) for k, v in SCRIPTS.items()}
    bad = [k for k, (p, want) in list(src.items()) + list(scr.items()) if H.digest(p) != want]
    if bad: print('REFUSED: digests differ for %s' % bad); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['trap_pair_notebook'] = {'this_sha256': H.digest(os.path.abspath(__file__)), 'w1a_sha256': W1A_SHA256, 'essay_sha256': ESSAY_SHA256, 'module_sha256': MODULE_SHA256,
                               'scripts': SCRIPTS, 'caps': {'stage_s': STAGE_S, 'build': [BUILD_WALL_S, BUILD_CPU_S], 'read': [READ_WALL_S, READ_CPU_S],
                               'rss_stop_bytes': RSS_STOP_BYTES, 'artifacts_max_bytes': ARTIFACTS_MAX_BYTES, 'notebook_max_bytes': NOTEBOOK_MAX_BYTES}, 'nice_inherited': os.nice(0)}
    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)
    def on_term(signum, frame):
        raise SystemExit('SIGTERM')
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGUSR1, on_watch_signal)
    try:
        before = kit_state(kit); R['kit_before'] = before; sup.save()
        why = admission(before)
        if why: R['kit_refusal'] = why; stop('kit admission failed: %s' % why)
        inv0 = kernel_inventory(); R['kernels_baseline'] = inv0; sup.save()
        if len(inv0) > KERNEL_LIMIT - 1: stop('more than one Wolfram kernel at baseline: %s' % [k[0] for k in inv0])
        baseline_pids = {k[0] for k in inv0}; R['_baseline_pids'] = sorted(baseline_pids)
        def after_step(label):
            inv = kernel_inventory(); new = [k for k in inv if k[0] not in baseline_pids]
            gs = owned_groups(os.getpid()); unowned = [k for k in new if k[2] not in gs]
            for g in {k[2] for k in new if k[2] in gs}:
                try: os.killpg(g, signal.SIGKILL)
                except ProcessLookupError: pass
            rest = [k for k in kernel_inventory() if k[0] not in baseline_pids]
            R.setdefault('kernels_after_steps', {})[label] = {'new': new, 'unowned': unowned, 'remaining': rest}; sup.save()
            if unowned or rest: stop('UNKNOWN: a kernel outside the baseline remains after %s (not signalled if unowned): %s' % (label, [k[0] for k in rest or unowned]))
        if H.pressure_bad(sup.baseline): stop('pressure at launch')
        r = sup.register(H.preflight())
        if r['verdict'] != 'pass': stop('preflight failed')
        keep = os.path.join(out, 'preserved-scripts'); os.makedirs(keep)
        for k in SCRIPTS:
            p = os.path.join(pipe, k)
            if os.path.exists(p): shutil.copy2(p, os.path.join(keep, k))
        R['trap_pair_notebook']['preserved_scripts'] = {k: (H.digest(os.path.join(keep, k)) if os.path.exists(os.path.join(keep, k)) else None) for k in SCRIPTS}
        os.makedirs(os.path.join(pipe, NAME))
        for k, (p, want) in src.items():
            shutil.copy2(p, os.path.join(pipe, NAME, k))
            if H.digest(os.path.join(pipe, NAME, k)) != want: stop('staged %s digest differs' % k)
        for k, (p, want) in scr.items():
            shutil.copy2(p, os.path.join(pipe, k))
            if H.digest(os.path.join(pipe, k)) != want: stop('installed %s digest differs' % k)
        sup.art_baseline = {p: n for p, n in H.snapshot(kit, out).items() if not p.startswith(out + os.sep)}
        sup.save()
        nb_out = os.path.join(out, 'essay.nb'); t0 = time.time()
        with KernelWatch(sink=R, key='kernel_watch_build') as kw:
            rb = sup.run_step('build_notebook', ['wolframscript', '-file', 'build_sub.wl', NAME, nb_out], pipe, BUILD_WALL_S, BUILD_CPU_S, build_matcher)
        sup.save()
        why_w = decide_watch(kw)
        if why_w: stop(why_w + ' (build)')
        after_step('build')
        if rb['verdict'] != 'pass': stop('build: %s (%s) %s' % (rb['verdict'], rb['reason'], rb.get('match_note')))
        if not (os.path.exists(nb_out) and os.path.getmtime(nb_out) >= t0 - 1): stop('no fresh notebook')
        nb_bytes = os.path.getsize(nb_out); nb_sha = H.digest(nb_out)
        if nb_bytes > NOTEBOOK_MAX_BYTES: stop('notebook above 8 MiB')
        shutil.copy2(nb_out, os.path.join(pipe, NAME, 'essay.nb'))
        if H.digest(os.path.join(pipe, NAME, 'essay.nb')) != nb_sha: stop('notebook copy digest differs')
        R['notebook'] = {'bytes': nb_bytes, 'sha256': nb_sha}; sup.save()
        with KernelWatch(sink=R, key='kernel_watch_read') as kw2:
            rr = sup.run_step('read_cells', ['wolframscript', '-file', 'read_nb_full.wl', NAME, os.path.join(out, 'cells')], pipe, READ_WALL_S, READ_CPU_S, read_matcher)
        sup.save()
        why_w = decide_watch(kw2)
        if why_w: stop(why_w + ' (read)')
        after_step('read')
        if rr['verdict'] != 'pass': stop('read: %s (%s) %s' % (rr['verdict'], rr['reason'], rr.get('match_note')))
        n_cells = read_count(open(os.path.join(out, 'read_cells.log'), errors='replace').read()) if os.path.exists(os.path.join(out, 'read_cells.log')) else None
        R['cells'] = {'count': n_cells}
        after = kit_state(kit)
        try: m_final = H.metrics(kit)
        except H.MonitorError as e: m_final = {'error': str(e)}
        arts = H.new_artifact_bytes(kit, out, sup.art_baseline)
        predicates = {
            'kit_unchanged': after == before,
            'staged_sources_unchanged': all(H.digest(os.path.join(pipe, NAME, k)) == w for k, (p, w) in src.items()),
            'cells_written': isinstance(n_cells, int) and cells_complete(os.path.join(out, 'cells'), n_cells),
            'installed_scripts_unchanged': all(v['expected'] == v['actual'] for v in scripts_check(pipe).values()),
            'no_kernel_beyond_baseline': not [k for k in kernel_inventory() if k[0] not in baseline_pids],
            'build_step_cleanup': rb.get('group_members_after') == 0 and rb.get('final_problems') == [],
            'read_step_cleanup': rr.get('group_members_after') == 0 and rr.get('final_problems') == [],
            'stage_within_deadline': sup.remaining() >= 0,
            'artifacts_within_cap': arts <= ARTIFACTS_MAX_BYTES,
            'pressure_ok_after': isinstance(m_final, dict) and 'error' not in m_final and not H.pressure_bad(m_final),
            'swap_growth_within_cap': isinstance(m_final, dict) and 'swap_used_bytes' in m_final and m_final['swap_used_bytes'] - sup.baseline['swap_used_bytes'] <= H.CAPS['swap_growth_bytes'],
            'disk_above_floor': isinstance(m_final, dict) and m_final.get('disk_free_bytes', 0) >= H.CAPS['disk_free_min_bytes'],
        }
        R['final'] = {'predicates': predicates, 'values': {'artifact_bytes': arts, 'kit_after': after, 'stage_remaining_s': round(sup.remaining(), 1)}}
        sup.save()
        if not all(predicates.values()): stop('final validation failed: %s' % [k for k, v in predicates.items() if not v])
        R['complete'] = True
    except SystemExit:
        raise
    except KernelLimit:
        R['stopped'] = 'UNKNOWN: the kernel watch stopped the running step (kernel_watch_build / kernel_watch_read)'; sup.save()
        print('STOP:', R['stopped']); sys.exit(1)
    except BaseException as e:
        R['stopped'] = 'exception: %r' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    finally:
        R['final_kernels'] = final_kernel_record(R.get('_baseline_pids'), os.getpid())
        R['final_kernels']['late_stop_requests'] = WATCH['late']
        R.pop('_baseline_pids', None)
        R['recovery'] = {'preserved_scripts': os.path.join(out, 'preserved-scripts'), 'staged_folder': os.path.join(pipe, NAME),
                         'installed_scripts': scripts_check(pipe), 'note': 'the staged folder and installed scripts stay by design; no automatic retry'}
        R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: the trap-pair notebook built and its cells read (not submitted)')


if __name__ == '__main__':
    main()
