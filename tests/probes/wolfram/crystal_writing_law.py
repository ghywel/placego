#!/usr/bin/env python3
"""crystal_writing_law.py LOG2T K: the crystal's writing law (inquisition round 14, third block; Cloud, CL693). Left-frame system
(bit k of the big integer row = left wheel k). Cycles C_k (period dividing 16) read from the last 64 rows; settling time tau_k = 1 +
the last t with D_k(t) != C_k(t mod 16). Checks (predictions in the tracker): W1 C_k = F(C_(k-1), C_(k-2)) with F the unique periodic
solution of d(t+1) = w(t) ^ (u(t) | d(t)); W1b the all-white wheels and the integrals after them; W2 the band edge's decider equals
the table; W3 tau_k against the cascade formula; W4 B(t) = min{k : tau_k > t}; W5 pair repeats and distinct words; W6 white wheels.
Output: crystal_writing_law.out."""
import sys, numpy as np, collections
L2T, K = int(sys.argv[1]), int(sys.argv[2]); T = 1 << L2T; P = 1024; KB = K + 8; MASK = (1 << (T + P + 80)) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rows = []; V = 1
for t in range(T + P + 2): rows.append(V); V = stp(V)
def bit(t, k): return (rows[t] >> k) & 1 if k >= 0 else 0
# cycles from the last 64 rows: C[k][r] = D_k at the latest t <= T with t % 16 == r; confirmed over 4 periods
C = np.zeros((KB, 16), dtype=np.uint8); settled_by_end = np.ones(KB, dtype=bool)
late = {}
for r in range(16):
    tr = T - ((T - r) % 16)      # largest t <= T with t % 16 == r
    for m in range(4):
        t = tr - 16 * m; b = np.unpackbits(np.frombuffer((rows[t] & ((1 << KB) - 1)).to_bytes((KB + 7) // 8 + 1, "little"), dtype=np.uint8), bitorder='little')[:KB]
        if m == 0: C[:, r] = b
        else: settled_by_end &= (b == C[:, r])
Ks = int(np.flatnonzero(~settled_by_end).min()) if (~settled_by_end).any() else KB
print(f"T={T}, wheels to K={K}: cycles consistent over the last 4 periods for all wheels below {Ks}; using wheels < {min(K, Ks)}")
K = min(K, Ks)
# settling times tau_k: scan rows backwards against the cycle rows
cyc_rows = [sum(int(C[k, r]) << k for k in range(K)) for r in range(16)]
kmask = (1 << K) - 1
tau = np.full(K, -1, dtype=np.int64); unseen = kmask
for t in range(T, -1, -1):
    mism = (rows[t] ^ cyc_rows[t % 16]) & unseen
    while mism:
        low = mism & -mism; k = low.bit_length() - 1; tau[k] = t + 1; unseen &= ~low; mism &= ~low
    if not unseen: break
for k in range(K):
    if tau[k] < 0: tau[k] = 0
# W1: the writing law
def F(u, w):
    u = [int(x) for x in u]; w = [int(x) for x in w]
    blacks = [r for r in range(16) if u[r] == 1]
    if not blacks: return None
    d = [None] * 16; r0 = blacks[0]; d[(r0 + 1) % 16] = 1 - w[r0]
    r = (r0 + 1) % 16
    for _ in range(16):
        nr = (r + 1) % 16; d[nr] = w[r] ^ (u[r] | d[r]); r = nr
    # consistency around the cycle: recompute once more and compare
    d2 = d[:]
    for _ in range(16):
        nr = (r + 1) % 16; d2[nr] = w[r] ^ (u[r] | d2[r]); r = nr
    return tuple(d) if d == d2 else ("INCONSISTENT", tuple(d), tuple(d2))
w1_ok = w1_bad = 0; white = []; w1b = []
for k in range(2, K):
    u, w, c = C[k - 1], C[k - 2], tuple(int(x) for x in C[k])
    if not u.any():
        white.append(k - 1); par = int(w.sum()) % 2
        # integrals of w: d(t+1) = d(t) ^ w(t): two solutions if parity even
        d0 = [0] * 16
        for r in range(15): d0[r + 1] = d0[r] ^ int(w[r])
        d1 = [1 - x for x in d0]
        w1b.append((k - 1, par, c == tuple(d0) or c == tuple(d1)))
        continue
    f = F(u, w)
    if f == c: w1_ok += 1
    else: w1_bad += 1
print(f"W1 writing law C_k = F(C_(k-1), C_(k-2)) over settled wheels 2..{K-1} with a black in u: {w1_ok} agree, {w1_bad} disagree")
print(f"W6 all-white wheels below {K}: {white}")
print(f"W1b at the white wheels (wheel, parity of w over the period, next cycle is one of the two integrals): {w1b}")
# W2: the band edge's decider is the table
B = {}
for t in range(0, T - P + 1):
    x = rows[t] ^ rows[t + P]; B[t] = (x & -x).bit_length() - 1 if x else 10**9
w2_ok = w2_bad = 0
for t in range(T // 4, T - P + 1):
    k = B[t] - 1
    if 0 <= k < K:
        if bit(t, k) == C[k, t % 16]: w2_ok += 1
        else: w2_bad += 1
print(f"W2 decider D_(B-1)(t) == C_(B-1)(t mod 16) over t in [T/4, T-P]: {w2_ok} agree, {w2_bad} disagree")
# W3: the cascade formula
eq = early = late_ = 0; diffs = collections.Counter()
for k in range(2, K):
    t0 = max(int(tau[k - 1]), int(tau[k - 2])); u = C[k - 1]
    if not u.any(): continue
    t = t0
    while u[t % 16] == 0: t += 1
    that = t + 1
    if tau[k] == that: eq += 1
    elif tau[k] < that: early += 1; diffs[int(that - tau[k])] += 1
    else: late_ += 1; diffs[-int(tau[k] - that)] += 1
print(f"W3 settling time against the cascade formula: equal {eq}, earlier (coincidence) {early}, later (contradiction) {late_}; differences (formula - measured): {dict(sorted(diffs.items())[:12])}")
# W4: the band edge is the settling front
S = {}; kk = 0
for t in range(0, T - P + 1):
    while kk < K and tau[kk] <= t: kk += 1
    S[t] = kk
w4_ok = w4_bad = 0; w4_examples = []
for t in range(T // 4, T - P + 1):
    if S[t] >= K: break
    if B[t] == S[t]: w4_ok += 1
    else:
        w4_bad += 1
        if len(w4_examples) < 5: w4_examples.append((t, B[t], S[t]))
print(f"W4 B(t) == min{{k: tau_k > t}} over t in [T/4, T-P] (while below K): {w4_ok} agree, {w4_bad} disagree; examples {w4_examples}")
# W5: pair repeats and distinct words
words = [int(''.join(str(int(x)) for x in C[k]), 2) for k in range(K)]
pairs = {}; first_repeat = None
for k in range(1, K):
    key = (words[k - 1], words[k])
    if key in pairs and first_repeat is None: first_repeat = (k, pairs[key])
    pairs.setdefault(key, k)
distinct = len(set(words))
print(f"W5 pair repeats among k < {K}: first repeat {first_repeat}; distinct 16-bit words {distinct} of {K} (random-map reference about {K - K*K/2**17:.0f})")
# W5b: the word sequence's own structure: counts of the commonest words and the periods of the cycles
percount = collections.Counter()
for k in range(K):
    c = C[k]
    for per in (1, 2, 4, 8, 16):
        if all(c[r] == c[(r + per) % 16] for r in range(16)): percount[per] += 1; break
print(f"W5b least periods of the cycles among k < {K}: {dict(sorted(percount.items()))}; commonest words {collections.Counter(words).most_common(5)}")
print("CRYSTAL_WRITING_LAW_DONE")
