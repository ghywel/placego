#!/usr/bin/env python3
"""rule30_cloud_periodic_points.py: recount Epperlein's Table A.1 row for Rule 30 (temporally periodic points).

RUN-ON:     cpu (Python 3 standard library; bit-sliced big integers)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_periodic_points.py [PMAX=10]
COST:       expected under a few minutes at PMAX = 10 (2^21 windows).

Why. Kopra's accepted answer to MathOverflow 429509 (2022-09-01) cites "Table A.1 of
https://core.ac.uk/download/pdf/236376428.pdf" for the number of points of Rule 30 on the full shift with minimal
preperiod q and minimal period p: for q = 0 and p = 1 .. 6, "3,0,12,28,45,84 and in particular there does not exist
a configuration with minimal period 2". The survey (CL085) could not open the PDF (HTTP 403), and its own ring count
confirmed p = 1 .. 4 but only 20 of 45 at p = 5 and 0 of 84 at p = 6 among spatial periods up to 24. The owner found
a copy (2026-10-09). It is Jeremias Epperlein's dissertation, "Topological Conjugacies Between Cellular Automata"
(TU Dresden, defended 2017-04-21; examiners Stefan Siegmund and Jarkko Kari), Appendix A. Its Rule 30 row, read from
the copy (q, p with q + p <= 6):
  minimal preperiod q, minimal period p (Table A.1):
    (0,1..6) 3 0 12 28 45 84; (1,1..5) 1 0 0 14 5; (2,1..4) 3 0 0 21; (3,1..3) 3 0 0; (4,1..2) 6 0; (5,1) 6
  all of Pre_{q,p} = {x : f^q x = f^(q+p) x} (the appendix's fourth table):
    (0,1..6) 3 3 15 31 48 99; (1,1..5) 4 4 16 46 54; (2,1..4) 7 7 19 70; (3,1..3) 10 10 22; (4,1..2) 16 16; (5,1) 22
The record uses the p = 2 zero as a consistency anchor for the period-2 write-up, so it should be recounted here, not
trusted.

Method. Pre_{q,p} is a subshift of finite type: x is in it iff every window w of 2R + 1 cells (R = q + p) has
f^R(w) equal to the centre of f^q(w). All 2^(2R+1) windows are tested at once by bit-slicing; the allowed windows are
the edges of a de Bruijn graph on words of 2R cells. Pruning vertices without a predecessor or a successor leaves the
vertices on bi-infinite paths. The set is finite iff what is left is disjoint cycles, and then each vertex is one
point, a configuration whose spatial period is its cycle's length. Minimal counts follow by Moebius inversion over the
divisors of p and differencing in q. A point is a travelling wave when f(x) is a rotation of x on its cycle.

PREDICTIONS, written 2026-10-09 17:46 BST, before any run of this script.
  PP-C0 (control, 0.9): the recount equals both tables, all 42 entries.
  PP-C1 (control, 0.9): it agrees with the survey's ring count: of the points of minimal period 5, exactly 20 have
         spatial period <= 24; of minimal period 6, none.
  PP-P1 (0.75): Per_p(Rule 30) is finite for every p <= 10.
  PP-P2 (0.5): the counts of minimal period p grow on to p = 10, with the count at p = 10 between 150 and 3000, and
         p = 2 is the only p <= 10 with no point (0.7 for that part alone).
  PP-U, the unexpected check (0.5): for every p from 3 to 10 with points, fewer than half the points of minimal period
         p are travelling waves.
  Counterfactual. If PP-C0 fails, the window encoding or the table is wrong, and the p = 2 anchor is not cited until
  that is settled. If PP-P1 fails, Rule 30 has temporally periodic points that are not spatially periodic, which
  would be new to the record.

OUTCOME of the first run, 2026-10-09 (PMAX = 10; under a minute).
  PP-C0 PASS: all 42 entries of both tables recounted exactly. Rule 30 has no configuration of minimal temporal
    period 2, as Kopra's answer and the thesis say.
  PP-C1 PASS: of the 45 points of minimal period 5, 20 have spatial period <= 24 (5 and 15; the other 25 are one
    25-cell orbit); the 84 points of minimal period 6 are one orbit of spatial period 84.
  PP-P1 HELD: Per_p is finite for every p <= 10.
  PP-P2 PART. Minimal-period counts for p = 1 .. 10: 3, 0, 12, 28, 45, 84, 105, 88, 180, 550 (p = 7 .. 10 are new
    here). p = 10's count is in range and p = 2 is the only empty period, but growth is not monotone (88 < 105).
  PP-U REFUTED (the unexpected check): travelling waves are not rare. All points of minimal period 1, 3, 5 and 6
    are travelling waves (f x a rotation of x), none of periods 4, 7 and 10, and 80 of 88 and 135 of 180 at 8, 9.
  Links to the record (post hoc). The 84 points of minimal period 6 are one orbit up to shift, and it is GC686's
    84-cell all-S ring (its row is a rotation of 0x688eb74a45efb082671ee; 6 of its 84 columns have period 2). So
    that ring is the only Rule 30 configuration of least temporal period 6. Spatial periods at p = 10 are 30, 90
    and 155; the 155 matches the size of the record's all-L ring (not checked to be that ring).
"""
import sys

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10

A1 = {(0, 1): 3, (0, 2): 0, (0, 3): 12, (0, 4): 28, (0, 5): 45, (0, 6): 84, (1, 1): 1, (1, 2): 0, (1, 3): 0,
      (1, 4): 14, (1, 5): 5, (2, 1): 3, (2, 2): 0, (2, 3): 0, (2, 4): 21, (3, 1): 3, (3, 2): 0, (3, 3): 0,
      (4, 1): 6, (4, 2): 0, (5, 1): 6}
PRE = {(0, 1): 3, (0, 2): 3, (0, 3): 15, (0, 4): 31, (0, 5): 48, (0, 6): 99, (1, 1): 4, (1, 2): 4, (1, 3): 16,
       (1, 4): 46, (1, 5): 54, (2, 1): 7, (2, 2): 7, (2, 3): 19, (2, 4): 70, (3, 1): 10, (3, 2): 10, (3, 3): 22,
       (4, 1): 16, (4, 2): 16, (5, 1): 22}


def var_masks(n):
    """masks[i] has bit w set iff bit i of w is set, for every w < 2^n (bit i of w is cell i, left to right)."""
    nbytes = max(1, (1 << n) // 8)
    out = []
    for i in range(n):
        if i < 3:
            pat = bytes([(0xAA, 0xCC, 0xF0)[i]]) * nbytes
        else:
            b = 1 << (i - 3)
            pat = (b'\x00' * b + b'\xff' * b) * (nbytes // (2 * b))
        out.append(int.from_bytes(pat, 'little') & ((1 << (1 << n)) - 1))
    return out


def step(cells):
    return [cells[i] ^ (cells[i + 1] | cells[i + 2]) for i in range(len(cells) - 2)]


def allowed_windows(q, p):
    R = q + p
    n = 2 * R + 1
    full = (1 << (1 << n)) - 1
    cells = var_masks(n)
    for s in range(R):
        if s == q:
            mid = cells[p]                 # the centre of f^q(w), which has 2p + 1 cells
        cells = step(cells)
    return ~(cells[0] ^ mid) & full, n


def points(q, p):
    """Return (finite, list of cycles as vertex lists) for Pre_{q,p}."""
    A, n = allowed_windows(q, p)
    m = n - 1
    lowmask = (1 << m) - 1
    data = A.to_bytes(max(1, (1 << n) // 8), 'little')
    out_e, in_e = {}, {}
    for byte_i, byte in enumerate(data):
        if not byte:
            continue
        for b in range(8):
            if byte >> b & 1:
                w = byte_i * 8 + b
                u, v = w & lowmask, w >> 1
                out_e.setdefault(u, []).append(v)
                in_e.setdefault(v, []).append(u)
    alive = set(out_e) | set(in_e)
    outd = {u: len(out_e.get(u, [])) for u in alive}
    ind = {u: len(in_e.get(u, [])) for u in alive}
    stack = [u for u in alive if outd[u] == 0 or ind[u] == 0]
    dead = set()
    while stack:
        u = stack.pop()
        if u in dead:
            continue
        dead.add(u)
        for v in out_e.get(u, []):
            if v not in dead:
                ind[v] -= 1
                if ind[v] == 0:
                    stack.append(v)
        for v in in_e.get(u, []):
            if v not in dead:
                outd[v] -= 1
                if outd[v] == 0:
                    stack.append(v)
    live = alive - dead
    nxt = {}
    for u in live:
        succ = [v for v in out_e.get(u, []) if v in live]
        pre = [v for v in in_e.get(u, []) if v in live]
        if len(succ) != 1 or len(pre) != 1:
            return False, len(live)
        nxt[u] = succ[0]
    cycles, seen = [], set()
    for u in live:
        if u in seen:
            continue
        cyc, v = [], u
        while v not in seen:
            seen.add(v)
            cyc.append(v)
            v = nxt[v]
        cycles.append(cyc)
    return True, cycles


def ring_word(cyc, m):
    """The configuration on a cycle: cell i is bit 0 of the i-th vertex (the path moves one cell right a step)."""
    return [v & 1 for v in cyc]


def is_travelling(word):
    L = len(word)
    img = [word[i - 1] ^ (word[i] | word[(i + 1) % L]) for i in range(L)]
    return any(img == word[k:] + word[:k] for k in range(L))


def moebius(n):
    res, d, x = 1, 2, n
    while d * d <= x:
        if x % d == 0:
            x //= d
            if x % d == 0:
                return 0
            res = -res
        d += 1
    return -res if x > 1 else res


def main():
    N, cyc_of = {}, {}
    pairs = [(q, p) for q in range(6) for p in range(1, 7) if q + p <= 6] + [(0, p) for p in range(7, PMAX + 1)]
    for q, p in pairs:
        finite, c = points(q, p)
        if not finite:
            print('Pre_{%d,%d}: INFINITE (%d vertices on bi-infinite paths, not disjoint cycles)' % (q, p, c))
            N[(q, p)] = None
            continue
        N[(q, p)] = sum(len(x) for x in c)
        cyc_of[(q, p)] = c
        print('Pre_{%d,%d}: %d points on %d cycles' % (q, p, N[(q, p)], len(c)), flush=True)

    def M(q, p):
        return sum(moebius(p // d) * N[(q, d)] for d in range(1, p + 1) if p % d == 0)

    minimal = {}
    for q, p in pairs:
        if all(N.get((qq, d)) is not None for qq in (q, q - 1) if qq >= 0 for d in range(1, p + 1) if p % d == 0):
            minimal[(q, p)] = M(q, p) - (M(q - 1, p) if q else 0)
    bad = [(k, minimal.get(k), A1[k]) for k in A1 if minimal.get(k) != A1[k]] + \
          [(k, N.get(k), PRE[k]) for k in PRE if N.get(k) != PRE[k]]
    print('PP-C0: mismatches against the two tables: %s' % (bad or 'none'))

    for p in range(1, PMAX + 1):
        if N.get((0, p)) is None:
            continue
        cycles = [c for c in cyc_of[(0, p)]]
        word_min = []
        for c in cycles:
            w = ring_word(c, 2 * p)
            per = None
            for d in range(1, p + 1):                          # minimal temporal period of this point
                if p % d == 0:
                    x = w
                    for _ in range(d):
                        L = len(x)
                        x = [x[i - 1] ^ (x[i] | x[(i + 1) % L]) for i in range(L)]
                    if x == w:
                        per = d
                        break
            if per == p:
                word_min.append((len(c), is_travelling(w)))
        npts = sum(L for L, _ in word_min)
        trav = sum(L for L, tr in word_min if tr)
        small = sum(L for L, _ in word_min if L <= 24)
        lengths = sorted({L for L, _ in word_min})
        print('p = %2d: minimal-period points %5d (spatial periods %s); travelling waves %d; with spatial period'
              ' <= 24: %d' % (p, npts, lengths if len(lengths) <= 14 else '%d values, max %d' % (len(lengths),
                                                                                              lengths[-1]),
                               trav, small), flush=True)


if __name__ == '__main__':
    main()
