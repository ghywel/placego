#!/usr/bin/env python3
"""rule30_edge_deadline.py: DL, is there a uniform linear edge deadline? (PERIOD-TWO.md row Q1; GPT's GC637.)
Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before it started.

RUN-ON:     cpu (Python 3 and a C compiler; reuses count_j.c, exact); seconds to a minute
COMMAND:    python3 tests/probes/lexicon/rule30_edge_deadline.py [WMAX=26]

GC637 proves that IF every configuration of exact hull width w, observed at a hull cell at distance j from the hull's
left end, can follow 0101 (either phase) for T observations only when T <= c j + b, with c, b independent of w, j and
the configuration, then section 8.51's left-halving lemma gives Q1's count bound with alpha = 1/c. The hypothesis is
unproved. This probe measures the per-slice horizon H(w, j) = the largest T with N_{w,j}(T) > 0 (count_j.c's exact
counts, the same convention: T observations at times 0 .. T-1), for every w <= WMAX and every j, to see whether a
w-independent deadline is plausible at all. A finite table cannot prove the deadline; it can refute its uniformity
within the measured range or suggest constants.

PREDICTIONS (Local's, published before the run):
  DL-C0 (control): summing N_{w,j}(T) over j gives count_j.c's own total N_w(T); and section 8.51's lemma holds
         exactly, N_{w,j}(T) = N_{w,j}(1) / 2^(T-1) for 1 <= T <= j, at every w <= WMAX.
  DL-C1 (control, by hand): j = 0 is the black left end itself, x_1(0) = 0 XOR (1 OR x_0(1)) = 1 = x_0(0), so the
         trace cannot alternate past one observation: H(w, 0) = 1 at every w >= 2.
  DL-P1 (blind, confidence 0.5): for every j from 1 to 6, H(w, j) is the same at w = 22, 23, 24, 25 and 26
         (saturated in w over the last five widths).
  DL-P2 (blind, confidence 0.5): those saturated values satisfy H(j) <= 2 j + 4 for j = 1 .. 6.
  DL-P3 (blind, confidence 0.6): max over j of H(w, j) - j lies between 0 and 10 at every w from 16 to WMAX.
  D1 (descriptive): the table H(w, j) for j <= 12, and the smallest b(c) with H(w, j) <= c j + b(c) over all measured
         (w, j), for c = 1, 2, 3.
Counterfactual: if H(w, 1) keeps growing with w through w = 26, no w-independent deadline holds even at j = 1 within
reach of this count, and GC637's route needs a different hypothesis (or the growth must stop beyond w = 26).
OUTCOME, 2026-10-09 00:40 BST (M5, run at commit c2c80fd0; 4.8 s): DL-C0 PASS (the sum over j and the lemma, every
w <= 26). DL-C1 PASS (H(w, 0) = 1). No horizon reached the TMAX cap.
  DL-P1 HELD: H(w, j) is constant over w = 22 .. 26 for j = 1 .. 6 (8, 7, 6, 5, 9, 10).
  DL-P2 REFUTED: H(1) = 8 > 2 + 4 (the other five are below 2j + 4).
  DL-P3 REFUTED: max over j of H(w, j) - j is 7 to 9 for w = 16 .. 25 but 17 at w = 26, from j = 19 (H = 36).
  D1: every slice j <= 18 is constant from w = j + 10 at the latest through w = 26, with final H(j) = 8, 7, 6, 5, 9,
  10, 10, 17, 16, 15, 14, 15, 17, 20, 22, 24, 25, 24 for j = 1 .. 18: H(j) <= j + 9 throughout (equality at j = 8).
  The slices near the right end are not yet settled: j = 19 went 22 (w = 24) -> 36 (w = 26), j = 20 reached 35. Over
  all measured (w, j): c = 1 needs b >= 17, c = 2 needs b >= 6, c = 3 needs b >= 5. Within reach, a w-independent
  per-slice deadline holds wherever w - j >= 10; whether it stays linear in j is what the j = 19 jump questions.
"""
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 26
WMIN = 2
TMAX = 60


def run(exe):
    out = subprocess.run([str(exe), str(WMIN), str(WMAX), str(TMAX), "01" * 64, "2"], check=True,
                         capture_output=True, text=True).stdout
    J, C = {}, {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "J":
            J[(int(f[1]), int(f[2]), int(f[3]))] = int(f[4])
        elif f and f[0] == "C":
            C[(int(f[1]), int(f[2]))] = int(f[3])
    return J, C


def main():
    with tempfile.TemporaryDirectory() as d:
        exe = pathlib.Path(d) / "count_j"
        subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "count_j.c")], check=True)
        J, C = run(exe)
    # DL-C0
    ok_sum = all(sum(J.get((w, j, T), 0) for j in range(w)) == C.get((w, T), 0)
                 for w in range(WMIN, WMAX + 1) for T in range(1, TMAX + 1) if (w, T) in C)
    ok_lem = all(J.get((w, j, T), 0) * 2 ** (T - 1) == J.get((w, j, 1), 0)
                 for w in range(WMIN, WMAX + 1) for j in range(1, w) for T in range(1, j + 1))
    print('DL-C0 %s (sum over j %s; lemma %s)' % ('PASS' if ok_sum and ok_lem else 'FAIL', ok_sum, ok_lem))
    H = {}
    for w in range(WMIN, WMAX + 1):
        for j in range(w):
            ts = [T for T in range(1, TMAX + 1) if J.get((w, j, T), 0) > 0]
            H[w, j] = max(ts) if ts else 0
    capped = [(w, j) for (w, j), h in H.items() if h >= TMAX]
    print('horizons at the TMAX cap (would invalidate the table):', capped)
    c1 = all(H[w, 0] == 1 for w in range(WMIN, WMAX + 1))
    print('DL-C1 %s (H(w, 0) = %s)' % ('PASS' if c1 else 'FAIL', sorted({H[w, 0] for w in range(WMIN, WMAX + 1)})))
    print('D1: H(w, j) for j = 0 .. 12 (rows w):')
    for w in range(WMIN, WMAX + 1):
        print('  w %2d: %s' % (w, ' '.join('%3d' % H[w, j] if j < w else '  .' for j in range(13))))
    sat = {j: [H[w, j] for w in range(max(WMIN, WMAX - 4), WMAX + 1)] for j in range(1, 7)}
    p1 = all(len(set(v)) == 1 for v in sat.values())
    print('DL-P1 %s: H(w, j) for w = %d .. %d, j = 1 .. 6: %s' % ('HELD' if p1 else 'REFUTED', WMAX - 4, WMAX, sat))
    p2 = p1 and all(sat[j][0] <= 2 * j + 4 for j in range(1, 7))
    print('DL-P2 %s: saturated values against 2j + 4: %s' % (
        'HELD' if p2 else ('REFUTED' if p1 else 'UNDECIDED (no saturation)'),
        {j: (sat[j][-1], 2 * j + 4) for j in range(1, 7)}))
    ex = {w: max(H[w, j] - j for j in range(w)) for w in range(16, WMAX + 1)}
    p3 = all(0 <= v <= 10 for v in ex.values())
    print('DL-P3 %s: max_j H(w, j) - j by w: %s' % ('HELD' if p3 else 'REFUTED', ex))
    for c in (1, 2, 3):
        b = max(H[w, j] - c * j for (w, j) in H)
        print('D1: c = %d needs b >= %d over all measured (w, j)' % (c, b))
    print('COMPLETE')


if __name__ == '__main__':
    main()
