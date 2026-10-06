# The proofs, one by one

*Each proof in [PROOFS.md](../PROOFS.md), the master, has its own page here. Every page opens with a summary in
plain words: what the proof says, why it matters, and an everyday picture. The full formal proof follows, ready
for review. The pages are built from the master by `python3 proofs/build.py`, and the summaries live in
[summaries.md](summaries.md); edit those two, never the pages.*

## A primer in five minutes, no maths needed

**Rule 30** is a row of squares, each black or white, that repaints itself once per tick. Every square looks at
itself and its two neighbours and follows one fixed rule. Started from a single black square, it grows a pattern
famous for looking random. The same kind of pattern appears on the shell of the sea snail *Conus textile*, which
grows its shell one edge at a time. The prize asks whether the column straight down the middle ever settles into a
repeating rhythm.

The words the summaries use:
- **The wall** (column 0). We suppose the middle column blinks black, white, black, white... for ever, and ask
  whether any finite starting row can produce that. If none can, that rhythm is ruled out. Other repeating
  rhythms are studied the same way; a **white beat** of the wall (a "hole") is where the right side can be heard.
- **The left half.** Rule 30 has a useful quirk: once you know the middle column and the one to its right, every
  square to the left is forced, like a crossword where one column of answers fixes the rest. That forced left half
  is what the proofs study.
- **Column 1.** The column just right of the middle. It is the only channel through which the right side can
  "talk" to the left.
- **A finite seed.** A starting row with only finitely many black squares. A counterexample would need the forced
  left half to go white, and stay white, far enough out.
- **Periodic.** Repeating like a drumbeat. *Eventually periodic* means repeating from some point on.
- **Entropy.** How fast the number of possible patterns grows with their length: the rate at which a column can
  carry new information. Zero entropy means almost nothing new ever arrives.
- **Relatives of Rule 30.** *Rule 90* just adds its neighbours and draws Sierpinski triangles; its arithmetic is
  clean. *Rule 210* is a sibling of Rule 30 on which parts of the question can be answered, so it serves as a test
  bed for the methods.
- **Collatz.** Take a number. If it is even, halve it. If it is odd, triple it, add one, then halve. The conjecture
  says every start eventually falls to 1. The **step pattern** is the sequence of odd and even steps. The **growth
  factor** after some steps, three to the number of odd steps divided by two to the number of steps, says roughly
  whether the number has grown or shrunk. **Surviving** means staying at or above where you started.
- **The Collatz count.** How many starting numbers of a given size survive a given number of steps, compared with
  what fair coin tosses in place of the odd and even steps would predict. If the real count never beats the coin
  count by more than a fixed factor, survivors thin out exponentially. That would be a strong "almost all numbers
  fall" result, not by itself a proof of the conjecture.
- **Who proved it.** "Local" and "Cloud" are two Claude instances, and "GPT" is a model of a different make. A proof
  counts once a second party has read it. Pages in *the waiting room* have not had that second reading yet.

## The pages

## The wall form

- [Lemma 1 (where column 1 is invisible)](01-lemma-1-where-column-1-is-invisible.md): When the middle square is
  black, the right side cannot be heard on the left at all.
- [Lemma 2 (rotations are equivalent)](02-lemma-2-rotations-are-equivalent.md): Starting the rhythm one beat later
  is the same problem, so only one starting beat needs checking.
- [Lemma 3 (two local rules from the right side)](03-lemma-3-two-local-rules-from-the-right.md): Column 1 must obey
  two simple traffic rules, whatever lies further right.
- [Lemma 4 (the newest bit of column 1 enters once, as an XOR)](04-lemma-4-the-newest-bit-of-column-1.md): Each new
  bit from column 1 reaches the left exactly once, either as a clean flip or not at all.

## Windows, zero runs and the left band

- [Theorem A (a window cannot outlast the edge)](05-theorem-a-a-window-cannot-outlast-the-edge.md): A steady rhythm
  in two neighbouring columns cannot last once news from the edge arrives.
- [Theorem B (a zero run cannot outlast two periods)](06-theorem-b-a-zero-run-cannot-outlast-two.md): If the middle
  and column 1 both repeat, the forced left half can never be silent for more than two periods.
- [Theorem A′ (a block recurs only if it is no longer than the edge is far)](07-theorem-a-a-block-recurs-only-if-it.md):
  A pattern can only repeat if it is shorter than the distance to the edge.
- [Lemma B1 (white, then black)](08-lemma-b1-white-then-black.md): In the band near the edge, two neighbouring
  diagonals can never both fall silent for ever.
- [Lemma B2 (the clock never stops)](09-lemma-b2-the-clock-never-stops.md): The edge band's rhythms keep slowing
  down for ever: the clock never stops.
- [Theorem A‴ (the window principle, with the band)](10-theorem-a-the-window-principle-with-the-band.md): A repeat
  leaves a white stripe behind it, and a black diagonal there caps the repeat.
- [Corollary F (near-squares at the start are fatal)](11-corollary-f-near-squares-at-the-start-are.md): A column 1
  that starts by almost repeating itself, at bigger and bigger scales, is fatal.
- [Lemma B3 (the settled band has no long white run)](12-lemma-b3-the-settled-band-has-no-long.md): Once the edge
  band settles into its rhythm, it has no long white gaps.
- [Theorem A⁗ (a repeat's white run cannot lie in the settled band)](13-theorem-a-a-repeat-s-white-run-cannot.md):
  The white stripe a repeat leaves cannot sit inside the settled band.
- [Theorem E](14-theorem-e.md): A perfectly regular wheel, never nudged, cannot produce the pattern.
- [Theorem E″ (any arcs, for a typical rotation number; added the same night)](15-theorem-e-any-arcs-for-a-typical-rotation.md):
  The same holds for almost every wheel speed, whatever pattern of marks it passes.

## Siblings, Jen and the squeeze

- [Proposition 5 (Rule 90 has no finite configuration with a period-two column)](16-proposition-5-rule-90-has-no-finite-configuration.md):
  In Rule 30's simpler cousin, Rule 90, the blinking middle is impossible, proved with Pascal's triangle.
- [Proposition 7 (Jen)](17-proposition-7-jen.md): If both the middle and column 1 eventually repeat, the left half
  cannot be finite (Jen's theorem).
- [Theorem (the parity invariant)](18-theorem-the-parity-invariant.md): Next to a blinking wall, Rule 30's sibling
  Rule 210 behaves exactly like the simple cousin Rule 90.
- [Lemma (the squeeze)](19-lemma-the-squeeze.md): A counterexample would have to be almost frozen: the right side
  can only whisper.
- [Proposition 6 (computed): the pure wheel cannot make a finite left half](20-proposition-6-computed-the-pure-wheel-cannot-make.md):
  We ran the pure wheel until it repeated, about 15 billion ticks, and checked: it fails.

## Short proofs restated from the running text

*From the head of this section in PROOFS.md:*

These were proved inside sections as running text. They are restated so that each is a checkable unit.

*The pages:*

- [The checkerboard lemma](C1-the-checkerboard-lemma.md): While the middle column stays black, the left half next to
  it is a fixed checkerboard, whatever the right side does.
- [The latch](C2-the-latch.md): While the middle column stays white, column 1 can switch on but never off.
- [The shrink theorem for white triangles](C3-the-shrink-theorem-for-white-triangles.md): A run of white squares
  shrinks by exactly one square at each end per tick, so Rule 30's white triangles are perfect.
- [The leftward speed of information is an identity](C4-the-leftward-speed-of-information-is-an-identity.md): How
  fast news travels leftwards in Rule 30 is an exact bookkeeping identity: full speed, minus the times it gets
  squashed.
- [The triangle law of the uniform measure](C5-the-triangle-law-of-the-uniform-measure.md): In a random row, Rule 30
  keeps the row random, so white triangles of each width appear at an exact, predictable rate.
- [Gliders on prime rings](C6-gliders-on-prime-rings.md): On a ring with a prime number of squares, any rhythm that
  is rare must be a pattern travelling round the ring.
- [The first three columns are affine in column 1](C7-the-first-three-columns-are-affine-in-column.md): The first
  three columns left of the middle just copy or flip column 1; the first real mixing happens in the fourth.
- [Rule 30's velocity is Rule 210](C8-rule-30-s-velocity-is-rule-210.md): Rule 30's change from one tick to the next
  follows Rule 210, its closest sibling.

## Theorems proved by GPT

*From the head of this section in PROOFS.md:*

GPT's lane is its own file. The statements are copied so that this list is complete; GPT is asked to append its
proofs here in its own words, or to say which it would rather keep as pointers.

*The pages:*

- [G13.2. Complete reset language, with a failed first characterization retained](E1-g13-2-complete-reset-language-with-a-failed.md):
  GPT found exactly which stretches of a row erase all memory when you rebuild the row before it.
- [G13.5. Several backward steps, with the protected window's exact cost](E2-g13-5-several-backward-steps-with-the-protected.md):
  A single changed bit from the right side is forgotten at a steady rate as you go back in time: three squares per
  step.
- [G17.1. Exact all-period theorem and certificate](E3-g17-1-exact-all-period-theorem-and-certificate.md): For walls
  with one white beat per period, checking three columns on the right rules out no more than checking two.
- [G18.2. Exact finite-prefix map from a latch position](E4-g18-2-exact-finite-prefix-map-from-a.md): On a slow
  wall, the left half near the middle carries only "when did the switch go on", so there are just a + 1
  possibilities.
- [G18.3. Uniform protected-band theorem, even without a white prefix](E5-g18-3-uniform-protected-band-theorem-even-without.md):
  A long enough black stretch wipes the slate: the left half becomes a known checkerboard whatever came before.
- [G20.1. Exact theorem, including the failed first prediction](E6-g20-1-exact-theorem-including-the-failed-first.md):
  For walls with one white beat per odd period of 5 or more, even four columns of the right side allow every
  pattern.
- [G27.2. The periodic-pair obstruction works on the forced half-line](E7-g27-2-the-periodic-pair-obstruction-works-on.md):
  Jen's classic argument works from the left half alone, without assuming anything about the right.

## Collatz

- [The remainder lemma](F1-the-remainder-lemma.md): After k Collatz steps, a number's remainder in base 2 has become
  a remainder in base 3, and the rest passes through untouched.
- [Dubickas's theorem (external; the record's W2)](F2-dubickas-s-theorem-external-the-record-s-w2.md): A Collatz
  number that ran off to infinity would have to change its step pattern endlessly: it could not loop or repeat.

## GPT's proofs, second-read by Local

- [Fixed-endpoint survival conditioning](G39-fixed-endpoint-survival-conditioning.md): Insisting that a Collatz step
  pattern "survives" at every step can raise any probability by at most a factor of its length.
- [Survival-compatible adjacent-pair phase product](G40-survival-compatible-adjacent-pair-phase-product.md):
  Swapping neighbouring odd and even steps shifts a Collatz number's final value by an exact, predictable amount.
- [Interior-endpoint free-pair mass](G41-interior-endpoint-free-pair-mass.md): Typical surviving Collatz patterns
  have plenty of those independent switches: a fixed fraction of their length.
- [A primitive-character resonance with linearly many free pairs](G42-a-primitive-character-resonance-with-linearly-many-free.md):
  Many independent switches are still not enough: one particular frequency can stay perfectly in tune.
- [Exact binary-reader Fourier weights](G43-exact-binary-reader-fourier-weights.md): An exact translation table
  between base 3, where the Collatz state lives, and odd or even, which decides the next step.
- [Exact finite-ensemble parity-tail information budget](G44-exact-finite-ensemble-parity-tail-information-budget.md):
  A remainder modulo 3^a can imitate only so many fair coin tosses; ask for more and the repetition shows.
- [Word-specific actual-start survival ceilings](G45-word-specific-actual-start-survival-ceilings.md): For a given
  step pattern, the numbers that follow it and stay above their start are a fixed class with a height limit.
- [Unbounded formal ceilings and residue-count rounding](G46-unbounded-formal-ceilings-and-residue-count-rounding.md):
  Those height limits can be as large as you like, because powers of 3 sometimes come very close to powers of 2.
- [First-deficit single-run survival implies a periodic return](G47-first-deficit-single-run-survival-implies-a-periodic.md):
  For those patterns, surviving to the end would mean coming back to exactly the starting number: a cycle.
- [First-deficit gap and its positive-lift domain](G48-first-deficit-gap-and-its-positive-lift-domain.md): A simple
  formula for how far above or below its start a number ends after its first dip.
- [Computed first-deficit certificate through horizon16](G48C-computed-first-deficit-certificate-through-horizon16.md):
  A computer certificate: every number above 1 whose growth factor first dips below 1 within 16 steps really does
  drop below itself then.
- [Scope of the floor(3n/2) test bed](G49-scope-of-the-floor-3n-2-test-bed.md): A Collatz-like test bed, multiply by
  3/2 and round down, keeps the arithmetic but asks a different survival question.
- [Mahler itinerary coupling and alphabet scope](G50-mahler-itinerary-coupling-and-alphabet-scope.md): Mahler's 3/2
  problem needs two conditions at once, and its known cellular-automaton form works differently from Rule 30.
- [Exact finite Mahler coupling window](G51-exact-finite-mahler-coupling-window.md): The exact finite form of
  Mahler's two conditions over T steps: a class of whole numbers and a window of fractions.
- [Phase-aligned period-block extension of Corollary F](G52-phase-aligned-period-block-extension-of-corollary-f.md):
  Near-repeats in column 1 rule out a finite seed for every repeating wall, not only black-white.
- [Period-block form of the entropy squeeze](G53-period-block-form-of-the-entropy-squeeze.md): The information limit
  on the left half can be computed one period of the wall at a time.
- [Gap-matrix coarse squeeze for every periodic wall](G54-gap-matrix-coarse-squeeze-for-every-periodic-wall.md): A
  simple two-by-two calculation bounds the information reaching the left half, for every repeating wall.
- [Prime-ring quotient cycle lifting](G55-prime-ring-quotient-cycle-lifting.md): On a prime ring, every Rule 30
  cycle is a lifted copy of a simpler cycle, which explains when cycle lengths are distinct.
- [Prime-ring moment phase coordinate](G56-prime-ring-moment-phase-coordinate.md): A "centre of mass" for patterns
  on a prime ring tells exactly how far a cycle drifts.
- [Rule30 nonlinear correction and moment drift](G57-rule30-nonlinear-correction-and-moment-drift.md): How a Rule 30
  pattern drifts round a prime ring is set exactly by where its "and" operations happen.
- [Explicit one-parity witness](G58-explicit-one-parity-witness.md): For Rule 30's sibling Rule 210, GPT built an
  explicit left half that keeps a whole family of walls going.
- [Late nonlinear activity](G59-late-nonlinear-activity.md): In Rule 210, a finite seed with a repeating wall would
  need its "and" operations to keep happening for ever.
- [infinite right realization](G60-infinite-right-realization.md): G58's left half can be matched by a full right
  half, though an infinite one.
- [first right-layer gates](G61-first-right-layer-gates.md): In Rule 210, column 1 can carry a hidden black bit only
  at moments when the visible signal switches on.
- [first nonlinear pair](G62-first-nonlinear-pair.md): In Rule 210, the first pair of black squares next to the wall
  can appear only at a sparse list of even times: 0, 6, 30, 126, ...
- [forced right strip](G63-forced-right-strip.md): While the visible signal holds steady, each column on the right
  is forced into a fixed rhythm too.
- [fixed-column temporal complexity](G64-fixed-column-temporal-complexity.md): In that Rule 210 family, every fixed
  column on the right is almost completely predictable.
- [mirror extension and quantifiers](G65-mirror-extension-and-quantifiers.md): Any finite left half for Rule 210 can
  be matched by mirroring it on the right, and then column 1's freedom jumps.
- [bounded-left-support temporal complexity](G66-bounded-left-support-temporal-complexity.md): If the left half's
  black squares stay within a fixed distance, the right side's columns are still almost predictable.
- [first-deficit offset envelope](G67-first-deficit-offset-envelope.md): The largest possible "offset" at a first
  dip, and the pattern that reaches it.
- [endpoint digit certificates](G68-endpoint-digit-certificates.md): At a first dip, the start and the end share the
  same height limit.
- [polynomial first-deficit ceiling](G69-polynomial-first-deficit-ceiling.md): A known theorem about how close
  powers of 2 and 3 can get gives a polynomial cap on every height limit.
- [finite-horizon count bridge](G70-finite-horizon-count-bridge.md): Above a polynomial size, "the growth factor
  stays above 1" and "the number stays above its start" pick out exactly the same numbers.
- [selected critical-boundary losses](G71-selected-critical-boundary-losses.md): The surviving count loses numbers
  only at the critical boundary, and the loss is set by whether the leftover number is odd or even.
- [admitted terminal multiplicity](G72-admitted-terminal-multiplicity.md): Few surviving Collatz numbers can arrive
  at the same value: at most 1 + a/3 of them.
- [finite-tail short-label reconstruction](G73-finite-tail-short-label-reconstruction.md): For a long stretch of
  surviving steps, the current value reveals the start from a short label.
- [backward survival weights](G74-backward-survival-weights.md): The gap between the real Collatz count and the
  coin-toss prediction is an exact sum of odd-even imbalances.
- [backward coin atom bound](G75-backward-coin-atom-bound.md): Those weights are uniformly small: about (log h)/√h,
  where h is the number of steps still to go.
- [coarse triangle bootstrap obstruction](G77-coarse-triangle-bootstrap-obstruction.md): The simplest way of
  combining G74 and G75 cannot bound the Collatz count for all horizons: that route is closed.
- [ideal allocation proxy obstruction](G78-ideal-allocation-proxy-obstruction.md): Even a perfectly fair spread of
  numbers would leave that crude bound growing, so the route needs real cancellation.
- [interior mixed-pair cancellation](G80-interior-mixed-pair-cancellation.md): When a Collatz number has room to
  spare, an odd-even pair and an even-odd pair cancel to first order.
- [offset-code collision reduction](G81-offset-code-collision-reduction.md): Whether two surviving Collatz numbers
  can ever meet reduces to a finite check on step patterns.
- [localized coin overshoot and curvature](G82-localized-coin-overshoot-and-curvature.md): A sharper version of G75:
  the weights shrink like 1/√h, with no logarithm.
- [forced initial parity and the spacing cutoff](G83-forced-initial-parity-and-the-spacing-cutoff.md): The prefix
  growth-factor condition rules out two starts meeting with the same odd-step count up to 20.
- [the prefix orientation of a first collision](G84-the-prefix-orientation-of-a-first-collision.md): At 21 odd
  steps, any meeting allowed by these conditions must have one precise orientation.
- [two further forced odd bits at a = 21](G85-two-further-forced-odd-bits-at-a-21.md): The same possible pair must
  follow two more common odd steps.
- [the shifted barrier, a closed shortcut](G86-the-shifted-barrier-a-closed-shortcut.md): A prefix can buy slack
  that its remaining steps cannot satisfy on their own.
- [the offset budget and the eight-bit prefix](G87-the-offset-budget-and-the-eight-bit-prefix.md): An offset bound
  forces the sixth step and then two more steps of any possible 21-odd-step meeting pair.
- [the paired-prefix collision certificate](G88-the-paired-prefix-collision-certificate.md): A candidate tree can be
  cut off using exact bounds on every possible continuation.
- [the first admitted collisions, at odd count 22](G89-the-first-admitted-collisions-at-odd-count-22.md): Two starts
  can meet while both satisfy the prefix growth-factor condition: universal injectivity is false.
- [equal terminals do not force weighted cancellation](G90-equal-terminals-do-not-force-weighted-cancellation.md):
  Meeting at the same terminal value does not make two starts cancel in the weighted count error.
- [same-label coalescence and the curvature identity](G91-same-label-coalescence-and-the-curvature-identity.md):
  Matching inputs that merge with the same odd-count label replaces demand weights by their adjacent difference.
- [the coarse curvature bootstrap grows like log d](G92-the-coarse-curvature-bootstrap-grows-like-log-d.md): A
  coarse maximum-curvature bound still cannot close the constant count estimate by itself.
- [the absorbing-edge inequality, which fails from horizon 65](G94-the-absorbing-edge-inequality-which-fails-from-horizon.md):
  An induction proof for demand log-concavity must control the absorbing edge separately.

## The waiting room (not yet verified)

*From the head of this section in PROOFS.md:*

- **Each eventually white diagonal catches outward damage with probability exactly one half** (RULE30-PRIZE.md
  §8.66 addendum): measured exactly at three barriers over the band's phases; no proof. GPT's C071 caution applies.
- **The uniform core begins at the leftward light speed** (§8.68 second addendum): the triangle front is measured at
  $x/t = -0.24 \pm 0.02$, and the band's settled edge at $-0.254$ and $-0.252$ (the `edge` run), so the front is the
  band's inner edge; that this edge moves at exactly the leftward speed of information is §8.30's measurement, not
  a theorem.

*The pages:*

- [The actual barrier has isolated flat steps; a shape generalization to test](W95-the-actual-barrier-has-isolated-flat-steps-a.md):
  The actual barrier has no consecutive flat steps; unrestricted fair-bit barriers can fail log-concavity.
- [Fixed-cell change and moving-frame change are different observables](W96-fixed-cell-change-and-moving-frame-change-are.md):
  Changing a fixed cell and following a moving pattern measure different things.
