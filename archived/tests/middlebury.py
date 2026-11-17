#!/usr/bin/env python3
"""Score a machine velocity frame (read_view 4) against a Middlebury ground-truth flow (.flo).

    middlebury.py <v.png (rgb48le, mode 4)> <flow.flo> [fs=32]

The Middlebury "other" set (Baker, Scharstein, Lewis, Roth, Black, Szeliski, IJCV 2011) publishes the
flow from frame10 to frame11 of eight-frame colour sequences; the shaders, fed the sequence at N:N,
report at output frame n the chord n-1 -> n, so the frame to score is the one that lands on frame11.
Read it through the exact path (format=rgb48le inside the filter graph). The .flo is float32 [H, W, 2]
after a 'PIEH' tag and two int32 (w, h); values above 1e9 are unknown and left unscored.

Prints the benchmark's two measures, average endpoint error (AEE, px) and average angular error (AAE,
degrees, the angle between (u, v, 1) vectors), plus the median endpoint error, the fraction of pixels
within 1 px, and the same for the zero field (the floor any reading must beat). The field is 1/8-res,
bilinearly upsampled by the shader; the truth is per pixel, so the number includes that resolution.
"""
import os
import pathlib
import struct
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
FP = os.environ.get("FFPROBE", "ffprobe")
png = pathlib.Path(sys.argv[1]); flo = pathlib.Path(sys.argv[2])
fs = float(sys.argv[3]) if len(sys.argv) > 3 else 32.0

with open(flo, "rb") as fh:
    tag, w, h = struct.unpack("<fii", fh.read(12))
    assert abs(tag - 202021.25) < 1e-3, "not a .flo file"
    tr = np.frombuffer(fh.read(), np.float32).reshape(h, w, 2).astype(np.float64)
known = np.all(np.abs(tr) < 1e9, axis=-1)
wh = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(png)],
                    capture_output=True, text=True, check=True).stdout.strip().split(",")
W, H = int(wh[0]), int(wh[1])
assert (W, H) == (w, h), "frame %dx%d, truth %dx%d" % (W, H, w, h)
raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True, check=True).stdout
im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
meas = np.stack([(im[..., 0] - 0.5) * 2 * fs, (im[..., 1] - 0.5) * 2 * fs], -1)


def scores(F):
    e = np.linalg.norm(F - tr, axis=-1)[known]
    a = np.concatenate([F, np.ones(F.shape[:2] + (1,))], -1); b = np.concatenate([tr, np.ones(tr.shape[:2] + (1,))], -1)
    cos = (a * b).sum(-1) / (np.linalg.norm(a, axis=-1) * np.linalg.norm(b, axis=-1))
    ang = np.degrees(np.arccos(np.clip(cos, -1, 1)))[known]
    return e.mean(), np.median(e), ang.mean(), (e < 1.0).mean()


tn = np.linalg.norm(tr, axis=-1)[known]
print("  %s: %dx%d, %d known px, |truth| mean %.2f max %.2f px" % (flo.parent.name, w, h, known.sum(), tn.mean(), tn.max()))
for name, F in (("reading", meas), ("zero field", np.zeros_like(tr))):
    aee, mede, aae, w1 = scores(F)
    print("  %-11s AEE %.3f px  median EPE %.3f  AAE %.2f deg  within 1 px %.1f%%" % (name, aee, mede, aae, 100 * w1))
