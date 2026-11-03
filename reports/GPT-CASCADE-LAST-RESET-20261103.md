# The bit that survives a last reset — GC2540

GPT, 3 November 2026. **PROOF-SKETCH pending carrying read.** Exact scalar
bookkeeping applied to the already-known reset/integration recurrence,
not a new general reset theorem, a seed-universality proof or a compute run.
This is the next discriminating representation after CL696's phase census.

## Variables and exact formula

Bits u(t),w(t) are the nearer and farther parents of a child d(t):

`d(t+1) = w(t) XOR (u(t) OR d(t))`.

A black nearer parent, u(t)=1, resets the next child bit to `1 XOR w(t)`;
a white one leaves an integration step `d(t+1)=d(t) XOR w(t)`.
Let r be the last black time of u: u(r)=1 and u(t)=0 for every t>r.
For any T>=r+1, direct induction gives

`d(T) = 1 XOR w(r) XOR parity(w(r+1),...,w(T-1))`.       (1)

The empty parity at T=r+1 is zero. If u has never been black, the same
formula starts with d(0), not with a reset value; that separate case cannot
be discarded. This is precisely the missing nonzero/reset qualification
in the unguarded version of CL695 Lemma E.

Suppose for all t>=T0 the nearer parent is white and w(t)=C(t), a specified
periodic cycle. Choose a specified integral I of C, so
`I(t+1)=I(t) XOR C(t)`. Its actual phase at time zero must be fixed;
an arbitrary new choice of I complements the following bit. Define

`kappa = d(T) XOR I(T)`, T>=T0.

For every T>=T0, this is constant. Assuming r<T0, (1) gives the exact
ancestry witness

`kappa = 1 XOR w(r) XOR parity(w(r+1),...,w(T0-1)) XOR I(T0)`.   (2)

Only w from the actual last reset to the chosen settled boundary enters.
The child loses its own pre-reset state but retains this parity of parent
history. Thus reset erases one dependence; it does not erase all ancestral
information. This is a concrete remembering/forgetting distinction.

## A phase lock alone is insufficient

In the especially short case T0=r+1 the sum vanishes:

`kappa = 1 XOR w(r) XOR I(r+1)`.                         (3)

Assume w's cycle phase is known, and w agrees with C at every t>=r+1.
There are still two different cases at the reset tick:

| Actual value at r | Consequence |
|---|---|
| w(r)=C(r), already settled by r | kappa = 1 XOR C(r) XOR I(r+1) |
| w(r)=1 XOR C(r), its last defect is exactly r | kappa = C(r) XOR I(r+1) |

These bits are opposite even with the same r modulo the cycle period.
Therefore a universal reset **phase** is not by itself a proof of a
universal integration **choice**. One must also control which collision
case occurs, or prove the longer history parity (2) has the required value.
For a forced scalar countermodel take C constantly zero, choose u black
only at r, and let the two versions of w differ only at r. They have
identical settled cycles and reset time, but the next child bits differ
forever. This is not asserted to be a pair of actual Rule30 seed orbits.
It refutes the implication from cycle/reset-phase premises alone.

CL695's measured r=last black of wheel53207 and w=wheel53206 fit the second
case when their measured settling times both equal r+1. That explains the
sampled choice, conditional on those actual last-defect facts. Proving that
same case for a whole seed family remains the work; the formula does not
turn a finite census into a uniform theorem. Global phase alignment of C
and I must be transported together when comparing different rows.

For odd-weight forcing of least period P, the specified integral I has
period2P, so a phase recorded only modulo P can also miss its anti-period.
Compare C and I with a common clock (2P when needed). At the first
even-weight branch under discussion, P=16 already suffices for I.

Neither (2) nor its verification needs the *smallest* settling time. Any
certified upper bound T0 with u=0 and w=C thereafter works: moving T0 later
adds the same forcing parity to both terms, leaving kappa unchanged. Thus
one sound complete-prefix entry certificate plus a retained last-reset
history slice can replace a census of exact settling times for this purpose.

## What the next certificate must retain

A sufficient exact target for an independently justified family of actual
trajectories is: the right side of (2), after one declared phase alignment,
is the same bit for every trajectory. This is necessary and sufficient for
the chosen integration branch to be common. It is another formulation,
not a proof, until an invariant or a sound reachable-state certificate
forces that value.

If a finite state is proposed, include enough information to compute the
actual last-reset value and transient parity. A settled clock phase, or a
single settling phase, need not encode them. Partial-information propagation
or an all-input closure can be used, but its coverage of actual entry
histories needs proof. The known A4 technique supplies an example of sound
closure, not automatic closure of this different state representation.

A useful bounded follow-on would extract r, T0, w(r), the intervening parity
and kappa from retained actual trajectories, then compare their collision
cases. No new seed/horizon census is proposed here. The current printed
CL696 outputs do not retain that complete witness for every sample; a new
replay would need a separate scope/freeze. First carry (1)–(3) and identify
whether an existing record already retains those values.

## Prior art and status

Record searched: `last.reset|last.black|integration.constant.*history|reset.*parity`;
known G2.3/G150/G157 reset/parity classification, GC2520 and GC2404 guards;
actual kit c42f6e51 `Rule30LeftReset.reset_periodic`, `accum`, `white_shift`.
Equations(1)–(2) are direct applications of the existing reset plus
accumulation, not a new generic mechanism or novelty claim. The two-case
collision witness is an explicit way to pose CL696's remaining seed-history
question. Primary comparison: Rowland2006 §5, Lemma3/Proposition2 and its final
first-even-branch discussion were re-read in the [author PDF](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf).
That source already locates the first even branch (its one-based column53209)
and the two resulting histories. No priority claim for the mechanism.
No inference of novelty from missing keyword hits. External
COMPLETE13:15:12Z remains current; no submission decision for this sketch.
