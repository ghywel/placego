"""ENERGY-TRANSFER.md 2.1: hidden spin -- how much of a body's kinetic energy a centre tracker misses.

    koenig.py <scene dir> [hosts=metal,placebo] [frames=12,48,84] [fs=48] [erode=6]

Reads the field tier's machine velocity (np-scratch/ladder2/field/<scene>/<host>_<k>.png, rgb48le, TRI_DIAG 7,
0.5 + px / (2 fs) in R and G -- decoded as fieldcheck.py decodes it, with the same zero-level alarm) and the
closed-form truth beside it (truth/truth_<k>.npy, the chord over the interval, and mask_<k>.npy). Pixel area is
the mass: the master scenes' bodies are uniform discs.

Koenig's theorem splits the kinetic energy exactly into the centre's share and the share about the centre:
    dense route:  total = sum 1/2 |u|^2 over the body, centre = 1/2 N |mean u|^2, spin = total - centre
    curl route:   omega = median(curl) / 2 over the inner 70 percent of the radius (the rim's alias band and the
                  boundary kept out), spin = 1/2 omega^2 sum r^2 over the body (r from the body's centroid)
The two must agree: that is the check. The truth field goes through the same arithmetic on the same pixels, so
the comparison is instrument against truth; the analytic figure for a uniform disc rolling is 1/3 and for one
spinning in place 1.

Pre-registered (ENERGY-TRANSFER.md, commit ea58d47, before any of this ran): on a rolling disc the dense route
reads 0.32-0.34 and the curl route agrees within 5 percent. The field tier reads frame k best against truth
k or a neighbour (an off-by-one it recorded on the Metal side); each row uses the truth frame that fits best.
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
FP = os.environ.get("FFPROBE", "ffprobe")
scene = pathlib.Path(sys.argv[1])
hosts = (sys.argv[2] if len(sys.argv) > 2 else "metal,placebo").split(",")
frames = [int(k) for k in (sys.argv[3] if len(sys.argv) > 3 else "12,48,84").split(",")]
fs = float(sys.argv[4]) if len(sys.argv) > 4 else 48.0
ER = int(sys.argv[5]) if len(sys.argv) > 5 else 6
tdir = scene / "truth"


def read_png(p):
    wh = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0",
                         str(p)], capture_output=True, text=True, check=True).stdout.strip().split(",")
    W, H = int(wh[0]), int(wh[1])
    raw = subprocess.run([FF, "-v", "error", "-i", str(p), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"],
                         capture_output=True, check=True).stdout
    im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
    return im


def erode(m, r):
    out = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out &= np.roll(np.roll(m, dy, 0), dx, 1)
    return out


def split(u, m, inner, h=8):
    """Spin shares by three routes, and the rigid fit's residual noise.
    dense: Koenig on the raw field (counts per-pixel scatter as energy about the centre -- noise included);
    curl:  omega = median(curl) / 2, the curl by central differences h px apart -- the field is computed on a grid
           of 8-px cells, so differences one pixel apart mostly fall inside a cell (the first run, 0.5x truth);
    rigid: least-squares u = t + omega x r over the body; its residual variance s2 is the noise, and
    dense_corr removes it from the dense route (N s2 / 2 of spurious internal energy)."""
    v = u[m]
    N = len(v)
    mean = v.mean(0)
    ke_c = 0.5 * N * (mean ** 2).sum()
    ke_t = 0.5 * (v ** 2).sum()
    dense = (ke_t - ke_c) / ke_t
    dudy = (np.roll(u[..., 0], -h, 0) - np.roll(u[..., 0], h, 0)) / (2 * h)
    dvdx = (np.roll(u[..., 1], -h, 1) - np.roll(u[..., 1], h, 1)) / (2 * h)
    curl = dvdx - dudy
    omega_c = np.median(curl[inner]) / 2
    ys, xs = np.nonzero(m)
    X, Y = xs - xs.mean(), ys - ys.mean()
    r2 = X ** 2 + Y ** 2
    ke_r = lambda om: 0.5 * om ** 2 * r2.sum()
    curl_share = ke_r(omega_c) / (ke_c + ke_r(omega_c))
    du, dv = v[:, 0] - mean[0], v[:, 1] - mean[1]
    omega_f = (X * dv - Y * du).sum() / r2.sum()
    res = np.stack([du + omega_f * Y, dv - omega_f * X], -1)
    s2 = (res ** 2).sum(-1).mean()                     # per-pixel residual |.|^2: the noise the dense route books as spin
    rigid_share = ke_r(omega_f) / (ke_c + ke_r(omega_f))
    dense_corr = (ke_t - ke_c - 0.5 * N * s2) / (ke_t - 0.5 * N * s2)
    return dict(dense=dense, curl=curl_share, rigid=rigid_share, corr=dense_corr, mean=mean, om_c=omega_c, om_f=omega_f,
                noise=np.sqrt(s2))


print(f"# {scene.name}: fs {fs}, erode {ER} px, pixel area as mass; curl over the 8-px grid; rigid = least-squares t + omega x r")
print(f"{'host':8s} {'k':>3s} {'tk':>3s} {'centre v':>13s} | {'spin share: truth':>17s} {'dense':>6s} {'corr':>6s} {'rigid':>6s} {'curl':>6s}"
      f" | {'omega truth':>11s} {'rigid':>8s} {'curl':>8s} | {'noise px':>8s}")
for host in hosts:
    for k in frames:
        p = scene / f"{host}_{k}.png"
        if not p.exists():
            print(f"{host:8s} {k:3d}  (no {p.name})"); continue
        im = read_png(p)
        meas = np.stack([(im[..., 0] - 0.5) * 2 * fs, (im[..., 1] - 0.5) * 2 * fs], -1)
        best = None
        for fr in (k - 1, k, k + 1):
            tp, mp = tdir / f"truth_{fr:03d}.npy", tdir / f"mask_{fr:03d}.npy"
            if not tp.exists(): continue
            truth, mask = np.load(tp), np.load(mp)
            # THE INSTRUMENT CHECK (fieldcheck.py's): off the body the field is exactly zero, encoded 0.5
            bg = ~mask
            for dy in (-8, 8):
                for dx in (-8, 8):
                    bg &= ~np.roll(np.roll(mask, dy, 0), dx, 1)
            if bg.sum() > 1000:
                z = np.median(im[bg][:, :2], axis=0)
                if np.any(np.abs(z - 0.5) > 0.0005):
                    sys.exit(f"READ PATH BROKEN on {p.name}: the zero level reads {z}, not 0.5")
            m = erode(mask, ER)
            err = np.median(np.abs(meas[m] - truth[m]).sum(-1))
            if best is None or err < best[0]:
                best = (err, fr, truth, mask, m)
        _, fr, truth, mask, m = best
        ys, xs = np.nonzero(mask)
        cx, cy = xs.mean(), ys.mean()
        R = np.sqrt(mask.sum() / np.pi)
        yy, xx = np.mgrid[0:mask.shape[0], 0:mask.shape[1]]
        inner = m & (np.hypot(xx - cx, yy - cy) < 0.7 * R)
        t = split(truth, m, inner)
        r = split(meas, m, inner)
        print(f"{host:8s} {k:3d} {fr:3d} ({r['mean'][0]:5.2f},{r['mean'][1]:5.2f}) | {t['dense']:17.4f} {r['dense']:6.4f} {r['corr']:6.4f}"
              f" {r['rigid']:6.4f} {r['curl']:6.4f} | {t['om_f']:11.5f} {r['om_f']:8.5f} {r['om_c']:8.5f} | {r['noise']:8.3f}")
