"""clock_witness_extract.py: retain the cut-49 witness that L1006 reported but did not keep (GC1946's request; L1009).

Local, 2026-10-27. ONE named instance only: cut L = 49, white ticks constrained through TH = 49. There is no control
grid, no window search and no other cut. Frozen in git and proposed to GPT; it runs only after GPT agrees the
executable and caps.

What it decides and retains. It encodes the right half next to the clamped clock exactly as in
clock_right_realizability.py: x(t+1, j) = x(t, j-1) XOR (x(t, j) OR x(t, j+1)), with x(t, 0) = clock(t) and units
x(t, 1) = NOT l(t) at odd t <= TH. It adds the two guards GC1946 asked for:
  G1  The left-black prerequisite is asserted before solving: l(t) = 1 at every black tick t <= TH. Without it, the
      white-tick units would not be equivalent to keeping the clock.
  G2  The replay endpoint. A model promises the clock through TH+1 inclusive, so a first failure at or before TH+1
      is an instrument error. A replay with no failure within its horizon counts as success only if the horizon is
      at least TH+1.
Retained in CAPPED_OUT/artifacts (a fresh directory outside git, supplied by the supervisor):
  instance.cnf; kissat.out (raw stdout, including the model); right_row.txt (the initial right cells 1..TH+1);
  replay.txt (time, left, centre, right at sites -1, 0, 1 for t = 0..56, from unclamped full-line Rule 30);
  diagnostic.txt (the clamped-left l(t) for t = 41..56); manifest.json (SHA256 of each file, argv and exit status).

Prediction (copied from L1006, not new): SAT, and the replay's first failure is 52. So the clock is kept through 51
and fails at the white tick 51, where r(51) = 1 was needed.
Counterfactual: UNSAT conflicts with the earlier SAT report and requires audit. UNKNOWN is inconclusive; G1 or
replay failure is an instrument/setup failure, not a mathematical refutation. A new model need not equal the lost one.

GC1949 amendments: run ONLY under run_capped.py as specified in
reports/rule30-clock-witness-extraction-agreement.md. One Python driver and one sequential kissat child;
20 s CPU per process (not an aggregate 20 s), 10 s solver timeout, 30 s stage wall alarm plus supervisor group
cleanup, sampled 256 MiB group RSS and 1 MiB stage disk stop. Each artifact has a hard 256 KiB file ceiling.
The 256 KiB aggregate artifact target is a final acceptance check, NOT a preventative aggregate cap.
Raw stdout/stderr survive timeout. No GPU, network, retry or broader instance. A fresh artifacts subdirectory
under CAPPED_OUT is mandatory. Supervisor receipts retain killed/incomplete stages without a manifest.
"""
import hashlib
import json
import os
import resource
import signal
import subprocess
import sys
import time

CUT, TH = 49, 49
RIGHT = [int(c) for c in "0000110110001101000"]
NL = 400


def clock(t):
    return 1 if t % 2 == 0 else 0


def left_row(cut):
    left = [1 if (d % 7) in (0, 1, 2) else 0 for d in range(NL, 0, -1)]
    return [v if (NL - i) <= cut else 0 for i, v in enumerate(left)]


def diagnostic(cut, T=60):
    x = left_row(cut) + [1] + [0] * 4
    out = [x[NL - 1]]
    for t in range(T):
        y = [0] * len(x)
        for i in range(1, len(x) - 1):
            y[i] = x[i - 1] ^ (x[i] | x[i + 1])
        y[NL] = clock(t + 1)
        for i in range(NL + 1, len(y)):
            y[i] = 0
        x = y
        out.append(x[NL - 1])
    return out


def main():
    root = os.environ.get("CAPPED_OUT")
    if not root:
        raise RuntimeError("run_capped.py required; see the frozen agreement")
    out = os.path.join(os.path.realpath(root), "artifacts")
    os.makedirs(out, exist_ok=False)
    started = time.monotonic()
    resource.setrlimit(resource.RLIMIT_FSIZE, (256 * 1024, 256 * 1024))
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    signal.alarm(30)
    l = diagnostic(CUT)
    g1 = all(l[t] == 1 for t in range(0, TH + 1, 2))
    status, model, replay_rows, first_fail = "NOT RUN", None, [], None
    solver_rc, timed_out, model_checked = None, False, False
    if g1:
        var, clauses = {}, []

        def v(t, j):
            if (t, j) not in var:
                var[(t, j)] = len(var) + 1
            return var[(t, j)]

        J = lambda t: TH - t + 1
        for t in range(TH):
            for j in range(1, J(t + 1) + 1):
                y, b, c = v(t + 1, j), v(t, j), v(t, j + 1)
                o = len(var) + 1
                var[("o", t, j)] = o
                clauses += [[-b, o], [-c, o], [b, c, -o]]
                if j == 1:
                    clauses += ([[-o, -y], [o, y]] if clock(t) else [[-o, y], [o, -y]])
                else:
                    a = v(t, j - 1)
                    clauses += [[-a, -o, -y], [a, o, -y], [a, -o, y], [-a, o, y]]
        for t in range(1, TH + 1, 2):
            clauses.append([v(t, 1) if (1 - l[t]) else -v(t, 1)])
        cnf = os.path.join(out, "instance.cnf")
        with open(cnf, "x") as fh:
            fh.write("p cnf %d %d\n" % (len(var), len(clauses)))
            for cl in clauses:
                fh.write(" ".join(map(str, cl)) + " 0\n")
        stdout_path, stderr_path = os.path.join(out, "kissat.out"), os.path.join(out, "kissat.err")
        with open(stdout_path, "x") as so, open(stderr_path, "x") as se:
            try:
                r = subprocess.run(["kissat", "-q", cnf], stdout=so, stderr=se, timeout=10)
                solver_rc = r.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
        with open(stdout_path) as fh:
            raw = fh.read()
        status = ("SAT" if solver_rc == 10 and "s SATISFIABLE" in raw else
                  "UNSAT" if solver_rc == 20 and "s UNSATISFIABLE" in raw else "UNKNOWN")
        if status == "SAT":
            lits = set()
            for line in raw.splitlines():
                if line.startswith("v "):
                    lits.update(int(z) for z in line[2:].split())
            complete = all((q in lits) != (-q in lits) for q in range(1, len(var) + 1))
            model_checked = complete and all(any(q in lits for q in clause) for clause in clauses)
            if not model_checked:
                raise RuntimeError("SAT model is incomplete, inconsistent, or violates a retained clause")
            model = [1 if v(0, j) in lits else 0 for j in range(1, J(0) + 1)]
            with open(os.path.join(out, "right_row.txt"), "x") as fh:
                fh.write("".join(map(str, model)) + "\n")
            x = left_row(CUT) + [1] + model + [0] * 80
            for t in range(57):
                replay_rows.append((t, x[NL - 1], x[NL], x[NL + 1]))
                if first_fail is None and x[NL] != clock(t):
                    first_fail = t
                x = [(x[i - 1] if i else 0) ^ (x[i] | (x[i + 1] if i + 1 < len(x) else 0)) for i in range(len(x))]
            with open(os.path.join(out, "replay.txt"), "x") as fh:
                fh.write("t left centre right\n")
                for row in replay_rows:
                    fh.write("%d %d %d %d\n" % row)
    with open(os.path.join(out, "diagnostic.txt"), "x") as fh:
        fh.write("t l_clamped\n" + "".join("%d %d\n" % (t, l[t]) for t in range(41, 57)))
    g2 = status == "SAT" and len(replay_rows) >= TH + 2 and (first_fail is None or first_fail >= TH + 2)
    verdict = {"G1_left_black": g1, "status": status, "first_failure": first_fail, "G2_endpoint": g2,
               "prediction_held": status == "SAT" and first_fail == 52,
               "solver_returncode": solver_rc, "timeout": timed_out, "model_checked": model_checked}
    total = sum(os.path.getsize(os.path.join(out, f)) for f in os.listdir(out))
    if total > 256 * 1024:
        verdict["cap"] = "output over 256 KiB"
    files = {}
    for f in sorted(os.listdir(out)):
        with open(os.path.join(out, f), "rb") as fh:
            files[f] = hashlib.sha256(fh.read()).hexdigest()
    exit_status = 0 if (g1 and g2 and model_checked and "cap" not in verdict) else 1
    with open(__file__, "rb") as fh:
        source_hash = hashlib.sha256(fh.read()).hexdigest()
    payload = {"source_sha256": source_hash, "cut": CUT, "TH": TH, "verdict": verdict,
               "exit_status": exit_status, "wall_s": time.monotonic() - started, "sha256": files}
    # Include the manifest itself in the declared aggregate acceptance target.
    body = json.dumps(payload, indent=1)
    if total + len(body.encode()) > 256 * 1024:
        verdict["cap"] = "aggregate artifacts including manifest over 256 KiB"
        payload["exit_status"] = exit_status = 1
        body = json.dumps(payload, indent=1)
    with open(os.path.join(out, "manifest.json"), "x") as fh:
        fh.write(body)
    print(json.dumps(verdict))
    return exit_status


if __name__ == "__main__":
    sys.exit(main())
