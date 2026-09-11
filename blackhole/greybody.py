"""Hawking radiation of a Schwarzschild black hole in photons: the greybody factors, the spectrum, the power, and
the mode functions at the spectrum's peak (2026-09-08, the owner's question "can Hawking radiation be rendered").

Geometric units G = c = hbar = k_B = 1, M = 1: T_H = 1 / (8 pi) = 0.0398. For each multipole l the electromagnetic
(s = 1) Regge-Wheeler equation  d2psi/dr*2 + (w^2 - V) psi = 0,  V = (1 - 2/r) l (l + 1) / r^2,  r* = r + 2 ln(r/2 - 1)
is integrated inward from r = R_far with the pure outgoing wave psi = exp(i w r*) (this is the "up" mode: born at the
horizon, partly transmitted to infinity, partly reflected back in) down to r - 2 = 1e-7, where it is decomposed into
A exp(i w r*) + B exp(-i w r*). The transmission probability Gamma_l(w) = 1 / |A|^2 is the greybody factor (by
reciprocity the same as for a wave sent in from infinity), and psi / A is the mode itself, unit outgoing amplitude at the
horizon. The photon emission is then

    dN/dt dw = 2 * sum_l (2l + 1) Gamma_l(w) / (2 pi (exp(8 pi w) - 1)),   dE/dt dw = w dN/dt dw,

the 2 for the polarisations. Checks printed: Gamma -> 1 at high w for low l, the w^4 law at low w, and the total photon
power against Page 1976 (3.36e-5 hbar c^6 / G^2 M^2, 16.7 % of his 2.011e-4 total). Writes greybody.npz: the w grid,
Gamma[l, w], the spectra, and the l = 1, 2 up-modes on an r* grid at the spectrum's peak frequency.
"""
import math
import pathlib
import sys
import time

import numpy as np

here = pathlib.Path(__file__).resolve().parent
OUT = here / "greybody.npz"
LMAX = 8
R_FAR = 3000.0
X_HOR = 1e-7                  # r - 2 where the horizon decomposition is done
H = 0.05                      # step in r*
w = np.exp(np.linspace(math.log(0.01), math.log(1.5), 260))   # the frequency grid, w M
NW = w.size
T_H = 1.0 / (8 * math.pi)


def rstar_of_x(x):
    return 2.0 + x + 2.0 * np.log(x / 2.0)


def x_of_rstar(rs):
    """invert r* = 2 + x + 2 ln(x/2) by Newton (rs may be an array)"""
    rs = np.asarray(rs, dtype=np.float64)
    x = np.where(rs > 4, rs - 2.0, 2.0 * np.exp((rs - 2.0) / 2.0))
    for _ in range(60):
        f = 2.0 + x + 2.0 * np.log(x / 2.0) - rs
        x = np.maximum(x - f / (1.0 + 2.0 / x), 1e-300)
    return x


def integrate_up(l, ws, keep_below=None):
    """the up-mode for multipole l at frequencies ws (vector): inward RK4 from R_FAR. Returns Gamma (per w), and if
    keep_below is given (an r* value) the arrays (rstar, x, psi[w, i]) for r* < keep_below."""
    ll = l * (l + 1)
    x0 = R_FAR - 2.0
    rs0 = rstar_of_x(x0)
    rs_end = rstar_of_x(X_HOR)
    n = int(math.ceil((rs0 - rs_end) / H))
    h = -(rs0 - rs_end) / n
    rs = rs0
    x = np.float64(x0)
    psi = np.exp(1j * ws * rs0)
    dpsi = 1j * ws * psi
    keep_rs, keep_x, keep_psi = [], [], []

    def V_of_x(xx):
        return (xx / (xx + 2.0)) * ll / (xx + 2.0) ** 2

    def dx(xx):
        return xx / (xx + 2.0)

    for i in range(n):
        # x at the stage points (scalar, shared by all w)
        k1x = dx(x)
        x2 = x + 0.5 * h * k1x
        k2x = dx(x2)
        x3 = x + 0.5 * h * k2x
        k3x = dx(x3)
        x4 = x + h * k3x
        k4x = dx(x4)
        V1, V2, V4 = V_of_x(x), V_of_x(x2), V_of_x(x4)       # V at stage 2 and 3 are the same point in r*
        w2 = ws * ws
        k1p = dpsi;                     k1d = (V1 - w2) * psi
        p2 = psi + 0.5 * h * k1p;       d2 = dpsi + 0.5 * h * k1d
        k2p = d2;                       k2d = (V2 - w2) * p2
        p3 = psi + 0.5 * h * k2p;       d3 = dpsi + 0.5 * h * k2d
        k3p = d3;                       k3d = (V2 - w2) * p3
        p4 = psi + h * k3p;             d4 = dpsi + h * k3d
        k4p = d4;                       k4d = (V4 - w2) * p4
        psi = psi + h / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        dpsi = dpsi + h / 6 * (k1d + 2 * k2d + 2 * k3d + k4d)
        x = x + h / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        rs = rs + h
        if keep_below is not None and rs < keep_below:
            keep_rs.append(rs); keep_x.append(float(x)); keep_psi.append(psi.copy())
    # decompose at the horizon end: psi = A e^{i w r*} + B e^{-i w r*}
    A = 0.5 * (psi + dpsi / (1j * ws)) * np.exp(-1j * ws * rs)
    B = 0.5 * (psi - dpsi / (1j * ws)) * np.exp(1j * ws * rs)
    gamma = 1.0 / np.abs(A) ** 2
    flux_check = np.abs(A) ** 2 - np.abs(B) ** 2      # must be 1 (unit transmitted flux at infinity)
    if keep_below is None:
        return gamma, flux_check, A, B
    keep = (np.array(keep_rs[::-1]), np.array(keep_x[::-1]), np.array(keep_psi[::-1]) / A[None, :])
    return gamma, flux_check, A, B, keep


t0 = time.time()
Gamma = np.zeros((LMAX + 1, NW))
for l in range(1, LMAX + 1):
    g, fc, A, B = integrate_up(l, w)
    Gamma[l] = g
    print(f"l = {l}: Gamma at w = {w[0]:.3f}: {g[0]:.3e}, at w = {w[NW // 2]:.3f}: {g[NW // 2]:.4f}, at w = {w[-1]:.2f}: {g[-1]:.6f}; "
          f"flux conservation max |1 - (|A|^2 - |B|^2)| = {np.abs(1 - fc).max():.1e} ({time.time() - t0:.0f} s)", flush=True)

# checks: the w^4 law at low w for l = 1 (Gamma ~ c w^4), and the geometric-optics limit sum (2l+1) Gamma -> 27 w^2
lo = (w < 0.03)
slope = np.polyfit(np.log(w[lo]), np.log(Gamma[1][lo]), 1)[0]
S = np.sum((2 * np.arange(LMAX + 1) + 1)[:, None] * Gamma, axis=0)
print(f"low-w slope of Gamma_1: {slope:.3f} (theory 4)")
for wi in (0.3, 0.6, 1.0, 1.5):
    i = np.argmin(np.abs(w - wi))
    print(f"  sum (2l+1) Gamma at w = {w[i]:.2f}: {S[i]:.3f}  vs geometric 27 w^2 = {27 * w[i] ** 2:.3f}  (ratio {S[i] / (27 * w[i] ** 2):.3f})")

# the spectrum and the power
planck = 1.0 / np.expm1(8 * math.pi * w)
dNdw = 2.0 * S * planck / (2 * math.pi)
dEdw = w * dNdw
dEdw_geo = 2.0 * 27 * w ** 2 * planck / (2 * math.pi) * w
P = np.trapezoid(dEdw, w); P_geo = np.trapezoid(dEdw_geo, w); Ndot = np.trapezoid(dNdw, w)
P_geo_exact = 27 * math.pi ** 3 * T_H ** 4 / 15
ipk = int(np.argmax(dEdw)); ipk_n = int(np.argmax(dNdw))
print(f"photon power P M^2 = {P:.3e}  (Page 1976: 3.36e-5; geometric-optics blackbody {P_geo:.3e}, exact {P_geo_exact:.3e}; ratio P/P_geo = {P / P_geo_exact:.3f})")
print(f"photon rate  N M   = {Ndot:.3e} per unit time M;  mean photon energy {P / Ndot:.4f} = {P / Ndot / T_H:.2f} T_H")
print(f"energy spectrum peak at w M = {w[ipk]:.3f} = {w[ipk] / T_H:.2f} T_H  (blackbody peak 2.82 T_H = {2.82 * T_H:.3f});  wavelength 2 pi / w = {2 * math.pi / w[ipk]:.1f} M = {math.pi / w[ipk]:.1f} r_s")
print(f"number spectrum peak at w M = {w[ipk_n]:.3f}")
frac = {}
for l in range(1, 5):
    frac[l] = np.trapezoid(w * 2 * (2 * l + 1) * Gamma[l] * planck / (2 * math.pi), w) / P
print("share of the power by multipole: " + ", ".join(f"l={l}: {frac[l] * 100:.1f}%" for l in frac))

# the modes at the peak, l = 1 and 2, kept for r* < 90 (r < ~ 80)
w_pk = float(w[ipk])
modes = {}
for l in (1, 2):
    g, fc, A, B, (krs, kx, kpsi) = integrate_up(l, np.array([w_pk]), keep_below=90.0)
    modes[l] = (krs, kx, kpsi[:, 0], float(g[0]), complex(B[0] / A[0]))
    print(f"mode l = {l} at w = {w_pk:.3f}: Gamma = {g[0]:.4f}, |R|^2 = {abs(B[0] / A[0]) ** 2:.4f}, {krs.size} points kept, r* in [{krs[0]:.1f}, {krs[-1]:.1f}] ({time.time() - t0:.0f} s)")

np.savez(OUT, w=w, Gamma=Gamma, S=S, dNdw=dNdw, dEdw=dEdw, dEdw_geo=dEdw_geo, P=P, Ndot=Ndot, w_peak=w_pk,
         rs1=modes[1][0], x1=modes[1][1], psi1=modes[1][2], gamma1=modes[1][3],
         rs2=modes[2][0], x2=modes[2][1], psi2=modes[2][2], gamma2=modes[2][3])
print(f"wrote {OUT} ({time.time() - t0:.0f} s)")
