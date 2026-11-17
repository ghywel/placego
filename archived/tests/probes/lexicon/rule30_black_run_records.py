#!/usr/bin/env python3
"""rule30_black_run_records.py: 8.82's black-run records Q and P in git, the exact coupling checked, and each record
depth classified by the coupling term that carries it (RULE30-PRIZE.md 8.95; claimed in CHAT-LEDGER L657, the question
named in L658 after GPT's GC1167 advice).

8.82's exact coupling of the two wall phases (S = white start, B = black start; "end" = first depth after the run):
    E_B(d) = max(d, E_S(d-1) - 1, Q_S(d) - 1, P_S(d) - 1),     E_S(d) = max(d, E_B(d-1) - 1, Q_B(d) - 1, P_B(d) - 1),
with E_P(d) = d + R_P(d) the end of the longest zero run from depth d, Q_P(d) the end of the longest run of ones from
depth d, and P_P(d) the end of the longest 1, 0, 1, 1, ... pattern begun at depth d - 1. R_S = R (8.36), R_B = R° (8.82,
GC1043's phase-correct game). R°(1..62), Q and P were third-party (swarm lane q2) and not in git.

Engines: records_pattern.c (a variant of the frozen records.c: the same anti-diagonal recurrence with a phase parameter
and a target pattern), records.c (V1), leftside_survivors.c through GC1166's bridge (V2), and a pure-Python forward
simulation of the wall form (V4).

RUN-ON:     cpu, 10 threads (OpenMP; ompflags.py)
COMMAND:    python3 tests/probes/lexicon/rule30_black_run_records.py [DMAX=40]
COST:       several minutes; the deepest P and Z runs dominate.

Record searched: 'black-run', 'Q_S', 'R°', 'coupling' -> 8.82, CL215/CL216 (CHAT-LEDGER.12.md), KIMI-QUESTIONS-3.md,
GC1043, GC1166, GC1167 (the W = 31 champion's standard-phase parent is a P birth).

PREDICTIONS (CHAT-LEDGER L657 and L658, pushed at 232781f7 and e07324c5 before any run).
  V1 must hold: E_S(d) - d from the new engine equals records.c's R(d), d = 3 .. 33.
  V2 must hold: E_B(d) - d equals the census-derived R°(d) (GC1166's bridge), d = 1 .. 33.
  V3 must hold if 8.82's coupling and this reading of its definitions are right: both identities, d = 2 .. DMAX.
  V4 must hold (independent code path): Q_P(d) and P_P(d) in both phases from a pure-Python forward simulation of the
     wall form equal the engine's, d = 2 .. 12.
  C1 must not fail silently: no run reaches the engine's cap (no "CAP").
  K  blind (L658): the black-start peaks R°(12) = 19 and R°(32) = 35 are attained by the P term; ordinary depths by the
     shifted zero record; the Q term alone attains no record at any depth 2 .. DMAX in either identity.
     REFUTED-BY: a depth whose maximum is attained by Q alone, or either peak not attained by P.

OUTCOME (2026-10-13, M5; machine output quoted): V1, V2, V3, V4, C1 HELD; K REFUTED (seen first in the depth-14 smoke run).
  V1: R(d) = records.c's at d = 3 .. 33. V2: R°(d) = the census bridge at d = 1 .. 33. V3: both coupling identities hold
  exactly at every d = 2 .. 40. V4: the forward simulation agrees for Q and P, both phases, d = 2 .. 12. No cap.
  Tables, d = 2 .. 40 (exclusive ends):
    Q_S: 4, 4, 8, 8, 10, 10, 14, 14, 18, 20, 20, 32, 32, 34, 34, 34, 34, 34, 34, 40, 40, 42, 42, 44, 44, 46, 50, 50, 50, 50, 68, 68, 68, 68, 68, 68, 68, 74, 74
    P_S: 4, 8, 6, 8, 8, 12, 14, 12, 20, 16, 32, 18, 30, 34, 22, 30, 32, 32, 40, 32, 38, 42, 42, 44, 46, 44, 50, 50, 50, 54, 68, 56, 66, 64, 64, 64, 64, 68, 76
    Q_B: 3, 9, 9, 9, 11, 11, 11, 13, 19, 19, 19, 31, 31, 31, 33, 33, 33, 33, 35, 39, 39, 43, 43, 45, 45, 45, 45, 47, 49, 51, 57, 57, 67, 67, 67, 67, 71, 71, 79
    P_B: 9, 5, 7, 7, 11, 11, 11, 19, 17, 17, 17, 25, 25, 23, 33, 27, 33, 35, 31, 35, 37, 43, 45, 43, 43, 43, 45, 47, 51, 55, 57, 67, 59, 63, 65, 63, 71, 71, 79
  K: the Q term alone attains the maximum in 26 of the 78 (d, phase) cases (Q alone 26, Q and P 15, E and Q 14, P alone
  13, all three 7, E and P 2, E alone 1, at white start d = 29). R°(12) = 19 is P alone (predicted); R°(32) = 35 is Q
  and P tied. The largest black-run end minus 2d is 5 for Q_B (d = 13) and P_B (d = 2), and 8 for P_S (d = 12), with
  6 for Q_S (d = 13); through the coupling these give the sharp R(13) = 17 = 13 + 4 and R°(12) = 19 = 12 + 7, and no
  larger excess appears to d = 40. P_S(32) = 68 is GC1167's reconstructed parent (1 at 31, 0 at 32, ones 33 .. 67).
CORRECTION (2026-10-13 13:36 BST, after GPT's pointer in GC1168): the "Record searched" line above overstates the search. The
  terms were grepped in tests/ and in the named sections, not run through record_find. record_find 'Q and P' and
  'coupling' hit STRATEGY-PLAN.md D3, which had already COMPUTED Q and P in both phases and the coupling to depth
  60 (a swarm agent and its skeptic) and PROVED the leaky-max form Psi(d) = max(-d, Psi(d-1) - 3, b(d)), so the
  coupled system is bounded if and only if the births are. This probe's tables duplicate D3's to 40; what it adds
  is a committed engine and tables, and the term-by-term classification.
"""
import pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ompflags import OMP

def wall_pattern_end(phase, mode, d):
    """Pure-Python forward simulation of the wall form: the largest exclusive end of the target pattern over every
    compatible row 0 (depth j forced when j - 1 is a black time; free otherwise). Independent of the anti-diagonal code."""
    start = d - 1 if mode == "P" else d
    tau = lambda t: (t + phase) & 1
    tgt = lambda j: 0 if mode == "Z" else (1 if mode == "Q" else (0 if j == d else 1))
    def neighbour(row, t):                       # row: list of depths 1..len; value of column -1 at tick t
        x = {j + 1: v for j, v in enumerate(row)}
        for s in range(t):
            new = {}
            for j in range(1, len(row) + 2):
                left = x.get(j + 1, 0); me = x.get(j, 0); right = x.get(j - 1, 0) if j > 1 else tau(s)
                new[j] = left ^ (me | right)
            x = new
        return x.get(1, 0)
    best = 0
    def dfs(row):
        nonlocal best
        j = len(row) + 1
        if j > 3 * d + 40: raise RuntimeError("cap")
        forced = tau(j - 1) == 1                  # the check at tick j - 1 fixes depth j
        if forced:
            vals = [v for v in (0, 1) if neighbour(row + [v], j - 1) == 1]
            assert len(vals) == 1
            options = vals
        else:
            options = [0, 1]
        if j >= start:
            options = [v for v in options if v == tgt(j)]
            if not options:
                best = max(best, j); return
        for v in options:
            dfs(row + [v])
    dfs([])
    return best

def main():
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    tmp = pathlib.Path(tempfile.mkdtemp())
    arch = ["-mcpu=native"] if sys.platform == "darwin" else ["-march=native"]
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(tmp / "rp"), str(HERE / "records_pattern.c")], check=True)
    subprocess.run(["cc", "-O2", *OMP, "-o", str(tmp / "rc"), str(HERE / "records.c")], check=True)
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(tmp / "ls"), str(HERE / "leftside_survivors.c")], check=True)
    caps = []
    def run(ph, mode, d):
        out = subprocess.run([str(tmp / "rp"), str(ph), mode, str(d), "10"], capture_output=True, text=True,
                             check=True).stdout.split()
        if len(out) > 6 and out[6] == "CAP": caps.append((ph, mode, d))
        return int(out[4])
    E = {(ph, d): run(ph, "Z", d) for ph in (0, 1) for d in range(1, dmax + 1)}
    Qv = {(ph, d): run(ph, "Q", d) for ph in (0, 1) for d in range(1, dmax + 1)}
    Pv = {(ph, d): run(ph, "P", d) for ph in (0, 1) for d in range(2, dmax + 1)}
    ok = {}
    ok["V1"] = all(int(subprocess.run([str(tmp / "rc"), str(d), "0"], capture_output=True, text=True,
                   check=True).stdout.split()[2]) == E[(0, d)] - d for d in range(3, min(33, dmax) + 1))
    out = subprocess.run([str(tmp / "ls"), "01", "0", str(min(32, dmax - 1)), "90", "10"], capture_output=True, text=True, check=True).stdout
    H = {}
    for line in out.splitlines():
        head, _, body = line.partition(":"); _, _, W, ph = head.split()
        H[(int(W), int(ph))] = max(int(x.split()[0]) for x in body.strip().strip(",").split(",") if x.strip())
    Rc = {d: max(H[(W, 1)] for W in range(d)) - (d - 1) for d in range(1, min(33, dmax) + 1)}
    ok["V2"] = all(E[(1, d)] - d == Rc[d] for d in Rc)
    v3 = True; rows = []
    for d in range(2, dmax + 1):
        for ph, other in ((1, 0), (0, 1)):            # E_ph(d) from the other phase's terms
            terms = {"d": d, "E": E[(other, d - 1)] - 1, "Q": Qv[(other, d)] - 1, "P": Pv[(other, d)] - 1}
            m = max(terms.values()); v3 &= (m == E[(ph, d)])
            rows.append((d, ph, E[(ph, d)] - d, [k for k, v in terms.items() if v == m], terms))
    ok["V3"] = v3
    v4 = True
    for d in range(2, 13):
        for ph in (0, 1):
            for mode, tab in (("Q", Qv), ("P", Pv)):
                v4 &= wall_pattern_end(ph, mode, d) == tab[(ph, d)]
    ok["V4"] = v4
    ok["C1"] = not caps
    print("d  phase  R_phase(d)  attaining terms   (E-1, Q-1, P-1 of the other phase)")
    for d, ph, r, att, t in rows:
        print(f"{d:2d}  {'S' if ph == 0 else 'B'}  {r:+3d}   {','.join(att):10s}  E-1={t['E']:3d} Q-1={t['Q']:3d} P-1={t['P']:3d}")
    qalone = [(d, ph) for d, ph, r, att, t in rows if att == ["Q"]]
    peaks = {d: att for d, ph, r, att, t in rows if ph == 1 and d in (12, 32)}
    ok["K"] = not qalone and all("P" in peaks.get(d, []) for d in (12, 32) if d <= dmax)
    print("\nQ alone attains:", qalone, "| black-start peaks' attaining terms:", peaks)
    print("tables (d: Q_S, P_S, Q_B, P_B):", {d: (Qv[(0, d)], Pv.get((0, d)), Qv[(1, d)], Pv.get((1, d))) for d in range(2, dmax + 1)})
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))
    print("ALL CHECKS PASS" if all(ok.values()) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    main()
