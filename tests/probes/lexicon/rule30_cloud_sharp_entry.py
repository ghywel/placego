#!/usr/bin/env python3
"""rule30_cloud_sharp_entry.py: SE, GC913's backward pair formulas, and which PHYSICAL odd zero returns are one-parity.

RUN-ON:     cpu, one core (Python 3 standard library); about 15 s
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_sharp_entry.py

Why. GC909 and GC911 (second-read by Local, L514, and Cloud, CL132) show that a doubling entry is sharp, wt(f) = q/4,
exactly when its odd source (a, 0) is supported on one temporal parity. GC911 left OPEN whether physical odd zero
returns of least period >= 4 can be one-parity; GC912 and GC913 closed two backward shortcuts for excluding them. This
probe second-reads GC913's eight-step formulas by replay, then simply looks: which zero-driver ends of the physical tree
(ZF, rule30_cloud_zero_first_roots.py, q <= 16; Proposition 8) and which q = 32 drivers recorded in rule30_tm6b.c's
certificate (Proposition 10: 72 branches, 56 exits) are one-parity?

Record searched: "one.parity|single parity|one temporal parity" with "physical|87,?867|single cell" -> 20 hits, all
GC909 .. GC913 and the Q7 board note "physical one-parity source exclusion remains OPEN"; no physical example.

PREDICTIONS, written 2026-10-10 01:25 BST (Cloud, scratch copy first; CL134), before any of these was run or read:
  X1 (0.95): GC913's B^5 .. B^8 formulas hold for every nonzero one-parity a at q = 8, 16 (30, 510 words) and for
             3,000 random one-parity words at q = 32; B^8's first profile meets both parities exactly when a != S^2 a.
  X2 (0.7): no zero-driver end (x, 0) of the physical tree at q <= 16 has x on one parity, except period-2 words.
  X3 (0.6, the unexpected check): none of TM6b's q = 32 exit or branch drivers is one-parity.
  Counterfactual. A one-parity physical end of least period >= 4 would refute the hoped-for exclusion and, by
  GC911, make the next doubling entry sharp.
OUTCOME, 2026-10-10 01:26 BST: X1 HELD, X2 REFUTED, X3 HELD.
  - X2's exception is a single class: the q = 16 odd end x = 1010100010100000 (time order; weight 5, least period
    16, all ones at even times). It is the end of the chain from (0, 0010110101101111) at depth 58,288, length
    29,580, so (x, 0) is at depth 87,867: Proposition 8's least N_5, "attained only by the single cell's own
    history". So the single cell's own entry to period 32 has a one-parity odd source.
  - Post hoc, checked by separately written code (low bit = time 0, no ZF import): (x, 0) reaches (0, 0) under B in
    exactly 87,867 steps at q = 16, and so does its doubled lift at q = 32. At q = 32 both integration children give
    wt(f) = 8 = q/4. The single cell's period-32 entry is sharp, GC911's equality case.
  - X3: none of the 72 branch drivers or 56 exit drivers at q = 32 is one-parity (controls: every exit driver has odd
    weight, every branch driver even). So no recorded physical entry to period 64 is sharp.
  - Reading. The exclusion GC911 hoped for is false as a universal statement (least period 16 has a physical
    one-parity odd return). The equality case is rare in the recorded data: 1 of the 16 entries to period 32, none of
    the 56 recorded entries to period 64. That it is the shortest history is noted, not explained (one example).
"""
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_cloud_zero_first_roots as zf                    # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def masks(q):
    M = (1 << q) - 1
    even = sum(1 << t for t in range(0, q, 2))
    return M, even, M ^ even


def one_parity(x, q):
    M, even, odd = masks(q)
    return x != 0 and ((x & even) == 0 or (x & odd) == 0)


def least_period(x, q):
    M = (1 << q) - 1
    for k in range(1, q + 1):
        if q % k == 0 and ((((x >> k) | (x << (q - k))) & M) if k < q else x) == x:
            return k
    return q


def check_gc913(q, words):
    """Low bit = time 0; S x (t) = x(t + 1); B(x, y) = (S y + (x OR y), x)."""
    M, even, odd = masks(q)

    def S(x, k=1):
        return (((x >> k) | (x << (q - k))) & M) if k % q else x

    def B(x, y):
        return (S(y) ^ (x | y), x)
    ok = True
    for a in words:
        st, seq = (a, 0), []
        for _ in range(8):
            st = B(*st)
            seq.append(st)
        d, h, r = a ^ S(a, 2), a | S(a, 2), a & ~S(a, 2) & M
        want = [(h ^ S(a), d), (h ^ S(a, 3), h ^ S(a)), (r, h ^ S(a, 3)), (h ^ S(a, 4) ^ S(r), r)]
        ok = ok and seq[3] == (d, a) and seq[4:] == want
        f = seq[7][0]
        ok = ok and (((f & even) != 0 and (f & odd) != 0) == (a != S(a, 2)))
        if a == S(a, 2):
            ok = ok and seq[7] == (0, 0)
    return ok


def b_steps_to_zero(x, y, q, cap=10 ** 7):
    M = (1 << q) - 1
    n = 0
    while (x, y) != (0, 0) and n < cap:
        x, y = ((y >> 1) | ((y & 1) << (q - 1))) & M ^ (x | y), x
        n += 1
    return n if (x, y) == (0, 0) else None


def entry_weights(src, q):
    """wt(f) along (a, 0) -> (0, c) -> (c, 1) -> (1, e) -> (e, f), for each integration child c (low bit = time 0)."""
    M = (1 << q) - 1

    def bit(v, t):
        return (v >> t) & 1

    def children(a, b):
        out = []
        for c0 in (0, 1):
            c, ct = c0, c0
            for t in range(q - 1):
                ct = bit(a, t) ^ (bit(b, t) | ct)
                c |= ct << (t + 1)
            if (bit(a, q - 1) ^ (bit(b, q - 1) | ct)) == c0:
                out.append(c)
        return out
    ws = []
    for c in children(src, 0):
        (one,) = children(0, c)
        (e,) = children(c, one)
        (f,) = children(M, e)
        ws.append(bin(f).count('1'))
    return ws


def main():
    x1 = True
    for q in (8, 16):
        M, even, odd = masks(q)
        words = [a for a in range(1, M + 1) if one_parity(a, q)]
        x1 = x1 and check_gc913(q, words)
    rng = random.Random(913)
    M, even, odd = masks(32)
    words = [(rng.getrandbits(32) & (even if rng.random() < 0.5 else odd)) or even for _ in range(3000)]
    x1 = x1 and check_gc913(32, words)
    print('X1 (GC913 formulas, q = 8, 16 all, q = 32 sampled): %s' % ('HELD' if x1 else 'REFUTED'))
    hits = []
    for q in (2, 4, 8, 16):
        for r in zf.chains(q):
            x = r[4]
            if one_parity(x, q) and least_period(x, q) > 2:
                hits.append((q, format(x, '0%db' % q), r[2] + r[3] - 1, r[5]))
    print('X2 (no one-parity physical end beyond period 2, q <= 16): %s; exceptions (q, x in time order, depth of '
          '(x, 0), weight): %s' % ('HELD' if not hits else 'REFUTED', hits))
    cert = open(os.path.join(HERE, 'rule30_tm6b.c')).read().split('CERTIFICATE', 1)[1].split('LIVE at the stop', 1)[0]
    br = [int(m) for m in re.findall(r'\d+:\d+>\d+:(\d+)', cert)]
    ex = [int(m) for m in re.findall(r'\d+:\d+:(\d+)', cert.split('EXITS', 1)[1])]
    ctrl = len(br) == 72 and len(ex) == 56 and all(bin(x).count('1') % 2 for x in ex) and \
        all(bin(x).count('1') % 2 == 0 for x in br)
    one = [x for x in br + ex if one_parity(x, 32)]
    print('X3 (no one-parity q = 32 driver among %d branches, %d exits; parse/parity control %s): %s' % (
        len(br), len(ex), 'PASS' if ctrl else 'FAIL', ('HELD' if not one else 'REFUTED %s' % one) if ctrl
        else 'NOT DECIDED'))
    for (q, w, depth, wt) in hits:
        x = sum(int(ch) << t for t, ch in enumerate(w))         # time order -> low bit = time 0
        print('  check %s: B-steps to zero at q = %d: %s; at 2q: %s; wt(f) at 2q for both children: %s (q/2 = %d)' % (
            w, q, b_steps_to_zero(x, 0, q), b_steps_to_zero(x | (x << q), 0, 2 * q), entry_weights(x | (x << q), 2 * q),
            q // 2))


if __name__ == '__main__':
    main()
