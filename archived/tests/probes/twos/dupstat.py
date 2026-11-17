#!/usr/bin/env python3
"""The cadence branch's held-copy statistic, computed offline (2026-09-19): for every consecutive pair of a source,
the MAXIMUM |A - B| over the coarse level exactly as the quad builds it (LUMA_*_S: one bilinear tap per 16 x 16
cell at the cell's centre, i.e. the mean of the central 2 x 2 pixels), and the cut statistic (the mean of a 24 x 24
sparse grid of it). Reads the source at its own rate; a lavfi string or a file.

    dupstat.py <source> [frames]          FFMPEG in the environment, or ~/np-build/ffmpeg

Prints one line per pair: n, max, mean, and the branch's verdict at the shipped CADENCE_DUP_MAX. Built when the
ones column of the ladder moved under the branch and the shader could not say why: it said the branch never fires
there (every pair 0.5-1.0), and the movement was the Mac ladder's own run-to-run noise (NFRAME-LIMITS.md,
2026-09-19). Then the survey: on four anime episodes held drawings read 0.000-0.011 after the encoder and the
smallest real moves 0.03 and up; a live-action pool reads 0.03-0.9 with exact copies only at clip ends and a
clean static shot at 0.016-0.019; the engine's stage (the private NFrameDemo tree, the player) counts the same
copies this does, 26 of 132 on the on-twos clip."""
import os, subprocess, sys
import numpy as np

FF = os.environ.get("FFMPEG", os.path.expanduser("~/np-build/ffmpeg/ffmpeg"))
DUP_MAX = float(os.environ.get("CADENCE_DUP_MAX", "0.02"))

def frames(src, n):
    fmt = [] if os.path.isfile(src) else ["-f", "lavfi"]
    cmd = [FF, "-hide_banner", "-loglevel", "error", *fmt, "-i", src, "-frames:v", str(n),
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    p = subprocess.run(cmd, capture_output=True, stdin=subprocess.DEVNULL)
    probe = subprocess.run([FF, "-hide_banner", *fmt, "-i", src, "-frames:v", "1", "-f", "null", "-"],
                           capture_output=True, text=True, stdin=subprocess.DEVNULL).stderr
    import re
    m = re.search(r"(\d{2,5})x(\d{2,5})", probe)
    w, h = int(m.group(1)), int(m.group(2))
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    return a.reshape(-1, h, w).astype(np.float32) / 255.0

def s_level(f):
    h, w = f.shape
    ys = np.arange(h // 16) * 16 + 8; xs = np.arange(w // 16) * 16 + 8
    # the bilinear tap at (x*16+8, y*16+8) in pixel units is centred between pixels 7|8 of the cell
    return 0.25 * (f[np.ix_(ys - 1, xs - 1)] + f[np.ix_(ys - 1, xs)] + f[np.ix_(ys, xs - 1)] + f[np.ix_(ys, xs)])

def main():
    src = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 48
    fr = frames(src, n)
    s = [s_level(f) for f in fr]
    print(f"{os.path.basename(src)[:70]}  frames {len(fr)}  S-level {s[0].shape[1]}x{s[0].shape[0]}  DUP_MAX {DUP_MAX}")
    fired = 0
    for i in range(1, len(s)):
        d = np.abs(s[i] - s[i - 1])
        sh, sw = d.shape
        gy = ((np.arange(24) + 0.5) / 24 * sh).astype(int); gx = ((np.arange(24) + 0.5) / 24 * sw).astype(int)
        mean24 = float(d[np.ix_(gy, gx)].mean())
        held = d.max() < DUP_MAX
        fired += held
        print(f"  pair {i - 1:3d}-{i:<3d}  max {d.max():.4f}  mean24 {mean24:.4f}  {'HELD' if held else ''}")
    print(f"  pairs read as held: {fired}/{len(s) - 1}")

if __name__ == "__main__":
    main()
