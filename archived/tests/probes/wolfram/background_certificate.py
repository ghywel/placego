#!/usr/bin/env python3
"""bg_certificate.py NAME r s t0 w PERIOD SHIFT: a self-contained periodic-band certificate for the inserted-edge witness's front.
Invariant at time t: X = E at every depth > R*(t) (the front), and the band B(t) = X on depths [b(t), R*(t)+2] is known.
Step: the band at t+1 on [b(t+1), R*(t+1)+2] is computed from the band at t by the masking rule (the deeper input of a
cell is read only when its nearer input is white; the bottom rises by 1 when the bottom cell is black, else by 2); cells
above R*(t)+2 at time t are E by the invariant and are the only extra inputs needed; every computed cell above the new
front must equal E, and nothing deeper than R*(t)+4 can change, since its inputs are all E and E obeys the recurrence.
Closure: B(t0+PERIOD) equals B(t0) shifted by SHIFT in depth, and E is invariant under (depth+SHIFT, time+PERIOD).
Then by induction the front law R*(t+PERIOD) = R*(t)+SHIFT holds for all t >= t0, and the arrival times follow."""
import sys, numpy as np
name = sys.argv[1]; r, s, t0, w, PER, SH = map(int, sys.argv[2:8])
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(st): return tuple(st[j] ^ (st[(j-1) % p] | st[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
def E(j, t): return orbit[(t + s) % q][(j + r) % p]
assert all(E(j + SH, t + PER) == E(j, t) for j in range(2*p) for t in range(2*q)), "E is not invariant under (SHIFT, PERIOD)"
# exact evolution to t0 to obtain the band (prefix autonomy: exact for depths < J - 2t0)
J = 4*t0 + 400
X = np.zeros(J+1, dtype=np.uint8); X[0] = 1
for j in range(1, J+1): X[j] = E(j, 0)
for t in range(t0):
    Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
lim = J + 1 - 2*t0
Dm = np.flatnonzero(np.array([X[j] ^ E(j, t0) for j in range(lim)], dtype=np.uint8)); R0 = int(Dm.max())
band = {j: int(X[j]) for j in range(R0 - w, R0 + 3)}
assert all(X[j] == E(j, t0) for j in range(R0 + 1, lim)), "invariant at t0"
print(f"{name} alignment ({r},{s}): t0={t0} front {R0} band depths {R0-w}..{R0+2}")
def step(band, t, R):
    b = min(band); top = max(band)
    def xt(j):
        if j in band: return band[j]
        assert j > top; return E(j, t)
    bn = b + 1 if band[b] == 1 else b + 2
    newtop = top + 2
    nb = {}
    for j in range(bn, newtop + 1):
        m = xt(j - 1); o = 1 if m == 1 else xt(j - 2); nb[j] = xt(j) ^ o
    mism = [j for j in nb if nb[j] != E(j, t + 1)]
    Rn = max(mism) if mism else -1
    assert Rn <= R + 2
    # shrink the top to Rn + 2: every computed cell above Rn equals E (checked), and cells above newtop are E by the recurrence
    nb = {j: v for j, v in nb.items() if j <= Rn + 2}
    return nb, Rn
cur = dict(band); R = R0; fronts = [R0]
for t in range(t0, t0 + PER):
    cur, R = step(cur, t, R); fronts.append(R)
shifted = {j + SH: v for j, v in band.items()}
ok = (cur == shifted) and (R == R0 + SH)
print("  fronts over one period:", fronts)
print("  increments:", [fronts[i+1] - fronts[i] for i in range(PER)], "sum", fronts[-1] - fronts[0])
print("  band returns shifted by", SH, "after", PER, "ticks:", cur == shifted, "| front shifted:", R == R0 + SH)
print("CERTIFICATE", "PASS" if ok else "FAIL")
