"""Score a machine-read velocity frame against a manifolds.py truth field.

    fieldcheck.py <v.png (rgb48le, mode 4)> <truthdir> <frame> [fs=32] [outprefix]

Decodes 0.5 + px / (2 fs) from R and G (the PNG is read through ffmpeg as raw rgb48le: no image library
on this Python), compares with truth_<frame>.npy over the visible mask eroded by 6 px so the boundary's own
ambiguity is not scored, and prints: median and 90th-percentile |error|, the gross fraction (|error| >
2 px), the median angular error where |v| > 1 px, and the same against the two neighbouring truth frames so
a one-frame misalignment shows itself. Optional images (PPM): <outprefix>-meas / -true / -err, hue =
direction, brightness = magnitude / (fs/4) (err: |err| / 4 px).
"""
import pathlib
import subprocess
import sys

import numpy as np

import os
# $FFMPEG / $FFPROBE as the other tests here use them (on Windows, native paths with the patched build's
# DLL directory already on PATH -- the MSYS shell TOOLS.md describes), else the ones on PATH
FF = os.environ.get("FFMPEG", "ffmpeg")
FP = os.environ.get("FFPROBE", "ffprobe")
png = pathlib.Path(sys.argv[1]); tdir = pathlib.Path(sys.argv[2]); frame = int(sys.argv[3])
fs = float(sys.argv[4]) if len(sys.argv) > 4 else 32.0
outp = sys.argv[5] if len(sys.argv) > 5 else None
ERODE = int(sys.argv[6]) if len(sys.argv) > 6 else 3       # px of boundary left unscored; 1-2 for tube scenes

wh = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(png)],
                    capture_output=True, text=True, check=True).stdout.strip().split(",")
W, H = int(wh[0]), int(wh[1])
raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True, check=True).stdout
im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
meas = np.stack([(im[..., 0] - 0.5) * 2 * fs, (im[..., 1] - 0.5) * 2 * fs], -1)


def erode(m, r):
    out = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out &= np.roll(np.roll(m, dy, 0), dx, 1)
    return out


def score(fr):
    p = tdir / ("truth_%03d.npy" % fr)
    if not p.exists():
        return None
    tr = np.load(p); mk = np.load(tdir / ("mask_%03d.npy" % fr))
    assert tr.shape[:2] == (H, W), (tr.shape, (H, W))
    mk = erode(mk, ERODE) & ~np.isnan(tr[..., 0])
    if mk.sum() == 0:
        return None
    e = meas[mk] - tr[mk]; en = np.linalg.norm(e, axis=1); tn = np.linalg.norm(tr[mk], axis=1)
    mv = tn > 1.0
    if mv.any():
        cosang = (meas[mk][mv] * tr[mk][mv]).sum(1) / (np.linalg.norm(meas[mk][mv], axis=1) * tn[mv] + 1e-9)
        ang = np.degrees(np.arccos(np.clip(cosang, -1, 1)))
    else:
        ang = np.array([np.nan])
    # POOLED: both fields box-averaged over 24x24 px inside the mask (the reading's own scale), which
    # separates per-texel noise (averages away) from bias (does not)
    P = 24
    def pool(A, m):
        Hs, Ws = (H // P) * P, (W // P) * P
        a = np.where(m[..., None], A, 0.0)[:Hs, :Ws].reshape(Hs // P, P, Ws // P, P, 2).sum(axis=(1, 3))
        c = m[:Hs, :Ws].reshape(Hs // P, P, Ws // P, P).sum(axis=(1, 3))
        full = c >= P * P * 0.9
        return a[full] / c[full][:, None], full
    pm, full = pool(meas, mk); pt, _ = pool(tr, mk)
    pe = np.linalg.norm(pm - pt, axis=1); ptn = np.linalg.norm(pt, axis=1)
    pooled = dict(n=int(full.sum()), med=float(np.median(pe)) if full.any() else np.nan,
                  rel=float(np.median(pe[ptn > 1.0] / ptn[ptn > 1.0])) if (ptn > 1.0).any() else np.nan)
    return dict(n=int(mk.sum()), med=float(np.median(en)), p90=float(np.percentile(en, 90)), gross=float((en > 2.0).mean()),
                ang=float(np.median(ang)), tmean=float(tn.mean()), mmean=float(np.linalg.norm(meas[mk], axis=1).mean()), pooled=pooled)


res = {fr: score(fr) for fr in (frame - 1, frame, frame + 1)}
scored = [fr for fr in res if res[fr]]
if not scored:
    sys.exit("  nothing to score: the mask is empty after erosion (try a smaller erosion)")
best = min(scored, key=lambda fr: res[fr]["med"])
for fr in sorted(res):
    r = res[fr]
    if r:
        print("  vs truth %3d: n=%6d  median %.3f px  p90 %.3f  gross(>2px) %5.1f%%  angle %5.1f deg  |v| true %.2f meas %.2f | pooled 24px: n=%d median %.3f px = %.1f%% of |v|%s"
              % (fr, r["n"], r["med"], r["p90"], 100 * r["gross"], r["ang"], r["tmean"], r["mmean"],
                 r["pooled"]["n"], r["pooled"]["med"], 100 * r["pooled"]["rel"], "   <- best" if fr == best else ""))
if best != frame:
    print("  NOTE: best alignment is truth frame %d, not %d: an off-by-one in the read; quote that row" % (best, frame))


def hue_img(V, fsv):
    mag = np.linalg.norm(V, axis=-1); ang = np.arctan2(V[..., 1], V[..., 0])
    h = (ang / (2 * np.pi)) % 1.0; v = np.clip(np.nan_to_num(mag) / fsv, 0, 1)
    i = np.floor(h * 6).astype(int) % 6; f = h * 6 - np.floor(h * 6)
    p = np.zeros_like(v); q = v * (1 - f); t = v * f
    r = np.select([i == 0, i == 1, i == 2, i == 3, i == 4, i == 5], [v, q, p, p, t, v])
    g = np.select([i == 0, i == 1, i == 2, i == 3, i == 4, i == 5], [t, v, v, q, p, p])
    b = np.select([i == 0, i == 1, i == 2, i == 3, i == 4, i == 5], [p, p, t, v, v, q])
    out = np.stack([r, g, b], -1); out[np.isnan(mag)] = 0.08
    return (out * 255).astype(np.uint8)


def ppm(path, img):
    with open(path, "wb") as fh:
        fh.write(b"P6\n%d %d\n255\n" % (img.shape[1], img.shape[0])); fh.write(img.tobytes())


if outp:
    tr = np.load(tdir / ("truth_%03d.npy" % best)); mk = np.load(tdir / ("mask_%03d.npy" % best))
    m2 = meas.copy(); m2[~mk] = np.nan
    ppm(outp + "-meas.ppm", hue_img(m2, fs / 4)); ppm(outp + "-true.ppm", hue_img(tr, fs / 4)); ppm(outp + "-err.ppm", hue_img(m2 - tr, 4.0))
    print("  wrote %s-{meas,true,err}.ppm (brightness |v| / %.0f px; err / 4 px)" % (outp, fs / 4))
