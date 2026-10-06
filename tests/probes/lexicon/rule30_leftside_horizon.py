#!/usr/bin/env python3
"""rule30_leftside_horizon.py: the slow walls' B question from the LEFT (section 8.63, item 5.2). Next to a periodic
column 0 the left half evolves on its own, with the wall as boundary; the right half reaches it only through two
conditions on column -1 (leftside_horizon.c, header): at black times column -1 is forced, at white times the stream it
implies must be monotone inside each white stretch. For every finite left seed of width W and every phase of the
wall, the survival time is the first failure; H_L(W) is the best over seeds and phases, an upper bound on the
lifetime of every two-sided configuration whose left half has width W. Every B-side search so far (sections 8.42,
8.60, 8.63; rule30_uniform.py) enumerated RIGHT halves; this is the first enumeration of left ones, and it asks whether
the left half's own constraints already give the "total width plus a constant" law. (Local, 2026-10-06; section 8.66.)

RUN-ON:     cpu, 8 threads (OpenMP; ompflags.py)
COMMAND:    python3 tests/probes/lexicon/rule30_leftside_horizon.py [WMAX=20] [T=100]
COST:       seconds to a few minutes.

SEEN BEFORE these predictions: the right-half horizon law of section 8.42 (total width plus 6 to 10 for every word up
to period 4); rule30_uniform.py slow (next to 0^a 1^a, a = 4, 8, 16, every right half to width 16 has excess at most
+9); the checkerboard lemma (next to a black stretch the forced left half is the checkerboard to its depth); no
left-only measurement of any kind.

PREDICTIONS, written 2026-10-06 before the first run.
  LH0 (control, must hold): next to the black wall 1, condition (i) asks column -1 to be white for ever, which the
      infinite checkerboard does (it is a fixed point of Rule 30 with a black boundary); a finite seed of width W can
      hold it only until its left end's defect reaches column -1 at speed about 1: H_L(W) = W + c with -2 <= c <= 2
      for 4 <= W <= 20.
  CF  (control, must hold): next to the white wall 0, the empty seed satisfies (ii) for ever: H_L(0) reaches the cap.
  LH1 (blind, the question): next to 0101, H_L(W) = W + c with c <= 12 for every W <= 20: the left half's own
      constraints already stop every seed at "width plus a constant". If c grows with W, the right half's content
      is essential to B and the slow-wall reframing's "nearly deterministic target" is weaker than section 8.63 says.
  LH2 (blind): next to the slow walls 0^a 1^a for a = 2, 4, 8, 16, no seed of width W <= 16 survives two complete
      black stretches (for a = 8: H_L(W) < 40; for a = 16: H_L(W) < 80 is unreachable at T = 100 so the test is
      H_L(W) < 48 with W + T <= 128), and the excess c = H_L(W) - W is at most 2a + 12 for every W <= 16.
  LH3 (blind): next to 0101 the best seed at W = 16 and W = 20 is the same seed extended on the left (the record
      seeds nest), as the right-half records of section 8.42 did not.
REFUTED-BY: LH0 or CF failing (the instrument); LH1 to LH3 the other way.
"""
import pathlib, subprocess, sys, tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "probes" / "lexicon"))
from ompflags import OMP

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_leftside_horizon.txt"
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
T = int(sys.argv[2]) if len(sys.argv) > 2 else 100
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def build():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_leftside_horizon"
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(exe), str(HERE / "leftside_horizon.c")], check=True)
    return exe


def run(exe, word, wmax, t):
    out = subprocess.run([str(exe), word, str(wmax), str(t), "8"], capture_output=True, text=True, check=True).stdout
    with open(OUT, "a") as fh:
        fh.write(out)
    res = {}
    for ln in out.splitlines():
        f = ln.split()
        res[int(f[2])] = (int(f[4]), int(f[6]), int(f[8], 16), "CAPPED" in ln)
    return res


def main():
    exe = build()
    with open(OUT, "a") as fh:
        fh.write(f"# run WMAX={WMAX} T={T}\n")
    res = {}
    for word in ["1", "0", "01", "0011", "00001111", "0000000011111111", "0" * 16 + "1" * 16]:
        wm = WMAX if word in ("1", "0", "01") else min(WMAX, 16)
        t = min(T, 128 - wm)
        res[word] = run(exe, word, wm, t)
        print(f"   {word[:8]}{'...' if len(word) > 8 else ''}: " +
              " ".join(f"{W}:{v[0]}{'*' if v[3] else ''}" for W, v in sorted(res[word].items())), flush=True)
    b = res["1"]
    report("LH0 black wall: H_L(W) = W + c, -2 <= c <= 2, for 4 <= W <= 20",
           all(-2 <= b[W][0] - W <= 2 for W in range(4, WMAX + 1)), f"c = {[b[W][0] - W for W in range(4, WMAX + 1)]}")
    report("CF  white wall: the empty seed reaches the cap", res["0"][0][3])
    z = res["01"]
    cs = [z[W][0] - W for W in range(0, WMAX + 1)]
    verdict("LH1 0101: H_L(W) = W + c with c <= 12 for every W <= 20", max(cs) <= 12, f"c = {cs}")
    ok2 = True; det = []
    for a, word in ((2, "0011"), (4, "00001111"), (8, "0000000011111111"), (16, "0" * 16 + "1" * 16)):
        r = res[word]
        lim = {2: 100, 4: 100, 8: 40, 16: 48}[a]
        hs = [r[W][0] for W in range(0, 17)]
        cmax = max(h - W for W, h in enumerate(hs))
        det.append(f"a={a}: max H {max(hs)} (limit {lim}), max c {cmax} (limit {2 * a + 12})")
        ok2 &= max(hs) < lim and cmax <= 2 * a + 12
    verdict("LH2 slow walls: no seed of width <= 16 survives two black stretches; c <= 2a + 12", ok2, "; ".join(det))
    s16, s20 = z[16][2], z[20][2]
    verdict("LH3 0101: the record seed at W = 20 extends the record seed at W = 16 on the left",
            (s20 & ((1 << 16) - 1)) == s16, f"W16 {s16:x}, W20 {s20:x}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
