#!/usr/bin/env python3
"""W1A harness, revision 3: the kit's width-52 certificate as an M5 workload, under GPT's specification
(reports/wolfram-agents/GPT-L780-JOB-DESIGN.md section 3, accepted in CHAT-LEDGER.md L781) and GPT's source review of
revision 2 (reports/wolfram-agents/GPT-L782-HARNESS-REVIEW.md). Launch 1 (revision 2) is retained in its own output
folder; this revision never reuses an output folder.

Usage:  python3 w1a_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

The job (unchanged from L781): in order, stopping at the first step that is not a pass, with no retry:
  0. pins: the clone's commit, toolchain and the six source hashes must EQUAL the constants below (not merely be
     recorded); the imports of the targets must already be built; the output folder must be fresh; no serious memory
     pressure at launch;
  1. preflight: the supervisor observes its own child (pid, RSS, CPU) with checked, time-bounded `ps`, terminates the
     group, and sees it gone;
  2. two independent engines for the zero-boundary evolution, compared on every start of W = 1, 2, 4 for 16 steps and
     on GPT's literal orbits (1,3,6,13,25,55,100,222 from 1; 3,6,13,25,55,100,222 from 3; first even white at depth 1
     is 2 and 6, first odd 7 and 1): the packed word  pstep r = (r >> 1) xor (r | (r << 1))  and a scalar list-of-bools
     cell update  new[d] = c[d+1] xor (c[d] or c[d-1])  on a growing light cone with the wall c[0] = false;
     K for W = 2 and W = 4 (one more than the latest first even white time over all starts) comes from the scalar
     engine and must agree with the packed one, and K(2) must be 7;
  3. Lean controls, each its own file under the clone's lean/w1a_controls/, `lake env lean`:
     pos_w2   check 2 7 1 0 = true by decide +kernel            must compile;
     neg_w2   check 2 6 1 0 = true by decide +kernel            must fail with the diagnostic "proved that the
              proposition … check 2 6 1 0 = true … is false", and with no other error kind;
     cov_neg  q01_of_chunks 4 K 1 fed ChunksOK 4 K 1 0 1         must fail with the type mismatch naming the supplied
              one-chunk range and the expected ChunksOK 4 K 1 0 (2 ^ (4 / 2 - 1));
     cov_pos  the authentic two-chunk composition at W = 4      must compile;
  4. the four original width-52 chunk modules then the wrapper, one at a time, `lake build <module>` after their
     outputs were deleted from the clone (fresh compilation is evidenced: object absent before, present after with a
     later mtime); at most one `lean` process in the group at any sample (else UNKNOWN, extra workers);
     after each module's receipt is saved, the COST-MISS gate: wall > 60 s or peak RSS > 4.5 GiB (sampled group peak or
     time -l peak) ends the stage after that module; a cost miss is a successful proof with an adverse cost, not FAIL;
  5. the kit's Check.lean on the wrapper: its JSON is parsed and must say verdict pass, the headline
     Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52.q01_width_le_52 found and ok, axioms within
     {propext, Classical.choice, Quot.sound}, newAxioms empty; anything else is a nonzero harness exit.

Running guards, sampled once a second for every step, each a stop with verdict UNKNOWN and its own reason:
  wall cap (per step, and never past the stage deadline, which is passed into every step), live CPU cap (the sum over
  the live members of the group; cumulative CPU is the `time -l` user+sys in the receipt, and a step whose cumulative
  CPU exceeds its cap is recorded as a cap miss after the fact: the live sum is an operational guard, not the
  accounting), aggregate group RSS stop 6 GiB (soft, sampled), memory pressure (kern.memorystatus_vm_pressure_level
  2 = warning or 4 = critical when available, else free memory below 10 percent), swap growth over the launch
  baseline above 256 MiB, free disk below 5 GiB, new artifacts above 512 MiB, a step log above 10 MiB, extra lean
  workers, and MONITOR FAILURE: a `ps`, `sysctl` or `df` call that fails, times out or does not parse while the child
  is still alive is not zero; the group is terminated and the step is UNKNOWN (if the child has just exited, the
  sample is retried once). Every receipt is written atomically before the next decision; an exception anywhere kills
  the owned group and leaves an `incomplete` receipt. Fault-injection knobs in FAULTS are inert unless a test sets them
  (tests/probes/wolfram/w1a_faults.py).

Caps: stage 30 min; module and wrapper 180 s wall / 150 s CPU; checker 600 / 540 s; controls 30 / 30 s; one worker.

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import hashlib, json, os, signal, subprocess, sys, time

GIB = 1 << 30; MIB = 1 << 20
PIN = {
    'commit': 'cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554',
    'toolchain': 'leanprover/lean4:v4.35.0',
    'sources': {
        'Rule30ZeroBoundaryLanes.lean': 'e34541fa34ee09d0f480db469384fcab9c05311e7f26bc135db02c5f692de7e3',
        'Rule30ZeroBoundaryWidth52.lean': 'e1457d03ff4b40b2630cc9ab7ac901e67335373a60d88abff18c5028b772ad64',
        'Rule30Certificates/ZeroBoundaryWidth52Chunks0.lean': '1e2b672db9c9f6ee8c44ad85d85dc8a27029f3c8e919c6dd41e4ad1da04d6dd7',
        # chunks 1-3 are bound by the hashes recorded at the first pin check, see pin_sources() below
    },
}
CAPS = {'stage_s': 30 * 60, 'module_wall_s': 180, 'module_cpu_s': 150, 'checker_wall_s': 600, 'checker_cpu_s': 540,
        'control_wall_s': 30, 'control_cpu_s': 30, 'rss_stop_bytes': 6 * GIB, 'cost_miss_wall_s': 60,
        'cost_miss_rss_bytes': int(4.5 * GIB), 'swap_growth_bytes': 256 * MIB, 'disk_free_min_bytes': 5 * GIB,
        'artifacts_max_bytes': 512 * MIB, 'log_max_bytes': 10 * MIB, 'free_pct_min': 10, 'monitor_timeout_s': 5}
FAULTS = {'ps_fail_after': None, 'raise_after': None, 'rss_stop_bytes': None, 'log_max_bytes': None}
TARGETS = [('Ruliology.CellularAutomata.Rule30Certificates.ZeroBoundaryWidth52Chunks%d' % i,
            'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks%d' % i)
           for i in range(4)] + \
          [('Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52',
            'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth52')]
DEPS = ['lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryLanes.olean',
        'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.olean',
        'lean/.lake/build/lib/lean/Ruliology/CellularAutomata/Rule30ZeroBoundarySmall.olean']
HEADLINE = 'Ruliology.CellularAutomata.Rule30ZeroBoundaryWidth52.q01_width_le_52'
STD_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}

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
}


class MonitorError(Exception):
    pass


class Stop(Exception):
    pass


def checked(cmd, timeout=None):
    """Run a monitor command; a nonzero exit, a timeout or empty output is a MonitorError, never a zero."""
    timeout = timeout or CAPS['monitor_timeout_s']
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise MonitorError('timeout: %s' % ' '.join(cmd))
    if r.returncode != 0:
        raise MonitorError('exit %d: %s: %s' % (r.returncode, ' '.join(cmd), r.stderr.strip()[:200]))
    if not r.stdout.strip():
        raise MonitorError('empty output: %s' % ' '.join(cmd))
    return r.stdout


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def metrics(path_for_disk):
    """Memory pressure, swap and disk, parsed and validated; MonitorError if any is unavailable."""
    m = {}
    try:
        lvl = checked(['sysctl', '-n', 'kern.memorystatus_vm_pressure_level']).strip()
        m['pressure_level'] = int(lvl)          # 1 normal, 2 warning, 4 critical
    except MonitorError:
        m['pressure_level'] = None             # recorded as unavailable, the free-percent guard applies instead
    m['free_pct'] = int(checked(['sysctl', '-n', 'kern.memorystatus_level']).strip())
    sw = checked(['sysctl', '-n', 'vm.swapusage'])
    used = [p for p in sw.replace('(', ' ').split() if p.endswith('M') and p[:-1].replace('.', '', 1).isdigit()]
    if len(used) < 2:
        raise MonitorError('swapusage parse: %s' % sw.strip())
    m['swap_used_bytes'] = int(float(used[1][:-1]) * MIB)
    df = checked(['df', '-k', path_for_disk]).splitlines()
    if len(df) < 2:
        raise MonitorError('df parse')
    m['disk_free_bytes'] = int(df[1].split()[3]) * 1024
    return m


def pressure_bad(m):
    if m['pressure_level'] is not None:
        return m['pressure_level'] >= 2
    return m['free_pct'] < CAPS['free_pct_min']


def group_sample(pgid, sample_no=0):
    """(aggregate RSS bytes, live CPU seconds, members, lean processes) of the process group, by checked ps."""
    if FAULTS['ps_fail_after'] is not None and sample_no >= FAULTS['ps_fail_after']:
        raise MonitorError('injected ps failure')
    out = checked(['ps', '-axo', 'pgid=,rss=,time=,comm='])
    rss = 0; cpu = 0.0; n = 0; lean = 0
    for line in out.splitlines():
        parts = line.split(None, 3)
        if len(parts) < 4 or parts[0] != str(pgid):
            continue
        n += 1
        rss += int(parts[1]) * 1024
        secs = 0.0
        for piece in parts[2].split(':'):
            secs = secs * 60 + float(piece)
        cpu += secs
        if os.path.basename(parts[3].strip()) == 'lean':
            lean += 1
    return rss, cpu, n, lean


def tree_bytes(paths):
    total = 0
    for p in paths:
        if os.path.isfile(p):
            total += os.path.getsize(p)
        elif os.path.isdir(p):
            for root, _, files in os.walk(p):
                for f in files:
                    total += os.path.getsize(os.path.join(root, f))
    return total


def atomic_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)


class Supervisor:
    def __init__(self, kit, out):
        self.kit = kit; self.out = out
        self.t0 = time.monotonic(); self.deadline = self.t0 + CAPS['stage_s']
        self.receipts = {'kit': kit, 'caps': CAPS, 'faults': FAULTS, 'started': time.strftime('%Y-%m-%dT%H:%M:%S'),
                         'steps': [], 'complete': False}
        self.baseline = metrics(kit)
        self.receipts['baseline'] = self.baseline
        self.artifact_paths = [os.path.join(kit, rel + ext) for _, rel in TARGETS for ext in ('.olean', '.ilean', '.trace')] + [out]
        self.save()

    def remaining(self):
        return self.deadline - time.monotonic()

    def save(self):
        self.receipts['elapsed_s'] = round(time.monotonic() - self.t0, 1)
        atomic_json(os.path.join(self.out, 'receipts.json'), self.receipts)

    def add(self, rec):
        self.receipts['steps'].append(rec); self.save()

    def run_step(self, name, cmd, cwd, wall_cap, cpu_cap, matcher):
        """Run cmd in its own process group under /usr/bin/time -l with every guard; returns the receipt."""
        logpath = os.path.join(self.out, name + '.log')
        rec = {'step': name, 'cmd': cmd, 'cwd': cwd, 'verdict': 'incomplete', 'reason': 'started',
               'wall_cap_s': min(wall_cap, max(1.0, self.remaining())), 'cpu_cap_s': cpu_cap,
               'metrics_before': metrics(self.kit)}
        if pressure_bad(rec['metrics_before']):
            rec['verdict'] = 'UNKNOWN'; rec['reason'] = 'pressure-before-start'; return rec
        rss_stop = FAULTS['rss_stop_bytes'] or CAPS['rss_stop_bytes']
        log_max = FAULTS['log_max_bytes'] or CAPS['log_max_bytes']
        log = open(logpath, 'w')
        t_start = time.monotonic(); wall_start = time.time()
        proc = subprocess.Popen(['/usr/bin/time', '-l'] + cmd, cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
        pgid = os.getpgid(proc.pid)
        peak_rss = 0; peak_members = 0; peak_lean = 0; live_cpu_peak = 0.0; reason = 'completed'; sample_no = 0
        try:
            while proc.poll() is None:
                if FAULTS['raise_after'] is not None and sample_no >= FAULTS['raise_after']:
                    raise RuntimeError('injected supervisor exception')
                try:
                    rss, cpu, n, lean = group_sample(pgid, sample_no)
                    m = metrics(self.kit)
                except MonitorError as e:
                    time.sleep(0.2)
                    if proc.poll() is not None:        # the child had just exited: a normal race, not a failure
                        break
                    rec['monitor_error'] = str(e); reason = 'monitor-failure'; break
                sample_no += 1
                peak_rss = max(peak_rss, rss); peak_members = max(peak_members, n); peak_lean = max(peak_lean, lean)
                live_cpu_peak = max(live_cpu_peak, cpu)
                wall = time.monotonic() - t_start
                logsize = os.path.getsize(logpath) if os.path.exists(logpath) else 0
                arts = tree_bytes(self.artifact_paths)
                if rss > rss_stop: reason = 'rss-stop'; break
                if wall > rec['wall_cap_s']: reason = 'wall-cap'; break
                if time.monotonic() > self.deadline: reason = 'stage-deadline'; break
                if cpu > cpu_cap: reason = 'cpu-cap'; break
                if pressure_bad(m): reason = 'memory-pressure'; break
                if m['swap_used_bytes'] - self.baseline['swap_used_bytes'] > CAPS['swap_growth_bytes']: reason = 'swap-growth'; break
                if m['disk_free_bytes'] < CAPS['disk_free_min_bytes']: reason = 'disk-low'; break
                if logsize > log_max: reason = 'log-cap'; break
                if arts > CAPS['artifacts_max_bytes']: reason = 'artifact-cap'; break
                if lean > 1: reason = 'extra-workers'; break
                time.sleep(1.0)
        finally:
            if proc.poll() is None:
                try:
                    os.killpg(pgid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait()
            log.close()
            # confirm the group is gone (owned processes only)
            try:
                _, _, n_after, _ = group_sample(pgid)
            except MonitorError:
                n_after = None
            text = open(logpath, errors='replace').read() if os.path.exists(logpath) else ''
            tl = {}
            for line in text.splitlines():
                s = line.strip()
                if s.endswith('maximum resident set size'):
                    tl['time_l_max_rss_bytes'] = int(s.split()[0])
                elif 'real' in s and 'user' in s and 'sys' in s and len(s.split()) == 6:
                    p = s.split(); tl['time_l_real_s'] = float(p[0]); tl['time_l_user_s'] = float(p[2]); tl['time_l_sys_s'] = float(p[4])
            rec.update({'exit': proc.returncode, 'reason': reason, 'wall_s': round(time.monotonic() - t_start, 2),
                        'started_at': wall_start, 'live_cpu_peak_s': round(live_cpu_peak, 1),
                        'sampled_group_rss_peak_bytes': peak_rss, 'group_members_peak': peak_members,
                        'lean_processes_peak': peak_lean, 'group_members_after': n_after, 'samples': sample_no,
                        'log_bytes': len(text), 'log_tail': text[-2000:], 'metrics_after': None, **tl})
            try:
                rec['metrics_after'] = metrics(self.kit)
            except MonitorError as e:
                rec['metrics_after'] = 'unavailable: %s' % e
            cum = (tl.get('time_l_user_s') or 0) + (tl.get('time_l_sys_s') or 0)
            rec['cumulative_cpu_s'] = round(cum, 2)
            rec['cpu_cap_miss_after_the_fact'] = cum > cpu_cap
            if reason != 'completed':
                rec['verdict'] = 'UNKNOWN'
            else:
                rec['verdict'], rec['match_note'] = matcher(proc.returncode, text)
        return rec


# ---- matchers (verdict, note) -------------------------------------------------------------------------------------
def m_pass(rc, text):
    return ('pass' if rc == 0 and ' error' not in text and 'error:' not in text else 'FAIL', 'exit %d' % rc)


def m_neg_w2(rc, text):
    want = ['proved that the proposition', 'check 2 6 1 0 = true', 'is false']
    ok = rc != 0 and all(w in text for w in want)
    other = [l for l in text.splitlines() if 'error' in l and 'decide' not in l and 'proposition' not in l]
    return ('pass' if ok and not other else 'FAIL', 'expected diagnostic %s; other errors %d' % (ok, len(other)))


def m_cov_neg(rc, text):
    want = ['type mismatch', 'ChunksOK 4 K 1 0 1', 'ChunksOK 4 K 1 0 (2 ^ (4 / 2 - 1))']
    ok = rc != 0 and all(w in text for w in want)
    return ('pass' if ok else 'FAIL', 'range diagnostic %s' % ok)


def m_checker(rc, text):
    last = [l for l in text.splitlines() if l.startswith('{') and '"verdict"' in l]
    if rc != 0 or not last:
        return 'FAIL', 'no JSON verdict (exit %d)' % rc
    try:
        d = json.loads(last[-1])
    except Exception as e:
        return 'FAIL', 'JSON parse: %s' % e
    hs = {h.get('name'): h for h in d.get('headlines', [])}
    h = hs.get(HEADLINE)
    good = (d.get('verdict') == 'pass' and h is not None and h.get('found') and h.get('ok')
            and set(h.get('axioms', [])) <= STD_AXIOMS and d.get('newAxioms') == [] and d.get('replay', {}).get('ok'))
    return ('pass' if good else 'FAIL', json.dumps({'verdict': d.get('verdict'), 'headline': h, 'newAxioms': d.get('newAxioms'), 'replay': d.get('replay')}))


# ---- the two engines -----------------------------------------------------------------------------------------------
def packed_orbit(r, steps):
    pstep = lambda r: (r >> 1) ^ (r | (r << 1))
    out = [r]
    for _ in range(steps):
        r = pstep(r); out.append(r)
    return out


def scalar_orbit(start_bits, steps):
    """List-of-bools engine: c[0] is the wall (always white), c[d] the cell at depth d; the cone grows one cell a step."""
    cells = [False] + list(start_bits)
    out = []
    for _ in range(steps + 1):
        out.append(sum(1 << (d - 1) for d in range(1, len(cells)) if cells[d]))
        c = cells + [False, False]
        new = [False] + [c[d + 1] ^ (c[d] or c[d - 1]) for d in range(1, len(c) - 1)]
        cells = new
    return out


def first_white(orbit, parity):
    for t, r in enumerate(orbit):
        if t % 2 == parity and (r & 1) == 0:
            return t
    return None


def death_K_scalar(W, tmax=400):
    worst = 0
    for start in range(1 << W):
        bits = [(start >> i) & 1 == 1 for i in range(W)]
        orb = scalar_orbit(bits, tmax)
        t = first_white(orb, 0)
        if t is None:
            return None
        worst = max(worst, t)
    return worst + 1


def engines_control():
    rec = {'step': 'engines-control', 'verdict': 'pass', 'checks': {}}
    for W in (1, 2, 4):
        agree = all(packed_orbit(s, 16) == scalar_orbit([(s >> i) & 1 == 1 for i in range(W)], 16) for s in range(1 << W))
        rec['checks']['W%d_all_starts_16_steps' % W] = agree
        rec['verdict'] = rec['verdict'] if agree else 'FAIL'
    o1 = packed_orbit(1, 7); o3 = packed_orbit(3, 6)
    lit = (o1 == [1, 3, 6, 13, 25, 55, 100, 222] and o3 == [3, 6, 13, 25, 55, 100, 222]
           and first_white(o1, 0) == 2 and first_white(o3, 0) == 6 and first_white(o1, 1) == 7 and first_white(o3, 1) == 1)
    rec['checks']['literal_orbits'] = lit
    rec['orbits'] = {'from_1': o1, 'from_3': o3}
    K2 = death_K_scalar(2); K4 = death_K_scalar(4)
    rec['K_scalar'] = {'W2': K2, 'W4': K4}
    rec['checks']['K2_is_7'] = K2 == 7
    rec['checks']['K_not_none'] = K2 is not None and K4 is not None
    if not (lit and K2 == 7 and K4 is not None):
        rec['verdict'] = 'FAIL'
    return rec, K4


def cost_miss(rec):
    peak = max(rec.get('sampled_group_rss_peak_bytes', 0), rec.get('time_l_max_rss_bytes', 0))
    return rec.get('wall_s', 0) > CAPS['cost_miss_wall_s'] or peak > CAPS['cost_miss_rss_bytes']


def pin_sources(kit):
    L = os.path.join(kit, 'lean/Ruliology/CellularAutomata')
    got = {f: digest(os.path.join(L, f)) for f in list(PIN['sources']) +
           ['Rule30Certificates/ZeroBoundaryWidth52Chunks%d.lean' % i for i in (1, 2, 3)]}
    bad = {f: got[f] for f, want in PIN['sources'].items() if got[f] != want}
    return got, bad


def preflight():
    proc = subprocess.Popen(['sleep', '30'], start_new_session=True)
    pgid = os.getpgid(proc.pid)
    time.sleep(1.0)
    rss, cpu, n, _ = group_sample(pgid)
    os.killpg(pgid, signal.SIGKILL); proc.wait(); time.sleep(0.5)
    _, _, n2, _ = group_sample(pgid)
    return {'step': 'preflight', 'observed_members': n, 'observed_rss': rss, 'terminated': n2 == 0,
            'verdict': 'pass' if n >= 1 and rss > 0 and n2 == 0 else 'FAIL'}


def main():
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    sup = Supervisor(kit, out); R = sup.receipts

    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    # 0. pins
    commit = checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    toolchain = open(os.path.join(kit, 'lean-toolchain')).read().strip()
    got, bad = pin_sources(kit)
    R['pins'] = {'commit': commit, 'toolchain': toolchain, 'sources': got,
                 'lean_version': subprocess.run(['lake', 'env', 'lean', '--version'], cwd=kit, capture_output=True, text=True).stdout.strip(),
                 'check_lean_sha256': digest(os.path.join(kit, 'Check.lean')),
                 'deps_built': {d: os.path.exists(os.path.join(kit, d)) for d in DEPS}}
    sup.save()
    if commit != PIN['commit'] or toolchain != PIN['toolchain'] or bad or not all(R['pins']['deps_built'].values()):
        stop('pin mismatch: commit %s toolchain %s bad sources %s deps %s' % (commit[:8], toolchain, list(bad), R['pins']['deps_built']))
    if pressure_bad(sup.baseline):
        stop('serious memory pressure at launch: %s' % sup.baseline)

    # 1. preflight
    r = preflight(); sup.add(r)
    if r['verdict'] != 'pass':
        stop('preflight failed')

    # 2. engines
    r, KW4 = engines_control(); sup.add(r)
    if r['verdict'] != 'pass' or KW4 is None:
        stop('engines control failed')
    R['KW4'] = KW4; sup.save()

    # 3. Lean controls
    cdir = os.path.join(kit, 'lean', 'w1a_controls'); os.makedirs(cdir, exist_ok=True)
    for name, src in CONTROLS.items():
        open(os.path.join(cdir, name), 'w').write(src.replace('KW4', str(KW4)))
    for name, matcher in (('pos_w2', m_pass), ('neg_w2', m_neg_w2), ('cov_neg', m_cov_neg), ('cov_pos', m_pass)):
        r = sup.run_step(name, ['lake', 'env', 'lean', 'w1a_controls/%s.lean' % name], os.path.join(kit, 'lean'),
                         CAPS['control_wall_s'], CAPS['control_cpu_s'], matcher)
        sup.add(r)
        if r['verdict'] != 'pass':
            stop('control %s: %s (%s)' % (name, r['verdict'], r['reason']))

    # 4. the targets, compiled fresh
    for mod, rel in TARGETS:
        for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
            p = os.path.join(kit, rel + ext)
            if os.path.exists(p):
                os.remove(p)
    for mod, rel in TARGETS:
        olean = os.path.join(kit, rel + '.olean')
        absent_before = not os.path.exists(olean)
        r = sup.run_step('build_' + mod.split('.')[-1], ['lake', 'build', mod], kit, CAPS['module_wall_s'], CAPS['module_cpu_s'], m_pass)
        exists = os.path.exists(olean)
        r['olean'] = {'absent_before': absent_before, 'exists_after': exists,
                      'bytes': os.path.getsize(olean) if exists else None, 'sha256': digest(olean) if exists else None,
                      'mtime_after_start': (os.path.getmtime(olean) >= r['started_at'] - 1) if exists else None}
        r['fresh_compilation'] = bool(absent_before and exists and r['olean']['mtime_after_start'])
        r['cost_miss'] = cost_miss(r)
        sup.add(r)
        if r['verdict'] != 'pass' or not r['fresh_compilation']:
            stop('module %s: %s (%s)' % (mod, r['verdict'], r['reason']))
        if r['cost_miss']:
            stop('COST-MISS after %s: wall %.1f s, peak RSS %.2f GiB; stage ended as agreed, remaining modules not run'
                 % (mod, r['wall_s'], max(r['sampled_group_rss_peak_bytes'], r.get('time_l_max_rss_bytes', 0)) / GIB), 2)

    # 5. the checker
    r = sup.run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', TARGETS[-1][0], '--claim', 'partial', '--headline', HEADLINE],
                     kit, CAPS['checker_wall_s'], CAPS['checker_cpu_s'], m_checker)
    sup.add(r)
    if r['verdict'] != 'pass':
        stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note', '')))
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: all steps pass')


if __name__ == '__main__':
    main()
