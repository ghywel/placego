import TwoPairsShortWindows
import TwoPairsShortPositive

/-! The seven ten-cell words that force perpetual three-cell backward motion
of an equal top pair. Even an anchored physical row supplies a counterexample
for every other ten-cell word; the nine-cell exclusions are in ShortWindows. -/
namespace TwoPairs.Shortest
open WindowExclusions ShortWindows

/-- Both eleven-cell extensions of each of the seven are among the eighteen
robust windows or the six certified entrances. -/
theorem ten_extensions : ∀ k, k ∈ tenRetained →
    (false :: tenWord k ∈ B11 ++ Six.fast ++ Six.slow) ∧
    (true :: tenWord k ∈ B11 ++ Six.fast ++ Six.slow) := by decide +kernel

/-- For a retained ten-cell word the edge colour can be arbitrary. -/
theorem ten_forever (i : Fin 512) (h : i.val ∈ tenRetained)
    (x : Row) (L : Nat) (hw : seg x L 10 = tenWord i.val) (ht : Top x (L+8)) (r : Nat) :
    Top (previousN x r) (L+8+3*r) := by
  obtain ⟨lo,hi⟩ := ten_extensions _ h
  exact ShortPositive.both_extensions _ lo hi x L hw ht r

/-- Exact ten-cell classification on rows anchored by a black edge. -/
theorem ten_iff_anchored (i : Fin 512) : i.val ∈ tenRetained ↔
    ∀ (x : Row) (L : Nat), x 0 = true → seg x L 10 = tenWord i.val →
      Top x (L+8) → ∀ r, Top (previousN x r) (L+8+3*r) := by
  constructor
  · intro h x L _ hw ht r
    exact ten_forever i h x L hw ht r
  · intro h
    by_cases hmem : i.val ∈ tenRetained
    · exact hmem
    · obtain ⟨x,L,r,_,_,black,hw,ht,miss⟩ := ten_exclusion i hmem
      exact False.elim (miss (h x L black hw ht r))

/-- The same seven and only those seven work over all physical rows. -/
theorem ten_iff (i : Fin 512) : i.val ∈ tenRetained ↔
    ∀ (x : Row) (L : Nat), seg x L 10 = tenWord i.val →
      Top x (L+8) → ∀ r, Top (previousN x r) (L+8+3*r) := by
  constructor
  · exact ten_forever i
  · intro h
    exact (ten_iff_anchored i).mpr (fun x L _ hw ht r => h x L hw ht r)

#print axioms ten_iff_anchored
#print axioms ten_iff
end TwoPairs.Shortest
