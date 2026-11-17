"""Painting a velocity field the way the shaders' read_view 1 does, in numpy, for the tests that compare a
measured field with a truth field on equal terms (loopfield.py). Hue is direction (red = moving right,
cyan = left, purple/blue = down, yellow-green = up), saturation and visibility follow the shader's gates
(nothing below 1 px/frame, full colour at 3), over the picture at 0.35 luma. The shader paints its POOLED
field (13x13 cells, with memory across frames); this paints the field it is given as it is.
"""
import os
import subprocess

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)


def hsv2rgb(h, s, v):
    K = np.array([1.0, 2.0 / 3.0, 1.0 / 3.0])
    p = np.abs(((h[..., None] + K) % 1.0) * 6.0 - 3.0)
    return v[..., None] * (1.0 + s[..., None] * (np.clip(p - 1.0, 0, 1) - 1.0))


def maxfilt(a, r, step):
    o = a.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            o = np.maximum(o, np.roll(np.roll(a, dy * step, 0), dx * step, 1))
    return o


def paint(F, lum, vel=True):
    """F: (H, W, 2) px per frame (or per frame^2 with vel=False, the acceleration gates); lum: (H, W) in 0..1."""
    H, W = F.shape[:2]
    YY, XX = np.mgrid[0:H, 0:W]
    border = smoothstep(4.0, 28.0, np.minimum(np.minimum(XX, W - 1 - XX), np.minimum(YY, H - 1 - YY)).astype(np.float32))
    lo, hi, sat_full = (1.0, 2.0, 3.0) if vel else (0.12, 0.22, 0.30)
    Fz = np.nan_to_num(F); mag = np.linalg.norm(Fz, axis=-1)
    vis = smoothstep(lo, hi, mag) * 0.9 * smoothstep(0.5 * lo, lo, maxfilt(mag, 2, 8)) * border
    sat = 0.95 * smoothstep(lo, sat_full, mag)
    hue = (np.arctan2(Fz[..., 1], Fz[..., 0]) / (2 * np.pi)) % 1.0
    rgb = hsv2rgb(hue, sat, np.ones_like(mag))
    out = (lum * 0.35)[..., None] * (1 - vis[..., None]) + rgb * vis[..., None]
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)


def paint_err(E, mask, scale=4.0):
    """An error field: hue = direction of the error, brightness = |error| / scale px; dark grey off the mask."""
    Ez = np.nan_to_num(E); mag = np.linalg.norm(Ez, axis=-1)
    hue = (np.arctan2(Ez[..., 1], Ez[..., 0]) / (2 * np.pi)) % 1.0
    rgb = hsv2rgb(hue, np.ones_like(mag), np.clip(mag / scale, 0, 1))
    rgb[~mask] = 0.08
    return (rgb * 255).astype(np.uint8)


def png(path, img):
    """Write an (H, W, 3) uint8 image through ffmpeg (no image library needed)."""
    subprocess.run([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (img.shape[1], img.shape[0]), "-i", "-",
                    "-update", "1", str(path)], input=img.tobytes(), check=True)


def load_rgb24(path, W, H, select=None):
    """Decode one frame of a file (frame `select` of a video, or an image) to (H, W, 3) uint8."""
    cmd = [FF, "-v", "error", "-i", str(path)]
    if select is not None:
        cmd += ["-vf", "select='eq(n\\,%d)'" % select, "-frames:v", "1"]
    raw = subprocess.run(cmd + ["-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8)[:H * W * 3].reshape(H, W, 3)


def up8(F, C=8):
    """A cell field (h, w, 2) to full res: nearest x C then a C x C box blur (a linear ramp between cells)."""
    G = np.repeat(np.repeat(F, C, axis=0), C, axis=1).astype(np.float32)
    cs = np.cumsum(np.cumsum(np.pad(G, ((C, C), (C, C), (0, 0))), axis=0), axis=1)
    r = C // 2; h, w = G.shape[:2]
    return (cs[C + r:C + r + h, C + r:C + r + w] - cs[C - r:C - r + h, C + r:C + r + w]
            - cs[C + r:C + r + h, C - r:C - r + w] + cs[C - r:C - r + h, C - r:C - r + w]) / float((2 * r) ** 2)
