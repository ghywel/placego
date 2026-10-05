#!/usr/bin/env python3
"""rule30_leftside_million.py: the universal left side of Rule 30 to a million diagonals. Which diagonals are
eventually white, and at each one whether the period doubles or the left side branches (Rowland's question,
section 8.31; Lemma B2 of section 8.59 says the eventually white diagonals never stop). The small item "do branch
points go on for ever" on PERIOD-TWO.md's board. (Local, 2026-10-06; section 8.60.)

RUN-ON:     cpu, one core (pure Python 3, big integers; about 150 MB)
COMMAND:    python3 tests/probes/lexicon/rule30_leftside_million.py [K=1000000] [STEPS=2200000]  |  ... sides
COST:       about ten minutes.

METHOD (section 8.31). The strip of the first K left diagonals, held as a K-bit integer V (bit k = diagonal k), is
a closed system: V' = ((V << 2) xor ((V << 1) or V)) mod 2^K. From the single cell it is run STEPS steps, and the
last 128 strips are kept; an equality V(T) = V(T - P) is a certificate that the strip is periodic with period P
for ever after. Over one period: a diagonal is eventually white if its bit is 0 in every strip of the period. At
an eventually white diagonal j, diagonal j + 1 obeys D(t+1) = D_(j-1)(t) xor D(t): its period is twice that of
diagonal j - 1 when the latter has an odd number of black cells per period (a doubling, Rowland's Proposition
2), and the same period, with two possible continuations, when even (a branch, the seed decides). The single
cell takes the generic branch at each (section 8.31).

SEEN BEFORE these predictions: section 8.31's run to 160,000 diagonals (white at 2, 7, 28, 399; branches at 53207
and 58286 on the generic side; period 16 at 160,000) and rule30_band.py's strip to 53,200. Nothing beyond 160,000.

PREDICTIONS, written 2026-10-06 before this script's first run.
  M0 (control, must hold): the certificate is found with a period P that is a power of two, and the strip's
      eventually white diagonals below 160,000 are exactly 2, 7, 28, 399, 53207, 58286, with 2, 7, 28, 399
      doublings and 53207, 58286 branches.
  M1 (blind): between 160,000 and K there are at least one and at most three more eventually white diagonals.
  M2 (blind): every one of them is a branch: the period at K is still 16.
  M3 (blind): the worst-phase settling front of section 8.59, run to K, has slope between 2.00 and 2.05 at K - 1.
  CF  (counterfactual, must fail): the same strip run 1000 steps fewer than STEPS is NOT yet periodic with period P
      on all K diagonals (the transient really is about 2 K steps; if it were periodic much earlier the front
      bound of section 8.59 would be far from tight).
REFUTED-BY: M0 failing (the instrument, or section 8.31); M1 to M3 the other way; CF passing is recorded, not a
  failure of a proof.

OUTCOME of the first run, 2026-10-06 (K = 1,000,000, 2,200,000 steps in 253 s): certificate found, period 32.
  Eventually white diagonals: 2, 7, 28, 399 (doublings, 1 -> 2 -> 4 -> 8 -> 16), 53207 and 58286 (branches, 16 -> 16),
  87866 (a doubling, 16 -> 32), and none from 87,867 to 999,999.
  M0 FAILED on my list: the probe rule30_leftsides.py had recorded 87866 as a doubling in its own outcome, and the
  prose of section 8.31 did not repeat it; the certificate and the classification of the six listed ones are right.
  M1 REFUTED (no new white diagonal between 160,000 and K). M2 REFUTED (the period at K is 32, from 87,867 on).
  M3 HELD: the worst-phase front's slope is 2.0057 at 999,999 (2.0128 at 100,000).
  CF FAILED by design: the strip settles at about 2.006 steps per diagonal, so it was periodic about 190,000 steps
  before the end; 1,000 steps was no test. Lesson, again: predict from the probes' recorded outcomes, not from prose.
"""
import sys, time
import numpy as np

SIDES = "sides" in sys.argv[1:]
sys.argv = [a for a in sys.argv if a != "sides"]

K = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
STEPS = int(sys.argv[2]) if len(sys.argv) > 2 else 2200000
KEEP = 128
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


# ADDENDUM, written 2026-10-06 before the second run (python3 rule30_leftside_million.py sides), after GPT's C004:
# the four left sides that section 8.31 realised, each to a million diagonals. The generic side (the single cell);
# the flip of diagonal 53208 in its settled strip; the generic side's second split, the flip at 58287; and the
# flipped side's own split, the flip at 72576 in ITS settled strip. A settled strip is itself a finite row, so each
# flipped strip is a finite seed of a million cells.
#   L0 (control, must hold): each side's strip certifies with a power-of-two period; the flipped sides differ from
#       their parent side at the flipped diagonal in the certified cycle, and agree with it (up to phase) below it.
#   L1 (blind): every side's period at a million is 32.
#   L2 (blind): the doubling at 87,866 occurs on all four sides.
#   L3 (blind): no side has an eventually white diagonal between 160,000 and a million.
#   L4 (blind): the four worst-phase settling slopes at a million lie within 0.01 of one another.
# REFUTED-BY: L0 failing (the construction); L1 to L4 the other way.

def run(v, mask, steps, keep):
    hist = []
    for t in range(steps):
        v = ((v << 2) ^ ((v << 1) | v)) & mask
        if t >= steps - keep:
            hist.append(v)
    return hist


def to_bits(v):
    return np.unpackbits(np.frombuffer(v.to_bytes((K + 7) // 8, "little"), dtype=np.uint8), bitorder="little")[:K]


def minimal_period(seq):
    n = len(seq)
    for p in range(1, n + 1):
        if n % p == 0 and all(seq[i] == seq[i + p] for i in range(n - p)):
            return p
    return n


def analyse(name, hist):
    period = next((p for p in range(1, KEEP) if hist[-1] == hist[-1 - p]), None)
    cyc = hist[-period:] if period else hist[-16:]
    U = np.array([to_bits(v) for v in cyc], dtype=np.uint8)
    anyk = U.any(axis=0)
    white = [int(k) for k in np.nonzero(~anyk)[0]]
    kinds = {}
    for j in white:
        if 1 <= j < K - 1:
            before = U[:, j - 1].tolist(); pb = minimal_period(before); w = sum(before[:pb])
            after = U[:, j + 1].tolist(); pa = minimal_period(after)
            kinds[j] = ("doubling" if w % 2 else "branch", pb, pa)
    P = len(cyc)
    worst = np.zeros(K, dtype=np.int64)
    for phi in range(P):
        tau = np.zeros(K, dtype=np.int64); prev = 0
        for k in range(K - 1):
            start = max(int(tau[k]), prev)
            if not anyk[k]:
                nxt = start
            else:
                tt = start
                while not U[(tt + phi) % P, k]:
                    tt += 1
                nxt = tt + 1
            prev = int(tau[k]); tau[k + 1] = nxt
        worst = np.maximum(worst, tau)
    slope = int(np.maximum.accumulate(worst)[K - 1]) / (K - 1)
    print(f"   {name}: period {period}; white " + ", ".join(f"{j} ({kinds[j][0]}, {kinds[j][1]} -> {kinds[j][2]})"
                                                             for j in white if j in kinds)
          + f"; slope {slope:.4f}", flush=True)
    return period, cyc, white, kinds, slope


def sides():
    mask = (1 << K) - 1
    t0 = time.time()
    generic = run(1, mask, STEPS, KEEP)
    res = {"generic": analyse("generic", generic)}
    seedA = res["generic"][1][0] ^ (1 << 53208)
    res["flip 53208"] = analyse("flip 53208", run(seedA, mask, STEPS, KEEP))
    seedB = res["generic"][1][0] ^ (1 << 58287)
    res["flip 58287"] = analyse("flip 58287", run(seedB, mask, STEPS, KEEP))
    seedC = res["flip 53208"][1][0] ^ (1 << 72576)
    res["flip 53208 and 72576"] = analyse("flip 53208 and 72576", run(seedC, mask, STEPS, KEEP))
    print(f"   four sides in {time.time() - t0:.0f} s", flush=True)
    ok0 = all(r[0] is not None and r[0] & (r[0] - 1) == 0 for r in res.values())
    for child, parent, flip in (("flip 53208", "generic", 53208), ("flip 58287", "generic", 58287),
                                ("flip 53208 and 72576", "flip 53208", 72576)):
        cp, cc = res[parent][1], res[child][1]
        low = (1 << flip) - 1
        same_below = any((cc[0] & low) == (v & low) for v in cp)        # agree below the flip, up to phase
        bit = (1 << flip)
        differ_at = all(((cc[0] & bit) != (v & bit)) for v in cp if (cc[0] & low) == (v & low))
        ok0 &= same_below and differ_at
    report("L0 every side certifies; each flipped side agrees with its parent below the flip and differs at it", ok0,
           "; ".join(f"{k}: period {v[0]}" for k, v in res.items()))
    verdict("L1 every side's period at a million is 32", all(v[0] == 32 for v in res.values()))
    verdict("L2 the doubling at 87,866 occurs on all four sides",
            all(87866 in v[3] and v[3][87866][0] == "doubling" for v in res.values()),
            "; ".join(f"{k}: {[j for j in v[2] if j > 60000]}" for k, v in res.items()))
    verdict("L3 no side has an eventually white diagonal between 160,000 and a million",
            all(not any(160000 <= j < K for j in v[2]) for v in res.values()))
    slopes = [v[4] for v in res.values()]
    verdict("L4 the four worst-phase slopes lie within 0.01 of one another", max(slopes) - min(slopes) <= 0.01,
            ", ".join(f"{s:.4f}" for s in slopes))
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if SIDES:
        sides()
        return
    mask = (1 << K) - 1
    t0 = time.time()
    hist = run(1, mask, STEPS, KEEP)
    period = next((p for p in range(1, KEEP) if hist[-1] == hist[-1 - p]), None)
    print(f"   {STEPS} steps in {time.time() - t0:.0f} s; certificate period {period}", flush=True)
    ok0 = period is not None and period & (period - 1) == 0
    cyc = hist[-period:] if period else hist[-16:]
    U = np.array([to_bits(v) for v in cyc], dtype=np.uint8)           # shape (P, K)
    anyk = U.any(axis=0)
    white = [int(k) for k in np.nonzero(~anyk)[0]]
    kinds = {}
    for j in white:
        if j < 1 or j + 1 >= K:
            continue
        before = U[:, j - 1].tolist()
        pb = minimal_period(before)
        weight = sum(before[:pb])
        after = U[:, j + 1].tolist()
        pa = minimal_period(after)
        kinds[j] = ("doubling" if weight % 2 == 1 else "branch", pb, pa)
    print("   eventually white diagonals: " + ", ".join(f"{j} ({kinds[j][0]}, {kinds[j][1]} -> {kinds[j][2]})"
                                                           for j in white if j in kinds), flush=True)
    low = [j for j in white if j < 160000]
    ok0 &= low == [2, 7, 28, 399, 53207, 58286] and all(kinds[j][0] == "doubling" for j in (2, 7, 28, 399) if j in kinds) \
        and all(kinds[j][0] == "branch" for j in (53207, 58286) if j in kinds)
    report("M0 the certificate (a power-of-two period); below 160,000 the whites are 2, 7, 28, 399, 53207, 58286",
           ok0, f"period {period}, below 160,000: {low}")
    new = [j for j in white if j >= 160000]
    verdict("M1 one to three more eventually white diagonals between 160,000 and K", 1 <= len(new) <= 3, f"{new}")
    verdict("M2 every new one is a branch; the period at K is still 16", period == 16 and
            all(kinds[j][0] == "branch" for j in new), f"period {period}")

    # M3: the settling front of section 8.59, worst over the P phases
    P = len(cyc)
    worst = np.zeros(K, dtype=np.int64)
    for phi in range(P):
        tau = np.zeros(K, dtype=np.int64)
        prev = 0
        for k in range(K - 1):
            start = max(int(tau[k]), prev)
            if not anyk[k]:
                nxt = start
            else:
                t = start
                while not U[(t + phi) % P, k]:
                    t += 1
                nxt = t + 1
            prev = int(tau[k])
            tau[k + 1] = nxt
        worst = np.maximum(worst, tau)
    worst = np.maximum.accumulate(worst)
    slope = worst[K - 1] / (K - 1)
    verdict("M3 the worst-phase front's slope at K - 1 is between 2.00 and 2.05", 2.0 <= slope <= 2.05,
            f"tau = {int(worst[K - 1])}, slope {slope:.4f}; at {min(100000, K - 1)}: {worst[min(100000, K - 1)] / min(100000, K - 1):.4f}")

    # CF: 1000 steps earlier the strip is not yet periodic with period P
    early = run(1, mask, STEPS - 1000, period + 1) if period else []
    cf_periodic = bool(early) and early[-1] == early[-1 - period]
    report("CF  1000 steps before the end the strip is not yet periodic (it must not be)", not cf_periodic)
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
