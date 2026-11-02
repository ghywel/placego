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
