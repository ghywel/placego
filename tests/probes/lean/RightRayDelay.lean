import Lean

/-!
# Delayed signals on the half-speed ray

The one-sided register reads a finite physical row from its rightmost black
cell towards the left. Its update is the Rule 30 truth table in that frame.
At tick t the observer reads bit floor(t/2), i.e. physical site ceil(t/2).
All statements below use the explicit update. The final theorem is parametric
only in how a recognizer represents a history and its allowed continuations.
-/

namespace RightRayDelay

abbrev Row := Nat → Bool

def driver (x : Row) : Nat → Bool
  | 0 => false
  | 1 => x 0
  | n + 2 => x (n + 1) || x n

def step (x : Row) (j : Nat) : Bool := xor (x j) (driver x j)

def run (x : Row) : Nat → Row
  | 0 => x
  | t + 1 => step (run x t)

def readRay (x : Row) (t : Nat) : Bool := run x t (t / 2)

def Seed (x : Row) : Prop := x 0 = true ∧ ∃ d, ∀ j, d < j → x j = false

def Below (x y : Row) (d : Nat) : Prop := ∀ j, j < d → x j = y j

theorem driver_eq {x y : Row} {j : Nat} (h : Below x y j) :
    driver x j = driver y j := by
  cases j with
  | zero => rfl
  | succ j =>
    cases j with
    | zero => exact h 0 (by omega)
    | succ j => simp only [driver, h j (by omega), h (j+1) (by omega)]

theorem below_step {x y : Row} {d : Nat} (h : Below x y d) : Below (step x) (step y) d := by
  intro j hj
  have hd := driver_eq (j := j) (fun k hk => h k (by omega))
  simp only [step, h j hj, hd]

theorem below_run {x y : Row} {d : Nat} (h : Below x y d) (t : Nat) :
    Below (run x t) (run y t) d := by
  induction t with
  | zero => exact h
  | succ t ih => exact below_step ih

theorem run_add (x : Row) (t k : Nat) : run x (t + k) = run (run x t) k := by
  induction k with
  | zero => rfl
  | succ k ih => exact congrArg step ih

theorem spot_iff {x y : Row} {j : Nat} (h : Below x y j) (t : Nat) :
    run x t j = run y t j ↔ x j = y j := by
  induction t with
  | zero => rfl
  | succ t ih =>
    have hd := driver_eq (below_run h t)
    change xor (run x t j) (driver (run x t) j) =
      xor (run y t j) (driver (run y t) j) ↔ _
    rw [hd, ← ih]
    cases run x t j <;> cases run y t j <;> cases driver (run y t) j <;> decide

theorem decode {x y : Row} {d : Nat}
    (h : ∀ t, t ≤ 2 * d → readRay x t = readRay y t) :
    Below x y (d + 1) := by
  intro j
  induction j using Nat.strongInductionOn with
  | h j ih =>
    intro hj
    apply (spot_iff (fun a ha => ih a ha (by omega)) (2*j)).mp
    have he := h (2*j) (by omega)
    simpa only [readRay, show 2*j/2 = j by omega] using he

theorem hold {x y : Row} {d : Nat}
    (h : ∀ t, t ≤ 2 * d → readRay x t = readRay y t) :
    readRay x (2*d+1) = readRay y (2*d+1) := by
  exact (below_run (decode h) (2*d+1)) ((2*d+1)/2) (by omega)

-- A prescribed finite window can be placed at any cut. Invert the
-- triangular register bit by bit, then truncate the preimage to that window.
def back (y : Row) : Nat → Bool
  | 0 => y 0
  | 1 => xor (y 1) (y 0)
  | n + 2 => xor (y (n + 2)) (back y (n + 1) || back y n)

private theorem xor_twice (a b : Bool) : xor (xor a b) b = a := by
  cases a <;> cases b <;> rfl

theorem step_back (y : Row) : step (back y) = y := by
  funext j
  cases j with
  | zero => change xor (y 0) false = y 0; cases y 0 <;> rfl
  | succ j =>
    cases j with
    | zero => exact xor_twice (y 1) (y 0)
    | succ j => exact xor_twice (y (j+2)) (back y (j+1) || back y j)

def undo (y : Row) : Nat → Row
  | 0 => y
  | t + 1 => undo (back y) t

theorem run_undo (y : Row) (t : Nat) : run (undo y t) t = y := by
  induction t generalizing y with
  | zero => rfl
  | succ t ih =>
    change step (run (undo (back y) t) t) = y
    rw [ih, step_back]

theorem undo_zero (y : Row) (t : Nat) : undo y t 0 = y 0 := by
  induction t generalizing y with
  | zero => rfl
  | succ t ih => exact ih (back y)

theorem place (y : Row) (h : y 0 = true) (t d : Nat) :
    ∃ x : Row, Seed x ∧ Below (run x t) y (d+1) := by
  let x : Row := fun j => if j ≤ d then undo y t j else false
  have hx : Below x (undo y t) (d+1) := by
    intro j hj
    simp [x, show j ≤ d by omega]
  refine ⟨x, ⟨by simp [x, undo_zero, h], d, ?_⟩, ?_⟩
  · intro j hj
    simp [x, Nat.not_le.mpr hj]
  · have hr := below_run hx t
    rwa [run_undo] at hr

def Top (x : Row) (b : Nat) : Prop := x b = true ∧ ∀ j, b < j → x j = false

theorem top_step {x : Row} {b : Nat} (h : Top x b) : Top (step x) (b+2) := by
  constructor
  · simp [step, driver, h.1, h.2 (b+1) (by omega), h.2 (b+2) (by omega)]
  · intro j hj
    obtain ⟨n, rfl⟩ : ∃ n, j = n+2 := ⟨j-2, by omega⟩
    simp [step, driver, h.2 n (by omega), h.2 (n+1) (by omega), h.2 (n+2) (by omega)]

theorem top_run {x : Row} {b : Nat} (h : Top x b) (r : Nat) : Top (run x r) (b+2*r) := by
  induction r with
  | zero => simpa using h
  | succ r ih =>
    rw [show b+2*(r+1) = (b+2*r)+2 by omega]
    exact top_step ih

def pulse (b j : Nat) : Bool := decide (j = 0 ∨ j = b)

theorem pulse_top (b : Nat) : Top (pulse b) b := by
  refine ⟨by simp [pulse], ?_⟩
  intro j hj
  simp [pulse, show j ≠ 0 by omega, show j ≠ b by omega]

theorem delayed (m i : Nat) (hi : i < m) :
    ∃ x : Row, Seed x ∧
      (∀ r, r ≤ 2*i → readRay x (6*m+r) = false) ∧
      readRay x (6*m+2*i+1) = true := by
  let b := 3*m-3*i-2
  let D := 3*m+i
  obtain ⟨x, hx, hp⟩ := place (pulse b) (by simp [pulse]) (6*m) D
  have hread : ∀ r, r ≤ 2*i+1 →
      readRay x (6*m+r) = run (pulse b) r ((6*m+r)/2) := by
    intro r hr
    unfold readRay
    rw [run_add]
    exact below_run hp r _ (by dsimp [D]; omega)
  refine ⟨x,hx,?_,?_⟩
  · intro r hr
    rw [hread r (by omega)]
    apply (top_run (pulse_top b) r).2
    dsimp [b]; omega
  · rw [show 6*m+2*i+1 = 6*m+(2*i+1) by omega, hread _ (by omega)]
    rw [show (6*m+(2*i+1))/2 = b+2*(2*i+1) by dsimp [b]; omega]
    exact (top_run (pulse_top b) _).1

theorem baseline (m : Nat) :
    ∃ x : Row, Seed x ∧ ∀ r, r < 2*m → readRay x (6*m+r) = false := by
  obtain ⟨x, hx, hp⟩ := place (pulse 0) (by simp [pulse]) (6*m) (4*m)
  refine ⟨x,hx,?_⟩
  intro r hr
  unfold readRay
  rw [run_add, below_run hp r ((6*m+r)/2) (by omega)]
  apply (top_run (pulse_top 0) r).2
  omega

/-- Whether k further white readings can follow x's history through T. -/
def Whites (x : Row) (T k : Nat) : Prop :=
  ∃ y : Row, Seed y ∧ (∀ t, t ≤ T → readRay y t = readRay x t) ∧
    ∀ r, 0 < r → r ≤ k → readRay y (T+r) = false

theorem reject {x : Row} {m i : Nat}
    (hz : ∀ r, r ≤ 2*i → readRay x (6*m+r) = false)
    (ho : readRay x (6*m+2*i+1) = true) :
    ¬ Whites x (6*m) (2*i+1) := by
  rintro ⟨y, _, he, hw⟩
  let d := 3*m+i
  have hall : ∀ t, t ≤ 2*d → readRay x t = readRay y t := by
    intro t ht
    by_cases h : t ≤ 6*m
    · exact (he t h).symm
    · let r := t-6*m
      have et : t = 6*m+r := by dsimp [r]; omega
      rw [et, hz r (by dsimp [r,d] at *; omega),
        hw r (by dsimp [r]; omega) (by dsimp [r,d] at *; omega)]
  have h := hold hall
  rw [show 2*d+1 = 6*m+2*i+1 by dsimp [d]; omega, ho] at h
  have hy := hw (2*i+1) (by omega) (by omega)
  rw [show 6*m+(2*i+1) = 6*m+2*i+1 by omega, ← h] at hy
  contradiction

theorem accept {x : Row} (hx : Seed x) {T k : Nat}
    (hw : ∀ r, 0 < r → r ≤ k → readRay x (T+r) = false) : Whites x T k :=
  ⟨x,hx,fun _ _ => rfl,hw⟩

/-- At the same age 6m, any state representation which decides allowed
white continuations for anchored finite seeds distinguishes m+1 histories. -/
theorem state_lower_bound (m : Nat) {S : Type} (encode : Row → S)
    (sound : ∀ x y, Seed x → Seed y → encode x = encode y →
      ∀ k, Whites x (6*m) k ↔ Whites y (6*m) k) :
    ∃ f : Fin (m+1) → S, Function.Injective f := by
  let P (i : Fin (m+1)) (x : Row) : Prop := Seed x ∧
    (∀ r, r ≤ 2*i.val → r < 2*m → readRay x (6*m+r) = false) ∧
    (i.val < m → readRay x (6*m+2*i.val+1) = true)
  have exists_row (i : Fin (m+1)) : ∃ x, P i x := by
    by_cases hi : i.val < m
    · obtain ⟨x,hx,hz,ho⟩ := delayed m i.val hi
      exact ⟨x,hx,fun r hr _ => hz r hr,fun _ => ho⟩
    · obtain ⟨x,hx,hz⟩ := baseline m
      exact ⟨x,hx,fun r _ hr => hz r hr,fun h => False.elim (hi h)⟩
  let seq (i : Fin (m+1)) : Row := Classical.choose (exists_row i)
  have hseq (i : Fin (m+1)) : P i (seq i) := Classical.choose_spec (exists_row i)
  have sep (i j : Fin (m+1)) (hij : i.val < j.val) : encode (seq i) ≠ encode (seq j) := by
    intro he
    have hj := j.isLt
    have hi : i.val < m := by omega
    have left := hseq i
    have right := hseq j
    have no := reject (fun r hr => left.2.1 r hr (by omega)) (left.2.2 hi)
    exact no ((sound _ _ left.1 right.1 he _).mpr
      (accept right.1 (fun r _ hr => right.2.1 r (by omega) (by omega))))
  refine ⟨fun i => encode (seq i), ?_⟩
  intro i j he
  apply Fin.ext
  by_cases hij : i.val < j.val
  · exact False.elim (sep i j hij he)
  · by_cases hji : j.val < i.val
    · exact False.elim (sep j i hji he.symm)
    · omega

end RightRayDelay
