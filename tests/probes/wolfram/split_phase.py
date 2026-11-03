#!/usr/bin/env python3
"""split_phase.py NSEEDS: why the split at wheel 53,208 is decided at one phase (round 14, fifth block; Cloud, CL695; after 8.31's
LS8). Left-finite strip of K wheels (big integer, bit k = wheel k) run to T; the bits of wheels 53,200..53,210 are recorded at
every tick. For each row: the cycles (last 64 rows), the settling time of each wheel (first time from which it equals its cycle),
the last black of wheel 53,207, the first black of C = cycle of 53,206 after both parents settle, the constant of wheel 53,208, and
the phases measured against the row's own cycle (the shift aligning its C to the single seed's C). Predictions in the tracker."""
import sys, numpy as np
NS = int(sys.argv[1]); K0 = 53200; K = 53300; T = int(1.45 * 53300) + 64; MASK = (1 << K) - 1
WH = list(range(K0, K0 + 11))
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rng = np.random.default_rng(53)
seeds = [1] + [int(rng.integers(0, 1 << 24)) | 1 for _ in range(NS)]
ref_C = None
for seed in seeds:
    V = seed; hist = np.zeros((T, len(WH)), dtype=np.uint8)
    for t in range(T):
        for i, k in enumerate(WH): hist[t, i] = (V >> k) & 1
        V = stp(V)
    # cycles from the last 64 rows (period dividing 16 assumed; checked)
    cyc = {}; ok = True
    for i, k in enumerate(WH):
        c = hist[T - 16:T, i]; c2 = hist[T - 32:T - 16, i]; c3 = hist[T - 48:T - 32, i]
        if not (np.array_equal(c, c2) and np.array_equal(c, c3)): ok = False
        cyc[k] = c   # c[r] = value at t with t % 16 == (T - 16 + r) % 16
    def cycval(k, t): return int(cyc[k][(t - (T - 16)) % 16])
    tau = {}
    for i, k in enumerate(WH):
        mism = [t for t in range(T) if hist[t, i] != cycval(k, t)]
        tau[k] = (mism[-1] + 1) if mism else 0
    kw = 53207; i_w = WH.index(kw)
    blacks = np.flatnonzero(hist[:, i_w]); last_black = int(blacks[-1]) if len(blacks) else None
    tp = max(tau[53205], tau[53206])
    fb = next(t for t in range(tp, T) if cycval(53206, t) == 1)        # first black of C after the parents settle
    # phase against the single seed's cycle C_53206: find shift j with cyc[53206] == ref shifted by j
    C = cyc[53206]
    if ref_C is None: ref_C = C.copy(); shift = 0
    else:
        shift = next((j for j in range(16) if np.array_equal(np.roll(ref_C, j), C)), None)
    const = ''.join(str(int(x)) for x in cyc[53208])
    equal_parents = np.array_equal(cyc[53205], cyc[53206])
    ph = " ".join(f"{(tau[k] - (shift or 0)) % 16:2d}" for k in WH)
    print(f"seed 0x{seed:x}: settling phases of wheels 53200..53210 against own cycle: {ph}")
    print(f"seed 0x{seed:x}: cycles consistent {ok}; parents equal {equal_parents}; tau 53205={tau[53205]}, 53206={tau[53206]}, 53207={tau[53207]}, 53208={tau[53208]}; "
          f"last black of 53207 at {last_black} (= first black of C after parents settle - 1: {last_black == fb - 1}); "
          f"shift vs seed {shift}; phases vs own cycle: tau53206 {(tau[53206] - (shift or 0)) % 16}, last black {(last_black - (shift or 0)) % 16}; "
          f"black at parents' settling {int(hist[tp, i_w])}; constant word of 53208 {const}", flush=True)
print("SPLIT_PHASE_DONE")
