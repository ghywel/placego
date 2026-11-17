#!/usr/bin/env python3
"""hostwatch.py: the SW-02 host monitor (Local, 5 November 2026; the owner's request to guard against running out of memory).

Samples every INTERVAL seconds: free + inactive memory, swap used, memory pressure, load, thermal state, the summed resident
memory of the desktop app's processes and the largest single process. Logs a line to DATA/host/watch.log.

Stops (design section 13): free + inactive under FLOOR MiB on three samples running, swap growth over GROW MiB against the
baseline taken at launch, or critical memory pressure on three samples. A stop writes DATA/HOST-STOP (q.py then refuses
new jobs), terminates a running queue job, and exits 3, so that the background task notifies Local. WARN lines (free under
WARN MiB, or pressure warn) go to the log and to DATA/host/warnings.log. No identifiers are printed: names only.
"""
import os, re, signal, subprocess, sys, time

DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
INTERVAL = int(os.environ.get("WATCH_INTERVAL", "15"))
FLOOR, WARN, GROW = 1024, 2048, 4096


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, timeout=10).stdout


def free_mib():
    out = sh("vm_stat")
    page = int(out.split("page size of ")[1].split(" bytes")[0])
    v = {}
    for line in out.splitlines()[1:]:
        if ":" in line:
            k, x = line.split(":", 1)
            v[k.strip()] = int(x.strip().rstrip("."))
    return (v["Pages free"] + v["Pages inactive"]) * page // (1 << 20)


def swap_mib():
    s = sh("sysctl", "-n", "vm.swapusage").split("used =")[1].split()[0]
    return float(s[:-1]) * {"M": 1, "G": 1024, "K": 1 / 1024}[s[-1]]


def pressure():
    return int(sh("sysctl", "-n", "kern.memorystatus_vm_pressure_level").strip() or 0)


def procs():
    app, top, name, n = 0, 0, "", 0
    for line in sh("ps", "-axo", "rss=,comm=").splitlines():
        m = re.match(r"\s*(\d+)\s+(.*)", line)
        if not m:
            continue
        rss, comm = int(m.group(1)) // 1024, m.group(2)
        base = os.path.basename(comm)[:24]
        if "Claude" in comm or "claude" in comm:
            app += rss
            n += 1
        if rss > top:
            top, name = rss, base
    return app, n, top, name


def thermal():
    t = sh("pmset", "-g", "therm")
    m = re.search(r"CPU_Speed_Limit\s*=\s*(\d+)", t)
    return int(m.group(1)) if m else -1


def stop(why, log):
    with open(os.path.join(DATA, "HOST-STOP"), "w") as f:
        f.write(why + "\n")
    print("HOST STOP:", why, file=log, flush=True)
    subprocess.run(["pkill", "-TERM", "-f", "swarm/sw02/q.py"], capture_output=True)
    print("HOST STOP:", why)
    sys.exit(3)


def main():
    os.makedirs(os.path.join(DATA, "host"), exist_ok=True)
    log = open(os.path.join(DATA, "host", "watch.log"), "a")
    warn = open(os.path.join(DATA, "host", "warnings.log"), "a")
    base = swap_mib()
    lowfree = crit = 0
    print(time.strftime("%H:%M:%S", time.gmtime()), "start swap", round(base), file=log, flush=True)
    while True:
        try:
            f, s, p = free_mib(), swap_mib(), pressure()
            app, n, top, name = procs()
            load = os.getloadavg()[0]
            th = thermal()
        except Exception as e:  # fail closed
            stop("monitor failure: %r" % (e,), log)
        stamp = time.strftime("%H:%M:%S", time.gmtime())
        print(stamp, "free", f, "swap", round(s), "grow", round(s - base), "press", p, "load", round(load, 1), "therm", th,
              "app", app, "n", n, "top", top, name, file=log, flush=True)
        lowfree = lowfree + 1 if f < FLOOR else 0
        crit = crit + 1 if p >= 4 else 0
        if f < WARN or p >= 2:
            print(stamp, "WARN free", f, "press", p, "swapgrow", round(s - base), file=warn, flush=True)
        if lowfree >= 3:
            stop("free+inactive under %d MiB on three samples (%d)" % (FLOOR, f), log)
        if s - base > GROW:
            stop("swap growth %d MiB over %d" % (s - base, GROW), log)
        if crit >= 3:
            stop("critical memory pressure on three samples", log)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
