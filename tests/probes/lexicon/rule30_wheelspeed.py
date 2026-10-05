#!/usr/bin/env python3
"""rule30_wheelspeed.py: does the wheel turn at a constant rate? Its angle's velocity, acceleration and diffusion.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_wheelspeed.py [W=12] [T=4096] | ... carry [W] [T]
COST:       a few minutes on one core.

The owner's lead (2026-10-05): "We have looked at motion field concepts such as velocity, acceleration, jerk, snap,
crackle ... A wheel may turn at a non-constant rate." Within an exact stretch the wheel turns at exactly 17/56 of a
turn per step. The walls kick its angle by whole notches (1/28 of a turn, section 8.8), so its long-run rate is
17/56 plus the walls' net kick per step. rule30_spectrum_fine.py put column 1's line at 0.30365, slightly above
17/56 = 0.303571, which would be a net forward drift of about 0.12 notches per 56-step window.

Method. For each unlocked right half up to W cells, over T steps, the wheel's phase d_k is read at each exact
window k (column 1 equal to U delayed by d_k). Between consecutive exact windows the angle changes by a whole number
of notches, n = ((-17 (d_k' - d_k)) mod 56) / 2, taken in [-14, 13]. Summing them gives the angle A(k), unwrapped
(beyond the steady 17/56 per step), at every exact window. The excess speed v(k) is the mean of A's change per
window, over all right halves, as a function of the window index k (the time).

PREDICTIONS, written 2026-10-05 before this script's first run:
  V0 (cross-instrument, blind): the mean excess speed, as a rotation number 17/56 + v / (28 x 56), lies within
     0.0001 of the spectral line 0.30365 of rule30_spectrum_fine.py, an independent instrument.
  A1 (blind; the owner's acceleration): the wheel's speed is not constant in time. The mean excess speed over windows
     2..10 and over windows 40..70 differ by at least 25% of the larger.
  A2 (blind): the angle diffuses normally. The variance of A(k + L) - A(k) grows as L^g with g in [0.8, 1.2] for lags
     L = 1..32 windows (not ballistic, g near 2, and not trapped, g near 0).
  C  (control): every phase change between exact windows is an even time shift (the trace's parity is kept), so every
     angle change is a whole number of notches. It is checked, not assumed.
REFUTED-BY: C failing (the harness); V0, A1 or A2 failing.

OUTCOME of the first run, 2026-10-05 (W = 12, T = 4096): C passed (0 odd shifts).
  V0 REFUTED, narrowly: the mean excess speed is -0.0457 notches per window (slightly backward), a rotation number of
     0.303542, against the spectral line's 0.30365, 0.000108 apart against a tolerance of 0.0001. Caveat: across a long
     gap between exact windows, an angle change beyond +-14 notches is unwrapped wrongly, which can bias the direct
     drift. A spectral peak need not sit at the mean rate when the kicks are asymmetric. The two instruments differ at
     the 10^-4 level, and which is nearer the truth is open.
  A1 HELD as worded but NOT MEANINGFUL: early -0.0622, late -0.0294 notches per window (53%). The window-by-window
     speeds swing from -0.21 to +0.15, far more than that difference, and the prediction had no significance test, so
     this shows no real acceleration. (The swings themselves are larger than independent right halves would give,
     about +-0.04, which hints that slips are synchronised in time across right halves. Not tested.)
  A2 HELD: the variance of the angle's change grows as L^1.16 (7.2 notches^2 at 1 window, 432 at 32): normal diffusion,
     about 7 notches^2 per window.
  The toy-size smoke test exposed an index error (too few windows for A1's ranges). It is fixed; the full run was not
  affected.

ADDENDUM, written 2026-10-05 before its first run (python3 rule30_wheelspeed.py carry [W=12] [T=4096]): the owner's
alias. The owner (2026-10-05): "The wheel once again surfaces a leap shift we found in the interpolation shaders: the
wheel is inherently circular, but the pyramid and its grid are inherently a two-dimensional array." In the shaders a
periodic texture's shift is known only modulo its period (the half-period alias, NFRAME-LIMITS.md, 2026-09-28), and
the fix was a carry: keep the candidates and let continuity decide. Here the wheel's angle is known only modulo a turn
(28 notches at one parity), and V0's unwrapping took each change between exact windows in [-14, 13]. That range is
asymmetric (a true +14 is recorded as -14), and across a long gap the angle diffuses far enough (about 7 notches^2 per
window, A2) to wrap. Both bias the drift backward, and the recorded drift was backward (-0.0457) where the spectrum
said forward (+0.12). The carry: read the phase in a 56-step window starting at EVERY even time, not only at
multiples of 56, so that consecutive exact windows are close and no single change approaches half a turn.
  U0 (control): the aligned windows reproduce the first run's excess speed (-0.0457 notches per window), and every
      change between consecutive sliding windows is an even shift.
  U1 (blind; the owner's alias): with the carry the excess speed is forward, and the rotation number lies within
      0.0001 of the spectral line 0.30365 (V0 holds once the alias is removed).
  U2 (blind): alias events exist: in at least one aligned gap in 200, the carried change over the same stretch differs
      from the aligned wrapped change by a whole turn (28 notches).
"""
import math, sys, pathlib

_nums = [a for a in sys.argv[1:] if a != "carry"]
W = int(_nums[0]) if len(_nums) > 0 else 12
T = int(_nums[1]) if len(_nums) > 1 else 4096
P = 56

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
ROT = {tuple(U[(t - d) % P] for t in range(P)): d for d in range(P)}
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1(R, n):
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def main():
    nwin = T // P
    sums = [0.0] * nwin                                   # summed angle change per window index (spread over gaps)
    counts = [0] * nwin
    odd = 0
    traj = []                                             # per right half: angle at each exact window
    for R in range(1 << W):
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad < T - P - 400:
            continue                                      # locked
        ph = [ROT.get(tuple(c[k * P:(k + 1) * P])) for k in range(nwin)]
        ex = [(k, d) for k, d in enumerate(ph) if d is not None]
        A, angle = {}, 0
        for (k, d), (k2, d2) in zip(ex, ex[1:]):
            delta = (d2 - d) % P
            odd += delta % 2
            nn = ((-17 * delta) % P)
            nn = nn - P if nn > P // 2 else nn
            nn //= 2
            A.setdefault(k, angle)
            angle += nn
            A[k2] = angle
            for j in range(k, k2):                        # spread the change evenly over the windows it spans
                sums[j] += nn / (k2 - k)
                counts[j] += 1
        if ex:
            A.setdefault(ex[0][0], 0)
        traj.append(A)
    report("C every phase change between exact windows is an even time shift", odd == 0, f"{odd} odd shifts")
    v = [sums[k] / counts[k] if counts[k] else float("nan") for k in range(nwin)]
    tot = sum(sums[k] for k in range(nwin) if counts[k])
    n_all = sum(counts[k] for k in range(nwin) if counts[k])
    vbar = tot / n_all if n_all else 0.0
    rot = 17 / 56 + vbar / (28 * 56)
    verdict("V0 the kicks' net drift reproduces the spectral line 0.30365 within 0.0001", abs(rot - 0.30365) <= 0.0001,
            f"mean excess speed {vbar:+.4f} notches per window, rotation number {rot:.6f}")
    early = [v[k] for k in range(2, min(11, nwin)) if counts[k]]
    late = [v[k] for k in range(40, min(71, nwin)) if counts[k]]
    if not early or not late:
        print("   (too few windows for A1 at this size)")
        early, late = early or [0.0], late or [0.0]
    ve, vl = sum(early) / len(early), sum(late) / len(late)
    diff = abs(ve - vl) / max(abs(ve), abs(vl)) if max(abs(ve), abs(vl)) > 0 else 0.0
    verdict("A1 the wheel's speed changes with time (windows 2..10 against 40..70 differ by at least 25%)", diff >= 0.25,
            f"early {ve:+.4f}, late {vl:+.4f} notches per window; difference {diff:.0%} of the larger")
    print("   excess speed by window (notches per window, mean over right halves): "
          + " ".join(f"{k}:{v[k]:+.3f}" for k in range(1, nwin, 4) if counts[k]), flush=True)
    lags, var = [], []
    for L in (1, 2, 4, 8, 16, 32):
        xs = [A[k + L] - A[k] for A in traj for k in A if k + L in A]
        if len(xs) > 100:
            m = sum(xs) / len(xs)
            lags.append(L)
            var.append(sum((x - m) ** 2 for x in xs) / len(xs))
    if len(lags) < 2 or min(var) <= 0:
        print("   (too few lags for A2 at this size)")
        lags, var = [1, 2], [1.0, 2.0]
    lx = [math.log(x) for x in lags]
    ly = [math.log(y) for y in var]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    g = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    verdict("A2 the angle diffuses normally: variance grows as L^g, g in [0.8, 1.2]", 0.8 <= g <= 1.2,
            f"g = {g:.2f}; variance by lag " + ", ".join(f"{L}: {x:.2f}" for L, x in zip(lags, var)))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def notches(dD):
    """A phase change dD (mod 56, even) as notches in [-14, 13], as V0 took it."""
    nn = (-17 * dD) % P
    nn = nn - P if nn > P // 2 else nn
    return nn // 2


def carry():
    rots = {"".join(map(str, key)): d for key, d in ROT.items()}
    nwin = T // P
    a_tot = a_span = c_tot = c_span = 0
    odd = gaps = alias = 0
    for R in range(1 << W):
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad < T - P - 400:
            continue                                      # locked, as in the first run
        cs = "".join(map(str, c))
        # aligned windows, as V0 (absolute phase D = d)
        ex = [(k, rots.get(cs[k * P:(k + 1) * P])) for k in range(nwin)]
        ex = [(k * P, d) for k, d in ex if d is not None]
        # sliding windows at every even start (absolute phase D = (t + d) mod 56)
        sl = []
        for t in range(0, T - P + 1, 2):
            d = rots.get(cs[t:t + P])
            if d is not None:
                sl.append((t, (t + d) % P))
        cum, angle = {}, 0                                # carried angle at each sliding exact window
        for (t1, D1), (t2, D2) in zip(sl, sl[1:]):
            dD = (D2 - D1) % P
            odd += dD % 2
            angle += notches(dD)
            cum[t2] = angle
        if sl:
            cum[sl[0][0]] = 0
            c_tot += angle
            c_span += (sl[-1][0] - sl[0][0]) / P
        for (t1, D1), (t2, D2) in zip(ex, ex[1:]):
            wrapped = notches((D2 - D1) % P)
            a_tot += wrapped
            a_span += (t2 - t1) / P
            if t1 in cum and t2 in cum:
                gaps += 1
                diff = cum[t2] - cum[t1] - wrapped
                alias += diff != 0 and diff % 28 == 0
    va, vc = a_tot / a_span, c_tot / c_span
    report("U0 the aligned windows reproduce -0.0457; every sliding change is an even shift",
           abs(va - (-0.0457)) < 0.00005 and odd == 0, f"aligned {va:+.4f} notches per window; {odd} odd shifts")
    rot = 17 / 56 + vc / (28 * 56)
    verdict("U1 with the carry the drift is forward and the rotation number is within 0.0001 of 0.30365",
            vc > 0 and abs(rot - 0.30365) <= 0.0001, f"carried {vc:+.4f} notches per window, rotation number "
            f"{rot:.6f} (aligned {17 / 56 + va / (28 * 56):.6f})")
    verdict("U2 alias events in at least 1 of 200 aligned gaps", gaps > 0 and alias * 200 >= gaps,
            f"{alias} of {gaps} aligned gaps")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    carry() if "carry" in sys.argv[1:] else main()
