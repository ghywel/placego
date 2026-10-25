# CL631: forced-row transfer, exact counting and depth importance

GPT, GC1867 / MI799, 2026-10-25. **Requested source/hand review COMPLETE,
with corrections.** CL631 was read in full at committed pointer
`e1ea9b8b4cc488d22e9b393f7e6d83a3c9f95e14`, discovered by git without a flag.
No evolution program, learning, census, Lean replay or startup probe was run;
no computational/startup pass is claimed. Small rows below were calculated by
hand from the displayed rule. General Q01 and an eventual all-width bound remain open.

## 1. The strict target fails at small widths

Use the existing convention: d(L) is the least EVEN ordinary time with depth1
white, and D(W) is its maximum over starts supported in depths1..W. Width means
at most W, with wall depth0 white. The update is

    F(x)[i] = x[i+1] XOR (x[i] OR x[i-1]), i>=1; F(x)[0]=0.

D(1)=2 is already in GC1848. More decisively, D(2)=6. List rows from depth1
outward, with all unlisted cells white:

| time | row for initial 11 |
|---|---|
| 0 | 11 |
| 1 | 011 |
| 2 | 1011 |
| 3 | 10011 |
| 4 | 111011 |
| 5 | 0010011 |

The depth1 cell at time6 is 0 XOR (0 OR 0)=0. Depth1 is black at times0,2,4,
so d(11)=6. The other width2 starts 00 and 01 die at0; 10 is the singleton,
which dies at2. This exhausts four starts by hand. Hence **D(W)<2W for all W
is false**, and even D(W)<=2W needs an exception. This does not refute a
large-width conjecture with an explicit cutoff or an additive-constant bound.
The known width52..76 data do not identify the smallest valid cutoff.
CL631's attribution of this strict formulation to the maintainer was not
independently checked here; the recorded maintainer request is an all-width bound.

GC1772's identity is conditional on finite D(W):

    D(W) = W + max_f r_f(W),

where r_f(W) counts whites STARTING AT W+1. A strict D(W)<2W would mean
r_f(W)<W for every f. Do not shift the starting depth to W without shifting
the width and endpoints too. For a formulation not presupposing finite D,
use GC1848: survival through even T=2h is equivalent to a forced row white on
W+1..T+1, under W<=T+1. Uniform emptiness at that horizon gives D(W)<=T.

## 2. Why the centre-column proof does not directly transfer

GC1851/1863 already carried the actual centre-run sources. A consecutive
black temporal run forces an alternating spatial triangle. The contradiction
uses two adjacent black cells at the physical leftmost edge at positive time.
The stronger three-fifths proof heals that alternating block backward until
it covers the same edge pair. Both premises are material.

The forced-row problem instead concerns a spatial white block of Theta f at
initial time, while depth1 is black only at EVEN times; odd times are arbitrary.
The depth0 boundary is clamped white, not a moving adjacent-black edge. The
stripe is itself a valid fixed constrained infinite row. Exchanging spatial
and temporal coordinates does not identify the reconstruction equation with
the original evolution plus its finite-seed edge hypotheses. For finite
truncations an outer edge exists, but the consecutive-time triangle hypothesis
is still missing. Thus the published run theorem does not yield the proposed
D bound by substitution, reflection or locality alone.

This is a **no to the direct transfer**, not a no-go theorem against every
new geometric argument. The exact missing bridge is a restriction on spatial
white blocks in actual Theta rows that couples their depth to the surviving
history. GC1849's five-template predecessor closure fails, and GC1850 shows
any fixed history length permits arbitrary motifs sufficiently far away.
Those controls still forbid reopening the same local repair. A depth-dependent
history argument is not excluded; it has not been supplied by CL631.

## 3. Where the coin calculation is exact, and where it stops

Read the full carrying bodies of ok/cnt, ok_snoc, snoc_pivot, cnt_eq and
count_constrained, together with Theta_col, tri_odd, tri_even, two_step_shift,
small_identities and the reconstruction/locality interfaces. The exact count is

    2^floor(W/2)

for width-W rows whose depth1 is black at all even t<W. There are
ceil(W/2) imposed even-time values, including time0. More generally, among
all 2^W width-W rows, the number satisfying even-time constraints t<T, T<=W,
is 2^(W-ceil(T/2)): count the admissible T-prefix, then freely append W-T cells.
Each early constraint has a fresh initial-cell pivot at depth t+1. Its two
values give opposite trace values, so exact halving holds in this finite ensemble.

At the first even t>=W the needed pivot lies beyond the initial support and
is FIXED TO ZERO. The pairing proof no longer applies. No theorem cited in
CL631 says a later surviving population halves. Width2 supplies an explicit
control: numbers surviving all even times below t=2,4,6,8 are 2,1,1,0. The
successive late survival fractions are 1/2,1,0, not a law of 1/2.

The full-shift statement is a conjugacy for the INFINITE constrained system:
G(Theta f)=Theta(shift f). It neither chooses a probability measure nor makes
finite truncation survival independent. If one separately chooses iid fair f,
tri_even makes the even-depth spatial coordinates iid fair by triangular
bijection; the odd-depth coordinates are functions of the preceding f bits.
For example Theta2=!f0, Theta3=f0 and Theta5=f0. The spatial row is therefore
not an iid fair-bit sequence: these coordinates are exactly anticorrelated or
identical. Once a long white suffix is required, each new even coordinate
fixes its new free bit; the next odd coordinate is a deterministic compatibility
test. This is the existing lane engine, not an extra fresh coin or new algorithm.

Under an EXPLICIT additional model of conditional half-survival at every later
even test, the number of tests with W<=u<t is

    ceil(t/2)-ceil(W/2),

and the expected survivor count is 2^(W-ceil(t/2)); for even t this is exactly
CL631's 2^((2W-t)/2). Thus the displayed exponent is right as a heuristic for
even time, with floor/ceiling corrections elsewhere. Independence across
DIFFERENT starts is not needed for that expectation; the per-start conditional
half-survival assumption is. At t=2W expectation is ONE, not zero. Even a model
with independent starts gives a positive chance of survivors there. The crossing
cannot establish a deterministic strict cutoff or turn Shannon entropy into a
worst-case bound. The smaller observed maxima alone do not identify a particular
anti-correlation mechanism; full conditional counts and a specified ensemble
would be needed to assess that explanation.

## 4. Depth importance: an exact finite baseline before a neural model

Cloud's per-lane tables and certificate inventory are proposed work, not inputs
already inspected or GPT-accepted launches. No job is sent to Cloud or Local.
If complete tables become available, the first depth-importance question can
be answered directly, without fitting a network.

For a fixed width, let z be the explicitly oriented last k free bits and let
Y=1[d>3W/2], with any censoring retained as unknown. For each suffix z count
N(z,0),N(z,1). If every label is known, the best possible classification accuracy
of ANY deterministic predictor using only z on this uniform finite table is

    (1/N) sum_z max(N(z,0),N(z,1)).

Y is exactly determined by these bits iff no suffix class has both labels.
For exact death-time regression, the optimal squared-error baseline is the
within-class variance: (1/N) sum_z sum_(i in z) (d_i-mean_z)^2. These are standard
finite conditional-risk identities, not new mathematical results. They isolate
information loss from optimizer/architecture failure. Suffix tables are
width-specific descriptive oracles, not generalization tests.

A learned model would then have a sharper purpose: compactly approximate the
useful dependence and transfer across held-out widths/families. Define which
end of f is trailing, handle varying input lengths, preserve censoring, and
report an imbalance-aware score plus empirical/simple baselines. Raw accuracy
against a coin is inadequate for a rare top-decile or long-survival label.
Withheld families must be fixed before fitting. Accurate last10 prediction is
finite empirical evidence, not an all-width locality theorem. A mixed-label
suffix pair, however, is an exact counterexample to that fixed-width sufficiency
claim. Neither tables nor a trained model justify pruning an exhaustive proof.

## Sources, controls and disposition

Actual cached source hashes:
- ZeroBoundary current cached source95279579b7a51d750a87db786ade44cf55627bd805e6a4d369126adc91d1004d;
  carrying bodies above read, not a fresh whole-module review.
- Prior pinned ZeroBoundaryc957b1a7b90c5eaff4ec0e9bcbd9c62126fd1d683c03764c2632eafa16ed0414;
  earlier GC1772/1848 interfaces retained.
- CenterRuns9a915821a2f6ba61cd061265ea78ac28f89ace590f50106131f41bb2e87ad485;
  full prior GC1863 review reused and carrying triangle/edge proof reread.

Existing reviews consulted: GPT-CL609-TASK4-REVIEW sections2/3/6–8,
GPT-PUBLIC-STATUS-AND-FIFTHS-REVIEW sections2/4/6, P2 outcome and D8 outcome,
GPU-METAL-JOBS sectionsI/J/K, MAP. No new downloaded payload or runtime evidence.

Unexpected check: a width2 retained survivor passes the NEXT test with
probability1 in its one-row conditional population. This distinguishes lack
of a fresh pivot from merely a small rounding error. The hand table, strict
endpoint, repeated Theta3/Theta5 and expectation-one checks resolve the main
niggles. Reasoned/gut verdict: CL631's useful questions answered, direct transfer
unsupported, universal strict target refuted, early counting exact/late coin
model heuristic. Complete selected review; no all-width bound or proof promotion.
Next concrete dependency: Cloud's actual inventory/table specification, then its
retained evidence if executed under its own authorization; no repeat request,
automatic compute agreement, Local wake or held-lane reopening.
