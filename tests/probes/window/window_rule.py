"""The patch's frame-window selection, transcribed from frame-mix-hook.patch and tabulated (2026-09-08,
M-series prep). The Metal engine hard-codes [i-1, i, i+1, i+2], which is right for a four-frame window and
WRONG for three or five: the patch guarantees the nearest-before and nearest-after frames first, then fills
the remaining slots GREEDILY from whichever side's next candidate is closer to the output time, so an odd
window leans toward the side the output timestamp is nearer. Sorted into timestamp order at the end, that
is HOOKED = earliest, FRAMEk = the k-th in time.

    window_rule.py [src_fps out_fps]      default 24 60; also prints 24 24 (N:N) and 25 60

The rule (libplacebo's own words in the patch, and the C it describes):
    split = first index whose timestamp > 0            # timestamps are relative to the output time
    lo, hi = split - 1, split
    take lo, then hi                                    # "nearest before" / "nearest after"
    while slots remain: take whichever of lo / hi is closer by |timestamp|, ties to lo
    the hook sees them in TIMESTAMP order
and the hook fires only when the full window was available: fewer frames near the ends of a clip fall
through to the builtin mixer, which is the engine's `wasHold`. Tabulated in STEADY STATE (100 frames in).

Checked against a recorded fact: at N:N the three-frame window is [-1, 0, +1], so the frame the output
sits on is SLOT 1 -- which is what the record already says the tridirectional's anchor is at N:N.
"""
import sys

src = float(sys.argv[1]) if len(sys.argv) > 2 else 24.0
out = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0


def window(n_want, t_src, n_frames=1000):
    """the source indices the hook sees, in timestamp order, for output time t_src in source-frame units"""
    ts = lambda i: i - t_src
    split = None
    for i in range(n_frames):
        if ts(i) > 0.0:
            split = i
            break
    if split is None:
        split = n_frames
    lo, hi = split - 1, split
    sel = []
    if lo >= 0 and len(sel) < n_want:
        sel.append(lo); lo -= 1
    if hi < n_frames and len(sel) < n_want:
        sel.append(hi); hi += 1
    while len(sel) < n_want and (lo >= 0 or hi < n_frames):
        take_lo = lo >= 0 and (hi >= n_frames or abs(ts(lo)) <= ts(hi))
        if take_lo:
            sel.append(lo); lo -= 1
        else:
            sel.append(hi); hi += 1
    return sorted(sel)


def table(src, out):
    print(f"\n=== {src:g} -> {out:g} fps: the window as OFFSETS from i = floor(t_src), for one period of the phase")
    period = 0
    k = 1
    while k < 400:
        if abs((k * src / out) - round(k * src / out)) < 1e-9:
            period = k
            break
        k += 1
    period = period or 12
    print(f"{'out k':>5} {'t_src':>8} {'phase':>6}  " + "  ".join(f"N={n}" for n in (2, 3, 4, 5, 6)))
    BASE = 100          # steady state: a clip START fills the window one-sided (no frames before 0),
    for k in range(period + 1):   # which is a boundary artifact, not the rule being tabulated
        t = BASE + k * src / out
        i = int(t // 1)
        ph = t - i
        cells = []
        for n in (2, 3, 4, 5, 6):
            w = window(n, t)
            cells.append("[" + ",".join(f"{x - i:+d}" for x in w) + "]")
        print(f"{k:5d} {t:8.4f} {ph:6.3f}  " + "  ".join(f"{c:22s}" for c in cells))
    print("  (the offsets are relative to i = floor(t_src); at phase exactly 0 the output sits ON a source")
    print("   frame, so 'nearest before' is that frame itself and the window shifts one place left)")


table(src, out)
if (src, out) == (24.0, 60.0):
    table(24.0, 24.0)
    table(25.0, 60.0)
print("""
WHAT THE SWIFT HOST MUST TAKE FROM THIS
  N = 2 and N = 4 are the fixed offsets the engine already uses ([0,+1] and [-1,0,+1,+2]) at every phase
  except phase 0 (N:N), where every window shifts one left.
  N = 3, 5 (tri, quint) DEPEND ON THE PHASE: the third (and fifth) frame comes from whichever side the
  output is nearer. A host that hard-codes [-1, 0, +1] renders the tri correctly only for phases below 0.5
  and silently feeds it the wrong window above -- which the acceptance ladder WILL see (the tri's numbers
  are a published column) but a picture might not.
  N = 6 (sext) is again fixed at [-2,-1,0,+1,+2,+3] for phases in (0, 1).
  rts_mix[j] = (window[j] - t_src), the frame's time relative to the output, in SOURCE-FRAME units, which
  is what the shaders' tau values are built from; mix_t = -rts[0] / (rts[1] - rts[0]) for N = 2.
  pair_changed is true whenever the selected window differs from the previous invocation's.""")
