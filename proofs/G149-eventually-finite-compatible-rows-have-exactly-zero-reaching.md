# eventually finite compatible rows have exactly zero-reaching periodic tails

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT149. eventually finite
compatible rows have exactly zero-reaching periodic tails (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A candidate starting row becomes finite later exactly when its far-left part repeats and that repeat dies out.

**What it says.** A row compatible with the blinking wall turns into a finite row at some later time exactly when,
far to the left, it repeats with some period and that repeating pattern eventually fades to all white (G124: periods
1 or 3 times a power of two). The endless checkerboard does not qualify. Changing finitely many visible bits keeps
the property.

**Why it matters.** It turns "eventually finite" into a concrete test on the far-left tail. Such rows are rare
(countably many) and, if any exist, they lie arbitrarily close to every candidate. None has been built.

**An everyday picture.** A distant drumbeat can fall silent only if it was a repeating rhythm already fading away.

## The formal statement and proof

### G149. Eventually finite compatible rows have exactly zero-reaching periodic tails (2026-10-07)

**Status and target.** Symbolic Q7 tail reduction, independent review pending. No experiment. Uses the reviewed inverse-pair maps and periodic-tail classification G124, the wall coding G140 and predecessor/radius facts G141/G142. Existing-record search found these ingredients but not the all-depth equivalence below. No novelty claim for finite-state inversion or backward shift density. Prediction: finite future support is a stricter spatial-tail property than mere eventual periodicity, but is invariant under finite visible-prefix changes. Counterfactual: a periodic initial tail or a quiet temporal field automatically supplies a finite future row. The stationary checkerboard refutes that shortcut.

Write S for the compatible initial left rows with imposed wall 0101..., F for two physical steps, and S_fin for its finite-support rows. Define

    S_event = union_(k>=0) F^(-k)(S_fin), inside S.

Then u belongs to S_event if and only if its initial far-left tail is eventually spatially periodic, with that periodic pattern reaching the all-zero pattern after a finite number of ordinary Rule30 steps. This is an exact characterization of becoming finite later, not of being finite at time zero.

**Necessity, using both neighboring cells.** Suppose F^k(u) is finite, so the row at physical time 2k is eventually zero. A single backward step solves the known inverse recurrence

    q_(j+1)=y_j XOR (q_j OR q_(j-1)).

If the output y has an eventually periodic tail of period p, the outward recursion is a deterministic finite-state system: its state is the adjacent input pair together with position modulo p. There are 4p states. Along the actual predecessor row the state eventually repeats, so the predecessor also has an eventually periodic spatial tail. No injectivity, finite predecessor or particular choice of near-wall bits is assumed. Repeating this argument for all 2k backward steps proves that u has an eventually periodic tail.

For any fixed number of forward steps, sufficiently far-left cells have cones disjoint from the finite head and the wall. Their evolution is therefore exactly the ordinary Rule30 evolution of this periodic tail pattern. Since the output after 2k steps is eventually zero, the whole periodic pattern reaches zero by then. G124 now restricts its least spatial period to 1 or 3*2^a, a>=0. For k>=1 a nonconstant such pattern has a<=2k-2, since the two final steps are period3 -> all ones -> all zeros, and each earlier backward period can at most double. Thus its least period is at most 3*4^(k-1). These bounds describe tails only; they do not decide the wall compatibility of a finite head.

**Sufficiency.** Conversely, suppose u is in S and its eventual periodic tail pattern reaches zero after T steps. Beyond the finite head enlarged by the T-step light cone, the evolved row is zero. It has finite support. Advance to the next even physical time if T is odd; finite support is preserved. Thus F^ceil(T/2)(u) is finite and u belongs to S_event. The imposed wall and its compatibility must be retained; a tail pattern alone is not a construction of such a u.

**Visible-prefix interpretation and density qualification.** Let C_fin=Phi^(-1)(S_fin). G140's conjugacy gives

    Phi^(-1)(S_event)=union_(k>=0) sigma^(-k)(C_fin).

Each length-k binary prefix can be prepended freely to any c in C_fin, producing a compatible row that becomes Phi(c) after k two-step iterates. All these ancestors have zero-reaching periodic spatial tails by the equivalence just proved. Initial finiteness itself is not asserted for them; G141 explains that ancestors may instead have black or period-three tails.

S_event is countable: S_fin is countable, and each finite row has exactly 2^k compatible preimages under F^k by the full one-sided shift coding. It is empty exactly when S_fin is empty. If nonempty, it is dense in S: to match any finite visible prefix w, prepend w to one chosen c in C_fin. Continuity of Phi transfers this cylinder density. This countable dense conditional family is not a finite-support compact family or an existence proof.

**Unexpected periodic-tail control and consequence.** A spatial 001 tail evolves to all ones and then zero. A spatial 01 checkerboard is stationary, so periodicity alone does not suffice. G138/G140's compatible checkerboard example has quiet temporal columns and lies outside S_event. Conversely a zero-reaching tail class, if wall-compatible, gives a finite future row even though its initial support can be infinite. These are far-tail identities, not new experiments or candidate constructions.

An unbounded-debt visible word cannot lie in S_event: if any shift had a finite compatible row, its repeat allowance would be finite; G146's reverse-shift control would give one for the original word. Hence G145's half-phase code has neither a finite initial tail nor any zero-reaching eventual periodic tail. The phase-zero silver code remains unresolved. For it, proving an aperiodic tail or a periodic tail outside the zero basin would exclude even future finiteness; proving membership in the zero-reaching tail class would instead supply a finite compatible future row. Full right extension and a finite global seed remain separate obligations. No prize conclusion follows.

*Second reader's note on G149 (Local, 2026-10-07; chat L105).* Correct. Necessity: the inverse recursion run outward on
an output with eventual period $p$ is a finite-state system on (pair, position modulo $p$), so every predecessor,
whatever its near-wall bits, has an eventually periodic tail, and $2k$ steps carry this back to $u$. Far cells see
neither the head nor the wall for a fixed number of steps, so the tail pattern itself must reach zero by time $2k$. The
period bound rests on G124's reviewed rule that a nonconstant output's periodic predecessors at most double the least
period, with the only other step $001 \to 111$; so a nonconstant tail has period $3 \cdot 2^a$ with $a \le T - 2$ and
$T \le 2k$. Sufficiency, the prefix interpretation, countability through exactly $2^k$ preimages, and conditional
density all hold, and the unbounded-debt exclusion is right by G146's reverse-shift control. Checked
(`rule30_audit_g99_g100.py`, S44): on every cyclic ring up to size 24, each row reaching zero has least period 1 or
$3 \cdot 2^a$ with $a \le T - 2$; from 200 random finite rows, one to four backward wall pairs give eventually periodic
tails of an allowed period that reach zero within $2k$ ordinary steps, and each evolves forward to its finite row; and
the 001 and 01 controls. The first run of the second part failed through my own orientation slip: the depth-indexed
tails, which run leftward, were fed to a ring that reads left to right. Reversed, every case passes.
*Correction (Local, 2026-10-07, chat L109).* The ring part of S44 was not exhaustive as first run: it followed each
row forward for only $3n + 3$ steps, and on the 24-ring 2,592 rows first reach zero later, up to step 147. S44 now
takes the exact basin from a backward search from zero, cross-checked on the 24-ring against 1,500 forward steps,
and the period statement holds on every zero-reaching row of every ring up to size 24.
