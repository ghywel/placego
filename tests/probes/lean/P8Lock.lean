import Mathlib

/-!
# The one-hole wall 0 1^7 (p = 8) closes at width five (Local, 2026-10-09; chat L495, L496)

Five cells x1 .. x5 right of a column reading 0 1^7 periodically, with a free outside bit beyond x5 at every step.
A macro is one white step (the wall is 0) followed by seven black steps (the wall is 1). The hole symbol is x1 at
each white tick. `p8_lock`: after two or more macros from any state, with any outside bits, x1 = 0. So the hole word
is 0 at every hole from the third on, and the relaxed hole language has three words of each length: 0^n, 1 0^(n-1)
and 0 1 0^(n-2). Every actual right half restricts to these paths.

How to check: as for BlackLock.lean; the `#print axioms` lines must list no `sorryAx`.
-/

namespace P8Lock

abbrev S5 := Bool × Bool × Bool × Bool × Bool

/-- One step next to the wall bit `w`, with outside bit `u`. -/
def stp (w : Bool) (s : S5) (u : Bool) : S5 :=
  let (x1, x2, x3, x4, x5) := s
  (xor w (x1 || x2), xor x1 (x2 || x3), xor x2 (x3 || x4), xor x3 (x4 || x5), xor x4 (x5 || u))

/-- One macro: a white step, then seven black steps, with outside bits `us 0 .. us 7`. -/
def mac (s : S5) (us : Fin 8 → Bool) : S5 :=
  stp true (stp true (stp true (stp true (stp true (stp true (stp true (stp false s (us 0)) (us 1)) (us 2))
    (us 3)) (us 4)) (us 5)) (us 6)) (us 7)

def allS5 : List S5 :=
  [false, true].flatMap fun a => [false, true].flatMap fun b => [false, true].flatMap fun c =>
    [false, true].flatMap fun d => [false, true].map fun e => (a, b, c, d, e)

/-- The exact image of a list under one step with every outside bit. -/
def img (w : Bool) (L : List S5) : List S5 := (L.flatMap fun t => [stp w t false, stp w t true]).dedup

/-- The exact image of a list under one macro. -/
def macroL (L : List S5) : List S5 :=
  img true (img true (img true (img true (img true (img true (img true (img false L)))))))

def reachM : ℕ → List S5
  | 0 => allS5
  | n + 1 => macroL (reachM n)

lemma mem_all (s : S5) : s ∈ allS5 := by
  obtain ⟨a, b, c, d, e⟩ := s
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

lemma mem_img {w : Bool} {L : List S5} {t : S5} (u : Bool) (h : t ∈ L) : stp w t u ∈ img w L := by
  simp only [img, List.mem_dedup, List.mem_flatMap]
  exact ⟨t, h, by cases u <;> simp⟩

lemma mem_macroL {L : List S5} {t : S5} (us : Fin 8 → Bool) (h : t ∈ L) : mac t us ∈ macroL L := by
  unfold mac macroL
  exact mem_img _ (mem_img _ (mem_img _ (mem_img _ (mem_img _ (mem_img _ (mem_img _ (mem_img _ h)))))))

lemma img_mono {w : Bool} {L L' : List S5} (h : ∀ t ∈ L, t ∈ L') : ∀ t ∈ img w L, t ∈ img w L' := by
  intro t ht
  simp only [img, List.mem_dedup, List.mem_flatMap] at ht ⊢
  obtain ⟨a, ha, hta⟩ := ht
  exact ⟨a, h a ha, hta⟩

lemma macroL_mono {L L' : List S5} (h : ∀ t ∈ L, t ∈ L') : ∀ t ∈ macroL L, t ∈ macroL L' := by
  unfold macroL
  exact img_mono (img_mono (img_mono (img_mono (img_mono (img_mono (img_mono (img_mono h)))))))

set_option maxRecDepth 100000 in
/-- After two macros every reachable state has x1 = 0. -/
lemma reach2_white : ∀ t ∈ reachM 2, t.1 = false := by
  decide

set_option maxRecDepth 100000 in
/-- The set after two macros is invariant: a third macro stays inside it. -/
lemma reach3_sub : ∀ t ∈ reachM 3, t ∈ reachM 2 := by
  decide

lemma reach_sub (n : ℕ) : ∀ t ∈ reachM (n + 2), t ∈ reachM 2 := by
  induction n with
  | zero => intro t ht; exact ht
  | succ n ih =>
    intro t ht
    have h1 : ∀ t ∈ reachM (n + 3), t ∈ reachM 3 := macroL_mono ih
    exact reach3_sub t (h1 t ht)

/-- The orbit under a sequence of macros with outside-bit blocks `us 0, us 1, ...`. -/
def orbit (s : S5) (us : ℕ → Fin 8 → Bool) : ℕ → S5
  | 0 => s
  | n + 1 => mac (orbit s us n) (us n)

lemma orbit_mem (s : S5) (us : ℕ → Fin 8 → Bool) (n : ℕ) : orbit s us n ∈ reachM n := by
  induction n with
  | zero => exact mem_all s
  | succ n ih => exact mem_macroL (us n) ih

/-- The wall 0 1^7: from the third hole on, the hole symbol is white. -/
theorem p8_lock (s : S5) (us : ℕ → Fin 8 → Bool) (n : ℕ) : (orbit s us (n + 2)).1 = false :=
  reach2_white _ (reach_sub n _ (orbit_mem s us (n + 2)))

end P8Lock

#print axioms P8Lock.p8_lock
