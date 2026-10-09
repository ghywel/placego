#!/usr/bin/env python3
"""rule30_edge_period_universal.py: UB, how fast do the left edge's prefix periods P_e grow, row by row? (GPT's GC742
asks for P_e along an actual edge history; Cloud's section 8.74 measured the single cell's band.) Local's run (chat
L383), claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu (Python 3 big integers); about a minute per row
COMMAND:    python3 tests/probes/lexicon/rule30_edge_period_universal.py

Read from its leftmost black, any finite row's left-edge diagonals d_e(t) = x_t(-J - t + e) form a closed system:
d_e(t+1) = d_(e-2)(t) xor (d_(e-1)(t) or d_e(t)), with d_0 = 1 for ever. So the prefix of diagonals 0 .. e depends only
on the row's first e + 1 cells, and is Rule 30 in a frame moving left at light speed: one big-integer update per step,
bit e holding d_e. If the prefix 0 .. e agrees at times t and t + P, it is periodic with period dividing P from t on
(prefix determinism). So B_P(t), the lowest diagonal where the states at t and t + P differ, certifies
P_e <= P for every e < B_P(t). GC742: an actual realization of the sparse word W = concat S^(2^j) L from left-edge
distance J_0 needs P_e >= (6/e)(2^((e - J_0 - 14)/10) - 1) at every eventually white e. Slow growth of P_e along the
row's own history would therefore exclude W. This probe measures B_(2^k)(t) for k = 1 .. 11 at t = 2^17 on the single
cell and on 20 seeded random finite rows (a leading 1, then 63 random cells, then white).

PREDICTIONS (Local's, published before the run):
  UB-C1 (control): the moving frame equals direct Rule 30 on the line for t < 300 on a random row; for the single cell
        B_1024(16) = 18 and B_1024(2^17) is within 2 of 98,295 (Cloud's section 8.74: deviation -533 from 0.754 t).
  UB-P1 (blind, confidence 0.6): every random row has B_1024(2^17) within 2% of the single cell's.
  UB-P2 (blind, confidence 0.7): B_2048(2^17) = B_1024(2^17) on every row (section 8.74's lag-2P check, all rows).
  UB-D1 (descriptive): each row's staircase B_(2^k)(2^17), k = 1 .. 11, and the certified bound it gives, P_e <= 2^k
        for e < B_(2^k).
  UNEXPECTED CHECK UB-U (blind, confidence 0.5): the low steps are universal: B_(2^k)(2^17) for k <= 5 is the same on
        all 21 rows.
Counterfactual: a random row whose band at period 1024 stays far behind the single cell's (or a fast-growing staircase)
would show that the single cell's slow period growth is not typical, and GC742's route would need the row's own data.
These are measurements on sampled rows, not an all-history theorem.
OUTCOME: not yet run.
"""
import random

T = 1 << 17
KS = range(1, 12)
ROWS = 20
WIDTH = 64


def evolve(init_bits, steps_needed):
    """returns {t: state} for every t in steps_needed (bit e of a state is d_e(t))"""
    E = 2 * (max(steps_needed) + 1) + WIDTH + 8
    mask = (1 << E) - 1
    S = sum(b << e for e, b in enumerate(init_bits))
    want, out = set(steps_needed), {}
    for t in range(max(steps_needed) + 1):
        if t in want:
            out[t] = S
        S = ((S << 2) ^ ((S << 1) | S)) & mask
    return out


def low_bit(x):
    return (x & -x).bit_length() - 1 if x else None


def staircase(init_bits, t):
    snaps = evolve(init_bits, [t] + [t + (1 << k) for k in KS])
    return {k: low_bit(snaps[t] ^ snaps[t + (1 << k)]) for k in KS}


def literal_control():
    rng = random.Random(1)
    row0 = [1] + [rng.getrandbits(1) for _ in range(WIDTH - 1)]
    S = sum(b << e for e, b in enumerate(row0))
    mask = (1 << 1000) - 1
    line = {e: b for e, b in enumerate(row0)}
    for t in range(300):
        if any(line.get(-t + e, 0) != (S >> e) & 1 for e in range(2 * t + WIDTH)):
            return False
        keys = range(min(line) - 1, max(line) + 2)
        line = {i: line.get(i - 1, 0) ^ (line.get(i, 0) | line.get(i + 1, 0)) for i in keys}
        S = ((S << 2) ^ ((S << 1) | S)) & mask
    return True


def main():
    lit = literal_control()
    single = [1]
    b16 = low_bit(evolve(single, [16, 16 + 1024])[16] ^ evolve(single, [16, 16 + 1024])[16 + 1024])
    st0 = staircase(single, T)
    c1 = lit and b16 == 18 and abs(st0[10] - 98295) <= 2
    print('UB-C1', 'PASS' if c1 else 'FAIL', '(literal %s; single cell B_1024(16) = %s, B_1024(2^17) = %s)' % (lit, b16, st0[10]),
          flush=True)
    print('single cell staircase B_(2^k)(2^17):', st0, flush=True)
    rows = []
    for r in range(ROWS):
        rng = random.Random(1000 + r)
        bits = [1] + [rng.getrandbits(1) for _ in range(WIDTH - 1)]
        st = staircase(bits, T)
        rows.append(st)
        print('row %2d staircase:' % r, st, flush=True)
    p1 = all(abs(st[10] - st0[10]) <= 0.02 * st0[10] for st in rows)
    print('UB-P1', 'HELD' if p1 else 'REFUTED', '(B_1024 range %d .. %d against %d)' % (
        min(st[10] for st in rows), max(st[10] for st in rows), st0[10]))
    p2 = all(st[11] == st[10] for st in rows + [st0])
    print('UB-P2', 'HELD' if p2 else 'REFUTED')
    u = all(st[k] == st0[k] for st in rows for k in KS if k <= 5)
    print('UB-U', 'HELD' if u else 'REFUTED', '(k <= 5 values:', sorted({tuple(st[k] for k in KS if k <= 5) for st in rows + [st0]}), ')')
    print('COMPLETE')


if __name__ == '__main__':
    main()
