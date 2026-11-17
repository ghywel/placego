#!/usr/bin/env python3
"""step_entropy.py [LOG2T]: the band edge's step process, its entropy ladder, waiting-time hazard and the boundary pattern's
Markov test (Cloud, CL720, Part A; M4/CL679 has the step law and its one-step memory, Block 26 the speed's k-step closure).

Streaming: the left-frame system V' = (V<<2) XOR ((V<<1) OR V) to T = 2^LOG2T (default 2^18), a 17-row buffer for the lag-16
XOR; B(t) = lowest wheel where rows t and t+16 differ; Delta_t = B(t+1) - B(t) on the trusted window [T/8, T/2]. Certified prefix
(GC2621): wheels agreeing at T-W and T-W+16 (asserted to cover the window's edges plus 8). Reported: the step distribution and
entropy H0; the plug-in conditional entropies H_k = H(Delta_t | Delta_{t-1..t-k}), k = 1..4, with the two-halves gap as the bias
gauge; the waiting-time hazard between heals; the mismatch pattern M_t on wheels B..B+4 (bit 0 always set) and its Markov test
H(M' | M) - H(M' | M, M_prev); the mask-law control."""
import sys, math, time
from collections import Counter, defaultdict, deque
L2T = int(sys.argv[1]) if len(sys.argv) > 1 else 18
T = 1 << L2T; P = 16; W = min(8192, T // 8); T0 = T // 8; TH = T // 2
t0 = time.time()
K = 2 * T + 40; MASK = (1 << K) - 1
buf = deque([1]); V = 1
B = []; rowT = {}
for t in range(0, TH + P + 1 + 0):
    pass
# simulate with a rolling buffer; record B(t) for t <= TH+1, and keep rows T-W and T-W+16 for the certificate
V = 1; rows = deque([V], maxlen=P + 1); Bs = []; keepA = keepB = None
for t in range(0, T - W + P + 1):
    if t - P >= 0 and t - P <= TH + 1:
        x = rows[0] ^ rows[-1]                   # rows[t-P] ^ rows[t]
        Bs.append((x & -x).bit_length() - 1)
    if t == T - W: keepA = V
    if t == T - W + P: keepB = V
    V = ((V << 2) ^ ((V << 1) | V)) & MASK; rows.append(V)
    if t == T - W + P: break
assert keepA is not None and keepB is not None
d = keepA ^ keepB; Kc = (d & -d).bit_length() - 1 if d else K
print(f"T=2^{L2T}, trusted window [{T0}, {TH}], certified 16-periodic prefix wheels 0..{Kc-1} ({time.time()-t0:.1f} s)", flush=True)
B = Bs; assert len(B) >= TH + 2
assert max(B[:TH + 2]) + 8 < Kc, "window edges beyond the certified prefix"
# we need rows t and t+16 again for the pattern/decider; rerun with the buffer, storing only what the window needs
V = 1; rows = deque([V], maxlen=P + 1); dec = []; pat = []
for t in range(0, TH + P + 2):
    if t >= P:
        s = t - P
        if s <= TH + 1:
            b = B[s]; r0 = rows[0]; x = r0 ^ rows[-1]
            dec.append((r0 >> (b - 1)) & 1 if b >= 1 else 0)
            pat.append((x >> b) & 31)
    V = ((V << 2) ^ ((V << 1) | V)) & MASK; rows.append(V)
D = [B[t + 1] - B[t] for t in range(T0, TH + 1)]
n = len(D)
viol = sum(1 for i, t in enumerate(range(T0, TH + 1)) if (D[i] == 0) != (dec[t] == 0))
print(f"mask law: violations {viol} over {n} ticks")
def H(counter):
    tot = sum(counter.values()); return -sum(c / tot * math.log2(c / tot) for c in counter.values())
def cond_entropy(seq, k):
    joint = Counter(); ctx = Counter()
    for i in range(k, len(seq)):
        c = tuple(seq[i - k:i]); joint[(c, seq[i])] += 1; ctx[c] += 1
    tot = len(seq) - k
    return -sum(v / tot * math.log2(v / ctx[c]) for (c, s), v in joint.items())
dist = Counter(D); print("step distribution:", sorted(dist.items()), f"mean {sum(D)/n:.4f}")
print(f"H0 = H(Delta) = {H(dist):.4f} bits")
half = n // 2
for k in range(1, 5):
    hk = cond_entropy(D, k); h1 = cond_entropy(D[:half], k); h2 = cond_entropy(D[half:], k)
    print(f"H_{k} = H(Delta_t | last {k}) = {hk:.4f} bits (halves {h1:.4f}, {h2:.4f}; plug-in bias gauge {(hk - (h1 + h2)/2):+.4f})")
# waiting-time hazard between heals: wait = number of ticks from one heal to the next
waits = []; last = None
for i, dlt in enumerate(D):
    if dlt > 0:
        if last is not None: waits.append(i - last)
        last = i
wc = Counter(waits); tot = len(waits)
print(f"waits between heals: n={tot}, mean {sum(waits)/tot:.3f} (1/P(heal) = {n/sum(1 for d_ in D if d_ > 0):.3f})")
surv = tot; line = []
for w_ in range(1, 9):
    c = wc.get(w_, 0); line.append(f"h({w_})={c/surv:.3f} [n={surv}]"); surv -= c
print("  hazard h(n) = P(next heal at wait n | not before):", "; ".join(line))
# the boundary pattern's Markov test
M = pat; Mk = Counter(M)
print(f"mismatch pattern on B..B+4: {len(Mk)} states seen (bit 0 always set), entropy {H(Mk):.3f} bits")
h1m = cond_entropy(M[T0:TH + 2], 1); h2m = cond_entropy(M[T0:TH + 2], 2)
print(f"  H(M' | M) = {h1m:.4f}, H(M' | M, M_prev) = {h2m:.4f}, gap {h1m - h2m:.4f} bits")
print(f"total {time.time()-t0:.1f} s")
print("STEP_ENTROPY_DONE")
