#!/usr/bin/env python3
"""kernel_watch.py: stage limits for a notebook build in the Wolfram MCP kernel (Local, L1116).

run_capped.py supervises a child it starts; the MCP kernel is started by its own server, so this watcher attaches to
an existing kernel process instead. Every second it samples the kernel's whole process tree (the PID and all its
descendants, from `ps -A -o pid=,ppid=,rss=`), free+inactive memory (vm_stat) and swap use (sysctl vm.swapusage), and
appends one JSON line to the log. It stops the tree (SIGTERM, then SIGKILL after 5 s) when
  * the tree's summed RSS exceeds --rss-mib, or
  * free+inactive falls below --min-free-mib, or
  * swap use grows by more than --swap-growth-mib over its value at attach, or
  * --wall seconds pass,
and records the reason. A monitor failure also stops the tree, never reads as zero. It exits when the kernel is gone,
or when --until-file appears (the build finished and the caller wants the kernel kept for reading outputs), printing
one summary line. Only a PID whose parent is the given --parent is accepted, so another session's kernel is never
touched.

Run: python3 -I kernel_watch.py --pid PID --parent PPID --rss-mib M --min-free-mib F --swap-growth-mib W --wall S
     --log FILE [--until-file FILE]
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import time


def vm_free_mib():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True, timeout=5).stdout
    page = int(out.split("page size of ")[1].split(" bytes")[0])
    vals = {}
    for line in out.splitlines()[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            vals[k.strip()] = int(v.strip().rstrip("."))
    return (vals["Pages free"] + vals["Pages inactive"]) * page // (1 << 20)


def swap_used_mib():
    out = subprocess.run(["sysctl", "-n", "vm.swapusage"], capture_output=True, text=True, timeout=5).stdout
    used = out.split("used =")[1].split()[0]
    return float(used[:-1]) * {"M": 1, "G": 1024, "K": 1 / 1024}[used[-1]]


def tree(root):
    r = subprocess.run(["ps", "-A", "-o", "pid=,ppid=,rss="], capture_output=True, text=True, timeout=5)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError("ps failed")
    rows = {}
    for line in r.stdout.splitlines():
        f = line.split()
        if len(f) != 3:
            raise RuntimeError("ps unparsable")
        rows[int(f[0])] = (int(f[1]), int(f[2]))
    if root not in rows:
        return None, 0
    members, frontier = {root}, [root]
    while frontier:
        p = frontier.pop()
        for pid, (ppid, _) in rows.items():
            if ppid == p and pid not in members:
                members.add(pid)
                frontier.append(pid)
    return members, sum(rows[p][1] for p in members)


def stop(members):
    for sig in (signal.SIGTERM, signal.SIGKILL):
        for p in members:
            try:
                os.kill(p, sig)
            except ProcessLookupError:
                pass
        if sig == signal.SIGTERM:
            time.sleep(5)


def main():
    ap = argparse.ArgumentParser()
    for k in ("pid", "parent", "rss-mib", "min-free-mib", "swap-growth-mib", "wall"):
        ap.add_argument("--" + k, type=int, required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--until-file")
    a = ap.parse_args()
    ps = subprocess.run(["ps", "-o", "ppid=", "-p", str(a.pid)], capture_output=True, text=True)
    if ps.returncode != 0 or int(ps.stdout.strip() or -1) != a.parent:
        print("REFUSED: PID is not a child of the given parent")
        sys.exit(2)
    start, swap0 = time.time(), swap_used_mib()
    peak, minfree, reason, last = 0, 10 ** 9, None, {a.pid}
    with open(a.log, "a") as log:
        while True:
            t = time.time() - start
            try:
                members, kib = tree(a.pid)
                free, swap = vm_free_mib(), swap_used_mib()
            except Exception as e:
                members, kib = None, 0
                reason = "MONITOR_FAILURE " + str(e)
            if members is None and reason is None:
                reason = "KERNEL_GONE"
                break
            if reason is None:
                last = members
                peak, minfree = max(peak, kib), min(minfree, free)
                log.write(json.dumps({"t": round(t, 1), "rss_kib": kib, "procs": len(members), "free_mib": free,
                                      "swap_growth_mib": round(swap - swap0, 1)}) + "\n")
                log.flush()
                if kib > a.rss_mib * 1024:
                    reason = "RSS_STOP"
                elif free < a.min_free_mib:
                    reason = "PRESSURE_STOP"
                elif swap - swap0 > a.swap_growth_mib:
                    reason = "SWAP_STOP"
                elif t > a.wall:
                    reason = "WALL_STOP"
                elif a.until_file and os.path.exists(a.until_file):
                    reason = "UNTIL_FILE"
                    break
            if reason is not None:
                try:
                    members, _ = tree(a.pid)
                except Exception:
                    members = last
                if members:
                    stop(members)
                break
            time.sleep(1)
    print(json.dumps({"reason": reason, "peak_rss_kib": peak, "min_free_mib": minfree, "wall_s": round(time.time() - start, 1),
                      "swap_at_attach_mib": swap0}))


if __name__ == "__main__":
    main()
