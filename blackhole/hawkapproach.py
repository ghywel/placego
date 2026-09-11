"""The approach: a static (hovering) observer descends toward a Schwarzschild black hole that is radiating Hawking
photons into empty space (the Unruh state: outgoing modes thermal at T_H, nothing coming in but starlight), and
looks straight down and straight up (2026-09-08, the owner's question: can the never-seen Hawking glow be rendered
by going closer than anyone has looked).

    hawkapproach.py <outdir> [frames] [panel px] [T_H in kelvin] [r_start / M] [r_end / M]

Ray optics (honest for the short-wavelength tail of the spectrum, wrong at its peak, where the wavelength is 13 horizon
radii and the glow is a dipole blur; see hawkmode.py): every direction the observer looks is traced backwards, and it
either came from the horizon or from infinity. From the horizon it carries the Hawking glow: a uniform radiance,
thermal at T_H at infinity, blueshifted for the static observer at r by beta = 1 / sqrt(1 - 2M/r), the same in every
direction, so the glow is a uniform disc (or, inside r = 3M, a uniform sky with a hole in it) at the local temperature
T_H beta. From infinity it carries a faint star field, lensed, and blueshifted by the same beta. The border between
the two is the escape cone: from the outward direction, sky for angles psi < psi_e with sin(psi_e) = (3 sqrt3 M / r)
sqrt(1 - 2M/r) inside r = 3M, and psi_e = pi - asin(...) outside; every ray is also integrated numerically (the affine
null geodesic r'' = b^2 (1 - 3M/r) / r^3) for the lensing of the stars, and the two agree. The observer hovers: the
thrust needed is a = M / (r^2 sqrt(1 - 2M/r)), and as r -> 2M the glow's temperature T_H beta -> a / 2 pi, the Unruh
temperature of that thrust: at the horizon Hawking's radiation and Unruh's are one thing.

The glow's colour is the blackbody at T_H beta, integrated against the CIE colour-matching functions for a hole of
the mass that gives the chosen T_H (2000 K: 6.1e19 kg, a 91-nanometre horizon). Not the greybody-filtered spectrum
of greybody.npz: the filtering happens at the barrier at r = 3M, so a hoverer inside it sees the unfiltered thermal
flux, and the filter is the same wave effect that forbids this picture's sharp edge; the blackbody is the one spectrum
consistent with ray optics, and the real spectrum is in the chart. A camera's auto-exposure holds the glow at a fixed
display luminance (the caption counts the stops, which climb by 17 over the descent) so the colour is what changes:
orange-red at T_H, white near 5000 K, blue-white at 20,000 K. The stars are drawn at a fixed brightness with their
true colour shift (under that exposure they would fade out within a few M). Output: rgb24 frames
(<outdir>/frames.rgb), 1920 x 1040 (two 960 panels and a caption strip), and PPM stills at a few radii.
"""
import math
import pathlib
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import hawkcolor as hc

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
NF = int(sys.argv[2]) if len(sys.argv) > 2 else 240
P = int(sys.argv[3]) if len(sys.argv) > 3 else 960
TH_K = float(sys.argv[4]) if len(sys.argv) > 4 else 2000.0
R0 = float(sys.argv[5]) if len(sys.argv) > 5 else 40.0
R1 = float(sys.argv[6]) if len(sys.argv) > 6 else 2.02
FOV = math.radians(100.0)
HUD = 80
W, H = 2 * P, P + HUD
R_FAR = 800.0
SQ27 = 3 * math.sqrt(3)

t0 = time.time()
M_kg = hc.mass_for_TH(TH_K)
hk = hc.Hawking()
rs_m = hc.rs_metres(M_kg)
P_W = hk.power_watts(M_kg)
print(f"T_H = {TH_K:.0f} K -> M = {M_kg:.3e} kg, r_s = {rs_m * 1e9:.1f} nm, photon power {P_W:.3e} W; spectrum peak at w M = {hk.w_peak:.3f}")


def lum(rgb):
    return 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]


glow1 = hc.blackbody_rgb(TH_K, M_kg)
TARGET_L = 0.8                       # the glow's linear luminance before the tone map (0.44 after it, 0.69 displayed)
EXPO0 = TARGET_L / lum(glow1)        # the exposure at the start; then a camera's auto-exposure holds the glow there
STAR_T = 3000.0 * (10000.0 / 3000.0) ** (np.arange(8) / 7.0)   # and the caption counts the stops
print(f"exposure: glow at T_H -> linear luminance {TARGET_L} (linear rgb of the glow at beta = 1: {np.round(glow1 / glow1.max(), 3)})")
# the stars are drawn at a fixed display brightness with their true colour shift: under the auto-exposure that holds
# the glow they would fade to nothing within a few M (the glow, in the Wien tail, brightens thousands of times faster)

# ---- the two panels' look directions (fixed) ------------------------------------------------------------------
tanx = math.tan(FOV / 2)
px = (np.arange(P) + 0.5) / P * 2 - 1
py = 1 - (np.arange(P) + 0.5) / P * 2
PX, PY = np.meshgrid(px, py)
panels = {}
for name, fz in (("down", -1.0), ("up", 1.0)):
    # the observer's frame: z is up (away from the hole), x right, y up-in-the-picture; looking down flips z and x
    nx = tanx * PX * (1.0 if fz > 0 else -1.0)
    ny = tanx * PY
    nz = np.full_like(nx, fz)
    nrm = np.sqrt(nx * nx + ny * ny + nz * nz)
    nx, ny, nz = nx / nrm, ny / nrm, nz / nrm
    psi = np.arccos(np.clip(nz, -1, 1))                              # angle from up
    s = np.maximum(np.sqrt(nx * nx + ny * ny), 1e-12)
    panels[name] = (psi.ravel(), (nx / s).ravel(), (ny / s).ravel())  # psi and the unit transverse direction e


def cone(r):
    B = (SQ27 / r) * math.sqrt(1 - 2 / r)
    return math.asin(min(B, 1.0)) if r < 3 else math.pi - math.asin(min(B, 1.0))


def trace(r_obs, psis):
    """null geodesics from a static observer at r_obs looking at angles psis from the outward radial direction.
    Returns (escaped mask, phi_infinity) with phi the position angle from the outward direction in the ray's plane."""
    n = psis.size
    b = r_obs * np.sin(psis) / math.sqrt(1 - 2 / r_obs)
    r = np.full(n, r_obs); pr = np.cos(psis); ph = np.zeros(n)
    state = np.zeros(n, np.int8)                                     # 0 flying, 1 escaped, 2 fell / lost
    phi_inf = np.zeros(n)
    active = np.arange(n)
    b2 = b * b
    steps = 0
    while active.size and steps < 60000:
        ra, pa, pha, bb = r[active], pr[active], ph[active], b2[active]
        h = np.clip(0.01 * ra, 0.004, 5.0)

        def f(rr, pp):
            return pp, bb * (1.0 / rr ** 3 - 3.0 / rr ** 4), np.sqrt(bb) / (rr * rr)

        k1r, k1p, k1f = f(ra, pa)
        k2r, k2p, k2f = f(ra + 0.5 * h * k1r, pa + 0.5 * h * k1p)
        k3r, k3p, k3f = f(ra + 0.5 * h * k2r, pa + 0.5 * h * k2p)
        k4r, k4p, k4f = f(ra + h * k3r, pa + h * k3p)
        rn = ra + h / 6 * (k1r + 2 * k2r + 2 * k3r + k4r)
        pn = pa + h / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        phn = pha + h / 6 * (k1f + 2 * k2f + 2 * k3f + k4f)
        esc = rn > R_FAR
        fell = rn < 2.0005
        idx = active
        r[idx] = rn; pr[idx] = pn; ph[idx] = phn
        state[idx[esc]] = 1
        phi_inf[idx[esc]] = phn[esc] + np.arcsin(np.clip(np.sqrt(bb[esc]) / rn[esc], -1, 1))
        state[idx[fell & ~esc]] = 2
        active = idx[~(esc | fell)]
        steps += 1
    state[active] = 2
    return state == 1, phi_inf


def deflection_table(r_obs, psi_e):
    qa = np.linspace(0, 1, 1400, endpoint=False) * psi_e
    qb = psi_e - np.exp(np.linspace(math.log(psi_e / 1400), math.log(1e-8), 1400))
    psis = np.unique(np.concatenate([qa, qb]))
    psis = psis[(psis > 1e-5) & (psis < psi_e)]
    escm, phi_inf = trace(r_obs, psis)
    # the nearly radial rays are straight
    psis = np.concatenate([[0.0], psis[escm]]); phi_inf = np.concatenate([[0.0], phi_inf[escm]])
    return psis, phi_inf, int((~escm).sum())


def stars(ex, ey, ez):
    v0 = np.floor((ex + 1.0) * 400.0).astype(np.int64)
    v1 = np.floor((ey + 1.0) * 400.0).astype(np.int64)
    v2 = np.floor((ez + 1.0) * 400.0).astype(np.int64)
    h = (v0 * 73856093 ^ v1 * 19349663 ^ v2 * 83492791) & 0xFFFFFF
    h2 = (v0 * 83492791 ^ v1 * 73856093 ^ v2 * 19349663) & 0xFFFF
    on = h < int(0xFFFFFF * 0.004)
    bright = 0.25 + 0.75 * ((h2 >> 3) & 0xFF) / 255.0
    cls = h2 & 7
    return on, bright, cls


# ---- the frames ------------------------------------------------------------------------------------------------
rr = 2.0 + (R0 - 2.0) * ((R1 - 2.0) / (R0 - 2.0)) ** (np.arange(NF) / max(NF - 1, 1))
stills = {int(np.argmin(np.abs(rr - v))): v for v in (R0, 10.0, 4.0, 2.5, 2.1, R1)}
fh = open(out / "frames.rgb", "wb")
checked = False
for n in range(NF):
    r = float(rr[n])
    beta = 1.0 / math.sqrt(1 - 2 / r)
    T_loc = TH_K * beta
    psi_e = cone(r)
    accel = 1.0 / (r * r * math.sqrt(1 - 2 / r))                   # in units of c^4 / (G M)
    accel_g = accel * hc.C ** 4 / (hc.G * M_kg) / 9.80665
    psis, phis, lost = deflection_table(r, psi_e)
    if not checked:
        # the analytic cone against the tracer, once: a ray just inside the cone escapes, just outside falls
        e_in, _ = trace(r, np.array([psi_e - 0.02]))
        e_out, _ = trace(r, np.array([min(psi_e + 0.02, math.pi - 1e-4)]))
        print(f"cone check at r = {r:.2f}: psi_e = {math.degrees(psi_e):.2f} deg; inside escapes: {bool(e_in[0])}, outside escapes: {bool(e_out[0])}")
        checked = True
    glow_lin = hc.blackbody_rgb(T_loc, M_kg)
    EXPO = TARGET_L / lum(glow_lin)
    stops = math.log2(EXPO0 / EXPO)
    glow = glow_lin * EXPO
    star_rgb = []
    for T in STAR_T:
        c = hc.blackbody_rgb(float(T) * beta, M_kg)
        star_rgb.append(c / max(lum(c), 1e-30) * 0.9)
    star_rgb = np.stack(star_rgb)
    frame = np.zeros((H, W, 3), np.uint8)
    for k, name in enumerate(("down", "up")):
        psi, ex, ey = panels[name]
        sky = psi < psi_e
        rgb = np.tile(glow[None, :], (psi.size, 1))
        if sky.any():
            phi_inf = np.interp(psi[sky], psis, phis)
            c, s = np.cos(phi_inf), np.sin(phi_inf)
            on, bright, cls = stars(s * ex[sky], s * ey[sky], c)
            col = star_rgb[cls] * (bright * on)[:, None]
            rgb[sky] = col
        img = hc.tonemap(rgb.reshape(P, P, 3))
        frame[:P, k * P:(k + 1) * P] = (img * 255 + 0.5).astype(np.uint8)
    frame[P - 1:P + 1, :] = 40
    frame[:P, P - 1:P + 1] = 40
    hc.draw_text(frame, 16, 14, "looking down at the hole", 2, (200, 200, 200))
    hc.draw_text(frame, P + 16, 14, "looking up, away from it", 2, (200, 200, 200))
    line1 = f"hovering at r = {r:6.3f} M    glow T = {beta:5.2f} T_H = {T_loc:6.0f} K    sky cone {math.degrees(psi_e):5.1f} deg    exposure {-stops:+5.1f} stops"
    line2 = f"thrust to hover a = {accel:8.4f} c^4/GM = {accel_g:8.2e} g    T_H = {TH_K:.0f} K, M = {M_kg:.2e} kg, horizon {rs_m * 1e9:.0f} nm, {P_W * 1e9:.0f} nW    stars: fixed brightness, true colour shift"
    hc.draw_text(frame, 16, P + 14, line1, 2, (230, 230, 230))
    hc.draw_text(frame, 16, P + 46, line2, 2, (150, 150, 150))
    fh.write(frame.tobytes())
    if n in stills:
        hc.write_ppm(out / f"still_r{stills[n]:.2f}.ppm", frame)
    if n % 24 == 0 or n == NF - 1:
        print(f"  frame {n:3d}: r = {r:6.3f}, beta = {beta:5.2f}, T = {T_loc:6.0f} K, cone {math.degrees(psi_e):5.1f} deg, table {psis.size} rays ({lost} lost) ({time.time() - t0:.0f} s)", flush=True)
fh.close()
print(f"{NF} frames of {W}x{H} -> {out / 'frames.rgb'} ({time.time() - t0:.0f} s)")
