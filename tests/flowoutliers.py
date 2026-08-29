#!/usr/bin/env python3
"""Measure isolated-outlier islands in the flow field.

    ./flowoutliers.py <flowvis-render.mkv> [radius-px] [threshold-px]

The cartoon defect this was built for is a small patch of flow pointing
somewhere its whole neighbourhood disagrees with -- a confident block match to
a facial feature that was REDRAWN between source frames rather than moved.
Frame-averaged image metrics are blind to that (it is a few hundred pixels on
a handful of frames), and this project has twice been misled by a metric that
could not see the thing being judged. So measure the defect directly.

For every pixel: how far does its flow sit from the MEDIAN of its
neighbourhood? A genuine motion boundary is a CONTIGUOUS region, so most of
its neighbours share its value and its deviation from a large-radius median
stays small. An isolated false match is a local minority everywhere and
deviates hugely. That asymmetry is what lets this see false matches while
ignoring real motion -- the same discrimination the vector median filter
itself relies on.

Input is a flow-visualiser render (see flowvis.py), which encodes f.x in R and
f.y in G as 0.5 + f*0.05, i.e. +-10 px full scale, 0.078 px per 8-bit step.

Set FFMPEG/FFPROBE to point at the patched build.
"""
import os
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
FP = os.environ.get("FFPROBE", "ffprobe")
SCALE = 10.0 / 127.5          # one 8-bit step, in pixels

RADIUS = int(sys.argv[2]) if len(sys.argv) > 2 else 6
THRESH = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0


def load(path):
    """Decode a flowvis render to (fx, fy) arrays in pixels."""
    # Probe rather than assume. A hardcoded frame size silently reinterprets
    # the byte stream at any other resolution and still prints a full,
    # plausible table -- exactly the failure mode this harness has been
    # burned by before.
    dims = subprocess.run(
        [FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "csv=p=0:s=x", path],
        capture_output=True, text=True).stdout.strip()
    try:
        w, h = (int(x) for x in dims.split("x"))
    except ValueError:
        sys.exit(f"could not probe dimensions of {path} (got {dims!r})")

    raw = subprocess.run(
        [FF, "-v", "error", "-i", path, "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-"],
        capture_output=True).stdout
    frame = w * h * 3
    n = len(raw) // frame
    if n == 0:
        sys.exit(f"no frames decoded from {path}")
    if len(raw) % frame:
        print(f"  warning: {len(raw) % frame} trailing bytes -- not a whole frame")

    a = np.frombuffer(raw, np.uint8)[:n * frame].reshape(n, h, w, 3)
    print(f"  {n} frames at {w}x{h}")
    return ((a[..., 0].astype(np.float32) - 127.5) * SCALE,
            (a[..., 1].astype(np.float32) - 127.5) * SCALE)


def med_blur(a, r):
    """Median over a (2r+1) box, sampled on a decimated grid.

    Sampling the neighbourhood rather than using every pixel is fine here:
    what is wanted is the neighbourhood's consensus value, not an exact
    median, and this keeps a full-clip sweep to a few seconds.
    """
    h, w = a.shape
    p = np.pad(a, r, mode="edge")
    step = max(1, r // 3)
    stack = [p[dy + r:dy + r + h, dx + r:dx + r + w]
             for dy in range(-r, r + 1, step)
             for dx in range(-r, r + 1, step)]
    return np.median(np.stack(stack, 0), axis=0)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__.strip().splitlines()[2].strip())

    fx, fy = load(sys.argv[1])
    n = fx.shape[0]
    tot_out = 0
    tot_px = 0
    worst = []
    for i in range(n):
        dev = np.hypot(fx[i] - med_blur(fx[i], RADIUS),
                       fy[i] - med_blur(fy[i], RADIUS))
        out = int((dev > THRESH).sum())
        tot_out += out
        tot_px += dev.size
        worst.append((out, i, float(dev.max())))

    worst.sort(reverse=True)
    print(f"  radius {RADIUS}px  threshold {THRESH}px")
    print(f"  outlier pixels: {tot_out} / {tot_px} "
          f"({100.0 * tot_out / tot_px:.4f}%)")
    print(f"  mean per frame: {tot_out / n:.1f}")
    print("  worst frames (count, frame, max deviation px):")
    for c, i, m in worst[:6]:
        print(f"    frame {i:3d}  {c:6d} px  max {m:5.1f}")


if __name__ == "__main__":
    main()
