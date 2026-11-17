#!/usr/bin/env python3
"""Harmless fault tests of the W1A supervisor (tests/probes/wolfram/w1a_harness.py, revision 4), the focused cases
GPT asked for in GPT-L783-HARNESS-REVIEW.md plus the revision-3 set, re-run against the new lifecycle. No Lean, no
kit module, no benchmark: tiny shell and Python children with tiny caps, and synthetic receipts through the terminal
policy where burning CPU would be pointless. Each expectation is declared here before it runs; results go to
OUT_DIR/faults.json. Every case that promises a persisted receipt READS receipts.json to check it.

Usage:  python3 w1a_faults.py OUT_DIR

  F1  wall cap: `sleep 20`, 2 s cap                   -> UNKNOWN/wall-cap persisted; group gone
  F2  RSS stop: a child holding 300 MiB, stop 100 MiB   -> UNKNOWN/rss-stop
  F3  monitor failure: ps fails from sample 2            -> UNKNOWN/monitor-failure persisted; child killed
  F4  exception after 2 samples                          -> exception propagates; the PERSISTED step says
                                                            verdict UNKNOWN, reason exception; child killed
  F5  log burst then sleep, 1 MiB cap                    -> UNKNOWN/log-cap (running guard)
  F6  non-empty output folder                            -> main refuses, exit 3
  F7  cost-miss gate on synthetic receipts               -> 70 s miss; 4.6 GiB miss; 30 s/3 GiB no miss
  F8  engines agree; K(2) = 7
  F9  checker parser: good / missing headline / extra axiom -> pass / FAIL / FAIL
  F10 a sample failure injected after the child exits    -> pass/completed, late error recorded (scope: the completed
                                                            race only; not recovery from a failed live sample)
  F11 matchers: real neg_w2 diagnostic / import error    -> pass / FAIL
  F12 TERMINAL: successful exit, synthetic over-cap final CPU (user+sys 200 s, cap 150 s) -> UNKNOWN/cpu-cap-final
  F13 TERMINAL: successful exit, missing time -l accounting -> UNKNOWN/missing-accounting:…
  F14 TERMINAL: log burst (12 MiB) then IMMEDIATE exit, 1 MiB cap -> UNKNOWN/log-cap-final even if no sample saw it
  F15 TERMINAL: leader exits while an owned child remains (`sh -c 'sleep 20 & exit 0'`) -> orphan killed,
                                                            UNKNOWN/cleanup-orphans, group gone afterwards
  F16 expired stage deadline                             -> run_step refuses to spawn: UNKNOWN/stage-deadline, no child
  F17 pins: a modified tracked file in a throwaway clone of the clone -> main stops with 'pin mismatch' (dirty tree)
  F18 the harness digest is in the receipt and matches the file

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import json, os, shutil, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H

KIT = os.path.expanduser('~/np-scratch-int/wolfram-agents/width/kit-w1a')


def fresh(out, name):
    d = os.path.join(out, name); os.makedirs(d, exist_ok=True); return d


def persisted(sup, step):
    d = json.load(open(os.path.join(sup.out, 'receipts.json')))
    return [s for s in d['steps'] if s.get('step') == step]


def gone(pattern):
    return subprocess.run(['pgrep', '-f', pattern], capture_output=True).returncode != 0


def main():
    out = os.path.abspath(sys.argv[1]); os.makedirs(out, exist_ok=True)
    PY = sys.executable; R = {}

    def sup(name):
        H.FAULTS.update({'ps_fail_after': None, 'raise_after': None, 'rss_stop_bytes': None, 'log_max_bytes': None})
        return H.Supervisor(KIT, fresh(out, name))

    s = sup('F1'); r = s.run_step('f1', ['sleep', '20'], out, 2, 30, H.m_pass); p = persisted(s, 'f1')
    R['F1_wall_cap'] = {'expected': 'UNKNOWN/wall-cap persisted, group gone', 'got': (r['verdict'], r['reason']), 'persisted': len(p) == 1 and p[0]['verdict'] == 'UNKNOWN',
                        'members_after': r.get('group_members_after'),
                        'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'wall-cap') and len(p) == 1 and p[0]['reason'] == 'wall-cap' and r.get('group_members_after') == 0}

    s = sup('F2'); H.FAULTS['rss_stop_bytes'] = 100 << 20
    r = s.run_step('f2', [PY, '-c', 'import time; b = bytearray(300 << 20); time.sleep(20)'], out, 30, 30, H.m_pass)
    R['F2_rss_stop'] = {'expected': 'UNKNOWN/rss-stop', 'got': (r['verdict'], r['reason']), 'peak_MiB': r['sampled_group_rss_peak_bytes'] >> 20,
                        'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'rss-stop')}

    s = sup('F3'); H.FAULTS['ps_fail_after'] = 2
    r = s.run_step('f3', ['sleep', '20'], out, 30, 30, H.m_pass); H.FAULTS['ps_fail_after'] = None; p = persisted(s, 'f3')
    R['F3_monitor_failure'] = {'expected': 'UNKNOWN/monitor-failure persisted, child killed', 'got': (r['verdict'], r['reason']), 'persisted_reason': p[0]['reason'] if p else None,
                               'child_gone': gone('^sleep 20$'), 'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'monitor-failure') and p and p[0]['reason'] == 'monitor-failure' and gone('^sleep 20$')}

    s = sup('F4'); H.FAULTS['raise_after'] = 2; raised = False
    try:
        s.run_step('f4', ['sleep', '20'], out, 30, 30, H.m_pass)
    except RuntimeError as e:
        raised = 'injected' in str(e)
    H.FAULTS['raise_after'] = None; time.sleep(0.5); p = persisted(s, 'f4')
    R['F4_exception_persisted'] = {'expected': 'raised; persisted step UNKNOWN/exception; child gone', 'raised': raised,
                                   'persisted': (p[0]['verdict'], p[0]['reason'], 'exception' in p[0]) if p else None, 'child_gone': gone('^sleep 20$'),
                                   'pass': raised and len(p) == 1 and p[0]['verdict'] == 'UNKNOWN' and p[0]['reason'] == 'exception' and gone('^sleep 20$')}

    s = sup('F5'); H.FAULTS['log_max_bytes'] = 1 << 20
    r = s.run_step('f5', [PY, '-c', "import sys\nfor i in range(12): sys.stdout.write('x' * (1 << 20)); sys.stdout.flush()\nimport time; time.sleep(20)"], out, 30, 30, H.m_pass)
    H.FAULTS['log_max_bytes'] = None
    R['F5_log_cap_running'] = {'expected': 'UNKNOWN/log-cap', 'got': (r['verdict'], r['reason']), 'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'log-cap')}

    d = fresh(out, 'F6'); open(os.path.join(d, 'old.txt'), 'w').write('x')
    pr = subprocess.run([PY, H.__file__, KIT, d], capture_output=True, text=True)
    R['F6_fresh_output'] = {'expected': 'refused, exit 3', 'exit': pr.returncode, 'pass': pr.returncode == 3 and 'REFUSED' in pr.stdout}

    g = H.GIB
    R['F7_cost_miss_gate'] = {'expected': 'miss, miss, no miss',
                              'got': [H.cost_miss({'wall_s': 70, 'sampled_group_rss_peak_bytes': g, 'time_l_max_rss_bytes': g}),
                                      H.cost_miss({'wall_s': 10, 'sampled_group_rss_peak_bytes': int(4.6 * g), 'time_l_max_rss_bytes': g}),
                                      H.cost_miss({'wall_s': 30, 'sampled_group_rss_peak_bytes': 3 * g, 'time_l_max_rss_bytes': 3 * g})]}
    R['F7_cost_miss_gate']['pass'] = R['F7_cost_miss_gate']['got'] == [True, True, False]

    r, K4 = H.engines_control()
    R['F8_engines'] = {'expected': 'all checks true, K2 = 7', 'checks': r['checks'], 'K': r['K_scalar'], 'pass': r['verdict'] == 'pass'}

    good = json.dumps({'verdict': 'pass', 'replay': {'ok': True, 'constants': 1}, 'newAxioms': [],
                       'headlines': [{'name': H.HEADLINE, 'found': True, 'ok': True, 'axioms': ['propext', 'Classical.choice', 'Quot.sound']}]})
    nohead = json.dumps({'verdict': 'pass', 'replay': {'ok': True}, 'newAxioms': [], 'headlines': []})
    extra = good.replace('"Quot.sound"]', '"Quot.sound", "myAxiom"]')
    got = [H.m_checker(0, 'noise\n' + good)[0], H.m_checker(0, nohead)[0], H.m_checker(0, extra)[0]]
    R['F9_checker_parser'] = {'expected': 'pass, FAIL, FAIL', 'got': got, 'pass': got == ['pass', 'FAIL', 'FAIL']}

    s = sup('F10'); H.FAULTS['ps_fail_after'] = 3
    r = s.run_step('f10', ['sleep', '1'], out, 30, 30, H.m_pass); H.FAULTS['ps_fail_after'] = None
    R['F10_completed_race'] = {'expected': 'pass/completed (scope: a failure injected after the child exits; not recovery from a failed live sample)',
                               'got': (r['verdict'], r['reason']), 'late_error_recorded': 'late_sample_error_ignored' in r,
                               'pass': (r['verdict'], r['reason']) == ('pass', 'completed')}

    real = "neg_w2.lean:4:37: error: Tactic `decide` proved that the proposition\n  check 2 6 1 0 = true\nis false\n"
    unrelated = "neg_w2.lean:1:0: error: unknown module prefix 'Ruliology'\n"
    got = [H.m_neg_w2(1, real)[0], H.m_neg_w2(1, unrelated)[0]]
    R['F11_matchers'] = {'expected': 'pass, FAIL', 'got': got, 'pass': got == ['pass', 'FAIL']}

    # F12, F13: the terminal policy on synthetic completed receipts (no CPU burnt)
    s = sup('F12')
    base = {'step': 'syn', 'reason': 'completed', 'proof_verdict': 'pass', 'wall_s': 10.0, 'wall_cap_s': 180, 'time_l_real_s': 10.0,
            'time_l_user_s': 150.0, 'time_l_sys_s': 50.0, 'time_l_max_rss_bytes': 1 << 30, 'sampled_group_rss_peak_bytes': 1 << 30,
            'log_bytes': 100, 'metrics_after': dict(s.baseline)}
    rec = s.register(dict(base)); ok = s.finalize(rec, 150, H.CAPS['rss_stop_bytes'], H.CAPS['log_max_bytes'])
    R['F12_terminal_cpu_cap'] = {'expected': 'not accepted; UNKNOWN/cpu-cap-final', 'got': (ok, rec['verdict'], rec['reason']), 'pass': (not ok) and rec['reason'] == 'cpu-cap-final'}
    s = sup('F13'); rec = s.register({k: v for k, v in base.items() if not k.startswith('time_l_')}); rec['metrics_after'] = dict(s.baseline)
    ok = s.finalize(rec, 150, H.CAPS['rss_stop_bytes'], H.CAPS['log_max_bytes'])
    R['F13_terminal_missing_accounting'] = {'expected': 'not accepted; UNKNOWN/missing-accounting', 'got': (ok, rec['verdict'], rec['reason']),
                                            'pass': (not ok) and rec['reason'].startswith('missing-accounting')}

    s = sup('F14'); H.FAULTS['log_max_bytes'] = 1 << 20
    r = s.run_step('f14', [PY, '-c', "import sys\nfor i in range(12): sys.stdout.write('x' * (1 << 20)); sys.stdout.flush()"], out, 30, 30, H.m_pass)
    H.FAULTS['log_max_bytes'] = None
    R['F14_terminal_log_burst_exit'] = {'expected': 'UNKNOWN with reason log-cap or log-cap-final', 'got': (r['verdict'], r['reason']), 'log_MiB': r['log_bytes'] >> 20,
                                        'pass': r['verdict'] == 'UNKNOWN' and r['reason'] in ('log-cap', 'log-cap-final')}

    s = sup('F15'); r = s.run_step('f15', ['sh', '-c', 'sleep 20 & exit 0'], out, 30, 30, H.m_pass); time.sleep(0.5)
    R['F15_terminal_orphan'] = {'expected': 'UNKNOWN/cleanup-orphans, orphan killed, group gone', 'got': (r['verdict'], r['reason']), 'orphans_killed': r.get('orphans_killed'),
                                'child_gone': gone('^sleep 20$'), 'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'cleanup-orphans') and gone('^sleep 20$')}

    s = sup('F16'); s.deadline = time.monotonic() - 1
    r = s.run_step('f16', ['sleep', '20'], out, 30, 30, H.m_pass)
    R['F16_expired_deadline'] = {'expected': 'UNKNOWN/stage-deadline, nothing spawned', 'got': (r['verdict'], r['reason']), 'spawned': 'started_at' in r,
                                 'pass': (r['verdict'], r['reason']) == ('UNKNOWN', 'stage-deadline') and 'started_at' not in r}

    # F17: a throwaway copy of the clone's tracked tree with one tracked file modified (no build trees needed for the pin check to fail)
    d = fresh(out, 'F17'); tmpkit = os.path.join(d, 'kit'); os.makedirs(tmpkit)
    subprocess.run(['git', 'clone', '-q', '--shared', KIT, tmpkit], check=True)
    with open(os.path.join(tmpkit, 'Check.lean'), 'a') as f:
        f.write('\n-- modified for F17\n')
    pr = subprocess.run([PY, H.__file__, tmpkit, os.path.join(d, 'out')], capture_output=True, text=True)
    R['F17_dirty_tracked_tree'] = {'expected': "stops with 'pin mismatch'", 'exit': pr.returncode, 'stdout': pr.stdout.strip()[:120],
                                   'pass': pr.returncode == 1 and 'pin mismatch' in pr.stdout}
    shutil.rmtree(tmpkit, ignore_errors=True)

    s = sup('F18'); d18 = json.load(open(os.path.join(s.out, 'receipts.json')))
    R['F18_harness_digest'] = {'expected': 'receipt digest equals the file digest', 'pass': d18['harness_sha256'] == H.digest(H.__file__)}

    R['all_pass'] = all(v['pass'] for k, v in R.items() if isinstance(v, dict))
    json.dump(R, open(os.path.join(out, 'faults.json'), 'w'), indent=1)
    for k, v in R.items():
        if isinstance(v, dict):
            print('%-34s %s' % (k, 'PASS' if v['pass'] else 'FAIL  ' + json.dumps({a: b for a, b in v.items() if a != 'pass'}, default=str)[:200]))
    print('ALL PASS' if R['all_pass'] else 'SOME FAILED')
    sys.exit(0 if R['all_pass'] else 1)


if __name__ == '__main__':
    main()
