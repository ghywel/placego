#!/usr/bin/env python3
"""run_capped_tree_controls.py (Local, L1119): controls for run_capped.py's opt-in --track-tree.

Each control runs run_capped.py on this file's `spawn` mode, which starts a grandchild in a NEW SESSION (its own process
group, as a Wolfram kernel's RunProcess/StartProcess children are, L1117) and records the grandchild's PID and start time
in CAPPED_OUT. After each run the control checks the supervisor's exit reason and whether that exact grandchild is still
alive. A grandchild left alive by a control is killed by this script, and the kill is reported.
  escape_rss   tracked; the escaped grandchild holds 300 MB under a 200 MiB cap  -> RSS_STOP, grandchild gone
  orphan       tracked; the parent exits at 2 s, the grandchild sleeps 30 s      -> LEFTOVER_CLEANED, grandchild gone
  orphan_off   the same without --track-tree (the old group-only behaviour)       -> COMPLETED, grandchild ALIVE
  clean        tracked; the grandchild exits at 1 s, the parent at 3 s           -> COMPLETED, nothing left
Prediction: all four as listed. Counterfactual: any other outcome rejects --track-tree as it stands.
Caps for every control: CPU 30, wall 60, file 4 MiB, disk 8 MiB, launch 2048 MiB, ongoing 1024 MiB, swap 256 MiB;
RSS 200 MiB for escape_rss and 2048 MiB otherwise. Nothing here touches Lean or Wolfram.
Run: python3 -I run_capped_tree_controls.py SCRATCH-DIR    (SCRATCH-DIR must not exist)
"""
import json
import os
import signal
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def start_of(pid):
    r = subprocess.run(["ps", "-o", "lstart=", "-p", str(pid)], capture_output=True, text=True)
    return r.stdout.strip() or None


def spawn(mode):
    out = os.environ["CAPPED_OUT"]
    code = {"escape_rss": "b = bytearray(300 * 1024 * 1024)\nfor i in range(0, len(b), 4096): b[i] = 1\nimport time; time.sleep(30)",
            "orphan": "import time; time.sleep(30)", "orphan_off": "import time; time.sleep(30)",
            "clean": "import time; time.sleep(1)"}[mode]
    g = subprocess.Popen([sys.executable, "-I", "-c", code], start_new_session=True,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(0.3)
    with open(os.path.join(out, "grandchild.json"), "w") as fh:
        json.dump({"pid": g.pid, "start": start_of(g.pid)}, fh)
    time.sleep({"escape_rss": 30, "orphan": 2, "orphan_off": 2, "clean": 3}[mode])


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "spawn":
        return spawn(sys.argv[2])
    scratch = sys.argv[1]
    if os.path.exists(scratch):
        print("REFUSED: scratch exists"); return 2
    os.makedirs(scratch)
    expected = {"escape_rss": ("RSS_STOP", False), "orphan": ("LEFTOVER_CLEANED", False),
                "orphan_off": ("COMPLETED", True), "clean": ("COMPLETED", False)}
    results, ok = {}, True
    for mode, (want_reason, want_alive) in expected.items():
        out = os.path.join(scratch, mode)
        cmd = [sys.executable, "-I", os.path.join(HERE, "run_capped.py"), "--out", out, "--cpu", "30", "--wall", "60",
               "--rss-mib", "200" if mode == "escape_rss" else "2048", "--file-mib", "4", "--disk-mib", "8",
               "--launch-free-mib", "2048", "--min-free-mib", "1024", "--swap-growth-mib", "256"]
        if mode != "orphan_off":
            cmd.append("--track-tree")
        cmd += ["--", sys.executable, "-I", os.path.abspath(__file__), "spawn", mode]
        subprocess.run(cmd, capture_output=True, text=True)
        rec = json.load(open(os.path.join(out, "launcher.json")))
        g = json.load(open(os.path.join(out, "grandchild.json")))
        alive = g["start"] is not None and start_of(g["pid"]) == g["start"]
        if alive:
            os.kill(g["pid"], signal.SIGKILL)
        good = rec["exit_reason"] == want_reason and alive == want_alive
        ok = ok and good
        results[mode] = {"exit_reason": rec["exit_reason"], "grandchild_alive_after": alive, "pass": good,
                         "cleanup": rec.get("cleanup"), "rss_kib_max": rec.get("maxima", {}).get("rss_kib"),
                         "procs_max": rec.get("maxima", {}).get("procs"), "killed_by_control": alive}
        print(mode, json.dumps(results[mode]))
    print("TREE_CONTROLS_PASS" if ok else "TREE_CONTROLS_FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
