#!/usr/bin/env python3
"""rule30_r88_census.py: RC88, how many q = 8 rooted walks first return to zero at r = 88, and with which return
words (Q7's "other r88 / r52808 components"; PERIOD-TWO.md §6). Drawn by Local under draw-and-work (seed 1791575358,
chat L482); predictions pushed before the run.

RUN-ON:     cpu (Python 3); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_r88_census.py

The walk is S84's (rule30_pr195_d0.py): q-periodic profiles, (x, y) -> (y, c) for each child c of (x, y) by the
descending recursion. A rooted walk starts at (a, 0), with a = blk | blk << 4 for an odd 4-bit block, and first returns
to zero when a child is 0. S84's witness takes the first child at every step and returns at r = 88, with return word
w = 00111101 (time order) and prof[r - 1] = prof[r - 2] = w.
Instead of following one child, this tracks the set of pair states reachable at each depth with no zero profile yet,
over every source and every child choice. That is exact over all walks, because the state space has 2^16 pairs. A
first return at depth r is a reachable state (x, y) at depth r - 1 with 0 among its children. Its return word is
y = prof[r - 1]. The D0 shape needs prof[r - 2] = prof[r - 1] = w, that is the state (w, w).

PREDICTIONS (Local's, published before the run):
  RC-C1 (control): the census contains S84's witness: from a = 17, a first return at r = 88 through the state (w, w)
        with w = 00111101.
  RC-P1 (blind, confidence 0.6): at r = 88 there is more than one return word, up to rotation, in the D0 shape
        (state (w, w)).
  RC-P2 (blind, confidence 0.5): first returns occur at more than 20 distinct depths r <= 400.
  RC-D1 (descriptive): the first-return depths r <= 400 with their counts of return words. At r = 88: every return
        word, its rotation class, and whether it has the D0 shape.
OUTCOME, 2026-10-09 20:51 BST (M5, seconds, run at commit f43de64c): RC-C1 PASS, RC-P1 REFUTED, RC-P2 REFUTED.
  - Over every q = 8 rooted walk (all eight odd sources, every child choice), first returns to zero occur at only two
    depths up to 400: r = 88 and r = 371, with 8 return states at each.
  - At r = 88, all 8 return words are rotations of one word (class 11110100, D0 shape, sources 17, 34, 68, 136, which
    are rotations of each other). They are the eight phases of S84's eight-cycle.
  - So, up to rotation, there is no other rooted r = 88 component. The one there is, PR195-D0 already closed.
  - Exploratory, after the run (no predictions), the same census to depth 5000:
    - every rooted walk has returned by then (nothing is alive at 5000);
    - the live set never exceeds 16 states;
    - the only depths are 88 and 371;
    - r = 371 is one class, 10110000 (sources 119, 187, 221, 238), also with prof[r-2] = prof[r-1]. But r - 2 = 369 is
      odd, so it is the odd case and outside D0's m = (r - 2)/2 construction.
  - So the q = 8 rooted returns are completely classified: two classes, each a single rotation orbit.
Q16 (registered 20:51 BST, before running; COMMAND: ... rule30_r88_census.py 16):
  The same census at q = 16. The sources are a = blk | blk << 8 for odd 8-bit blocks, which include the rooted
  witness's 161. It is tracked to depth 60,000, with a cap of 200,000 live states.
  RC16-C1 (control): the census contains the rooted witness, a first return at r = 52,808 from a = 161 | 161 << 8 with
          w = 1000101001100001.
  RC16-P1 (blind, confidence 0.5): at r = 52,808 there is exactly one return word up to rotation.
  RC16-P2 (blind, confidence 0.5): every q = 16 rooted walk has returned by depth 60,000.
RC16 OUTCOME, 2026-10-09 20:54 BST (M5, 87 s, 0.57 GB peak, run at commit 3397ff5f): RC16-C1 PASS, RC16-P1 HELD,
  RC16-P2 REFUTED.
  - The 128 odd doubled sources give first returns at exactly nine depths up to 60,000. Each depth has 16 return states
    forming one rotation class, all of D0 shape, from 8 sources (one rotation orbit):
    - even r: 18826, 26356, 34854, 40804, 49732 and 52808;
    - odd r: 6343, 29167 and 44841.
    Some walks are still alive at 60,000 (the live set peaks at 256).
  - At r = 52,808 there is exactly one return word up to rotation, the rooted witness's. So there is no other component
    at that depth; other components exist only at the other depths.
  - EXPLORATORY, after the run (no predictions; whether G196 applies to these returns is not established):
    - PR196-D1's exit derivative d was computed on each even return's class representative (rule30_pr196_d1's U_masks
      and d_masks, checked against its scalar lists).
    - At r = 52,808 it reproduces PR196's recorded d rotated by one phase, with legal decisions {1, 5} for PR196's
      {0, 4}.
    - Legal unordered decisions at the others: 18826: [1]; 26356: [2, 7]; 34854: [1, 4, 5]; 40804: [0, 1, 7];
      49732: none.
    - Every one has lp(w) = 16, and U_(r - 3) is all ones, as at the witness.
    - If D1's derivation applies, the rooted r = 49,732 component is exactly its sixteen-cycle (closed, as PR195-D0
      closed q = 8). The others have exits, which would need PR198-D2's successor test.
RC16X (registered 2026-10-09 21:01 BST, before running; COMMAND: ... rule30_r88_census.py 16 400000): the same q = 16
  census, continued to depth 400,000 for the walks still alive at 60,000.
  RC16X-C1 (control): the nine depths up to 60,000 are reproduced exactly.
  RC16X-P1 (blind, confidence 0.6): at least one new return depth appears in (60,000, 400,000].
  RC16X-P2 (blind, confidence 0.5): some q = 16 rooted walk is still alive at depth 400,000.
  (Any new even return then gets QX's and QX2's tests, with predictions registered then.)
RC16X OUTCOME, 2026-10-09 21:03 BST (M5, about 6 minutes, 0.57 GB, run at commit 6d5c489d): RC16X-C1 PASS, RC16X-P1 HELD,
  RC16X-P2 REFUTED. (The script's "RC16-P2 HELD" line uses the original label, "every walk has returned".)
  - Every q = 16 rooted walk returns. The last returns at r = 214,006 and nothing is alive after it.
  - There are 16 return depths, each one rotation class from one orbit of 8 sources. 16 orbits x 8 = 128, every odd
    doubled source, so each source orbit has exactly one first return. q = 8 has 2 orbits and 2 depths (88 and 371).
  - The new depths are 62791, 72473, 93358, 114129, 125209, 171541 and 214006. The new even ones are 93358 and
    214006.
RW (registered 21:10 BST, before any q = 32 result; the C walker rule30_rooted_walk.c, one orbit at a time, 64 ns a
  step at q = 32):
  RW-C1 (control, run as the instrument smoke before this registration and disclosed): q = 4, 8 and 16 reproduce
        21; 88 and 371; and all 16 q = 16 depths, orbit by orbit. PASS. A 10^7-step timing run of q = 32's first orbit
        (block 0001) reported "alive at 10^7"; that concerns no prediction below.
  RW-P1 (blind, confidence 0.5): at least 8 of q = 32's first 16 orbits (least-rotation order) return within 10^9
        steps.
  RW-P2 (blind, confidence 0.6): every one of them keeps at most 2 live states.
  RW-D1 (descriptive): the return depths, or "alive at 10^9".
RWC (registered 21:13 BST, while RW ran; RW had reported 0031 -> 45,059,052 and 003b -> 704,584,852, and 0001, 0007,
  0013, 0015, 0023, 0025 and 0037 alive at 10^9; the walker's cycle mode, Brent's detection on the one deterministic
  path, where GC863's reset uniqueness gives exactly one child to every nonzero driver):
  RWC-C1 (control, run before this registration and disclosed): the cycle mode reproduces all q = 8 and q = 16 return
         depths. PASS.
  RWC-P1 (blind, confidence 0.5): at least one q = 32 orbit alive at 10^9 enters a NONZERO cycle (never returns)
         within 5 x 10^9 steps.
  RWC-P2 (control): every orbit that RW saw return returns at the same depth in the cycle mode.
RWC OUTCOME, 2026-10-09 21:22 BST (M5, 4 processes, about 20 minutes, run at commit f9cc3b14): RWC-C1 PASS, RWC-P1
  REFUTED, RWC-P2 PASS.
  - No orbit enters a nonzero cycle, as L487's proof requires: the injective step and the unique child of a nonzero
    driver force every rooted walk to return.
  - Return depths:
    0031 45,059,052; 003b 704,584,852; 0025 1,050,667,725; 0001 1,315,402,133; 0013 1,741,884,389;
    003d 1,812,722,509; 000b 2,081,031,909; 0023 2,217,100,541; 000d 3,377,532,947; 001f 3,477,203,763;
    0007 3,744,206,545; 0019 4,568,428,694.
  - 0015, 0029, 002f and 0037 pass 5 x 10^9 with no return, so their returns lie deeper.
  - RWC extension (registered before running, descriptive, no prediction): those four rerun one at a time to 2 x 10^10
    (orbit ordinals 5, 10, 11 and 13), one low-priority process beside the Collatz run.
  - Return depths therefore grow from about 10^2 (q = 8) and 10^5 (q = 16) to about 10^9 (q = 32).
  - Why about 2^q (exploratory, scratch, after the runs; a counting reading, not a theorem about any one orbit).
    - The rooted step is a partial permutation on the about 4^q nonzero-driver pairs, so these split into cycles and
      chains. Each chain starts at a state (0, c) with no preimage, c != 0, and ends at a return.
    - There are exactly 2^q - 1 starts, and so exactly 2^q - 1 returns. The mean chain length is at most
      4^q / (2^q - 1), about 2^q.
    - Checked exhaustively:
      - q = 4: 15 chains, mean length 15.1 against the bound 16; 226 states on chains, 14 on cycles;
      - q = 8: 255 chains, mean 234.4 against 256, longest 667; 59,770 states on chains, 5,510 on cycles.
    - The rooted returns fit the same scale: q = 16's mean is about 72,000 against 2^16 = 65,536, and q = 32's sampled
      depths are near 2^32.
    - The distribution looks like a random partial permutation's.
      - q = 8 chain-length deciles 20, 87, 194, 370, 507, against 28, 83, 173, 338, 514 for a random split of the same
        59,770 chain states into 255 chains.
      - The tail is lighter: the longest chain is 667, against 1,656 for the random split.
      - q = 16's rooted depths over 2^16 are 0.10 .. 3.27, exponential-looking with mean about 1.1.
RW OUTCOME, 2026-10-09 21:17 BST (M5, 4 processes, about 5 minutes, run at commit 33c2978e): RW-C1 PASS, RW-P1 REFUTED,
  RW-P2 HELD.
  - Of q = 32's first 16 orbits, only 2 return within 10^9 steps: block 0031 at 45,059,052 and block 003b at
    704,584,852. The other 14 are alive at 10^9.
  - Every orbit keeps at most 2 live states. GPT's GC863 shows this is forced by reset uniqueness, so P2 was not a
    real test.
"""
import sys

Q = 8


def children(a, b, q=Q):
    out = []
    bit = lambda w, t: (w >> (t % q)) & 1
    for c0 in (0, 1):
        c = [c0]
        for t in range(q - 1):
            c.append(bit(a, t) ^ (bit(b, t) | c[t]))
        if bit(a, q - 1) ^ (bit(b, q - 1) | c[q - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def rotclass(w, q=Q):
    return min(((w >> d) | (w << (q - d))) & ((1 << q) - 1) for d in range(q))


def tstr(w, q=Q):
    return ''.join(str((w >> t) & 1) for t in range(q))


def main_q16(RMAX=60000, CAP=200000):
    q = 16
    roots = [blk | (blk << 8) for blk in range(256) if bin(blk).count('1') % 2]
    CH = {}

    def ch(x, y):
        k = (x, y)
        if k not in CH:
            CH[k] = children(x, y, q)
        return CH[k]
    layer = {}
    for a in roots:
        for c in ch(a, 0):
            if c:
                layer.setdefault((0, c), set()).add(a)
    returns, depth, maxl, wit = {}, 1, 0, False
    W = int('1000101001100001'[::-1], 2)
    while layer and depth < RMAX:
        nxt = {}
        for (x, y), srcs in layer.items():
            for c in ch(x, y):
                if c == 0:
                    returns.setdefault(depth + 1, set()).add((x, y, frozenset(srcs)))
                    if depth + 1 == 52808 and (161 | 161 << 8) in srcs and y == W:
                        wit = True
                else:
                    nxt.setdefault((y, c), set()).update(srcs)
        layer = nxt
        depth += 1
        maxl = max(maxl, len(layer))
        if len(layer) > CAP:
            print('CAPPED at depth', depth, 'live', len(layer))
            break
        if len(CH) > 2000000:
            CH.clear()
    print('RC16-C1', 'PASS' if wit else 'FAIL')
    print('depth reached %d; alive %s; max live %d' % (depth, bool(layer), maxl))
    for r in sorted(returns):
        cls = {rotclass(y, q) for x, y, s2 in returns[r]}
        print('r = %d: %d states, %d classes %s, D0 shape %s, sources %d' % (r, len(returns[r]), len(cls), [tstr(c, q) for c in sorted(cls)][:4], sorted({x == y for x, y, s2 in returns[r]}), len({a for x, y, s2 in returns[r] for a in s2})))
    one = {rotclass(y, q) for x, y, s2 in returns.get(52808, set())}
    print('RC16-P1', 'HELD' if len(one) == 1 else 'REFUTED (%d classes)' % len(one))
    print('RC16-P2', 'HELD' if not layer else 'REFUTED (alive at %d)' % depth)
    print('COMPLETE')


def main(RMAX=400):
    CH = {(x, y): children(x, y) for x in range(1 << Q) for y in range(1 << Q)}
    roots = [blk | (blk << 4) for blk in range(16) if bin(blk).count('1') % 2]
    # depth 1: the first child step from (a, 0) gives (0, c); a walk's profiles are 0, c, ...; depth = number of steps
    layer = {}
    for a in roots:
        for c in CH[(a, 0)]:
            if c:
                layer.setdefault((0, c), set()).add(a)
    returns = {}
    depth = 1
    witness_ok = False
    while layer and depth < RMAX:
        nxt = {}
        for (x, y), srcs in layer.items():
            for c in CH[(x, y)]:
                if c == 0:
                    r = depth + 1
                    returns.setdefault(r, set()).add((x, y, frozenset(srcs)))
                    if r == 88 and 17 in srcs and x == y == int('00111101'[::-1], 2):
                        witness_ok = True
                else:
                    nxt.setdefault((y, c), set()).update(srcs)
        layer = nxt
        depth += 1
    print('RC-C1', 'PASS' if witness_ok else 'FAIL', flush=True)
    rs = sorted(returns)
    print('first-return depths r <= %d (%d distinct): %s' % (RMAX, len(rs), ' '.join(
        '%d:%d' % (r, len({y for x, y, s in returns[r]})) for r in rs)))
    r88 = returns.get(88, set())
    shapes = {}
    for x, y, srcs in r88:
        shapes.setdefault(rotclass(y), set()).add((tstr(x), tstr(y), x == y, tuple(sorted(srcs))))
    print('r = 88: %d return states, %d return words up to rotation' % (len(r88), len(shapes)))
    for cls, items in sorted(shapes.items()):
        for xs, ys, d0, srcs in sorted(items):
            print('  class %s: prof[r-2] = %s, prof[r-1] = %s, D0 shape %s, sources %s' % (tstr(cls), xs, ys, d0, list(srcs)))
    d0classes = {cls for cls, items in shapes.items() if any(d0 for _, _, d0, _ in items)}
    print('RC-P1', 'HELD' if len(d0classes) > 1 else 'REFUTED', '(%d D0-shape classes at r = 88)' % len(d0classes))
    print('RC-P2', 'HELD' if len(rs) > 20 else 'REFUTED', '(%d distinct depths)' % len(rs))
    print('COMPLETE')


if __name__ == '__main__':
    if sys.argv[1:2] == ['16']:
        main_q16(int(sys.argv[2]) if len(sys.argv) > 2 else 60000)
    else:
        main()
