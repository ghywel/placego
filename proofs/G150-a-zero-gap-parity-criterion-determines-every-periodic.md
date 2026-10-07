# a zero-gap parity criterion determines every periodic predecessor period

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT150. a zero-gap parity
criterion determines every periodic predecessor period (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For a nonconstant periodic spatial row, its runs of ones between zeros tell us exactly how its predecessors behave. A run of length one modulo three resets the inverse and gives one predecessor of the same period. Without a reset, an odd number of runs of length two modulo three gives two predecessors with doubled period; an even number gives two of the same period. This sharpens the earlier stay-or-double bound, but does not control successive backward rows or construct a finite wall-compatible head.

## The formal statement and proof

### G150. A zero-gap parity criterion determines every periodic predecessor period (2026-10-07)

**Status and target.** Symbolic periodic-tail refinement, independent review pending. No experiment. Uses reviewed G13's exact reset language and G124's inverse-pair period bound; relevant prior-art scope is in PRIOR-ART.md. Prediction: for a nonconstant periodic output, the stay-or-double choice is determined by a parity of its cyclic zero gaps. Counterfactual: G124's bound alone leaves that choice unspecified. The two-state return calculation below supplies the exact choice and counts the aligned whole-line predecessors. This concerns ordinary spatial rows, not temporal diagonals or a forced-wall finite head.

Fix a nonconstant whole-line output y of least spatial period p. Around one primitive period, list the lengths L of runs of ones between consecutive zeros, including L=0 for adjacent zeros. Then:

- If any L is 1 modulo3, y has exactly one whole-line predecessor, of least period p.
- Otherwise, let N count the gaps with L=2 modulo3. If N is even, y has exactly two whole-line predecessors, both of least period p. If N is odd, it has exactly two whole-line predecessors, both of least period 2p; translation by p exchanges them.

Every whole-line predecessor is periodic. Counts are for a fixed labeled output y, without quotienting the predecessors by spatial phase. Constant outputs are separate: zero has its two constant predecessors, and one has the three period-three phases from G124.

**Return-map proof.** Use G13's adjacent input state (a,b) and descending driver transitions

    T_y(a,b)=(b, y XOR (a OR b)).

Reading one spatial output period gives a deterministic map H on four states. A whole-line predecessor supplies a bi-infinite orbit of H at successive period cuts. Every such orbit lies on a cycle: in a finite functional graph, a noncycle point has only a bounded backward transient; a deterministic cycle cannot be exited. Conversely every cycle point determines a unique predecessor by following the within-period transitions in both directions. This also proves that no nonperiodic whole-line predecessor was omitted.

If a cyclic gap has L=1 modulo3, repetitions of the driver contain the G13 reset factor 0 1^(3h+1) 0 z. Some power of H therefore has singleton image. H has exactly one cycle point and that point is fixed, giving one p-periodic predecessor. Least period is p because an output's least period divides every predecessor period. The reset factor may straddle periods; it is not necessary that H itself already have rank one.

Suppose no gap is 1 modulo3. After sufficiently many zeros, the surviving pair-state set just after a zero is either

    C={00,11},    A={00,01}.

This follows from G13's image table: the second zero reduces the full image to at most two states, and in the absence of the forbidden gap the after-zero sets are C or A. Label 00 as zero and the other state as one. Direct use of the four-state transition table gives, for a run of L ones followed by a zero:

| L modulo3 | Starting C or A | Ending set | Label map |
|---|---|---|---|
| 0 | either | C | identity |
| 2 | either | A | interchange |

This includes L=0. For positive multiples of three, T_1 cycles 00->01->10->00, and the following zero yields C with the same labels; for residue two the following zero yields A with exchanged labels. In particular both labels survive every permitted gap. At a fixed cyclic cut the set type returns to itself, so H on its recurrent two-state set is identity when N is even and interchange when N is odd. The corresponding one- or two-period cycles give exactly the stated two predecessors. Output least period p rules out any smaller period; the interchange case is not p-periodic, so its least period is 2p.

**Independent arithmetic controls, without a run.** Output (001)^infinity has a cyclic one-run of length1 and the unique predecessor (101)^infinity. Output (011)^infinity has one gap of length2, hence two period-six predecessors: (001010)^infinity and its translate by three, as in G124's literal trajectory. Output (000111)^infinity has gaps 0,0,3 and no interchange; its two period-six predecessors are (000010)^infinity and (111001)^infinity. Their six literal triples give the same labeled output 000111. This last example is the unexpected guard: absence of a reset does not itself imply period doubling; the parity is essential. Constants cannot be put into the zero-gap rule unchanged.

**Tail implication and limit.** G149's backward periodic tail can now be classified at each step by reset presence and this parity, rather than only bounded by p or 2p. A reset fixes the tail independently of the finite head; without one, the head selects a surviving label, possibly only the phase of a doubled tail. This does not bound reset gaps across successive backward rows, determine the boundary-phase silver initial tail, or prove a forced wall has a finite head. The one-step criterion must not be iterated as though its gap counts stayed unchanged. No new run, finite witness or prize conclusion follows.

*Second reader's note on G150 (Local, 2026-10-07; chat L106).* Correct. I checked the gap-label table by hand from the
descending transitions: after a zero the surviving pair sets are $\{00, 11\}$ or $\{00, 01\}$. A run of ones of length
$0 \bmod 3$ returns to the first set with labels kept, one of length $2 \bmod 3$ ends in the second set with labels
exchanged, and a run of length $1 \bmod 3$ is G13's reset. The aligned counts follow from the cycle structure of the
period return map. Every whole-line predecessor is periodic because its cut states form a bi-infinite orbit of a finite
deterministic map. The counts were also checked by a method that does not use the reset machinery
(`rule30_audit_g99_g100.py`, S45). For every nonconstant cyclic output of least period at most 14 (32,474 outputs:
28,637 with a reset, 1,872 even, 1,965 odd), the left-to-right transfer matrix counts the predecessors on rings of size
$mp$ for $m = 1$ to 6. They are 1 for every $m$ with a reset, 2 for every $m$ with even parity, and 2 or 0 by the parity
of $m$ with odd parity, so no predecessor of period $3p$, $4p$, $5p$ or $6p$ exists anywhere in that range. The three
literal controls were checked as ring steps. GC167's caution stands: the criterion is exact for one step, and the gaps
change from row to row.
