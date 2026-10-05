#!/usr/bin/env python3
"""rule30_mirror.py: the owner's two questions of the night about the pyramid's shape. Run backwards from the single
1, is the pattern a mirror of the forward one? And what changes with two starting cells?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_mirror.py
COST:       about a minute on one core.

The owner (2026-10-05): "What happens if you build the pyramid from the starting point upwards as well as downwards as
a mirror? Does it progress in the same way, or are the sides reversed or different due to the sign flip?" And: "What
if there is more than one starting cell, just as the 3-sphere is rooted in a pair of points?"

Backwards. A row y has parent x when y(i) = x(i-1) XOR (x(i) OR x(i+1)). The XOR is reversible, the OR is not, so the
equation can only be solved for the left neighbour, x(i-1) = y(i) XOR (x(i) OR x(i+1)), working leftwards from a
choice of x's right tail. That is the same equation, read in time instead of space, as the forced left half of
sections 5 to 8. A finite parent is impossible: a finite nonzero row's image is two cells wider (the leftmost 1 makes
a 1 on its left, the rightmost one on its right), so a single 1 cannot have one.
Two seeds. With seeds at 0 and d > 0 every cell right of the left seed's light cone (x > t) is outside it, so it is
exactly the lone right seed's pattern: a strip d cells wide riding the right edge. The right seed's influence moves
left slowly.

An exploratory look (2026-10-05, recorded in the chat, checked here): the single 1 has exactly two parents,
...1111|0000... and ...1111 0 1111... (ones to the left for ever); two and three generations up, the left tails are
period 3, four up period 6, while the right tails stay all 0, all 1 or period 3. With two seeds at d = 8 to 128 the
strip was exact, the influence front moved left at about 0.2 to 0.3 cells per step, and column 0 first changed at
t = 1.0 to 2.9 d.

PREDICTIONS, written 2026-10-05 before this script's first run (M0 to M2 check what was seen; M3 and M4 are blind):
  M0 (exact): the two parents above both map to the single 1 on a window of 200 cells, and no row of at most 14 cells
      (all 2^14 - 1, placed anywhere) maps to it.
  M1 (seen): the two parents' own parents (right tails of period at most 6) all have left tails of period 3.
  M2 (exact, the light cone): with seeds at 0 and d, cells x > t equal the lone right seed's, for d = 8 .. 512.
  M3 (blind): for d = 256 and 512, column 0 first differs from the single seed's at a time between 1.5 d and 4 d.
  M4 (blind): for d = 256 and 512, the right seed's influence front moves left at 0.15 to 0.35 cells per step between
      t = 2d and t = 4d (the bottleneck's single-flip arrival speed was 0.21).
REFUTED-BY: M0 or M2 failing (the instrument); M1, M3 or M4 failing.

OUTCOME of the first run, 2026-10-05: M0 passed (exactly the two parents; no finite parent of at most 14 cells). M1
HELD (5 grandparents, every left tail period 3). M2 passed (the strip exact for d = 8 to 512). M3 HELD: column 0
first differs at 578 (2.26 d) and 1,300 (2.54 d) for d = 256 and 512. M4 HELD: the front moves left at 0.281 and
0.277 cells per step.
"""
import itertools, sys

FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step_list(x):
    return [x[i - 1] ^ (x[i] | x[i + 1]) for i in range(1, len(x) - 1)]


def left_tail_period(x, n=36):
    tail = x[:n]
    return min(p for p in range(1, n) if all(tail[i] == tail[i + p] for i in range(n - p)))


def right_tails(ytail, pmax=6):
    out = []
    for p in range(1, pmax + 1):
        L = p * len(ytail)
        for bits in itertools.product((0, 1), repeat=p):
            w = [bits[i % p] for i in range(L)]
            y = [ytail[i % len(ytail)] for i in range(L)]
            if all(w[(i - 1) % L] == y[i] ^ (w[i] | w[(i + 1) % L]) for i in range(L)):
                for k in range(L):
                    r = tuple(w[k:] + w[:k])
                    q = min(q for q in range(1, L + 1) if L % q == 0 and all(r[i] == r[(i + q) % L] for i in range(L)))
                    if r[:q] not in out:
                        out.append(r[:q])
    return out


def parents(y, ytail):
    res = []
    for w in right_tails(ytail):
        ext = y + [ytail[i % len(ytail)] for i in range(2)]
        x = [None] * len(y) + [w[0], w[1 % len(w)]]
        for i in range(len(y) - 1, -1, -1):
            x[i] = ext[i + 1] ^ (x[i + 1] | x[i + 2])
        res.append((x[:len(y)], w))
    return res


def main():
    M = 100
    y = [0] * (2 * M + 3)
    y[M] = 1
    P1 = parents(y, (0,))
    ok0 = len(P1) == 2 and all(step_list(x + [w[0], w[1 % len(w)]])[:len(x) - 1] == y[1:len(x)] for x, w in P1)
    shapes = sorted("".join(map(str, x[M - 4:M + 5])) + "|" + "".join(map(str, w)) for x, w in P1)
    finite_hits = 0
    for R in range(1, 1 << 14):
        row = R << 20
        img = ((row << 1) ^ (row | (row >> 1)))
        finite_hits += img != 0 and img & (img - 1) == 0
    report("M0 exactly two parents, both infinite to the left, and no finite row of <= 14 cells is a parent",
           ok0 and finite_hits == 0, f"parents around 0 | right tail: {shapes}; finite parents found: {finite_hits}")
    P2 = [p for x, w in P1 for p in parents(x, w)]
    per = sorted({left_tail_period(x) for x, w in P2})
    verdict("M1 the grandparents' left tails have period 3", per == [3], f"{len(P2)} grandparents; left-tail periods {per}")

    T = 4 * 512 + 8
    OFF = T + 2
    mask = (1 << (2 * T + 1100)) - 1

    def run(cells):
        row = sum(1 << (OFF + c) for c in cells)
        rows = [row]
        for _ in range(T):
            row = ((row << 1) ^ (row | (row >> 1))) & mask
            rows.append(row)
        return rows
    single = run([0])
    strip, first, speed = True, {}, {}
    for d in (8, 16, 32, 64, 128, 256, 512):
        pair, right = run([0, d]), run([d])
        strip &= all(((pair[t] ^ right[t]) >> (OFF + t + 1)) == 0 for t in range(T))
        first[d] = next((t for t in range(T) if ((pair[t] ^ single[t]) >> OFF) & 1), None)

        def front(t):
            x = pair[t] ^ single[t]
            return (x & -x).bit_length() - 1 - OFF
        if 4 * d <= T:
            speed[d] = (front(2 * d) - front(4 * d)) / (2 * d)
    report("M2 the strip right of the left seed's light cone is the lone right seed's pattern, d = 8 .. 512", strip)
    verdict("M3 column 0 first differs between 1.5 d and 4 d (d = 256, 512)",
            all(first[d] is not None and 1.5 * d <= first[d] <= 4 * d for d in (256, 512)),
            ", ".join(f"d {d}: t = {first[d]} ({first[d] / d:.2f} d)" for d in sorted(first)))
    verdict("M4 the influence front moves left at 0.15 to 0.35 cells per step (d = 256, 512, t = 2d .. 4d)",
            all(0.15 <= speed[d] <= 0.35 for d in (256, 512)),
            ", ".join(f"d {d}: {speed[d]:.3f}" for d in sorted(speed)))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
