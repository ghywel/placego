# Period-growth gap is an exponentially weighted stage-length condition

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G184 — Period-growth gap is
an exponentially weighted stage-length condition (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Period must grow slowly compared with depth; exponentially long stages alone do not guarantee it.

**What it says.** Divide each stage's length by its period. The depth-to-period ratio is an exponentially weighted sum of these normalized lengths. That sum must grow without bound to make period negligible compared with depth.

**Why it matters.** A large finite delay, or stage lengths proportional to their periods, is insufficient. Individual normalized lengths need not all grow; a growing sum over a fixed recent window is another sufficient condition.

**An everyday picture.** Each doubling halves the savings already accumulated. New deposits must eventually overcome that repeated halving; one large old deposit cannot settle the long-term balance.

## The formal statement and proof

**Symbolic checkpoint, second reader pending; no run.** Fix one infinite admissible rooted history, with N_j the first node of least pair period2^j as in G165. Let ell_j=N_(j+1)-N_j be its spatial stage length, lambda_j=ell_j/2^j and R_j=N_j/2^j. G165's required sublinear period growth is exactly R_j->infinity. The entry recurrence becomes

    R_(j+1)=(R_j+lambda_j)/2,
    R_j=2^(-(j-J))*R_J + sum from i=J to j-1 of 2^(-(j-i))*lambda_i.

Thus the missing growth estimate is divergence of this exponentially weighted moving sum of normalized stage lengths. It is not merely divergence of absolute stage lengths, a large observed entry depth, or a geometric delay lower bound.

**Proof and useful sufficient condition.** N_(j+1)=N_j+ell_j gives the first identity after division by2^(j+1); induction gives the second. G165 already proves p_k=o(k) iff2^j/N_j->0, which is R_j->infinity. If lambda_j->infinity, then R_(j+1)>=lambda_j/2->infinity. More generally, for any fixed positive m and j>=J+m,

    R_j >= 2^(-m) * sum from i=j-m to j-1 of lambda_i.

Hence divergence of an unweighted sum over any fixed recent window of normalized stage lengths is sufficient. These are conditions to prove from compatibility, not estimates supplied here. Their constants and eventual thresholds may depend on the history, as G165 allows.

**Counterfactual: geometric delay alone is insufficient.** For a synthetic stage schedule with lambda_j=C>0 after J (choose integer C so ell_j=C*2^j are positive integers), the recurrence gives R_j=C+2^(-(j-J))*(R_J-C). Thus R_j tends to C rather than infinity, despite exponentially increasing absolute stage lengths and arbitrarily large initial R_J. Its period/depth ratio tends to1/C rather than0. This is a logical stage-schedule control, not a compatible Rule30 counterexample. It shows that a proof of ell_j>=c*2^j with fixed c would not by itself settle the growth target.

**Identified unexpected check: individual normalized stage lengths need not diverge.** In a synthetic integer schedule let lambda_j=1 at even j and lambda_j=j at odd j (after any finite prefix). Then R_j->infinity: if j-1 is odd, R_j>=(j-1)/2; if j-1 is even, the preceding odd term gives R_j>=(j-2)/4. Yet lambda_j remains1 at every even index. Therefore lambda_j->infinity is sufficient, not necessary; refuting that stronger condition would not refute period growth. The two-step recent-window sufficient condition covers this example. Conversely any finite prefix's contribution decays as2^(-(j-J)), so no finite delay record alone can force the limit.

**What the recorded depths say.** The certified unbranched small-cap prefixes give N_1=3,N_2=8,N_3=29,N_4=400, hence R_1=1.5,R_2=2,R_3=29/8,R_4=25. Their normalized completed stage lengths are lambda_1=5/2,lambda_2=21/4,lambda_3=371/8. These are existing G161/G165 and Local L115 records, not new measurements. The known period16 genuine branch at depth53208 preserves period16; it is NOT N_5. Later period16 branch examples likewise supply no certified period32 entry. No N_5 value or asymptotic stage-length estimate is inferred.

**Scope and next proof obligation.** The recurrence is elementary weighted summation applied to G165's reviewed dyadic stage structure; no novelty claim or new experiment. All controls here are algebraic synthetic schedules and explicitly lack Rule30 compatibility. A sufficient next lemma would bound actual normalized stage lengths from below by a quantity tending to infinity, or establish divergence of their recent-window sum on each admissible history. Genuine branch spacing from G159 does not imply this bound: same-period branches do not end the stage. GPT next examines constraints at consecutive odd zero-driver doubling events, reasoning first; no new gap-1 family or larger-period run is queued.
