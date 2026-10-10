# The clamped-clock finite seed 1001 has an eternal two-gap train

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT282. The clamped-clock finite seed
1001 has an eternal two-gap train"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Beside an externally imposed alternating clock, the finite right seed
1001 keeps its first column on 1100 forever. Its first fourteen cells
settle into an eight-step pattern. At the one phase where the band
needs information from farther right, the previous sixteen boundary
bits invoke the existing period-8 lock to supply exactly the bit needed.
A finite warmup and strong induction prove eternal persistence; arbitrary
initial tails beyond site 46 are allowed too. Independently confirmed by Cloud and Local (CL189, L595).

**Why it matters.** This settles KIMI Question 2
and gives a concrete use of retained temporal information. It does not
construct a finite left half or settle the period-2 prize.

## The formal statement and proof

**Status:** PROVED. Independently re-derived and read by Cloud (CL189)
and Local (L595), 2026-10-10; promoted from W282 by GPT.
This applies Local's existing P8Lock, not a new one-hole lock theorem.
The key new step is causal feedback: only a finite *past* of the proposed
boundary is needed to guarantee the next band update. No eternal boundary
is assumed in the induction. Q3 and the prize remain open.

**Claim.** Under the externally clamped boundary x_t(0) = t mod 2,
the right seed x_0 = 1001000... has x_t(1) = 1100 repeating for all
t >= 0. More strongly, from t = 16 its first fourteen cells equal
P_(t mod 8), where sites are written left to right:

    phase    P_phase
      0      10011000100101
      1      11110101111101
      2      00000101000001
      3      00001101100011
      4      10011001010110
      5      11110111010101
      6      00000100010101
      7      00001110110101

**Finite premises, independently encoded controls.** The retained
`tests/probes/lexicon/rule30_train_p8_closure.py` checks all the following.
Literal Rule 30 lookup and packed Boolean updates agree. A shrinking
46-cell cone checks x_t(1) for 0 <= t <= 32 and the displayed band for
16 <= t <= 32. These checks need no assumption about sites beyond 46.
Every displayed row, with boundary phase mod 2, advances to the next
row for either exterior bit, except phase 4: there it does so exactly
when x_t(15) = 0. In particular column 14 reads 11110111, a rotation
of the one-white/seven-black wall.

**Causal lock, existing result.** If a cell reads 0111111101111111
at times a through a+15, its right neighbour is white at a+16,
whatever the five-cell starting state and whatever inputs arrive at the
sixth cell to its right. This is the n = 0 case of Local's
`tests/probes/lean/P8Lock.lean`, `p8_lock`; GC878 audits its causal
physical transfer. Only the sixteen specified wall bits are used.
To make the finite premise reproducible without a Lean installation,
start with all 32 five-bit states and repeatedly take the union of
both exterior-input successors, using these sixteen wall bits.
The successive image sizes are

    25,20,22,20,20,18,16,13,11,11,15,17,17,15,14,10.

The final image is exactly

    00000,00001,01000,01001,01010,
    01011,01100,01101,01110,01111.

Every member begins white. The probe reconstructs these exact sets
using independent literal and packed update implementations. Unioning
both inputs at every step covers every possible exterior sequence,
including exterior bits correlated with the interior. The eight-tick
image still contains a black-first state, so replacing sixteen by eight
in this argument fails its countercontrol. The established Lean theorem
was source-read; no new Lean compilation is claimed.

**Induction proving eternity.** The warmup supplies all rows from
16 through 32. Suppose the displayed band has held through time t,
where t >= 32. If t mod 8 is not 4, its last cell is black and masks
site 15; the finite transition table gives the correct band at t+1.
If t mod 8 is 4, then t >= 36 and a = t-16 >= 20. By the induction
hypothesis, site 14 on times a through t-1 is exactly two copies of
01111111. Apply the causal lock to sites 15..19, treating site 20 as
arbitrary at every update. It gives x_t(15) = 0, which is precisely
the missing condition for the phase-4 band transition. Thus the band
also advances correctly in this case. Strong induction proves the
band for all t >= 16. Its first cell has profile 11001100; the checked
warmup handles earlier times. This proves the claim.

**Unexpected stronger consequence.** The same conclusion holds for
*every* initial right half whose first 46 cells are 1001 followed by
42 zeros, with no restriction on the remaining tail. Finite speed
makes the warmup identical; the induction already allows every
subsequent exterior input. The probe checks zero and all-one finite
far-tail controls, but the universal-tail assertion follows from the
cone and the proof, not from those two tests. Neither periodicity nor
aperiodicity of site 15 is required or proved.

**Why the earlier window searches do not refute this.** Their failure
was closure of the particular sets sampled along the orbit. This proof
keeps a sixteen-tick boundary history and uses the exact five-cell
all-input lock; it never assumes that a sampled window set is closed.
The original first-macro gate at the 0111 boundary need not be invariant
(GC1018). The proof closes at the farther 01111111 boundary instead.

**Scope and credit.** Cloud's corrected fourteen-site observation
(CL187) identifies the useful boundary; Local's P8Lock supplies the
lock; GPT supplies the phase table and causal self-consistency induction.
The earlier seven-ring certificate (GC1013) realized the same visible
train with a periodic right tail; it did not prove this specified finite
right seed or the arbitrary-tail cylinder result. No finite left half
or all-depth record bound is constructed. `proof_dupes.py --near G271`
returned 03, C1, C2; all three read. Their white latch/checkerboard
rules and G271's black lock are antecedents, not the finite-seed
feedback induction proved here. Waiting-room referral only until
independent review; no new reviewed proof number is claimed.

**Filing check for waiting entry W282.** `proof_dupes.py --near W282`
returned G271, 10 and 37; all read in full. G271 contains the reused
P8 lock and its language consequence, but not this seed or feedback
induction. Entry 10 requires a leftmost black cell and bounds paired
repeats; entry 37 excludes constant columns in a nonzero finite global
seed. Neither applies to the imposed alternating boundary here. W282
is filed for review with its own summary; it is not yet a reviewed entry.

**Independent reviews (CL189 and L595, 2026-10-10).** Both reviewers
used their own implementations to reproduce the warmup, all eight band
transitions, the sixteen-tick all-input image and the failed eight-tick
control. Both accepted the strong induction and the arbitrary-tail
cylinder consequence. Local retained `rule30_gc1020_review.py`; Cloud's
review is in CL189. No assertion about site 15's full trace is needed.
The prior waiting-room wording above records the filing history; this
entry is now reviewed. Neither review claims a solution to Question 3.
