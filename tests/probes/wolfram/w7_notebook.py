#!/usr/bin/env python3
"""W7, revision 1 (2026-10-24, for GPT's GC1762 gates): the width-60 submission notebook build as a stage under the
UNCHANGED W1A supervisor (tests/probes/wolfram/w1a_harness.py, the bytes pinned below), replacing the shell wrapper of
L847. NOT an agreed job until GPT accepts this exact file; nothing runs on import; the submission itself follows only
on a pass, by the pipeline's submit script, on the owner's express permission.

What the stage does, in order:
  pins     the supervisor's bytes, the two pipeline scripts, the staged essay, the module (pipeline copy and the kit's
           installed copy), the build-1 reference cells, the kit copy (commit, toolchain, pinned sources, deps built,
           git status: the only tracked change `Rule30Submission.lean`, untracked paths against the allow-list),
           the machine's physical memory (recorded, and the group RSS stop must be below half of it);
  fresh    `NAME/essay.nb` must NOT exist before the build (the build script refuses too); afterwards it must exist,
           be newer than the step start, and differ from build 1's notebook digest (the prose changed);
  step 1   `/usr/bin/time -l wolframscript -file build_sub.wl NAME` in the pipeline folder, under run_step: own
           session and process group, 1-second samples of the GROUP's aggregate RSS (kernel + lake + lean together),
           live CPU, member and lean counts; stops on group RSS, wall, CPU, stage deadline, memory pressure >= 2,
           swap growth, low disk, log size, artifact growth, more than one lean process; a monitor failure is
           UNKNOWN, never a pass; the leader's exit kills any surviving member and records it (W1A.finalize);
           matcher: exit 0, a `build seconds:` line, a `resource provenance:` line, a `notebook bytes:` line, no
           `RESULT FAIL`, no `$Failed`, and `RESULT OK` as the last non-empty line;
  step 2   `wolframscript -file read_nb_full.wl NAME OUT/cells` under run_step (small caps): every Output cell in full
           InputForm to OUT/cells/cell-NN.txt; matcher: exit 0 and `output cells: 10`;
  gate     the FULL-CELL gate (not a 160-character preview): exactly 10 cells; cells 1, 2, 3, 5, 6, 7, 8, 9 byte-equal to
           build 1's reference; cells 4 and 10 (the LeanEnvironment and Success summary boxes) equal after one
           normalisation, LeanLink's per-run temporary module name `LeanLinkTmp<digits>x<digits>` -> `LeanLinkTmp<id>`,
           AND the semantic predicates: cell 10 carries `TagBox["Success", "SummaryHead"]` and the message `The kernel
           accepts all 8466 declarations of LeanLinkTmp<id>.`; cell 4 carries the LeanEnvironment summary with
           `Constants: ` 4363; cell 1 is {60, 114}; cell 9 is exactly the three standard axioms; cell 8 names the first
           and last chunk checks and ChunksOK 60 115 18 0 4096;
  final    predicates: both steps' cleanup (group empty, no final problems), fresh-output, essay and module unchanged,
           stage deadline, pressure, swap growth, disk, artifact total, notebook size cap; complete only if all hold.
  signals  SIGTERM, SIGINT and SIGHUP to this process raise Interrupted inside run_step's loop, so its `finally` kills
           the owned group and records `exception`; main records `stopped: interrupted` and exits 130. Every
           non-pass outcome exits nonzero (STOP 1, REFUSED 3, interrupted 130).

Envelope (the caps, with the reasons): stage 4,500 s; build step wall 3,600 s and CPU 4,000 s (build 1 took 2,120.8 s wall
on this machine; its CPU was not measured, Lean's share was about 1,170 s in W6 and the kernel's replay is of the same
order); read step 300 s / 300 s; GROUP RSS stop 7 GiB (the machine has 16 GiB physical, hw.memsize 17179869184; build 1's
sampled per-process peaks were 4,209 MiB for lean and 4,277 MiB for the kernel at different times, their simultaneity
unknown, so the group cap is set below half of physical memory and the pressure guard at level 2 stands beside it);
swap growth 1 GiB (two runtimes on 16 GiB; build 1's growth was not measured; W6's was 0); disk floor 5 GiB; artifacts
512 MiB over the kit's build trees and the output folder; the notebook itself at most 8 MiB (build 1: 515,336 bytes); log
10 MiB; one lean process; ordinary priority, the inherited nice recorded; no retry.

Controls (`--controls`, seconds, no production step, one short kernel for the two build-script failure paths):
matcher: RESULT FAIL text fails, missing RESULT OK fails, `$Failed` fails, exit 1 fails, a good log passes;
cell gate: the reference against itself passes; an equal-160-character-prefix but different full cell FAILS; a
missing cell file FAILS; nine cells FAIL; a different LeanLinkTmp id in cells 4 and 10 passes (the normalisation);
`8465 declarations` FAILS; fresh-output: a notebook older than the step start FAILS, a missing one FAILS;
interruption: a stand-in step with a child (`zsh -c 'sleep 60 & sleep 60'`) under run_step, SIGTERM delivered to this
process after 2 s: the step records `exception`, the group is empty afterwards, Interrupted propagates; monitor
failure: FAULTS ps_fail_after = 1 on a `sleep 5` stand-in: reason `monitor-failure`, verdict UNKNOWN, group empty;
build script: a folder without an essay -> exit 1 and RESULT FAIL; a folder whose essay.nb already exists -> exit 1
and RESULT FAIL (the stale-notebook path).

Usage: python3 w7_notebook.py PIPELINE_DIR OUT_DIR      (absolute; OUT_DIR empty or absent)
       python3 w7_notebook.py --controls
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
NOTEBOOK_MAX_BYTES = 8 * H.MIB
EXPECTED_CELLS = 10
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
BUILD_SUB_SHA256 = '83bdcc90a0f348e2e659a1ba11c0353442606366e45344f938e29451448db609'
READ_NB_SHA256 = 'c5b89fb60f57bccee440983eeaaf65edeb37d434cca47025783bf25bd6787f44'
ESSAY_SHA256 = 'd83f1bd06ccb615ec630de427be3e37e331824f3e86ac980347173e4969a419b'
MODULE_SHA256 = 'f53da13f999db822e6f5560bbc7c9f9188c963a4294377e5712c6857633fff04'
BUILD1_NB_SHA256 = 'd02d8cc0a5eaa3e5288c449d97299603cbe45171b2ba46bdc8ebead7b5fdf4d1'
REF_DIGESTS_SHA256 = 'aa5c1203bfa1d2128b666eabc84d39cd90c1f32c63d0eb2163e66ca18f51aaac'   # ref-build1/digests.txt
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


def _raise_interrupted(signum, frame):
    raise Interrupted(signal.Signals(signum).name)


def install_signal_handlers():
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, _raise_interrupted)


# ---- matchers ------------------------------------------------------------------------------------------------------

def m_build(rc, text):
    """exit 0; `build seconds:`, `resource provenance:` and `notebook bytes:` lines present; no RESULT FAIL and no
    $Failed anywhere; RESULT OK is the last non-empty line of the script's own output (the `time -l` block follows it,
    so the check is on the lines before the first `real` line)."""
    try:
        if rc != 0:
            return 'FAIL', 'exit %d' % rc
        lines = [l.rstrip() for l in text.splitlines()]
        own = []
        for l in lines:
            if re.match(r'\s*[\d.]+ real\s+[\d.]+ user\s+[\d.]+ sys', l):
                break
            own.append(l)
        own_ne = [l for l in own if l.strip()]
        problems = []
        if not any(l.startswith('build seconds:') for l in own): problems.append('no build seconds line')
        if not any(l.startswith('resource provenance:') for l in own): problems.append('no resource provenance line')
        if not any(l.startswith('notebook bytes:') for l in own): problems.append('no notebook bytes line')
        if any('RESULT FAIL' in l for l in own): problems.append('RESULT FAIL present')
        if any('$Failed' in l for l in own): problems.append('$Failed present')
        if not own_ne or own_ne[-1].strip() != 'RESULT OK': problems.append('RESULT OK is not the last line')
        prov = [l for l in own if l.startswith('resource provenance:')]
        secs = [l for l in own if l.startswith('build seconds:')]
        note = json.dumps({'provenance': prov[:1], 'build_seconds_line': secs[:1]})
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


# ---- the full-cell gate --------------------------------------------------------------------------------------------

def normalise(i, text):
    return TMP_RE.sub('LeanLinkTmp<id>', text) if i in NORMALISED_CELLS else text


def cell_gate(cells_dir, ref_dir):
    """Returns (verdict, report). Every exception is a FAIL."""
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
            a = open(p, encoding='utf-8').read(); b = open(q, encoding='utf-8').read()
            na, nb = normalise(i, a), normalise(i, b)
            equal = (na == nb)
            per_cell[i] = {'bytes': len(a.encode('utf-8')), 'equal_to_reference': equal, 'normalised': i in NORMALISED_CELLS,
                           'sha256': H.digest(p)}
            if not equal: problems.append('cell %d differs from the reference%s' % (i, ' after normalisation' if i in NORMALISED_CELLS else ''))
            for needle in SEMANTIC.get(i, []):
                if needle not in na: problems.append('cell %d lacks %r' % (i, needle[:60]))
        extra = sorted(f for f in os.listdir(cells_dir) if f.startswith('cell-') and f not in {'cell-%02d.txt' % i for i in range(1, EXPECTED_CELLS + 1)})
        if extra: problems.append('extra cell files %r' % extra)
        return ('pass' if not problems else 'FAIL'), {'problems': problems, 'cells': per_cell, 'count': count}
    except Exception as e:
        return 'FAIL', {'problems': ['gate exception: %r' % e]}


def fresh_output(path, t_start_epoch, old_sha, max_bytes):
    """(ok, record): the file exists, is newer than the step start, differs from the old digest, is within the cap."""
    rec = {'exists': os.path.exists(path)}
    if not rec['exists']:
        return False, rec
    st = os.stat(path)
    rec.update({'mtime_epoch': st.st_mtime, 'newer_than_step_start': st.st_mtime >= t_start_epoch - 1.0, 'bytes': st.st_size,
                'sha256': H.digest(path)})
    rec['differs_from_build1'] = rec['sha256'] != old_sha
    rec['within_size_cap'] = st.st_size <= max_bytes
    return rec['newer_than_step_start'] and rec['differs_from_build1'] and rec['within_size_cap'], rec


# ---- controls ------------------------------------------------------------------------------------------------------

def controls():
    res = {}
    good = 'essay sha256: x\nresource provenance: name MarkdownToNotebook  version 1.0.0\nbuild seconds: 2120.8  result: Shallow[y, 2]\nnotebook bytes: 515336  sha256: z\nRESULT OK\n      2120.0 real      3000.0 user      100.0 sys\n'
    res['good_log_passes'] = m_build(0, good)[0] == 'pass'
    res['result_fail_fails'] = m_build(0, good.replace('RESULT OK', 'RESULT FAIL conversion failed'))[0] == 'FAIL'
    res['missing_result_ok_fails'] = m_build(0, good.replace('RESULT OK\n', ''))[0] == 'FAIL'
    res['dollar_failed_fails'] = m_build(0, good.replace('Shallow[y, 2]', '$Failed'))[0] == 'FAIL'
    res['exit_1_fails'] = m_build(1, good)[0] == 'FAIL'
    res['missing_provenance_fails'] = m_build(0, good.replace('resource provenance: name MarkdownToNotebook  version 1.0.0\n', ''))[0] == 'FAIL'
    res['read_matcher_ten_passes'] = m_read(0, 'output cells: 10  written to x')[0] == 'pass'
    res['read_matcher_nine_fails'] = m_read(0, 'output cells: 9  written to x')[0] == 'FAIL'
    ref = os.path.join(os.environ.get('W7_REF_DIR', ''), '')
    if not (ref and os.path.isdir(ref)):
        res['reference_dir_present'] = False
    else:
        res['reference_dir_present'] = H.digest(os.path.join(ref, 'digests.txt')) == REF_DIGESTS_SHA256
        res['reference_against_itself_passes'] = cell_gate(ref, ref)[0] == 'pass'
        t = tempfile.mkdtemp()
        shutil.copytree(ref, os.path.join(t, 'same'))
        c = os.path.join(t, 'same', 'cell-07.txt'); s = open(c, encoding='utf-8').read()
        open(c, 'w', encoding='utf-8').write(s[:160] + s[160:].replace('114', '116', 1))                     # equal 160-prefix, different full cell
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
        shutil.rmtree(t)
    t = tempfile.mkdtemp(); nb = os.path.join(t, 'essay.nb'); open(nb, 'wb').write(b'x' * 100)
    old = time.time() - 3600; os.utime(nb, (old, old))
    res['stale_notebook_fails'] = fresh_output(nb, time.time(), 'none', NOTEBOOK_MAX_BYTES)[0] is False
    res['missing_notebook_fails'] = fresh_output(os.path.join(t, 'none.nb'), time.time(), 'none', NOTEBOOK_MAX_BYTES)[0] is False
    os.utime(nb, None)
    res['fresh_notebook_passes'] = fresh_output(nb, time.time() - 5, 'none', NOTEBOOK_MAX_BYTES)[0] is True
    res['same_as_build1_fails'] = fresh_output(nb, time.time() - 5, H.digest(nb), NOTEBOOK_MAX_BYTES)[0] is False
    shutil.rmtree(t)
    # interruption with a child, under the real supervisor
    out = tempfile.mkdtemp(); kit = tempfile.mkdtemp()
    H.CAPS['stage_s'] = 120
    install_signal_handlers()
    sup = H.Supervisor(kit, out)
    threading.Timer(2.0, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()
    got = None
    try:
        sup.run_step('interrupt_standin', ['zsh', '-c', 'sleep 60 & sleep 60'], out, 60, 60, H.m_pass)
    except Interrupted as e:
        got = str(e)
    rec = sup.receipts['steps'][-1]
    time.sleep(0.5)
    left = subprocess.run(['pgrep', '-x', 'sleep'], capture_output=True, text=True).stdout.split()
    res['interrupt_raised'] = got == 'SIGTERM'
    res['interrupt_step_recorded_exception'] = rec.get('reason') == 'exception' and rec.get('verdict') == 'UNKNOWN'
    res['interrupt_group_empty_after'] = rec.get('group_members_after') == 0
    res['interrupt_no_sleep_left'] = not any(l for l in left)
    # failed process enumeration
    H.FAULTS['ps_fail_after'] = 1
    sup2 = H.Supervisor(kit, out)
    r2 = sup2.run_step('monitor_failure_standin', ['sleep', '5'], out, 60, 60, H.m_pass)
    H.FAULTS['ps_fail_after'] = None
    res['monitor_failure_is_unknown'] = r2.get('reason') == 'monitor-failure' and r2.get('verdict') == 'UNKNOWN'
    res['monitor_failure_group_cleaned'] = r2.get('group_members_after') == 0 and r2.get('exit') is not None
    shutil.rmtree(out); shutil.rmtree(kit)
    # the build script's two failure paths (one short kernel each)
    bs = os.path.join(PIPE_SCRIPTS, 'build_sub.wl')
    if os.path.exists(bs) and shutil.which('wolframscript'):
        d = tempfile.mkdtemp(); os.makedirs(os.path.join(d, 'noessay'))
        r = subprocess.run(['wolframscript', '-file', bs, 'noessay'], cwd=d, capture_output=True, text=True, timeout=240)
        res['build_script_no_essay_exit1_result_fail'] = r.returncode == 1 and 'RESULT FAIL' in r.stdout
        os.makedirs(os.path.join(d, 'stale')); open(os.path.join(d, 'stale', 'essay.md'), 'w').write('x'); open(os.path.join(d, 'stale', 'essay.nb'), 'w').write('x')
        r = subprocess.run(['wolframscript', '-file', bs, 'stale'], cwd=d, capture_output=True, text=True, timeout=240)
        res['build_script_stale_notebook_exit1_result_fail'] = r.returncode == 1 and 'RESULT FAIL' in r.stdout
        shutil.rmtree(d)
    else:
        res['build_script_controls_ran'] = False
    ok = all(v is True for v in res.values())
    print(json.dumps(res, indent=1)); print('W7 CONTROLS', 'PASS' if ok else 'FAIL'); return ok


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
    for p, want, what in ((bs, BUILD_SUB_SHA256, 'build_sub.wl'), (rn, READ_NB_SHA256, 'read_nb_full.wl'),
                          (os.path.join(pipe, NAME, 'essay.md'), ESSAY_SHA256, 'staged essay'),
                          (os.path.join(pipe, NAME, 'Rule30Submission.lean'), MODULE_SHA256, 'pipeline module copy'),
                          (os.path.join(kit, 'Rule30Submission.lean'), MODULE_SHA256, "the kit's installed module"),
                          (os.path.join(pipe, NAME, 'ref-build1', 'digests.txt'), REF_DIGESTS_SHA256, 'reference digests')):
        if not os.path.exists(p) or H.digest(p) != want:
            print('REFUSED: %s missing or not the pinned bytes' % what); sys.exit(3)
    nb_path = os.path.join(pipe, NAME, 'essay.nb')
    if os.path.exists(nb_path):
        print('REFUSED: %s/essay.nb already exists; the output would not be fresh' % NAME); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    install_signal_handlers()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = GROUP_RSS_STOP; H.CAPS['swap_growth_bytes'] = SWAP_GROWTH
    sup = H.Supervisor(kit, out); R = sup.receipts
    memsize = int(H.checked(['sysctl', '-n', 'hw.memsize']).strip())
    R['w7'] = {'this_sha256': H.digest(os.path.abspath(__file__)), 'w1a_sha256': W1A_SHA256, 'build_sub_sha256': BUILD_SUB_SHA256,
               'read_nb_sha256': READ_NB_SHA256, 'essay_sha256': ESSAY_SHA256, 'module_sha256': MODULE_SHA256, 'build1_nb_sha256': BUILD1_NB_SHA256,
               'ref_digests_sha256': REF_DIGESTS_SHA256, 'caps': {'stage_s': STAGE_S, 'build_wall_s': BUILD_WALL_S, 'build_cpu_s': BUILD_CPU_S,
               'read_wall_s': READ_WALL_S, 'read_cpu_s': READ_CPU_S, 'group_rss_stop_bytes': GROUP_RSS_STOP, 'swap_growth_bytes': SWAP_GROWTH,
               'notebook_max_bytes': NOTEBOOK_MAX_BYTES}, 'hw_memsize_bytes': memsize, 'nice_inherited': os.nice(0), 'paths': {'pipeline': pipe, 'kit': kit, 'out': out}}
    sup.save()

    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    try:
        if GROUP_RSS_STOP * 2 > memsize: stop('group RSS stop is not below half of physical memory')
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
        R['stopped'] = 'interrupted in setup: %s' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(130)
    except BaseException as e:
        R['stopped'] = 'setup exception: %r' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    try:
        t_build = time.time()
        rb = sup.run_step('build_notebook', ['wolframscript', '-file', bs, NAME], pipe, BUILD_WALL_S, BUILD_CPU_S, m_build)
        ok_fresh, fresh = fresh_output(nb_path, t_build, BUILD1_NB_SHA256, NOTEBOOK_MAX_BYTES)
        R['w7']['fresh_output'] = fresh; sup.save()
        if rb['verdict'] != 'pass': stop('build: %s (%s) %s' % (rb['verdict'], rb['reason'], rb.get('match_note')))
        if not ok_fresh: stop('fresh-output predicate failed: %s' % fresh)
        cells = os.path.join(out, 'cells')
        rr = sup.run_step('read_cells', ['wolframscript', '-file', rn, NAME, cells], pipe, READ_WALL_S, READ_CPU_S, m_read)
        if rr['verdict'] != 'pass': stop('read: %s (%s) %s' % (rr['verdict'], rr['reason'], rr.get('match_note')))
        gv, greport = cell_gate(cells, os.path.join(pipe, NAME, 'ref-build1'))
        R['w7']['cell_gate'] = {'verdict': gv, **greport}; sup.save()
        if gv != 'pass': stop('cell gate: %s' % greport['problems'])
        try: m_final = H.metrics(kit)
        except H.MonitorError as e: m_final = {'error': str(e)}
        arts = H.new_artifact_bytes(kit, out, sup.art_baseline)
        _, fresh2 = fresh_output(nb_path, t_build, BUILD1_NB_SHA256, NOTEBOOK_MAX_BYTES)
        predicates = {
            'build_step_cleanup': rb.get('group_members_after') == 0 and rb.get('final_problems') == [],
            'read_step_cleanup': rr.get('group_members_after') == 0 and rr.get('final_problems') == [],
            'notebook_fresh_and_unchanged_since_build': ok_fresh and fresh2.get('sha256') == fresh.get('sha256'),
            'essay_unchanged': H.digest(os.path.join(pipe, NAME, 'essay.md')) == ESSAY_SHA256,
            'module_unchanged': H.digest(os.path.join(pipe, NAME, 'Rule30Submission.lean')) == MODULE_SHA256 and H.digest(os.path.join(kit, 'Rule30Submission.lean')) == MODULE_SHA256,
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
    except SystemExit:
        raise
    except Interrupted as e:
        R['stopped'] = 'interrupted: %s' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(130)
    except BaseException as e:
        R['stopped'] = 'post-setup exception: %r' % e; R['post_setup_exception'] = repr(e); sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: width-60 notebook built, read in full and gated here (not submitted); notebook sha256', fresh.get('sha256'))


if __name__ == '__main__':
    main()
