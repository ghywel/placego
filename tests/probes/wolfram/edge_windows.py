"""edge_windows.py: the seed's edge statistics in matched windows (CL743, after GC2682). The error process of
error_process.py on the seed against its strip at the seed's phase, on 894,236 wheels to the exact settling, with every
quantity of the heal identity read per window of wheels: ticks T, heals D, stays W, A (heals followed by a white parent),
B (stays followed by a black parent), q = B/W, S = A/D, p = D/T, the jump law and P(parent black | jump d); the finite
identity D/T = (q - (H_T - H_0)/T)/(q + S) (GC2682, PROVED two-party) checked in each window; and the same for the
whole run. A window is the stretch of ticks during which the edge lies in [a, a + WIDTH).
Usage: python3 edge_windows.py ROWSDIR [WIDTH]   (the rows of tree16_data.py at 894,236 wheels; A0.bin at phase 0)"""
import sys, time, collections
ROWS = sys.argv[1]; WIDTH = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
A0 = int.from_bytes(open(f"{ROWS}/A0.bin", 'rb').read(), 'little')
K = A0.bit_length(); K = ((K + 7) // 8) * 8 if False else int(sys.argv[3]) if len(sys.argv) > 3 else 894236
MASK = (1 << K) - 1; P = 32
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
cyc = [A0 & MASK]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == cyc[0], "the strip does not return at 32 on these wheels"; cyc = cyc[:P]
class Win:
    def __init__(s): s.T = 0; s.D = 0; s.A = 0; s.B = 0; s.H0 = None; s.HT = None; s.jumps = collections.Counter(); s.pbj = collections.Counter(); s.t0 = None; s.t1 = None
wins = collections.defaultdict(Win); allw = Win()
t0 = time.time(); x = 1; t = 0; m_prev = None; h_prev = None; dec = 0
while True:
    C = cyc[t % P]; e = x ^ C; m = lowbit(e)
    if m >= K: break
    if m_prev is not None and m < m_prev: dec += 1
    h = (C >> (m - 1)) & 1 if m >= 1 else 0           # H_t: the parent black = the edge heals at t -> t+1
    x2 = step(x); C2 = cyc[(t + 1) % P]; e2 = x2 ^ C2; m2 = lowbit(e2)
    h2 = (C2 >> (m2 - 1)) & 1 if 1 <= m2 < K else 0  # H_{t+1}
    for w in (wins[m // WIDTH], allw):
        if w.H0 is None: w.H0 = h; w.t0 = t
        w.T += 1; w.HT = h2; w.t1 = t + 1
        if h:
            w.D += 1; d = m2 - m; w.jumps[d] += 1
            if h2: w.pbj[d] += 1
            else: w.A += 1
        elif h2: w.B += 1
    x = x2; t += 1; m_prev = m
print(f"settled through {K-1} at tick {t}; edge decreases {dec}; {time.time()-t0:.0f} s")
print("window(wheels)      ticks    p=D/T   q=B/W   S=A/D   identity   E[jump]  P(1)   P(2)   P(3)   pb1    pb4    pb5    H0 HT")
def report(name, w):
    Wst = w.T - w.D; q = w.B / Wst; S = w.A / w.D; p = w.D / w.T
    ident = (q - (w.HT - w.H0) / w.T) / (q + S)
    tot = sum(w.jumps.values()); mean = sum(j * v for j, v in w.jumps.items()) / tot
    jl = {j: w.jumps[j] / tot for j in (1, 2, 3)}
    pb = {j: (w.pbj[j] / w.jumps[j] if w.jumps[j] else float('nan')) for j in (1, 4, 5)}
    print(f"{name:16s} {w.T:9d}  {p:.4f}  {q:.4f}  {S:.4f}  {ident:.6f}  {mean:.4f}  {jl[1]:.3f}  {jl[2]:.3f}  {jl[3]:.3f}  {pb[1]:.3f}  {pb[4]:.3f}  {pb[5]:.3f}  {w.H0}  {w.HT}   exact: {abs(ident - p) < 1e-12}")
for k in sorted(wins): report(f"{k*WIDTH}-{min((k+1)*WIDTH, K)-1}", wins[k])
report("all", allw)
