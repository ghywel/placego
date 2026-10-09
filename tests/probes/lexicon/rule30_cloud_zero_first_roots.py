#!/usr/bin/env python3
"""rule30_cloud_zero_first_roots.py: ZF, which zero-first pairs (0, b) of period q are in the physical-root tree.

RUN-ON:     cpu, one core (Python 3 standard library); about 15 s (q = 16 by the chain walk)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_zero_first_roots.py [QMAX=16]

Why. GC903 showed that GPT's q = 4 fibre starts (0, 1110) and (0, 1011) lie on a 28-cycle of the backward pair map
B(a, b) = (S b XOR (a OR b), a), so they are not in the physical tree (G199: a nonzero pair is rooted exactly when
some B iterate reaches (0, 0)). Cloud's replay of GC903 (CL126) found, as its unexpected check, that at q = 4 the
zero-first starts that do reach zero are exactly the 8 words b of even weight. This probe asks whether that is a law.

Method. Every rooted pair is in the in-tree of (0, 0). It is built by breadth-first search on predecessors: B(a, b) =
(a', b') forces a = b', and b solves b(t+1) = a'(t) XOR (b'(t) OR b(t)) around the cycle, so each choice of b(0)
either closes up or not, giving at most two predecessors. Words are written in increasing time, S b(t) = b(t + 1).

Record searched: "even weight|odd weight" with "root|zero|absorb|tree" -> 34 hits, none a characterisation of
rooted zero-first pairs; "rooted" with "q = 4" and "count|states" -> G185, G188, G247, GC571, GC594, none a count.
G199's absorption criterion (B(a, b) = 0 only from the root (0, 1)) is used, not reproved.

PREDICTIONS, written 2026-10-10 00:36 BST, after the q = 4 replay (which is post hoc) and before any other q was run.
  ZF-C1 (control, proved by hand): at odd q the only rooted zero-first pairs are b = 0 and b = 1^q. (A predecessor
         of (1^q, 0) needs S b XOR b = 1^q, which has no solution around an odd cycle, so the tree is (0, 0), (0, 1),
         (1, 1), (1, 0).)
  ZF-C2 (control, from the replay): at q = 4 the rooted zero-first b are the 8 words of even weight, and the tree
         has 98 states; a direct forward check of every state agrees with the BFS.
  ZF-P1 (0.4): at q = 8, (0, b) is rooted exactly when b has even weight (128 of 256).
  ZF-P2 (0.3): the same at q = 16 (32,768 of 65,536), if the BFS finishes.
  ZF-P3 (0.5): at q = 6, the rooted zero-first b are only the four of period dividing 2.
  ZF-U, the unexpected check (0.5): at q = 8 some rooted zero-first pair takes more than 100 steps of B to reach zero.
  Counterfactual. If P1 fails, the q = 4 parity pattern is a small-q coincidence, and GC903's cycle is not part of a
  parity barrier. If P1 holds, an invariant (weight parity of b is the image test b in (1 + S)) is the thing to prove.
OUTCOME for q <= 12, 2026-10-10 00:37 BST (seconds; the predictions were written but not pushed before this run):
  ZF-C1 PASS, ZF-C2 PASS; ZF-P1 REFUTED, ZF-P3 HELD, ZF-U REFUTED; ZF-P2 not yet run.
  - Tree sizes: 4, 14, 98, 3,066 states at q = 1, 2, 4, 8 (depths 3, 8, 29, 400). Every other q <= 12 repeats the tree
    of its largest power-of-2 divisor: 4 at odd q, 14 at q = 6, 10, and 98 at q = 12.
  - At q = 8 only 16 zero-first b are rooted, not 128, so the parity pattern of q = 4 is a small-q coincidence. The
    deepest rooted zero-first pair at q = 8 is 30 steps from zero (U refuted).
  - Post hoc, a sharper pattern: at q = 1, 2, 4, 8 exactly 2q zero-first b are rooted. They are the two constant
    words and one primitive rotation orbit of each period 2^j, j = 1 .. k: 01, 0011, then at q = 8 the orbit of
    00101101.
PREDICTIONS for q = 16, written 2026-10-10 00:37 BST, after the q <= 12 outcome and before q = 16 was run.
  ZF-P4 (0.5): at q = 16 exactly 32 zero-first b are rooted: 0, 1^16 and one primitive orbit of each period 2, 4, 8, 16.
  ZF-P5 (0.6): the q = 16 tree has more than 100,000 states.
  ZF-P2 is expected to be REFUTED (0.95), since the parity law already fails at q = 8.
OUTCOME for q = 16, 2026-10-10 00:45 BST (run at the commit that pushed these predictions, 54b6be6, plus the walker):
  ZF-P2 REFUTED, ZF-P4 REFUTED, ZF-P5 HELD; ZF-C3 (added with the walker, below) PASS.
  - Instrument change, disclosed. The first q = 16 attempt, the full BFS, was stopped by Cloud after 76 s at
    1.3 GB of memory (it shared the container with RR3's kissat calls); nothing was read from it. The chain walk,
    chains(), keeps one rotation class per chain in O(q) memory. Control C3: it equals the BFS tree (size, zero-first
    set, depth) at every q <= 12. Its q = 8 chain, 371 states, is the record's rooted return at 371 (L486).
  - q = 16: 34,541,082 states, depth 894,235, in 9 s. 512 zero-first words are rooted (2q^2, against 2q to q = 8):
    the constants, one class each of period 2, 4, 8, and 31 classes of period 16.
  - The period-16 part is a binary tree. The doubling entry (0, 0000011011111001) at depth 401 walks 52,808 states
    (the record's r = 52,808; RC16's other returns, 18,826 .. 49,732, are not on this tree) to an even return. In all,
    15 period-16 chains end at even returns and branch, and 16 end at odd returns and stop. Those 16 dead ends are the
    seeds of q = 32 (cf. the record's 16 sampled rooted orbits at q = 32, L488).
  - GC904 on physical data (CL127): at every doubling entry for q = 2, 4, 8, 16, f is primitive and q/4 <= wt(f) <= q/2
    (weights 1, 1, 3, 5). At the 30 same-period branch starts of q = 16, which GC904 does not cover, two f have weight
    3 and one has least period 8: the guard and the bound need the entry's antiperiodic structure.
"""
import sys

QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16


def tools(q):
    M = (1 << q) - 1

    def bit(x, t):
        return (x >> (q - 1 - (t % q))) & 1                    # bit t of a word written in increasing time

    def S(b):
        return ((b << 1) | (b >> (q - 1))) & M

    def B(a, b):
        return (S(b) ^ (a | b), a)

    def preds(a2, b2):
        out = []
        for b0 in (0, 1):
            bits = [b0]
            for t in range(q):
                bits.append(bit(a2, t) ^ (bit(b2, t) | bits[t]))
            if bits[q] == b0:
                b = 0
                for t in range(q):
                    b = (b << 1) | bits[t]
                out.append((b2, b))
        return out
    return M, S, B, preds


def tree(q):
    M, S, B, preds = tools(q)
    depth = {(0, 0): 0}
    frontier = [(0, 0)]
    while frontier:
        nxt = []
        for x in frontier:
            for y in preds(*x):
                if y not in depth:
                    depth[y] = depth[x] + 1
                    nxt.append(y)
        frontier = nxt
    return depth


def chains(q, cap=10 ** 9):
    """The same tree, walked as chains, one per rotation class, in O(q) memory (CL127).

    In the predecessor direction a state (a', b') with b' != 0 has the single predecessor (b', c), c its unique child
    (entry 39). A chain from a zero-first state (0, c) runs until the child is 0, at a zero-driver state (x, 0). There
    the tree branches into (0, d) and (0, NOT d), d(t+1) XOR d(t) = x(t), if x has even weight, and stops otherwise.
    Returns, per rotation class of zero-first starts: (start c, least period, depth of (0, c), number of states from
    (0, c) to (x, 0) inclusive, x, weight of x)."""
    M, S, B, preds = tools(q)

    def per(w):
        for k in range(1, q + 1):
            if q % k == 0:
                r = ((w << k) | (w >> (q - k))) & M if k < q else w
                if r == w:
                    return k
        return q

    def canon(w):
        best, r = w, w
        for _ in range(q - 1):
            r = S(r)
            best = min(best, r)
        return best

    def child(a2, b2):
        t0 = next(t for t in range(q) if (b2 >> (q - 1 - t)) & 1)
        bits = [0] * q
        cur = 1 - ((a2 >> (q - 1 - t0)) & 1)                  # the reset: c(t0 + 1) = NOT a'(t0)
        for k in range(1, q + 1):
            t = (t0 + k) % q
            bits[t] = cur
            cur = ((a2 >> (q - 1 - t)) & 1) ^ (((b2 >> (q - 1 - t)) & 1) | cur)
        assert cur == bits[(t0 + 1) % q]
        w = 0
        for t in range(q):
            w = (w << 1) | bits[t]
        return w

    out, todo, seen = [], [(M, 1)], {M}                      # (0, 1^q) at depth 1
    while todo:
        c, dep = todo.pop()
        st, L = (0, c), 1
        while True:
            a2, b2 = st
            z = child(a2, b2)
            st, L = (b2, z), L + 1
            if z == 0 or L > cap:
                break
        x = st[0]
        out.append((c, per(c), dep, L, x, weight(x)))
        if z == 0 and weight(x) % 2 == 0:
            for b0 in (0, 1):
                d, cur = 0, b0
                for t in range(q):
                    d = (d << 1) | cur
                    cur ^= (x >> (q - 1 - t)) & 1
                k = canon(d)
                if k not in seen:
                    seen.add(k)
                    todo.append((k, dep + L))
    return out


def weight(b):
    return bin(b).count('1')


def orbit_classes(words, q):
    """Rotation classes of a set of q-bit words: sorted list of (least period, number of classes)."""
    M, S, _, _ = tools(q)
    left, out = set(words), {}
    while left:
        b = left.pop()
        orb, c = [b], S(b)
        while c != b:
            orb.append(c)
            c = S(c)
        left -= set(orb)
        out[len(orb)] = out.get(len(orb), 0) + 1
    return sorted(out.items())


def from_chains(q, ch):
    """Tree size, rooted zero-first words, deepest zero-first start and tree depth, from the chain walk."""
    M = (1 << q) - 1
    words = set()
    for (c, p, dep, L, x, w) in ch:
        r = c
        for _ in range(q):
            words.add(r)
            r = ((r << 1) | (r >> (q - 1))) & M
    words.add(0)
    size = 1 + sum(p * L for (c, p, dep, L, x, w) in ch)
    return size, sorted(words), max(dep for (c, p, dep, L, x, w) in ch), max(dep + L - 1 for (c, p, dep, L, x, w) in ch)


def main():
    res, c3 = {}, True
    for q in range(1, QMAX + 1):
        if q > 12 and q not in (16,):
            continue
        M = (1 << q) - 1
        ch = chains(q)
        size, zf, maxzf, depth = from_chains(q, ch)
        if q <= 12:                                            # C3: the chain walk against the full BFS
            d = tree(q)
            c3 = c3 and len(d) == size and set(zf) == {b for (a, b) in d if a == 0} and max(d.values()) == depth
        even = [b for b in range(1 << q) if weight(b) % 2 == 0]
        per2 = sorted({b for b in range(1 << q) if (((b << 2) | (b >> (q - 2))) & M) == b}) if q >= 2 else [0, 1]
        res[q] = (size, zf, set(zf) == set(even), per2, maxzf, depth, orbit_classes(zf, q), ch)
        print('q = %2d: tree %d states, depth %d; rooted zero-first b: %d (even-weight law %s; first %s); '
              'deepest zero-first %d' % (q, size, depth, len(zf), 'yes' if set(zf) == set(even) else 'no',
                                         [format(b, '0%db' % q) for b in zf[:6]], maxzf), flush=True)
        print('        rotation classes (least period, number): %s' % res[q][6], flush=True)
    if 16 in res:
        ends = [w % 2 for (c, p, dep, L, x, w) in res[16][7] if p == 16]
        print('q = 16 primitive chains: %d; ending at an even return (branch) %d, at an odd return (dead) %d' % (
            len(ends), ends.count(0), ends.count(1)))
    # C2's forward check at q = 4
    M, S, B, _ = tools(4)
    fw = set()
    for a in range(16):
        for b in range(16):
            x, seen = (a, b), set()
            while x not in seen and x != (0, 0):
                seen.add(x)
                x = B(*x)
            if x == (0, 0):
                fw.add((a, b))
    c1 = all(set(res[q][1]) == ({0, (1 << q) - 1} if q > 1 else {0, 1}) for q in res if q % 2)
    c2 = res[4][2] and res[4][0] == 98 and fw == set(tree(4))
    print('ZF-C1 (odd q: only b = 0, 1^q): %s' % ('PASS' if c1 else 'FAIL'))
    print('ZF-C2 (q = 4 even-weight law, 98 states, forward check agrees): %s' % ('PASS' if c2 else 'FAIL'))
    print('ZF-C3 (chain walk equals the BFS tree for q <= 12): %s' % ('PASS' if c3 else 'FAIL'))
    ok = c1 and c2 and c3
    nd = 'NOT DECIDED'
    print('ZF-P1 (q = 8 even-weight law): %s' % (nd if not ok else ('HELD' if res[8][2] else 'REFUTED')))
    print('ZF-P2 (q = 16 even-weight law): %s' % (nd if not ok or 16 not in res else ('HELD' if res[16][2]
                                                                                       else 'REFUTED')))
    print('ZF-P3 (q = 6: only period-2 b): %s' % (nd if not ok else ('HELD' if res[6][1] == res[6][3] else 'REFUTED')))
    print('ZF-U (q = 8: a zero-first pair deeper than 100): %s' % (nd if not ok else ('HELD' if res[8][4] > 100
                                                                                      else 'REFUTED')))
    if 16 in res:
        want = [(1, 2), (2, 1), (4, 1), (8, 1), (16, 1)]
        print('ZF-P4 (q = 16: 32 rooted zero-first b, one primitive orbit per period 2 .. 16): %s' % (
            nd if not ok else ('HELD' if len(res[16][1]) == 32 and res[16][6] == want else 'REFUTED')))
        print('ZF-P5 (q = 16 tree above 100,000 states): %s' % (nd if not ok else ('HELD' if res[16][0] > 100000
                                                                                   else 'REFUTED')))


if __name__ == '__main__':
    main()
