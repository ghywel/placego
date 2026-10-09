#!/usr/bin/env python3
"""rule30_one_hole_widths.py: OH, the one-hole channel layers past width four (PERIOD-TWO.md §6, "The one-hole
channel layers"; CONSTELLATION row 16; GPT G15-G17, G20). Drawn at random by Local under draw-and-work (seed
1791571552, chat L472); predictions pushed before the run.

RUN-ON:     cpu (Python 3); minutes, under 1 GB
COMMAND:    python3 tests/probes/lexicon/rule30_one_hole_widths.py [MAXWIDTH=10]

The model is G20's relaxation, reimplemented with bitmask relations so that widths beyond four are cheap. The wall
column has period p: white at t = 0 mod p, black otherwise. k cells x1 .. xk lie to its right, and the input beyond
xk is free at every step. One step is xj' = left_j XOR (xj OR right_j), with left_1 = the wall and right_k = the
free input. The visible symbol is x1 at each white (hole) time, read before that step. The macro relation is one
white step, then p - 1 black steps. A visible word is allowed when some state and input history realise it. The
subset construction from the full state set decides the language exactly. Reaching the empty set gives a forbidden
word, which is then forbidden for the true wall as well, because the relaxation only adds freedom. A closed graph
with no empty edge proves that every finite and infinite word is allowed at that width and period (G20.2's
argument).
All periods at once: the black relation B is a relation on a finite set, so its powers are eventually periodic,
B^(n + P) = B^n for n >= n0. The macro for p uses B^(p - 1), so the odd periods p from 5 to 1 + n0 + 2P cover every
odd p >= 5. (G20 found n0 = 8 and P = 8 at width four.)

PREDICTIONS (Local's, published before the run):
  OH-C1 (control): widths 1 .. 4 reproduce G15-G17 and G20 exactly:
        - width 4: B^8 = B^16 with GPT's sixteen masks, and every odd p from 5 to 129 has the closed graph I -> (E, H),
          E -> (E, H), H -> (H, H), with E = 59351 and H = 59078;
        - width 2: every even p from 4 to 16 misses 11;
        - p = 3 misses 100 at widths 2 and 4.
  OH-C2 (control): for width 5 and p = 5, 7, the subset language through 8 visible bits equals a direct enumeration
        of state and input paths.
  OH-P1 (blind, confidence 0.7): width 5 still allows every visible word at every odd p >= 5.
  OH-P2 (blind, confidence 0.5): no width from 5 to MAXWIDTH restricts any odd p >= 5.
  OH-P3 (blind, confidence 0.3): the black relation's eventual period is P(k) = 2^(k - 1) at every width tested
        (width 2 has 2 and width 4 has 8).
  OH-P4 (blind, confidence 0.5): the odd-period certificates stay small, at most 8 reachable subsets, through width 8.
  OH-D1 (descriptive): per width, (n0, P), the number of distinct odd-period macro classes, the reachable subset
        counts, and the first forbidden word if any. The same for p = 3 and the even periods 4 .. 16.
OUTCOME, 2026-10-09 19:48 BST (M5, 2.4 s, 29 MB, run at commit 735de69c): OH-C1 PASS, OH-C2 PASS, OH-P1 REFUTED,
  OH-P2 REFUTED, OH-P3 REFUTED, OH-P4 HELD.
  - **Width five is the first restrictive width for every odd p >= 11.** The visible word 01 is forbidden. The black
    relation is eventually periodic from n0 = 11 with period 4, so the classes p = 13 and p = 15 cover every larger
    odd p. p = 11 is forbidden separately.
  - Width six restricts the same periods. Width seven also restricts p = 5 (first forbidden word 10000) and p = 7
    (01111). Width eight also restricts p = 9 (01101). Widths eight to ten restrict every odd p >= 5.
  - So the first restrictive width is exactly 5 for odd p >= 11, 7 for p = 5 and 7, and 8 for p = 9. G20's bound
    (at least 5) is attained.
  - Width 4 reproduces G20 exactly (OH-C1). The black relation's least eventual period there is 4, which is
    consistent with G20's B^8 = B^16.
  - Even p from 4 to 16 and p = 3 stay restricted as before. At widths 5 and up, p = 10 .. 16 first lose 01.
  - P by width, 1 .. 10: 1, 2, 4, 4, 4, 4, 4, 4, 4, 4, so the period-doubling guess P3 was wrong from width 4.
    n0 by width: 2, 3, 5, 8, 11, 14, 19, 20, 28, 29.
  - Every closed certificate had at most 3 reachable subsets (P4).
  - Independent check (scratch, no shared code: the Rule 30 table, every start state and every outside-input
    sequence):
    - the word 01 is ALLOWED at width 4 for p = 11 and 13 (witness start 0100, inputs 00001000000), and at width 5
      for p = 9;
    - it is FORBIDDEN at width 5 for p = 11, 13, 15 and 17, and at width 6 for p = 11.
  - Reading: the relaxation only adds freedom, so any wall 0 1^(p - 1) with odd p >= 11 can never show the hole word 01
    on its right. Once the hole bit is 0, it stays 0.
EXTENSION (registered 2026-10-09 19:52 BST, before running; COMMAND: ... rule30_one_hole_widths.py ext):
  OH-X0 (control): the subset automaton's word counts equal direct enumeration at width 5, p = 11 through 3 bits, and
        at width 7, p = 5 through 6 bits.
  OH-X1 (blind, confidence 0.5): at width 5, every odd p >= 11 has exactly the language 1^a 0^b. That is n + 1 words
        of length n, with the single minimal forbidden word 01.
  OH-X2 (blind, confidence 0.5): that language is unchanged at every width from 6 to 10, for every odd p >= 11.
  OH-X3 (blind, confidence 0.6): at width 10, p = 5, 7 and 9 keep positive entropy: more than 2^(n/2) words at n = 14.
  OH-D2 (descriptive): per width and odd-period class, the word counts for n = 1 .. 14, the minimal forbidden words
        through length 10, and the growth rate (the largest eigenvalue of the subset graph).
"""
import sys
from itertools import product


def step(s, wall, u, k):
    out = 0
    for j in range(k):
        left = wall if j == 0 else (s >> (j - 1)) & 1
        centre = (s >> j) & 1
        right = u if j == k - 1 else (s >> (j + 1)) & 1
        out |= (left ^ (centre | right)) << j
    return out


class Rel:
    """a relation on 2^k states, stored as image bitmasks, applied to sets through byte-chunk tables"""

    def __init__(self, k, img):
        self.k, self.img = k, img
        n = 1 << k
        self.nchunk = (n + 7) // 8
        tab = []
        for c in range(self.nchunk):
            row = [0] * 256
            for v in range(1, 256):
                low = v & -v
                x = c * 8 + low.bit_length() - 1
                row[v] = row[v ^ low] | (img[x] if x < n else 0)
            tab.append(row)
        self.tab = tab

    def apply(self, S):
        out, c = 0, 0
        while S:
            b = S & 255
            if b:
                out |= self.tab[c][b]
            S >>= 8
            c += 1
        return out


def single(k, wall):
    return [(1 << step(s, wall, 0, k)) | (1 << step(s, wall, 1, k)) for s in range(1 << k)]


def black_powers(k, nmax):
    """yield (n, images of B^n), n = 0, 1, ...; B^0 is the identity"""
    B = Rel(k, single(k, 1))
    cur = [1 << s for s in range(1 << k)]
    for n in range(nmax + 1):
        yield n, cur
        cur = [B.apply(x) for x in cur]


def eventual_period(k, nmax=4096):
    seen = {}
    for n, imgs in black_powers(k, nmax):
        key = hash(tuple(imgs))
        if key in seen:
            m = seen[key]
            if dict(black_powers(k, m))[m] == imgs:          # confirm exactly; a hash match alone is not proof
                return m, n - m
        seen[key] = n
    raise RuntimeError('no repeat by %d' % nmax)


def macro(k, Bp):
    W = single(k, 0)
    out = []
    for s in range(1 << k):
        m, img = W[s], 0
        while m:
            low = m & -m
            img |= Bp[low.bit_length() - 1]
            m ^= low
        out.append(img)
    return Rel(k, out)


def graph(k, M):
    n = 1 << k
    full = (1 << n) - 1
    odd = sum(1 << s for s in range(n) if s & 1)
    sel = (full ^ odd, odd)
    queue, seen, edges = [(full, '')], {full}, {}
    for S, w in queue:
        edges[S] = []
        for bit in (0, 1):
            T = M.apply(S & sel[bit])
            edges[S].append(T)
            if T == 0:
                return False, w + str(bit), edges
            if T not in seen:
                seen.add(T)
                queue.append((T, w + str(bit)))
    return True, len(seen), edges


def macros_for_periods(k, ps):
    """macro relations for every p in ps, from one pass over the black powers"""
    want = {p - 1: p for p in ps}
    out = {}
    for n, imgs in black_powers(k, max(want)):
        if n in want:
            out[want[n]] = macro(k, imgs)
    return out


def direct_words(k, p, nbits):
    states = {(s, ()) for s in range(1 << k)}
    for t in range(nbits * p):
        wall = 0 if t % p == 0 else 1
        states = {(step(s, wall, u, k), w + ((s & 1,) if t % p == 0 else ())) for s, w in states for u in (0, 1)}
    return {w for _, w in states}


def subset_words(k, M, nbits):
    n = 1 << k
    full = (1 << n) - 1
    odd = sum(1 << s for s in range(n) if s & 1)
    sel = (full ^ odd, odd)
    paths = {(full, ())}
    for _ in range(nbits):
        paths = {(T, w + (b,)) for S, w in paths for b in (0, 1) for T in [M.apply(S & sel[b])] if T}
    return {w for _, w in paths}


def main():
    maxw = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 10
    ok = True
    # OH-C1
    n0, P = eventual_period(4)
    imgs16 = dict(black_powers(4, 16))
    masks = [imgs16[8][s] for s in range(16)]
    c1 = (masks == [17476, 17472, 1028, 26182, 17492, 26182, 17472, 50372, 17733, 1028, 1024, 50372, 17492, 26182,
                    17472, 17476]) and imgs16[8] == imgs16[16]
    ms = macros_for_periods(4, list(range(3, 130)))
    I = (1 << 16) - 1
    for p in range(5, 130, 2):
        closed, cnt, edges = graph(4, ms[p])
        E, H = edges[I]
        c1 &= closed and cnt == 3 and E == 59351 and H == 59078 and edges == {I: [E, H], E: [E, H], H: [H, H]}
    ms2 = macros_for_periods(2, list(range(3, 17)))
    for p in range(4, 17, 2):
        closed, w, _ = graph(2, ms2[p])
        c1 &= (not closed) and ('11' in w or w == '11') and (1, 1) not in subset_words(2, ms2[p], 2)
    for kk, msx in ((2, ms2), (4, ms)):
        sw = subset_words(kk, msx[3], 3)
        c1 &= (1, 0, 0) not in sw and len(sw) == 7
    print('OH-C1', 'PASS' if c1 else 'FAIL', '(width 4: n0 = %d, P = %d)' % (n0, P), flush=True)
    ok &= c1
    # OH-C2
    ms5 = macros_for_periods(5, [5, 7])
    c2 = all(subset_words(5, ms5[p], 8) == direct_words(5, p, 8) for p in (5, 7))
    print('OH-C2', 'PASS' if c2 else 'FAIL', flush=True)
    ok &= c2
    # widths 1 .. maxw
    res = {}
    for k in range(1, maxw + 1):
        n0, P = eventual_period(k)
        top = 1 + n0 + 2 * P
        odd_ps = list(range(5, top + 1 + (top % 2 == 0), 2))
        want = {p - 1: p for p in [3] + list(range(4, 17, 2)) + odd_ps}
        classes, other = {}, {}
        for n, imgs in black_powers(k, max(want)):          # one table at a time: memory stays small
            if n not in want:
                continue
            p = want[n]
            W = single(k, 0)
            mimg = []
            for st in range(1 << k):
                m, img = W[st], 0
                while m:
                    low = m & -m
                    img |= imgs[low.bit_length() - 1]
                    m ^= low
                mimg.append(img)
            key = tuple(mimg)                               # exact key: no silent hash collision
            if p % 2 and p >= 5:
                if key not in classes:
                    closed, info, _ = graph(k, Rel(k, mimg))
                    classes[key] = (p, closed, info)
            else:
                other[p] = graph(k, Rel(k, mimg))[:2]
        first_bad = [(p, info) for p, closed, info in classes.values() if not closed]
        sizes = sorted({info for p, closed, info in classes.values() if closed})
        p3 = other[3]
        evens = {p: other[p] for p in range(4, 17, 2)}
        res[k] = (n0, P, len(classes), first_bad, sizes)
        print('width %2d: B eventual (n0, P) = (%d, %d); odd p 5 .. %d: %d macro classes; %s; p = 3: %s; even p 4 .. 16: %s'
              % (k, n0, P, odd_ps[-1], len(classes),
                 ('FORBIDDEN at %s' % first_bad) if first_bad else 'all closed, reachable subsets %s' % sizes,
                 'closed (%s subsets)' % p3[1] if p3[0] else 'forbids %s' % p3[1],
                 {p: ('closed %s' % v[1]) if v[0] else ('forbids %s' % v[1]) for p, v in evens.items()}), flush=True)
    if 5 in res:
        print('OH-P1', 'HELD' if not res[5][3] else 'REFUTED %s' % res[5][3])
    w5 = [k for k in range(5, maxw + 1) if k in res]
    bad = [k for k in w5 if res[k][3]]
    print('OH-P2', ('HELD (widths 5 .. %d)' % maxw) if not bad else 'REFUTED at widths %s' % bad)
    p3 = [k for k in res if k >= 2 and res[k][1] != 2 ** (k - 1)]
    print('OH-P3', 'HELD' if not p3 else 'REFUTED at widths %s (P by width: %s)' % (p3, [res[k][1] for k in sorted(res)]))
    big = [k for k in range(5, min(8, maxw) + 1) if k in res and res[k][4] and max(res[k][4]) > 8]
    print('OH-P4', 'HELD' if not big else 'REFUTED at widths %s' % big)
    print('ALL CONTROLS PASS' if ok else 'CONTROL FAILURE: results void')
    print('COMPLETE')


def subset_graph_full(k, M):
    """the whole reachable subset automaton, empty set excluded: nodes and transitions (None marks an empty edge)"""
    n = 1 << k
    full = (1 << n) - 1
    odd = sum(1 << s for s in range(n) if s & 1)
    sel = (full ^ odd, odd)
    nodes, queue, trans = {full: 0}, [full], {}
    for S in queue:
        trans[S] = []
        for bit in (0, 1):
            T = M.apply(S & sel[bit])
            if T and T not in nodes:
                nodes[T] = len(nodes)
                queue.append(T)
            trans[S].append(T if T else None)
    return full, trans


def language(start, trans, nmax):
    counts, layer = [], {start: 1}
    allowed = {0: {''}}
    paths = {('', start)}
    for n in range(1, nmax + 1):
        nxt = {}
        for S, c in layer.items():
            for T in trans[S]:
                if T is not None:
                    nxt[T] = nxt.get(T, 0) + c
        layer = nxt
        counts.append(sum(layer.values()))
        if n <= 10:
            paths = {(w + str(b), T) for w, S in paths for b, T in enumerate(trans[S]) if T is not None}
            allowed[n] = {w for w, _ in paths}
    mfw = []
    for n in range(1, 11):
        for w in (format(i, '0%db' % n) for i in range(1 << n)):
            if w not in allowed[n] and w[1:] in allowed[n - 1] and w[:-1] in allowed[n - 1]:
                mfw.append(w)
    return counts, mfw


def growth(start, trans):
    import numpy as np
    idx = {S: i for i, S in enumerate(trans)}
    A = np.zeros((len(idx), len(idx)))
    for S, ts in trans.items():
        for T in ts:
            if T is not None:
                A[idx[S], idx[T]] += 1
    return max(abs(np.linalg.eigvals(A))) if len(idx) else 0.0


def ext(maxw=10):
    m5 = macros_for_periods(5, [11])
    m7 = macros_for_periods(7, [5])
    x0 = all(len(subset_words(5, m5[11], n)) == len(direct_words(5, 11, n)) for n in range(1, 4)) and \
        all(len(subset_words(7, m7[5], n)) == len(direct_words(7, 5, n)) for n in range(1, 7))
    print('OH-X0', 'PASS' if x0 else 'FAIL', flush=True)
    stair = [n + 1 for n in range(1, 15)]
    x1 = x2 = True
    x3 = None
    for k in range(5, maxw + 1):
        n0, P = eventual_period(k)
        top = 1 + n0 + 2 * P
        ps = list(range(5, top + 1 + (top % 2 == 0), 2))
        want = {p - 1: p for p in ps}
        seen = {}
        for n, imgs in black_powers(k, max(want)):
            if n not in want:
                continue
            p = want[n]
            W = single(k, 0)
            mimg = []
            for st in range(1 << k):
                m, img = W[st], 0
                while m:
                    low = m & -m
                    img |= imgs[low.bit_length() - 1]
                    m ^= low
                mimg.append(img)
            key = tuple(mimg)
            if key in seen:
                seen[key][1].append(p)
                continue
            start, trans = subset_graph_full(k, Rel(k, mimg))
            counts, mfw = language(start, trans, 14)
            seen[key] = ((counts, mfw, growth(start, trans)), [p])
        for (counts, mfw, g), plist in seen.values():
            print('width %2d, odd p %s: counts n = 1 .. 14 %s; growth %.4f; minimal forbidden words (<= 10) %s'
                  % (k, plist if len(plist) < 6 else plist[:5] + ['...'], counts, g, mfw[:12] + (['...'] if len(mfw) > 12 else [])),
                  flush=True)
            if min(plist) >= 11:
                ok = counts == stair and mfw == ['01']
                if k == 5:
                    x1 &= ok
                else:
                    x2 &= ok
            if k == 10 and min(plist) <= 9:
                x3 = (x3 is not False) and counts[13] > 2 ** 7
    print('OH-X1', 'HELD' if x1 else 'REFUTED')
    print('OH-X2', 'HELD' if x2 else 'REFUTED')
    print('OH-X3', 'HELD' if x3 else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    ext() if sys.argv[1:2] == ['ext'] else main()
