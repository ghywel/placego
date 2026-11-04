import TwoPairsWindowClassification

/-! Projection removes low cells, keeping the same top wall. The free low
bit for length ten, and both free low bits for length nine, are quantified
over actual anchored exclusions from the eleven-bit classification. -/
namespace TwoPairs.ShortWindows
open WindowExclusions WindowClassification

def tenWord (i : Nat) : List Bool := (digits (word (2*i))).drop 1
def nineWord (i : Nat) : List Bool := (digits (word (4*i))).drop 2

/-- Compressed equal-top indices. The corresponding ten-bit encodings are
778, 790, 798, 842, 854, 862, and 946. -/
def tenRetained : List Nat := [266,278,286,330,342,350,434]

set_option maxRecDepth 8192 in
theorem ten_fibres : ∀ i : Fin 512,
    (i.val ∈ tenRetained ↔ word (2*i.val) ∈ retained ∧ word (2*i.val+1) ∈ retained) ∧
    (digits (word (2*i.val+1))).drop 1 = tenWord i.val := by decide +kernel

theorem ten_count : tenRetained.length = 7 ∧ tenRetained.Nodup := by decide +kernel

set_option maxRecDepth 8192 in
private theorem nine_bad_fibre : ∀ i : Fin 256, ∃ b : Fin 4,
    word (4*i.val+b.val) ∉ retained ∧
    (digits (word (4*i.val+b.val))).drop 2 = nineWord i.val := by decide +kernel

theorem segment_suffix (x : Row) (L d m : Nat) :
    (seg x L (d+m)).drop d = seg x (L+d) m := by
  rw [seg_append x d m L, List.drop_left' (seg_length x d L)]

/-- A physical witness of failure to sustain the expected +3 motion. -/
def Failure (m : Nat) (w : List Bool) : Prop :=
  ∃ (x : Row) (L r : Nat), 1 ≤ r ∧ r ≤ 3 ∧ x 0 = true ∧
    seg x L m = w ∧ Top x (L+(m-2)) ∧ ¬Top (previousN x r) (L+(m-2)+3*r)

/-- The same physical witness refutes every suffix ending in the same top pair. -/
theorem suffix_failure {w : List Bool} (d m : Nat) (hm : 2 ≤ m)
    (bad : Failure (d+m) w) : Failure m (w.drop d) := by
  obtain ⟨x,L,r,h1,h3,hx,hw,wall,fail⟩ := bad
  have pos : L+(d+m-2) = (L+d)+(m-2) := by omega
  rw [pos] at wall fail
  exact ⟨x,L+d,r,h1,h3,hx,by rw [← hw, segment_suffix],wall,fail⟩

private theorem eleven_failure (i : Fin 1024) (off : word i.val ∉ retained) :
    Failure 11 (digits (word i.val)) := physical_exclusion i off

theorem ten_exclusion (i : Fin 512) (outside : i.val ∉ tenRetained) :
    Failure 10 (tenWord i.val) := by
  have small := i.isLt
  obtain ⟨both, shift⟩ := ten_fibres i
  by_cases even : word (2*i.val) ∈ retained
  · have off : word (2*i.val+1) ∉ retained := fun odd => outside (both.mpr ⟨even, odd⟩)
    let idx : Fin 1024 := ⟨2*i.val+1, by omega⟩
    have f := suffix_failure 1 10 (by decide) (eleven_failure idx off)
    change Failure 10 ((digits (word (2*i.val+1))).drop 1) at f
    rwa [shift] at f
  · let idx : Fin 1024 := ⟨2*i.val, by omega⟩
    exact suffix_failure 1 10 (by decide) (eleven_failure idx even)

theorem nine_exclusion (i : Fin 256) : Failure 9 (nineWord i.val) := by
  obtain ⟨b,off,shift⟩ := nine_bad_fibre i
  have hi := i.isLt
  have hb := b.isLt
  let idx : Fin 1024 := ⟨4*i.val+b.val, by omega⟩
  have f := suffix_failure 2 9 (by decide) (eleven_failure idx off)
  change Failure 9 ((digits (word (4*i.val+b.val))).drop 2) at f
  rwa [shift] at f

theorem nine_and_shorter (i : Fin 256) (d m : Nat) (hm : 2 ≤ m) (len : d+m=9) :
    Failure m ((nineWord i.val).drop d) :=
  suffix_failure d m hm (len.symm ▸ nine_exclusion i)

#print axioms ten_exclusion
#print axioms nine_and_shorter
end TwoPairs.ShortWindows
