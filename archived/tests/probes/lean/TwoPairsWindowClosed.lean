import TwoPairsThreeMoves

/-!
# Closed sets of windows at the wall

A set `S` of words of `W` cells is *closed* when each word, with rain above it, goes to a word of `S` under the backward tick for
every pair of lower cells, three cells higher, with rain above again. A row showing a word of a closed set at its top then shows
words of `S` at every backward tick for ever, whatever lies below (`held_forever`). The checks are finite, so each closed set is
one `decide`. The theorem is general; the sets are in the modules that import this one.
-/

namespace TwoPairs.WindowClosed

/-- A window with seven cells of rain over its last. -/
def inp (W : Nat) (w : List Bool) : List Bool := w.take (W - 1) ++ alt (w.getD (W - 1) false) 7

/-- The image of a window under the backward tick with lower cells `p1`, `p2`. -/
def next (W : Nat) (w : List Bool) (p1 p2 : Bool) : List Bool := ((back p1 p2 (inp W w)).drop 3).take W

/-- The finite checks. -/
structure Closed (W : Nat) (S : List (List Bool)) : Prop where
  pos : 1 ≤ W
  mem : ∀ w, w ∈ S → ∀ p1 p2 : Bool, next W w p1 p2 ∈ S
  a : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 3) false = !(back p1 p2 (inp W w)).getD (W + 2) false
  d : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(back p1 p2 (inp W w)).getD (W + 3) false
  b : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(inp W w).getD (W + 4) false
  c : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 5) false = !(inp W w).getD (W + 5) false

/-- A row with its window of `W` cells from `L` in `S` and rain above it. -/
def Held (W : Nat) (S : List (List Bool)) (x : Row) (L : Nat) : Prop :=
  seg x L W ∈ S ∧ ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j

theorem seg_inp {W : Nat} (hW : 1 ≤ W) {x : Row} {L : Nat} (h : ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j) :
    seg x L (W + 6) = inp W (seg x L W) := by
  have e1 : seg x L W = seg x L (W - 1) ++ seg x (L + (W - 1)) 1 := by
    have := seg_append x (W - 1) 1 L
    rwa [show W - 1 + 1 = W by omega] at this
  have e2 : (seg x L W).take (W - 1) = seg x L (W - 1) := by
    rw [e1]; exact List.take_left' (seg_length x (W - 1) L)
  have e3 : (seg x L W).getD (W - 1) false = x (L + (W - 1)) := seg_getD x W L (W - 1) (by omega)
  show seg x L (W + 6) = (seg x L W).take (W - 1) ++ alt ((seg x L W).getD (W - 1) false) 7
  rw [e2, e3, ← seg_alt (J := L + (W - 1)) (fun j hj => h j (by omega)) 7 (L + (W - 1)) (Nat.le_refl _)]
  have := seg_append x (W - 1) 7 L
  rwa [show W - 1 + 7 = W + 6 by omega] at this

private theorem seg_next (W : Nat) {z : Row} {L : Nat} :
    seg z (L + 3) W = ((seg z L (W + 6)).drop 3).take W := by
  have e1 : seg z L (W + 6) = seg z L 3 ++ seg z (L + 3) (W + 3) := by
    have := seg_append z 3 (W + 3) L
    rwa [show 3 + (W + 3) = W + 6 by omega] at this
  have e2 : seg z (L + 3) (W + 3) = seg z (L + 3) W ++ seg z (L + 3 + W) 3 := seg_append z W 3 (L + 3)
  rw [e1, List.drop_left' (seg_length z 3 L), e2]
  exact (List.take_left' (seg_length z W (L + 3))).symm

/-- One tick, on rows. -/
theorem next_seg {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : seg z (L + 3) W = next W (seg x L W) (z (L - 1)) (z (L - 2)) := by
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp C.pos hf.2]
  rw [seg_next, e]; rfl

/-- **The tick.** Every predecessor of a held row is held three cells higher, whatever lies below the window. -/
theorem held_back {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : Held W S z (L + 3) := by
  have hW := C.pos
  obtain ⟨hw, hr⟩ := id hf
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp hW hr]
  have ha := C.a _ hw (z (L - 1)) (z (L - 2))
  have hb := C.b _ hw (z (L - 1)) (z (L - 2))
  have hc := C.c _ hw (z (L - 1)) (z (L - 2))
  have hd := C.d _ hw (z (L - 1)) (z (L - 2))
  have hm := C.mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd
  have g : ∀ i, i < W + 6 → (seg z L (W + 6)).getD i false = z (L + i) := fun i h => seg_getD z (W + 6) L i h
  rw [g (W + 2) (by omega), g (W + 3) (by omega)] at ha
  rw [g (W + 3) (by omega), g (W + 4) (by omega)] at hd
  rw [g (W + 4) (by omega)] at hb
  rw [g (W + 5) (by omega)] at hc
  have q : ∀ i, i < W + 6 → (inp W (seg x L W)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hW hr]; exact seg_getD x (W + 6) L i h
  rw [q (W + 4) (by omega)] at hb
  rw [q (W + 5) (by omega)] at hc
  refine ⟨by rw [next_seg C hL hs hf]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + (W + 4)) (fun j hj => hr j (by omega)) hb
    (by rw [show L + (W + 4) + 1 = L + (W + 5) by omega]; exact hc)
  intro j hj
  by_cases c1 : j = L + (W + 2)
  · subst c1; exact ha
  · by_cases c2 : j = L + (W + 3)
    · subst c2; exact hd
    · exact htail j (by omega)

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher. -/
theorem held_forever {W : Nat} {S : List (List Bool)} (C : Closed W S) {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W S x L) :
    ∀ n z, iter z n = x → Held W S z (L + 3 * n) := by
  intro n
  induction n with
  | zero => intro z hz; rw [show iter z 0 = z from rfl] at hz; subst hz; exact h
  | succ n ih =>
    intro z hz
    have e : iter z (1 + n) = iter (iter z 1) n := iter_add z 1 n
    rw [Nat.add_comm n 1, e] at hz
    have := held_back C (by omega) (show step z = iter z 1 from rfl) (ih (iter z 1) hz)
    have e2 : L + 3 * n + 3 = L + 3 * (n + 1) := by omega
    rw [e2] at this
    exact this

#print axioms held_back
#print axioms held_forever
end TwoPairs.WindowClosed
