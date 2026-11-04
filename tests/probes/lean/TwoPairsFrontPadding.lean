import TwoPairsEntrances

/-!
# The robust window starting at physical cell 0 or 1

The boundary rule amounts to white cells below index zero. Two explicit white
cells let us use `front_back` with its required two lower cells, including
when the original window starts at the edge. The padded row has a white edge.
This use is legitimate because `front_back` applies to rows of either colour.
-/

namespace TwoPairs.FrontPadding

private def white (x : Row) : Row
  | 0 => false
  | i + 1 => x i

private theorem step_white (x : Row) : step (white x) = white (step x) := by
  funext j
  cases j with
  | zero => rfl
  | succ j =>
    cases j with
    | zero => cases h : x 0 <;> simp [step, white, h]
    | succ j =>
      cases j with
      | zero => cases h : x 0 <;> simp [step, white, h]
      | succ j => rfl

def padTwo (x : Row) : Row := white (white x)

theorem step_padTwo (x : Row) : step (padTwo x) = padTwo (step x) := by
  simp only [padTwo, step_white]

theorem iter_padTwo (x : Row) (t : Nat) : iter (padTwo x) t = padTwo (iter x t) := by
  induction t with
  | zero => rfl
  | succ t ih =>
    show step (iter (padTwo x) t) = padTwo (step (iter x t))
    rw [ih, step_padTwo]

private theorem seg_white (x : Row) (n L : Nat) : seg (white x) (L + 1) n = seg x L n := by
  induction n generalizing L with
  | zero => rfl
  | succ n ih =>
    change x L :: seg (white x) (L + 1 + 1) n = x L :: seg x (L + 1) n
    rw [ih (L + 1)]

private theorem front_white (x : Row) (L : Nat) : Front (white x) (L + 1) ↔ Front x L := by
  constructor
  · intro ⟨w, h⟩
    refine ⟨(seg_white x 11 L) ▸ w, ?_⟩
    intro j hj
    exact h (j + 1) (by omega)
  · intro ⟨w, h⟩
    refine ⟨by rw [seg_white]; exact w, ?_⟩
    intro j hj
    obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
    exact h i (by omega)

theorem front_padTwo (x : Row) (L : Nat) : Front (padTwo x) (L + 2) ↔ Front x L :=
  (front_white (white x) (L + 1)).trans (front_white x L)

/-- Backward closure by exactly three cells, including windows at zero and one. -/
theorem front_back_all {z x : Row} {L : Nat} (hs : step z = x) (f : Front x L) :
    Front z (L + 3) := by
  have hs' : step (padTwo z) = padTwo x := by rw [step_padTwo, hs]
  have lifted := front_back (by omega : 2 ≤ L + 2) hs' ((front_padTwo x L).2 f)
  exact (front_padTwo z (L + 3)).1 lifted

def Robust (x : Row) : Prop := ∃ L, Front x L

def Entrance (x : Row) : Prop := Robust x ∧ ¬Robust (step x)

theorem robust_padTwo (x : Row) : Entrances.Robust (padTwo x) ↔ Robust x := by
  constructor
  · intro ⟨M, hM, f⟩
    obtain ⟨L, rfl⟩ : ∃ L, M = L + 2 := ⟨M - 2, by omega⟩
    exact ⟨L, (front_padTwo x L).1 f⟩
  · intro ⟨L, f⟩
    exact ⟨L + 2, by omega, (front_padTwo x L).2 f⟩

theorem entrance_padTwo (x : Row) : Entrances.Entrance (padTwo x) ↔ Entrance x := by
  simp only [Entrances.Entrance, step_padTwo, robust_padTwo, Entrance]

theorem reaches_entrance {x : Row} {L : Nat} (f : Front x L) :
    ∃ t, 3 * t ≤ L ∧ Entrance (iter x t) := by
  obtain ⟨t, ht, e⟩ := Entrances.reaches_entrance (by omega : 2 ≤ L + 2) ((front_padTwo x L).2 f)
  rw [iter_padTwo] at e
  exact ⟨t, by omega, (entrance_padTwo _).1 e⟩

theorem entrance_time_unique {x : Row} {s t : Nat} (hs : Entrance (iter x s))
    (ht : Entrance (iter x t)) : s = t := by
  have es := (entrance_padTwo _).2 hs
  have et := (entrance_padTwo _).2 ht
  rw [← iter_padTwo] at es et
  exact Entrances.entrance_time_unique es et

theorem entrance_iff {x : Row} {L : Nat} (f : Front x (L + 3)) :
    Entrance x ↔ ¬Front (step x) L := by
  have hf := (front_padTwo x (L + 3)).2 f
  have test := Entrances.entrance_iff (by omega : 2 ≤ L + 2) hf
  rw [step_padTwo, front_padTwo, entrance_padTwo] at test
  exact test

theorem shallow_entrance {x : Row} {L : Nat} (low : L < 3) (f : Front x L) :
    Entrance x := by
  exact (entrance_padTwo _).1
    (Entrances.shallow_entrance (by omega : 2 ≤ L + 2) (by omega) ((front_padTwo x L).2 f))

/-- On anchored rows the inverse sends the entire level L exactly onto the
non-entrances at L+3. This includes L=0, at which the anchor lies in the window. -/
theorem previous_image {x : Row} {L : Nat} :
    (x 0 = true ∧ Front x (L + 3) ∧ ¬Entrance x) ↔
      ∃ y : Row, y 0 = true ∧ Front y L ∧ Entrances.previous y = x := by
  constructor
  · intro ⟨black, f, h⟩
    have g : Front (step x) L := by
      apply Classical.byContradiction
      exact fun ng => h ((entrance_iff f).2 ng)
    exact ⟨step x, black, g, Entrances.previous_step x⟩
  · intro ⟨y, black, g, eq⟩
    subst x
    refine ⟨black, front_back_all (Entrances.step_previous y) g, ?_⟩
    intro e
    apply e.2
    rw [Entrances.step_previous]
    exact ⟨L, g⟩

end TwoPairs.FrontPadding
