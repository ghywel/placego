# Exact live-chain units and conditional partial-bijection law

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G274 — Exact live-chain
units and conditional partial-bijection law (GPT, 2026-10-09; waiting room, GC869)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The complete-domain mean chain length has a counting bound, and an explicitly defined random comparison has an exact conditional length law.

**What it says.** With N=2^q there are N(N-1) live states and N-1 chains, so mean live length is at most N. Original return depth adds one. In the uniform partial-bijection comparison, fixing total chain mass makes the lengths minus their two endpoints a uniform weak composition. Cloud second-read the counting text; formal filing remains separate.

**Why it matters.** A matching conditioned mean cannot establish randomness or restricted-source growth. This supplies a precise benchmark, not a Rule30 distribution theorem.

## The formal statement and proof

#### GC869 — Chain lengths, return offsets and an explicitly conditional random null (2026-10-09 21:43 BST)

**Registered hand audit; second reading pending.** Record searched: partial permutation -> one hit, the RC/RW census header; chain states -> same header. Local already records the partial-permutation decomposition, start count and mean-chain bound. This entry sharpens units and specifies a null; it does not claim discovery of that mechanism. Predict the mean is structural, while a uniform partial-bijection null conditional on chain mass is a uniform weak composition after removing two endpoints per chain. Countercontrol: conditioning on chain mass fixes the mean and cannot test randomness. Independent q1/q2 controls and the unexpected restricted-source mean check below. No random draw, trajectory replay, literature claim or prize-board expansion.

**Exact complete-domain count and units.** Write N=2^q. The live domain V consists of (x,y) with y nonzero, so M=|V|=N(N-1), rather than N^2. By the reset existence/uniqueness argument, each live pair has one child. Its successor leaves V precisely when the child is zero, which in the cyclic equation means x=y. Thus B={(w,w): w nonzero} is the terminal set, of size s=N-1. By unique predecessor H, precisely A={(0,c): c nonzero} has no live predecessor. A and B are disjoint. The live transition is a bijection V\B -> V\A: injectivity is H, and the two sets both have (N-1)^2 elements.

Consequently V decomposes into s disjoint directed chains from A to B, and directed cycles. If L_i counts live vertices on chain i, including both its start and terminal, and S is total live chain mass, then sum L_i=S<=M and mean L=S/s<=N. The original excursion begins one edge earlier at (a,0) and stops one edge later at (w,0). A chain with L vertices therefore has return depth r=L+1; its complete-source mean r is at most N+1. The correspondence to admissible excursions is bijective: a first child c determines a=S c XOR c, and all nonzero c occur.

Local's reported q4 figures S=226, s=15 give live mean226/15, with return mean241/15; q8 figures S=59770, s=255 give live mean59770/255, with return mean60025/255. These arithmetic conversions use reported exhaustive counts, not GPT reruns. The published rounded means15.1 and234.4 match live-node lengths. Local's bound N^2/(N-1) is valid and slightly looser than the exact N. Neither is an individual-path bound.

**Specified abstract null, not an identification of the earlier random split.** Fix M labelled vertices and disjoint labelled sets A and B of size s. Choose uniformly a bijection f:V\B -> V\A. Its graph again consists of s chains and cycles. Condition on total chain mass S, where 2s<=S<=M, and set K=S-2s. Order chains by their labelled starts. Then L_i=k_i+2 with k_i>=0 and sum k_i=K.

Each fixed weak composition (k_1,...,k_s) is realized by exactly binom(M-2s,K) K! s! (M-S)! bijections. Choose the K intermediate chain vertices from V\(A union B), put them in ordered positions along the chains (K!), match the starts to terminals (s!), and freely permute the remaining M-S vertices into cycles. Conversely every bijection supplies these choices uniquely. The count is independent of the composition, so the conditional k-vector is uniform over binom(K+s-1,s-1) weak compositions.

For s>=2 and integer 0<=t<=K this gives

P(L_1>=2+t | S) = binom(K-t+s-1,s-1) / binom(K+s-1,s-1).

The probability is zero for t>K. Exchangeability and the fixed sum give E[L_i|S]=S/s. For s=1 there is one chain, deterministically L_1=S. This is an exact counting theorem for the defined ensemble, not a theorem that Rule30 samples that ensemble.

**Independent literal controls.** At q1, V has two vertices (0,1),(1,1), forming one chain: L=2 and r=3. At q2, GC865's literal paths have live lengths2,4,4 and return depths3,5,5. Their ten live chain vertices leave the two-cycle (01,10)<->(10,01), giving M=12, s=3, S=10, K=4. The null has binom(6,2)=15 equally likely ordered compositions. The observed length vector(2,4,4) corresponds to k=(0,2,2), one of the fifteen vectors. Its one-chain tail at L>=4 is binom(4,2)/binom(6,2)=2/5, directly checked by the six triples with k_1>=2. There can be no one-vertex chain because starts and terminals are disjoint. A uniform positive composition of S, allowing L=1, is a different null. The earlier header does not specify its random-split algorithm, so its law is not inferred here.

**Unexpected domain guard and failure retained.** The reported q16 odd-doubled-source mean around72000 exceeds N=65536 without contradicting mean L<=N: that bound averages all N-1 nonzero first children, whereas the census selects a restricted set of initial children. A subset mean need not obey the full-domain bound. Similarly, a fixed-sum null's matching mean is automatic and cannot support the randomness analogy. The observed q8 maximum667 versus one random maximum1656 remains descriptive; a lighter-tail claim needs a defined statistic and calibrated ensemble, not one draw. No new random test is proposed or run here.

This abstract null also discards the Rule30 constraint that a successor's first coordinate is the preceding second coordinate, and discards rotation equivariance. Any rejection would distinguish Rule30 from this particular ensemble, without proving individual growth or the prize statement. Even within the null, all K intermediate vertices can occupy one chain, so an average bound supplies no per-chain bound. This is an abstract countercontrol, not a claimed realizable Rule30 path.

**Disposition.** The complete-domain mean scale is already explained by Local's counting observation. The new conditional law makes a future comparison reviewable, but neither the mean nor an exponential-looking histogram proves restricted rooted growth. Next useful mathematical target is information in source-to-length matching, retained after controlling for total mass and rotations. Leave Local's running census and Cloud's one-hole construction in their lanes; no expensive experiment requested.


**GPT duplicate audit (2026-10-09 21:43 BST).** W274 hard checks pass; nearest older W273, G269 and entry23 were read. W273 supplies the return mechanism and endpoint count reused with credit; G269 classifies lifted odd-period parity-mask cycles; entry23 is the retained period32 run certificate. None supplies the conditional weak-composition law. The mean-scale observation is already Local's census header and is expressly credited, not claimed as new. No proof promotion.
