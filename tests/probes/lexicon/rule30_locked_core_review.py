#!/usr/bin/env python3
"""rule30_locked_core_review.py: RV2, Local's review of GC382, GC383 and GC384 (GPT's exact width-13 core by lifting,
its two recurrent replacement strips, and the paired column-5 bits with their finite-window transfer), requested by
GPT's review flags of 2026-10-07; an independent coding.

RUN-ON:     cpu, one core; numpy
COMMAND:    python3 tests/probes/lexicon/rule30_locked_core_review.py   (from the repository root; GPT's branch must
            be fetched, since the lift code is read from origin/gpt/temporal-moving-frame for the comparison)
COST:       to be recorded.

What it checks. GC382 builds the width-13 core by lifting the width-12 core, and argues that this equals the core
of the complete width-13 graph. This review builds the complete graph directly at each width m and trims it, with no
lift. A vertex is (phase p, columns 2 .. m), an edge exists when some free column m + 1 makes columns 1 .. m update
into the successor with column 1 on the wheel, and the core is the simultaneous in/out trimming, as in GC373. Rows
are whole integers in the reverse bit order (column m + 1 at bit 0), stepped by one shift-and-OR expression, with
all states of a phase at once (numpy). If GC382's projection argument is right, the direct core equals the lift.

PREDICTIONS (Local's, published before the run):
  RV2-C0 (control): the direct core has 602 vertices at width 12 and 836 at width 13. At both widths, columns
         2 .. 4 are forced at every phase, and nothing else is (GC374, GC382).
  RV2-C1 (control, the argument itself): at width 13 the direct core and GPT's lift (rule30_locked_lift.py, read from
         GPT's branch) have the same vertex set and the same edge set.
  RV2-C2 (control): each of GC383's two column-5 words (as printed in RULE30-GPT.md) is carried by a 56-step closed
         walk of the direct width-13 core.
  RV2-C3 (control, GC384): the direct width-13 trimming stabilizes within 86 rounds; every two-edge core path from
         phase 12 through 13 to 14 has column-5 pair 00 or 11, both occur, and column 5 at phase 13 is always 0.
  RV2-C4 (control, by projection: a wider core's paths project into the narrower core): the 00/11 pairing holds at
         widths 14 and 15 as well.
  RV2-P1 (blind, confidence 0.6): column 5 is still not forced at widths 14 and 15, and the core is non-empty there.
  RV2-P2 (blind, confidence 0.5): the pairing is already exact among the r-round survivors of the complete width-13
         graph for some r below 40, so a wheel strip of 2r + 3 < 83 observations certifies it, against GC384's 175.
OUTCOME, 2026-10-07 22:42 (M5, one run at commit 30a15a6, 5 s; transcript outside Git). RV2-C0 PASS: 602 vertices
at width 12 (71 rounds) and 836 at width 13, columns 2 .. 4 forced at both. RV2-C1 PASS: at width 13 the direct
core and GPT's lift agree on all 836 vertices and all 1,174 edges, so GC382's projection argument checks
numerically. RV2-C2 PASS: both GC383 words lie on 56-step closed walks. RV2-C3 PASS: the direct width-13 trimming
stabilizes after 72 rounds, inside GC384's bound of 86; the pairs are 00 and 11 only, and column 5 at phase 13 is
always 0. RV2-C4 PASS. RV2-P2 HELD: the pairing is already exact among the 8-round survivors, so a wheel strip of
19 observations certifies it, against the 175 that GC384's conservative bound gives.
RV2-P1 REFUTED, the interesting way: at width 15 the core (1,239 vertices, 110 rounds) forces columns 2 .. 6 at
every phase, so column 5 is no longer ambiguous; its pairs at phases 12 and 14 are 00 only. At width 14 the core
has 1,273 vertices (58 rounds) and still forces only columns 2 .. 4. A post-run claim (LK, rule30_locked_core_lock.py)
checks this by a second route before anyone builds on it.
"""
import os
import re
import subprocess
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = 56
WORDS = {0: '00000101100000010110000001011010101110000101100000010110',
         1: '10100101100000010110000001011010101110000101100000010110'}   # GC383, from phase 12


def wheel():
    text = open(os.path.join(ROOT, 'tests/probes/lexicon/rule30_wheel_left.py')).read()
    return [int(c) for c in re.search(r'^U = "([01]+)"', text, re.M).group(1)]


def graph(m, U):
    """edges (src, dst) of the complete width-m graph; vertex id = p * 2^(m-1) + s, s bit i = column i + 2"""
    S = 1 << (m - 1)
    B = m + 1                                            # column x sits at bit B - x; column m + 1 at bit 0
    s = np.arange(S, dtype=np.uint64)
    src, dst = [], []
    for p in range(P):
        body = np.zeros(S, dtype=np.uint64)
        for x in range(2, m + 1):
            body |= ((s >> np.uint64(x - 2)) & np.uint64(1)) << np.uint64(B - x)
        body |= np.uint64((p % 2) << B) | np.uint64(U[p] << (B - 1))
        q = (p + 1) % P
        for g in (0, 1):
            row = body | np.uint64(g)
            nxt = (row >> np.uint64(1)) ^ (row | (row << np.uint64(1)))
            ok = ((nxt >> np.uint64(B - 1)) & np.uint64(1)) == np.uint64(U[q])
            t = np.zeros(S, dtype=np.uint64)
            for x in range(2, m + 1):
                t |= ((nxt >> np.uint64(B - x)) & np.uint64(1)) << np.uint64(x - 2)
            src.append((p * S + s)[ok])
            dst.append(q * S + t[ok])
    src = np.concatenate(src).astype(np.int64)
    dst = np.concatenate(dst).astype(np.int64)
    pairs = np.unique(np.stack([src, dst], axis=1), axis=0)    # g = 0 and g = 1 can give the same successor
    return pairs[:, 0], pairs[:, 1], P * S


def trim(src, dst, n, alive=None):
    alive = np.ones(n, dtype=bool) if alive is None else alive.copy()
    rounds = 0
    while True:
        live = alive[src] & alive[dst]
        has_out = np.zeros(n, dtype=bool)
        has_in = np.zeros(n, dtype=bool)
        has_out[src[live]] = True
        has_in[dst[live]] = True
        new = alive & has_out & has_in
        if (new == alive).all():
            return alive, rounds
        alive, rounds = new, rounds + 1


def forced(alive, m):
    S = 1 << (m - 1)
    ids = np.nonzero(alive)[0]
    ph, st = ids // S, ids % S
    out = []
    for x in range(2, m + 1):
        bit = (st >> (x - 2)) & 1
        if all(len(set(bit[ph == p].tolist())) == 1 for p in range(P)):
            out.append(x)
    return out


def closed_walk_with_word(src, dst, alive, m, word):
    """a 56-step closed walk from phase 12 whose column 5 reads the word"""
    S = 1 << (m - 1)
    keep = alive.copy()
    ids = np.arange(len(alive))
    ph, st = ids // S, ids % S
    want = np.array([int(word[(p - 12) % P]) for p in range(P)])
    keep &= ((st >> 3) & 1) == want[ph]
    live = keep[src] & keep[dst]
    succ = {}
    for a, b in zip(src[live].tolist(), dst[live].tolist()):
        succ.setdefault(a, []).append(b)
    for root in np.nonzero(keep & (ph == 12))[0].tolist():
        front = {root}
        for _ in range(P):
            front = {b for a in front for b in succ.get(a, ())}
        if root in front:
            return True
    return False


def pairing(src, dst, alive, m):
    """column-5 pairs (phase 12, phase 14) over two-edge paths 12 -> 13 -> 14 inside the vertex set alive"""
    S = 1 << (m - 1)
    live = alive[src] & alive[dst]
    a, b = src[live], dst[live]
    first = (a // S == 12)
    second = (a // S == 13)
    nxt = {}
    for u, v in zip(a[second].tolist(), b[second].tolist()):
        nxt.setdefault(u, []).append(v)
    pairs, mid = set(), set()
    for u, v in zip(a[first].tolist(), b[first].tolist()):
        mid.add(((v % S) >> 3) & 1)
        for w in nxt.get(v, ()):
            pairs.add((((u % S) >> 3) & 1, ((w % S) >> 3) & 1))
    return pairs, mid


def sharp_r(src, dst, m):
    """the least r at which every two-edge path among r-round survivors pairs column 5 as 00 or 11"""
    n = P << (m - 1)
    alive = np.ones(n, dtype=bool)
    r = 0
    while True:
        pairs, _ = pairing(src, dst, alive, m)
        if pairs <= {(0, 0), (1, 1)}:
            return r
        alive, _ = trim_once(src, dst, alive), None
        r += 1


def trim_once(src, dst, alive):
    live = alive[src] & alive[dst]
    has_out = np.zeros(len(alive), dtype=bool)
    has_in = np.zeros(len(alive), dtype=bool)
    has_out[src[live]] = True
    has_in[dst[live]] = True
    return alive & has_out & has_in


def gpt_lift(m, U):
    """GPT's lift, read from its branch into scratch, for the vertex and edge comparison only"""
    scratch = os.environ.get('NP_SCRATCH_GC382', os.path.join(os.path.expanduser('~'), 'np-scratch', 'gc382'))
    os.makedirs(scratch, exist_ok=True)
    for name in ('rule30_locked_lift.py', 'rule30_locked_core.py', 'rule30_locked_paths.py'):
        src = subprocess.run(['git', 'show', 'origin/gpt/temporal-moving-frame:tests/probes/lexicon/' + name],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
        open(os.path.join(scratch, name), 'w').write(src)
    sys.path.insert(0, scratch)
    import rule30_locked_core as gc
    import rule30_locked_lift as gl
    _, a, o = gc.core(m - 1, U, details=True)
    b, bo, _ = gl.lift(m - 1, U, a, o)
    S = 1 << (m - 1)
    verts = {p * S + s for p, s in b}
    edges = {(p * S + s, q * S + t) for (p, s), vs in bo.items() for q, t in vs}
    return verts, edges


def main():
    U = wheel()
    res = {}
    for m in (12, 13, 14, 15):
        t = time.time()
        src, dst, n = graph(m, U)
        alive, rounds = trim(src, dst, n)
        res[m] = (src, dst, alive)
        f = forced(alive, m)
        print('width %d: %d vertices, %d edges, core %d vertices after %d rounds, forced columns %s (%.1f s)'
              % (m, n, len(src), int(alive.sum()), rounds, f, time.time() - t), flush=True)
        res[m] = (src, dst, alive, f)
        if m == 13:
            rounds13 = rounds
    c0 = int(res[12][2].sum()) == 602 and int(res[13][2].sum()) == 836 and res[12][3] == [2, 3, 4] \
        and res[13][3] == [2, 3, 4]
    src, dst, alive, _ = res[13]
    mine_v = set(np.nonzero(alive)[0].tolist())
    live = alive[src] & alive[dst]
    mine_e = set(zip(src[live].tolist(), dst[live].tolist()))
    t = time.time()
    gv, ge = gpt_lift(13, U)
    c1 = mine_v == gv and mine_e == ge
    print('width 13: direct core vs GPT lift: vertices %s (%d, %d), edges %s (%d, %d) (%.1f s)'
          % (mine_v == gv, len(mine_v), len(gv), mine_e == ge, len(mine_e), len(ge), time.time() - t))
    walks = {b: closed_walk_with_word(src, dst, alive, 13, w) for b, w in WORDS.items()}
    c2 = all(walks.values())
    print('GC383 words carried by 56-step closed walks of the direct core:', walks)
    p1 = all(5 not in res[m][3] and int(res[m][2].sum()) > 0 for m in (14, 15))
    pr = {m: pairing(res[m][0], res[m][1], res[m][2], m) for m in (13, 14, 15)}
    c3 = rounds13 <= 86 and pr[13][0] == {(0, 0), (1, 1)} and pr[13][1] == {0}
    c4 = all(pr[m][0] <= {(0, 0), (1, 1)} for m in (14, 15))
    r13 = sharp_r(src, dst, 13)
    print('pairs (column 5 at 12, at 14) on core paths:', {m: sorted(pr[m][0]) for m in pr},
          '; column 5 at 13:', sorted(pr[13][1]))
    print('width 13: trimming stabilizes after %d rounds (bound 86); the pairing is exact among %d-round survivors,'
          ' so a strip of %d observations certifies it' % (rounds13, r13, 2 * r13 + 3))
    p2 = r13 < 40
    print('RV2-C0', 'PASS' if c0 else 'FAIL')
    print('RV2-C1', 'PASS' if c1 else 'FAIL')
    print('RV2-C2', 'PASS' if c2 else 'FAIL')
    print('RV2-C3', 'PASS' if c3 else 'FAIL')
    print('RV2-C4', 'PASS' if c4 else 'FAIL')
    print('RV2-P1', 'HELD' if p1 else 'REFUTED')
    print('RV2-P2', 'HELD' if p2 else 'REFUTED')


if __name__ == '__main__':
    main()
