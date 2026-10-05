#!/usr/bin/env python3
"""rule30_merge.py: are the ladder's long runs luck or structure? And why are real right halves so poor?

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_merge.py
COST:       about five minutes on one core, 1.5 GB of memory at the deepest point.

Two questions left by rule30_ladder_budget.py (PRIZE-PROBLEMS.md section 8.14).

Part A, the "families". With column 1 free, 21 start groups hold the left half at zero for exactly 33 cells from depth
33, and none for 25 to 31; section 8.14 called that "structure, not luck". Looked at afterwards (ladder.c keys and
merge modes), the 21 groups reach one and the same left-side state, the anti-diagonal pair (a_{s-2}, a_{s-3}), so they
are one event counted 21 times. Counting distinct states instead (10,040 at depth 33, 309,669 at depth 45), the tail
looked like coin flips, and the outliers at 33 and 45 had a chance of about 14% each. With column 1 free only the
forced cells (even depths) can end a run, so under the coin model a run of R cells from an odd depth s has
f(R) = (R - 1) / 2 forced cells, and P(run >= R) = 2^-f(R) for each distinct state.

Part B, the real right halves. BL5 found that right halves of 16 cells hold the left half at zero for only 11 cells
at depths 41 to 105, far below one bit per cell. Two explanations: merging (most right halves give the same column 1,
so there are far fewer than 2^16 distinct histories), or cost (the histories are distinct, but each zero cell costs
more than a bit).

PREDICTIONS, written 2026-10-05 before this script's first run. Part A uses depths not examined before.
  MA0 (control, exact): with column 1 free, equal left-side states give equal runs: 0 conflicts at every depth.
  MA1 (blind; the coin model over distinct states): at s = 35, 39, 43, 47, 49, the number of distinct states whose run
      is at least R is within a factor 2 of G_eff 2^-f(R), for every odd R whose expectation is at least 10.
  MA2 (blind; the maxima are luck): the coin model's chance of a maximum at least as long as the one observed,
      1 - (1 - 2^-f(R))^G_eff, is at least 0.01 at each of those five depths.
  MA3 (blind): merging grows with depth: G / G_eff rises from s = 35 to s = 49 (it is 6.5 at 33 and 13.5 at 45).
  MB1 (blind; little merging): among the 65,535 right halves of at most 16 cells, the number of distinct visible
      column-1 histories (even times below s + 40) is at least 2^14 at each depth s = 41, 57, 73, 89, 105.
  MB2 (blind; each cell costs more than a bit): over the distinct histories, the number whose zero run from depth s
      is at least k falls by beta_real >= 1.2 bits per cell (least-squares slope of log2 N(k), k = 1 up to the last
      k with N(k) >= 20), at each of the five depths.
REFUTED-BY: MA0 failing (the instrument); MA1 to MA3 or MB1 to MB2 failing. MB1 and MB2 decide between merging and
  cost: if MB1 fails, merging explains BL5; if MB2 fails while MB1 holds, BL5 is not explained by either.

OUTCOME of the first run, 2026-10-05 (about three minutes): MA0 passed (0 conflicts at all five depths).
  MA1 HELD: over distinct states the coin model fits closely, e.g. at s = 49 (965,204 distinct states) 60,745 last at
      least 9 cells against 60,325 expected, and 119 at least 27 against 117.8. Nothing is outside a factor 2.
  MA2 HELD: the maxima's coin chances are 0.419, 0.819, 0.737, 0.406, 0.841 (s = 35, 39, 43, 47, 49). The maxima are
      luck. Section 8.14's "structure, not luck" for the depth-33 and depth-45 families was wrong: each is one state
      counted 21 and 8 times, with a coin chance of about 14%.
  MA3 HELD: G / G_eff = 7.4, 9.4, 12.0, 15.3, 17.4.
  MB1 REFUTED: the 65,535 right halves of at most 16 cells give only 4,703, 6,493, 8,351, 10,314 and 12,352 distinct
      visible histories (2^12.2 to 2^13.6) at s = 41 to 105. Most of a right half's 16 bits have not reached column 1
      by time s + 40.
  MB2 REFUTED: over those distinct histories a zero cell costs about one bit: beta_real = 0.91, 1.07, 1.07, 1.04, 1.20.
  So BL5 is explained by merging, and the coin model holds for real right halves too, once histories are counted
  rather than seeds.
"""
import math, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
DEPTHS_A = [35, 39, 43, 47, 49]
DEPTHS_B = [41, 57, 73, 89, 105]
W = 16
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def slope(N):
    ks = [k for k in range(1, len(N)) if N[k] >= 20]
    if len(ks) < 3:
        return float("nan")
    ys = [math.log2(N[k]) for k in ks]
    mx, my = sum(ks) / len(ks), sum(ys) / len(ys)
    return -sum((x - mx) * (y - my) for x, y in zip(ks, ys)) / sum((x - mx) ** 2 for x in ks)


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "ladder"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "ladder.c")], check=True)

    conflicts, ma1_bad, ma2, ratios = [], [], {}, {}
    for s in DEPTHS_A:
        out = subprocess.run([str(exe), "merge", "0", str(s)], capture_output=True, text=True, timeout=3600).stdout
        G = int(re.search(r"of (\d+) start", out).group(1))
        R = int(re.search(r"= (\d+)", out).group(1))
        Ge = int(re.search(r"^D 0 \d+ distinct (\d+)", out, re.M).group(1))
        conflicts.append(int(re.search(r"conflicts (\d+)", out).group(1)))
        dh = {int(a): int(b) for a, b in re.findall(r"^DH 0 \d+ (\d+) (\d+)$", out, re.M)}
        ratios[s] = G / Ge
        rows = []
        for r in range(1, R + 1, 2):
            obs = sum(v for k, v in dh.items() if k >= r)
            exp = Ge * 2.0 ** (-(r - 1) / 2)
            if exp >= 10:
                rows.append((r, obs, round(exp, 1)))
                if not exp / 2 <= obs <= 2 * exp:
                    ma1_bad.append((s, r, obs, round(exp, 1)))
        f = (R - 1) / 2
        ma2[s] = 1 - (1 - 2.0 ** -f) ** Ge
        print(f"   s {s}: G {G}, distinct {Ge} (G / distinct {G / Ge:.1f}), R {R}, coin chance of a max >= R "
              f"{ma2[s]:.3f}; observed vs expected (R: obs exp) " + " ".join(f"{r}: {o} {e}" for r, o, e in rows),
              flush=True)
    report("MA0 equal left-side states give equal runs (column 1 free)", all(c == 0 for c in conflicts),
           f"conflicts {conflicts}")
    verdict("MA1 the coin model over distinct states, within a factor 2", not ma1_bad, f"outside: {ma1_bad}")
    verdict("MA2 the maxima are luck: coin chance >= 0.01 at every depth", all(p >= 0.01 for p in ma2.values()),
            ", ".join(f"s {s}: {p:.3f}" for s, p in ma2.items()))
    rs = [ratios[s] for s in DEPTHS_A]
    verdict("MA3 merging grows with depth", all(b > a for a, b in zip(rs, rs[1:])),
            ", ".join(f"s {s}: {ratios[s]:.1f}" for s in DEPTHS_A))

    K = max(DEPTHS_B) + 40
    tau = [t % 2 for t in range(K + 2)]
    hist_by_s = {s: {} for s in DEPTHS_B}
    for R0 in range(1, 1 << W):
        mask = (1 << (R0.bit_length() + K + 3)) - 1
        row, vis = R0 << 1, []
        for t in range(K + 1):
            if t % 2 == 0:
                vis.append((row >> 1) & 1)
            row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
        L = r30.forced_left(R0, tau, K)
        for s in DEPTHS_B:
            key = tuple(vis[:(s + 40) // 2])
            n = 0
            while s - 1 + n < len(L) and L[s - 1 + n] == 0:
                n += 1
            hist_by_s[s].setdefault(key, n)
    mb1, mb2 = {}, {}
    for s in DEPTHS_B:
        runs = list(hist_by_s[s].values())
        mb1[s] = len(runs)
        top = max(runs)
        N = [sum(1 for r in runs if r >= k) for k in range(top + 1)]
        mb2[s] = slope(N)
        print(f"   real right halves, s {s}: distinct histories {len(runs)} (log2 {math.log2(len(runs)):.2f}), longest run "
              f"{top}, beta {mb2[s]:.3f}; N(k) " + " ".join(f"{k}:{N[k]}" for k in range(1, top + 1)), flush=True)
    verdict("MB1 little merging: at least 2^14 distinct histories at every depth", all(v >= 1 << 14 for v in mb1.values()),
            ", ".join(f"s {s}: {v}" for s, v in mb1.items()))
    verdict("MB2 each cell costs more than a bit: beta_real >= 1.2 at every depth", all(b >= 1.2 for b in mb2.values()),
            ", ".join(f"s {s}: {b:.3f}" for s, b in mb2.items()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
