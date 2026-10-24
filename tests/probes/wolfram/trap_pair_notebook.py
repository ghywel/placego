#!/usr/bin/env python3
"""trap-pair notebook, revision 1 (Local, 2026-10-24, L926): the pipeline's notebook build and full-cell read for the submission
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
Controls (`--controls`): the build matcher on RESULT OK (pass) and on RESULT FAIL, a missing result line and a nonzero exit (FAIL); the
read matcher on a cell count (pass) and on its absence (FAIL); the four digest gates against one-byte changes.
Usage: python3 trap_pair_notebook.py PIPELINE_DIR REPO_DIR OUT_DIR   |   python3 trap_pair_notebook.py --controls
"""
import json, os, shutil, signal, subprocess, sys, time

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


def build_matcher(rc, text):
    try:
        if rc != 0: return 'FAIL', 'build exit %d' % rc
        if 'RESULT FAIL' in text: return 'FAIL', 'RESULT FAIL in the build output'
        if not any(l.strip() == 'RESULT OK' for l in text.splitlines()): return 'FAIL', 'no RESULT OK line'
        return 'pass', 'RESULT OK'
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


def read_matcher(rc, text):
    try:
        if rc != 0: return 'FAIL', 'read exit %d' % rc
        if not any(l.startswith('output cells: ') for l in text.splitlines()): return 'FAIL', 'no cell count'
        return 'pass', [l for l in text.splitlines() if l.startswith('output cells: ')][-1]
    except Exception as e:
        return 'FAIL', 'matcher exception: %r' % e


def kit_state(kit):
    st = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True, timeout=H.CAPS['monitor_timeout_s'])
    if st.returncode != 0: raise H.MonitorError('git status exit %d' % st.returncode)
    return {'commit': H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip(), 'status': sorted(l for l in st.stdout.splitlines() if l.strip()),
            'sources': {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}, 'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip()}


def controls():
    import tempfile
    res = {}
    res['build_ok_passes'] = build_matcher(0, 'notebook path: x\nbuild seconds: 100\nRESULT OK\n')[0] == 'pass'
    res['build_fail_line_fails'] = build_matcher(0, 'RESULT FAIL conversion failed\n')[0] == 'FAIL'
    res['build_no_result_fails'] = build_matcher(0, 'build seconds: 100\n')[0] == 'FAIL'
    res['build_nonzero_exit_fails'] = build_matcher(1, 'RESULT OK\n')[0] == 'FAIL'
    res['read_count_passes'] = read_matcher(0, 'output cells: 9  written to x\n')[0] == 'pass'
    res['read_no_count_fails'] = read_matcher(0, 'NOT A NOTEBOOK\n')[0] == 'FAIL'
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
    try:
        before = kit_state(kit); R['kit_before'] = before; sup.save()
        tracked_other = [l for l in before['status'] if not l.startswith('??') and l[3:].strip() != 'Rule30Submission.lean']
        if before['commit'] != H.PIN['commit'] or before['toolchain'] != H.PIN['toolchain'] or tracked_other or any(before['sources'][f] != w for f, w in H.PIN['sources'].items()):
            stop('kit pin mismatch')
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
        rb = sup.run_step('build_notebook', ['wolframscript', '-file', 'build_sub.wl', NAME, nb_out], pipe, BUILD_WALL_S, BUILD_CPU_S, build_matcher)
        if rb['verdict'] != 'pass': stop('build: %s (%s) %s' % (rb['verdict'], rb['reason'], rb.get('match_note')))
        if not (os.path.exists(nb_out) and os.path.getmtime(nb_out) >= t0 - 1): stop('no fresh notebook')
        nb_bytes = os.path.getsize(nb_out); nb_sha = H.digest(nb_out)
        if nb_bytes > NOTEBOOK_MAX_BYTES: stop('notebook above 8 MiB')
        shutil.copy2(nb_out, os.path.join(pipe, NAME, 'essay.nb'))
        if H.digest(os.path.join(pipe, NAME, 'essay.nb')) != nb_sha: stop('notebook copy digest differs')
        R['notebook'] = {'bytes': nb_bytes, 'sha256': nb_sha}; sup.save()
        rr = sup.run_step('read_cells', ['wolframscript', '-file', 'read_nb_full.wl', NAME, os.path.join(out, 'cells')], pipe, READ_WALL_S, READ_CPU_S, read_matcher)
        if rr['verdict'] != 'pass': stop('read: %s (%s) %s' % (rr['verdict'], rr['reason'], rr.get('match_note')))
        after = kit_state(kit)
        try: m_final = H.metrics(kit)
        except H.MonitorError as e: m_final = {'error': str(e)}
        arts = H.new_artifact_bytes(kit, out, sup.art_baseline)
        predicates = {
            'kit_unchanged': after == before,
            'staged_sources_unchanged': all(H.digest(os.path.join(pipe, NAME, k)) == w for k, (p, w) in src.items()),
            'cells_written': os.path.exists(os.path.join(out, 'cells', 'count.txt')),
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
    except BaseException as e:
        R['stopped'] = 'exception: %r' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    finally:
        R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: the trap-pair notebook built and its cells read (not submitted)')


if __name__ == '__main__':
    main()
