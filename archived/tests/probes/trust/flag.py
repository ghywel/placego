#!/usr/bin/env python3
"""THE PER-LEVEL TRUST GATE, step T1 (2026-10-01): which per-level flag says "this level is aliased here", and how often
would it fire on real footage? Offline, one frame at a time; no motion is needed, since the flag is a property of
the image at each level.

    flag.py synthetic                      the ladder's and the masters' textures, and the weave at P = 10 / 14 / 20
    flag.py video <file> [<file> ...]      FRAMES (default 8) frames spread over each file, at its own size, luma
    flag.py census                         the same for the census's 20 sources (halfrate.py's seeded choice; FOOTAGE)

Each pyramid level L (16, 8, 4: the 1/16, 1/8 and 1/4 levels) is built as the shader builds it: the POINT sample, the
mean of the 2 x 2 full-resolution pixels at the texel's centre (a bilinear tap on a pixel boundary). Beside it the
BOX, the mean of the texel's whole L x L footprint. A texel is TEXTURED if its level's 5 x 5 point range is at least
0.02 (the coarse search's MIN_CONTRAST). Three candidate flags, each per texel and level, over that 5 x 5 window
(5L x 5L pixels):
  A  the range ratio      range(box) / range(point)          flag if under tau (0.3, 0.5, 0.7)
  B  the variance ratio   var(box) / var(point)              flag if under tau (0.1, 0.25, 0.5)
  C  the rms frequency    f = rms(gradient) / (2 pi sd)  at full resolution over the window (Rice's mean frequency of
                          the window's spectrum); flag if f > kappa / (2 L), i.e. above the level's Nyquist (kappa 0.7,
                          1.0, 1.4). The gradient is the central difference, so the highest frequencies read low.
Printed: for each source and level, the share of textured texels each flag fires on. Numbers only.
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2]))
import masters                                                                   # noqa: E402

FF = os.environ.get("FFMPEG", str(pathlib.Path.home() / "np-build/ffmpeg/ffmpeg"))
FFPROBE = os.environ.get("FFPROBE", FF.replace("ffmpeg", "ffprobe") if FF.endswith("ffmpeg") else "ffprobe")
LEVELS = (16, 8, 4)
TAU_A, TAU_B, KAPPA = (0.3, 0.5, 0.7), (0.1, 0.25, 0.5), (0.7, 1.0, 1.4)


def boxsum(a, r):
    """sum of a over the (2r+1) x (2r+1) window centred on each element (edges: only what is inside)"""
    c = np.pad(a, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    H, W = a.shape
    y0 = np.clip(np.arange(H) - r, 0, H); y1 = np.clip(np.arange(H) + r + 1, 0, H)
    x0 = np.clip(np.arange(W) - r, 0, W); x1 = np.clip(np.arange(W) + r + 1, 0, W)
    return c[y1][:, x1] - c[y0][:, x1] - c[y1][:, x0] + c[y0][:, x0]


def flags(img):
    """img: luma in [0, 1], H x W. Returns {L: dict of flag name -> (fired, textured) counts}."""
    H, W = img.shape
    gx = np.zeros_like(img); gy = np.zeros_like(img)
    gx[:, 1:-1] = 0.5 * (img[:, 2:] - img[:, :-2]); gy[1:-1] = 0.5 * (img[2:] - img[:-2])
    out = {}
    for L in LEVELS:
        h, w = H // L, W // L
        if h < 7 or w < 7: continue
        c = L // 2
        pt = 0.25 * (img[c - 1:h * L:L, c - 1:w * L:L][:h, :w] + img[c - 1:h * L:L, c:w * L:L][:h, :w]
                     + img[c:h * L:L, c - 1:w * L:L][:h, :w] + img[c:h * L:L, c:w * L:L][:h, :w])
        bx = img[:h * L, :w * L].reshape(h, L, w, L).mean(axis=(1, 3))
        P, B = swv(pt, (5, 5)), swv(bx, (5, 5))                    # (h-4, w-4, 5, 5)
        rp = P.max(axis=(2, 3)) - P.min(axis=(2, 3)); rb = B.max(axis=(2, 3)) - B.min(axis=(2, 3))
        vp = P.var(axis=(2, 3)); vb = B.var(axis=(2, 3))
        # the rms frequency over the 5L x 5L window centred on the texel's centre
        r = (5 * L) // 2
        n = boxsum(np.ones_like(img), r)
        m1 = boxsum(img, r) / n; m2 = boxsum(img * img, r) / n
        g2 = boxsum(gx * gx + gy * gy, r) / n
        sd = np.sqrt(np.maximum(m2 - m1 * m1, 1e-12))
        f = np.sqrt(g2) / (2 * math.pi * sd)
        fc = f[c:h * L:L, c:w * L:L][:h, :w][2:-2, 2:-2]            # at the texel centres, the 5 x 5 windows' middles
        tex = rp >= 0.02
        nt = int(tex.sum())
        d = {"textured": (nt, rp.size)}
        for t in TAU_A: d[f"A<{t}"] = (int((tex & (rb < t * rp)).sum()), nt)
        for t in TAU_B: d[f"B<{t}"] = (int((tex & (vb < t * vp)).sum()), nt)
        for k in KAPPA: d[f"C>{k}"] = (int((tex & (fc > k / (2 * L))).sum()), nt)
        d["f_med"] = float(np.median(fc[tex])) if nt else float("nan")
        out[L] = d
    return out


def merge(acc, d):
    for L, dd in d.items():
        a = acc.setdefault(L, {})
        for k, v in dd.items():
            if k == "f_med": a.setdefault(k, []).append(v)
            else:
                p = a.get(k, (0, 0)); a[k] = (p[0] + v[0], p[1] + v[1])


def report(name, acc):
    for L in LEVELS:
        if L not in acc: continue
        a = acc[L]
        nt, ntot = a["textured"]
        cols = "  ".join(f"{k} {100 * a[k][0] / max(a[k][1], 1):5.1f}%" for k in a if k not in ("textured", "f_med"))
        fm = np.nanmedian(a["f_med"]) if a["f_med"] else float("nan")
        print(f"{name:34s} 1/{L:<2d} textured {100 * nt / max(ntot, 1):5.1f}%  f_med 1/{1 / fm if fm > 0 else float('inf'):5.1f}px | {cols}",
              flush=True)


def ladder(expr_u_v):
    def f(u, v): return eval(expr_u_v, {"np": np, "sin": np.sin, "u": u, "v": v}) / 255.0
    return f


SYN = {
    "weave P=10": lambda u, v: weave(u, v, 10.0),
    "weave P=14 (the masters' weave)": lambda u, v: masters.tex_value("weave", u, v),
    "weave P=20": lambda u, v: weave(u, v, 20.0),
    "noise (masters' fbm)": lambda u, v: masters.tex_value("noise", u, v),
    "cells": lambda u, v: masters.tex_value("cells", u, v),
    "wood": lambda u, v: masters.tex_value("wood", u, v),
    "sines": lambda u, v: masters.tex_value("sines", u, v),
    "lattice (masters, period 40)": lambda u, v: masters.tex_value("lattice", u, v),
    "TEX_M1 (five sines, 4.6-42 px)": ladder("128+22*(sin(0.15*u+0.09*v)+sin(0.28*u-0.21*v)+sin(0.51*u+0.44*v)+sin(0.83*u-0.97*v)+sin(1.21*u+0.64*v))"),
    "TEX_L7 (period 15.7)": ladder("128+110*sin(u/2.5)*sin(v/2.5)"),
    "TEX_M2 (period 40)": ladder("128+110*sin(u/6.366)*sin(v/6.366)"),
    "TEX_M3 (period 16)": ladder("128+110*sin(u/2.546)*sin(v/2.546)"),
    "TEX_V1 (soft bars, 24)": ladder("128+110*sin(v/3.8197)"),
    "TEX_V2 (stairs, 24)": ladder("18+220*(sin(v/3.8197)>0)"),
    "TEX_P (stairs + fine speckle)": ladder("18+220*(sin(v/3.8197)>0)+12*sin(u/2.2)*sin(v/1.8)"),
}


def weave(u, v, P):
    a = 0.5 + 0.5 * np.sin(2 * np.pi * u / P); b = 0.5 + 0.5 * np.sin(2 * np.pi * v / P)
    over = ((np.floor(u / P).astype(np.int64) + np.floor(v / P).astype(np.int64)) % 2) == 0
    thread = np.where(over, a * 0.7 + b * 0.3, b * 0.7 + a * 0.3)
    return 0.15 + 0.7 * thread + 0.1 * (masters.vnoise(u / 3, v / 3) - 0.5)


if sys.argv[1] == "synthetic":
    ys, xs = np.mgrid[0:720, 0:1280].astype(np.float64)
    for name, fn in SYN.items():
        img = np.clip(fn(xs + 0.5 + 37.0, ys + 0.5 + 11.0) * 0.9 + 0.05, 0, 1) if "TEX_" not in name else np.clip(fn(xs + 0.5, ys + 0.5), 0, 1)
        acc = {}; merge(acc, flags(img)); report(name, acc)
else:
    NF = int(os.environ.get("FRAMES", "8"))
    paths = sys.argv[2:]
    if sys.argv[1] == "census":                                # the census's 20 sources (halfrate.py's choice, verbatim)
        import random
        V = (".mkv", ".mp4", ".m4v", ".avi", ".mov")

        def pick(root, n, seed):
            folders = sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir())
            out = []
            for f in random.Random(seed).sample(folders, min(n, len(folders))):
                vids = [p for p in f.rglob("*") if p.suffix.lower() in V and p.stat().st_size > 50e6]
                if vids: out.append(max(vids, key=lambda p: p.stat().st_size))
            return out
        FOOTAGE = os.environ.get("FOOTAGE", "/footage")
        paths = [str(p) for p in pick(f"{FOOTAGE}/Movies", 12, 20260930) + pick(f"{FOOTAGE}/Anime", 4, 20260930)
                 + pick(f"{FOOTAGE}/Shows", 4, 20260930)]
    for path in paths:
        dur = float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                   capture_output=True, text=True).stdout.strip() or 0)
        wh = subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                             "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip().split(",")
        Wv, Hv = int(wh[0]), int(wh[1])
        acc = {}
        for i in range(NF):
            t = dur * (i + 0.5) / NF
            r = subprocess.run([FF, "-v", "error", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1", "-vf", "format=gray16le",
                                "-f", "rawvideo", "-pix_fmt", "gray16le", "-"], capture_output=True)
            if len(r.stdout) != Wv * Hv * 2: continue
            img = np.frombuffer(r.stdout, "<u2").reshape(Hv, Wv).astype(np.float64) / 65535.0
            merge(acc, flags(img))
        report(pathlib.Path(path).stem[:34], acc)
