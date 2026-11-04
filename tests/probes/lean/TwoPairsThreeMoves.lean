import TwoPairsRetreat
import TwoPairsSixCertificate

/-! After three actual backward advances of three cells, the deepest
top window must be one of two words in the original eighteen. -/
namespace TwoPairs.ThreeMoves
open WindowTransport

def wordA : List Bool := [false,false,true,true,true,true,false,false,false,true,true]
def wordB : List Bool := [false,true,false,true,true,true,false,false,false,true,true]
private def mark : List Bool := [true,false,false,false,true,true]

private theorem known : wordA ∈ B11 ∧ wordB ∈ B11 := by decide +kernel

/-- Three forward retreat markers, displaced three cells at each step.
The ten free lower bits suffice for all three observations by exact locality. -/
set_option maxRecDepth 8192 in
set_option maxHeartbeats 1200000 in
private theorem local_cut : ∀ c, c ∈ Six.contexts 10 →
    (((shrink (c ++ mark)).drop 5).take 6 = mark) →
    ((shrinkN (c ++ mark) 2).take 6 = mark) →
    (c ++ mark).drop 5 = wordA ∨ (c ++ mark).drop 5 = wordB := by decide +kernel

private theorem slice_seg (x : Row) (L a m b : Nat) :
    ((seg x L (a+(m+b))).drop a).take m = seg x (L+a) m := by
  rw [seg_append x a (m+b) L, List.drop_left' (seg_length x a L),
    seg_append x m b (L+a), List.take_left' (seg_length x m (L+a))]

theorem deep_words (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) :
    seg z D 11 = wordA ∨ seg z D 11 = wordB := by
  obtain ⟨k, rfl⟩ : ∃ k, D=k+5 := ⟨D-5, by omega⟩
  have m0 := Retreat.marker (k+9) a b
  have m1 := Retreat.marker (k+6) b c
  have m2 := Retreat.marker (k+3) c d
  let low := seg z k 10
  have whole : low ++ mark = seg z k 16 := by
    rw [seg_append z 10 6 k, m0]
  have context : low ∈ Six.contexts 10 := by
    simpa only [low, seg_length] using Six.mem_contexts (seg z k 10)
  have p1 : ((shrink (low ++ mark)).drop 5).take 6 = mark := by
    rw [whole, shrink_seg z k 14, slice_seg (step z) (k+2) 5 6 3]
    exact m1
  have p2 : (shrinkN (low ++ mark) 2).take 6 = mark := by
    rw [whole, shrinkN_seg z k 2 12, seg_append (iter z 2) 6 6 (k+4),
      List.take_left' (seg_length (iter z 2) 6 (k+4))]
    exact m2
  have choices := local_cut low context p1 p2
  rw [whole, seg_append z 5 11 k, List.drop_left' (seg_length z 5 k)] at choices
  exact choices

theorem deep (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) : Front z D := by
  have choices := deep_words z D hD a b c d
  refine ⟨?_, a.2⟩
  rcases choices with w | w
  · rw [w]; exact known.1
  · rw [w]; exact known.2

#print axioms deep_words
end TwoPairs.ThreeMoves
