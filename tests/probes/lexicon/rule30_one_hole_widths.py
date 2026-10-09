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
EXTENSION OUTCOME, 2026-10-09 19:54 BST (M5, seconds, run at commit bbcb1873): OH-X0 PASS, OH-X1 REFUTED, OH-X2
  REFUTED, OH-X3 HELD.
  - Odd p >= 11, every width from 5 to 10: exactly 2 words of every length. The minimal forbidden words are 01 and
    11, so the hole bit is 0 at every hole after the first; the allowed words are 0^n and 1 0^(n - 1).
    - My X1 language 1^a 0^b was too generous, so X1 is refuted. X2 is refuted with it, though the language is the
      same at every width from 5 to 10.
    - One macro step from any state ends with x1 = 0, for any outside input.
  - p = 5, 7 and 9 keep positive entropy at width 10, with growth 1.7335, 1.8814 and 1.8668. Their minimal forbidden
    words begin:
    - p = 5: 10000, then several of length 7;
    - p = 7: 01111, 11111, 011100, 111100;
    - p = 9: 01101, 11101.
    All three are still fully free at widths 5 and 6, and p = 9 also at width 7.
  - Relation to PROOFS.md entry 38 (the black-end walls; method from cochon123/rule30-prize, repaired by GPT,
    replicated by Local).
    - For finite seeds, entry 38 already excludes these walls for q = p - 1 = 7 and q >= 9, that is, p = 8 and
      p >= 10. Its two-sided strip on -6 .. 6 contains this width-5 right relaxation.
    - OH's forcing for odd p >= 11 is the one-sided, seed-free version: it needs no left half and no finiteness.
    - The periods that keep positive entropy here (p = 5, 7, 9, so q = 4, 6, 8) are exactly entry 38's open
      black-end cases among odd p >= 5. Entry 38 marks q = 2 .. 6 and 8 open; p = 3 is the separate 100 case.
    - So, among odd p, the one-sided channel collapses exactly where the two-sided finite-seed exclusion holds, and
      survives exactly where it does not. This is a finite-width observation, not a theorem about all widths.
WIDENING (registered 2026-10-09 20:03 BST, before running; COMMAND: ... rule30_one_hole_widths.py widen [12]):
  Only the three periods left alive, p = 5, 7, 9 (entry 38's open q = 4, 6, 8), at widths 5 .. 12. Growth is the
  exact ratio of word counts at n = 60 and 59, by dynamic programming on the subset automaton. The automaton is capped
  at 300,000 subsets, and a capped case is reported as such, never as a value.
  OH-Y0 (control): at widths 5 .. 10 the growth agrees with the extension's eigenvalues to 3 decimals (2, 2, 2 at 5
        and 6; 1.8724, 1.8832, 2 at 7; and so on to 1.7335, 1.8814, 1.8668 at 10).
  OH-Y1 (blind, confidence 0.7): p = 7 and p = 9 keep growth above 1.85 at widths 11 and 12.
  OH-Y2 (blind, confidence 0.6): p = 5 keeps growth above 1.6 at width 12.
  OH-Y3 (blind, confidence 0.7): no width up to 12 closes any of them (growth 1, as odd p >= 11 have at width 5).
WIDENING OUTCOME, 2026-10-09 20:02 BST (M5, 4.4 s, 160 MB, run at commit 615d58ff): OH-Y0 PASS, OH-Y1 REFUTED,
  OH-Y2 HELD, OH-Y3 HELD.
  Growth at widths 5 .. 12, with the reachable subset counts in brackets:
    p = 5: 2 (5), 2 (7), 1.8724 (20), 1.7489 (31), 1.7489 (38), 1.7335 (54), 1.7033 (93), 1.6950 (147).
    p = 7: 2 (4), 2 (4), 1.8832 (13), 1.8832 (13), 1.8832 (20), 1.8814 (39), 1.8428 (85), 1.8158 (152).
    p = 9: 2 (3), 2 (3), 2 (5), 1.8668 (9), 1.8668 (11), 1.8668 (13), 1.8668 (28), 1.8668 (33).
  - p = 9 is flat from width 8 to 12. p = 5 and p = 7 keep narrowing; p = 7 falls fastest from width 11, which
    refutes Y1.
  - None closes by width 12.
WIDTH 13 (registered 20:02 BST, before running; COMMAND: ... widen 13, the same code; about 0.6 GB):
  OH-Z1 (blind, confidence 0.6): p = 9 stays at 1.8668 at width 13.
  OH-Z2 (blind, confidence 0.6): p = 7 falls again, below 1.8158, but stays above 1.6.
  OH-Z3 (blind, confidence 0.7): p = 5 stays above 1.6.
WIDTH 13 OUTCOME, 2026-10-09 20:03 BST (M5, 22 s, 709 MB peak, run at commit 81ea84ce): OH-Z1 REFUTED, OH-Z2 HELD,
  OH-Z3 HELD.
  - Width 13: p = 5 1.6725 (288 subsets), p = 7 1.7882 (231), p = 9 1.8537 (60). p = 9 left its plateau, so all three
    are now narrowing, and none closes.
  - The rerun printed OH-Y2 at the new largest width (1.6725). That is still above 1.6, but Y2 was registered for width
    12 (1.6950, held).
  - Width 14 would need about 3 GB in this implementation, so it was not run on the M5 tonight. A C or numpy version
    would be needed to go further.
EXACT FORMS (exploratory, after the runs, no predictions; 2026-10-09 20:33 BST, Local; COMMAND: ... closed):
  - Derivation, by hand. A language whose minimal forbidden words are x w, for both x, is "w occurs only as a prefix".
    Its growth equals that of w-avoidance, which is the Guibas-Odlyzko correlation formula, or Goulden-Jackson
    clusters for a set of words.
  - Check. The `closed` mode compares OH's subset automaton with the pattern automaton by a product search: at every
    reachable pair both must be dead or both alive. That proves exact language equality.
  - p = 9, widths 8 .. 12: exactly "1101 only as a prefix".
    - Correlation 1 + z^3. Denominator (1 - 2z)(1 + z^3) + z^4 = 1 - 2z + z^3 - z^4.
    - Growth = the largest root of x^4 - 2x^3 + x - 1 = 1.866760399173861, so 0.90054 bits per hole.
  - p = 7, widths 7 .. 9: exactly "1111 and 11100 only as prefixes".
    - Clusters: C_1111 = -z^4/(1 + z + z^2 + z^3), and 11100 follows 1111 with overlaps 3, 2, 1.
    - The denominator reduces to 1 - z - z^2 - z^3 - z^4 + z^5.
    - Growth = the largest root of x^5 - x^4 - x^3 - x^2 - x + 1 = 1.883203505913524, so 0.91319 bits per hole.
  - Both agree with OH's count ratios to about 1e-15. Equality fails exactly where the measured growth changed (p = 7
    at widths 10 and 11, p = 9 at width 13), which is the negative control.
  - These are exact forms of the relaxed languages, which contain the true wall's language. They are upper bounds on
    the true hole entropy, not its value.
OHC (registered 2026-10-09 20:31 BST, before any width above 13 ran; the C instrument rule30_one_hole_widths.c,
  the same model with sets stepped one update at a time, 128-bit subset keys, and only the frontier kept; caps of 2M
  subsets and 1.5 GB of frontier):
  OHC-C1 (control, already run as the instrument smoke): widths 5, 7, 9, 11 and 13 for p = 5, 7, 9 reproduce OH's
         subset counts exactly and its growth to 1e-6; width 5 p = 11 gives growth 1, and width 4 gives 2. All of
         these held (for example K 13: 288, 231, 60 subsets; growth 1.6725, 1.7882, 1.8537).
  OHC-P1 (blind, confidence 0.6): no width from 14 to 18 closes p = 5, 7 or 9 (growth stays above 1.01).
  OHC-P2 (blind, confidence 0.5): growth keeps falling, and p = 5 is below 1.6 by width 16.
  OHC-P3 (blind, confidence 0.4): p = 9 reaches a new plateau (equal growth at two consecutive widths) somewhere in
         14 .. 18, as it did at 8 .. 12.
  OHC-D1 (descriptive): growth and subset counts per width; how far the caps allow.
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


def widen(maxw=12, cap=300000):
    ext_vals = {5: (2, 2, 2), 6: (2, 2, 2), 7: (1.8724, 1.8832, 2), 8: (1.7489, 1.8832, 1.8668),
                9: (1.7489, 1.8832, 1.8668), 10: (1.7335, 1.8814, 1.8668)}
    y0, res = True, {}
    zs = {}
    for k in range(5, maxw + 1):
        row = []
        for p in (5, 7, 9):
            M = macros_for_periods(k, [p])[p]
            n = 1 << k
            full = (1 << n) - 1
            odd = sum(1 << s for s in range(n) if s & 1)
            sel = (full ^ odd, odd)
            nodes, queue, trans, capped = {full: 0}, [full], {}, False
            for S in queue:
                ts = []
                for bit in (0, 1):
                    T = M.apply(S & sel[bit])
                    if T and T not in nodes:
                        if len(nodes) >= cap:
                            capped = True
                            break
                        nodes[T] = len(nodes)
                        queue.append(T)
                    ts.append(T)
                if capped:
                    break
                trans[S] = ts
            del M
            if capped:
                row.append((p, None, len(nodes)))
                continue
            layer = {full: 1}
            counts = []
            for _ in range(60):
                nxt = {}
                for S, c in layer.items():
                    for T in trans[S]:
                        if T:
                            nxt[T] = nxt.get(T, 0) + c
                layer = nxt
                counts.append(sum(layer.values()))
            g = counts[59] / counts[58] if counts[58] else 0.0
            row.append((p, g, len(nodes)))
        res[k] = row
        print('width %2d: %s' % (k, '; '.join('p = %d: growth %s (%d subsets)' % (p, ('%.4f' % g) if g is not None else 'CAPPED', m)
                                            for p, g, m in row)), flush=True)
        if k in ext_vals:
            y0 &= all(g is not None and abs(g - e) < 0.002 for (p, g, m), e in zip(row, ext_vals[k]))
    print('OH-Y0', 'PASS' if y0 else 'FAIL')
    g = lambda k, p: dict((pp, gg) for pp, gg, mm in res[k])[p] if k in res else None
    y1 = all(g(k, p) is not None and g(k, p) > 1.85 for k in (11, 12) for p in (7, 9) if k in res)
    print('OH-Y1', 'HELD' if y1 else 'REFUTED', [(k, p, g(k, p)) for k in (11, 12) for p in (7, 9) if k in res])
    print('OH-Y2', 'HELD' if (maxw in res and g(maxw, 5) and g(maxw, 5) > 1.6) else 'REFUTED', g(maxw, 5))
    closed = [(k, p) for k in res for p in (5, 7, 9) if g(k, p) is not None and g(k, p) < 1.0001]
    print('OH-Y3', 'HELD' if not closed else 'REFUTED at %s' % closed)
    if 13 in res:
        print('OH-Z1', 'HELD' if abs((g(13, 9) or 0) - 1.8668) < 0.0005 else 'REFUTED', g(13, 9))
        print('OH-Z2', 'HELD' if g(13, 7) and 1.6 < g(13, 7) < g(12, 7) else 'REFUTED', g(13, 7))
        print('OH-Z3', 'HELD' if g(13, 5) and g(13, 5) > 1.6 else 'REFUTED', g(13, 5))
    print('COMPLETE')


def closed():
    """exact language equality between OH's subset automaton and a 'patterns only as a prefix' automaton"""
    def equal(k, p, patterns):
        M = macros_for_periods(k, [p])[p]
        n = 1 << k
        full = (1 << n) - 1
        odd = sum(1 << s for s in range(n) if s & 1)
        sel = (full ^ odd, odd)
        L = max(map(len, patterns))

        def step(d, b):
            cnt, tail = d
            cnt2, tail2 = min(cnt + 1, L + 2), (tail + str(b))[-L:]
            if any(tail2.endswith(w) and cnt2 - len(w) >= 1 for w in patterns):
                return None
            return (cnt2, tail2)
        seen, queue = {(full, (0, ''))}, [(full, (0, ''))]
        for S, d in queue:
            for b in (0, 1):
                S2, d2 = M.apply(S & sel[b]), step(d, b)
                if (S2 == 0) != (d2 is None):
                    return False
                if S2 and (S2, d2) not in seen:
                    seen.add((S2, d2))
                    queue.append((S2, d2))
        return True
    for k in range(8, 13):
        print('p = 9, width %d: language == 1101 only as a prefix: %s' % (k, equal(k, 9, ['1101'])))
    for k in (7, 8, 9):
        print('p = 7, width %d: language == 1111, 11100 only as prefixes: %s' % (k, equal(k, 7, ['1111', '11100'])))
    print('controls (must be False): p = 7 width 10 %s; p = 9 width 13 %s'
          % (equal(10, 7, ['1111', '11100']), equal(13, 9, ['1101'])))


if __name__ == '__main__':
    if sys.argv[1:2] == ['ext']:
        ext()
    elif sys.argv[1:2] == ['closed']:
        closed()
    elif sys.argv[1:2] == ['widen']:
        widen(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
    else:
        main()
