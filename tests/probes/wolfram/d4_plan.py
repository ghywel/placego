#!/usr/bin/env python3
"""D4 plan runner (GC1747's whole-plan budget): runs `d1_engine.py runmax W (2W+9) 2 OUT_W` for the listed widths in
order, one at a time, and REFUSES to start the next stage when the plan's cumulative wall or CPU (summed from each
stage's supervisor receipt: the step's wall and time -l user + sys, plus this runner's own wall) would exceed the
whole-plan budget, or when any stage ended other than complete with verdict pass. Budget (proposed): 1,800 s wall and
2,400 s CPU for the whole plan; per-stage caps as the engine's launcher (stage 1,800, step 1,500 / 2,400). Nothing
runs on import. Usage: python3 d4_plan.py OUT_ROOT W1 W2 ...   (each stage's folder OUT_ROOT/d4-W<W>-<stamp>)
"""
import json, os, subprocess, sys, time

BUDGET_WALL_S, BUDGET_CPU_S = 1800, 2400


def main():
    root = os.path.abspath(sys.argv[1]); widths = [int(w) for w in sys.argv[2:]]
    eng = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'd1_engine.py')
    plan = {'budget_wall_s': BUDGET_WALL_S, 'budget_cpu_s': BUDGET_CPU_S, 'widths': widths, 'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'stages': [], 'verdict': 'RUNNING'}
    t0 = time.monotonic(); cpu = 0.0
    os.makedirs(root, exist_ok=True); planf = os.path.join(root, 'd4_plan.json')
    json.dump(plan, open(planf, 'w'), indent=1)
    for W in widths:
        wall = time.monotonic() - t0
        if wall >= BUDGET_WALL_S or cpu >= BUDGET_CPU_S:
            plan['verdict'] = 'STOPPED'; plan['reason'] = 'plan budget reached before width %d (wall %.0f s, cpu %.0f s)' % (W, wall, cpu); break
        out = os.path.join(root, 'd4-W%d-%s' % (W, time.strftime('%Y%m%d-%H%M%S')))
        r = subprocess.run(['nice', '-n', '5', sys.executable, eng, 'runmax', str(W), str(2 * W + 9), '2', out], capture_output=True, text=True)
        rec = {'W': W, 'K': 2 * W + 9, 'out': os.path.basename(out), 'exit': r.returncode, 'tail': r.stdout.strip().splitlines()[-1:] }
        try:
            d = json.load(open(os.path.join(out, 'receipts.json'))); s = d['steps'][-1]
            rec.update({'complete': d.get('complete'), 'verdict': s.get('verdict'), 'reason': s.get('reason'), 'wall_s': s.get('wall_s'), 'cpu_s': (s.get('time_l_user_s') or 0) + (s.get('time_l_sys_s') or 0), 'note': s.get('match_note')})
            cpu += rec['cpu_s'] or 0
        except Exception as e:
            rec.update({'complete': False, 'verdict': 'UNKNOWN', 'reason': 'receipt unreadable: %r' % e})
        plan['stages'].append(rec); plan['cumulative_wall_s'] = round(time.monotonic() - t0, 1); plan['cumulative_cpu_s'] = round(cpu, 2)
        json.dump(plan, open(planf, 'w'), indent=1)
        if not rec.get('complete') or rec.get('verdict') != 'pass' or r.returncode != 0:
            plan['verdict'] = 'STOPPED'; plan['reason'] = 'stage W%d did not pass (%s, %s); no further stage' % (W, rec.get('verdict'), rec.get('reason')); break
    else:
        plan['verdict'] = 'COMPLETE'
    plan['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); plan['cumulative_wall_s'] = round(time.monotonic() - t0, 1); plan['cumulative_cpu_s'] = round(cpu, 2)
    json.dump(plan, open(planf, 'w'), indent=1)
    print(plan['verdict'], plan.get('reason', ''), 'wall %.0f s cpu %.0f s' % (plan['cumulative_wall_s'], plan['cumulative_cpu_s']))
    sys.exit(0 if plan['verdict'] == 'COMPLETE' else 1)


if __name__ == '__main__':
    main()
