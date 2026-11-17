#!/usr/bin/env python3
"""GC2093: new controls only: double SIGTERM during cleanup, broken monitor, live-process cap,
and synthetic stale-identity/failing-snapshot signalling. No Lean/Wolfram, no replay of L1119's four tests.
Run once under the separately frozen outer run_capped envelope. Retain every inner receipt on failure.
"""
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from unittest import mock

HERE = Path(__file__).resolve().parent


def identity(pid):
    r = subprocess.run(["ps", "-o", "stat=,lstart=", "-p", str(pid)], capture_output=True, text=True, timeout=3)
    parts = r.stdout.strip().split(None, 1)
    return parts[1] if r.returncode == 0 and len(parts) == 2 and not parts[0].startswith("Z") else None


def spawn(mode):
    code = "import time, signal; "
    if mode == "signal":
        code += "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
    code += "time.sleep(30)"
    g = subprocess.Popen([sys.executable, "-I", "-c", code], start_new_session=True)
    p = Path(os.environ["CAPPED_OUT"]) / "ready.json"
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps({"parent": [os.getpid(), identity(os.getpid())], "grand": [g.pid, identity(g.pid)]}))
    tmp.replace(p)
    time.sleep(30)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "spawn":
        spawn(sys.argv[2]); return 0
    root = Path(os.environ["CAPPED_OUT"])
    spec = importlib.util.spec_from_file_location("capped_control_subject", HERE / "run_capped.py")
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    checks = {}
    with mock.patch.object(h, "tree_update", side_effect=RuntimeError("no snapshot")), \
            mock.patch.object(h.os, "kill") as kill, mock.patch.object(h.os, "killpg"):
        h.kill_owned({100: "stale"}, 77, "broken", signal.SIGTERM)
        checks["failed_snapshot_never_signals_stale_pid"] = not kill.called
    rows = {100: (1, 99, 999, "S", "new"), 101: (100, 88, 100, "S", "child-new"),
            102: (1, 77, 7, "S", "ours")}
    with mock.patch.object(h, "ps_tree_rows", return_value=rows):
        owned = {100: "old"}; live, rss = h.tree_update(owned, 77, "ps")
        checks["reused_parent_does_not_adopt_unrelated_child"] = live == [102] and rss == 7 and 101 not in owned
    results = {}
    for mode, want in [("signal", "INTERRUPTED"), ("monitor", "MONITOR_FAILURE"), ("procs", "PROCESS_STOP")]:
        out = root / mode
        cmd = [sys.executable, "-I", str(HERE / "run_capped.py"), "--out", str(out), "--track-tree",
               "--cpu", "10", "--wall", "20", "--rss-mib", "128", "--file-mib", "1", "--disk-mib", "8",
               "--launch-free-mib", "2048", "--min-free-mib", "1024", "--swap-growth-mib", "256"]
        if mode == "procs": cmd += ["--max-procs", "2"]
        cmd += ["--", sys.executable, "-I", str(Path(__file__).resolve()), "spawn", mode]
        env = dict(os.environ)
        if mode == "monitor": env["CAPPED_TEST_PS"] = "bogus"
        ready = {}; p = None
        try:
            with (root / (mode + "-supervisor.log")).open("w") as log:
                p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
                deadline = time.monotonic() + 5
                while not (out / "ready.json").exists() and time.monotonic() < deadline and p.poll() is None:
                    time.sleep(0.02)
                ready = json.loads((out / "ready.json").read_text())
                if mode == "signal":
                    time.sleep(0.8)  # Allow the first ownership snapshot and the grandchild's signal handler.
                    p.send_signal(signal.SIGTERM); time.sleep(0.3); p.send_signal(signal.SIGTERM)
                p.wait(timeout=30)
            rec = json.loads((out / "launcher.json").read_text())
            gone = all(identity(pid) != start for pid, start in ready.values())
            good = rec["exit_reason"] == want and p.returncode != 0 and gone
            if mode == "signal": good = good and len(rec.get("stop_signals", [])) >= 2
            results[mode] = {"pass": good, "exit_reason": rec["exit_reason"], "owned_children_gone": gone,
                             "cleanup": rec.get("cleanup"), "stop_signals": rec.get("stop_signals", [])}
        finally:
            if p is not None and p.poll() is None:
                p.kill(); p.wait(timeout=5)
            for pid, start in ready.values():
                if start is not None and identity(pid) == start:
                    os.kill(pid, signal.SIGKILL)
    result = {"unit_checks": checks, "lifecycle_checks": results}
    (root / "lifecycle-result.json").write_text(json.dumps(result, indent=2) + "\n")
    good = all(checks.values()) and len(results) == 3 and all(r["pass"] for r in results.values())
    print(json.dumps(result)); print("LIFECYCLE_CONTROLS_PASS" if good else "LIFECYCLE_CONTROLS_FAIL")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
