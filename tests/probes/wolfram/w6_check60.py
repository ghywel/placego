#!/usr/bin/env python3
"""W6, revision 1 (for GPT's read): the supervised local build and check of the width-60 single-module submission
(reports/wolfram-agents/submissions/d-exact-60/Rule30Submission.lean, 4,096 kernel-decided chunk checks, the wrapper,
the witness, `death_time_60_exact`) in the kit copy used by the submission pipeline, under the unchanged W1A supervisor
(3f908914…) with an explicit resource envelope (GC1750 asked for one before this build): stage 3,600 s (two steps,
each at most 1,800 s wall and 1,800 s CPU: the build, predicted about 20 minutes from W5's 64 modules at 19.4 s, and
the kit's checker replaying about 8,500 constants, predicted 15 to 20 minutes from the width-56 checker's 4 minutes
for 2,130); group RSS stop 6 GiB; pressure >= 2 with the free-percent fallback; swap growth 256 MiB; disk 5 GiB; new
artifacts 512 MiB; log 10 MiB; one Lean worker; no retry; no other job. Pins: the kit copy at cc1e0e0 with the seven
pinned sources and deps built (untracked submission files allowed, their names recorded); the module's sha256
recorded and compared to the committed one. NOT an agreed job until GPT accepts this exact file; nothing runs on
import; the submission itself follows only on a pass, by the pipeline, on the owner's express permission.

Usage: python3 w6_check60.py KIT_COPY MODULE.lean OUT_DIR
Verdict: pass when both steps pass with the checker's headline `Rule30Submission.death_time_60_exact` found and ok,
standard axioms, newAxioms [], replay ok; the check JSON is copied to OUT_DIR/check.json.
"""
import json, os, shutil, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

STAGE_S, STEP_WALL_S, STEP_CPU_S = 3600, 1800, 1800
HEADLINES = ['Rule30Submission.death_time_60_exact', 'Rule30Submission.q01_width_le_60']


def m_checker60(rc, text):
    try:
        d = json.loads([l for l in text.splitlines() if l.startswith('{')][-1])
    except Exception as e:
        return 'FAIL', 'no JSON: %r' % e
    hs = d.get('headlines') or []
    ok = d.get('verdict') == 'pass' and d.get('newAxioms') == [] and (d.get('replay') or {}).get('ok') and len(hs) == 2 and all(h.get('found') and h.get('ok') and set(h.get('axioms', [])) <= H.STD_AXIOMS for h in hs)
    return ('pass' if ok else 'FAIL'), json.dumps({k: d.get(k) for k in ('verdict', 'newAxioms', 'replay')} | {'headlines': [(h.get('name'), h.get('ok')) for h in hs], 'declared': len(d.get('declared', []))})


def main():
    H.CAPS['stage_s'] = STAGE_S
    kit, mod, out = (os.path.abspath(a) for a in sys.argv[1:4])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    sup = H.Supervisor(kit, out); R = sup.receipts
    R['w6'] = {'module_sha256': H.digest(mod), 'module_bytes': os.path.getsize(mod), 'this_sha256': H.digest(os.path.abspath(__file__)), 'caps': {'stage_s': STAGE_S, 'step_wall_s': STEP_WALL_S, 'step_cpu_s': STEP_CPU_S}}

    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    commit = H.checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    status = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip().splitlines()
    tracked_changed = [l for l in status if not l.startswith('??') and 'Rule30Submission.lean' not in l]
    got = {f: H.digest(os.path.join(kit, f)) for f in H.PIN['sources']}
    bad = [f for f, want in H.PIN['sources'].items() if got[f] != want]
    R['pins'] = {'commit': commit, 'tracked_changed_other_than_submission': tracked_changed, 'untracked_count': len([l for l in status if l.startswith('??')]), 'bad_sources': bad,
                 'deps_built': {d: os.path.exists(os.path.join(kit, d)) for d in H.DEPS}, 'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip()}
    sup.save()
    if commit != H.PIN['commit'] or tracked_changed or bad or not all(R['pins']['deps_built'].values()) or R['pins']['toolchain'] != H.PIN['toolchain']:
        stop('pin mismatch: %s' % R['pins'])
    if H.pressure_bad(sup.baseline): stop('pressure at launch')
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass': stop('preflight failed')
    shutil.copy2(mod, os.path.join(kit, 'Rule30Submission.lean'))
    for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
        p = os.path.join(kit, '.lake/build/lib/lean/Rule30Submission' + ext)
        if os.path.exists(p): os.remove(p)
    sup.art_baseline = H.snapshot(kit, out)
    r = sup.run_step('build_Rule30Submission', ['lake', 'build', 'Rule30Submission'], kit, STEP_WALL_S, STEP_CPU_S, H.m_pass)
    olean = os.path.join(kit, '.lake/build/lib/lean/Rule30Submission.olean')
    r['olean'] = {'exists_after': os.path.exists(olean), 'sha256': H.digest(olean) if os.path.exists(olean) else None, 'bytes': os.path.getsize(olean) if os.path.exists(olean) else None}
    sup.save()
    if r['verdict'] != 'pass' or not r['olean']['exists_after']: stop('build: %s (%s)' % (r['verdict'], r['reason']))
    cmd = ['lake', 'env', 'lean', '--run', 'Check.lean', 'Rule30Submission', '--claim', 'partial'] + sum([['--headline', h] for h in HEADLINES], [])
    r = sup.run_step('checker', cmd, kit, STEP_WALL_S, STEP_CPU_S, m_checker60)
    if r['verdict'] != 'pass': stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note')))
    text = open(os.path.join(out, 'checker.log'), errors='replace').read()
    open(os.path.join(out, 'check.json'), 'w').write([l for l in text.splitlines() if l.startswith('{')][-1] + '\n')
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: width-60 submission module built and checked here (not submitted)')


if __name__ == '__main__':
    main()
