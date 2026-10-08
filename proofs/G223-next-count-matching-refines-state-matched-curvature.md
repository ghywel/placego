# next-count matching refines state-matched curvature

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT223. next-count matching refines
state-matched curvature (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Matching parent branches by next count gives the same curvature identity with a triangle bound no worse than state matching.

**What it says.** Pool all odd and even occurrences landing in the same count bin, regardless of their integer states. Pairing their minimum multiplicity cancels more nonnegative demand than keeping states separate.

**Why it matters.** Actual state coalescence is unnecessary for this weighted cancellation. The unmatched signed mass remains open, and this grouping can lose cancellation already captured by the original class bound.

**An everyday picture.** Contributions can share the same accounting label without reaching the same physical place.

## The formal statement and proof

**Where:** RULE30-GPT.md GC443 at b3817e9; statement and proof copied verbatim below. Local L261 at 2f86de3 checks the count-bin identity, nonnegative-demand triangle, multiplicity comparison, admission, both hand controls and failed-child guard. This is a finite regrouping of G91, not a matched-mass or bootstrap estimate.

At fixed t,T, keep all admitted parent occurrences with multiplicity, including children that will fail admission. Write d_a=f_(t+1)(a+1)-f_(t+1)(a)>=0. Let O_b count odd parents with current count b-1 and E_b count even parents with current count b, and let M_b=min(O_b,E_b). Then

    S_t=(1/2)*sum_b [M_b*(d_(b-1)-d_b)
        +(O_b-M_b)*d_(b-1)-(E_b-M_b)*d_b].

The matched coefficient is exactly G91's adjacent-demand difference, but matched occurrences need not have the same next integer state. Its triangle bound is

    A_count=(1/2)*sum_b [M_b*abs(d_(b-1)-d_b)
        +(O_b-M_b)*d_(b-1)+(E_b-M_b)*d_b].

Let A_state be G91's triangle bound retaining its separate (next state y,next count b) groups. Then abs(S_t)<=A_count<=A_state. No comparison with G74's already class-cancelled absolute bound is asserted.

**Proof.** Every odd parent supplies d_(b-1)/2, every even parent -d_b/2. Subtract M_b from both multiplicities and collect terms, then apply the triangle inequality. For nonnegative u,v and O,E with M=min(O,E), the group's unscaled triangle expression is

    M*abs(u-v)+(O-M)*u+(E-M)*v
      = O*u+E*v-2*M*min(u,v).

Summing G91's state groups gives the same O_b,E_b but total matched multiplicity sum_y min(O_(y,b),E_(y,b))<=min(sum_y O_(y,b),sum_y E_(y,b))=M_b. Hence count-only matching subtracts at least as much nonnegative mass and A_count<=A_state. Any matched child is count-admitted: its odd parent was admitted and adding one odd step clears the next threshold. No integer-state coalescence or independently realized swapped orbit is needed. Unmatched failed even children remain in E_b; their removal corrupts S_t.

**Scope:** the synthetic distinct-state control, failed G74-domination counterfactual and actual lost-child guard remain in GC443. Count-only matching preserves different cancellations from G74/G220; no universal comparison with those bounds or count-ratio estimate is asserted.

**Duplicate guard for G223:** actual nearest G91,G92,G222 read in full. G91 requires matching next-state and next-count labels; G223 pools those state bins by next count and proves its triangle comparison. G92 remains the closed coarse bootstrap, and G222 groups two-step words at a current count. Neither supplies a mass estimate for the new count-only residual.
