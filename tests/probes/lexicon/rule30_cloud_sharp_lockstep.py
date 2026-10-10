#!/usr/bin/env python3
"""rule30_cloud_sharp_lockstep.py: SL2, how long sharp doubling entries stay in lockstep, and what breaks it.

RUN-ON:     cpu, one core (Python 3 standard library); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_sharp_lockstep.py

Why. A sharp entry (GC909, GC911) has f on one parity pi with weight q/4. GC917, GC918 and CL138 (second-read by
Local, L520, and GPT, GC919) give closed forms for the next profiles g, h, k, with weights 3q/4, 3q/4, q/2 for every
sharp entry. This probe asks how far that lockstep goes, and what the first differing profile depends on.

Record searched: "sharp" with "fifth|lockstep|profile 5|later profiles" -> 3 hits, none on sharp entries (GC566 is a
channel-cell result); GC917, GC918, CL138 read.

PREDICTIONS, written 2026-10-10 02:14 BST before the run:
  L1 (0.5): at q = 8, 16, 32 all sharp entries share exactly the weights of f, g, h, k and differ at the next profile.
  L2 (0.5): the common weights are multiples of q/4.
  L-U (0.4): the lockstep length grows with q.
OUTCOME, 02:14 BST: L1 HELD at q = 16 and 32 and REFUTED at q = 8, where the 8 sharp entries are one symmetry class
  and agree for all 40 profiles computed; L2 HELD; L-U REFUTED (the same length at q = 16 and 32). The common prefix
  after the profile 1 is e, f, g, h, k with weights q/2, q/4, 3q/4, 3q/4, q/2. The next profile, l, has odd weight in
  [q/4 + 1, q/2 - 1]: 5 or 7 (16 each) at q = 16; 9, 11, 13, 15 (32, 224, 224, 32) at q = 32.
POST HOC (after the outcome; CL143). Write u for f's first-half bits on its parity pi (q/4 of them; the second half is
  their complement, since Tf = f + 1_pi). Let tau(u) be the number of changes around the twisted cycle u_1 .. u_n,
  NOT u_1, which is odd. Then wt(l) = q/4 + tau(u) at q = 16 and 32, exactly, with 2 C(q/4, tau) words per parity.
  By hand, from h = 1 + S^-1 f and k = 1_(pi+1) + S^-1 f + S^-2 f:
  - at t on pi+1, h(t) = k(t), so l(t+1) = (NOT k(t)) AND l(t) = f(t-1) l(t);
  - at t on pi, h(t) = 1, so l(t+1) = NOT (f(t-2) OR l(t)).
  Writing A_s = l(s) on pi, A_(s+2) = f(s) (1 + f(s-2)) (1 + A_s). Rising edges of f along pi are isolated, and
  A_s <= rise(s-2), so A_(s+2) = rise(s); on pi+1, l(s+1) = 1 + f(s-2). Hence
      l = 1_(pi+1) + S^-3 f + S^-2 f (1 + S^-4 f),    wt(l) = q/4 + (rises of f along its parity cycle) = q/4 + tau(u),
  and the literal formula holds on all 4, 8, 32 and 512 sharp entries at q = 4, 8, 16, 32 (last block below).
  PROOF-SKETCH (Cloud), wanting a second reader. Ambient: it says nothing about which sharp entries are physical.
"""
import sys
from collections import Counter
sys.path.insert(0, 'tests/probes/lexicon')
def child(q, x, y):
    M = (1 << q) - 1
    bit = lambda v, t: (v >> (q - 1 - t)) & 1
    t0 = next(t for t in range(q) if bit(y, t))
    bits = [0] * q; cur = 1 - bit(x, t0)
    for k in range(1, q + 1):
        t = (t0 + k) % q
        bits[t] = cur
        cur = bit(x, t) ^ (bit(y, t) | cur)
    c = 0
    for t in range(q): c = (c << 1) | bits[t]
    return c
for q in (8, 16, 32):
    m = q // 2; M = (1 << q) - 1
    bitq = lambda v, t: (v >> (q - 1 - t)) & 1
    ind = lambda par: sum(1 << (q - 1 - t) for t in range(par, q, 2))
    seqs = []
    for blk in range(1, 1 << m):
        if bin(blk).count('1') % 2 == 0: continue
        a = (blk << m) | blk
        if (a & ind(0)) and (a & ind(1)): continue
        for c0 in (0, 1):
            bits = [c0]
            for t in range(q): bits.append(bitq(a, t) ^ bits[t])
            c = 0
            for t in range(q): c = (c << 1) | bits[t]
            prof = [0, c, M]                                     # (0, c) -> child 1
            ws = []
            for _ in range(40):
                if prof[-1] == 0: break
                z = child(q, prof[-2], prof[-1]); prof.append(z); ws.append(bin(z).count('1'))
            seqs.append(ws)
    L = 0
    while all(len(s) > L for s in seqs) and len({s[L] for s in seqs}) == 1: L += 1
    print('q %d: %d sharp entries; common weights for the first %d profiles after 1: %s; at profile %d: %s' % (
        q, len(seqs), L, seqs[0][:L], L + 1, dict(Counter(s[L] for s in seqs if len(s) > L))))
# POST HOC: relate the sixth profile's weight to the half-word u of f (f on parity pi, first-half pi-bits = u).
from collections import defaultdict
for q in (16, 32):
    m = q // 2; M = (1 << q) - 1
    bitq = lambda v, t: (v >> (q - 1 - t)) & 1
    ind = lambda par: sum(1 << (q - 1 - t) for t in range(par, q, 2))
    table = defaultdict(set)
    for blk in range(1, 1 << m):
        if bin(blk).count('1') % 2 == 0: continue
        a = (blk << m) | blk
        if (a & ind(0)) and (a & ind(1)): continue
        for c0 in (0, 1):
            bits = [c0]
            for t in range(q): bits.append(bitq(a, t) ^ bits[t])
            c = 0
            for t in range(q): c = (c << 1) | bits[t]
            prof = [0, c, M]
            for _ in range(6): prof.append(child(q, prof[-2], prof[-1]))
            f, l = prof[4], prof[8]
            pi = 0 if (f & ind(1)) == 0 else 1
            u = [bitq(f, t) for t in range(pi, m, 2)]            # f's first-half bits on its parity
            # candidate statistics, with the twist: the cyclic successor of u's last bit is NOT u's first bit
            ext = u + [1 - u[0]]
            changes = sum(ext[i] != ext[i + 1] for i in range(len(u)))
            table[('changes', changes)].add(bin(l).count('1'))
            table[('weight', sum(u))].add(bin(l).count('1'))
    for key in sorted(table): print('q', q, key, sorted(table[key]))
# POST HOC: the literal closed form l = 1_(pi+1) + S^-3 f + S^-2 f (1 + S^-4 f) on every sharp entry.
for q in (4, 8, 16, 32):
    m = q // 2; M = (1 << q) - 1
    bitq = lambda v, t: (v >> (q - 1 - t)) & 1
    ind = lambda par: sum(1 << (q - 1 - t) for t in range(par, q, 2))
    Sinv = lambda v, k=1: ((v >> k) | (v << (q - k))) & M     # (S^-k v)(t) = v(t - k) in time order
    ok, n = True, 0
    for blk in range(1, 1 << m):
        if bin(blk).count('1') % 2 == 0: continue
        a = (blk << m) | blk
        if (a & ind(0)) and (a & ind(1)): continue
        for c0 in (0, 1):
            bits = [c0]
            for t in range(q): bits.append(bitq(a, t) ^ bits[t])
            c = 0
            for t in range(q): c = (c << 1) | bits[t]
            prof = [0, c, M]
            for _ in range(6): prof.append(child(q, prof[-2], prof[-1]))
            f, l = prof[4], prof[8]
            pi = 0 if (f & ind(1)) == 0 else 1
            want = ind(1 - pi) ^ Sinv(f, 3) ^ (Sinv(f, 2) & (M ^ Sinv(f, 4)))
            ok &= l == want; n += 1
    print('q %d: closed form for the sixth profile holds on all %d sharp entries: %s' % (q, n, ok))
