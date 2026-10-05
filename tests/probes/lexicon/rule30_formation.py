#!/usr/bin/env python3
"""rule30_formation.py: where the long two-sided zero runs come from (the wheel's formation, its slips, or neither),
what does not set a wall's kick, and (the random-chaos step) what a single glitch in the drive does to the wheel.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_formation.py [W=12] [K=192] [W2=13] [K2=384]
COST:       about ten minutes on one core.

A correction prompted this. Sections 8.5, 8.6 and 8.8 said "the long zero runs sit next to slips", from
rule30_wheel.py's Q4: no run of 14 or more lies wholly inside a stretch where column 1 equals itself 56 steps earlier.
An exploratory look (2026-10-05, not recorded) classified the 87 runs of 14 or more at depth <= 192 (right halves up to
12 cells). 51 started before the wheel first forms, 20 fell between exact windows (a slip episode), and 16 overlapped
an exact window. So most long runs come from the wheel's formation, the transient before it first locks, and Q4's
"next to slips" over-read it.

Definitions. Column 1 is cut into 56-step windows; a window is exact when it is U at some phase. The wheel forms at
the first exact window. A run of n zeros starting at depth s uses column 1 over [s - 1, s + n - 2] (Lemma 4). It is
"before formation" if that span ends before the first exact window, "in a slip episode" if it touches no exact window
and comes after formation, and "overlapping" otherwise.

PREDICTIONS, written 2026-10-05 before this script's first run:
  F1 (seen, recorded as a check): at depth <= K = 192, right halves up to W = 12 cells, of the runs of 14 or more,
     more than half are before formation, and none lies wholly inside an exact stretch.
  F2 (blind): deeper, at depth <= K2 = 384 with right halves up to W2 = 13 cells, of the runs of 16 or more, fewer than
     half are before formation (later runs, after the wheel has formed, take over).
  N  (seen, recorded as a measurement): the gap since the previous slip does not determine the kick. Within each gap
     (in windows, with at least 30 slips) the commonest kick stays below 80%. Kicks are read from slips that re-lock
     within 2 windows.
  G1 (blind, the random-chaos step: kick the drive): with column 0 = 0101... except one bit flipped at t0 = 503,
     inside the wheel's coherent running, column 1 is exact again within 10 windows in at least 90% of right halves
     whose column 1 was exact in the window holding t0.
  G2 (blind): in at least half of those, the wheel comes back at the same phase as without the glitch (the glitch
     heals, leaving no lasting kick).
  C  (control, causality): for every right half the glitched column 1 equals the unglitched one up to t0 exactly,
     and differs from it somewhere after t0 in at least one right half (the glitch is felt, and only afterwards).
REFUTED-BY: C failing (the harness); F1 failing (the exploratory look misled); F2, G1 or G2 failing; N failing (then a
  feature does set the kick).
"""
import sys, pathlib
from collections import Counter, defaultdict

W = int(sys.argv[1]) if len(sys.argv) > 1 else 12
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
W2 = int(sys.argv[3]) if len(sys.argv) > 3 else 13
K2 = int(sys.argv[4]) if len(sys.argv) > 4 else 384
P = 56

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1(R, n, glitch=None):
    """Column 1 for n steps with column 0 = 0101..., optionally with column 0's bit flipped at time `glitch`."""
    mask = (1 << (R.bit_length() + n + 3)) - 1
    tau = [t % 2 for t in range(n + 1)]
    if glitch is not None:
        tau[glitch] ^= 1
    row, out = tau[0] | (R << 1), []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | tau[t + 1]
    return out


def phases(c):
    out = []
    for a in range(0, len(c) - P + 1, P):
        out.append(next((d for d in range(P) if all(c[a + t] == U[(t - d) % P] for t in range(P))), None))
    return out


def locked(c):
    last_bad = max([t for t in range(len(c) - P) if c[t] != c[t + P]], default=-1)
    return last_bad < len(c) - P - 400


def classify(w, k, minrun):
    out, inside = Counter(), 0
    tau = [t % 2 for t in range(k + 1)]
    for R in range(1 << w):
        c = column1(R, max(1024, k + 1))
        if locked(c):
            continue
        ph = phases(c)
        exact = [j for j, d in enumerate(ph) if d is not None]
        first = exact[0] * P if exact else None
        good = [t >= P and c[t] == c[t - P] for t in range(k + 1)]
        L = r30.forced_left(R, tau, k)
        run = 0
        for kk, b in enumerate(L, 1):
            if b == 0:
                run += 1
                continue
            if run >= minrun:
                s, e = kk - run - 1, kk - 2
                if first is None or e < first:
                    out["before formation"] += 1
                elif any(j * P <= e and s <= j * P + P - 1 for j in exact):
                    out["overlapping"] += 1
                else:
                    out["slip episode"] += 1
                inside += all(good[max(0, s):e + 1]) and s >= P
            run = 0
    return out, inside


def main():

    f1, inside = classify(W, K, 14)
    n1 = sum(f1.values())
    verdict(f"F1 (seen) depth <= {K}, W <= {W}: most runs of 14+ before formation, none wholly inside an exact stretch",
            n1 > 0 and f1["before formation"] / n1 > 0.5 and inside == 0, f"{dict(f1)} of {n1}; wholly inside {inside}")
    f2, _ = classify(W2, K2, 16)
    n2 = sum(f2.values())
    verdict(f"F2 depth <= {K2}, W <= {W2}: fewer than half of the runs of 16+ before formation",
            n2 > 0 and f2["before formation"] / n2 < 0.5, f"{dict(f2)} of {n2}")

    # N: features of slips against kicks (W cells, T = 1024), using exact windows of column 1 only
    def notch(delta):
        k = (-17 * delta) % P
        k = k - P if k > P // 2 else k
        return k // 2
    by_gap, n_slips = defaultdict(Counter), 0
    for R in range(1 << W):
        c = column1(R, 1024)
        if locked(c):
            continue
        ph = phases(c)
        last = None
        for k in range(1, len(ph)):
            if ph[k - 1] is not None and ph[k] is None:
                d = ph[k - 1]
                nxt = next(((j, ph[j]) for j in range(k + 1, min(len(ph), k + 3)) if ph[j] is not None), None)
                if nxt is None:
                    last = k
                    continue
                kick = notch((nxt[1] - d) % P)
                if last is not None:
                    by_gap[min(6, k - last)][kick] += 1
                n_slips += 1
                last = k
    worst = max((c.most_common(1)[0][1] / sum(c.values()) for c in by_gap.values() if sum(c.values()) >= 30),
                default=1.0)
    verdict("N (seen) the gap since the previous slip does not set the kick (commonest kick < 80% at every gap)",
            worst < 0.80, f"largest share {worst:.2f} over {n_slips} slips that re-lock within 2 windows; "
            + "; ".join(f"gap {g}: " + ", ".join(f"{kk:+d} x{v}" for kk, v in c.most_common(3))
                        for g, c in sorted(by_gap.items())))

    # G: kick the drive
    t0, n_g, relock, same = 503, 0, 0, 0
    jumps = Counter()
    acausal = felt = 0
    for R in range(1 << W):
        c = column1(R, 1024)
        gg = column1(R, 1024, glitch=t0)
        acausal += gg[:t0 + 1] != c[:t0 + 1]
        felt += gg[t0 + 1:] != c[t0 + 1:]
        if locked(c):
            continue
        ph = phases(c)
        k0 = t0 // P
        if ph[k0] is None:
            continue
        n_g += 1
        pg = phases(gg)
        back = next(((j, pg[j]) for j in range(k0 + 1, min(len(pg), k0 + 11)) if pg[j] is not None), None)
        if back is None:
            continue
        relock += 1
        j, d = back
        if ph[j] is not None and ph[j] == d:
            same += 1
        elif ph[j] is not None:
            jumps[notch((d - ph[j]) % P)] += 1
    report("C causality: the glitch changes nothing up to t0, and is felt after it", acausal == 0 and felt > 0,
           f"{acausal} right halves changed before t0; {felt} changed after")
    verdict("G1 after a glitch in the drive the wheel is exact again within 10 windows (at least 90%)",
            n_g > 0 and relock / n_g >= 0.90, f"{relock} of {n_g}")
    verdict("G2 in at least half of those the wheel returns at its unglitched phase (the glitch heals)",
            relock > 0 and same / relock >= 0.5, f"{same} of {relock}; lasting kicks (notches): {jumps.most_common(8)}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
