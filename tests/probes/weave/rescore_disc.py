"""ENERGY-TRANSFER.md, lead 4 on a ROTATING print (D4, D5): rescore1.py's step 1c (rescore_cell, the same code) on
the spinning discs of rotwarp.py.

    rescore_disc.py <workdir> <tap.glsl (T2)> [cases=box:weave:11,spin-constant:lattice,spin-pendulum:lattice,spin-constant:noise]

- `box:<tex>:<v>` is the translating box, run through rescore_cell here: an EQUIVALENCE CHECK. It must reproduce
  rescore1.py main()'s own number (weave 11 px/frame: core 98.2 -> 4.9 percent), or this script is not measuring
  step 1c.
- `<scene>:<tex>` is a masters' disc (rotwarp.py's sources: np-scratch/energy/rotwarp/<scene>/src24-<tex>.raw,
  96 frames). The field at index k + 1 is scored for the interval [k, k + 1] (the k + 1 convention). The truth per cell
  is the masters' own chord from k to k + 1, and the core is the disc more than 32 px inside its rim.
Frames 10-58, every fourth. Numbers only.
RESCORE_LATTICE=rival (step 1h) on a weave box also reports, over the core's cells that found offsets: the share with a
raw 1/8 offset within 4 px of a true lattice vector of the print (n (P, P) + m (P, -P), P = 14 or the weave:P given),
and with a refined vector within 1 px of one.
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
work, tap = sys.argv[1], sys.argv[2]
CASES = (sys.argv[3] if len(sys.argv) > 3 else "box:weave:11,spin-constant:lattice,spin-pendulum:lattice,spin-constant:noise").split(",")
sys.argv = [sys.argv[0], work, tap]                               # rescore1's module-level arguments
sys.path.insert(0, str(HERE.parent)); import rescore1 as R1       # noqa: E402
sys.path.insert(0, str(HERE.parents[2])); import masters          # noqa: E402

W, H = R1.W, R1.H
cy_, cx_ = np.mgrid[4:H:8, 4:W:8].astype(np.float64) + 0.5
print(f"{'case':26s} | {'core gross: before -> after':>28s} | changed")
for case in CASES:
    R1.reset_caches()                                                  # no case may read another's cache
    parts = case.split(":")
    if parts[0] == "box":
        tex, v = parts[1], float(parts[2])
        src = pathlib.Path(f"{R1.SRC}/src-{tex}-{v:g}.raw"); n = 48; frames = range(10, 31, 2)
        S = np.fromfile(src, "<u2").reshape(n, H, W).astype(np.float32) / 65535.0
        F = R1.field(src)
        def core_truth(k, u):
            x0 = R1.X0 + v * k
            inbox = (cx_ > x0) & (cx_ < x0 + R1.BW) & (cy_ > R1.Y0) & (cy_ < R1.Y0 + R1.BH)
            dd = np.minimum.reduce([cx_ - x0, x0 + R1.BW - cx_, cy_ - R1.Y0, R1.Y0 + R1.BH - cy_])
            tr = np.zeros_like(u); tr[..., 0] = v
            return inbox, inbox & (dd > 32), tr, F[k]
    else:
        scene, tex = parts
        src = R1.NP / f"energy/rotwarp/{scene}/src24-{tex}.raw"; n = 96                      # rotwarp.py's sources
        frames = range(10, 59, 4)
        S = np.fromfile(src, "<u2").reshape(n, H, W).astype(np.float32) / 65535.0
        F = R1.field(src)
        table = {nm: (kd, p) for nm, kd, p, *_ in masters.masters(W, H)}
        kd, P = table[scene]
        sc = masters.Scene(kd, P, W, H, "textured", tex, 0.0)
        R = P[0]
        def core_truth(k, u):
            ch, _ = sc.chord(float(k), float(k + 1))
            tr = ch[(cy_ - 0.5).astype(int), (cx_ - 0.5).astype(int)]
            r = np.hypot(cx_ - W / 2, cy_ - H / 2)
            return r < R - 8, r < R - 32, tr, F[k + 1]                # the field's k + 1 convention
    tal = [0, 0, 0]; changed = 0; cells = 0
    diag = [0, 0, 0, 0, 0]                                             # cells with offsets, raw near, refined near, two directions, self-match evals
    PW = float(parts[1].split("-")[1]) if parts[0] == "box" and "-" in parts[1] else 14.0
    LV = [np.array([PW * (n + m), PW * (n - m)]) for n in range(-4, 5) for m in range(-4, 5) if (n, m) != (0, 0)]
    near = lambda z, tol: min(np.hypot(*(z - q)) for q in LV) <= tol
    for k in frames:
        region, core, tr, u = core_truth(k, F[k])
        out = u.copy()
        mv = region & (np.hypot(u[..., 0], u[..., 1]) > 0.5)
        for i, j in zip(*np.nonzero(mv)):
            R1.LAST.clear()
            res = R1.rescore_cell(S[k], S[k + 1], u, mv, i, j, cx_[i, j], cy_[i, j])
            if res is not None: out[i, j] = res[0]
            if R1.LAST.get("raw") and core[i, j] and parts[0] == "box" and parts[1].startswith("weave"):
                diag[0] += 1; diag[1] += any(near(z, 4) for z in R1.LAST["raw"]); diag[2] += any(near(z, 1) for z in R1.LAST.get("vec", []))
                vv = R1.LAST.get("vec", []); diag[3] += any(abs(a[0] * b[1] - a[1] * b[0]) > 1e-6 for a in vv for b in vv)
                diag[4] += R1.LAST.get("evals", 0) * R1.LAST.get("taps", 256) / 256
                diag.append(R1.LAST.get("menu", 0))
        e0 = np.hypot(*(u[core] - tr[core]).T); e1 = np.hypot(*(out[core] - tr[core]).T)
        tal[0] += int(core.sum()); tal[1] += int((e0 > 2).sum()); tal[2] += int((e1 > 2).sum())
        changed += int(np.any(out[core] != u[core], axis=-1).sum()); cells += int(core.sum())
    print(f"{case:26s} | {100 * tal[1] / max(tal[0], 1):5.1f}% -> {100 * tal[2] / max(tal[0], 1):5.1f}%{'':13s} | "
          f"{100 * changed / max(cells, 1):5.1f}%"
          + (f" | step 1h: offsets in {diag[0]} core cells; raw within 4 px of the lattice {100 * diag[1] / diag[0]:5.1f}%, "
             f"refined within 1 px {100 * diag[2] / diag[0]:5.1f}%, two directions {100 * diag[3] / diag[0]:5.1f}%, "
             f"{256 * diag[4] / diag[0] / 1000:.1f} thousand self-match fetches per cell, menu {np.mean(diag[5:]):.0f} candidates" if diag[0] else ""), flush=True)
