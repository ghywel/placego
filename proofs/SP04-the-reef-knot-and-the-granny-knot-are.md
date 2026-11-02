# The reef knot and the granny knot are different, and only the granny is chiral

*Proofs from the sparks. Derived from [PROOFS.md](../PROOFS.md), entry "SP04. The reef knot and the granny knot are
different, and only the granny is chiral (SPARKS.md SC17; 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved; a classical result of knot theory, restated by Cloud with.

## In plain words

Why a granny bow can't be tugged into a reef bow: they are different knots, and only one is its own mirror image.

**What it says.** Under every shoelace bow is either a reef knot or a granny knot. The two are different knots: no
amount of pulling, pushing or adjusting turns one into the other without untying. The reef is made of a left-handed
half-knot and a right-handed one, and is its own mirror image; the granny's two halves have the same hand, so it has
a separate mirror twin. The proof uses the Jones polynomial, a formula that any two equivalent knots share, and a
computer check worked it out directly from drawings of the knots.

**Why it matters.** It came out of two break-room entries, GPT's bow and Local's word heterochiral, which turn out to
describe the same thing. It is a classical result, written out here so that it can be checked on its own page.

**An everyday picture.** A bow whose loops lie along the shoe instead of across it is usually tied as a granny.
Tugging will not fix it; retying with the first half-knot crossed the other way will.

## The formal statement and proof

*Where:* SPARKS.md SC17; `tests/probes/sparks/sc17_reef_granny.py` (an exact computation from braid diagrams, with
controls). *Bears on:* nothing in the prize; GPT's break-room entry "the loop with a release handle" and Local's
"heterochiral, and the hands inside it". *Status:* proved; a classical result of knot theory, restated by Cloud with
a self-contained argument on the standard properties of the Jones polynomial and checked by direct computation;
awaiting a second reader of this write-up.

**Setting.** A shoelace bow is a reef knot or a granny knot whose second half-knot is tied with its ends folded back
as loops; pulling the loops through leaves the knot itself. Join the lace's two ends far from the knot, which changes
nothing that tugging and adjusting can do without passing an end through. The trefoil $T$ is the simplest true knot,
the closed form of an overhand knot, and $T^*$ is its mirror image. The reef knot is $T \# T^*$, a half-knot of one
hand followed by one of the other; the granny is $T \# T$, two of the same hand ($\#$ is the connected sum: cut each
knot open and join the ends).

**Theorem.** (1) The reef knot and the granny knot are different knots. (2) The reef knot is equivalent to its mirror
image; the granny knot is not.

*Proof.* Three standard facts about the Jones polynomial $V_K(t)$ are used (Jones, 1985; Kauffman's bracket gives an
elementary proof of the first, 1987): (a) $V_K$ is the same for equivalent knots; (b) $V_{K \# L} = V_K V_L$; (c) the
mirror image has $V_{K^*}(t) = V_K(t^{-1})$. With $V_T(t) = t + t^3 - t^4$ for the right-handed trefoil,

```math
V_{\text{granny}} = (t + t^3 - t^4)^2 = t^2 + 2t^4 - 2t^5 + t^6 - 2t^7 + t^8,
```

```math
V_{\text{reef}} = V_T(t)\,V_T(t^{-1}) = -t^{-3} + t^{-2} - t^{-1} + 3 - t + t^2 - t^3 .
```

The two polynomials differ (the reef's has constant term 3, the granny's none), so by (a) the knots are different,
which is (1). For (2): the mirror image of $T \# T^*$ is $T^* \# T$, the same knot, since a connected sum does not
depend on the order of its summands (one summand can be slid along the other); so the reef is its own mirror image.
The granny's mirror image $T^* \# T^*$ has polynomial $V_{\text{granny}}(t^{-1})$, whose exponents run from $-8$ to
$-2$ rather than from 2 to 8, so by (a) the granny is not its own mirror image. $\square$

*The computation (SC17).* An exact state sum of the Kauffman bracket over every way of splitting the crossings, taken
from braid diagrams (the granny as the closure of $\sigma_1^3 \sigma_2^3$, the reef of $\sigma_1^3 \sigma_2^{-3}$),
gives both polynomials directly, without using (b) or (c), and gives the granny's mirror image as
$V_{\text{granny}}(t^{-1})$. Its controls give 1 for the unknot, $t + t^3 - t^4$ for the positive trefoil and the
symmetric $t^2 - t + 1 - t^{-1} + t^{-2}$ for the figure-eight knot. A first version split each crossing the wrong
way round; the unknot control caught it, giving $A^{-6}$ instead of 1.

*What it means for a shoelace.* A bow tied as a granny cannot be made into a reef bow by tugging: the knot under the
loops is a different knot, and only untying, which passes an end through, changes it. The two also differ in
handedness, in Local's word. The reef joins a left-handed half-knot to a right-handed one and is its own mirror
image, heterochiral; the granny's halves share a hand, and it has a distinct mirror twin.

### L1072 — the degree law: Rule 30's t-step rule has algebraic degree 2t − 1 (Local, 28 October 2026)

**Status:** PROVED, second-read by GPT, GC2032. **Known, reproved here (L1077):** the kit's
`equivalents/Rule30Equivalents/AlgebraicDegree.lean` (2026-10-18) already proves it in Lean. Our own core-Lean proof is
complete as well (L1077).
[Carrying review and independent symbolic validation](../reports/rule30-degree-law-gpt-review.md). Every lemma was checked as an
exact identity by `tests/probes/wolfram/degree_law_check.py`, and the theorem is computed for t ≤ 12.
[Full statement and proof](../reports/rule30-degree-law.md).

For t ≥ 2 the t-step local rule f_t(y_(−t), …, y_t) has GF(2) degree exactly 2t − 1. For t ≥ 3 its unique top
monomial is y_(−t+2) ⋯ y_t; for t = 2 the top monomials are y_(−1) y_1 y_2 and y_0 y_1 y_2. The proof has three
steps:
1. ∂f_t/∂y_t is the indicator that the anti-diagonal x_k(t−1−k) stays white, by damage at light speed.
2. The anti-diagonal conditions are triangular in pivots y_(t−1−2k). This settles every candidate coefficient except
   the top one.
3. In the frame left of the anti-diagonal, an induction on two damage recursions gives the remaining parity.

Novelty remains unresolved: Mariot describes a broader research direction, and the already-recorded Deva
abstract claims degree growth but its full argument has not been compared. This is not a prize result.


### L1279 — Black lines of descent do not cross, and the left child's reach has an exact front rule

**PROVED (hand, Local L1279; independent GPT carrying read GC2352, 1 November 2026).** [Hand arguments](../reports/rule30-genealogy.md#6-hand-arguments-proof-sketch-gpts-read-requested).
(a) In the designated-parent tree (L for 100, C for 010 and 011, R for 001), adjacent lines cannot swap sides, because
that needs x_p(t−1) to be 0 and 1 at once. Families are therefore intervals.
(b) In the single-seed orbit, the black cells reachable from (−1, 1) through black parents are exactly the black
cells of [−t, B(t)]. The front B(t+1) = B+1 if x_(B+1)(t) = x_(B+2)(t) = 0, else the rightmost black cell of row t+1 at
or left of B.

Checked on every row to 20,000 (`tests/probes/genealogy_front.py`). The speed, about 0.046, is MEASURED only.

GPT read both carrying steps and their boundary conventions; [review and qualifications](../reports/rule30-genealogy.md#7-gpt-carrying-review-and-next-discriminating-step-gc2352). The new retreat-corridor consequence (a retreat of d forces ceil(d/2) advances) and GPT's all-choice non-crossing are carried by Local (L1280): **PROVED (GPT's proofs, Local's read)**, with no violation on the orbit to t = 20,000. Local's simpler form B(t+1) = max{i ≤ B(t)+1 : x_i(t+1) = 1} is a two-line PROOF-SKETCH, machine-checked to 20,000; GPT's read is requested.

### L1280 / GC2352 — Ancestry follower, recovery corridor and lift scope

**PROVED, two-party:** GC2352's all-choice non-crossing, retreat recovery and alternate-lift
counter-control were carried by Local L1280. L1280's follower formula and non-multilinear
lift counterexample are carried by GPT GC2353. [Exact arguments and scopes](../reports/rule30-genealogy.md#8-locals-read-of-gc2352-l1280).
These are structural identities, not a speed or centre-density theorem.

### GC2353 — Gap-episode stopping time and transported trailing bit

**PROVED (GPT's proofs; Local's carrying read L1281, with an actual-orbit check to t = 20,000).** [Carrying argument](../reports/rule30-genealogy.md#exact-stopping-time-and-the-trailing-bit); [Local's read](../reports/rule30-genealogy.md#10-locals-read-of-gc2353-l1281): a finite white gap M gives exactly floor(M/2) advances, the trailing bit toggles, and its collision value decides stay versus retreat. A nonadvance retreats by the left black-run length minus one. Uses the known C3 shrink theorem;4097 fixed scalar episodes checked. Explicit finite-row pair refutes lengths-only predictive closure. No single-seed drift theorem.


### GC2354 — Fresh initial bits at ancestry collisions

**PROVED (GPT's proof; Local's carrying read L1282, with an independent exhaustive check on three right halves).** [Full model and proof](../reports/rule30-genealogy.md#11-fresh-initial-bits-at-successive-collisions-gc2354); [Local's read](../reports/rule30-genealogy.md#13-locals-read-of-gc2354-l1282). Fix the right half with a black front and a farther rightmost black cell; take independent fair bits on the left. At episode starts expose precisely the initial suffix beginning c=B-time. A collision black run L reveals exactly L new initial bits and the next episode starts at c-L. Thus every finite L-list fixes one prefix and has probability2^(-sum L); the L values are independent geometric(mean2), conditional on completed history/current gap before the trailing bit is inspected. The fixed single seed is outside this random-input hypothesis. Finite cylinder controls pass; no drift or novelty claim.


### L1283 / GC2356 — Deep-side clock and finite-word periodicity obstruction

**PROVED, Local's hand argument carried by GPT GC2356.**
[Precise carrying read](../reports/rule30-genealogy.md#161-carrying-verdict-on-locals-two-hand-steps).
For infinitely many finite ancestry episodes, the deep word obeys
L=1+lead1(Phi^r(w)), w_next=shift^L(Phi^(r+1)(w)). An eventually periodic pair history
on a configuration with a leftmost black cell has sum L=2 sum(r+1) per cycle. Its distance from
the left edge is bounded and periodic, not necessarily constant within a cycle. Consequently
unbounded limsup distance implies nonperiodicity of that pair history. The latter unboundedness
is not proved. Prescribed deep-side histories need not satisfy the actual shallow-gap conditions.

### GC2357 / L1284 — Uniform ancestry capture and band escape; the seed's collision history is not eventually periodic

**PROVED (two-party: GPT's proof GC2357, Local's carrying read L1284).**
[Proof](../reports/rule30-genealogy.md#17-a-uniform-capture-argument-replaces-the-clock-induction-gc2357);
[read](../reports/rule30-genealogy.md#18-locals-carrying-read-of-gc2357-and-gc2356-received-l1284).
For any row with a leftmost black cell, marks propagated along every black-parent edge from that cell capture
diagonal j (left-edge coordinates) from time 1 + j(j−1)/2, and the marked front leaves band 0..D within (D+2)(D+3)/2
updates from any start. With the entry above and `JenPow2.infinitely_many_black`: on the single seed the ancestry
front's distance from the left edge tends to infinity, and its (r, L) collision history is not eventually periodic.
Not a centre-column or speed statement. Replay: `tests/probes/genealogy_capture.py` (GPT) and
`tests/probes/genealogy_capture_seed.py` (Local, on the seed).
**Lean (L1287):** capture and exit are machine-checked in `tests/probes/lean/Capture.lean` (Mathlib, Lean 4.33.1,
standard axioms, no `sorry`) for every rule with f(000) = 0, f(001) = 1, f(100) = 1, instantiated at Rule 30
(`Capture.capture`, `Capture.exit`, `Capture.unbounded`, `Capture.capture30`, `Capture.exit30`;
[statement](../reports/rule30-genealogy.md#21-capture-and-exit-in-lean-l1287-at-the-owners-direction)). The lock
and the nonperiodicity conclusion remain hand, two-party.
