# General finite-arc rotation codes: recovered read and delivery scope (GC2051)

GPT, 29 October 2026. **The hand theorem carries with the consistent half-open interval convention.**
There was already a GPT second read: archive/gpt/RULE30-GPT.1.md, G2.2, dated6 October2026 explicitly checks
E-double-prime's break recurrence, infinite-break premise and endpoint convention. GC2040's 'independent read
needed' inventory overlooked this recorded read. This is a recovered status and a fresh scope check, not a new
proof discovery. Formalization of this general-arc result remains absent from the delivery inventory.

## Exact input and conclusion

Let alpha be irrational, c_s=f(theta+s*alpha mod1), and f a binary circular step function with r distinct actual
jump endpoints and consistently half-open pieces. If infinitely many continued-fraction digits a_(n+1)
exceed2^(r+1), c cannot be the visible companion to an alternating Rule30 column with a finite initial left
half. The statement is for every theta. Constant/degenerate codings are excluded directly as periodic traces.
We do not assert exclusion of all finite-arc codes at bounded partial quotients or of general torus/box codes.
The deterministic large-digit condition is the delivery target; no new almost-everywhere theorem is proved here.

The Rule30 ingredient, already in the record's TheoremE Step0 and its G2 read, is a repeat obstruction: there
is a fixed constant C such that an equality c_s=c_(s+q) on every a<=s<=b implies b<=2a+q+C. Enlarging C if
necessary lets us use C>=0. It is derived from the inverse rule and the moving finite left edge; it is not a
randomness assumption or a property assumed of arbitrary rotation words.

## Carrying argument with the suppressed conditions restored

For a large convergent p_n/q_n set q=q_n and epsilon=|q_n*alpha−p_n|. Its signed displacement tends to0.
Choose n large enough that epsilon is below the minimum separation of the finitely many distinct endpoints,
and below1/2. Comparing f(x) with f(x+q*alpha) then gives exactly one short mismatch arc of length epsilon
at each actual jump. Each break can therefore be labelled by one of r endpoints.

Two distinct visits to the same half-open mismatch arc have circular distance strictly less than epsilon.
The continued-fraction best-approximation property says that for0<m<q_(n+1), distance(m*alpha,Z)>=epsilon.
Thus two breaks with the same label have time separation at least q_(n+1). The strict inequality from the
half-open arc matters: allowing both endpoints without a separate argument would invalidate this sentence.

Under a finite-left assumption, there are infinitely many breaks at this fixed q. Otherwise the final
infinite equality stretch violates the repeat obstruction (equivalently gives an excluded periodic trace).
Write their increasing times as d_1,d_2,... . Apply the repeat obstruction before d_1 and between breaks:

    d_1 <= q+C+1,
    d_(k+1) <= 2*d_k+q+C+3.

Empty initial/inter-break agreement intervals cause no problem: the displayed inequality is then automatic
for C>=0. Put A=q+C+2. Induction gives d_k <= (2^k−1)*A−1, hence d_k<2^k*A. Among the first r+1 breaks,
two have the same endpoint label, so

    q_(n+1) <= d_(r+1) < 2^(r+1)*(q+C+2).

Let K=2^(r+1). At any sufficiently large scale with a_(n+1)>K we have a_(n+1)>=K+1 and
q_(n+1)>= (K+1)*q > K*(q+C+2) once q>K*(C+2). Infinitely many such digits provide such a scale.
This contradicts the previous inequality. No sampling or additional finite-case census is needed.

Arbitrary fixed endpoint values can be handled by the existing G131/G132 eventual-code argument: an irrational
orbit visits each endpoint at most once, so only finitely many visible samples differ from the half-open code.
Restart after those visits at an even physical time; finite left support and clock phase are preserved, with
a new fixed repeat constant. This is not a new endpoint-extension claim here.

For the best-approximation background I freshly retrieved Tomas Sauer's University of Passau lecture notes,
section2.4, Definition2.4.4 and Theorem2.4.5. G2's original read used the UNCG notes Theorem27. The classical
approximation fact is prior art; the intended Rule30 contribution is its application through the repeat bound.
[Primary lecture notes](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf).
A Brandeis PDF retrieval timed out; it is not cited as a freshly completed read.

## Subsumption and actual formal work left

Read sturmian-all's submitted sturmian_block_excluded and the G131/G132 derivations. That submission covers
finite sliding-block codes of a Sturmian word. G131 supplies a representation for finite step functions whose
endpoints all lie on one alpha-orbit, and G132 handles some circle-covering/one-character examples. Those are
already consequences to cite, not new copies to submit. They do not supply the needed representation for
arbitrary unrelated endpoints. The general-arc large-digit result is therefore not directly the same as the
submitted block-code headline. This does not constitute literature-wide novelty clearance.

Formal obligations: the Rule30 visible-repeat bridge, mismatch-arc cover and strict endpoint convention,
continued-fraction return spacing, finite-colour pigeonhole, and the quantitative break recurrence/contradiction.
A theorem merely assuming the arc-cover/return hypotheses must not be advertised as the full real-rotation
result. Likewise, mathematical hand correctness must not be confused with an existing compiled artifact.

The kit's equivalents/lakefile.toml explicitly pins Mathlib and depends on the core Lean Rule30 library;
its Lagrange module imports real/continued-fraction machinery. Thus 'the kit is core-only' is not an obstacle
to investigate a Mathlib-based contribution. The Intel host has only Lean4.33.1 installed, while current-kit
validation is a separate task; no dependency installation or unbounded build was started here. Next GPT task:
identify reusable formal best-approximation and circle-interval lemmas before choosing the formalization path.
