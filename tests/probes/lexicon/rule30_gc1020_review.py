#!/usr/bin/env python3
"""rule30_gc1020_review.py: Local's independent second reading of GC1020 / W282 (the finite seed 1001's eternal
two-gap train beside the clamped clock), written from the statement in RULE30-GPT.md, not from GPT's checker
rule30_train_p8_closure.py.

RUN-ON:     cpu (Python 3, no solver); a few seconds
COMMAND:    python3 tests/probes/lexicon/rule30_gc1020_review.py
Checks: (a) the warmup to t = 32 on sites 1 .. 46 (shrinking cone): x_t(1) = 1100 repeated and the band P_(t mod 8)
at t = 16 .. 32; (b) the eight-phase table, for both values of x(15); (c) the P8 lock as a union over all 32
five-cell states and both site-20 inputs at every step, with the eight-tick countercontrol; (d) the index guard
t >= 36, a = t - 16 >= 16 and the sixteen site-14 bits; (e) a sanity simulation with a random tail beyond 46 (not
part of the proof). Outcome in L595.
"""
P = ['10011000100101', '11110101111101', '00000101000001', '00001101100011',
     '10011001010110', '11110111010101', '00000100010101', '00001110110101']


def r30(l, c, r):
    return l ^ (c | r)


# (a) warmup: seed 1001 0^42 on sites 1..46, wall x_t(0) = t mod 2; at time t sites 1 .. 46 - t are exact
row = {i: int(b) for i, b in enumerate('1001' + '0' * 42, start=1)}
col1, band_ok = [], []
for t in range(0, 33):
    known = 46 - t
    col1.append(row[1])
    if t >= 16:
        band_ok.append(''.join(str(row[i]) for i in range(1, 15)) == P[t % 8])
    new = {}
    for i in range(1, known):                      # site i at t+1 needs i+1 <= known
        left = t % 2 if i == 1 else row[i - 1]
        new[i] = r30(left, row[i], row[i + 1])
    row = new
print('(a) x_t(1), t = 0..32:', ''.join(map(str, col1)))
print('    equals 1100 repeated:', ''.join(map(str, col1)) == ('1100' * 9)[:33])
print('    band P_(t mod 8) at every t = 16..32:', all(band_ok), '(%d rows)' % len(band_ok))

# (b) the 8-phase table: P_p -> P_(p+1) with left = p mod 2 (t = p mod 8, 8 even) and right x(15) in {0, 1}
for p in range(8):
    ok = []
    for x15 in (0, 1):
        cur = [int(b) for b in P[p]]
        nxt = [r30(p % 2 if i == 0 else cur[i - 1], cur[i], cur[i + 1] if i < 13 else x15) for i in range(14)]
        ok.append(''.join(map(str, nxt)) == P[(p + 1) % 8])
    print('(b) phase %d: site14=%s; advances with x15=0: %s, x15=1: %s' % (p, P[p][13], ok[0], ok[1]))
print('    column 14 over phases 0..7:', ''.join(P[p][13] for p in range(8)))
print('    column 1 over phases 0..7:', ''.join(P[p][0] for p in range(8)))


# (c) the lock: sites 15..19, left input site 14 = wall bits, right input site 20 free at every step
def image(wall):
    states = {tuple((s >> k) & 1 for k in range(4, -1, -1)) for s in range(32)}
    sizes = []
    for w in wall:
        nxt = set()
        for st in states:
            for x20 in (0, 1):
                ext = (int(w),) + st + (x20,)
                nxt.add(tuple(r30(ext[i - 1], ext[i], ext[i + 1]) for i in range(1, 6)))
        states = nxt
        sizes.append(len(states))
    return states, sizes


img, sizes = image('0111111101111111')
print('(c) image sizes:', ','.join(map(str, sizes)))
print('    final image:', sorted(''.join(map(str, s)) for s in img))
print('    every final state has site 15 white:', all(s[0] == 0 for s in img))
img8, _ = image('01111111')
print('    countercontrol, 8 ticks: a black-first state remains:', any(s[0] == 1 for s in img8))

# (d) the index guard: the lock is used at t = 4 mod 8, t >= 36; its wall window is site 14 at t-16 .. t-1
ok = True
for t in range(36, 36 + 8 * 50, 8):
    a = t - 16
    win = ''.join(P[s % 8][13] for s in range(a, t))
    ok &= (a >= 16 and win == '0111111101111111')
print('(d) for t = 36, 44, ..: a = t-16 >= 16 and site 14 on a..t-1 reads 0111111101111111:', ok)
# and the first lock use after the checked warmup (32) is t = 36; t = 20, 28 lie inside the warmup
print('    phase-4 times inside the warmup 16..32:', [t for t in range(16, 33) if t % 8 == 4])

# (e) an independent long simulation as a sanity check (not part of the proof): random tail beyond 46
import random
rng = random.Random(1020)
N, T = 46 + 2 * 600 + 10, 600
row = [0] * (N + 2)
for i, b in enumerate('1001' + '0' * 42, start=1):
    row[i] = int(b)
for i in range(47, N + 1):
    row[i] = rng.randint(0, 1)
good = True
for t in range(T):
    if t >= 16 and ''.join(map(str, row[1:15])) != P[t % 8]:
        good = False
        print('    band broken at', t)
        break
    new = row[:]
    new[0] = (t + 1) % 2
    for i in range(1, N):
        new[i] = r30(row[i - 1] if i > 1 else t % 2, row[i], row[i + 1])
    row = new
print('(e) random tail beyond 46, band held t = 16..%d: %s' % (T - 1, good))
