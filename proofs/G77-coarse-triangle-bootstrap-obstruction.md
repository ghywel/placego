# coarse triangle bootstrap obstruction

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT77. coarse triangle
bootstrap obstruction (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The simplest way of combining G74 and G75 cannot bound the Collatz count for all horizons: that route is closed.

**What it says.** The goal is to show the real Collatz count never exceeds the coin-toss prediction by more than a
fixed factor. The crudest approach takes G75's largest weight, assumes every class is as unbalanced as it can be,
and feeds the hoped-for bound back in. GPT showed that this approach gives a bound that grows like the square root
of the number of steps, so it can never give a fixed factor. GPT also noted that a big cancellation ratio in the
data does not by itself rule out a useful bound.

**Why it matters.** It closes one tempting route cleanly, and says what is left open: sharper estimates that use how
the numbers are actually spread out, or real cancellation between plus and minus terms.

**An everyday picture.** A builder's quote that prices every job at its worst case: add up enough jobs and the quote
climbs far past what the work will really cost.

## The formal statement and proof

### G77. Which triangle estimate the signed diagnostic does and does not exclude (2026-10-06)

The count target is an upper bound on C_w(T)/Q_w(T), not a small cancellation factor A/abs(D). From G76, C=Q+D<=Q+A. Therefore a uniform estimate A<=B*Q would suffice to give C/Q<=1+B, or excess at most log2(1+B) bits whenever C>0. Cancellation is one possible mechanism, not a necessary assumption for that upper-bound strategy.

**Unexpected normalization guard.** G76's largest positive-count cancellation factor2155/88 (width10,T20) has A/Q=2155/3416<1, D/Q=-11/427 and C/Q=416/427. A triangle estimate already gives C/Q<=1+2155/3416<2 in that case. Thus a large A/abs(D) does not refute a useful bound on A/Q. This is an exact consequence of the retained rational row, not a new run. The full small sample's maximum A/Q=1033093/95527 also supplies no uniform constant at larger width.

A particular coarse use of G75, however, cannot close a horizon-independent estimate. For h>=0 put

    b(h)=min(1, inf over integer L>=1 of
                  (L/sqrt(h+1)+32*exp(-(L-1)/2))).

Each term inside the infimum is at least1/sqrt(h+1), so b(h)>=1/sqrt(h+1). Since sum_a abs(I_w(t,a))<=C_w(t), G74-G75 give

    A_w(T)<= (1/2)*sum_(t=m)^(T-1) b(T-t-1)*C_w(t).

Suppose one substitutes the desired bootstrap C_w(t)<=K*Q_w(t) at all preceding horizons. Q_w(t) is nonincreasing, because the coin survivor probability is nonincreasing. Consequently the resulting sufficient upper bound has the form

    A_w(T)/Q_w(T) <= K*B_(m,T),
    B_(m,T)=(1/2)*sum_(t=m)^(T-1)
                       b(T-t-1)*Q_w(t)/Q_w(T),
    B_(m,T)>=sqrt(T-m+1)-1.

The last inequality follows from the preceding lower bound on b and sum_(j=1)^d j^(-1/2)>=2*(sqrt(d+1)-1), with d=T-m. Thus the coefficient in this particular sufficient estimate grows with the paid-tail length. It cannot certify a uniform B or close a fixed-K induction simply by substituting the same coarse count bound. This is a statement about the estimate's right-hand side, not a lower bound on the true A or D and not a refutation of the count conjecture. It remains valid along linear horizons where the paid tail grows with width.

**Route status.** Close only the route that takes the maximum coin weight, replaces every class imbalance by its full class size, and feeds a uniform count bootstrap into that bound. A sharper triangle estimate retaining the actual odd-count allocation, or cancellation in the signed sum, remains open. The next reasoning question is whether the barrier-demand weights suppress classes carrying most of the actual mass, rather than taking their maximum. No new experiment is proposed in this audit; G74-G76 identities and the exact normalization guard are the controls. Independent Local reading requested. This is elementary accounting of recorded bounds, with no novelty claim.
