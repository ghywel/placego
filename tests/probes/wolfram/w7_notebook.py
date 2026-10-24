#!/usr/bin/env python3
"""W7, revision 2 (2026-10-24; revision 1 answered GPT's GC1762 gates, this revision answers GC1764's three corrections):
the width-60 submission notebook build as a stage under the UNCHANGED W1A supervisor (tests/probes/wolfram/w1a_harness.py,
bytes pinned below). NOT an agreed job until GPT accepts this exact file; nothing runs on import; the submission itself
follows only on a pass, by the pipeline's submit script, on the owner's express permission.

Revision 2 changes (GC1764):
  1. Reference payloads bound, not just the manifest: the ten build-1 reference cells' BYTE sha256 (Python, H.digest on
     file bytes) are pinned as constants in this file (they equal the Wolfram-side string hashes of digests.txt, checked
     once, but the gate relies on the byte digests alone); every reference file is verified against its constant before
     production AND again inside the gate at the moment it is read, so a changed reference with an unchanged manifest FAILS.
  2. The notebook is written INSIDE the stage's output folder (build_sub.wl revision 3 takes the output path), so the
     supervisor's artifact sampling covers it (artifact cap lowered to 64 MiB: W6's build artifacts were 11.8 MiB, build 1's
     notebook 0.5 MiB), and a watcher thread samples the notebook's size every second during the build: above 8 MiB, or
     an existing but unreadable file, kills the owned group and records the reason (fail closed). On a pass the notebook
     is copied to NAME/essay.nb for the submit script, which must not exist beforehand, and the copy's digest is verified.
  3. Ownership and signals over the whole child lifetime: the watcher discovers owned groups every second as this
     process's children that lead their own session (the supervisor spawns every step with start_new_session), records
     them, and the signal handler kills every owned group ITSELF before raising, so a TERM/INT/HUP that lands between
     the supervisor's spawn and its try/finally still terminates the child; a repeated signal during cleanup is recorded
     and deferred (no second exception); a final owned-group check runs on every exit path and persists the receipt;
     a watcher that cannot enumerate processes three times running kills the owned groups and stops the stage
     (UNKNOWN, never a pass). Supervisor construction and the memory read are inside the guarded receipt path; a
     failure there still writes a stopped receipt. The group RSS stop must be STRICTLY below half of physical memory.
     The remote MarkdownToNotebook resource is recorded by its provenance line, not pinned.

The stage, in order: pins (supervisor, both pipeline scripts, staged essay, module in both places, the ten reference
cells, the kit copy's commit/toolchain/pinned sources/deps/git status, physical memory); refuse if the output notebook
or NAME/essay.nb exists; step 1 `wolframscript -file build_sub.wl NAME OUT/essay.nb` under run_step (group RSS, wall,
CPU, deadline, pressure, swap, disk, log, artifacts, extra lean) with the watcher beside it; fresh-output check (exists,
newer than the step start, differs from build 1's digest, within 8 MiB); step 2 `read_nb_full.wl NAME OUT/cells
OUT/essay.nb`; the FULL-CELL gate (ten cells; 1, 2, 3, 5, 6, 7, 8, 9 byte-equal to the verified reference; 4 and 10 equal
after normalising LeanLink's per-run temporary module name; semantic predicates); final predicates; the copy for the
submit script. Exit codes: pass 0, STOP 1, REFUSED 3, interrupted 130.

Envelope: stage 4,500 s; build wall 3,600 s / CPU 4,000 s (build 1: 2,120.8 s wall); read 300 / 300 s; GROUP RSS stop 7 GiB
(strictly below half of the 16 GiB read from hw.memsize); pressure level 2; swap growth 1 GiB; disk floor 5 GiB;
artifacts 64 MiB over the kit's build trees and the output folder; the notebook 8 MiB, sampled during the build; log
10 MiB; one lean process; ordinary priority recorded; no retry.

Controls (`--controls`): revision 1's 27 (matcher, read matcher, gate, fresh output, interruption with a child inside
run_step, failed process enumeration, the build script's two failure paths) plus: a changed reference payload with an
unchanged manifest FAILS the gate; the notebook growing past the cap during a stand-in step is killed by the watcher
(reason recorded, group empty); a signal arriving while an owned session-leader child exists OUTSIDE run_step kills it;
two signals in quick succession raise once, record two, leave the group empty; a watcher that cannot enumerate
processes stops the stage with the group killed.

Usage: python3 w7_notebook.py PIPELINE_DIR OUT_DIR      (absolute; OUT_DIR empty or absent)
       python3 w7_notebook.py --controls               (W7_REF_DIR = the reference folder)
"""
import json, os, re, shutil, signal, subprocess, sys, tempfile, threading, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import w1a_harness as H

NAME = 'd-exact-60'
REPO = os.path.realpath(os.path.join(HERE, '..', '..', '..'))
PIPE_SCRIPTS = os.path.join(REPO, 'reports', 'wolfram-agents', 'pipeline')
STAGE_S, BUILD_WALL_S, BUILD_CPU_S, READ_WALL_S, READ_CPU_S = 4500, 3600, 4000, 300, 300
GROUP_RSS_STOP = 7 * H.GIB
SWAP_GROWTH = 1 * H.GIB
ARTIFACTS_MAX = 64 * H.MIB
NOTEBOOK_MAX_BYTES = 8 * H.MIB
EXPECTED_CELLS = 10
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
BUILD_SUB_SHA256 = '6f734fbd71a8936c0251d321dfb69b858ea35fca371dc776b221a3cb712187da'
READ_NB_SHA256 = 'c5b89fb60f57bccee440983eeaaf65edeb37d434cca47025783bf25bd6787f44'
ESSAY_SHA256 = 'd83f1bd06ccb615ec630de427be3e37e331824f3e86ac980347173e4969a419b'
MODULE_SHA256 = 'f53da13f999db822e6f5560bbc7c9f9188c963a4294377e5712c6857633fff04'
BUILD1_NB_SHA256 = 'd02d8cc0a5eaa3e5288c449d97299603cbe45171b2ba46bdc8ebead7b5fdf4d1'
REF_CELL_SHA256 = {                      # byte sha256 of ref-build1/cell-NN.txt, the frozen build-1 output cells
    1: 'dc1fb470fcab0ce4f3672fdb2e95fd75d485837f1f1631367b8e72fecda79924',
    2: '539f78a4995e567cb424373f3264d022c1498e1ee086468b436b047254241363',
    3: 'd0523433febede1c1707a8e33113ee9979c442bc9b6b68d20680852af18dc22d',
    4: 'e251783a317ac7ce42ff819751c3e367fd7abc5978946c9fb35787e76dc1601f',
    5: 'a3174adb1733bc712abe48364da6e83faa43f03ab10c280fbb172be92439d3fa',
    6: '43dbafd058ca4c7be2a9dcaca576d68a751c1f8b4dd92fbd3f62b4af03487714',
    7: '03458d6b62d3f5856abe0fee17ff7cedf90c266e56b2a932a47468cd299515e2',
    8: 'cb8589a60d320d995fbc31dd15414e1f224a2889a50743530be6edf50b7c6b8a',
    9: '8072de8d525a6da8e7d88e6ea94c1a18114f8f65ad9e51debfe2d102a3de4ff5',
    10: '913a71b3e59d02f9426fdf8bce96aa678624fd1251db3293347fb5dbb7cd8313',
}
KNOWN_SUBMISSION_ARTIFACTS = {'Rule30Submission.lean', 'Rule30Submission.template.lean', 'Rule30Submission.prev.lean.bak', 'channel-12.lean',
                              'corollary-f.lean', 'diagonals.lean', 'README.md', 'rule-210-two-sided.lean', 'rule-210.lean', 'sturmian-all.lean',
                              'sturmian.lean', 'theorem-a4.lean', 'white-end.lean', 'words-A.lean', 'words-B.lean'}
TMP_RE = re.compile(r'LeanLinkTmp\d+x\d+')
NORMALISED_CELLS = {4, 10}
SEMANTIC = {
    1: ['BoxData[RowBox[{"{", RowBox[{"60", ",", "114"}], "}"}]]'],
    4: ['LeanEnvironment', 'Constants: ', '"4363"'],          # InputForm text escapes the strings inside boxes, so the needles are the bare words
    8: ['check 60 115 18 0 = true', 'check 60 115 18 4095 = true', 'ChunksOK 60 115 18 0 4096'],
    9: ['BoxData[RowBox[{"{", RowBox[{"\\"Classical.choice\\"", ",", "\\"Quot.sound\\"", ",", "\\"propext\\""}], "}"}]]'],
    10: ['TagBox["Success", "SummaryHead"]', 'The kernel accepts all 8466 declarations of LeanLinkTmp<id>.'],
}


class Interrupted(BaseException):
    pass


# ---- ownership, the watcher and the signal path ----------------------------------------------------------------------

class Owned:
    """Owned process groups: this process's children that lead their own session (the supervisor's steps and nothing
    else). Discovered by checked ps; killed as groups; verified after. One instance per stage; the signal handler and
    the watcher thread share it."""

    def __init__(self, record):
        self.rec = record                      # a dict inside the receipt: groups, events, signals
        self.rec.setdefault('groups', {}); self.rec.setdefault('events', []); self.rec.setdefault('signals', [])
        self.lock = threading.Lock(); self.interrupting = False; self.stop_reason = None
        self.in_handler = False                # re-entrancy guard: a signal that lands inside the handler is recorded and deferred
        self.fail_discover = False             # control knob: make discovery fail

    def discover(self):
        if self.fail_discover:
            raise H.MonitorError('injected discovery failure')
        out = H.checked(['ps', '-axo', 'pid=,pgid=,ppid=,comm='])
        me = os.getpid(); found = {}
        for line in out.splitlines():
            parts = line.split(None, 3)
            if len(parts) < 4: continue
            pid, pgid, ppid = int(parts[0]), int(parts[1]), int(parts[2])
            if ppid == me and pgid == pid:
                found[pgid] = parts[3].strip()
        with self.lock:
            for g, comm in found.items():
                self.rec['groups'].setdefault(str(g), {'comm': comm, 'first_seen': time.strftime('%H:%M:%S')})
        return found

    def members(self, pgid):
        out = H.checked(['ps', '-axo', 'pgid=,pid='])
        return sum(1 for l in out.splitlines() if l.split() and l.split()[0] == str(pgid))

    def kill_all(self, reason):
        """Re-discover (a decision to kill is always taken on a process list read AFTER the trigger, so a child spawned
        between the last sample and the trigger is included), then SIGKILL every owned group not yet verified gone;
        verify; mark the empty ones gone (so a reused pgid is never signalled later); record. Returns the number of
        members left (None if unverifiable)."""
        try:
            self.discover()
        except H.MonitorError as e:
            with self.lock: self.rec['events'].append({'t': time.strftime('%H:%M:%S'), 'reason': 'rediscovery failed before kill: %s' % e})
        with self.lock:
            groups = [int(g) for g, v in self.rec['groups'].items() if not v.get('gone')]
        left_total = 0; unverified = False; errors = []
        for g in groups:
            try:
                H.kill_group(g)
            except OSError as e:                       # EPERM: the pgid belongs to someone else now; recorded, never retried
                errors.append('%d: %r' % (g, e))
        if groups: time.sleep(0.5)
        for g in groups:
            try:
                n = self.members(g)
            except H.MonitorError:
                unverified = True; n = None
            if n: left_total += n
            if n == 0:
                with self.lock: self.rec['groups'][str(g)]['gone'] = True
        with self.lock:
            self.rec['events'].append({'t': time.strftime('%H:%M:%S'), 'reason': reason, 'groups': groups,
                                       'members_left': None if unverified else left_total, 'errors': errors})
        return None if unverified else left_total

    def on_signal(self, signum, frame):
        name = signal.Signals(signum).name
        if self.in_handler:                            # landed inside this handler: record, defer, return
            self.rec['signals'].append({'t': time.strftime('%H:%M:%S'), 'signal': name, 'deferred': True, 'nested': True}); return
        self.in_handler = True
        try:
            with self.lock:
                self.rec['signals'].append({'t': time.strftime('%H:%M:%S'), 'signal': name, 'deferred': self.interrupting})
                first = not self.interrupting
                self.interrupting = True
            self.kill_all('signal ' + name)
        finally:
            self.in_handler = False
        if first:
            raise Interrupted(name)
        # a repeated signal during cleanup: owned groups re-killed above, nothing raised (deferred)

    def install(self):
        for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
            signal.signal(s, self.on_signal)


class Watcher(threading.Thread):
    """Every second: discover owned groups; sample the notebook's size (fail closed on an unreadable existing file);
    kill the owned groups on a cap or on three consecutive enumeration failures and record the reason."""

    def __init__(self, owned, notebook_path, cap_bytes, interval=1.0):
        super().__init__(daemon=True)
        self.owned = owned; self.nb = notebook_path; self.cap = cap_bytes; self.interval = interval
        self.stop_flag = threading.Event(); self.failures = 0; self.peak_nb = 0

    def run(self):
        while not self.stop_flag.is_set():
            try:
                self.owned.discover(); self.failures = 0
            except H.MonitorError as e:
                self.failures += 1
                if self.failures >= 3:
                    self.owned.stop_reason = 'watcher-monitor-failure: %s' % e
                    self.owned.kill_all(self.owned.stop_reason); break
            if self.nb and os.path.exists(self.nb):
                try:
                    size = os.stat(self.nb).st_size
                except OSError as e:
                    self.owned.stop_reason = 'notebook-unreadable: %r' % e
                    self.owned.kill_all(self.owned.stop_reason); break
                self.peak_nb = max(self.peak_nb, size)
                if size > self.cap:
                    self.owned.stop_reason = 'notebook-cap: %d bytes > %d' % (size, self.cap)
                    self.owned.kill_all(self.owned.stop_reason); break
            self.stop_flag.wait(self.interval)


# ---- matchers ------------------------------------------------------------------------------------------------------

def m_build(rc, text):
    """exit 0; `build seconds:`, `resource provenance:` (recorded, not pinned) and `notebook bytes:` lines present; no
    RESULT FAIL and no $Failed; RESULT OK is the last non-empty line of the script's own output (before `time -l`)."""
    try:
        if rc != 0:
            return 'FAIL', 'exit %d' % rc
        own = []
        for l in text.splitlines():
            if re.match(r'\s*[\d.]+ real\s+[\d.]+ user\s+[\d.]+ sys', l):
                break
            own.append(l.rstrip())
        own_ne = [l for l in own if l.strip()]
        problems = []
        if not any(l.startswith('build seconds:') for l in own): problems.append('no build seconds line')
        if not any(l.startswith('resource provenance:') for l in own): problems.append('no resource provenance line')
        if not any(l.startswith('notebook bytes:') for l in own): problems.append('no notebook bytes line')
        if any('RESULT FAIL' in l for l in own): problems.append('RESULT FAIL present')
        if any('$Failed' in l for l in own): problems.append('$Failed present')
        if not own_ne or own_ne[-1].strip() != 'RESULT OK': problems.append('RESULT OK is not the last line')
        note = json.dumps({'provenance_recorded_not_pinned': [l for l in own if l.startswith('resource provenance:')][:1],
                           'build_seconds_line': [l for l in own if l.startswith('build seconds:')][:1]})
        return ('pass' if not problems else 'FAIL'), (note if not problems else 'FAIL: %s | %s' % ('; '.join(problems), note))
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


def m_read(rc, text):
    try:
        if rc != 0:
            return 'FAIL', 'exit %d' % rc
        ok = any(l.strip().startswith('output cells: %d ' % EXPECTED_CELLS) or l.strip() == 'output cells: %d' % EXPECTED_CELLS for l in text.splitlines())
        return ('pass', 'output cells: %d' % EXPECTED_CELLS) if ok else ('FAIL', 'cell count line missing or not %d' % EXPECTED_CELLS)
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


# ---- the reference binding and the full-cell gate ---------------------------------------------------------------------

def verify_reference(ref_dir):
    """Every pinned reference cell present with its pinned byte digest. Returns (ok, {i: digest_or_error})."""
    got = {}
    for i, want in REF_CELL_SHA256.items():
        p = os.path.join(ref_dir, 'cell-%02d.txt' % i)
        if not os.path.exists(p): got[i] = 'missing'; continue
        d = H.digest(p); got[i] = d if d == want else 'MISMATCH ' + d
    return all(v == REF_CELL_SHA256[i] for i, v in got.items()), got


def normalise(i, text):
    return TMP_RE.sub('LeanLinkTmp<id>', text) if i in NORMALISED_CELLS else text


def cell_gate(cells_dir, ref_dir):
    """(verdict, report). The reference file is re-verified against its pinned byte digest at the moment it is read, so
    the comparison is with the frozen build-1 cell and nothing else. Every exception is a FAIL."""
    try:
        problems = []; per_cell = {}
        cnt_path = os.path.join(cells_dir, 'count.txt')
        if not os.path.exists(cnt_path):
            return 'FAIL', {'problems': ['no count.txt']}
        try:
            count = int(open(cnt_path).read().strip())
        except Exception as e:
            return 'FAIL', {'problems': ['count.txt unreadable: %r' % e]}
        if count != EXPECTED_CELLS: problems.append('cell count %d' % count)
        for i in range(1, EXPECTED_CELLS + 1):
            fn = 'cell-%02d.txt' % i
            p = os.path.join(cells_dir, fn); q = os.path.join(ref_dir, fn)
            if not os.path.exists(p): problems.append('%s missing' % fn); per_cell[i] = 'missing'; continue
            if not os.path.exists(q): problems.append('%s missing in the reference' % fn); per_cell[i] = 'no-reference'; continue
            qd = H.digest(q)
            if qd != REF_CELL_SHA256[i]: problems.append('reference %s is not the pinned bytes' % fn); per_cell[i] = 'reference-unbound'; continue
            a = open(p, encoding='utf-8').read(); b = open(q, encoding='utf-8').read()
            na, nb = normalise(i, a), normalise(i, b)
            equal = (na == nb)
            per_cell[i] = {'bytes': len(a.encode('utf-8')), 'equal_to_reference': equal, 'normalised': i in NORMALISED_CELLS,
                           'sha256': H.digest(p), 'reference_sha256_verified': qd}
            if not equal: problems.append('cell %d differs from the reference%s' % (i, ' after normalisation' if i in NORMALISED_CELLS else ''))
            for needle in SEMANTIC.get(i, []):
                if needle not in na: problems.append('cell %d lacks %r' % (i, needle[:60]))
        extra = sorted(f for f in os.listdir(cells_dir) if f.startswith('cell-') and f not in {'cell-%02d.txt' % i for i in range(1, EXPECTED_CELLS + 1)})
        if extra: problems.append('extra cell files %r' % extra)
        return ('pass' if not problems else 'FAIL'), {'problems': problems, 'cells': per_cell, 'count': count}
    except Exception as e:
        return 'FAIL', {'problems': ['gate exception: %r' % e]}


def fresh_output(path, t_start_epoch, old_sha, max_bytes):
    rec = {'exists': os.path.exists(path)}
    if not rec['exists']:
        return False, rec
    try:
        st = os.stat(path)
    except OSError as e:
        rec['error'] = repr(e); return False, rec
    rec.update({'mtime_epoch': st.st_mtime, 'newer_than_step_start': st.st_mtime >= t_start_epoch - 1.0, 'bytes': st.st_size,
                'sha256': H.digest(path)})
    rec['differs_from_build1'] = rec['sha256'] != old_sha
    rec['within_size_cap'] = st.st_size <= max_bytes
    return rec['newer_than_step_start'] and rec['differs_from_build1'] and rec['within_size_cap'], rec


# ---- controls ------------------------------------------------------------------------------------------------------

def controls():
    res = {}
    good = 'essay sha256: x\nnotebook path: y\nresource provenance: name MarkdownToNotebook  version 1.0.0\nbuild seconds: 2120.8  result: Shallow[y, 2]\nnotebook bytes: 515336  sha256: z\nRESULT OK\n      2120.0 real      3000.0 user      100.0 sys\n'
    res['good_log_passes'] = m_build(0, good)[0] == 'pass'
    res['result_fail_fails'] = m_build(0, good.replace('RESULT OK', 'RESULT FAIL conversion failed'))[0] == 'FAIL'
    res['missing_result_ok_fails'] = m_build(0, good.replace('RESULT OK\n', ''))[0] == 'FAIL'
    res['dollar_failed_fails'] = m_build(0, good.replace('Shallow[y, 2]', '$Failed'))[0] == 'FAIL'
    res['exit_1_fails'] = m_build(1, good)[0] == 'FAIL'
    res['missing_provenance_fails'] = m_build(0, good.replace('resource provenance: name MarkdownToNotebook  version 1.0.0\n', ''))[0] == 'FAIL'
    res['read_matcher_ten_passes'] = m_read(0, 'output cells: 10  written to x')[0] == 'pass'
    res['read_matcher_nine_fails'] = m_read(0, 'output cells: 9  written to x')[0] == 'FAIL'
    ref = os.environ.get('W7_REF_DIR', '')
    if not (ref and os.path.isdir(ref)):
        res['reference_dir_present'] = False
    else:
        okref, _ = verify_reference(ref)
        res['reference_payloads_bound'] = okref
        res['reference_against_itself_passes'] = cell_gate(ref, ref)[0] == 'pass'
        t = tempfile.mkdtemp()
        shutil.copytree(ref, os.path.join(t, 'same'))
        c = os.path.join(t, 'same', 'cell-07.txt'); s = open(c, encoding='utf-8').read()
        open(c, 'w', encoding='utf-8').write(s[:160] + s[160:].replace('114', '116', 1))
        res['equal_prefix_different_full_fails'] = cell_gate(os.path.join(t, 'same'), ref)[0] == 'FAIL'
        shutil.copytree(ref, os.path.join(t, 'miss')); os.remove(os.path.join(t, 'miss', 'cell-03.txt'))
        res['missing_cell_fails'] = cell_gate(os.path.join(t, 'miss'), ref)[0] == 'FAIL'
        shutil.copytree(ref, os.path.join(t, 'nine')); open(os.path.join(t, 'nine', 'count.txt'), 'w').write('9')
        res['nine_cells_fail'] = cell_gate(os.path.join(t, 'nine'), ref)[0] == 'FAIL'
        shutil.copytree(ref, os.path.join(t, 'tmpid'))
        for i in (4, 10):
            p = os.path.join(t, 'tmpid', 'cell-%02d.txt' % i); s = open(p, encoding='utf-8').read()
            open(p, 'w', encoding='utf-8').write(TMP_RE.sub('LeanLinkTmp11111111111111111111x222222', s))
        res['different_tmp_id_passes'] = cell_gate(os.path.join(t, 'tmpid'), ref)[0] == 'pass'
        shutil.copytree(ref, os.path.join(t, 'count'))
        p = os.path.join(t, 'count', 'cell-10.txt'); s = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(s.replace('8466', '8465'))
        res['wrong_declaration_count_fails'] = cell_gate(os.path.join(t, 'count'), ref)[0] == 'FAIL'
        # GC1764 item 1: a changed REFERENCE payload with an unchanged manifest, compared against an identical candidate
        shutil.copytree(ref, os.path.join(t, 'badref')); shutil.copytree(os.path.join(t, 'badref'), os.path.join(t, 'cand'))
        p = os.path.join(t, 'badref', 'cell-05.txt'); open(p, 'a', encoding='utf-8').write(' ')
        shutil.copy2(p, os.path.join(t, 'cand', 'cell-05.txt'))
        res['changed_reference_unchanged_manifest_fails'] = cell_gate(os.path.join(t, 'cand'), os.path.join(t, 'badref'))[0] == 'FAIL'
        res['verify_reference_detects_changed_payload'] = verify_reference(os.path.join(t, 'badref'))[0] is False
        shutil.rmtree(t)
    t = tempfile.mkdtemp(); nb = os.path.join(t, 'essay.nb'); open(nb, 'wb').write(b'x' * 100)
    old = time.time() - 3600; os.utime(nb, (old, old))
    res['stale_notebook_fails'] = fresh_output(nb, time.time(), 'none', NOTEBOOK_MAX_BYTES)[0] is False
    res['missing_notebook_fails'] = fresh_output(os.path.join(t, 'none.nb'), time.time(), 'none', NOTEBOOK_MAX_BYTES)[0] is False
    os.utime(nb, None)
    res['fresh_notebook_passes'] = fresh_output(nb, time.time() - 5, 'none', NOTEBOOK_MAX_BYTES)[0] is True
    res['same_as_build1_fails'] = fresh_output(nb, time.time() - 5, H.digest(nb), NOTEBOOK_MAX_BYTES)[0] is False
    shutil.rmtree(t)
    # the real supervisor, the ownership tracker and the watcher
    out = tempfile.mkdtemp(); kit = tempfile.mkdtemp()
    H.CAPS['stage_s'] = 300
    rec = {}; owned = Owned(rec); owned.install()
    # (a) interruption with a child inside run_step
    sup = H.Supervisor(kit, out)
    w = Watcher(owned, None, NOTEBOOK_MAX_BYTES); w.start()
    threading.Timer(2.0, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()
    got = None
    try:
        sup.run_step('interrupt_standin', ['zsh', '-c', 'sleep 60 & sleep 60'], out, 60, 60, H.m_pass)
    except Interrupted as e:
        got = str(e)
    step = sup.receipts['steps'][-1]
    time.sleep(0.6)
    res['interrupt_raised'] = got == 'SIGTERM'
    res['interrupt_step_recorded_exception'] = step.get('reason') == 'exception' and step.get('verdict') == 'UNKNOWN'
    res['interrupt_group_empty_after'] = step.get('group_members_after') == 0
    res['interrupt_owned_group_was_discovered'] = len(rec['groups']) >= 1
    res['interrupt_no_sleep_left'] = not subprocess.run(['pgrep', '-x', 'sleep'], capture_output=True, text=True).stdout.split()
    owned.interrupting = False
    # (b) GC1764 item 3: a signal while an owned session-leader child exists OUTSIDE run_step
    child = subprocess.Popen(['sleep', '60'], start_new_session=True)
    time.sleep(1.5)                                   # the watcher discovers it
    got2 = None
    try:
        os.kill(os.getpid(), signal.SIGTERM); time.sleep(0.2)
    except Interrupted as e:
        got2 = str(e)
    time.sleep(0.6); child.poll()
    res['outside_step_signal_raised'] = got2 == 'SIGTERM'
    res['outside_step_child_killed'] = child.returncode is not None and child.returncode != 0
    owned.interrupting = False
    # (c) two signals in quick succession: one exception, two recorded, group empty
    n_before = len(rec['signals'])
    threading.Timer(2.0, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()
    threading.Timer(2.4, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()
    raised = 0
    try:
        sup.run_step('double_signal_standin', ['zsh', '-c', 'sleep 60 & sleep 60'], out, 60, 60, H.m_pass)
    except Interrupted:
        raised += 1
        time.sleep(1.0)                               # the second signal lands here, during "cleanup"
    time.sleep(0.6)
    res['double_signal_raised_once'] = raised == 1
    res['double_signal_recorded_two_one_deferred'] = len(rec['signals']) - n_before == 2 and rec['signals'][-1]['deferred'] is True
    res['double_signal_no_sleep_left'] = not subprocess.run(['pgrep', '-x', 'sleep'], capture_output=True, text=True).stdout.split()
    owned.interrupting = False
    # (d) GC1764 item 2: the notebook growing past the cap during a step is killed by the watcher
    w.stop_flag.set(); w.join(2)
    nbpath = os.path.join(out, 'essay.nb')
    w2 = Watcher(owned, nbpath, NOTEBOOK_MAX_BYTES); w2.start()
    r = sup.run_step('notebook_growth_standin', ['zsh', '-c', 'dd if=/dev/zero of=%s bs=1m count=20 2>/dev/null; sleep 30' % nbpath], out, 60, 60, H.m_pass)
    w2.stop_flag.set(); w2.join(2)
    res['notebook_cap_killed_step'] = r.get('exit') not in (0, None) and r.get('verdict') != 'pass'
    res['notebook_cap_reason_recorded'] = (owned.stop_reason or '').startswith('notebook-cap')
    res['notebook_cap_group_empty'] = r.get('group_members_after') == 0
    os.remove(nbpath); owned.stop_reason = None
    # (e) failed process enumeration inside the supervisor (W1A fault knob)
    H.FAULTS['ps_fail_after'] = 1
    sup2 = H.Supervisor(kit, out)
    r2 = sup2.run_step('monitor_failure_standin', ['sleep', '5'], out, 60, 60, H.m_pass)
    H.FAULTS['ps_fail_after'] = None
    res['monitor_failure_is_unknown'] = r2.get('reason') == 'monitor-failure' and r2.get('verdict') == 'UNKNOWN'
    res['monitor_failure_group_cleaned'] = r2.get('group_members_after') == 0 and r2.get('exit') is not None
    # (f) the watcher cannot enumerate processes: owned groups killed, stage stop reason set
    w3 = Watcher(owned, None, NOTEBOOK_MAX_BYTES, interval=0.2); w3.start()
    child2 = subprocess.Popen(['sleep', '60'], start_new_session=True); time.sleep(0.8)
    owned.fail_discover = True; time.sleep(1.5); owned.fail_discover = False
    w3.stop_flag.set(); w3.join(2); child2.poll()
    res['watcher_failure_stops_and_kills'] = (owned.stop_reason or '').startswith('watcher-monitor-failure') and child2.returncode is not None
    owned.stop_reason = None
    shutil.rmtree(out); shutil.rmtree(kit)
    # the build script's two failure paths (one short kernel each)
    bs = os.path.join(PIPE_SCRIPTS, 'build_sub.wl')
    if os.path.exists(bs) and shutil.which('wolframscript'):
        d = tempfile.mkdtemp(); os.makedirs(os.path.join(d, 'noessay'))
        r = subprocess.run(['wolframscript', '-file', bs, 'noessay'], cwd=d, capture_output=True, text=True, timeout=240)
        res['build_script_no_essay_exit1_result_fail'] = r.returncode == 1 and 'RESULT FAIL' in r.stdout
        os.makedirs(os.path.join(d, 'stale')); open(os.path.join(d, 'stale', 'essay.md'), 'w').write('x'); open(os.path.join(d, 'stale', 'out.nb'), 'w').write('x')
        r = subprocess.run(['wolframscript', '-file', bs, 'stale', os.path.join(d, 'stale', 'out.nb')], cwd=d, capture_output=True, text=True, timeout=240)
        res['build_script_existing_output_exit1_result_fail'] = r.returncode == 1 and 'RESULT FAIL' in r.stdout
        shutil.rmtree(d)
    else:
        res['build_script_controls_ran'] = False
    ok = all(v is True for v in res.values())
    print(json.dumps(res, indent=1)); print('W7 CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


# ---- main ----------------------------------------------------------------------------------------------------------

def main():
    if sys.argv[1:] == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(sys.argv) != 3 or not all(os.path.isabs(a) for a in sys.argv[1:3]):
        print('REFUSED: usage w7_notebook.py PIPELINE_DIR OUT_DIR (absolute)'); sys.exit(3)
    pipe, out = (os.path.realpath(a) for a in sys.argv[1:3])
    kit = os.path.join(pipe, 'Rule30PrizeKit')
    if out.startswith(pipe + os.sep) or pipe.startswith(out + os.sep):
        print('REFUSED: the output folder must not lie inside the pipeline folder nor contain it'); sys.exit(3)
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty'); sys.exit(3)
    if H.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: the imported W1A supervisor is not the pinned bytes'); sys.exit(3)
    bs, rn = os.path.join(PIPE_SCRIPTS, 'build_sub.wl'), os.path.join(PIPE_SCRIPTS, 'read_nb_full.wl')
    ref_dir = os.path.join(pipe, NAME, 'ref-build1')
    for p, want, what in ((bs, BUILD_SUB_SHA256, 'build_sub.wl'), (rn, READ_NB_SHA256, 'read_nb_full.wl'),
                          (os.path.join(pipe, NAME, 'essay.md'), ESSAY_SHA256, 'staged essay'),
                          (os.path.join(pipe, NAME, 'Rule30Submission.lean'), MODULE_SHA256, 'pipeline module copy'),
                          (os.path.join(kit, 'Rule30Submission.lean'), MODULE_SHA256, "the kit's installed module")):
        if not os.path.exists(p) or H.digest(p) != want:
            print('REFUSED: %s missing or not the pinned bytes' % what); sys.exit(3)
    okref, refgot = verify_reference(ref_dir)
    if not okref:
        print('REFUSED: reference cells not the pinned bytes: %s' % {i: v for i, v in refgot.items() if v != REF_CELL_SHA256[i]}); sys.exit(3)
    nb_out = os.path.join(out, 'essay.nb'); nb_final = os.path.join(pipe, NAME, 'essay.nb')
    if os.path.exists(nb_final):
        print('REFUSED: %s/essay.nb already exists; the submit copy would not be fresh' % NAME); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    rec_w7 = {'this_sha256': H.digest(os.path.abspath(__file__)), 'w1a_sha256': W1A_SHA256, 'build_sub_sha256': BUILD_SUB_SHA256,
              'read_nb_sha256': READ_NB_SHA256, 'essay_sha256': ESSAY_SHA256, 'module_sha256': MODULE_SHA256, 'build1_nb_sha256': BUILD1_NB_SHA256,
              'reference_cells_verified': refgot, 'caps': {'stage_s': STAGE_S, 'build_wall_s': BUILD_WALL_S, 'build_cpu_s': BUILD_CPU_S,
              'read_wall_s': READ_WALL_S, 'read_cpu_s': READ_CPU_S, 'group_rss_stop_bytes': GROUP_RSS_STOP, 'swap_growth_bytes': SWAP_GROWTH,
              'artifacts_max_bytes': ARTIFACTS_MAX, 'notebook_max_bytes': NOTEBOOK_MAX_BYTES}, 'nice_inherited': os.nice(0),
              'paths': {'pipeline': pipe, 'kit': kit, 'out': out, 'notebook_out': nb_out, 'notebook_final': nb_final}, 'owned': {}}
    owned = Owned(rec_w7['owned']); owned.install()
    sup = None; R = None; code = [1]

    def persist():
        if sup is not None:
            sup.save()
        else:
            H.atomic_json(os.path.join(out, 'receipts.json'), {'w7': rec_w7, 'complete': False})

    def stop(msg, c=1):
        if R is not None: R['stopped'] = msg
        else: rec_w7['stopped'] = msg
        persist(); print('STOP:', msg); code[0] = c; raise SystemExit(c)

    watcher = None
    try:
        try:
            H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = GROUP_RSS_STOP; H.CAPS['swap_growth_bytes'] = SWAP_GROWTH; H.CAPS['artifacts_max_bytes'] = ARTIFACTS_MAX
            memsize = int(H.checked(['sysctl', '-n', 'hw.memsize']).strip()); rec_w7['hw_memsize_bytes'] = memsize
            if GROUP_RSS_STOP * 2 >= memsize: stop('group RSS stop is not strictly below half of physical memory')
            sup = H.Supervisor(kit, out); R = sup.receipts; R['w7'] = rec_w7; sup.save()
            commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
            st = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True, timeout=H.CAPS['monitor_timeout_s'])
            if st.returncode != 0: raise H.MonitorError('git status exit %d: %s' % (st.returncode, st.stderr.strip()[:200]))
            status = [l for l in st.stdout.splitlines() if l.strip()]
            tracked = [l for l in status if not l.startswith('??')]
            tracked_other = [l for l in tracked if l[3:].strip() != 'Rule30Submission.lean']
            untracked = [l[3:].strip() for l in status if l.startswith('??')]
            unknown_untracked = [u for u in untracked if u.rstrip('/') not in KNOWN_SUBMISSION_ARTIFACTS]
            got = {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}
            bad = [f for f, want in H.PIN['sources'].items() if got[f] != want]
            R['pins'] = {'commit': commit, 'tracked_changes': tracked, 'tracked_changes_other_than_submission': tracked_other, 'untracked_paths': untracked,
                         'unknown_untracked': unknown_untracked, 'bad_sources': bad, 'deps_built': {d: os.path.exists(os.path.join(kit, d)) for d in H.DEPS},
                         'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip()}
            sup.save()
            if commit != H.PIN['commit'] or tracked_other or unknown_untracked or bad or not all(R['pins']['deps_built'].values()) or R['pins']['toolchain'] != H.PIN['toolchain']:
                stop('pin mismatch or unknown input: %s' % {k: R['pins'][k] for k in ('commit', 'tracked_changes_other_than_submission', 'unknown_untracked', 'bad_sources', 'toolchain')})
            if H.pressure_bad(sup.baseline): stop('pressure at launch')
            r = sup.register(H.preflight())
            if r['verdict'] != 'pass': stop('preflight failed')
        except SystemExit:
            raise
        except Interrupted as e:
            stop('interrupted in setup: %s' % e, 130)
        except BaseException as e:
            stop('setup exception: %r' % e)
        try:
            watcher = Watcher(owned, nb_out, NOTEBOOK_MAX_BYTES); watcher.start()
            t_build = time.time()
            rb = sup.run_step('build_notebook', ['wolframscript', '-file', bs, NAME, nb_out], pipe, BUILD_WALL_S, BUILD_CPU_S, m_build)
            rec_w7['watcher'] = {'stop_reason': owned.stop_reason, 'notebook_peak_bytes_sampled': watcher.peak_nb}
            ok_fresh, fresh = fresh_output(nb_out, t_build, BUILD1_NB_SHA256, NOTEBOOK_MAX_BYTES)
            rec_w7['fresh_output'] = fresh; sup.save()
            if owned.stop_reason: stop('watcher stop: %s' % owned.stop_reason)
            if rb['verdict'] != 'pass': stop('build: %s (%s) %s' % (rb['verdict'], rb['reason'], rb.get('match_note')))
            if not ok_fresh: stop('fresh-output predicate failed: %s' % fresh)
            cells = os.path.join(out, 'cells')
            rr = sup.run_step('read_cells', ['wolframscript', '-file', rn, NAME, cells, nb_out], pipe, READ_WALL_S, READ_CPU_S, m_read)
            if owned.stop_reason: stop('watcher stop: %s' % owned.stop_reason)
            if rr['verdict'] != 'pass': stop('read: %s (%s) %s' % (rr['verdict'], rr['reason'], rr.get('match_note')))
            gv, greport = cell_gate(cells, ref_dir)
            rec_w7['cell_gate'] = {'verdict': gv, **greport}; sup.save()
            if gv != 'pass': stop('cell gate: %s' % greport['problems'])
            try: m_final = H.metrics(kit)
            except H.MonitorError as e: m_final = {'error': str(e)}
            arts = H.new_artifact_bytes(kit, out, sup.art_baseline)
            _, fresh2 = fresh_output(nb_out, t_build, BUILD1_NB_SHA256, NOTEBOOK_MAX_BYTES)
            predicates = {
                'build_step_cleanup': rb.get('group_members_after') == 0 and rb.get('final_problems') == [],
                'read_step_cleanup': rr.get('group_members_after') == 0 and rr.get('final_problems') == [],
                'watcher_no_stop': owned.stop_reason is None,
                'owned_groups_all_gone': all(v.get('gone') or owned.members(int(g)) == 0 for g, v in rec_w7['owned']['groups'].items()),
                'notebook_fresh_and_unchanged_since_build': ok_fresh and fresh2.get('sha256') == fresh.get('sha256'),
                'essay_unchanged': H.digest(os.path.join(pipe, NAME, 'essay.md')) == ESSAY_SHA256,
                'module_unchanged': H.digest(os.path.join(pipe, NAME, 'Rule30Submission.lean')) == MODULE_SHA256 and H.digest(os.path.join(kit, 'Rule30Submission.lean')) == MODULE_SHA256,
                'reference_still_bound': verify_reference(ref_dir)[0],
                'cell_gate_pass': gv == 'pass',
                'stage_within_deadline': sup.remaining() >= 0,
                'artifacts_within_cap': arts <= H.CAPS['artifacts_max_bytes'],
                'pressure_ok_after': isinstance(m_final, dict) and 'error' not in m_final and not H.pressure_bad(m_final),
                'swap_growth_within_cap': isinstance(m_final, dict) and 'swap_used_bytes' in m_final and m_final['swap_used_bytes'] - sup.baseline['swap_used_bytes'] <= H.CAPS['swap_growth_bytes'],
                'disk_above_floor': isinstance(m_final, dict) and m_final.get('disk_free_bytes', 0) >= H.CAPS['disk_free_min_bytes'],
            }
            R['final'] = {'predicates': predicates, 'values': {'notebook': fresh2, 'artifact_bytes': arts, 'metrics_after': m_final, 'stage_remaining_s': round(sup.remaining(), 1)}}
            sup.save()
            if not all(predicates.values()): stop('final validation failed: %s' % [k for k, v in predicates.items() if not v])
            if os.path.exists(nb_final): stop('the submit copy target appeared during the stage')
            shutil.copy2(nb_out, nb_final)
            if H.digest(nb_final) != fresh2['sha256']: stop('the submit copy digest differs')
            R['final']['values']['submit_copy'] = {'path_is_pipeline_essay_nb': True, 'sha256': H.digest(nb_final)}
        except SystemExit:
            raise
        except Interrupted as e:
            stop('interrupted: %s' % e, 130)
        except BaseException as e:
            if R is not None: R['post_setup_exception'] = repr(e)
            stop('post-setup exception: %r' % e)
        R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save(); code[0] = 0
        print('DONE: width-60 notebook built, read in full and gated here (not submitted); notebook sha256', fresh2.get('sha256'))
    except SystemExit:
        pass
    finally:
        # one owned-child finalization on every exit path; repeated signals are deferred by the handler
        try:
            if watcher is not None: watcher.stop_flag.set(); watcher.join(2)
            left = owned.kill_all('finalization') if rec_w7['owned']['groups'] else 0
            rec_w7['owned']['finalization_members_left'] = left
            if left is None or left:
                if R is not None: R['complete'] = False
                rec_w7['owned']['verdict'] = 'UNKNOWN: owned members left or unverifiable'
                if code[0] == 0: code[0] = 1
            persist()
        except BaseException as e:
            rec_w7['owned']['finalization_error'] = repr(e)
            try: persist()
            except BaseException: pass
            if code[0] == 0: code[0] = 1
    sys.exit(code[0])


if __name__ == '__main__':
    main()
