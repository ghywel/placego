# Mahler's admissible set meets its doubles and triples only at 0

*Mahler and ternary digit obstructions. Derived from [PROOFS.md](../PROOFS.md), entry "Cloud 8.109 — Mahler's
admissible set meets its doubles and triples only at 0 (Cloud, 2026-10-14; waiting room)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** second-read; the head of PROOFS.md section M, quoted in the proofs index, gives each entry's current status.

## In plain words

If a nonzero number passes the admissibility test from Mahler's 3/2 problem, its double and its triple both fail.

**What it says.** Mahler asked whether some positive number, multiplied by 3/2 again and again, always keeps its
fractional part (the part after the point) below one half. Such a number is called a Z-number, and none is known.
The record recasts the question as a set of "admissible" 2-adic numbers: numbers that may have endlessly many binary
digits running leftwards, like an odometer that never ends. A whole number n is the whole-number part of a Z-number
exactly when it lies in the set's strict core, the admissible numbers whose every step stays strictly below one
half. The proof shows that a nonzero number is never admissible together with its double or its triple:
admissibility forbids two odd steps of the 3/2 map in a row, and for a number and its triple that would need two
quantities, one three times the other, both to leave remainder 3 on division by 4, which is impossible. So if n is
the whole-number part of a Z-number, then 2n and 3n are not, and neither are n/2 or n/3 when those are whole.
Multiplying by 2/3, by contrast, always keeps an admissible number admissible, though not every admissible number
arises that way.

**Why it matters.** It closes one hoped-for route. The famous rigidity theorems about multiplying by 2 and by 3
(Furstenberg's, which say that a set kept by two independent multipliers must be very simple) need a set that both
multipliers keep, and each of 2 and 3 pushes this set off itself instead. It describes the set, not which whole
numbers lie in it: it does not say whether any Z-number exists, and it does not list every multiplier that keeps the
set.

**An everyday picture.** Think of the set as a choir's list of allowed pitches, where doubling a frequency is an
octave up and multiplying by 3/2 is a fifth up. Any allowed note can always be sung a fifth lower, but never an
octave higher or lower, nor an octave and a fifth either way.

## The formal statement and proof

*Status:* PROOF-SKETCH, single-party. A second reader is wanted (GPT or Local). Filed late: it was written up in
RULE30-PRIZE.md 8.109 but not filed here, a miss logged in INSTINCT.md.
*Where:* RULE30-PRIZE.md 8.109 (the induction) and its 8.110 note (a one-step proof);
`tests/probes/mahler/mahler_cloud_two_multipliers.py` (exact to depth 28).

**Claim.** K, the closure of S_strict in Z_2 (the x whose every code prefix is admissible), satisfies
K ∩ 3K = K ∩ K/3 = K ∩ 2K = K ∩ K/2 = {0}. K is invariant under x -> 2x/3.

**Proof sketch.** 2y lies in K exactly when 3y does, since T(2y) = 3y. For x = 2^k m in K with m odd, the code
begins 0^k 1 c, where c is the parity of (3^(k+1) m + 1)/2. A 1 is always followed by a 0, so
3^(k+1) m = 3 mod 4. The same condition for 3x reads 3^(k+2) m = 3 mod 4, and the two cannot hold together.


**Independent carrying second read (GPT, GC1246, 2026-10-14). VERIFIED.** The original waiting-room status above
is retained as publication history. The first1/next-parity contradiction works in K and S_strict; closure cannot
introduce11. It also gives exactly{0,2^(T-1)} at every finite depth, including the one-bit boundary. The equivalence
2y in K iff3y in K is valid. Its precise image form is(2/3)K=K intersect2Z_2, a proper subset, not an automorphism
of all K. Direct multiplication by2 or3 is excluded; no classification of all multiplicative symmetries is verified.
Independent implementation and source replays: tests/probes/mahler/mahler_gpt_sign_review.py, registered de3b5c1a;
GC1246 records the controls, negative cases, original failures and finite scope. Bears on: Mahler's pair obstruction,
not exclusion of an individual positive integer. Source proof copied verbatim; no prize claim.
