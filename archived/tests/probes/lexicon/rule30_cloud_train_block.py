#!/usr/bin/env python3
"""rule30_cloud_train_block.py: TG, the 2-gap train. Is the visible word 1010.. (column 1 of period 4 in time beside
the 0101 wall) actual at every length, and does a finite right half sustain it? (row Q6, serving CUT's cuts.)

RUN-ON:     cpu (Python 3; mode member needs kissat and rule30_relaxed_records_k.py's scratch, NP_SCRATCH_RLK)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_train_block.py member [NMAX=200]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py periods [STEPS=40000] [SITES=40]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py boundary [N=8] [W=10]      (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py memory [LEAD=4] [NMAX=16]   (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py follower [N=13]            (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py carrier                  (needs kissat)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py packet
            python3 tests/probes/lexicon/rule30_cloud_train_block.py arming                   (needs kissat, ~1 min)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py cut45                    (needs kissat, ~3 min)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py separator                (needs kissat, ~1 min)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py entrymemory              (needs kissat, ~10 min)
            python3 tests/probes/lexicon/rule30_cloud_train_block.py past
            python3 tests/probes/lexicon/rule30_cloud_train_block.py joint                    (GC1039 second reading)
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

MODE carrier, OUTCOME (2026-10-10 15:25 BST; data for the lemma posed in CL194). After q T^12 not even a 0 can follow
(q T^12 IN, q T^12 0 ABSENT): the 13th car is forced by the prefix q. After q T^13 every prefix of v is IN. Dropping
q's first two symbols lifts that obstruction (q[2:] T^12 0 IN, q[2:] T^12 v[:9] IN) but q[2:] T^12 v is still ABSENT
(a 47-symbol minimal forbidden word); with three symbols dropped all is IN. Unconditioned synchronization: from all
states of sites 7 .. 6+w, gate each cycle, free exterior, the reachable set stabilizes at 20 (w = 5, from cycle 1),
52 (w = 7, from 3), 105 (w = 9, from 5), 269 (w = 11, from 8).

MODE packet, OUTCOME (2026-10-10 15:30 BST; review of W283). Seven cells 1001101 with site 8 free give exactly the
claimed 23-tick column 1 and white trace 101000100001 (exit 4, 5): CONFIRMED. Six cells with site 7 free leave
column 1 undetermined from tick 8. The CL193 model has the slab 1001100 at t = 62 .. 70, the failed gate 1001101
at t = 74 and 1011010 at t = 78 (the last car): CL194's gated propagation to the last car was unsound; revised in
CL195 to a strip propagation from the interior time 62 with the visible word imposed.

MODE cut45, OUTCOME (2026-10-10 15:55 BST; GC1029 reviewed, CL198). GC1029's final-bit criterion holds (all 256 rows;
W283's 15 states at offset 22; exactly 1000110, 1001100, 1001101 permit the final 1). Over realizers of the 44-symbol
word (entry 000010001010000, ten cars, the nine forced exit bits) the seven cells at t = 84 are 1110101 or 1110111,
so sites 2 and 3 are black and the final 1 is impossible: the length-45 cut. Certificate: the whole word forces all
24 cells of sites 1 .. 24 at t = 30 (SAT census) to 100110011001100000000010, and that strip alone, with a free site
25 at every tick and no further samples, reaches 736 states at t = 84, every one beginning 11101. The entry and train
alone force only sites 1 .. 8 at t = 30; the exit's forced packet pins the rest. Control: with the leading 0 replaced
by 1, five strip cells (16, 20, 21, 22, 24) stay free and the propagation reaches states beginning 100 (final 1
possible), as 1 + 00010001010000 T^10 v is IN. The cut needs the leading 0 exactly: every proper suffix of the entry
gives IN.

MODE separator, OUTCOME (2026-10-10 16:05 BST; GC1029's backward separator reviewed, CL199). Rows at offset 7 after the
failed gate are 0110000 and 0110001; only 0110000 can reach the three final-one states at offset 22; backward set
sizes 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3 at offsets 7 .. 22 (GPT's figures). For the length-45 cut
(gate failed at 62) the separator x_7(69) = 0 is realized, indeed forced, so it does not cut. The cut bites at t = 76:
the leading-0 history's row at 75 is 1001000 and x_8(75) is forced 1, so the row at 76 is 0111101, outside the
backward set {0111010, 0111100, 0111111}; the pinned strip's free-exterior propagation forces x_8(75) = 1 too. With
the leading 1, x_8(75) can be 0 or 1 and the final 1 is realizable either way.

MODE entrymemory, OUTCOME (2026-10-10 16:50 BST; GC1033's request, CL203). Entry + ten cars, no exit, sites 1 .. 45:
the leads' forced cells differ at t = 0 (sites 2 .. 6 = 11111 after the leading 0), t = 5 (sites 4, 8, 9) and t = 10
(site 7 = 0 after the leading 0), and not at all at t = 15, 20, 30. At t = 30 the exact set of sites 7 .. 18 is 19
states after the leading 0 and 31 after the leading 1, the first within the second (seven two-cell relations hold
for the leading 0 only). Propagated through the cars and the failed gate with a free exterior beyond site 18, both
sets reach the same 231 states at t = 75 with x_7 and x_8 free: the near-wall strip does not carry the memory.
  WITHDRAWN (GC1035, 16:55 BST): that propagation kept the 0111 boundary at site 6 after the failed gate at 62, where
  the slab changes (x_6(63) = 0, x_7(64) = 1 in truth). Repaired by propagating all 18 cells under the real clock
  with the sample and gate filters; the repaired outcome is in CL204 and below.
  REPAIRED OUTCOME (17:05 BST): the same 19 and 31 twelve-cell sets (retained in CL204), each prefixed by the slab and
  propagated as 18 cells under the real clock with the sample and gate filters, reach the same 190 states at t = 75,
  sites 1 .. 5 forced 10010, x_7 and x_8 free, for both leads. The strip of sites 1 .. 18 at the first car, with a
  free exterior beyond it, still carries no trace of the leading symbol; the conclusion stands on the repaired loop.

MODE past, OUTCOME (2026-10-10 18:00 BST; GC1037 reviewed, CL207). GPT's backward propagation reproduced: from the
eight fillings with cells 16 and 20 black, with the entry samples at 2 .. 28 imposed, 23 rows survive at t = 0, every
one beginning 1, peak layer 261, three fillings with a past; so under the 19 common pins the leading 0 excludes a
black (16, 20) origin and the final 1. Common-pin test: with sites 1 .. 8 fixed and 9 .. 24 free at t = 30, the train,
the exit bits and the gates leave 581 survivors (2,282 at width 26) with only sites 1 .. 8 in common: the eleven other
pins are not forced in a free-exterior row of width 24 or 26; they remain an exact-cone (SAT) fact of the whole word.

MODE arming, OUTCOME (2026-10-10 15:45 BST; review of GC1028 and data for CL197). The exit target is exactly GPT's 39
nine-bit words (01101????, 01110????, 0111100??, 0111111ab with ab != 00), all beginning 011. A' has 34 states and
misses the target: over A' the pair (site 8, site 9) is never (1, 1), while every target word has it. After q the
arming pattern (slab, sites 7 .. 9 = 011 at the k-th car's white tick) is realizable at every car 5 .. 16 except the
ninth; after the prefixes 1000, 01000 and the empty prefix it is realizable at every car 5 .. 16.

JOINT (mode joint; GPT's GC1039 second reading, CL210). Predictions written 2026-10-10 18:42 BST, before the mode's
first run; GPT's script was run once (its printed counts seen: 581, 2, 4975, 0, two prefixes), my code is independent.
Record searched: GC1039, CL207, CL198, "common pin", "joint".
  JP1: from CL207's 581 suffix origins at t = 30 (first 8 sites 10011001, width 24, free exterior, samples to 86 and the
       site-7 gates), the exact width-24 reverse to t = 0 under the whole entry, leading 0 included, leaves exactly 2
       origins, equal at sites 1 .. 23 (10011001100110000000001) and differing at site 24 (0.85).
  JP2: with first 8 sites 10011000 the forward suffix set has 4975 origins with a future and none has an entry past
       (0.85).
  JP3: the width-12 reverse from the slab 1001100 at t = 34 (five free sites) to t = 20 under the samples leaves exactly
       the two first-8 patterns 10011000 and 10011001 at t = 30 (0.8).
  JP4 (unexpected check): with only the leading 0 relaxed (t = 0 unconstrained, samples 2 .. 28 kept), at least 10 of
       the 581 keep a past: the leading 0 does the work, as in GC1037 and CL207 (0.7).
  Counterfactual: if GPT's label merging, parent enumeration or the gate at 62 were off, the counts differ from 2,
  4975 and 0, or the prefix set differs from {10011000, 10011001}.
  What a HELD JP1 .. JP3 gives: GC1039's inference (all 19 common pins, indeed sites 1 .. 23, follow from the entry,
  the samples, the proved slab and gates in the width-24 free-exterior strip) is CONFIRMED by independent code; the
  premises (GC1027's slab and gates; the gate at 62 from the first exit 0) are those already accepted in CL206 .. CL208.
OUTCOME (18:46 BST, 9 s). JP1 HELD: 581 origins with a future (CL207's count), 2 with an entry past, common
  10011001100110000000001?, 45 rows at t = 0, past peak 2857 (GPT's numbers exactly). JP2 HELD: 4975 and 0, peak 7300.
  JP3 HELD: {10011000, 10011001}, peak 95. JP4 REFUTED: with only the leading 0 relaxed, 5 of the 581 keep a past (253
  rows at t = 0) and their common sites are 100110011001100?000???1?, exactly CL198's 19 pins: the samples 2 .. 28
  alone pin the 19 sites, and the leading 0 then cuts 5 to 2, pinning 16, 20, 21 and 22 white. GC1039 CONFIRMED.
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


def carrier():
    """Where the memory across the train sits (CL194). (1) By SAT: how much of q and of v the obstruction q T^12 v
    needs.
    (2) Pure Python: starting from all states of sites 7 .. 6+w, with the gate (site 7 white at the phase-0 tick) each
    cycle and a free exterior at site 7+w every tick, how fast the reachable set under the train stabilizes."""
    import rule30_relaxed_records_k as rk
    q, v, T = '000010001010000', '0010000101', '10'
    IN = lambda w: rk.in_language_phase(w, 0)
    print('q T^12 v[:j], j = 0 .. 10:', ''.join('I' if IN(q + T * 12 + v[:j]) else 'A' for j in range(11)),
          '(I in, A absent)')
    print('q[i:] T^12 v, i = 0 .. 15:', ''.join('I' if IN(q[i:] + T * 12 + v) else 'A' for i in range(16)))
    print('q T^13 v[:j], j = 0 .. 10:', ''.join('I' if IN(q + T * 13 + v[:j]) else 'A' for j in range(11)))
    print('q[2:] T^12 v[:9]:', 'IN' if IN(q[2:] + T * 12 + v[:9]) else 'ABSENT',
          '| q[2:] T^12 0:', 'IN' if IN(q[2:] + T * 12 + '0') else 'ABSENT')
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    for w in (5, 7, 9, 11):
        S = {tuple((m >> j) & 1 for j in range(w)) for m in range(1 << w)}
        sizes = []
        for k in range(16):
            S = {x for x in S if x[0] == 0}
            for wall in (0, 1, 1, 1):
                S = {tuple(step_bits(list(x), wall, e)) for x in S for e in (0, 1)}
            sizes.append(len(S))
        print('w = %2d: reachable states of sites 7 .. %d after 1 .. 16 gated cycles: %s'
              % (w, 6 + w, sizes))


def packet():
    """W283 / GC1026 (GPT): from sites 1 .. 7 = 1001101 beside the white-start clock, with site 8 free at every tick,
    column 1 is forced for 22 ticks (the exit packet 4, 5). Pure Python, union over the free input; also the six-cell
    countercontrol (site 7 free) and the CL193 model's slab at the last cars."""
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    def trace(start, ticks):
        S, out = {tuple(int(c) for c in start)}, []
        for t in range(ticks + 1):
            firsts = {x[0] for x in S}
            out.append('?' if len(firsts) > 1 else str(firsts.pop()))
            S = {tuple(step_bits(list(x), t % 2, e)) for x in S for e in (0, 1)}
        return ''.join(out)
    tr = trace('1001101', 22)
    print('seven cells 1001101, site 8 free: column 1 =', tr, '| white trace', tr[::2],
          '| as claimed:', tr == '11001100010011010001001')
    tr6 = trace('100110', 22)
    print('six cells 100110, site 7 free: column 1 =', tr6, '| first undetermined tick', tr6.find('?'))
    rh = ('0111111001110101001100011000110010010111101100100110100010100111101110001010011011101000000000000'
          '0000')
    w = '000010001010000' + '10' * 13 + '0010000101'
    T = 2 * len(w) - 2
    row = [0] + [int(c) for c in rh] + [0] * (T + 4)
    for t in range(T + 1):
        row[0] = t % 2
        if t in (62, 70, 74, 78, 82):
            print('CL193 model, t = %2d: sites 1 .. 7 = %s' % (t, ''.join(map(str, row[1:8]))))
        row = [row[0]] + [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)] + [0]


def _cone_sat(word, extra, tmax):
    """SAT over the right cone to time tmax: the visible word at the white ticks and extra unit cells (t, i, b)."""
    import os, subprocess, tempfile
    import rule30_relaxed_records_k as rk
    var, nv, cl = {}, [0], []
    def x(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]
    for t in range(tmax):
        for i in range(1, tmax - t + 1):
            r, c, y = x(t, i + 1), x(t, i), x(t + 1, i)
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:
                cl += ([[-y, -o], [y, o]] if t % 2 else [[-y, o], [y, -o]])
            else:
                l = x(t, i - 1)
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for k, b in enumerate(word):
        cl.append([x(2 * k, 1)] if b == '1' else [-x(2 * k, 1)])
    for (t, i, b) in extra:
        cl.append([x(t, i)] if b else [-x(t, i)])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=rk.DIR, delete=False) as f:
        f.write('p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        name = f.name
    try:
        rc = subprocess.run([rk.KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return rc == 10


def arming():
    """GC1028's exit target and q's allowed states (CL197). Target: nine bits of sites 7 .. 15 at the white tick 62 (sla
        b
    100110 at sites 1 .. 6) whose gates read 0 at 62, 0 at 66, 1 at 70. A': those nine bits over realizers of q T^9 with
    the slab at 62 (SAT). Then the cars at which the arming pattern (slab, sites 7 .. 9 = 011) is realizable after a
    prefix."""
    import itertools
    def gates(nine):
        cells, g = list(nine), {}
        g[62] = cells[0]
        for k in range(8):
            wall = 0 if (62 + k) % 4 == 2 else 1
            r = [wall] + cells
            cells = [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(cells))]
            if 62 + k + 1 in (66, 70):
                g[62 + k + 1] = cells[0]
        return g
    target = {''.join(map(str, s)) for s in itertools.product((0, 1), repeat=9)
              if (lambda g: g[62] == 0 and g[66] == 0 and g[70] == 1)(gates(s))}
    print('target (gates 0, 0, 1 at 62, 66, 70): %d nine-bit words; all begin 011: %s'
          % (len(target), all(w.startswith('011') for w in target)))
    q = '000010001010000'
    slab = [(62, i + 1, int(b)) for i, b in enumerate('100110')]
    A = [''.join(map(str, s)) for s in itertools.product((0, 1), repeat=9)
         if _cone_sat(q + '10' * 9, slab + [(62, 7 + j, b) for j, b in enumerate(s)], 78)]
    print("A' (sites 7 .. 15 at 62 over q T^9 realizers with the slab): %d states; meets the target: %s"
          % (len(A), bool(set(A) & target)))
    print("  (site 8, site 9) over A':", sorted({(w[1], w[2]) for w in A}), '| over the target: only (1, 1)')
    def cars(prefix, kmax=16):
        out = []
        for k in range(5, kmax + 1):
            s_k = 2 * len(prefix) + 4 * (k - 1)
            extra = [(s_k, i + 1, int(b)) for i, b in enumerate('100110')] + [(s_k, 7, 0), (s_k, 8, 1), (s_k, 9, 1)]
            if _cone_sat(prefix + '10' * k, extra, s_k + 12):
                out.append(k)
        return out
    for prefix in (q, '1000', '01000', ''):
        print('prefix %-16s arming realizable at cars %s' % (repr(prefix), cars(prefix)))


def cut45():
    """The length-45 cut q T^10 v (L593; GC1029) explained by a finite certificate (CL198). Steps: GC1029's criterion
    for
    the exit's final bit; the seven-cell states at t = 84 over realizers of q T^10 and the forced nine exit bits; the
    cells forced at t = 30 by the entry alone and by the whole word; propagation of the forced strip to t = 84 with a
    free exterior (union over inputs). Control: the same entry preceded by a 1 instead of a 0."""
    import itertools
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    def forced_row(word, t, n, tmax):
        out = ''
        for i in range(1, n + 1):
            c0, c1 = _cone_sat(word, [(t, i, 0)], tmax), _cone_sat(word, [(t, i, 1)], tmax)
            out += '0' if c0 and not c1 else '1' if c1 and not c0 else '?' if c0 and c1 else '!'
        return out
    def propagate(starts, t0, t1, cap=3_000_000):
        S = set(starts)
        for t in range(t0, t1):
            S = {tuple(step_bits(list(x), t % 2, e)) for x in S for e in (0, 1)}
            if len(S) > cap:
                return None
        return S
    def forced(S, n):
        def one(i):
            return '0' if all(x[i] == 0 for x in S) else '1' if all(x[i] == 1 for x in S) else '?'
        return ''.join(one(i) for i in range(n))
    tail, exit9 = '00010001010000', '001000010'
    three = {'1000110', '1001100', '1001101'}
    for lead in ('0', '1'):
        entry = lead + tail
        word = entry + '10' * 10 + exit9                      # 44 symbols, samples to t = 86
        B = [''.join(map(str, x)) for x in itertools.product((0, 1), repeat=7)
             if _cone_sat(word, [(84, i + 1, b) for i, b in enumerate(x)], 92)]
        print('entry %s: states of sites 1..7 at t = 84: %s; meets GC1029\'s three: %s'
              % (entry, ' '.join(B), bool(set(B) & three)))
        f_entry = forced_row(entry + '10' * 10, 30, 24, 76)
        f_word = forced_row(word, 30, 24, 92)
        print('  forced at t = 30, sites 1..24, by entry + train: %s | by the whole word: %s' % (f_entry, f_word))
        free = [i for i, c in enumerate(f_word) if c == '?']
        starts = []
        for bits in itertools.product((0, 1), repeat=len(free)):
            x = [int(c) if c != '?' else 0 for c in f_word]
            for j, i in enumerate(free):
                x[i] = bits[j]
            starts.append(tuple(x))
        S = propagate(starts, 30, 84)
        print('  propagation of the forced strip (free site 25 every tick, no samples used): %s states at t = 84, '
              'forced sites 1..8 = %s' % (len(S) if S else '>cap', forced(S, 8) if S else '-'))


def separator():
    """GC1029's backward separator (CL199): from the failed gate 1001101, which seven-cell rows at each offset can still
    reach the three final-one states at offset 22; where the leading-0 history leaves that set; the single cell that
    decides it."""
    import itertools
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    three = {tuple(int(c) for c in w) for w in ('1000110', '1001100', '1001101')}
    S = {tuple(int(c) for c in '1001101')}
    layers = [S]
    for t in range(22):
        S = {tuple(step_bits(list(x), t % 2, e)) for x in S for e in (0, 1)}
        layers.append(S)
    def can_reach(row, k):
        T = {row}
        for t in range(k, 22):
            T = {tuple(step_bits(list(x), t % 2, e)) for x in T for e in (0, 1)}
        return bool(T & three)
    B = {k: {r for r in layers[k] if can_reach(r, k)} for k in range(23)}
    print('rows at offset 7:', sorted(''.join(map(str, r)) for r in layers[7]),
          '| able to reach the three:', sorted(''.join(map(str, r)) for r in B[7]))
    print('backward set sizes, offsets 7 .. 22:', [len(B[k]) for k in range(7, 23)])
    strip = tuple(int(c) for c in '100110011001100000000010')
    T = {strip}
    for t in range(30, 62):
        T = {tuple(step_bits(list(x), t % 2, e)) for x in T for e in (0, 1)}
    first = None
    for t in range(62, 85):
        if not {x[:7] for x in T} & B[t - 62] and first is None:
            first = t
        if t == 75:
            print('pinned strip propagated to t = 75: site 8 forced to',
                  ''.join(sorted({str(x[7]) for x in T})))
        if t < 84:
            T = {tuple(step_bits(list(x), t % 2, e)) for x in T for e in (0, 1)}
    print('first tick at which the propagated rows all leave the backward set:', first)
    for lead in ('0', '1'):
        w = lead + '00010001010000' + '10' * 10 + '001000010'
        vals = [str(b) for b in (0, 1) if _cone_sat(w, [(75, 8, b)], 92)]
        rows = [''.join(map(str, x)) for x in itertools.product((0, 1), repeat=7)
                if _cone_sat(w, [(76, i + 1, b) for i, b in enumerate(x)], 92)]
        inb = [r for r in rows if tuple(int(c) for c in r) in B[14]] or 'none'
        print('leading %s: x_8(75) can be %s; rows at t = 76: %s; in the backward set: %s'
              % (lead, '/'.join(vals), ' '.join(rows), inb))


def entrymemory():
    """GC1033's request (CL203) with GC1035's repair (CL204): where the leading symbol's memory sits during the train.
    Entry + ten cars only (no exit) for the SAT sets. (1) Cells forced at t = 5, 10, 15, 20, 30 over sites 1 .. 45, both
    leads. (2) The exact sets of sites 7 .. 18 at t = 30 (SAT, 4096 calls a lead; printed and retained), each state
    prefixed by the known slab 100110, propagated as 18 cells under the real clock with a free site 19, filtered at
    the white ticks by the word's samples (cars at 30 .. 66, then 0, 0, 1 at 70, 72, 74) and by the gates (site 7 = 0
    at 30 .. 58, = 1 at 62), to t = 75. Runtime about ten minutes."""
    import itertools
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    def forced_row(word, t, sites, tmax):
        out = ''
        for i in sites:
            c0, c1 = _cone_sat(word, [(t, i, 0)], tmax), _cone_sat(word, [(t, i, 1)], tmax)
            out += '0' if c0 and not c1 else '1' if c1 and not c0 else '?'
        return out
    tail, train, exit9 = '00010001010000', '10' * 10, '001000010'
    for t in (5, 10, 15, 20, 30):
        rows = {lead: forced_row(lead + tail + train, t, range(1, 46), 80) for lead in ('0', '1')}
        diff = [i + 1 for i, (a, b) in enumerate(zip(rows['0'], rows['1'])) if a != b]
        print('t = %2d: lead 0 %s | lead 1 %s | differ at sites %s' % (t, rows['0'], rows['1'], diff))
    sets = {}
    for lead in ('0', '1'):
        w = lead + tail + train
        sets[lead] = sorted(x for x in itertools.product((0, 1), repeat=12)
                            if _cone_sat(w, [(30, 7 + j, b) for j, b in enumerate(x)], 76))
        print('lead %s: exact set of sites 7 .. 18 at t = 30: %d states: %s'
              % (lead, len(sets[lead]), ' '.join(''.join(map(str, x)) for x in sets[lead])), flush=True)
    print('leading-0 set within the leading-1 set:', set(sets['0']) <= set(sets['1']))
    slab = tuple(int(c) for c in '100110')
    samples = {30 + 4 * k: 1 for k in range(10)}
    samples.update({70: 0, 72: 0, 74: 1})
    for lead in ('0', '1'):
        S = {slab + x for x in sets[lead]}
        for t in range(30, 75):
            if t % 2 == 0 and t in samples:
                S = {x for x in S if x[0] == samples[t]}
            if t % 4 == 2 and t <= 62:
                S = {x for x in S if x[6] == (1 if t == 62 else 0)}
            S = {tuple(step_bits(list(x), t % 2, e)) for x in S for e in (0, 1)}
        print('lead %s: 18-cell propagation to t = 75: %d states; sites 1 .. 8 forced = %s; x_7 %s; x_8 %s'
              % (lead, len(S), ''.join('0' if all(x[i] == 0 for x in S) else '1' if all(x[i] == 1 for x in S) else '?'
                                        for i in range(8)), sorted({x[6] for x in S}), sorted({x[7] for x in S})))


def past():
    """GC1037's backward propagation (CL207), own code. From the eight row-30 fillings with cells 16 and 20
    black (the 19
    common pins of CL198 held), reverse Rule 30 exactly under the clock (each parent is fixed by its two rightmost
    cells and left-permutivity, with the wall checked), imposing the entry's samples at t = 2 .. 28 and leaving t = 0
    free: every row at t = 0 that survives begins with 1, so the leading 0 excludes a black (16, 20) origin. Then the
    common-pin test: do the train, the exit bits and the gates alone force the 11 common pins beyond sites 1 .. 8 at
    t = 30 in a free-exterior row of width 24? (They do not: only sites 1 .. 8 are common to the survivors.)"""
    import itertools
    def step_bits(bits, wall, ext):
        r = [wall] + bits + [ext]
        return [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1)]
    entry = '000010001010000'
    base = list('100110011001100?000???1?')
    free = [i for i, c in enumerate(base) if c == '?']
    def parents(child, t):
        out = []
        for p24 in (0, 1):
            for p25 in (0, 1):
                p = [None] * 26
                p[24], p[25] = p24, p25
                for i in range(24, 0, -1):
                    p[i - 1] = child[i - 1] ^ (p[i] | p[i + 1])
                if p[0] == t % 2:
                    out.append(tuple(p[1:25]))
        return out
    layer = {}
    for c, d, e in itertools.product((0, 1), repeat=3):
        row = base[:]
        for i, v in zip(free, (1, 1, c, d, e)):
            row[i] = str(v)
        r = tuple(int(x) for x in row)
        layer[r] = {r}
    peak = len(layer)
    for t in range(29, -1, -1):
        new = {}
        for child, labels in layer.items():
            for q in parents(child, t):
                if t % 2 == 0 and t >= 2 and q[0] != int(entry[t // 2]):
                    continue
                new.setdefault(q, set()).update(labels)
        layer, peak = new, max(peak, len(new))
    srcs = set().union(*layer.values()) if layer else set()
    print('rows at t = 0 from a black (16, 20) origin, entry samples 2 .. 28 imposed: %d, all beginning 1: %s, peak %d'
          % (len(layer), all(r[0] == 1 for r in layer), peak))
    print('fillings (16, 20, 21, 22, 24) with a past:', sorted(''.join(str(r[i]) for i in free) for r in srcs))
    word = '0' + entry[1:] + '10' * 10 + '001000010'
    samples = {2 * k: int(c) for k, c in enumerate(word)}
    inits = [tuple(int(c) for c in '10011001') + x for x in itertools.product((0, 1), repeat=16)]
    cur = {}
    for k, r in enumerate(inits):
        cur[r] = cur.get(r, 0) | (1 << k)
    for t in range(30, 87):
        if t in samples:
            cur = {r: m for r, m in cur.items() if r[0] == samples[t]}
        if t % 4 == 2 and 34 <= t <= 62:
            cur = {r: m for r, m in cur.items() if r[6] == (1 if t == 62 else 0)}
        if t == 86:
            break
        nxt = {}
        for r, m in cur.items():
            for e in (0, 1):
                c = tuple(step_bits(list(r), t % 2, e))
                nxt[c] = nxt.get(c, 0) | m
        cur = nxt
    alive = 0
    for m in cur.values():
        alive |= m
    surv = [inits[k] for k in range(len(inits)) if (alive >> k) & 1]
    common = ''.join('0' if all(r[i] == 0 for r in surv) else '1' if all(r[i] == 1 for r in surv) else '?'
                     for i in range(24))
    print('common-pin test, width 24: %d of 65536 rows survive the train, exit bits and gates; common cells %s'
          % (len(surv), common))
    # GC1038's two checks: pin 23 released (18 pins, width 24) and the prefix-15-only template at width 20
    def pasts(template, W):
        frees = [i for i, c in enumerate(template) if c == '?']
        lay = {}
        for bits in itertools.product((0, 1), repeat=len(frees)):
            row = list(template)
            for i, v in zip(frees, bits):
                row[i] = str(v)
            lay[tuple(int(x) for x in row)] = 1
        pk = len(lay)
        for t in range(29, -1, -1):
            nxt = {}
            for child in lay:
                for a in (0, 1):
                    for b in (0, 1):
                        q = [None] * (W + 2)
                        q[W], q[W + 1] = a, b
                        for i in range(W, 0, -1):
                            q[i - 1] = child[i - 1] ^ (q[i] | q[i + 1])
                        if q[0] != t % 2 or (t % 2 == 0 and t >= 2 and q[1] != int(entry[t // 2])):
                            continue
                        nxt[tuple(q[1:W + 1])] = 1
            lay, pk = nxt, max(pk, len(nxt))
        return sorted(lay), pk
    for name, tpl, W in (('pin 23 released, width 24', '1001100110011001' + '000' + '1' + '????', 24),
                         ('prefix 15 only, width 20', '100110011001100' + '1' + '???' + '1', 20)):
        rows0, pk = pasts(tpl, W)
        print('%s: rows at t = 0 %d, with a leading 0 %d, peak %d'
              % (name, len(rows0), sum(r[0] == 0 for r in rows0), pk))


def joint():
    """GC1039's joint entry-and-exit relation (CL210), own code. Forward from t = 30 at width 24 with a free exterior
    (first 8 sites fixed, 16 free), filtered by the 44-prefix's samples to t = 86 and the site-7 gates, then reversed
    exactly through the kept layers to the origins with a future (CL207's 581); then those origins reversed to t = 0
    under the whole entry, leading 0 included. Also the wrong-x8 branch, the width-12 slab support, and the
    leading-0 relaxation as the unexpected check."""
    import itertools
    entry = '000010001010000'
    word = entry + '10' * 10 + '001000010'
    samples = {2 * k: int(c) for k, c in enumerate(word)}

    def step_bits(bits, wall, ext):
        r = (wall,) + bits + (ext,)
        return tuple(r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(bits) + 1))

    def parents(child, t, W):
        out = set()
        for a, b in itertools.product((0, 1), repeat=2):
            p = [None] * (W + 2)
            p[W], p[W + 1] = a, b
            for i in range(W, 0, -1):
                p[i - 1] = child[i - 1] ^ (p[i] | p[i + 1])
            if p[0] == t % 2:
                out.add(tuple(p[1:W + 1]))
        return out

    def keep(t, r):
        if t in samples and r[0] != samples[t]:
            return False
        if t % 4 == 2 and 34 <= t <= 62 and r[6] != (1 if t == 62 else 0):
            return False
        return True

    def origins_with_future(prefix, W=24):
        head = tuple(int(c) for c in prefix)
        layers = {30: {r for r in (head + x for x in itertools.product((0, 1), repeat=W - len(head))) if keep(30, r)}}
        for t in range(30, 86):
            layers[t + 1] = {s for r in layers[t] for e in (0, 1) for s in (step_bits(r, t % 2, e),) if keep(t + 1, s)}
        cur = layers[86]
        for t in range(85, 29, -1):
            cur = {p for s in cur for p in parents(s, t, W) if p in layers[t]}
        return cur, max(len(l) for l in layers.values())

    def entry_pasts(origins, leading0=True, W=24):
        src = sorted(origins)
        rows = {r: 1 << i for i, r in enumerate(src)}
        peak = len(rows)
        for t in range(29, -1, -1):
            nxt = {}
            for child, m in rows.items():
                for p in parents(child, t, W):
                    if t % 2 == 0 and (t > 0 or leading0) and p[0] != int(entry[t // 2]):
                        continue
                    nxt[p] = nxt.get(p, 0) | m
            rows, peak = nxt, max(peak, len(nxt))
        alive = 0
        for m in rows.values():
            alive |= m
        return [r for i, r in enumerate(src) if alive >> i & 1], len(rows), peak

    def slab_support(W=12):
        rows = {tuple(int(c) for c in '1001100') + x: 0 for x in itertools.product((0, 1), repeat=W - 7)}
        peak = len(rows)
        for t in range(33, 19, -1):
            nxt = {}
            for child, m in rows.items():
                for p in parents(child, t, W):
                    if t % 2 == 0 and p[0] != samples[t]:
                        continue
                    lab = (1 << sum(b << i for i, b in enumerate(p[:8]))) if t == 30 else m
                    nxt[p] = nxt.get(p, 0) | lab
            rows, peak = nxt, max(peak, len(nxt))
        alive = 0
        for m in rows.values():
            alive |= m
        return sorted(format(k, '08b')[::-1] for k in range(256) if alive >> k & 1), peak

    def common(rows):
        return ''.join(str(rows[0][i]) if all(r[i] == rows[0][i] for r in rows) else '?' for i in range(len(rows[0])))

    o1, pk1 = origins_with_future('10011001')
    print('first 8 = 10011001: origins with a future %d (CL207: 581), forward peak %d' % (len(o1), pk1))
    j1, n0, pk = entry_pasts(o1)
    print('  with an entry past, leading 0 included: %d, rows at t = 0 %d, past peak %d, common %s'
          % (len(j1), n0, pk, common(j1) if j1 else '-'))
    jp1 = len(j1) == 2 and common(j1) == '10011001100110000000001?'
    print('JP1', 'HELD' if jp1 else 'REFUTED')
    r1, n0r, pkr = entry_pasts(o1, leading0=False)
    print('  unexpected check, leading 0 relaxed: %d origins keep a past (rows at t = 0 %d, peak %d), common %s'
          % (len(r1), n0r, pkr, common(r1) if r1 else '-'))
    print('JP4', 'HELD' if len(r1) >= 10 else 'REFUTED')
    o0, pk0 = origins_with_future('10011000')
    j0, _, pk = entry_pasts(o0)
    print('first 8 = 10011000: origins with a future %d (GPT: 4975), with an entry past %d (GPT: 0), past peak %d'
          % (len(o0), len(j0), pk))
    print('JP2', 'HELD' if (len(o0), len(j0)) == (4975, 0) else 'REFUTED')
    pats, pk = slab_support()
    print('slab 1001100 at t = 34, width 12, back to t = 20: first-8 patterns at t = 30 %s, peak %d' % (pats, pk))
    print('JP3', 'HELD' if pats == ['10011000', '10011001'] else 'REFUTED')


if __name__ == '__main__':
    cmd, a = sys.argv[1], [int(x) for x in sys.argv[2:]]
    t0 = time.time()
    {'member': lambda: member(*(a or [200])), 'seeds': lambda: seeds(*(a or [12, 400])),
     'block': lambda: block(*(a or [20000, 24])), 'periods': lambda: periods(*(a or [40000, 40])),
     'boundary': lambda: boundary(*(a or [8, 10])), 'memory': lambda: memory(*(a or [4, 16])),
     'follower': lambda: follower(*(a or [13])), 'carrier': carrier, 'packet': packet, 'arming': arming,
         'cut45': cut45,
     'separator': separator, 'entrymemory': entrymemory, 'past': past, 'joint': joint}[cmd]()
    print('(%.0f s)' % (time.time() - t0))
