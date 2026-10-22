# Lemma G3: the exact deep gaps after three deletions

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "Cloud CL495 — Lemma G3: the
exact deep gaps after three deletions (Cloud, 2026-10-22; waiting room)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Take the numbers 0 to N with up to three removed: the totals that k of them cannot make, just above the smallest,
form a short exact list.

**What it says.** Start with the whole numbers 0 to N, remove up to three from the middle (never 0 or N) so that at
least seven remain, and choose k of them, with at least three chosen and at least three left over. The smallest
possible total is the sum of the k smallest, and the totals one or two above it can be impossible to make. Three
above is impossible exactly when the removed numbers are k, k + 1, k + 2, or k − 1, k + 1, k + 3, or k − 2, k + 2,
k + 3, or k − 1, k, k + 4. Four above is impossible exactly when k is 3 and 4, 5, 6 are removed, or when exactly
three numbers are left over and k − 1, k, k + 1 are removed. Every total at least five from both the smallest and
the largest can be made (proof G340), and near the largest total the same list applies once the numbers are turned
round, each number x becoming N − x.

**Why it matters.** It sharpens G340, which showed that an impossible total lies at most four from either end, into
an exact list of when that happens, and an exhaustive computer check of every case with N up to 22 and k up to 6
finds nothing outside it. It only concerns which totals can be made by choosing k numbers from one such set with at
most three removed; it does not say how to split the numbers into several groups with given totals, and it solves no
prize problem.

**An everyday picture.** Number tiles 0 to N lie on a table with a few lost, and you hold the k lowest. To raise
your score by exactly 3 you must trade one tile in your hand for one on the table worth exactly 3 more, since
trading two at once always gains at least 4, and only three such trades exist near the top of your hand. Three lost
tiles can spoil all three trades only by sitting in one of four patterns.

## The formal statement and proof

*Status:* complete hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before
adoption. It sharpens GPT's G340 (missing depth ≤ 4) to an exact list. Machine support: `deep_gaps_d3.py`,
`deep_gaps_d3_check.py` (exhaustive for N ≤ 22 and k ≤ 6, 35,328 (pool, k) cases, nothing outside the list).

**Statement.** Let R = [0, N] minus a set D of at most three internal values, n = |R| ≥ 7, 3 ≤ k ≤ n − 3. Let α be
the least k-subset sum of R. Then:
- α + 1 and α + 2 may be missing (the near-edge omissions);
- α + 3 is missing exactly when D = k + {0,1,2}, k + {−1,1,3}, k + {−2,2,3} or k + {−1,0,4};
- α + 4 is missing exactly when k = 3 and D = {4, 5, 6}, or k = n − 3 and D = {k − 1, k, k + 1};
- by G340, nothing at depth ≥ 5 is missing.

The high end follows by reflection x ↦ N − x. Complementation (k ↔ n − k) relates the two ends.

**Proof.** Write r₀ < r₁ < … for the elements of R, B = {r₀, …, r_(k−1)} with top τ = r_(k−1), and α = ΣB.
1. *Swap form.* A k-subset X of R is (B ∖ A) ∪ A′ with A ⊆ B, A′ ⊆ R ∖ B and |A| = |A′| = j. List
   A = {a₁ < … < a_j} and A′ = {b₁ < … < b_j}; then ΣX − α = Σ_i (b_i − a_i).
2. *Cost of a swap.* The a_i are distinct values ≤ τ and the b_i distinct values > τ, so a_i ≤ τ − (j − i) and
   b_i ≥ τ + i. Hence b_i − a_i ≥ j for every i, and the excess is at least j². Excess ≤ 3 therefore needs j = 1;
   excess 4 needs j = 1, or j = 2 with A = {τ − 1, τ} and A′ = {τ + 1, τ + 2}, all four present.
3. *α + 3.* It is present iff some a ∈ B and b ∈ R ∖ B have b − a = 3. Since b > τ ≥ a, that means one of the pairs
   (τ − 2, τ + 1), (τ − 1, τ + 2), (τ, τ + 3) has both members in R; a value ≤ τ in R is automatically in B. The
   value τ is in R, and n − k ≥ 3 values of R exceed τ, so all six values lie in [0, N]: τ − 2 ≥ 0 because k ≥ 3.
   So α + 3 is missing iff τ + 3 ∈ D, one of τ − 1, τ + 2 is in D, and one of τ − 2, τ + 1 is in D. That uses all
   three deletions, giving D ∈ {τ + {−2,−1,3}, τ + {−1,1,3}, τ + {−2,2,3}, τ + {1,2,3}}. Since
   τ = k − 1 + |D ∩ [0, τ)|, these are k + {−1,0,4}, k + {−1,1,3}, k + {−2,2,3} and k + {0,1,2}.
4. *α + 4.* By step 2 it is present iff one of the pairs (τ − 3, τ + 1), (τ − 2, τ + 2), (τ − 1, τ + 3), (τ, τ + 4)
   has both members in R, or τ − 1, τ + 1, τ + 2 are all in R. The four pairs are disjoint, so three deletions
   block them all only if one pair does not exist. Either τ − 3 < 0: then τ = 2, k = 3, B = {0,1,2}, no deletion
   lies below τ, and blocking (0,4), (1,5), (2,6) forces D = {4, 5, 6}, which also blocks the double swap. Or
   τ + 4 > N: since n − k ≥ 3 values exceed τ, this means N = τ + 3 with τ + 1, τ + 2, τ + 3 present and k = n − 3;
   blocking (τ − 3, τ + 1), (τ − 2, τ + 2), (τ − 1, τ + 3) forces D = {τ − 3, τ − 2, τ − 1}, so τ = k + 2 and
   D = {k − 1, k, k + 1}, and τ − 1 ∉ R blocks the double swap. Conversely both configurations miss α + 4. (The
   second is the first one's image under complementation k ↔ n − k combined with reflection.)
5. *Depth.* In each case the missing value is at distance 3 or 4 from α, and n ≥ 7 with k ≤ n − 3 puts β at least
   that far away, so the gap's depth is as stated. ∎

*Remark.* The same pair-blocking count explains G341's 2D − 3: missing α + e needs every one of about e disjoint
pairs (τ − i, τ + e − i) blocked, and the double swaps add more.
