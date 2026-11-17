#!/usr/bin/env python3
"""L1062: the OR overlap term at the read-out frontier B(P), checked against its hand reduction.

Local, 2026-10-28. For P = 2^v, B(P) is the first right diagonal whose least period does not divide P (GC1998).
Hand claims checked here, on forward cells only:
  H1  B(P) = L(P) + 1, where L(P) is the white run just inside the right edge at time P (Proposition 23).
  H2  p_(B-1) = P, and p_(B-2) is P or P/2.
  H3  overlap parity pi_P(D_(B-1) D_(B-2)) = 1 + w(B-1) + w(B-2) (mod 2), where w(k) is the parity of the 1s in
      P steps of D_k; w(k) = 0 unless p_k = P and D_k did not double at k.
  H4  every term in H3 is a cell on diagonals B-2, B-1 at times 0..P-1, i.e. within B cells of the right edge;
      no centre cell c(n) = D_n(n) with n > B is among them.
Usage: frontier_overlap.py [VMAX]   (default 10, so P <= 1024 and 4P + 2 forward steps)
"""
import sys
VMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
T = 4 * 2**VMAX + 2; OFF = T + 2
x = 1 << OFF; fut = []
for t in range(T + 1):
    fut.append(x); x = (x << 1) ^ (x | (x >> 1))
cell = lambda t, pos: (fut[t] >> (pos + OFF)) & 1
D = lambda d, t: cell(t, t - d)
def period(d):  # least dyadic period of D_d, checked over a full window of length p
    p = 1
    while 2 * p <= T:
        if all(D(d, t) == D(d, t + p) for t in range(0, T - p + 1 - 0)): return p
        p *= 2
    return None
per = {}
d = 0
while True:
    per[d] = period(d)
    if per[d] is None or per[d] > 2**VMAX: break
    d += 1
ok = True
for v in range(2, VMAX + 1):
    P = 2**v
    B = next(k for k in range(1, len(per)) if per[k] is None or P % per[k])
    L = 0
    while cell(P, P - 1 - L) == 0: L += 1
    h1 = (B == L + 1)
    h2 = per[B - 1] == P and per[B - 2] in (P, P // 2)
    pi = lambda f: sum(f(t) for t in range(P)) & 1
    ov = pi(lambda t: D(B - 1, t) & D(B - 2, t))
    w1, w2 = pi(lambda t: D(B - 1, t)), pi(lambda t: D(B - 2, t))
    orp = pi(lambda t: D(B - 1, t) | D(B - 2, t))
    doubled = lambda k: per[k] == 2 * per[k - 1]
    pred_w = lambda k, w: w == 0 if not (per[k] == P and not doubled(k)) else True
    h3 = ov == (1 + w1 + w2) % 2 and orp == 1 and pred_w(B - 1, w1) and pred_w(B - 2, w2)
    ok &= h1 and h2 and h3
    case = "p(B-2)=P/2" if per[B - 2] == P // 2 else "p(B-2)=P"
    print(f"P=2^{v:<2} B={B:<3} L={L:<3} p(B-1)={per[B-1]:<5} {case:<11} OR={orp} overlap={ov} w(B-1)={w1} "
          f"w(B-2)={w2}  H1 {h1} H2 {h2} H3 {h3}")
print("periods:", [per[k] for k in range(len(per))])
print("ALL HOLD" if ok else "FAILURE")
