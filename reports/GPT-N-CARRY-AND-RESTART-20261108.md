# Theorem N carrying read and restart

GPT GC2720, 8 November 2026. Pulled Local L1580–L1583 through86c77b84. The owner asks for catch-up and another research block; L1582 records the owner's assignment of Theorem N to GPT.

## Verdict: Theorem N(a)–(e) carried

**PROVED hand/two-party**, with positive rows, K≥1 and the eventual-cycle definition retained. I read the complete [Local report and reader's guide](SW02-NEVER-MERGE.md), its five carrying steps, the cited exact kit definitions and proofs, the C/Python replay sources and the digest-verified retained evidence. This is a hand carry of the theorem. No new second-host simulation, Lean compilation or external verification is claimed.

Let F be the natural white-boundary map, w=width(Y), and L_K the odd-residue top-strip map. Wait until width(F^t Y)≥K and its K-cell top strip lies on a cycle. Inverse powers below act on the periodic-point set Per_K, where L_K is a permutation; no invertibility on all odd residues is assumed.

**Time independence and F invariance.** Increasing t by one applies L_K once to the strip and increases the inverse exponent t+w by one. Replacing Y by FY also increases w by one and shifts the strip trajectory by one. Both cancel exactly, giving a well-defined ν_K and ν_K(FY)=ν_K(Y).

**Compatibility.** Reduction commutes with L and sends periodic points to periodic points. On these finite periodic sets it also commutes with the unique inverse: apply L to both proposed inverse images and use uniqueness. Therefore ν_K reduces to ν_K′ for K′≤K. Their compatible odd residues define ν(Y) in the2-adics. Equality F^aY=F^bY′ implies ν(Y)=ν(Y′), with arbitrary nonnegative lags. At equal initial widths the width law additionally forces a=b, but that is not needed for the invariant proof.

**Reversed witnesses.** For p∈Per_W, take v=L_W^W(p), and Y=reverse_W(v). Oddness makes Y have width exactly W. Its top strip starts at the periodic point v, so applying the definition at t=0 gives ν_W(Y)=L_W^−W(v)=p. Distinct p give rows that never merge, even asynchronously. Hence the limiting number M(W) of distinct equal-width futures is at least Π(W)=|Per_W|. The definition remains valid at t=0 here because the strip is already on its cycle and has the required width.

**Unboundedness.** Reduction Per_(K+1)→Per_K is onto. For p on a base cycle of period P, L_(K+1)^P maps its two-element lift fibre to itself. A periodic point of that finite map is periodic under L_(K+1) and reduces to p. Thus Π is nondecreasing.

The kit step uses the **full single-seed left diagonals**, not an unproved identification with the white-boundary natural seed's transient. `Rule30Diagonals.D j t` is `cell t (j−t)`. Encoding its first K diagonals as a word gives exactly L_K: `D_zero`, `D_one` and `D_step` agree with the three bit equations of `Rule30UniversalLeftSide.stepK`. This finite word trajectory eventually cycles, say with period P. Then each of its bit traces, including D j when K=j+1, has eventual period P. `Rule30LeftUnbounded.D_least_period_unbounded Q` supplies a j for which no positive period≤Q works. Therefore that word's cycle has P>Q, so Π(j+1)≥P>Q. Monotonicity now gives Π(W)→∞ and M(W)→∞. No rate of growth is obtained.

The exact kit pin checked is48d8fbbc0d4a74ef5dd740cb76131704a6fc9167. I read `D`'s definition, its three recurrence facts, the `stepK` bit identities and the complete proof of `D_least_period_unbounded`, including the positive-LCM/divisibility step. This closes the specific source/convention obligation in L1582.

## Computational and clock scope

The raw Python replay reports distinct counts1,2,2,3,5,9 through width6, matching Local's table. Theorem N supplies the logic of these lower certificates; witnessed finite merges supply upper bounds. Those computations remain Local/M5 evidence here. The report's exact small values can use that evidence and this carried theorem; they are not a new Intel replay. Larger finite lower bounds and all clock observations retain their recorded statuses.

For the clock paragraph, the explicit transient guard is useful: τ_g(FY)=max(τ_g(Y)−1,0), with strip width part of the admissibility convention. Hence θ_g(FY)=θ_g(Y) whenever τ_g(Y)>0, in particular when g>width(Y). At a level already on-cycle at t=0 the raw θ identity need not hold. This only makes the existing “for large g” wording precise; it does not prove the lock conjecture or completeness of ν.

Evidence read: `cited/local/never-merge-20261106.tar.gz`,26,913 bytes,SHA256 `75a248a0d1f23310934218faf6b8a17c05082a1f3490b1e5f41ad403ef3158c4`. No hash collision is needed for the logical implication “different hashes imply different values”; equal hashes do not certify equality.

## Returned A-block review and outside update

L1582's complete carrying paragraphs, independent replay source and scope are read. The GC2719 trunk, join and finite-cone arguments are adopted **PROVED hand/two-party**; the tables remain COMPUTED. Local's wording correction is accepted: prefixes32/64/96 select a **next gap2**, while the rest of the next A requires its later input word.

The complete index refresh finished2026-11-08T10:37:16Z at the kit pin above:43 added,42 changed,54 no longer listed,12 open PRs. This differs from Local's earlier baseline counts because the prior GPT checkpoint was older. S-01 and S-03 are now in kit main. New `Rule30ResponseAncestry` and `Rule30ResponseWidth` statements were read: their universal-response/finite-full-row guards do not certify our fixed-drive E history, and they are not Theorem N's periodic-strip invariant. Local's L1583 comparison of the h3artfield entry is received at its stated source-read scope; it is not an independent full-notebook audit here. No novelty or submission decision is made in this review.

**Continuation:** GPT owns the thirteen A-block gap3-launch fibres through the rest of E, with actual initial cells and incoming words retained. First impose one initial-black step as well as the entire A/E head word, so a positive model is a finite prefix in the kit's phase. This is one excursion after A, not the earlier E A^4 E A^7 E query. A separately frozen bounded test follows. Schedules remain paused.
