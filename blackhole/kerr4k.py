"""THE 4K FORM of kerr.py (the owner, 2026-09-08: "a 4K render of the Johannsen-Psaltis by itself, regardless of
how long it takes"): the same tracer, run over horizontal BANDS of the frame so 8.3 million rays fit in memory,
the dust and star textures four times finer, the frames written one at a time. Everything else identical.

Black holes that are NOT Schwarzschild, rendered from the same camera by one metric-agnostic geodesic tracer
(the owner's challenge, 2026-09-08).

    kerr.py <metric> <outdir> [frames] [width] [height]
        metric: schwarzschild | kerr | jp        (kerr: a = 0.9; jp: Johannsen-Psaltis deformation of Kerr a = 0.9)

THE TRACER. Every pixel's photon is integrated backwards from the camera with Hamilton's equations for a null
geodesic, H = 1/2 g^{mu nu} p_mu p_nu = 0, in Boyer-Lindquist-like coordinates (t, r, theta, phi):
    dx^mu / dlambda = g^{mu nu} p_nu,      dp_r / dlambda = -dH/dr,      dp_theta / dlambda = -dH/dtheta,
with p_t = -1 (energy 1) and p_phi conserved. The metric enters ONLY as its covariant components g_tt, g_tphi,
g_rr, g_thetatheta, g_phiphi as functions of (r, theta); the inverse is taken numerically (a 2x2 block and two
reciprocals) and dH/dr, dH/dtheta by central differences, so any stationary axisymmetric metric can be dropped
in without deriving anything. Fourth-order Runge-Kutta, the step shrinking toward the horizon. A ray ends when
it falls through the horizon (black), escapes beyond 55 M (a star field by its exit direction), or crosses the
disc's plane theta = pi/2 between the innermost stable circular orbit and 18 M (a hit).

THE METRICS (M = 1).
    schwarzschild   a = 0: the control, the same physics as blackhole.py by a different route.
    kerr            a = 0.9: frame dragging, the D-shaped shadow, the ISCO at 2.32 instead of 6, a prograde disc.
    jp              Johannsen & Psaltis (2011), Kerr a = 0.9 with the deformation h = eps3 r / Sigma^2, eps3 = 3:
                    NOT a solution of the vacuum Einstein equations, a parametrised deviation of the kind used to
                    test whether real black holes are Kerr; the image comes from integrating this metric's
                    geodesics, nothing else.

THE DISC. Thin, opaque, prograde circular orbits; the innermost stable orbit and the orbital frequency Omega(r)
are found numerically from the metric (Omega from the radial derivatives of g_tt, g_tphi, g_phiphi in the
equatorial plane; the ISCO at the minimum of the orbit's energy). The redshift factor of a hit is
g = 1 / (u^t (1 - Omega p_phi)) with u^t from the metric and p_phi the photon's conserved angular momentum:
gravitational and Doppler shifts together (Cunningham's g). Then frames are lookups as in blackhole.py: a
multi-octave dust pattern winding up under the metric's own Omega(r), weighted g^4, coloured by temperature.
Output: <outdir>/frames.rgb (rgb24), plus a text summary of the horizon, ISCO and hit counts.
"""
import math
import pathlib
import sys
import time

import numpy as np

metric_name = sys.argv[1]
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 120
W = int(sys.argv[4]) if len(sys.argv) > 4 else 3840
H = int(sys.argv[5]) if len(sys.argv) > 5 else 2160
BANDS = int(sys.argv[6]) if len(sys.argv) > 6 else 4
FPS = 24.0
A = {"schwarzschild": 0.0, "kerr": 0.9, "jp": 0.9}[metric_name]
EPS3 = {"schwarzschild": 0.0, "kerr": 0.0, "jp": 3.0}[metric_name]
R_OBS, TH_OBS = 40.0, math.radians(78.0)
FOV = math.radians(56.0)
R_OUT = 18.0
R_ESC = 55.0
t0 = time.time()


def metric_cov(r, th):
    """Covariant components g_tt, g_tp, g_rr, g_hh, g_pp of the Kerr metric with the Johannsen-Psaltis
    deformation h = EPS3 r / Sigma^2 (EPS3 = 0 is Kerr; A = 0 too is Schwarzschild). M = 1."""
    s2 = np.maximum(np.sin(th) ** 2, 1e-12)
    c2 = 1.0 - s2
    Sig = r * r + A * A * c2
    Del = r * r - 2.0 * r + A * A
    h = EPS3 * r / (Sig * Sig)
    g_tt = -(1.0 + h) * (1.0 - 2.0 * r / Sig)
    g_tp = -2.0 * A * r * s2 * (1.0 + h) / Sig
    g_pp = s2 * (r * r + A * A + 2.0 * A * A * r * s2 / Sig) + h * A * A * s2 * s2 * (Sig + 2.0 * r) / Sig
    g_rr = Sig * (1.0 + h) / np.maximum(Del + A * A * h * s2, 1e-9)
    g_hh = Sig
    return g_tt, g_tp, g_rr, g_hh, g_pp


def metric_inv(r, th):
    g_tt, g_tp, g_rr, g_hh, g_pp = metric_cov(r, th)
    det = g_tt * g_pp - g_tp * g_tp
    det = np.where(np.abs(det) < 1e-12, -1e-12, det)
    return g_pp / det, -g_tp / det, 1.0 / g_rr, 1.0 / g_hh, g_tt / det      # g^tt, g^tp, g^rr, g^hh, g^pp


def hamiltonian(r, th, p_t, p_r, p_h, p_p):
    gtt, gtp, grr, ghh, gpp = metric_inv(r, th)
    return 0.5 * (gtt * p_t * p_t + 2.0 * gtp * p_t * p_p + gpp * p_p * p_p + grr * p_r * p_r + ghh * p_h * p_h)


def rhs(r, th, p_r, p_h, p_t, p_p):
    gtt, gtp, grr, ghh, gpp = metric_inv(r, th)
    dr = grr * p_r
    dth = ghh * p_h
    dph = gtp * p_t + gpp * p_p
    hr = 1e-4 * np.maximum(r, 1.0)
    dHdr = (hamiltonian(r + hr, th, p_t, p_r, p_h, p_p) - hamiltonian(r - hr, th, p_t, p_r, p_h, p_p)) / (2.0 * hr)
    hh = 1e-4
    dHdh = (hamiltonian(r, th + hh, p_t, p_r, p_h, p_p) - hamiltonian(r, th - hh, p_t, p_r, p_h, p_p)) / (2.0 * hh)
    return dr, dth, dph, -dHdr, -dHdh


# ---- the horizon and the disc's orbits from the metric ------------------------------------------------------
r_h = 1.0 + math.sqrt(max(1.0 - A * A, 0.0))
rr = np.linspace(r_h * 1.02, 30.0, 6000)
th_eq = np.full_like(rr, math.pi / 2)
dr_ = 1e-4
def eq(r):
    return metric_cov(r, np.full_like(r, math.pi / 2))
gtt0, gtp0, _, _, gpp0 = eq(rr)
gtt1, gtp1, _, _, gpp1 = eq(rr + dr_); gtt2, gtp2, _, _, gpp2 = eq(rr - dr_)
dgtt = (gtt1 - gtt2) / (2 * dr_); dgtp = (gtp1 - gtp2) / (2 * dr_); dgpp = (gpp1 - gpp2) / (2 * dr_)
disc_ = dgtp * dgtp - dgtt * dgpp
Om = (-dgtp + np.sqrt(np.maximum(disc_, 0.0))) / dgpp                       # prograde
norm = -(gtt0 + 2.0 * gtp0 * Om + gpp0 * Om * Om)
ok = (norm > 0) & (disc_ > 0)
E_orb = np.where(ok, -(gtt0 + gtp0 * Om) / np.sqrt(np.maximum(norm, 1e-12)), np.inf)
i_isco = int(np.argmin(E_orb))
R_IN = float(rr[i_isco])
def orbit(r):
    """Omega and u^t of the prograde circular orbit at equatorial r, by interpolation on the grid."""
    Omg = np.interp(r, rr, Om)
    ut = np.interp(r, rr, 1.0 / np.sqrt(np.maximum(norm, 1e-12)))
    return Omg, ut
print(f"{metric_name}: a = {A}, eps3 = {EPS3}, horizon r = {r_h:.3f}, ISCO r = {R_IN:.3f} (Omega there {float(Om[i_isco]):.4f})")

# ---- the camera: a zero-angular-momentum observer's tetrad at (R_OBS, TH_OBS, phi = 0) ---------------------
g_tt, g_tp, g_rr, g_hh, g_pp = [float(x[0]) for x in metric_cov(np.array([R_OBS]), np.array([TH_OBS]))]
omega_z = -g_tp / g_pp
alpha = math.sqrt(-(g_tt - g_tp * g_tp / g_pp))
tanx = math.tan(FOV / 2); tany = tanx * H / W
px = (np.arange(W) + 0.5) / W * 2 - 1
py = 1 - (np.arange(H) + 0.5) / H * 2


def trace_band(y0, y1):
    """Trace the rays of rows y0..y1-1; return state, hit_r, hit_az, hit_pp, esc_dir for them."""
    PX, PY = np.meshgrid(px, py[y0:y1])
    PX = PX.ravel(); PY = PY.ravel()
    N = PX.size
    n_r = -np.ones(N); n_h = -tany * PY; n_p = -tanx * PX
    k = 1.0 / np.sqrt(n_r * n_r + n_h * n_h + n_p * n_p)
    n_r *= k; n_h *= k; n_p *= k
    pu_t = 1.0 / alpha * np.ones(N)
    pu_r = n_r / math.sqrt(g_rr)
    pu_h = n_h / math.sqrt(g_hh)
    pu_p = omega_z / alpha + n_p / math.sqrt(g_pp)
    p_t = g_tt * pu_t + g_tp * pu_p
    p_p = g_tp * pu_t + g_pp * pu_p
    p_r = g_rr * pu_r
    p_h = g_hh * pu_h
    E = -p_t
    p_t = p_t / E; p_p = p_p / E; p_r = p_r / E; p_h = p_h / E
    r = np.full(N, R_OBS); th = np.full(N, TH_OBS); ph = np.zeros(N)
    state = np.zeros(N, np.int8)
    hit_r = np.zeros(N); hit_az = np.zeros(N); hit_pp = np.zeros(N); esc_dir = np.zeros((N, 3))
    active = np.arange(N)
    step = 0
    while active.size and step < MAX_STEPS:
        ra, ta, pa, pra, pha = r[active], th[active], ph[active], p_r[active], p_h[active]
        pt, pp = p_t[active], p_p[active]
        dl = np.clip(0.04 * (ra - r_h), 0.004, 0.5) * np.clip(np.sin(ta) / 0.25, 0.04, 1.0)
        k1 = rhs(ra, ta, pra, pha, pt, pp)
        k2 = rhs(ra + 0.5 * dl * k1[0], ta + 0.5 * dl * k1[1], pra + 0.5 * dl * k1[3], pha + 0.5 * dl * k1[4], pt, pp)
        k3 = rhs(ra + 0.5 * dl * k2[0], ta + 0.5 * dl * k2[1], pra + 0.5 * dl * k2[3], pha + 0.5 * dl * k2[4], pt, pp)
        k4 = rhs(ra + dl * k3[0], ta + dl * k3[1], pra + dl * k3[3], pha + dl * k3[4], pt, pp)
        rn = ra + dl / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        tn = ta + dl / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        pn = pa + dl / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        prn = pra + dl / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
        phn = pha + dl / 6 * (k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4])
        fell = rn <= r_h * 1.02
        escaped = (rn > R_ESC) & (rn > ra)
        zc = (np.cos(ta) * np.cos(tn) < 0)
        frac = np.where(zc, np.abs(np.cos(ta)) / np.maximum(np.abs(np.cos(ta)) + np.abs(np.cos(tn)), 1e-12), 0.0)
        rc = ra + frac * (rn - ra); pc = pa + frac * (pn - pa)
        hit = zc & (rc >= R_IN) & (rc <= R_OUT) & ~fell
        idx = active
        state[idx[hit]] = 1; hit_r[idx[hit]] = rc[hit]; hit_az[idx[hit]] = pc[hit]; hit_pp[idx[hit]] = pp[hit]
        state[idx[fell & ~hit]] = 2
        esc = escaped & ~hit & ~fell
        state[idx[esc]] = 3
        esc_dir[idx[esc]] = np.stack([np.sin(tn) * np.cos(pn), np.sin(tn) * np.sin(pn), np.cos(tn)], -1)[esc]
        r[idx] = rn; th[idx] = np.clip(tn, 1e-4, math.pi - 1e-4); ph[idx] = pn; p_r[idx] = prn; p_h[idx] = phn
        active = idx[~(hit | fell | esc)]
        step += 1
    state[active] = 2
    return state, hit_r, hit_az, hit_pp, esc_dir


MAX_STEPS = 40000
parts = []
for b in range(BANDS):
    y0, y1 = b * H // BANDS, (b + 1) * H // BANDS
    parts.append(trace_band(y0, y1))
    st = parts[-1][0]
    print(f"  band {b + 1}/{BANDS} (rows {y0}-{y1 - 1}): {int((st == 1).sum())} hit, {int((st == 2).sum())} fell, {int((st == 3).sum())} escaped ({time.time() - t0:.0f} s)", flush=True)
state = np.concatenate([p[0] for p in parts]); hit_r = np.concatenate([p[1] for p in parts]); hit_az = np.concatenate([p[2] for p in parts])
hit_pp = np.concatenate([p[3] for p in parts]); esc_dir = np.concatenate([p[4] for p in parts]); del parts
N = state.size
print(f"traced {N} rays in {time.time() - t0:.0f} s: {int((state == 1).sum())} hit, {int((state == 2).sum())} fell, {int((state == 3).sum())} escaped", flush=True)

# ---- the redshift and the frames ---------------------------------------------------------------------------
hitm = state == 1
Omg, ut = orbit(np.where(hitm, hit_r, R_IN))
g = np.where(hitm, 1.0 / (ut * (1.0 - Omg * hit_pp)), 0.0)
g = np.clip(g, 0.0, 3.0)
emis = np.where(hitm, (1.0 - np.sqrt(R_IN / np.maximum(hit_r, R_IN))) * np.maximum(hit_r, R_IN) ** -3.0, 0.0)
emis /= emis[hitm].max() if hitm.any() else 1.0

def stars(dirs):
    v = np.floor((dirs + 1.0) * 1600.0).astype(np.int64)
    hsh = (v[:, 0] * 73856093 ^ v[:, 1] * 19349663 ^ v[:, 2] * 83492791) & 0xFFFFFF
    return (hsh < 0xFFFFFF * 0.0025).astype(np.float64) * (0.3 + 0.7 * ((hsh >> 8) & 0xFF) / 255.0)
sky = np.zeros(N); escm = state == 3
sky[escm] = stars(esc_dir[escm]) * 0.9

rng = np.random.default_rng(3)
NP, NR = 2048, 512
def band_noise(nr, nph, k_lo, k_hi):
    fr = np.fft.fftfreq(nr)[:, None]; fp = np.fft.fftfreq(nph)[None, :]
    kk = np.hypot(fr * nr / 32.0, fp * nph / 160.0)
    band = (kk >= k_lo) & (kk <= k_hi)
    spec = np.where(band, np.exp(1j * rng.uniform(0, 2 * np.pi, (nr, nph))), 0.0)
    x = np.fft.ifft2(spec).real
    return (x - x.mean()) / (x.std() + 1e-9)
dust = 0.6 * band_noise(NR, NP, 0.5, 2.0) + 0.3 * band_noise(NR, NP, 2.0, 6.0) + 0.15 * band_noise(NR, NP, 6.0, 16.0)
dust = np.clip(0.5 + 0.45 * dust, 0.03, 1.4)

def ramp(x):
    x = np.clip(x, 0, 1.6)
    return np.stack([np.clip(x * 1.6, 0, 1), np.clip(x * 1.15 - 0.25, 0, 1) ** 1.3, np.clip(x * 0.9 - 0.55, 0, 1) ** 1.6], -1)

lr = np.where(hitm, (np.log(np.maximum(hit_r, R_IN)) - math.log(R_IN)) / (math.log(R_OUT) - math.log(R_IN)), 0.0)
ri = np.clip((lr * (NR - 1)).astype(int), 0, NR - 1)
Om_in = float(np.interp(R_IN, rr, Om))
omega_vis = np.where(hitm, 2 * np.pi / 4.0 * Omg / Om_in, 0.0)        # the metric's own Omega(r), one turn in 4 s at the ISCO
temp_scale = np.where(hitm, g * (R_IN / np.maximum(hit_r, R_IN)) ** 0.75, 0.0)
sky_rgb = np.stack([sky, sky, sky * 1.1], -1)
base_col = ramp(temp_scale * 1.15) * 1.5
with open(out / "frames.rgb", "wb") as fh:
    for n in range(NF):
        t = n / FPS
        phn_ = np.mod(hit_az - omega_vis * t, 2 * np.pi)
        pi_ = np.clip((phn_ / (2 * np.pi) * NP).astype(int), 0, NP - 1)
        I = emis * g ** 4 * dust[ri, pi_] * 6.0
        col = base_col * (I / (1.0 + I))[:, None] + sky_rgb
        fh.write((np.clip(col, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8).tobytes())
        if n % 24 == 0:
            print(f"  frame {n} ({time.time() - t0:.0f} s)", flush=True)
(out / "summary.txt").write_text(f"{metric_name} a={A} eps3={EPS3} horizon={r_h:.4f} isco={R_IN:.4f} hits={int(hitm.sum())} fell={int((state == 2).sum())} escaped={int(escm.sum())} g_max={float(g[hitm].max()) if hitm.any() else 0:.3f}\n")
print(f"{NF} frames of {W}x{H} -> {out / 'frames.rgb'} ({time.time() - t0:.0f} s)", flush=True)
