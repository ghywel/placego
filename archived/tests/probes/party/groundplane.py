"""The ground plane from the skeleton alone: the camera's tilt, each child's height relative to the camera's height, and
from them a METRIC depth for every standing child -- no depth camera, no calibration object.

A camera at height h_c, pitched down by theta, sees a floor point at horizontal distance D at image row
y - cy = f tan(atan(h_c / D) - theta) ~ f h_c / D - f theta (small angles). A standing child of stature H at the same
distance has an image size s = f c H / D (c = the neck-to-ankle share of stature). So, for ONE child:

    y_foot - cy = (h_c / (c H)) s - f theta          a line in s, slope k = h_c / (c H), intercept -f theta

The slope is one number per child and the intercept one number for the whole camera. Fitted together over many
children moving nearer and further (depth2.npz's rows: every tracked child's raw Vision joints, 30 Hz), on frames
where the child STANDS (both ankles and the neck confident, the torso upright, the knees straight -- a jump or a
crouch takes the feet off the model). Then:
  - the relative statures c H_i = h_c / k_i: a party's children and its grown-ups should separate;
  - the tilt theta = -b / f (f = 962 px: the 12 Pro's 26-mm-equivalent 1x lens on 4:3, 67 deg across -- an estimate);
  - D = f c H / s per frame: the room's depth, per child, in units of h_c.

    groundplane.py   (reads $NP_SCRATCH/party-analysis/depth2.npz, which depth2.py wrote)"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

F = 962.0
a = np.load(pd.NP / "party-analysis" / "depth2.npz")["rows"]
si, tid, t, ruler = a[:, 0], a[:, 1], a[:, 2], a[:, 3]
J = a[:, 7:].reshape(-1, 19, 3)
W, H = 1280, 960
cy = H / 2

conf = lambda j: J[:, j, 2]
ank = (J[:, 17, :2] + J[:, 18, :2]) / 2
neck, root = J[:, 5, :2], J[:, 12, :2]
hipL, hipR, kneeL, kneeR, ankL, ankR = (J[:, j, :2] for j in (13, 14, 15, 16, 17, 18))


def straight(h, k, an):
    u, v = k - h, an - k
    c = (u * v).sum(1) / np.maximum(np.linalg.norm(u, axis=1) * np.linalg.norm(v, axis=1), 1e-6)
    return c > np.cos(np.radians(20))                      # hip-knee-ankle within 20 deg of straight


upright = np.abs(neck[:, 0] - root[:, 0]) < 0.25 * np.abs(root[:, 1] - neck[:, 1])
ok = (np.minimum.reduce([conf(5), conf(12), conf(13), conf(14), conf(15), conf(16), conf(17), conf(18)]) > 0.5) \
    & upright & straight(hipL, kneeL, ankL) & straight(hipR, kneeR, ankR) & (np.abs(ankL[:, 1] - ankR[:, 1]) < 12) \
    & (ank[:, 1] < H - 4)                                  # the feet inside the picture
s = np.linalg.norm(ank - neck, axis=1)
yf = np.maximum(ankL[:, 1], ankR[:, 1]) - cy
print(f"standing frames {ok.sum()} of {len(a)}")

# tracks with enough depth travel to show a slope
keys = si * 1e6 + tid
cand = []
for k in np.unique(keys[ok]):
    m = ok & (keys == k)
    if m.sum() >= 30 and np.percentile(s[m], 90) / np.percentile(s[m], 10) > 1.15:
        cand.append(k)
print(f"children (tracks) with standing frames over a 15%+ range of size: {len(cand)}")

# the joint fit: per-track slope k_i, one intercept b per SESSION (the camera may have moved between them)
sess = sorted(set(int(x // 1e6) for x in cand))
cols = len(cand) + len(sess)
rows_A, rows_y, rows_w = [], [], []
for i, k in enumerate(cand):
    m = ok & (keys == k)
    n = int(m.sum())
    A = np.zeros((n, cols))
    A[:, i] = s[m]
    A[:, len(cand) + sess.index(int(k // 1e6))] = 1.0
    rows_A.append(A)
    rows_y.append(yf[m])
    rows_w.append(np.full(n, 1 / np.sqrt(n)))            # each child counts about equally
A = np.vstack(rows_A)
y = np.concatenate(rows_y)
w = np.concatenate(rows_w)
sol, *_ = np.linalg.lstsq(A * w[:, None], y * w, rcond=None)
res = y - A @ sol
print(f"fit: RMS residual {np.sqrt(np.mean(res ** 2)):.1f} px over {len(y)} frames (the foot row, predicted from size)")
k_i = sol[:len(cand)]
b_s = sol[len(cand):]
for sidx, b in zip(sess, b_s):
    print(f"  session {sidx}: intercept b {b:+.1f} px -> the camera pitched {np.degrees(np.arctan(-b / F)):+.1f} deg "
          f"(down if positive, f = {F:.0f})")
good = k_i > 0
stat = 1 / k_i[good]                                       # c H_i / h_c: stature (neck-to-ankle) in camera heights
print(f"\nrelative statures (neck-to-ankle, in units of the camera's height) of {good.sum()} children: "
      f"p10 {np.percentile(stat, 10):.2f} p50 {np.median(stat):.2f} p90 {np.percentile(stat, 90):.2f}")
hist, edges = np.histogram(stat, bins=np.arange(0.2, 2.01, 0.1))
print("  histogram: " + "  ".join(f"{edges[j]:.1f}-{edges[j + 1]:.1f}:{hist[j]}" for j in range(len(hist)) if hist[j]))
# each child's own line: how well does ONE slope explain its frames?
r2 = []
for i, k in enumerate(cand):
    m = ok & (keys == k)
    pred = k_i[i] * s[m] + b_s[sess.index(int(k // 1e6))]
    r2.append(1 - np.var(yf[m] - pred) / max(np.var(yf[m]), 1e-9))
print(f"per-child R^2 of the foot row on size: p25 {np.percentile(r2, 25):.2f} p50 {np.median(r2):.2f} p75 {np.percentile(r2, 75):.2f}")
# distances in camera heights: D / h_c = F c H / (s h_c) = F / (k s)
D = []
for i, k in enumerate(cand):
    m = ok & (keys == k)
    if k_i[i] > 0:
        D.append(F / (k_i[i] * s[m]))
D = np.concatenate(D)
print(f"standing children's distance, in camera heights: p10 {np.percentile(D, 10):.2f} p50 {np.median(D):.2f} "
      f"p90 {np.percentile(D, 90):.2f} (x the tripod's height gives metres)")
np.savez_compressed(pd.NP / "party-analysis" / "groundplane.npz", k=k_i, b=b_s, stat=stat, D=D)
