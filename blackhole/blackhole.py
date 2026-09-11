"""A Schwarzschild black hole with a thin, opaque, glowing dust disc, seen from a camera near the disc's plane
so the far side of the disc is lensed over and under the shadow (the owner's ask, 2026-09-08).

    blackhole.py <outdir> [frames] [width] [height]

Geometric units, M = 1 (the horizon at r = 2, the photon sphere at 3, the innermost stable orbit at 6). The
camera sits at distance D = 40 at inclination 78 degrees from the disc's axis. For every pixel the null
geodesic is integrated once in its own orbital plane with the Binet equation u'' = -u + 3 u^2 (u = 1 / r),
fourth-order Runge-Kutta, until it falls through the horizon (black), escapes (a faint lensed star field
looked up by its exit direction) or crosses the disc's plane between r_in = 6 and r_out = 18 (a hit: the
disc's radius and azimuth there, and the redshift factor g = sqrt(1 - 3/r) / (1 + Omega b_z) for a Keplerian
emitter with Omega = r^-1.5 and b_z the photon's angular momentum about the disc's axis, which carries the
gravitational and Doppler shifts together). Only the first crossing counts: the disc is opaque.

Then every frame is a lookup: emission = g^4 * (1 - sqrt(6 / r)) r^-3 * dust(r, phi - omega(r) t), the dust a
multi-octave noise in (log r, phi) that winds up under differential rotation, and a warm colour ramp by the
observed temperature. Output: rgb24 raw frames for ffmpeg (<outdir>/frames.rgb), plus one PNG-ready preview.
The tracing takes a few minutes at 1280x720; the frames are fast.
"""
import math
import pathlib
import sys
import time

import numpy as np

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
NF = int(sys.argv[2]) if len(sys.argv) > 2 else 240
W = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
H = int(sys.argv[4]) if len(sys.argv) > 4 else 720
FPS = 24.0

D = 40.0                      # camera distance
INC = math.radians(78.0)      # inclination from the disc's axis
FOV = math.radians(56.0)      # horizontal field of view
R_IN, R_OUT = 6.0, 18.0
DPHI = 0.004                  # integration step in the orbital angle
PHI_MAX = 3.5 * math.pi       # rays that loop more than this are lost (they are the photon ring's tail)

t0 = time.time()
# ---- camera rays -------------------------------------------------------------------------------------------
c_hat = np.array([math.sin(INC), 0.0, math.cos(INC)])            # the camera's position direction
fwd = -c_hat
right = np.cross(fwd, np.array([0.0, 0.0, 1.0])); right /= np.linalg.norm(right)
up = np.cross(right, fwd)
tanx = math.tan(FOV / 2); tany = tanx * H / W
px = (np.arange(W) + 0.5) / W * 2 - 1
py = 1 - (np.arange(H) + 0.5) / H * 2
PX, PY = np.meshgrid(px, py)
d = fwd[None, None, :] + tanx * PX[..., None] * right[None, None, :] + tany * PY[..., None] * up[None, None, :]
d = d.reshape(-1, 3); d /= np.linalg.norm(d, axis=1, keepdims=True)
N = d.shape[0]
e1 = np.repeat(c_hat[None, :], N, axis=0)                        # the orbital plane: e1 toward the camera
d_r = d @ c_hat
e2 = d - d_r[:, None] * e1[:, :]
d_t = np.linalg.norm(e2, axis=1)
e2 /= np.maximum(d_t, 1e-9)[:, None]
b_z = D * np.cross(c_hat, d)[:, 2]                               # the photon's L_z / E (sign chooses the disc's spin)

u = np.full(N, 1.0 / D, np.float64)
du = -u * d_r / np.maximum(d_t, 1e-9)                            # du/dphi at the camera (inward: positive)
phi = np.zeros(N)
z_prev = D * c_hat[2] * np.ones(N)
state = np.zeros(N, np.int8)                                     # 0 flying, 1 hit the disc, 2 fell in, 3 escaped
hit_r = np.zeros(N); hit_az = np.zeros(N); esc_dir = np.zeros((N, 3))
e1z, e2z = c_hat[2], e2[:, 2]

def f(u, du):
    return du, -u + 3.0 * u * u

active = np.arange(N)
step = 0
while active.size and step * DPHI < PHI_MAX:
    ua, dua = u[active], du[active]
    k1u, k1d = f(ua, dua)
    k2u, k2d = f(ua + 0.5 * DPHI * k1u, dua + 0.5 * DPHI * k1d)
    k3u, k3d = f(ua + 0.5 * DPHI * k2u, dua + 0.5 * DPHI * k2d)
    k4u, k4d = f(ua + DPHI * k3u, dua + DPHI * k3d)
    un = ua + DPHI / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
    dn = dua + DPHI / 6 * (k1d + 2 * k2d + 2 * k3d + k4d)
    phin = phi[active] + DPHI
    r = 1.0 / np.maximum(un, 1e-9)
    z = r * (math.cos(0) * 0 + np.cos(phin) * e1z + np.sin(phin) * e2z[active])
    fell = un >= 0.5
    escaped = (un < 1.0 / (2.5 * D)) & (dn < 0)
    crossed = (np.sign(z) != np.sign(z_prev[active])) & (z_prev[active] != 0) & ~fell
    # the crossing point, interpolated in phi
    frac = np.where(crossed, np.abs(z_prev[active]) / np.maximum(np.abs(z_prev[active]) + np.abs(z), 1e-9), 0.0)
    phic = phi[active] + frac * DPHI
    uc = u[active] + frac * (un - u[active])
    rc = 1.0 / np.maximum(uc, 1e-9)
    hit = crossed & (rc >= R_IN) & (rc <= R_OUT)
    # azimuth in the disc plane at the crossing
    pos = rc[:, None] * (np.cos(phic)[:, None] * e1[active] + np.sin(phic)[:, None] * e2[active])
    az = np.arctan2(pos[:, 1], pos[:, 0])
    idx = active
    state[idx[hit]] = 1; hit_r[idx[hit]] = rc[hit]; hit_az[idx[hit]] = az[hit]
    state[idx[fell & ~hit]] = 2
    esc = escaped & ~hit & ~fell
    state[idx[esc]] = 3
    esc_dir[idx[esc]] = (np.cos(phin)[:, None] * e1[active] + np.sin(phin)[:, None] * e2[active])[esc]
    u[idx] = un; du[idx] = dn; phi[idx] = phin; z_prev[idx] = z
    active = idx[~(hit | fell | esc)]
    step += 1
    if step % 400 == 0:
        print(f"  step {step}: {active.size} rays flying, {int((state == 1).sum())} hits, {int((state == 2).sum())} fell in, {int((state == 3).sum())} escaped ({time.time() - t0:.0f} s)")
state[active] = 2                                                # what is still circling is the photon ring's tail: black
print(f"traced {N} rays in {time.time() - t0:.0f} s: {int((state == 1).sum())} hit the disc, {int((state == 2).sum())} fell in, {int((state == 3).sum())} escaped")

# ---- the redshift, the geometry maps -----------------------------------------------------------------------
hitm = state == 1
omega = np.where(hitm, hit_r ** -1.5, 0.0)
g = np.where(hitm, np.sqrt(np.clip(1.0 - 3.0 / np.maximum(hit_r, 3.01), 0, 1)) / (1.0 + omega * b_z), 0.0)
emis = np.where(hitm, (1.0 - np.sqrt(R_IN / np.maximum(hit_r, R_IN))) * np.maximum(hit_r, R_IN) ** -3.0, 0.0)
emis /= emis[hitm].max() if hitm.any() else 1.0

# ---- the star field for escaped rays: sparse points by a hash of the exit direction -------------------------
def stars(dirs):
    v = np.floor((dirs + 1.0) * 400.0).astype(np.int64)
    h = (v[:, 0] * 73856093 ^ v[:, 1] * 19349663 ^ v[:, 2] * 83492791) & 0xFFFFFF
    s = (h < 0xFFFFFF * 0.004).astype(np.float64) * (0.3 + 0.7 * ((h >> 8) & 0xFF) / 255.0)
    return s
sky = np.zeros(N); escm = state == 3
sky[escm] = stars(esc_dir[escm]) * 0.9

# ---- the dust: multi-octave noise in (log r, phi), periodic in phi ------------------------------------------
rng = np.random.default_rng(3)
NP, NR = 512, 128
def band_noise(nr, nph, k_lo, k_hi):
    fr = np.fft.fftfreq(nr)[:, None]; fp = np.fft.fftfreq(nph)[None, :]
    k = np.hypot(fr * nr / 8.0, fp * nph / 40.0)
    band = (k >= k_lo) & (k <= k_hi)
    spec = np.where(band, np.exp(1j * rng.uniform(0, 2 * np.pi, (nr, nph))), 0.0)
    x = np.fft.ifft2(spec).real
    return (x - x.mean()) / (x.std() + 1e-9)
dust = 0.6 * band_noise(NR, NP, 0.5, 2.0) + 0.3 * band_noise(NR, NP, 2.0, 6.0) + 0.15 * band_noise(NR, NP, 6.0, 16.0)
dust = np.clip(0.5 + 0.45 * dust, 0.03, 1.4)

def ramp(x):
    """a warm ramp: black -> deep red -> orange -> yellow -> white, x in [0, ~1.5]"""
    x = np.clip(x, 0, 1.6)
    r = np.clip(x * 1.6, 0, 1)
    gch = np.clip(x * 1.15 - 0.25, 0, 1) ** 1.3
    b = np.clip(x * 0.9 - 0.55, 0, 1) ** 1.6
    return np.stack([r, gch, b], -1)

lr = np.where(hitm, (np.log(np.maximum(hit_r, R_IN)) - math.log(R_IN)) / (math.log(R_OUT) - math.log(R_IN)), 0.0)
ri = np.clip((lr * (NR - 1)).astype(int), 0, NR - 1)
omega_vis = np.where(hitm, 2 * np.pi / 4.0 * (R_IN / np.maximum(hit_r, R_IN)) ** 1.5, 0.0)   # one turn in 4 s at r_in
sky_rgb = np.stack([sky, sky, sky * 1.1], -1)

frames = np.zeros((NF, H * W, 3), np.uint8)
for n in range(NF):
    t = n / FPS
    ph = np.mod(hit_az - omega_vis * t, 2 * np.pi)
    pi_ = np.clip((ph / (2 * np.pi) * NP).astype(int), 0, NP - 1)
    tex = dust[ri, pi_]
    I = emis * g ** 4 * tex * 6.0
    temp = np.where(hitm, g * (R_IN / np.maximum(hit_r, R_IN)) ** 0.75, 0.0)
    col = ramp(temp * 1.15) * (I / (1.0 + I))[:, None] * 1.5 + sky_rgb
    frames[n] = (np.clip(col, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8)
    if n % 60 == 0:
        print(f"  frame {n} ({time.time() - t0:.0f} s)")
frames.tofile(out / "frames.rgb")
print(f"{NF} frames of {W}x{H} -> {out / 'frames.rgb'} ({time.time() - t0:.0f} s)")
