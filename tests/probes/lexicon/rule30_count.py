#!/usr/bin/env python3
"""rule30_count.py: the counting form of the uniform law, and the tetralemma's fourth game (PERIOD-TWO.md section 7,
questions 1 and 8).

RUN-ON:     cpu (Python 3 and a C compiler; count.c does the counting; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_count.py [WMAX=24]
COST:       about a minute on one core.

Background (RULE30-PRIZE.md sections 8.42, 8.47, 8.49). N_w(T) is the number of pairs (configuration, position)
where the configuration's hull has exact width w (its first and last cells black), the position is a cell of the
hull taken as column 0, and that column reads a phase of the word at times 0 .. T-1. Fewer than one is none, so a
proof that N_w(T) <= 2^(w - alpha T) poly(w, T) for some alpha > 0 would close period 2 (question 1). The horizon
H(w) is the largest T with N_w(T) >= 1. The four games (question 8, from the tetralemma): every game asks for the
word at time 0; "both" asks for it at every later time; "black" only at times t whose word cell at t - 1 is black
(there the condition involves the left half alone); "white" only at the others; "neither" at no later time. The
ratio R(T) = N_both N_neither / (N_black N_white) is 1 if the two kinds of condition are independent, as the coin
model assumes.

PREDICTIONS, written 2026-10-05 before this script's first run (word 0101..., both phases, unless stated):
  CT0 (control, must hold): count.c's four counts equal a direct Python count, cell by cell, for every w from 1 to 9
      and T up to 16, for the words 01 (both phases) and 0.
  CT1 (blind; the horizon): H(w) - w lies between +2 and +14 for every w from 10 to WMAX.
  CT2 (blind; the counting form): at w = WMAX - 4, WMAX - 2 and WMAX, the least-squares slope of log2 N_w(T)
      against T, over T from w/2 to H(w) - 4, lies between -1.2 and -0.8 (alpha between 0.8 and 1.2).
  CT3 (blind; the tetralemma): at w = WMAX, R(T) lies between 0.5 and 2 for every T from 4 to H(WMAX) - 6.
  CT4 (random-chaos: does the law need a period?): a random word (seed 1940) has a slope within 0.15 of 0101's at
      w = WMAX, and its R(T) also stays between 0.5 and 2 over the same range of T.
  CT5 (counterfactual, the one-colour words, from Condrey's theorem): for the words 0 and 1, H(w) <= w + 2 at every
      w up to WMAX.
REFUTED-BY: CT0 failing (the instrument); CT1 to CT5 failing.
"""
import math, pathlib, random, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
TMAX = 50
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def run_c(exe, wmin, wmax, tmax, word, per):
    out = subprocess.run([str(exe), str(wmin), str(wmax), str(tmax), word, str(per)], check=True,
                         capture_output=True, text=True).stdout
    res = {}
    for line in out.split("\n"):
        if line.startswith("C "):
            _, w, t, b, k, h, n = line.split()
            res[(int(w), int(t))] = (int(b), int(k), int(h), int(n))
    return res


def direct(wmax, tmax, word, per):
    """The same four counts, cell by cell: lists of cells, the rule applied to each."""
    res = {}
    for w in range(1, wmax + 1):
        tot = {t: [0, 0, 0, 0] for t in range(1, tmax + 1)}
        pats = [[1]] if w == 1 else [[1] + [(q >> i) & 1 for i in range(w - 2)] + [1] for q in range(1 << (w - 2))]
        for pat in pats:
            pad = tmax + 2
            row = [0] * pad + pat + [0] * pad
            rows = [row]
            for _ in range(tmax - 1):
                r = rows[-1]
                rows.append([0] + [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(r) - 1)] + [0])
            for pos in range(w):
                col = [rows[t][pad + pos] for t in range(tmax)]
                for ph in range(per):
                    e = [int(word[ph + t]) for t in range(tmax)]
                    for T in range(1, tmax + 1):
                        if col[0] != e[0]:
                            continue
                        both = all(col[t] == e[t] for t in range(1, T))
                        blk = all(col[t] == e[t] for t in range(1, T) if e[t - 1] == 1)
                        wht = all(col[t] == e[t] for t in range(1, T) if e[t - 1] == 0)
                        for g, v in enumerate((both, blk, wht, True)):
                            tot[T][g] += v
        for T in range(1, tmax + 1):
            res[(w, T)] = tuple(tot[T])
    return res


def horizon(res, w, tmax):
    return max([t for t in range(1, tmax + 1) if res[(w, t)][0] >= 1], default=0)


def slope(res, w, lo, hi):
    pts = [(t, math.log2(res[(w, t)][0])) for t in range(lo, hi + 1) if res[(w, t)][0] > 0]
    n = len(pts)
    if n < 3:
        return float("nan")
    mt, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    return sum((t - mt) * (y - my) for t, y in pts) / sum((t - mt) ** 2 for t, _ in pts)


def ratio(res, w, t):
    b, k, h, n = res[(w, t)]
    return b * n / (k * h) if k and h else float("nan")


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_count_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "count.c")], check=True)
    w01 = "01" * 200
    rnd = random.Random(1940)
    wr = "".join(rnd.choice("01") for _ in range(400))
    ok0 = True
    for word, per in ((w01, 2), ("0" * 400, 1)):
        c = run_c(exe, 1, 9, 16, word, per)
        d = direct(9, 16, word, per)
        ok0 &= all(c[k] == d[k] for k in d)
    report("CT0 count.c equals the direct count for w = 1 .. 9, T <= 16, words 01 and 0", ok0)
    res = run_c(exe, 1, WMAX, TMAX, w01, 2)
    H = {w: horizon(res, w, TMAX) for w in range(1, WMAX + 1)}
    print("   0101: H(w) - w for w = 1 .. %d: " % WMAX + " ".join(f"{H[w] - w:+d}" for w in range(1, WMAX + 1)))
    for w in (WMAX - 4, WMAX):
        print(f"   0101, w = {w}: log2 N_w(T) for T = 1 .. {H[w]}: "
              + " ".join(f"{math.log2(res[(w, t)][0]):.1f}" for t in range(1, H[w] + 1)))
    verdict("CT1 H(w) - w between +2 and +14 for w = 10 .. WMAX",
            all(2 <= H[w] - w <= 14 for w in range(10, WMAX + 1)),
            ", ".join(f"{w}: {H[w] - w:+d}" for w in range(10, WMAX + 1) if not 2 <= H[w] - w <= 14) or "all within")
    sl = {w: slope(res, w, w // 2, H[w] - 4) for w in (WMAX - 4, WMAX - 2, WMAX)}
    verdict("CT2 slope of log2 N_w(T) between -1.2 and -0.8", all(-1.2 <= s <= -0.8 for s in sl.values()),
            ", ".join(f"w = {w}: {s:.3f}" for w, s in sl.items()))
    Rs = {t: ratio(res, WMAX, t) for t in range(4, H[WMAX] - 5)}
    print(f"   0101, w = {WMAX}: R(T) for T = 2 .. {H[WMAX]}: "
          + " ".join(f"{ratio(res, WMAX, t):.2f}" for t in range(2, H[WMAX] + 1)))
    print(f"   0101, w = {WMAX}: log2 N_black, log2 N_white at T = 10, 20, 30: "
          + "; ".join(f"{math.log2(max(res[(WMAX, t)][1], 1)):.1f}, {math.log2(max(res[(WMAX, t)][2], 1)):.1f}"
                      for t in (10, 20, 30)))
    verdict("CT3 R(T) between 0.5 and 2 for T = 4 .. H - 6", all(0.5 <= r <= 2 for r in Rs.values()),
            f"range {min(Rs.values()):.2f} to {max(Rs.values()):.2f}")
    rr = run_c(exe, WMAX, WMAX, TMAX, wr, 1)
    Hr = horizon(rr, WMAX, TMAX)
    sr = slope(rr, WMAX, WMAX // 2, Hr - 4)
    Rr = {t: ratio(rr, WMAX, t) for t in range(4, H[WMAX] - 5) if t <= Hr}
    print(f"   random word, w = {WMAX}: H - w = {Hr - WMAX:+d}, slope {sr:.3f}; R(T): "
          + " ".join(f"{r:.2f}" for r in Rr.values()))
    verdict("CT4 the random word's slope within 0.15 of 0101's, and its R(T) between 0.5 and 2",
            abs(sr - sl[WMAX]) <= 0.15 and all(0.5 <= r <= 2 for r in Rr.values()),
            f"slope {sr:.3f} against {sl[WMAX]:.3f}; R {min(Rr.values()):.2f} to {max(Rr.values()):.2f}")
    worst = []
    for word in ("0" * 400, "1" * 400):
        r1 = run_c(exe, 1, WMAX, TMAX, word, 1)
        h1 = {w: horizon(r1, w, TMAX) for w in range(1, WMAX + 1)}
        print(f"   word {word[0]}: H(w) - w for w = 1 .. {WMAX}: " + " ".join(f"{h1[w] - w:+d}" for w in h1))
        worst.append(max(h1[w] - w for w in h1))
    verdict("CT5 the one-colour words have H(w) <= w + 2", all(x <= 2 for x in worst),
            f"largest H(w) - w: word 0 {worst[0]:+d}, word 1 {worst[1]:+d}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
