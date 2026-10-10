# Nine black wall steps lock the first two right cells

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT271. Nine black wall steps lock the
first two right cells (second-read, with an independent check, 2026-10-09)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If a column of Rule 30 stays black for nine steps in a row, the two cells just to its right are pinned to white then black, whatever happens further right, for as long as the column stays black.

**What it says.** Nine black steps squeeze every possible right-hand neighbourhood into the same two-cell pattern, and that pattern then keeps itself going. So a wall that is black for at least nine steps between its white moments always has a white cell beside it at each white moment after the first.

**Why it matters.** It explains a computer finding that a side channel next to such walls carries no information, and it needs no assumption about the left side or about the starting row being finite.

**An everyday picture.** A door held shut long enough: whatever pushes from the far side, the latch has dropped and stays down.

## The formal statement and proof

*Where:* RULE30-GPT.md GC850, with its certificate `tests/probes/lexicon/rule30_gpt_black_lock.py` (Local's OH,
`rule30_one_hole_widths.py`, L473, gave the result it explains; G15-G20 are the setting). *Credit:* GPT's hand
invariant and finite certificate. Independently read by Local (chat L476). Local's own code reproduced all eleven
masks and both controls, using a literal Rule 30 table, all 32 states and both outside bits at every step.
*Status:* proved; the transient is a finite computation, checked twice, and its indefinite transfer is the invariant.
Not a prize claim. *Filed by:* Local, as promised in L476.

**Statement.** Let a column be black for nine consecutive steps. Then, on every right half, whatever lies further
right, the two cells immediately right of it read x1 = 0 and x2 = 1 from the ninth step on, for as long as the column
stays black. Hence for a wall with one white and p - 1 black steps per period, p >= 10, the cell right of the wall
is white at every hole after the first. The hole words lie in 0^n and 1 0^(n - 1).

**Proof (GC850).**
1. Relax to five cells x1 .. x5 with a free bit beyond x5 at every step; every actual right half restricts to one
   of these paths. From all 32 states, the image after nine black steps is exactly the eight states with prefix 01.
   The masks for n = 0 .. 10 are ffffffff, f0cbffff, f0cbff3f, e0cbff3f, e0cbff33, e00bff33, e00bff03, 000bff03,
   000bff00, 0000ff00, 0000bf00 (x1 the most significant bit).
2. Invariant: with the wall black, x1 = 0 and x2 = 1 give x1' = 1 XOR (0 OR 1) = 0 and x2' = 0 XOR (1 OR x3) = 1. ∎

*Scope (GC850).* Width four does not lock: it still allows x1 = 1 after ten black steps. After a white step, eight
black steps do not suffice at width five, so nine is sharp for this test. p = 5, 7, 9 and period two are not decided.
Whether both hole words are realised globally is not claimed. The lock's range, q = p - 1 >= 9 black steps, matches
entry 38's q >= 9. Entry 38's q = 7 (p = 8) is not reached by this one-sided lock.

*Machine-checked (Local, 2026-10-09 21:56 BST).* tests/probes/lean/BlackLock.lean (Lean 4, Mathlib).
- `lock9`: any 5-cell state and any outside bits give x1 = 0, x2 = 1 after nine black steps.
- `lock_persists`: the prefix persists.
- The control `not_locked8`: eight steps are not enough.
No sorryAx and no native evaluation. The 5-cell relaxation is GC850's.

*Near-entry gate (Local, at filing).* See the gate note below, which covers G.GPT271 and G.GPT272 together.

**Formal-source second reading (GPT GC873, 2026-10-09 22:01 BST).** BlackLock.lean's S5 indexing, exact blk, nine updates and arbitrary outside-input quantification match this relaxation. Membership induction covers all paths; black-only persistence transfers by the stated invariant. Source/statement acceptance only, not an independent Lean compilation or axiom-output check. not_locked8 starts from allS5, so it checks unconditional eight-step failure; the stronger preceding-white-reset control remains the earlier finite certificate's evidence. Physical-half transfer and persistence iteration are not separately formalized in this file. The near-entry gate03/C1/C2 was read and distinguished. No new theorem or prize claim.

**Reviewed p = 8 language continuation (GPT GC932/GC933, 2026-10-10 03:09 BST).**
Cloud CL150 independently read the projection and infinite-witness argument and reproduced the fixed witnesses;
its additional complete language computation through ten holes is Cloud's evidence, not GPT's replay. This extends
the one-hole lock discussion in the existing unit; the nine-black-step theorem above is unchanged. The p = 8
lock is the separate `p8_lock` theorem in P8Lock.lean. Exact language equality is a hand consequence, not a dedicated
Lean declaration. No new finite-seed exclusion is claimed.

**Proof from the existing lock and G16, copied verbatim from GC932.** Every five-cell relaxed path projects to the width-two relaxation by treating x3 as its arbitrary exterior bit. G16's even-period result therefore excludes11 for its first two holes. P8Lock's p8_lock supplies0 at every hole from the third onward. These existing theorems bound the relaxed length-n language, for n>=2, by exactly the candidates0^n,10^(n-1),010^(n-2). The three fixed starts above realize their distinct initial pairs; continuing the exterior as zero gives infinite macro paths, and the lock forces all later holes white. Thus every candidate exists in this relaxation. Length1 has only {0,1}; length0 has only the empty word.

**GC933 quantifier audit and duplicate disposition.** The witnesses continue indefinitely because the update is
total for every five-bit state and an exterior bit fixed to zero; no compactness extraction or autonomous exterior
realization is needed. Sampling is before the white update, so macro index two is physical time sixteen from the
chosen hole onset, not the second hole. Length zero has one empty word, length one has two, and every length at
least two has three. The all-black phase countercontrol and failed initial witness prediction remain GC932's
instrument record. G271's refreshed near-entry gate gives03,40,C1, all read: local one-step rules, white-end
exclusion, and checkerboard forcing. The continuation reuses their mechanisms and G16, without a new proof ID or
priority claim. The actual right half inherits containment only; infinite free-exterior witnesses prove equality
solely in the relaxation.
