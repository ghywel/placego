Rule30LeftCoincidence: the farther parent and the coincidence criterion of the left reset recurrence

This adds `lean/Ruliology/CellularAutomata/Rule30LeftCoincidence.lean`, with its `public import` in `lean/Ruliology.lean`
and a row in *Added in the kit*.

**What it proves.** `Rule30LeftReset` studies `x (t + 1) = a t ⊕ (b t ∨ x t)`: a child `x` driven by a nearer word `b`
and a farther word `a`. The left diagonals obey it (`Rule30Diagonals.D_step`: child `D (j + 2)`, nearer `D (j + 1)`,
farther `D j`). For arbitrary words in natural time:
- `closed_form` (F1): after a black of `b` at `r` and a white run of `b` on `(r, t]`, the child is the complemented
  parity of `a` over `r … t`.
- `farther_of_child`, `farther_unique`, `solutions_agree` (F2): `a t = x (t + 1) ⊕ (b t ∨ x t)` for any triple, so the
  farther word is determined by the child and the nearer word; two children of the same words agree after a black of `b`.
- `coincidence_iff` (F3): after a black of `b` at `s`, the child equals `b` from `s + 1` on iff `a` is the difference
  `b t ⊕ b (t + 1)` from `s` on. No periodicity is needed.
- `white_of_coincidence`, `evwhite_iff_eventually_eq` (Lemma E): if `a = b` from some time on, the child is white after
  the next black of `b`; so, when `b` has blacks arbitrarily late, the child is eventually white iff `a` and `b`
  eventually coincide. The forward way is the kit's `white_forces_eq`.
- The `D_` forms are the same for the left diagonals. With the kit's `D_white_of_eq`, a white `D (j + 3)` forces
  `D (j + 1) = D (j + 2)`, and after a black of `D (j + 1)` that holds iff `D j` is the difference of `D (j + 1)`.

**Checks**, on main c42f6e5 with Lean 4.35.0:
- `lake build Ruliology.CellularAutomata.Rule30LeftCoincidence`: no warnings. `lake build Ruliology`: completes
  (199 jobs).
- `lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30LeftCoincidence --claim partial` with the ten
  headlines `closed_form`, `farther_of_child`, `solutions_agree`, `coincidence_iff`, `white_of_coincidence`,
  `evwhite_iff_eventually_eq`, `D_closed_form`, `D_coincidence_iff`, `D_white_of_coincidence` and
  `D_evwhite_iff_eventually_eq`: `pass`. 37 constants are replayed, the official statements are imported, and there
  are no new axioms.
- Not run: the full catalog build (`bash build_all.sh`).
- Every declaration is in the new namespace `Ruliology.CellularAutomata.Rule30LeftCoincidence`.

**Credit and related work.**
- The lemmas were proposed in the contributors' record by Claude (Anthropic).
- The recurrence, its reset step and the accumulation are `Rule30LeftReset`'s (AIOvernight); `D_white_of_eq` and
  `white_forces_eq` are the forward direction used here. Rowland, "Local nested structure in rule 30" (Complex Systems
  16, 2006), §5, studies the same left diagonals.
- The portal submission is `R30-PENDING`: a map of the portal's partial results by object, with this module as its
  Lean content.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
