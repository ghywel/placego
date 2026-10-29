#!/usr/bin/env python3
"""run_capped.py: run ONE single-worker probe under enforced stage limits, with receipts (Local, 2026-10-26, L962; replaces run_capped.sh
after GPT's GC1903 review). Scoped to one CPU-bound child; not a general supervisor.

Usage: python3 run_capped.py --out DIR --cpu S --wall S --rss-mib M --file-mib F --disk-mib D [--min-free-mib G] [--swap-growth-mib W] -- cmd...

What is enforced, and how:
  * fresh destination: DIR must not exist (refused otherwise); everything the stage writes goes under DIR.
  * per-process limits in the child, set before exec and VERIFIED by getrlimit (launch refused if not applied): RLIMIT_CPU = S seconds,
    RLIMIT_FSIZE = F MiB per file. These are inherited per-process limits, not an aggregate process-tree CPU budget.
  * isolated process group: the child is started in a new session (start_new_session), so every descendant shares its process group.
  * monitor every second over the WHOLE process group (ps -A -o pid=,pgid=,rss=): summed RSS (sampled, not a system peak); stop if > M MiB.
    A monitor command failure or unparsable output STOPS the stage (exit reason MONITOR_FAILURE), never reads as zero.
  * memory pressure, every second: free+inactive pages (vm_stat; a declared proxy for headroom) must stay >= G MiB, and swap used
    (sysctl vm.swapusage) must not grow by more than W MiB over its launch value; parse failure stops the stage.
  * wall: stop after S seconds.  * aggregate artifact envelope: total bytes under DIR (including this log) checked every second <= D MiB.
  * stop procedure: SIGTERM to the process group, wait up to 5 s, then SIGKILL to the group, then verify no process of the group remains;
    the cleanup outcome is recorded.  Supervisor's own CPU is reported separately.
Receipts in DIR: out.txt (child stdout), time_receipt.txt (the full /usr/bin/time -l output = child stderr), launcher.json (limits, applied
limits, launch gate values, samples summary and maxima, exit reason, child return code, cleanup outcome, supervisor CPU, file inventory).
Exit reasons: COMPLETED, CPU_LIMIT (child killed by SIGXCPU), RSS_STOP, WALL_STOP, PRESSURE_STOP, DISK_STOP, MONITOR_FAILURE, REFUSED,
LEFTOVER_CLEANED (L974: the child exited but a member of its process group was still alive; the group is cleaned on this path too).
L974: the child receives CAPPED_OUT = the resolved destination, so a driver can bind its artifacts to it.
L1119, opt-in --track-tree (default off; without it behaviour is unchanged): the child's processes are tracked across
process groups, because a Wolfram kernel's RunProcess/StartProcess children (LeanLink's `lean` compile among them) take
process groups of their own (L1117). Every 0.5 s one `ps -A -o pid=,ppid=,pgid=,rss=,stat=,lstart=` call grows an OWNED
set: the group's members, and every process whose parent is owned when it is seen, each keyed by (pid, start time) so a
reused PID is never mistaken for an owned one. Owned processes stay tracked after reparenting. RSS and process counts
sum the live owned set; every stop, a leftover at the end and an exception in the supervisor terminate the owned set as
well as the group, and cleanup verifies that no owned process remains. Limit: a process created and orphaned within one
sampling interval is not seen.
GC2093: SIGTERM/SIGINT request normal cleanup (also during cleanup); failed tree sampling never falls back
to signalling stale PID-only identities. Optional --max-procs bounds the sampled live owned/group count.
Test hooks (harmless controls only, read from the environment): CAPPED_TEST_PS=bogus (monitor failure), CAPPED_TEST_MINFREE_MIB (raise
the pressure threshold).
"""
import argparse, json, os, resource, signal, subprocess, sys, time

MIB = 1 << 20

def vm_free_mib():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True, timeout=5).stdout
    page = int(out.split("page size of ")[1].split(" bytes")[0])
    vals = {}
    for line in out.splitlines()[1:]:
        if ":" in line:
            k, v = line.split(":", 1); vals[k.strip()] = int(v.strip().rstrip("."))
    return (vals["Pages free"] + vals["Pages inactive"]) * page // MIB

def swap_used_mib():
    out = subprocess.run(["sysctl", "-n", "vm.swapusage"], capture_output=True, text=True, timeout=5).stdout
    used = out.split("used =")[1].split()[0]
    num, unit = float(used[:-1]), used[-1]
    return num * {"M": 1, "G": 1024, "K": 1 / 1024}[unit]

def group_rss_kib(pgid, ps_cmd):
    r = subprocess.run([ps_cmd, "-A", "-o", "pid=,pgid=,rss="], capture_output=True, text=True, timeout=5)
    if r.returncode != 0 or not r.stdout.strip(): raise RuntimeError("ps failed")
    tot, n = 0, 0
    for line in r.stdout.splitlines():
        f = line.split()
        if len(f) != 3: raise RuntimeError("ps unparsable")
        if int(f[1]) == pgid: tot += int(f[2]); n += 1
    return tot, n

def ps_tree_rows(ps_cmd):
    r = subprocess.run([ps_cmd, "-A", "-o", "pid=,ppid=,pgid=,rss=,stat=,lstart="], capture_output=True, text=True, timeout=5)
    if r.returncode != 0 or not r.stdout.strip(): raise RuntimeError("ps failed")
    rows = {}
    for line in r.stdout.splitlines():
        f = line.split(None, 5)
        if len(f) != 6: raise RuntimeError("ps unparsable")
        rows[int(f[0])] = (int(f[1]), int(f[2]), int(f[3]), f[4], f[5].strip())
    return rows

def tree_update(owned, pgid, ps_cmd):
    """Grow owned {pid: start} from one ps listing; return (live owned pids, their summed RSS KiB)."""
    rows = ps_tree_rows(ps_cmd)
    grown = True
    while grown:
        grown = False
        for pid, (ppid, pg, _, stat, start) in rows.items():
            if pid in owned or stat.startswith("Z"): continue
            if pg == pgid or (ppid in owned and owned[ppid] == rows.get(ppid, (0, 0, 0, "", None))[4]):
                owned[pid] = start; grown = True
    live = [pid for pid, start in owned.items() if pid in rows and rows[pid][4] == start and not rows[pid][3].startswith("Z")]
    return live, sum(rows[pid][2] for pid in live)

def kill_owned(owned, pgid, ps_cmd, sig):
    # Discover BEFORE terminating the leader, or an escaping child may already be reparented when sampled.
    # A broken monitor/test command must not cause stale PID-only signalling: retry a fresh real ps snapshot.
    # If even that fails, only the owned group is signalled and cleanup stays explicitly unverified.
    try: live, _ = tree_update(owned, pgid, ps_cmd)
    except Exception:
        try: live, _ = tree_update(owned, pgid, "ps")
        except Exception: live = []
    try: os.killpg(pgid, sig)
    except (ProcessLookupError, PermissionError): pass
    for pid in live:
        try: os.kill(pid, sig)
        except (ProcessLookupError, PermissionError): pass

def dir_bytes(d):
    s = 0
    for root, _, files in os.walk(d):
        for f in files:
            try: s += os.path.getsize(os.path.join(root, f))
            except OSError: pass
    return s

def main():
    stop_signals = []
    # Do not raise from a handler: an interruption during cleanup must not interrupt cleanup itself.
    def request_stop(sig, _frame):
        stop_signals.append(sig)
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    ap = argparse.ArgumentParser()
    for k in ("out",): ap.add_argument("--" + k, required=True)
    for k in ("cpu", "wall", "rss-mib", "file-mib", "disk-mib"): ap.add_argument("--" + k, type=int, required=True)
    ap.add_argument("--min-free-mib", type=int, default=1024); ap.add_argument("--launch-free-mib", type=int, default=4096)
    ap.add_argument("--swap-growth-mib", type=int, default=256)
    ap.add_argument("--track-tree", action="store_true")
    ap.add_argument("--max-procs", type=int)
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
    rec = {"limits": vars(a) | {"cmd": cmd}, "start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if os.path.exists(a.out):
        print("REFUSED: destination exists", file=sys.stderr); return 2
    os.makedirs(a.out)
    logp = os.path.join(a.out, "launcher.json")
    ps_cmd = "bogus-ps-for-test" if os.environ.get("CAPPED_TEST_PS") == "bogus" else "ps"
    minfree = int(os.environ.get("CAPPED_TEST_MINFREE_MIB", a.min_free_mib))
    def finish(reason, rc=None, extra=None):
        if reason == "COMPLETED" and stop_signals:
            reason = "INTERRUPTED"
        rec.update({"exit_reason": reason, "child_rc": rc, "end_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "supervisor_cpu_s": round(resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime, 3)})
        if extra: rec.update(extra)
        if stop_signals: rec["stop_signals"] = stop_signals
        rec["inventory"] = {f: os.path.getsize(os.path.join(a.out, f)) for f in sorted(os.listdir(a.out))}
        with open(logp, "w") as fh: json.dump(rec, fh, indent=1)
        print(f"{reason} rc={rc}")
        return 0 if reason == "COMPLETED" and rc == 0 else 1
    try:
        free0, swap0 = vm_free_mib(), swap_used_mib()
    except Exception as e:
        return finish("REFUSED", extra={"gate_error": repr(e)})
    rec["gate"] = {"free_inactive_mib": free0, "swap_used_mib": swap0}
    if free0 < a.launch_free_mib:
        return finish("REFUSED", extra={"gate_error": "free+inactive below launch gate"})
    if stop_signals or (a.max_procs is not None and a.max_procs < 1):
        return finish("REFUSED", extra={"gate_error": "interrupted or invalid process cap"})
    def preexec():
        resource.setrlimit(resource.RLIMIT_CPU, (a.cpu, a.cpu))
        resource.setrlimit(resource.RLIMIT_FSIZE, (a.file_mib * MIB, a.file_mib * MIB))
        if resource.getrlimit(resource.RLIMIT_CPU) != (a.cpu, a.cpu) or resource.getrlimit(resource.RLIMIT_FSIZE) != (a.file_mib * MIB, a.file_mib * MIB):
            os._exit(97)
    out = open(os.path.join(a.out, "out.txt"), "w"); err = open(os.path.join(a.out, "time_receipt.txt"), "w")
    try:
        env = dict(os.environ, CAPPED_OUT=os.path.realpath(a.out))      # L974: the child can bind its artifact directory to this destination
        p = subprocess.Popen(["/usr/bin/time", "-l"] + cmd, stdout=out, stderr=err, preexec_fn=preexec, start_new_session=True, env=env)
    except Exception as e:
        return finish("REFUSED", extra={"spawn_error": repr(e)})
    pgid = p.pid
    owned = {}                                           # L1119 --track-tree: {pid: start time}
    t0 = time.time(); reason = None; samples = []; mx = {"rss_kib": 0, "procs": 0, "disk_bytes": 0, "swap_growth_mib": 0.0, "min_free_mib": free0}
    try:
      while p.poll() is None:
        if stop_signals: reason = "INTERRUPTED"; break
        time.sleep(0.5 if a.track_tree else 1)
        if p.poll() is not None: break
        try:
            if a.track_tree:
                live, rss = tree_update(owned, pgid, ps_cmd); n = len(live)
            else:
                rss, n = group_rss_kib(pgid, ps_cmd)
            fr = vm_free_mib(); sg = swap_used_mib() - swap0; db = dir_bytes(a.out)
        except Exception as e:
            reason = "MONITOR_FAILURE"; rec["monitor_error"] = repr(e); break
        mx["rss_kib"] = max(mx["rss_kib"], rss); mx["procs"] = max(mx["procs"], n); mx["disk_bytes"] = max(mx["disk_bytes"], db)
        mx["swap_growth_mib"] = max(mx["swap_growth_mib"], sg); mx["min_free_mib"] = min(mx["min_free_mib"], fr)
        if len(samples) < 600: samples.append([round(time.time() - t0, 1), rss, fr, round(sg, 1), db])
        if a.max_procs is not None and n > a.max_procs: reason = "PROCESS_STOP"; break
        if rss > a.rss_mib * 1024: reason = "RSS_STOP"; break
        if fr < minfree or sg > a.swap_growth_mib: reason = "PRESSURE_STOP"; break
        if db > a.disk_mib * MIB: reason = "DISK_STOP"; break
        if time.time() - t0 > a.wall: reason = "WALL_STOP"; break
    except BaseException as e:                           # L1119: a supervisor exception still stops the child's tree
        reason = "MONITOR_FAILURE"; rec["monitor_error"] = repr(e)
    if stop_signals: reason = "INTERRUPTED"
    cleanup = None
    def group_left():                                   # live (non-zombie) processes still in the group
        if a.track_tree:                                 # L1119: the whole owned set, group members included
            try: return len(tree_update(owned, pgid, ps_cmd)[0])
            except Exception as e: return f"unverified: {e!r}"
        try:
            n = 0
            result = subprocess.run(["ps", "-A", "-o", "pgid=,stat="], capture_output=True, text=True, timeout=5)
            if result.returncode != 0 or not result.stdout.strip():
                raise RuntimeError("cleanup ps failed")
            for line in result.stdout.splitlines():
                f = line.split()
                if len(f) != 2:
                    raise RuntimeError("cleanup ps unparsable")
                if int(f[0]) == pgid and not f[1].startswith("Z"): n += 1
            return n
        except Exception as e:
            return f"unverified: {e!r}"
    if not reason:                                       # L974: the child ended by itself; any live group member is a leftover
        try: p.wait(timeout=5)
        except subprocess.TimeoutExpired: pass
        if group_left() != 0: reason_leftover = True
        else: reason_leftover = False
    else:
        reason_leftover = False
    if reason or reason_leftover:
        sig = "TERM"
        if a.track_tree: kill_owned(owned, pgid, ps_cmd, signal.SIGTERM)
        else:
            try: os.killpg(pgid, signal.SIGTERM)
            except (ProcessLookupError, PermissionError): pass
        deadline = time.time() + 5                       # wait for the WHOLE group, not just the direct child
        while time.time() < deadline and group_left() != 0:
            p.poll(); time.sleep(0.2)                          # reap the direct child as soon as it exits
        if group_left() != 0:
            sig = "TERM+KILL"
            if a.track_tree: kill_owned(owned, pgid, ps_cmd, signal.SIGKILL)
            else:
                try: os.killpg(pgid, signal.SIGKILL)
                except (ProcessLookupError, PermissionError) as e: sig += f" ({type(e).__name__})"
            time.sleep(0.5)
        try: p.wait(timeout=5)
        except subprocess.TimeoutExpired: pass
        cleanup = {"signal": sig, "group_processes_left": group_left()}
        if a.track_tree: cleanup["owned_seen"] = len(owned)
    rc = p.returncode
    out.close(); err.close()
    if not reason and reason_leftover:
        reason = "LEFTOVER_CLEANED"                       # L974: a failure exit even if the child returned 0
    if not reason:
        reason = "CPU_LIMIT" if rc in (-signal.SIGXCPU, 128 + signal.SIGXCPU, 152) or "Cputime limit" in open(os.path.join(a.out, "time_receipt.txt")).read() else ("COMPLETED" if rc == 0 else "CHILD_FAILED")
    db = dir_bytes(a.out)
    extra = {"maxima": mx, "samples_kept": samples[:600], "wall_s": round(time.time() - t0, 2), "cleanup": cleanup, "final_dir_bytes": db}
    if db > a.disk_mib * MIB and reason == "COMPLETED": reason = "DISK_STOP"
    return finish(reason, rc, extra)

if __name__ == "__main__":
    sys.exit(main())
