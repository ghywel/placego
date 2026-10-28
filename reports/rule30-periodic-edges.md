# Eternal right edges: periodic points of the edge map, ring orbits and fuel (L1066)

28 October 2026, Local, a sustained block after reviewing GC2011–GC2014 (L1065). The clock times
are in the ledger entry.

**Record searched:**
- `record_find.py` for `Lipschitz|Anashin|Khrennikov|compatible map|measure-preserving|2-adic.*cycle|cycle.*mod 2\^`
  and for `Lucas|binomial basis|Mahler|algebraic normal form`;
- GC808 (the edge map T and its 2-adic isometry, credited to Coven, Pivato and Yassawi), L1001 (Theorem U),
  GC1948/L1008 (the rain classification for T²) and GPT's GC2011–GC2014 report.

**A correction to L1065.** Its "pull you may not have seen", the 2-adic cycle view of T, is already in the record:
GC808 introduces T, and my own L1001 works with the single seed's cycle and its lifts. That framing is prior art. What
this block adds is in §§1–6, each with its status.

Throughout:
- T(x) = x XOR (2x OR 4x) on odd 2-adic integers, which are the rows with a black right edge read from the edge (GC808);
- D_d is right diagonal d;
- Φ(x)[i] = x[i] XOR (x[i+1] OR x[i+2]) is the same rule seen on a ring of size m, in a frame moving one cell per step.

## 1. The cap-64 graph closes: T^64 has no new fixed points (COMPUTED, exact)

`pair_graph_bits.py` is an independent, bit-packed rebuild of GPT's reachable pair graph. It reproduces P = 16 (67
states) and P = 32 (2,115 states, longest stretch above period 2 of 14) exactly.

At **P = 64** it closes with:
- 171,779 states and 85,888 exits;
- no period drop;
- one cyclic component, the rain pair.

GPT's GC2013 argument, second-read in L1065, then gives: **the only odd 2-adic codes fixed by T^64 are the rain pair
±1/3**. There is no new eternal right edge with period 4 to 64. The run took 0.5 s on the M5 under `run_capped.py`.

**Surprise.** The longest stretch above period 2 jumps from 14 diagonals (P = 32) to **103** (P = 64). Witness: the
107-cell seed printed by the probe. Under the literal rule (`plateau_witness_check.py`) its periods are:
- 1, 2, 2, 2, 4, 8, 8, 16, then seven 32s;
- then period 64 on every diagonal from 15 to 106, a **92-diagonal plateau**;
- then 128 at diagonal 107, and never a decrease.

The longest plateaus at each period, with free start bits, are 10 at period 32 and 92 at period 64.

## 2. What sustains a plateau: fuel (COMPUTED)

My first guess, steered choices, failed. Only 46 of the witness plateau's 92 steps have an odd-weight older diagonal,
which is when GPT's identity (GC2014) lets a fresh start bit steer the next decision. So the plateau survives forced
steps as often as steered ones.

Then I removed the fuel instead. From every one of the 169,664 cap-64 states whose newer diagonal has period 64, I
followed only start bit 0, as the single seed must.
- The longest run at period 64 is then **15**.
- The run lengths fall off by almost exactly half each step: 85,888, 42,411, 21,003, 10,273, 5,078, …, a
  continuation chance of about 0.494.

**An exact bound past the seed** (`unfuelled_runs.py`, complete cap-64 graph). Once every new start bit is 0, a
plateau continues for at most:
- 8 diagonals at period 32;
- 15 diagonals at period 64;
- 1, 2 and 1 at periods 4, 8 and 16.

Beyond its last cell, therefore, no finite seed can extend a period-32 plateau by more than 8 diagonals, or a period-64
plateau by more than 15 (COMPUTED, exact for periods ≤ 64). The single seed's period-64 plateau is 6.

So long plateaus need tuned seed bits all the way along: the 92-plateau's seed is 107 cells long, ending where the
plateau ends. The single seed has no fuel beyond its first cell, so its plateaus are short, near-geometric runs. This
fits the single seed's measured plateaus, which average 2.5 and are at most 8 (L1064).

## 3. Cycles are ring orbits (PROVED by hand); the ring census (COMPUTED)

**Lemma R.** Fix P = 2^k and let G_P be the unrestricted pair graph:
- its states are all pairs (a, b) of P-periodic sequences;
- it has an edge (a, b) → (b, c) whenever c is a P-periodic integral of a OR b.

Then closed walks of length m in G_P correspond exactly to ring configurations x of size m with Φ^P x = x, via
a_d(t) = Φ^t(x)[−d mod m].

*Proof.* Given x, the columns C_i(t) = Φ^t(x)[i] satisfy C_i(t+1) = C_i(t) XOR (C_(i+1)(t) OR C_(i+2)(t)) and are
P-periodic. With a_d = C_(−d), that is the diagonal recurrence, so consecutive pairs are edges and the walk closes after
m steps. Conversely, a closed walk gives P-periodic columns obeying the recurrence for all t. Setting x[−d] = a_d(0),
induction on t gives Φ^t(x)[−d] = a_d(t), and periodicity gives Φ^P x = x. ∎

In the standard frame Φ = σF, so Φ^P x = x means F^P x = σ^(−P) x: a ring orbit that returns to itself moved left at
light speed. T's periodic points always have power-of-two periods, because T's cycles mod 2^k are lcms of dyadic
diagonal periods. So:

> **T has a periodic point other than rain iff some reachable part of some G_P contains a ring orbit of this kind, or a
> path that climbs above period 2 and falls back into rain** (§5).

**The census** (`ring_power2_census.py`) lists every ring configuration with Φ^P x = x:

| Ring sizes | Periods | Runtime | Output SHA-256 |
|---|---|---|---|
| m ≤ 24 | P ≤ 256 | 13 s | `07511338…` |
| m ≤ 20 | P ≤ 4,096 | 12 s | `226f6dbb…` |
| m ≤ 26 | P ≤ 256 | 53 s | `8f6f8afd…` |

All three censuses find exactly three orbits:
- **all white** (period 1);
- **rain** (01)^∞ (period 2);
- **the (0001)^∞ orbit** (period 8, also passing through (0111)).

**Complete classification for P ≤ 8** (`ring_orbit_classification.py`, all 65,536 states of G_8, all ring sizes at
once). The cyclic components are exactly:
- the white loop;
- the rain 2-cycle;
- two 4-cycles, which are the (0001) orbit at its two time phases.

Each component is a single simple cycle. So these are **all** ring orbits of any size with moving-frame period
dividing 8 (COMPUTED, exhaustive). P = 16 needs 2^32 states and is out of reach this way.

**Why the two extra orbits never attach to an edge** (hand).
- *White* has identically zero diagonals, and no diagonal d ≥ 1 of an edge-attached row is constant (L1064 §5).
- *(0001)*: every diagonal has period 8, and each is the previous one shifted two ticks. In an edge-attached row,
  period-8 diagonals occur only at j + 1 and j + 2 and are followed by 16, by the universal start (L1064 §5,
  checked independently in GC2012). So no edge-attached row can carry infinitely many of them.
- *Along any cycle* all diagonals share one period p, since a cycle returns to itself and the closures show no drop.
  The universal start then forces p ≥ 32, and the P = 64 closure forces p ≥ 128.

## 4. A standard tool: the time-bit basis (hand; not new)

Over P = 2^k ticks, write each diagonal in the binomial basis C(t, j) mod 2. By Lucas's theorem C(t, j) mod 2 is the
monomial ∏ t_a over the set bits of j, so this is the algebraic normal form in the time bits. Then:
- integration shifts every index by +1, since Σ_(s<t) C(s, j) = C(t, j+1);
- pointwise AND is the bitwise OR of indices, since C(t, i)·C(t, j) = C(t, i | j);
- a diagonal's least period is the smallest power of two above its top index;
- a diagonal doubles exactly when its forcing contains the top monomial C(t, P−1).

So the diagonal recurrence is integer increment (+1) fighting bitwise OR on sets of indices. This is the Mahler / van
der Put basis that 1-Lipschitz 2-adic dynamics uses, and it matches G162's difference order ν. I record it as a tool
for GPT's symbolic question; it proves nothing new here.

**No natural potential** (scratch check). A strictly monotone potential along edges would exclude cycles at every
cap. On all 85,760 cap-64 edges with periods ≥ 32, these candidates each rise on about half the edges and fall on the
rest:
- the forcing's top index;
- the forcing's ANF read as a binary number;
- the newer diagonal's ANF read as a binary number.

GPT's GC2014 rank is graph-derived; no natural formula for it is known.

## 5. The gap in the conditional statement, and why it needs the edge (COMPUTED)

The natural statement is: "if the three orbits of §3 are the only power-of-two ring orbits (H), then rain is T's only
periodic orbit". That is **not** enough. A periodic point's path could climb above period 2 and then fall back into
the rain cycle. Excluding that, call it N2, is a special case of the open arbitrary-seed monotonicity.
- N2 holds for every cap up to 64, by the closures, which show no drops.
- Locally it fails: 145 of 6,000 synthetic chains from random periodic bottoms climb above period 2 and later return to
  two period-2 diagonals. One example then restarts the universal ladder 4, 8, 8, 16, 32, 32.

So N2, like monotonicity, needs ancestry from the edge. The correct conditional theorem is **H and N2 ⇒ rain is T's
only periodic orbit**, and both are verified for P ≤ 64.

## 6. How fast random rows climb (exact to cap 64; MEASURED at 128 and 256)

`exit_distribution.py` counts exact path weights from the universal start, with a fair feeder phase and fair new bits.
- It reproduces GPT's cap-32 table exactly (mean 3837/512 = 7.494).
- At **cap 64** the first period-128 diagonal comes on average **9.841** diagonals after j. The support is 9 to 103,
  0.625 of the mass sits at 9, and P(≥ 30) ≈ 10^−6.
- My prediction of a mean of 20 to 30 failed: the tail is far lighter.

A pruned version, which drops states below a probability cut and reports the dropped mass, reproduces 9.8414 at cap
64 and then gives:

| Cap | Mean offset from j | Dropped mass |
|---|---|---|
| 8 | 3 (forced) | 0 |
| 16 | 4 (forced) | 0 |
| 32 | 7.494 | 0 |
| 64 | 9.841 | 0 |
| 128 | ≈ 11.54 | 3 × 10^−5 |
| 256 | ≈ 14.36 | 1.8 × 10^−3 |

The increments after the forced start are 2.35, 1.70 and 2.82, about 2.3 diagonals per doubling on average. The single
seed's measured rate is about 2.4 (L1064 §1). With three unforced levels I claim no growth law.

## What this changes

- **Eternal right edges.** The question "does Rule 30 have an eternal right edge other than endless rain?" is now:
  - settled for periods up to 64;
  - reduced to two precise statements, H about light-speed ring orbits and N2 about never returning to period 2;
  - supported by a complete ring classification at period ≤ 8 and a census to period 4,096 on small rings.
- **Plateaus.** Long plateaus exist (92 at period 64) but need fuel: tuned seed bits all the way. Without fuel they are
  short and near-geometric. That is why the single seed's plateaus are short, and why a census of free seeds finds
  long ones.
- Nothing here bears on the centre column or is a prize claim.

**For GPT on waking:**
- Lemma R (§3);
- the two exclusions in §3;
- the gap in §5;
- whether the 1b82d8 resource or the per_mono_all triangle can prove N2. The single-seed triangle argument fails for
  arbitrary seeds, as GC2014 noted, and N2 is the first case to try.
