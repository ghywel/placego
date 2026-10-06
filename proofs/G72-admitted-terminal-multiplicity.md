# admitted terminal multiplicity

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT72. admitted terminal
multiplicity (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Few surviving Collatz numbers can arrive at the same value: at most 1 + a/3 of them.

**What it says.** Among starting numbers of a given size that survive m steps with a odd steps, at most 1 +
floor(a/3) can end on the same value.

**Why it matters.** Paths rarely merge, so counting end values nearly counts starts. The bookkeeping stays almost
one to one.

**An everyday picture.** Few trains can arrive at the same platform at the same minute.

## The formal statement and proof

### G72. A polynomial bound on admitted terminal multiplicity (2026-10-06)

Continue the selected coefficient-survivor ensemble, respecting Local's separate width40 counting claim. Fix m>=1. For each coefficient-admissible length-m word w, let r be its least representative, a its odd count, B its intercept, and q=T^m(r). The corresponding width-(m+1) start is n=2^m+r, with terminal y=3^a+q. The parity bijection, least-terminal-residue lemma and G67's barrier position bound are already recorded; the following is an elementary synthesis with no novelty or mixing claim.

**Offset interval.** Every admissible word obeys p_i<=floor(i*log2(3)), by the proper prefix before its(i+1)-st odd step. Thus B<=B_max(a) from G67, even when m is not its first-deficit length. This is an upper bound only; its extremizer need not fit length m. The increasing positions also satisfy p_i>=i, giving

    B>=sum_i 3^(a-1-i)*2^i=3^a-2^a.

At a fixed terminal q and odd count a,2^m*q=3^a*r+B. Distinct representatives r have distinct offsets B separated by multiples of3^a. The number of such offsets in the indicated interval, and therefore the fibre size, is at most

    L(a)=1+floor((B_max(a)-(3^a-2^a))/3^a)
        <=1+floor(a/3).

The conservative last bound follows from G67's B_max<=a*3^a/3 and positivity of the lower endpoint. No monotonicity or tightness of L(a) is asserted.

**The upper-half terminal labels its odd count.** The least-residue lemma gives0<=q<3^a, hence

    3^a<=y<2*3^a.

These intervals are disjoint for distinct a. Therefore y determines a, and the same L(a) bound holds for its full fibre across all admitted odd-count classes. In particular the terminal map from admitted width-(m+1) starts has multiplicity at most L_m=max_(1<=a<=m)L(a)<=1+floor(m/3).

For a uniform distribution on N admitted starts, each terminal atom has probability at most L_m/N. Since y is deterministic, its Shannon entropy in bits satisfies

    H(y)>=log2(N)-log2(L_m).

This bounds loss of initial information by a logarithmic quantity. It does not assert terminal residues are uniform, independent or fair in either base. G44's sparse-cylinder obstruction remains intact.

**Why this is relevant to the selected event.** Starts in the same terminal fibre have the same a and the same future integer orbit. Their future coefficient-barrier status is therefore identical: at d more steps it depends on3^(a+future_odd_count)/2^(m+d), not the original representative. Future coefficient counts can consequently be written as sums of fibre sizes over a selected terminal set, with each weight at most L_m. This does not give the selected set's size relative to its coin probability. In particular the bound is not a uniform all-cylinder density comparison, and it gives no bounded hazard debt by itself. Actual survival compares iterates with the original start and is a separate predicate; no fibre equivalence is claimed for that predicate.

**Unexpected barrier guard.** At m6, the width-seven starts85,84,80 have parity words100000,001000,000010 and all end at y4 after six steps. Their odd count is a1 and the fibre size is3, whereas L(1)=1. These words are not coefficient-admissible: the first has a deficit at step2 and the other two at step1. Thus dropping the barrier invalidates the multiplicity bound. More generally all m words with one odd step have terminal q in{1,2}, giving unbounded unrestricted multiplicity as m grows. The disjoint odd-count terminal intervals alone do not control multiplicity.

**Next controls, preregistered NOT RUN.** FM1: reuse admitted words at m1..12 (the BT1 population), independently evolve the upper-half starts, verify their terminal odd-count labels, offset interval and exact L(a) fibre bound, recording all non-singleton fibres if any. FM2: for those fibres, compare coefficient-survival statuses through eight additional steps by independent evolution of each start; verify agreement within a fibre and the weighted selected-terminal count. Predict no bound/label/status failure; no collision frequency prediction. Counterfactual: the same L(a) holds without the barrier; must fail on the three m6,a1 starts above. These are bounded controls, not Local's width40 job or an asymptotic entropy measurement. Independent Local reading requested.


### G72 controls outcome (2026-10-06)

FM1 passes507 admitted starts across m1..12, independently comparing parity-word specifications with upper-half trajectories, odd-count terminal labels, offset intervals and exact L(a) bounds. They give507 distinct terminal values: no non-singleton admitted fibre occurs in this sample. Thus it does not empirically exercise the multiplicity bound on an actual admitted collision. FM2 passes4563 future coefficient-status checks and108 weighted selected-terminal counts through eight additional steps. The unexpected unrestricted m6,a1 guard has all three starts85,84,80 end at4 and refutes dropping admission, as predicted.

Probe: `tests/probes/prizes/collatz_gpt_terminal_fibres.py`; Python on GPT's Intel host, under1 s. No control failed. Entropy remains an analytic consequence, not an estimated limit or a measurement. Cloud's documentation sweep is read and preserved; Local's width40 counting claim remains separate. The following addendum strengthens the algebraic statement rather than enlarge the sample to find a collision.

### G72 addendum: merging starts are close; a short input label restores injectivity (2026-10-06)

The same proof yields more than a cardinality bound. If two admitted width-(m+1) starts n,n' have the same terminal y, they have the same odd count a. Their affine identities imply

    3^a*(n-n')=B'-B,
    abs(n-n')<a/3<=m/3.

The strict inequality uses B_max<=a*3^a/3 and the positive lower intercept3^a-2^a. All admitted starts are odd, since a first even step would immediately violate the coefficient barrier. Their offsets in a fixed terminal fibre are therefore spaced by multiples of2*3^a. The sharper bound is

    L_odd(a)=1+floor((B_max(a)-(3^a-2^a))/(2*3^a))
            <=ceil(a/6).

The final inequality follows from a fibre's span being strictly less than a/3 and spacing at least2. It is a conservative bound, not an assertion of attainable collisions. The terminal entropy bound improves by replacing L_m with max L_odd(a)<=ceil(m/6).

Let s be the least nonnegative integer with3*2^s>=m. Then the map

    n -> (terminal y, n modulo2^s)

is injective on the admitted width-(m+1) ensemble. Equal labels would make the nonzero difference at least2^s>=m/3, contradicting the strict span bound. Since s=O(log m) and s<=m, the low-input label can equivalently be given by the first s parity bits, by the known parity bijection. At s0 the modulus is1. This is exact reconstruction with a short side label, not a fairness or future-distribution statement.

**Unexpected admission guard for the stronger claim.** At m9, unrestricted odd starts625 and597 both have a2 and terminal11. Their parity words are101000000 and100000001; their trajectories are625,938,469,704,352,176,88,44,22,11 and597,896,448,224,112,56,28,14,7,11. Their low residues modulo4 agree (both1), as do their first two parities10, so the joint label is not injective. Here s2 since3*4>=9. Both have already had coefficient deficits, at steps4 and2 respectively. Their difference28 also violates the admitted span bound9/3. This exact counterexample strengthens the original barrier guard without asserting any admitted collision.

**Next control, preregistered NOT RUN.** FM3: on the same admitted m1..12 population, check L_odd(a), the strict fibre-span bound, and injectivity of both short labels (y,low input residue) and(y,first s parities), including modulus1. Predict no failure; the existing FM1 result says these samples have no admitted non-singleton fibres, so this sample does not empirically exercise the collision-span case. Independently evolve the two unrestricted m9 guard trajectories and require their matching labels and failure of admission. No larger census or Local compute job. This addendum is a direct algebraic refinement, not a new asymptotic count theorem; independent reading requested.


### G72 short-label controls outcome (2026-10-06)

FM3 passes507 admitted starts/507 terminal fibres at m1..12, checking sharp odd-input multiplicity bounds, strict spans, low-residue labels and parity-prefix labels. Four admitted starts exercise modulus1. There are still no admitted non-singleton fibres in this sample, so its collision-span cases are not empirically exercised. The unrestricted625/597 guard trajectories are independently checked: both end at11 after9 steps with a2, share both short labels, and fail admission and the span bound. Probe mode: `tests/probes/prizes/collatz_gpt_terminal_fibres.py --short-labels`; predictions atfc268ed, Python on GPT's Intel host, under1 s. No control failed; no larger population was run. G73 extends the analytic result to specified finite tail horizons.
