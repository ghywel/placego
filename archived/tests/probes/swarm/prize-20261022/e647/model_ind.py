# Independence model: P(D(n)<=delta) = prod_{t>delta} F(t), F(t)=P(tau(m)<=t) for m in the same dyadic block.
# (Telescoping: prod_{k>=1} F(k+delta) = prod_{t>=delta+1} F(t).)  Compare predicted vs observed counts per block.
import sys, math
fn = sys.argv[1]
T = {}; D = {}
for line in open(fn):
    parts = line.split()
    tag, j, tot = parts[0], int(parts[1]), int(parts[2])
    h = {int(a): int(b) for a, b in (p.split(':') for p in parts[3:])}
    (T if tag == 'T' else D)[j] = (tot, h)
deltas = [2,3,4,5,6,8,10,12,14]
print("j  |B|  E[tau]  " + "  ".join(f"d{d}:obs/pred" for d in deltas))
for j in sorted(D):
    if j < 6 or j not in T: continue
    tot, h = T[j]
    if tot < 2**j: pass
    tmax = max(h)
    cum = 0; F = {}
    for t in range(0, tmax+1):
        cum += h.get(t, 0); F[t] = cum / tot
    Etau = sum(t*c for t, c in h.items())/tot
    dtot, dh = D[j]
    row = [f"{j:2d} {dtot:>12d} {Etau:6.2f}"]
    for d in deltas:
        logp = sum(math.log(F[t]) for t in range(d+1, tmax+1) if F[t] > 0)
        pred = dtot * math.exp(logp)
        obs = sum(c for dd, c in dh.items() if dd <= d)
        row.append(f"{obs}/{pred:.3g}")
    print("  ".join(row))
