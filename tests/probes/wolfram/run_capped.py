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
Exit reasons: COMPLETED, CPU_LIMIT (child killed by SIGXCPU), RSS_STOP, WALL_STOP, PRESSURE_STOP, DISK_STOP, MONITOR_FAILURE, REFUSED.
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

def dir_bytes(d):
    s = 0
    for root, _, files in os.walk(d):
        for f in files:
            try: s += os.path.getsize(os.path.join(root, f))
            except OSError: pass
    return s

def main():
    ap = argparse.ArgumentParser()
    for k in ("out",): ap.add_argument("--" + k, required=True)
    for k in ("cpu", "wall", "rss-mib", "file-mib", "disk-mib"): ap.add_argument("--" + k, type=int, required=True)
    ap.add_argument("--min-free-mib", type=int, default=1024); ap.add_argument("--launch-free-mib", type=int, default=4096)
    ap.add_argument("--swap-growth-mib", type=int, default=256)
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
        rec.update({"exit_reason": reason, "child_rc": rc, "end_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "supervisor_cpu_s": round(resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime, 3)})
        if extra: rec.update(extra)
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
    def preexec():
        resource.setrlimit(resource.RLIMIT_CPU, (a.cpu, a.cpu))
        resource.setrlimit(resource.RLIMIT_FSIZE, (a.file_mib * MIB, a.file_mib * MIB))
        if resource.getrlimit(resource.RLIMIT_CPU) != (a.cpu, a.cpu) or resource.getrlimit(resource.RLIMIT_FSIZE) != (a.file_mib * MIB, a.file_mib * MIB):
            os._exit(97)
    out = open(os.path.join(a.out, "out.txt"), "w"); err = open(os.path.join(a.out, "time_receipt.txt"), "w")
    try:
        p = subprocess.Popen(["/usr/bin/time", "-l"] + cmd, stdout=out, stderr=err, preexec_fn=preexec, start_new_session=True)
    except Exception as e:
        return finish("REFUSED", extra={"spawn_error": repr(e)})
    pgid = p.pid
    t0 = time.time(); reason = None; samples = []; mx = {"rss_kib": 0, "procs": 0, "disk_bytes": 0, "swap_growth_mib": 0.0, "min_free_mib": free0}
    while p.poll() is None:
        time.sleep(1)
        if p.poll() is not None: break
        try:
            rss, n = group_rss_kib(pgid, ps_cmd); fr = vm_free_mib(); sg = swap_used_mib() - swap0; db = dir_bytes(a.out)
        except Exception as e:
            reason = "MONITOR_FAILURE"; rec["monitor_error"] = repr(e); break
        mx["rss_kib"] = max(mx["rss_kib"], rss); mx["procs"] = max(mx["procs"], n); mx["disk_bytes"] = max(mx["disk_bytes"], db)
        mx["swap_growth_mib"] = max(mx["swap_growth_mib"], sg); mx["min_free_mib"] = min(mx["min_free_mib"], fr)
        if len(samples) < 600: samples.append([round(time.time() - t0, 1), rss, fr, round(sg, 1), db])
        if rss > a.rss_mib * 1024: reason = "RSS_STOP"; break
        if fr < minfree or sg > a.swap_growth_mib: reason = "PRESSURE_STOP"; break
        if db > a.disk_mib * MIB: reason = "DISK_STOP"; break
        if time.time() - t0 > a.wall: reason = "WALL_STOP"; break
    cleanup = None
    def group_left():                                   # live (non-zombie) processes still in the group
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
    if reason:
        sig = "TERM"
        try: os.killpg(pgid, signal.SIGTERM)
        except (ProcessLookupError, PermissionError): pass
        deadline = time.time() + 5                       # wait for the WHOLE group, not just the direct child
        while time.time() < deadline and group_left() != 0:
            p.poll(); time.sleep(0.2)                          # reap the direct child as soon as it exits
        if group_left() != 0:
            sig = "TERM+KILL"
            try: os.killpg(pgid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError) as e: sig += f" ({type(e).__name__})"
            time.sleep(0.5)
        try: p.wait(timeout=5)
        except subprocess.TimeoutExpired: pass
        cleanup = {"signal": sig, "group_processes_left": group_left()}
    rc = p.returncode
    out.close(); err.close()
    if not reason:
        reason = "CPU_LIMIT" if rc in (-signal.SIGXCPU, 128 + signal.SIGXCPU, 152) or "Cputime limit" in open(os.path.join(a.out, "time_receipt.txt")).read() else ("COMPLETED" if rc == 0 else "CHILD_FAILED")
    db = dir_bytes(a.out)
    extra = {"maxima": mx, "samples_kept": samples[:600], "wall_s": round(time.time() - t0, 2), "cleanup": cleanup, "final_dir_bytes": db}
    if db > a.disk_mib * MIB and reason == "COMPLETED": reason = "DISK_STOP"
    return finish(reason, rc, extra)

if __name__ == "__main__":
    sys.exit(main())
