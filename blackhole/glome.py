#!/usr/bin/env python3
"""Fly through the 3-sphere: an honest render from INSIDE (2026-09-10).

The 3-sphere is the set of unit vectors in R^4. Its 'surface' is three-dimensional, so a creature living in
it lives in a 3-D world whose straight lines are great circles. That is what makes it renderable at all:
the camera is an ordinary 3-D camera, and only the rays are different.

A ray from p in unit tangent direction d (both in R^4, d orthogonal to p) is
    g(t) = p cos t + d sin t,   t in [0, 2 pi),
and after 2 pi it is back where it started. A ball of angular radius rho about centre c is the set
{q : <q,c> >= cos rho}. Along the ray,
    <g(t), c> = A cos t + B sin t = R cos(t - phi),   A = <p,c>, B = <d,c>, R = hypot(A,B), phi = atan2(B,A)
so the ray ENTERS the ball at t = phi - arccos(cos rho / R) (mod 2 pi) when R >= cos rho, and never
otherwise. Closed form; no marching. Every ray that misses every ball comes back to the observer at
t = 2 pi: there is no sky and no infinity.

Three things are true from inside, and the film shows all three:
  1. no horizon -- every direction ends on something, at most 2 pi away;
  2. antipodal focusing -- all geodesics from a point reconverge at its antipode, so an object near the
     antipode looks enormous, and under a headlamp is lit with irradiance 1/sin^2(d), which peaks there;
  3. the backdrop of every view is the back of your own head, lit by your own lamp after a trip round.
The objects are the 120 vertices of the 600-cell (the 4-D icosahedron), each a small ball. The camera
flies once round a great circle chosen to keep clear of them. Direct lighting only, one bounce, a headlamp
at the eye; exposure is a fixed Reinhard curve (noted in the caption, as for the Hawking renders).

  glome.py still <out.png> [frame_index]        one frame
  glome.py film  <out.mp4> [frames]             the flight, 24 fps, one full circuit
  glome.py path                                 report the chosen circle and its clearance
"""
import itertools
import os
import pathlib
import subprocess
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # hawkcolor.py is beside this file
from hawkcolor import draw_text, text_width  # the 5x7 caption font from the Hawking films

FF = os.environ.get("FFMPEG", "ffmpeg")
# run from a shell with the project's ffmpeg build and mingw64/bin on PATH, as every tool in tests/ does
W, H = 1280, 720
FOV_DEG = 100.0
RHO = np.radians(8.0)          # each vertex ball, angular radius
RHO_SELF = np.radians(3.0)     # the observer's own head
FPS = 24
TWO_PI = 2 * np.pi


def cell600():
    """The 120 unit vectors of the 600-cell."""
    phi = (1 + 5 ** 0.5) / 2
    V = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = s
            V.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        V.append(list(signs))
    base = [phi / 2, 0.5, 1 / (2 * phi)]
    for perm in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
        if inv % 2:
            continue
        for signs in itertools.product((1.0, -1.0), repeat=3):
            vals = [signs[0] * base[0], signs[1] * base[1], signs[2] * base[2], 0.0]
            v = [0.0] * 4
            for k in range(4):
                v[perm[k]] = vals[k]
            V.append(v)
    V = np.array(V)
    assert V.shape == (120, 4), V.shape
    assert np.allclose(np.linalg.norm(V, axis=1), 1.0)
    assert len({tuple(np.round(v, 9)) for v in V}) == 120, "duplicate vertices"
    d = np.degrees(np.arccos(np.clip(V @ V.T, -1, 1)))
    np.fill_diagonal(d, 999)
    assert abs(d.min() - 36.0) < 1e-6, d.min()   # the 600-cell's edge is 36 degrees
    return V


def flight_circle(C, seed=7, trials=40000):
    """A great circle (an orthonormal pair a, b) whose closest approach to any vertex is as large as
    possible, so the camera never enters a ball. Returns a, b and the clearance in radians."""
    rng = np.random.default_rng(seed)
    best = (-1.0, None, None)
    for _ in range(trials):
        a = rng.normal(size=4)
        a /= np.linalg.norm(a)
        b = rng.normal(size=4)
        b -= a * (a @ b)
        b /= np.linalg.norm(b)
        clearance = np.arccos(np.clip(np.hypot(C @ a, C @ b).max(), -1, 1))
        if clearance > best[0]:
            best = (clearance, a, b)
    return best[1], best[2], best[0]


def complete_frame(a, b):
    """Two unit vectors orthogonal to both a and b: the camera's right and up, parallel along the circle."""
    basis = [a, b]
    for e in np.eye(4):
        v = e.copy()
        for q in basis:
            v -= q * (q @ v)
        if np.linalg.norm(v) > 1e-6:
            basis.append(v / np.linalg.norm(v))
        if len(basis) == 4:
            break
    return basis[2], basis[3]


def hue_rgb(h):
    """h in [0,1) -> rgb in [0,1], a plain six-segment wheel."""
    h = (h % 1.0) * 6
    i = np.floor(h).astype(int)
    f = h - i
    out = np.zeros(h.shape + (3,))
    seg = [(1, "t", 0), ("q", 1, 0), (0, 1, "t"), (0, "q", 1), ("t", 0, 1), (1, 0, "q")]
    for k, comps in enumerate(seg):
        m = i == k
        for ch, cval in enumerate(comps):
            if cval == "t":
                out[m, ch] = f[m]
            elif cval == "q":
                out[m, ch] = 1 - f[m]
            else:
                out[m, ch] = cval
    return out


class Scene:
    def __init__(self):
        C = cell600()
        self.a, self.b, self.clearance = flight_circle(C)
        self.r, self.u = complete_frame(self.a, self.b)
        assert self.clearance > RHO + RHO_SELF + np.radians(1), "the flight would enter a ball"
        # colour each vertex by its angle around one fixed plane, so the structure reads as rings
        hue = (np.arctan2(C @ self.u, C @ self.r) / TWO_PI) % 1.0
        col = 0.15 + 0.85 * hue_rgb(hue)
        # the observer's own head is the last ball: dark slate, so the backdrop reads as a surface
        self.C = np.vstack([C, np.zeros((1, 4))])            # the head's centre is set per frame
        self.col = np.vstack([col, np.array([[0.30, 0.32, 0.36]])])
        self.rho = np.concatenate([np.full(120, RHO), [RHO_SELF]])
        self.cosr = np.cos(self.rho).astype(np.float32)
        f = (W / 2) / np.tan(np.radians(FOV_DEG) / 2)
        xs = (np.arange(W) - (W - 1) / 2) / f
        ys = -(np.arange(H) - (H - 1) / 2) / f
        self.X, self.Y = np.meshgrid(xs, ys)

    def camera(self, s):
        p = np.cos(s) * self.a + np.sin(s) * self.b
        fwd = -np.sin(s) * self.a + np.cos(s) * self.b
        return p, fwd

    def render(self, s, exposure=0.75):
        p, fwd = self.camera(s)
        C = self.C.copy()
        # the head sits just behind the eye, so the eye is on its front surface and the lamp is outside it
        C[-1] = p * np.cos(RHO_SELF) - fwd * np.sin(RHO_SELF)
        D = (fwd[None, None, :] + self.X[..., None] * self.r[None, None, :]
             + self.Y[..., None] * self.u[None, None, :])
        D /= np.linalg.norm(D, axis=-1, keepdims=True)
        D = D.astype(np.float32)
        tbest = np.full((H, W), np.inf, np.float32)
        idx = np.full((H, W), -1, np.int32)
        A_all = (C @ p).astype(np.float32)
        Cf = C.astype(np.float32)
        tb_flat, idx_flat = tbest.ravel(), idx.ravel()       # views: writes land in tbest and idx
        for k in range(len(C)):
            B = D @ Cf[k]
            R = np.hypot(A_all[k], B)
            ii = np.flatnonzero(R >= self.cosr[k])           # only the pixels whose ray meets this ball
            if ii.size == 0:
                continue
            Bf, Rf = B.ravel()[ii], R.ravel()[ii]
            t = np.arctan2(Bf, A_all[k]) - np.arccos(np.clip(self.cosr[k] / Rf, -1, 1))
            t = np.mod(t, TWO_PI).astype(np.float32)
            better = t < tb_flat[ii]
            jj = ii[better]
            tb_flat[jj] = t[better]
            idx_flat[jj] = k
        assert (idx >= 0).all(), "a ray escaped a closed universe"
        # shading at the hit: q on the ball's surface, the ray direction there, the inward normal
        t = tbest.astype(np.float64)
        ct, st = np.cos(t)[..., None], np.sin(t)[..., None]
        Dd = D.astype(np.float64)
        q = p[None, None, :] * ct + Dd * st
        g = -p[None, None, :] * st + Dd * ct
        c = C[idx]
        n_in = c - np.sum(c * q, axis=-1, keepdims=True) * q
        n_in /= np.maximum(np.linalg.norm(n_in, axis=-1, keepdims=True), 1e-9)
        lam = np.clip(np.sum(g * n_in, axis=-1), 0, 1)
        irr = 1.0 / np.maximum(np.sin(t) ** 2, 1e-4)        # a headlamp's irradiance on the 3-sphere
        col = self.col[idx]
        # the back of your own head: dark (albedo a few percent, it is hair) with a faint grid so it reads
        # as a surface -- because your own lamp lights it at 1/sin^2(6 deg), ninety times anything a
        # quarter of the way round, and a pale head would render as a white sky
        head = idx == len(C) - 1
        if head.any():
            qr = np.sum(q[head] * self.r, axis=-1)
            qu = np.sum(q[head] * self.u, axis=-1)
            grid = (np.floor(qr * 300) + np.floor(qu * 300)) % 2
            col[head] = (0.018 + 0.022 * grid)[:, None] * np.array([[0.85, 0.9, 1.0]])
        v = exposure * (irr * lam)[..., None] * col + 0.05 * col
        img = v / (1 + v)                                   # Reinhard, per channel: hot things go white
        return (np.clip(img, 0, 1) * 255).astype(np.uint8), tbest

    def caption(self, img, s):
        frac = (s / TWO_PI) % 1.0
        lines = [f"inside the 3-sphere   {frac:5.1%} of the way round the universe",
                 "straight ahead is the antipode; behind everything is the back of your own head"]
        y = H - 14 - 24 * len(lines)
        for ln in lines:
            draw_text(img, 16, y, ln, scale=2, color=(215, 215, 215))
            y += 24
        note = "Reinhard exposure, headlamp only"
        draw_text(img, W - 16 - text_width(note, 2), H - 26, note, scale=2, color=(150, 150, 150))
        return img


def write_png(path, img):
    subprocess.run([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                    "-i", "-", "-frames:v", "1", "-update", "1", path], input=img.tobytes(), check=True)


if __name__ == "__main__":
    mode = sys.argv[1]
    sc = Scene()
    if mode == "path":
        print(f"clearance {np.degrees(sc.clearance):.2f} deg; balls {np.degrees(RHO):.0f} deg; "
              f"head {np.degrees(RHO_SELF):.0f} deg")
        sys.exit(0)
    if mode == "still":
        frames = 480
        k = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        s = TWO_PI * k / frames
        t0 = time.time()
        img, tb = sc.render(s)
        print(f"frame {k}: {time.time() - t0:.1f} s; nearest hit {np.degrees(tb.min()):.1f} deg, "
              f"farthest {np.degrees(tb.max()):.1f} deg")
        write_png(sys.argv[2], sc.caption(img, s))
        sys.exit(0)
    if mode == "film":
        frames = int(sys.argv[3]) if len(sys.argv) > 3 else 480
        out = sys.argv[2]
        # frames go to disk as PNG and are encoded from there: a 2.7 MB write to a Windows pipe fails
        import os
        fdir = out + ".frames"
        os.makedirs(fdir, exist_ok=True)
        t0 = time.time()
        for k in range(frames):
            s = TWO_PI * k / frames
            img, _ = sc.render(s)
            write_png(os.path.join(fdir, f"f{k:04d}.png"), sc.caption(img, s))
            if k % 24 == 0:
                print(f"  frame {k}/{frames}  {time.time() - t0:.0f} s", flush=True)
        n = len([f for f in os.listdir(fdir) if f.endswith(".png")])
        assert n == frames, f"{n} frames on disk, {frames} expected"
        subprocess.run([FF, "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(fdir, "f%04d.png"),
                        "-vf", "format=yuv420p", "-c:v", "h264_mf", "-b:v", "20M",   # this build has no libx264
                        "-movflags", "+faststart", out], check=True)
        print(f"FILM DONE {frames} frames in {time.time() - t0:.0f} s -> {out}")
