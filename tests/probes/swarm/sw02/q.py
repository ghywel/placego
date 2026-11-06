#!/usr/bin/env python3
"""q.py: the SW-02 compute queue (Local, 5 November 2026; design section 13).

Every experimental command in the swarm runs through this wrapper, however short:

    python3 q.py --task ID [--cpu 60] [--wall 120] [--rss-mib 4096] -- cmd args...

What it enforces:
  * one job at a time on the host: an exclusive lock on DATA/queue/lock, waited for up to --lock-wait seconds;
  * a per-task CPU budget, kept in DATA/queue/ledger.jsonl, charged with the worker's user+system time as measured by
    /usr/bin/time inside run_capped.py (one worker per job, so `--cpu` per process is the job's budget; a job that spawns
    children must declare it with --max-procs and is charged the same way);
  * run_capped.py with --track-tree and the owner's memory rules: --rss-mib at least 4096, --swap-growth-mib 4096,
    --min-free-mib 1024; nice 10; output and disk envelopes;
  * fail closed: if DATA/HOST-STOP exists (hostwatch.py wrote it), or the ledger cannot be read, nothing runs.

Budgets: default 120 CPU seconds per task over the whole swarm; DATA/queue/budgets.json can grant a task more, and only
Local writes that file. Output: the job's stdout (first 400 lines), then one line QUEUE-RESULT with reason, cpu and run folder.
DATA comes from the environment variable SW02_DATA, or ~/placego-data/sw02.
"""
import argparse, fcntl, json, os, re, subprocess, sys, time

DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
HERE = os.path.dirname(os.path.abspath(__file__))
CAPPED = os.path.join(HERE, "..", "..", "wolfram", "run_capped.py")
DEFAULT_BUDGET = 120


def die(msg, code=3):
    print("QUEUE-REFUSED: " + msg)
    sys.exit(code)


def ledger_used(task):
    path = os.path.join(DATA, "queue", "ledger.jsonl")
    used, n = 0.0, 0
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                if r["task"] == task:
                    used += r.get("cpu", 0.0)
                    n += 1
    return used, n


def budget(task):
    path = os.path.join(DATA, "queue", "budgets.json")
    if os.path.exists(path):
        with open(path) as f:
            return float(json.load(f).get(task, DEFAULT_BUDGET))
    return float(DEFAULT_BUDGET)


def cpu_from_receipt(run):
    """user + sys seconds from the /usr/bin/time -l receipt that run_capped writes."""
    try:
        txt = open(os.path.join(run, "time_receipt.txt"), errors="replace").read()
    except OSError:
        return None
    m = re.search(r"([\d.]+)\s+real\s+([\d.]+)\s+user\s+([\d.]+)\s+sys", txt)
    return float(m.group(2)) + float(m.group(3)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--cpu", type=int, default=60)
    ap.add_argument("--wall", type=int, default=120)
    ap.add_argument("--rss-mib", type=int, default=4096)
    ap.add_argument("--max-procs", type=int, default=3)
    ap.add_argument("--file-mib", type=int, default=16)
    ap.add_argument("--disk-mib", type=int, default=128)
    ap.add_argument("--lock-wait", type=int, default=1500)
    ap.add_argument("--lane", default="small", choices=["small", "bench"])  # bench: the one substantive job; small: seconds-long checks
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
    if not cmd:
        die("no command")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", a.task):
        die("bad task id")
    if a.rss_mib < 4096:
        a.rss_mib = 4096  # the owner's rule, 4 November 2026
    q = os.path.join(DATA, "queue")
    os.makedirs(os.path.join(q, "runs"), exist_ok=True)
    if a.lane == "small" and (a.cpu > 120 or a.wall > 180):
        die("the small lane takes jobs up to 120 CPU seconds and 180 s wall; a longer job goes in your report for Local's queue", 7)
    if os.path.exists(os.path.join(DATA, "HOST-STOP")):
        die("host stop is set; try again later or report that the test could not run", 4)
    # one job at a time per lane, and one job at a time per task across both lanes (GC2688)
    tlock = open(os.path.join(q, "task-%s.lock" % a.task), "w")
    lock = open(os.path.join(q, "lock" if a.lane == "small" else "lock-bench"), "w")
    t0 = time.time()
    for lk in (tlock, lock):
        while True:
            try:
                fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.time() - t0 > a.lock_wait:
                    die("queue busy for %d s" % a.lock_wait, 5)
                time.sleep(1.0)
    used, n = ledger_used(a.task)
    b = budget(a.task)
    if used + a.cpu > b + 1e-9:
        left = b - used
        die("task %s has %.1f of %.0f CPU seconds left; ask for less with --cpu, or put the test in your report for Local's queue" % (a.task, max(left, 0), b), 6)
    run = os.path.join(q, "runs", "%s-%03d-%d" % (a.task, n + 1, os.getpid()))
    full = [sys.executable, CAPPED, "--out", run, "--cpu", str(a.cpu), "--wall", str(a.wall), "--rss-mib", str(a.rss_mib),
            "--file-mib", str(a.file_mib), "--disk-mib", str(a.disk_mib), "--min-free-mib", "1024", "--launch-free-mib", "2048",
            "--swap-growth-mib", "4096", "--track-tree", "--max-procs", str(a.max_procs), "--", "nice", "-n", "10"] + cmd
    start = time.time()
    r = subprocess.run(full, capture_output=True, text=True)
    wall = time.time() - start
    reason, charged = "UNKNOWN", None
    try:
        j = json.load(open(os.path.join(run, "launcher.json")))
        reason = j.get("exit_reason", "UNKNOWN")
    except (OSError, ValueError):
        pass
    charged = cpu_from_receipt(run)
    missing_receipt = charged is None
    if missing_receipt:
        charged = float(a.cpu)  # no receipt: charge the whole allowance, and mark it for reconciliation (GC2688)
    with open(os.path.join(q, "ledger.jsonl"), "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps({"task": a.task, "n": n + 1, "cpu": round(charged, 3), "wall": round(wall, 3), "reason": reason, "at": int(time.time()), "lane": a.lane, "missing_receipt": missing_receipt}) + "\n")
    out = os.path.join(run, "out.txt")
    if os.path.exists(out):
        with open(out, errors="replace") as f:
            for i, line in enumerate(f):
                if i >= 400:
                    print("[output cut at 400 lines; the rest is in the run folder]")
                    break
                sys.stdout.write(line[:2000])
    if reason != "COMPLETED":
        tail = (r.stdout + r.stderr)[-1500:]
        print(tail)
    print("QUEUE-RESULT reason=%s cpu=%.3f wall=%.1f left=%.1f run=%s" % (reason, charged, wall, b - used - charged, os.path.relpath(run, DATA)))
    sys.exit(0 if reason == "COMPLETED" else 2)


if __name__ == "__main__":
    main()
