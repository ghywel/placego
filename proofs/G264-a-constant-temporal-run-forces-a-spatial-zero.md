# A constant temporal run forces a spatial zero wedge; a ring containing GC828's profile needs at least 14 cells

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT264. A constant temporal run forces
a spatial zero wedge; a ring containing GC828's profile needs at least 14 cells (second-read, 2026-10-09)"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In Rule 30's moving frame, a column that stays white for a while forces a growing wedge of white to its right.

**What it says.** If one column holds the same colour for L steps in a row, the columns to its right are pushed to white in a widening wedge: two columns lose one step each, then the next two another, and so on. At the start of the run, 2L - 2 cells to the right are white. On a ring this makes the ring at least 2L cells around, or the whole row would be white and stay white for ever.

**Why it matters.** It turns a property of one column into a hard constraint on its neighbours and on the size of any repeating pattern that contains it. For the template under study it means any ring containing it has at least 14 cells.

**An everyday picture.** A long pause in one drummer's part silences the drummers beside them for a shrinking stretch, like a shadow narrowing with distance.

## The formal statement and proof

*Where:* RULE30-GPT.md GC834. *Credit:* GPT's proof. Independently read by Local (chat L456). As a literal
corroboration, every imposed profile of TC's saved K = 4 and K = 6 witnesses has the predicted initial zeros in all
five blocks. *Status:* hand proof verified by a second reader. Not a prize claim. *Filed by:* Local, at GPT's request
(GC835).

**Lemma.** Let V0, V1, ... be consecutive G profiles, with $\Delta V_i = V_{i+1} \lor V_{i+2}$. If V0 is constant on
L consecutive ticks starting at t0, then for every 1 <= k <= L - 1 the profiles V1, ..., V_(2k) are 0 at ticks
t0 .. t0 + L - k - 1. In particular V_j has at least L - ceil(j/2) initial zeros, and the row at t0 has 2L - 2 zeros
right of V0.

**Proof.**
1. $\Delta V_0 = 0$ on the first L - 1 ticks, so V1 = V2 = 0 there.
2. If V1 .. V_(2k) vanish on the first L - k ticks, their differences vanish on the first L - k - 1. The equations
   for V_(2k-1) and V_(2k) then force V_(2k+1) = V_(2k+2) = 0 there. ∎

**Ring corollary.** Let the diagram be spatially periodic with period d, and V0 temporally periodic, nonconstant,
with a white run of length L. If d <= 2L - 1, the t0 row is all white, and G keeps it white, contradicting V0. So
d >= 2L. For GC828's D, L = 7, so d >= 14.
- For a black run, only d >= 2L - 1 follows: the zero wedge cannot wrap onto the black V0.
- Control: the five-phase ring (L = 1) gives d >= 2, consistent with its five cells.
- The bound concerns ring realizations containing D, not an eventual cycle reached through a bridge.

*Near-entry gate (Local, at filing).* `--near G264` gives G256, E3 and 06 (all <= 0.12 on the formal text), read; none
is restated.
