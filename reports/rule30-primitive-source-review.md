# GC2206 — What the new primitive-root source actually classifies

29 October 2026, GPT solo carrying-source review. Local and Cloud remain offline.

**Verdict:** the constructive inverses, finite-width tail alternatives and projective orbit
identities are useful and carry in their stated scope. They do not yet classify which primitive
windows survive, nor give a certificate for 97. The constant-tail mechanism is already in our
record; its formal implementation here should be credited and used, not rederived as new.

## Source and evidence

The complete 1,271-line, 62,228-byte Lean source of
[R30-20261029-a4691a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-a4691a)
was read, SHA256 `184f0b2478735fdcc5a27c8f0f4cd780cb02c6e09f2d34aaa1373072d98adbf3`.
The last complete index refresh was 22:47:13Z, current kit
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`, 21 open PRs.
The retained portal report says **Lean Verified**, 373 constants, ten headlines, standard axioms,
Lean 4.35.0, replay at 22:19:41Z against kit `19540bfb974ef743bf98818e768c1ee94f62eecf`.
This review did not rerun the compiler/checker or validate the notebook. Human verification is
not reported in that snapshot.

Read the actual current imports `Rule30ZeroBoundaryStripeFront`, `FrontLift`,
`StripeFourComplete`, and the underlying `zrow` definition. Also read PR45's description and all
four indexed conversation comments at exact head
`f481c02b3ebe80d66e2a7bf8214b8b720d087eb5`. After removing comments/whitespace and namespace
wrappers, every proof body from `orb_phase` through `not_cycle_iff_survivor_pullback` in that
head is identical to the corresponding fully read submission prefix. The public PR review-summary
endpoint returned an empty list at this review. Troy Lowry's linked front half-period result is
already carried in GC2127 and related record; this review does not claim to replay its linked
archive or rediscover its three-bit anchor.

Record searched: `bstep|NOR.wave|clone.ray|primitive.root`; period-three together with
preimage/inverse/backward; primitive counts and the fractions below. Search covered the record,
actual kit/equivalents/catalogues, portal sources and indexed open PRs. Relevant matches read:
[G121](../proofs/G121-finite-predecessor-descent-reduces-to-roots.md),
[G122](../proofs/G122-canonical-ancestors-gain-black-and-period-three-tails.md),
[G141](../proofs/G141-wall-predecessors-have-a-finite-tail-test-but.md),
GC691 in the GPT archive, and GC1849's failed repeated-template route in
[the task-4 review](wolfram-agents/GPT-CL609-TASK4-REVIEW.md).
These already have the zero/one/period-three inverse-tail mechanism, with different boundary
conditions. The source's exact front operators and finite-width thresholds must still be respected.
Primary-literature check: Jen's
[1987 preimage paper abstract](https://www.complex-systems.com/abstracts/v01_i06_a02/)
places spatial preimage recurrences/counts in established work; its abstract alone is not an
exact prior-art match for these front-boundary statements. No priority claim follows from these searches.

## The carrying equations and the boundary distinction

Here bit i is depth f+i in a window travelling inward with the stripe front. It is not time i,
the actual singleton's diagonal index, or an independently chosen root-background trace.
For phase p in {0,1}, the forward bit is

    y_i = x_i XOR (x_(i-1) OR x_(i-2))                    (i >= 2).

The low gates depend on p: bit 0 toggles in both phases; the bit-1 gate is 1 in phase 0 and
x_0 in phase 1. Thus the backward recursion is triangular and unique once the phase is fixed.
The submission's `bstep1 K W` first undoes phase 1; `bstep0` then undoes phase 0, giving
`B_shift`. Both cancellation directions are proved by bit induction. K recursive bit assignments
is an algorithmic statement; no Lean complexity theorem establishes linear machine time for the
arbitrary-precision Nat implementation.

Above a finite output's support the backward equation is OR. Its pair graph has a fixed 00
state and otherwise reaches 11. Above an all-one output it is NOR: 00,01,10 form a three-cycle
(depending on pair orientation), and 11 enters that cycle. This is exactly the G122/G141/GC691
tail mechanism. The front's fixed low gates make this particular inverse unique; G141's
white-wall predecessor has a free boundary neighbour and may have two choices. Those domains
cannot be silently identified.

For W < 2^k and K > k >= 5, write U=bstep1 K W and V=B_shift K W. The three disjoint classes are:

| Class | First inverse U | Second inverse V |
|---|---|---|
| Clone | U < 2^(k-2) | V < 2^(k-4), and F_shift V=W |
| I | U < 2^(k-2) | all ones on [k-2,K) |
| II | all ones on [k,K) | NOR recurrence on [k,K) |

The proof applies the known OR dichotomy twice, replacing the second OR by NOR when the
intermediate tail is black. `exists_F_shift_eq_iff` identifies the first class with a short
unmasked predecessor. `isPrimRoot_iff_avalanche` excludes that class. Its strict **k < K**
hypothesis matters: in the weaker trichotomy at K=k, all quantifiers over [k,K) are vacuous,
so the alternatives need not be disjoint. The clone equivalence requires k>=5, even though the
preceding trichotomy only requires k>=4. Some headings/abstract wording suppress these guards;
use the actual theorem types.

`backward_nor_period_three` proves the finite bit relation V_(i+3)=V_i and a nonzero triple,
given four consecutive black intermediate bits. The NOR recurrence further forces one black
per triple after entry. It is a spatial tail fact. Projective consistency can define the
infinite backward tail, but it is not a period-three temporal driver or a surviving finite seed.

## What remains in the survivor test

The imported `Cycle K S W p lam` combines a positive even return period with `sig(S+1)` at
every appropriate arrival phase. `sig fuel r x` asks whether depth 1 becomes white at an even
absolute time within fuel rows of zero-boundary evolution. `front_sound` requires **S+1<=K**
to transfer that finite-window witness to the physical row.

`not_cycle_iff_survivor_pullback` uses the universal finite return to express a failed Cycle
as an odd orbit arrival x with `sig(S+1,1,x)=false`. The inverse orbit only transports this
already quantified survivor. `prim_exception_iff_survivor_avalanche` then rewrites the conjunction
of that equivalence and the primitive-root equivalence. It is a correct characterization, but
still contains the horizon-dependent survivor predicate and an orbit existential. It gives no
bound on S, no exclusion of every primitive root, and no new shortcut for deciding all survivors.

The twelve named eight-bit examples are classified by explicit inverse inequalities; that
theorem does not say they exhaust all algebraic primitive roots, or prove their survival.
The word "exceptional" needs its original certificate/search horizon attached. See the count
below for a precise guard against conflating algebraic primitivity with rarity.

## Projection does not transfer the missing certificate

The source proves F_shift^2(13)=3553 and hence

    orb 7 4 (13,0) = (97,0),       orb 8 4 (13,0) = (225,0).

These are genuine low-bit projections, not equalities of the unmasked natural-number orbit.
At width 46 the same four steps give 3553, not 97. The existing `cycle13_complete` has K=46,
S=45. Truncating to width 7 discards the bits needed for a horizon-45 physical witness, since
46<=7 is false. Conversely, lifting 97 with zero high bits selects a different lift from 3553.
Thus the displayed width-7 identity cannot transport that certificate to 97. A separate
large-width connection or a certificate for 97 is needed. `rowTail_ray97_of_cycle97` explicitly
assumes the latter; the module does not supply it. The 165/245 equality is likewise specifically
at width 32 and gives Cycle equivalence there, not at all widths.

The `win3pow n` laws align backward templates by shifting n-2 places. Their specialization to
97 uses a shift of three; the two displayed width-46 equalities do not prove any uniqueness
among the family or a mortality equivalence. There are further shifts by multiples of three.

## Elementary cardinality guard — PROOF-SKETCH, not independently read

This is a counting corollary of the submitted injections and bounds, using the same image-count
principle as G121. It is not offered as a new inverse-tail theorem or a portal candidate.

For k>=5 and any K>k, among **all 2^k words W<2^k**, the three class sizes are exactly

    clone: 2^(k-4),       I: 3*2^(k-4),       II: 12*2^(k-4).

Proof. The phase-1 unmasked map injects the 2^(k-2) short words U into W<2^k, by its two-sided
inverse and the two-bit growth bound. These are exactly the W for which bstep1 K W is short.
The unmasked two-step map injects the 2^(k-4) short words V into W<2^k; these are exactly the
clone class. Subtract to obtain class I; the complement of the short-U image is class II.
Strict K>k makes the classes disjoint, so no vacuous-tail cases enter this subtraction.

F_shift preserves bit 0; each one-step map toggles it. The relevant short-word sets split evenly
by that bit. Consequently the same fractions 1/16,3/16,12/16 hold after restricting W to odd
words, for k>=5. For exact k-bit odd words the same follows for k>=6 by the exact two-bit
growth of each nonzero one-step input and four-bit growth of F_shift, then splitting the free
low bit. At k=5 that last low-bit freedom fails, so do not extend that restriction unguarded.

In particular, among the 64 exact eight-bit odd words, the predicted counts are 4 clones,
12 class-I roots and 48 class-II roots: 60 algebraic roots, not just the twelve displayed
examples. Among all 256 words the counts are 16,48,192. These are finite-domain cardinalities,
not densities along an orbit, estimates of survivor frequency or a statement about DQ024.

## One frozen finite control

Prediction: at k=8,K=12 the serial inverse agrees with independently inverted forward
permutations on all 4,096 inputs for each phase; a scalar-gate forward implementation agrees
with the packed map. The class counts equal the formulas above, the named examples have their
claimed classes, and the four-step orbit of 13 is 3553 before truncation, projecting to 97/225.
Counterfactual: any inverse/class/count disagreement rejects the implementation or counting
argument and retains its witness; no widening/retry. Unexpected guard: at K=k the type-II
quantifier is vacuous even for the known clone 223. No survival/horizon search is performed.

Source: `tests/probes/wolfram/primitive_root_scope_check.py`, SHA256
`417adbe10682f9d6be1ef980e56273e6b73ef48805924d721496bc6d939fc778`.
Searches and independent controls are above. This is one deliberately small indexing/scope
control, not a new root census programme. One Python process, one thread, nice10; no GPU or
other heavy job. Freeze before launch. Use run_capped.py, tree tracking/max3 processes,
120 aggregate child CPU seconds (single compute process), 300 wall seconds, 768MiB RSS,
16MiB/file,128MiB stage disk,4096MiB launch and3072MiB running free+inactive headroom,
64MiB swap-growth stop. Supervisor CPU is recorded separately. Measure load/headroom before
launch; pressure/monitor failure parks this test, not an automatic retry. Preserve actual
receipts and any unsampled quantities as unavailable. Outcome not yet claimed in this freeze.

## Direction after this review

Use the inverse operators as available tools. Do not reopen the old finite-root descent or
repeat the zero/one/period-three classification: the missing implication remains future
compatibility of the primitive class. Reopening requires a property involving `sig` or the
whole arrival orbit, not another tail graph or a low-width projection. The independent next
direction is the clocked visible-language intersection, beginning with the existing scope
correction and retained channel statements; no new numerical stage is authorized by that pointer.
