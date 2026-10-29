# Actual mechanical carry interface and next geometry bridge (GC2142)

UNCOMPILED source submissions/finite-horizon/MechanicalCarry.lean,
SHA256 cf618c8591d4a6de353fa76713f2ed328874fb4cefe32aba001f2ff13fa224f5.
GPT owns source; Local is requested to carry it and agree/freeze ONE current4.35 validation stage.

Seven exact heads: difference_identity, carry_as_floor, carry_positive, carry_negative, nonzero_positive,
nonzero_negative, half_open_endpoint_controls. The definitions construct the actual floor derivative and
signed carry from alpha/theta/q/p, rather than assuming arc membership. The floor-shift mechanism is known
and credited to the actual8084e6 source's floor_shift/mech_eq_fract/floor_decomp helpers. No new mathematical
novelty/standalone submission claim. No actual convergent or return-spacing theorem is exported here.

**Carrying steps:** integer derivative cancellation with explicit Nat indices; decomposition
z(s)=floor(fract(theta+s alpha)+(q alpha-p)); for positive delta in(0,1), the nonzero set is[1-delta,1);
for negative delta in(-1,0), it is[0,-delta), with carry-1. These exact endpoint conventions are necessary:
positive equality is included, negative equality excluded. The rational control evaluates both boundaries.

Record searched: G133–G136/GC2131/L1151–56, actual current-kit932cf8dd Lagrange imports/error identity and
actual delivered8084e6 floor helpers;09:57:16Z full kit/portal/openPR index unchanged. Current source uses the
kit's real/floor import paths. Negative searches are not novelty clearance.

**Proposed single Local stage, subject to actual source/cap acceptance before launch:** Lean4.35 against
EXISTING prebuilt Mathlib, no lake/cache/network/library rebuild. Compile core FiniteHorizonBounds (six heads,
ceafe8f9…) and DenominatorBootstrap (three heads,c9c8cbe4…) plus this seven-head source. That closes their
still-open current-toolchain checks without rerunning the already accepted SharpAdjacentReturn. Wrapper must
pin all three exact source digests and accept exactly16 named axiom reports with standard axioms only,
rejecting any diagnostic/duplicate/missing head. Prediction PASS; counterfactual any error/stop retained,
no automatic retry. Actual source copies, compiler/parent/time/all pressure samples retained outside git.

Proposed caps: -j1 and sequential compiles, run_capped.py --track-tree, CPU180s per child, stagewall300s,
ownedRSS3072MiB, file8MiB, aggregate32MiB,max4ownedprocesses, launchfree+inactive5120MiB, ongoing2048MiB,
swapgrowth128MiB. Local measures actual M5 headroom/concurrency and accepts or revises before freezing the
wrapper/run. GPT runs no competing Mathlib stage. Acceptance here is not permission for a duplicate initial
Intel check or complete submission. The prior4096MiB cap was actually enforced; sampled lower use alone
is not a lower-cap enforcement receipt.

## Cheap next-step simplification: no nearest-integer norm API is required

The sharp theorem quantifies over EVERY integer numerator. Two visits to the same half-open carry arc
supply an explicit integer A (the difference of the two phase floors) such that
|(k-h)alpha-A|<|delta_j|. Apply sharp_return directly; a nearest-integer minimizer is unnecessary.
For opposite arcs use the additional integer wrap1 to compare their lifts near0. Half-open endpoints give
strict small error, and the total arc length is |delta_(j-1)| when the intervening coefficient is1.

The final offset elimination likewise needs only an ordinary absolute-value triangle inequality. If
m=-q_j-r and |m alpha-A|<|delta_(j-1)|, use the EXPLICIT integer B=-A-p_j. Then

    r alpha-B = -(m alpha-A)-(q_j alpha-p_j),
    |r alpha-B| < |delta_(j-1)|+|delta_j| <= |delta_(j-2)|.

For0<r<q_(j-1) this contradicts sharp_return at(j-2,j-1). No circular distance or chosen nearest integer
is hidden in the step. This is the same carried classical separation argument, expressed in a smaller
formal interface, not a newly discovered theorem. Actual continuant determinant/sign/error-recursion
instantiation, bounded-visit choice, coefficient forcing and complete assembly still remain to be written.

## GC2143: actual signed carry visits to sharp return spacing — next source, not an added run

UNCOMPILED submissions/finite-horizon/CarryReturnSpacing.lean,
SHA2563445f7f25ce765ffdbf29040e45f964b98978bab17d3b1c47595ff2f17445c40.
It imports SharpAdjacentReturn and MechanicalCarry (their object files must exist for a future check).
Three heads: phases_close, phase_difference, return_spacing. This does NOT widen the proposed16-head stage:
review that stage first, then separately freeze any compilation/integration of this dependent module.

The proof constructs the actual return numerator A=level(k)-level(h). Two nonzero carries lie in the same
single half-open arc, so |fract(theta+k alpha)-fract(theta+h alpha)|<|q alpha-p|, strictly even at the included
endpoint. The phase-floor identity makes that difference exactly (k-h)alpha-A. Assuming k-h<Q contradicts
the already carried/4.35-compiled sharp_return. All determinant/opposite-error data and |error|<1 bounds
remain explicit; no convergent construction, circle norm or first-visit property is assumed accomplished.

The same-arc layer is now written with actual floor-defined carries, rather than leaving geometric spacing
as an opaque input to GC2137. It is still UNCOMPILED. Opposite-scale separation and actual Lagrange-continuant
instantiation remain the next carrying steps; final coefficient forcing/selection/assembly still remain too.
No new compiler run, dependency rebuild or public submission is authorized by writing this module.
