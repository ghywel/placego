#!/usr/bin/env python3
"""Mutation meta-controls for P2 revision 2's controls (Local, 2026-10-24, L879): each GC1787 fix is undone in a copy of the source and
the controls that guard it must FAIL, while the unmutated source passes them all. CPU only (mocks and Python stubs, as the controls).
Usage: python3 p2_controls_meta.py
OUTCOME (Local, 2026-10-24, development check, CPU only): P2 META PASS 7. The unmutated source passed all 68 controls; each mutation
made exactly its guarding controls fail. Under finally_closes_nothing three further end-to-end controls also failed, because they
also assert that no server is left live; every other control passed under every mutation."""
import contextlib, importlib.util, io, json, os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0_serve_controls as S0

MUTATIONS = [   # (name, source text, replacement, controls that must fail)
    ('batch_end_first_reach', 'self.first_reach, self.first_batch_gross, self.first_batch_s = prior + j + 1, self.gross, t',
     'self.first_reach, self.first_batch_gross, self.first_batch_s = self.gross, self.gross, t',
     ['first_reach_ordered_within_batch', 'first_reach_ordered_second_batch']),
    ('censor_ranked_as_a_death', '            if -1 in out:\n', '            if False:\n',
     ['censored_lane_stops_retained_unranked', 'censored_lane_inside_a_method_stops', 'e2e_censor_stops_retained_and_closed']),
    ('scalar_mismatch_ignored', "if sb != c['best']: fail(", "if False: fail(", ['score_scalar_mismatch_fails']),
    ('gate_ignores_failures', "    if d.get('failures') != []:", "    if False:", ['gate_correctness_failure_fails']),
    ('poll_ignores_buffer', "    if srv.buf: return 'trailing'\n    r, _, _ = select.select", "    if False: return 'trailing'\n    r, _, _ = select.select",
     ['evaluator_trailing_bytes_stop']),
    ('final_silence_check_skipped', '            q = srv.quiet()\n', "            q = 'silence'\n", ['e2e_final_tail_fails_close_check']),
    ('finally_closes_nothing', "        R['live_servers_closed_dead'] = S0.close_all()\n", "        R['live_servers_closed_dead'] = []\n",
     ['e2e_censor_stops_retained_and_closed', 'e2e_dead_server_stops_saved_and_closed']),
]


def run_controls(text, tag, tmp):
    p = os.path.join(tmp, 'p2_%s.py' % tag); open(p, 'w').write(text)
    spec = importlib.util.spec_from_file_location('p2_%s' % tag, p); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            mod.controls()
        except Exception as e:
            print(json.dumps({'_crashed': repr(e)[:200]})); print('P2 CONTROLS CRASH')
    out = buf.getvalue(); S0.close_all()
    return json.loads(out[:out.rfind('P2 CONTROLS')])


if __name__ == '__main__':
    src = open(os.path.join(HERE, 'p2_search.py')).read(); report = {}
    with tempfile.TemporaryDirectory() as tmp:
        base = run_controls(src, 'base', tmp)
        report['unmutated_all_pass'] = all(v is True for v in base.values()) and len(base) > 0
        for name, a, b, must in MUTATIONS:
            assert src.count(a) == 1, ('mutation site not unique', name)
            r = run_controls(src.replace(a, b), name, tmp)
            failed = [k for k in must if r.get(k) is not True]
            report[name] = {'must_fail': must, 'failed': failed, 'crashed': r.get('_crashed'),
                            'others_still_pass': sum(1 for k, v in r.items() if k not in must and v is True), 'others_total': sum(1 for k in r if k not in must)}
    ok = report['unmutated_all_pass'] and all(v['failed'] == v['must_fail'] and not v['crashed'] for k, v in report.items() if k != 'unmutated_all_pass')
    print(json.dumps(report, indent=1)); print('P2 META', 'PASS' if ok else 'FAIL', len(MUTATIONS)); sys.exit(0 if ok else 1)
