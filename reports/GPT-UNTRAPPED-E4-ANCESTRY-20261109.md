# The untrapped E A⁴ E history: initial ancestry and a shorter launch obligation

GPT GC2776, 9 November 2026. The owner requests a sustained block of at least
30 minutes, continuing automatically from its results, and one unexpected or
random experiment with predictions. GPT owns this block. Both schedules remain
paused. No colleague computation or pending merge is duplicated.

## The exact question

Use the driven right half with center black at even ticks. Let A=25 and
E=33535555 be sampled column-1 gap words at odd ticks. The full E A⁴ E head
condition runs from1 through193; its second E launches at125. The previous
[trap audit](GPT-E4-AND-TRANSIENT-REVIEW-20261109.md#outcome--gc2775) says any
such history avoids the known829-state trap through125, conditional on that
finite audit and its physical transfer (pending the independent carrying read).
Adding this entailed guard to the unchanged full query would not resolve its
previous UNKNOWN. Cloud's existing free-row passage survives through width62;
restricting those paths also gives free-prefix nonexclusion there.

This block instead separates **the initial image condition** from the later
shared history. A free tick-1 row is not automatically the image of a tick-0
row with black center. The known Rule30 predecessor transfer gives a constant
state description of precisely that condition. The test below asks whether
E's own beginning makes it automatic. No answer is assumed.

## Eight states retain the first ancestor

Write y for the tick-1 row, with y1=1. A tick-0 predecessor x has x0=1 and
therefore x1=x2=0. After reading y1..yi, retain the set S_i of possible pairs
(x_i,x_(i+1)). A new output bit b gives the subset update

    S_(i+1) = { (q,r) : (p,q) in S_i, r in {0,1}, p XOR (q OR r)=b }.

Starting with a={00}, exactly the following eight subsets are reachable:

| State | Pairs | Input0 | Input1 |
|---|---|---|---|
| a | 00 | a | b |
| b | 01 | empty | c |
| c | 10,11 | d | a |
| d | 01,10,11 | d | e |
| e | 00,10,11 | U | f |
| f | 00,01 | a | d |
| U | all four | U | U |
| empty | none | empty | empty |

**PROOF-SKETCH, same-worker self-check only:** induction on the read prefix
shows that this is exactly the set of possible terminal predecessor pairs.
Thus S_W nonempty is equivalent to a finite predecessor of width at most W+1
for the observed W-cell prefix. Pad the chosen predecessor with zeroes, not the
observed output, to obtain that finite completion.

The stronger state S_W=U means that **every finite higher output completion**
has a black-center predecessor: invert that higher tail from its white end,
then splice its required terminal pair into the prefix reconstruction. Conversely,
each missing pair is realized by a finite predecessor tail, whose output tail
therefore supplies a completion incompatible with the prefix. For one specified
whole output with white cells above W, the condition is instead **00 in S_W**.
These three quantifiers must not be interchanged.

Replacing the initial tick-0 strip of the193-tick cone by this automaton on
its193 tick-1 cells, accepting any nonempty final state, preserves the entire
existential tick-0 ancestry condition. It need not make a solver faster. This
is a specialization of the kit's known `Rule30Predecessors.T`, `back`,
`lin_back`, `eq_back`; no new inverse theorem or novelty claim.

The first gap3 alone does not settle the issue. Hand substitution gives
initial cells1..5=111de with d OR e=1. Some such rows have no prefix predecessor;
some synchronize to U; others retain a proper nonempty set. The fixed controls
will independently replay this claim, and the proposed free33/nonimage root639.

## Frozen test and predictions

Three fixed native SAT questions use exact white-center tick-1 cones, all
sampled heads, and the above deterministic automaton:

1. Opening3353,29 root cells, final state proper and nonempty. Prediction:
   UNSAT (weak). This would mean that the opening has already decided prefix
   ancestry: either impossible or independent of all higher completion.
2. Complete E,69 root cells, final state empty. Prediction: SAT (weak). A
   witness would show that even a full free E cannot simply be admitted as
   having tick-0 ancestry.
3. Complete E,69 root cells, final state proper and nonempty. Prediction:
   UNSAT (weak). A witness would instead expose dependence on the later tail.

UNKNOWN remains UNKNOWN. No horizon, conflict or seed expansion follows it.
Every SAT model is checked against all original case clauses and independent
integer/scalar evolution; its possible predecessor roots are reconstructed.
Every UNSAT claim needs native drat-trim and cake_lpr checks in a separately
frozen certificate-only follow-up. The first stage has a nontrivial native
UNSAT control; a false empty proof is reserved for the checker stage.

Controls also compare all1,023 odd output prefixes of widths1..10 with direct
forward predecessor enumeration, both the prefix and whole-white-tail criteria,
and the automaton's sixteen transitions with the local rule. The exact count
will be reported from execution, not assumed if it differs. A known actual E
from seed2135555 at91..159, shifted by90, must enter U by its69-cell root cut.

### The owner's chaos experiment: one original-root tail replacement

Take the actual tick90 row of seed2135555 as a new tick0 root. Its E occurs at
new ticks1..69. Freeze cells1..70, then replace cells71..194 with one124-bit
pseudorandom word, using the fixed seed `GC2776-chaos-one-root-tail`.
This is one draw, with no search for a favorable outcome. It preserves the
complete first E by causality and keeps full ancestry by changing the original
root, rather than transplanting an intermediate row.

**Prediction:** at least one sampled head changes by125 (tentative). The
counterfactual—agreement through125—would exhibit stronger actual shielding
than the maximal-speed cone alone. Also retain the first difference, the full
E A⁴ E mismatch lists and both trajectories through193. An accidental target
witness is checked, but is not the prediction or the admission criterion.

**Record searched:** GC2709/CL753 exact diagonal ancestry, GC2714/L1579 image
black-row guards (which require an earlier odd sample and do not automatically
apply to initial tick1), GC2753's anchored193 UNKNOWN, GC2773/2775 generated
state and trap guard; fresh `record_find` predecessor/E4/untrapped and separate
Rule30Predecessors searches. Current actual kit source at
6d2c05796ace0993c6d409f5704369afba912847, index complete11:54:04Z, includes
Predecessors transfer/reconstruction and the known preimage tools. Its cyclic
predecessor-count theorem has a different boundary condition. Earlier primary
Rule30 inversion literature remains background; no novelty/submission decision.

## Resources and source freeze

One serial stage, at most65 aggregate CPU seconds including outer monitoring;
outer75CPU/240wall. Prepare8CPU/25wall; native control3CPU/10wall; each of three
native cases12CPU/30wall and5000 conflicts; audit6CPU/20wall. One thread/nice10,
RSS8192MiB, swap-growth4096MiB, launch headroom4096MiB, running floor1024MiB,
max6 processes,16MiB/file,128MiB/stage. Pressure, thermal, monitoring, control or
hash failure stops the stage. No GPU or larger search.

Source `image_ancestry_audit.py` SHA256
`ab907144ae4072b24991baeb6b07b0f55b6b127dd3af5d1bf8bb82bd7e20516e`;
plan `c2fb7a9b62bd6bb45d7ff006b95b9d1972fcd562e24e2c018f2858819cb12808`.
The plan pins all copied dependencies and the native solver. Data remain
outside git; the source and this plan are committed before launch.

Next independent alternative, already derived but not launched: an anchored
E A⁴ 3353 prefix through153 with154 root cells. This is a shorter physical
obligation than the old193 UNKNOWN, retaining the first E, four A blocks and
the untrapped second launch. Its source109=4520 follows from the already
certified five-head support83,87,101,115,129 inside this prefix. A new run needs
its own freeze; a surviving candidate must then keep all earlier ancestry.

My own pull: locate where the first E's generated history permits or obstructs
the second launch, then follow a real candidate's first failed completion head.
