#!/usr/bin/env python3
"""The master scenes as ground truth on any host (2026-09-12): the second tier beside the ladder.

    masters.py <scene> [--size WxH] [--src-fps F] [--out-fps F] [--frames N] [--settle N]
               [--bg flat|textured] [--texture NAME] [--export-source SRC.raw] [--export-truth TRUTH.raw]
               [--export-field DIR]
    masters.py --list [--size WxH]

The ladder (scenes.sh) is forty-two small, sub-pixel-calibrated cases: the shader regression gate, frozen.
This is the other tier: the full-frame master scenes the Metal demo shows -- a rectangle bouncing off all
four walls under five speed laws, a disc breathing (pure divergence) with or without spin, a disc spinning
under three laws, and a spoked wheel rolling without slipping including the wagon-wheel profile whose
spokes advance exactly one pitch per source frame. Each is one analytic law of (x, y, t), so the same law
renders the source at one rate and the exact truth at another, as the ladder's lavfi expressions do.

The laws are the demo engine's, ported line for line (nframe/metal-demo/Sources/QuadEngine/QuadEngine.swift,
SyntheticScene): every constant, the exact box-filter coverage of the rectangle, the one-pixel ramp on a
disc's rim, the wheel's ink, the deterministic textures. The identity check (probes/masters/identity.sh)
holds this file to the engine's own exports to the last 16-bit level, so the engine is not the truth --
this file is, and anyone with python3, numpy and ffmpeg regenerates it.

Time: every law is written in frames at 24 fps (px per frame, the ladder's unit), and that is its clock
at any source rate: source frame k is law time k * 24 / fps, so a scene lasts the same at 60 as at 24 with
finer steps; the truth at the output rate samples law time j * 24 / outFps. `--settle N` holds the scene
still for its first N law frames (the demo uses 24: the reading's settling second).

Output: rgb48le rawvideo (R = G = B, 16-bit, the value rounded from the law) -- what the demo's CLI exports,
so probes/masters/check.sh scores both hosts against the same bytes. Textured ground = the demo's dim
five-sine field under the mover (every edge an occlusion); flat = black.

The FIELD truth (--export-field DIR, the plan's S4): per source interval k, truth_NNN.npy [H, W, 2] float32
is the one-interval chord of the material point under each pixel -- where it is at source frame k + 1 minus
where it is at k, in px (x right, y down), the quantity a two-frame flow measures -- and mask_NNN.npy the
mover's coverage at k; the ground is still, its chord zero. manifolds.py's format, so fieldcheck.py scores a
machine-read frame against it. Closed forms: a translating rectangle's chord is its centre's; a breathing
disc's is the radial scaling r(k+1)/r(k) (with the spin's turn); a spinning disc's the turn; the wheel's
its axle's travel plus the turn about it.
"""
import argparse
import math
import sys

import numpy as np

# ------------------------------------------------------------------ the textures (deterministic)

def hash2(i, j):
    """The engine's 64-bit integer hash in [0, 1): SplitMix-style, wrapping arithmetic."""
    i = np.asarray(i, dtype=np.int64).astype(np.uint64); j = np.asarray(j, dtype=np.int64).astype(np.uint64)
    h = i * np.uint64(0x9E3779B97F4A7C15)
    h = h ^ (j * np.uint64(0xC2B2AE3D27D4EB4F))
    h = h ^ (h >> np.uint64(31)); h = h * np.uint64(0xBF58476D1CE4E5B9); h = h ^ (h >> np.uint64(29))
    return (h >> np.uint64(11)).astype(np.float64) / float(1 << 53)

def vnoise(x, y):
    xf = np.floor(x); yf = np.floor(y)
    xi = xf.astype(np.int64); yi = yf.astype(np.int64)
    fx = x - xf; fy = y - yf
    fx = fx * fx * (3 - 2 * fx); fy = fy * fy * (3 - 2 * fy)
    a = hash2(xi, yi); b = hash2(xi + 1, yi); c = hash2(xi, yi + 1); d = hash2(xi + 1, yi + 1)
    return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy

def fbm(x, y):
    a, f, s = 0.5, 1.0 / 64.0, 0.0
    for _ in range(5):
        s = s + a * vnoise(x * f + 17.3, y * f + 9.1); a *= 0.5; f *= 2
    return s

def cells(x, y):
    g = 48.0
    cx = np.floor(x / g).astype(np.int64); cy = np.floor(y / g).astype(np.int64)
    best = np.full(x.shape, 1e9)
    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            px = ((cx + i).astype(np.float64) + hash2(cx + i, cy + j)) * g
            py = ((cy + j).astype(np.float64) + hash2(cy + j + 977, cx + i + 331)) * g
            best = np.minimum(best, (x - px) * (x - px) + (y - py) * (y - py))
    d = np.sqrt(best) / (0.72 * g)
    m = np.minimum(d, 1)
    return 0.15 + 0.8 * (1 - m) * (1 - m)

def wood(x, y):
    r = np.sqrt((x - 260) * (x - 260) + (y - 1800) * (y - 1800)) + 7 * fbm(x * 1.7, y * 0.6)
    rings = 0.5 + 0.5 * np.sin(r / 9.0)
    grain = 0.5 + 0.5 * vnoise(x / 2.6, y / 55.0)
    return 0.18 + 0.7 * (0.6 * rings * rings + 0.4 * grain)

def weave(x, y):
    p = 14.0
    a = 0.5 + 0.5 * np.sin(2 * np.pi * x / p); b = 0.5 + 0.5 * np.sin(2 * np.pi * y / p)
    over = ((np.floor(x / p).astype(np.int64) + np.floor(y / p).astype(np.int64)) % 2) == 0
    thread = np.where(over, a * 0.7 + b * 0.3, b * 0.7 + a * 0.3)
    return 0.15 + 0.7 * thread + 0.1 * (vnoise(x / 3, y / 3) - 0.5)

def tex(x, y):
    """The engine's five-sine field: the legacy laws' texture and the dim ground."""
    return (0.5 + 0.16 * np.sin(2 * np.pi * x / 173.0) + 0.13 * np.sin(2 * np.pi * x / 89.0 + 0.7)
            + 0.09 * np.sin(2 * np.pi * (x + 0.6 * y) / 127.0) + 0.07 * np.sin(2 * np.pi * y / 97.0)
            + 0.05 * np.sin(2 * np.pi * x / 47.0 + 2.1))

TEXTURES = ["sines", "lattice", "flat", "noise", "cells", "wood", "weave"]

def tex_value(name, u, v):
    if name == "sines": return tex(u, v)
    if name in ("lattice", "m2"): return 0.5 + 0.43 * np.sin(u / 6.366) * np.sin(v / 6.366)
    if name == "flat": return np.full(u.shape, 0.5)
    if name == "noise": return fbm(u, v)
    if name == "cells": return cells(u, v)
    if name == "wood": return wood(u, v)
    if name == "weave": return weave(u, v)
    raise SystemExit("unknown texture " + name)

def clamp01(a): return np.minimum(np.maximum(a, 0), 1)

# ------------------------------------------------------------------ the laws

def envelope(w):
    return min(max(16 + 8 * (w - 640) / 640, 12), 24)

class Bounce:
    def __init__(self, speed, w, h, x0, y0, angle, e=(1, 1, 1, 1), frames=480):
        self.speed = speed; self.w = w; self.h = h; self.x0 = x0; self.y0 = y0; self.angle = angle
        self.eLeft, self.eRight, self.eTop, self.eBottom = e; self.frames = frames
    def s(self, t):
        k = self.speed[0]
        if k == "constant": return self.speed[1] * t
        if k == "oscillating":
            v0, m, omega = self.speed[1:]
            return v0 * (t + (m / omega) * (1 - math.cos(omega * t)))
        if k == "hardJerk":
            v1, v2, every = self.speed[1:]
            per = 2 * every
            full = math.floor(t / per); rem = t - full * per
            return full * every * (v1 + v2) + (v1 * rem if rem < every else v1 * every + v2 * (rem - every))
        return 0.0
    @property
    def vMin(self):
        k = self.speed[0]
        if k == "constant": return self.speed[1]
        if k == "oscillating": return self.speed[1] * (1 - self.speed[2])
        if k == "hardJerk": return min(self.speed[1], self.speed[2])
        return 1.0

def trajectory(b, W, H):
    """The engine's segments: exact wall hits, the path-length law inverted by 80 bisections."""
    segs = []
    xl, xr, yt, yb = b.w / 2, W - b.w / 2, b.h / 2, H - b.h / 2
    tEnd = float(b.frames)
    sgn = lambda v: -1.0 if v < 0 else 1.0
    x = min(max(b.x0, xl), xr); y = min(max(b.y0, yt), yb)
    if b.speed[0] == "gravity":
        vx, vy, g = b.speed[1], b.speed[2], b.speed[3]
        t0 = 0.0; guard = 0
        while t0 < tEnd and guard < 100000:
            guard += 1
            tau = math.inf; wall = 0
            if vx > 0:
                c = (xr - x) / vx
                if c < tau: tau = c; wall = 2
            if vx < 0:
                c = (xl - x) / vx
                if c < tau: tau = c; wall = 1
            for wallY, code in ((yt, 3), (yb, 4)):
                A, B, C = g / 2, vy, y - wallY
                roots = []
                if abs(A) < 1e-12:
                    if abs(B) > 1e-12: roots = [-C / B]
                else:
                    disc = B * B - 4 * A * C
                    if disc >= 0:
                        q = math.sqrt(disc); roots = [(-B - q) / (2 * A), (-B + q) / (2 * A)]
                for c in roots:
                    if c > 1e-9 and c < tau: tau = c; wall = code
            segs.append((t0, x, y, vx, vy, 0.0))
            if not math.isfinite(tau) or t0 + tau > tEnd: break
            x += vx * tau; y += vy * tau + g * tau * tau / 2; vy += g * tau
            v2 = vx * vx + vy * vy
            if wall in (1, 2):
                e = b.eLeft if wall == 1 else b.eRight
                x = xl if wall == 1 else xr
                vx = -e * vx
                vy = sgn(vy) * math.sqrt(max(v2 - vx * vx, 0))
            elif wall in (3, 4):
                e = b.eTop if wall == 3 else b.eBottom
                y = yt if wall == 3 else yb
                vy = -e * vy
                if wall == 4 and abs(vy) < 1.5: vy = -1.5
                vx = sgn(vx) * math.sqrt(max(v2 - vy * vy, 0))
            t0 += tau
        return segs
    dx, dy, s0, t0 = math.cos(b.angle), math.sin(b.angle), 0.0, 0.0
    guard = 0
    while t0 < tEnd and guard < 100000:
        guard += 1
        dist = math.inf; wall = 0
        if dx > 0:
            c = (xr - x) / dx
            if c < dist: dist = c; wall = 2
        if dx < 0:
            c = (xl - x) / dx
            if c < dist: dist = c; wall = 1
        if dy > 0:
            c = (yb - y) / dy
            if c < dist: dist = c; wall = 4
        if dy < 0:
            c = (yt - y) / dy
            if c < dist: dist = c; wall = 3
        segs.append((t0, x, y, dx, dy, s0))
        if not math.isfinite(dist): break
        sHit = s0 + max(dist, 0)
        lo, hi = t0, t0 + max(dist, 0) / b.vMin + 1e-9
        for _ in range(80):
            mid = (lo + hi) / 2
            if b.s(mid) < sHit: lo = mid
            else: hi = mid
        tHit = (lo + hi) / 2
        if tHit > tEnd: break
        x += dx * dist; y += dy * dist
        if wall in (1, 2):
            e = b.eLeft if wall == 1 else b.eRight
            x = xl if wall == 1 else xr
            dx = -e * dx
            dy = sgn(dy) * math.sqrt(max(1 - dx * dx, 0))
        elif wall in (3, 4):
            e = b.eTop if wall == 3 else b.eBottom
            y = yt if wall == 3 else yb
            dy = -e * dy
            dx = sgn(dx) * math.sqrt(max(1 - dy * dy, 0))
        t0 = tHit; s0 = sHit
    return segs

def bounce_centre(b, segs, t):
    if not segs: return b.x0, b.y0
    lo, hi = 0, len(segs) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if segs[mid][0] <= t: lo = mid
        else: hi = mid - 1
    t0, x, y, dx, dy, s0 = segs[lo]
    if b.speed[0] == "gravity":
        tau = t - t0; g = b.speed[3]
        return x + dx * tau, y + dy * tau + g * tau * tau / 2
    ds = b.s(t) - s0
    return x + dx * ds, y + dy * ds

class Scene:
    """One master scene: (kind, params), the working size, the ground, the texture, the settle."""
    def __init__(self, kind, p, W, H, bg="textured", texture="sines", settle=0.0):
        self.kind = kind; self.p = p; self.W = W; self.H = H; self.bg = bg; self.texture = texture; self.settle = settle
        self.segs = trajectory(p, float(W), float(H)) if kind == "bounce" else []
        ys, xs = np.mgrid[0:H, 0:W]
        self.x = xs.astype(np.float64) + 0.5; self.y = ys.astype(np.float64) + 0.5

    def chord(self, tRaw0, tRaw1):
        """The one-interval chord of the material point under each pixel, and the mover's mask at the start."""
        t0 = max(tRaw0 - self.settle, 0.0); t1 = max(tRaw1 - self.settle, 0.0)
        x, y, W, H = self.x, self.y, float(self.W), float(self.H)
        k = self.kind
        zero = np.zeros(x.shape + (2,))
        def rot(dth, px, py):
            c, s = math.cos(dth), math.sin(dth)
            return px * c - py * s, px * s + py * c
        if k == "bounce":
            b = self.p
            cx0, cy0 = bounce_centre(b, self.segs, t0); cx1, cy1 = bounce_centre(b, self.segs, t1)
            x0, y0 = cx0 - b.w / 2, cy0 - b.h / 2
            covx = clamp01(np.minimum(x0 + b.w, x + 0.5) - np.maximum(x0, x - 0.5))
            covy = clamp01(np.minimum(y0 + b.h, y + 0.5) - np.maximum(y0, y - 0.5))
            mask = (covx * covy) > 0.5
            ch = zero.copy(); ch[..., 0] = cx1 - cx0; ch[..., 1] = cy1 - cy0
            return np.where(mask[..., None], ch, 0.0), mask
        if k == "breathe":
            rMin, rMax, period, spin = self.p
            rf = lambda t: rMin + (rMax - rMin) * (1 - math.cos(2 * math.pi * t / period)) / 2
            r0, r1 = rf(t0), rf(t1)
            px, py = x - W / 2, y - H / 2
            d = np.sqrt(px * px + py * py)
            mask = (r0 - d + 0.5) > 0.5
            qx, qy = rot(spin * (t1 - t0), px, py)
            s = r1 / max(r0, 1e-6)
            ch = np.stack([qx * s - px, qy * s - py], -1)
            return np.where(mask[..., None], ch, 0.0), mask
        if k == "spin":
            r, law = self.p
            def th(t):
                if law[0] == "constant": return law[1] * t
                if law[0] == "accelerating": return law[1] * t * t / 2
                return law[1] * math.sin(2 * math.pi * t / law[2])
            px, py = x - W / 2, y - H / 2
            d = np.sqrt(px * px + py * py)
            mask = (r - d + 0.5) > 0.5
            qx, qy = rot(th(t1) - th(t0), px, py)
            ch = np.stack([qx - px, qy - py], -1)
            return np.where(mask[..., None], ch, 0.0), mask
        if k == "roll":
            rr, vv, spokes = self.p
            p = 2 * (W - 2 * rr) / vv; half = p / 2
            def state(t):
                tp = math.fmod(t, p); sl = vv * tp if tp < half else vv * (p - tp)
                return rr + sl, sl / rr
            cx0, th0 = state(t0); cx1, th1 = state(t1)
            cy = H - rr - 8
            px, py = x - cx0, y - cy
            d = np.sqrt(px * px + py * py)
            mask = (rr - d + 0.5) > 0.5
            qx, qy = rot(th1 - th0, px, py)
            ch = np.stack([cx1 + qx - x, cy + qy - y], -1)
            return np.where(mask[..., None], ch, 0.0), mask
        raise SystemExit("unknown kind " + k)

    def value(self, tRaw):
        t = max(tRaw - self.settle, 0.0)
        x, y, W, H = self.x, self.y, float(self.W), float(self.H)
        bg = np.zeros_like(x) if self.bg == "flat" else clamp01(tex(x, y) * 0.35 + 0.1)
        k = self.kind
        if k == "bounce":
            b = self.p
            cx, cy = bounce_centre(b, self.segs, t)
            x0, y0 = cx - b.w / 2, cy - b.h / 2
            covx = clamp01(np.minimum(x0 + b.w, x + 0.5) - np.maximum(x0, x - 0.5))
            covy = clamp01(np.minimum(y0 + b.h, y + 0.5) - np.maximum(y0, y - 0.5))
            cov = covx * covy
            inside = clamp01(tex_value(self.texture, x - x0, y - y0) * 0.9 + 0.05)
            return np.where(cov > 0, bg + (inside - bg) * cov, bg)
        if k == "breathe":
            rMin, rMax, period, spin = self.p
            r = rMin + (rMax - rMin) * (1 - math.cos(2 * math.pi * t / period)) / 2
            cx, cy = W / 2, H / 2
            px, py = x - cx, y - cy
            d = np.sqrt(px * px + py * py)
            cov = clamp01(r - d + 0.5)
            th = spin * t; c, s = math.cos(th), math.sin(th)
            kk = rMax / max(r, 1e-6)
            u = (px * c + py * s) * kk + rMax; v = (-px * s + py * c) * kk + rMax
            inside = clamp01(tex_value(self.texture, u, v) * 0.9 + 0.05)
            return np.where(cov > 0, bg + (inside - bg) * cov, bg)
        if k == "spin":
            r, law = self.p
            cx, cy = W / 2, H / 2
            px, py = x - cx, y - cy
            d = np.sqrt(px * px + py * py)
            cov = clamp01(r - d + 0.5)
            if law[0] == "constant": th = law[1] * t
            elif law[0] == "accelerating": th = law[1] * t * t / 2
            else: th = law[1] * math.sin(2 * math.pi * t / law[2])
            c, s = math.cos(th), math.sin(th)
            u = px * c + py * s + r; v = -px * s + py * c + r
            inside = clamp01(tex_value(self.texture, u, v) * 0.9 + 0.05)
            return np.where(cov > 0, bg + (inside - bg) * cov, bg)
        if k == "roll":
            rr, vv, spokes = self.p
            p = 2 * (W - 2 * rr) / vv; half = p / 2
            tp = math.fmod(t, p)
            sl = vv * tp if tp < half else vv * (p - tp)
            cx, th = rr + sl, sl / rr
            cy = H - rr - 8
            px, py = x - cx, y - cy
            d = np.sqrt(px * px + py * py)
            cov = clamp01(rr - d + 0.5)
            c, s = math.cos(th), math.sin(th)
            u = px * c + py * s; v = -px * s + py * c
            pitch = 2 * math.pi / spokes
            ang = np.fmod(np.arctan2(v, u), pitch)
            ang = np.where(ang < 0, ang + pitch, ang)
            toSpoke = d * np.sin(np.minimum(ang, pitch - ang))
            hub = 0.10 * rr
            ink = np.maximum(np.maximum(clamp01(d - (rr - 9) + 0.5), clamp01(hub - d + 0.5)), clamp01(2.5 - toSpoke + 0.5))
            texv = clamp01(tex_value(self.texture, u + rr, v + rr) * 0.9 + 0.05)
            val = texv + (0.04 - texv) * ink
            return np.where(cov > 0, bg + (val - bg) * cov, bg)
        raise SystemExit("unknown kind " + k)

def masters(w, h):
    """The showing's list, continuous in the working size: (name, kind, params, seamless, law frames)."""
    W, H = float(w), float(h)
    vmax = 0.8 * envelope(w)
    bw, bh = round(0.25 * W), round(0.28 * H)
    x0, y0 = round(0.37 * W), round(0.41 * H)
    frames = 480
    def bounce(speed, e=(1, 1, 1, 1)):
        return Bounce(speed, bw, bh, x0, y0, 0.6, e, frames)
    drop = max(H - bh / 2 - y0, 1)
    g = vmax * vmax / (2 * drop)
    rMin, rMax = round(0.06 * H), round(0.48 * H)
    bPeriod = max(96, round(math.pi * (rMax - rMin) / (0.6 * vmax)))
    sr = round(0.47 * H)
    omega = 0.9 * vmax / sr
    rr = round(0.28 * H)
    spin_frames = lambda om: max(24, round(2 * math.pi / om)) if om > 1e-9 else 240
    roll_frames = lambda v: max(24, round(2 * (1280 - 2 * rr) / v))
    return [
        ("bounce-constant",    "bounce", bounce(("constant", vmax)), False, frames),
        ("bounce-oscillating", "bounce", bounce(("oscillating", 0.6 * vmax, 0.6, 2 * math.pi / 72)), False, frames),
        ("bounce-hardjerk",    "bounce", bounce(("hardJerk", 0.4 * vmax, vmax, 24.0)), False, frames),
        ("bounce-gravity",     "bounce", bounce(("gravity", 0.5 * vmax, 0.0, g)), False, frames),
        ("bounce-masses",      "bounce", bounce(("constant", vmax), e=(1, 0.6, 0.8, 0.4)), False, frames),
        ("breathe",            "breathe", (rMin, rMax, bPeriod, 0.0), True, round(2 * bPeriod)),
        ("breathe-spin",       "breathe", (rMin, rMax, bPeriod, 0.3 * vmax / rMax), True, round(2 * bPeriod)),
        ("spin-constant",      "spin", (sr, ("constant", omega)), True, spin_frames(omega)),
        ("spin-accelerating",  "spin", (sr, ("accelerating", omega / 240)), False, 240),
        ("spin-pendulum",      "spin", (sr, ("pendulum", 0.7, 120.0)), True, 120),
        ("roll-12",            "roll", (rr, vmax / 2, 12), True, roll_frames(vmax / 2)),
        ("roll-12-fast",       "roll", (rr, vmax, 12), True, roll_frames(vmax)),
        ("roll-wagon",         "roll", (rr, vmax, max(6, round(2 * math.pi * rr / vmax))), True, roll_frames(vmax)),
        ("static",             "spin", (sr, ("constant", 0.0)), True, 240),
    ]

def master(name, w, h):
    for m in masters(w, h):
        if m[0] == name: return m
    raise SystemExit("no master scene named " + name + " (see --list)")

CLOCK = 24.0

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("scene", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--size", default="1280x720")
    ap.add_argument("--src-fps", type=float, default=24.0)
    ap.add_argument("--out-fps", type=float, default=60.0)
    ap.add_argument("--frames", type=int, default=None, help="source frames (default: the law's own length at the source rate)")
    ap.add_argument("--settle", type=float, default=0.0, help="law frames held still at the start (the demo uses 24)")
    ap.add_argument("--bg", default="textured", choices=["textured", "flat"])
    ap.add_argument("--texture", default="sines", choices=TEXTURES)
    ap.add_argument("--export-source", default=None)
    ap.add_argument("--export-truth", default=None)
    ap.add_argument("--export-field", default=None, help="directory for truth_NNN.npy / mask_NNN.npy per source interval")
    a = ap.parse_args()
    W, H = (int(s) for s in a.size.lower().split("x"))
    if a.list:
        for name, kind, p, seamless, n in masters(W, H):
            print("%-20s %-8s %4d law frames%s" % (name, kind, n, "  (seamless)" if seamless else ""))
        return
    if not a.scene: ap.error("a scene name, or --list")
    name, kind, p, seamless, lawFrames = master(a.scene, W, H)
    sc = Scene(kind, p, W, H, a.bg, a.texture, a.settle)
    fps = a.src_fps
    frames = a.frames if a.frames is not None else (lawFrames if fps == CLOCK else int(round(lawFrames * fps / CLOCK)))
    def write(fh, t):
        v = np.rint(sc.value(t) * 65535).clip(0, 65535).astype("<u2")
        fh.write(np.repeat(v[:, :, None], 3, axis=2).tobytes())
    if a.export_source:
        with open(a.export_source, "wb") as fh:
            for k in range(frames):
                write(fh, float(k) if fps == CLOCK else k * CLOCK / fps)
        print("scene %s: %d source frames at %g fps -> %s" % (name, frames, fps, a.export_source))
    if a.export_truth:
        outCount = int(round(frames * a.out_fps / fps))
        with open(a.export_truth, "wb") as fh:
            for j in range(outCount):
                write(fh, j * CLOCK / a.out_fps)
        print("scene %s: %d truth frames at %g fps -> %s" % (name, outCount, a.out_fps, a.export_truth))
    if a.export_field:
        import os
        os.makedirs(a.export_field, exist_ok=True)
        dt = 1.0 if fps == CLOCK else CLOCK / fps
        for k in range(frames):
            t0 = (float(k) if fps == CLOCK else k * CLOCK / fps)
            ch, mk = sc.chord(t0, t0 + dt)
            np.save(os.path.join(a.export_field, "truth_%03d.npy" % k), ch.astype(np.float32))
            np.save(os.path.join(a.export_field, "mask_%03d.npy" % k), mk)
        print("scene %s: %d field-truth intervals at %g fps -> %s" % (name, frames, fps, a.export_field))
    if not a.export_source and not a.export_truth and not a.export_field:
        print("scene %s: %s, %d law frames, %d source frames at %g fps (nothing exported: give --export-source / --export-truth)"
              % (name, kind, lawFrames, frames, fps))

if __name__ == "__main__":
    main()
