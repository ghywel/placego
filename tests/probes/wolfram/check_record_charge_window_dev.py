#!/usr/bin/env python3
"""One bounded development-only compile; no download, lake, retry, or official replay.

Requires run_capped.py plus explicit compiler/kit arguments. Uses at most twelve
sequential compiler invocations, each with an eight-CPU-second hard limit; the
driver has a four-second CPU soft limit. Thus the assigned computational CPU
budgets sum to 100 seconds, below the outer 120-second pilot envelope. Kernel
limit granularity and the outer time/monitor overhead are recorded separately.
Lean is given one worker and no command here launches descendants deliberately.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys


def main():
    out = Path(os.environ["CAPPED_OUT"])
    compiler, kit, drafts = map(Path, sys.argv[1:])
    if len(sys.argv) != 4:
        raise SystemExit("compiler, kit lean root and draft directory required")
    resource.setrlimit(resource.RLIMIT_CPU, (4, 120))
    src, lib = out / "src", out / "lib"
    src.mkdir(); lib.mkdir()
    env = dict(os.environ, LEAN_PATH=str(lib))
    modules = ["Rule30Jen", "Rule30Diagonals", "Rule30Prize", "Rule30Window",
               "Rule30RecordCharge", "Rule30DifferenceOrder", "Rule30RightPeriods"]
    inputs = {}
    for name in modules:
        relative = Path("Ruliology/CellularAutomata") / (name + ".lean")
        target = src / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(kit / relative, target)
        inputs[str(relative)] = hashlib.sha256(target.read_bytes()).hexdigest()
    extra = ["Rule30RecordChargeWindow", "Rule30RightPeriodWindow"]
    for name in extra:
        target = src / (name + ".lean")
        shutil.copyfile(drafts / target.name, target)
        inputs[target.name] = hashlib.sha256(target.read_bytes()).hexdigest()
    (out / "inputs.json").write_text(json.dumps(inputs, indent=2) + "\n")

    records = []
    def invoke(args, label, expected=0):
        if len(records) >= 12:
            raise RuntimeError("fixed compiler-call ceiling reached")
        applied = out / (label + "-limits.json")
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU, (8, 8))
            if resource.getrlimit(resource.RLIMIT_CPU) != (8, 8):
                os._exit(97)
            applied.write_text(json.dumps({"cpu": resource.getrlimit(resource.RLIMIT_CPU),
                "file": resource.getrlimit(resource.RLIMIT_FSIZE)}))
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        with (out / (label + ".txt")).open("w") as log:
            result = subprocess.run([str(compiler)] + args, env=env, stdout=log,
                stderr=subprocess.STDOUT, preexec_fn=limits, timeout=120)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        rec = {"label": label, "rc": result.returncode,
               "cpu_s": after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
               "expected": expected}
        records.append(rec)
        (out / "calls.json").write_text(json.dumps(records, indent=2) + "\n")
        print(json.dumps(rec), flush=True)
        if result.returncode != expected:
            raise SystemExit("STOP: unexpected outcome, no retry")

    invoke(["--version"], "version")
    if "version 4.33.1" not in (out / "version.txt").read_text():
        raise SystemExit("STOP: unexpected development compiler")
    all_names = ["Ruliology.CellularAutomata." + n for n in modules] + extra
    for name in all_names:
        relative = Path(name.replace(".", "/"))
        output = (lib / relative).with_suffix(".olean")
        output.parent.mkdir(parents=True, exist_ok=True)
        invoke(["-j1", "--root=" + str(src), "-o", str(output),
                str((src / relative).with_suffix(".lean"))], name.split(".")[-1])

    control = src / "Control.lean"
    control.write_text("""module
public import Rule30RightPeriodWindow
@[expose] public section
open Ruliology.CellularAutomata
#print axioms Rule30RecordChargeWindow.shift
#print axioms Rule30RecordChargeWindow.exponent_window
#print axioms Rule30RecordChargeWindow.exponent_window_uniform
#print axioms Rule30RecordChargeWindow.exponent_window_up_to
#print axioms Rule30RightPeriodWindow.pair_window
#print axioms Rule30RightPeriodWindow.arbitrary_window
-- Unexpected boundary control: restart does not demand resource zero.
def nonzeroResource : Rule30RecordCharge.Path 0 where
  weight _ := 0
  exponent _ := 0
  resource _ := 7
  exponent_zero := rfl
  exponent_step _ := rfl
  weight_le_two _ := by decide
  reset_before _ h := by contradiction
  reset_after _ h := by contradiction
  countdown _ h := by contradiction
example : (Rule30RecordChargeWindow.shift nonzeroResource 3).resource 0 = 7 := rfl
example : Rule30RecordCharge.Q 0 0 = 0 := rfl
example : Rule30RecordCharge.Q 0 1 = 1 := by decide
example : Rule30RecordCharge.Q 0 2 = 1 := by decide
example : Rule30RecordCharge.Q 0 3 = 2 := by decide
example : Rule30RecordCharge.Q 0 18 = 2 := by decide
example : Rule30RecordCharge.Q 0 19 = 3 := by decide
""")
    invoke(["-j1", str(control)], "control")
    negative = src / "Negative.lean"
    negative.write_text("module\npublic import Rule30RightPeriodWindow\n"
                        "example : False := by decide\n")
    invoke(["-j1", str(negative)], "negative", expected=1)
    negative_text = (out / "negative.txt").read_text()
    if "error:" not in negative_text or "False" not in negative_text:
        raise SystemExit("STOP: negative control failed for an unrelated reason")
    if "sorryAx" in (out / "control.txt").read_text():
        raise SystemExit("STOP: unexpected sorry axiom")
    usage = resource.getrusage(resource.RUSAGE_SELF)
    result = {"status": "PASS_DEVELOPMENT_4331_ONLY", "compiler_calls": len(records),
              "child_cpu_s": sum(r["cpu_s"] for r in records),
              "driver_cpu_s": usage.ru_utime + usage.ru_stime,
              "official_435_check": "NOT_RUN", "independent_review": "PENDING"}
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
