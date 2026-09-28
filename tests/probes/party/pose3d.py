"""Apple's 3D body pose at the party (the first two sessions, 2 Hz, 5,260 results): what it knows about depth that the
2D skeleton does not, and whether it can be the depth TEACHER the shaders' questions need (THREEDIMENSIONAL.md 9.8).

Each result: per person, 17 joints in metres from the root (y up) with their image points, the camera's pose in the
root's frame (cameraOrigin, 4x4 column-major), bodyHeight (1.8 m, the reference: no depth camera).

  Q1  the focal length Apple assumes: fitted from its own 3D joints, camera pose and image points (the projection
      conventions tried and the best one kept -- the residual says which is right)
  Q2  does its distance carry anything beyond the 2D skeleton's size? Distance x body ruler (px) should be constant
      for one child if it is scale alone; and the two relative rates, per child
  Q3  limb angles out of the image plane: Apple's 3D bone against the 2D bone-length rule (a limb that looks short
      beside the body has left the plane: tilt = acos(L2D / L2D_max) with the child's own longest L2D as the full
      length) -- the party app's depth-from-bone-length idea, scored against Apple's model

    pose3d.py        -> the tables; rows in $NP_SCRATCH/party-analysis/pose3d.npz"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

J3 = ["human_top_head_3D", "human_center_head_3D", "human_center_shoulder_3D", "human_left_shoulder_3D",
      "human_right_shoulder_3D", "human_left_elbow_3D", "human_right_elbow_3D", "human_left_wrist_3D",
      "human_right_wrist_3D", "human_spine_3D", "human_root_3D", "human_left_hip_3D", "human_right_hip_3D",
      "human_left_knee_3D", "human_right_knee_3D", "human_left_ankle_3D", "human_right_ankle_3D"]
BONES3 = {"upperArmL": ("human_left_shoulder_3D", "human_left_elbow_3D"),
          "forearmL": ("human_left_elbow_3D", "human_left_wrist_3D"),
          "upperArmR": ("human_right_shoulder_3D", "human_right_elbow_3D"),
          "forearmR": ("human_right_elbow_3D", "human_right_wrist_3D"),
          "thighL": ("human_left_hip_3D", "human_left_knee_3D"), "thighR": ("human_right_hip_3D", "human_right_knee_3D")}


def load():
    rec = []
    for si, d in enumerate(pd.sessions()):
        vis = pd.vision(d)
        vt = np.array(sorted(vis))
        for o in pd.jsonl(d, "pose3d"):
            for p in o["people"]:
                if not all(j in p["joints"] and len(p["joints"][j]) == 5 for j in J3):
                    continue
                M = np.array(p["cameraOrigin"], float).reshape(4, 4).T          # column-major -> M[row, col]
                P = np.array([p["joints"][j][:3] for j in J3], float)
                I = np.array([p["joints"][j][3:] for j in J3], float)
                # the same child in Vision's 2D result at that frame (nearest by the image position of the neck)
                k = np.searchsorted(vt, o["t"])
                V = None
                for c in (k - 1, k, k + 1):
                    if 0 <= c < len(vt) and abs(vt[c] - o["t"]) < 0.002:
                        V = vis[vt[c]]
                r2d, v2 = np.nan, None
                if V is not None and len(V):
                    neck3 = I[2]
                    dd = [np.hypot(*(q[5, :2] - neck3)) if q[5, 2] > 0.3 else 1e9 for q in V]
                    q = V[int(np.argmin(dd))]
                    if min(dd) < 60:
                        r2d, v2 = pd.ruler(q), q
                rec.append({"s": si, "t": o["t"], "M": M, "P": P, "I": I, "r2d": r2d, "v2": v2, "size": o["size"]})
        print(f"{d.name}: {len(rec)} 3D people so far", flush=True)
    return rec


def focal(rec):
    """Q1: fit u - cx = f X/Z, v - cy = +-f Y/Z over every joint, for each convention; the best residual wins."""
    best = None
    for name, inv in (("camera pose in the root frame (world->cam = R^T (P - t))", True),
                      ("root->camera transform (cam = R P + t)", False)):
        for zs in (1, -1):
            for ys in (1, -1):
                A, B = [], []
                for r in rec:
                    M = r["M"]
                    R, tt = M[:3, :3], M[:3, 3]
                    Pc = (r["P"] - tt) @ R if inv else r["P"] @ R.T + tt
                    Z = zs * Pc[:, 2]
                    ok = Z > 0.3
                    if ok.sum() < 8:
                        continue
                    w, h = r["size"]
                    A.append(np.r_[Pc[ok, 0] / Z[ok], ys * Pc[ok, 1] / Z[ok]])
                    B.append(np.r_[r["I"][ok, 0] - w / 2, h / 2 - r["I"][ok, 1]])
                if not A:
                    continue
                a, b = np.concatenate(A), np.concatenate(B)
                f = (a @ b) / (a @ a)
                res = np.sqrt(np.mean((b - f * a) ** 2))
                if f > 0 and (best is None or res < best[0]):
                    best = (res, f, name, zs, ys)
    return best


def main():
    rec = load()
    res, f, name, zs, ys = focal(rec)
    w = rec[0]["size"][0]
    print(f"\nQ1 Apple's projection: best convention '{name}' (z sign {zs}, y sign {ys}): f = {f:.0f} px at {w} wide "
          f"(horizontal field of view {2 * np.degrees(np.arctan(w / 2 / f)):.1f} deg), RMS residual {res:.1f} px over the joints")
    # Q2: distance x ruler constancy, per child track (associate by image-position continuity is not stored: use
    # session + nearest in time and image; simpler: pool all and look at the relation's scatter)
    Z = np.array([np.linalg.norm(r["M"][:3, 3]) for r in rec])
    R2 = np.array([r["r2d"] for r in rec])
    ok = np.isfinite(R2) & (R2 > 20)
    prod = Z[ok] * R2[ok]
    print(f"\nQ2 distance x 2D body ruler (should be one constant per child if Apple's distance is scale alone): "
          f"n {ok.sum()}, p10 {np.percentile(prod, 10):.0f} p50 {np.median(prod):.0f} p90 {np.percentile(prod, 90):.0f} m*px; "
          f"corr(1/Z, ruler) {np.corrcoef(1 / Z[ok], R2[ok])[0, 1]:.2f}")
    print(f"   Apple's distances: p10 {np.percentile(Z, 10):.2f} p50 {np.median(Z):.2f} p90 {np.percentile(Z, 90):.2f} m "
          f"(a child of height H is really at about Z x H / 1.8)")
    # Q3: limb tilt from Apple's 3D vs the 2D bone-length rule
    print("\nQ3 limb tilt out of the image plane: Apple's 3D against the 2D bone-length rule")
    rows = []
    for r in rec:
        if r["v2"] is None or not np.isfinite(r["r2d"]):
            continue
        M = r["M"]
        R, tt = M[:3, :3], M[:3, 3]
        Pc = (r["P"] - tt) @ R
        for bname, (ja, jb) in BONES3.items():
            ia, ib = J3.index(ja), J3.index(jb)
            d3 = Pc[ib] - Pc[ia]
            tilt3 = np.degrees(np.arcsin(min(1, abs(d3[2]) / max(np.linalg.norm(d3), 1e-6))))
            a2, b2 = pd.BONES[bname]
            v = r["v2"]
            if min(v[a2, 2], v[b2, 2]) < 0.4:
                continue
            l2 = np.hypot(*(v[b2, :2] - v[a2, :2])) / r["r2d"]
            rows.append((bname, r["s"], l2, tilt3))
    import collections
    by = collections.defaultdict(list)
    for bname, s, l2, t3 in rows:
        by[(bname, s)].append((l2, t3))
    t2s, t3s = [], []
    for key, v in by.items():
        v = np.array(v)
        full = np.percentile(v[:, 0], 95)                  # the child-population's longest look of this bone, per session
        t2 = np.degrees(np.arccos(np.clip(v[:, 0] / full, 0, 1)))
        t2s.append(t2)
        t3s.append(v[:, 1])
    t2, t3 = np.concatenate(t2s), np.concatenate(t3s)
    print(f"   n {len(t2)}: corr {np.corrcoef(t2, t3)[0, 1]:.2f}; Apple tilt p50 {np.median(t3):.0f} deg, 2D-rule tilt p50 {np.median(t2):.0f} deg")
    for lo, hi in ((0, 20), (20, 40), (40, 60), (60, 90)):
        m = (t3 >= lo) & (t3 < hi)
        if m.sum() > 20:
            print(f"   Apple tilt {lo:2}-{hi:2} deg: n {int(m.sum()):5d}  2D-rule tilt p25/p50/p75 "
                  f"{np.percentile(t2[m], 25):4.0f} / {np.percentile(t2[m], 50):4.0f} / {np.percentile(t2[m], 75):4.0f} deg")
    np.savez_compressed(pd.NP / "party-analysis" / "pose3d.npz", Z=Z, R2=R2, t2=t2, t3=t3, f=f)


if __name__ == "__main__":
    main()
