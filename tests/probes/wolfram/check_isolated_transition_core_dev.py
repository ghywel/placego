#!/usr/bin/env python3
"""One core-only development stage; three compiler calls, no automatic retry.

Run only under run_capped.py with the frozen caps. The driver has a four-second
CPU soft limit and each of exactly three possible sequential compiler calls has
a hard twenty-second CPU limit. Assigned computation budgets total64 seconds,
below120 seconds; supervisor overhead is reported separately. No lake/download
or deliberate compiler descendants. Use only an explicit local compiler path.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import sys


def main():
    if len(sys.argv) != 3:
        raise SystemExit("compiler and source arguments required")
    compiler, source = map(Path, sys.argv[1:])
    out = Path(os.environ["CAPPED_OUT"])
    resource.setrlimit(resource.RLIMIT_CPU, (4, 120))
    if resource.getrlimit(resource.RLIMIT_CPU) != (4, 120):
        raise SystemExit("driver CPU limit not applied")
    env = dict(os.environ, LEAN_PATH="", LEAN_NUM_THREADS="1")
    heads = ["xor_cancel", "delta_of_recurrence", "local_forcing", "ancestors_equal_or",
             "isolated_transition_forces_ancestors", "isolation_is_needed",
             "second_recurrence_is_needed", "first_recurrence_is_needed"]
    text = source.read_text()
    if any(word in text for word in ["sorry", "native_decide", "axiom "]):
        raise SystemExit("forbidden proof escape")
    proof = out / source.name
    proof.write_text(text + "\n" + "\n".join(
        "#print axioms Rule30IsolatedTransitionCore." + h for h in heads) + "\n" +
        "#check @Rule30IsolatedTransitionCore.isolated_transition_forces_ancestors\n")
    (out / "inputs.json").write_text(json.dumps({
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "compiler_sha256": hashlib.sha256(compiler.read_bytes()).hexdigest(),
        "driver_cpu_limit": [4, 120], "compiler_cpu_limit": [20, 20],
        "max_compiler_calls": 3, "threads": 1}, indent=2) + "\n")
    calls = []

    def invoke(args, label, expected):
        if len(calls) >= 3:
            raise RuntimeError("compiler-call ceiling reached")
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
            if resource.getrlimit(resource.RLIMIT_CPU) != (20, 20):
                os._exit(97)
            (out / (label + "-limits.json")).write_text(json.dumps({
                "cpu": resource.getrlimit(resource.RLIMIT_CPU),
                "file": resource.getrlimit(resource.RLIMIT_FSIZE)}))
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        with (out / (label + ".txt")).open("w") as log:
            r = subprocess.run([str(compiler)] + args, env=env, stdout=log,
                               stderr=subprocess.STDOUT, preexec_fn=limits, timeout=80)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        calls.append({"label": label, "returncode": r.returncode, "expected": expected,
                      "cpu_s": after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime})
        (out / "calls.json").write_text(json.dumps(calls, indent=2) + "\n")
        if r.returncode != expected:
            raise SystemExit("STOP: unexpected compiler result; no retry")

    invoke(["--version"], "version", 0)
    if "version 4.33.1" not in (out / "version.txt").read_text():
        raise SystemExit("unexpected development toolchain")
    invoke(["-j1", str(proof)], "positive", 0)
    log = (out / "positive.txt").read_text()
    if "warning:" in log or "error:" in log or "sorryAx" in log:
        raise SystemExit("unexpected positive diagnostic")
    for h in heads:
        if "'Rule30IsolatedTransitionCore." + h + "' does not depend on any axioms" not in log:
            raise SystemExit("missing empty-axiom report: " + h)
    negative = out / "Negative.lean"
    negative.write_text("import Init\nexample : False := by decide\n")
    invoke(["-j1", str(negative)], "negative", 1)
    bad = (out / "negative.txt").read_text()
    if "error:" not in bad or "False" not in bad or "decide" not in bad:
        raise SystemExit("negative control failed for another reason")

    # Independent literal rule30 table, not the proof's XOR/OR implementation.
    table = [0, 1, 1, 1, 1, 0, 0, 0]
    step = lambda x, y, z: table[4*x + 2*y + z]
    rows = []
    for b, a, d, h in itertools.product([0, 1], repeat=4):
        bn, an = step(b, a, d), step(a, d, h)
        admitted = not (b or a) or not (bn or an)
        assert not admitted or b == a == (b or a)
        rows.append([b, a, d, h, bn, an, admitted])
    (out / "literal-oracle.json").write_text(json.dumps(rows) + "\n")
    usage = resource.getrusage(resource.RUSAGE_SELF)
    result = {"status": "PASS_DEVELOPMENT_4331_CORE_ONLY", "headlines": len(heads),
              "axioms": [], "literal_rows": len(rows), "compiler_calls": len(calls),
              "child_cpu_s": sum(x["cpu_s"] for x in calls),
              "driver_cpu_s": usage.ru_utime + usage.ru_stime,
              "official_435_replay": "NOT_RUN", "independent_carrying_review": "PENDING"}
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
