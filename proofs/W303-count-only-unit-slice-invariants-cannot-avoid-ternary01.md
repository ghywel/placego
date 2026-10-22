# Count-only unit-slice invariants cannot avoid ternary01

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G303 — Count-only
unit-slice invariants cannot avoid ternary01 (2026-10-15; GC1277-1278)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A set closed under multiplication by4 and containing a unit1 cannot avoid ternary01 if membership on
that unit slice depends only on digit counts. Legal unit-preserving permutations and explicit carry
identities give a terminating reduction. PROOF-SKETCH pending independent review.

**Why it matters.** Count-only middle memory, including residues and thresholds, cannot supply the sought
invariant. General order-sensitive automata remain open; the controlled path is not an unchanged power orbit.

## The formal statement and proof

*Status:* PROOF-SKETCH, independent carrying read requested. Small exact controls COMPUTED separately.
*Bears on:* a restricted all-state K2-prime barrier, not K2-prime for arbitrary regular languages or Erdős.
*Provenance:* direct use of the x4 carry transducer, prompted by G302's odd-count-of2s countercontrol.
Bounded record/prior-art searches are in GC1277/PRIOR-ART; no novelty claim. No Parikh-image theorem imported.

**Definition and claim.** Say L is count-only on the unit1 slice if for any positive n,n' congruent to1 mod3
with the same three ternary digit counts, n belongs to L iff n' belongs to L. Only canonical finite numerals
are used: no leading-zero padding and no change to the lowest digit1 are permitted. If4L subset L and L
contains any unit1, then L meets C-star, the positive ternary01 integers. No regularity assumption is needed.
In particular no invariant deciding its unit1 membership only from digit counts (including any count
residues or thresholds) can prove avoidance. General order-sensitive regular invariants are not covered.

**Controlled operation.** At each stage we may replace the current numeral by a canonical unit1 numeral
with the same counts and THEN multiply by4. The extra saturation hypothesis preserves L under the first
operation and forward closure preserves it under the second. This is not multiplication alone on the
original integer. We prove that a finite sequence of these operations reaches C-star.

Write(a,b,c) for counts of0,1,2; b>=1 because the low digit is1. If c=0 we are done. In the words below
digits are written LSD-FIRST, so first digit1 means unit1 and the last digit must be nonzero for canonicity.
Every displayed input starts1 and ends2. Multiplication by4 at digit d and carry q emits(4d+q) mod3 and
updates the carry to floor((4d+q)/3). Carries range0..3.

    old carry q | d=0: (output,next) | d=1            | d=2
              0 | (0,0)              | (1,1)          | (2,2)
              1 | (1,0)              | (2,1)          | (0,3)
              2 | (2,0)              | (0,2)          | (1,3)
              3 | (0,1)              | (1,2)          | (2,3)

Start at carry0; final carries0,1,2,3 flush as the LSD words empty,1,2,01 respectively. That flush is
part of the canonical product. The following cases follow directly, keeping all counts including zeros.

**A: normalize when a<c.** Choose

    1^b 2^(c-a) (02)^a.

After the ones the carry is1: the first1 emits1 and the rest emit2. The first2 emits0 and reaches carry3;
the next c-a-1 twos emit2 and keep carry3. Each02 then emits00 and returns to carry3. Flushing01 gives

    (a,b,c) -> (2a+2, 2, b+c-a-2).                       (A)

The exponent c-a is positive and the new count of2s is nonnegative. The input uses exactly a zeros,
b ones and c twos, without ever moving a zero into the least-significant position.

**B: normalize when a>=c>=1.** Choose

    1^b 0^a 2^c.

The first1 emits1, the next b-1 ones emit2, leaving carry1. The first0 emits1 and resets carry0, and
the next a-1 zeros emit0. The first2 emits2 and reaches carry2. If it is the only2, the final carry2
flushes one more2. Otherwise the second2 emits1 and reaches carry3; the remaining c-2 twos emit2 and
carry3 flushes01. Thus

    (a,b,1) -> (a-1, 2, b+1),
    (a,b,c) -> (a, 4, b+c-2) if c>=2.                    (B)

All exponents are valid because a>=1. These are universal carry identities, not sampled recurrence fits.

**H2: finish if b=2 and a>=c>=1.** Choose

    1 0^(a-c+1) 1 2 (02)^(c-1).

After the first1 the nonempty zero run resets carry0 using only outputs0/1; the next1 reaches carry1,
then2 reaches carry3 emitting0. Each02 emits00 and the final flush is01. The product has no2.
This input has exactly counts(a,2,c), and its product has counts(a+c,4,0).

**H4: finish if b=4, c>=2 and a>=c.** Choose

    1 0^(a-c+2) 1 2 1^2 2 (02)^(c-2).

The first zero run resets carry0. The next12 reaches carry3, the two1s go3->2->2 with outputs1,0,
and the next2 goes2->3 emitting1. The remaining02 pairs emit00 and the flush is01. Again no2 occurs.
The input has exactly counts(a,4,c), starts1 and ends2. No leading-zero convention is used.

**Termination for all counts.** While c>0, apply H2 or H4 when applicable. Otherwise use A if a<c and B
if a>=c. A lands at b=2. B either lands at b=2 (c=1), or at b=4. From b=4, one further step either
finishes by H4, uses A to reach b=2, or, in the remaining a>=c,c=1 case, uses B to reach b=2. Therefore
at most two normalization steps reach b=2 or finish. At b=2, if a>=c, H2 finishes; otherwise A gives

    (a,2,c) -> (2a+2,2,c-a).

If a=0 this first increases it to2 without increasing c. After that a is positive and every further
nonfinal A step strictly decreases the positive integer c. Hence only finitely many such steps are
possible; a finisher or c=0 is reached. All products are still unit1 because4=1 mod3. Starting in L,
every operation stays in L, so the eventual c=0 contradicts avoidance. This proves the claim.

**Automaton consequence.** For an LSD-first DFA, let q1 be its state after consuming the required first1.
If the three digit transition maps commute on the states reachable from q1, then any permutation of the
remaining digits gives the same state. On canonical unit numerals that implies the saturation hypothesis,
so such an automaton cannot be an avoiding invariant with a unit1 witness. A general DFA can retain order
through noncommuting transitions; no state-count bound or exclusion of that case is proved.

**Registered finite controls and unexpected check.** GC1277/e8f615c7 precedes erdos_gpt_digit_counts.py.
All288 feasible triples a=0..6,b=1..6,c=0..6 pass, excluding six unrealizable c=0,b=1,a>0 triples.
There are582 controlled multiplications, maximum4 in this range, with36 zero-step cases. Every reordered
input is canonical, unit1 and count-preserving; literal integer multiplication agrees with a separate
local carry transducer and the declared formulas. Gadgets used: A241,H2 207,B1 35,B2 60,H4 39.
Omitting the final carry fails at21_3. Unexpected path from19 is

    19 -> 76 -> 304; permute304 to550; then4*550=2200, which is ternary01.

Both304 and550 have counts(2,2,2) and end1. But2200 is NOT19*4^3=1216. This retained control prevents
calling the constructed path an unchanged power orbit, and therefore prevents an Erdős inference. The
initial shortcut of moving zeros to the low end was rejected before running; every repaired move keeps low1.

**Limits.** Unit saturation is an added hypothesis, not a consequence of regularity. Empty unit1 slices
are allowed (e.g.{n=2 mod3} is x4-closed and avoids C-star), showing the witness is essential. The theorem
excludes a defined count-only class, including G302's unit1/odd-count-of2s countercontrol under any proposed
closure, but not all finite middle memory. No dependency on G302's density proof and no solver run duplicated.

**Independent carrying second read (Cloud, CL399, 2026-10-15 14:11 BST). VERIFIED.**
- *The transducer.* Each entry is (4d + q) mod 3 and floor((4d + q)/3); the twelve cases check, carries stay in
  0 .. 3, and the flush words (empty, 1, 2, 01 LSD-first) are the base-3 digits of the final carry.
- *(A), a < c.* After 1^b the carry is 1 and the outputs are 1 2^(b-1); the first 2 emits 0 and sets carry 3; the
  remaining c - a - 1 twos emit 2; each 02 emits 00 and returns to carry 3; the flush adds 01. Counts: zeros
  1 + 2a + 1, ones 2, twos (b - 1) + (c - a - 1). Exact, including a = 0 (no 02 block).
- *(B), a >= c >= 1.* The zero run's first digit at carry 1 emits 1 and resets the carry, so a >= 1 is used and
  holds; the two cases c = 1 (flush 2) and c >= 2 (second 2 emits 1 at carry 2, then carry 3, flush 01) give
  (a - 1, 2, b + 1) and (a, 4, b + c - 2).
- *H2 and H4.* Both words have exactly the claimed counts (zeros a - c + 1 + (c - 1) = a; a - c + 2 + (c - 2) = a),
  start with 1 and end with 2, and every emitted digit is 0 or 1 along the stated carry path (H4: 1 2 1 1 2 runs
  carries 1 -> 3 -> 2 -> 2 -> 3 with outputs 1 0 1 0 1). The products end in the flush's 1, so they are canonical.
- *Termination.* B's c = 1 case and A land at b = 2; B's c >= 2 case lands at b = 4, from which one more step
  finishes (H4), or reaches b = 2 (A, or B with c = 1). At b = 2 with a < c, A maps (a, 2, c) to (2a + 2, 2, c - a):
  from a = 0 it only raises a to 2, after which each step lowers c by at least 2; a >= c then finishes by H2.
- *The logic.* Each rearrangement stays in L by the count-only hypothesis (the gadget words are unit-1 canonical
  numerals with the same counts) and each product stays in L by 4L in L, unit-1 since 4 = 1 mod 3; a count with
  c = 0 is a member of C*.
- *Replay.* `tests/probes/swarm/erdos_gpt_digit_counts.py` reproduces ALL CONTROLS PASS (288 feasible triples, 582
  multiplications, maximum 4 steps; flush omission refuted; the 19 -> 76 -> 304, 550 -> 2200 path).
Scope as GPT states it: count-only invariants on the unit slice are excluded; order-sensitive automata are not.
Read because it bears on K2′, the active capped block. Moved out of the waiting room on this read.

Filing check: proof_dupes --near W303 passes. Nearest G298, G297 and G302 read in full: backward-hit
3-adic density, unit normalization and joint-end density respectively. This proof uses none of their
density mechanisms. G303 removes the extra count-only class by explicit legal permutations and carries,
not all regular invariants. G302 was promoted on Local L737 with its original carrying review intact.

**Scope niggle.** G302's end-only exclusion and this count-only exclusion do NOT exclude combinations of
end information with counts. The regular language unit1 + leading2 + odd-count-of2s has an order-insensitive
middle summary yet is not count-only (211_3 accepted,121_3 rejected with the same counts) and not determined
by bounded ends (toggle a free middle2). It fails closure at22->88, so supplies no invariant. It does show
that the two partial theorems alone do not establish a need for deep interior order-sensitivity.
