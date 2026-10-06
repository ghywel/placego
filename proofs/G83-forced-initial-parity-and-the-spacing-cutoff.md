# forced initial parity and the spacing cutoff

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT83. forced initial parity
and the spacing cutoff (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The prefix growth-factor condition rules out two starts meeting with the same odd-step count up to 20.

**What it says.** Require the multiplier from tripling and halving to stay at least one after every prefix of the step pattern. Any such pattern lasting two steps begins with two odd steps. Its start therefore leaves remainder 3 on division by 4. Two different starts with the same final value and the same number of odd steps must differ by at least 4. The exact range of their additive offsets is too small to allow that through 20 odd steps.

**Why it matters.** This extends the finite word search through 17 using a proof and exact arithmetic. It concerns the growth-factor condition, which differs from requiring the actual number to stay above its start. The new spacing proof awaits independent review; it does not resolve Collatz.

**An everyday picture.** Two arrivals must be at least four minutes apart, but their permitted arrival window is shorter than four minutes.

## The formal statement and proof

### G83. Forced initial parity sharpens admitted fibre spacing (2026-10-06)

Reply L040/L043. Admission through step 2 forces both initial parity bits to be11: one odd step would leave coefficient3<4. Thus every admitted start at a horizon t>=2 is3 modulo 4. Any same-odd-count terminal collision has displacement delta=(B-B')/3^a divisible by 4, rather than merely even. At t = 1 the affine map with the admitted first bit1 is already injective; this short horizon must be handled separately.

For a>=2 pad the admitted words to t_a as in G81. Their intercepts lie between B_min=3^a-2^a (all a odd positions first) and G67's B_max. The lower bound follows termwise from p_i>=i; the all-ones prefix followed by zeroes is admitted through t_a and attains it. Define the exact normalized span

    R_a=(B_max-(3^a-2^a))/3^a.

In any fixed-a terminal fibre, distinct starts are separated by at least4 and their full span is at most R_a. Consequently

    fibre size <= 1+floor(R_a/4),
    R_a <= a/3-1+(2/3)^a.

This bound applies to the admitted words at any shorter horizon by padding, and to all terminal fibres in G73's domain because there the terminal labels a. It is a stronger multiplicity bound, not a proof of singleton fibres at every a.

**Analytic cutoff.** The right-hand side increases with a: its successive difference is(1-(2/3)^a)/3>0. At a = 14 it is11/3+(2/3)^14<4, since(2/3)^14<(2/3)^3=8/27<1/3. Hence R_a<4 for2<=a<=14, so delta must be zero and the affine map forces the starts to coincide. The a = 1 case has only the admitted length-one word. Therefore same-odd-count admitted collisions require a>=15. This explains more of L040's unexercised fibre bound analytically; L043's independent exhaustive code search already excludes a<=17, a stronger finite cutoff. No duplication of that search is requested.

The exact spans also have a simple recurrence, from appending the last term of B_max:

    R_(a+1)-R_a=2^floor(log_2(3^a))/3^(a+1)-(2/3)^a/3.

For a>=2 its first term exceeds1/6, while the subtracted term is at most4/27<1/6, so R_a strictly increases there; R_1=R_2=0. This identifies where the spacing bound can first stop proving injectivity, without searching words or claiming a collision actually exists.

**Unexpected short-horizon guard.** At t = 1, n = 1 is coefficient-admitted but is1 modulo 4, so the assertion that every admitted start is3 modulo 4 is false without t>=2. It does not refute injectivity at that horizon. The unrestricted625/597 guard remains outside admission and does not challenge the span bound, even though its displacement28 is divisible by 4.

**Next controls, preregistered NOT RUN.** FS1: exact integer intercept-span recurrence and monotonicity for a = 1 to 64, locate the first a with R_a>=4 (no numerical value predicted); require R_a<4 through 14. FS2: reuse the already covered a = 1 to 12 words to verify first11, the common offset residue5*3^(a-2) modulo 4 for a>=2, and the exact span bounds; independently check both short-horizon and unrestricted guards. Counterfactual: the3-modulo 4 requirement applies already at horizon1; must fail on n = 1. No new a = 13 to 17 enumeration or actual-start population. The derivation uses only the recorded affine/barrier identities and offset extrema; independent reading requested, no novelty or prize claim.

### G83 exact-span controls and stronger cutoff (2026-10-06)

FS1 passes 64 exact span bounds and63 recurrence comparisons. The first a with R_a>=4 is21, an unpredicted arithmetic outcome. The exact bracket is

    R_20=13805179460/3486784401<4,
    R_21=43561973452/10460353203>4.

G83's proved monotonicity therefore gives R_a<4 for every a<=20. Combining the exact integer evaluation with the spacing 4 argument analytically excludes same-odd-count admitted collisions through a = 20, across widths and horizons. This is not a new word enumeration; it strengthens Local L043's a<=17 finite code result using the extrema and a proved recurrence. At a = 21 the bound merely stops excluding a collision; no collision, frequency estimate or all-a singleton theorem follows.

FS2 passes 4403 existing a = 1 to 12 admitted words, checking initial11, common offset residue modulo 4 and exact extrema. Both guards pass, and unconditional3-modulo 4 at horizon1 is refuted on n = 1. Probe: `tests/probes/prizes/collatz_gpt_forced_spacing.py`; predictions ate9b1213, GPT Intel Python, under1 s. No control failed; no Local a = 13 to 17 search or actual-start population was repeated. Independent review of the new spacing lemma and strengthened cutoff remains pending.

*Second reader's note on G83 (Local, 2026-10-06; chat L046).* Correct. Admission through step 2 forces the bits 11,
so admitted starts at $t \ge 2$ are $3 \bmod 4$ and same-count displacements are multiples of 4; the span bound and
its recurrence are exact. Checked (`collatz_audit_g83_g89.py`, K2): over every admitted word the least intercept is
$3^a - 2^a$ and the greatest is G67's $B_{\max}$, for $a \le 22$; $R_a$ increases for $a \ge 2$ and obeys the bound
for $a \le 64$; $R_{20} < 4 < R_{21}$ with the stated fractions; $R_{22} = 4.438 < 8$. Independently, enumerating all
of $W_a$ with no pruning finds no realized same-count collision for any $a \le 21$ (K1), confirming the analytic cutoff
at 20 and, by a different method, G88's certificate at 21.
