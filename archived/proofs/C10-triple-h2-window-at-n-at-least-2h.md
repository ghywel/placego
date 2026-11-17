# Triple H2 window at n at least 2h+4 (Cloud CL517; second-read by GPT, MI619)

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.10 Triple H2 window
at n at least 2h+4 (Cloud CL517; second-read by GPT, MI619)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** PROVED in the stated triple-only range by Cloud's hand proof,.

## In plain words

**Triple sums fill the prescribed total-dependent window when the pool is large enough.**
An interval with h missing values and n remaining values, n>=7 and
n>=2h+4, realizes every triple target between 3+3h and its total minus
the complementary-bin lower bound. Pair matchings cover the middle;
counting the bottom holes supplies the small upper extension.

**Why it matters.** This verifies the first-triple existence premise in
that range. It does not partition three or more bins or prove the full
conjectured spectrum threshold.

## The formal statement and proof

*Status:* PROVED in the stated triple-only range by Cloud's hand proof,
with GPT's targeted carrying read,2026-10-22. The original candidate
text follows for provenance. No claim for general subset size or the
full measured sharp threshold is adopted.

**Carrying check, GPT.** Endpoint trimming preserves the window inclusion
and weakens the cardinality gate. Each anchor's pair matching has at
least h+2 edges, against h holes plus one forbidden anchor. The translates
integer-join because their cardinality exceeds every possible consecutive
pool gap. For the upper excess, counting each hole's incidences below the
first n-3 values gives E<=d. At offset j, pairs in[0,M-1] have exact
count h+1-ceil(j/2) and smallest possible endpoint
n-h-3+j>d. Hence only h-d holes can hit them, strictly fewer than the
pair count for j<=d. Both endpoint formulas and strict inequalities
were re-derived; no numerical census was rerun or used as a proof premise.
The nearest already-carried G318/G340/G341 scalar engines were read:
this is a different total-dependent H2 window/range, not their restatement.

### Cloud CL517 — Triple sums of an interval with holes fill the H₂ window when n ≥ 2h + 4 (Cloud, 2026-10-22 04:15 BST; waiting room)

*Status:* complete hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before
adoption. It is the r = 3 case of H₂ (CL514), the two-bin base of the H(h) reduction tree (CL508, CL515). Machine
support: `spectrum_h.py` and its edge runs (no window gap for n ≥ 7 and h ≤ 2n − 8 on every pool tested). The
threshold is confirmed by an independent self-check (CL518).

**Statement.** Let S = [0, M] ∖ H with |H| = h, n = |S| = M + 1 − h ≥ 7, and n ≥ 2h + 4. Then every integer u with
3 + 3h ≤ u ≤ ΣS − L(n − 3) − h(n − 3) is the sum of three distinct elements of S. (L(r) = r(r − 1)/2.)

**Proof.**

*Step 0 (reductions).*
- If s₁ = min S > 0, the pool S − s₁ ⊆ [0, M − s₁] has h − s₁ holes. The map u ↦ u − 3s₁ sends the window for (S, h)
  onto the window for (S − s₁, h − s₁):
  - the lower ends agree, since 3 + 3h − 3s₁ = 3 + 3(h − s₁);
  - the upper ends agree, since ΣS − n·s₁ − L(n − 3) − (h − s₁)(n − 3) = ΣS − L(n − 3) − h(n − 3) − 3s₁.
- If max S < M, deleting the top holes lowers h, which lowers the window's lower end and raises its upper end. The
  window only grows.
- Both changes preserve n ≥ 2h + 4. So assume 0, M ∈ S, with all holes interior.
- Write s_i = i − 1 + d_i, where d_i is the number of holes below s_i, and let d = d₂ (the holes between 0 and s₂).

*Step 1 (pairs).* For every z ∈ S and every v with 2h + 3 ≤ v ≤ 2M − 2h − 3, v = x + y with x < y in S ∖ {z}.
- The pairs {x, v − x} with 0 ≤ x < v − x ≤ M are pairwise disjoint.
- There are min(⌊(v + 1)/2⌋, ⌊(2M − v + 1)/2⌋) ≥ h + 2 of them.
- The h holes and z meet at most h + 1 of them.

*Step 2 (the middle).* Σ₃(S) ⊇ [2h + 3, 3M − 2h − 3].
- Σ₃(S) ⊇ ∪_{z ∈ S} (z + I), where I = [2h + 3, 2M − 2h − 3], by Step 1.
- I has 2M − 4h − 5 integers. That is at least h + 1 because 2M = 2n + 2h − 2 ≥ 5h + 6, which follows from n ≥ 2h + 4.
- Consecutive elements of S differ by at most h + 1, so consecutive translates overlap.
- The union therefore runs from 0 + 2h + 3 to M + 2M − 2h − 3.

*Step 3 (the bottom).* 3 + 3h ≥ 2h + 3.

*Step 4 (the top).*
- Since ΣS = L(n) + Σ d_i, L(n) − L(n − 3) = 3n − 6 and d_n = h:
  W_hi − (3M − 2h − 3) = Σ_{i ≤ n−3} (d_i − h) + d_{n−2} + d_{n−1}.
- Here Σ_{i ≤ n−3} (h − d_i) = Σ over holes q of #{i ≤ n − 3 : s_i < q}. Every hole contributes at least 1 (0 ∈ S), and
  at least 2 unless it lies between 0 and s₂.
- So the excess E = W_hi − (3M − 2h − 3) ≤ 2h − (2h − d) = d.
- For u = 3M − 2h − 3 + j with 1 ≤ j ≤ d, write u = M + v with v = 2M − 2h − 3 + j. The pairs {x, v − x} in [0, M − 1]
  number h + 1 − ⌈j/2⌉, and every one has x ≥ n − h − 3 + j.
- The d holes below s₂ lie in [1, d]. Since d ≤ h and n ≥ 2h + 4, d < n − h − 3 + j, so those holes miss every pair.
  At most h − d other holes meet the pairs, and h + 1 − ⌈j/2⌉ > h − d because ⌈j/2⌉ ≤ d.
- So some pair survives, and u = M + x + y with x < y < M. ∎

**Scope.**
- Only r = 3, and only n ≥ 2h + 4. The census indicates the truth is h ≤ 2n − 8, which is sharp by
  S = {0} ∪ [h + 1, M], where u = 2M is missing at h = 2n − 7.
- r ≥ 4 does not follow by window induction (CL519).
