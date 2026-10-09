#!/usr/bin/env python3
"""rule30_cloud_triangle_ladders.py: descending from triangle to triangle in the single cell's pyramid.

RUN-ON:     cpu (Python 3 standard library; big-integer rows, regex white runs)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_triangle_ladders.py [D=8192] [STARTS=100]
COST:       a few minutes at D = 8192.

Why (the owner, 2026-10-09): "A new descending mechanism idea again using the (apparent) black triangles. From the
top, select the first largest black triangle, then, draw a line to the next largest triangle anywhere underneath
it, continue to some arbitrary depth. If 2 triangles compete for the next largest, the path splits and forks like
lightening. Also possible, select the next triangle available triangle of the exact same size and descend that way."
Rule 30's triangles are white (a maximal white run shrinks by one cell at each end per row, §8.18); they look black
on a dark page. This is not §8.25/§8.28's lightning, which walks cell by cell; here a path jumps between triangles.

Definitions (Cloud's reading, stated before any run). A triangle is identified by its top: a maximal white run
[i, i + L - 1] in row t that is not the continuation of the run [i - 1, i + L] in row t - 1 (§8.68). Its width is L,
its tip is at row t + ceil(L/2) - 1, centre i + (L - 1)/2. "Underneath it" is the tip's downward light cone: a
triangle of row t' below the tip whose top run meets [c - (t' - t_tip), c + (t' - t_tip)], the cells a change at the
tip could reach. Two rules:
  BIGGER ("next largest", read as the next bigger triangle): go to the first row below the tip, inside the cone,
    that holds a triangle wider than the current one; there take the widest; all of equal widest width fork.
  SAME (the owner's second rule): go to the first row below the tip, inside the cone, that holds a triangle of
    exactly the current width; all of them fork.
Branches that reach the same triangle merge. Starts: the topmost triangle (row 2, width 2, on the edge), the widest
triangle in the first 32 rows, and STARTS random core triangles (|x/t| <= 0.3, rows 256 to 512).

What the record implies before the run. The widest triangles sit on the right edge, at the ruler's rows (§8.68);
Proposition 23 makes the edge triangle at t = 2^v m (m odd) of width w(v) = 2, 3, 5, 6, 8, 14, ... So from an edge
triangle at t = 2^v m, the next wider edge triangle is at t + 2^v, the next row with more factors of 2. An interior
start at distance d from the edge can meet an edge triangle only once w(v) >= d, about 2.5 log2(t) >= d.

PREDICTIONS, written 2026-10-09 before any run of this script (D = 8192, STARTS = 100).
  TL0 (control). Every white run is a top or the continuation of one run above (§8.18), and the tops' widths in the
      core follow §8.68's law: N(L + 1)/N(L) within 0.45 to 0.55 for L = 1 .. 6.
  TL1 (blind; the owner's first rule from the top). BIGGER from the topmost triangle runs down the right edge
      through the rows 4, 8, 16, ..., 4096 (each a power of 2, on the edge) and never forks or leaves the edge.
      Confidence 0.6. Counterfactual: a core triangle wider than the edge's comes first and the bolt leaves the edge.
  TL2 (blind). BIGGER from the core starts stays in the core (none reaches the edge by row 8192), gains about one
      width per step, ends at widths between 2 log2(D) - 9 and 2 log2(D) - 1 (17 to 25), and forks at under 10% of
      its steps. Confidence 0.5.
  TL3 (blind; the owner's second rule). SAME from core starts of width 1 forks at 5% to 40% of its steps and its
      live branches number more than 10 by 500 rows below the start, while SAME from widths 5 and up forks at under
      5% of steps. Confidence 0.4.
UNEXPECTED CHECK, TL4: SAME from the edge triangles at rows 2^k stays on the edge for its next three steps (rows
  3, 5, 7 times 2^k, the ruler's equal marks) for k >= 6, and leaves the edge within three steps for k <= 3.
  Confidence 0.5.
REFUTED-BY: TL0 failing (the instrument); TL1 to TL4 failing as worded.
Disclosed: a smoke test at D = 600, STARTS = 5, run before pushing with its output discarded, found one crash
  (fixed); no result was seen before the predictions were pushed.
"""
import bisect
import random
import re
import sys
from array import array

D = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
STARTS = int(sys.argv[2]) if len(sys.argv) > 2 else 100
W = 2 * D + 3
MASK = (1 << W) - 1
BIG = 6                                                   # tops at least this wide are also indexed separately


def build():
    """Per row: tops sorted by start (array of starts, array of widths), and the same for wide tops."""
    tops_s, tops_w, big_s, big_w = [], [], [], []
    r = 1 << (D + 1)                                      # bit D + 1 + x is cell x
    prev, cont_bad, runs_total = set(), 0, 0
    pat = re.compile("0+")
    for t in range(D):
        s = format(r, f"0{W}b")[::-1][D + 1 - t: D + 2 + t]          # cells x = -t .. t
        assert s[0] == "1" and s[-1] == "1"
        cur = set()
        ts, tw, bs, bw = array("i"), array("i"), array("i"), array("i")
        for m in pat.finditer(s):
            i, L = m.start() - t, m.end() - m.start()
            cur.add((i, L))
            runs_total += 1
            if (i - 1, L + 2) in prev:
                continue                                  # the continuation of the run above
            ts.append(i); tw.append(L)
            if L >= BIG:
                bs.append(i); bw.append(L)
        tops_s.append(ts); tops_w.append(tw); big_s.append(bs); big_w.append(bw)
        prev = cur
        r = ((r << 1) ^ (r | (r >> 1))) & MASK
    return tops_s, tops_w, big_s, big_w, runs_total


def tip(tri):
    t, i, L = tri
    return t + (L + 1) // 2 - 1, i + (L - 1) / 2


def successors(tri, rule, T):
    tops_s, tops_w, big_s, big_w = T[:4]
    t0, i0, L0 = tri
    tt, c = tip(tri)
    use_big = rule == "bigger" and L0 + 1 >= BIG
    for t in range(tt + 1, D):
        S, Wd = (big_s[t], big_w[t]) if use_big else (tops_s[t], tops_w[t])
        if not S:
            continue
        lo, hi = c - (t - tt), c + (t - tt)
        a = bisect.bisect_left(S, int(lo) - 64)
        b = bisect.bisect_right(S, int(hi) + 1)
        cand = [(S[k], Wd[k]) for k in range(a, b) if S[k] <= hi and S[k] + Wd[k] - 1 >= lo]
        if rule == "bigger":
            cand = [(i, L) for i, L in cand if L > L0]
            if cand:
                m = max(L for _, L in cand)
                return [(t, i, L) for i, L in cand if L == m]
        else:
            cand = [(i, L) for i, L in cand if L == L0]
            if cand:
                return [(t, i, L) for i, L in cand]
    return []


def descend(start, rule, T, max_nodes=200000):
    """Breadth-first over the branching path; merged branches are visited once. Returns nodes, edges, forks."""
    seen, frontier, edges, forks, steps = {start}, [start], [], 0, 0
    while frontier and len(seen) < max_nodes:
        nxt = []
        for tri in frontier:
            succ = successors(tri, rule, T)
            steps += 1 if succ else 0
            forks += len(succ) >= 2
            for s in succ:
                edges.append((tri, s))
                if s not in seen:
                    seen.add(s); nxt.append(s)
        frontier = nxt
    return seen, edges, forks, steps


def on_edge(tri):
    t, i, L = tri
    return i + L - 1 == t - 1


def main():
    T = build()
    tops_s, tops_w, big_s, big_w, runs_total = T
    ntops = sum(len(a) for a in tops_s)
    print(f"D = {D}: {runs_total:,} white runs, {ntops:,} triangle tops")
    # TL0: the core's width law
    cnt = {}
    for t in range(D // 4, D):
        for i, L in zip(tops_s[t], tops_w[t]):
            if abs(i + (L - 1) / 2) <= 0.3 * t:
                cnt[L] = cnt.get(L, 0) + 1
    print("TL0 core ratios N(L+1)/N(L), L = 1 .. 8:", ", ".join(f"{cnt.get(L + 1, 0) / max(1, cnt.get(L, 0)):.3f}"
                                                         for L in range(1, 9)))
    first = next((t, i, L) for t in range(D) for i, L in zip(tops_s[t], tops_w[t]))
    best = max(((t, i, L) for t in range(33) for i, L in zip(tops_s[t], tops_w[t])), key=lambda x: (x[2], -x[0]))
    print("topmost triangle:", first, "on edge" if on_edge(first) else "", "; widest in rows 0 .. 32:", best,
          "on edge" if on_edge(best) else "")
    # TL1: BIGGER from the top
    for name, st in [("topmost", first), ("widest of the first 32 rows", best)]:
        seen, edges, forks, steps = descend(st, "bigger", T)
        path = sorted(seen)
        print(f"TL1 BIGGER from the {name}: {len(path)} triangles, {forks} forks; all on the edge: "
              f"{all(on_edge(x) for x in path)}")
        print("  rows and widths:", " ".join(f"{t}:{L}{'' if on_edge((t, i, L)) else '*'}" for t, i, L in path[:40]))
    # core starts
    rng = random.Random(20261009)
    pool = [(t, i, L) for t in range(256, 513) for i, L in zip(tops_s[t], tops_w[t])
            if abs(i + (L - 1) / 2) <= 0.3 * t]
    starts = rng.sample(pool, STARTS)
    # TL2: BIGGER from the core
    reached_edge, widths, fork_steps, all_steps = 0, [], 0, 0
    for st in starts:
        seen, edges, forks, steps = descend(st, "bigger", T)
        reached_edge += any(on_edge(x) for x in seen)
        widths.append(max(L for _, _, L in seen))
        fork_steps += forks; all_steps += steps
    widths.sort()
    print(f"TL2 BIGGER from {STARTS} core starts: reached the edge {reached_edge}; final widest width min "
          f"{widths[0]}, median {widths[len(widths) // 2]}, max {widths[-1]}; forks at {fork_steps} of {all_steps} "
          f"steps ({fork_steps / max(1, all_steps):.1%})")
    # TL3: SAME from the core, by width
    for L0 in range(1, 9):
        sub = [x for x in pool if x[2] == L0][:20]
        if not sub:
            continue
        fs, ss, live500, depth = 0, 0, [], []
        for st in sub:
            seen, edges, forks, steps = descend(st, "same", T, max_nodes=60000)
            fs += forks; ss += steps
            live500.append(sum(1 for (t, _, _) in seen if st[0] + 450 <= t < st[0] + 500))
            depth.append(max(t for t, _, _ in seen))
        live500.sort(); depth.sort()
        print(f"TL3 SAME width {L0}: {len(sub)} starts; forks at {fs} of {ss} steps ({fs / max(1, ss):.1%}); "
              f"triangles in rows start+450 .. +500: median {live500[len(live500) // 2]}, max {live500[-1]}; "
              f"deepest row reached: median {depth[len(depth) // 2]}")
    # TL4: SAME from the edge's ruler marks
    for k in range(2, 12):
        t = 2 ** k
        if t >= D:
            break
        edge = [(t, i, L) for i, L in zip(tops_s[t], tops_w[t]) if on_edge((t, i, L))]
        if not edge:
            continue
        cur, trail = edge[0], []
        for _ in range(3):
            succ = successors(cur, "same", T)
            if not succ:
                break
            trail.append(succ)
            cur = succ[0]
        desc = " -> ".join("/".join(f"{x[0]}{'e' if on_edge(x) else 'c'}" for x in s) for s in trail)
        print(f"TL4 SAME from the edge triangle at 2^{k} (width {edge[0][2]}): {desc}")


if __name__ == "__main__":
    main()
