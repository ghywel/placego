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

OUTCOME of the first run, 2026-10-06 11:19 (WMAX = 20 for the walls 1, 0, 01 and 16 for the slow walls; T = 100; seconds;
  the table is rule30_leftside_horizon.txt). LH0 PASSED (black wall: c alternates +1, -1, the checkerboard seed's
  parity). CF PASSED. LH1 REFUTED in its bracket only: next to 0101 the left-only horizon is H_L(W) = 1, 7, 6, 5, 6, 9,
  10, 12, 17, 18, 17, 30, 29, 28, 32, 31, 30, 31, 33, 38, 37 for W = 0 .. 20, i.e. W + c with c between 14 and 19 from
  W = 11 on (a jump from 9 to 19 at W = 11), not c <= 12; "width plus a constant" holds in shape, the constant is
  about 17 against the two-sided law's 6 to 10 (section 8.42), as it must be with fewer conditions. LH2 HELD, and
  far more strongly than written: next to 0^a 1^a the left half's own two conditions stop EVERY seed of width <= 16
  within 29 steps for a = 2, 22 for a = 4, 22 for a = 8 and 21 for a = 16 (over all phases). Two consecutive complete
  black stretches need at least 3a steps from any phase, so for a = 8 (24) and a = 16 (48) no seed of width <= 16
  survives two consecutive black stretches; for a = 16 not even one period (21 < 32); for a = 2 and 4 seeds outlive
  several periods. (A first reading said "less than one period for a = 8 and 16", wrong for a = 8: 22 > 16; corrected
  at 11:35.) LH3 REFUTED (the record seeds at W = 16 and 20 differ: cbb5, d1541).

WIDE ADDENDUM, written 2026-10-06 before the second run (python3 rule30_leftside_horizon.py wide): widths 17 to 24 next
  to 0^8 1^8, 0^16 1^16 and 0101 (T = 100). The question: can a seed wider than the black stretch rebuild the
  checkerboard across a white stretch and pass a second black stretch?
  LW1 (blind): next to 0^8 1^8 no seed of width <= 24 survives two consecutive complete black stretches: H_L(W) <= 23
      for every W <= 24. A seed three times the stretch's width is still not enough.
  LW2 (blind): next to 0^16 1^16, H_L(W) < 32 for every W <= 24 (not one period), and the gain from W = 16 to 24 is
      at most 8 steps.
  LW3 (blind): on both slow walls the horizon grows by less than one step per unit width from W = 16 to 24 (the
      law "width plus a constant" does not hold there: the wall sets the horizon, not the seed).
  CF  (counterfactual, must fail): next to 0101 the law stops too: H_L(24) < 24 + 10. The first run's W + 17 says
      it will not; H_L(24) >= 34 is expected.
  REFUTED-BY: LW1 to LW3 the other way; CF holding. What would change my mind: a width at which the slow-wall horizon
  jumps past two black stretches would locate the seed width that can carry a checkerboard across a white stretch,
  and the theorem of section 8.63 would need that width in its hypothesis.
  OUTCOME of the second run, 2026-10-06 11:28 (wide; a minute). All three blind predictions REFUTED the informative
  way, CF PASSED (0101: H_L(24) = 42, the law W + 17 continues). 0^8 1^8: H_L = 21, 22, 21, 24, 25, 26, 29, 31, 30, 34,
  36 for W = 14 .. 24: a seed of width 20 passes two consecutive black stretches (29 >= 24) and one of width 24 lives
  36 steps, two full periods and four more. 0^16 1^16: 21, 20, 21, 21, 24, 26, 26, 26, 29, 30, 32: width 24 reaches
  exactly one period (one black stretch and the white stretch beside it) and dies at the second black stretch. So
  the seed's width against the stretch is the whole hypothesis: W = 16 = 2b fails at b = 8 and W = 20 = 2.5 b passes;
  W = 24 = 1.5 b fails at b = 16. The horizon gains about 1.9 steps per unit width on 0^8 1^8 and 1.4 on 0^16 1^16
  between W = 16 and 24, more than the 0101 law's one, because passing a stretch is worth a stretch.

WHITE-STRETCH ADDENDUM, written 2026-10-06 before the third run (python3 rule30_leftside_horizon.py white), after GPT's
  G003: the 2b threshold was measured with a = b only. Here the black stretch is fixed at b = 8 and the white
  stretch varies, a = 4, 8, 16, 32, widths to 24, T = 100. The passing width P(a) is the least W whose best seed
  survives two consecutive complete black stretches (H_L(W) >= 2b + a from some phase; the test uses H_L >= 2b + a).
  LA1 (blind): P(a) is non-decreasing in a and P(32) >= P(4) + 2: a longer white stretch gives the left half longer
      to lose the carrier, so more width is needed.
  LA2 (blind): P(4) <= 16: with a short white stretch, width 2b already passes.
  LA3 (blind): the horizon for W < P(a) is independent of a to within 2 steps (the seed dies in the second black
      stretch at the same depth whatever the white stretch was).
  CF  (counterfactual, must fail): P(32) <= 12 (a wide white stretch makes passing easier). It should not.
  REFUTED-BY: LA1 to LA3 the other way; CF holding. What would change my mind about "W against b": P(a) growing
  without bound in a would say the white stretch, not the black one, sets the hypothesis.
  OUTCOME of the third run, 2026-10-06 11:37 (white; 4 minutes). P(4) = 13, P(8) = 17, P(16) = 23, P(32) = none to
  width 24 (48 steps needed). LA1's substance HELD (non-decreasing, and P(16) - P(4) = 10), the verdict printed
  REFUTED only because P(32) is undefined at this width; LA2 HELD; LA3 likewise substantively held (below the
  passing width the rows for a = 8, 16, 32 agree within 2 steps; a = 4 within 3) and printed REFUTED for the same
  technical reason; CF PASSED. The reading, not pre-registered: P(a) = a + b + 1 at a = 4 and 8 and a + b - 1 at
  a = 16, i.e. the passing width is about the wall's PERIOD, not 2b. The run with a = b = 8 (P = 17 = 16 + 1) and
  a = b = 16 (no pass at 24, period 32) agree. GPT's G003 caution was right: the hypothesis is W against a + b.

PERIOD ADDENDUM, written 2026-10-06 before the fourth run (python3 rule30_leftside_horizon.py period): b = 4 and 16
  with a = 4, 8: the walls 0^4 1^4, 0^8 1^4, 0^4 1^16, 0^8 1^16, widths to 24, passing = two consecutive complete
  black stretches (H_L >= 2b + a).
  LB1 (blind, the period reading): P(4,4) in [7, 11], P(8,4) in [11, 15], P(4,16) in [19, 23], and P(8,16) is none to
      width 24 (it would be about 25).
  CF  (counterfactual, must fail): P(8,4) <= 9, which the old "2b" reading would give. It must not.
  REFUTED-BY: LB1 the other way (then the period is not the hypothesis either); CF holding.
"""
import pathlib, subprocess, sys, tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "probes" / "lexicon"))
from ompflags import OMP

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_leftside_horizon.txt"
WMAX = int(next((a for a in sys.argv[1:] if a.isdigit()), 20))
T = int(([a for a in sys.argv[1:] if a.isdigit()] + ["100", "100"])[1])
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


def wide():
    exe = build()
    with open(OUT, "a") as fh:
        fh.write("# wide run: widths 17 .. 24, T = 100\n")
    res = {}
    for word in ["0000000011111111", "0" * 16 + "1" * 16, "01"]:
        out = subprocess.run([str(exe), word, "24", "100", "8"], capture_output=True, text=True, check=True).stdout
        with open(OUT, "a") as fh:
            fh.write(out)
        r = {}
        for ln in out.splitlines():
            f = ln.split(); r[int(f[2])] = int(f[4])
        res[word] = r
        print(f"   {word[:8]}{'...' if len(word) > 8 else ''}: " + " ".join(f"{W}:{r[W]}" for W in range(14, 25)), flush=True)
    a8, a16, z = res["0000000011111111"], res["0" * 16 + "1" * 16], res["01"]
    verdict("LW1 0^8 1^8: H_L(W) <= 23 for every W <= 24", all(a8[W] <= 23 for W in range(0, 25)), f"max {max(a8[W] for W in range(25))}")
    verdict("LW2 0^16 1^16: H_L(W) < 32 for W <= 24 and the gain from 16 to 24 is at most 8",
            all(a16[W] < 32 for W in range(25)) and a16[24] - a16[16] <= 8, f"max {max(a16[W] for W in range(25))}, H(16) {a16[16]}, H(24) {a16[24]}")
    verdict("LW3 both slow walls gain less than one step per unit width from 16 to 24",
            a8[24] - a8[16] < 8 and a16[24] - a16[16] < 8, f"a=8: {a8[16]} -> {a8[24]}; a=16: {a16[16]} -> {a16[24]}")
    report("CF  0101: the law does NOT stop (H_L(24) >= 34)", z[24] >= 34, f"H_L(24) = {z[24]}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def white():
    exe = build()
    b = 8
    with open(OUT, "a") as fh:
        fh.write("# white-stretch run: 0^a 1^8, a = 4, 8, 16, 32, widths to 24, T = 100\n")
    res, P = {}, {}
    for a in (4, 8, 16, 32):
        word = "0" * a + "1" * b
        out = subprocess.run([str(exe), word, "24", "100", "8"], capture_output=True, text=True, check=True).stdout
        with open(OUT, "a") as fh:
            fh.write(out)
        r = {int(ln.split()[2]): int(ln.split()[4]) for ln in out.splitlines()}
        res[a] = r
        P[a] = next((W for W in range(25) if r[W] >= 2 * b + a), None)
        print(f"   0^{a} 1^8: " + " ".join(f"{W}:{r[W]}" for W in range(8, 25)) + f"   passing width {P[a]} (needs {2 * b + a})", flush=True)
    ok1 = all(P[a] is not None for a in P) and P[4] <= P[8] <= P[16] <= P[32] and P[32] >= P[4] + 2
    verdict("LA1 P(a) non-decreasing and P(32) >= P(4) + 2", ok1, f"P = {P}")
    verdict("LA2 P(4) <= 16", P[4] is not None and P[4] <= 16, f"P(4) = {P[4]}")
    lows = {a: [res[a][W] for W in range(8, min(P[x] for x in P if P[x] is not None))] for a in res} if all(P[a] is not None for a in P) else {}
    ok3 = bool(lows) and all(abs(lows[a][i] - lows[4][i]) <= 2 for a in lows for i in range(len(lows[4])))
    verdict("LA3 below the passing width the horizon is independent of a within 2 steps", ok3,
            "; ".join(f"a={a}: {v}" for a, v in lows.items()) if lows else "no passing width for some a")
    report("CF  P(32) is NOT <= 12", P[32] is None or P[32] > 12, f"P(32) = {P[32]}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def period():
    exe = build()
    with open(OUT, "a") as fh:
        fh.write("# period run: 0^a 1^b for (a, b) = (4,4), (8,4), (4,16), (8,16), widths to 24, T = 100\n")
    P = {}
    for a, b in ((4, 4), (8, 4), (4, 16), (8, 16)):
        word = "0" * a + "1" * b
        out = subprocess.run([str(exe), word, "24", "100", "8"], capture_output=True, text=True, check=True).stdout
        with open(OUT, "a") as fh:
            fh.write(out)
        r = {int(ln.split()[2]): int(ln.split()[4]) for ln in out.splitlines()}
        P[(a, b)] = next((W for W in range(25) if r[W] >= 2 * b + a), None)
        print(f"   0^{a} 1^{b}: " + " ".join(f"{W}:{r[W]}" for W in range(6, 25)) + f"   passing width {P[(a, b)]} (needs {2 * b + a})", flush=True)
    ok = (P[(4, 4)] is not None and 7 <= P[(4, 4)] <= 11 and P[(8, 4)] is not None and 11 <= P[(8, 4)] <= 15
          and P[(4, 16)] is not None and 19 <= P[(4, 16)] <= 23 and P[(8, 16)] is None)
    verdict("LB1 P(4,4) in [7,11], P(8,4) in [11,15], P(4,16) in [19,23], P(8,16) none to 24", ok, f"P = {P}")
    report("CF  P(8,4) is NOT <= 9", P[(8, 4)] is None or P[(8, 4)] > 9, f"P(8,4) = {P[(8, 4)]}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "period" in sys.argv[1:]:
        period()
        return
    if "white" in sys.argv[1:]:
        white()
        return
    if "wide" in sys.argv[1:]:
        wide()
        return
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
