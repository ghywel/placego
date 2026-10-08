#!/usr/bin/env python3
"""rule30_edge_deadline2.py: DL2, DL's per-slice horizons H(w, j) extended to w = 32 (row Q1; GPT's GC637; L346).
Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before it started.

RUN-ON:     cpu, one core (count_j.c, exact); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_edge_deadline2.py [WMAX=32]

DL (rule30_edge_deadline.py) found every slice j <= 18 constant in w from w = j + 10 at the latest, with
H(j) <= j + 9, but the slices near the right end unsettled: H(w, 19) went 22 -> 36 from w = 24 to 26. DL2 runs
count_j.c to w = 32. Instrument limit: count_j.c evolves a 128-bit word whose hull starts at bit 64 - w/2, so at
w = 32 a horizon above 48 would run off the word; TMAX is 48, and any horizon of 46 or more at w >= 27 is reported
as invalid rather than used.

PREDICTIONS (Local's, published before the run):
  DL2-C0 (control): the sum over j and section 8.51's lemma hold at every w <= WMAX, and the table for w <= 26 equals
         DL's (j = 1 .. 18 values 8, 7, 6, 5, 9, 10, 10, 17, 16, 15, 14, 15, 17, 20, 22, 24, 25, 24).
  DL2-C2 (instrument): no horizon of 46 or more at w >= 27.
  DL2-P4 (blind, confidence 0.5): H(w, 19) is constant over w = 29 .. 32.
  DL2-P5 (blind, confidence 0.6): every slice j <= 18 keeps its DL value through w = 32.
  DL2-P6 (blind, confidence 0.4): every slice j <= 22 that is constant over its last three measured widths has
         H(j) <= j + 17.
Counterfactual: a slice j <= 18 changing after w = 26 would show that DL's saturation was not final, and that the
deadline's constant could grow with w.
"""
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 32
TMAX = 48
DL = {1: 8, 2: 7, 3: 6, 4: 5, 5: 9, 6: 10, 7: 10, 8: 17, 9: 16, 10: 15, 11: 14, 12: 15, 13: 17, 14: 20, 15: 22,
      16: 24, 17: 25, 18: 24}


def main():
    with tempfile.TemporaryDirectory() as d:
        exe = pathlib.Path(d) / "count_j"
        subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "count_j.c")], check=True)
        out = subprocess.run([str(exe), "2", str(WMAX), str(TMAX), "01" * 64, "2"], check=True,
                             capture_output=True, text=True).stdout
    J, C = {}, {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "J":
            J[(int(f[1]), int(f[2]), int(f[3]))] = int(f[4])
        elif f and f[0] == "C":
            C[(int(f[1]), int(f[2]))] = int(f[3])
    ok_sum = all(sum(J.get((w, j, T), 0) for j in range(w)) == C.get((w, T), 0)
                 for w in range(2, WMAX + 1) for T in range(1, TMAX + 1) if (w, T) in C)
    ok_lem = all(J.get((w, j, T), 0) * 2 ** (T - 1) == J.get((w, j, 1), 0)
                 for w in range(2, WMAX + 1) for j in range(1, w) for T in range(1, j + 1))
    H = {}
    for w in range(2, WMAX + 1):
        for j in range(w):
            ts = [T for T in range(1, TMAX + 1) if J.get((w, j, T), 0) > 0]
            H[w, j] = max(ts) if ts else 0
    ok_dl = all(H[26, j] == v for j, v in DL.items())
    print('DL2-C0 %s (sum %s, lemma %s, DL table at w = 26 %s)' % ('PASS' if ok_sum and ok_lem and ok_dl else 'FAIL',
                                                                 ok_sum, ok_lem, ok_dl))
    bad = sorted((w, j, H[w, j]) for w in range(27, WMAX + 1) for j in range(w) if H[w, j] >= 46)
    print('DL2-C2 %s (horizons >= 46 at w >= 27: %s)' % ('PASS' if not bad else 'FAIL', bad))
    print('H(w, j) for w = 24 .. %d, j = 0 .. %d:' % (WMAX, WMAX - 1))
    for w in range(24, WMAX + 1):
        print('  w %2d: %s' % (w, ' '.join('%2d' % H[w, j] for j in range(w))))
    v19 = [H[w, 19] for w in range(29, WMAX + 1)]
    print('DL2-P4 %s: H(w, 19) for w = 29 .. %d: %s' % ('HELD' if len(set(v19)) == 1 else 'REFUTED', WMAX, v19))
    ch = [(j, w, H[w, j]) for j in DL for w in range(27, WMAX + 1) if H[w, j] != DL[j]]
    print('DL2-P5 %s: changes after w = 26 among j <= 18: %s' % ('HELD' if not ch else 'REFUTED', ch))
    settled = {}
    for j in range(1, 23):
        ws = [w for w in range(j + 1, WMAX + 1)]
        if len(ws) >= 3 and len({H[w, j] for w in ws[-3:]}) == 1:
            settled[j] = H[ws[-1], j]
    over = {j: h for j, h in settled.items() if h > j + 17}
    print('DL2-P6 %s: settled slices j <= 22 and H(j) - j: %s; over j + 17: %s' % (
        'HELD' if not over else 'REFUTED', {j: (h, h - j) for j, h in settled.items()}, over))
    for c in (1, 2, 3):
        b = max(h - c * j for j, h in settled.items())
        print('settled slices: c = %d needs b >= %d' % (c, b))
    print('COMPLETE')


if __name__ == '__main__':
    main()
