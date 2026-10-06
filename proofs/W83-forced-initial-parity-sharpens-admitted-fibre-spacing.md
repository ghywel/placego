# Forced initial parity sharpens admitted fibre spacing

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G83. Forced initial parity
sharpens admitted fibre spacing (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Surviving Collatz numbers always start with two odd steps, which rules out meetings for up to 20 odd steps without a
search.

**What it says.** To keep its growth factor at least 1 through two steps, a number must take two odd steps first, so
it leaves a remainder of 3 when divided by 4. Two surviving numbers that meet must therefore differ by a multiple of
4. GPT combined that with the known range of offsets to show that no two such numbers can meet when the number of
odd steps a is between 2 and 14; an exact calculation of the same bound then carries this to a = 20.

**Why it matters.** It goes past the finite search that followed G81 (no meeting up to a = 17) with a short
argument, and sharpens the bound on how many numbers can share an end value. It has not yet had its second reading.

**An everyday picture.** If every guest arrives on the hour or at a quarter past, and the doors are less than four
minutes apart, no two guests can collide in the doorway.

## The formal statement and proof

Reply L040/L043. Admission through step2 forces both initial parity bits to be11: one odd step would leave coefficient3<4. Thus every admitted start at a horizon t>=2 is3 modulo4. Any same-odd-count terminal collision has displacement delta=(B-B')/3^a divisible by4, rather than merely even. At t1 the affine map with the admitted first bit1 is already injective; this short horizon must be handled separately.

For a>=2 pad the admitted words to t_a as in G81. Their intercepts lie between B_min=3^a-2^a (all a odd positions first) and G67's B_max. The lower bound follows termwise from p_i>=i; the all-ones prefix followed by zeroes is admitted through t_a and attains it. Define the exact normalized span

    R_a=(B_max-(3^a-2^a))/3^a.

In any fixed-a terminal fibre, distinct starts are separated by at least4 and their full span is at most R_a. Consequently

    fibre size <= 1+floor(R_a/4),
    R_a <= a/3-1+(2/3)^a.

This bound applies to the admitted words at any shorter horizon by padding, and to all terminal fibres in G73's domain because there the terminal labels a. It is a stronger multiplicity bound, not a proof of singleton fibres at every a.

**Analytic cutoff.** The right-hand side increases with a: its successive difference is(1-(2/3)^a)/3>0. At a14 it is11/3+(2/3)^14<4, since(2/3)^14<(2/3)^3=8/27<1/3. Hence R_a<4 for2<=a<=14, so delta must be zero and the affine map forces the starts to coincide. The a1 case has only the admitted length-one word. Therefore same-odd-count admitted collisions require a>=15. This explains more of L040's unexercised fibre bound analytically; L043's independent exhaustive code search already excludes a<=17, a stronger finite cutoff. No duplication of that search is requested.

The exact spans also have a simple recurrence, from appending the last term of B_max:

    R_(a+1)-R_a=2^floor(log_2(3^a))/3^(a+1)-(2/3)^a/3.

For a>=2 its first term exceeds1/6, while the subtracted term is at most4/27<1/6, so R_a strictly increases there; R_1=R_2=0. This identifies where the spacing bound can first stop proving injectivity, without searching words or claiming a collision actually exists.

**Unexpected short-horizon guard.** At t1, n1 is coefficient-admitted but is1 modulo4, so the assertion that every admitted start is3 modulo4 is false without t>=2. It does not refute injectivity at that horizon. The unrestricted625/597 guard remains outside admission and does not challenge the span bound, even though its displacement28 is divisible by4.

**Next controls, preregistered NOT RUN.** FS1: exact integer intercept-span recurrence and monotonicity for a1..64, locate the first a with R_a>=4 (no numerical value predicted); require R_a<4 through14. FS2: reuse the already covered a1..12 words to verify first11, the common offset residue5*3^(a-2) modulo4 for a>=2, and the exact span bounds; independently check both short-horizon and unrestricted guards. Counterfactual: the3-modulo4 requirement applies already at horizon1; must fail on n1. No new a13..17 enumeration or actual-start population. The derivation uses only the recorded affine/barrier identities and offset extrema; independent reading requested, no novelty or prize claim.


### G83 exact-span controls and stronger cutoff (2026-10-06)

FS1 passes64 exact span bounds and63 recurrence comparisons. The first a with R_a>=4 is21, an unpredicted arithmetic outcome. The exact bracket is

    R_20=13805179460/3486784401<4,
    R_21=43561973452/10460353203>4.

G83's proved monotonicity therefore gives R_a<4 for every a<=20. Combining the exact integer evaluation with the spacing4 argument analytically excludes same-odd-count admitted collisions through a20, across widths and horizons. This is not a new word enumeration; it strengthens Local L043's a<=17 finite code result using the extrema and a proved recurrence. At a21 the bound merely stops excluding a collision; no collision, frequency estimate or all-a singleton theorem follows.

FS2 passes4403 existing a1..12 admitted words, checking initial11, common offset residue modulo4 and exact extrema. Both guards pass, and unconditional3-modulo4 at horizon1 is refuted on n1. Probe: `tests/probes/prizes/collatz_gpt_forced_spacing.py`; predictions ate9b1213, GPT Intel Python, under1 s. No control failed; no Local a13..17 search or actual-start population was repeated. Independent review of the new spacing lemma and strengthened cutoff remains pending.
