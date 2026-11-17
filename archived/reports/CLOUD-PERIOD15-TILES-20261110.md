# Period 15: two and three freely joining 31-cell tiles (K-09, first step)

Cloud, CL774 and CL775, 10 November 2026, at the owner's word. This sizes row K-09 of the kit-candidate table in
[WARM-LEADS](../WARM-LEADS.md). It builds nothing for the kit and is not a prize statement.

**Outcome.** The positive-entropy half of K-09 is small. At period 15 there are two freely joining tiles of
31 cells at every branch vertex, and three at half of them. A kernel certificate for two tiles would check 1,860
local equations; the kit's period-12 module checks 1,632 for its two 34-cell tiles. The other half of K-09, that
periods 13 and 14 have no positive entropy, still needs strip certificates of the kind the kit holds for periods
1 to 11, and is the large part.

## 1. What was read off the census core

[Probe](../tests/probes/swarm/sw02/carry/cloud_period15_tiles.py),
[output](../tests/probes/swarm/sw02/carry/cloud_period15_tiles.out),
[first run](../tests/probes/swarm/sw02/carry/cloud_period15_tiles_run1.out),
[the 606 core pairs](../tests/probes/swarm/sw02/carry/cloud_core15_pairs.txt) from `cloud_core_census.c` (CL772).
Predictions K1 to K5 were pushed first (CL774).

Frame, as before: a pair (c, d) of 15-tick profiles at sites i+1, i+2 has children (u, c) with
u(t+1) = u(t) xor (c(t) or d(t)). In the kit's words a path is a row x with `orbit x 15 = x`, that is
evol x 15 (i + 15) = x i.

COMPUTED:

| Fact | Value |
|---|---|
| Branching component | 525 pairs, 555 edges, every pair of least period 15 |
| Branch vertices | 30, in two rotation classes of 15 |
| Stretches between branch vertices | 60, of 3, 7, 9 and 27 cells, fifteen of each; none returns to its own start |
| Shortest cycle | 31 cells |
| Growth rate | 1.087715, so 0.1213 bits per cell (LN-12's number, second code) |
| Least length with two closed walks at one vertex | 31 cells, at all 30 branch vertices |
| Closed walks of 31 cells | two at 15 branch vertices, three at the other 15 |
| Weights of the two continuing children | 7 and 8 at all 30 branch vertices |

## 2. The tiles

A tile is the 31 new columns of a closed walk, read at tick 0, in increasing site order. The full 15-tick
profile lists are in the output for a builder.

At the vertex (5293, 7347), two tiles, differing in cells 20 and 21 only:

```
1100100000001111010110110110011
1100100000001111010101110110011
```

At the vertex (5461, 23930), three tiles:

```
1010111000011111001010010011110
1010110110110011110010000000111
1010111000011111001010000000111
```

Each set is a set of closed walks at one vertex, so any two-sided string of its tiles is a path in the component
and hence a row that returns after 15 steps at light speed. The tiles of a set are distinct, so by the usual
determinism argument (GC2830, carried CL768) the coding is injective. Every pair in the component has least
period 15, so every coded row has least return period 15.

Controls, COMPUTED: every ring built from a word of 1 to 4 of the two tiles (30 rings), and of 1 to 3 of the three
tiles (39 rings), returns after 15 moving steps, satisfies the ordinary-rule form of the law, and does not return
after 1, 3 or 5 steps.

Entropy from the codes: 1/31 = 0.0323 bits per cell with two tiles, log₂3 / 31 = 0.0511 with three, against
0.1213 for the whole component.

## 3. Predictions

| Prediction | Outcome |
|---|---|
| K1 (0.7): two closed walks of one length at some branch vertex, least length at most 150 | PASS: 31 |
| K2 (0.9): growth rate 1.0877 | PASS: 1.087715 |
| K3 (0.95): rings from the tiles return after 15 and not after 1, 3, 5 | PASS |
| K4 (0.5): exactly two closed walks at the least length, not three | HALF: two at one rotation class, three at the other. The three-tile alphabet of period 12 is not special |
| K5 (0.4): the two continuing children have weights 7 and 8 at every branch vertex | PASS |

On K5, for GPT: at period 12 the split was 5 and 7, equal parity; at 15 it is 7 and 8, as it must be for
complements over an odd period. The common feature is only that the two children are as balanced as the period
allows.

## 4. What this does to row K-09

K-09 splits.

- **K-09a, positive entropy at period 15.** Statement in the kit's form: an injective coding of two-sided binary
  (or ternary) sequences into rows with exact minimal return period 15, by two (or three) 31-cell tiles. Size:
  the same as the period-12 half of `Rule30MovingWaves`, with 1,860 seam equations in place of 1,632. Status:
  COMPUTED by one code on a core that two codes agree on in size. **Wants GPT's independent check of the tiles**
  before Local builds. Small to medium.
- **K-09b, no positive entropy at 13 and 14.** The census says both cores are plain cycles (143 pairs at 13;
  cycles of 14, 21, 21 and the rain at 14). A kit proof needs strip certificates like `low_period_linear_words`,
  which rests on eleven SAT certificate modules for periods 1 to 11. Large, Intel-scale, and not started.
- Without K-09b the honest headline is "period 15 also carries an exponential language", not "15 is the next
  after 12".
