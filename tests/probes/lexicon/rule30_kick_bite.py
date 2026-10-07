#!/usr/bin/env python3
"""rule30_kick_bite.py: KB, why the wheel never kicks at classes 12 and 42 (PERIOD-TWO.md row 6.1; the owner's
"bite" steer of 2026-10-07; Cloud's block, claimed in CLOUD-LOCAL.md with these predictions pushed before the run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_kick_bite.py [TRIALS=400] [T=3000]  |  ... --hunt N
COST:       minutes.

Setting. Local's KL (rule30_kick_layers.py, PROOFS.md entry 26) proves, for every right side, that after 133 steps
on the wheel U a departure of column 1 can occur only at classes 12, 32, 42 and 52, with kicks +4..+8, +2..+6, +1..+5
and -6..-1. Real slips (11,437 in section 8.43, 408 in KL-C1) were only ever seen at 32 and 52. KL's automaton lets
the input at column m + 1 be anything at every step, so it over-approximates in one specific way: it never uses
that a real right half is finite. This script asks whether that is where the bite is. It runs the wall form (column
0 = t mod 2, any right half) on four families of right halves and tallies every departure after a long settled
stretch on the wheel:
  F1  finite random right halves, widths 16, 32, 64 and 128;
  F2  infinite random right halves (a random row wider than the light cone, T + 2 cells, so no right edge is ever
      seen by column 1 within T steps);
  F3  infinite spatially periodic right halves, a random word of period 1 to 12 repeated past the light cone;
  F4  infinite random right halves of density 1/8 and 7/8 (sparse and dense backgrounds).
A departure is counted as in KL-C1: column 1 follows U at an even phase d for at least S steps, leaves it at time s,
and then follows U at an even phase d' for 21 observations; its class is (s - d) mod 56 and its kick is KL's
kick_of(d' - d). S = 168 (three turns), past KL's 133-step settling.

Controls:
  KB-C0 (the detector can see the bite): a synthetic column 1 that runs U at phase 0 for 300 steps and then jumps
        to a phase chosen to make a class-12 kick of +6 is reported as exactly that, and likewise class 42, +3.
  KB-C1 (KL's theorem as a guard): every settled departure in every family lies inside KL's settled table. A
        departure outside it would mean a bug here, or an error in entry 26.
  KB-C2 (replication): F1 at width 16 shows classes 32 and 52 only, as KL-C1 and section 8.43 did.

PREDICTIONS (Cloud's, written and pushed before the first run):
  KB-P1: F1 at every width shows no class 12 or 42 departure. Confidence 0.9.
  KB-P2: F2 shows no class 12 or 42 departure either. Confidence 0.7. Near column 1, a finite right half looks like
         an infinite random one until the right edge's influence arrives, so if F1 never shows them, F2 probably
         does not.
  KB-P3: some F3 background (a periodic right half) does show a class 12 or 42 departure. Confidence 0.4.
  KB-P4: F4 shows class 12 or 42 at one of the two densities. Confidence 0.3.
Counterfactual: if F2, F3 or F4 show classes 12 or 42 while F1 never does, the absence comes from the right half's
finiteness or genericity, and that is the bite: a non-local constraint of the kind Q2 asks for. If no family shows
them, the absence is a deeper law (or very rare), and the next step is an exact search for a finite right half that
makes one.

OUTCOME, run 1, 2026-10-07 20:54 BST (container CPU, 25 s, 400 trials per family, T = 3000, at commit 7c4e4b6):
  KB-C0 FAILED, as written, by a fault in the control's design. Given a column 1 built to kick at class 12 by +6,
        the detector reports class 12 exactly. But it reports four kicks, +4 .. +7, because 21 observations do not
        separate nearby phases of a rotation code. The same holds at 42, 32 and 52. So the detector sees classes 12
        and 42; the kick is a set, as in KL's tables. The tallies below count (event, kick) pairs, so each event is
        counted up to five times.
  KB-C1 PASS: every settled departure lies inside KL's settled table.
  KB-C2 FAILED: F1 at width 16 showed one class-42 event.
  KB-P1 REFUTED: class 42 occurs in finite right halves, one event at width 16 and one at width 64, among about 300
        settled events in F1. Seeds 47231 and 63761 (width 16) were found again in a separate search, and an
        independent per-cell coding of the step reproduces their column 1 and their class-42 departures. So class 42
        is rare, not forbidden: half of the bite was a sampling gap.
  KB-P2 HELD (no class 12 or 42 in F2). KB-P3 and KB-P4 REFUTED (none in F3 or F4).
  No class-12 event in any family (about 650 settled events in all).

POST-HOC (written before the hunt mode first ran, 2026-10-07 20:56 BST; not part of the preregistered test):
  HUNT: --hunt N runs N trials of finite random right halves at widths 16 to 64, and of infinite random ones, and
  counts events, not (event, kick) pairs.
  KB-H1: class 42 appears at a rate between 1 in 50 and 1 in 1,000 settled events. Confidence 0.7.
  KB-H2: class 12 appears at least once in 20,000 settled events. Confidence 0.5. If it never does, the next step is
         an exact witness: a path through KL's m = 16 automaton for a class-12 kick, extended column by column to
         the right until it closes into a finite right half or is shown not to.
OUTCOME of the hunt, 2026-10-07 (one run, --hunt 80000, finished at 21:05 BST): 80,000 trials, 20,282 settled
  events: class 32, 13,120; class 52, 7,095; class 42, 67; class 12, none. KB-H1 HELD (class 42 at 1 in 303).
  KB-H2 REFUTED. The exact form, rule30_kick_bite_sat.py (KS), then showed why: no right half can do it.
"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P, F, S = 56, 20, 168
_pos = [a for a in sys.argv[1:] if not a.startswith('--')
        and not (sys.argv.index(a) > 1 and sys.argv[sys.argv.index(a) - 1] == '--hunt')]
TRIALS = int(_pos[0]) if len(_pos) > 0 else 400
T = int(_pos[1]) if len(_pos) > 1 else 3000
KL = {12: range(4, 9), 32: range(2, 7), 42: range(1, 6), 52: range(-6, 0)}


def kick_of(dn):                                             # as in rule30_kick_layers.py
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def column1(R, width):
    """Column 1 for T steps of the wall form, right half R (bit i = column i + 1), the row cut at width cells."""
    mask = (1 << (width + T + 4)) - 1
    row, c1 = R << 1, []
    for t in range(T):
        c1.append((row >> 1) & 1)
        row = ((((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)) & mask
    return c1


def departures(c1, need=S):
    out = []
    t, n = 0, len(c1)
    while t + P + F < n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        if s + F >= n:
            break
        if s - t >= need:
            a = (s - d) % P
            for dn in range(0, P, 2):
                if all(c1[s + j] == U[(s + j - dn) % P] for j in range(F + 1)):
                    out.append((a, kick_of((dn - d) % P)))
        t = s
    return out


def synthetic(cls, kick):
    """U at phase 0 for 300 steps, then the even phase that gives (class, kick) at the departure."""
    s = next(s for s in range(300, 300 + P) if s % P == cls)
    dn = next(dn for dn in range(0, P, 2) if kick_of(dn) == kick and U[(s - dn) % P] != U[s % P])
    return [U[t % P] for t in range(s)] + [U[(t - dn) % P] for t in range(s, s + 200)]


def main():
    c0 = all(departures(synthetic(c, k)) == [(c, k)] for c, k in ((12, 6), (42, 3), (32, 4), (52, -3)))
    print('KB-C0', 'PASS' if c0 else 'FAIL', flush=True)
    rng = random.Random(int.from_bytes(os.urandom(4), 'big'))
    fams = {}
    for w in (16, 32, 64, 128):
        fams['F1 finite w%d' % w] = lambda w=w: (rng.getrandbits(w) | 1, w)
    fams['F2 infinite random'] = lambda: (rng.getrandbits(T + 2), T + 2)

    def periodic():
        p = rng.randint(1, 12)
        word = rng.getrandbits(p) or 1
        R = 0
        for i in range(0, T + 2, p):
            R |= word << i
        return R & ((1 << (T + 2)) - 1), T + 2
    fams['F3 periodic'] = periodic

    def dense(q):
        R = 0
        for i in range(T + 2):
            if rng.random() < q:
                R |= 1 << i
        return R, T + 2
    fams['F4 density 1/8'] = lambda: dense(1 / 8)
    fams['F4 density 7/8'] = lambda: dense(7 / 8)
    guard, bite = True, {}
    for name, make in fams.items():
        tally = Counter()
        for _ in range(TRIALS):
            R, w = make()
            for a, k in departures(column1(R, w)):
                tally[(a, k)] += 1
                guard &= a in KL and k in KL[a]
        classes = Counter()
        for (a, k), v in tally.items():
            classes[a] += v
        bite[name] = classes[12] + classes[42]
        print('%-20s departures %6d  by class %s' % (name, sum(tally.values()), dict(sorted(classes.items()))),
              flush=True)
        for a in sorted(classes):
            print('    class %2d kicks %s' % (a, dict(sorted((k, v) for (b, k), v in tally.items() if b == a))))
    print('KB-C1', 'PASS' if guard else 'FAIL (a departure outside KL\'s settled table)')
    print('KB-C2', 'PASS' if bite['F1 finite w16'] == 0 else 'FAIL')
    f1 = sum(v for n, v in bite.items() if n.startswith('F1'))
    f4 = bite['F4 density 1/8'] + bite['F4 density 7/8']
    print('KB-P1', 'HELD' if f1 == 0 else 'REFUTED', '(%d)' % f1)
    print('KB-P2', 'HELD' if bite['F2 infinite random'] == 0 else 'REFUTED', '(%d)' % bite['F2 infinite random'])
    print('KB-P3', 'HELD' if bite['F3 periodic'] > 0 else 'REFUTED', '(%d)' % bite['F3 periodic'])
    print('KB-P4', 'HELD' if f4 > 0 else 'REFUTED', '(%d)' % f4)


def hunt(n):
    rng = random.Random(int.from_bytes(os.urandom(4), 'big'))
    events, by_class, seeds = 0, Counter(), {12: [], 42: []}
    for i in range(n):
        w = (16, 24, 32, 48, 64, T + 2)[i % 6]
        R = rng.getrandbits(w) | 1
        for a, ks, _ in event_list(column1(R, w)):
            events += 1
            by_class[a] += 1
            if a in seeds and len(seeds[a]) < 5:
                seeds[a].append((w, R if w <= 64 else 'infinite'))
        if (i + 1) % 2000 == 0:
            print('%6d trials, %7d events, by class %s' % (i + 1, events, dict(sorted(by_class.items()))), flush=True)
    print('HUNT: %d trials, %d settled events, by class %s' % (n, events, dict(sorted(by_class.items()))))
    print('class 12 seeds:', seeds[12])
    print('class 42 seeds (up to 5):', seeds[42])
    r42 = by_class[42] / events if events else 0
    print('KB-H1', 'HELD' if 1 / 1000 <= r42 <= 1 / 50 else 'REFUTED', '(rate %.5f)' % r42)
    print('KB-H2', 'HELD' if by_class[12] else 'REFUTED', '(%d class-12 events)' % by_class[12])


def event_list(c1, need=S):
    """departures(), one entry per event: (class, kicks, count)."""
    out = []
    t, n = 0, len(c1)
    while t + P + F < n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        if s + F >= n:
            break
        if s - t >= need:
            ks = [kick_of((dn - d) % P) for dn in range(0, P, 2)
                  if all(c1[s + j] == U[(s + j - dn) % P] for j in range(F + 1))]
            if ks:
                out.append(((s - d) % P, sorted(ks), len(ks)))
        t = s
    return out


if __name__ == '__main__':
    if '--hunt' in sys.argv:
        hunt(int(sys.argv[sys.argv.index('--hunt') + 1]))
    else:
        main()
