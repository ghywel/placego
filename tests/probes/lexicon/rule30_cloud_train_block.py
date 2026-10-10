#!/usr/bin/env python3
"""rule30_cloud_train_block.py: TG, the 2-gap train. Is the visible word 1010.. (column 1 of period 4 in time beside
the 0101 wall) actual at every length, and does a finite right half sustain it? (row Q6, serving CUT's cuts.)

RUN-ON:     cpu (Python 3; mode member needs kissat and rule30_relaxed_records_k.py's scratch, NP_SCRATCH_RLK)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_train_block.py member [NMAX=200]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py periods [STEPS=40000] [SITES=40]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py boundary [N=8] [W=10]      (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py memory [LEAD=4] [NMAX=16]   (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py follower [N=13]            (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py seeds [SITES=12] [CAP=400]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py block [STEPS=20000] [WMAX=24]
COST:       member: seconds a call to n = 200. seeds: about 10 s. block: about a minute at WMAX = 24, more at 60.

Why. CUT's cuts at Cloud's depths, length 53 at d = 140 (L590) and length 81 at d = 152 (L591), are built around long
2-gap trains (gaps 2,2,2,.. between visible ones), as L557 read the K = 18 words. If the pure train had a maximal
length m, (10)^(m+1) would be a minimal forbidden word, a provable family and the home of relax40's slack at those
depths. If the train is actual at every length, the cuts forbid how a train is entered and left, not its length.
Visible index k is wall time 2k + phase; 1 at k and k + 2 means x(1) = 1, 0, 1 at those white times.

Record searched: `record_find.py "2-gap"` -> L557's reading only (via KIMI-ONBOARDING §2); `"ring" "period 4"`,
`alternat`, `"finite right half"`, `shield` -> nothing on this train (G112's white shield is the left half).

PREDICTIONS. TG-P1 (registered in CL185, pushed 13:33 BST before the run; 0.65): (10)^n is in L and in L1 for every
n to 40. Counterfactual: a maximal train length. TG-P2 (informed, not blind: formed after the first SAT witness's cone
showed the four-cell right half 1001 followed by zeros; written here after its run; 0.5): the FINITE right half 1001
beside the phase-0 clock keeps column 1 on the train for 3000 readings. Counterfactual: a finite failure time, so
long trains need an infinite tailored right half. TG-P3 (informed, 0.5): the observed windows (t mod 4, sites 1..W)
close under one step with a free site W + 1 for some W <= 40, a finite certificate that the block lasts for ever.
Counterfactual: no closure, the state count outrunning the sample.

OUTCOME (2026-10-10 13:45 BST). TG-P1 HELD, to n = 200 in both phases (Local, L592, to n = 100 independently).
TG-P2 HELD: 3000 of 3000 readings; the same seed in phase 1 fails at the first reading; of the 4095 seeds on sites
1..12 (phase 0), 28 reach the 400-reading cap and every one of them begins 1001; the longest failing seed reaches 32.
Block: sites 1..6 follow a period-4 cycle for 20,000 steps from t = 2 while site 7 is still broken at the end of the
run (chaos sits against the block), so column 1 reads 1100 repeating. TG-P3 REFUTED: no closure to W = 60 (an ad hoc
run; the distinct windows grow to the sample size), and at W = 6 the single unclosed transition is x(7) = 1 at t = 0
mod 4, never observed. The chain of what the train needs of the right half runs one site further back each step:
x(2) = 0 at t = 2, 3 mod 4; x(7) = 0 at t = 0; x(7) or x(8) at t = 3; .. The eternity of the train, and of the block,
is OPEN: measured to 20,000 steps, not proved. Unexpected check: the block holds although site 7 is chaotic throughout.

ADDENDUM (2026-10-10 14:12 BST). "Site 7 is chaotic" is WITHDRAWN: the period-4 test misread it. Mode `periods` (40,000
steps) finds each column's eventual period: sites 1 .. 6 period 4 (transient <= 2), sites 7 .. 14 period 8 (transients
4 .. 10), and from site 15 on no period <= 8192 over the second half of the run. The ordered band beside the clock is
14 sites wide with chaos pinned at site 15 for 40,000 steps. Noticed in the orbit printout of the owner's third-party
test (Kimi's q2b.py), whose own period test, like mine, allowed no transient and so also missed it.

ADDENDUM 2 (2026-10-10 14:45 BST). The eternity is PROVED: GPT's GC1020 (waiting entry W282) shows the fourteen-cell
band repeats with period 8 for ever, so column 1 reads 1100 for ever, and the same holds for every right half whose
first 46 cells are 1001 followed by zeros. Mechanism: at the one phase where site 14 is white and site 15 matters,
the sixteen previous bits of column 14 (0111111101111111) force site 15 white by Local's P8Lock (all 32 five-cell
states, both exterior inputs every tick, 16 ticks: ten states survive, all white-first); strong induction from a
warmup to t = 32. Cloud re-derived the warmup, the eight-phase transition table (phase 4 needs e = 0 and fails on
e = 1) and the lock's image sizes 25, 20, 22, 20, 20, 18, 16, 13, 11, 11, 15, 17, 17, 15, 14, 10 independently
(CL189). Why the closure searches failed: they demanded closure of sampled window sets at one step; the proof keeps
a sixteen-tick boundary history instead.

MODE boundary, OUTCOME (2026-10-10 15:05 BST; computed facts, no prior prediction: the mode was written to pose a
question, CL190). After (10)^n, n = 4 .. 14, both phases, 6- and 10-bit windows: of 1,024 ten-bit continuations
exactly 7 are realizable: the train continues (gaps 2), or it ends with the gap 4 followed by the gap 5 (then 2 or
the window ends). No exit by 3, by 5 directly, or by 6 or more. Entrances: of 1,024 ten-bit words before the train,
19 (phase 0) and 17 (phase 1) are realizable; the gap into the train's first one is 4 or 5 (or 2, the train itself),
never 3 and never 6 or more; the gap before that is 2, 3, 4 or 5. The sets are identical for every n tested.
  CORRECTION (GC1023, checked 15:05 BST): the entrance rule has a startup exception the windows could not show: when
  the one before the train is the visible word's first symbol, a gap-3 entrance exists (100 + (10)^4 is IN, both
  phases; with any symbol before it, ABSENT). The exit rule follows from eight K18 forbidden words (GC1023), all
  re-checked absent and minimal here, so it is implied by Local's base list and explains no overshoot.

MODE memory, OUTCOME (2026-10-10 15:20 BST; computed after L596, no prior prediction). The word "lead 0, gap 4, a
train of n ones, then 4,5,2,2,2,2,4,5,3,3,3,5,5,5,5,2" is the length-81 cut at n = 10 and a factor of the R_real(152)
witness at n = 11. By SAT it is IN for n = 6, 7, 8, 9, 11 and ABSENT for n = 5, 10, 12, 13, 14, 15, 16 (both phases
agree); with the lead gap 5 it is IN for n = 10, 11 and ABSENT for 8, 9, 12, 13. With the tail cut short, every
prefix of the tail is IN for both n = 10 and n = 11; only the final gap 2 separates them. So a train does not forget
its length: it is read back some 60 visible symbols later, and the dependence on n is not monotone and not a parity.
CL190's Question B is false in its strong form at this scale; whether the set stabilizes for n >= 12 is open.

MODE follower, OUTCOME (2026-10-10 15:15 BST; GC1024's request). q T^11 v IN, q T^12 v ABSENT, q T^13 v IN, q T^14 v IN
(phase 0). A 101-site right half for q T^13 v is found by SAT and read back by a plain simulation; flipping site 21
breaks it. The right half is printed by the mode and kept in CL193. So n0(10) >= 13 rests on a simulated model.
"""
import os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def step(row, wall):
    """One Rule 30 step of the right half (site i is bit i - 1) with the wall value at site 0."""
    return ((row << 1) | wall) ^ (row | (row >> 1))


def train_length(seed, phase, cap):
    """Readings of column 1 at the wall's white times that follow 1010.. before the first break, at most cap."""
    row, k = seed, 0
    for t in range(2 * cap):
        wall = (t + phase) % 2
        if wall == 0:
            if (row & 1) != (1 - k % 2):
                return k
            k += 1
        row = step(row, wall)
    return k


def member(nmax):
    import rule30_relaxed_records_k as rk
    for ph in (0, 1):
        assert not rk.in_language_phase('11', ph) and rk.in_language_phase('0101', ph), 'controls'
    for n in (5, 10, 20, 40, 100, nmax):
        w = '10' * n
        verdicts = ['L%d %s' % (ph, 'IN' if rk.in_language_phase(w, ph) else 'ABSENT') for ph in (0, 1)]
        print('(10)^%-3d len %3d: %s' % (n, len(w), '  '.join(verdicts)), flush=True)


def seeds(sites, cap):
    print('seed 1001, phase 0: train length %d of %d; phase 1: %d'
          % (train_length(0b1001, 0, cap), cap, train_length(0b1001, 1, cap)))
    full, best = [], 0
    for s in range(1, 1 << sites):
        n = train_length(s, 0, cap)
        if n >= cap:
            full.append(format(s, 'b')[::-1])
        else:
            best = max(best, n)
    print('%d of %d seeds on sites 1..%d reach the cap; longest failing seed %d; all capped seeds begin 1001: %s'
          % (len(full), (1 << sites) - 1, sites, best, all(f.startswith('1001') for f in full)))


def block(steps, wmax):
    rows, row = [], 0b1001
    for t in range(steps + 1):
        rows.append(row)
        row = step(row, t % 2)
    bit = lambda r, i: (r >> (i - 1)) & 1
    last = {i: max([t for t in range(steps - 3) if bit(rows[t], i) != bit(rows[t + 4], i)] or [-1])
            for i in range(1, 13)}
    print('last period-4 violation by site:', ' '.join('%d:%d' % kv for kv in last.items()))
    print('cycle of sites 1..6 by t mod 4 (from t = 4):', [format(rows[4 + p] & 63, '06b')[::-1] for p in range(4)])
    mask = lambda W: (1 << W) - 1
    for W in range(6, wmax + 1):
        seen = {p: set() for p in range(4)}
        for t in range(2, steps + 1):
            seen[t % 4].add(rows[t] & mask(W))
        bad = sum(1 for p in range(4) for w in seen[p] for b in (0, 1)
                  if step(w | (b << W), p % 2) & mask(W) not in seen[(p + 1) % 4])
        print('W=%2d windows per phase %s unclosed %d%s'
              % (W, [len(seen[p]) for p in range(4)], bad, '  CLOSED' if bad == 0 else ''))
        if bad == 0:
            break


def periods(steps, sites):
    """Each column's eventual period (powers of two to 8192, every q <= 64) and the first time it holds to the end."""
    row, cols = 0b1001, {i: [] for i in range(1, sites + 1)}
    for t in range(steps + 1):
        for i in cols:
            cols[i].append((row >> (i - 1)) & 1)
        row = step(row, t % 2)
    for i in cols:
        seq, found = cols[i], None
        for q in sorted(set([2 ** k for k in range(14)] + list(range(1, 65)))):
            lv = next((t for t in range(steps - q, -1, -1) if seq[t] != seq[t + q]), -1)
            if lv < steps // 2:
                found = (q, lv + 1)
                break
        print('site %2d: period %s from t = %s' % ((i,) + (found if found else ('none <= 8192', '-'))))


def boundary(n, W):
    """Which W-bit visible words can follow, and which can precede, the 2-gap train (10)^n? (SAT, both phases.)
    Printed with the train's last (first) one included, so the gaps read correctly: exits as gaps of '10' + u,
    entrances as
    gaps of w + '1'."""
    import itertools
    import rule30_relaxed_records_k as rk
    def gaps(x):
        idx = [i for i, c in enumerate(x) if c == '1']
        return [b - a for a, b in zip(idx, idx[1:])]
    words = [''.join(b) for b in itertools.product('01', repeat=W)]
    for ph in (0, 1):
        ex = [u for u in words if rk.in_language_phase('10' * n + u, ph)]
        en = [w for w in words if rk.in_language_phase(w + '10' * n, ph)]
        print('phase %d, train (10)^%d, %d-bit windows: %d exits, %d entrances' % (ph, n, W, len(ex), len(en)))
        for u in ex:
            print('  exit     %s  gaps after the train\'s last one: %s' % (u, gaps('10' + u)))
        for w in en:
            print('  entrance %s  gaps up to the train\'s first one: %s' % (w, gaps(w + '1')))


def memory(lead, nmax):
    """Does a train remember its length? The length-81 cut (L591) is lead 0, gap 4, a train of 10 ones, then the gaps
    4,5,2,2,2,2,4,5,3,3,3,5,5,5,5,2; the R_real(152) >= 18 witness (L596) is the same word with a train of 11 ones.
    Membership of that word for a train of n ones, and for the tail cut short (n = 10 against 11)."""
    import rule30_relaxed_records_k as rk
    word = lambda gaps: '0' + '1' + ''.join('0' * (g - 1) + '1' for g in gaps)
    tail = [4, 5, 2, 2, 2, 2, 4, 5, 3, 3, 3, 5, 5, 5, 5, 2]
    verdict = lambda w, ph: 'IN' if rk.in_language_phase(w, ph) else 'ABSENT'
    print('lead gap %d, train of n ones, then the tail %s:' % (lead, tail))
    for n in range(5, nmax + 1):
        w = word([lead] + [2] * (n - 1) + tail)
        print('  n = %2d (length %3d): phase 0 %-6s phase 1 %s' % (n, len(w), verdict(w, 0), verdict(w, 1)), flush=True)
    print('tail cut short, lead 4, n = 10 against n = 11 (phase 0):')
    for k in range(2, len(tail) + 1):
        print('  %-42s n=10 %-6s n=11 %s' % (tail[:k], verdict(word([4] + [2] * 9 + tail[:k]), 0),
                                          verdict(word([4] + [2] * 10 + tail[:k]), 0)), flush=True)


def follower(n):
    """GC1024's request: one retained, directly simulated right half for q T^n v (q = 000010001010000, v = 0010000101,
    T = 10; L593 reports q T^12 v absent and q T^13 v present). Finds a right half by SAT, simulates it with a plain
    loop, and prints it; a flipped site is the countercontrol."""
    import rule30_relaxed_records_k as rk
    q, v = '000010001010000', '0010000101'
    for k in (11, 12, 13, 14):
        print('q T^%d v: %s' % (k, 'IN' if rk.in_language_phase(q + '10' * k + v, 0) else 'ABSENT'))
    w = q + '10' * n + v
    right = rk.right_half_for(w, 0)
    rh = ''.join(str(right.get(i, 0)) for i in range(1, max(right) + 1))
    def reads(rh):
        T = 2 * len(w) - 2
        row = [0] + [int(c) for c in rh] + [0] * (T + 4)
        vis = []
        for t in range(T + 1):
            row[0] = t % 2
            if t % 2 == 0:
                vis.append(str(row[1]))
            row = [row[0]] + [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)] + [0]
        return ''.join(vis) == w
    print('right half (%d sites) for q T^%d v, phase 0: %s' % (len(rh), n, rh))
    print('direct simulation reads the word: %s; with site 21 flipped: %s'
          % (reads(rh), reads(rh[:20] + ('1' if rh[20] == '0' else '0') + rh[21:])))


if __name__ == '__main__':
    cmd, a = sys.argv[1], [int(x) for x in sys.argv[2:]]
    t0 = time.time()
    {'member': lambda: member(*(a or [200])), 'seeds': lambda: seeds(*(a or [12, 400])),
     'block': lambda: block(*(a or [20000, 24])), 'periods': lambda: periods(*(a or [40000, 40])),
     'boundary': lambda: boundary(*(a or [8, 10])), 'memory': lambda: memory(*(a or [4, 16])),
     'follower': lambda: follower(*(a or [13]))}[cmd]()
    print('(%.0f s)' % (time.time() - t0))
