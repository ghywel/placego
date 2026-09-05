#!/usr/bin/env python3
"""Synthetic cel-animation scenes with an EXACT in-between at every instant.

    ./cel_scenes.py <scene> <out.mkv> [frames=97] [fps=24]      scene: rigid | walk | walk_flat

Flat fills, two-pixel dark outlines, anti-aliased by 2x supersampling, 640x360 -- the regime the cel work
is measured in (decimate-and-reconstruct at 360p keeps a walk inside the tracker's reach). Unlike the
footage, where the true in-between of a walk cycle is a third drawing no warp can reach, these scenes are
rendered at every instant, so the odd frames of a decimated pair ARE the ground truth and the metrics mean
what they say.

rigid      a character (head, body, two straight legs) translating right at 6 px/frame with a head bob,
           limbs fixed: the template's ideal, an in-between that is exactly a rigid shift, over a
           DETAILED static background (the plate's case: what the character uncovers has structure).
walk       the same, with the legs swinging +-25 degrees at 1.5 Hz: redrawn limbs, a real in-between that
           is neither source drawing shifted.
walk_flat  walk over a flat sky, as the footage was.
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np

W, H, SS = 640, 360, 2
scene = sys.argv[1]; out = pathlib.Path(sys.argv[2])
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 97
FPS = float(sys.argv[4]) if len(sys.argv) > 4 else 24.0
FF = os.environ.get("FFMPEG", "ffmpeg")
Wp, Hp = W * SS, H * SS
Y, X = np.mgrid[0:Hp, 0:Wp]; X = (X + 0.5) / SS; Y = (Y + 0.5) / SS      # pixel coordinates at the supersample centres


def background(flat):
    if flat:
        return np.full((Hp, Wp, 3), [0.40, 0.65, 0.92])
    bg = np.zeros((Hp, Wp, 3))
    bg[..., 0] = 0.55 + 0.25 * ((np.floor(X / 40) + np.floor(Y / 40)) % 2)          # a checker
    bg[..., 1] = 0.55 + 0.20 * np.sin(X / 9.0) * np.sin(Y / 13.0)                    # and a soft weave
    bg[..., 2] = 0.50 + 0.30 * ((np.floor(Y / 26)) % 2)                              # and stripes
    return bg


def ellipse(cx, cy, rx, ry, ang=0.0):
    c, s = math.cos(ang), math.sin(ang)
    u = (X - cx) * c + (Y - cy) * s; v = -(X - cx) * s + (Y - cy) * c
    return (u / rx) ** 2 + (v / ry) ** 2 <= 1.0


def capsule(x0, y0, x1, y1, r):
    dx, dy = x1 - x0, y1 - y0; L2 = dx * dx + dy * dy + 1e-9
    t = np.clip(((X - x0) * dx + (Y - y0) * dy) / L2, 0, 1)
    px, py = x0 + t * dx, y0 + t * dy
    return (X - px) ** 2 + (Y - py) ** 2 <= r * r


def erode(m, r):
    o = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r: o &= np.roll(np.roll(m, dy, 0), dx, 1)
    return o


def draw(t, legs_swing, flat):
    cx = 60.0 + 6.0 * FPS * t                       # 6 px per frame
    cy = 200.0 + 3.0 * math.sin(2 * math.pi * 3.0 * t)
    img = background(flat).copy()
    parts = []                                       # (mask, colour)
    swing = math.radians(25.0) * math.sin(2 * math.pi * 1.5 * t) if legs_swing else 0.0
    for sgn in (-1.0, 1.0):
        a = sgn * swing
        x1, y1 = cx + 30.0 * math.sin(a) + sgn * 8.0, cy + 30.0 + 30.0 * math.cos(a)
        parts.append((capsule(cx + sgn * 8.0, cy + 30.0, x1, y1, 7.0), [0.95, 0.60, 0.25]))
    parts.append((ellipse(cx, cy + 5.0, 26.0, 32.0), [0.35, 0.60, 0.90]))          # body
    parts.append((ellipse(cx + 6.0, cy - 36.0, 22.0, 20.0), [0.35, 0.60, 0.90]))   # head
    parts.append((ellipse(cx + 14.0, cy - 40.0, 5.0, 6.0), [1.0, 1.0, 1.0]))      # eye
    parts.append((ellipse(cx + 15.0, cy - 40.0, 2.0, 2.5), [0.05, 0.05, 0.08]))   # pupil
    for m, col in parts:
        img[m] = col
    union = np.zeros((Hp, Wp), bool)
    for m, _ in parts: union |= m
    outline = union & ~erode(union, 2 * SS)          # a 2 px ink line around the silhouette
    for m, _ in parts[:3]:                           # and around each part, so limbs read as drawn
        outline |= m & ~erode(m, 2 * SS)
    img[outline] = [0.08, 0.06, 0.12]
    return img.reshape(H, SS, W, SS, 3).mean(axis=(1, 3))


legs, flat = {"rigid": (False, False), "walk": (True, False), "walk_flat": (True, True)}[scene]
raw = out.with_suffix(".rgb")
with open(raw, "wb") as fh:
    for n in range(NF):
        fh.write((draw(n / FPS, legs, flat) * 255).clip(0, 255).astype(np.uint8).tobytes())
subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", str(FPS),
                "-i", str(raw), "-c:v", "ffv1", "-level", "3", "-pix_fmt", "yuv444p", str(out)], check=True)
raw.unlink()
print("%s: %d frames at %g fps, 6 px/frame walk%s over a %s background -> %s" % (scene, NF, FPS, " with swinging legs" if legs else ", limbs fixed", "flat" if flat else "detailed", out))
