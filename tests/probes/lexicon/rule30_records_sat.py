#!/usr/bin/env python3
"""rule30_records_sat.py: the record zero runs of lead 1 (records.c), found from the crib, not by enumeration.
(Local, 2026-10-05; the owner's Enigma lead: Turing and Welchman did not try every key, they ran the crib through the
machine and let contradictions prune. A SAT solver is the Bombe's descendant.)

RUN-ON:     cpu, one core per solver call (kissat 4 or CaDiCaL 3 on the PATH)
COMMAND:    python3 tests/probes/lexicon/rule30_records_sat.py check [SOLVER=kissat] [TIMEOUT=600]
            python3 tests/probes/lexicon/rule30_records_sat.py ask D R [SOLVER] [TIMEOUT]
COST:       the controls (depths 3 .. 41) in minutes; the timing ladder (53 .. 73) up to TIMEOUT per call.

The question asked of the solver: is there a column 1 (column 0 = 0101...) whose forced left half has zeros at every
depth d, d+1, ..., d+R-1? records.c's R(d) is the largest R for which the answer is yes. The encoding is the
anti-diagonal recurrence of records.c, A_k[j] = A_k[j-1] XOR (A_{k-1}[j-1] OR A_{k-2}[j-2]), A_k[0] = k mod 2, with
c(k-1) in place of A_{k-2}[-1]; every cell of the triangle up to depth d+R-1 is a variable (constants folded), each
OR and XOR a gate in CNF, and the crib is d..d+R-1 forced to 0. Column 1 at odd times is hidden (Lemma 1) and set to 0,
as records.c does; its even-time bits are the only free variables.
A satisfying column 1 is checked by an independent simulator: the left half built cell by cell from the left-parent
rule x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1)), never through the diagonals.

Why this might beat enumeration. records.c tries all 2^(d/2) prefixes and only then meets the crib (Lemma 4 makes the
run a single forced walk, so the prefixes are the whole cost). A CDCL solver can branch on any bit, in any order,
propagate the crib backwards through the gates, and learn each contradiction once.

PREDICTIONS, written 2026-10-05 before this script's first run. Known: R(d) from records.c/records_fast.c
(41: 37; 53: 45; 57: 45; 61: 49; 65: 57; 69: 55; 73: 59), and records.c's wall times on the M5's 10 cores
(53: 0.9 s, 61: 14 s, 65: 57 s, 69: 3.9 min; that is 9, 140, 570 and 2,350 core-seconds).
  S0 (control, must hold): for every odd depth d from 3 to 41, "R(d)" is SAT, the witness passes the independent
     simulator, and "R(d) + 1" is UNSAT, with R(d) from records_fast.c. Anything else voids the rest.
  S1 (blind): finding a record witness (the SAT call at R(d)) is at least 10x faster than records.c's core-seconds at
     every depth from 53 to 73.
  S2 (blind): proving the record (the UNSAT call at R(d) + 1) is SLOWER than records.c's core-seconds from depth 65 on:
     the crib finds keys fast, but proving that no key exists is still a search of the space.
REFUTED-BY: S0 failing (the encoding); S1 or S2 the other way round.
"""
import os, re, subprocess, sys, tempfile, time

TRUE, FALSE = "T", "F"


class CNF:
    def __init__(self):
        self.n = 0
        self.clauses = []

    def var(self):
        self.n += 1
        return self.n

    def OR(self, a, b):
        if a == TRUE or b == TRUE: return TRUE
        if a == FALSE: return b
        if b == FALSE: return a
        if a == b: return a
        if a == -b: return TRUE
        o = self.var()
        self.clauses += [[-a, o], [-b, o], [a, b, -o]]
        return o

    def XOR(self, a, b):
        if a == FALSE: return b
        if b == FALSE: return a
        if a == TRUE: return FALSE if b == TRUE else -b
        if b == TRUE: return -a
        if a == b: return FALSE
        if a == -b: return TRUE
        x = self.var()
        self.clauses += [[-a, -b, -x], [a, b, -x], [a, -b, x], [-a, b, x]]
        return x


def encode(d, R):
    """CNF for: zeros at depths d .. d+R-1. Returns (cnf, {time: var} for column 1's even bits, contradiction?)."""
    f = CNF()
    K = d + R - 1
    col1 = {}
    def c(t):
        if t % 2: return FALSE                               # hidden bit, as records.c
        if t not in col1: col1[t] = f.var()
        return col1[t]
    Q, P = [], [FALSE]                                       # A_{-1} = (), A_0 = (tau(0)) = (0)
    contradiction = False
    for k in range(1, K + 1):
        A = [TRUE if k % 2 else FALSE]
        for j in range(1, k + 1):
            x = f.OR(P[j - 1], c(k - 1) if j == 1 else Q[j - 2])
            A.append(f.XOR(A[j - 1], x))
        if k >= d:                                           # the crib: the cell at depth k is 0
            cell = A[k]
            if cell == TRUE: contradiction = True
            elif cell != FALSE: f.clauses.append([-cell])
        Q, P = P, A
    return f, col1, contradiction


def forced_row(bits, K):
    """Independent: the forced left half from columns 0 (t mod 2) and 1 (bits), by the left-parent rule; returns
    x_0(-1) .. x_0(-K)."""
    T = K + 1
    right = [(t % 2) for t in range(T + 1)]                  # column 0
    far = [bits.get(t, 0) if t % 2 == 0 else 0 for t in range(T + 2)]   # column 1
    row = []
    for depth in range(1, K + 1):                            # column -depth from columns -depth+1, -depth+2
        n = T + 1 - depth
        col = [right[t + 1] ^ (right[t] | far[t]) for t in range(n)]
        row.append(col[0])
        far, right = right, col
    return row


def solve(cnf, solver, timeout):
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as fh:
        fh.write(f"p cnf {cnf.n} {len(cnf.clauses)}\n")
        fh.write("".join(" ".join(map(str, cl)) + " 0\n" for cl in cnf.clauses))
        path = fh.name
    cmd = [solver, f"--time={timeout}", path] if solver == "kissat" else [solver, "-t", str(timeout), path]
    t0 = time.time()
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    dt = time.time() - t0
    os.unlink(path)
    if re.search(r"^s SATISFIABLE", out, re.M):
        vals = set()
        for ln in out.splitlines():
            if ln.startswith("v "):
                vals.update(int(x) for x in ln[2:].split() if int(x) > 0)
        return "SAT", vals, dt
    if re.search(r"^s UNSATISFIABLE", out, re.M):
        return "UNSAT", None, dt
    return "UNKNOWN", None, dt


def ask(d, R, solver, timeout):
    cnf, col1, contra = encode(d, R)
    if contra:
        return "UNSAT", None, 0.0, cnf
    status, vals, dt = solve(cnf, solver, timeout)
    bits = None
    if status == "SAT":
        bits = {t: (1 if v in vals else 0) for t, v in col1.items()}
    return status, bits, dt, cnf


def run_length(bits, d, K):
    row = forced_row(bits, K)
    r = 0
    while d + r <= K and row[d + r - 1] == 0:
        r += 1
    return r


def records_fast(d):
    here = os.path.dirname(os.path.abspath(__file__))
    exe = os.path.join(tempfile.gettempdir(), "records_fast_sat")
    if not os.path.exists(exe):
        lib = next((p for p in ("/opt/homebrew/opt/libomp", "/usr/local/opt/libomp") if os.path.isdir(p)), None)
        omp = ["-Xpreprocessor", "-fopenmp", f"-I{lib}/include", f"-L{lib}/lib", "-lomp"] if lib else ["-fopenmp"]
        subprocess.run(["cc", "-O3", "-mcpu=apple-m1"] + omp + ["-o", exe, os.path.join(here, "records_fast.c")],
                       check=True)
    out = subprocess.run([exe, str(d), "2"], capture_output=True, text=True, check=True).stdout
    return int(out.split()[2])


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode == "ask":
        d, R = int(sys.argv[2]), int(sys.argv[3])
        solver = sys.argv[4] if len(sys.argv) > 4 else "kissat"
        timeout = int(sys.argv[5]) if len(sys.argv) > 5 else 600
        st, bits, dt, cnf = ask(d, R, solver, timeout)
        extra = ""
        if st == "SAT":
            extra = f"; witness run {run_length(bits, d, d + R + 40)} (independent simulator)"
        print(f"ASK d {d} R {R} {solver}: {st} in {dt:.2f} s ({cnf.n} vars, {len(cnf.clauses)} clauses){extra}",
              flush=True)
        return
    solver = sys.argv[2] if len(sys.argv) > 2 else "kissat"
    timeout = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    fails = 0
    for d in range(3, 42, 2):
        R = records_fast(d)
        st1, bits, dt1, _ = ask(d, R, solver, timeout)
        ok1 = st1 == "SAT" and run_length(bits, d, d + R + 40) >= R
        st2, _, dt2, _ = ask(d, R + 1, solver, timeout)
        ok2 = st2 == "UNSAT"
        fails += (not ok1) + (not ok2)
        print(f"  d {d:2d}: R {R:2d}  at R {st1} {dt1:6.2f} s{'' if ok1 else '  FAIL'};  at R+1 {st2} {dt2:6.2f} s"
              f"{'' if ok2 else '  FAIL'}", flush=True)
    print(f"S0 {'PASSED' if fails == 0 else 'FAILED'} ({fails} failures)")


if __name__ == "__main__":
    main()
