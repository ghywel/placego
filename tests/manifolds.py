"""Deterministic weird geometry with ANALYTIC per-pixel motion, for the field shaders.

    manifolds.py <scene> <outdir> [frames] [fps]
        scene: torus | mobius | tesseract | hopf | mobius_bl | zoom | aperture

READ THE FIELD EXACTLY. A machine-mode frame must come out of ffmpeg with `format=rgb48le` INSIDE the
filter graph (or as rawvideo); `-pix_fmt rgb48le` on the output passes through an 8-bit limited-range
intermediate and corrupts every value (NFRAME-LIMITS.md section 9, the retraction). fieldcheck.py refuses
such a frame. The three later scenes: mobius_bl is the band with a texture band-limited above the coarsest
level's Nyquist; zoom is a flat disc expanding 0.6% per frame (pure divergence, no rotation); aperture is
a rigid translation seen through a static rim -- the calibration control and the silhouette-capture test.

Every scene is a rigid or 4D-rigid motion of a textured object rendered orthographically at 1280x720 by
forward splatting with a z-buffer at 2x supersampling. Each rendered sample carries the 2D velocity of the
surface point it came from (px per source interval, from the exact chord of the motion), so the truth
field is known at every visible pixel; occluded and background pixels are NaN in the truth. Output:
  <outdir>/src.mkv           the frames, ffv1, 8-bit gray, <fps>
  <outdir>/truth_NNN.npy     per frame: float32 [H, W, 2] velocity in px/interval (x right, y down), NaN off-object
  <outdir>/mask_NNN.npy      per frame: bool [H, W] visible surface
The velocity is the ONE-INTERVAL CHORD (position at t+1 minus position at t, projected), which is what a
two-frame flow measures; the instantaneous velocity differs from it by the curvature term.

TEXTURE. One recipe for every surface, in arc-length coordinates on the surface so it is the same texture
wherever the surface is seen: the ladder's M1 sum of three incommensurate sines at 42, 22 and 12 px
periods (aperiodic, no repeat to lock onto, band-limited well above what a 2x splat can alias). Tubes are
shaded around their circumference and textured along their length the same way.

torus     R=180 r=70 about (640,360), symmetry axis tilted 55 deg from the line of sight, spinning about
          that axis at 0.9 rad/s: the silhouette is static, the texture slides and foreshortens, the far
          half is hidden. Non-rigid 2D flow of a rigid 3D motion.
mobius    the half-twist band (R=170, half-width 55) rotating about the vertical image axis at 0.6 rad/s:
          a tumbling object whose silhouette and occlusions move.
tesseract the 16-vertex hypercube rotating in the xw plane at 0.5 rad/s and the yz plane at 0.35 rad/s,
          projected 4D->3D by perspective (w) and 3D->2D orthographically, drawn as 10 px tubes: thin
          structures crossing each other, with the aperture problem everywhere.
hopf      fibres of the Hopf fibration of S^3, stereographically projected to R^3 and drawn as tubes; the
          3-sphere rotates by the Hopf action (equal angles in the xy and zw planes, 0.7 rad/s), under
          which every fibre slides along ITSELF: the flow is tangent to every tube. Fibres that pass near
          the projection pole are left out (they fly off the frame).
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np

W, H = 1280, 720
SS = 2                                   # supersampling for the splat
# The encoder: $FFMPEG as the other tests here use it (on Windows a native path, and the patched build's
# DLL directory must already be on PATH -- run from the MSYS shell TOOLS.md describes), else "ffmpeg".
FF = os.environ.get("FFMPEG", "ffmpeg")

scene = sys.argv[1]
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 97
FPS = float(sys.argv[4]) if len(sys.argv) > 4 else 24.0
DT = 1.0 / FPS


def texture(sa, sb):
    """The M1 recipe, band-limited: three sines at 42, 22 and 12 px periods in surface arc length."""
    return 0.5 + 0.14 * (np.sin(0.15 * sa + 0.09 * sb) + np.sin(0.28 * sa - 0.21 * sb) + np.sin(0.51 * sa + 0.44 * sb))


def rot3(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    c, s = math.cos(ang), math.sin(ang)
    x, y, z = a
    return np.array([[c + x * x * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                     [y * x * (1 - c) + z * s, c + y * y * (1 - c), y * z * (1 - c) - x * s],
                     [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z * z * (1 - c)]])


def splat(P2, Z, lum, Vel):
    """Forward-splat samples (N,2) px coords, depth (N,), luma (N,), velocity (N,2) into frame buffers.
    Nearest sample wins per supersampled texel (max depth = nearest to the viewer, +z toward viewer)."""
    Wp, Hp = W * SS, H * SS
    img = np.zeros((Hp, Wp), np.float32)
    vx = np.full((Hp, Wp), np.nan, np.float32); vy = np.full((Hp, Wp), np.nan, np.float32)
    xi = np.round(P2[:, 0] * SS).astype(int); yi = np.round(P2[:, 1] * SS).astype(int)
    ok = (xi >= 0) & (xi < Wp) & (yi >= 0) & (yi < Hp)
    xi, yi, Z, lum, Vel = xi[ok], yi[ok], Z[ok], lum[ok], Vel[ok]
    order = np.argsort(Z)                  # far first, near last: last write wins
    xi, yi, lum, Vel = xi[order], yi[order], lum[order], Vel[order]
    img[yi, xi] = lum; vx[yi, xi] = Vel[:, 0]; vy[yi, xi] = Vel[:, 1]
    img = img.reshape(H, SS, W, SS).mean(axis=(1, 3))
    with np.errstate(all="ignore"):
        vxs = np.nanmean(vx.reshape(H, SS, W, SS), axis=(1, 3)); vys = np.nanmean(vy.reshape(H, SS, W, SS), axis=(1, 3))
    mask = ~np.isnan(vxs)
    return img, np.stack([vxs, vys], -1).astype(np.float32), mask


def project(P3):
    """Orthographic: x right, y down, z toward the viewer. Centre of the frame."""
    return np.stack([P3[:, 0] + W / 2, H / 2 - P3[:, 1]], -1), P3[:, 2]


def tubes(curves, s_along, radius, n_around, tex_phase=0.0):
    """Tube surfaces around (n_curves, n_along, 3) polylines; textured along by arc length s_along
    (n_curves, n_along) and shaded around. Returns points (N,3) and luma (N,)."""
    pts = []; lum = []
    th = np.linspace(0, 2 * np.pi, n_around, endpoint=False)
    for C, s in zip(curves, s_along):
        T = np.gradient(C, axis=0); T /= (np.linalg.norm(T, axis=1, keepdims=True) + 1e-9)
        ref = np.where(np.abs(T[:, 2:3]) < 0.9, np.array([[0, 0, 1.0]]), np.array([[0, 1.0, 0]]))
        n1 = np.cross(T, ref); n1 /= (np.linalg.norm(n1, axis=1, keepdims=True) + 1e-9); n2 = np.cross(T, n1)
        Pe = C[:, None, :] + radius * (np.cos(th)[None, :, None] * n1[:, None, :] + np.sin(th)[None, :, None] * n2[:, None, :])
        shade = (0.65 + 0.35 * np.cos(th))[None, :]
        tx = texture(s[:, None] + tex_phase, radius * th[None, :])
        pts.append(Pe.reshape(-1, 3)); lum.append((tx * shade).ravel())
    return np.concatenate(pts), np.concatenate(lum)


# ------------------------------------------------------------------ scenes: at(t) -> points, luma
def torus_scene():
    R, r = 180.0, 70.0
    u = np.linspace(0, 2 * np.pi, 2400, endpoint=False); v = np.linspace(0, 2 * np.pi, 900, endpoint=False)
    U, V = np.meshgrid(u, v, indexing="ij"); U = U.ravel(); V = V.ravel()
    P = np.stack([(R + r * np.cos(V)) * np.cos(U), (R + r * np.cos(V)) * np.sin(U), r * np.sin(V)], -1)
    lum = texture((R + r * np.cos(V)) * U, r * V)
    tilt = rot3([1, 0, 0], math.radians(55))
    def at(t):
        return P @ rot3([0, 0, 1], 0.9 * t).T @ tilt.T, lum
    return at


def mobius_scene():
    R, w = 170.0, 55.0
    u = np.linspace(0, 2 * np.pi, 2600, endpoint=False); v = np.linspace(-w, w, 260)
    U, V = np.meshgrid(u, v, indexing="ij"); U = U.ravel(); V = V.ravel()
    P = np.stack([(R + V * np.cos(U / 2)) * np.cos(U), (R + V * np.cos(U / 2)) * np.sin(U), V * np.sin(U / 2)], -1)
    lum = texture(R * U, V)
    base = rot3([1, 0, 0], math.radians(60))
    def at(t):
        return P @ base.T @ rot3([0, 1, 0], 0.6 * t).T, lum
    return at


def tesseract_scene():
    verts = np.array([[(i >> k) & 1 for k in range(4)] for i in range(16)], float) * 2 - 1
    edges = [(i, j) for i in range(16) for j in range(i + 1, 16) if bin(i ^ j).count("1") == 1]
    n_along = 300
    def at(t):
        a, b = 0.5 * t, 0.35 * t
        Rxw = np.eye(4); Rxw[[0, 0, 3, 3], [0, 3, 0, 3]] = [math.cos(a), -math.sin(a), math.sin(a), math.cos(a)]
        Ryz = np.eye(4); Ryz[[1, 1, 2, 2], [1, 2, 1, 2]] = [math.cos(b), -math.sin(b), math.sin(b), math.cos(b)]
        V4 = verts @ Rxw.T @ Ryz.T
        V3 = V4[:, :3] / (3.2 - V4[:, 3:4]) * 330.0             # perspective from 4D along w
        curves = []; s_along = []
        for k, (i, j) in enumerate(edges):
            s = np.linspace(0, 1, n_along)
            C = V3[i] * (1 - s)[:, None] + V3[j] * s[:, None]
            curves.append(C); s_along.append(s * np.linalg.norm(V3[j] - V3[i]) + 137.0 * k)   # a different phase per edge
        return tubes(curves, s_along, 10.0, 28)
    return at


def hopf_scene():
    n_fib, n_along = 40, 1400
    k = np.arange(n_fib); phi = np.arccos(1 - 2 * (k + 0.5) / n_fib); th0 = k * 2.399963
    keep = np.sin(phi / 2) <= 0.9                          # fibres near the projection pole fly off the frame
    view = rot3([1, 0.3, 0], 0.6)
    def at(t):
        curves = []; s_along = []
        for f in np.nonzero(keep)[0]:
            a = math.cos(phi[f] / 2); b = math.sin(phi[f] / 2)
            s = np.linspace(0, 2 * np.pi, n_along, endpoint=False) + 0.7 * t   # the Hopf rotation slides along s
            z1 = a * np.exp(1j * s); z2 = b * np.exp(1j * (s + th0[f]))
            X = np.stack([z1.real, z1.imag, z2.real, z2.imag], -1)            # on S^3
            C = X[:, :3] / ((1.0 - X[:, 3])[:, None] + 1e-6) * 120.0 @ view.T
            seg = np.linalg.norm(np.diff(C, axis=0, prepend=C[:1]), axis=1); arc = np.cumsum(seg)
            curves.append(C); s_along.append(arc + 91.0 * f)
        return tubes(curves, s_along, 9.0, 24)
    return at


def texture_bl(sa, sb):
    """Aperiodic and band-limited ABOVE the coarsest level's Nyquist: four incommensurate sines at 32, 36,
    48 and 65 px periods (the 1/16 level's texels are 16 px, so nothing here aliases at any level)."""
    return 0.5 + 0.11 * (np.sin(0.185 * sa + 0.07 * sb) + np.sin(0.137 * sa - 0.11 * sb)
                         + np.sin(0.103 * sa + 0.081 * sb) + np.sin(0.076 * sa - 0.059 * sb))


def mobius_bl_scene():
    """The band with the band-limited texture: the time-asymmetry test without a component the coarse
    levels alias (NFRAME-LIMITS.md section 9, 'The pipeline is not time-symmetric')."""
    R, w = 170.0, 55.0
    u = np.linspace(0, 2 * np.pi, 2600, endpoint=False); v = np.linspace(-w, w, 260)
    U, V = np.meshgrid(u, v, indexing="ij"); U = U.ravel(); V = V.ravel()
    P = np.stack([(R + V * np.cos(U / 2)) * np.cos(U), (R + V * np.cos(U / 2)) * np.sin(U), V * np.sin(U / 2)], -1)
    lum = texture_bl(R * U, V)
    base = rot3([1, 0, 0], math.radians(60))
    def at(t):
        return P @ base.T @ rot3([0, 1, 0], 0.6 * t).T, lum
    return at


def zoom_scene():
    """A flat textured disc in the image plane scaling about the frame's centre by 0.6% per frame at 24 fps
    (radial flow, 1.9 px/frame at the rim): pure expansion forward, pure contraction backwards, no rotation
    and no occlusion. The translation-only matcher's response to a scale change, each way."""
    r = np.sqrt(np.linspace(0, 1, 900)) * 320.0; th = np.linspace(0, 2 * np.pi, 2400, endpoint=False)
    Rr, T = np.meshgrid(r, th, indexing="ij"); Rr = Rr.ravel(); T = T.ravel()
    P = np.stack([Rr * np.cos(T), Rr * np.sin(T), np.zeros_like(Rr)], -1)
    lum = texture(P[:, 0] + 5000.0, P[:, 1] + 5000.0)        # the texture is fixed to the surface, in its own pixels
    def at(t):
        return P * (1.0 + 0.144 * t), lum                         # 0.144/s = 0.6% per frame at 24 fps
    return at


def aperture_scene():
    """SILHOUETTE CAPTURE, isolated: a textured plane translating rigidly at (4.0, 1.5) px per frame, seen
    through a STATIC circular aperture of radius 250 px. Inside the aperture the truth is one constant
    vector; the aperture's edge is a high-contrast outline that does not move. If the coarse levels'
    windows are captured by the outline, the flow near it reads low and recovers with distance."""
    n = 1400; xs = np.linspace(-700, 700, n); ys = np.linspace(-420, 420, 840)
    X, Y = np.meshgrid(xs, ys, indexing="ij"); X = X.ravel(); Y = Y.ravel()
    lum = texture(X + 3000.0, Y + 3000.0)
    vel = np.array([4.0, -1.5, 0.0]) * 24.0               # px/s: (4.0, 1.5) px/frame on screen (y down)
    def at(t):
        P = np.stack([X, Y, np.zeros_like(X)], -1) + vel * t
        return P, lum, np.hypot(P[:, 0], P[:, 1]) < 250.0      # the same points every frame; visibility is the aperture
    return at


SCENES = {"torus": torus_scene, "mobius": mobius_scene, "tesseract": tesseract_scene, "hopf": hopf_scene,
          "mobius_bl": mobius_bl_scene, "zoom": zoom_scene, "aperture": aperture_scene}
at = SCENES[scene]()

frames = []
for n in range(NF):
    r0 = at(n * DT); r1 = at((n + 1) * DT)
    P0, lum = r0[0], r0[1]; P1 = r1[0]
    if len(r0) > 2:                          # a scene with a visibility flag (an aperture): the points are
        vis = r0[2]                          # the same set every frame, and only those visible at t are drawn
        P0, P1, lum = P0[vis], P1[vis], lum[vis]
    p2a, z = project(P0); p2b, _ = project(P1)
    vel = p2b - p2a                                              # one-interval chord in px
    img, V, mask = splat(p2a, z, lum, vel)
    img = np.where(mask, img, 0.12)
    frames.append((img * 255).clip(0, 255).astype(np.uint8))
    np.save(out / ("truth_%03d.npy" % n), V); np.save(out / ("mask_%03d.npy" % n), mask)
    if n % 24 == 0:
        vis = mask.sum(); vn = np.linalg.norm(V[mask], axis=1) if vis else np.zeros(1)
        print("  frame %3d: %6d visible px, |v| mean %.2f max %.2f px/interval" % (n, vis, vn.mean(), vn.max()))

raw = out / "src.gray"
with open(raw, "wb") as fh:
    for f in frames: fh.write(f.tobytes())
subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "gray", "-s", "%dx%d" % (W, H),
                "-r", str(FPS), "-i", str(raw), "-c:v", "ffv1", "-level", "3", "-pix_fmt", "yuv420p", str(out / "src.mkv")], check=True)
raw.unlink()
print("%s: %d frames -> %s" % (scene, NF, out / "src.mkv"))
