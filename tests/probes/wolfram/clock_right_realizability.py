"""clock_right_realizability.py: can ANY finite right row keep the cut clock to its three-screen bound? (L1006, DQ-023)

Local, 2026-10-27, after GC1942/GC1943. An exact decision, not an edit-family census. Frozen in git before it runs.

Setting (GC1938, GC1942). The reference is c137e0's natural clock: a 7-periodic infinite left half and a finite right
row. A cut L keeps the left half through depth L. While every beat is kept, the centre equals the clock (black at even
t), and the left half is the clamped-left diagnostic, so the left neighbour l(t) is known. A beat is kept exactly when
l(t) = 1 at each black tick and r(t) = NOT l(t) at each white tick. Only right cells 1..TH+1 can affect site 1 by time
TH. So "some finite right row keeps every beat through TH+1" is a finite SAT question. The right half evolves next to
the clamped clock column and must meet the white-tick values up to TH.

Encoding. Variables x(t, j) for 0 <= t <= TH and 1 <= j <= TH - t + 1. The update is
x(t+1, j) = x(t, j-1) XOR (x(t, j) OR x(t, j+1)), with x(t, 0) = clock(t), using an auxiliary variable for the OR. The
units are x(t, 1) = NOT l(t) at every odd t <= TH. Every model is replayed end to end: the cut left half, centre 1 and
the model's right cells evolve by unclamped full-line Rule 30. Its first failure must be the predicted one.

Predictions (written before the run):
  C1 (positive control, known): cut 21 with TH = 21 is SAT (GC1940's flips 10 and 12), and its replay fails at 23.
  C2 (negative control, known): cut 23 with TH = 27 is UNSAT (no-11: r(25) = r(27) = 1 required).
  C3 (negative control, known): cut 15 with TH = 15 is UNSAT (no-11 at 13, 15).
  C4 (sanity): the uncut reference with TH = 55 is SAT, and its replay keeps the clock through 56.
  P_R (the question): cut 49 with TH = 55 is SAT. A finite right row then keeps the clock through 56, and the replay
      fails at exactly 57 (black tick 56 has l = 0). Gut confidence is about 55 per cent.
  Counterfactual: if cut 49 is UNSAT at some odd TH < 55, a fourth obstruction exists beyond the three screens. The
      smallest such TH is then reported, and the outcome is retained either way.
Caps: kissat with a 60 s timeout per instance; a timeout is UNKNOWN, never UNSAT. One process. Instances have under
2,000 cell variables.
Record searched: "right-visible", "J(L,B,n)" (GC1804, the finite CQ01 language), "col1_five_check" (GC1943),
"no11" (Lemma 3, GC1941).

Run: python3 -I tests/probes/wolfram/clock_right_realizability.py   (exit 1 on a control failure)
"""
import subprocess
import sys
import tempfile

RIGHT = [int(c) for c in "0000110110001101000"]
NL = 400
T_DIAG = 140


def clock(t):
    return 1 if t % 2 == 0 else 0


def left_diag(cut):
    left = [1 if (d % 7) in (0, 1, 2) else 0 for d in range(NL, 0, -1)]
    if cut is not None:
        left = [v if (NL - i) <= cut else 0 for i, v in enumerate(left)]
    x = left + [1] + [0] * 4
    out = [x[NL - 1]]
    for t in range(T_DIAG):
        y = [0] * len(x)
        for i in range(1, len(x) - 1):
            y[i] = x[i - 1] ^ (x[i] | x[i + 1])
        y[NL] = clock(t + 1)
        for i in range(NL + 1, len(y)):
            y[i] = 0                                  # the clamped-left diagnostic never reads the right side
        x = y
        out.append(x[NL - 1])
    return out


def solve(cut, TH):
    l = left_diag(cut)
    var = {}

    def v(t, j):
        if (t, j) not in var:
            var[(t, j)] = len(var) + 1
        return var[(t, j)]

    clauses = []
    J = lambda t: TH - t + 1
    for t in range(TH):
        for j in range(1, J(t + 1) + 1):
            y = v(t + 1, j)
            b, c = v(t, j), v(t, j + 1)
            o = len(var) + 1
            var[("o", t, j)] = o
            clauses += [[-b, o], [-c, o], [b, c, -o]]
            if j == 1:                               # left input is the clamped clock
                if clock(t):
                    clauses += [[-o, -y], [o, y]]    # y = NOT o
                else:
                    clauses += [[-o, y], [o, -y]]    # y = o
            else:
                a = v(t, j - 1)
                clauses += [[-a, -o, -y], [a, o, -y], [a, -o, y], [-a, o, y]]
    for t in range(1, TH + 1, 2):
        want = 1 - l[t]
        clauses.append([v(t, 1) if want else -v(t, 1)])
    n = len(var)
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as fh:
        fh.write("p cnf %d %d\n" % (n, len(clauses)))
        for cl in clauses:
            fh.write(" ".join(map(str, cl)) + " 0\n")
        path = fh.name
    try:
        r = subprocess.run(["kissat", "-q", path], capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return "UNKNOWN", None, n, len(clauses)
    status = "SAT" if "s SATISFIABLE" in r.stdout else ("UNSAT" if "s UNSATISFIABLE" in r.stdout else "UNKNOWN")
    model = None
    if status == "SAT":
        lits = set()
        for line in r.stdout.splitlines():
            if line.startswith("v "):
                lits.update(int(z) for z in line[2:].split())
        model = [1 if v(0, j) in lits else 0 for j in range(1, J(0) + 1)]
    return status, model, n, len(clauses)


def replay(cut, right_cells, T=200):
    left = [1 if (d % 7) in (0, 1, 2) else 0 for d in range(NL, 0, -1)]
    if cut is not None:
        left = [v if (NL - i) <= cut else 0 for i, v in enumerate(left)]
    x = left + [1] + list(right_cells) + [0] * (T + 5)
    for t in range(T + 1):
        if x[NL] != clock(t):
            return t
        y = [0] * len(x)
        for i in range(1, len(x) - 1):
            y[i] = x[i - 1] ^ (x[i] | x[i + 1])
        x = y
    return None


fails = 0
plan = [("C1", 21, 21, "SAT", 23), ("C2", 23, 27, "UNSAT", None), ("C3", 15, 15, "UNSAT", None),
        ("C4", None, 55, "SAT", None)]
for name, cut, TH, want, want_fail in plan:
    status, model, n, m = solve(cut, TH)
    f = replay(cut, model) if model else None
    ok = status == want and (want_fail is None or f == want_fail) and (name != "C4" or f is None or f > TH + 1)
    fails += not ok
    print("%s cut %s TH %d: %s (%d vars, %d clauses); replay first failure %s -> %s" % (name, cut, TH, status, n, m, f, "PASS" if ok else "FAIL"))
results = {}
for TH in (49, 51, 53, 55):
    status, model, n, m = solve(49, TH)
    f = replay(49, model) if model else None
    results[TH] = (status, f)
    print("P_R cut 49 TH %d: %s (%d vars); replay first failure %s" % (TH, status, n, f))
    if status == "SAT" and (f is None or f <= TH):
        print("  model replay contradicts the encoding: instrument error")
        fails += 1
print("P_R:", "HELD" if results[55][0] == "SAT" and results[55][1] == 57 else "NOT HELD (outcome retained above)")
print("controls:", "ALL PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
