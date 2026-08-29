#!/usr/bin/env python3
"""Find TEMPORAL defects: where the output does not flow smoothly in time.

    ./jitter.sh <source> [start] [duration]     # wrapper that renders and pipes

WHY A SECOND DETECTOR. prospect.py measures the FLOW FIELD and finds isolated
false matches -- one region disagreeing with its neighbourhood. That is a
spatial test, and it is blind to a whole class of defect:

  * flow that is uniform but WRONG, so nothing disagrees with anything
  * judder and stutter, where each frame is individually fine but the sequence
    does not advance evenly
  * anything the gate or the blend does to the OUTPUT, since the flow field is
    unchanged by it

This measures the output instead, and asks a different question: does frame
n follow frame n-1 by about as much as frame n-1 followed n-2?

TWO READINGS.

**Phase profile.** At 23.976 -> 60 there are five output frames per two source
intervals, so the pipeline has a five-frame cycle. If interpolation is even,
every phase should show the same mean frame-to-frame change. A ratio of
max/min across phases well above 1 means the cycle itself is uneven -- the
classic judder where some steps are large and others near zero. This project
has measured 8.75x from a hard mix_t switch and 1.09x after fixing it.

**Local anomalies.** Frames whose change differs sharply from their immediate
neighbours in the same phase. A smooth pan has a large but STEADY change; a
defect is a discontinuity in that steadiness, not a large value. Comparing
within a phase matters, because comparing across phases would just rediscover
the cycle.

Neither reading proves a defect. Both narrow where to look.
"""
import argparse
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys

import numpy as np


def read_exactly(fh, n):
    chunks, got = [], 0
    while got < n:
        b = fh.read(n - got)
        if not b:
            return None
        chunks.append(b)
        got += len(b)
    return b"".join(chunks)


def hhmmss(t):
    m, s = divmod(t, 60)
    h, m = divmod(int(m), 60)
    return f"{h:d}:{m:02d}:{s:06.3f}" if h else f"{int(m):d}:{s:06.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--width", type=int, required=True)
    ap.add_argument("--height", type=int, required=True)
    ap.add_argument("--out-fps", type=float, default=60.0)
    ap.add_argument("--src-fps", type=float, default=24000.0 / 1001.0)
    ap.add_argument("--offset", type=float, default=0.0)
    ap.add_argument("--phase", type=int, default=5,
                    help="output frames per pipeline cycle (5 for 24->60)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--save", metavar="FILE")
    ap.add_argument("--load", metavar="FILE")
    ap.add_argument("--progress", type=int, default=0)
    ap.add_argument("--exclude", metavar="FILE",
                    help="file of source timestamps to mask -- typically scene "
                         "cuts, which otherwise dominate both readings")
    ap.add_argument("--exclude-pad", type=int, default=5,
                    help="output frames masked either side of each timestamp")
    args = ap.parse_args()

    if args.load:
        d = []
        for line in open(args.load):
            if line.startswith("#") or not line.strip():
                continue
            d.append(float(line.split("\t")[1]))
        diffs = np.array(d)
    else:
        w, h = args.width, args.height
        nbytes = w * h
        prev = None
        d = []
        while True:
            buf = read_exactly(sys.stdin.buffer, nbytes)
            if buf is None:
                break
            cur = np.frombuffer(buf, np.uint8).astype(np.float32)
            if prev is not None:
                d.append(float(np.abs(cur - prev).mean()))
            prev = cur
            if args.progress and len(d) % args.progress == 0 and d:
                print(f"    ...{len(d)} frames", file=sys.stderr, flush=True)
        diffs = np.array(d)

    n = len(diffs)
    if n < args.phase * 4:
        sys.exit(f"only {n} frame deltas -- too few to profile")

    if args.save:
        with open(args.save, "w") as fh:
            fh.write(f"# jitter scan\n# out_fps {args.out_fps}\n")
            fh.write(f"# offset {args.offset}\n# frame\tdelta\n")
            for i, v in enumerate(diffs):
                fh.write(f"{i}\t{v:.6f}\n")
        print(f"  saved {n} deltas to {args.save}")

    # A cut is an enormous frame-to-frame change. Left in, it dominates the
    # anomaly ranking and skews whichever phase it happens to land on, which
    # is the difference between "this material judders" and "this material
    # contains cuts". Mask them and read what is underneath.
    mask = np.zeros(n, dtype=bool)
    if args.exclude:
        stamps = []
        for line in open(args.exclude):
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    stamps.append(float(line.split()[0]))
                except ValueError:
                    pass
        for ts in stamps:
            k = int(round((ts - args.offset) * args.out_fps))
            mask[max(0, k - args.exclude_pad):min(n, k + args.exclude_pad + 1)] = True
        print(f"  masked {int(mask.sum())} of {n} deltas "
              f"around {len(stamps)} excluded timestamps")

    live = diffs[~mask]
    print(f"  {n} frame-to-frame deltas, mean {live.mean():.3f}"
          + (f" (excluding masked)" if mask.any() else ""))

    # --- phase profile ----------------------------------------------------
    # Delta i is between output frames i and i+1, so its phase is i % period.
    print()
    print("  phase profile (even interpolation gives a flat column)")
    means = []
    for p in range(args.phase):
        sel = diffs[p::args.phase][~mask[p::args.phase]]
        m = sel.mean() if sel.size else 0.0
        means.append(m)
        bar = "#" * int(round(40 * m / max(live.mean() * 2, 1e-9)))
        print(f"    phase {p}: {m:7.3f}  {bar}")
    ratio = max(means) / max(min(means), 1e-9)
    verdict = ("even" if ratio < 1.15 else
               "slightly uneven" if ratio < 1.4 else
               "UNEVEN -- visible judder likely")
    print(f"    max/min = {ratio:.2f}x  ({verdict})")

    # --- local anomalies --------------------------------------------------
    # Compared WITHIN a phase: across phases the cycle above would dominate.
    print()
    print("  local anomalies (delta against its own phase's neighbours)")
    score = np.zeros(n)
    local = np.zeros(n)
    for p in range(args.phase):
        idx = np.arange(p, n, args.phase)
        v = diffs[idx]
        if v.size < 5:
            continue
        # local median over a small window in the same phase
        k = 5
        pad = np.pad(v, k, mode="edge")
        loc = np.array([np.median(pad[i:i + 2 * k + 1]) for i in range(v.size)])
        local[idx] = loc
        score[idx] = np.abs(v - loc) / np.maximum(loc, 1e-3)
    score[mask] = 0.0

    order = np.argsort(-score)
    print("    rank   time         delta   local    ratio")
    print("    " + "-" * 46)
    shown, seen = 0, []
    for i in order:
        t = args.offset + i / args.out_fps
        if any(abs(t - s) < 0.25 for s in seen):
            continue
        seen.append(t)
        print(f"    {shown + 1:>4}   {hhmmss(t):>9}  {diffs[i]:7.3f}  "
              f"{local[i]:7.3f}  {1 + score[i]:6.2f}x")
        shown += 1
        if shown >= args.top:
            break


if __name__ == "__main__":
    main()
