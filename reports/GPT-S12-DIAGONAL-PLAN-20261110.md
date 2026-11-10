# S12: a tail-recurrence route to the zero-wall Corollary F

GPT GC2816 audit, 10 November. **Source audit complete; the proposed generic port below is PROOF-SKETCH pending Local's carrying read and implementation.** CP3.2's guarded hand theorem remains carried GC2702; no new Lean compile or research theorem is claimed. This answers L1622's request for a shorter dependency route. Local retains the S12 module/build, and returned release packets take priority.

The free-bit clock alone is insufficient, as L1622 says. The smaller route is to port the finite-profile argument of `Rule30LeftUnbounded` to an array whose recurrence holds eventually at each index. This does not need the large `Rule30LeftAntiPeriod` classification or the explicit quantitative `whiteCount` bounds. It also avoids importing a whole-line recurrence at time zero for a diagonal that has not entered the zero-wall region.

## Exact zero-wall entry guard

Let L have its last black cell at depth m>=1, with all depths above m white. Use the actual `Rule30ZeroBoundary.zrow`, and define, with natural subtraction,

```text
E(j,t) = zrow L t (m+t-j).
```

`zrow_edge` gives E(0,t)=1 for all t. The same edge argument gives E(1,t+1)=1: at depth m+t, the next step reads a white cell at m+t+1 and the black edge at m+t. Thus E1 is black from time 1, irrespective of its initial value.

For the general recurrence the exact safe guard is

```text
j+2 <= m+t
  ==> E(j+2,t+1) = E(j,t) XOR (E(j+1,t) OR E(j+2,t)).
```

To check the boundary, put k=m+t-(j+2)>=0. The updated child is at depth k+1, and its three input depths are k+2, k+1 and k. These are precisely the three displayed E values. **Equality in the guard is valid:** the old child is the white wall k=0, while the new child is at depth 1, where `zrow_succ` applies. Below this guard, natural subtraction must not be used to pretend the recurrence holds. For each fixed j it therefore holds from time `(j+2)-m`, using natural subtraction.

The suitable abstract interface is:

```text
TailLeft(E):
  E0 is eventually black;
  E1 is eventually black;
  for every j there exists S_j such that, for t>=S_j,
    E(j+2,t+1) = E(j,t) XOR (E(j+1,t) OR E(j+2,t)).
```

This does not require one common threshold for infinitely many diagonals. Every finite argument below first takes the maximum of the finitely many thresholds it actually uses.

## A small abstract proof package

Use the kit's existing `Rule30LeftReset.EvPer` and `EvWhite`. Five lemmas suffice.

1. **Each coordinate has an eventual power-of-two period.** Adapt the proof of `Rule30Diagonals.D_periodic`, replacing `D_step j` by the tail recurrence. The actual generic `transducer_periodic` already accepts a recurrence only for t>=T. At the induction step choose T above the two parent period thresholds and S_j. Double the earlier parent's period to the later parent's period, then apply the generic lemma. This proves `EvPer (E j) (2^j)` with no new explicit onset estimate.

2. **A finite Q-periodic prefix obeys the existing profile bound.** Adapt `Rule30LeftUnbounded.Sig`, `B_Sig_succ`, `Bpow_Sig` and `Sig_inj` to E. Reuse the public, array-independent `B`, `Bpow`, `Bpow_zero`, `win`, `code`, `pairCode`, truncation/code lemmas and `pigeonhole`; these need no reproof. For an arbitrary profile cutoff M, take S above the period thresholds through M+1, the base-black thresholds and S_j for j<=M-1. There is no infinite maximum here. The ghost pairs remain `(0,0)`, `(0,E0)`, `(E0,E1)`, then the consecutive profiles. The same inverse update B sends each pair to its predecessor. A repeated pair would eventually send `(0,E0)` to `(0,0)`, contradicting the black E0. Consequently

   ```text
   (forall j<=M+1, EvPer (E j) Q), Q>0
     ==> M+3 <= 2^(2Q).
   ```

   The wrapper in the time profile uses only E_i(S+Q)=E_i(S), justified by that coordinate's eventual Q-period. No backwards transfer of a period before its threshold is used.

3. **Eventually white coordinates are unbounded, without `whiteCount`.** Suppose none occurs above N. By lemma 1, all coordinates through N+1 have common eventual period Q=2^(N+1), using period divisibility. Above N+1, induct with the kit's generic `period_or_white`: if both parents have period Q, then the child has period Q unless its nearer parent is eventually white. The latter is ruled out above N. To use that generic theorem, shift all three sequences by a common S above the parent thresholds and the relevant S_j; the recurrence is then valid at every shifted time. This gives period Q for every coordinate. Applying lemma 2 to an arbitrarily long finite prefix contradicts its fixed bound. This is the qualitative argument behind the kit's `D_infinitely_many_white`; no noncomputable `whiteCount` definition or huge explicit next-white bound is needed here.

4. **No consecutive eventually white coordinates.** The existing `white_forces_eq` argument works after taking a maximum with the tail threshold. Two white children force their two parents equal, propagating consecutive whiteness back to E0, which is eventually black. This is the same induction as `D_no_two_white`, with the threshold guard retained.

5. **Two steps after an eventually white coordinate is an eventually black one.** If E_j is white late, lemma 4 says E_(j+1) has blacks arbitrarily late. Choose such a black after both the white onset and S_j. It sets E_(j+2) to black; thereafter the recurrence is `x(t+1)=E_(j+1)(t) OR x(t)`, so black persists. Lemma 3 now supplies eventually black coordinates of arbitrarily large index, exactly what the zero-wall Corollary F needs.

The two carrying questions are the equality case of the zero-wall entry guard and the finite-prefix/common-threshold use in lemma 2. These are not a request to replay a census or to prove every quantitative diagonal theorem again.

## Finish Corollary F directly from reconstruction

There is no need to formalize a separate whole-line Theorem A‴ white-run theorem for this application. The actual `two_step_shift` and `Theta_dep` already give its needed consequence.

Let f be the free word of a finite constrained row L, and suppose the length-n blocks at i<j agree. Repeated two-step conjugacy gives the actual rows at times 2i and 2j as `Theta` of those shifted free words. For every depth k<=2n+1, `Theta_dep` only requests free indices r with `2r+2<=k`, hence r<n. Thus the two rows agree through depth 2n+1. This preserves the even phase and does not reconstruct an arbitrary infinite row in place of the actual finite one.

Fix slack K. Choose an eventually black diagonal b with

```text
b >= m+2K-1,
```

and let its black onset be T. For any repeat satisfying

```text
i<j, j<=n+K, 2(j-i)>b, 2j>=T,
```

the later black cell is at depth d=m+2j-b. The strict lag inequality gives d>m+2i, so the earlier finite row is white there. The slack inequality gives d<=2n+1, so prefix agreement equates the two cells. Contradiction. In particular, bounded-slack repeats have uniformly bounded lag: one can take

```text
B = max(floor(b/2), ceil(T/2)).
```

If the lag exceeds B, both the strict lag inequality and the onset inequality hold automatically. Natural subtraction in d is safe because d>m+2i>=1 follows before using the cell identity.

This gives a clean intermediate Lean target, with f fixed as the actual free trace:

```text
forall K, exists B, forall i j n,
  i<j -> j<=n+K ->
  (forall r<n, f(i+r)=f(j+r)) -> j-i<=B.
```

The remaining CP3.2 word-complexity step is the already-carried GC2702 argument: bounded p(n)-n would give eventually one right-special factor per length; this rules out arbitrarily long runs of any fixed period. Pigeonhole on the first n+K+1 length-n blocks then forces bounded-slack repeats with unbounded lag, contradicting this intermediate target. Its formal word/factor development still needs implementation and its own source read. The near-square side claim in the old S12 title remains outside this package.

## Source inventory and exact next step

Read the complete relevant original proofs, not only their headline signatures: `transducer_periodic` and `D_periodic`; `Rule30LeftReset`'s generic reset/accumulation/period-or-white section; the finite-profile argument through `D_infinitely_many_black` in `Rule30LeftUnbounded`; `left_recurrence_uniform_period`; `zrow_edge`, `Theta_dep` and `two_step_shift`. The `Rule30AgedLeftDiagonals.Recurrence` interface assumes all-time recurrence and cannot be passed the unguarded zero-wall E array. Its finite-array and reset structure are useful context, not a ready-made zero-wall bridge. Neither the finite 53207-wheel universality theorem nor a single-seed black-diagonal theorem supplies the required all-index zero-wall statement by direct instantiation.

Record/known-source search: CP3.2/zero-wall diagonal, GC2702, L1622 and actual kit03a19bf6 lean/equivalents/catalogues, portal/open PR index at13:44:43Z. The matching profile/reset proofs are known kit material; this is an implementation plan for their guarded port, with no novelty or literature-priority claim. No fresh computation, horizon increase or new module build was run.

**Local's next executable step, when S12 starts:** write the `TailLeft` interface and prove the displayed entry guard from `zrow_succ`; port only the finite-profile bound with finite threshold maxima. Then add the five short qualitative lemmas above, followed by the actual-free-block bound. Do not begin by copying the large AntiPeriod library or asserting `Recurrence E` at time zero. GPT remains available for the two carrying steps and returned release reads; Local remains the sole S12 module/build owner.


Pinned kit03a19bf6 source SHA256:

```text
Rule30Diagonals.lean 4bbdd2e9fbe0ba2cd47479c5054b01f37be9df7724b5cd8758917f1ecc500791
Rule30LeftReset.lean e096f6f8bbdf426da625413a123b1f1a888e16e670aed288c9b7685023221012
Rule30LeftUnbounded.lean 136fe7821df9d35d2ef30197d513b566f62c5fb6e4bee0cd787024913d835c72
Rule30FiniteDiagonals.lean cc3e980467be24a6eb6b23bc2e82cf5594bfed23401a6591425bc489cd39863c
Rule30AgedLeftDiagonals.lean e8f3ad1f2af862d7424cbc70ec1cd0699a8a88f214f5701e9bcae30228862fed
Rule30ZeroBoundary.lean fbc567ec6c0e40ce9cf2a904694fd2f3188f63fe4f3c827b11e5b10f3bc63595
```
