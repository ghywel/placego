#!/usr/bin/env python3
"""A looping torus with an EXACTLY STATIONARY velocity field, and its truth: the phase-locked test.

    loop_torus.py <outdir> [shade=0.25] [turn=80] [tex=m1|broad] [bg=flat|tex] [noise=0]

The torus (R 180, r 70, at the centre of a 1280x720 frame) has its symmetry axis tilted arccos(1/sqrt 3)
= 54.7 degrees from the line of sight (the isometric view) and spins about that axis by exactly one turn
per <turn> frames at 24 fps (turn 80: the outer rim moves 19.6 px/frame; 160: 9.8). Because it spins
about its OWN symmetry axis the surface, the silhouette and the shading never change -- only the texture
slides -- so the Eulerian velocity field (what the surface point under a pixel does) is the same at every
frame, and three turns are rendered so the middle one is a steady-state loop with a full turn on either
side. That makes the loop a test no single frame can be: every frame is a fresh reading of ONE field, and
the readings' distribution over the turn separates what the tracker gets right from what it gets wrong.

Texture, in arc length on the surface: m1 is the ladder's three incommensurate sines (42, 22 and 12 px
periods); broad adds two long periods (about 84 and 170 px), which the coarse levels can hold. Shading is
a fraction <shade> of the luminance following the surface normal (static under the spin; 0 = none).
bg=tex puts a STATIC textured backdrop behind the torus (the same recipe at a different scale and phase,
half contrast), so the reading's other job -- staying quiet on a textured static background -- is gated
in the same loop; truth/back.npy marks the visible backdrop, where the true velocity is zero. noise=<sigma>
adds Gaussian sensor noise of that many 8-bit levels, independent per frame (seeded), so the backdrop's
speckle is a real test of a reading's memory, not of a matcher on a noiseless picture.

Output:
  <outdir>/src.mkv               3 x <turn> frames, ffv1, 8-bit gray, 24 fps
  <outdir>/truth/truth_bwd.npy   float32 [720, 1280, 2] px/frame, x right, y down: the chord n-1 -> n of the
                                 point visible at n -- what the shaders report at output frame n at N:N
  <outdir>/truth/truth_fwd.npy   the chord n -> n+1 (manifolds.py's convention)
  <outdir>/truth/truth_ctr.npy   their mean, the instantaneous velocity to second order
  <outdir>/truth/truth_acc.npy   fwd - bwd: the one-interval acceleration, px/frame^2
  <outdir>/truth/mask.npy        bool [720, 1280], the visible surface
  <outdir>/truth/back.npy        bool [720, 1280], the visible static backdrop (bg=tex; all False for flat)
The truth is computed at frame <turn> and checked against frame 1.5 <turn>: the difference is zero.

Read the machine field of the middle turn with the exact path (format=rgb48le INSIDE the graph):
  sed '/^\\/\\/!PARAM read_view/,/^$/ s/^0$/4/' ../shaders/quaddirectional-interpolation-propagated.glsl > c.glsl
  ffmpeg -init_hw_device vulkan=vk -filter_hw_device vk -i src.mkv \\
      -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=c.glsl,select='between(n\\,80\\,159)',format=rgb48le" \\
      -start_number 80 -frames:v 80 rv4/v%03d.png
then loopfield.py scores the turn. loop.sh does all of it.
"""
import math
import os
import pathlib
import subprocess
import sys
import warnings

import numpy as np

W, H, SS, FPS = 1280, 720, 2, 24.0
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
SHADE = float(sys.argv[2]) if len(sys.argv) > 2 else 0.25
TURN = int(sys.argv[3]) if len(sys.argv) > 3 else 80
TEX = sys.argv[4] if len(sys.argv) > 4 else "m1"
BG = sys.argv[5] if len(sys.argv) > 5 else "flat"
NOISE = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
rng = np.random.default_rng(20260905)
NF = 3 * TURN
OMEGA = 2 * math.pi / (TURN / FPS)
FF = os.environ.get("FFMPEG", "ffmpeg")


def texture(sa, sb):
    m1 = np.sin(0.15 * sa + 0.09 * sb) + np.sin(0.28 * sa - 0.21 * sb) + np.sin(0.51 * sa + 0.44 * sb)
    if TEX == "broad":
        return 0.5 + 0.11 * m1 + 0.08 * (np.sin(0.075 * sa + 0.03 * sb) + np.sin(0.037 * sa - 0.02 * sb))
    return 0.5 + 0.14 * m1


def rot3(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    c, s = math.cos(ang), math.sin(ang); x, y, z = a
    return np.array([[c + x * x * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                     [y * x * (1 - c) + z * s, c + y * y * (1 - c), y * z * (1 - c) - x * s],
                     [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z * z * (1 - c)]])


R, r = 180.0, 70.0
u = np.linspace(0, 2 * np.pi, 2400, endpoint=False); v = np.linspace(0, 2 * np.pi, 900, endpoint=False)
U, V = np.meshgrid(u, v, indexing="ij"); U = U.ravel(); V = V.ravel()
P = np.stack([(R + r * np.cos(V)) * np.cos(U), (R + r * np.cos(V)) * np.sin(U), r * np.sin(V)], -1)
N = np.stack([np.cos(V) * np.cos(U), np.cos(V) * np.sin(U), np.sin(V)], -1)
lum = texture((R + r * np.cos(V)) * U, r * V)
tilt = rot3([1, 0, 0], math.acos(1 / math.sqrt(3)))
Wp, Hp = W * SS, H * SS
YY, XX = np.mgrid[0:H, 0:W]
BACKDROP = 0.12 + (0.07 * (np.sin(0.11 * XX + 0.06 * YY) + np.sin(0.23 * XX - 0.17 * YY) + np.sin(0.41 * XX + 0.37 * YY)) + 0.21 if BG == "tex" else 0.0)


def pose(n):
    M = rot3([0, 0, 1], OMEGA * n / FPS).T @ tilt.T
    Q = P @ M
    return np.stack([Q[:, 0] + W / 2, H / 2 - Q[:, 1]], -1), Q[:, 2], N @ M


def order_of(p2, z):
    xi = np.round(p2[:, 0] * SS).astype(int); yi = np.round(p2[:, 1] * SS).astype(int)
    ok = (xi >= 0) & (xi < Wp) & (yi >= 0) & (yi < Hp)
    o = np.argsort(z[ok])
    return ok, xi[ok][o], yi[ok][o], o


def render(n):
    p2, z, Nn = pose(n)
    ok, xi, yi, o = order_of(p2, z)
    shade = (1.0 - SHADE) + SHADE * np.clip(Nn[:, 2], 0, 1)
    img = np.zeros((Hp, Wp), np.float32); hit = np.zeros((Hp, Wp), bool)
    img[yi, xi] = (lum[ok] * shade[ok])[o]; hit[yi, xi] = True
    img = img.reshape(H, SS, W, SS).mean(axis=(1, 3)); hm = hit.reshape(H, SS, W, SS).any(axis=(1, 3))
    return np.where(hm, img, BACKDROP)


def truth(n):
    pm = pose(n - 1)[0]; p0, z0, _ = pose(n); pp = pose(n + 1)[0]
    fwd = pp - p0; bwd = p0 - pm
    ok, xi, yi, o = order_of(p0, z0)
    outs = []
    for F in (bwd, fwd, fwd - bwd):
        buf = np.full((Hp, Wp, 2), np.nan, np.float32)
        buf[yi, xi] = F[ok][o]
        with np.errstate(all="ignore"), warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)          # nanmean of an all-NaN texel: off the object
            outs.append(np.nanmean(buf.reshape(H, SS, W, SS, 2), axis=(1, 3)).astype(np.float32))
    Fb, Ff, Fa = outs
    return Fb, Ff, (Fb + Ff) * 0.5, Fa, ~np.isnan(Fb[..., 0])


raw = out / "src.gray"
with open(raw, "wb") as fh:
    for n in range(NF):
        img = render(n) * 255
        if NOISE > 0:
            img = img + rng.normal(0.0, NOISE, img.shape)
        fh.write(img.clip(0, 255).astype(np.uint8).tobytes())
        if n % TURN == 0:
            print("  frame %3d" % n, flush=True)
subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "gray", "-s", "%dx%d" % (W, H), "-r", str(FPS),
                "-i", str(raw), "-c:v", "ffv1", "-level", "3", "-pix_fmt", "yuv420p", str(out / "src.mkv")], check=True)
raw.unlink()
td = out / "truth"; td.mkdir(exist_ok=True)
Fb, Ff, Fc, Fa, mask = truth(TURN)
for name, F in (("bwd", Fb), ("fwd", Ff), ("ctr", Fc), ("acc", Fa)):
    np.save(td / ("truth_%s.npy" % name), F)
np.save(td / "mask.npy", mask)
np.save(td / "back.npy", (~mask) if BG == "tex" else np.zeros_like(mask))
Gb, _, _, _, mask2 = truth(TURN + TURN // 2)
d = np.linalg.norm((Fb - Gb)[mask & mask2], axis=1); vn = np.linalg.norm(Fb[mask], axis=1)
print("loop_torus [%s, shade %.2f, turn %d, bg %s, noise %g]: %d frames, rim %.1f px/frame, |v| median %.2f px/frame -> %s" % (TEX, SHADE, TURN, BG, NOISE, NF, OMEGA * (R + r) / FPS, np.median(vn), out / "src.mkv"))
print("  truth at frame %d (%d visible px); stationarity vs frame %d: masks differ on %d px, |dv| max %.4f px" % (TURN, mask.sum(), TURN + TURN // 2, (mask ^ mask2).sum(), d.max() if d.size else 0.0))
