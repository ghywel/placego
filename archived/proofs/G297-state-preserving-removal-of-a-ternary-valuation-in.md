# State-preserving removal of a ternary valuation in K2-prime

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT297. State-preserving removal of a
ternary valuation in K2-prime (second-read by Local, 2026-10-15)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If a digit-reading machine accepts a base-3 number ending in zeros, an equally small machine accepts one ending in
the digit 1.

**What it says.** Write whole numbers in base 3, using only the digits 0, 1 and 2. Take a set of numbers that stays
inside itself when every member is multiplied by 4, contains no number written only with 0s and 1s, and is
recognised by a finite automaton. A finite automaton is a simple machine with a fixed number of internal states that
reads a number's digits one at a time, here either lowest digit first or highest first, and answers yes or no.
Suppose the set contains a number, called the witness, whose last nonzero digit is 1. Then there is another set with
the same three properties that contains a number whose very last digit is 1, so one that leaves remainder 1 when
divided by 3; its machine has no more states and reads in the same direction. The new set is made by keeping the
members of the old set that end in at least as many zeros as the witness does and removing those zeros, and the
machine changes only where it starts (lowest digit first) or which of its states count as yes (highest digit first).

**Why it matters.** The record is looking for small machines of this kind as part of an approach to Erdős's question
of whether every large enough power of 2 has a digit 2 in base 3. This result lets that search assume the witness
ends in the digit 1, at no cost in machine size. It does not show whether such machines exist and says nothing
either way about Erdős's question. It also does not keep a particular starting number, such as 1024, in the set.

**An everyday picture.** Think of a ticket reader at a car park gate. Keep only the tickets that end in a certain
row of zeros and tear that row off: the short tickets need no bigger reader. You set its dial as if the zeros had
already gone through, or, if it reads the other way, you light the green lamp wherever the zeros would have taken
it.

## The formal statement and proof

**PROVED, Local L732 at62a33268 (merged atf0e57aa4).** Promoted by GPT in GC1259. The proof and review below are
retained verbatim from the waiting room; the original PROOF-SKETCH and review-request labels are historical.
Former heading: GPT G297, 2026-10-15 11:48 BST, GC1258. Scope: the state bound in each fixed reading direction;
not K2-prime or Erdős. The computational cross-check is separate from this hand proof.

**Status:** PROOF-SKETCH, awaiting Local's carrying read. **Bears on:** SW-01's K2-prime certificate class,
not a proof of Erdős or of the all-state barrier. **Source:** RULE30-GPT GC1258; L731 and GC1257 set the domain.

**Claim.** Let C-star be the positive integers with ternary digits only 0 and 1. For either fixed reading
direction, an at-most-s-state DFA recognising a set L of positive integers with 4L subset L and L disjoint from
C-star, and accepting some x whose lowest nonzero ternary digit is 1, exists if and only if one such at-most-s-state
DFA accepts some u congruent to 1 modulo 3. Canonical finite numerals are used; no padding condition is imposed.

**Proof.** Only the forward implication needs work. Write the accepted x as 3^a u, with u congruent to 1 modulo 3,
and set J = {n >= 1 : 3^a n belongs to L}. If n belongs to J then 3^a(4n)=4(3^a n) belongs to L, so 4J subset J.
If n belongs to C-star then 3^a n also belongs to C-star; hence n cannot belong to J. Finally u belongs to J.

For an LSD-first DFA (Q, delta, q0, F) for L, retain Q, delta and F and replace its start by delta(q0,0^a).
The canonical LSD numeral for 3^a n is 0^a followed by the canonical numeral for n. This new DFA recognises J.
For an MSB-first DFA, retain Q, delta and q0 and replace F by {q in Q : delta(q,0^a) belongs to F}. The canonical
MSB numeral for 3^a n is the numeral for n followed by 0^a, so this DFA also recognises J. Neither construction
adds states. Empty words and representations of zero stay outside the numerical domain in both cases. The
reverse implication holds because a unit congruent to 1 modulo 3 already has lowest nonzero digit 1.

**Carrying step to review.** Left quotient by 0^a in LSD order versus right quotient by 0^a in MSB order;
forward closure commutes with scaling, and scaling C-star by 3^a preserves C-star. Requiring a particular seed
such as 1024 is not guaranteed to be preserved by this normalization. No enumeration, small-state nonexistence or global
automatic-induction barrier is claimed. The argument uses standard regular-language quotient constructions;
no claim of novelty for that construction is made here.

Filing check: proof_dupes --near W297 passes after using the waiting-room heading convention. Nearest older
entries G127, G193 and G56 read: those concern Rule 30 sections, labelled graph quotients and ring phases,
respectively; none is this regular-language valuation quotient. Initial advisory lookup failed because the
first draft's W297 heading was not recognised; corrected to the existing GPT G297 waiting-room form.

**Independent carrying second read (Local, L732, 2026-10-15 11:57 BST). VERIFIED.** Each step was checked:
- *Closure.* n in J gives 3^a n in L, so 3^a(4n) = 4(3^a n) is in L, and 4n is in J.
- *Avoidance.* n in C-star makes 3^a n's numeral that of n followed by a zeros, still in C-star, so 3^a n is not in L.
- *The witness.* u is in J, with u = 1 mod 3.
- *LSD.* The canonical numeral of 3^a n is 0^a followed by that of n; the DFA started at delta(q0, 0^a) accepts a
  canonical w iff the original accepts 0^a w. Relabelling the new start as state 0 keeps the count and completeness.
- *MSB.* The numeral is n's followed by 0^a, and F' = {q : delta(q, 0^a) in F} accepts w iff the original accepts
  w 0^a; canonicity is unchanged in both directions.

Exactly-n and at-most-n searches agree, since unreachable states can be added. The scope note stands: a prescribed
seed is not preserved. A computational cross-check is registered in tests/probes/swarm/erdos_k2prime_barrier.py, P4:
the unit-witness and seed-free searches must agree at every size and direction. Status: PROVED (a proof with a second
reader); GPT may move it out of the waiting room.
