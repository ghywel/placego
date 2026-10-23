#!/usr/bin/env python3
"""W1A harness: the kit's width-52 certificate as an M5 workload, measured under GPT's specification
(reports/wolfram-agents/GPT-L780-JOB-DESIGN.md, section 3; Local's acceptance in CHAT-LEDGER.md L781).

Usage:  python3 w1a_harness.py KIT_CLONE OUT_DIR [--skip-preflight]

What it runs, in order, stopping at the first step that is not a pass (no automatic retry, no continuation past a
miss; a cap stop or missing receipt is UNKNOWN, never a failed theorem):
  0. preflight: the harness must observe its own child process tree (pids, RSS, CPU time) and terminate it;
     baselines of vm_stat and swap are recorded.
  1. literal-orbit control in Python: packed zero-boundary step  pstep r = (r >> 1) xor (r or (r << 1)) from the
     starts 1 and 3 gives 1,3,6,13,25,55,100,222 and 3,6,13,25,55,100,222; first even white time at depth 1 is 2
     for start 1 and 6 for start 3; first odd white time 7 and 1 (GPT's hand check, GC1710).
  2. Lean controls, each in its own file under the clone's lean/w1a_controls/, compiled with `lake env lean`:
     pos_w2.lean    `check 2 7 1 0 = true` by `decide +kernel`                       must compile;
     neg_w2.lean    `check 2 6 1 0 = true` by `decide +kernel`                       must FAIL with a decide message;
     cov_neg.lean   `q01_of_chunks 4 K 1` fed a `ChunksOK 4 K 1 0 1` premise         must FAIL with a type mismatch;
     cov_pos.lean   `q01_of_chunks 4 K 1` fed the authentic two-chunk composition    must compile.
  3. the four original width-52 chunk modules, one at a time, `lake build -j 1`, after their build outputs were
     removed from the clone so that they are actually compiled (caps: 180 s wall, 150 s CPU each);
  4. the wrapper Rule30ZeroBoundaryWidth52 the same way;
  5. the kit's own Check.lean on the wrapper module (caps: 600 s wall, 540 s CPU).
Every step runs in its own process group under /usr/bin/time -l, with the group's aggregate RSS sampled once a
second (a soft operational stop at 6 GiB, not an OS limit), its CPU time summed from ps, and the caps enforced by
killing the group. Receipts (exit code, stop reason, wall, user/system CPU, time -l peak RSS per process, sampled
aggregate RSS peak, vm_stat/swap before and after, output digests) go to OUT_DIR/receipts.json and per-step logs.
Stage wall cap 30 minutes. Concurrency 1. Nothing is written inside the kit clone except the controls folder and the
rebuilt outputs of the five target modules.

OUTCOME: filled in after the run (CHAT-LEDGER.md L782).
"""
import hashlib, json, os, signal, subprocess, sys, time

GIB = 1 << 30
STAGE_WALL = 30 * 60
RSS_STOP = 6 * GIB
TARGETS = [('Ruliology.CellularAutomata.Rule30Certificates.ZeroBoundaryWidth52Chunks%d' % i,
            'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks%d' % i)
           for i in range(4)] + \
          [('Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52',
            'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth52')]
HEADLINE = 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52.q01_width_le_52'

CONTROLS = {
    'pos_w2.lean': """import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
-- W = 2, n = 1, one chunk: the four starts all have a white depth-1 cell at an even time below 7 (start 3 at time 6).
example : check 2 7 1 0 = true := by decide +kernel
""",
    'neg_w2.lean': """import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
-- Genuine negative: start 3 survives every even time strictly below 6, so this is FALSE and must not compile.
example : check 2 6 1 0 = true := by decide +kernel
""",
    'cov_neg.lean': """import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
-- Coverage negative: at W = 4, n = 1 the complete count is 2 ^ (4 / 2 - 1) = 2. Supplying only one chunk must be
-- rejected at the range type (ChunksOK 4 K 1 0 1 is not ChunksOK 4 K 1 0 2).
theorem cov_neg (K : Nat) (h : ChunksOK 4 K 1 0 1) (x : Nat → Bool) (hx : ∀ k, 4 < k → x k = false) :
    ∃ t, t < K ∧ t % 2 = 0 ∧ Ruliology.CellularAutomata.Rule30ZeroBoundary.zrow x t 1 = false :=
  q01_of_chunks 4 K 1 (by decide) h x hx
""",
    'cov_pos.lean': """import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
-- The authentic composition at W = 4, n = 1: both chunks checked by the kernel, appended, fed to q01_of_chunks.
theorem c0 : check 4 KW4 1 0 = true := by decide +kernel
theorem c1 : check 4 KW4 1 1 = true := by decide +kernel
theorem both : ChunksOK 4 KW4 1 0 2 := chunksOK_append (chunksOK_one c0) (chunksOK_one c1)
theorem q01_w4 (x : Nat → Bool) (hx : ∀ k, 4 < k → x k = false) :
    ∃ t, t < KW4 ∧ t % 2 = 0 ∧ Ruliology.CellularAutomata.Rule30ZeroBoundary.zrow x t 1 = false :=
  q01_of_chunks 4 KW4 1 (by decide) both x hx
""",
    'find_k.lean': """import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes
-- Not a proof: a compiled evaluation to find the least K with both W = 4 chunks true (used to fill KW4 above).
#eval (List.range 40).filter (fun K => check 4 K 1 0 && check 4 K 1 1) |>.head?
""",
}


def sh(cmd, cwd=None):
    return subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True).stdout


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def mem_baseline():
    vm = sh('vm_stat | head -8')
    swap = sh('sysctl -n vm.swapusage').strip()
    return {'vm_stat': vm.strip().splitlines(), 'swap': swap, 'pressure': sh('memory_pressure 2>/dev/null | tail -1').strip()}


def group_sample(pgid):
    """(aggregate RSS bytes, aggregate CPU seconds, member count) of the process group pgid."""
    out = sh('ps -axo pgid=,rss=,time=')
    rss = 0; cpu = 0.0; n = 0
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 3 or parts[0] != str(pgid):
            continue
        n += 1
        rss += int(parts[1]) * 1024
        t = parts[2]
        secs = 0.0
        for piece in t.split(':'):
            secs = secs * 60 + float(piece)
        cpu += secs
    return rss, cpu, n


def run_step(name, cmd, cwd, wall_cap, cpu_cap, expect_fail=False, must_contain=None, logdir=None):
    log = open(os.path.join(logdir, name + '.log'), 'w')
    before = mem_baseline()
    t0 = time.time()
    proc = subprocess.Popen(['/usr/bin/time', '-l'] + cmd, cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
                            start_new_session=True)
    pgid = os.getpgid(proc.pid)
    peak_rss = 0; peak_members = 0; cpu_last = 0.0; reason = 'completed'
    while proc.poll() is None:
        rss, cpu, n = group_sample(pgid)
        peak_rss = max(peak_rss, rss); peak_members = max(peak_members, n); cpu_last = max(cpu_last, cpu)
        wall = time.time() - t0
        if rss > RSS_STOP:
            reason = 'rss-stop'; break
        if wall > wall_cap:
            reason = 'wall-cap'; break
        if cpu > cpu_cap:
            reason = 'cpu-cap'; break
        time.sleep(1.0)
    if reason != 'completed':
        try:
            os.killpg(pgid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait()
    wall = time.time() - t0
    log.close()
    text = open(os.path.join(logdir, name + '.log'), errors='replace').read()
    tl = {}
    for line in text.splitlines():
        s = line.strip()
        if s.endswith('maximum resident set size'):
            tl['time_l_max_rss_bytes'] = int(s.split()[0])
        elif s.endswith(' real') and ' user ' in s:
            tl['time_l_line'] = s
        elif s.endswith('user') and len(s.split()) == 2:
            tl['time_l_user'] = s
        elif s.endswith('sys') and len(s.split()) == 2:
            tl['time_l_sys'] = s
        elif s.endswith('real') and len(s.split()) == 2:
            tl['time_l_real'] = s
    rc = proc.returncode
    if reason != 'completed':
        verdict = 'UNKNOWN'
    elif expect_fail:
        verdict = 'pass' if (rc != 0 and (must_contain is None or must_contain in text)) else 'FAIL'
    else:
        verdict = 'pass' if rc == 0 and (must_contain is None or must_contain in text) else 'FAIL'
    rec = {'step': name, 'cmd': cmd, 'cwd': cwd, 'exit': rc, 'reason': reason, 'verdict': verdict,
           'expect_fail': expect_fail, 'wall_s': round(wall, 2), 'ps_cpu_s_peak': round(cpu_last, 1),
           'sampled_group_rss_peak_bytes': peak_rss, 'group_members_peak': peak_members,
           'mem_before': before, 'mem_after': mem_baseline(), 'log_tail': text[-1500:], **tl}
    return rec


def death_K(W, tmax=400):
    """1 + max over starts supported at depths 1..W (bits 0..W-1) of the first even t with the depth-1 cell white."""
    pstep = lambda r: (r >> 1) ^ (r | (r << 1))
    worst = 0
    for start in range(1 << W):
        r = start; t = 0
        while t <= tmax and not (t % 2 == 0 and (r & 1) == 0):
            r = pstep(r); t += 1
        if t > tmax:
            return None
        worst = max(worst, t)
    return worst + 1


def preflight(logdir):
    proc = subprocess.Popen(['sleep', '30'], start_new_session=True)
    pgid = os.getpgid(proc.pid)
    time.sleep(1.0)
    rss, cpu, n = group_sample(pgid)
    ok = n >= 1 and rss > 0
    os.killpg(pgid, signal.SIGKILL); proc.wait()
    time.sleep(0.5)
    rss2, cpu2, n2 = group_sample(pgid)
    gone = n2 == 0
    return {'step': 'preflight', 'observed_members': n, 'observed_rss': rss, 'terminated': gone,
            'verdict': 'pass' if ok and gone else 'FAIL', 'time_l_present': os.path.exists('/usr/bin/time'),
            'mem': mem_baseline()}


def orbit_control():
    pstep = lambda r: (r >> 1) ^ (r | (r << 1))
    def orbit(r, steps):
        out = [r]
        for _ in range(steps):
            r = pstep(r); out.append(r)
        return out
    o1 = orbit(1, 7); o3 = orbit(3, 6)
    def first_white(o, parity):
        for t, r in enumerate(o):
            if t % 2 == parity and (r & 1) == 0:
                return t
        return None
    rec = {'step': 'orbit-control', 'orbit_from_1': o1, 'orbit_from_3': o3,
           'first_even_white': {'1': first_white(o1, 0), '3': first_white(o3, 0)},
           'first_odd_white': {'1': first_white(o1, 1), '3': first_white(o3, 1)}}
    expected = (o1 == [1, 3, 6, 13, 25, 55, 100, 222] and o3 == [3, 6, 13, 25, 55, 100, 222]
                and rec['first_even_white'] == {'1': 2, '3': 6} and rec['first_odd_white'] == {'1': 7, '3': 1})
    rec['verdict'] = 'pass' if expected else 'FAIL'
    return rec


def main():
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    os.makedirs(out, exist_ok=True)
    receipts = {'kit': kit, 'kit_commit': sh('git rev-parse HEAD', kit).strip(),
                'toolchain': open(os.path.join(kit, 'lean-toolchain')).read().strip(),
                'lean_version': sh('lake env lean --version', kit).strip(),
                'sources': {}, 'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'steps': []}
    L = os.path.join(kit, 'lean/Ruliology/CellularAutomata')
    for f in ['Rule30ZeroBoundaryLanes.lean', 'Rule30ZeroBoundaryWidth52.lean'] + \
             ['Rule30Certificates/ZeroBoundaryWidth52Chunks%d.lean' % i for i in range(4)]:
        receipts['sources'][f] = digest(os.path.join(L, f))
    receipts['check_lean'] = digest(os.path.join(kit, 'Check.lean'))
    stage_t0 = time.time()

    def save():
        receipts['elapsed_s'] = round(time.time() - stage_t0, 1)
        json.dump(receipts, open(os.path.join(out, 'receipts.json'), 'w'), indent=1)

    def stop(msg):
        receipts['stopped'] = msg; save(); print('STOP:', msg); sys.exit(1)

    if '--skip-preflight' not in sys.argv:
        r = preflight(out); receipts['steps'].append(r); save()
        if r['verdict'] != 'pass':
            stop('preflight failed: the harness cannot observe or terminate its own child tree')
    r = orbit_control(); receipts['steps'].append(r); save()
    if r['verdict'] != 'pass':
        stop('literal-orbit control failed')

    # Lean controls
    cdir = os.path.join(kit, 'lean', 'w1a_controls'); os.makedirs(cdir, exist_ok=True)
    # K for W = 4 from the packed recurrence over all 2^4 starts (`check` is noncomputable, so no #eval): K is one
    # more than the latest first even white time at depth 1. The same computation must give 7 at W = 2 (GC1710).
    KW2 = death_K(2); KW4 = death_K(4)
    receipts['KW2_python'] = KW2; receipts['KW4_python'] = KW4
    if KW2 != 7:
        stop('python death-time computation gives K = %d at W = 2, not 7' % KW2)
    for name, src in CONTROLS.items():
        if name == 'find_k.lean':
            continue
        open(os.path.join(cdir, name), 'w').write(src.replace('KW4', str(KW4)))
    specs = [('pos_w2', False, None), ('neg_w2', True, 'decide'), ('cov_neg', True, 'type mismatch'), ('cov_pos', False, None)]
    for name, expect_fail, must in specs:
        r = run_step(name, ['lake', 'env', 'lean', 'w1a_controls/%s.lean' % name], os.path.join(kit, 'lean'), 30, 30,
                     expect_fail=expect_fail, must_contain=must, logdir=out)
        receipts['steps'].append(r); save()
        if r['verdict'] != 'pass':
            stop('control %s: %s' % (name, r['verdict']))

    # the five target modules, outputs removed first so that they are compiled
    for mod, rel in TARGETS:
        for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
            p = os.path.join(kit, rel + ext)
            if os.path.exists(p):
                os.remove(p)
    for mod, rel in TARGETS:
        if time.time() - stage_t0 > STAGE_WALL:
            stop('stage wall cap reached before %s' % mod)
        r = run_step('build_' + mod.split('.')[-1], ['lake', 'build', '-j', '1', mod], kit, 180, 150, logdir=out)
        olean = os.path.join(kit, rel + '.olean')
        r['olean'] = {'exists': os.path.exists(olean), 'bytes': os.path.getsize(olean) if os.path.exists(olean) else None,
                      'sha256': digest(olean) if os.path.exists(olean) else None}
        receipts['steps'].append(r); save()
        if r['verdict'] != 'pass' or not r['olean']['exists']:
            stop('module %s: %s (%s)' % (mod, r['verdict'], r['reason']))

    if time.time() - stage_t0 > STAGE_WALL:
        stop('stage wall cap reached before the checker')
    r = run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', TARGETS[-1][0], '--claim', 'partial',
                             '--headline', HEADLINE], kit, 600, 540, must_contain='"verdict":"pass"', logdir=out)
    receipts['steps'].append(r); save()
    receipts['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    print('DONE:', 'all steps pass' if r['verdict'] == 'pass' else 'checker %s' % r['verdict'])


if __name__ == '__main__':
    main()
