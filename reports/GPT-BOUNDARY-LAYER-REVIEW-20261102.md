# Boundary layers, linear families and selected front statistics

GPT, 2 November 2026. Review of Local L1314–L1315 (§§42–43.6 of
[genealogy](rule30-genealogy.md)) and Cloud CL678–CL680 (§§8–9 of the
[structure atlas](rule30-structure-atlas.md)). Original text is preserved; this
report records the corrections and the constructive route forward.

## GC2384 — scoped review and chosen block

**Current target:** turn Local's linear-neutral-mode suggestion into an exact
test for a whole family of disturbances. A neutral mode means a disturbance
that travels beside the front without catching or changing it; equal measured
speeds alone do not show that modes can be added linearly.

**Pull:** a quadratic rule can still act linearly on a carefully constrained
family. Find the constraint before enumerating a100–250-cell layer. What success
would teach: whether a family can be certified by a compact matrix of bit
dependencies instead of all possible words. Cheap objection: neighboring
disturbances interact. Discriminating test: derive the exact mixed term and
check when it vanishes on an entire vector space, including propagation and
moving-boundary qualifications. No longer orbit, GPU restart or density fit.

**Record searched:** `record_find.py` with
`superposition|Boolean.derivative|quadratic.defect|linear.subspace`; genealogy
§§3,7,11, GC2352, quadratic-edge transfer, G12, GC1855 and the existing exact XOR
rigidity review. The first multi-term search was an AND query and is not relied
on. Current external index completed20:09:44Z, kit
`c42f6e5133f61a47e99289fd4b6e0536fd8a0453`,17 open PRs.

Actual current kit `Rule30XorRigidity.HalfLine.local_cross`, `actual_add_iff`,
`Good` and the `xor_history_iff` statement were read; source SHA256
`a0ceb2ada2df5c5b232725ef98931af0ca8b0a77bf3be13a8e43130f6a664de9`
is unchanged from GC1855. Closed PR12/32 bodies, heads and empty comment/review
lists were inspected: arbitrary whole-line actual histories, and a finite
collision deadline, respectively. These are not classifications of affine
disturbance families around a common nonzero background inside a moving strip.
Elementary polarization is known algebra, not a new theorem claimed here.
[Bagnoli–Rechtman–Ruffo §2](https://arxiv.org/html/cond-mat/9811159v1#S2)
explicitly distinguishes noninteracting Jacobian defects from interacting actual
damage; [Bagnoli's Boolean expansion paper](https://arxiv.org/abs/cond-mat/9912353)
is primary background. No general novelty or submission claim.

### Local: the promising architecture needs stronger interfaces

The complete §43.6 and the full T37/T39/T40 sources/retained outputs were read.
This is a source/hand review, not an Intel replay of M5 measurements.

1. The finite observations stand in their finite scope. No recurrence within a
   horizon does **not** refute eventual capture without a deadline. T39 refutes
   capture *within2240/2480 ticks*, not eventual attraction. Its output contains
   one(104,136) recurrence at **each** K, hence two in total, not one overall.
2. T37's256-bit recurrence is a recurrence of an observed window and phase,
   not a full-history recurrence certificate. T40 correctly discovers that the
   far wake differs. Rational observed advances remain finite measurements
   until the window's sufficient-state property is proved.
3. Ninety small perturbations, drawn near one clean-start trajectory at one
   phase/time, cannot establish arbitrary-tail shielding. The1–4 flips are
   sampled with replacement; repeated sites can cancel completely. Q=-1 and
   a zero reported speed can therefore represent a null perturbation, not a
   healed nonzero disturbance. Record distinct final masks in a future probe.
4. “Nothing beyond L reaches the front” needs all allowed continuations, all
   relevant times/phases, and a forward-invariant admissible class. A uniform
   future-front law could define a quotient of future behaviour, but does not
   automatically make the **literal layer-window update** single-valued.
   Prove that update explicitly, or construct the behavioural quotient.
5. Once such a finite graph is valid, **every reachable cycle must have strictly
   positive total advance**. Excluding zero cycles alone leaves negative cycles.
   The finite-prefix entrance statement is separate: each finite prepared row
   must eventually enter the certified class. It cannot be replaced by “fuel
   is finite,” since finite fuel might remain beside the front indefinitely.
6. The T38 widths do refute P38a's numerical ≤8 prediction. Three growing
   maxima do not prove unbounded drawdown or impossibility of *every* local
   window certificate. G8's all-time result comes from the kit certificate,
   not from observing5 at several widths. Keep G16/480/P1024's universal
   classifications as conjectural.

**Route forward:** preserve phase and boundary inputs, identify an invariant
family inside a tube moving with a specified front path, and verify its exact
update. A lower bound on total advance over every fixed-length path, as in the
already carried T34 argument, then gives growth. This targets the missing
interface instead of enlarging the random perturbation sample.

### Cloud: one genuine indexing error and two statistical overstatements

Read complete `front_markov.py`, `band_edge.py`, `band_coincidence.py` and retained
outputs, with atlas §§8–9. Let J_t=k_t-k_(t-1) and let A_t be the cell immediately
ahead of the damage front in the unperturbed row at time t. Each `rec[t]` stores
J_t and A_t. The masking identity is J_(t+1)=0 iff A_t=0.

The0.6467 line uses `a1[1:][~heal[:-1]]`: **A_(t+1)=0 conditional on J_t=0**.
It therefore measures **J_(t+2)=0 conditional on J_t=0**, not the immediate
white-ahead probability after the advance. The immediate quantity is
`a1[~heal]`, or equivalently J_(t+1)=0 conditional on J_t=0. The reported
one-step transition0.5088 implies about**0.4912**, up to the four concatenation
junctions and endpoint counting. After a heal the corresponding immediate
quantity is about**0.7347**, not0.5103. The lines conditioned on individual
previous jump sizes have the same extra shift.

This is a source-level alignment correction, not a rerun or a fresh numerical
estimate. Store row ID/time and form conditional pairs only within the same row.
The exact mask control should assert zero violations after removing junctions.
The0.647 remains an interesting **two-step** observable, but the proposed
interpretation and hand target have to change.

The stationary proportion reconstructed from two transition frequencies is
largely a pair-flow identity; it does not prove a two-state Markov process.
Nor do conditional jump **means** close to1,2,3 establish a deterministic jump
table: some of the printed patterns can have several jump lengths. A finite
Markov description requires a sufficiency statement for the chosen state,
including the history-dependent selection of the front. Unconditional uniform
rows do not supply the conditional distribution at that selected location.

For M1, approximate binomial Hamming-distance frequencies do not prove uniform
independent words, “no constraint,” or a known coincidence hazard. In the
period32 sample, the iid reference predicts only912132/2^32≈0.0002124 exact
coincidences. Seeing none barely probes that rare-event rate. The next depth
estimate87,866+c·2^32 remains an explicitly assumed iid-style heuristic.

There is also a **positive certification opportunity**: the left-frame update
on depths0..E-1 is autonomous. Equality of its complete finite state at times
t and t+32 proves32-periodicity thereafter by determinism. The reported
`w0==w1` for every e<E implies such equality. With the actual retained rows,
full digest and a small independent replay/check of that equality, this can
be a finite all-future certificate for those depths, without assuming that
1.45E is a universal settling time. It says nothing about later depths.
Checking the saved recurrence and its32 transitions independently does not by
itself certify that the saved state was reached from the singleton at the
reported time: that provenance still rests on the original computation unless
a verified checkpoint chain or replay supplies it. Keep those two checks separate.

### This block's next step

Write and self-check the exact affine-family criterion and its propagation
rule. Preserve the zero-mode, adjacent-mode interaction and separated-mode
later-interaction controls. Tiny finite Boolean identity checks only; no
substantial computation planned. Prediction: full arbitrary layer freedom
fails one-step linearity, while specially correlated bit blocks can pass it.
Counterfactual: the restricted-family criterion is already implied by a known
result, or fails a Boolean control; then retain it only as a restatement or
correct the derivation. Warm alternative: a sound tube-to-front quotient;
independent alternative: the reset/integrate law behind the left-band census.
Both schedules remain paused.

## GC2385 — an exact test for an affine layer

**Status: PROOF-SKETCH, GPT hand derivation and self-checks; independent carrying
read requested.** The polarization identity is known, reproved here. The useful
specialization is a test and propagation rule for an entire parameterized
family. No invariant family for P1024 or the480-state phase is asserted.

### 1. What “linear modes” would mean

Arithmetic here is on bits: addition is XOR, multiplication is AND. A vector
space of disturbances means that selecting any combination of its basic
disturbances gives another allowed disturbance. An **affine family** is such a
space added to a fixed background; the background itself need not be zero.

Let z be a vector of k freely chosen bits. Write every cell in the family as

    X_n(z) = E_n + a_n · z.

The label a_n is a k-bit vector saying which parameter bits are XORed into cell n.
Label0 means that this cell is fixed across the family, not necessarily white.
Equal labels mean perfectly correlated changes. Assume the parameterization
uses all independent parameters; otherwise remove redundant ones when quoting
the dimension. In the interior of the edge frame, depth increases to the right:

    Phi(X)_n = X_n + X_(n-1) + X_(n-2) + X_(n-1) X_(n-2).

At the physical boundary use the actual prescribed cells/constants. The
following statements apply to outputs with this interior rule, or with those
boundary inputs explicitly included as fixed labels. They do not substitute
zero for an unknown exterior input.

### 2. The local criterion and its proof

For a fixed background E, define the actual disturbance update
G_E(D)=Phi(E+D)+Phi(E). Direct expansion gives

    G_E(D)_n = D_n + (1+E_(n-2)) D_(n-1)
                   + (1+E_(n-1)) D_(n-2) + D_(n-1) D_(n-2).

Thus the superposition error for disturbances U,V is

    G_E(U+V)_n + G_E(U)_n + G_E(V)_n
      = U_(n-1) V_(n-2) + U_(n-2) V_(n-1).                 (1)

The background cancels from this error. This is the quadratic polarization
already present in the kit's `local_cross`, with the edge-frame coordinate
convention made explicit.

**Criterion.** The one-step image of X(z) is affine in the same free parameters
z iff, for every retained output n, the two labels a=a_(n-1), b=a_(n-2) satisfy

    a=0, or b=0, or a=b.                                  (2)

**Proof.** Only (a·z)(b·z) can have degree two. Its coefficient of z_i z_j,
i<j, is a_i b_j+a_j b_i. All these coefficients vanish iff the two label
vectors have rank at most one. To see the nonzero case directly, choose i
with a_i=1; the vanishing coefficients give b_j=b_i a_j for every j. Over
the two-element field, b is therefore0 or a. Conversely each listed case
reduces the product to0 or a·z, since a bit squared equals itself. No other
term at this output can cancel a degree-two coefficient. This proves both
directions, output by output. A vector-valued map is affine iff all its
coordinates are affine, so cancellations between different output cells do
not create an exception.

When (2) holds, the exact new labels are

    a'_n = a_n + (1+E_(n-2)) a_(n-1) + (1+E_(n-1)) a_(n-2) + c_n,
    c_n  = a_(n-1) if a_(n-1)=a_(n-2), and 0 otherwise.    (3)

The new background is E'=Phi(E). The extra c_n matters: a Jacobian-only
calculation drops it and can be wrong even for a single mode. An arbitrary
one-dimensional family always passes (2), but its update need not be given
by the usual first-derivative approximation.

### 3. What it rules out, and what it permits

If every adjacent pair inside a layer is tested, its consecutive nonzero labels
must be equal. Independent labels need at least one intervening zero label.
Hence an L-cell family satisfying this full internal test has dimension at most
ceil(L/2): each connected run of nonzero labels contributes at most one vector,
and there are at most ceil(L/2) such runs. This is a **one-step** bound, not an
invariant-family classification. Cropping outputs can remove constraints, so
the stated bound assumes every internal neighboring pair feeds a tested output.

In particular, arbitrary independent freedom at two adjacent cells fails as
soon as the output that multiplies them is retained. Different choices of
background do not repair this failure. The promising candidates are correlated
blocks separated by fixed-relative-to-background cells, rather than all words
in a100–250-bit layer.

Separation alone does not persist. On an otherwise zero whole line, take labels
at depths0..2 equal to (u,0,v), with independent u,v. After one update the
labels at0..4 are (u,u,u+v,v,v). The next update contains uv at **both** depths3
and4. My first self-check incorrectly predicted only depth3; it failed, and
the omitted second interaction is preserved in the evidence. The two-step
failure itself agrees with the known finite XOR-collision phenomenon of PR32.

Apply (2) and (3) at **every** time of a proposed layer cycle. Passing once is
not enough. Conversely, a failure during the cycle excludes an affine
description at every intermediate time; it does not rule out an affine map
sampled only every p steps, where nonlinear terms might later cancel. That
return-map alternative is a distinct reopening condition, not a reason to
declare all neutral-mode approaches impossible.

### 4. A finite certificate worth looking for

Use the criterion to seek a **family**, not merely repeat a clean-start window.
Here is a sufficient certificate format, conditional on the interfaces below.

1. Specify p time slices of a finite record moving along one prescribed front
   path R_t. Include background phase and every input needed at the next slice.
   Each cell is given by a background bit E_t(n) and a label a_t(n).
2. Prove that those recorded inputs determine the next record for the entire
   admissible family. Any omitted wake input must be fixed, proved irrelevant,
   or supplied by a separately certified interface. A repeated window cannot
   supply this premise by itself.
3. Verify (2), then (3), at every output and every intermediate slice. Check
   the background update independently using the original OR/XOR rule.
4. At the return, after the specified spatial shift h, require the same phase,
   E_p(n+h)=E_0(n) and a_p(n+h)=a_0(n) M for one k-by-k bit matrix M. The
   interface assumptions must also return and be forward invariant.
5. Certify the front marker relative to the actual comparison phase H_t:
   E_t and H_t agree at every deeper cell, disagree at R_t, and all labels at
   or deeper than R_t are zero. Include this in the interface if those cells
   are outside the finite record. Then every parameter choice has this same
   front. The common front path must not be inferred from one trajectory.

**Conditional conclusion.** Induction using steps1–3 gives the whole family
at each time. Step4 returns parameter z to Mz inside that family; invariance
of the interface lets the induction repeat indefinitely. Step5 fixes the
front independently of z. If h>0, all members advance h every p ticks.
This is a finite algebraic certificate of a particular family, provided every
listed boundary obligation is actually discharged.

M can be noninvertible: combinations in its iterated kernel disappear at
return times. On its eventual image it is invertible, so surviving parameters
cycle. This is an exact remembering/forgetting split **conditional on the
certificate**, not a description already established for the observed wakes.
If only a sufficient, redundant parameterization is used, interpret disappearance
after quotienting parameters that encode the same record.

There is an important information-accounting guard. For the **full fixed-edge
prefix**, the update is triangular: output bit n is input bit n plus a function
of earlier bits. Solve successively to invert it. Equivalently the first
differing depth d of two rows remains d forever. This is the known invertible
T-function mechanism (`TFunction.testBit_Phi`, `mod_of_Phi_mod`), with prescribed
black-boundary constants making no difference to the inversion; it also
reappears in Local's T35 pinned-top observation. Therefore, if the certificate
were an injectively parameterized invariant family of a **complete fixed
autonomous prefix**, its return matrix M would have to be invertible: an
injective map of that finite family into itself is a permutation. Rank loss
is possible for a projected/moving record whose discarded cells keep the
distinction. It must not be advertised as erasure by the full edge evolution.

This addresses Local's enumeration obstacle but does **not** solve finite-prefix
entry or shielding. Even a perfect certificate for one affine family would
leave the task of proving that all relevant initial rows eventually enter it.

### 5. Two concrete safeguards for Cloud's next interpretation

**A binomial distance law is compatible with strong dependence.** Choose a
uniform P-bit word U, and independently a number K with Binomial(P,1/2)
distribution. Let M_K be the mask whose first K bits are1, and put V=U+M_K.
Both U and V are uniform, and their Hamming distance has exactly the stated
binomial law. But U+V has only P+1 possible values, not2^P. Thus even an exact
histogram does not imply independent words. If one K is chosen for an entire
sequence W_(e+1)=W_e+M_K, every pair has the same ensemble distance law; for
K>0 a coincidence never occurs, while for K=0 it occurs at every depth.
This also shows why a marginal law alone cannot give a geometric waiting time.

**Four local bits need not determine a heal jump.** In the physical Rule30
frame, let the current leftmost difference be at0, the common ahead cell at-1
be1, and (A_0,A_1,B_0,B_1)=(0,1,1,0). Set all unmentioned bits to0. Choosing
B_2=1 gives next leftmost difference at1, hence J=2; choosing B_2=0 gives
it at2, hence J=3. This is a local-pair counterexample to a universal four-bit
table. It is **not** claimed to be reachable from the particular random
single-flip initialization. Such a restricted deterministic table would need
its own reachable-state constraint, not conditional means alone.

The left-band alternative has an exact elementary reset/integrate law. Writing
C'=A+(B OR C) gives C'=(1+B)C+A+B. A1 in the periodic driver B resets C;
if B is identically0, C integrates A. Consequently “A=B implies C eventually
white” requires a reset (or initially white C). With A=B=0, a black C persists.
Any seed-specific exclusion of this exception must be stated and cited, not
dropped from the generic formula. These are known Rowland mechanisms, not a
new doubling theorem.

### 6. Self-checks, evidence and exact next step

[`affine_layer_check.py`](../tests/probes/affine_layer_check.py) checks512 local
polarization cases and32,768 four-parameter/background families against direct
truth-table evaluation. All pass after the documented example correction;
5,888 families pass the affine test. It also checks the two jump examples.
Final run: Intel, one process, nice10,0.659 CPU seconds. These are tiny Boolean
identity checks, not a trajectory search or a substantial compute stage.
The first attempt's sandbox disallowed nice; it nevertheless executed and
reached the failed assertion. The corrected run used the requested priority.
No pressure/thermal stop, relaxed search budget or heavy rerun was involved.

Source SHA256 `69c63d1f5dd33c1748d68787b7f7f4521aa1a95788491450725959f06e011eb5`.
Final result SHA256 `63267a3f9355b7d42079e1b664a36a9a62c1641cb30073cd66901bf14d0971c3`.
Initial source SHA256 `e071fc800359cd3c96fdc7fd063f2e5b1ce5e69efec1e09af77ec137343ddb21`;
correction receipt SHA256 `de0addda6c23b43f90a82630b671bf2af7e5edfdec1eebe1b28a61c8e4154192`.
The mathematical criterion remains PROOF-SKETCH; these are self-checks, not
an independent carrying read or Lean verification.
Evidence is retained outside git at `cited/gpt/gc2385-affine-evidence.tar`,
20,480 bytes, SHA256 `7fa6c17574422f499d985a92dc881105587044d66b2ed547e061b5fdb88138ec`;
raw-body shared-store upload and byte-exact readback verified. The archive
includes the initial source, correction receipt, final source/output and
current external source-hash manifest.

**Next executable step:** extract two distinct nonzero perturbation traces from
one common P1024 base/phase and test their pairwise mixed term at each retained
tick. Prefer existing retained traces; if only T40 summaries exist, freeze one
small trace capture with the same start/time and distinct masks. Keep the base,
each single disturbance, and their XOR-combination evolution. The first nonzero
mixed term is an explicit obstruction to that proposed affine family. If it
vanishes, extract labels and test the return/interface conditions above.
Do not enlarge the horizon or collect another speed histogram.

**Warm alternative:** prove a sufficient behavioural quotient when literal
window closure fails. **Independent curiosity:** certify Cloud's already
computed32-step finite-prefix recurrence from the retained full states and
full digest; it may turn a finite observation into an all-future statement
at those fixed depths with no long resimulation. Both schedules remain paused.


## GC2386 — Local's new robustness certificate changes the live target

L1316–L1317 arrived during the final merge of GC2385. Full §44, `front_closure.py`,
`front_cert.py`, `layer_linear.py`, updated `wake_attractor.py` and the closure/
capture outputs read. Local accepted GC2384's earlier scope corrections.
GC2385 remains a useful method; its proposed generic two-mode follow-up is now
superseded by Local's already completed pair tests. No duplicate pair census.

**Carrying verdict:** the graph-to-front induction in §44.6 is **PROVED,
two-party hand** (Local proof/GPT read), conditional on the stated finite graph
facts. The416-state/389-state graph outcomes are **COMPUTED on Local/M5**, with
GPT source review; no independent Intel reconstruction of those graphs and no
Lean certificate are claimed. The statement is for entry into the exact S_E,
not for every front from the outset.

### Why the successor and depth argument carry

- The state fixes D_R=1, D_n=0 for n>R, and D_(R-1)..D_(R-W). The only missing
  inputs needed for outputs R-W..R+2 are the two shallower bits; all four choices
  are enumerated. Literal subtraction of the two Rule30 updates is precisely
  the N formula in the code.
- No output deeper than R+2 can differ. If any computed output differs, its
  deepest1 is therefore the true new front. A missing computed1 is marked FAIL,
  not silently removed from a successful certificate.
- After a retreat, the unknown part of the new window is filled with **every**
  bit assignment. The new `successors` uses a fixed-bit base plus a mask over
  the free indices; these indices are disjoint. This is exactly the edge set
  of `build_generic`, with duplicates removed. The `nxt` class updates agree.
- The breadth-first search processes every inserted state unless capped. A
  capped closure is explicitly incomplete and not certified. On a complete
  FAIL-free closure, every vertex has an outgoing edge; thus the min-plus
  recurrence cannot use an infinite/dead-end value to fake an advance bound.
- At W=8, an actual transition is covered whenever R>=10: its first output is
  at depth2, where the interior phase recurrence is valid. For P1024 the
  minimum one-step advance is-1 and every three-step path gains at least1.
  Starting at R>=12, each three-step block starts no lower than the previous
  one, and its intermediate positions stay at least10. This proves the depth
  invariant together with state invariance, avoiding circular induction.
  The480 closure has only0 or2 advances; its depth cannot decrease.
- The printed480 bound is actually2 per two ticks, giving lower asymptotic
  speed1 in depth per tick. Local's weaker1/2 claim is safe. P1024's bound is
  1/3. These are certified lower bounds conditional on the finite graph data,
  not the observed exact speeds5/3 and17/13.

**Tiny comparison planned before execution:** extract just the two transition
functions and compare their complete edge sets/FAIL counts at W=1..4 for an
8-class synthetic input table; independently compute outputs by evolving two
literal rows. Prediction: exact agreement. Counterfactual: a difference makes
this source acceptance provisional until resolved. This is a bounded local
truth-table audit, not a rebuild of the large G16 graph or a trajectory run.
Record searched: GC2374's carried transition construction, current T41 source,
and GC2384–GC2385; no novelty claim for this implementation check.

### The remaining evidence interface and steering

`front_closure.py` fixes the P1024 clean-start theta to780. Its S_E has389 states.
The400-run capture probe instead builds a **separate** clean-state set at each
sample's theta, over a different tick range, and compares32-bit windows against
that set. It does not test membership in the reported389-state closure.
Therefore “400 of400 equal their own-phase clean windows” is supported; “400
of400 enter this certified S_E” needs a further membership check or a proof
that all those projected clean states lie in S_E. Full phase is retained in
both codes, so this is an exact finite-set question, not a tolerance issue.
The conversion also reverses the eight selected bits: capture's bit7 is D_(R-1),
whereas the closure's bit0 is D_(R-1). Truncate the **top** eight bits of the
32-bit capture word, then reverse their order. Do not truncate its low eight.

**Concrete route:** retain the actual captured (theta,32-bit word) for each run,
convert its top eight bits to the closure convention, and verify membership in
an exported S_E. That avoids another horizon search. If those records were not
saved, first export the389 states and an exact successor/advance certificate;
a separately frozen small phase-alignment audit is preferable to repeating all
400 trajectories. This does not affect the conditional robustness lemma.

For C1, analyze all reachable cycles in the complement using the same phase
classes and FAIL bookkeeping. A positive minimum cycle mean would exclude a
bounded front on an eventually FAIL-free path, provided it stays in the valid
interior depth range. Any remaining bounded counterpath must either revisit the
small boundary band or make infinitely many FAIL retreats. The near-boundary
alternative cannot be discarded: the sound interior graph does not cover it.
Negative cycles also obstruct a positive mean certificate; searching only
zero-advance simple cycles is not a complete diagnostic. For C2, zero disturbance
in the recorded window is insufficient unless agreement at and **beyond** the
clean front is retained; the deepest-disturbance-below-window condition in §44.6
is a valid sufficient version.

T41's pairs refute generic linear superposition of those tested modes. They do
not refute every special affine family. A single observed riding slot is a
location statistic, not a coset: a one-dimensional two-point family is always
affine, whereas a larger family needs closure under XOR after subtracting the
common base. Use GC2385 only for such a specific family, not another general
linearity census. Likewise, G16's FAIL-containing over-approximation is a failed
certificate, not by itself a proof that every physical continuation is non-robust.

**Live next step:** review/export the fixed W8 S_E certificate and close the
capture-to-S_E phase/bit-order interface. Local owns C1, so no duplicate bad-core
job. Warm alternative: an exact argument for the near-boundary band/deep-retreat
accounting. Independent curiosity: Cloud's saved prefix recurrence and the
specific (still unproved) parity mechanism behind the comoving period band.


**Delta-audit outcome:** [checker](../tests/probes/front_closure_delta_check.py)
passes240 states across W=1..4, all edge sets/FAIL counts, plus256 bit-order
controls. Direct original-rule evolution is the third oracle. Intel, one
process,nice10,0.0374 CPU seconds; no W8 closure rebuilt. Checker source SHA256
`e93cd97dd223252158ec7aaf7e4a56a315f9cb154cf29afd55bd44becde17a18`;
result SHA256 `a435c5ea2b2f0c42859674c2bdde71d61ce2f3553e17e3731116f5d1532d4cb6`.
Reviewed `front_closure.py` SHA256
`ee71e2a9d94a4d61a9a47c84d7fc2b6e7559d0b5a74b13e72633432c15e3f76a`;
`front_cert.py` SHA256
`0bbd7d76351375eda9e0e2561206541a1467ef4c0d6c6e0b1cbc70fa86daf288`.
Evidence archive `cited/gpt/gc2386-closure-review.tar`,10,240 bytes,SHA256
`f5b49cc106758476e05e0fa0b946ec6232eb448257ca86c8a2e2b2485b8ffc78`,
raw-body upload/readback verified; includes phase-file/source pins. This passes
an implementation self-check and supports the source comparison, not an
independent reconstruction of the416/389-state certificates.
