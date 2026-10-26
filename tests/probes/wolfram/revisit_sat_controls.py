#!/usr/bin/env python3
"""revisit_sat_controls.py: harmless containment controls for revisit_sat.py's single-group architecture (Local, 2026-10-26, L974).

Each control is one stage under run_capped.py; no SAT solver, checker or dynamics runs. Usage (one control per stage):
  REVISIT_SAT_OUT=<dest> python3 run_capped.py --out <dest> ... -- python3 revisit_sat_controls.py <name>
Controls and the outcome each must show:
  normal     a quick tool returns rc 0 with no leftover; supervisor COMPLETED.
  timeout    a tool sleeping past its 1 s timeout is killed; the driver ends with TOOL_TIMEOUT; no group member left.
  leftover   a tool that leaves a background grandchild ends the driver with LEFTOVER; the supervisor then cleans the group:
             LEFTOVER_CLEANED (or a failure exit with cleanup recorded), and nothing of the group survives.
  filecap    a tool writing 2 MB to one file is stopped by the 1 MiB RLIMIT_FSIZE; the file is at most 1 MiB.
  cpu        with the CPU budget set 2 s above the current total, a busy tool is killed by the sampled budget (CPU_BUDGET).
  binding    the driver main() refuses when REVISIT_SAT_OUT differs from CAPPED_OUT (exit 3).
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import revisit_sat as R

def main():
    name = sys.argv[1]
    R.OUT = os.environ["REVISIT_SAT_OUT"]
    stem = os.path.join(R.OUT, "ctl_" + name)
    try:
        if name == "normal":
            rc, _ = R.run_tool(["/bin/sh", "-c", "echo ok"], stem, 5); print(f"normal rc {rc}")
        elif name == "timeout":
            R.run_tool(["/bin/sleep", "10"], stem, 1); print("timeout NOT stopped")
        elif name == "leftover":
            R.run_tool(["/bin/sh", "-c", "/bin/sleep 30 & exit 0"], stem, 5); print("leftover NOT detected")
        elif name == "filecap":
            rc, _ = R.run_tool([sys.executable, "-c", f"open({stem + '.big'!r},'wb').write(b'0'*2000000)"], stem, 10)
            print(f"filecap rc {rc} size {os.path.getsize(stem + '.big')}")
        elif name == "cpu":
            R.CPU_BUDGET = R.cpu_total() + 2.0
            R.run_tool([sys.executable, "-c", "while True: pass"], stem, 30); print("cpu NOT stopped")
        elif name == "binding":
            os.environ["REVISIT_SAT_OUT"] = "/tmp"; R.OUT = "/tmp"
            print(f"binding main() returned {R.main()}")
    except SystemExit as e:
        print(f"{name} driver stop: {e}")
        print(f"strangers after stop: {len(R.strangers())}")
        raise
    print(f"strangers at end: {len(R.strangers())}")

if __name__ == "__main__":
    main()
