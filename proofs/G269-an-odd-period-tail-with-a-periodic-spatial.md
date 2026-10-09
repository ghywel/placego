# An odd-period tail with a periodic spatial parity mask has no hidden transient

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT269. An odd-period tail with a
periodic spatial parity mask has no hidden transient (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If the black-cell counts down the columns of a repeating stretch of Rule 30 follow a fixed repeating odd-even pattern, the stretch cannot have a lead-in: it repeats from its very first column.

**What it says.** Fix an odd time period. Each column then has exactly two possible left neighbours, one with an odd count of black cells and one with an even count. A prescribed odd-even pattern picks at most one of them. So every column has at most one possible predecessor, and a finite system in which every state has at most one predecessor and goes on for ever can only run in closed loops. A starting column of the kind that never has a predecessor therefore cannot begin such a stretch.

**Why it matters.** It removes one way the critical case could have hidden a lead-in, and it says what any real one would need: an odd-even pattern that does not repeat from the start.

**An everyday picture.** A one-way train line on which every station has only one incoming track: a train that runs for ever must be going round a loop, so it cannot have started at a terminus.

## The formal statement and proof

*Where:* RULE30-GPT.md GC846 (GC743's unique-incoming mechanism; GC816's odd-driver zero indegree; GC817's controls).
*Credit:* GPT's hand proof. Independently read by Local (chat L470). Checked literally on the full lifted graphs at
q = 1, 3, 5 for every mask of period 1 to 4: in-degree at most 1, the live set is disjoint cycles, no live pair has an
odd driver. The q = 2 countercontrol shows in-degree 2 and a transient. GC816's q = 5 ring has odd parities and even
pair drivers. *Status:* proved by hand. Not a prize claim. *Filed by:* Local.

**Statement.** Let q be odd, and let the G-frame column profiles V_0, V_1, ... (q-bit cyclic temporal words, with
ΔV_i = V_(i+1) OR V_(i+2)) have black parities p(V_i) = e_(i mod m) for a fixed mask e of period m. Then the pair
sequence (V_i, V_(i+1)) is purely periodic from i = 0. In particular, an odd-driver entry (D, U), one where D OR U
has odd weight, never begins a right tail whose parity mask is purely periodic from D.

**Proof (GC846).**
1. Lift the phase. Vertices are (r, X, Y) with r mod m, p(X) = e_r and p(Y) = e_(r+1). Edges go
   (r, X, Y) -> (r + 1, Y, Z) when ΔX = Y OR Z. There are at most m 2^(2q - 2) vertices.
2. A predecessor of (r, X, Y) is (r - 1, A, X) with ΔA = X OR Y. The solutions are none, or exactly A and NOT A. For
   odd q these have opposite parities, so e_(r - 1) admits at most one: every in-degree is at most 1.
3. Let L be the vertices with an infinite forward path. Each has an out-edge into L, and at most one in-edge. Counting
   the edges inside L gives at least |L| and at most |L|. So both degrees inside L are exactly 1, and L is a disjoint
   union of cycles. An infinite path from a vertex of L follows L's unique successors, so it is periodic from its first
   pair.
4. If (D, U) had odd driver and a purely periodic mask, it would lie on a cycle. That needs a predecessor with
   ΔA = D OR U, which has odd weight and so no cyclic solution. ∎

*Scope (GC846).* A mask that becomes periodic only after a transient is not excluded; the retained template stays
open. Even q is outside the lemma: at q = 2, the profiles 11, 00, 00, ... have constant parity and a transient. No
parity conservation, critical uniqueness, higher-period or prize result follows. The q = 310 branch is outside it.

*Machine-checked ingredients (Local, 2026-10-09 21:59 BST).* tests/probes/lean/ParityMask.lean (Lean 4, Mathlib; no
sorryAx) proves the ingredients:
- `live_has_pred`: step 3's degree count;
- `diff_eq_cases`: step 2's "none, or A and NOT A";
- `parity_compl` and `at_most_one_pred`: odd q flips parity, so the mask admits at most one predecessor;
- `diff_even` and `odd_driver_no_pred`: step 4's entry has no predecessor.
The glue, meaning the phase-lifted graph and its live set as Lean objects, is not formalized.

*Near-entry gate (Local, at filing).* `--near G269` gives C2, C1 and G63, all at formal similarity 0.05 or less
(different subjects). GC743's and GC816's mechanisms are not filed entries, so nothing is restated. Hard checks pass.
