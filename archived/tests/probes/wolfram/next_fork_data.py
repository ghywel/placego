"""next_fork_data.py: the tree beyond wheel 87,866 (CL736, stage 1). On 165,750 wheels, the single black cell and the rows
A1, B0, B1 of the four-left-sides kit module are evolved to tick 340,000; the final row's return (16, 32 or 64 ticks) gives
the cycle, its words, the white wheels through 165,749 with the parity of the farther word at each (even: a fork, odd: a
doubling, PROOFS Prop. 8), the second child's row at a fork (the top bit complemented), the forced front at phase 0 by the
walk, the lag-32 band edge of each orbit every tick with its crossings of 87,866 and 165,749 and any retreat, and digests of
the phase-0 rows. Predictions P-X1, P-X2 in CL736. Usage: python3 next_fork_data.py"""
import re, sys, time, hashlib
import numpy as np
K = 165750; MASK = (1 << K) - 1; T_END = 340000; LAG = 32; OLD = 87867
SRC = 'reports/wolfram-agents/submissions/four-left-sides/Rule30FourLeftSides.lean'
src = open(SRC).read()
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def literal(name):
    m = re.search(r'^def %s : Nat := (.*?)$' % name, src, re.M); body = m.group(1)
    h = int(re.findall(r'0x[0-9a-fA-F]+', body)[0], 16); sh = re.search(r'<<<\s*(\d+)', body)
    return h << int(sh.group(1)) if sh else h
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
def bits_of(x): return np.unpackbits(np.frombuffer(x.to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
def digest(x): return hashlib.sha256(format(x, 'x').encode()).hexdigest()[:16]
def rot(c, q, P): return ((c >> q) | (c << (P - q))) & ((1 << P) - 1)
def popc(c): return bin(c).count('1')
def minperiod(c, P):
    for q in (1, 2, 4, 8, 16, 32, 64):
        if q >= P: return P
        if rot(c, q, P) == c: return q
def front(words, P, jmax):
    F = [0, 1]
    for j in range(jmax - 1):
        w = words[j + 1]; m = max(F[j], F[j + 1])
        if w == 0: F.append(m); continue
        r = 0
        while not (w >> ((m + r) % P)) & 1: r += 1
        F.append(m + r + 1)
    return F
A0 = literal('A0'); A1 = A0 ^ literal('A1'); B0 = A0 ^ literal('B0'); B1 = B0 ^ literal('B1')
old = {'seed': A0, 'A1': A1, 'B0': B0, 'B1': B1}
starts = [('seed', 1), ('A1', A1), ('B0', B0), ('B1', B1)]
print(f"K = {K} wheels, T_END = {T_END}, lag {LAG}")
results = {}
for name, v in starts:
    t0 = time.time(); ring = [v]; x = v
    cross = {OLD - 1: None, K - 1: None}; retreats = 0; prev = 0; nonzero_after = 0
    for t in range(1, T_END + 1):
        x = step(x); ring.append(x)
        if len(ring) > LAG + 1: ring.pop(0)
        if t >= LAG:
            d = x ^ ring[0]; e = lowbit(d)
            if e < prev: retreats += 1
            prev = e
            for j in cross:
                if cross[j] is None and e > j: cross[j] = t
            if cross[K - 1] is not None and e <= K - 1: nonzero_after += 1
    per = None; its = [x]
    for p in range(1, 65):
        its.append(step(its[-1]))
        if per is None and p in (16, 32, 64) and its[p] == x: per = p
    rows = its[:per]
    bits = np.stack([bits_of(r) for r in rows]).astype(np.int64)        # P x K
    words = (bits * (1 << np.arange(per, dtype=np.int64))[:, None]).sum(axis=0)
    whites = [int(j) for j in np.where(words == 0)[0] if j >= 2]
    print(f"\n{name}: {time.time()-t0:.1f} s; period {per}; low {OLD} bits of the phase-0 row equal the old literal: {x % (1 << OLD) == old[name]}; "
          f"edge crossed 87,866 at tick {cross[OLD-1]}, 165,749 at tick {cross[K-1]}, retreats {retreats}, nonzero lag-{LAG} differences after the last crossing {nonzero_after}")
    print(f"  white wheels through {K-1}: {whites}")
    for w in whites:
        a = int(words[w - 1]); q = minperiod(a, per); par = popc(a & ((1 << q) - 1)) % 2
        c = int(words[w + 1]) if w + 1 < K else None
        kind = ('fork' if par == 0 else 'doubling')
        if c is not None:
            comp = (~c) & ((1 << per) - 1)
            chk = ('child period ' + str(minperiod(c, per)) + ', complement is its rotation by ' + str(q) + ': ' + str(rot(c, q, per) == comp))
        else: chk = 'child beyond the register'
        print(f"  white {w}: farther word period {q}, parity {par} -> {kind}; {chk}")
    F = front([int(w) for w in words], per, K - 1)
    print(f"  forced front at phase 0: F(53207) = {F[53207]}, F(87866) = {F[87866]}, F(165749) = {F[K-1]}; increment over the last 50,000 wheels {(F[K-1]-F[K-1-50000])/50000:.4f} ticks/wheel")
    print(f"  phase-0 row digest (sha256 of hex, first 16) {digest(x)}")
    if per == 32:
        ok1 = all(rows[r + 16] % (1 << OLD) == rows[r] % (1 << OLD) for r in range(16))
        ok2 = all(((rows[r + 16] >> OLD) & 1) != ((rows[r] >> OLD) & 1) for r in range(16))
        print(f"  doubling facts for Lean: rows r+16 = rows r below {OLD}: {ok1}; bit {OLD} flips after 16 ticks: {ok2}")
    results[name] = (x, per, whites, F)
    if (K - 2) in whites:
        x2 = x ^ (1 << (K - 1)); its2 = [x2]
        for p in range(per): its2.append(step(its2[-1]))
        bits2 = np.stack([bits_of(r) for r in its2[:per]]).astype(np.int64)
        words2 = (bits2 * (1 << np.arange(per, dtype=np.int64))[:, None]).sum(axis=0)
        diff = [int(j) for j in np.where(words2 != words)[0]]
        print(f"  fork at {K-2}: second child row = row ^ 2^{K-1}: returns after {per}: {its2[per] == x2}; words differ exactly at {diff}; "
              f"complement at {K-1}: {int(words2[K-1]) == ((~int(words[K-1])) & ((1 << per) - 1))}; digest {digest(x2)}")
print("\ndone")
