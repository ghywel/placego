#!/usr/bin/env python3
"""trap-pair Check, revision 1 (Local, 2026-10-24, L924; GPT's GC1831 cap and restoration requirements). The pipeline's required local
build and checker pass of reports/wolfram-agents/submissions/trap-pair/Rule30Submission.lean (sha256 MODULE_SHA256, source PASS in
GC1831) in the pipeline kit copy, under the unchanged W1A supervisor (pinned bytes). NOT an agreed job until GPT accepts this exact file;
nothing runs on import; `--controls` runs the gate and restoration controls only. No notebook build, no submission, no retry.

Envelope (GC1831's proposal, adopted): stage wall 1,200 s; two steps, `lake build Rule30Submission` then the kit's checker, each at most
600 s wall and 600 s child CPU (clamped by the supervisor to the remaining stage time); sampled process-group RSS stop 4 GiB; log 10 MiB;
new artifacts 128 MiB; free disk >= 5 GiB; W1A's pressure stop (level >= 2, free-percent fallback) and 256 MiB swap-growth stop; one Lean
worker; launched at ordinary priority (the inherited nice recorded); one failed step stops the stage.

Bindings: the module's sha256 is compared before anything is copied, again after installation and after the checker; W1A's bytes;
the kit's commit (W1A PIN, cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554), toolchain (leanprover/lean4:v4.35.0) and pinned sources including
Check.lean (W1A PIN); `git status` through W1A's time-bounded runner, the only tracked change allowed being the kit root's
Rule30Submission.lean and the untracked paths limited to the pipeline's known submission copies (KNOWN_SUBMISSION_ARTIFACTS); the
module's dependency objects (DEP_OLEANS: Rule30PeriodTwoSideways and its import chain) must exist before the build and be byte-identical
after it (no unplanned dependency rebuild); the checker runs with exactly the five HEADLINES and --claim partial.
Restoration (GC1831): before mutation, the kit root's Rule30Submission.lean and the Rule30Submission objects are preserved, with digests,
in OUT/preserved-*; a finally path (also reached on SIGTERM, which is turned into an exit) restores them on success, checker failure,
resource stop or interruption, verifies the restored digests, and records `restoration` in the receipt; check.json and the logs are kept in
OUT. The checker gate requires exit 0, the JSON's verdict pass, newAxioms [], replay ok, and exactly the five distinct headline names, each
found, ok, type-matching, on the three standard axioms, with no problems.
Controls (`--controls`): the checker gate on a passing five-name JSON (pass) and on one missing name, a duplicate, a non-standard axiom,
a nonzero exit, malformed and unparseable JSON (each FAIL); the module hash gate against a one-byte change; the restoration path on a
temporary fake kit, both after a normal run and after an exception raised mid-run, must restore the original bytes exactly.
Usage: python3 trap_pair_check.py KIT_COPY MODULE.lean OUT_DIR   |   python3 trap_pair_check.py --controls
"""
import json, os, shutil, signal, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

STAGE_S, STEP_WALL_S, STEP_CPU_S = 1200, 600, 600
RSS_STOP_BYTES, ARTIFACTS_MAX_BYTES, LOG_MAX_BYTES = 4 << 30, 128 << 20, 10 << 20
HEADLINES = ['Rule30Submission.CQ01_R31', 'Rule30Submission.CQ01_R495', 'Rule30Submission.Psi_eq', 'Rule30Submission.u_R31',
             'Rule30Submission.not_move_equivalent']
MODULE_SHA256 = '27f799f47eecf22f138967ac27ccbc14ab0dffb20f55f5dc29be800aa6b44fd6'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
KNOWN_SUBMISSION_ARTIFACTS = {'Rule30Submission.lean', 'Rule30Submission.template.lean', 'Rule30Submission.prev.lean.bak', 'channel-12.lean', 'corollary-f.lean', 'diagonals.lean', 'README.md', 'build_all.sh', 'comparator',
                              'rule-210-two-sided.lean', 'rule-210.lean', 'sturmian-all.lean', 'sturmian.lean', 'theorem-a4.lean', 'white-end.lean', 'words-A.lean', 'words-B.lean'}
DEP_OLEANS = ['lean/.lake/build/lib/lean/Ruliology/CellularAutomata/%s.olean' % m for m in
              ('Rule30PeriodTwoSideways', 'Rule30PeriodTwoCoupled', 'Rule30Ether', 'Rule30ZeroBoundaryBarriers', 'Rule30StripCertificates', 'Rule30Diagonals',
               'Rule30ZeroBoundary', 'Rule30Jen')]
TARGETS = ['.lake/build/lib/lean/Rule30Submission' + ext for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash')]


def checker_gate(rc, text, headlines=HEADLINES):
    """A total gate (W8's, with five names): rc 0; the last JSON line parses to an object; verdict pass; newAxioms []; replay an object with
    ok True; declared a list; exactly the expected distinct headline names, each found, ok and typeMatches True, axioms a list of standard
    axiom names, problems []; any exception is a FAIL."""
    try:
        if rc != 0: return 'FAIL', 'checker exit %d' % rc
        lines = [l for l in text.splitlines() if l.startswith('{')]
        if not lines: return 'FAIL', 'no JSON line'
        try: d = json.loads(lines[-1])
        except Exception as e: return 'FAIL', 'JSON parse: %r' % e
        if not isinstance(d, dict): return 'FAIL', 'JSON is not an object'
        problems = []
        if d.get('verdict') != 'pass': problems.append('verdict %r' % d.get('verdict'))
        if d.get('newAxioms') != []: problems.append('newAxioms %r' % d.get('newAxioms'))
        rep = d.get('replay')
        if not (isinstance(rep, dict) and rep.get('ok') is True): problems.append('replay not an object with ok True')
        dec = d.get('declared')
        if not isinstance(dec, list): problems.append('declared not a list')
        hs = d.get('headlines')
        if not (isinstance(hs, list) and all(isinstance(h, dict) for h in hs)): return 'FAIL', 'malformed headlines field; ' + '; '.join(problems)
        names = []
        for h in hs:
            nm = h.get('name')
            if not isinstance(nm, str): problems.append('a headline without a string name'); continue
            names.append(nm)
            for key in ('found', 'ok', 'typeMatches'):
                if h.get(key) is not True: problems.append('headline %s: %s is not True' % (nm, key))
            ax = h.get('axioms')
            if not (isinstance(ax, list) and all(isinstance(a, str) for a in ax) and set(ax) <= H.STD_AXIOMS): problems.append('headline %s: axioms not standard' % nm)
            if h.get('problems') != []: problems.append('headline %s: problems %r' % (nm, h.get('problems')))
        if sorted(names) != sorted(headlines) or len(set(names)) != len(headlines): problems.append('headline names %r' % names)
        note = json.dumps({'verdict': d.get('verdict'), 'newAxioms': d.get('newAxioms'), 'replay': rep if isinstance(rep, dict) else repr(rep),
                           'headlines': [(h.get('name'), h.get('ok'), h.get('axioms')) for h in hs], 'declared': len(dec) if isinstance(dec, list) else repr(dec)})
        return ('pass' if not problems else 'FAIL'), note if not problems else 'FAIL: %s | %s' % ('; '.join(problems), note)
    except Exception as e:
        return 'FAIL', 'gate exception: %r' % e


def preserve(kit, keep):
    """Copy the kit root's Rule30Submission.lean and the Rule30Submission objects to keep; return {relative path: digest or None}."""
    rec = {}
    for rel in ['Rule30Submission.lean'] + TARGETS:
        p = os.path.join(kit, rel)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(keep, rel.replace('/', '__'))); rec[rel] = H.digest(p)
        else:
            rec[rel] = None
    return rec


def restore(kit, keep, rec):
    """Put every preserved file back (and remove objects that did not exist before); return the verification record."""
    out = {}
    for rel, dg in rec.items():
        p = os.path.join(kit, rel)
        if dg is None:
            if os.path.exists(p): os.remove(p)
            out[rel] = not os.path.exists(p)
        else:
            shutil.copy2(os.path.join(keep, rel.replace('/', '__')), p)
            out[rel] = H.digest(p) == dg
    return out


def controls():
    import tempfile
    base = {'verdict': 'pass', 'newAxioms': [], 'replay': {'constants': 1, 'ok': True}, 'declared': []}
    good = lambda names: json.dumps(base | {'headlines': [{'name': n, 'found': True, 'ok': True, 'typeMatches': True, 'axioms': sorted(H.STD_AXIOMS), 'problems': []} for n in names]})
    res = {}
    res['five_clean_headlines_pass'] = checker_gate(0, good(HEADLINES))[0] == 'pass'
    res['four_headlines_fail'] = checker_gate(0, good(HEADLINES[:4]))[0] == 'FAIL'
    res['duplicate_name_fails'] = checker_gate(0, good(HEADLINES[:4] + [HEADLINES[0]]))[0] == 'FAIL'
    bad_ax = json.loads(good(HEADLINES)); bad_ax['headlines'][2]['axioms'].append('sorryAx'); res['nonstandard_axiom_fails'] = checker_gate(0, json.dumps(bad_ax))[0] == 'FAIL'
    res['nonzero_exit_fails'] = checker_gate(1, good(HEADLINES))[0] == 'FAIL'
    res['malformed_json_fails'] = checker_gate(0, '{"verdict": "pass", "headlines": "oops"}')[0] == 'FAIL'
    res['unparseable_json_fails'] = checker_gate(0, '{not json')[0] == 'FAIL'
    mod = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../reports/wolfram-agents/submissions/trap-pair/Rule30Submission.lean')
    res['module_hash_gate_true_file'] = H.digest(mod) == MODULE_SHA256
    t = tempfile.mkdtemp(); p = os.path.join(t, 'x.lean'); data = open(mod, 'rb').read(); open(p, 'wb').write(data[:-1] + b' ')
    res['module_hash_gate_rejects_one_byte_change'] = H.digest(p) != MODULE_SHA256
    for mode in ('normal', 'exception'):
        kit = tempfile.mkdtemp(); keep = tempfile.mkdtemp()
        os.makedirs(os.path.join(kit, '.lake/build/lib/lean'))
        open(os.path.join(kit, 'Rule30Submission.lean'), 'w').write('-- original\n')
        open(os.path.join(kit, TARGETS[0]), 'wb').write(b'old object')
        before = {rel: (H.digest(os.path.join(kit, rel)) if os.path.exists(os.path.join(kit, rel)) else None) for rel in ['Rule30Submission.lean'] + TARGETS}
        rec = preserve(kit, keep); ver = None
        try:
            shutil.copy2(mod, os.path.join(kit, 'Rule30Submission.lean'))
            for rel in TARGETS: open(os.path.join(kit, rel), 'wb').write(b'new object')
            if mode == 'exception': raise RuntimeError('mid-run failure')
        except RuntimeError:
            pass
        finally:
            ver = restore(kit, keep, rec)
        after = {rel: (H.digest(os.path.join(kit, rel)) if os.path.exists(os.path.join(kit, rel)) else None) for rel in ['Rule30Submission.lean'] + TARGETS}
        res['restoration_exact_after_' + mode] = all(ver.values()) and after == before
    ok = all(res.values())
    print(json.dumps(res, indent=1)); print('TRAP-PAIR CHECK CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def main():
    if sys.argv[1:] == ['--controls']:
        sys.exit(0 if controls() else 1)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = RSS_STOP_BYTES; H.CAPS['artifacts_max_bytes'] = ARTIFACTS_MAX_BYTES; H.CAPS['log_max_bytes'] = LOG_MAX_BYTES
    kit, mod, out = (os.path.realpath(os.path.abspath(a)) for a in sys.argv[1:4])
    if not all(os.path.isabs(a) for a in sys.argv[1:4]): print('REFUSED: all three paths must be absolute'); sys.exit(3)
    if len({kit, os.path.dirname(mod), out}) != 3 or out.startswith(kit + os.sep) or mod.startswith(kit + os.sep):
        print('REFUSED: the kit, the module and the output must be distinct and outside one another'); sys.exit(3)
    if os.path.exists(out) and os.listdir(out): print('REFUSED: output folder exists and is not empty'); sys.exit(3)
    if H.digest(mod) != MODULE_SHA256: print('REFUSED: the module is not the reviewed source (sha256 differs)'); sys.exit(3)
    if H.digest(H.__file__) != W1A_SHA256: print('REFUSED: the imported W1A supervisor is not the pinned bytes'); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['trap_pair'] = {'module_sha256': MODULE_SHA256, 'w1a_sha256': W1A_SHA256, 'this_sha256': H.digest(os.path.abspath(__file__)), 'headlines': HEADLINES,
                      'caps': {'stage_s': STAGE_S, 'step_wall_s': STEP_WALL_S, 'step_cpu_s': STEP_CPU_S, 'rss_stop_bytes': RSS_STOP_BYTES,
                               'artifacts_max_bytes': ARTIFACTS_MAX_BYTES, 'log_max_bytes': LOG_MAX_BYTES}, 'nice_inherited': os.nice(0)}
    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)
    def on_term(signum, frame):
        raise SystemExit('SIGTERM')
    signal.signal(signal.SIGTERM, on_term)
    try:
        commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
        st = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True, timeout=H.CAPS['monitor_timeout_s'])
        if st.returncode != 0: raise H.MonitorError('git status exit %d' % st.returncode)
        status = [l for l in st.stdout.splitlines() if l.strip()]
        tracked_other = [l for l in status if not l.startswith('??') and l[3:].strip() != 'Rule30Submission.lean']
        untracked = [l[3:].strip() for l in status if l.startswith('??')]
        unknown_untracked = [u for u in untracked if u.rstrip('/') not in KNOWN_SUBMISSION_ARTIFACTS]
        bad = [f for f, want in H.PIN['sources'].items() if H.digest(os.path.join(kit, f)) != want]
        deps_before = {d: (H.digest(os.path.join(kit, d)) if os.path.exists(os.path.join(kit, d)) else None) for d in DEP_OLEANS}
        R['pins'] = {'commit': commit, 'tracked_changes_other_than_submission': tracked_other, 'untracked_paths': untracked, 'unknown_untracked': unknown_untracked,
                     'bad_sources': bad, 'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip(), 'dep_oleans_before': deps_before}
        sup.save()
        if (commit != H.PIN['commit'] or tracked_other or unknown_untracked or bad or R['pins']['toolchain'] != H.PIN['toolchain']
                or any(v is None for v in deps_before.values())):
            stop('pin mismatch, unknown input or missing dependency object')
        if H.pressure_bad(sup.baseline): stop('pressure at launch')
        r = sup.register(H.preflight())
        if r['verdict'] != 'pass': stop('preflight failed')
    except SystemExit:
        raise
    except BaseException as e:
        R['stopped'] = 'setup exception: %r' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    keep = os.path.join(out, 'preserved-' + time.strftime('%Y%m%d-%H%M%S')); os.makedirs(keep)
    baseline = {p: n for p, n in H.snapshot(kit, out).items() if not p.startswith(out + os.sep)}
    rec = preserve(kit, keep); R['trap_pair']['preserved'] = rec; sup.save()
    try:
        shutil.copy2(mod, os.path.join(kit, 'Rule30Submission.lean'))
        if H.digest(os.path.join(kit, 'Rule30Submission.lean')) != MODULE_SHA256: stop('installed module digest differs')
        for rel in TARGETS:
            p = os.path.join(kit, rel)
            if os.path.exists(p): os.remove(p); baseline.pop(p, None)
        sup.art_baseline = baseline; sup.save()
        rb = sup.run_step('build_Rule30Submission', ['lake', 'build', 'Rule30Submission'], kit, STEP_WALL_S, STEP_CPU_S, H.m_pass)
        olean = os.path.join(kit, TARGETS[0])
        rb['olean'] = {'exists_after': os.path.exists(olean), 'sha256': H.digest(olean) if os.path.exists(olean) else None}
        sup.save()
        if rb['verdict'] != 'pass' or not rb['olean']['exists_after']: stop('build: %s (%s)' % (rb['verdict'], rb['reason']))
        cmd = ['lake', 'env', 'lean', '--run', 'Check.lean', 'Rule30Submission', '--claim', 'partial'] + sum([['--headline', h] for h in HEADLINES], [])
        r = sup.run_step('checker', cmd, kit, STEP_WALL_S, STEP_CPU_S, checker_gate)
        if r['verdict'] != 'pass': stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note')))
        text = open(os.path.join(out, 'checker.log'), errors='replace').read()
        open(os.path.join(out, 'check.json'), 'w').write([l for l in text.splitlines() if l.startswith('{')][-1] + '\n')
        try: m_final = H.metrics(kit)
        except H.MonitorError as e: m_final = {'error': str(e)}
        arts = H.new_artifact_bytes(kit, out, sup.art_baseline)
        deps_after = {d: (H.digest(os.path.join(kit, d)) if os.path.exists(os.path.join(kit, d)) else None) for d in DEP_OLEANS}
        predicates = {
            'module_unchanged_after_checker': H.digest(os.path.join(kit, 'Rule30Submission.lean')) == MODULE_SHA256,
            'object_unchanged_after_checker': (H.digest(olean) if os.path.exists(olean) else None) == rb['olean']['sha256'],
            'dependencies_not_rebuilt': deps_after == deps_before,
            'build_step_cleanup': rb.get('group_members_after') == 0 and rb.get('final_problems') == [],
            'checker_step_cleanup': r.get('group_members_after') == 0 and r.get('final_problems') == [],
            'stage_within_deadline': sup.remaining() >= 0,
            'artifacts_within_cap': arts <= ARTIFACTS_MAX_BYTES,
            'pressure_ok_after': isinstance(m_final, dict) and 'error' not in m_final and not H.pressure_bad(m_final),
            'swap_growth_within_cap': isinstance(m_final, dict) and 'swap_used_bytes' in m_final and m_final['swap_used_bytes'] - sup.baseline['swap_used_bytes'] <= H.CAPS['swap_growth_bytes'],
            'disk_above_floor': isinstance(m_final, dict) and m_final.get('disk_free_bytes', 0) >= H.CAPS['disk_free_min_bytes'],
        }
        R['final'] = {'predicates': predicates, 'values': {'artifact_bytes': arts, 'metrics_after': m_final, 'stage_remaining_s': round(sup.remaining(), 1)}}
        sup.save()
        if not all(predicates.values()): stop('final validation failed: %s' % [k for k, v in predicates.items() if not v])
        R['complete'] = True
    except SystemExit:
        raise
    except BaseException as e:
        R['stopped'] = 'post-setup exception: %r' % e; sup.save(); print('STOP:', R['stopped']); sys.exit(1)
    finally:
        try:
            ver = restore(kit, keep, rec); R['restoration'] = {'verified': ver, 'all_restored': all(ver.values())}
        except BaseException as e:
            R['restoration'] = {'error': repr(e), 'all_restored': False}
        if not R['restoration'].get('all_restored'): R['complete'] = False     # a passing check with an unrestored kit is not complete
        R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    if not R['restoration'].get('all_restored'): print('STOP: restoration failed'); sys.exit(1)
    print('DONE: trap-pair built and checked here (not submitted); the kit copy restored')


if __name__ == '__main__':
    main()
