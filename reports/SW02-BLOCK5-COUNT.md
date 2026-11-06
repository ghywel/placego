# Block 5: the count in class units, and where it stops

*Local, L1573, 6 November 2026. Block 5 of [WARM-LEADS](../WARM-LEADS.md). Probes: [`tests/probes/swarm/sw02/block5/`](../tests/probes/swarm/sw02/block5/), about 30 CPU seconds on the M5. The theorems here are hand arguments, PROOF-SKETCH until GPT reads them. The tables are COMPUTED, self-check.*

**The answer: the last obstruction is the last fibre, not the main term.** The conditional theorem the block asked for turns out to be nearly empty. Its hypothesis matters only at the level where the class count stops falling, and a stop at that level is exactly an immortal row. So the statistical law on distinct futures, however well it holds in the bulk, does not move Q01. It would, if one immortal row forced far more distinct futures than we know how to force.

## The theorem

Fix W. Let t0 be the last tick of the exact range, and let N_k(W) be the number of distinct rows at tick t0 + 2k among the rows of width at most W that are black at depth 1 at every even tick so far. Survivors at a tick map onto survivors at the next, and some fail, so N_k ≤ N_(k-1), and N_k has a limit q(W): the number of immortal futures at width W. Define β_k by N_k = N_(k-1)(1 + β_k)/2.

**Theorem 1 (the gap).** If y is an immortal row of bit length w, then q(W) ≥ ⌊(W − w)/2⌋ + 1 for every W ≥ w. If Q01 holds, q(W) = 0 for every W. So q(W) = o(W) on an infinite set of widths implies Q01.

*Proof.* G^j y is immortal, of width w + 2j by the width law. For w + 2j ≤ W these rows are survivors at every tick. At tick t their images have widths w + 2j + t, all different, so they are different classes at every tick. For the second statement, survivors of width at most W form a decreasing family of finite sets, so if every N_k is positive some row survives for ever, against Q01. ∎

**Theorem 2 (the law, in its exact strength).** Suppose N_k ≤ ½ N_(k-1) (1 + K N_(k-1)^(-1/2)) at every k with N_(k-1) > K². Then q(W) ≤ K². So if K(W)² ≤ cW with c < ½ on an infinite set of widths, Q01 follows.

*Proof.* If q(W) > K², then N_k = N_(k-1) = q(W) for all large k, and the hypothesis gives 1 ≤ ½(1 + K q^(-1/2)), that is q ≤ K², a contradiction. The corollary is Theorem 1. ∎

**What this replaces.** MM-1 reached the same conclusion through CT-4's Theorem C, with Q_W ≤ 392K² and K(W)² = o(W). No induction, no geometric sum and no two-sided control is needed: the constant is ½, not 1/784, and only the upper side is used. Theorem C remains a true two-sided estimate of how N_k falls, which is about the death time D(W), not about Q01. So Block 6's read of Theorem C can be dropped for this purpose. CT-3's bridge U2(K, c) ⇒ Q01 is the same one line.

## Why it is nearly empty

The hypothesis of Theorem 2 is used at one place only: the level q(W) where the count stops. At every higher level it plays no part. So the bulk of the law, from C(W) ≈ 2^(0.41 W) down to about W/2, could fail wildly and the conclusion would stand, or hold perfectly and the conclusion would not follow from it. What the theorem really asks is that no plateau lasts for ever at a level of at least ⌊(W − w)/2⌋ + 1, and a permanent plateau is q(W) > 0. That is Q01 at width W.

**Named obstruction.** Every statistical statement about the count, in rows or in classes, stops at the last fibre, because the floor forced by an immortal row is only linear in W. A real use for the main term needs a **class amplifier**: a proof that one immortal row forces 2^(εW) immortal rows with pairwise different futures. Then fair decay in the bulk would contradict the floor long before the last fibre, and the coin data would bear on Q01. Nothing known gives that. AM-1: the family forced by one immortal row is exactly its G-orbit. MM-1: every amplifier output shares its future with an orbit row of equal width by tick n. GC2690's 2^3955 rows are rows, not futures.

## Tables (COMPUTED)

K(W) is the largest |β_k| √N_(k-1) over checks with N_(k-1) ≥ 2. Pmax is the largest class count on a plateau. D is the first empty tick. C(40) = 125,401 and D(44) = 78 match the record.

| W | C(W) | D | K | K²/W | Pmax |
|---:|---:|---:|---:|---:|---:|
| 30 | 7,214 | 52 | 2.71 | 0.245 | 1 |
| 31 | 6,796 | 66 | 2.75 | 0.245 | 1 |
| 32 | 12,807 | 66 | 2.45 | 0.187 | 1 |
| 34 | 22,669 | 66 | 2.00 | 0.118 | 4 |
| 36 | 40,239 | 66 | 2.13 | 0.126 | 0 |
| 38 | 71,049 | 72 | 2.41 | 0.153 | 1 |
| 40 | 125,401 | 76 | 2.11 | 0.111 | 0 |
| 42 | 221,428 | 78 | 1.90 | 0.086 | 0 |
| 44 | 390,428 | 78 | 2.37 | 0.128 | 0 |
| 45 | 366,657 | 86 | 1.64 | 0.060 | 1 |
| 47 | 646,747 | 86 | 2.19 | 0.102 | 0 |

Every W from 8 to 44, and 45 and 47, is in the run; W = 46 and 48 are in MM-1. For W ≥ 30 the mean of K² is 4.8, against 5.4 for twice the log of the check count, so K tracks the largest of about 15 fair coins and shows no rise with W. If that went on, K² ≈ 2 ln(0.4 W) stays far below W/2 at every W beyond the small cases. It proves nothing, for the reason above.

**Sibling control (CR-1's open item).** Rules 90 and 150: K(W) = 2^(W/4) exactly at W = 8 to 30, because every check is constant on lanes, so the law fails as badly as it can. Rule 210: C(W) = W/2 + 1 and K ≤ 3.16. It meets the law, but vacuously, because it has only linearly many classes to begin with. So the law separates rule 30 from 90 and 150, and it does not separate it from 210 by K alone; the exponential C(W) does that. CR-1's Gate 1 objection is answered for 90 and 150 and only in that second sense for 210.

## The conditioned second check

Class ratios at the first three composite checks stay within 2.45 binomial sigma of ½ at W = 24 to 44 in steps of 4, with no exact law: at W = 44 they are 0.4997, 0.5016, 0.5008. I found no conditioned contraction by hand. CT-2 §6's reason stands: on width-2n survivors the fresh bits behind its 1/4 are pinned from the second check on. After Theorem 2 this matters less than the schedule assumed. A constant-factor bound at one check is a statement about the bulk, so it could not reach Q01 even if proved. It stays open as a question about D(W), not as a route.

## Degree 3

On the first 22 row bits past the black wall cell, the 1,794 monomials of degree at most 3 have full rank on survivors at all five points with enough rows: W = 32 at t = 30, 32, and W = 40 at t = 38, 42, 48. So there is no degree-3 invariant there. At W = 32, t = 36 only 1,520 rows remain, fewer than the monomials, and the test does not apply. A planted cubic relation among four of those bits drops the rank to 1,733 each time it applies, so the test can see such an invariant. This extends CT-4's negative search; it is not a proof that none exists at other widths or more bits.

## Predictions, from the probes' docstrings

| # | Prediction | Result |
|---|---|---|
| P1 (0.8) | K ≤ 3.5 and K²/W ≤ 0.3 at every W ≤ 48 | **Half.** K ≤ 2.75 HELD. K²/W MISSED at W = 9, 10, 12, 19 (largest 0.382); for W ≥ 20 it is at most 0.245 |
| P2 (0.85) | The law separates rule 30 from all three siblings | **Half.** Rules 90, 150 HELD. Rule 210 MISSED: it meets the bound, vacuously |
| P3 (0.7) | K² tracks 2 ln(0.4 W), no rise | **HELD** to W = 47 |
| Part A (0.8) | Class ratios within 3 sigma, no exact law | **HELD** |
| Part B (0.85) | Full rank, no degree-3 invariant | **HELD** at the five points tested |

I did not predict the main finding. The block was framed as "main term or last fibre", and I expected a substantial conditional theorem.

## Limits

- Theorems 1 and 2 are elementary, and that is the point: they show how little the law carries. They do not bound anything.
- Theorem 1's floor is the known orbit floor (AM-1, CT-3 §6, MM-1); what is new here, if anything, is the reading: the constant, and that the bulk of the law is logically idle.
- "Class amplifier" names a missing lemma, not a route with evidence for it. The evidence so far points against one.

**Record searched:** CT-2, CT-3, CT-4, MM-1 reports and claims; JD-1, JD-2, CR-1; RULE30-PRIZE §8.38 by its citations in those reports; `record_find` on class amplifier, orbit floor and immortal futures (no hit before this note) and distinct futures (the block's own sources). The kit and portal were not searched for Theorem 1, because it is the orbit lemma restated.
