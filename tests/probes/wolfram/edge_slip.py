"""edge_slip.py: the anatomy of one clock slip between two walks over the same strip (CL746, GPT's continuation in
GC2683). Two rows on the strip A0 (894,236 wheels): the seed (x = 1, phase 0) and the row damaged above wheel W0 with
random seed DAMAGE (settling on A0 at phase PHASE). Both are evolved to the ticks at which their edges pass wheel J
(tau_J from the saved settling ticks), and for ticks tau_J - BEFORE .. tau_J + AFTER each row's edge m(t), its actual
bits a and the strip's bits C at wheels m-3 .. m+10, and the errors, are printed side by side, each row at its own tick
so that the two edges are compared wheel by wheel. The first tick at which the two edge trajectories (read against
the wheel) differ is marked.
Usage: python3 edge_slip.py ROWSDIR J TAU_SEED.npy TAU_DAMAGED.npy [DAMAGE=11] [W0=64] [PHASE=8] [BEFORE=40] [AFTER=60]"""
import sys, random, numpy as np
ROWS = sys.argv[1]; J = int(sys.argv[2]); ta = np.load(sys.argv[3]); tb = np.load(sys.argv[4])
DAMAGE = int(sys.argv[5]) if len(sys.argv) > 5 else 11; W0 = int(sys.argv[6]) if len(sys.argv) > 6 else 64
PHASE = int(sys.argv[7]) if len(sys.argv) > 7 else 8; BEFORE = int(sys.argv[8]) if len(sys.argv) > 8 else 40; AFTER = int(sys.argv[9]) if len(sys.argv) > 9 else 60
K = 894236; MASK = (1 << K) - 1; P = 32
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
A0 = int.from_bytes(open(f"{ROWS}/A0.bin", 'rb').read(), 'little') & MASK
cyc = [A0]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == A0; cyc = cyc[:P]
rng = random.Random(DAMAGE); xb0 = (A0 ^ ((rng.getrandbits(K) >> W0) << W0 | (1 << W0))) & MASK
def trace(x, t_start, t_end, phase):
    """evolve from tick 0 to t_start, then record ticks t_start..t_end: (t, m, a-bits, C-bits at m-3..m+10)"""
    t = 0
    while t < t_start: x = step(x); t += 1
    out = []
    while t <= t_end:
        C = cyc[(t + phase) % P]; e = x ^ C; m = lowbit(e)
        bits_a = ''.join(str((x >> (m - 3 + i)) & 1) for i in range(14)); bits_c = ''.join(str((C >> (m - 3 + i)) & 1) for i in range(14))
        out.append((t, m, bits_a, bits_c)); x = step(x); t += 1
    return out
ta_J = int(ta[J]); tb_J = int(tb[J])
print(f"wheel {J}: the seed passes it at tick {ta_J}, the damaged row at {tb_J} (offset {tb_J - ta_J}, residue mod 32: {(tb_J - ta_J) % 32})")
A = trace(1, ta_J - BEFORE, ta_J + AFTER, 0); B = trace(xb0, tb_J - BEFORE, tb_J + AFTER, PHASE)
print("tick(seed)  m(seed)  a[m-3..m+10](seed)  C[m-3..m+10]   |  tick(dmg)  m(dmg)  a[m-3..m+10](dmg)  C[m-3..m+10]   | same m? same a-window?")
first = None
for (t1, m1, a1, c1), (t2, m2, a2, c2) in zip(A, B):
    same_m = (m1 == m2); same_a = (a1 == a2)
    if not same_m and first is None: first = t1
    print(f"{t1:9d}  {m1:7d}  {a1}  {c1}   |  {t2:9d}  {m2:7d}  {a2}  {c2}   | {'=' if same_m else 'X'} {'=' if same_a else 'X'}")
print(f"first tick (seed clock) at which the edges differ in this window: {first}")
