import Mathlib

/-!
# The nine-step black lock (G.GPT271, GPT's GC850), machine-checked (Local, 2026-10-09)

Five cells x1 .. x5 right of a column that stays black, with a free outside bit u beyond x5 at every step. One Rule 30
step: x1' = 1 xor (x1 or x2), xj' = x(j-1) xor (xj or x(j+1)) for j = 2 .. 4, x5' = x4 xor (x5 or u).
`lock9`: from any state, after nine steps with any outside bits, x1 = 0 and x2 = 1.
`lock_persists`: the prefix x1 = 0, x2 = 1 survives every further black step, whatever x3 .. x5 and u are.
Every actual right half restricts to these paths (the relaxation only adds freedom), so a column black for nine
steps has a white then a black cell beside it from then on.

How to check: as for RootedReturn.lean (`lake env lean LocalScratch/BlackLock.lean` in the formal-conjectures
checkout); the `#print axioms` lines must list no `sorryAx` and no `Lean.ofReduceBool`.
-/

namespace BlackLock

/-- The five cells nearest a black column. -/
abbrev S5 := Bool × Bool × Bool × Bool × Bool

/-- One step beside a black column, with outside bit `u`. -/
def blk (s : S5) (u : Bool) : S5 :=
  let (x1, x2, x3, x4, x5) := s
  (xor true (x1 || x2), xor x1 (x2 || x3), xor x2 (x3 || x4), xor x3 (x4 || x5), xor x4 (x5 || u))

/-- Nine steps with outside bits `us 0 .. us 8`, written out. -/
def run9 (s : S5) (us : Fin 9 → Bool) : S5 :=
  blk (blk (blk (blk (blk (blk (blk (blk (blk s (us 0)) (us 1)) (us 2)) (us 3)) (us 4)) (us 5)) (us 6)) (us 7)) (us 8)

/-- All 32 states. -/
def allS5 : List S5 :=
  (([false, true].flatMap fun a => [false, true].flatMap fun b => [false, true].flatMap fun c =>
    [false, true].flatMap fun d => [false, true].map fun e => (a, b, c, d, e)))

/-- The exact image of all states after `n` steps, with every outside bit allowed. -/
def reach : ℕ → List S5
  | 0 => allS5
  | n + 1 => ((reach n).flatMap fun t => [blk t false, blk t true]).dedup

lemma mem_all (s : S5) : s ∈ allS5 := by
  obtain ⟨a, b, c, d, e⟩ := s
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

lemma mem_step {n : ℕ} {t : S5} (u : Bool) (h : t ∈ reach n) : blk t u ∈ reach (n + 1) := by
  simp only [reach, List.mem_dedup, List.mem_flatMap]
  exact ⟨t, h, by cases u <;> simp⟩

set_option maxRecDepth 100000 in
lemma reach9_locked : ∀ t ∈ reach 9, t.1 = false ∧ t.2.1 = true := by
  decide

set_option maxRecDepth 100000 in
/-- Control: eight steps are not enough (some reachable state still has x1 = 1). -/
lemma not_locked8 : ∃ t ∈ reach 8, t.1 = true := by
  decide

theorem lock9 (s : S5) (us : Fin 9 → Bool) : (run9 s us).1 = false ∧ (run9 s us).2.1 = true := by
  apply reach9_locked
  unfold run9
  exact mem_step _ (mem_step _ (mem_step _ (mem_step _ (mem_step _ (mem_step _ (mem_step _ (mem_step _
    (mem_step (n := 0) _ (mem_all s)))))))))

theorem lock_persists (s : S5) (u : Bool) (h1 : s.1 = false) (h2 : s.2.1 = true) :
    (blk s u).1 = false ∧ (blk s u).2.1 = true := by
  obtain ⟨x1, x2, x3, x4, x5⟩ := s
  simp only at h1 h2
  subst h1; subst h2
  simp [blk]

end BlackLock

#print axioms BlackLock.lock9
#print axioms BlackLock.lock_persists
#print axioms BlackLock.not_locked8
