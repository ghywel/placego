#!/usr/bin/env python3
"""W1A harness, revision 4: the kit's width-52 certificate as an M5 workload, under GPT's specification
(reports/wolfram-agents/GPT-L780-JOB-DESIGN.md section 3, accepted in L781), GPT's reviews of revisions 2 and 3
(GPT-L782-HARNESS-REVIEW.md, GPT-L783-HARNESS-REVIEW.md). Revision 3 and its fault evidence are retained in git
history and in width/faults-20261023-1754/. Launch 1 (revision 2) keeps its own output folder; an output folder is
never reused.

Usage:  python3 w1a_harness.py KIT_CLONE OUT_DIR          (OUT_DIR must not exist or must be empty)

The step lifecycle, explicit (GPT-L783 section "Trajectory check"):
  registered -> spawned -> proof exit (the child's exit code and the matcher's reading of its output, kept apart from
  accounting) -> FINAL VALIDATION by one terminal policy (`finalize`) -> persisted outcome -> advance or stop.
A step's receipt is registered and saved atomically BEFORE its child is spawned and updated in every exit path,
including an exception (verdict UNKNOWN, reason `exception`, re-raised) and a stop; the same step is never appended
twice. The terminal policy accepts a step only if: the proof verdict is pass; the required accounting is present
(`time -l` real/user/sys and peak RSS, final metrics, final group sample; a missing value is `missing-accounting`,
never zero); the cumulative CPU (`time -l` user+sys) is within the step's CPU cap; the wall is within the step's cap;
the stage deadline has not passed; the peak RSS by either metric is within the stop; the final log, artifact and
swap-growth values are within their caps (a child that finishes between samples cannot pass a cap it crossed); and
the owned process group is gone (any member remaining after the leader exits is killed and the step is
`cleanup-orphans`, UNKNOWN). An accounting or cleanup stop is UNKNOWN for the benchmark; a proof failure is FAIL. A
successful module above 60 s or 4.5 GiB is COST-MISS: a proof with an adverse cost, which ends the stage after that
module. An expired stage deadline prevents spawning (no extra second is granted).

The job (unchanged from L781), in order, stopping at the first step that is not accepted, with no retry:
  0. pins: the clone's HEAD must be the pinned commit, its tracked tree clean (`git status --porcelain` empty before
     the untracked controls folder is written), the toolchain and the SEVEN consumed sources (lanes, wrapper, the four
     chunk modules, Check.lean) must EQUAL the pinned hashes; the targets' imports must already be built; the output
     folder fresh; no serious memory pressure at launch; the harness's own digest goes into the receipt;
  1. preflight: the supervisor observes its own child (pid, RSS, CPU) with checked, time-bounded `ps`, terminates the
     group and sees it gone (cleanup protected if the first sample raises);
  2. two independent engines (packed word; scalar list-of-bools on a growing cone) compared on every start of
     W = 1, 2, 4 for 16 steps and on GPT's literal orbits; K(2) = 7 is a gate;
  3. Lean controls pos_w2, neg_w2, cov_neg, cov_pos (`lake env lean`), diagnostics matched exactly as in revision 3;
  4. the four original width-52 chunk modules then the wrapper, `lake build <module>` after their outputs were deleted
     (fresh compilation evidenced), at most one `lean` process per sample, the COST-MISS gate after each;
  5. the kit's Check.lean on the wrapper, its JSON parsed (verdict pass, the headline found and ok, axioms within the
     standard three, newAxioms empty, replay ok).

Running guards, sampled about once a second (sampling and monitor calls add latency; the caps are operational, not
OS-enforced): wall, live CPU (the sum over live group members, an operational guard only; accounting is the final
cumulative value), aggregate group RSS stop 6 GiB, memory pressure (`kern.memorystatus_vm_pressure_level` >= 2;
if that interface is unavailable the fallback is free memory below 10 percent, recorded as a different, conservative
policy, not a pressure measurement), swap growth > 256 MiB over the launch baseline, free disk < 5 GiB, new
artifacts > 512 MiB (every new file under the clone's two build trees and the output folder, relative to a baseline
snapshot; dependency caches do not count), a step log > 10 MiB, extra lean workers, monitor failure (a `ps`,
`sysctl` or `df` that fails, times out or does not parse while the child is alive terminates the group; a sample
that fails after the child has exited is retried once and is not a failure). Fault-injection knobs in FAULTS are
inert unless tests/probes/wolfram/w1a_faults.py sets them.

Caps: stage 30 min; module and wrapper 180 s wall / 150 s CPU; checker 600 / 540 s; controls 30 / 30 s; one worker.

OUTCOME: filled in after the run (CHAT-LEDGER.md).
"""
import hashlib, json, os, signal, subprocess, sys, time

GIB = 1 << 30; MIB = 1 << 20
PIN = {
    'commit': 'cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554',
    'toolchain': 'leanprover/lean4:v4.35.0',
    'sources': {
        'lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryLanes.lean': 'e34541fa34ee09d0f480db469384fcab9c05311e7f26bc135db02c5f692de7e3',
        'lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth52.lean': 'e1457d03ff4b40b2630cc9ab7ac901e67335373a60d88abff18c5028b772ad64',
        'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks0.lean': '1e2b672db9c9f6ee8c44ad85d85dc8a27029f3c8e919c6dd41e4ad1da04d6dd7',
        'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks1.lean': '7b6882f26550f923bc3cef49db84cf862c1ca2a02d48b307e6656be090461010',
        'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks2.lean': 'de2040b1fcbde5c694800d3ebb4fc8ef0d07a5fe0e8f59e7568ac8fb17faeb26',
        'lean/Ruliology/CellularAutomata/Rule30Certificates/ZeroBoundaryWidth52Chunks3.lean': '1cfadd6eb650987dfeff909d565fd925a2e7c4d6fefe297ee62c45f8ff15a85e',
        'Check.lean': 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905',
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
BUILD_TREES = ['lean/.lake/build', '.lake/build']
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
    """Memory pressure, swap and disk, parsed and validated; MonitorError if any required value is unavailable."""
    m = {}
    try:
        m['pressure_level'] = int(checked(['sysctl', '-n', 'kern.memorystatus_vm_pressure_level']).strip())
        m['pressure_policy'] = 'level'
    except (MonitorError, ValueError):
        m['pressure_level'] = None; m['pressure_policy'] = 'free-percent-fallback'
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
    if m.get('pressure_level') is not None:
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


def kill_group(pgid):
    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def snapshot(kit, out):
    """Every file under the clone's build trees and the output folder, with sizes: the artifact baseline."""
    seen = {}
    for root_rel in BUILD_TREES + [None]:
        root = out if root_rel is None else os.path.join(kit, root_rel)
        for r, _, files in os.walk(root):
            for f in files:
                p = os.path.join(r, f)
                try:
                    seen[p] = os.path.getsize(p)
                except OSError:
                    pass
    return seen


def new_artifact_bytes(kit, out, baseline):
    total = 0
    for p, size in snapshot(kit, out).items():
        if p not in baseline or size > baseline[p]:
            total += size - baseline.get(p, 0)
    return total


def atomic_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)


def parse_time_l(text):
    tl = {}
    for line in text.splitlines():
        s = line.strip()
        if s.endswith('maximum resident set size'):
            tl['time_l_max_rss_bytes'] = int(s.split()[0])
        elif 'real' in s and 'user' in s and 'sys' in s and len(s.split()) == 6:
            p = s.split(); tl['time_l_real_s'] = float(p[0]); tl['time_l_user_s'] = float(p[2]); tl['time_l_sys_s'] = float(p[4])
    return tl


class Supervisor:
    def __init__(self, kit, out):
        self.kit = kit; self.out = out
        self.t0 = time.monotonic(); self.deadline = self.t0 + CAPS['stage_s']
        self.receipts = {'kit': kit, 'caps': CAPS, 'faults': dict(FAULTS), 'started': time.strftime('%Y-%m-%dT%H:%M:%S'),
                         'harness_sha256': digest(os.path.abspath(__file__)), 'steps': [], 'complete': False}
        self.baseline = metrics(kit)
        self.receipts['baseline'] = self.baseline
        self.art_baseline = snapshot(kit, out)
        self.receipts['artifact_baseline_files'] = len(self.art_baseline)
        self.save()

    def remaining(self):
        return self.deadline - time.monotonic()

    def save(self):
        self.receipts['elapsed_s'] = round(time.monotonic() - self.t0, 1)
        atomic_json(os.path.join(self.out, 'receipts.json'), self.receipts)

    def register(self, rec):
        """Register a step once, before it runs; later updates mutate the same dict and save."""
        self.receipts['steps'].append(rec); self.save(); return rec

    def finalize(self, rec, cpu_cap, rss_stop, log_max, pgid=None):
        """The one terminal policy. Sets rec['verdict'] and rec['reason'] from the proof verdict, the required final
        accounting, the caps and the cleanup; returns True only if the step may advance."""
        problems = []
        # cleanup: any owned member still alive after the leader exited is killed and recorded
        if pgid is not None:
            try:
                _, _, n_after, _ = group_sample(pgid)
            except MonitorError as e:
                n_after = None; rec['cleanup_sample_error'] = str(e)
            if n_after:
                kill_group(pgid); time.sleep(0.5)
                try:
                    _, _, n_after2, _ = group_sample(pgid)
                except MonitorError:
                    n_after2 = None
                rec['orphans_killed'] = n_after
                problems.append('cleanup-orphans' if n_after2 == 0 else 'cleanup-failed')
            elif n_after is None:
                problems.append('cleanup-unverified')
            rec['group_members_after'] = n_after
        # required accounting
        if rec.get('reason') == 'completed':
            for k in ('time_l_real_s', 'time_l_user_s', 'time_l_sys_s', 'time_l_max_rss_bytes'):
                if rec.get(k) is None:
                    problems.append('missing-accounting:' + k)
            if not isinstance(rec.get('metrics_after'), dict):
                problems.append('missing-accounting:metrics_after')
        if rec.get('reason') == 'completed' and not problems:
            cum = rec['time_l_user_s'] + rec['time_l_sys_s']
            rec['cumulative_cpu_s'] = round(cum, 2)
            if cum > cpu_cap: problems.append('cpu-cap-final')
            if rec['wall_s'] > rec['wall_cap_s']: problems.append('wall-cap-final')
            if time.monotonic() > self.deadline: problems.append('stage-deadline-final')
            peak = max(rec.get('sampled_group_rss_peak_bytes', 0), rec['time_l_max_rss_bytes'])
            rec['peak_rss_bytes_either'] = peak
            if peak > rss_stop: problems.append('rss-stop-final')
            if rec['log_bytes'] > log_max: problems.append('log-cap-final')
            rec['new_artifact_bytes_final'] = new_artifact_bytes(self.kit, self.out, self.art_baseline)
            if rec['new_artifact_bytes_final'] > CAPS['artifacts_max_bytes']: problems.append('artifact-cap-final')
            if rec['metrics_after']['swap_used_bytes'] - self.baseline['swap_used_bytes'] > CAPS['swap_growth_bytes']:
                problems.append('swap-growth-final')
        rec['final_problems'] = problems
        if rec.get('reason') != 'completed':
            rec['verdict'] = 'UNKNOWN'                      # a running-guard stop, monitor failure or exception
        elif problems:
            rec['verdict'] = 'UNKNOWN'; rec['reason'] = problems[0]
        else:
            rec['verdict'] = rec['proof_verdict']
        self.save()
        return rec['verdict'] == 'pass'

    def run_step(self, name, cmd, cwd, wall_cap, cpu_cap, matcher):
        """registered -> spawned -> proof exit -> finalize -> persisted outcome. Returns the persisted receipt."""
        rss_stop = FAULTS['rss_stop_bytes'] or CAPS['rss_stop_bytes']
        log_max = FAULTS['log_max_bytes'] or CAPS['log_max_bytes']
        rec = self.register({'step': name, 'cmd': cmd, 'cwd': cwd, 'verdict': 'incomplete', 'reason': 'registered',
                             'wall_cap_s': min(wall_cap, self.remaining()), 'cpu_cap_s': cpu_cap})
        if self.remaining() <= 0:
            rec['reason'] = 'stage-deadline'; rec['verdict'] = 'UNKNOWN'; self.save(); return rec
        try:
            rec['metrics_before'] = metrics(self.kit)
        except MonitorError as e:
            rec['reason'] = 'monitor-failure'; rec['monitor_error'] = str(e); rec['verdict'] = 'UNKNOWN'; self.save(); return rec
        if pressure_bad(rec['metrics_before']):
            rec['reason'] = 'pressure-before-start'; rec['verdict'] = 'UNKNOWN'; self.save(); return rec
        logpath = os.path.join(self.out, name + '.log')
        log = open(logpath, 'w')
        t_start = time.monotonic(); rec['started_at'] = time.time(); rec['reason'] = 'spawned'; self.save()
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
                        rec['late_sample_error_ignored'] = str(e); break
                    rec['monitor_error'] = str(e); reason = 'monitor-failure'; break
                sample_no += 1
                peak_rss = max(peak_rss, rss); peak_members = max(peak_members, n); peak_lean = max(peak_lean, lean)
                live_cpu_peak = max(live_cpu_peak, cpu)
                wall = time.monotonic() - t_start
                logsize = os.path.getsize(logpath) if os.path.exists(logpath) else 0
                arts = new_artifact_bytes(self.kit, self.out, self.art_baseline)
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
        except BaseException as e:
            reason = 'exception'; rec['exception'] = repr(e)
            raise
        finally:
            if proc.poll() is None:
                kill_group(pgid); proc.wait()
            log.close()
            text = open(logpath, errors='replace').read() if os.path.exists(logpath) else ''
            rec.update({'exit': proc.returncode, 'reason': reason, 'wall_s': round(time.monotonic() - t_start, 2),
                        'live_cpu_peak_s': round(live_cpu_peak, 1), 'sampled_group_rss_peak_bytes': peak_rss,
                        'group_members_peak': peak_members, 'lean_processes_peak': peak_lean, 'samples': sample_no,
                        'log_bytes': len(text), 'log_tail': text[-2000:], **parse_time_l(text)})
            try:
                rec['metrics_after'] = metrics(self.kit)
            except MonitorError as e:
                rec['metrics_after'] = 'unavailable: %s' % e
            if reason == 'completed':
                rec['proof_verdict'], rec['match_note'] = matcher(proc.returncode, text)
            else:
                rec['proof_verdict'] = None
            if reason == 'exception':
                rec['verdict'] = 'UNKNOWN'
                try:
                    _, _, n_after, _ = group_sample(pgid)
                    if n_after:
                        kill_group(pgid)
                    rec['group_members_after'] = n_after
                except MonitorError:
                    rec['group_members_after'] = None
                self.save()
            else:
                self.finalize(rec, cpu_cap, rss_stop, log_max, pgid)
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
        cells = [False] + [c[d + 1] ^ (c[d] or c[d - 1]) for d in range(1, len(c) - 1)]
    return out


def first_white(orbit, parity):
    for t, r in enumerate(orbit):
        if t % 2 == parity and (r & 1) == 0:
            return t
    return None


def death_K_scalar(W, tmax=400):
    worst = 0
    for start in range(1 << W):
        t = first_white(scalar_orbit([(start >> i) & 1 == 1 for i in range(W)], tmax), 0)
        if t is None:
            return None
        worst = max(worst, t)
    return worst + 1


def engines_control():
    rec = {'step': 'engines-control', 'verdict': 'pass', 'reason': 'completed', 'checks': {}}
    for W in (1, 2, 4):
        agree = all(packed_orbit(s, 16) == scalar_orbit([(s >> i) & 1 == 1 for i in range(W)], 16) for s in range(1 << W))
        rec['checks']['W%d_all_starts_16_steps' % W] = agree
    o1 = packed_orbit(1, 7); o3 = packed_orbit(3, 6)
    lit = (o1 == [1, 3, 6, 13, 25, 55, 100, 222] and o3 == [3, 6, 13, 25, 55, 100, 222]
           and first_white(o1, 0) == 2 and first_white(o3, 0) == 6 and first_white(o1, 1) == 7 and first_white(o3, 1) == 1)
    rec['checks']['literal_orbits'] = lit
    rec['orbits'] = {'from_1': o1, 'from_3': o3}
    K2 = death_K_scalar(2); K4 = death_K_scalar(4)
    rec['K_scalar'] = {'W2': K2, 'W4': K4}
    rec['checks']['K2_is_7'] = K2 == 7
    rec['checks']['K_not_none'] = K2 is not None and K4 is not None
    if not all(rec['checks'].values()):
        rec['verdict'] = 'FAIL'
    return rec, K4


def cost_miss(rec):
    peak = max(rec.get('sampled_group_rss_peak_bytes', 0), rec.get('time_l_max_rss_bytes') or 0)
    return rec.get('wall_s', 0) > CAPS['cost_miss_wall_s'] or peak > CAPS['cost_miss_rss_bytes']


def preflight():
    proc = subprocess.Popen(['sleep', '30'], start_new_session=True)
    pgid = os.getpgid(proc.pid)
    try:
        time.sleep(1.0)
        rss, cpu, n, _ = group_sample(pgid)
    finally:
        kill_group(pgid); proc.wait(); time.sleep(0.5)
    try:
        _, _, n2, _ = group_sample(pgid)
    except MonitorError:
        n2 = None
    return {'step': 'preflight', 'reason': 'completed', 'observed_members': n, 'observed_rss': rss, 'terminated': n2 == 0,
            'verdict': 'pass' if n >= 1 and rss > 0 and n2 == 0 else 'FAIL'}


def main():
    kit = os.path.abspath(sys.argv[1]); out = os.path.abspath(sys.argv[2])
    if os.path.exists(out) and os.listdir(out):
        print('REFUSED: output folder exists and is not empty:', out); sys.exit(3)
    os.makedirs(out, exist_ok=True)
    cdir = os.path.join(kit, 'lean', 'w1a_controls')
    if os.path.isdir(cdir):
        for f in os.listdir(cdir):
            os.remove(os.path.join(cdir, f))
        os.rmdir(cdir)
    sup = Supervisor(kit, out); R = sup.receipts

    def stop(msg, code=1):
        R['stopped'] = msg; sup.save(); print('STOP:', msg); sys.exit(code)

    # 0. pins and a clean tracked tree
    commit = checked(['git', '-C', kit, 'rev-parse', 'HEAD']).strip()
    dirty = subprocess.run(['git', '-C', kit, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip()
    toolchain = open(os.path.join(kit, 'lean-toolchain')).read().strip()
    got = {f: digest(os.path.join(kit, f)) for f in PIN['sources']}
    bad = {f: got[f] for f, want in PIN['sources'].items() if got[f] != want}
    R['pins'] = {'commit': commit, 'tracked_tree_dirty': dirty.splitlines(), 'toolchain': toolchain, 'sources': got,
                 'bad_sources': list(bad),
                 'lean_version': subprocess.run(['lake', 'env', 'lean', '--version'], cwd=kit, capture_output=True, text=True).stdout.strip(),
                 'deps_built': {d: os.path.exists(os.path.join(kit, d)) for d in DEPS}}
    sup.save()
    if commit != PIN['commit'] or dirty or toolchain != PIN['toolchain'] or bad or not all(R['pins']['deps_built'].values()):
        stop('pin mismatch: commit %s dirty %r toolchain %s bad sources %s deps %s' % (commit[:8], bool(dirty), toolchain, list(bad), R['pins']['deps_built']))
    if pressure_bad(sup.baseline):
        stop('serious memory pressure at launch: %s' % sup.baseline)

    # 1. preflight
    r = sup.register(preflight())
    if r['verdict'] != 'pass':
        stop('preflight failed')

    # 2. engines
    r, KW4 = engines_control(); sup.register(r)
    if r['verdict'] != 'pass' or KW4 is None:
        stop('engines control failed')
    R['KW4'] = KW4; sup.save()

    # 3. Lean controls (untracked, written after the clean-tree check)
    os.makedirs(cdir, exist_ok=True)
    for name, src in CONTROLS.items():
        open(os.path.join(cdir, name), 'w').write(src.replace('KW4', str(KW4)))
    R['control_sha256'] = {n: digest(os.path.join(cdir, n)) for n in CONTROLS}; sup.save()
    for name, matcher in (('pos_w2', m_pass), ('neg_w2', m_neg_w2), ('cov_neg', m_cov_neg), ('cov_pos', m_pass)):
        r = sup.run_step(name, ['lake', 'env', 'lean', 'w1a_controls/%s.lean' % name], os.path.join(kit, 'lean'),
                         CAPS['control_wall_s'], CAPS['control_cpu_s'], matcher)
        if r['verdict'] != 'pass':
            stop('control %s: %s (%s)' % (name, r['verdict'], r['reason']))

    # 4. the targets, compiled fresh
    for mod, rel in TARGETS:
        for ext in ('.olean', '.ilean', '.trace', '.olean.hash', '.ilean.hash'):
            p = os.path.join(kit, rel + ext)
            if os.path.exists(p):
                os.remove(p)
    sup.art_baseline = snapshot(kit, out)        # the deletions are not new artifacts
    for mod, rel in TARGETS:
        olean = os.path.join(kit, rel + '.olean')
        absent_before = not os.path.exists(olean)
        r = sup.run_step('build_' + mod.split('.')[-1], ['lake', 'build', mod], kit, CAPS['module_wall_s'], CAPS['module_cpu_s'], m_pass)
        exists = os.path.exists(olean)
        r['olean'] = {'absent_before': absent_before, 'exists_after': exists,
                      'bytes': os.path.getsize(olean) if exists else None, 'sha256': digest(olean) if exists else None,
                      'mtime_after_start': (os.path.getmtime(olean) >= r.get('started_at', 0) - 1) if exists else None}
        r['fresh_compilation'] = bool(absent_before and exists and r['olean']['mtime_after_start'])
        r['cost_miss'] = cost_miss(r) if r['verdict'] == 'pass' else None
        sup.save()
        if r['verdict'] != 'pass' or not r['fresh_compilation']:
            stop('module %s: %s (%s)' % (mod, r['verdict'], r['reason']))
        if r['cost_miss']:
            stop('COST-MISS after %s: wall %.1f s, peak RSS %.2f GiB; stage ended as agreed, remaining modules not run'
                 % (mod, r['wall_s'], r['peak_rss_bytes_either'] / GIB), 2)

    # 5. the checker
    r = sup.run_step('checker', ['lake', 'env', 'lean', '--run', 'Check.lean', TARGETS[-1][0], '--claim', 'partial', '--headline', HEADLINE],
                     kit, CAPS['checker_wall_s'], CAPS['checker_cpu_s'], m_checker)
    if r['verdict'] != 'pass':
        stop('checker: %s (%s) %s' % (r['verdict'], r['reason'], r.get('match_note', '')))
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE: all steps pass')


if __name__ == '__main__':
    main()
