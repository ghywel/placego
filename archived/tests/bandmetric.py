"""Error split into the MOVING BAND and the rest, for realbench outputs.

    bandmetric.py <outroot> <segment-seconds> <label> [label...]

Reads OUTROOT/ref_<s>.mkv (the truth) and OUTROOT/o_<label>_<s>.mkv (the reconstruction) as gray, takes the
odd frames (the synthesised ones), and for each defines the moving band as the texels where the two source
frames the interpolator saw (ref n-1 and n+1) differ by more than 12/255, dilated by 4 px. Prints PSNR over
the band, PSNR outside it, and the band's share of the frame, per label -- the ghosting lives in the band.
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
root = pathlib.Path(sys.argv[1]); seg = sys.argv[2]; labels = sys.argv[3:]


def frames(path):
    p = subprocess.run([FF, "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True)
    wh = subprocess.run([os.environ.get("FFPROBE", "ffprobe"), "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
                        capture_output=True, text=True, check=True).stdout.strip().split(",")
    W, H = int(wh[0]), int(wh[1])
    a = np.frombuffer(p.stdout, np.uint8); n = len(a) // (W * H)
    return a[:n * W * H].reshape(n, H, W).astype(np.float64)


def dilate(m, r):
    o = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1): o |= np.roll(np.roll(m, dy, 0), dx, 1)
    return o


ref = frames(root / ("ref_%s.mkv" % seg))
n = len(ref)
odd = [k for k in range(1, n - 1, 2)]
bands = {}
for k in odd:
    bands[k] = dilate(np.abs(ref[k - 1] - ref[k + 1]) > 12.0, 4)
share = np.mean([bands[k].mean() for k in odd])
print("  segment %s: %d synthesised frames scored, moving band %.1f%% of the frame" % (seg, len(odd), 100 * share))
for label in labels:
    out = frames(root / ("o_%s_%s.mkv" % (label, seg)))
    m = min(len(out), n)
    ib, ob = [], []
    for k in odd:
        if k >= m: break
        e2 = (out[k] - ref[k]) ** 2; b = bands[k]
        if b.sum() > 100: ib.append(e2[b].mean())
        ob.append(e2[~b].mean())
    psnr = lambda mse: 10 * np.log10(255.0 ** 2 / max(np.mean(mse), 1e-9))
    print("    %-14s PSNR in the band %.2f dB   outside %.2f dB   (whole-frame %.2f)" % (label, psnr(ib), psnr(ob), psnr([((out[k] - ref[k]) ** 2).mean() for k in odd if k < m])))
