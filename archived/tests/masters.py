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
spokes advance exactly one pitch per source frame -- and, since 2026-09-12, four COMPLEX scenes of many
rigid bodies over a still ground: snow (flakes in depth layers, each its own fall, sway, turn and size), fish
(horizontal only, left or right by lane, each its own length, speed, bob and tail beat), planets (a turning
sun, five planets on Kepler orbits, two eccentric, lit from the sun, a moon, rings) and a roundabout from
above (a ring road with four arms; vehicles come up an arm, swing into the ring, circulate clockwise and
leave by another arm -- straights and arcs at one speed, so the acceleration steps at each change of
curvature). Each is one analytic law of (x, y, t), so the same law renders the source at one rate and the
exact truth at another, as the ladder's lavfi expressions do; every complex scene closes in 360 law frames.

The laws are the demo engine's, ported line for line (Sources/QuadEngine/QuadEngine.swift in the NFrameDemo
tree, which is private and not published, SyntheticScene): every constant, the exact box-filter coverage
of the rectangle, the one-pixel ramp on a
disc's rim, the wheel's ink, the deterministic textures. The identity check (probes/masters/identity.sh)
holds this file to the engine's own exports to the last 16-bit level, so the engine is not the truth --
this file is, and anyone with python3, numpy and ffmpeg regenerates it.

Time: every law is written in frames at 24 fps (px per frame, the ladder's unit), and that is its clock
at any source rate: source frame k is law time k * 24 / fps, so a scene lasts the same at 60 as at 24 with
finer steps; the truth at the output rate samples law time j * 24 / outFps. `--settle N` holds the scene
still for its first N law frames (the demo uses 24: the reading's settling second).

Output: rgb48le rawvideo (R = G = B, 16-bit, the value rounded half up from the law, as the engine rounds) -- what the demo's CLI exports,
so probes/masters/check.sh scores both hosts against the same bytes. Textured ground = the demo's dim
five-sine field under the mover (every edge an occlusion); flat = black.

The FIELD truth (--export-field DIR, the plan's S4): per source interval k, truth_NNN.npy [H, W, 2] float32
is the one-interval chord of the material point under each pixel -- where it is at source frame k + 1 minus
where it is at k, in px (x right, y down), the quantity a two-frame flow measures -- and mask_NNN.npy the
mover's coverage at k; the ground is still, its chord zero. manifolds.py's format, so fieldcheck.py scores a
machine-read frame against it. Closed forms: a translating rectangle's chord is its centre's; a breathing
disc's is the radial scaling r(k+1)/r(k) (with the spin's turn); a spinning disc's the turn; the wheel's
its axle's travel plus the turn about it. A complex scene's chord is per body, part by part: a rigid
translation with the body's turn (the fish's tail turns about its root, rings do not turn), the nearer body
overwriting the farther, zero on the ground.
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

# ------------------------------------------------------------------ the complex scenes (2026-09-12, P27)
# The engine's bodies(at:), shade and roundaboutGround, line for line: scalar laws in math (libm, as Swift's),
# the drawing in numpy over each body's box, composited far to near exactly as the engine composites.

LOOP = 360.0
COMPLEX = ("snow", "fish", "planets", "roundabout")

def rnd(v):
    """The engine's .rounded() for a positive value (half away from zero; Python's round() is to even)."""
    return math.floor(v + 0.5)

def hs(i, j):
    with np.errstate(over="ignore"):          # the hash wraps on purpose; a numpy scalar warns where an array would not
        return float(hash2(i, j))

class RoundaboutGeometry:
    def __init__(self, W, H):
        self.Cx, self.Cy = W / 2, H / 2
        self.Rc, self.Ri, self.Ro, self.hw, self.d, self.rt, mg = 0.21 * H, 0.11 * H, 0.31 * H, 0.10 * H, 0.05 * H, 0.09 * H, 0.08 * H
        self.s = math.sqrt((self.Rc - self.d) * (self.Rc + self.d + 2 * self.rt))
        self.phi = math.atan2(self.s, self.d + self.rt)
        self.L1 = (H + mg) - (self.Cy + self.s); self.L2 = self.rt * self.phi
        self.L3 = self.Rc * (math.pi / 2 + 2 * self.phi); self.L4 = self.rt * self.phi
        self.L5 = (W + mg) - (self.Cx + self.s)
        self.L = self.L1 + self.L2 + self.L3 + self.L4 + self.L5

def track_pose(g, sigma):
    """(x, y, heading) at path length sigma along the first track (bottom arm in, right arm out)."""
    u = sigma
    if u < g.L1: return (g.Cx - g.d, g.Cy + g.s + (g.L1 - u), -math.pi / 2)
    u -= g.L1
    if u < g.L2:
        ang = -u / g.rt
        return (g.Cx - g.d - g.rt + g.rt * math.cos(ang), g.Cy + g.s + g.rt * math.sin(ang), ang - math.pi / 2)
    u -= g.L2
    if u < g.L3:
        ang = math.pi - g.phi + u / g.Rc
        return (g.Cx + g.Rc * math.cos(ang), g.Cy + g.Rc * math.sin(ang), ang + math.pi / 2)
    u -= g.L3
    if u < g.L4:
        ang = math.pi / 2 + g.phi - u / g.rt
        return (g.Cx + g.s + g.rt * math.cos(ang), g.Cy - g.d - g.rt + g.rt * math.sin(ang), ang - math.pi / 2)
    u -= g.L4
    return (g.Cx + g.s + u, g.Cy - g.d, 0.0)

def bodies(kind, p, W, H, t):
    """The bodies of a complex scene at law time t, far to near: dicts of kind, pose, box and parameters."""
    L = LOOP; vmax = 0.8 * envelope(W)
    out = []
    if kind == "snow":
        kmax = max(1, math.floor(vmax * L / (H + 23)))
        for z in range(4):
            for i in range(z, p, 4):
                h = [None] + [hs(i, j) for j in range(1, 10)]
                r = 3 + 2.2 * z + 1.5 * h[1]
                f = 0.12 + 0.88 * (z + h[2]) / 4
                k = float(max(1, rnd(f * kmax)))
                py_ = H + 2 * r; px_ = W + 2 * r
                vy = k * py_ / L; wind = px_ / L
                A = 5 + 12 * h[5]; m = float(1 + int(h[6] * 4)); phi = 2 * math.pi * h[7]
                q = float(int(h[8] * 7) - 3)
                cy = math.fmod(h[3] * py_ + vy * t, py_) - r
                cx = math.fmod(h[4] * px_ + wind * t, px_) - r + A * math.sin(2 * math.pi * m * t / L + phi)
                out.append(dict(kind="flake", r=r, bright=0.72 + 0.25 * h[9], cx=cx, cy=cy, th=2 * math.pi * q * t / L,
                                x0=cx - r - 1, y0=cy - r - 1, x1=cx + r + 1, y1=cy + r + 1, wx=px_, wy=py_))
    elif kind == "fish":
        n = p
        items = sorted(((0.07 + 0.08 * hs(i, 1)) * H, i) for i in range(n))
        for ell, i in items:
            h = [None] + [hs(i, j) for j in range(1, 9)]
            a = ell / 2; b = 0.28 * ell; tl = 0.38 * ell; th = 0.32 * ell
            dir_ = 1.0 if i % 2 == 0 else -1.0
            y0 = H * (0.12 + 0.76 * (i + 0.5) / n) + (h[2] - 0.5) * 0.05 * H
            P = W + 2 * (a + tl)
            kmax = max(1, math.floor(vmax * L / P))
            k = float(1 + int(h[3] * kmax))
            v = k * P / L
            s = math.fmod(h[4] * P + v * t, P)
            cx = s - (a + tl) if dir_ > 0 else W + (a + tl) - s
            m = float(1 + int(h[5] * 3))
            cy = y0 + 0.04 * H * math.sin(2 * math.pi * m * t / L + 2 * math.pi * h[6])
            w = 8 + 6 * k
            alpha = 0.35 * math.sin(2 * math.pi * w * t / L + 2 * math.pi * h[7])
            ext = 0.46 * ell + 1
            out.append(dict(kind="fish", dir=dir_, a=a, b=b, tl=tl, th_=th, alpha=alpha, off=300 * i, bright=0.8 + 0.4 * h[8],
                            cx=cx, cy=cy, th=0.0, x0=cx - (a + tl + 1), y0=cy - ext, x1=cx + (a + tl + 1), y1=cy + ext, wx=P, wy=0.0))
    elif kind == "planets":
        Cx, Cy, Rs = W / 2, H / 2, 0.075 * H
        out.append(dict(kind="sun", r=Rs, cx=Cx, cy=Cy, th=2 * math.pi * t / L, x0=Cx - Rs - 1, y0=Cy - Rs - 1, x1=Cx + Rs + 1, y1=Cy + Rs + 1, wx=0.0, wy=0.0))
        # (orbits per loop, semi-major axis / 0.455 H, radius / H, eccentricity, perihelion angle, spins per loop, mean anomaly at 0)
        P = [(8, 0.25, 0.016, 0, 0, 6, 0.3), (5, 0.343, 0.024, 0.30, 0.6, -4, 2.0), (3, 0.48, 0.032, 0.45, 2.4, 3, 4.1),
             (2, 0.63, 0.020, 0, 0, 2, 1.2), (1, 1.0, 0.036, 0, 0, 1, 5.5)]
        centres = []
        for k, af, rf, e, w, spin, M0 in P:
            a = af * 0.455 * H
            M = M0 + 2 * math.pi * k * t / L
            E = M
            for _ in range(8):
                E = E - (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
            ox = a * (math.cos(E) - e); oy = a * math.sqrt(1 - e * e) * math.sin(E)
            centres.append((Cx + ox * math.cos(w) - oy * math.sin(w), Cy + ox * math.sin(w) + oy * math.cos(w)))
        for pi_ in range(4, -1, -1):
            cx, cy = centres[pi_]; r = P[pi_][2] * H
            dx = cx - Cx; dy = cy - Cy; dd = math.sqrt(dx * dx + dy * dy)
            ext = 2.3 * r + 1 if pi_ == 4 else r + 1
            out.append(dict(kind="planet", r=r, lx=dx / dd, ly=dy / dd, off=1000 * pi_, ring=(pi_ == 4), cx=cx, cy=cy,
                            th=2 * math.pi * P[pi_][5] * t / L, x0=cx - ext, y0=cy - ext, x1=cx + ext, y1=cy + ext, wx=0.0, wy=0.0))
            if pi_ == 3:
                Rm, rm, mu = 0.045 * H, 0.007 * H, 2 * math.pi * 12 * t / L + 0.7
                mx = cx + Rm * math.cos(mu); my = cy + Rm * math.sin(mu)
                mdx = mx - Cx; mdy = my - Cy; mdd = math.sqrt(mdx * mdx + mdy * mdy)
                out.append(dict(kind="planet", r=rm, lx=mdx / mdd, ly=mdy / mdd, off=5000, ring=False, cx=mx, cy=my, th=0.0,
                                x0=mx - rm - 1, y0=my - rm - 1, x1=mx + rm + 1, y1=my + rm + 1, wx=0.0, wy=0.0))
    elif kind == "roundabout":
        g = p
        laps = float(max(1, math.floor(0.65 * vmax * L / g.L)))
        v = laps * g.L / L
        vehicles = [(0, 0, 0.060, 0.032, 0.85), (0, 1.0 / 3, 0.11, 0.036, 0.5), (0, 2.0 / 3, 0.060, 0.032, 0.7),
                    (1, 1.0 / 6, 0.060, 0.032, 0.35), (1, 0.5, 0.072, 0.034, 0.9)]
        for j, (track, phase, ln, wd, bright) in enumerate(vehicles):
            sigma = math.fmod(phase * g.L + v * t, g.L)
            px_, py_, hd = track_pose(g, sigma)
            if track == 1:
                px_ = 2 * g.Cx - px_; py_ = 2 * g.Cy - py_; hd += math.pi
            hl = ln * H / 2; hw = wd * H / 2
            ext = math.sqrt(hl * hl + hw * hw) + 1
            out.append(dict(kind="vehicle", hl=hl, hw=hw, bright=bright, off=700 * j, cx=px_, cy=py_, th=hd,
                            x0=px_ - ext, y0=py_ - ext, x1=px_ + ext, y1=py_ + ext, wx=0.0, wy=0.0))
    return out

def parts(b, X, Y, texture):
    """One body's parts over its box, in the engine's drawing order: (coverage, value, how it moves)."""
    px = X - b["cx"]; py = Y - b["cy"]
    c = math.cos(b["th"]); s = math.sin(b["th"])
    u = px * c + py * s; v = -px * s + py * c
    k = b["kind"]
    if k == "flake":
        r, bright = b["r"], b["bright"]
        d = np.sqrt(px * px + py * py)
        rad = r * (0.74 + 0.26 * np.cos(6 * np.arctan2(v, u)))
        cov = clamp01(rad - d + 0.5)
        dn = np.minimum(d / r, 1)
        return [(cov, bright * (1 - 0.3 * dn * dn), "rigid")]
    if k == "fish":
        dir_, a, bb, tl, th, alpha, off, bright = b["dir"], b["a"], b["b"], b["tl"], b["th_"], b["alpha"], b["off"], b["bright"]
        fu = dir_ * px; fv = py
        ca, sa = math.cos(alpha), math.sin(alpha)
        tu = (fu + a) * ca + fv * sa; tv = -(fu + a) * sa + fv * ca
        e1 = tu + tl; e3 = th * (-tu / tl) - np.abs(tv)
        covT = clamp01(np.minimum(e1, e3) + 0.5)
        texT = clamp01(tex_value(texture, tu + off + 50, tv + off) * 0.9 + 0.05)
        pvT = clamp01(0.85 * bright * (0.3 + 0.7 * texT))
        rho = np.sqrt((fu / a) * (fu / a) + (fv / bb) * (fv / bb))
        covB = clamp01((1 - rho) * bb + 0.5)
        texB = clamp01(tex_value(texture, fu + off, fv + off) * 0.9 + 0.05)
        shade = 0.6 + 0.4 * clamp01((fv / bb + 1) / 2)
        pvB = clamp01((0.3 + 0.7 * texB) * shade * bright)
        ex = fu - 0.6 * a; ey = fv + 0.3 * bb
        covE = clamp01(0.09 * a - np.sqrt(ex * ex + ey * ey) + 0.5)
        return [(covT, pvT, "tail"), (covB, pvB, "rigid"), (covE, 0.08, "rigid")]
    if k == "sun":
        r = b["r"]
        d = np.sqrt(px * px + py * py)
        cov = clamp01(r - d + 0.5)
        texv = clamp01(tex_value(texture, u + r, v + r) * 0.9 + 0.05)
        dn = np.minimum(d / r, 1)
        return [(cov, clamp01((0.6 + 0.4 * texv) * (1 - 0.25 * dn * dn)), "rigid")]
    if k == "planet":
        r, lx, ly, off, ring = b["r"], b["lx"], b["ly"], b["off"], b["ring"]
        d = np.sqrt(px * px + py * py)
        cov = clamp01(r - d + 0.5)
        ry = py / 0.3; q = np.sqrt(px * px + ry * ry)
        covR = clamp01(np.minimum(q - 1.5 * r, 2.3 * r - q) + 0.5) if ring else np.zeros_like(px)
        ringv = 0.45 + 0.25 * np.cos(2 * np.pi * (q - 1.5 * r) / (0.4 * r))
        far = np.where(py <= 0, covR, 0.0); near = np.where(py > 0, covR, 0.0)
        kk = 60 / r
        texv = clamp01(tex_value(texture, u * kk + off, v * kk + off) * 0.9 + 0.05)
        lam = np.maximum(-(px / r * lx + py / r * ly), 0)
        pv = clamp01(texv * (0.35 + 0.65 * lam))
        return [(far, ringv, "ring"), (cov, pv, "rigid"), (near, ringv, "ring")]
    if k == "vehicle":
        hl, hw, bright, off = b["hl"], b["hw"], b["bright"], b["off"]
        rc = 0.3 * hw
        qx = np.abs(u) - (hl - rc); qy = np.abs(v) - (hw - rc)
        mx = np.maximum(qx, 0); my = np.maximum(qy, 0)
        sd = np.sqrt(mx * mx + my * my) + np.minimum(np.maximum(qx, qy), 0) - rc
        cov = clamp01(0.5 - sd)
        texv = clamp01(tex_value(texture, u * 3 + off, v * 3 + off) * 0.9 + 0.05)
        body = clamp01(bright * (0.85 + 0.15 * texv))
        ws = clamp01(np.minimum(u - 0.25 * hl, 0.55 * hl - u) + 0.5)
        body = body + (0.12 - body) * ws
        rw = clamp01(np.minimum(u + 0.65 * hl, -0.45 * hl - u) + 0.5)
        body = body + (0.15 - body) * rw
        outline = clamp01(sd + 2)
        body = body + (0.1 - body) * outline
        return [(cov, body, "rigid")]
    raise SystemExit("unknown body " + k)

def box(b, W, H):
    """The pixel rows and columns whose centres lie in the body's box (the engine tests the same box)."""
    r0 = max(0, math.ceil(b["y0"] - 0.5)); r1 = min(H - 1, math.floor(b["y1"] - 0.5))
    c0 = max(0, math.ceil(b["x0"] - 0.5)); c1 = min(W - 1, math.floor(b["x1"] - 0.5))
    if r0 > r1 or c0 > c1: return None
    return (slice(r0, r1 + 1), slice(c0, c1 + 1))

def roundabout_ground(g, X, Y, H, texture, bg):
    kw = 0.0055 * H; dp = 0.055 * H; lw = 0.002 * H
    dx = X - g.Cx; dy = Y - g.Cy; dist = np.sqrt(dx * dx + dy * dy)
    ax = np.abs(dx); ay = np.abs(dy)
    val = bg.copy()
    annulus = clamp01(np.minimum(dist - g.Ri, g.Ro - dist) + 0.5)
    armV = clamp01(np.minimum(g.hw - ax, dist - g.Ri) + 0.5)
    armH = clamp01(np.minimum(g.hw - ay, dist - g.Ri) + 0.5)
    tarmac = np.maximum(annulus, np.maximum(armV, armH))
    val = np.where(tarmac > 0, val + (0.30 - val) * tarmac, val)
    island = clamp01(g.Ri - dist + 0.5)
    texv = clamp01(tex_value(texture, X, Y) * 0.9 + 0.05)
    iv = 0.22 + 0.15 * texv
    kerb = clamp01(dist - (g.Ri - kw) + 0.5)
    iv = iv + (0.75 - iv) * kerb
    val = np.where(island > 0, val + (iv - val) * island, val)
    onArmV = clamp01(g.hw - ax + 0.5); onArmH = clamp01(g.hw - ay + 0.5)
    line = clamp01(np.minimum(dist - (g.Ro - kw), g.Ro - dist) + 0.5) * (1 - np.maximum(onArmV, onArmH))
    val = np.where(line > 0, val + (0.85 - val) * line, val)
    past = clamp01(dist - g.Ro + 0.5)
    mV = np.fmod(ay, dp); mH = np.fmod(ax, dp)
    dashV = clamp01(lw - ax + 0.5) * past * clamp01(np.minimum(mV, dp / 2 - mV) + 0.5)
    dashH = clamp01(lw - ay + 0.5) * past * clamp01(np.minimum(mH, dp / 2 - mH) + 0.5)
    dash = np.maximum(dashV, dashH)
    val = np.where(dash > 0, val + (0.85 - val) * dash, val)
    return val

class Scene:
    """One master scene: (kind, params), the working size, the ground, the texture, the settle."""
    def __init__(self, kind, p, W, H, bg="textured", texture="sines", settle=0.0):
        self.kind = kind; self.p = p; self.W = W; self.H = H; self.bg = bg; self.texture = texture; self.settle = settle
        self.segs = trajectory(p, float(W), float(H)) if kind == "bounce" else []
        self.geom = RoundaboutGeometry(float(W), float(H)) if kind == "roundabout" else None
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
        if k in COMPLEX:
            # per body, part by part: the nearer overwrites the farther; a wrap (a flake re-entering at the
            # top, a fish at the far edge) is undone, so the chord is the body's own motion
            param = self.geom if k == "roundabout" else self.p
            b0 = bodies(k, param, W, H, t0); b1 = bodies(k, param, W, H, t1)
            ch = zero.copy(); mask = np.zeros(x.shape, dtype=bool)
            for A, B in zip(b0, b1):
                sl = box(A, self.W, self.H)
                if sl is None: continue
                X, Y = x[sl], y[sl]
                dcx = B["cx"] - A["cx"]; dcy = B["cy"] - A["cy"]
                if A["wx"] > 0 and abs(dcx) > A["wx"] / 2: dcx -= math.copysign(A["wx"], dcx)
                if A["wy"] > 0 and abs(dcy) > A["wy"] / 2: dcy -= math.copysign(A["wy"], dcy)
                dth = B["th"] - A["th"]
                for cov, _, how in parts(A, X, Y, self.texture):
                    m = cov > 0.5
                    if not m.any(): continue
                    if how == "rigid":
                        qx, qy = rot(dth, X - A["cx"], Y - A["cy"])
                        chx = (A["cx"] + dcx + qx) - X; chy = (A["cy"] + dcy + qy) - Y
                    elif how == "ring":
                        chx = np.full(X.shape, dcx); chy = np.full(X.shape, dcy)
                    else:   # the tail turns about its root, which moves with the fish; mirrored for a left-swimmer
                        pvx = A["cx"] - A["dir"] * A["a"]; pvy = A["cy"]
                        qx, qy = rot(A["dir"] * (B["alpha"] - A["alpha"]), X - pvx, Y - pvy)
                        chx = (pvx + dcx + qx) - X; chy = (pvy + dcy + qy) - Y
                    sub = ch[sl]; sub[..., 0] = np.where(m, chx, sub[..., 0]); sub[..., 1] = np.where(m, chy, sub[..., 1]); ch[sl] = sub
                    mask[sl] |= m
            return ch, mask
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
            r, law = self.p[0], self.p[1]
            orbR, orbOm = (self.p[2], self.p[3]) if len(self.p) > 2 else (0.0, 0.0)
            def centre(t): return (W / 2, H / 2) if orbR == 0 else (W / 2 + orbR * math.cos(orbOm * t), H / 2 + orbR * math.sin(orbOm * t))
            def th(t):
                if law[0] == "constant": return law[1] * t
                if law[0] == "accelerating": return law[1] * t * t / 2
                return law[1] * math.sin(2 * math.pi * t / law[2])
            cx0, cy0 = centre(t0); cx1, cy1 = centre(t1)
            px, py = x - cx0, y - cy0
            d = np.sqrt(px * px + py * py)
            mask = (r - d + 0.5) > 0.5
            qx, qy = rot(th(t1) - th(t0), px, py)
            ch = np.stack([cx1 + qx - x, cy1 + qy - y], -1)
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
        if k in COMPLEX:
            val = roundabout_ground(self.geom, x, y, H, self.texture, bg) if k == "roundabout" else bg.copy()
            param = self.geom if k == "roundabout" else self.p
            for b in bodies(k, param, W, H, t):
                sl = box(b, self.W, self.H)
                if sl is None: continue
                for cov, pv, _ in parts(b, x[sl], y[sl], self.texture):
                    sub = val[sl]
                    val[sl] = np.where(cov > 0, sub + (pv - sub) * cov, sub)
            return val
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
            r, law = self.p[0], self.p[1]
            orbR, orbOm = (self.p[2], self.p[3]) if len(self.p) > 2 else (0.0, 0.0)
            cx, cy = (W / 2, H / 2) if orbR == 0 else (W / 2 + orbR * math.cos(orbOm * t), H / 2 + orbR * math.sin(orbOm * t))
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
    orbR, orbA = round(0.38 * H), round(0.09 * H)
    orbOmega = 0.6 * vmax / orbR
    MIN_CLIP = 360                                    # fifteen seconds at 24: every clip at least this, in whole periods
    def whole(period):
        p = max(period, 1); return round(p * math.ceil(MIN_CLIP / p))
    spin_frames = lambda om: whole(2 * math.pi / om) if om > 1e-9 else MIN_CLIP
    roll_frames = lambda v: whole(2 * (1280 - 2 * rr) / v)
    return [
        ("bounce-constant",    "bounce", bounce(("constant", vmax)), False, frames),
        ("bounce-oscillating", "bounce", bounce(("oscillating", 0.6 * vmax, 0.6, 2 * math.pi / 72)), False, frames),
        ("bounce-hardjerk",    "bounce", bounce(("hardJerk", 0.4 * vmax, vmax, 24.0)), False, frames),
        ("bounce-gravity",     "bounce", bounce(("gravity", 0.5 * vmax, 0.0, g)), False, frames),
        ("bounce-masses",      "bounce", bounce(("constant", vmax), e=(1, 0.6, 0.8, 0.4)), False, frames),
        ("breathe",            "breathe", (rMin, rMax, bPeriod, 0.0), True, whole(bPeriod)),
        ("breathe-spin",       "breathe", (rMin, rMax, bPeriod, 0.3 * vmax / rMax), True, whole(bPeriod)),
        ("spin-constant",      "spin", (sr, ("constant", omega)), True, spin_frames(omega)),
        ("spin-accelerating",  "spin", (sr, ("accelerating", omega / 360)), False, MIN_CLIP),
        ("spin-pendulum",      "spin", (sr, ("pendulum", 0.7, 120.0)), True, whole(120.0)),
        ("spin-orbit",         "spin", (orbR, ("constant", orbOmega), orbA, 2 * orbOmega), True, spin_frames(orbOmega)),
        ("roll-12",            "roll", (rr, vmax / 2, 12), True, roll_frames(vmax / 2)),
        ("roll-12-fast",       "roll", (rr, vmax, 12), True, roll_frames(vmax)),
        ("roll-wagon",         "roll", (rr, vmax, max(6, round(2 * math.pi * rr / vmax))), True, roll_frames(vmax)),
        # the complex scenes (P27): many bodies, each its own law, over a still ground; the count is the parameter
        ("snow",               "snow", max(24, rnd(96 * W * H / (1280 * 720))), True, int(LOOP)),
        ("fish",               "fish", max(4, rnd(7 * H / 720)), True, int(LOOP)),
        ("planets",            "planets", None, True, int(LOOP)),
        ("roundabout",         "roundabout", None, True, int(LOOP)),
        ("static",             "spin", (sr, ("constant", 0.0)), True, MIN_CLIP),
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
        v = np.floor(sc.value(t) * 65535 + 0.5).clip(0, 65535).astype("<u2")   # half up, as the engine rounds (0.30 * 65535 is a tie)
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
