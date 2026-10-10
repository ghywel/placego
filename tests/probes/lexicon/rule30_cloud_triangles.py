#!/usr/bin/env python3
"""rule30_cloud_triangles.py: TA, the owner's triangle-area question: how much of each side, the orderly band and the
random region split at the exact front B(t) of section 8.74, is coloured by white triangles, by triangle size.

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_triangles.py [LOG2T=12] [LOG2P=10]
COST:       about a minute at LOG2T = 12.

The owner's question (chat, 2026-10-10): the random right seems to hold more and larger triangles than the orderly
left; would adding up the AREA of the white triangles on each side, not just their number, reveal anything?

What is exact, before any run. Every white triangle is exact (section 8.18: a run of L zeros loses one cell at each
end per step), so a top of width L colours A(L) cells, A(2m - 1) = m^2 and A(2m) = m(m + 1), and every white cell lies
in exactly one triangle. Section 8.68 derived the density of tops of width L under the uniform measure, 3 * 2^-(L+4)
per cell, and found the single cell's core matches it to three decimals. Integrating that law against A(L) gives, with
sum_m m / 4^m = 4/9 and sum_m m^2 / 4^m = 20/27,
    sum_L 3 * 2^-(L+4) A(L) = (3/16) [3 * 20/27 + 4/9] = (3/16)(72/27) = 1/2   exactly (PROVED, by hand, 2026-10-10),
the uniform measure's white density: the triangle law and the half-density are one fact. So the SUM of white areas on
the random side is half its area and tells nothing; the information is in the share by size. On the random side the
share of all cells in tops of width L is 3 * 2^-(L+4) A(L): 3/32 for each of L = 1, 2, 3 (9.4% each), then falling by
about half per step, so tops of width 8 and more hold about 3.6% of the cells (7% of the white). On the orderly side
Lemma B3 (section 8.59, Lean-certified) caps a white run at twice the local stripe period less one, and section 8.68
saw no top wider than 16 in the band x/t < -0.6.

What is measured: rows 2 .. 2^LOG2T of the single cell, read from the left edge (bit e = x_t(-t + e)); B(t) as in
section 8.74 (lowest differing bit of V_t and V_(t+P), P = 2^LOG2P). Maximal white runs of each row; a run [a, b] at
time t is a TOP unless [a - 2, b] was a maximal run at t - 1 (the exact-shrink parent). A top is assigned to the
orderly side if b < B(t), to the random side if a >= B(t), else to the front. Per side: cells, white cells, tops by
width, area by width (A(L) per top), the largest width; on the random side the top density per cell against the law;
and for the handover, the law in the first 32 diagonals past B(t) against the rest.
Record searched: "triangle area", "2^-(L+4)", triangle census (section 8.68: counts of tops by width and by x/t, not
areas and not split at B(t)); sections 8.18, 8.29, 8.59 (B3), 8.74, 8.75.

PREDICTIONS, written 2026-10-10 19:52 BST, before the first run (LOG2T = 12, LOG2P = 10).
  TA-P0 (controls). Every maximal white run of length L >= 3 at time t has the run shrunk by one cell at each end as
      a maximal run at t + 1 (exactness, zero violations). On each side the white cells equal the summed areas of the
      tops assigned to it, within the front's share (tops straddling B(t) are under 1% of all tops). The white fraction
      on each side is within 0.005 of 1/2.
  TA-P1 (blind, the law by area). On the random side the share of cells in tops of width L is within 5% (relative) of
      3 * 2^-(L+4) A(L) for L = 1 .. 8, so the three smallest widths hold 9.4% each and widths 8 and more hold 3.6%
      (within 0.5 points) of the random side's cells.
  TA-P2 (blind, the band). On the orderly side at least 90% of the white area is in tops of width at most 8
      (confidence 0.6), and the largest top has width at most 31 (B3's cap for the band's period 16; confidence 0.5).
  TA-P3 (blind, the handover; unexpected check). The law holds already in the first 32 diagonals past B(t): the top
      densities for L = 1 .. 6 there are within 15% of 3 * 2^-(L+4), as they are farther in (confidence 0.5). The
      front is sharp for triangles as it was for compressibility (CH-P4 refuted a slow zone).
  Counterfactual: if the triangles were not exact or did not partition the white cells, TA-P0's area identity fails;
  if the random side were not at the uniform measure, TA-P1 fails; if the band had a graded edge, TA-P3 fails.

OUTCOME (19:54 BST, 4 s at LOG2T = 12). TA-P0 HELD: no exactness violation among 3.16 million tops; the front holds
  0.03% of the tops; white fractions 0.4982 (orderly) and 0.4998 (random); triangle areas 0.4979 and 0.4996 of the
  cells. TA-P1 HELD: the random side's area shares match 3 * 2^-(L+4) A(L) within 1.5% for L = 1 .. 11 (9.35%, 9.37%,
  9.39% at L = 1, 2, 3; widths >= 8 hold 3.74%); the largest random top is 33, on the right edge, as section 8.68's
  log2 t + 22 says for t = 4096. TA-P2 HELD: 95.7% of the orderly white area is in widths <= 8 and the largest orderly
  top is 16, the band's period; beyond width 8 the band's census is not geometric (2,233 tops of width 10 against
  1,275 of width 9; 429 of width 12 against 113 of 11; none of 13 or 14; 180 of 15; 63 of 16). TA-P3 HELD, with a
  faint graded edge: in the first 32 diagonals past B(t) the top densities for L = 1, 2, 3, 6 run 2% to 9% below the
  law (0.981, 0.974, 0.956, 0.907) while beyond they sit at 1.00: a small deficit of births just past the front that
  the compressors of the chains probe could not see.
"""
import re, sys, time


def A(L):
    m = (L + 1) // 2
    return m * m if L % 2 else m * (m + 1)


def law(L):
    return 3.0 * 2.0 ** -(L + 4)


def rows(n):
    V = [1]
    for _ in range(n):
        v = V[-1]
        V.append((v << 2) ^ ((v << 1) | v))
    return V


def main(log2t=12, log2p=10):
    t0 = time.time()
    N, P = 1 << log2t, 1 << log2p
    V = rows(N + P)
    sides = {'O': {}, 'R': {}, 'F': {}}
    cells = {'O': 0, 'R': 0}
    white = {'O': 0, 'R': 0}
    near, far = {}, {}
    near_cells = far_cells = 0
    exact_viol = 0
    prev = set()
    for t in range(2, N + 1):
        s = format(V[t], 'b')[::-1]
        x = V[t] ^ V[t + P]
        B = (x & -x).bit_length() - 1 if x else len(s)
        cells['O'] += B
        cells['R'] += len(s) - B
        white['O'] += s[:B].count('0')
        white['R'] += s[B:].count('0')
        near_cells += min(32, len(s) - B)
        far_cells += max(0, len(s) - B - 32)
        runs = set()
        for m in re.finditer('0+', s):
            a, b = m.start(), m.end()          # [a, b)
            runs.add((a, b))
            L = b - a
            if L >= 3 and t > 2 and (a - 2, b) not in prev:
                pass
            if (a - 2, b) in prev:
                continue                       # a continuation, not a top
            side = 'O' if b <= B else ('R' if a >= B else 'F')
            sides[side][L] = sides[side].get(L, 0) + 1
            if side == 'R':
                (near if a - B < 32 else far)[L] = (near if a - B < 32 else far).get(L, 0) + 1
        # exactness control: every run of length >= 3 in prev has its shrunk child here
        for (a, b) in prev:
            if b - a >= 3 and (a + 2, b) not in runs:
                exact_viol += 1
        prev = runs
    tops = {k: sum(v.values()) for k, v in sides.items()}
    area = {k: sum(A(L) * n for L, n in v.items()) for k, v in sides.items()}
    print('rows 2 .. %d, P = %d; tops O %d, R %d, front %d (%.2f%% of tops); exactness violations %d'
          % (N, P, tops['O'], tops['R'], tops['F'], 100.0 * tops['F'] / sum(tops.values()), exact_viol))
    for k in 'OR':
        print('side %s: cells %d, white %d (%.4f), triangle area %d (%.4f of cells), largest top %d'
              % (k, cells[k], white[k], white[k] / cells[k], area[k], area[k] / cells[k], max(sides[k])))
    p0 = (exact_viol == 0 and tops['F'] / sum(tops.values()) < 0.01
          and all(abs(white[k] / cells[k] - 0.5) < 0.005 for k in 'OR'))
    print('TA-P0', 'HELD' if p0 else 'REFUTED')
    print('random side, share of cells by top width L (measured / law 3*2^-(L+4)*A(L)); top density / law:')
    p1 = True
    for L in range(1, 13):
        sh = A(L) * sides['R'].get(L, 0) / cells['R']
        dens = sides['R'].get(L, 0) / cells['R']
        print('  L=%2d  area share %.5f / %.5f  (ratio %.3f)   density ratio %.3f'
              % (L, sh, law(L) * A(L), sh / (law(L) * A(L)), dens / law(L)))
        if L <= 8 and abs(sh / (law(L) * A(L)) - 1) > 0.05: p1 = False
    big = sum(A(L) * n for L, n in sides['R'].items() if L >= 8) / cells['R']
    print('  random side: widths >= 8 hold %.4f of cells (law 0.036)' % big)
    p1 &= abs(big - 0.036) < 0.005
    print('TA-P1', 'HELD' if p1 else 'REFUTED')
    small = sum(A(L) * n for L, n in sides['O'].items() if L <= 8) / area['O']
    print('orderly side: share of white area in widths <= 8: %.4f; tops by width: %s'
          % (small, ' '.join('%d:%d' % (L, sides['O'][L]) for L in sorted(sides['O']))))
    p2 = small >= 0.90 and max(sides['O']) <= 31
    print('TA-P2', 'HELD' if p2 else 'REFUTED')
    p3 = True
    print('handover: top density / law in the first 32 diagonals past B(t) (near) and beyond (far):')
    for L in range(1, 7):
        rn = near.get(L, 0) / near_cells / law(L)
        rf = far.get(L, 0) / far_cells / law(L)
        print('  L=%d  near %.3f  far %.3f' % (L, rn, rf))
        if abs(rn - 1) > 0.15: p3 = False
    print('TA-P3 (unexpected check)', 'HELD' if p3 else 'REFUTED', '(%d s)' % (time.time() - t0))


if __name__ == '__main__':
    main(*[int(x) for x in sys.argv[1:]])
