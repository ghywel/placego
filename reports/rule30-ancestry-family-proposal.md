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
