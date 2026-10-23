#!/usr/bin/env python3
"""Harmless fault tests of the W1A supervisor (tests/probes/wolfram/w1a_harness.py, revision 3), run before launch 2
at GPT's request (GPT-L782-HARNESS-REVIEW.md). No Lean, no kit module, no benchmark: tiny shell and Python children
with tiny caps. Each test declares its expectation here, before it runs; the result goes to OUT_DIR/faults.json.

Usage:  python3 w1a_faults.py OUT_DIR

  F1 wall cap:        `sleep 20` with a 2 s wall cap           -> UNKNOWN / wall-cap, group gone afterwards
  F2 RSS stop:        a Python child holding 300 MiB, stop 100 MiB -> UNKNOWN / rss-stop
  F3 monitor failure: ps made to fail after 2 samples, child `sleep 20` -> UNKNOWN / monitor-failure, child killed
  F4 exception path:  a supervisor exception injected after 2 samples -> the group is killed in `finally`, the receipt
                      is left `incomplete`, and the exception propagates to the caller
  F5 log cap:         a child printing 12 MiB with a 1 MiB log cap  -> UNKNOWN / log-cap
  F6 fresh output:    a non-empty output folder is refused by main (exit 3)
  F7 cost-miss gate:  synthetic receipts: wall 70 s -> miss; RSS 4.6 GiB -> miss; wall 30 s and 3 GiB -> no miss
  F8 engines:         packed and scalar engines agree on W = 1, 2, 4 and the literal orbits; K(2) = 7 from the scalar one
  F9 checker parser:  a good JSON line passes; verdict pass with a missing headline fails; an extra axiom fails
  F10 completed race: `sleep 1` with ps failing from sample 3 on -> the child exits first; verdict pass, no false failure
  F11 matchers:       neg_w2's matcher rejects an unrelated error text and accepts the real diagnostic text

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import json, os, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w1a_harness as H


def fresh(out, name):
    d = os.path.join(out, name); os.makedirs(d, exist_ok=True); return d


def main():
    out = os.path.abspath(sys.argv[1]); os.makedirs(out, exist_ok=True)
    kit = os.path.expanduser('~/np-scratch-int/wolfram-agents/width/kit-w1a')
    results = {}
    PY = sys.executable

    def sup(name):
        H.FAULTS.update({'ps_fail_after': None, 'raise_after': None, 'rss_stop_bytes': None, 'log_max_bytes': None})
        return H.Supervisor(kit, fresh(out, name))

    # F1
    s = sup('F1'); r = s.run_step('f1', ['sleep', '20'], out, 2, 30, H.m_pass)
    results['F1_wall_cap'] = {'expected': 'UNKNOWN/wall-cap, group gone', 'verdict': r['verdict'], 'reason': r['reason'],
                              'members_after': r['group_members_after'], 'wall_s': r['wall_s'],
                              'pass': r['verdict'] == 'UNKNOWN' and r['reason'] == 'wall-cap' and r['group_members_after'] == 0}
    # F2
    s = sup('F2'); H.FAULTS['rss_stop_bytes'] = 100 << 20
    r = s.run_step('f2', [PY, '-c', 'import time; b = bytearray(300 << 20); time.sleep(20)'], out, 30, 30, H.m_pass)
    results['F2_rss_stop'] = {'expected': 'UNKNOWN/rss-stop', 'verdict': r['verdict'], 'reason': r['reason'],
                              'peak_MiB': r['sampled_group_rss_peak_bytes'] >> 20,
                              'pass': r['verdict'] == 'UNKNOWN' and r['reason'] == 'rss-stop'}
    # F3
    s = sup('F3'); H.FAULTS['ps_fail_after'] = 2
    r = s.run_step('f3', ['sleep', '20'], out, 30, 30, H.m_pass)
    H.FAULTS['ps_fail_after'] = None
    gone = subprocess.run(['pgrep', '-f', '^sleep 20$'], capture_output=True).returncode != 0
    results['F3_monitor_failure'] = {'expected': 'UNKNOWN/monitor-failure, child killed', 'verdict': r['verdict'], 'reason': r['reason'],
                                     'monitor_error': r.get('monitor_error'), 'child_gone': gone,
                                     'pass': r['verdict'] == 'UNKNOWN' and r['reason'] == 'monitor-failure' and gone}
    # F4
    s = sup('F4'); H.FAULTS['raise_after'] = 2; raised = False; rec_after = None
    try:
        s.run_step('f4', ['sleep', '20'], out, 30, 30, H.m_pass)
    except RuntimeError as e:
        raised = 'injected' in str(e)
    H.FAULTS['raise_after'] = None
    time.sleep(0.5)
    gone = subprocess.run(['pgrep', '-f', '^sleep 20$'], capture_output=True).returncode != 0
    results['F4_exception_path'] = {'expected': 'exception propagates, group killed', 'raised': raised, 'child_gone': gone,
                                    'pass': raised and gone}
    # F5
    s = sup('F5'); H.FAULTS['log_max_bytes'] = 1 << 20
    r = s.run_step('f5', [PY, '-c', "import sys\nfor i in range(12): sys.stdout.write('x' * (1 << 20)); sys.stdout.flush()\nimport time; time.sleep(20)"], out, 30, 30, H.m_pass)
    H.FAULTS['log_max_bytes'] = None
    results['F5_log_cap'] = {'expected': 'UNKNOWN/log-cap', 'verdict': r['verdict'], 'reason': r['reason'], 'log_bytes': r['log_bytes'],
                             'pass': r['verdict'] == 'UNKNOWN' and r['reason'] == 'log-cap'}
    # F6
    d = fresh(out, 'F6'); open(os.path.join(d, 'old.txt'), 'w').write('x')
    p = subprocess.run([PY, H.__file__, kit, d], capture_output=True, text=True)
    results['F6_fresh_output'] = {'expected': 'refused, exit 3', 'exit': p.returncode, 'stdout': p.stdout.strip()[:100],
                                  'pass': p.returncode == 3 and 'REFUSED' in p.stdout}
    # F7
    g = H.GIB
    results['F7_cost_miss_gate'] = {'expected': 'miss, miss, no miss',
                                    'wall70': H.cost_miss({'wall_s': 70, 'sampled_group_rss_peak_bytes': g, 'time_l_max_rss_bytes': g}),
                                    'rss4_6': H.cost_miss({'wall_s': 10, 'sampled_group_rss_peak_bytes': int(4.6 * g), 'time_l_max_rss_bytes': g}),
                                    'ok': H.cost_miss({'wall_s': 30, 'sampled_group_rss_peak_bytes': 3 * g, 'time_l_max_rss_bytes': 3 * g})}
    results['F7_cost_miss_gate']['pass'] = (results['F7_cost_miss_gate']['wall70'] and results['F7_cost_miss_gate']['rss4_6']
                                            and not results['F7_cost_miss_gate']['ok'])
    # F8
    r, K4 = H.engines_control()
    results['F8_engines'] = {'expected': 'all checks true, K2 = 7', 'checks': r['checks'], 'K': r['K_scalar'], 'pass': r['verdict'] == 'pass'}
    # F9
    good = json.dumps({'verdict': 'pass', 'replay': {'ok': True, 'constants': 1}, 'newAxioms': [],
                       'headlines': [{'name': H.HEADLINE, 'found': True, 'ok': True, 'axioms': ['propext', 'Classical.choice', 'Quot.sound']}]})
    nohead = json.dumps({'verdict': 'pass', 'replay': {'ok': True}, 'newAxioms': [], 'headlines': []})
    extra = good.replace('"Quot.sound"]', '"Quot.sound", "myAxiom"]')
    v1 = H.m_checker(0, 'noise\n' + good)[0]; v2 = H.m_checker(0, nohead)[0]; v3 = H.m_checker(0, extra)[0]
    results['F9_checker_parser'] = {'expected': 'pass, FAIL, FAIL', 'got': [v1, v2, v3], 'pass': [v1, v2, v3] == ['pass', 'FAIL', 'FAIL']}
    # F10
    s = sup('F10'); H.FAULTS['ps_fail_after'] = 3
    r = s.run_step('f10', ['sleep', '1'], out, 30, 30, H.m_pass)
    H.FAULTS['ps_fail_after'] = None
    results['F10_completed_race'] = {'expected': 'pass/completed (child exits before the injected failure bites)', 'verdict': r['verdict'],
                                     'reason': r['reason'], 'pass': r['verdict'] == 'pass' and r['reason'] == 'completed'}
    # F11
    real = "neg_w2.lean:4:37: error: Tactic `decide` proved that the proposition\n  check 2 6 1 0 = true\nis false\n"
    unrelated = "neg_w2.lean:1:0: error: unknown module prefix 'Ruliology'\n"
    results['F11_matchers'] = {'expected': 'pass, FAIL', 'got': [H.m_neg_w2(1, real)[0], H.m_neg_w2(1, unrelated)[0]],
                               'pass': [H.m_neg_w2(1, real)[0], H.m_neg_w2(1, unrelated)[0]] == ['pass', 'FAIL']}
    results['all_pass'] = all(v['pass'] for k, v in results.items() if isinstance(v, dict))
    json.dump(results, open(os.path.join(out, 'faults.json'), 'w'), indent=1)
    for k, v in results.items():
        if isinstance(v, dict):
            print('%-22s %s' % (k, 'PASS' if v['pass'] else 'FAIL  ' + json.dumps({a: b for a, b in v.items() if a != 'pass'})[:160]))
    print('ALL PASS' if results['all_pass'] else 'SOME FAILED')
    sys.exit(0 if results['all_pass'] else 1)


if __name__ == '__main__':
    main()
