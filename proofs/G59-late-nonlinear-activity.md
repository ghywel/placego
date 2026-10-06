# Late nonlinear activity

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT59. Late nonlinear activity
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In Rule 210, a finite seed with a repeating wall would need its "and" operations to keep happening for ever.

**What it says.** Rule 210 without its non-linear term is Rule 90, which cannot sustain such a wall from a finite
row (proof 16). So any finite seed for Rule 210 must keep switching on the non-linear term infinitely often.

**Why it matters.** It rules out the simplest kind of witness: one that misbehaves for a while and then goes linear.

**An everyday picture.** A spinning top needs pushing again and again; one push at the start will not keep it up.

## The formal statement and proof

### G59. A finite periodic Rule210 witness needs infinitely many nonlinear events (2026-10-06)

A bounded proof audit extending G28's necessary condition, using the already recorded general Rule90 obstruction (PROOFS B′16), not a new mechanism or a computational search. Suppose a finite global Rule210 initial row realizes a nonzero periodic temporal wall of period p. Then adjacent black pairs must occur at arbitrarily late times. Equivalently its nonlinear source V_t(i)=x_t(i)*x_t(i+1) cannot vanish identically for all sufficiently large t.

Proof. If V_t=0 for every t>=t0, the configuration at t0 is finite by finite propagation, and all later updates are Rule90. Write A=S+S^(-1). If that row has support in[-R,R], then A^(2^k)=S^(2^k)+S^(-2^k). For every j=0,...,p-1 and 2^k>R+p, the centre of A^(2^k+j)x is0: it samples A^j x at sites plus/minus2^k, outside its support[-R-j,R+j]. Thus the wall contains p consecutive zeros at arbitrarily late times. A nonzero p-periodic wall cannot contain even one such block. Contradiction. The argument also covers an eventually periodic nonzero wall by choosing k beyond its transient.

This strengthens G28's requirement of at least one nonlinear activation to infinitely many activations for any nonzero periodic wall, including G58's one-parity family. It does not prove activations reach the wall, exclude a finite witness, or realize the required right stream. Infinite nonlinear activity is necessary, not asserted sufficient. Because a global single-parity row stays Rule90 forever, no finite global single-parity seed can realize any nonzero eventually periodic wall; the period-two clock was only G28's special case.

**Unexpected scope guard, checked algebraically.** Finiteness cannot be dropped from the Rule90 step. A spatially period-three row100 repeated evolves under Rule90 to011 repeated, which is fixed: the three neighbor XORs are0,1,1. At the sites with value1 this gives a nonzero constant temporal wall from time1. This is a Rule90 domain counterexample, not a Rule210 witness (the adjacent pairs activate its nonlinear gate). It prevents importing the finite-row obstruction into unrestricted infinite backgrounds.

No experiment ran and no numerical extrapolation is used. Existing G28 controls and the recorded Rule90 identity are reused. Independent Local reading requested; next right-realization reasoning must allow mixed parity and unbounded nonlinear activity, rather than a finite correction followed by a linear tail.


*Second reader's note on G59 (Local, 2026-10-06; chat L034).* Correct. With no adjacent black pair from $t_0$ on,
Rule 210's term $c \cdot r$ is $V_t(i) = 0$ and the global evolution is Rule 90 from a finite row; over GF(2),
$A^{2^k} = S^{2^k} + S^{-2^k}$, so the centre of $A^{2^k + j}x$ samples $A^j x$ outside its support once
$2^k > R + p$, and the wall has $p$ consecutive zeros at arbitrarily late times, impossible for a nonzero
(eventually) periodic wall. The single-parity corollary and the period-3 scope guard ($100\ldots \to 011\ldots$, then
fixed) check. Checked (`rule30_audit_g59.py`): the zero blocks on 300 random finite rows and the fixed point.
