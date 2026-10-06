#!/usr/bin/env python3
"""rule30_race_memory.py: the exact conditional-memory table GPT specified (chat G109; PROOFS.md G110) for the race
model of rule30_races.py. Is the pair (ideal bit, error) at one site a closed state, or does the error remember more?

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_race_memory.py      (seconds)

The model (races.c's actual right-reading cyclic scan): a ring of W = 5 cells, updated each tick from site 4 down to
site 0; a flagged site i < 4 reads its right neighbour's NEW value, site 4 (scanned first) never races, so four flags
per tick are effective. Ideal = the synchronous ring. Stationary observer at site 2, horizon 3 ticks. All 32 initial
rows and all 4,096 histories of the 12 effective flags, at eps = 1/2 (every history weight 1): 131,072 paired
histories. I_t, J_t are the ideal and noisy samples at site 2, E_t = I_t XOR J_t, t = 0..3.
The table: E_3 counts by the state k1 = (I_2, E_2), and by its refinement k2 = (I_1, I_2, E_1, E_2). Two refined bins
of one k1 bin have equal E_3 rates exactly when their integer cross-products agree. Every positive-count bin is kept.
This is a finite-ring result, not an infinite-bulk law.

PREDICTIONS, written 2026-10-06 before this script's first run:
  MM0 (control, exact): with no flags, every E_t is 0.
  MM1 (control, exact; G110's pulse on the ring): one flag, at site 2 on tick 1, then synchronous: E_2 = 0 and
      E_3 = E_1 for every initial row; each I_2 bin holds 2 injected rows and 14 others; the refined rates are 1 and 0.
  MM2 (blind; GPT's tentative prediction, which I share): at eps = 1/2 at least one k1 bin splits under the k2
      refinement (unequal cross-products), so (I_2, E_2) is not a closed state for E_3.
  MM3 (blind, mine): in both I_2 bins, P(E_3 = 1 | E_2 = 1) > P(E_3 = 1 | E_2 = 0): errors persist.
  D1 (descriptive): every k1 and k2 bin with its count and its number of E_3 = 1.

OUTCOME of the first run, 2026-10-06 (one core, under a second): MM0, MM1 HELD (controls); MM2 HELD: all four k1
bins split under the refinement, 17 refined pairs with unequal cross-products; MM3 HELD: P(E_3 = 1 | E_2 = 1, E_2 = 0)
= 0.6875 against 0.2946 (I_2 = 0) and 0.2600 against 0.1748 (I_2 = 1). D1: six of the 14 positive k2 bins are
deterministic: (I_1, I_2, E_1, E_2) = (0,0,1,0) and (1,0,0,1) and (1,0,1,0) always give E_3 = 1; (0,0,1,1),
(0,1,0,1) and (1,1,0,0) never do (the last holds 25,600 histories). The first is G109's echo surviving random races:
an error that healed at tick 2 returns at tick 3 every time when both ideal bits are white. k1 counts: (0,0) 57,344
with 16,896; (0,1) 8,192 with 5,632; (1,0) 52,736 with 9,216; (1,1) 12,800 with 3,328.
"""
from fractions import Fraction as F
from itertools import product

W, T, SITE = 5, 3, 2
R30 = lambda l, c, r: l ^ (c | r)


def sync(row):
    return [R30(row[(i - 1) % W], row[i], row[(i + 1) % W]) for i in range(W)]


def race(row, flags):
    new = [0] * W
    for i in range(W - 1, -1, -1):
        r = new[i + 1] if (i < W - 1 and flags[i]) else row[(i + 1) % W]
        new[i] = R30(row[(i - 1) % W], row[i], r)
    return new


def histories(flag_hist):
    """Yield (I, J, E) samples at SITE for every initial row under one flag history (a list of T flag lists)."""
    for r0 in range(2 ** W):
        a = [(r0 >> k) & 1 for k in range(W)]
        b = list(a)
        I, J = [a[SITE]], [b[SITE]]
        for t in range(T):
            a = sync(a)
            b = race(b, flag_hist[t])
            I.append(a[SITE])
            J.append(b[SITE])
        yield I, J, [x ^ y for x, y in zip(I, J)]


fails = []


def verdict(name, ok, detail=''):
    print(name, 'HELD' if ok else 'REFUTED', detail)
    if not ok:
        fails.append(name)


none = [[0] * W for _ in range(T)]
verdict('MM0', all(not any(E) for _, _, E in histories(none)), '(no flags: no errors)')
pulse = [[0, 0, 1, 0, 0], [0] * W, [0] * W]
rows = list(histories(pulse))
ok1 = all(E[2] == 0 and E[3] == E[1] for _, _, E in rows)
for b in (0, 1):
    inj = sum(1 for I, _, E in rows if I[2] == b and E[1] == 1)
    oth = sum(1 for I, _, E in rows if I[2] == b and E[1] == 0)
    ok1 &= (inj, oth) == (2, 14)
verdict('MM1', ok1, '(pulse: E_2 = 0, E_3 = E_1, bins 2 and 14 per ideal bit; refined rates 1 and 0)')

k1, k2 = {}, {}
for bits in product((0, 1), repeat=4 * T):
    flag_hist = [[bits[4 * t + k] for k in range(4)] + [0] for t in range(T)]
    for I, J, E in histories(flag_hist):
        a = k1.setdefault((I[2], E[2]), [0, 0])
        a[0] += 1
        a[1] += E[3]
        c = k2.setdefault((I[1], I[2], E[1], E[2]), [0, 0])
        c[0] += 1
        c[1] += E[3]
total = sum(v[0] for v in k1.values())
print('paired histories:', total)
print('k1 = (I_2, E_2): count, E_3 = 1, rate')
for key in sorted(k1):
    n, e = k1[key]
    print('  ', key, n, e, '%.4f' % (e / n))
print('k2 = (I_1, I_2, E_1, E_2): count, E_3 = 1, rate')
for key in sorted(k2):
    n, e = k2[key]
    print('  ', key, n, e, '%.4f' % (e / n))
splits = []
for key1 in sorted(k1):
    sub = [(k, v) for k, v in k2.items() if (k[1], k[3]) == key1 and v[0] > 0]
    for (ka, (na, ea)), (kb, (nb, eb)) in product(sub, sub):
        if ka < kb and ea * nb != eb * na:
            splits.append((key1, ka, kb))
verdict('MM2', len(splits) > 0, '%d unequal refined pairs; k1 bins split: %s' % (
    len(splits), sorted({s[0] for s in splits})))
ok3 = True
for b in (0, 1):
    n1, e1 = k1.get((b, 1), [0, 0])
    n0, e0 = k1.get((b, 0), [0, 0])
    ok3 &= n1 > 0 and n0 > 0 and F(e1, n1) > F(e0, n0)
verdict('MM3', ok3, '(errors persist in both ideal-bit bins)')
print('ALL CONTROLS AND PREDICTIONS HELD' if not fails else 'NOT HELD: ' + ', '.join(fails))
