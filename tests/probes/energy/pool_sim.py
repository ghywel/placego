"""ENERGY-TRANSFER.md 2.4 in simulation: the pool shot's physics -> per-frame states (JSON) for the render and the reading.

    pool_sim.py <out.json> <roll|stun> [frames=64]

Frame: image px, X right, Y down, Z INTO the table (away from the top-down camera); the table is the image plane and
a ball's cloth contact is at +R Z from its centre. Units px and frames (24 fps), slowed to the field's reach as a
high-speed camera would see it: R = 80, the cue ball at 8 px/frame, mu g = 0.1 px/frame^2.

Physics (Alciatore, TP A.4; standard): the slip at the cloth contact is u = v + omega x (0, 0, R) = v + R (wy, -wx).
Friction -mu g u_hat changes v at -mu g u_hat and omega at (5 mu g / 2R) (u_y, -u_x, 0)_hat, so u shrinks along a
fixed direction at 7/2 mu g and the path is a parabola until u = 0 (rolling; no rolling resistance after). The
ball-ball contact is frictionless and elastic between equal masses: the object ball takes the normal component, the
cue ball keeps the tangential one and its spin. Orientation integrates dq/dt = 1/2 [0, omega] q (image frame).
"""
import json
import math
import sys

import numpy as np

out, shot = sys.argv[1], sys.argv[2]
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 64
R, V0, MUG, T0, SUB = 80.0, 8.0, 0.1, 20, 200
CUT = math.radians(30)                                  # half-ball hit
O = np.array([760.0, 430.0])                            # the object ball at rest
d = np.array([1.0, 0.0])                                 # the cue ball's line
nc = np.array([math.cos(CUT), math.sin(CUT)])           # the line of centres, cue -> object
contact = O - 2 * R * nc                                 # the cue ball's centre at contact


def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


class Ball:
    def __init__(self, p, v, w):
        self.p, self.v, self.w = np.array(p, float), np.array(v, float), np.array(w, float); self.q = np.array([1.0, 0, 0, 0])
        self.moving = True

    def slip(self): return self.v + R * np.array([self.w[1], -self.w[0]])

    def step(self, dt):
        u = self.slip(); us = np.linalg.norm(u)
        if us > 1e-6:
            uh = u / us
            dv = -MUG * uh * dt
            dw = (5 * MUG / (2 * R)) * np.array([uh[1], -uh[0], 0.0]) * dt
            if np.linalg.norm(u + (-3.5 * MUG * uh * dt)) >= us or 3.5 * MUG * dt >= us:     # would overshoot: land on rolling
                self.v = self.v - (2 / 7) * u                                              # the rolling state it reaches
                self.w = np.array([self.v[1] / R, -self.v[0] / R, self.w[2]])
            else:
                self.v = self.v + dv; self.w = self.w + dw
        self.p = self.p + self.v * dt
        om = self.w
        self.q = self.q + 0.5 * qmul(np.array([0.0, *om]), self.q) * dt
        self.q /= np.linalg.norm(self.q)


w_roll = np.array([0.0, -V0 / R, 0.0]) if shot == "roll" else np.zeros(3)   # rolling along +X: R (wy, -wx) = -v
cue = Ball(contact - d * V0 * T0, d * V0, w_roll)
obj = Ball(O, [0, 0], [0, 0, 0]); obj.moving = False
frames, hit, t_s = [], None, None
dt = 1.0 / SUB
t = 0.0
for k in range(NF):
    frames.append({"k": k, "cue": {"p": cue.p.tolist(), "q": cue.q.tolist(), "v": cue.v.tolist(), "w": cue.w.tolist(),
                                   "slip": float(np.linalg.norm(cue.slip()))},
                   "obj": {"p": obj.p.tolist(), "q": obj.q.tolist(), "v": obj.v.tolist(), "w": obj.w.tolist()}})
    for _ in range(SUB):
        if hit is None and np.linalg.norm(obj.p - cue.p) <= 2 * R:
            hit = t
            vn = (cue.v @ nc) * nc
            obj.v = vn.copy(); cue.v = cue.v - vn; obj.moving = True
            cue_slip0 = float(np.linalg.norm(cue.slip()))
            t_s_pred = hit + 2 * cue_slip0 / (7 * MUG)
        before = np.linalg.norm(cue.slip())
        if shot == "roll" or hit is not None:
            cue.step(dt)
        else:                                             # the stun ball arrives with no spin: idealised, no friction before
            cue.p = cue.p + cue.v * dt
        if obj.moving: obj.step(dt)
        if hit is not None and t_s is None and before > 1e-6 and np.linalg.norm(cue.slip()) < 1e-6: t_s = t + dt
        t += dt
ang = lambda v: math.degrees(math.atan2(-v[1], v[0]))   # degrees above the +X line (image Y down)
final = frames[-1]["cue"]["v"]
meta = {"shot": shot, "R": R, "v0": V0, "mug": MUG, "cut_deg": 30, "hit_t": hit, "t_s": t_s, "t_s_pred": t_s_pred,
        "cue_after_hit_deg": ang(frames[int(hit) + 2]["cue"]["v"]) if hit else None, "cue_final_deg": ang(final),
        "obj_deg": ang(frames[-1]["obj"]["v"]), "frames": frames}
json.dump(meta, open(out, "w"))
print(f"{shot}: hit at t {hit:.3f}; rolling again at t {t_s if t_s is None else round(t_s, 2)} (predicted {t_s_pred:.2f}); "
      f"cue ball leaves at {meta['cue_after_hit_deg']:.1f} deg, ends at {meta['cue_final_deg']:.1f} deg; the object ball at {meta['obj_deg']:.1f} deg")
