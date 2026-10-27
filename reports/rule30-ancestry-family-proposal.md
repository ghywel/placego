# A candidate family with compulsory ancestry (L1044)

Local, 27 October 2026. GC1997 asked for one explicit suffix family w_k, before any more enumeration, with three
parts:
- d(w_k) finite and unbounded;
- the obligation that would force every late realization back to a start-only head;
- cheap alternatives answered first.

This note is reasoning only. Nothing was run except a hand-equivalent screen of the family against already-recorded
words. The screen inputs are the factor law, the certified deaths d(0010001) = 32, d(1000101) = 34 and
d(10001001) = 17, and L1041's short post-reset forbidden gap words. Gap words follow GC1997's endpoint rule: they are
complete words that start and end with 1.

## 1. Two constraints any unbounded family must meet (proved, from the factor law)

**(N) Non-nesting.** If w_j is a factor of w_k at offset o, then d(w_k) ≤ d(w_j) − o. So a family whose members
extend earlier members has non-increasing deaths. This rules out "longer train, same defect" families such as
T^a·D·T^b.

**(C) No common mortal factor.** If every w_k contains a fixed word v with d(v) < ∞, then d(w_k) ≤ d(v) for all k.
So the members' shared building blocks must all be eternal (d = ∞), and each finite death must come from the
*separation* between them. This is the even-shift pattern GC1997 raised: there, 10^(2k+1)1 is forbidden for every k,
while every proper factor is allowed.

**Screening consequence (proved, given the three certified deaths).** Any word with d ≥ 35 avoids 0010001, 1000101
and 10001001. So:
- a gap 3 is never preceded by a gap ≥ 2;
- it is never followed by 1 or 2;
- since (3,3) contains 0010001, it is followed only by 4.

Hence, away from the word's two ends, **gap 3 occurs only inside (1,3,4)**.

The record's length-20 control, with d = 43 and gaps (1,1,3,4,1,1), obeys this. That is a consistency check I did
not set up for it.

## 2. The candidate

Two eternal trains joined twice. The visible gap-1 train (10)^∞ is eternal: 8.86, the right half (1001100)^∞. Gap-2
trains are reported eternal by the record (the two-gap train, CL189/L595, PROVED). *Caveat:* the older notes
sometimes count distances rather than zeros, so this must be checked to mean gap 2 in our convention.

The junctions are forced by the post-reset tables:
- **1 → 2** cannot be direct, since (1,2) is not in Λ. A gap 3 needs the context (1,3,4), so the shortest bridge is
  (1,3,4,2). Its factors (3,4,2) and (4,2,2) are not on L1041's list.
- **2 → 1** cannot be direct, since (2,1) and (2,3) are not in Λ. (2,4,1) and (2,4,3) are also excluded, so the
  shortest bridge is (2,4,4,1). (1,4,4,1) is excluded, but (2,4,4,1) is not.

**Family.** For k ≥ 1:

    F_k  =  gap word (1, 1, 3, 4, 2^k, 4, 4, 1, 1),

that is, the binary word 1·(0^g 1 over the gaps). Its lengths are 31, 34, 37, 40 and 43 for k = 1 to 5.

**Screen** (by hand, mechanical): for k = 1 to 5, F_k contains none of the 18 short post-reset forbidden gap words
and none of the three late-dead words. (N) holds, since the separation k differs between members. Whether (C) holds
is exactly obligation O1.

## 3. The compulsory-ancestry obligation

To prove d(F_k) < ∞ and d(F_k) → ∞, three things are needed.

- **O1. Eternal parts.** The one-junction words A_m = (1,1,3,4,2^m) and B_m = (2^m,4,4,1,1) have d = ∞ for every
  m, or at least d → ∞ uniformly in m. Without this, (C) caps the family. This is the first thing to settle.
- **O2. Finite death: the ancestry step.** For each k there is J_k such that F_k occurs at no age j ≥ J_k. The
  mechanism to prove is *shielding*:
  - while a gap-2 train runs beside the wall, the near-wall region is locked to the train's background (compare the
    forcing results G205/G208, and the reset tracks of L1040);
  - so the exit junction (2,4,4,1) after k train periods must be caused by a disturbance that was already inside a
    bounded unlocked window at the entry junction's reset row;
  - **the content of that window must be compulsory**: it must be a configuration only an initial row can carry,
    like 0110 for z, so every late realization is excluded.

  8.60 §1 shows the wall often never sees the far right ("the wall never sees the far end", 37.6% of sister pairs).
  It also shows the opposite happens, at a median of 34 steps. So O2 must exclude *every* late injection from the
  right through the train, not just typical ones.
- **O3. Growth.** Realizations of F_k at ages r_k → ∞, so d(F_k) > r_k. A construction would place the two junction
  causes at distances that grow with k in the initial row.

## 4. Cheap alternatives, answered or ranked

| Alternative | Status |
|---|---|
| A nested family (longer trains around one defect) | Ruled out by (N). |
| A family built around the 43 control's defect | Ruled out by (C) unless (1,3,4,1)-type factors are eternal. Not known. |
| F_k is not in L at all | Open. The first kill test, membership of F_1…F_5 in the certified list, is cheap: lengths ≤ 43. |
| F_k is eternal (O2 fails), because injections from the right can pass the train | Open. Plausible given 8.60's 62% of sister pairs that do see the change. This is the likely failure. |
| A junction is itself mortal (O1 fails) | Open. Check d(A_m) and d(B_m) for small m where decidable. |

**Predictions, written before any test.**
- K1: F_1…F_5 are all in L. Gut 60%.
- K2: d(A_m) and d(B_m) are beyond the certified range, i.e. no finite death is visible, for m ≤ 3. Gut 50%.
- That F_k has finite and unbounded deaths: gut **15%**.

The likeliest outcome is that O2 fails because the train does not shield. Then F_k is eternal, and the family idea
moves to junction pairs inside a train that is proved to shield.

**Order of work proposed.**
1. K1 and K2: certified-list look-ups only, bounded and seconds long.
2. Only then, a hand attempt at O2's shielding lemma for the gap-2 train using the reset tracks.

No other enumeration.

## 5. Result: the family fails its own quick tests (L1045, same evening)

Following the owner's guidance, I ran the cheap tests and checked the record myself instead of deferring them. These
are all look-ups in the certified phase-0 list, using GC1997's rule that g ∈ Λ iff 0W(g) ∈ L.

- **The convention question, answered from the record.** The eternal "two-gap train" counts distances, not zeros.
  GC1017 writes its white-time word as (10)^N, and CL189 says column 1 reads 1100 repeating. So it is our **gap-1**
  train. No train with gaps of 2 in our convention is known to be eternal, so O1's premise for gap-2 trains was
  unsupported.
- **K0.** Runs of n gap-2s after a reset are legal for every n ≤ 14 the list can decide. This is consistent with an
  eternal gap-2 train, but does not prove one.
- **K1, predicted 60% yes: refuted.** F_1…F_5 are not in L at all, at age 0 or after a reset. The exit bridge is
  mortal:
  - B_1 = (2,4,4,1,1) has d = 6;
  - B_2 = (2,2,4,4,1,1) has d = 1;
  - B_m is illegal for m ≥ 3, killed by the certified word 01001001000010000101, gaps (2,2,4,4,1).
- **K2.** The entry words A_m = (1,1,3,4,2^m) are legal, and their pasts run past the certified range for m ≤ 4, so
  no finite death is visible.
- **Red team, all short exits.** After a gap-2 run of length 3, 6 or 9 following a reset, no bridge of at most 3 gaps
  reaches a gap-1 train.
- **A broader guess killed at once.** I guessed that "after a post-reset gap 2, all later gaps are 2 or 4". It is
  false: gaps 1 and 3 still occur in the legal continuations.
- **The decisive test, for memory.** The fewest gaps from a run of m 2-gaps to the first gap 1:
  - (4,4,1) for m = 1;
  - (4,4,4,4,1) for every m from 2 to 6;
  - m ≥ 7 is beyond the list's length, so no information.

  The exit delay does not grow with the run length. **The gap-2 run carries no memory of its length** in the
  decidable range. That is the opposite of what O2's shielding-with-memory mechanism needs.

**Verdict.** F_k is withdrawn, refuted by K1. The natural repair, exiting via (4,4,4,4), would also lack memory,
since the exit delay is constant. So I propose no replacement family yet.

**The lesson for any next candidate.** A family with unbounded deaths needs a regime whose *exit delay grows with
its length*: a counter that is never saturated. Two regimes have now been measured:
- the 3-run saturates at six (L1042);
- the 2-run's exit saturates at four 4-gaps.

The first test for any new candidate is therefore the exit-delay curve, which is a cheap look-up in the certified list.
