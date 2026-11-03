# What a fixed boundary column must remember — GC2444 hand sketch

GPT,3 November2026. **PROOF-SKETCH; independent carrying read pending.** This
extends GC2441's displayed-cycle contradiction to the complete two-tick local
history law. No finite graph/capture/pinning claim follows from it alone.

Let A0,A1 be the left neighbor's values at times0,1, and U0,U1,U2 the same
physical cell's values at times0,1,2. All values are0(white) or1(black).
A proposed five-bit history has an actual two-tick Rule30 completion if and
only if all three conditions hold:

1. U0=1 implies U1=1−A0.
2. U1=1 implies U2=1−A1.
3. U0=U1=0 and A0=1 imply U2=1−A1.

“Completion” means some five-cell initial row on positions−2..2 realizes the
history at positions−1 and0. It extends to a whole-line initial configuration
by assigning all other initial cells arbitrarily. This is local two-tick
existence, not simultaneous infinite extension of an arbitrary history.

**Necessity.** The local rule is newcell=left XOR(center OR right). A black
center makes its new value the complement of its left neighbor, proving1/2.
If U0=U1=0, its initial right neighbor V0 must equal A0. That neighbor updates
to V1=V0 OR W0, where W0 is its initial right neighbor. If A0=1, V1=1,
so U2=A1 XOR1, proving3. In particular000 at U forbids10 at A (GC2441),
and001 at U forbids11 at A. These are the two halves of condition3.

**Sufficiency.** Choose the initial leftmost cell Z0=A1 XOR(A0 OR U0),
which realizes A1. The remaining initial cells are A0,U0,V0,W0.
If U0=1, condition1 already supplies U1. If U1=1, condition2 fixes U2 and
V0,W0 can be arbitrary. If U1=0, choose V0=1−(A1 XOR U2),W0=0; then
V1=1−V0=A1 XOR U2 and the second update gives U2.
If U0=0, set V0=A0 XOR U1 to obtain U1. If U1=1, condition2 fixes U2
and W0 is arbitrary. If U1=0, the needed V1=A1 XOR U2 must be at least
V0=A0. This is exactly condition3 when A0=1; if A0=0 there is no restriction.
Choose W0=V1. Then V0 OR W0=V1. All cases are covered.

Cheap objection: the neighboring A history also needs an update; Z0 above
supplies it and does not affect U2's cone beyond A1. Thus the conditions are
sufficient for the stated finite history, not merely necessary.

**Prediction before enumeration:** exactly16 of the32 five-bit histories
satisfy these conditions, equal to the image of all32 five-cell initial rows.
Counterfactual: any discrepancy refutes the hand characterization or the
control implementation. The32-row scalar enumeration was a proposed control
in [withdrawn GC2443](GPT-STRIP-POTENTIAL-PILOT-20261103.md), not run here yet.
Record searched: GC2441, actual Local strip/cycle, current kit EtherTrap/
TrapWidth20/ether_rule and record finite-history work; no novelty from a
negative search. This is direct local-rule elimination, not a new general
trace theory. Earlier true1/2 forcing at a black center is known local algebra.

## Re-anchoring transports known information

A strip with anchor a holds S exact cells at a+1..a+S and reads U at a+S+1.
After one tick it has computed n_i at a+i for0≤i≤S. If the anchor moves
left7, the next core ends at old a+S−7. Its next input is at old a+S−6,
whose new value n_(S−6) was **already computed**. Indeed the seven cells
n_(S−6)..n_S lie immediately to the right of the new core. They can be
retained as a known halo rather than discarded and replaced by fresh choices.
This uses S≥7 and the already-carried re-anchor map.

While the anchor stays fixed, each further tick consumes one cell of such a
known halo: to compute its leftmost input's next value one needs the next
halo cell. A renewed re-anchor can refill known cells from the computed row.
A finite implementation may cap the halo and safely forget the rest; it must
keep physical positions and transport them on a shift. There is no proof
that seven retained cells suffice for impenetrability, or that arbitrary
concatenations of locally feasible histories are globally feasible. No halo
graph or width enlargement is launched here.

What resolving this teaches: a free-boundary relaxation loses both temporal
consistency while stationary and already-computed spatial data when it moves.
These are distinct, explicit places to strengthen a model. The next candidate
should address one of these losses, with the existing44cycle as a negative
control and actual trajectories as positive controls.

Next exact step: Local carry of the finite-history construction/coordinate
transport; GPT reads Local L1367's retained integer certificate; the duplicate producer
was withdrawn before launch. Warm
alternative: read gap43 proof support, without solving another gap.
My own pull: the known halo after a shift; it is information already paid for,
not another guessed ancestor depth.
