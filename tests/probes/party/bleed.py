"""The halo on real content: how far a moving limb's motion bleeds into the still background beside it.

The party app's own synthetic check (research/01) found the field "bleeds 12-32 px into the still background around
a moving limb" -- the source of an interpolator's halo. Here on real children: for every whole-field record of the
once-a-second schedule (not the crossing runs), every arm bone of a child standing ALONE (no other person within two
rulers, so the background beside the limb is the still room, whose true motion is zero) moving >= 8 px/frame, the
field is sampled on the line through the bone's midpoint PERPENDICULAR to the bone, at offsets s from -80 to +80 px,
and projected on the bone's own displacement (Vision's), divided by its length: 1 = moves with the limb, 0 = still.
s > 0 is the side the limb moves TOWARD (background about to be covered: occluded in B), s < 0 the side it leaves
(background uncovered, still visible in both frames: its true field is exactly zero).

    bleed.py        the median profile by speed band -> the table; rows -> $NP_SCRATCH/party-analysis/bleed.npz"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

OFFS = np.arange(-80, 81, 4, dtype=float)
ARMS = ["upperArmL", "upperArmR", "forearmL", "forearmR"]


def collect():
    prof, meta = [], []
    for si, d in enumerate(pd.sessions()):
        vis = pd.vision(d)
        vt = np.array(sorted(vis))
        segs = pd.fields(d, "full")
        ts = np.concatenate([m["t"] for m in segs]) if segs else np.array([])
        for m in segs:
            for k in range(len(m)):
                t, iv = float(m["t"][k]), float(m["interval"][k])
                near = np.abs(ts - t)
                if ((near > 1e-6) & (near < 0.5)).any():
                    continue                                   # a crossing run: not here
                def at(want):
                    c = np.searchsorted(vt, want)
                    for x in (c - 1, c, c + 1):
                        if 0 <= x < len(vt) and abs(vt[x] - want) < 0.002:
                            return vis[vt[x]]
                A, B = at(t - iv), at(t)
                if A is None or B is None or not len(A):
                    continue
                uv = np.asarray(m["uv"][k], np.float32)
                H, W = uv.shape[:2]
                cent = [p[5, :2] if p[5, 2] > 0.3 else None for p in A]
                for i, j in pd.match(A, B):
                    r = pd.ruler(A[i])
                    if not np.isfinite(r) or cent[i] is None:
                        continue
                    alone = all(c is None or q == i or np.hypot(*(c - cent[i])) > 2 * r for q, c in enumerate(cent))
                    if not alone:
                        continue
                    for name in ARMS:
                        ja, jb = pd.BONES[name]
                        if min(A[i, ja, 2], A[i, jb, 2], B[j, ja, 2], B[j, jb, 2]) < 0.5:
                            continue
                        pa, pb = A[i, ja, :2], A[i, jb, :2]
                        mid = (pa + pb) / 2
                        dv = ((B[j, ja, :2] + B[j, jb, :2]) - (pa + pb)) / 2
                        spd = np.hypot(*dv)
                        axis = pb - pa
                        L = np.hypot(*axis)
                        if spd < 8 or L < 10:
                            continue
                        nrm = np.array([-axis[1], axis[0]]) / L
                        if nrm @ dv < 0:
                            nrm = -nrm                                  # +s: toward where the limb is going
                        pts = mid[None, :] + OFFS[:, None] * nrm[None, :]
                        ci = np.floor(pts[:, 0] / 2).astype(int)
                        cj = np.floor(pts[:, 1] / 2).astype(int)
                        ok = (ci >= 0) & (ci < W) & (cj >= 0) & (cj < H)
                        f = np.full((len(OFFS), 2), np.nan, np.float32)
                        f[ok] = uv[cj[ok], ci[ok]]
                        proj = (f @ dv) / (spd * spd)
                        prof.append(proj)
                        meta.append((si, t, r, spd, L, abs(nrm @ dv) / spd))
        print(f"{d.name}: {len(prof)} limb profiles so far", flush=True)
    P, M = np.array(prof), np.array(meta)
    np.savez_compressed(pd.NP / "party-analysis" / "bleed.npz", prof=P, meta=M)
    return P, M


def table(P, M):
    si, t, r, spd, L, perp = M.T
    print(f"profiles {len(P)} (isolated children, arm bones moving >= 8 px/frame, once-a-second records)")
    print("offset px:      " + " ".join(f"{o:+4.0f}" for o in OFFS[::2]))
    for lo, hi in ((8, 16), (16, 24), (24, 36)):
        for plabel, pm in (("across", perp > 0.7), ("along", perp < 0.4)):
            m = (spd >= lo) & (spd < hi) & pm
            if m.sum() < 20:
                continue
            med = np.nanmedian(P[m], axis=0)
            print(f"{lo:2}-{hi:<2} px/f {plabel:6} n {int(m.sum()):4d}: " + " ".join(f"{v:4.2f}" for v in med[::2]))
    # the bleed's width: where the median profile falls below 0.5 and 0.1 of the limb's own motion, each side
    m = (spd >= 8) & (spd < 24) & (perp > 0.7)
    med = np.nanmedian(P[m], axis=0)
    rw = np.nanmedian(r[m])
    for side, sel in (("toward (to be covered)", OFFS > 0), ("away (uncovered, truth 0)", OFFS < 0)):
        o, v = np.abs(OFFS[sel]), med[sel]
        order = np.argsort(o)
        o, v = o[order], v[order]
        def reach(level):
            below = np.where(v < level)[0]
            return o[below[0]] if len(below) else np.nan
        print(f"  {side:26}: falls under 0.5 at {reach(0.5):3.0f} px, under 0.1 at {reach(0.1):3.0f} px from the bone "
              f"(ruler p50 {rw:.0f} px; a child's forearm is ~0.2-0.3 ruler wide)")


if __name__ == "__main__":
    p = pd.NP / "party-analysis" / "bleed.npz"
    if "--table" in sys.argv and p.exists():
        z = np.load(p)
        table(z["prof"], z["meta"])
    else:
        table(*collect())
