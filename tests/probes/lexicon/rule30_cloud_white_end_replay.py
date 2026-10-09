#!/usr/bin/env python3
"""rule30_cloud_white_end_replay.py: WR, an independent replay of L498's step 1 and step 2 (the white end 1 0^q).

RUN-ON:     cpu, one core (Python 3 standard library); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_white_end_replay.py

Why. Local's L498 excludes the Condrey white end (a column eventually reading 1 0^q) for every q >= 10. It uses
a width-8 relaxation: after the macro's stable set is reached, x1 is determined at every tick. Then W^(n+4) = W^n
for n >= 22 extends q = 10 .. 40 to every q >= 10, and Theorem A (PROOFS.md entry 5) finishes. Local asked for a
second reading. Cloud checked steps 2 and 3 by hand (CL110). This is a third, separately written implementation of
the computed facts, after Local's bitmask OH and literal-tuple WJ: states are 8-bit integers, relations are lists of
256-bit sets, and no code is shared.

Model. Cells x1 .. x8 right of the wall; x9 is free at every step; x_j' = x_(j-1) XOR (x_j OR x_(j+1)) with x_0 the
wall bit. The macro for q is one black step (wall 1) then q white steps (wall 0). Its stable set is the limit of the
images of all 256 states under repeated macros, with every input. The per-tick reading is x1 at the start and after
each step of one more macro from the stable set.

Record searched: "white end" with "1 0\\^q" -> L498, L499, WJ (rule30_white_end_jen.py), the board's Condrey row
(PARKED, "awaiting a second reader"), WE's strip test. No third replay.

PREDICTIONS, written 2026-10-09 22:32 BST, before any run of this script.
  WR-C1 (control, must hold): at width 6 no q in 10 .. 40 is determined at every tick (L498's refuted blind guess).
  WR-P1 (0.9): at width 8, every q = 10 .. 40 is determined at every tick, and column +1 reads 1 0 0 1^(q-2).
  WR-P2 (0.9): at width 8, the least n0 with W^(n0+4) = W^n0 (as relations with free input) is at most 22.
  WR-U, the unexpected check (0.5): at width 8 the stable set has the same size for all q >= 26 in one class mod 4,
        and different sizes across the four classes.
  Counterfactual. A failure of WR-P1 or WR-P2 means L498's computed step does not reproduce, and the exclusion is
  not filed until the discrepancy is found.
"""

K = 8


def step_img(states, wall, k):
    """Image of a set of k-bit states under one step with wall bit `wall` and a free input beyond x_k."""
    out = set()
    for s in states:
        x = [(s >> j) & 1 for j in range(k)]               # x[0] is x1
        for inp in (0, 1):
            y = []
            for j in range(k):
                left = wall if j == 0 else x[j - 1]
                right = inp if j == k - 1 else x[j + 1]
                y.append(left ^ (x[j] | right))
            out.add(sum(b << j for j, b in enumerate(y)))
    return frozenset(out)


def relation(wall, k):
    return [step_img([s], wall, k) for s in range(1 << k)]


def compose(R1, R2):
    """R2 after R1: for each state, the union of R2 over R1's image."""
    return [frozenset().union(*[R2[t] for t in R1[s]]) if R1[s] else frozenset() for s in range(len(R1))]


def apply(R, states):
    return frozenset().union(*[R[s] for s in states]) if states else frozenset()


def per_tick(q, k, Bw, Ww):
    full = frozenset(range(1 << k))
    S = full
    while True:
        T = S
        T = apply(Bw, T)
        for _ in range(q):
            T = apply(Ww, T)
        if T == S:
            break
        S = T
    reads = []
    cur = S
    vals = {s & 1 for s in cur}
    reads.append(vals)
    cur = apply(Bw, cur)
    reads.append({s & 1 for s in cur})
    for _ in range(q):
        cur = apply(Ww, cur)
        reads.append({s & 1 for s in cur})
    reads = reads[:q + 1]                                  # ticks t0 .. t0 + q
    det = all(len(v) == 1 for v in reads)
    word = ''.join(str(next(iter(v))) for v in reads) if det else None
    return det, word, len(S)


def main():
    res = {}
    for k in (6, 8):
        Bw, Ww = relation(1, k), relation(0, k)
        dets = {}
        for q in range(10, 41):
            dets[q] = per_tick(q, k, Bw, Ww)
        res[k] = dets
        print('width %d: determined for q = %s' % (k, [q for q in dets if dets[q][0]]), flush=True)
    c1 = not any(v[0] for v in res[6].values())
    print('WR-C1 (width 6 never determined): %s' % ('PASS' if c1 else 'FAIL'))
    ok = all(res[8][q][0] and res[8][q][1] == '100' + '1' * (q - 2) for q in range(10, 41))
    bad = [(q, res[8][q][1]) for q in range(10, 41) if not (res[8][q][0] and res[8][q][1] == '100' + '1' * (q - 2))]
    print('WR-P1 (width 8 determined for every q = 10 .. 40, reading 1 0 0 1^(q-2)): %s%s' % (
        'HELD' if ok else 'REFUTED', '' if ok else ' %s' % bad[:4]))
    Ww = relation(0, 8)
    powers = [[frozenset([s]) for s in range(256)]]
    for n in range(1, 40):
        powers.append(compose(powers[-1], Ww))
    n0 = next((n for n in range(0, 35) if powers[n + 4] == powers[n]), None)
    print('WR-P2 (least n0 with W^(n0+4) = W^n0 at width 8 is <= 22): n0 = %s, %s' % (
        n0, 'HELD' if n0 is not None and n0 <= 22 else 'REFUTED'))
    sizes = {q: res[8][q][2] for q in range(26, 41)}
    classes = {r: {sizes[q] for q in sizes if q % 4 == r} for r in range(4)}
    u = all(len(v) == 1 for v in classes.values()) and len({next(iter(v)) for v in classes.values()}) == 4
    print('WR-U (stable-set size constant within each class mod 4 from q = 26, distinct across classes): %s %s' % (
        {r: sorted(v) for r, v in classes.items()}, 'HELD' if u else 'REFUTED'))


if __name__ == '__main__':
    main()
