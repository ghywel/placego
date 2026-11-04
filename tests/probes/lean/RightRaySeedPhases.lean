import RightRayDelay

/-!
# Half-speed ray memory using only phases of the single black cell

Launch the same half-speed observer at the moving right edge at an arbitrary
time s of the singleton evolution. Its initial register is exactly
`run (pulse 0) s`. In particular the family below requires no independently
chosen bits in the launch row. Follower words range only over singleton phases.
-/

namespace RightRayDelay.SeedPhases

open RightRayDelay

def phase (s : Nat) : Row := run (pulse 0) s

private theorem bool_return {a b c : Bool} (h : (a = b ↔ b = c)) : a = c := by
  cases a <;> cases b <;> cases c <;> simp_all

/-- A period on the lower bits lifts to a period or its double on the next
bit. This elementary existence version suffices to place a past phase. -/
theorem some_period (x : Row) (w : Nat) : ∃ p, 0 < p ∧ Below (run x p) x w := by
  induction w with
  | zero => exact ⟨1, by omega, fun j hj => False.elim (by omega)⟩
  | succ w ih =>
    obtain ⟨p,hp,h⟩ := ih
    have hlow : Below (run x (p+p)) (run x p) w := by
      rw [run_add]
      exact below_run h p
    have hbit : run x (p+p) w = x w := by
      rw [run_add]
      exact bool_return (spot_iff h p)
    refine ⟨p+p, by omega, ?_⟩
    intro j hj
    by_cases hlt : j < w
    · exact (hlow j hlt).trans (h j hlt)
    · have he : j = w := by omega
      simpa only [he] using hbit

theorem multiple {x : Row} {p w : Nat} (h : Below (run x p) x w) (k : Nat) :
    Below (run x (k*p)) x w := by
  induction k with
  | zero => simpa only [Nat.zero_mul] using (fun _ _ => rfl : Below x x w)
  | succ k ih =>
    rw [Nat.succ_mul, run_add]
    have h2 := below_run ih p
    exact fun j hj => (h2 j hj).trans (h j hj)

/-- At any common later age T, some singleton launch realizes any specified
early singleton phase r on w bits. -/
theorem place_early (T r w : Nat) : ∃ s, Below (run (phase s) T) (phase r) w := by
  obtain ⟨p,hp,h⟩ := some_period (pulse 0) w
  have hT : T ≤ T*p := by
    calc
      T = T*1 := by simp
      _ ≤ T*p := Nat.mul_le_mul_left T (by omega)
  refine ⟨T*p+r-T, ?_⟩
  unfold phase
  rw [← run_add, show T*p+r-T+T = T*p+r by omega, run_add]
  exact below_run (multiple h T) r

private theorem second {x : Row} {b : Nat} (h : Top x b) :
    step x (b+1) = true := by
  cases b with
  | zero => simp [step, driver, h.1, h.2 1 (by omega)]
  | succ n => simp [step, driver, h.1, h.2 (n+2) (by omega)]

theorem head_bit (r : Nat) : Top (phase r) (2*r) := by
  simpa only [phase,Nat.zero_add] using top_run (pulse_top 0) r

theorem second_bit (r : Nat) : phase (r+1) (2*r+1) = true := second (head_bit r)

private theorem phase_zero (t : Nat) : phase t 0 = true := by
  induction t with
  | zero => simp [phase,run,pulse]
  | succ t ih =>
    change xor (phase t 0) false = true
    rw [ih]; rfl

theorem phase_seed (t : Nat) : Seed (phase t) :=
  ⟨phase_zero t, 2*t, (head_bit t).2⟩

/-- The first white failure can be prescribed at hold 2i+1 after age 6m,
with a phase of the actual singleton as the starting row. -/
theorem delayed_phase (m i : Nat) (hi : i < m) :
    ∃ s, (∀ k, k ≤ 2*i → readRay (phase s) (6*m+k) = false) ∧
      readRay (phase s) (6*m+2*i+1) = true := by
  let r := (3*m-3*i-1)/2
  obtain ⟨s,hs⟩ := place_early (6*m) r (3*m+i+1)
  have read_eq (k : Nat) (hk : k ≤ 2*i+1) :
      readRay (phase s) (6*m+k) = phase (r+k) ((6*m+k)/2) := by
    unfold readRay
    rw [run_add]
    have e := below_run hs k ((6*m+k)/2) (by omega)
    simpa only [phase,run_add (pulse 0) r k] using e
  refine ⟨s,?_,?_⟩
  · intro k hk
    rw [read_eq k (by omega)]
    apply (head_bit (r+k)).2
    dsimp [r]; omega
  · let q := r+2*i
    rw [show 6*m+2*i+1 = 6*m+(2*i+1) by omega, read_eq _ (by omega)]
    have hD : (6*m+(2*i+1))/2 = 3*m+i := by omega
    have hq : r+(2*i+1) = q+1 := by dsimp [q]; omega
    rw [hD,hq]
    have hh : 3*m+i = 2*(q+1) ∨ 3*m+i = 2*q+1 := by dsimp [q,r]; omega
    rcases hh with h | h
    · rw [h]; exact (head_bit _).1
    · rw [h]; exact second_bit q

theorem baseline_phase (m : Nat) :
    ∃ s, ∀ k, k < 2*m → readRay (phase s) (6*m+k) = false := by
  obtain ⟨s,hs⟩ := place_early (6*m) 0 (4*m+1)
  refine ⟨s,?_⟩
  intro k hk
  unfold readRay
  rw [run_add, below_run hs k ((6*m+k)/2) (by omega)]
  exact (head_bit k).2 _ (by omega)

/-- All histories and all extensions are taken from phases of the singleton. -/
def PhaseWhites (s T k : Nat) : Prop :=
  ∃ q, (∀ t, t ≤ T → readRay (phase q) t = readRay (phase s) t) ∧
    ∀ r, 0 < r → r ≤ k → readRay (phase q) (T+r) = false

theorem unrestricted {s T k : Nat} (h : PhaseWhites s T k) : Whites (phase s) T k := by
  obtain ⟨q,hq,hr⟩ := h
  exact ⟨phase q,phase_seed q,hq,hr⟩

/-- Distinct follower sets persist when both the possible histories and
their continuations must be actual singleton launch phases. -/
theorem phase_state_lower_bound (m : Nat) {S : Type} (encode : Nat → S)
    (sound : ∀ s q, encode s = encode q →
      ∀ k, PhaseWhites s (6*m) k ↔ PhaseWhites q (6*m) k) :
    ∃ f : Fin (m+1) → S, Function.Injective f := by
  let P (i : Fin (m+1)) (s : Nat) : Prop :=
    (∀ r, r ≤ 2*i.val → r < 2*m → readRay (phase s) (6*m+r) = false) ∧
    (i.val < m → readRay (phase s) (6*m+2*i.val+1) = true)
  have hs (i : Fin (m+1)) : ∃ s, P i s := by
    by_cases hi : i.val < m
    · obtain ⟨s,hz,ho⟩ := delayed_phase m i.val hi
      exact ⟨s,fun r hr _ => hz r hr,fun _ => ho⟩
    · obtain ⟨s,hz⟩ := baseline_phase m
      exact ⟨s,fun r _ hr => hz r hr,fun h => False.elim (hi h)⟩
  let launch (i : Fin (m+1)) := Classical.choose (hs i)
  have good (i : Fin (m+1)) : P i (launch i) := Classical.choose_spec (hs i)
  have sep (i j : Fin (m+1)) (hij : i.val < j.val) : encode (launch i) ≠ encode (launch j) := by
    intro he
    have hj := j.isLt
    have hi : i.val < m := by omega
    have left := good i
    have right := good j
    have no := reject (fun r hr => left.1 r hr (by omega)) (left.2 hi)
    have yes : PhaseWhites (launch j) (6*m) (2*i.val+1) :=
      ⟨launch j,fun _ _ => rfl,fun r _ hr => right.1 r (by omega) (by omega)⟩
    exact no (unrestricted ((sound _ _ he _).mpr yes))
  refine ⟨fun i => encode (launch i), ?_⟩
  intro i j he
  apply Fin.ext
  by_cases hij : i.val < j.val
  · exact False.elim (sep i j hij he)
  · by_cases hji : j.val < i.val
    · exact False.elim (sep j i hji he.symm)
    · omega

end RightRayDelay.SeedPhases
